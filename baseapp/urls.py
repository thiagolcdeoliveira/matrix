# coding=utf-8
from __future__ import unicode_literals

from django.conf.urls import url

from baseapp.views.ContadorGerarAjax import ContadorGerarAjaxView
from baseapp.views.EnderecoCreateAjax import EnderecoCreateAjaxView
from baseapp.views.EquipamentoSearchAjax import EquipamentoSearchAjaxView
from baseapp.views.GraficoGerarAjax import GraficoGerarAjaxView
from baseapp.views.ListaGerarAjax import ListaGerarAjaxView
from baseapp.views.PesquisarUserCreateAjax import PesquisarUserCreateAjaxView
from baseapp.views.ProdutoSearchAjax import ProdutoSearchAjaxView
from baseapp.views.PropriedadeCreateAjax import PropriedadeCreateAjaxView
from baseapp.views.PropriedadeSearchAjax import PropriedadeSearchAjaxView
from baseapp.views.SetorCreateAjax import SetorCreateAjaxView
from baseapp.views.TabelaGerarAjax import TabelaGerarAjaxView
from baseapp.views.TipoPropriedadeCreateAjax import TipoPropriedadeCreateAjaxView
from baseapp.views.chamado.chamadoAbrir import ChamadoAbrirView
from baseapp.views.chamado.chamadoCreate import ChamadoUsuarioCreateView, ChamadoCreateView
from baseapp.views.chamado.chamadoDetail import ChamadoDetailView, ChamadoUsuarioDetailView
from baseapp.views.chamado.chamadoFechar import ChamadoFecharView
from baseapp.views.chamado.chamadoList import ChamadoListView, ChamadoMeuListView
from baseapp.views.chamado.chamadoQrcode import ChamadoQrcodeView
from baseapp.views.chamado.chamadoUpadate import ChamadoUpdateView, ChamadoAdminUpdateView, ChamadoIniciarUpdateView
from baseapp.views.dashboard.dashboardCreate import DashboardCreateView
from baseapp.views.dashboard.dashboardDelete import DashboardDeleteView, DashboardActiveView, DashboardDesativeView
from baseapp.views.dashboard.dashboardDetail import DashboardDetailView
from baseapp.views.dashboard.dashboardListView import DashboardMeuListView
from baseapp.views.dashboard.dashboard import DashboardView
from baseapp.views.dashboard.dashboardUpdate import DashboardUpdateView
from baseapp.views.grafico.graficoDetail import GraficoDetailView
from baseapp.views.grafico.graficoList import GraficoListView
from baseapp.views.graficoCreateAjax import GraficoCreateAjaxView
from baseapp.views.mensagemCreate import MensagemCreateView
from baseapp.views.notificacao import NotificacaoView
from baseapp.views.notificacaoList import NotificacaoMeuListView
from baseapp.views.grafico.graficoCreate import GraficoCreateView
from baseapp.views.propriedade.propriedadeCreate import PropriedadeCreateView
from baseapp.views.propriedade.propriedadeDetail import PropriedadeDetailView
from baseapp.views.propriedade.propriedadeList import PropriedadeListView, PropriedadeMeuListView
from baseapp.views.propriedade.propriedadeUpadate import PropriedadeUpdateView

urlpatterns = [
    url(r'^chamado/cadastrar/$', ChamadoUsuarioCreateView.as_view(),
        name='chamado-add'),
    url(r'^chamado/admin/cadastrar/$', ChamadoCreateView.as_view(),
        name='chamado-admin-add'),
    url(r'^chamado/listar$', ChamadoListView.as_view(),
        name='chamado-list'),
    url(r'^chamado/servidor/listar$', ChamadoMeuListView.as_view(),
        name='chamado-meu-list'),
    url(r'^chamado/visualizar/(?P<pk>[\d\-]+)/$', ChamadoDetailView.as_view(),
        name='chamado-detail'),
    url(r'^chamado/(?P<pk>[\d\-]+)/visualizar/$', ChamadoUsuarioDetailView.as_view(),
        name='chamado-usuario-detail'),

    url(r'^chamado/atualizar/(?P<pk>[\d\-]+)/$', ChamadoUpdateView.as_view(),
        name='chamado-update'),
    url(r'^chamado/admin/atualizar/(?P<pk>[\d\-]+)/$', ChamadoAdminUpdateView.as_view(),
        name='chamado-admin-update'),
    url(r'^chamado/gerar/qrcode/(?P<pk>[\d\-]+)/$', ChamadoQrcodeView.as_view(),
        name='chamado-gera-qrcode'),

    url(r'^chamado/excluir/(?P<pk>[\d\-]+)/$', ChamadoCreateView.as_view(),
        name='chamado-delete'),
    url(r'^chamado/fechar/(?P<pk>[\d\-]+)', ChamadoFecharView.as_view(),
        name='chamado-fechar'),
    url(r'^chamado/abrir/(?P<pk>[\d\-]+)', ChamadoAbrirView.as_view(),
        name='chamado-abrir'),
    url(r'^chamado/usuario/atualizar/(?P<pk>[\d\-]+)/$', ChamadoUpdateView.as_view(),
        name='chamado-usuario-update'),
    url(r'^chamado/atendimento/iniciar/(?P<pk>[\d\-]+)/$', ChamadoIniciarUpdateView.as_view(),
        name='chamado-iniciar'),

    url(r'^chamado/servidor/pesquisar/$', PesquisarUserCreateAjaxView.as_view(),
        name='user-servidor-pesquisar'),
    url(r'^chamado/mensagem/cadastrar/(?P<pk>[\d\-]+)/$', MensagemCreateView.as_view(),
        name='mensagem-chamado-add'),
    url(r'^chamado/propriedade/(?P<pk>[\d\-]+)/$', ChamadoListView.as_view(),
        name='chamado-propriedade-history'),

    # Setor
    url(r'^setor/cadastrar/ajax/', SetorCreateAjaxView.as_view(),
        name='setor-add'),


    #Dashboard
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^grafico/gerar/ajax/(?P<pk>[\d\-]+)/', GraficoGerarAjaxView.as_view(),
        name='grafico-gerar'),
    url(r'^contador/gerar/ajax/(?P<pk>[\d\-]+)/', ContadorGerarAjaxView.as_view(),
        name='contador-gerar'),
    url(r'^tabela/gerar/ajax/(?P<pk>[\d\-]+)/', TabelaGerarAjaxView.as_view(),
        name='tabela-gerar'),
    url(r'^lista/gerar/ajax/(?P<pk>[\d\-]+)/', ListaGerarAjaxView.as_view(),
        name='lista-gerar'),

    url(r'^notificacao/(?P<pk>[\d\-]+)/', NotificacaoView.as_view(),
        name='notificacao'),
    url(r'^notificacao/usuario/listar/', NotificacaoMeuListView.as_view(),
        name='notificacao-meu-list'),

    # propriedade
    url(r'^propriedade/cadastrar/ajax/', PropriedadeCreateAjaxView.as_view(),
        name='propriedade-ajax-add'),
    url(r'^propriedade/pesquisar/$', PropriedadeSearchAjaxView.as_view(),
        name='propriedade-search'),

    #grafico
    url(r'^grafico/cadastrar/$', GraficoCreateView.as_view(),
        name='grafico-add'),
    url(r'^grafico/testar/$', GraficoCreateAjaxView.as_view(),
        name='grafico-testar'),
    url(r'^grafico/listar/$', GraficoListView.as_view(),
        name='grafico-listar'),
    url(r'^grafico/visualizador/(?P<pk>[\d\-]+)/$', GraficoDetailView.as_view(),
        name='grafico-detail'),

    #dashboard
    url(r'^dashboard/meusgraficos/listar/$', DashboardMeuListView.as_view(),
        name='dashboard-meu-listar'),
    url(r'^dashboard/visualizador/(?P<pk>[\d\-]+)/$', DashboardDetailView.as_view(),
        name='dashboard-detail'),
    url(r'^dashboard/cadastrar/$', DashboardCreateView.as_view(),
        name='dashboard-add'),
    url(r'^dashboard/delete/(?P<pk>[\d\-]+)/$', DashboardDeleteView.as_view(),
        name='dashboard-delete'),
    url(r'^dashboard/desativar/(?P<pk>[\d\-]+)/$', DashboardDesativeView.as_view(),
        name='dashboard-desative'),
    url(r'^dashboard/active/(?P<pk>[\d\-]+)/$', DashboardActiveView.as_view(),
        name='dashboard-active'),
    url(r'^dashboard/update/(?P<pk>[\d\-]+)/$', DashboardUpdateView.as_view(),
        name='dashboard-update'),

    #propriedade
    url(r'^propriedade/cadastrar/$', PropriedadeCreateView.as_view(),
        name='propriedade-add'),
    url(r'^propriedade/visualizar/(?P<pk>[\d\-]+)/$', PropriedadeDetailView.as_view(),
        name='propriedade-detail'),
    url(r'^propriedade/atualizar/(?P<pk>[\d\-]+)/$', PropriedadeUpdateView.as_view(),
        name='propriedade-update'),
    url(r'^propriedade/minhaspropriedades/listar/$', PropriedadeMeuListView.as_view(),
        name='propriedade-meu-listar'),
    url(r'^propriedade/listar/$', PropriedadeListView.as_view(),
        name='propriedade-listar'),
    url(r'^propriedade/historico/$', PropriedadeListView.as_view(),
        name='propriedade-history'),
    #tipo propriedade
    url(r'^propriedade/ajax/cadastrar/$', TipoPropriedadeCreateAjaxView.as_view(),
        name='tipo-propriedade-ajax-add'),


    # endereco
    url(r'^endereco/ajax/cadastrar/$', EnderecoCreateAjaxView.as_view(),
        name='endereco-ajax-add'),

    # equipamento
    url(r'^equipamento/ajax/search/$', EquipamentoSearchAjaxView.as_view(),
        name='equipamento-ajax-search'),

    # produto
    url(r'^produto/ajax/search/$', ProdutoSearchAjaxView.as_view(),
        name='produto-ajax-search'),
]
