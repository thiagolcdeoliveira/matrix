# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class ConfiguracaoEmail(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Defina um nome para configuração.')
    :param html: models.ForeignKey(User, verbose_name="Usuário", help_text='Defina o Html para corpo do email.)
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome da Configuração",
                            help_text='Defina um nome para configuração')
    html = models.TextField(max_length=4000, verbose_name="HTML",
                            help_text='Defina o Html para corpo do email')
    usuario = models.ForeignKey(User, verbose_name="Usuário", on_delete=SET_NULL, null=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        return reverse('produto-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Configuracao de email'
        verbose_name_plural = 'Configuracoes de emails'
        permissions = (
            ("baseapp_add_config_email", "Adicionar Configuração de Email"),
            ("baseapp_detail_config_email", "Visualizar Configuração de Email"),
            ("baseapp_delete_config_email", "Excluir Configuração de Email"),
        )
