# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class TipoNotificacao(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome do Tipo de Notificação",
                                help_text='Nome do Tipo de Notificação')
    descricao = models.CharField(max_length=200, verbose_name="Descrição do Conteudo da Notificação",
                                 help_text='Descrição do Conteudo da Notificação')
    link = models.CharField(max_length=200, verbose_name="Link",
                            help_text='Link da Notificação',blank=True)
    icon = models.CharField(max_length=200, verbose_name="icon",
                            help_text='Icone da Notificação')
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome
    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('tipo-notificacao-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Tipo Notificacao'
        verbose_name_plural = 'Tipos de notificacao'
        permissions = (
            ("baseapp_add_tipo_notificacao", "Adicionar tipo notificacao"),
            ("baseapp_detail_tipo_notificacao", "Visualizar tipo notificacao"),
            ("baseapp_delete_tipo_notificacao", "Excluir tipo notificacao"),

        )
