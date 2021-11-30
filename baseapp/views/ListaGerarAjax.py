from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from baseapp.models.grafico import Grafico


class ListaGerarAjaxView(View):
    '''
    Adiciona um pedido via AJAX.
   :URl: http://ip_servidor/pedido/cadastrar/
    '''

    def get(self, request, **kwargs):
        '''
        :param request:
        :param id:
        :param kwargs: id do produto
        :return: HTML do modal
        '''
        context = {}
        data = {}
        data['form_is_valid'] = True
        data['id'] = self.kwargs.get('pk')
        data['titulo'] = 'chamados'
        data['tipo'] = 'bar'
        lista = get_object_or_404(Grafico, pk=self.kwargs.get('pk'))

        consulta = my_custom_sql(lista.sql)
        print(consulta)
        data['titulo'] = lista.nome
        lista = []
        for item in consulta:
            lista.append(item[0])
        data['lista'] = lista
        data['valor'] = lista

        return JsonResponse(data)


def my_custom_sql(consulta):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(consulta)
    row = cursor.fetchall()
    return row
