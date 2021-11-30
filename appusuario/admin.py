from django.contrib.auth.models import User
from django.contrib.gis.geoip2 import resources

from appusuario.models import ComplementoUsuario\
    # , Email, Instituicao
from django.contrib import admin
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

#
# class ComplementoUsuarioResource(resources.ModelResource):
#
#     class Meta:
#         model = ComplementoUsuario
#
#
# class EmailResource(resources.ModelResource):
#
#     class Meta:
#         model = Email
#
#
# class InstituicaoResource(resources.ModelResource):
#
#     class Meta:
#         model = Instituicao

#
# class UserResource(resources.ModelResource):
#
#     class Meta:
#         model = User


# class ComplementoUsuarioAdmin(ImportExportModelAdmin):
# class ComplementoUsuarioAdmin():
#     list_display = (
#         'id',
#         'user_id',
#     )
#     list_display_links = (
#         'id',
#         'user_id',
#     )
#     search_fields = (
#         'id',
#         'user_id',
#         'instituicao',
#     )
#     empty_value_display = '-vazio-'
#
#
# # class EmailAdmin(ImportExportModelAdmin):
# class EmailAdmin():
#     list_display = (
#         'id',
#         'email',
#     )
#     list_display_links = (
#         'id',
#         'email',
#     )
#     search_fields = (
#         'id',
#         'email',
#     )
#     empty_value_display = '-vazio-'
#
#
# # class InstituicaoAdmin(ImportExportModelAdmin):
# class InstituicaoAdmin():
#     list_display = (
#         'id',
#         'nome',
#     )
#     list_display_links = (
#         'id',
#         'nome',
#     )
#     search_fields = (
#         'id',
#         'nome',
#     )
#     empty_value_display = '-vazio-'
#
#
# # class UserAdmin(ImportExportModelAdmin):
# class UserAdmin():
#     list_display = (
#         'id',
#         'username',
#         'first_name',
#         'last_name',
#     )
#     list_display_links = (
#         'id',
#         'username',
#         'first_name',
#         'last_name',
#     )
#     search_fields = (
#         'id',
#         'username',
#         'first_name',
#         'last_name',
#     )
#     empty_value_display = '-vazio-'
#
#
# # Register your models here.
# admin.site.register(ComplementoUsuario, ComplementoUsuarioAdmin)
# # admin.site.register(Email, EmailAdmin)
# # admin.site.register(Instituicao, InstituicaoAdmin)
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(ComplementoUsuario)
# admin.site.register(User)
