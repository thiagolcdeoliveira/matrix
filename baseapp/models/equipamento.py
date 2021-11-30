# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class Equipamento(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome do Equipamento",
                                help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).')
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome
    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('equipamento-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        permissions = (
            ("baseapp_add_equipamento", "Adicionar Equipamento"),
            ("baseapp_detail_equipamento", "Visualizar Equipamento"),
            ("baseapp_delete_equipamento", "Excluir Equipamento"),
        )
