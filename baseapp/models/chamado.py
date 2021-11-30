# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_DEFAULT, SET_NULL
from django.urls import reverse

from baseapp.models import Produto
from baseapp.models.equipamento import Equipamento
from baseapp.models.imagem import Imagem
from baseapp.models.mensagem import Mensagem
from baseapp.models.prioridade import Prioridade
from baseapp.models.propriedade import Propriedade
from baseapp.models.setor import Setor
from baseapp.models.situacao import Situacao
from baseapp.models.tipo_chamado import TipoChamado


class Chamado(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    cod = models.CharField(max_length=200, verbose_name="Codigo do Chamado",blank=True)
    nome = models.CharField(max_length=200, verbose_name="nome")
    descricao = models.TextField(max_length=1200, verbose_name="Descriçao",
                                help_text='Descriçao do chamado.')
    tipo_chamado = models.ForeignKey(TipoChamado, verbose_name="Tipo Chamado",on_delete=SET_NULL, null=True)
    prioridade = models.ForeignKey(Prioridade, verbose_name="Prioridade",on_delete=SET_NULL, null=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)
    mensagem = models.ManyToManyField(Mensagem, verbose_name="mensagem",blank=True)
    solicitante = models.ForeignKey(User, verbose_name="Solicitante",on_delete=SET_NULL, null=True,
                                    help_text='Solicitante que está solicitando o chamado.',
                                   related_name='servidor_usuario', blank=True )
    responsavel = models.ForeignKey(User, verbose_name="Responsavel",
                                    help_text='Servidor responsavel data TI pelo chamado .',
                                    related_name='responsavel_usuario', on_delete=SET_NULL, null=True)
    colaborador = models.ManyToManyField(User, verbose_name="",
                                    help_text='Colaborador .',
                                    related_name='colaborador_usuario',blank=True)

    setor = models.ForeignKey(Setor, verbose_name="Setor",
                                    help_text='Setor .',
                                    on_delete=SET_NULL, null=True)

    equipamento_utilizado = models.ManyToManyField(Equipamento, blank=True)
    produto_utilizado = models.ManyToManyField(Produto,related_name='chamado_produto_utlizado',blank=True)
    propriedade = models.ForeignKey(Propriedade,related_name='chamado_propriedade',blank=True,on_delete=SET_NULL,null=True)
    imagem = models.ManyToManyField(Imagem, blank=True)
    data_inicio = models.DateTimeField(auto_now_add=True, null=True)
    data_inicio_atendimento = models.DateTimeField(blank=True,null=True)
    data_fim = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    situacao = models.ForeignKey(Situacao,on_delete=SET_NULL, null=True,blank=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.cod

    def __str__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        return reverse('chamado-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "baseapp"
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'
        permissions = (
            ("baseapp_add_chamado", "Adicionar Chamado"),
            ("baseapp_detail_chamado", "Visualizar Chamado"),
            ("baseapp_delete_chamado", "Excluir Chamado"),
            ("baseapp_list_chamado", "Listar Chamado"),
        )
