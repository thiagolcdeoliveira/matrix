from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from appusuario.models.email import Email
from appusuario.models.instituicao import Instituicao
from appusuario.models.complemento_usuario import ComplementoUsuario


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_groups(self):
        convidado = Group(name='convidado', )
        convidado.save()
        admin = Group(name='admin', )
        admin.save()

    def _create_admin(self):
        admin = User(username='admin',
                     email='admin@admin.com',
                     first_name='Admin',
                     last_name='Administrador',
                     is_staff=True,
                     is_active=True,
                     is_superuser=True, )
        admin.set_password('admin')
        admin.save()

    def _create_user(self):
        user = User(username='jhon@snow.com',
                    email='jhon@snow.com',
                    first_name='john',
                    last_name='Snow')
        user.set_password('jhonsnow')
        user.save()

    def _create_email(self):
        email = Email(email='email@exemplo.com')
        email.save()

    def _create_instituicao(self):
        instituicao = Instituicao(nome='IFC')
        instituicao.save()
        instituicao1 = Instituicao(nome='UFSC')
        instituicao1.save()

    def _create_usuario(self):
        usuario = ComplementoUsuario(user_id=User.objects.get(username='admin'),
                                     lista_email=Email.objects.get(pk=1),
                                     instituicao=Instituicao.objects.get(pk=1), )
        usuario.save()

    def handle(self, *args, **options):
        self._create_groups()
        self._create_admin()
        self._create_user()
        # self._create_email()
        # self._create_instituicao()
        # self._create_usuario()
