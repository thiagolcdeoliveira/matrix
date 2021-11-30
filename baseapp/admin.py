from django.contrib import admin

# Register your models here.
from baseapp.models import Produto
from baseapp.models.chamado import Chamado
from baseapp.models.dashboard import Dashboard
from baseapp.models.email import ConfiguracaoEmail
from baseapp.models.endereco import Endereco
from baseapp.models.equipamento import Equipamento
from baseapp.models.grafico import Grafico
from baseapp.models.notificacao import Notificacao
from baseapp.models.prioridade import Prioridade
from baseapp.models.propriedade import Propriedade
from baseapp.models.secretaria import Secretaria
from baseapp.models.setor import Setor
from baseapp.models.settings import Settings
from baseapp.models.situacao import Situacao
from baseapp.models.tamanho import Tamanho
from baseapp.models.tipo_chamado import TipoChamado
from baseapp.models.tipo_grafico import TipoGrafico
from baseapp.models.tipo_notificacao import TipoNotificacao
from baseapp.models.tipo_propriedade import TipoPropriedade

admin.site.register(Secretaria)
admin.site.register(Setor)
admin.site.register(Produto)
admin.site.register(Equipamento)
admin.site.register(Prioridade)
admin.site.register(TipoChamado)
admin.site.register(Situacao)
admin.site.register(Chamado)


admin.site.register(Dashboard)
admin.site.register(Grafico)
admin.site.register(TipoGrafico)
admin.site.register(Tamanho)


admin.site.register(Notificacao)
admin.site.register(Settings)
admin.site.register(TipoNotificacao)

admin.site.register(TipoPropriedade)
admin.site.register(Propriedade)
admin.site.register(Endereco)

admin.site.register(ConfiguracaoEmail)
