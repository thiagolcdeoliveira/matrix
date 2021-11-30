from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.views import View

from baseapp.models.dashboard import Dashboard
from baseapp.models.grafico import Grafico


class ContadorGerarAjaxView(View):
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
        data = {}
        data['form_is_valid']  = True
        data['id']  = self.kwargs.get('pk')
        contador = get_object_or_404(Dashboard,pk=self.kwargs.get('pk'))
        data['titulo'] = contador.grafico.nome
        consulta = my_custom_sql(contador.grafico.consulta)
        print(consulta[0][0])
        data['valor'] = consulta[0][0]
        return JsonResponse(data)

def my_custom_sql(consulta):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(consulta)
    row = cursor.fetchall()
    return row
#