# coding=utf-8
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views.generic.edit import CreateView
from baseapp.forms.propriedade import PropriedadeForm
from baseapp.models.propriedade import Propriedade


class PropriedadeCreateView(LoginRequiredMixin, CreateView):
    # permission_required = ADD_CHAMADO
    template_name = 'propriedade/propriedade_form.html'
    model = Propriedade
    form_class = PropriedadeForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(PropriedadeCreateView, self).form_valid(form)


    def form_invalid(self, form):
        '''
        :param self:
        :param form: erro no form
        :return: retorna o erro no cadastro
        '''
        print(form.errors)
        return super(PropriedadeCreateView, self).form_invalid(form)

