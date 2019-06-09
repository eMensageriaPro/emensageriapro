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

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
        STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
        STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
        STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
        STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
        STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
        STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO

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

        quant_cadastrados = len(esocial_cadastrados) or 0
        quant_importados = len(esocial_importados) or 0
        quant_validados = len(esocial_validados) or 0
        quant_erros = len(esocial_erros_envio) or 0
        quant_erros += len(esocial_erros_validacao) or 0
        quant_enviados = len(esocial_enviados) or 0
        quant_processados = len(esocial_processados) or 0

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'tab': tab,
            'esocial_enviados': esocial_enviados,
            'esocial_validados': esocial_validados,
            'esocial_erros_validacao': esocial_erros_validacao,
            'esocial_importados': esocial_importados,
            'esocial_cadastrados': esocial_cadastrados,
            'esocial_erros_envio': esocial_erros_envio,
            'esocial_processados': esocial_processados,
            'quant_cadastrados': quant_cadastrados,
            'quant_importados': quant_importados,
            'quant_validados': quant_validados,
            'quant_erros': quant_erros,
            'quant_enviados': quant_enviados,
            'quant_processados': quant_processados,
            'data': datetime.datetime.now(),
        }

        return render(request, 'mapa_esocial.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)