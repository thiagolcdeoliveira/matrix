# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse

from baseapp.models.tipo_grafico import TipoGrafico


class Grafico(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome do Grafico",
                                help_text='Nome do Grafico.')
    consulta = models.TextField(max_length=2000, verbose_name="Consulta do Grafico",
                                help_text='Consulta do Grafico.')
    tipo_grafico = models.ForeignKey(TipoGrafico, verbose_name="TipoDoGrafico",on_delete=SET_NULL, null=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome
    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('grafico-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'grafico'
        verbose_name_plural = 'graficos'
        permissions = (
            ("baseapp_add_grafico", "Adicionar Grafico"),
            ("baseapp_detail_grafico", "Visualizar Grafico"),
            ("baseapp_delete_grafico", "Excluir Grafico"),

        )
