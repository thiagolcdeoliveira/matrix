# coding=utf-8
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from base.settings import MEDIA_ROOT
from django.views.generic.edit import CreateView

from baseapp.forms.grafico import GraficoForm
from baseapp.models.grafico import Grafico


class GraficoCreateView(LoginRequiredMixin, CreateView):
    # permission_required = ADD_CHAMADO
    template_name = 'grafico/grafico_form.html'
    model = Grafico
    form_class = GraficoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.usuario_recebe = self.request.user

        self.object.save()
        return super(GraficoCreateView, self).form_valid(form)


    def form_invalid(self, form):
        '''
        :param self:
        :param form: erro no form
        :return: retorna o erro no cadastro
        '''
        print(form.errors)
        return super(GraficoCreateView, self).form_invalid(form)


class GraficoAdminCreateView(LoginRequiredMixin, CreateView):
    # permission_required = ADD_CHAMADO
    template_name = 'grafico/grafico_form.html'
    model = Grafico
    form_class = GraficoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user

        self.object.save()

        return super(GraficoAdminCreateView, self).form_valid(form)

    def form_invalid(self, form):
        '''

        :param self:
        :param form: erro no form
        :return: retorna o erro no cadastro
        '''
        print(form.errors)

        return super(GraficoAdminCreateView, self).form_invalid(form)

