# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class TipoPropriedade(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome do Tipo de propriedade",
                                help_text='Nome do Tipo de Propriedade ')
    descricao = models.CharField(max_length=200, verbose_name="descricção do tipo de propriedade",
                            help_text='Descrição do Tipo de Propriedade')
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        return reverse('tipo-propriedade-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Tipo de Propriedade'
        verbose_name_plural = 'Tipos de Propriedades'
        permissions = (
            ("baseapp_add_tipo_propriedade", "Adicionar Tipo de propriedade"),
            ("baseapp_detail_tipo_propriedade", "Visualizar Tipo de propriedade"),
            ("baseapp_delete_tipo_propriedade", "Excluir tipo de propriedade"),


        )
