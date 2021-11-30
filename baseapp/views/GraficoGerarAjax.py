from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.views import View

from baseapp.models.dashboard import Dashboard
from baseapp.models.grafico import Grafico


class GraficoGerarAjaxView(View):
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
        grafico = get_object_or_404(Dashboard,pk=self.kwargs.get('pk'))
        data['titulo'] = grafico.grafico.nome
        data['tipo'] = grafico.tipo.descricao

        consulta = my_custom_sql(grafico.grafico.consulta)
        x=[]
        y=[]
        for item in consulta:
            x.append(item[0])
            y.append(item[1])
        data['y'] = y
        data['x'] = x

        return JsonResponse(data)
def my_custom_sql(consulta):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(consulta)
    row = cursor.fetchall()
    return row

