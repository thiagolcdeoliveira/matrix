# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse

from baseapp.models.grafico import Grafico
from baseapp.models.tamanho import Tamanho
from baseapp.models.tipo_grafico import TipoGrafico


class Dashboard(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    TIPO_CHOICES = (
        ("1", "Contador"),
        ("2", "Gráfico Area"),
        ("4", "Gráfico Barra"),
        ("4", "Gráfico Linha"),
        ("3", "Tabela")
    )
    nome = models.CharField(max_length=200, verbose_name="Nome do Dashboard",
                                help_text='Nome do Dashboard',blank=True)
    grafico = models.ForeignKey(Grafico, verbose_name="Grafico",on_delete=SET_NULL, null=True)
    tipo = models.ForeignKey(TipoGrafico,verbose_name="Tipo Grafico",on_delete=SET_NULL, null=True)
    ordem = models.PositiveIntegerField(null=True)
    tamanho = models.ForeignKey(Tamanho, verbose_name="Tamanho",on_delete=SET_NULL, null=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)
    usuario_recebe = models.ForeignKey(User,related_name="usuario_recebe_dashboard", verbose_name="Usuário Recebe",on_delete=SET_NULL, null=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome
    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('dashboard-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Dashboard'
        verbose_name_plural = 'Dashboards'
        permissions = (
            ("sgapapp_add_dashaboard", "Adicionar Dashboard"),
            ("sgapapp_detail_dashboard", "Visualizar Dashboard"),
            ("baseapp_delete_dashboard", "Excluir dashboard"),
        )
