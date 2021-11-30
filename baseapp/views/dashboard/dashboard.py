# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import  redirect, render
from django.urls import reverse_lazy

from django.views.generic import *

from baseapp.models.dashboard import Dashboard


class DashboardView(LoginRequiredMixin,TemplateView):

    template_name = 'dashboard.html'
    model = Dashboard

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dashboard = Dashboard.objects.filter(usuario_recebe=self.request.user, excluido=False, desativado=False ).order_by("ordem")
        context['dashboard'] = dashboard
        print(dashboard)
        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        else:
            if not self.request.user.groups.filter(name = 'Administrador').exists():
                return redirect(reverse_lazy('chamado-meu-list'))
        return render(request,self.template_name,self.get_context_data())

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)