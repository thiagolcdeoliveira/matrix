# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_DEFAULT, SET_NULL
from django.urls import reverse


class Imagem(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    imagem = models.ImageField(blank=True,null=True,upload_to="imagem/mensagem")
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.usuario

    def get_absolute_url(self):
        return reverse('produto-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        permissions = (
            ("baseapp_add_imagem", "Adicionar imagem"),
            ("baseapp_detail_imagens", "Visualizar imagem"),
            ("baseapp_delete_imagem", "Excluir imagem"),

        )
