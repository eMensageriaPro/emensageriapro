#coding:utf-8
import psycopg2
import datetime
import os
from django.contrib import messages
from emensageriapro.padrao import ler_arquivo, executar_sql
from emensageriapro.mensageiro.functions.funcoes import create_insert, testar_importacao_xml

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


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


from emensageriapro.mensageiro.functions.funcoes_esocial import TRANSMISSOR_STATUS_CADASTRADO, TRANSMISSOR_STATUS_ENVIADO,\
    TRANSMISSOR_STATUS_ENVIADO_ERRO, TRANSMISSOR_STATUS_CONSULTADO, TRANSMISSOR_STATUS_CONSULTADO_ERRO


def definir_status_evento(transmissor_lote_efdreinf_id):
    from django.apps import apps

    app_models = apps.get_app_config('esocial').get_models()

    for model in app_models:

        lista = model.objects.using('default').filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id).all()

        for a in lista:

            if a.transmissor_lote_esocial.status == TRANSMISSOR_STATUS_ENVIADO:
                model.objects.using('default').filter(id=a.id).update(status=STATUS_EVENTO_ENVIADO, ocorrencias=None)

            elif a.transmissor_lote_esocial.status == TRANSMISSOR_STATUS_ENVIADO_ERRO:
                model.objects.using('default').filter(id=a.id).update(transmissor_lote_esocial=None)



def get_ocorrencias_r5001(retornos_evttotal_id):

    import json
    from django.forms.models import model_to_dict
    from emensageriapro.r5001.models import r5001regOcorrs

    ocorrencias = r5001regOcorrs.objects.using( 'default' ).\
        filter(retornos_evttotal_id=retornos_evttotal_id).all()

    lista_ocor = []

    for o in ocorrencias:
        lista_ocor.append(json.dumps(model_to_dict(o), indent=4, sort_keys=True, default=str))

    txt_str = '|'.join(lista_ocor)
    txt_str = txt_str.replace("'", "''")

    return str(txt_str).replace("'", "''")


def get_ocorrencias_r5011(retornos_evttotalcontrib_id):

    import json
    from django.forms.models import model_to_dict
    from emensageriapro.r5011.models import r5011regOcorrs

    ocorrencias = r5011regOcorrs.objects.using( 'default' ).\
        filter(retornos_evttotalcontrib_id=retornos_evttotalcontrib_id).all()

    lista_ocor = []

    for o in ocorrencias:
        lista_ocor.append(json.dumps(model_to_dict(o), indent=4, sort_keys=True, default=str))

    txt_str = '|'.join(lista_ocor)
    txt_str = txt_str.replace("'", "''")

    return str(txt_str).replace("'", "''")



def read_envioLoteEventos(arquivo, transmissor_lote_id):

    from emensageriapro.mensageiro.functions.funcoes_efdreinf import ler_arquivo
    from emensageriapro.mensageiro.models import TransmissorLoteEfdreinfOcorrencias, TransmissorLoteEfdreinf, TransmissorEventosEfdreinf
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    child = doc.Envelope.Body.ReceberLoteEventosResponse.ReceberLoteEventosResult.Reinf.retornoLoteEventos

    lote = {}
    lote['transmissor_lote_id'] = transmissor_lote_id

    if 'IdTransmissor' in dir(child.ideTransmissor): lote['identidade_transmissor'] = child.ideTransmissor.IdTransmissor.cdata
    if 'cdStatus' in dir(child.status): lote['codigo_status'] = child.status.cdStatus.cdata
    if 'descRetorno' in dir(child.status): lote['retorno_descricao'] = child.status.descRetorno.cdata

    # update = """
    #     UPDATE public.transmissor_lote_efdreinf
    #     SET identidade_transmissor='%(identidade_transmissor)s',
    #     codigo_status='%(codigo_status)s',
    #     retorno_descricao='%(retorno_descricao)s'
    #     WHERE id=%(transmissor_lote_id)s;""" % lote
    # resp = executar_sql(update, False)

    TransmissorLoteEfdreinf.objects.using('default'). \
        filter(id=transmissor_lote_id).update(**lote)

    TransmissorLoteEfdreinfOcorrencias.objects.using('default').\
        filter(transmissor_lote_esocial_id=transmissor_lote_id).delete()

    transmissor_lote_efdreinf_id = transmissor_lote_id

    # executar_sql("""
    #   DELETE FROM public.transmissor_lote_efdreinf_ocorrencias
    #        WHERE transmissor_lote_efdreinf_id=%s;""" % transmissor_lote_id, False)


    if 'dadosRegistroOcorrenciaLote' in dir(child.status):

        for ocorrencia in child.status.dadosRegistroOcorrenciaLote.ocorrencias:

            lote_ocorrencias = {}
            lote_ocorrencias['localizacao'] = '-'

            if 'tipo' in dir(ocorrencia):
                lote_ocorrencias['tipo'] = ocorrencia.tipo.cdata

            if 'localizacaoErroAviso' in dir(ocorrencia):
                lote_ocorrencias['localizacao'] = ocorrencia.localizacaoErroAviso.cdata

            if 'codigo' in dir(ocorrencia):
                lote_ocorrencias['resposta_codigo'] = ocorrencia.codigo.cdata

            if 'descricao' in dir(ocorrencia):
                lote_ocorrencias['descricao'] = ocorrencia.descricao.cdata

            lote_ocorrencias['transmissor_lote_efdreinf_id'] = transmissor_lote_efdreinf_id

            obj = TransmissorLoteEfdreinfOcorrencias(**lote_ocorrencias)
            obj.save(using='default')

            # insert = create_insert('transmissor_lote_efdreinf_ocorrencias', lote_ocorrencias)
            # resp = executar_sql(insert, True)

    if 'retornoEventos' in dir(child):

        for evento in child.retornoEventos.evento:

            if 'evtTotal' in dir(evento.Reinf):

                from emensageriapro.efdreinf.views.r5001_evttotal_importar import read_r5001_evttotal_obj
                from emensageriapro.efdreinf.models import r5001evtTotal

                dados = read_r5001_evttotal_obj(evento, 9)

                retornos_evttotal = r5001evtTotal.objects.using('default'). \
                    get(id=dados['id'])

                from django.apps import apps

                app_models = apps.get_app_config('efdreinf').get_models()

                for model in app_models:

                    if retornos_evttotal.cdretorno == 1:

                        model.objects.using('default').filter(
                            identidade=retornos_evttotal.identidade,
                            transmissor_lote_efdreinf_id=transmissor_lote_id). \
                            update(status=STATUS_EVENTO_ENVIADO_ERRO,
                                   ocorrencias=get_ocorrencias_r5001(retornos_evttotal.id),
                                   retornos_evttotal_id=retornos_evttotal,
                                   transmissor_lote_efdreinf_id=None)

                    elif retornos_evttotal.cdretorno == 0:

                        model.objects.using('default').filter(
                            identidade=retornos_evttotal.identidade,
                            transmissor_lote_esocial_id=transmissor_lote_id). \
                            update(status=STATUS_EVENTO_PROCESSADO,
                                   ocorrencias=get_ocorrencias_r5001(retornos_evttotal.id),
                                   retornos_evttotal_id=retornos_evttotal,)

                return retornos_evttotal

                # evento = TransmissorEventosEfdreinf.objects.using('default'). \
                #     filter(identidade=dados['identidade_evento']).all()
                #
                # # evento_identidade = dados['identidade_evento']
                # #
                # # evento_dados = executar_sql("""
                # #     SELECT id, evento, identidade, tabela
                # #       FROM public.transmissor_eventos_efdreinf WHERE identidade='%s';
                # # """ % evento_identidade, True)
                #
                # if evento:
                #
                #     lista = (
                #         evento[0].tabela,
                #         dados['id'],
                #         evento[0].id
                #     )
                #
                #     executar_sql("UPDATE public.%s SET retornos_evttotal_id=%s WHERE id=%s;" % lista, False)

            if 'evtTotalContrib' in dir(evento.Reinf):

                from emensageriapro.efdreinf.views.r5011_evttotalcontrib_importar import read_r5011_evttotalcontrib_obj
                from emensageriapro.efdreinf.models import r5011evtTotal

                dados = read_r5011_evttotalcontrib_obj(evento, 9)

                retornos_evttotalcontrib = r5011evtTotal.objects.using('default'). \
                    get(id=dados['id'])

                from django.apps import apps

                app_models = apps.get_app_config('efdreinf').get_models()

                for model in app_models:

                    if retornos_evttotalcontrib.cdretorno == 1:

                        model.objects.using('default').filter(
                            identidade=retornos_evttotalcontrib.identidade,
                            transmissor_lote_efdreinf_id=transmissor_lote_id). \
                            update(status=STATUS_EVENTO_ENVIADO_ERRO,
                                   ocorrencias=get_ocorrencias_r5011(retornos_evttotalcontrib.id),
                                   retornos_evttotalcontrib_id=retornos_evttotalcontrib,
                                   transmissor_lote_efdreinf_id=None)

                    elif retornos_evttotalcontrib.cdretorno == 0:

                        model.objects.using('default').filter(
                            identidade=retornos_evttotalcontrib.identidade,
                            transmissor_lote_esocial_id=transmissor_lote_id). \
                            update(status=STATUS_EVENTO_PROCESSADO,
                                   ocorrencias=get_ocorrencias_r5011(retornos_evttotalcontrib.id),
                                   retornos_evttotalcontrib_id=retornos_evttotalcontrib,)

                return retornos_evttotalcontrib

                #
                #
                # evento = TransmissorEventosEfdreinf.objects.using('default').\
                #     filter(identidade=dados['identidade_evento']).all()
                #
                # # evento_identidade = dados['identidade_evento']
                # #
                # # evento_dados = executar_sql("""
                # #     SELECT id, evento, identidade, tabela
                # #       FROM public.transmissor_eventos_efdreinf WHERE identidade='%s';
                # # """ % evento_identidade, True)
                #
                # if evento:
                #
                #     lista = (
                #         evento[0].tabela,
                #         dados['id'],
                #         evento[0].id
                #     )
                #
                #     executar_sql("UPDATE public.%s SET retornos_evttotalcontrib_id=%s WHERE id=%s;" % lista, False)







def read_consultaLoteEventos(arquivo, transmissor_lote_id):
    from emensageriapro.efdreinf.views.r5011_evttotalcontrib_importar import read_r5011_evttotalcontrib_obj
    from emensageriapro.mensageiro.functions.funcoes_efdreinf import ler_arquivo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")

    doc = untangle.parse(xml)

    child = doc.Envelope.Body.ConsultaInformacoesConsolidadasResponse.ConsultaInformacoesConsolidadasResult

    lote = {}
    lote['transmissor_lote_id'] = transmissor_lote_id

    if 'evtTotalContrib' in dir(child.Reinf):

        dados = read_r5011_evttotalcontrib_obj(child, 9)
        evento_identidade = dados['identidade_evento']

        evento_dados = executar_sql("""
            SELECT id, evento, identidade, tabela
              FROM public.transmissor_eventos_efdreinf WHERE identidade='%s';
        """ % evento_identidade, True)

        if evento_dados:
            executar_sql("UPDATE public.%s SET retornos_evttotalcontrib_id=%s WHERE id=%s;" % (evento_dados[0][3], dados['id'], evento_dados[0][0]), False)

