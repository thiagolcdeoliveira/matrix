# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class TipoGrafico(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome do Tipo do grafico",
                                help_text='Nome do Tipo de Grafico.')
    descricao = models.CharField(max_length=200, verbose_name="Descricao/codigo grafico",
                            help_text='Nome do Tipo de Grafico.')
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome
    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('tipo-grafico-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Tipo de grafico'
        verbose_name_plural = 'Tipos de Graficos'
        permissions = (
            ("baseapp_add_tipo_de_grafico", "Adicionar tipo de grafico"),
            ("baseapp_detail_tipo_de_grafico", "Visualizar tipo  de grafico"),
            ("baseapp_delete_tipo_De_grafico", "Excluir tipo de grafico"),

        )
