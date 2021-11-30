# -*- coding: utf-8 -*-
from django.forms import *
from baseapp.models.mensagem import Mensagem


class MensagemForm(ModelForm):
    descricao = CharField(required=True,
        widget=Textarea(
                         attrs={'class': 'ui date',

                                 }))
    class Meta:
        model = Mensagem
        exclude = ('usuario', 'excluido', 'desativado')
