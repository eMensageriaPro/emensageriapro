#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from emensageriapro.mensageiro.models import *


@login_required
def vincular_eventos_esocial(request, pk):

    from django.db import connections

    transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial, id=pk)

    transmissor_eventos_esocial_vinculados_lista = TransmissorEventosEsocial.objects.\
        filter(transmissor_lote_esocial_id=pk).all()

    quant = 50 - transmissor_eventos_esocial_vinculados_lista.count()

    transmissor_eventos_esocial_lista = TransmissorEventosEsocial.objects.\
        filter(transmissor_lote_esocial__isnull=True,
               grupo=transmissor_lote_esocial.grupo).all()[:quant]

    n = 0

    for a in transmissor_eventos_esocial_lista:

        cursor = connections['default'].cursor()
        cursor.execute("UPDATE %s SET transmissor_lote_esocial_id=%s WHERE id=%s" % (a.tabela, pk, a.id))
        n += 1

    messages.success(request, '%s eventos foram vinculados com sucesso a este transmissor!' % n)

    return redirect('transmissor_lote_esocial_salvar_tab', pk=pk, tab='transmissor_eventos_esocial')
