# -*- coding: utf-8 -*-
from django.forms import *

from baseapp.forms.validation.grafico import ValidationSQL
from baseapp.models.grafico import Grafico
from baseapp.models.tipo_propriedade import TipoPropriedade


class TipoPropriedadeAjaxForm(ModelForm):
    class Meta:
        model = TipoPropriedade
        exclude = ('usuario', 'excluido', 'desativado')


class TipoPropriedadeForm(ModelForm):
    class Meta:
        model = TipoPropriedade
        exclude = ('usuario', 'excluido', 'desativado')
