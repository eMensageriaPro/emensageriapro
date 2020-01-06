#coding:utf-8
from emensageriapro.mensageiro.functions.funcoes import create_insert

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

import xmltodict
import json
from datetime import datetime
from django.apps import apps
from xml.dom import minidom
from emensageriapro.settings import BASE_DIR
from emensageriapro.mensageiro.models import TransmissorLoteEsocial
from emensageriapro.esocial.models import STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO
from emensageriapro.mensageiro.functions.funcoes import TRANSMISSOR_STATUS_ENVIADO,\
    TRANSMISSOR_STATUS_ENVIADO_ERRO, TRANSMISSOR_STATUS_CONSULTADO, TRANSMISSOR_STATUS_CONSULTADO_ERRO


def read_envioLoteEventos(arquivo, transmissor_lote_esocial_id):

    xmldoc = minidom.parse(BASE_DIR + arquivo)

    lote = {}
    lote['retorno_envio_json'] = json.dumps(xmltodict.parse(xmldoc.getElementsByTagName('retornoEnvioLoteEventos')[0].toxml()))
    if xmldoc.getElementsByTagName('ocorrencia'):
        lote['ocorrencias_json'] = json.dumps(xmltodict.parse(xmldoc.getElementsByTagName('ocorrencia')[0].toxml()))
    else:
        lote['ocorrencias_json'] = None

    lote['data_hora_envio'] = datetime.now()

    status = xmldoc.getElementsByTagName('status')
    if status:
        lote['resposta_codigo'] = status[0].getElementsByTagName('cdResposta')[0].firstChild.nodeValue
        lote['resposta_descricao'] = status[0].getElementsByTagName('descResposta')[0].firstChild.nodeValue
        if lote['resposta_codigo'][0] == '2':
            lote['status'] = TRANSMISSOR_STATUS_ENVIADO
        else:
            lote['status'] = TRANSMISSOR_STATUS_ENVIADO_ERRO

    dados_recepcao_lote = xmldoc.getElementsByTagName('dadosRecepcaoLote')
    if dados_recepcao_lote:
        lote['recepcao_data_hora'] = dados_recepcao_lote[0].getElementsByTagName('dhRecepcao')[0].firstChild.nodeValue
        lote['recepcao_versao_aplicativo'] = dados_recepcao_lote[0].getElementsByTagName('versaoAplicativoRecepcao')[0].firstChild.nodeValue
        lote['protocolo'] = dados_recepcao_lote[0].getElementsByTagName('protocoloEnvio')[0].firstChild.nodeValue

    TransmissorLoteEsocial.objects. \
        filter(id=transmissor_lote_esocial_id).update(**lote)

    app_models = apps.get_app_config('esocial').get_models()

    for model in app_models:

        dados = {}

        if lote['status'] == TRANSMISSOR_STATUS_ENVIADO:
            dados['status'] = STATUS_EVENTO_ENVIADO
            dados['retorno_envio_json'] = lote['retorno_envio_json']
            dados['ocorrencias_json'] = None

        elif lote['status'] == TRANSMISSOR_STATUS_ENVIADO_ERRO:
            dados['status'] = STATUS_EVENTO_ENVIADO_ERRO
            dados['transmissor_lote_esocial_id'] = None
            dados['transmissor_lote_esocial_error_id'] = transmissor_lote_esocial_id
            dados['retorno_envio_json'] = lote['retorno_envio_json']
            dados['ocorrencias_json'] = None

        model.objects. \
            filter(transmissor_lote_esocial_id=transmissor_lote_esocial_id). \
            update(**dados)

        # if lote['status'] == TRANSMISSOR_STATUS_ENVIADO:
        #     model.objects.filter(id=a.id).update(status=STATUS_EVENTO_ENVIADO,
        #                                          retorno_envio_json=lote['retorno_envio_json'],
        #                                          ocorrencias_json=None)
        #
        # elif lote['status'] == TRANSMISSOR_STATUS_ENVIADO_ERRO:
        #     model.objects.filter(id=a.id).update(status=STATUS_EVENTO_ENVIADO_ERRO,
        #                                          retorno_envio_json=lote['retorno_envio_json'],
        #                                          transmissor_lote_esocial=None,
        #                                          ocorrencias_json=None,
        #                                          transmissor_lote_esocial_error=transmissor_lote_esocial_id)

    return lote


def read_consultaLoteEventos(arquivo, transmissor_lote_esocial_id):

    xmldoc = minidom.parse(BASE_DIR + arquivo)

    lote = {}
    lote['retorno_consulta_json'] = json.dumps(xmltodict.parse(xmldoc.getElementsByTagName('retornoProcessamentoLoteEventos')[0].toxml()))
    if xmldoc.getElementsByTagName('ocorrencia'):
        lote['ocorrencias_json'] = json.dumps(xmltodict.parse(xmldoc.getElementsByTagName('ocorrencia')[0].toxml()))
    else:
        lote['ocorrencias_json'] = None

    lote['data_hora_consulta'] = datetime.now()

    status = xmldoc.getElementsByTagName('status')
    if status:
        lote['resposta_codigo'] = status[0].getElementsByTagName('cdResposta')[0].firstChild.nodeValue
        if lote['resposta_codigo'][0] == '2':
            lote['status'] = TRANSMISSOR_STATUS_CONSULTADO
        else:
            lote['status'] = TRANSMISSOR_STATUS_CONSULTADO_ERRO
        lote['resposta_descricao'] = status[0].getElementsByTagName('descResposta')[0].firstChild.nodeValue
        if status[0].getElementsByTagName('tempoEstimadoConclusao'):
            lote['tempo_estimado_conclusao'] = status[0].getElementsByTagName('tempoEstimadoConclusao')[0].firstChild.nodeValue
        else:
            lote['tempo_estimado_conclusao'] = None

    dados_recepcao_lote = xmldoc.getElementsByTagName('dadosRecepcaoLote')
    if dados_recepcao_lote:
        lote['recepcao_data_hora'] = dados_recepcao_lote[0].getElementsByTagName('dhRecepcao')[0].firstChild.nodeValue
        lote['recepcao_versao_aplicativo'] = dados_recepcao_lote[0].getElementsByTagName('versaoAplicativoRecepcao')[0].firstChild.nodeValue
        lote['protocolo'] = dados_recepcao_lote[0].getElementsByTagName('protocoloEnvio')[0].firstChild.nodeValue
    else:
        lote['recepcao_data_hora'] = None
        lote['recepcao_versao_aplicativo'] = None
        lote['protocolo'] = None

    dados_processamento_lote = xmldoc.getElementsByTagName('dadosProcessamentoLote')
    if dados_processamento_lote:
        lote['processamento_versao_aplicativo'] = dados_processamento_lote[0].getElementsByTagName('versaoAplicativoProcessamentoLote')[
            0].firstChild.nodeValue

    TransmissorLoteEsocial.objects.\
        filter(id=transmissor_lote_esocial_id).update(**lote)

    for evento in xmldoc.getElementsByTagName('evento'):

        identidade = evento.getAttribute('Id')

        retorno_consulta_json = json.dumps(xmltodict.parse(evento.toxml()))
        if evento.getElementsByTagName('ocorrencia'):
            ocorrencias_json = json.dumps(xmltodict.parse(evento.getElementsByTagName('processamento')[0].toxml()))
        else:
            ocorrencias_json = None
        app_models = apps.get_app_config('esocial').get_models()

        status = evento.getElementsByTagName('cdResposta')[0].firstChild.nodeValue

        for model in app_models:

            dados = {}
            if status[0] == '2':
                dados['status'] = STATUS_EVENTO_PROCESSADO
                dados['ocorrencias_json'] = None
                dados['retorno_consulta_json'] = retorno_consulta_json

            elif status[0] in ('3', '4', '5'):
                dados['status'] = STATUS_EVENTO_ENVIADO_ERRO
                dados['transmissor_lote_esocial_id'] = None
                dados['transmissor_lote_esocial_error_id'] = transmissor_lote_esocial_id
                dados['retorno_consulta_json'] = retorno_consulta_json
                dados['ocorrencias_json'] = ocorrencias_json

            dados['retorno_consulta_json'] = retorno_consulta_json

            model.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial_id,
                       identidade=identidade).\
                update(**dados)

            # for a in lista:
            #     if status[0] == '2':
            #         model.objects.filter(id=a.id).update(status=STATUS_EVENTO_PROCESSADO,
            #                                              retorno_consulta_json=retorno_consulta_json,
            #                                              ocorrencias_json=None)
            #
            #     elif status[0] in ('3', '4', '5'):
            #         model.objects.filter(id=a.id).update(status=STATUS_EVENTO_ENVIADO_ERRO,
            #                                              retorno_consulta_json=retorno_consulta_json,
            #                                              transmissor_lote_esocial=None,
            #                                              ocorrencias_json=ocorrencias_json,
            #                                              transmissor_lote_esocial_error=transmissor_lote_esocial_id)


    return lote
