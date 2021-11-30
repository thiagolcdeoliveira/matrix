# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse
from baseapp.models.bairro import Bairro


class Endereco(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome do Endereço",
                                help_text='Nome do endereço ')
    rua = models.CharField(max_length=200, verbose_name="Nome da Rua",
                            help_text='Nome da Rua ')
    bairro = models.ForeignKey(Bairro, verbose_name="Bairro",
                           help_text='Bairro', on_delete=SET_NULL, blank=True,null=True)
    coordenadas = models.CharField(max_length=200, verbose_name="Coordenadas",
                            help_text='Nome do Coordenadas ', blank=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        return reverse('endereco-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'
        permissions = (
            ("baseapp_add_endereco", "Adicionar Endereço"),
            ("baseapp_detail_endereco", "Visualizar Endereço"),
            ("baseapp_delete_endereco", "Excluir Endereço"),
        )
