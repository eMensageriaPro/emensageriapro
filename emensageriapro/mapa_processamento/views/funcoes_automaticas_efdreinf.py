#coding: utf-8

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



from constance import config
import datetime
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO

#
# Acessando via webservice:
#
# curl -X GET http://localhost:8000/mapa-processamento/esocial-validar/ -H 'Authorization: Token XXXXXXX'
#


def get_grupo(model):

    numero_evento = int(model._meta.db_table[1:5])

    if numero_evento < 1200:
        grupo = 1
    elif numero_evento >= 1200 and numero_evento <= 1300:
        grupo = 2
    else:
        grupo = 3

    return grupo



def criar_transmissor_efdreinf(request, grupo, nrinsc, tpinsc):

    transmissor_efdreinf_lista = TransmissorLoteEfdreinf.objects.filter(
        status=0,
        grupo=grupo,
        contribuinte_nrinsc=nrinsc,
        contribuinte_tpinsc=tpinsc).all()

    txt = ''

    if not transmissor_efdreinf_lista:

        transmissor = TransmissorLote.objects.filter(
            nrinsc=nrinsc,
            tpinsc=tpinsc).all()

        if not transmissor:

            txt = u'Cadastre um Transmissor para o empregador %s!' % nrinsc

            if hash:
                messages.error(request, txt)
                return redirect('mapa_efdreinf', tab='master')
            else:
                data = {'response': txt}
                return Response(data, status=HTTP_200_OK)

        elif len(transmissor) > 1:
            txt = u'Existe mais de um transmissor cadastrado o empregador %s, cadastre apenas um!' % nrinsc

            if hash:
                messages.error(request, txt)
                return redirect('mapa_efdreinf', tab='master')
            else:
                data = {'response': txt}
                return Response(data, status=HTTP_200_OK)

        else:

            dados = {}
            dados['transmissor_id'] = transmissor[0].id
            dados['contribuinte_tpinsc'] = transmissor[0].tpinsc
            dados['contribuinte_nrinsc'] = transmissor[0].nrinsc
            dados['grupo'] = grupo
            dados['status'] = 0
            transmissor_efdreinf = TransmissorLoteEfdreinf(**dados)
            transmissor_efdreinf.save()


def vincular_transmissor_efdreinf(request, grupo, model, a):

    transmissor_efdreinf_lista = TransmissorLoteEfdreinf.objects.filter(
        status=0,
        grupo=grupo,
        contribuinte_nrinsc=a.nrinsc,
        contribuinte_tpinsc=a.tpinsc).all()

    txt = ''

    for te in transmissor_efdreinf_lista:

        eventos_lista = TransmissorEventosEfdreinf.objects.filter(
            transmissor_lote_efdreinf=te.id).all()

        if len(eventos_lista) < config.EFDREINF_LOTE_MAX:
            model.objects.filter(id=a.id).update(transmissor_lote_efdreinf=te)

        txt = 'Evento vinculado com sucesso!'

    return txt



@csrf_exempt
@api_view(["GET"])
def validar(request, tab=None):

    texto = 'Validações processadas com sucesso!'

    from django.apps import apps

    app_models = apps.get_app_config('efdreinf').get_models()

    for model in app_models:

        STATUS = [
            STATUS_EVENTO_IMPORTADO,
        ]

        lista = model.objects.filter(status__in=STATUS).all()

        for a in lista:

            a.validar(request)

    if not tab:

        messages.success(request, texto)
        return redirect(request.session['return_page'])

    elif tab == 'json':

        data = {'response': texto}
        return Response(data, status=HTTP_200_OK)

    elif tab == 'mapa':

        messages.success(request, texto)
        return redirect('mapa_efdreinf', tab='master')

    elif tab == 'mapa_resumo':

        messages.success(request, texto)
        return redirect('visao_geral')

    else:

        data = {'response': u'Página não existe!'}
        return Response(data, status=HTTP_404_NOT_FOUND)





@csrf_exempt
@api_view(["GET"])
def enviar(request, tab=None):

    from emensageriapro.mensageiro.views.transmissor_lote_efdreinf_comunicacao import send_xml
    from django.apps import apps
    from emensageriapro.mensageiro.models import TransmissorLote, TransmissorLoteEfdreinf, TransmissorEventosEfdreinf

    texto = ''

    app_models = apps.get_app_config('efdreinf').get_models()

    for model in app_models:

        STATUS = [
            STATUS_EVENTO_AGUARD_ENVIO,
            STATUS_EVENTO_VALIDADO
        ]

        EVENTOS_GRUPOS = (
            (1, u'1 - Eventos de Tabelas'),
            (2, u'2 - Eventos Não Periódicos'),
            (3, u'3 - Eventos Periódicos'),
        )

        lista = model.objects.filter(status=STATUS_EVENTO_AGUARD_ENVIO,
                                     transmissor_lote_efdreinf=None).all()

        numero_evento = int(model._meta.db_table[1:5])

        if numero_evento < 1200:
            grupo = 1
        elif numero_evento >= 1200 and numero_evento <= 1300:
            grupo = 2
        else:
            grupo = 3

        txt = ''

        for a in lista:

            criar_transmissor_efdreinf(request, grupo, a.nrinsc, a.tpinsc)

            txt = vincular_transmissor_efdreinf(request, grupo, model, a)

        texto += txt

    lista_transmissores = TransmissorLoteEfdreinf.objects.filter(status=0).all()

    n = 0
    for a in lista_transmissores:
        n += 1
        send_xml(request, a.id, 'RecepcaoLoteReinf')

    texto = '%s transmissores enviaram eventos para o EFD-Reinf' % n

    if not tab:

        messages.success(request, texto)
        return redirect(request.session['return_page'])

    elif tab == 'mapa':

        messages.success(request, texto)
        return redirect('mapa_efdreinf', tab='master')

    elif tab == 'mapa_resumo':

        messages.success(request, texto)
        return redirect('visao_geral')

    elif tab == 'json':

        data = {'response': texto}
        return Response(data, status=HTTP_200_OK)

    else:

        data = {'response': u'Página não existe!'}
        return Response(data, status=HTTP_404_NOT_FOUND)




@csrf_exempt
@api_view(["GET"])
def consultar(request, tab=None):
    from emensageriapro.mensageiro.views.transmissor_lote_efdreinf_comunicacao import send_xml
    from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf

    texto = 'Eventos consultados com sucesso!'

    lista_transmissores = TransmissorLoteEfdreinf.objects.filter(status=1).all()

    for a in lista_transmissores:
        send_xml(request, a.id, 'ConsultasReinf')

    if not tab:

        messages.success(request, texto)
        return redirect(request.session['return_page'])

    elif tab == 'mapa':

        messages.success(request, texto)
        return redirect('mapa_esocial', tab='master')

    elif tab == 'mapa_resumo':

        messages.success(request, texto)
        return redirect('visao_geral')

    elif tab == 'json':

        data = {'response': texto}
        return Response(data, status=HTTP_200_OK)

    else:

        data = {'response': u'Página não existe!'}
        return Response(data, status=HTTP_404_NOT_FOUND)
