import datetime

from django import template

from base.settings import MEDIA_URL
from baseapp.models.chamado import Chamado
from baseapp.models.notificacao import Notificacao
from baseapp.models.settings import Settings

register = template.Library()

@register.simple_tag(name='chamadosmesaberto')
def chamadosmesaberto():
    data = datetime.datetime.now()

    data = (data.strftime("%Y-%m-01 00:00:00"))
    chamados =  Chamado.objects.filter(excluido=False, desativado=False, data_inicio__gte=data,status=False)
    return len(chamados)
@register.simple_tag(name='media')
def media():
    return MEDIA_URL
@register.simple_tag(name='settings_login_imagem')
def settings_login_imagem():
    settings = Settings.objects.filter(excluido=False,desativado=False).last()
    if settings:
        return settings.imagem_login
    return ''

@register.simple_tag(name='settings_cadastro_imagem')
def settings_cadastro_imagem():
    settings = Settings.objects.filter(excluido=False,desativado=False).last()
    if settings:
        return settings.imagem_cadastro
    return ''

@register.simple_tag(name='settings_logo_imagem')
def settings_logo_imagem():
    settings = Settings.objects.filter(excluido=False,desativado=False).last()
    if settings:
        return settings.logo
    return ''

@register.simple_tag(name='settings_logo_baixa_imagem')
def settings_logo_baixa_imagem():
    settings = Settings.objects.filter(excluido=False,desativado=False).last()
    if settings:
        return settings.logo_baixa
    return ''

@register.simple_tag(name='settings_cor')
def settings_cor():
    settings = Settings.objects.filter(excluido=False,desativado=False).last()
    if settings:
        return settings.cor
    return ''


@register.simple_tag(name='settings_nome')
def settings_nome():
    settings = Settings.objects.filter(excluido=False,desativado=False).last()
    if settings:
        return settings.nome
    return ''


@register.simple_tag(name='settings_customize')
def settings_customize():
    context={}
    context["customize"] = Settings.objects.filter(excluido=False,desativado=False).last()
    if context["customize"]:
        return context["customize"]
    return context


@register.inclusion_tag('includes/notificacao.html')
def show_notification(user):
    context={}
    context["object_list"] = Notificacao.objects.filter(desativado=False,excluido=False,usuario_recebe=user).reverse()
    context["notificacao"] = len( context["object_list"])
    context["notificacoes"] = len( context["object_list"])
    return context


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()