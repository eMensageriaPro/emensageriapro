#coding:utf-8
from __future__ import absolute_import, division, print_function, unicode_literals  # isort:skip

from django.contrib import admin
from django.db import transaction
from django.utils import timezone
from emensageriapro.controle_de_acesso.models import Auditoria
from emensageriapro.controle_de_acesso.models import ConfigPerfis


class AuditoriaAdmin(admin.ModelAdmin):
    readonly_fields = (
        'criado_em', 
        'criado_por',
        'modificado_em', 
        'modificado_por',
        'excluido',
    )


class ConfigPerfisAdmin(AuditoriaAdmin):

    search_fields = (
        'titulo',
    )
    
    list_filter = (
        'titulo',
    )
    
    list_display = (
        'titulo',
    )
    
    def queryset(self, request, queryset):
        return queryset.filter(excluido=False)



admin.site.register(ConfigPerfis, ConfigPerfisAdmin)


from emensageriapro.controle_de_acesso.models import Usuarios
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UsuariosInline(admin.StackedInline):

    model = Usuarios
    fk_name = "user"
    readonly_fields = (
        'criado_em',
        'criado_por',
        'modificado_em',
        'modificado_por',
        'excluido',
    )


class CustomUserAdmin(UserAdmin):

    inlines = [UsuariosInline]
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email',
    )
    list_display = UserAdmin.list_display
    list_filter = UserAdmin.list_filter


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class AuditoriaAdmin(AuditoriaAdmin):

    search_fields = (
        'tabela',
        'identidade',
    )
    
    list_filter = (
        'tabela',
        'identidade',
    )
    
    list_display = (
        'tabela',
        'identidade',
        'situacao_anterior',
        'situacao_posterior',
        'operador',
        'data_hora',
        'tipo',
    )

    readonly_fields = (
        'tabela',
        'identidade',
        'situacao_anterior',
        'situacao_posterior',
        'operador',
        'data_hora',
        'tipo',
        'criado_em',
        'criado_por',
        'modificado_em',
        'modificado_por',
        'excluido',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def queryset(self, request, queryset):
        return queryset.filter(excluido=False)

admin.site.register(Auditoria, AuditoriaAdmin)