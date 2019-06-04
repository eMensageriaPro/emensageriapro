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
def listar(request, tab='master'):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
        STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
        STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
        STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
        STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
        STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
        STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO

    if True:

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

        quant_cadastrados = len(efdreinf_cadastrados) or 0
        quant_importados = len(efdreinf_importados) or 0
        quant_validados = len(efdreinf_validados) or 0
        quant_erros = len(efdreinf_erros_envio) or 0
        quant_erros += len(efdreinf_erros_validacao) or 0
        quant_enviados = len(efdreinf_enviados) or 0
        quant_processados = len(efdreinf_processados) or 0

        context = {

            'tab': tab,
            'efdreinf_enviados': efdreinf_enviados,
            'efdreinf_validados': efdreinf_validados,
            'efdreinf_erros_validacao': efdreinf_erros_validacao,
            'efdreinf_importados': efdreinf_importados,
            'efdreinf_cadastrados': efdreinf_cadastrados,
            'efdreinf_erros_envio': efdreinf_erros_envio,
            'efdreinf_processados': efdreinf_processados,

            'quant_cadastrados': quant_cadastrados,
            'quant_importados': quant_importados,
            'quant_validados': quant_validados,
            'quant_erros': quant_erros,
            'quant_enviados': quant_enviados,
            'quant_processados': quant_processados,
            'data': datetime.datetime.now(),
        }

        return render(request, 'mapa_efdreinf.html', context)

    else:

        context = {
            'usuario': usuario,
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)