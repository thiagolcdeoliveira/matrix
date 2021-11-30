# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse
from baseapp.models.imagem import Imagem


class Mensagem(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    descricao = models.CharField(max_length=200, verbose_name="Descricao",
                             help_text='Adicione um imagem',blank=True,null=True)
    imagem = models.ManyToManyField(Imagem,blank=True)
    data = models.DateTimeField(auto_now=True,blank=True,null=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        return reverse('produto-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
        permissions = (
            ("baseapp_add_mensagem", "Adicionar mensagem"),
            ("baseapp_detail_mensagem", "Visualizar mensagem"),
            ("baseapp_delete_mensagem", "Excluir mensagem"),

        )
