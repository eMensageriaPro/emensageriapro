#coding:utf-8
from __future__ import absolute_import, division, print_function, unicode_literals  # isort:skip

from django.contrib import admin
from django.db import transaction
from django.utils import timezone


from emensageriapro.tabelas.models import Opcoes


class AuditoriaAdmin(admin.ModelAdmin):
    readonly_fields = (
        'criado_em', 
        'criado_por',
        'modificado_em', 
        'modificado_por',
        'excluido',
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
    
    def queryset(self, request, queryset):
        return queryset.filter(excluido=False)



admin.site.register(Opcoes, OpcoesAdmin)