# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import  redirect, render
from django.urls import reverse_lazy

from django.views.generic import *

from baseapp.models.dashboard import Dashboard
from baseapp.models.notificacao import Notificacao


class NotificacaoView(LoginRequiredMixin,TemplateView):

    template_name = 'notificacao.html'
    model = Dashboard

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notificacao = Notificacao.objects.get(pk=self.kwargs['pk'])
        notificacao.desativado = True
        notificacao.save()
        context["notificacao"] = notificacao
        return context

    def get(self, request, *args, **kwargs):
        notificacao =  self.get_context_data()["notificacao"]
        # link = notificacao.link.replace("https://","").replace("http://","")
        return redirect(notificacao.link)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)