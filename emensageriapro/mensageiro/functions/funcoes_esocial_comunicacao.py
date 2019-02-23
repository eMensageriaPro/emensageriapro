#coding:utf-8
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

import psycopg2
import datetime
import os
from django.contrib import messages
from emensageriapro.settings import BASE_DIR
from emensageriapro.padrao import ler_arquivo, executar_sql


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def get_ocorrencias(retornos_eventos_id):
    import json
    from django.forms.models import model_to_dict
    from emensageriapro.mensageiro.models import RetornosEventosOcorrencias

    ocorrencias = RetornosEventosOcorrencias.objects.using( 'default' ).filter(excluido = False, retornos_eventos_id=retornos_eventos_id).all()
    lista_ocor = []
    for o in ocorrencias:
        lista_ocor.append(json.dumps(model_to_dict(o), indent=4, sort_keys=True, default=str))
    txt_str = '|'.join(lista_ocor)
    txt_str = txt_str.replace("'", "''")

    return str(txt_str).replace("'", "''")



def read_envioLoteEventos(arquivo, transmissor_lote_esocial_id):

    from emensageriapro.mensageiro.models import TransmissorLoteEsocialOcorrencias, TransmissorLoteEsocial
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    child = doc.Envelope.Body.EnviarLoteEventosResponse.EnviarLoteEventosResult.eSocial.retornoEnvioLoteEventos

    lote = {}
    lote['status'] = 1
    lote['resposta_codigo'] = child.status.cdResposta.cdata
    lote['resposta_descricao'] = child.status.descResposta.cdata

    TransmissorLoteEsocialOcorrencias.objects.using('default').\
        filter(transmissor_lote_esocial_id=transmissor_lote_esocial_id).delete()

    if '<ocorrencias>' in xml:

        for a in child.status.ocorrencias.ocorrencia:
            ocorrencias = {}
            ocorrencias['transmissor_lote_esocial_id'] = transmissor_lote_esocial_id
            ocorrencias['codigo'] = a.codigo.cdata
            ocorrencias['descricao'] = a.descricao.cdata
            ocorrencias['descricao'] = ocorrencias['descricao'].replace("'", "''")
            ocorrencias['tipo'] = a.tipo.cdata
            try:
                ocorrencias['localizacao'] = a.localizacao.cdata
            except:
                ocorrencias['localizacao'] = ''

            obj = TransmissorLoteEsocialOcorrencias(**ocorrencias)
            obj.save(using='default')


    if '<dadosRecepcaoLote>' in xml:
        lote['recepcao_data_hora'] = child.dadosRecepcaoLote.dhRecepcao.cdata
        lote['recepcao_versao_aplicativo'] = child.dadosRecepcaoLote.versaoAplicativoRecepcao.cdata
        lote['protocolo'] = child.dadosRecepcaoLote.protocoloEnvio.cdata

    TransmissorLoteEsocial.objects.using('default'). \
        filter(id=transmissor_lote_esocial_id).update(**lote)




def read_retornoEvento(doc, transmissor_lote_id):
    from emensageriapro.mensageiro.models import TransmissorLoteEsocialOcorrencias, TransmissorLoteEsocial
    
    import untangle
    retorno_evento_dados = {}
    retorno_evento_dados['transmissor_lote_esocial_id'] = transmissor_lote_id
    retorno_evento_dados['identidade'] = doc.eSocial.retornoEvento['Id']
    retornoEvento = doc.eSocial.retornoEvento

    if 'tpInsc' in dir(retornoEvento.ideEmpregador):
        retorno_evento_dados['tpinsc'] = retornoEvento.ideEmpregador.tpInsc.cdata

    if 'nrInsc' in dir(retornoEvento.ideEmpregador):
        retorno_evento_dados['nrinsc'] = retornoEvento.ideEmpregador.nrInsc.cdata

    if 'recepcao' in dir(retornoEvento):

        if 'tpAmb' in dir(retornoEvento.recepcao):
            retorno_evento_dados['recepcao_tp_amb'] = retornoEvento.recepcao.tpAmb.cdata

        if 'dhRecepcao' in dir(retornoEvento.recepcao):
            retorno_evento_dados['recepcao_data_hora'] = retornoEvento.recepcao.dhRecepcao.cdata

        if 'versaoAppRecepcao' in dir(retornoEvento.recepcao):
            retorno_evento_dados['recepcao_versao_app'] = retornoEvento.recepcao.versaoAppRecepcao.cdata

        if 'protocoloEnvioLote' in dir(retornoEvento.recepcao):
            retorno_evento_dados['recepcao_protocolo_envio_lote'] = retornoEvento.recepcao.protocoloEnvioLote.cdata

    if 'processamento' in dir(retornoEvento):

        if 'cdResposta' in dir(retornoEvento.processamento):
            retorno_evento_dados['processamento_codigo_resposta'] = retornoEvento.processamento.cdResposta.cdata

        if 'descResposta' in dir(retornoEvento.processamento):
            retorno_evento_dados['processamento_descricao_resposta'] = retornoEvento.processamento.descResposta.cdata

        if 'versaoAppProcessamento' in dir(retornoEvento.processamento):
            retorno_evento_dados['processamento_versao_app_processamento'] = retornoEvento.processamento.versaoAppProcessamento.cdata

        if 'dhProcessamento' in dir(retornoEvento.processamento):
            retorno_evento_dados['processamento_data_hora'] = retornoEvento.processamento.dhProcessamento.cdata

    if 'recibo' in dir(retornoEvento):

        if 'nrRecibo' in dir(retornoEvento.recibo): retorno_evento_dados['recibo_numero'] = retornoEvento.recibo.nrRecibo.cdata

        if 'hash' in dir(retornoEvento.recibo): retorno_evento_dados['recibo_hash'] = retornoEvento.recibo.hash.cdata

        if 'contrato' in dir(retornoEvento.recibo):

            if 'ideEmpregador' in dir(retornoEvento.recibo.contrato):

                if 'tpInsc' in dir(retornoEvento.recibo.contrato.ideEmpregador):
                    retorno_evento_dados['empregador_tpinsc'] = retornoEvento.recibo.contrato.ideEmpregador.tpInsc.cdata

                if 'nrInsc' in dir(retornoEvento.recibo.contrato.ideEmpregador):
                    retorno_evento_dados['empregador_nrinsc'] = retornoEvento.recibo.contrato.ideEmpregador.nrInsc.cdata

            if 'trabalhador' in dir(retornoEvento.recibo.contrato):

                if 'cpfTrab' in dir(retornoEvento.recibo.contrato.trabalhador):
                    retorno_evento_dados['cpftrab'] = retornoEvento.recibo.contrato.trabalhador.cpfTrab.cdata

                if 'nisTrab' in dir(retornoEvento.recibo.contrato.trabalhador):
                    retorno_evento_dados['nistrab'] = retornoEvento.recibo.contrato.trabalhador.nisTrab.cdata

                if 'nmTrab' in dir(retornoEvento.recibo.contrato.trabalhador):
                    retorno_evento_dados['nmtrab'] = retornoEvento.recibo.contrato.trabalhador.nmTrab.cdata

            if 'infoDeficiencia' in dir(retornoEvento.recibo.contrato):

                if 'infoCota' in dir(retornoEvento.recibo.contrato.infoDeficiencia):
                    retorno_evento_dados['infocota'] = retornoEvento.recibo.contrato.infoDeficiencia.infoCota.cdata

            if 'vinculo' in dir(retornoEvento.recibo.contrato):

                if 'matricula' in dir(retornoEvento.recibo.contrato.vinculo):
                    retorno_evento_dados['matricula'] = retornoEvento.recibo.contrato.vinculo.matricula.cdata

            if 'infoCeletista' in dir(retornoEvento.recibo.contrato):

                if 'dtAdm' in dir(retornoEvento.recibo.contrato.infoCeletista):
                    retorno_evento_dados['dtadm'] = retornoEvento.recibo.contrato.infoCeletista.dtAdm.cdata

                if 'tpRegJor' in dir(retornoEvento.recibo.contrato.infoCeletista):
                    retorno_evento_dados['tpregjor'] = retornoEvento.recibo.contrato.infoCeletista.tpRegJor.cdata

                if 'dtBase' in dir(retornoEvento.recibo.contrato.infoCeletista):
                    retorno_evento_dados['dtbase'] = retornoEvento.recibo.contrato.infoCeletista.dtBase.cdata

                if 'cnpjSindCategProf' in dir(retornoEvento.recibo.contrato.infoCeletista):
                    retorno_evento_dados['cnpjsindcategprof'] = retornoEvento.recibo.contrato.infoCeletista.cnpjSindCategProf.cdata

            if 'infoEstatutario' in dir(retornoEvento.recibo.contrato):

                if 'dtPosse' in dir(retornoEvento.recibo.contrato.infoEstatutario):
                    retorno_evento_dados['dtposse'] = retornoEvento.recibo.contrato.infoEstatutario.dtPosse.cdata

                if 'dtExercicio' in dir(retornoEvento.recibo.contrato.infoEstatutario):
                    retorno_evento_dados['dtexercicio'] = retornoEvento.recibo.contrato.infoEstatutario.dtExercicio.cdata

            if 'infoContrato' in dir(retornoEvento.recibo.contrato):

                if 'cargo' in dir(retornoEvento.recibo.contrato.infoContrato):

                    if 'codCargo' in dir(retornoEvento.recibo.contrato.infoContrato.cargo):
                        retorno_evento_dados['codcargo'] = retornoEvento.recibo.contrato.infoContrato.cargo.codCargo.cdata

                    if 'nmCargo' in dir(retornoEvento.recibo.contrato.infoContrato.cargo):
                        retorno_evento_dados['nmcargo'] = retornoEvento.recibo.contrato.infoContrato.cargo.nmCargo.cdata

                    if 'codCBO' in dir(retornoEvento.recibo.contrato.infoContrato.cargo):
                        retorno_evento_dados['codcbocargo'] = retornoEvento.recibo.contrato.infoContrato.cargo.codCBO.cdata

                if 'funcao' in dir(retornoEvento.recibo.contrato.infoContrato):

                    if 'codFuncao' in dir(retornoEvento.recibo.contrato.infoContrato.funcao):
                        retorno_evento_dados['codfuncao'] = retornoEvento.recibo.contrato.infoContrato.funcao.codFuncao.cdata

                    if 'nmFuncao' in dir(retornoEvento.recibo.contrato.infoContrato.funcao):
                        retorno_evento_dados['nmfuncao'] = retornoEvento.recibo.contrato.infoContrato.funcao.nmFuncao.cdata

                    if 'codCBO' in dir(retornoEvento.recibo.contrato.infoContrato.funcao):
                        retorno_evento_dados['codcbofuncao'] = retornoEvento.recibo.contrato.infoContrato.funcao.codCBO.cdata

                if 'codCateg' in dir(retornoEvento.recibo.contrato.infoContrato):
                    retorno_evento_dados['codcateg'] = retornoEvento.recibo.contrato.infoContrato.codCateg.cdata

            if 'remuneracao' in dir(retornoEvento.recibo.contrato):

                if 'vrSalFx' in dir(retornoEvento.recibo.contrato.remuneracao):
                    retorno_evento_dados['vrsalfx'] = retornoEvento.recibo.contrato.remuneracao.vrSalFx.cdata

                if 'undSalFixo' in dir(retornoEvento.recibo.contrato.remuneracao):
                    retorno_evento_dados['undsalfixo'] = retornoEvento.recibo.contrato.remuneracao.undSalFixo.cdata

                if 'dscSalVar' in dir(retornoEvento.recibo.contrato.remuneracao):
                    retorno_evento_dados['dscsalvar'] = retornoEvento.recibo.contrato.remuneracao.dscSalVar.cdata

            if 'duracao' in dir(retornoEvento.recibo.contrato):

                if 'tpContr' in dir(retornoEvento.recibo.contrato.duracao):
                    retorno_evento_dados['tpcontr'] = retornoEvento.recibo.contrato.duracao.tpContr.cdata

                if 'dtTerm' in dir(retornoEvento.recibo.contrato.duracao):
                    retorno_evento_dados['dtterm'] = retornoEvento.recibo.contrato.duracao.dtTerm.cdata

                if 'clauAsseg' in dir(retornoEvento.recibo.contrato.duracao):
                    retorno_evento_dados['clauasseg'] = retornoEvento.recibo.contrato.duracao.clauAsseg.cdata

            if 'localTrabGeral' in dir(retornoEvento.recibo.contrato):

                if 'tpInsc' in dir(retornoEvento.recibo.contrato.localTrabGeral):
                    retorno_evento_dados['local_tpinsc'] = retornoEvento.recibo.contrato.localTrabGeral.tpInsc.cdata

                if 'nrInsc' in dir(retornoEvento.recibo.contrato.localTrabGeral):
                    retorno_evento_dados['local_nrinsc'] = retornoEvento.recibo.contrato.localTrabGeral.nrInsc.cdata

                if 'cnae' in dir(retornoEvento.recibo.contrato.localTrabGeral):
                    retorno_evento_dados['local_cnae'] = retornoEvento.recibo.contrato.localTrabGeral.cnae.cdata

            if 'horContratual' in dir(retornoEvento.recibo.contrato):

                if 'qtdHrsSem' in dir(retornoEvento.recibo.contrato.localTrabGeral):
                    retorno_evento_dados['qtdhrssem'] = retornoEvento.recibo.contrato.horContratual.qtdHrsSem.cdata

                if 'tpJornada' in dir(retornoEvento.recibo.contrato.localTrabGeral):
                    retorno_evento_dados['tpjornada'] = retornoEvento.recibo.contrato.horContratual.tpJornada.cdata

                if 'dscTpJorn' in dir(retornoEvento.recibo.contrato.localTrabGeral):
                    retorno_evento_dados['dsctpjorn'] = retornoEvento.recibo.contrato.horContratual.dscTpJorn.cdata

                if 'tmpParc' in dir(retornoEvento.recibo.contrato.localTrabGeral):
                    retorno_evento_dados['tmpparc'] = retornoEvento.recibo.contrato.horContratual.tmpParc.cdata

    insert = create_insert('retornos_eventos', retorno_evento_dados)
    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
    resp = executar_sql(insert, True)
    retorno_evento_id = resp[0][0]
    retorno_evento_dados['id'] = retorno_evento_id

    if 'processamento' in dir(retornoEvento):
        if 'ocorrencias' in dir(retornoEvento.processamento):

            for ocorrencia in (retornoEvento.processamento.ocorrencias.ocorrencia):
                ocorrencias_dados = {}
                ocorrencias_dados['retornos_eventos_id'] = retorno_evento_id
                if 'tipo' in dir(ocorrencia): ocorrencias_dados['tipo'] = ocorrencia.tipo.cdata
                if 'codigo' in dir(ocorrencia): ocorrencias_dados['codigo'] = ocorrencia.codigo.cdata.replace("'", "''")
                if 'descricao' in dir(ocorrencia): ocorrencias_dados['descricao'] = ocorrencia.descricao.cdata.replace("'", "''")
                if 'localizacao' in dir(ocorrencia): ocorrencias_dados['localizacao'] = ocorrencia.localizacao.cdata.replace("'", "''")
                #print ocorrencias_dados
                insert = create_insert('retornos_eventos_ocorrencias', ocorrencias_dados)
                for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                resp = executar_sql(insert, True)


    if 'recibo' in dir(retornoEvento):
        if 'contrato' in dir(retornoEvento.recibo):
            if 'horContratual' in dir(retornoEvento.recibo.contrato):
                if 'horario' in dir(retornoEvento.recibo.contrato.horContratual):
                    for horario in (retornoEvento.recibo.contrato.horContratual.horario):
                        horario_dados = {}
                        if 'dia' in dir(horario): horario_dados['dia'] = horario.dia.cdata
                        if 'codHorContrat' in dir(horario): horario_dados['codhorcontrat'] = horario.codHorContrat.cdata
                        if 'hrEntr' in dir(horario): horario_dados['hrentr'] = horario.hrEntr.cdata
                        if 'hrSaida' in dir(horario): horario_dados['hrsaida'] = horario.hrSaida.cdata
                        if 'durJornada' in dir(horario): horario_dados['durjornada'] = horario.durJornada.cdata
                        if 'perHorFlexivel' in dir(horario): horario_dados['perhorflexivel'] = horario.perHorFlexivel.cdata
                        horario_dados['retornos_eventos_id'] = retorno_evento_id
                        insert = create_insert('retornos_eventos_horarios', horario_dados)
                        for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                        resp = executar_sql(insert, True)
                        retornos_eventos_horarios_id = resp[0][0]


                        if 'horarioIntervalo' in dir(horario):
                            for intervalo in (horario.horarioIntervalo):
                                intervalo_dados = {}
                                if 'tpInterv' in dir(intervalo): intervalo_dados['tpinterv'] = intervalo.tpInterv.cdata
                                if 'durInterv' in dir(intervalo): intervalo_dados['durinterv'] = intervalo.durInterv.cdata
                                if 'iniInterv' in dir(intervalo): intervalo_dados['iniinterv'] = intervalo.iniInterv.cdata
                                if 'termInterv' in dir(intervalo): intervalo_dados['terminterv'] = intervalo.termInterv.cdata
                                intervalo_dados['retornos_eventos_horarios_id'] = retornos_eventos_horarios_id
                                insert = create_insert('retornos_eventos_intervalos', intervalo_dados)
                                for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                                resp = executar_sql(insert, True)


    from django.apps import apps

    app_models = apps.get_app_config('esocial').get_models()
    
    for model in app_models:
        
        if 'processamento_codigo_resposta' in retorno_evento_dados.keys():

            codigo_resposta = int(retorno_evento_dados['processamento_codigo_resposta'])
            
            if codigo_resposta >= 300:

                model.objects.using('default').filter(identidade=retorno_evento_dados['identidade']).\
                    update(status=STATUS_EVENTO_ENVIADO_ERRO,
                           ocorrencias=get_ocorrencias(retorno_evento_id),
                           retornos_eventos_id=retorno_evento_id)
            
            elif codigo_resposta >= 201 and codigo_resposta < 300:

                model.objects.using('default').filter(identidade=retorno_evento_dados['identidade']).\
                    update(status=STATUS_EVENTO_PROCESSADO,
                           ocorrencias=get_ocorrencias(retorno_evento_id),
                           retornos_eventos_id=retorno_evento_id)

    return retorno_evento_dados




def read_consultaLoteEventos(arquivo, transmissor_lote_esocial_id):
    from emensageriapro.mensageiro.models import TransmissorLoteEsocial

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    child = doc.Envelope.Body.ConsultarLoteEventosResponse.ConsultarLoteEventosResult.eSocial.retornoProcessamentoLoteEventos

    lote = {}
    lote['resposta_codigo'] = child.status.cdResposta.cdata
    lote['resposta_descricao'] = child.status.descResposta.cdata

    if '<tempoEstimadoConclusao>' in xml:

        lote['tempo_estimado_conclusao'] = child.status.tempoEstimadoConclusao.cdata

    else:

        lote['tempo_estimado_conclusao'] = None

    if '<dadosRecepcaoLote>' in xml:

        lote['recepcao_data_hora'] = child.dadosRecepcaoLote.dhRecepcao.cdata
        lote['recepcao_versao_aplicativo'] = child.dadosRecepcaoLote.versaoAplicativoRecepcao.cdata
        lote['protocolo'] = child.dadosRecepcaoLote.protocoloEnvio.cdata
        lote['status'] = 3

    else:

        lote['recepcao_data_hora'] = None
        lote['recepcao_versao_aplicativo'] = None
        lote['protocolo'] = None

    if '<versaoAplicativoProcessamentoLote>' in xml:
        lote['processamento_versao_aplicativo'] = child.dadosProcessamentoLote.versaoAplicativoProcessamentoLote.cdata
    else:
        lote['processamento_versao_aplicativo'] = None

    TransmissorLoteEsocial.objects.using('default').\
        filter(id=transmissor_lote_esocial_id).update(**lote)

    if '<retornoEventos>' in xml:

        for evento in child.retornoEventos.evento:

            if 'retornoEvento' in dir(evento):
                dados = read_retornoEvento(evento.retornoEvento, transmissor_lote_esocial_id)

                a = executar_sql("""
                SELECT tabela, id
                      FROM public.transmissor_eventos_esocial 
                      WHERE identidade='%(identidade)s';
                """ % dados, True)

                dados['tabela'] = a[0][0]
                dados['tabela_id'] = a[0][1]

                executar_sql(""" 
                     UPDATE public.%(tabela)s SET retornos_eventos_id=%(id)s
                      WHERE id=%(tabela_id)s;""" % dados, False)

            if 'evtBasesTrab' in dir(evento):
                from emensageriapro.esocial.views.s5001_evtbasestrab_importar import read_s5001_evtbasestrab_obj
                read_s5001_evtbasestrab_obj(evento.eSocial, 12)

            if 'evtIrrfBenef' in dir(evento):
                from emensageriapro.esocial.views.s5002_evtirrfbenef_importar import read_s5002_evtirrfbenef_obj
                read_s5002_evtirrfbenef_obj(evento.eSocial, 12)

            if 'evtCS' in dir(evento):
                from emensageriapro.esocial.views.s5011_evtcs_importar import read_s5011_evtcs_obj
                read_s5011_evtcs_obj(evento.eSocial, 12)

            if 'evtIrrf' in dir(evento):
                from emensageriapro.esocial.views.s5012_evtirrf_importar import read_s5012_evtirrf_obj
                read_s5012_evtirrf_obj(evento.eSocial, 12)



