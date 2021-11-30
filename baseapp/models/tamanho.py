# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class Tamanho(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome Tamanho",
                                help_text='Nome do tamanaho.')
    descricao = models.CharField(max_length=200, verbose_name="Descrição do Tamanho")
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome
    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('tamanho-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanho'
        permissions = (
            ("baseapp_add_tamanho", "Adicionar Tamanho"),
            ("baseapp_detail_tamanho", "Visualizar Tamanho"),
            ("baseapp_delete_tamanho", "Excluir tamanho"),

        )
