# # coding=utf-8
# from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.http import JsonResponse
# from django.views.generic import *
# from django.core.urlresolvers import reverse_lazy
# from appusuario.forms.instituicao import *
# from appbase.variaveis import *
#
#
# class InstituicaoListView(PermissionRequiredMixin, ListView):
#     '''
#     Lista todos os Instituicao.
#
#     :URl: http://ip_servidor/author-list/
#     '''
#     permission_required = LIST_INSTITUICAO
#     queryset = Instituicao.objects.all()
#
#
# class InstituicaoDetailView(PermissionRequiredMixin, DetailView):
#     '''
#     Exibe, atualiza e deleta um Instituicao específico.
#
#     :URl: http://ip_servidor/submissao/instituicao/<id>/
#     '''
#     permission_required = DETAIL_INSTITUICAO
#     queryset = Instituicao.objects.all()
#
#
# class InstituicaoCreateView(PermissionRequiredMixin, CreateView):
#     permission_required = ADD_INSTITUICAO
#     model = Instituicao
#     form_class = InstituicaoForm
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.usuario = self.request.user
#         self.object.save()
#         return super(InstituicaoCreateView, self).form_valid(form)
#
#
# class InstituicaoUpdateView(PermissionRequiredMixin, UpdateView):
#     permission_required = CHANGE_INSTITUICAO
#     model = Instituicao
#     form_class = InstituicaoForm
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.usuario = self.request.user
#         self.object.save()
#         return super(InstituicaoUpdateView, self).form_valid(form)
#
#
# class InstituicaoDeleteView(PermissionRequiredMixin, DeleteView):
#     permission_required = DELETE_INSTITUICAO
#     model = Instituicao
#     success_url = reverse_lazy('instituicao-list')
#
#     def get(self, *args, **kwargs):
#         return self.post(*args, **kwargs)
#
#
# def get_instituicao(request):
#     instituicao = request.GET.get('nome')
#     data = {
#         'id_instituicao': Instituicao.objects.get(nome=instituicao).id,
#         'nome_instituicao': Instituicao.objects.get(nome=instituicao).nome
#     }
#     return JsonResponse(data)
