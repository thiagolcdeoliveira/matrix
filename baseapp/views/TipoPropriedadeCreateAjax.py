from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View

from baseapp.forms.setor import SetorAjaxForm
from baseapp.forms.tipo_propriedade import TipoPropriedadeAjaxForm


class TipoPropriedadeCreateAjaxView(View):
    '''
    Adiciona um pedido via AJAX.
   :URl: http://ip_servidor/pedido/cadastrar/
    '''
    template_name_json = 'includes/form_json.html'
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
        form = TipoPropriedadeAjaxForm()
        context['form'] =  form
        context['url'] = reverse('tipo-propriedade-ajax-add')
        data['html_form'] = render_to_string(self.template_name_json, context, request=request)
        return JsonResponse(data)

    def post(self, request):
        '''
        :param self:
        :param request:
        :param id: id do produto
        :return: sucesso ou não do cadstro
        '''
        form = TipoPropriedadeAjaxForm(request.POST, request.FILES)
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
            data['campo_alterar'] = 'id_tipo_propriedade'
            data['sucesso'] = True
            return JsonResponse(data)
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
        context['classe_css'] = 'tipo_propriedade_add'
        context['url'] = reverse('tipo-propriedade-ajax-add')
        data['html_form'] = render_to_string(self.template_name_json, context, request=self.request)
        return JsonResponse(data)