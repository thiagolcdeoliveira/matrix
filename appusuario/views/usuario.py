# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import *
# from django.core.urlresolvers import reverse_lazy, reverse
# from appusuario.forms import InstituicaoForm
from appusuario.forms.usuario import *
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.shortcuts import redirect
# from appbase.variaveis import *
# from appusuario.models.instituicao import Instituicao
from appusuario.variaveis import LIST_COMPLEMENTO_USUARIO, DETAIL_COMPLEMENTO_USUARIO, CHANGE_COMPLEMENTO_USUARIO, \
    DELETE_COMPLEMENTO_USUARIO


class ComplementoUsuarioListView(PermissionRequiredMixin, ListView):
    '''
    Lista todos os Usuario.

    :URl: http://ip_servidor/author-list/
    '''
    permission_required = LIST_COMPLEMENTO_USUARIO
    queryset = ComplementoUsuario.objects.filter(excluido=False)


class CompletoUsuarioDetailView(PermissionRequiredMixin, DetailView):
    '''
    Exibe, atualiza e deleta um Usuario específico.

    :URl: http://ip_servidor/submissao/usuario/<id>/
    '''
    permission_required = DETAIL_COMPLEMENTO_USUARIO
    queryset = ComplementoUsuario.objects.filter(excluido=False)


class ComplementoUsuarioCreateView(CreateView):
    model = ComplementoUsuario
    form_class = UsuarioForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.id = self.request.user
        self.object.user_id = self.request.user
        self.object.save()
        return super(ComplementoUsuarioCreateView, self).form_valid(form)

#
# class ComplementoUsuarioCreateViewMultiForms(CreateView):
#     # instituicoes = Instituicao.objects.all()
#     model = ComplementoUsuario
#     form_class = UsuarioForm
#     second_form_class = InstituicaoForm
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.id = self.request.user
#         self.object.user_id = self.request.user
#         self.object.save()
#         return super(ComplementoUsuarioCreateViewMultiForms, self).form_valid(form)
#
#     def form_invalid(self, form):
#         return super(ComplementoUsuarioCreateViewMultiForms, self).form_invalid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super(ComplementoUsuarioCreateViewMultiForms, self).get_context_data(**kwargs)
#         context['instituicoes'] = self.instituicoes
#
#         if 'instituicao' not in context:
#             context['instituicao'] = self.second_form_class()
#         return context


class ComplementoUsuarioUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = CHANGE_COMPLEMENTO_USUARIO
    model = ComplementoUsuario
    form_class = UsuarioForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return super(ComplementoUsuarioUpdateView, self).form_valid(form)


class ComplementoUsuarioDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = DELETE_COMPLEMENTO_USUARIO
    model = ComplementoUsuario
    success_url = reverse_lazy('complemento-usuario-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.user_id = self.request.user
        self.object.excluido = True
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


def verifica_token(request, uidb64, token):
    if uidb64 is not None and token is not None:
        id = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponseRedirect('%s' % (reverse('login')))
        return redirect('login')
    return redirect('login')
