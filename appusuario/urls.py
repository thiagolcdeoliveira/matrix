# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib.auth.views import *
from appusuario.views.usuario import *
from appusuario.views.user import *


urlpatterns = [



    # ---- Usuario ----#
    # url(r'^complemento-usuario/cadastrar/$', ComplementoUsuarioCreateViewMultiForms.as_view(), name='complemento-usuario-add'),
    url(r'^complemento-usuario/(?P<pk>[0-9]+)/visualizar/$', CompletoUsuarioDetailView.as_view(), name='complemento-usuario-detail'),
    url(r'^complemento-usuario/(?P<pk>[0-9]+)/editar/$', ComplementoUsuarioUpdateView.as_view(), name='complemento-usuario-update'),
    url(r'^complemento-usuario/(?P<pk>[0-9]+)/excluir/$', ComplementoUsuarioDeleteView.as_view(), name='complemento-usuario-delete'),
    url(r'^complemento-usuario/listar/$', ComplementoUsuarioListView.as_view(), name='usuario-list'),

    url(r'^complemento-usuario/confirmar/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', verifica_token, name='complemento-usuario-verifica-token'),

    # ---- User ----#
    url(r'^user/cadastrar/$', UserCreateView.as_view(), name='user-add'),
    url(r'^user-convidado/cadastrar/$', UserConvidadoCreateView.as_view(), name='user-convidado-add'),
    url(r'^user-convidado/cadastrar/ajax/$', UserConvidadoAjaxCreateView.as_view(), name='user-servidor-add'),
    url(r'^user/(?P<pk>[0-9]+)/visualizar/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^user/perfil/$', UserProfileDetailView.as_view(), name='user-profile'),
    url(r'^user/perfil/editar/$', UserProfileUpdateView.as_view(), name='user-profile-edit'),
    url(r'^user/(?P<pk>[0-9]+)/excluir/$', UserDeleteView.as_view(), name='user-delete'),
    url(r'^user/listar/$', UserListView.as_view(), name='user-list'),
    url(r'^user/editar/$', UserUpdateView.as_view(), name='user-update'),
    url(r'^user/email/add/$', CreateEmailView.as_view(), name='user-email-add'),

    url(r'^user/sucesso/$', TemplateView.as_view(template_name='auth/user_messages.html'), name='user-message'),

    # ---- Senha ----#
    url(r'^usuario/alterar-senha/$', PasswordChangeView.as_view(template_name= 'appusuario/alterarsenha-form.html'), { 'template_name': 'appusuario/alterarsenha-form.html'}, name='password_change'),
    url(r'^usuario/alterar-senha/feito/$', PasswordChangeDoneView.as_view(template_name= 'appusuario/alterarsenha-feito.html'), {'template_name': 'appusuario/alterarsenha-feito.html'}, name='password_change_done'),

    url(r'^usuario/redefinir-senha/$', PasswordResetView.as_view(template_name = 'appusuario/redefinirsenha-form.html',
                                                          email_template_name= 'appusuario/redefinirsenha-email.html',
                                                          subject_template_name= 'appusuario/redefinirsenha-assunto.txt'), {'template_name': 'appusuario/redefinirsenha-form.html','email_template_name' : 'appusuario/redefinirsenha-email.html',
                                                          'subject_template_name': 'appusuario/redefinirsenha-assunto.txt'}, name='password_reset'),
    url(r'^usuario/redefinir-senha/feito/$', PasswordResetDoneView.as_view(template_name ='appusuario/redefinirsenha-feito.html'), {'template_name': 'appusuario/redefinirsenha-feito.html'}, name='password_reset_done'),
    url(r'^usuario/redefinir/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)//$', PasswordResetConfirmView.as_view(template_name ='appusuario/redefinirsenha-confirmacao.html'), {'template_name': 'appusuario/redefinirsenha-confirmacao.html'}, name='password_reset_confirm'),
    url(r'^usuario/redefinir/feito/$', PasswordResetCompleteView.as_view(template_name ='appusuario/redefinirsenha-completo.html'), {'template_name': 'appusuario/redefinirsenha-completo.html'}, name='password_reset_complete'),
    url(r'^complemento-usuario/troca-senha/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        verifica_token_autor,
        name='verifica_token_autor'),

    # --- AJAX --#
    url(r'^ajax/get-user/$', get_user, name='get-user'),
    url(r'^tasks/create/$', TaskView.as_view(), name='task-add'),

]
