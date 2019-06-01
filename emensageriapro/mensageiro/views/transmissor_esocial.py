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
def desvincular_eventos_esocial(request, hash):

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

        a = TransmissorEventosEsocial.get(iddentidade=evento_identidade)
        from django.db import connections
        cursor = connections[db_slug].cursor()
        cursor.execute("UPDATE %s SET transmissor_lote_esocial_id=Null WHERE id=%s" % (a.tabela, a.id) )
        messages.success(request, 'Evento desvinculado com sucesso!')

    else:

        messages.error(request, 'Erro ao desvincular evento!')

    return redirect('transmissor_lote_esocial_salvar', hash=dict_hash['return_hash'])


@login_required
def vincular_eventos_esocial(request, hash):
    
    try:
        
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        transmissor_lote_esocial_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
            
    except:
        
        usuario_id = False
        return redirect('login')
    
    if transmissor_lote_esocial_id:
        transmissor_lote_esocial = get_object_or_404(
            TransmissorLoteEsocial,
            
            id=transmissor_lote_esocial_id)
        transmissor_eventos_esocial_vinculados_lista = TransmissorEventosEsocial.objects.\
            filter(transmissor_lote_esocial_id=transmissor_lote_esocial_id).all()

        quant = 50 - transmissor_eventos_esocial_vinculados_lista.count()

        transmissor_eventos_esocial_lista = TransmissorEventosEsocial.objects.\
            filter(transmissor_lote_esocial__isnull=True, grupo=transmissor_lote_esocial.grupo).all()[:quant]

        from django.db import connections

        n = 0

        for a in transmissor_eventos_esocial_lista:

            cursor = connections['default'].cursor()
            cursor.execute("UPDATE %s SET transmissor_lote_esocial_id=%s WHERE id=%s" % (a.tabela, transmissor_lote_esocial_id, a.id) )
            n+=1

        messages.success(request, '%s eventos foram vinculados com sucesso a este transmissor!' % n)

    else:

        messages.error(request, 'Erro ao vincular eventos!')

    return redirect('transmissor_lote_esocial_salvar', hash=dict_hash['return_hash'])