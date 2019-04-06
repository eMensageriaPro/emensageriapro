#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos <www.emensageria.com.br>
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
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def read_s2206_evtaltcontratual_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2206_evtaltcontratual_obj(doc, status, validar)
    return dados

def read_s2206_evtaltcontratual(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2206_evtaltcontratual_obj(doc, status, validar)
    return dados



def read_s2206_evtaltcontratual_obj(doc, status, validar=False):
    s2206_evtaltcontratual_dados = {}
    s2206_evtaltcontratual_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2206_evtaltcontratual_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2206_evtaltcontratual_dados['identidade'] = doc.eSocial.evtAltContratual['Id']
    evtAltContratual = doc.eSocial.evtAltContratual

    try: s2206_evtaltcontratual_dados['indretif'] = evtAltContratual.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['nrrecibo'] = evtAltContratual.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['tpamb'] = evtAltContratual.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['procemi'] = evtAltContratual.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['verproc'] = evtAltContratual.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['tpinsc'] = evtAltContratual.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['nrinsc'] = evtAltContratual.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['cpftrab'] = evtAltContratual.ideVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['nistrab'] = evtAltContratual.ideVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['matricula'] = evtAltContratual.ideVinculo.matricula.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['dtalteracao'] = evtAltContratual.altContratual.dtAlteracao.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['dtef'] = evtAltContratual.altContratual.dtEf.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['dscalt'] = evtAltContratual.altContratual.dscAlt.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['tpregprev'] = evtAltContratual.altContratual.vinculo.tpRegPrev.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['codcargo'] = evtAltContratual.altContratual.infoContrato.codCargo.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['codfuncao'] = evtAltContratual.altContratual.infoContrato.codFuncao.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['codcateg'] = evtAltContratual.altContratual.infoContrato.codCateg.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['codcarreira'] = evtAltContratual.altContratual.infoContrato.codCarreira.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['dtingrcarr'] = evtAltContratual.altContratual.infoContrato.dtIngrCarr.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['vrsalfx'] = evtAltContratual.altContratual.infoContrato.remuneracao.vrSalFx.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['undsalfixo'] = evtAltContratual.altContratual.infoContrato.remuneracao.undSalFixo.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['dscsalvar'] = evtAltContratual.altContratual.infoContrato.remuneracao.dscSalVar.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['tpcontr'] = evtAltContratual.altContratual.infoContrato.duracao.tpContr.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['dtterm'] = evtAltContratual.altContratual.infoContrato.duracao.dtTerm.cdata
    except AttributeError: pass
    try: s2206_evtaltcontratual_dados['objdet'] = evtAltContratual.altContratual.infoContrato.duracao.objDet.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtAltContratual.altContratual): s2206_evtaltcontratual_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAltContratual.altContratual): s2206_evtaltcontratual_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAltContratual.altContratual): s2206_evtaltcontratual_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2206_evtaltcontratual', s2206_evtaltcontratual_dados)
    resp = executar_sql(insert, True)
    s2206_evtaltcontratual_id = resp[0][0]
    dados = s2206_evtaltcontratual_dados
    dados['evento'] = 's2206'
    dados['id'] = s2206_evtaltcontratual_id
    dados['identidade_evento'] = doc.eSocial.evtAltContratual['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'infoCeletista' in dir(evtAltContratual.altContratual.infoRegimeTrab) and evtAltContratual.altContratual.infoRegimeTrab.infoCeletista.cdata != '':
        for infoCeletista in evtAltContratual.altContratual.infoRegimeTrab.infoCeletista:
            s2206_infoceletista_dados = {}
            s2206_infoceletista_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id

            try: s2206_infoceletista_dados['tpregjor'] = infoCeletista.tpRegJor.cdata
            except AttributeError: pass
            try: s2206_infoceletista_dados['natatividade'] = infoCeletista.natAtividade.cdata
            except AttributeError: pass
            try: s2206_infoceletista_dados['dtbase'] = infoCeletista.dtBase.cdata
            except AttributeError: pass
            try: s2206_infoceletista_dados['cnpjsindcategprof'] = infoCeletista.cnpjSindCategProf.cdata
            except AttributeError: pass
            insert = create_insert('s2206_infoceletista', s2206_infoceletista_dados)
            resp = executar_sql(insert, True)
            s2206_infoceletista_id = resp[0][0]
            #print s2206_infoceletista_id

            if 'trabTemp' in dir(infoCeletista) and infoCeletista.trabTemp.cdata != '':
                for trabTemp in infoCeletista.trabTemp:
                    s2206_trabtemp_dados = {}
                    s2206_trabtemp_dados['s2206_infoceletista_id'] = s2206_infoceletista_id

                    try: s2206_trabtemp_dados['justprorr'] = trabTemp.justProrr.cdata
                    except AttributeError: pass
                    insert = create_insert('s2206_trabtemp', s2206_trabtemp_dados)
                    resp = executar_sql(insert, True)
                    s2206_trabtemp_id = resp[0][0]
                    #print s2206_trabtemp_id

            if 'aprend' in dir(infoCeletista) and infoCeletista.aprend.cdata != '':
                for aprend in infoCeletista.aprend:
                    s2206_aprend_dados = {}
                    s2206_aprend_dados['s2206_infoceletista_id'] = s2206_infoceletista_id

                    try: s2206_aprend_dados['tpinsc'] = aprend.tpInsc.cdata
                    except AttributeError: pass
                    try: s2206_aprend_dados['nrinsc'] = aprend.nrInsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s2206_aprend', s2206_aprend_dados)
                    resp = executar_sql(insert, True)
                    s2206_aprend_id = resp[0][0]
                    #print s2206_aprend_id

    if 'infoEstatutario' in dir(evtAltContratual.altContratual.infoRegimeTrab) and evtAltContratual.altContratual.infoRegimeTrab.infoEstatutario.cdata != '':
        for infoEstatutario in evtAltContratual.altContratual.infoRegimeTrab.infoEstatutario:
            s2206_infoestatutario_dados = {}
            s2206_infoestatutario_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id

            try: s2206_infoestatutario_dados['tpplanrp'] = infoEstatutario.tpPlanRP.cdata
            except AttributeError: pass
            try: s2206_infoestatutario_dados['indtetorgps'] = infoEstatutario.indTetoRGPS.cdata
            except AttributeError: pass
            try: s2206_infoestatutario_dados['indabonoperm'] = infoEstatutario.indAbonoPerm.cdata
            except AttributeError: pass
            try: s2206_infoestatutario_dados['indparcremun'] = infoEstatutario.indParcRemun.cdata
            except AttributeError: pass
            insert = create_insert('s2206_infoestatutario', s2206_infoestatutario_dados)
            resp = executar_sql(insert, True)
            s2206_infoestatutario_id = resp[0][0]
            #print s2206_infoestatutario_id

    if 'localTrabGeral' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho) and evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabGeral.cdata != '':
        for localTrabGeral in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabGeral:
            s2206_localtrabgeral_dados = {}
            s2206_localtrabgeral_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id

            try: s2206_localtrabgeral_dados['tpinsc'] = localTrabGeral.tpInsc.cdata
            except AttributeError: pass
            try: s2206_localtrabgeral_dados['nrinsc'] = localTrabGeral.nrInsc.cdata
            except AttributeError: pass
            try: s2206_localtrabgeral_dados['desccomp'] = localTrabGeral.descComp.cdata
            except AttributeError: pass
            insert = create_insert('s2206_localtrabgeral', s2206_localtrabgeral_dados)
            resp = executar_sql(insert, True)
            s2206_localtrabgeral_id = resp[0][0]
            #print s2206_localtrabgeral_id

    if 'localTrabDom' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho) and evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabDom.cdata != '':
        for localTrabDom in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabDom:
            s2206_localtrabdom_dados = {}
            s2206_localtrabdom_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id

            try: s2206_localtrabdom_dados['tplograd'] = localTrabDom.tpLograd.cdata
            except AttributeError: pass
            try: s2206_localtrabdom_dados['dsclograd'] = localTrabDom.dscLograd.cdata
            except AttributeError: pass
            try: s2206_localtrabdom_dados['nrlograd'] = localTrabDom.nrLograd.cdata
            except AttributeError: pass
            try: s2206_localtrabdom_dados['complemento'] = localTrabDom.complemento.cdata
            except AttributeError: pass
            try: s2206_localtrabdom_dados['bairro'] = localTrabDom.bairro.cdata
            except AttributeError: pass
            try: s2206_localtrabdom_dados['cep'] = localTrabDom.cep.cdata
            except AttributeError: pass
            try: s2206_localtrabdom_dados['codmunic'] = localTrabDom.codMunic.cdata
            except AttributeError: pass
            try: s2206_localtrabdom_dados['uf'] = localTrabDom.uf.cdata
            except AttributeError: pass
            insert = create_insert('s2206_localtrabdom', s2206_localtrabdom_dados)
            resp = executar_sql(insert, True)
            s2206_localtrabdom_id = resp[0][0]
            #print s2206_localtrabdom_id

    if 'horContratual' in dir(evtAltContratual.altContratual.infoContrato) and evtAltContratual.altContratual.infoContrato.horContratual.cdata != '':
        for horContratual in evtAltContratual.altContratual.infoContrato.horContratual:
            s2206_horcontratual_dados = {}
            s2206_horcontratual_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id

            try: s2206_horcontratual_dados['qtdhrssem'] = horContratual.qtdHrsSem.cdata
            except AttributeError: pass
            try: s2206_horcontratual_dados['tpjornada'] = horContratual.tpJornada.cdata
            except AttributeError: pass
            try: s2206_horcontratual_dados['dsctpjorn'] = horContratual.dscTpJorn.cdata
            except AttributeError: pass
            try: s2206_horcontratual_dados['tmpparc'] = horContratual.tmpParc.cdata
            except AttributeError: pass
            insert = create_insert('s2206_horcontratual', s2206_horcontratual_dados)
            resp = executar_sql(insert, True)
            s2206_horcontratual_id = resp[0][0]
            #print s2206_horcontratual_id

            if 'horario' in dir(horContratual) and horContratual.horario.cdata != '':
                for horario in horContratual.horario:
                    s2206_horario_dados = {}
                    s2206_horario_dados['s2206_horcontratual_id'] = s2206_horcontratual_id

                    try: s2206_horario_dados['dia'] = horario.dia.cdata
                    except AttributeError: pass
                    try: s2206_horario_dados['codhorcontrat'] = horario.codHorContrat.cdata
                    except AttributeError: pass
                    insert = create_insert('s2206_horario', s2206_horario_dados)
                    resp = executar_sql(insert, True)
                    s2206_horario_id = resp[0][0]
                    #print s2206_horario_id

    if 'filiacaoSindical' in dir(evtAltContratual.altContratual.infoContrato) and evtAltContratual.altContratual.infoContrato.filiacaoSindical.cdata != '':
        for filiacaoSindical in evtAltContratual.altContratual.infoContrato.filiacaoSindical:
            s2206_filiacaosindical_dados = {}
            s2206_filiacaosindical_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id

            try: s2206_filiacaosindical_dados['cnpjsindtrab'] = filiacaoSindical.cnpjSindTrab.cdata
            except AttributeError: pass
            insert = create_insert('s2206_filiacaosindical', s2206_filiacaosindical_dados)
            resp = executar_sql(insert, True)
            s2206_filiacaosindical_id = resp[0][0]
            #print s2206_filiacaosindical_id

    if 'alvaraJudicial' in dir(evtAltContratual.altContratual.infoContrato) and evtAltContratual.altContratual.infoContrato.alvaraJudicial.cdata != '':
        for alvaraJudicial in evtAltContratual.altContratual.infoContrato.alvaraJudicial:
            s2206_alvarajudicial_dados = {}
            s2206_alvarajudicial_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id

            try: s2206_alvarajudicial_dados['nrprocjud'] = alvaraJudicial.nrProcJud.cdata
            except AttributeError: pass
            insert = create_insert('s2206_alvarajudicial', s2206_alvarajudicial_dados)
            resp = executar_sql(insert, True)
            s2206_alvarajudicial_id = resp[0][0]
            #print s2206_alvarajudicial_id

    if 'observacoes' in dir(evtAltContratual.altContratual.infoContrato) and evtAltContratual.altContratual.infoContrato.observacoes.cdata != '':
        for observacoes in evtAltContratual.altContratual.infoContrato.observacoes:
            s2206_observacoes_dados = {}
            s2206_observacoes_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id

            try: s2206_observacoes_dados['observacao'] = observacoes.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2206_observacoes', s2206_observacoes_dados)
            resp = executar_sql(insert, True)
            s2206_observacoes_id = resp[0][0]
            #print s2206_observacoes_id

    if 'servPubl' in dir(evtAltContratual.altContratual.infoContrato) and evtAltContratual.altContratual.infoContrato.servPubl.cdata != '':
        for servPubl in evtAltContratual.altContratual.infoContrato.servPubl:
            s2206_servpubl_dados = {}
            s2206_servpubl_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id

            try: s2206_servpubl_dados['mtvalter'] = servPubl.mtvAlter.cdata
            except AttributeError: pass
            insert = create_insert('s2206_servpubl', s2206_servpubl_dados)
            resp = executar_sql(insert, True)
            s2206_servpubl_id = resp[0][0]
            #print s2206_servpubl_id

    from emensageriapro.esocial.views.s2206_evtaltcontratual_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2206_evtaltcontratual_id, 'default')
    return dados