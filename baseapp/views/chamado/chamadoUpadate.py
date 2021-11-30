# coding=utf-8
from datetime import date, datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *

from baseapp.forms.chamado import ChamadoForm, ChamadoUpdateForm, ChamadoAdminUpdateForm
from baseapp.models.chamado import Chamado
from baseapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ChamadoUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ADD_CHAMADO
    template_name = 'chamado/chamado_form.html'
    model = Chamado
    form_class = ChamadoUpdateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(ChamadoUpdateView, self).form_valid(form)

class ChamadoAdminUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ADD_CHAMADO
    template_name = 'chamado/chamado_admin_form.html'
    model = Chamado
    form_class = ChamadoAdminUpdateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(ChamadoAdminUpdateView, self).form_valid(form)
    def form_invalid(self, form):
        print(form.errors)
        return super(ChamadoAdminUpdateView, self).form_invalid(form)


class ChamadoIniciarUpdateView(PermissionRequiredMixin,View):
    permission_required = ADD_CHAMADO
    template_name = 'chamado/chamado_detail.html'
    model = Chamado
    form_class = ChamadoAdminUpdateForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     self.object = get_object_or_404(Chamado,pk= self.kwargs.get('pk'))
    #     self.object.data_inicio_antendimento = datetime.now()
    #     self.object.save()
    #     return context
    def get(self, request, **kwargs):
        # context = super().get_context_data(**kwargs)

        chamado = get_object_or_404(Chamado,pk= self.kwargs.get('pk'))
        data_atual  = datetime.now()
        # data_em_texto = data_atual.strftime('%d/%m/%Y %H:%M:%s' )
        chamado.data_inicio_antendimento = data_atual
        # chamado.data_inicio = data_em_texto
        if chamado.responsavel:
            chamado.responsavel = request.user
        chamado.save(force_update=True)
        # object.update(data_inicio_antendimento=datetime.now())
        # object.save()
      # ": self.kwargs.get('pk')})
      #   return  redirect(reverse_lazy('chamado-detail',kwargs={"pk": self.kwargs.get('pk')}))

        return HttpResponseRedirect(reverse_lazy('chamado-list'))

    # class ChamadoFecharView(View):
    #
    #     def get(self, request, **kwargs):
    #         chamado = get_object_or_404(Chamado, pk=self.kwargs['pk'])
    #         chamado.status = True
    #         chamado.save()
    #         return HttpResponseRedirect(reverse_lazy('chamado-list'))
    # # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.data_inicio_antendimento = datetime.date.now()
    #     self.object.save()
    #     return super(ChamadoIniciarUpdateView, self).form_valid(form)
    #
    # def get_success_url(self):
    #     return  reverse_lazy('chamado-detail',kwargs={"pk": self.kwargs.get('pk')})

    # def get(self, request, *args, **kwargs):
    #
    #     return  reverse_lazy('chamado-detail',kwargs={"pk": self.kwargs.get('pk')})

