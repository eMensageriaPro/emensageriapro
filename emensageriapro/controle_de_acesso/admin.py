#coding:utf-8
from __future__ import absolute_import, division, print_function, unicode_literals  # isort:skip

from django.contrib import admin
from django.db import transaction
from django.utils import timezone


from emensageriapro.controle_de_acesso.models import ConfigModulos
from emensageriapro.controle_de_acesso.models import ConfigPaginas
from emensageriapro.controle_de_acesso.models import ConfigPerfis
from emensageriapro.controle_de_acesso.models import ConfigPermissoes
from emensageriapro.controle_de_acesso.models import Auditoria


class AuditoriaAdmin(admin.ModelAdmin):
    readonly_fields = (
        'criado_em', 
        'criado_por',
        'modificado_em', 
        'modificado_por',
        'excluido',
    )
    
    



class ConfigModulosAdmin(AuditoriaAdmin):

    search_fields = (
        'titulo',
        'slug',
    )
    
    list_filter = (
        'titulo',
        'slug',
    )
    
    list_display = (
        'titulo',
        'slug',
    )
    
    def queryset(self, request, queryset):
        return queryset.filter(excluido=False)


class ConfigPaginasAdmin(AuditoriaAdmin):

    search_fields = (
        'config_modulos',
        'titulo',
        'endereco',
        'exibe_menu',
        'tipo',
    )
    
    list_filter = (
        'config_modulos',
        'titulo',
        'endereco',
        'exibe_menu',
        'tipo',
    )
    
    list_display = (
        'config_modulos',
        'titulo',
        'endereco',
        'exibe_menu',
    )
    
    def queryset(self, request, queryset):
        return queryset.filter(excluido=False)


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


class ConfigPermissoesAdmin(AuditoriaAdmin):

    search_fields = (
        'config_perfis',
        'config_paginas',
    )
    
    list_filter = (
        'config_perfis',
        'config_paginas',
    )
    
    list_display = (
        'config_perfis',
        'config_paginas',
    )
    
    def queryset(self, request, queryset):
        return queryset.filter(excluido=False)


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
    
    def queryset(self, request, queryset):
        return queryset.filter(excluido=False)



admin.site.register(ConfigModulos, ConfigModulosAdmin)
admin.site.register(ConfigPaginas, ConfigPaginasAdmin)
admin.site.register(ConfigPerfis, ConfigPerfisAdmin)
admin.site.register(ConfigPermissoes, ConfigPermissoesAdmin)
admin.site.register(Auditoria, AuditoriaAdmin)


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