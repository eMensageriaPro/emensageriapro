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
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES





@login_required
def listar(request, hash):
    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
        STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
        STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
        STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
        STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
        STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
        STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO
    for_print = 0
    db_slug = 'default'
    from emensageriapro.controle_de_acesso.views.login import criar_permissoes, salvar_modulos_paginas_permitidas
    criar_permissoes(db_slug)
    salvar_modulos_paginas_permitidas(db_slug)
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='mapa_efdreinf')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:

        esocial_enviados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_ENVIADO).exclude(id=0).all()

        esocial_validados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status__in=[STATUS_EVENTO_AGUARD_ENVIO,
                               STATUS_EVENTO_AGUARD_PRECEDENCIA,
                               STATUS_EVENTO_VALIDADO]).exclude(id=0).all()

        esocial_importados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status__in=[STATUS_EVENTO_IMPORTADO]).exclude(id=0).all()


        esocial_cadastrados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status__in=[STATUS_EVENTO_CADASTRADO,
                               STATUS_EVENTO_DUPLICADO,
                               STATUS_EVENTO_GERADO,
                               STATUS_EVENTO_ASSINADO]).exclude(id=0).all()

        esocial_erros_validacao = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_VALIDADO_ERRO).exclude(id=0).all()

        esocial_erros_envio = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_ENVIADO_ERRO).exclude(id=0).all()

        esocial_processados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False,
                   status=STATUS_EVENTO_PROCESSADO).exclude(id=0).all()

        esocial_quant_cadastrados = len(esocial_cadastrados) or 0
        esocial_quant_importados = len(esocial_importados) or 0
        esocial_quant_validados = len(esocial_validados) or 0
        esocial_quant_erros = len(esocial_erros_envio) or 0
        esocial_quant_erros += len(esocial_erros_validacao) or 0
        esocial_quant_enviados = len(esocial_enviados) or 0
        esocial_quant_processados = len(esocial_processados) or 0


        efdreinf_enviados = TransmissorEventosEfdreinf.objects.using(db_slug). \
            filter(excluido=False,
                   status=STATUS_EVENTO_ENVIADO).exclude(id=0).all()

        efdreinf_validados = TransmissorEventosEfdreinf.objects.using(db_slug). \
            filter(excluido=False,
                   status__in=[STATUS_EVENTO_AGUARD_ENVIO,
                               STATUS_EVENTO_AGUARD_PRECEDENCIA,
                               STATUS_EVENTO_VALIDADO]).exclude(id=0).all()

        efdreinf_importados = TransmissorEventosEfdreinf.objects.using(db_slug). \
            filter(excluido=False,
                   status__in=[STATUS_EVENTO_IMPORTADO]).exclude(id=0).all()

        efdreinf_cadastrados = TransmissorEventosEfdreinf.objects.using(db_slug). \
            filter(excluido=False,
                   status__in=[STATUS_EVENTO_CADASTRADO,
                               STATUS_EVENTO_DUPLICADO,
                               STATUS_EVENTO_GERADO,
                               STATUS_EVENTO_ASSINADO]).exclude(id=0).all()

        efdreinf_erros_validacao = TransmissorEventosEfdreinf.objects.using(db_slug). \
            filter(excluido=False,
                   status=STATUS_EVENTO_VALIDADO_ERRO).exclude(id=0).all()

        efdreinf_erros_envio = TransmissorEventosEfdreinf.objects.using(db_slug). \
            filter(excluido=False,
                   status=STATUS_EVENTO_ENVIADO_ERRO).exclude(id=0).all()

        efdreinf_processados = TransmissorEventosEfdreinf.objects.using(db_slug). \
            filter(excluido=False,
                   status=STATUS_EVENTO_PROCESSADO).exclude(id=0).all()

        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'visao_geral'

        efdreinf_quant_cadastrados = len(efdreinf_cadastrados) or 0
        efdreinf_quant_importados = len(efdreinf_importados) or 0
        efdreinf_quant_validados = len(efdreinf_validados) or 0
        efdreinf_quant_erros = len(efdreinf_erros_envio) or 0
        efdreinf_quant_erros += len(efdreinf_erros_validacao) or 0
        efdreinf_quant_enviados = len(efdreinf_enviados) or 0
        efdreinf_quant_processados = len(efdreinf_processados) or 0

        context = {

            'tab': dict_hash['tab'],

            'esocial_quant_cadastrados': esocial_quant_cadastrados,
            'esocial_quant_importados': esocial_quant_importados,
            'esocial_quant_validados': esocial_quant_validados,
            'esocial_quant_erros': esocial_quant_erros,
            'esocial_quant_enviados': esocial_quant_enviados,
            'esocial_quant_processados': esocial_quant_processados,

            'efdreinf_quant_cadastrados': efdreinf_quant_cadastrados,
            'efdreinf_quant_importados': efdreinf_quant_importados,
            'efdreinf_quant_validados': efdreinf_quant_validados,
            'efdreinf_quant_erros': efdreinf_quant_erros,
            'efdreinf_quant_enviados': efdreinf_quant_enviados,
            'efdreinf_quant_processados': efdreinf_quant_processados,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            #'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            #'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            #'filtrar': filtrar,

        }
        return render(request, 'visao_geral.html', context)
    else:
        context = {
            'usuario': usuario,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)