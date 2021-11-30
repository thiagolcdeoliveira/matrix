from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from baseapp.models.dashboard import Dashboard
from baseapp.models.grafico import Grafico


class TabelaGerarAjaxView(View):
    '''
    Adiciona um pedido via AJAX.
   :URl: http://ip_servidor/pedido/cadastrar/
    '''

    def get(self, request,**kwargs):
        '''
        :param request:
        :param id:
        :param kwargs: id do produto
        :return: HTML do modal
        '''
        context = {}
        data = {}
        data['form_is_valid']  = True
        data['id']  = self.kwargs.get('pk')
        data['titulo']  = 'chamados'
        data['tipo']  = 'bar'
        grafico = get_object_or_404(Dashboard,pk=self.kwargs.get('pk'))

        consulta = my_custom_sql(grafico.grafico.consulta)
        x=[]
        y=[]
        ii = consulta[0].keys()
        iii = []
        print(x)
        print(consulta)
        lista = list(ii)

        for item in consulta:
            iii = []
            for i in range(len(ii)):
                posicao = lista[i]
                iii.append(item[posicao])

            y.append(iii)
        x  = lista
        data['y'] = y
        data['x'] = x
        return JsonResponse(data)
def my_custom_sql(consulta):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(consulta)
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
