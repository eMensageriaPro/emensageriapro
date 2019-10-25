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


from emensageriapro.esocial.models import STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO
from emensageriapro.functions import EVENTOS_RETORNO


from emensageriapro.mensageiro.functions.funcoes_esocial import TRANSMISSOR_STATUS_ENVIADO,\
    TRANSMISSOR_STATUS_ENVIADO_ERRO


def definir_status_evento(transmissor_lote_efdreinf_id):

    from django.apps import apps

    app_models = apps.get_app_config('efdreinf').get_models()

    for model in app_models:

        lista = model.objects.filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id).all()

        for a in lista:

            if a.transmissor_lote_efdreinf.status == TRANSMISSOR_STATUS_ENVIADO:
                model.objects.filter(id=a.id).\
                    update(status=STATUS_EVENTO_ENVIADO,
                           ocorrencias=None)

            elif a.transmissor_lote_efdreinf.status == TRANSMISSOR_STATUS_ENVIADO_ERRO:
                model.objects.filter(id=a.id).\
                    update(transmissor_lote_efdreinf=None,
                           transmissor_lote_efdreinf_error=transmissor_lote_efdreinf_id)


def get_ocorrencias(evento_slug, retornos_evttotal_id):

    import json
    from django.forms.models import model_to_dict

    if evento_slug == 'r5001':

        from emensageriapro.r5001.models import r5001regOcorrs
        ocorrencias = r5001regOcorrs.objects.\
            filter(r5001_evttotal_id=retornos_evttotal_id).all()

    elif evento_slug == 'r5011':

        from emensageriapro.r5011.models import r5011regOcorrs
        ocorrencias = r5011regOcorrs.objects.\
            filter(r5011_evttotalcontrib_id=retornos_evttotal_id).all()

    elif evento_slug == 'r9001':

        from emensageriapro.r9001.models import r9001regOcorrs
        ocorrencias = r9001regOcorrs.objects.\
            filter(r9001_evttotal_id=retornos_evttotal_id).all()

    elif evento_slug == 'r9011':

        from emensageriapro.r9011.models import r9011regOcorrs
        ocorrencias = r9011regOcorrs.objects.\
            filter(r9011_evttotalcontrib_id=retornos_evttotal_id).all()

    lista_ocor = []

    for o in ocorrencias:
        lista_ocor.append(json.dumps(model_to_dict(o), sort_keys=True, default=str))

    txt_str = '|'.join(lista_ocor)
    txt_str = txt_str.replace("'", "''")

    return str(txt_str).replace("'", "''")


def read_envioLoteEventos(request, arquivo, transmissor_lote_efdreinf_id):

    from emensageriapro.mensageiro.functions.funcoes import ler_arquivo
    from emensageriapro.mensageiro.models import TransmissorLoteEfdreinfOcorrencias, TransmissorLoteEfdreinf
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    child = doc.Envelope.Body.ReceberLoteEventosResponse.ReceberLoteEventosResult.Reinf.retornoLoteEventos

    lote = {}

    if 'IdTransmissor' in dir(child.ideTransmissor): lote['identidade_transmissor'] = child.ideTransmissor.IdTransmissor.cdata
    if 'cdStatus' in dir(child.status): lote['codigo_status'] = child.status.cdStatus.cdata
    if 'descRetorno' in dir(child.status): lote['retorno_descricao'] = child.status.descRetorno.cdata

    TransmissorLoteEfdreinf.objects. \
        filter(id=transmissor_lote_efdreinf_id).update(**lote)

    TransmissorLoteEfdreinfOcorrencias.objects.\
        filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id).delete()

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

    if 'retornoEventos' in dir(child):

        eventos_retorno = [
            's5001evtBasesTrab',
            's5002evtIrrfBenef',
            's5003evtBasesFGTS',
            's5011evtCS',
            's5012evtIrrf',
            's5013evtFGTS', ]

        for evento in child.retornoEventos.evento:

            if 'evtTotal' in dir(evento.Reinf):

                from emensageriapro.efdreinf.views.r9001_evttotal_importar import read_r9001_evttotal_obj
                from emensageriapro.efdreinf.models import r9001evtTotal

                dados = read_r9001_evttotal_obj(request, evento, STATUS_EVENTO_PROCESSADO)

                retornos_evttotal = r9001evtTotal.objects. \
                    get(id=dados['id'])

                from django.apps import apps

                app_models = apps.get_app_config('efdreinf').get_models()

                for model in app_models:

                    if retornos_evttotal.cdretorno == '1' and model._meta.object_name not in EVENTOS_RETORNO:

                        model.objects.filter(
                            identidade=evento['id'],
                            transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id). \
                            update(status=STATUS_EVENTO_ENVIADO_ERRO,
                                   ocorrencias=get_ocorrencias('r9001', retornos_evttotal.id),
                                   retornos_r9001_id=retornos_evttotal.id,
                                   transmissor_lote_efdreinf_id=None,
                                   transmissor_lote_efdreinf_error=transmissor_lote_efdreinf_id)

                    elif retornos_evttotal.cdretorno == '0' and model._meta.object_name not in EVENTOS_RETORNO:

                        model.objects.filter(
                            identidade=evento['id'],
                            transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id). \
                            update(status=STATUS_EVENTO_ENVIADO,
                                   ocorrencias=get_ocorrencias('r9001', retornos_evttotal.id),
                                   retornos_r9001_id=retornos_evttotal.id,
                                   transmissor_lote_efdreinf_error_id=None)

                return retornos_evttotal


            if 'evtTotalContrib' in dir(evento.Reinf):

                from emensageriapro.efdreinf.views.r9011_evttotalcontrib_importar import read_r9011_evttotalcontrib_obj
                from emensageriapro.efdreinf.models import r9011evtTotalContrib

                dados = read_r9011_evttotalcontrib_obj(request, evento, STATUS_EVENTO_PROCESSADO)

                retornos_evttotalcontrib = r9011evtTotalContrib.objects.get(id=dados['id'])

                from django.apps import apps

                app_models = apps.get_app_config('efdreinf').get_models()

                for model in app_models:

                    if retornos_evttotalcontrib.cdretorno == '1' and model._meta.object_name not in EVENTOS_RETORNO:

                        model.objects.filter(
                            identidade=evento['id'],
                            transmissor_lote_efdreinf_id=transmissor_lote_efdreinf_id). \
                            update(status=STATUS_EVENTO_ENVIADO_ERRO,
                                   ocorrencias=get_ocorrencias('r9011', retornos_evttotalcontrib.id),
                                   retornos_r9011_id=retornos_evttotalcontrib.id,
                                   transmissor_lote_efdreinf_id=None
                                   )

                    elif retornos_evttotalcontrib.cdretorno == '0' and model._meta.object_name not in EVENTOS_RETORNO:

                        model.objects.filter(
                            identidade=evento['id'],
                            transmissor_lote_esocial_id=transmissor_lote_efdreinf_id). \
                            update(status=STATUS_EVENTO_PROCESSADO,
                                   ocorrencias=get_ocorrencias('r9011', retornos_evttotalcontrib.id),
                                   retornos_r9011_id=retornos_evttotalcontrib.id
                                   )

                return retornos_evttotalcontrib






def read_consultaLoteEventos(request, arquivo, transmissor_lote_efdreinf_id):

    from emensageriapro.efdreinf.views.r9011_evttotalcontrib_importar import read_r9011_evttotalcontrib_obj
    from emensageriapro.mensageiro.functions.funcoes import ler_arquivo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")

    doc = untangle.parse(xml)

    child = doc.Envelope.Body.ConsultaInformacoesConsolidadasResponse.ConsultaInformacoesConsolidadasResult

    lote = {}
    lote['transmissor_lote_efdreinf_id'] = transmissor_lote_efdreinf_id

    if 'evtTotalContrib' in dir(child.Reinf):

        dados = read_r9011_evttotalcontrib_obj(request, child, 9)
        evento_identidade = dados['identidade_evento']

        evento_dados = executar_sql("""
            SELECT id, evento, identidade, tabela
              FROM public.vw_transmissor_eventos_efdreinf WHERE identidade='%s';
        """ % evento_identidade, True)

        if evento_dados:
            executar_sql("UPDATE public.%s SET retornos_evttotalcontrib_id=%s WHERE id=%s;" % (
                evento_dados[0][3], dados['id'], evento_dados[0][0]), False)

