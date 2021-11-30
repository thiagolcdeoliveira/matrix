# -*- coding: utf-8 -*-
from datetime import date

from django.forms import *
from baseapp.models.setor import Setor


class SetorAjaxForm(ModelForm):

    class Meta:
        model = Setor
        exclude = ('usuario', 'excluido', 'desativado')