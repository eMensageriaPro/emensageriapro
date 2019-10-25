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





from emensageriapro.mensageiro.models import Certificados

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

    def queryset(self, request, queryset):
        return queryset.filter(ativo=True)

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.exclude = ('certificado', 'senha')
        else:
            self.exclude = ()
        form = super(CertificadosAdmin, self).get_form(request, obj, **kwargs)
        return form



admin.site.register(Certificados, CertificadosAdmin)