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
def listar(request):

    from emensageriapro.mensageiro.views.processar_arquivos import create_import_dirs
    create_import_dirs()

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
        STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
        STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
        STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
        STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
        STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
        STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO

    from emensageriapro.mapa_processamento.views.mapa_importacoes import STATUS_IMPORT_AGUARDANDO, \
        STATUS_IMPORT_PROCESSANDO, STATUS_IMPORT_PROCESSADO, \
        STATUS_IMPORT_ERRO_PROCESSAMENTO, STATUS_IMPORT_ERRO_OUTROS, \
        STATUS_IMPORT_ERRO_ARQUIVO_INVALIDO, STATUS_IMPORT_ERRO_IDENTIDADE_EXISTENTE, \
        STATUS_IMPORT_ERRO_VERSAO_LEIAUTE, STATUS_IMPORT_ERRO_VALIDACAO_LEIAUTE \

    status_erros = [
        STATUS_IMPORT_ERRO_PROCESSAMENTO,
        STATUS_IMPORT_ERRO_OUTROS,
        STATUS_IMPORT_ERRO_ARQUIVO_INVALIDO,
        STATUS_IMPORT_ERRO_IDENTIDADE_EXISTENTE,
        STATUS_IMPORT_ERRO_VERSAO_LEIAUTE,
        STATUS_IMPORT_ERRO_VALIDACAO_LEIAUTE,
    ]

    if True:

        esocial_enviados = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_ENVIADO).exclude(id=0).all()

        esocial_validados = TransmissorEventosEsocial.objects.\
            filter(status__in=[STATUS_EVENTO_AGUARD_ENVIO,
                               STATUS_EVENTO_AGUARD_PRECEDENCIA,
                               STATUS_EVENTO_VALIDADO]).exclude(id=0).all()

        esocial_importados = TransmissorEventosEsocial.objects.\
            filter(status__in=[STATUS_EVENTO_IMPORTADO]).exclude(id=0).all()


        esocial_cadastrados = TransmissorEventosEsocial.objects.\
            filter(status__in=[STATUS_EVENTO_CADASTRADO,
                               STATUS_EVENTO_DUPLICADO,
                               STATUS_EVENTO_GERADO,
                               STATUS_EVENTO_ASSINADO]).exclude(id=0).all()

        esocial_erros_validacao = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_VALIDADO_ERRO).exclude(id=0).all()

        esocial_erros_envio = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_ENVIADO_ERRO).exclude(id=0).all()

        esocial_processados = TransmissorEventosEsocial.objects.\
            filter(status=STATUS_EVENTO_PROCESSADO).exclude(id=0).all()

        esocial_quant_cadastrados = len(esocial_cadastrados) or 0
        esocial_quant_importados = len(esocial_importados) or 0
        esocial_quant_validados = len(esocial_validados) or 0
        esocial_quant_erros_envio = len(esocial_erros_envio) or 0
        esocial_quant_erros_validacao = len(esocial_erros_validacao) or 0
        esocial_quant_enviados = len(esocial_enviados) or 0
        esocial_quant_processados = len(esocial_processados) or 0


        efdreinf_enviados = TransmissorEventosEfdreinf.objects. \
            filter(status=STATUS_EVENTO_ENVIADO).exclude(id=0).all()

        efdreinf_validados = TransmissorEventosEfdreinf.objects. \
            filter(status__in=[STATUS_EVENTO_AGUARD_ENVIO,
                               STATUS_EVENTO_AGUARD_PRECEDENCIA,
                               STATUS_EVENTO_VALIDADO]).exclude(id=0).all()

        efdreinf_importados = TransmissorEventosEfdreinf.objects. \
            filter(status__in=[STATUS_EVENTO_IMPORTADO]).exclude(id=0).all()

        efdreinf_cadastrados = TransmissorEventosEfdreinf.objects. \
            filter(status__in=[STATUS_EVENTO_CADASTRADO,
                               STATUS_EVENTO_DUPLICADO,
                               STATUS_EVENTO_GERADO,
                               STATUS_EVENTO_ASSINADO]).exclude(id=0).all()

        efdreinf_erros_validacao = TransmissorEventosEfdreinf.objects. \
            filter(status=STATUS_EVENTO_VALIDADO_ERRO).exclude(id=0).all()

        efdreinf_erros_envio = TransmissorEventosEfdreinf.objects. \
            filter(status=STATUS_EVENTO_ENVIADO_ERRO).exclude(id=0).all()

        efdreinf_processados = TransmissorEventosEfdreinf.objects. \
            filter(status=STATUS_EVENTO_PROCESSADO).exclude(id=0).all()

        request.session["retorno_pagina"] = 'visao_geral'

        efdreinf_quant_cadastrados = len(efdreinf_cadastrados) or 0
        efdreinf_quant_importados = len(efdreinf_importados) or 0
        efdreinf_quant_validados = len(efdreinf_validados) or 0
        efdreinf_quant_erros_envio = len(efdreinf_erros_envio) or 0
        efdreinf_quant_erros_validacao = len(efdreinf_erros_validacao) or 0
        efdreinf_quant_enviados = len(efdreinf_enviados) or 0
        efdreinf_quant_processados = len(efdreinf_processados) or 0

        lista_aguardando = ImportacaoArquivosEventos.objects.filter(status=STATUS_IMPORT_AGUARDANDO).exclude(id=0).all()
        lista_erros = ImportacaoArquivosEventos.objects.filter(status__in=status_erros).exclude(id=0).all()
        lista_processando = ImportacaoArquivosEventos.objects.filter(status=STATUS_IMPORT_PROCESSANDO).all()
        lista_processados = ImportacaoArquivosEventos.objects.filter(status=STATUS_IMPORT_PROCESSADO).all()

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'esocial_quant_cadastrados': esocial_quant_cadastrados,
            'esocial_quant_importados': esocial_quant_importados,
            'esocial_quant_validados': esocial_quant_validados,
            'esocial_quant_erros_envio': esocial_quant_erros_envio,
            'esocial_quant_erros_validacao': esocial_quant_erros_validacao,
            'esocial_quant_enviados': esocial_quant_enviados,
            'esocial_quant_processados': esocial_quant_processados,
            'efdreinf_quant_cadastrados': efdreinf_quant_cadastrados,
            'efdreinf_quant_importados': efdreinf_quant_importados,
            'efdreinf_quant_validados': efdreinf_quant_validados,
            'efdreinf_quant_erros_envio': efdreinf_quant_erros_envio,
            'efdreinf_quant_erros_validacao': efdreinf_quant_erros_validacao,
            'efdreinf_quant_enviados': efdreinf_quant_enviados,
            'efdreinf_quant_processados': efdreinf_quant_processados,
            'quant_aguardando': len(lista_aguardando),
            'quant_erros': len(lista_erros),
            'quant_processando': len(lista_processando),
            'quant_processados': len(lista_processados),
            'data': datetime.datetime.now(),
            'tab_return': 'mapa_resumo',
            'tab': 'master',
        }

        return render(request, 'visao_geral.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)