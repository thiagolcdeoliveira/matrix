# coding=utf-8
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import *
from baseapp.forms.mensagem import MensagemForm
from baseapp.models.chamado import Chamado
from baseapp.models.mensagem import Mensagem






class MensagemCreateView( CreateView):
    template_name = 'includes/mensagem.html'
    model = Mensagem
    form_class = MensagemForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        self.chamado = get_object_or_404(Chamado,pk=self.kwargs.get('pk'))
        self.chamado.mensagem.add(self.object)
        self.chamado.save()
        return super(MensagemCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return reverse('chamado-detail',kwargs={"pk": self.kwargs.get('pk')})



    def get_success_url(self):
        return reverse('chamado-detail',kwargs={"pk": self.kwargs.get('pk')})
    def get_absolute_url(self):
        return reverse('chamado-detail',kwargs={"pk": self.kwargs.get('pk')})

