# coding=utf-8
from __future__ import absolute_import

import json
import random
import string

from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
# from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import *

# from appbase.variaveis import *
from appusuario.forms import UsuarioForm
from appusuario.forms.user import *
# from eventos.settings.settings import DEFAULT_FROM_EMAIL
from appusuario.models import ComplementoUsuario
from appusuario.variaveis import DETAIL_COMPLEMENTO_USUARIO, LIST_USER, DETAIL_USER, DELETE_USER
from baseapp.views.email import send_mail


class UserListView(PermissionRequiredMixin, ListView):
    '''
    Lista todos os User.

    :URl: http://ip_servidor/author-list/
    '''
    permission_required = LIST_USER
    queryset = User.objects.filter(is_active=True)


class UserDetailView(DetailView):
    '''
    Exibe, atualiza e deleta um User específico.

    :URl: http://ip_servidor/submissao/user/<id>/
    '''
    queryset = User.objects.filter(is_active=True)


@method_decorator(login_required, name='dispatch')
class UserProfileDetailView(DetailView):
    '''
    Exibe, atualiza e deleta um User específico.

    :URl: http://ip_servidor/submissao/user/<id>/
    '''
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if ComplementoUsuario.objects.filter(user__id=self.request.user.id):
            context['complemento'] = ComplementoUsuario.objects.get(user__id=self.request.user.id)
        return context

    def get_object(self, queryset=None):
        queryset = User.objects.get(id=self.request.user.id)
        return queryset


class UserCreateView(CreateView):
    model = User
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self.object.email
        self.object.set_password(self.object.password)
        self.object.is_active = False
        self.object.save()
        user = self.object
        convidado = False
        token = default_token_generator.make_token(user)
        id = urlsafe_base64_encode(force_bytes(user.pk))
        msg = mensagem(self.request, token, id, convidado, user.first_name)
        envia_email(user.email, msg)
        return super(UserCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(UserCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("user-message")


class UserConvidadoCreateView(CreateView):
    model = User
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self.object.email
        self.object.set_password(self.gerar_senha())
        self.object.is_active = False
        self.object.save()
        user = self.object
        convidado = True
        token = default_token_generator.make_token(user)
        id = urlsafe_base64_encode(force_bytes(user.pk))
        msg = mensagem(self.request, token, id, convidado, user.first_name)
        envia_email(user.email, msg)
        return super(UserConvidadoCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print('---- User ----')
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

    def gerar_senha(self):
        char = list(string.ascii_letters + string.punctuation)
        tamanho_char = len(char) - 1
        tamanho = random.randint(8, 16)
        return ''.join([char[random.randint(0, tamanho_char)] for i in range(tamanho)])

    def get_success_url(self):
        return reverse_lazy("login")

#class UserConvidadoAjaxCreateView(CreateView):
class UserConvidadoAjaxCreateView(View):
    model = User
    form_class = UserConvidadoForm
    template_name_json = 'includes/form_json.html'
    template_mensagem = 'includes/message_json.html'


    def post(self, request):
        '''
        :param self:
        :param request:
        :param id: id do produto
        :return: sucesso ou não do cadstro
        '''
        form = UserConvidadoForm(request.POST, request.FILES)
        if  form.is_valid():
            form = form.save(commit=False)
            # self.object = form.save(commit=False)
            self.object = form
            self.object.username = self.object.email
            self.object.set_password(self.gerar_senha())
            self.object.is_active = False
            self.object.save()
            user = self.object
            convidado = True
            token = default_token_generator.make_token(user)
            id = urlsafe_base64_encode(force_bytes(user.pk))
            msg = mensagem(self.request, token, id, convidado, user.first_name)
            envia_email(user.email, msg)
            form.save()
            context = {}
            data = dict()
            data['form_is_valid'] = True
            context['form'] =  form
            data['id_alterar'] =  form.pk
            data['nome_alterar'] =  form.username
            data['campo_alterar'] = 'id_solicitante'
            data['sucesso'] = True
            data['html_form'] = render_to_string(self.template_mensagem, context, request=self.request)
            return JsonResponse(data)
            # return self.form_valid(form)
        else:
            context = {}
            data = dict()
            data['form_is_valid'] = False
            context['form'] = form
            context['classe_css'] = 'pedido_add'
            context['url'] = reverse('user-servidor-add')

            # context['titulo'] =  get_object_or_404(Produto, pk=self.kwargs.get("id"))
            # context["url"] = reverse("pedido-produto-add", kwargs={"id":self.kwargs.get("id")})
            data['html_form'] = render_to_string(self.template_name_json, context, request=self.request)
            return JsonResponse(data)

    def get(self, request, **kwargs):
        '''
        :param request:
        :param id:
        :param kwargs: id do produto
        :return: HTML do modal
        '''
        print("aqui")
        context = {}
        data = {}
        form = UserConvidadoForm()
        context['form'] = form
        # context['titulo'] =  get_object_or_404(Produto,pk=self.kwargs.get("id"))
        context['url'] = reverse('user-servidor-add')
        data['html_form'] = render_to_string(self.template_name_json, context, request=request)
        return JsonResponse(data)

    def gerar_senha(self):
        char = list(string.ascii_letters + string.punctuation)
        tamanho_char = len(char) - 1
        tamanho = random.randint(8, 16)
        return ''.join([char[random.randint(0, tamanho_char)] for i in range(tamanho)])



class UserUpdateView(UpdateView):
    # permission_required = DETAIL_USER
    model = User
    form_class = UserEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UserUpdateView, self).form_valid(form)


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = DELETE_USER
    model = User
    success_url = reverse_lazy('user-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.user_id = self.request.user
        self.object.is_active = False
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


def envia_email(username, msg):
    send_mail(
        u'Sistema de Chamados',
        msg,
        [username],
    )



# from celery import shared_task


# @shared_task
# def envia_email_task(username, msg):
#     envia_email(username=username, msg=msg)
#     return "email de cadastro de usuario enviado com sucesso"
#


def get_user(request):
    username = request.GET.get('username')
    data = {
        'id_usuario': User.objects.get(username=username).id,
        'username_usuario': User.objects.get(username=username).username,
        'nome_usuario': '%s %s' % (
            User.objects.get(username=username).first_name, User.objects.get(username=username).last_name)
    }
    return JsonResponse(data)


def mensagem(request, token, id, convidado, nome):
    msg_topo = "<p>Prezado(a) senhor(a) " + nome + ",<br>voc&ecirc; foi cadastrado no Sistema de chamados da TI da prefeitura de Araquari</p>"
    msg_motivo = u"<p>Sua conta foi criada pois voc&ecirc;  foi  cadastrado  como autor de um chamado no sistema.</p>"
    texto_link = "<p> Para ativar sua conta, "
    link_user = "<a href='http://" + request.META[
        'HTTP_HOST'] + "/complemento-usuario/confirmar/%s/%s/'>CLIQUE AQUI</a>" % (id, token)
    link_autor = "<a href='http://" + request.META[
        'HTTP_HOST'] + "/complemento-usuario/troca-senha/%s/%s/'>CLIQUE AQUI</a>" % (id, token)
    msg_rodape = "<p><br><br>Este e-mail for enviado automaticamente pelo Sistema chamados, favor n&atilde;o responder.</p><p>Coordena&ccedil;&atilde;o Geral do Sistema</p>"
    if convidado:
        msg_completa_email = str(msg_topo + msg_motivo + texto_link + link_autor + msg_rodape)
    else:
        msg_completa_email = str(msg_topo + texto_link + link_user + msg_rodape)
    return msg_completa_email


class AjaxableResponseMixin(object):
    """ Ajax form based on the django docs example.
    https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/#ajax-example
    https://docs.djangoproject.com/en/dev/topics/class-based-views/mixins/#more-than-just-html
    """

    def render_to_json_response(self, context, **response_kwargs):
        """Render a json response of the context."""

        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class TaskView(AjaxableResponseMixin, CreateView):
    model = User
    form_class = UserConvidadoForm
    success_url = '/'

    def form_invalid(self, form):
        response = super(TaskView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self.object.email
        self.object.is_active = False
        self.object.save()
        user = self.object
        convidado = True
        token = default_token_generator.make_token(user)
        id = urlsafe_base64_encode(force_bytes(user.pk))
        msg = mensagem(self.request, token, id, convidado, user.first_name)
        envia_email(user.email, msg)

        response = super(TaskView, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'id_usuario': self.object.pk,
                'nome_usuario': '%s %s' % (self.object.first_name, self.object.last_name),
                'username_usuario': self.object.username,
            }
            return JsonResponse(data)
        else:
            return response


def verifica_token_autor(request, uidb64, token):
    if uidb64 is not None and token is not None:
        id = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect('%s' % (reverse('user-update')))
        return redirect('403')
    return redirect('403')


@method_decorator(login_required, name='dispatch')
class UserUpdateView(View):
    template = 'auth/user_edit_form.html'
    context = {}

    def get(self, request):
        self.context["form"] = UserEditForm(instance=request.user)
        self.context["email"] = request.user.email
        return render(request, self.template, self.context)

    def post(self, request, ):
        form = UserEditForm(instance=request.user, data=request.POST)

        if form.is_valid():
            form_edit = form.save(commit=False)
            form_edit.is_active = True
            form_edit.set_password(form_edit.password)
            form_edit.save()

            return redirect('/')
        else:
            self.context["form"] = form
            self.context["email"] = request.user.email

        return render(request, self.template, self.context)


@method_decorator(login_required, name='dispatch')
class UserProfileUpdateView(View):
    template = 'auth/user_profile_form.html'
    template_sucess = 'auth/user_detail.html'
    success_url = reverse_lazy('user-profile')

    context = {}

    def get(self, request):
        self.context["form"] = UserProfileForm(instance=request.user)
        # complemento = ComplementoUsuario.objects.filter(user=request.user)
        complemento, created = ComplementoUsuario.objects.get_or_create(user=request.user)

        # if complemento:
        self.context["formComplemento"] = UsuarioForm(instance=complemento)
        # else:
        #     self.context["formComplemento"] = UsuarioForm()
        self.context["email"] = request.user.email
        return render(request, self.template, self.context)

    def post(self, request, ):
        form = UserProfileForm(instance=request.user, data=request.POST)
        # complemento = ComplementoUsuario.objects.filter(user=request.user)
        # if complemento:
        #     formComplemento = UsuarioForm(instance=complemento[0],data=request.POST)
        # else:
        complemento, created = ComplementoUsuario.objects.get_or_create(user=request.user)
        formComplemento = UsuarioForm(instance=complemento,data=request.POST)

        if form.is_valid() and formComplemento.is_valid():
            form.save()
            formComplemento.user = request.user
            formComplemento.save()
            self.context["object"] = User.objects.get(id=self.request.user.id)
            self.context["message_sucess"] = True
            # return render(request, self.template_sucess, self.context)
            return HttpResponseRedirect(self.success_url)

        else:
            self.context["form"] = form
            self.context["formComplemento"] = formComplemento
            self.context["email"] = request.user.email
        return render(request, self.template, self.context)


@method_decorator(login_required, name='dispatch')
class CreateEmailView(View):
    template = 'auth/user_email_form.html'
    context = {}

    def get(self, request):
        self.context["form"] = CreateEmailForm(instance=request.user)
        return render(request, self.template, self.context)

    def post(self, request, ):
        form = CreateEmailForm(instance=request.user, data=request.POST)

        if form.is_valid():
            form_edit = form.save()

            form_edit.username = form_edit.email
            form_edit.save()

            return redirect('/')
        else:
            self.context["form"] = form

        return render(request, self.template, self.context)
