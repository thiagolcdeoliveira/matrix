# -*- coding: utf-8 -*-
# from django.core.urlresolvers import reverse
# from appusuario.models.instituicao import Instituicao
# from appusuario.models.email import Email
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse

from baseapp.models import Setor
from baseapp.models.propriedade import Propriedade


class ComplementoUsuario(models.Model):
    '''
    :param user_id: models.ForeignKey(User, related_name="user", verbose_name="ID do Usuário (Auth User)", help_text='Deve conter o usuário.')
    :param lista_email: models.ManyToManyField(Email, verbose_name="E-mails", help_text='Deve conter os e-mails relacionados ao usuário.')
    :param instituicao: models.ManyToManyField(Instituicao, verbose_name="Instituição", help_text='Deve conter as Instuições, Universidades ou Organizações.')
    :param nome: models.CharField(max_length=500)
    '''
    user = models.OneToOneField(User, related_name='user_user', verbose_name='ID do Usuário (Auth User)',
                                   help_text='Deve conter o usuário.',on_delete=SET_NULL, null=True)
    imagem = models.ImageField(upload_to='usuario/imagem', null=True, blank=True)
    setor = models.ForeignKey(Setor,related_name="usuario_setor", verbose_name="Setor", on_delete=SET_NULL, null=True)
    telefone = models.CharField(max_length=15,  verbose_name='Telefone',
                                   help_text='Telefone de Contato.', null=True,blank=True )
    propriedade = models.ManyToManyField(Propriedade,related_name='ususario_propriedade',blank=True)

    obs = models.TextField(max_length=200,  verbose_name='Observação',
                                help_text='Telefone de Contato.',  null=True, blank=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('complento-usuario-detail', kwargs={'pk': self.pk})
    def __unicode__(self):
        return u'%s' % self.user
    def __str__(self):
        return u'%s' % self.user
    class Meta:
        app_label = 'appusuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        permissions = (
            ("baseapp_add_complemento_usuario", "Adicionar Complemento Usuario"),
            ("baseapp_detail_complemento_usuario", "Visualizar Complemento Usuario"),
            ("baseapp_delete_complemento_usuario", "Excluir Complemento Usuario"),
            ("baseapp_type_administrador", "Tipo Administrador"),
        )
