#coding:utf-8
from emensageriapro.padrao import executar_sql

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
from xml.dom import minidom
from django.apps import apps
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf
from emensageriapro.settings import BASE_DIR
from emensageriapro.esocial.models import STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO
from emensageriapro.mensageiro.functions.funcoes_esocial import TRANSMISSOR_STATUS_ENVIADO,\
    TRANSMISSOR_STATUS_ENVIADO_ERRO, TRANSMISSOR_STATUS_CONSULTADO_ERRO, TRANSMISSOR_STATUS_CONSULTADO


def read_envioLoteEventos(request, arquivo, transmissor_lote_efdreinf_id):

    lote = {}
    xmldoc = minidom.parse(BASE_DIR + arquivo)

    lote['retorno_envio_json'] = json.dumps(xmltodict.parse(xmldoc.getElementsByTagName('retornoLoteEventos')[0].toxml()))

    transmissor = xmldoc.getElementsByTagName('IdTransmissor')
    if transmissor:
        lote['identidade_transmissor'] = transmissor[0].firstChild.nodeValue

    lote['data_hora_envio'] = datetime.now()

    status = xmldoc.getElementsByTagName('status')
    if status:
        lote['codigo_status'] = status[0].getElementsByTagName('cdStatus')[0].firstChild.nodeValue
        if lote['codigo_status'] == '0':  # 0 - Sucesso
            lote['status'] = TRANSMISSOR_STATUS_ENVIADO
        elif lote['codigo_status'] == '1':  # 1 - Erro
            lote['status'] = TRANSMISSOR_STATUS_ENVIADO_ERRO
        lote['retorno_descricao'] = status[0].getElementsByTagName('descRetorno')[0].firstChild.nodeValue

    TransmissorLoteEfdreinf.objects. \
        filter(id=transmissor_lote_efdreinf_id).update(**lote)

    for evento in xmldoc.getElementsByTagName('evento'):

        dados = {}

        identidade = evento.getAttribute('id')

        evento = evento.getElementsByTagName('Reinf')[0]
        evento = evento.getElementsByTagName('evtTotal')[0]

        dados['ocorrencias_json'] = None
        if evento.getElementsByTagName('tpOcorr'):
            dados['ocorrencias_json'] = json.dumps(xmltodict.parse(evento.getElementsByTagName('ideStatus')[0].toxml()))

        dados['retorno_envio_json'] = xmltodict.parse(evento.toxml())

        dados['cdretorno'] = None
        dados['descretorno'] = None
        dados['dhprocess'] = None
        if evento.getElementsByTagName('cdRetorno'):
            dados['cdretorno'] = evento.getElementsByTagName('cdRetorno')[0].firstChild.nodeValue
        if evento.getElementsByTagName('descRetorno'):
            dados['descretorno'] = evento.getElementsByTagName('descRetorno')[0].firstChild.nodeValue
        if evento.getElementsByTagName('dhProcess'):
            dados['dhprocess'] = evento.getElementsByTagName('dhProcess')[0].firstChild.nodeValue

        app_models = apps.get_app_config('efdreinf').get_models()


        if dados['cdretorno'] == '0':
            dados['status'] = STATUS_EVENTO_PROCESSADO
            dados['ocorrencias_json'] = None

        elif dados['cdretorno'] == '1':
            dados['status'] = STATUS_EVENTO_ENVIADO_ERRO
            dados['transmissor_lote_efdreinf_id'] = None
            dados['transmissor_lote_efdreinf_error_id'] = transmissor_lote_efdreinf_id


        for model in app_models:

            model.objects.filter(
                identidade=identidade,
                transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id). \
                update(**dados)

            # if cdretorno == '1':
            #
            #     model.objects.filter(
            #         identidade=identidade,
            #         transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id). \
            #         update(status=STATUS_EVENTO_ENVIADO_ERRO,
            #                cdretorno=cdretorno,
            #                descretorno=descretorno,
            #                dhprocess=dhprocess,
            #                ocorrencias_json=ocorrencias_json,
            #                transmissor_lote_efdreinf_id=None,
            #                transmissor_lote_efdreinf_error=transmissor_lote_efdreinf_id,
            #                retorno_envio_json=retorno_envio_json)
            #
            # elif cdretorno == '0':
            #
            #     model.objects.filter(
            #         identidade=identidade,
            #         transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id). \
            #         update(status=STATUS_EVENTO_ENVIADO,
            #                cdretorno=cdretorno,
            #                descretorno=descretorno,
            #                dhprocess=dhprocess,
            #                ocorrencias_json=None,
            #                transmissor_lote_efdreinf_error_id=None,
            #                retorno_envio_json=retorno_envio_json)

    return lote


def read_consultaLoteEventos(request, arquivo, transmissor_lote_efdreinf_id):

    lote = {}
    xmldoc = minidom.parse(BASE_DIR + arquivo)

    lote['retorno_consulta_json'] = json.dumps(xmltodict.parse(xmldoc.getElementsByTagName('evtTotalContrib')[0].toxml()))

    lote['data_hora_consulta'] = datetime.now()

    codigo_status = xmldoc.getElementsByTagName('cdStatus')
    if codigo_status:
        lote['codigo_status'] = codigo_status[0].firstChild.nodeValue
        if lote['codigo_status'] == '0':  # 0 - Sucesso
            lote['status'] = TRANSMISSOR_STATUS_CONSULTADO
        elif lote['codigo_status'] == '1':  # 1 - Erro
            lote['status'] = TRANSMISSOR_STATUS_CONSULTADO_ERRO

    desc_retorno = xmldoc.getElementsByTagName('descRetorno')
    if desc_retorno:
        lote['retorno_descricao'] = desc_retorno[0].firstChild.nodeValue

    TransmissorLoteEfdreinf.objects. \
        filter(id=transmissor_lote_efdreinf_id).update(**lote)

    for evento in xmldoc.getElementsByTagName('evento'):

        identidade = evento.getElementsByTagName('idEv')[0].getAttribute('id')
        print identidade

        break

        dados = {}

        dados['retorno_consulta_json'] = json.dumps(xmltodict.parse(evento.toxml()))
        if evento.getElementsByTagName('ocorrencia'):
            dados['ocorrencias_json'] = json.dumps(xmltodict.parse(evento.getElementsByTagName('processamento')[0].toxml()))
        else:
            dados['ocorrencias_json'] = None

        dados['cdretorno'] = None
        dados['descretorno'] = None
        dados['dhprocess'] = None

        if evento.getElementsByTagName('cdRetorno'):
            dados['cdretorno'] = evento.getElementsByTagName('cdRetorno')[0].firstChild.nodeValue
        if evento.getElementsByTagName('descRetorno'):
            dados['descretorno'] = evento.getElementsByTagName('descRetorno')[0].firstChild.nodeValue
        if evento.getElementsByTagName('dhProcess'):
            dados['dhprocess'] = evento.getElementsByTagName('dhProcess')[0].firstChild.nodeValue

        if dados['cdretorno'] == '0':
            dados['status'] = STATUS_EVENTO_PROCESSADO
            dados['ocorrencias_json'] = None

        elif dados['cdretorno'] == '1':
            dados['status'] = STATUS_EVENTO_ENVIADO_ERRO
            dados['transmissor_lote_efdreinf_id'] = None
            dados['transmissor_lote_efdreinf_error_id'] = transmissor_lote_efdreinf_id

        app_models = apps.get_app_config('efdreinf').get_models()

        for model in app_models:

            model.objects.filter(
                identidade=identidade,
                transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id). \
                update(**dados)

            # for a in lista:
            #     if cdretorno == '0':
            #         model.objects.filter(id=a.id).update(status=STATUS_EVENTO_PROCESSADO,
            #                                              cdretorno=cdretorno,
            #                                              descretorno=descretorno,
            #                                              dhprocess=dhprocess,
            #                                              retorno_consulta_json=retorno_consulta_json,
            #                                              ocorrencias_json=ocorrencias_json)
            #
            #     elif cdretorno == '1':
            #         model.objects.filter(id=a.id).update(status=STATUS_EVENTO_ENVIADO_ERRO,
            #                                              cdretorno=cdretorno,
            #                                              descretorno=descretorno,
            #                                              dhprocess=dhprocess,
            #                                              retorno_consulta_json=retorno_consulta_json,
            #                                              transmissor_lote_efdreinf=None,
            #                                              ocorrencias_json=ocorrencias_json,
            #                                              transmissor_lote_efdreinf_error=transmissor_lote_efdreinf_id)

    return lote

