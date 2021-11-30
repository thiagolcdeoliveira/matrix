# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import  redirect, render
from django.urls import reverse_lazy

from django.views.generic import *

from appusuario.variaveis import ADD_CHAMADO
from baseapp.forms.chamado import ChamadoForm
from baseapp.forms.grafico import GraficoForm
from baseapp.models import Chamado
from baseapp.models.dashboard import Dashboard
from baseapp.models.grafico import Grafico


class GraficoListView(PermissionRequiredMixin, ListView):
    template_name = 'grafico/grafico_list.html'
    model = Grafico
    queryset = Grafico
    paginate_by = 10
    form_class = GraficoForm
    select = {'todos': '0', 'solicitante': '3', 'responsavel': '4',
              'descricao': '5','nome': '1'
              }

    def get_queryset(self):

         form = self.request.GET
         self.queryset = Grafico.objects.all()
         descricao = form.get('descricao')
         query = get_queryset_filter(self,form,descricao)
         return query.order_by('-id').reverse()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = self.select
        context['form'] = self.form_class
        return context


def get_queryset_filter(self,form,descricao):

     if form.get('tipo'):

         if form.get('tipo') == self.select.get("descricao"):
            self.queryset = self.queryset.filter(grafico__consulta__icontains=descricao)
         elif form.get('tipo') == self.select.get("codigo"):
             if descricao.isdigit():
                self.queryset = self.queryset.filter(pk=form.get('descricao'))
         elif form.get('tipo') == self.select.get("responsavel"):
             self.queryset = self.queryset.filter(Q(usuario_recebe__username__icontains=descricao) |
                                                  Q(usuario_recebe__first_name__icontains=descricao) | Q(
                usuario_recebe__last_name__icontains=descricao))
         elif form.get('tipo') == self.select.get("nome"):
             self.queryset = self.queryset.filter(nome__icontains=descricao)
         elif form.get('tipo') == '0':
             if descricao.isdigit():
                 self.queryset = self.queryset.filter(
                     Q(consulta__icontains=descricao) | Q(usuario_recebe__username__icontains=descricao)
                     | Q(pk=descricao) | Q(usuario_recebe__icontains=descricao) |
                       Q(usuario_recebe__first_name__icontains=descricao)
                     | Q(usuario_recebe__last_name__icontains=descricao)
                 )
             else:
                 self.queryset = self.queryset.filter(
                     Q(grafico__consulta__icontains=descricao)
                     |Q(nome__icontains=descricao) | Q(usuario_recebe__username__icontains=descricao)|
                     Q(usuario_recebe__first_name__icontains=descricao)   | Q(usuario_recebe__last_name__icontains=descricao)
                 )
     print(form.get('status'))
     if form.get('status')=='1':
         self.queryset = self.queryset.filter(desativado=False)
     elif form.get('status')=='2':
         self.queryset = self.queryset.filter(desativado=True)

     return self.queryset.filter(excluido=False).order_by('-desativado','id').reverse()


class DashboardMeuListView(ListView):
    # permission_required = ADD_CHAMADO
    template_name = 'dashboard/dashboard_meu_list.html'
    model = Dashboard
    queryset = Dashboard
    paginate_by = 10
    select = {'todos': '0', 'codigo': '1', 'nome': '2', 'consulta': '4',
              }

    def get_queryset(self):

         form = self.request.GET
         self.queryset = Dashboard.objects.filter(usuario_recebe=self.request.user)
         descricao = form.get('descricao')
         query = get_queryset_filter(self,form,descricao)
         return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = self.select
        return context