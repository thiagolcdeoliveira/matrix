# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse

from baseapp.models.tipo_notificacao import TipoNotificacao


class Notificacao(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome da Notificação",
                                help_text='Nome da Notificação', blank=True)
    link = models.CharField(max_length=200, verbose_name="Link",
                            help_text='Link da Notificação', blank=True)
    destino = models.CharField(max_length=200, verbose_name="Destino",
                            help_text='Destino da Notificação',  blank=True)
    prioridade = models.CharField(max_length=200, verbose_name="Prioridade",
                            help_text='prioridade da Notificação', blank=True)
    data = models.DateField(auto_now=True , verbose_name="Data",
                                  help_text='Data da Notificação', blank=True)
    tipo_notificacao = models.ForeignKey(TipoNotificacao, verbose_name="Tipo a Notificar", on_delete=SET_NULL, null=True)

    usuario_recebe = models.ForeignKey(User,related_name="usuario_recebe", verbose_name="Usuário a Notificar", on_delete=SET_NULL, null=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome
    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('notificao-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
        permissions = (
            ("baseapp_add_notificacao", "Adicionar Notificação"),
            ("baseapp_detail_notificacao", "Visualizar Notificação"),
            ("baseapp_delete_notificaao", "Excluir Notificação"),

        )
