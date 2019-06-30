#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response

from emensageriapro.controle_de_acesso.models import *
from emensageriapro.mensageiro.models import *
from emensageriapro.padrao import *


#IMPORTACOES





@login_required
def listar(request, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
        STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
        STATUS_EVENTO_ASSINADO, \
        STATUS_EVENTO_VALIDADO, \
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
        quant_erros_envio = len(esocial_erros_envio) or 0
        quant_erros_validacao = len(esocial_erros_validacao) or 0
        quant_enviados = len(esocial_enviados) or 0
        quant_processados = len(esocial_processados) or 0

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'tab': tab,
            'output': output,
            'esocial_enviados': esocial_enviados,
            'esocial_validados': esocial_validados,
            'esocial_erros_validacao': esocial_erros_validacao,
            'esocial_importados': esocial_importados,
            'esocial_cadastrados': esocial_cadastrados,
            'esocial_erros_envio': esocial_erros_envio,
            'esocial_processados': esocial_processados,
            'esocial_quant_cadastrados': quant_cadastrados,
            'esocial_quant_importados': quant_importados,
            'esocial_quant_validados': quant_validados,
            'esocial_quant_erros_validacao': quant_erros_validacao,
            'esocial_quant_erros_envio': quant_erros_envio,
            'esocial_quant_enviados': quant_enviados,
            'esocial_quant_processados': quant_processados,
            'data': datetime.datetime.now(),
            'tab_return': 'mapa',
        }

        if output == 'pdf':
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='mapa_esocial.html',
                filename="mapa_esocial.pdf",
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
            response = render_to_response('mapa_esocial.html', context)
            filename = "mapa_importacoes.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif output == 'csv':
            response = render_to_response('csv/mapa_esocial.csv', context)
            filename = "mapa_importacoes.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        elif output == 'html':
            return render(request, 'mapa_esocial.html', context)

        else:
            return render(request, 'mapa_esocial.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)