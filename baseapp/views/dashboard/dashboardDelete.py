# coding=utf-8
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import *

from baseapp.models.dashboard import Dashboard
from baseapp.variaveis import DELETE_DASHBOARD


class DashboardDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = DELETE_DASHBOARD
    model = Dashboard
    success_url = reverse_lazy('dashboard-meu-listar')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.usuario = self.request.user
        self.object.excluido = True
        self.object.desativado = True
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

class DashboardDesativeView(PermissionRequiredMixin, DeleteView):
    permission_required = DELETE_DASHBOARD
    model = Dashboard
    success_url = reverse_lazy('dashboard-meu-listar')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.usuario = self.request.user
        self.object.desativado = True
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

class DashboardActiveView(PermissionRequiredMixin, DeleteView):
    permission_required = DELETE_DASHBOARD
    model = Dashboard
    success_url = reverse_lazy('dashboard-meu-listar')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.usuario = self.request.user
        self.object.excluido = False
        self.object.desativado = False
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)