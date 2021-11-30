# -*- coding: utf-8 -*-
from datetime import date

from django.forms import *

from baseapp.models.endereco import Endereco
from baseapp.models.setor import Setor


class EnderecoAjaxForm(ModelForm):

    class Meta:
        model = Endereco
        exclude = ('usuario', 'excluido', 'desativado')