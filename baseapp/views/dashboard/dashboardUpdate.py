# coding=utf-8
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from base.settings import MEDIA_ROOT
from django.views.generic.edit import CreateView, UpdateView

from baseapp.forms.dashboard import DashboardForm
from baseapp.forms.grafico import GraficoForm
from baseapp.models.dashboard import Dashboard
from baseapp.models.grafico import Grafico


class DashboardUpdateView(LoginRequiredMixin, UpdateView):
    # permission_required = ADD_CHAMADO
    template_name = 'dashboard/dashboard_form.html'
    # permission_required = DETAIL_USER
    model = Dashboard
    form_class = DashboardForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.nome = self.request.user.username + "-" +  self.object.grafico.nome
        self.object.save()
        return super(DashboardUpdateView, self).form_valid(form)


    def form_invalid(self, form):
        '''
        :param self:
        :param form: erro no form
        :return: retorna o erro no cadastro
        '''
        print(form.errors)
        return super(DashboardUpdateView, self).form_invalid(form)
