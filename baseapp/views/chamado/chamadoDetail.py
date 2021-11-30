# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import *


from baseapp.forms.mensagem import MensagemForm
from baseapp.models.chamado import Chamado

from baseapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ChamadoDetailView( DetailView):
    # permission_required = ADD_CHAMADO

    template_name = 'chamado/chamado_detail.html'
    model = Chamado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MensagemForm()
        return context

class ChamadoUsuarioDetailView( DetailView):
    # permission_required = ADD_CHAMADO

    template_name = 'chamado/chamado_usuario_detail.html'
    model = Chamado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MensagemForm()
        return context