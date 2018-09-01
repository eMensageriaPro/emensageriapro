#coding: utf-8

import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64


def desvincular_eventos_esocial(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        evento_identidade = dict_hash['id']
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    if evento_identidade:
        a = TransmissorEventosEsocial.objects.using(db_slug).get(identidade=evento_identidade)
        from django.db import connections
        cursor = connections[db_slug].cursor()
        cursor.execute("UPDATE %s SET transmissor_lote_esocial_id=Null WHERE id=%s" % (a.tabela, a.id) )
        messages.success(request, 'Evento desvinculado com sucesso!')
    else:
        messages.error(request, 'Erro ao desvincular evento!')
    return redirect('transmissor_lote_esocial_salvar', hash=dict_hash['return_hash'])


def vincular_eventos_esocial_transmissor(transmissor_lote_esocial_id):
    db_slug='default'
    transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial.objects.using(db_slug), excluido=False,
                                                 id=transmissor_lote_esocial_id)
    transmissor_eventos_esocial_vinculados_lista = TransmissorEventosEsocial.objects.using(db_slug).filter(
                                                            excluido=False,
                                                            transmissor_lote_esocial_id=transmissor_lote_esocial_id).all()
    quant = transmissor_lote_esocial.transmissor.esocial_lote_max - transmissor_eventos_esocial_vinculados_lista.count()
    if quant < 0: quant = 0
    transmissor_eventos_esocial_lista = TransmissorEventosEsocial.objects.using(db_slug).filter(excluido=False,
                                                                                                transmissor_lote_esocial__isnull=True,
                                                                                                grupo=transmissor_lote_esocial.grupo,
                                                                                                status=4,
                                                                                                validacao_precedencia=1
                                                                                                ).all()[:quant]
    from django.db import connections
    n = 0
    for a in transmissor_eventos_esocial_lista:
        cursor = connections[db_slug].cursor()
        cursor.execute(
            "UPDATE %s SET transmissor_lote_esocial_id=%s WHERE id=%s" % (a.tabela, transmissor_lote_esocial_id, a.id))
        n += 1
    return n


def vincular_eventos_esocial(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissor_lote_esocial_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    if transmissor_lote_esocial_id:
        n = vincular_eventos_esocial_transmissor(transmissor_lote_esocial_id)
        messages.success(request, '%s eventos foram vinculados com sucesso a este transmissor!' % n)
    else:
        messages.error(request, 'Erro ao vincular eventos!')
    return redirect('transmissor_lote_esocial_salvar', hash=dict_hash['return_hash'])