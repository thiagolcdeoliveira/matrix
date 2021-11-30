# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import *


from baseapp.forms.mensagem import MensagemForm
from baseapp.models.dashboard import Dashboard
from baseapp.models.grafico import Grafico

from baseapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class DashboardDetailView( DetailView):
    # permission_required = ADD_CHAMADO

    template_name = 'dashboard/dashboard_detail.html'
    model = Dashboard

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MensagemForm()
        return context

class ChamadoUsuarioDetailView( DetailView):
    # permission_required = ADD_CHAMADO

    template_name = 'chamado/chamado_usuario_detail.html'
    model = Grafico

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MensagemForm()
        return context