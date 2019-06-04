#coding:utf-8
from __future__ import absolute_import, division, print_function, unicode_literals  # isort:skip

from django.contrib import admin
from django.db import transaction
from django.utils import timezone
from emensageriapro.controle_de_acesso.models import Auditoria
from emensageriapro.mensageiro.models import Certificados


class AuditoriaAdmin(admin.ModelAdmin):
    readonly_fields = (
        'criado_em', 
        'criado_por',
        'modificado_em', 
        'modificado_por',
        'excluido',
    )


class CertificadosAdmin(AuditoriaAdmin):

    search_fields = (
        'nome',
    )
    
    list_filter = (
        'nome',
    )
    
    list_display = (
        'nome',
    )

    exclude = (
        'senha',
        'certificado',
    )
    
    def queryset(self, request, queryset):
        return queryset.filter(excluido=False)



admin.site.register(Certificados, CertificadosAdmin)