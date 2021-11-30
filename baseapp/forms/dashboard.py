# -*- coding: utf-8 -*-
from django.forms import *

from baseapp.forms.validation.grafico import ValidationSQL
from baseapp.models.dashboard import Dashboard
from baseapp.models.grafico import Grafico


class DashboardForm(ModelForm):
    class Meta:
        model = Dashboard
        exclude = ('usuario', 'usuario_recebe', 'excluido', 'desativado')

    # def clean_consulta(self):
    #     return ValidationSQL(self.cleaned_data.get("consulta"))

    # def __init__(self, *args, **kwargs):
    #     super(DashboardForm,self).__init__(*args, **kwargs)
    #
    #     self.fields['ordem'].widget = IntegerField(
    #         attrs={'class': 'form-control',
    #                })


class GraficoAdminForm(ModelForm):
    class Meta:
        model = Grafico
        exclude = ('usuario', 'excluido', 'desativado')