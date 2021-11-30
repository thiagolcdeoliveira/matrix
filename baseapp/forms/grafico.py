# -*- coding: utf-8 -*-
from django.forms import *

from baseapp.forms.validation.grafico import ValidationSQL
from baseapp.models.grafico import Grafico


class GraficoForm(ModelForm):
    class Meta:
        model = Grafico
        exclude = ('usuario', 'usuario_recebe', 'excluido', 'desativado')

    def clean_consulta(self):
        return ValidationSQL(self.cleaned_data.get("consulta"))

    def __init__(self, *args, **kwargs):
        super(GraficoForm,self).__init__(*args, **kwargs)
        self.fields['tipo_grafico'].widget = Select(
            choices=self.fields['tipo_grafico'].choices,
            attrs={'class': 'form-control',
                   })


class GraficoAdminForm(ModelForm):
    class Meta:
        model = Grafico
        exclude = ('usuario', 'excluido', 'desativado')