# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class Settings(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome da Configuração",
                                help_text='Nome da Configuração')
    logo = models.ImageField(verbose_name="Logo",
                            help_text='Logo Principal',blank=True,null=True,upload_to="imagem/settings")
    logo_baixa = models.ImageField(verbose_name="Logo Baixa Resolução",
                             help_text='Logo Baixa Resolução', blank=True, null=True, upload_to="imagem/settings")
    imagem_login = models.ImageField(verbose_name="Imagem Login",
                                  help_text='Imagem Login', blank=True, null=True, upload_to="imagem/settings")
    imagem_cadastro = models.ImageField(verbose_name="Imagem Cadastro",
                                     help_text='Imagem Cadastro', blank=True, null=True,
                                     upload_to="imagem/settings")
    cor = models.CharField(max_length=200, verbose_name="Cor de Menu",
                                help_text='Cor do Menu', blank=True)
    numero = models.BooleanField(verbose_name="Numero para Virada",
                           help_text='Numero para Virada')
    usuario_recebe = models.ForeignKey(User, related_name="usuario_recebe_settings", verbose_name="Usuário Recebe",on_delete=SET_NULL, null=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'
        permissions = (
            ("baseapp_add_settings", "Adicionar settings"),
            ("baseapp_detail_settings", "Visualizar settings"),
            ("baseapp_delete_settings", "Excluir settings"),

        )
