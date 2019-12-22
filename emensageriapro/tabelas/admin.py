# eMensageriaAI #
#coding:utf-8
from __future__ import absolute_import, division, print_function, unicode_literals  # isort:skip

from django.contrib import admin
from django.db import transaction
from django.utils import timezone
from emensageriapro.controle_de_acesso.models import Auditoria


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





class OpcoesAdmin(AuditoriaAdmin):

    search_fields = (
        'opcoes_slug',
        'opcoes_id',
        'codigo',
        'titulo',
        'descricao',
        'data_inicio',
        'data_termino',
    )

    list_filter = (
        'opcoes_slug',
        'opcoes_id',
        'codigo',
        'titulo',
        'descricao',
        'data_inicio',
        'data_termino',
    )

    list_display = (
        'opcoes_slug',
        'opcoes_id',
        'codigo',
        'titulo',
        'descricao',
        'data_inicio',
        'data_termino',
    )

    readonly_fields = (
        'opcoes_slug',
        'opcoes_id',
        'codigo',
        'titulo',
        'descricao',
        'data_inicio',
        'data_termino',
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

from emensageriapro.tabelas.models import Opcoes
admin.site.register(Opcoes, OpcoesAdmin)