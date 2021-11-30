# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse

# from baseapp.models.endereco import Endereco
from baseapp.models.endereco import Endereco
from baseapp.models.tipo_propriedade import TipoPropriedade


class Propriedade(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome da Propriedade",
                                help_text='Nome da Propriedade', blank=True)
    tipo_propriedade = models.ForeignKey(TipoPropriedade, verbose_name="Tipo de Propriedade",on_delete=SET_NULL, null=True)
    numero_patrimonio = models.CharField(max_length=200, verbose_name="Cód da Propriedade",
                                help_text='Cód da Propriedade', blank=True)
    endereco = models.ForeignKey(Endereco,related_name="endereco_propriedade", verbose_name="Endereço da Propriedade",
                                         help_text='Endereço da Propriedade', blank=True,on_delete=SET_NULL,null=True)
    descricao = models.TextField(max_length=200,  verbose_name="Descrição", blank=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome
    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('propriedade-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'propriedade'
        verbose_name_plural = 'propriedades'
        permissions = (
            ("baseaap_add_propriedade", "Adicionar Propriedade"),
            ("baseaap_detail_propriedade", "Visualizar Propriedade"),
            ("baseapp_delete_propriedade", "Excluir Propriedade"),

        )
