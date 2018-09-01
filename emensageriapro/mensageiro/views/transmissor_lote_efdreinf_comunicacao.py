#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.funcoes_efdreinf import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas


#IMPORTACOES

config = True


def enviar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissor_lote_efdreinf_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_efdreinf')
    transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf.objects.using(db_slug), excluido=False, id=transmissor_lote_efdreinf_id)
    if config:
        a = send_xml(request, transmissor_lote_efdreinf_id, 'RecepcaoLoteReinf')
    else:
        messages.error(request, 'Configure o certificado digital para o envio de eventos!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])


def consultar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        transmissor_lote_efdreinf_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='transmissor_lote_efdreinf')
    transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf.objects.using(db_slug), excluido=False, id=transmissor_lote_efdreinf_id)
    if config:
        a = send_xml(request, transmissor_lote_efdreinf_id, 'ConsultasReinf')
    else:
        messages.error(request, 'Configure o certificado digital para a consulta de eventoss!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])


def recibo(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        transmissor_lote_efdreinf_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='transmissor_lote_efdreinf')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf.objects.using(db_slug), excluido=False, id=transmissor_lote_efdreinf_id)
    ocorrencias_lista = TransmissorLoteEfdreinfOcorrencias.objects.using( db_slug ).filter(excluido = False, transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()
    eventos_lista = TransmissorEventosEfdreinf.objects.using( db_slug ).filter(excluido = False, transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

    context = {
        'eventos_lista': eventos_lista,
        'ocorrencias_lista': ocorrencias_lista,
        'transmissor_lote_efdreinf': transmissor_lote_efdreinf,
        'transmissor_lote_efdreinf_id': int(transmissor_lote_efdreinf_id),
        'usuario': usuario,

        'hash': hash,
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'for_print': int(dict_hash['print']),
        #'transmissor_eventos_lista': transmissor_eventos_lista,
        #'transmissor_ocorrencias_lista': transmissor_ocorrencias_lista,
    }
    if for_print in (0, 1):
        return render(request, 'transmissor_lote_efdreinf_recibo.html', context)
    elif for_print == 2:
        from wkhtmltopdf.views import PDFTemplateResponse
        response = PDFTemplateResponse(
            request=request,
            template='transmissor_lote_efdreinf_recibo.html',
            filename="transmissor_lote_efdreinf_recibo.pdf",
            context=context,
            show_content_in_browser=True,
            cmd_options={'margin-top': 10,
                         'margin-bottom': 10,
                         'margin-right': 10,
                         'margin-left': 10,
                         "zoom": 1,
                         "viewport-size": "1366 x 513",
                         'javascript-delay': 1000,
                         'footer-center': '[page]/[topage]',
                         "no-stop-slow-scripts": True},
        )
        return response
    elif for_print == 3:
        from django.shortcuts import render_to_response
        response = render_to_response('transmissor_lote_efdreinf_recibo.html', context)
        filename = "transmissor_lote_efdreinf_recibo.xls"
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
        return response
    elif for_print == 4:
        from django.shortcuts import render_to_response
        response = render_to_response('transmissor_lote_efdreinf_recibo_csv.html', context)
        filename = "transmissor_lote_efdreinf_recibo.csv"
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Type'] = 'text/csv; charset=UTF-8'
        return response



def scripts_enviar_lote(request, chave, transmissor_lote_efdreinf_id):
    from emensageriapro.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf.objects.using(db_slug), excluido=False, id=transmissor_lote_efdreinf_id)
        a = send_xml(transmissor_lote_efdreinf_id, 'WsEnviarLoteEventos', transmissor_lote_efdreinf.tipo)
        if 'HTTP/1.1 200 OK' in a:
            mensagem = 'Lote enviado com sucesso!'
        else:
            mensagem = 'Erro no envio do Lote de Eventos! %s' % a
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


def scripts_consultar_lote(request, chave, transmissor_lote_efdreinf_id):
    from emensageriapro.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf.objects.using(db_slug), excluido=False, id=transmissor_lote_efdreinf_id)
        a = send_xml(transmissor_lote_efdreinf_id, 'WsConsultarLoteEventos', transmissor_lote_efdreinf.tipo)
        if 'HTTP/1.1 200 OK' in a:
            mensagem = 'Lote consultado com sucesso!'
        else:
            mensagem = 'Erro na consulta do Lote de Eventos! %s' % a
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)