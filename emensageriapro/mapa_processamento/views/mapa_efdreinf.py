#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def listar(request, tab='master', output=None):

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
        quant_erros_envio = len(efdreinf_erros_envio) or 0
        quant_erros_validacao = len(efdreinf_erros_validacao) or 0
        quant_enviados = len(efdreinf_enviados) or 0
        quant_processados = len(efdreinf_processados) or 0

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'tab': tab,
            'output': output,
            'efdreinf_enviados': efdreinf_enviados,
            'efdreinf_validados': efdreinf_validados,
            'efdreinf_erros_validacao': efdreinf_erros_validacao,
            'efdreinf_importados': efdreinf_importados,
            'efdreinf_cadastrados': efdreinf_cadastrados,
            'efdreinf_erros_envio': efdreinf_erros_envio,
            'efdreinf_processados': efdreinf_processados,
            'efdreinf_quant_cadastrados': quant_cadastrados,
            'efdreinf_quant_importados': quant_importados,
            'efdreinf_quant_validados': quant_validados,
            'efdreinf_quant_erros_envio': quant_erros_envio,
            'efdreinf_quant_erros_validacao': quant_erros_validacao,
            'efdreinf_quant_enviados': quant_enviados,
            'efdreinf_quant_processados': quant_processados,
            'data': datetime.datetime.now(),
            'tab_return': 'mapa',
        }
        if output == 'pdf':
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='mapa_efdreinf.html',
                filename="mapa_efdreinf.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             'viewport-size': "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response

        elif output == 'xls':
            response = render_to_response('mapa_efdreinf.html', context)
            filename = "mapa_importacoes.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif output == 'csv':
            response = render_to_response('csv/mapa_efdreinf.csv', context)
            filename = "mapa_importacoes.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        elif output == 'html':
            return render(request, 'mapa_efdreinf.html', context)

        else:
            return render(request, 'mapa_efdreinf.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)