from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View

from baseapp.forms.setor import SetorAjaxForm


class SetorCreateAjaxView(View):
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
        form = SetorAjaxForm()
        context['form'] =  form
        # context['titulo'] =  get_object_or_404(Produto,pk=self.kwargs.get("id"))
        context['url'] = reverse('setor-add')


        data['html_form'] = render_to_string(self.template_name_json, context, request=request)
        return JsonResponse(data)

    def post(self, request):
        '''
        :param self:
        :param request:
        :param id: id do produto
        :return: sucesso ou não do cadstro
        '''
        form = SetorAjaxForm(request.POST, request.FILES)
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
            data['campo_alterar'] = 'id_setor'
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
        # data["carrinho"] = Pedido.objects.filter(desativado=False,finalizado=False,cliente__username=self.request.user).count()
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
        context['classe_css'] = 'pedido_add'
        context['url'] = reverse('setor-add')

        # context['titulo'] =  get_object_or_404(Produto, pk=self.kwargs.get("id"))
        # context["url"] = reverse("pedido-produto-add", kwargs={"id":self.kwargs.get("id")})
        data['html_form'] = render_to_string(self.template_name_json, context, request=self.request)
        return JsonResponse(data)