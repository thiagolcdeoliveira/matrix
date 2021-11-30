# -*- coding: utf-8 -*-
from django.forms import *

from baseapp.forms.validation.grafico import ValidationSQL
from baseapp.models.grafico import Grafico
from baseapp.models.propriedade import Propriedade


class PropriedadeAjaxForm(ModelForm):
    class Meta:
        model = Propriedade
        exclude = ('usuario', 'excluido', 'desativado')

class PropriedadeForm(ModelForm):
    class Meta:
        model = Propriedade
        exclude = ('usuario', 'excluido', 'desativado')

    def __init__(self, *args, **kwargs):
        super(PropriedadeForm,self).__init__(*args, **kwargs)
        self.fields['tipo_propriedade'].widget = Select(
            choices=self.fields['tipo_propriedade'].choices,
            attrs={'class': 'form-control',
                   })
        self.fields['endereco'].widget = Select(
            choices=self.fields['endereco'].choices,
            attrs={'class': 'form-control',
                   })




class PropriedadeAdminForm(ModelForm):
    class Meta:
        model = Grafico
        exclude = ('usuario', 'excluido', 'desativado')