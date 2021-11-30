# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from baseapp.models.chamado import Chamado
from baseapp.variaveis import *
from django.utils.translation import ugettext_lazy as _

# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ChamadoFechar1View(PermissionRequiredMixin, DeleteView):
    permission_required = ADD_CHAMADO
    template_name = 'chamado/notificacao_list.html'
    model = Chamado
    success_message = _("Chamado Fechado com sucesso!")

    queryset = Chamado.objects.all()
    success_url = reverse_lazy('chamado-list')


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = True
        self.object.save()
        return  HttpResponseRedirect(self.success_url)


class ChamadoFecharView(View):

        def get(self,request,**kwargs):
            chamado= get_object_or_404(Chamado,pk=self.kwargs['pk'])
            chamado.status = True
            chamado.save()
            return HttpResponseRedirect(reverse_lazy('chamado-list'))
