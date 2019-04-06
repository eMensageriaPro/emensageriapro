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



import datetime
from django.contrib import messages
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

@csrf_exempt
@api_view(["GET"])
def validar(request, hash=None):

    texto = 'Validações processadas com sucesso!'

    db_slug = 'default'

    if hash:

        try:
            usuario_id = request.user.id

        except:
            return redirect('login')

        usuario = get_object_or_404(Usuarios.objects.using(db_slug),
                                    excluido=False,
                                    id=usuario_id)

        pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False,
                                                          endereco='mapa_efdreinf')

        permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False,
                                                                config_paginas=pagina,
                                                                config_perfis=usuario.config_perfis)

        dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
        paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
        modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    from django.apps import apps

    app_models = apps.get_app_config('efdreinf').get_models()

    for model in app_models:

        STATUS = [
            STATUS_EVENTO_IMPORTADO,
        ]

        lista = model.objects.using('default').filter(status__in=STATUS).all()

        for a in lista:

            a.validar()

    if hash:

        messages.success(request, texto)
        return redirect(request.session["retorno_pagina"], hash=request.session['retorno_hash'])

    else:
        data = {'response': texto}
        return Response(data, status=HTTP_200_OK)





@csrf_exempt
@api_view(["GET"])
def enviar(request, hash=None):

    from emensageriapro.mensageiro.views.transmissor_lote_efdreinf_comunicacao import send_xml

    texto = ''

    db_slug = 'default'

    if hash:

        try:
            usuario_id = request.user.id

        except:
            return redirect('login')


        usuario = get_object_or_404(Usuarios.objects.using(db_slug),
                                    excluido=False,
                                    id=usuario_id)
        pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False,
                                                          endereco='mapa_efdreinf')

        permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False,
                                                                config_paginas=pagina,
                                                                config_perfis=usuario.config_perfis)

        dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
        paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
        modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    from django.apps import apps
    from emensageriapro.mensageiro.models import TransmissorLote, TransmissorLoteEfdreinf, TransmissorEventosEfdreinf

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

        lista = model.objects.using('default').filter(status=STATUS_EVENTO_AGUARD_ENVIO,
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

            transmissor_efdreinf_lista = TransmissorLoteEfdreinf.objects.using('default').filter(
                status=0,
                grupo=grupo,
                contribuinte_nrinsc=a.nrinsc,
                contribuinte_tpinsc=a.tpinsc).all()

            if not transmissor_efdreinf:

                transmissor = TransmissorLote.objects.using('default').filter(
                    contribuinte_nrinsc=a.nrinsc,
                    contribuinte_tpinsc=a.tpinsc).all()

                if not transmissor:

                    txt = u'Cadastre um Transmissor para o empregador %s!' % a.nrinsc

                    if hash:
                        messages.error(request, txt)
                        return redirect('mapa_efdreinf', hash=request.session['retorno_hash'])
                    else:
                        data = {'response': txt}
                        return Response(data, status=HTTP_200_OK)

                elif len(transmissor) > 1:
                    txt = u'Existe mais de um transmissor cadastrado o empregador %s, cadastre apenas um!' % a.nrinsc

                    if hash:
                        messages.error(request, txt)
                        return redirect('mapa_efdreinf', hash=request.session['retorno_hash'])
                    else:
                        data = {'response': txt}
                        return Response(data, status=HTTP_200_OK)

                else:

                    dados = {}
                    dados['transmissor_id'] = transmissor[0].id
                    dados['contribuinte_tpinsc'] = transmissor[0].contribuinte_tpinsc
                    dados['contribuinte_nrinsc'] = transmissor[0].contribuinte_nrinsc
                    dados['grupo'] = grupo
                    dados['status'] = 0
                    transmissor_efdreinf = TransmissorLoteEfdreinf(**dados)
                    transmissor_efdreinf.save()

            transmissor_efdreinf_lista = TransmissorLoteEfdreinf.objects.using('default').filter(
                status=0,
                grupo=grupo,
                contribuinte_nrinsc=a.nrinsc,
                contribuinte_tpinsc=a.tpinsc).all()

            for te in transmissor_efdreinf_lista:

                eventos_lista = TransmissorEventosEfdreinf.objects.using('default').filter(
                    transmissor_lote_efdreinf=te.id).all()

                if len(eventos_lista) < te.transmissor_lote_efdreinf.transmissor.efdreinf_lote_max:
                    model.objects.using('default').filter(id=a.id).update(transmissor_lote_efdreinf=te)

                txt = 'Evento vinculado com sucesso!'

        texto += txt

    lista_transmissores = TransmissorLoteEfdreinf.objects.using(db_slug).filter(status=0).all()

    n = 0
    for a in lista_transmissores:
        n += 1
        send_xml(request, a.id, 'RecepcaoLoteReinf')

    texto = '%s transmissores enviaram eventos para o EFD-Reinf' % n

    if hash:

        messages.success(request, texto)
        return redirect(request.session["retorno_pagina"], hash=request.session['retorno_hash'])

    else:
        data = {'response': texto}
        return Response(data, status=HTTP_200_OK)




@csrf_exempt
@api_view(["GET"])
def consultar(request, hash=None):
    from emensageriapro.mensageiro.views.transmissor_lote_efdreinf_comunicacao import send_xml
    from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf

    texto = 'Eventos consultados com sucesso!'

    if hash:

        try:
            usuario_id = request.user.id

        except:
            return redirect('login')

        usuario = get_object_or_404(Usuarios.objects.using(db_slug),
                                    excluido=False,
                                    id=usuario_id)

        pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False,
                                                          endereco='mapa_efdreinf')

        permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False,
                                                                config_paginas=pagina,
                                                                config_perfis=usuario.config_perfis)

        dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
        paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
        modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    db_slug = 'default'

    lista_transmissores = TransmissorLoteEfdreinf.objects.using(db_slug).filter(status=1).all()

    for a in lista_transmissores:
        send_xml(request, a.id, 'ConsultasReinf')

    if hash:

        messages.success(request, texto)
        return redirect(request.session["retorno_pagina"], hash=request.session['retorno_hash'])

    else:
        data = {'response': texto}
        return Response(data, status=HTTP_200_OK)
