from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View

from baseapp.forms.grafico import GraficoForm
from baseapp.forms.setor import SetorAjaxForm
from baseapp.models.tipo_grafico import TipoGrafico


class GraficoCreateAjaxView(View):
    '''
    Adiciona um pedido via AJAX.
   :URl: http://ip_servidor/pedido/cadastrar/
    '''
    template_name_json = 'includes/grafico_json.html'
    template_mensagem = 'includes/message_json.html'

    def get(self, request,**kwargs):
        '''
        :param request:
        :param id:
        :param kwargs: id do produto
        :return: HTML do modal
        '''
        context = {}
        data = {}
        form = GraficoForm(request.GET, request.FILES)
        context['form'] =  form
        context['url'] = reverse('grafico-testar')
        print(request.GET['tipo_grafico'])
        print(request.GET['nome'])
        print(self.kwargs)

        object1={}
        object1['titulo'] = request.GET['nome']
        object1['tipo'] = request.GET['tipo_grafico']
        object1['consulta'] = request.GET['consulta']
        consulta = my_custom_sql(object1['consulta'])
        print(consulta)

        tipo = TipoGrafico.objects.get(pk=object1['tipo'])
        data={}
        if str(tipo.id) in ['3',  '2']:
            print("grafico, tabela")
            x = []
            y = []
            for item in consulta:
                x.append(item[0])
                y.append(item[1])
            data['y'] = y
            data['x'] = x
        elif str(tipo.id) == '1':
            print("contador, tabela")
            data['x'] = consulta[0][0]
            print(data['x'])

        object1['data'] = data
        context['object'] = object1

        data['html_form'] = render_to_string(self.template_name_json, context, request=request)
        return JsonResponse(data)

    def post(self, request):
        '''
        :param self:
        :param request:
        :param id: id do produto
        :return: sucesso ou não do cadstro
        '''
        form = GraficoForm(request.POST, request.FILES)
        print(request.FILES)
        print(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            context = {}
            data = dict()
            data['form_is_valid'] = True
            context['form'] = form
            data['id_alterar'] = form.pk
            data['nome_alterar'] = form.nome
            data['campo_alterar'] = 'id_grafico'
            data['sucesso'] = True
            # data['html_form'] = render_to_string(self.template_mensagem, context, request=self.request)
            return JsonResponse(data)
            # return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)

    def form_valid(self, form):
        '''
        :param self:
        :param form: de cadastro do pedido
        :return: um JSON com as informações sobre o cadstro
        '''
        data = dict()
        context = {}
        form.save()
        data['form_is_valid'] = True
        data['html_mensagem'] = render_to_string(self.template_mensagem, context, request=self.request)
        return JsonResponse(data)

    def form_invalid(self, form):
        '''

        :param self:
        :param form: erro no form
        :return: retorna o erro no cadastro
        '''
        context = {}
        data = dict()
        data['form_is_valid'] = False
        context['form'] = form
        context['classe_css'] = 'grafico_testar'
        context['url'] = reverse('grafico-testar')

        # context['titulo'] =  get_object_or_404(Produto, pk=self.kwargs.get("id"))
        # context["url"] = reverse("pedido-produto-add", kwargs={"id":self.kwargs.get("id")})
        data['html_form'] = render_to_string(self.template_name_json, context, request=self.request)
        return JsonResponse(data)


def my_custom_sql(consulta):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(consulta)
    row = cursor.fetchall()
    return row