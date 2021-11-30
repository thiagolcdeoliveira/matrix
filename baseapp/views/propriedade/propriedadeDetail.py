# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import *


from baseapp.forms.mensagem import MensagemForm
from baseapp.models.grafico import Grafico
from baseapp.models.propriedade import Propriedade

from baseapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class PropriedadeDetailView( DetailView):
    # permission_required = ADD_CHAMADO

    template_name = 'propriedade/propriedade_detail.html'
    model = Propriedade

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

