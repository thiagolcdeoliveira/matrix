# coding=utf-8
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from base.settings import MEDIA_ROOT
from django.views.generic.edit import CreateView

from baseapp.forms.dashboard import DashboardForm
from baseapp.forms.grafico import GraficoForm
from baseapp.models.dashboard import Dashboard
from baseapp.models.grafico import Grafico


class DashboardCreateView(LoginRequiredMixin, CreateView):
    # permission_required = ADD_CHAMADO
    template_name = 'dashboard/dashboard_form.html'
    model = Dashboard
    form_class = DashboardForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.nome = self.request.user.username + "-" +  self.object.grafico.nome
        self.object.usuario_recebe = self.request.user

        self.object.save()
        return super(DashboardCreateView, self).form_valid(form)


    def form_invalid(self, form):
        '''
        :param self:
        :param form: erro no form
        :return: retorna o erro no cadastro
        '''
        print(form.errors)
        return super(DashboardCreateView, self).form_invalid(form)
