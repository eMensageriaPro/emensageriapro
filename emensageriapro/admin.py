#coding:utf-8

#from __future__ import absolute_import, division, print_function, unicode_literals

from django.contrib import admin

from django.db import transaction
from django.utils import timezone


from emensageriapro.mensageiro.models import Certificados


class AuditoriaAdmin(admin.ModelAdmin):
    readonly_fields = (
        'criado_em', 
        'criado_por',
        'modificado_em', 
        'modificado_por',
        'excluido',
    )
    
    



class CertificadosAdmin(admin.ModelAdmin):

    search_fields = (
        'arquivo',
    )

    list_filter = (
        'arquivo',
    )

    list_display = (
        'arquivo',
    )

    readonly_fields = (
        'criado_em',
        'criado_por',
        'modificado_em',
        'modificado_por',
        'excluido',
    )

admin.site.register(Certificados, CertificadosAdmin)






from emensageriapro.controle_de_acesso.models import Usuarios
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#
# class UsuariosInline(admin.StackedInline):
#     model = Usuarios
#
#
# class CustomUserAdmin(UserAdmin):
#     inlines = [UsuariosInline]
#     search_fields = (
#         'username',
#         'first_name',
#         'last_name',
#         'email',
#     )
#
#     list_display = UserAdmin.list_display
#     list_filter = UserAdmin.list_filter
#
#
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)

