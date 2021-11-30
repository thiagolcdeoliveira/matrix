# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import *
from baseapp.forms.propriedade import PropriedadeForm
from baseapp.models.propriedade import Propriedade
from baseapp.variaveis import *


class PropriedadeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ADD_CHAMADO
    template_name = 'propriedade/propriedade_form.html'
    model = Propriedade
    form_class = PropriedadeForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(PropriedadeUpdateView, self).form_valid(form)