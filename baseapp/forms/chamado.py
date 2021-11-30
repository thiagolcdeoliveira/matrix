# -*- coding: utf-8 -*-
from datetime import date

from django.contrib.auth.models import User
from django.forms import *

from baseapp.models.chamado import Chamado
from baseapp.models.setor import Setor
from baseapp.models.tipo_chamado import TipoChamado


class ChamadoForm(ModelForm):
    responsavel = ModelChoiceField(queryset=User.objects.filter(groups=1),required=False)
    setor = ModelChoiceField(queryset=Setor.objects.filter(desativado=False,excluido=False).order_by('nome'),
                             )
    colaborador = ModelMultipleChoiceField(queryset=User.objects.filter(is_superuser=True),required=False)
    tipo_chamado = ModelChoiceField(queryset=TipoChamado.objects.filter(desativado=False,excluido=False).order_by('nome'))
    solicitante = ModelChoiceField(queryset=User.objects.filter().order_by('username'))

    class Meta:
        model = Chamado
        exclude = ('usuario', 'excluido','cod','imagem','data_inicio','data_fim','status', 'desativado')

    def __init__(self, *args, **kwargs):
        super(ChamadoForm,self).__init__(*args, **kwargs)
        self.fields['propriedade'].widget = Select(
            choices=self.fields['propriedade'].choices,
            attrs={'class': 'form-control',
                   })
        self.fields['produto_utilizado'].widget = CheckboxSelectMultiple(
                            choices=self.fields['produto_utilizado'].choices,
                             attrs={'class': 'multiselect dropdown-toggle btn btn-default',
                                    })
        # self.fields['equipamento_utilizado'].widget = SelectMultiple(
        #     choices=self.fields['equipamento_utilizado'].choices,
        #     attrs={'class': 'ui fluid  multiple search normal selection dropdown',
        #            })
        self.fields['setor'].widget = Select(
            choices=self.fields['setor'].choices,
            attrs={'class': 'form-control  small',
                   })
        self.fields['tipo_chamado'].widget = Select(
            choices=self.fields['tipo_chamado'].choices,

            attrs={'class': 'ui fluid   search normal selection dropdown',
                   })
        self.fields['responsavel'].widget = Select(
            choices=self.fields['responsavel'].choices,

            attrs={'class': 'form-control',
                   })
        self.fields['solicitante'].widget = Select(
            choices=self.fields['solicitante'].choices,

            attrs={'class': 'form-control  small',
                   })
        self.fields['situacao'].widget = Select(
            choices=self.fields['situacao'].choices,

            attrs={'class': 'ui fluid   search normal selection dropdown',
                   })
        self.fields['colaborador'].widget = SelectMultiple(
            choices=self.fields['colaborador'].choices,
            # choices=User.objects.filter(is_superuser=True).values_list('id', 'username'),
            attrs={'class': 'ui fluid  multiple search normal selection dropdown',
                   })


class ChamadoUsuarioForm(ModelForm):
    setor = ModelChoiceField(queryset=Setor.objects.filter(desativado=False, excluido=False).order_by('nome'))
    tipo_chamado = ModelChoiceField(
        queryset=TipoChamado.objects.filter(desativado=False, excluido=False).order_by('nome'))

    class Meta:
        model = Chamado
        exclude = ('usuario','responsavel','excluido','cod','imagem','data_inicio','data_fim','status','produto_utilizado','produto_utilizado','servidor', 'desativado','data_inicio_atendimento')
        fields = ( 'nome', 'tipo_chamado', 'setor','descricao','prioridade' )



class ChamadoUpdateForm(ModelForm):
    setor = ModelChoiceField(queryset=Setor.objects.filter(desativado=False, excluido=False).order_by('nome'))
    tipo_chamado = ModelChoiceField(
        queryset=TipoChamado.objects.filter(desativado=False, excluido=False).order_by('nome'))
    solicitante = ModelChoiceField(queryset=User.objects.filter().order_by('username'))

    class Meta:
        model = Chamado
        exclude = ('usuario', 'excluido','cod', 'imagem','data_inico','data_fim','desativado')

class ChamadoAdminUpdateForm(ModelForm):
    setor = ModelChoiceField(queryset=Setor.objects.filter(desativado=False, excluido=False).order_by('nome'))
    tipo_chamado = ModelChoiceField(queryset=TipoChamado.objects.filter(desativado=False, excluido=False).order_by('nome'))
    solicitante = ModelChoiceField(queryset=User.objects.filter().order_by('username'))

    responsavel = ModelChoiceField(queryset=User.objects.filter(groups=1))
    colaborador = ModelMultipleChoiceField(queryset=User.objects.filter(is_superuser=True),required=False)

    class Meta:
            model = Chamado
            exclude = ('usuario', 'colaborador','excluido','cod', 'imagem','data_inico','data_fim','desativado','mensagem','data_inicio_atendimento')

    def __init__(self, *args, **kwargs):
        super(ChamadoAdminUpdateForm,self).__init__(*args, **kwargs)
        self.fields['propriedade'].widget = Select(
            choices=self.fields['propriedade'].choices,
            attrs={'class': 'form-control ',
                   })
        self.fields['produto_utilizado'].widget = CheckboxSelectMultiple(
                            # choices=self.fields['produto_utilizado'].choices,
                            choices={},
                             attrs={'class': ' hidden',
                                    })
        self.fields['equipamento_utilizado'].widget = CheckboxSelectMultiple(
            # choices=self.fields['equipamento_utilizado'].choices,
            choices={},
            attrs={'class': ' hidden',
                   })
        self.fields['setor'].widget = Select(
            choices=self.fields['setor'].choices,
            attrs={'class': 'form-control  small',
                   })
        self.fields['tipo_chamado'].widget = Select(
            choices=self.fields['tipo_chamado'].choices,

            attrs={'class': 'ui fluid   search normal selection dropdown',
                   })
        self.fields['responsavel'].widget = Select(
            choices=self.fields['responsavel'].choices,

            attrs={'class': 'ui fluid   search normal selection dropdown',
                   })
        self.fields['solicitante'].widget = Select(
            choices=self.fields['solicitante'].choices,

            attrs={'class': 'form-control  small',
                   })
        self.fields['situacao'].widget = Select(
            choices=self.fields['situacao'].choices,

            attrs={'class': 'ui fluid   search normal selection dropdown',
                   })
        self.fields['colaborador'].widget = SelectMultiple(
                choices=self.fields['colaborador'].choices,
                attrs={'class': 'ui fluid  multiple search normal selection dropdown',
                       })
