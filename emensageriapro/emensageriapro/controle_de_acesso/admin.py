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
        'desativado_em',
        'desativado_por',
        'ativo',
    )


def update_auth_user_groups_profile(modeladmin, request, queryset):
    from emensageriapro.controle_de_acesso.models import Usuarios
    for config in queryset:
        users = Usuarios.objects.filter(config_perfis=config).all()
        for u in users:
            update_user(u.user)


class ConfigPerfisAdmin(AuditoriaAdmin):

    actions = [update_auth_user_groups_profile]

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
        return queryset.filter(ativo=True)



admin.site.register(ConfigPerfis, ConfigPerfisAdmin)


from emensageriapro.controle_de_acesso.models import Usuarios
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


def update_user(user):
    from emensageriapro.controle_de_acesso.models import UserGroups, ConfigPerfis, PerfilGroups, Usuarios
    usuario = Usuarios.objects.get(user=user)
    list = PerfilGroups.objects.filter(configperfis_id=usuario.config_perfis_id).all()
    pgl = []
    for l in list:
        pgl.append(l.group_id)
    UserGroups.objects.filter(user_id=user.id).exclude(group_id__in=pgl).delete()
    for l in list:
        a = UserGroups.objects.filter(user_id=user.id, group_id=l.group_id).all()
        if not a:
            UserGroups.objects.create(user_id=user.id, group_id=l.group_id)


def update_auth_user_groups(modeladmin, request, queryset):
    for user in queryset:
        update_user(user)


update_auth_user_groups.short_description = "Atualizar Grupos de Permissões"


class UsuariosInline(admin.StackedInline):

    model = Usuarios
    fk_name = "user"
    readonly_fields = (
        'criado_em',
        'criado_por',
        'modificado_em',
        'modificado_por',
        'desativado_em',
        'desativado_por',
        'ativo',
    )


class CustomUserAdmin(UserAdmin):

    inlines = [UsuariosInline]
    search_fields = (
        'username',
        'name',
        'first_name',
        'last_name',
        'email',
    )
    list_display = UserAdmin.list_display
    list_filter = UserAdmin.list_filter
    actions = [update_auth_user_groups]


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
        'desativado_em',
        'desativado_por',
        'ativo',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def queryset(self, request, queryset):
        return queryset.filter(ativo=True)

admin.site.register(Auditoria, AuditoriaAdmin)