#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
import base64


@login_required
def desvincular_eventos_efdreinf(request, hash):

    from django.db import connections
    
    try:
        
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        evento_identidade = dict_hash['id']
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
            
    except:
        
        usuario_id = False
        return redirect('login')
    
    if evento_identidade:
        
        a = TransmissorEventosEfdreinf.objects.get(identidade=evento_identidade)
        cursor = connections['default'].cursor()
        cursor.execute("UPDATE %s SET transmissor_lote_efdreinf_id=Null WHERE id=%s" % (a.tabela, a.id) )
        messages.success(request, 'Evento desvinculado com sucesso!')

    else:

        messages.error(request, 'Erro ao desvincular evento!')

    return redirect('transmissor_lote_efdreinf_salvar', hash=dict_hash['return_hash'])


@login_required
def vincular_eventos_efdreinf(request, hash):

    from django.db import connections

    try:

        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        transmissor_lote_efdreinf_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''

    except:

        usuario_id = False
        return redirect('login')

    if transmissor_lote_efdreinf_id:

        transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf,
                                             id=transmissor_lote_efdreinf_id)

        transmissor_eventos_efdreinf_vinculados_lista = TransmissorEventosEfdreinf.objects.\
            filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id).all()

        quant = 50 - transmissor_eventos_efdreinf_vinculados_lista.count()

        transmissor_eventos_efdreinf_lista = TransmissorEventosEfdreinf.objects.\
            filter(transmissor_lote_efdreinf__isnull=True,
                  grupo = transmissor_lote_efdreinf.grupo ).all()[:quant]

        n = 0
        for a in transmissor_eventos_efdreinf_lista:

            cursor = connections['default'].cursor()
            cursor.execute("UPDATE %s SET transmissor_lote_efdreinf_id=%s WHERE id=%s" % (a.tabela, transmissor_lote_efdreinf_id, a.id) )
            n+=1

        messages.success(request, '%s eventos foram vinculados com sucesso a este transmissor!' % n)

    else:

        messages.error(request, 'Erro ao vincular eventos!')

    return redirect('transmissor_lote_efdreinf_salvar', hash=dict_hash['return_hash'])