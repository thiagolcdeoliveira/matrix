# coding=utf-8
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from storeapp.forms.chamado import ChamadoForm, ChamadoUpdateForm
from storeapp.models.chamado import Chamado
from storeapp.models.produto import Produto
from storeapp.forms.produto import ProdutoForm
from storeapp.variaveis import *

from django.utils.translation import ugettext_lazy as _
# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ChamadoDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ADD_CHAMADO
   # template_name = 'chamado/notificacao_list.html'
   # model = Chamado
    # form_class = ChamadoUpdateForm

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.uuario = self.request.user
    #     self.object.save()
    #     return super(ChamadoCreateView, self).form_valid(form)
    success_message = _("Chamado deletado com sucesso!")

    queryset = Chamado.objects.all()
    success_url = reverse_lazy('chamado-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.desativado = True
        self.object.save()
        messages.success(self.request, self.success_message)

        return super(ChamadoDeleteView, self).form_valid(form)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)