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


def read_s2206_evtaltcontratual_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2206_evtaltcontratual_obj(doc, status, validar)
    return dados

def read_s2206_evtaltcontratual(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2206_evtaltcontratual_obj(doc, status, validar)
    return dados



def read_s2206_evtaltcontratual_obj(doc, status, validar=False):
    s2206_evtaltcontratual_dados = {}
    s2206_evtaltcontratual_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2206_evtaltcontratual_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2206_evtaltcontratual_dados['identidade'] = doc.eSocial.evtAltContratual['Id']
    s2206_evtaltcontratual_dados['processamento_codigo_resposta'] = 1
    evtAltContratual = doc.eSocial.evtAltContratual

    if 'indRetif' in dir(evtAltContratual.ideEvento): s2206_evtaltcontratual_dados['indretif'] = evtAltContratual.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAltContratual.ideEvento): s2206_evtaltcontratual_dados['nrrecibo'] = evtAltContratual.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtAltContratual.ideEvento): s2206_evtaltcontratual_dados['tpamb'] = evtAltContratual.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAltContratual.ideEvento): s2206_evtaltcontratual_dados['procemi'] = evtAltContratual.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAltContratual.ideEvento): s2206_evtaltcontratual_dados['verproc'] = evtAltContratual.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAltContratual.ideEmpregador): s2206_evtaltcontratual_dados['tpinsc'] = evtAltContratual.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAltContratual.ideEmpregador): s2206_evtaltcontratual_dados['nrinsc'] = evtAltContratual.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtAltContratual.ideVinculo): s2206_evtaltcontratual_dados['cpftrab'] = evtAltContratual.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtAltContratual.ideVinculo): s2206_evtaltcontratual_dados['nistrab'] = evtAltContratual.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtAltContratual.ideVinculo): s2206_evtaltcontratual_dados['matricula'] = evtAltContratual.ideVinculo.matricula.cdata
    if 'dtAlteracao' in dir(evtAltContratual.altContratual): s2206_evtaltcontratual_dados['dtalteracao'] = evtAltContratual.altContratual.dtAlteracao.cdata
    if 'dtEf' in dir(evtAltContratual.altContratual): s2206_evtaltcontratual_dados['dtef'] = evtAltContratual.altContratual.dtEf.cdata
    if 'dscAlt' in dir(evtAltContratual.altContratual): s2206_evtaltcontratual_dados['dscalt'] = evtAltContratual.altContratual.dscAlt.cdata
    if 'tpRegPrev' in dir(evtAltContratual.altContratual.vinculo): s2206_evtaltcontratual_dados['tpregprev'] = evtAltContratual.altContratual.vinculo.tpRegPrev.cdata
    if 'codCargo' in dir(evtAltContratual.altContratual.infoContrato): s2206_evtaltcontratual_dados['codcargo'] = evtAltContratual.altContratual.infoContrato.codCargo.cdata
    if 'codFuncao' in dir(evtAltContratual.altContratual.infoContrato): s2206_evtaltcontratual_dados['codfuncao'] = evtAltContratual.altContratual.infoContrato.codFuncao.cdata
    if 'codCateg' in dir(evtAltContratual.altContratual.infoContrato): s2206_evtaltcontratual_dados['codcateg'] = evtAltContratual.altContratual.infoContrato.codCateg.cdata
    if 'codCarreira' in dir(evtAltContratual.altContratual.infoContrato): s2206_evtaltcontratual_dados['codcarreira'] = evtAltContratual.altContratual.infoContrato.codCarreira.cdata
    if 'dtIngrCarr' in dir(evtAltContratual.altContratual.infoContrato): s2206_evtaltcontratual_dados['dtingrcarr'] = evtAltContratual.altContratual.infoContrato.dtIngrCarr.cdata
    if 'vrSalFx' in dir(evtAltContratual.altContratual.infoContrato.remuneracao): s2206_evtaltcontratual_dados['vrsalfx'] = evtAltContratual.altContratual.infoContrato.remuneracao.vrSalFx.cdata
    if 'undSalFixo' in dir(evtAltContratual.altContratual.infoContrato.remuneracao): s2206_evtaltcontratual_dados['undsalfixo'] = evtAltContratual.altContratual.infoContrato.remuneracao.undSalFixo.cdata
    if 'dscSalVar' in dir(evtAltContratual.altContratual.infoContrato.remuneracao): s2206_evtaltcontratual_dados['dscsalvar'] = evtAltContratual.altContratual.infoContrato.remuneracao.dscSalVar.cdata
    if 'tpContr' in dir(evtAltContratual.altContratual.infoContrato.duracao): s2206_evtaltcontratual_dados['tpcontr'] = evtAltContratual.altContratual.infoContrato.duracao.tpContr.cdata
    if 'dtTerm' in dir(evtAltContratual.altContratual.infoContrato.duracao): s2206_evtaltcontratual_dados['dtterm'] = evtAltContratual.altContratual.infoContrato.duracao.dtTerm.cdata
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
    dados['status'] = 1

    if 'infoCeletista' in dir(evtAltContratual.altContratual.infoRegimeTrab):
        for infoCeletista in evtAltContratual.altContratual.infoRegimeTrab.infoCeletista:
            s2206_infoceletista_dados = {}
            s2206_infoceletista_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id
       
            if 'tpRegJor' in dir(infoCeletista): s2206_infoceletista_dados['tpregjor'] = infoCeletista.tpRegJor.cdata
            if 'natAtividade' in dir(infoCeletista): s2206_infoceletista_dados['natatividade'] = infoCeletista.natAtividade.cdata
            if 'dtBase' in dir(infoCeletista): s2206_infoceletista_dados['dtbase'] = infoCeletista.dtBase.cdata
            if 'cnpjSindCategProf' in dir(infoCeletista): s2206_infoceletista_dados['cnpjsindcategprof'] = infoCeletista.cnpjSindCategProf.cdata
            insert = create_insert('s2206_infoceletista', s2206_infoceletista_dados)
            resp = executar_sql(insert, True)
            s2206_infoceletista_id = resp[0][0]
            #print s2206_infoceletista_id

            if 'trabTemp' in dir(infoCeletista):
                for trabTemp in infoCeletista.trabTemp:
                    s2206_trabtemp_dados = {}
                    s2206_trabtemp_dados['s2206_infoceletista_id'] = s2206_infoceletista_id
               
                    if 'justProrr' in dir(trabTemp): s2206_trabtemp_dados['justprorr'] = trabTemp.justProrr.cdata
                    insert = create_insert('s2206_trabtemp', s2206_trabtemp_dados)
                    resp = executar_sql(insert, True)
                    s2206_trabtemp_id = resp[0][0]
                    #print s2206_trabtemp_id
   
            if 'aprend' in dir(infoCeletista):
                for aprend in infoCeletista.aprend:
                    s2206_aprend_dados = {}
                    s2206_aprend_dados['s2206_infoceletista_id'] = s2206_infoceletista_id
               
                    if 'tpInsc' in dir(aprend): s2206_aprend_dados['tpinsc'] = aprend.tpInsc.cdata
                    if 'nrInsc' in dir(aprend): s2206_aprend_dados['nrinsc'] = aprend.nrInsc.cdata
                    insert = create_insert('s2206_aprend', s2206_aprend_dados)
                    resp = executar_sql(insert, True)
                    s2206_aprend_id = resp[0][0]
                    #print s2206_aprend_id
   
    if 'infoEstatutario' in dir(evtAltContratual.altContratual.infoRegimeTrab):
        for infoEstatutario in evtAltContratual.altContratual.infoRegimeTrab.infoEstatutario:
            s2206_infoestatutario_dados = {}
            s2206_infoestatutario_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id
       
            if 'tpPlanRP' in dir(infoEstatutario): s2206_infoestatutario_dados['tpplanrp'] = infoEstatutario.tpPlanRP.cdata
            if 'indTetoRGPS' in dir(infoEstatutario): s2206_infoestatutario_dados['indtetorgps'] = infoEstatutario.indTetoRGPS.cdata
            if 'indAbonoPerm' in dir(infoEstatutario): s2206_infoestatutario_dados['indabonoperm'] = infoEstatutario.indAbonoPerm.cdata
            if 'indParcRemun' in dir(infoEstatutario): s2206_infoestatutario_dados['indparcremun'] = infoEstatutario.indParcRemun.cdata
            insert = create_insert('s2206_infoestatutario', s2206_infoestatutario_dados)
            resp = executar_sql(insert, True)
            s2206_infoestatutario_id = resp[0][0]
            #print s2206_infoestatutario_id

    if 'localTrabGeral' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):
        for localTrabGeral in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabGeral:
            s2206_localtrabgeral_dados = {}
            s2206_localtrabgeral_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id
       
            if 'tpInsc' in dir(localTrabGeral): s2206_localtrabgeral_dados['tpinsc'] = localTrabGeral.tpInsc.cdata
            if 'nrInsc' in dir(localTrabGeral): s2206_localtrabgeral_dados['nrinsc'] = localTrabGeral.nrInsc.cdata
            if 'descComp' in dir(localTrabGeral): s2206_localtrabgeral_dados['desccomp'] = localTrabGeral.descComp.cdata
            insert = create_insert('s2206_localtrabgeral', s2206_localtrabgeral_dados)
            resp = executar_sql(insert, True)
            s2206_localtrabgeral_id = resp[0][0]
            #print s2206_localtrabgeral_id

    if 'localTrabDom' in dir(evtAltContratual.altContratual.infoContrato.localTrabalho):
        for localTrabDom in evtAltContratual.altContratual.infoContrato.localTrabalho.localTrabDom:
            s2206_localtrabdom_dados = {}
            s2206_localtrabdom_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id
       
            if 'tpLograd' in dir(localTrabDom): s2206_localtrabdom_dados['tplograd'] = localTrabDom.tpLograd.cdata
            if 'dscLograd' in dir(localTrabDom): s2206_localtrabdom_dados['dsclograd'] = localTrabDom.dscLograd.cdata
            if 'nrLograd' in dir(localTrabDom): s2206_localtrabdom_dados['nrlograd'] = localTrabDom.nrLograd.cdata
            if 'complemento' in dir(localTrabDom): s2206_localtrabdom_dados['complemento'] = localTrabDom.complemento.cdata
            if 'bairro' in dir(localTrabDom): s2206_localtrabdom_dados['bairro'] = localTrabDom.bairro.cdata
            if 'cep' in dir(localTrabDom): s2206_localtrabdom_dados['cep'] = localTrabDom.cep.cdata
            if 'codMunic' in dir(localTrabDom): s2206_localtrabdom_dados['codmunic'] = localTrabDom.codMunic.cdata
            if 'uf' in dir(localTrabDom): s2206_localtrabdom_dados['uf'] = localTrabDom.uf.cdata
            insert = create_insert('s2206_localtrabdom', s2206_localtrabdom_dados)
            resp = executar_sql(insert, True)
            s2206_localtrabdom_id = resp[0][0]
            #print s2206_localtrabdom_id

    if 'horContratual' in dir(evtAltContratual.altContratual.infoContrato):
        for horContratual in evtAltContratual.altContratual.infoContrato.horContratual:
            s2206_horcontratual_dados = {}
            s2206_horcontratual_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id
       
            if 'qtdHrsSem' in dir(horContratual): s2206_horcontratual_dados['qtdhrssem'] = horContratual.qtdHrsSem.cdata
            if 'tpJornada' in dir(horContratual): s2206_horcontratual_dados['tpjornada'] = horContratual.tpJornada.cdata
            if 'dscTpJorn' in dir(horContratual): s2206_horcontratual_dados['dsctpjorn'] = horContratual.dscTpJorn.cdata
            if 'tmpParc' in dir(horContratual): s2206_horcontratual_dados['tmpparc'] = horContratual.tmpParc.cdata
            insert = create_insert('s2206_horcontratual', s2206_horcontratual_dados)
            resp = executar_sql(insert, True)
            s2206_horcontratual_id = resp[0][0]
            #print s2206_horcontratual_id

            if 'horario' in dir(horContratual):
                for horario in horContratual.horario:
                    s2206_horario_dados = {}
                    s2206_horario_dados['s2206_horcontratual_id'] = s2206_horcontratual_id
               
                    if 'dia' in dir(horario): s2206_horario_dados['dia'] = horario.dia.cdata
                    if 'codHorContrat' in dir(horario): s2206_horario_dados['codhorcontrat'] = horario.codHorContrat.cdata
                    insert = create_insert('s2206_horario', s2206_horario_dados)
                    resp = executar_sql(insert, True)
                    s2206_horario_id = resp[0][0]
                    #print s2206_horario_id
   
    if 'filiacaoSindical' in dir(evtAltContratual.altContratual.infoContrato):
        for filiacaoSindical in evtAltContratual.altContratual.infoContrato.filiacaoSindical:
            s2206_filiacaosindical_dados = {}
            s2206_filiacaosindical_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id
       
            if 'cnpjSindTrab' in dir(filiacaoSindical): s2206_filiacaosindical_dados['cnpjsindtrab'] = filiacaoSindical.cnpjSindTrab.cdata
            insert = create_insert('s2206_filiacaosindical', s2206_filiacaosindical_dados)
            resp = executar_sql(insert, True)
            s2206_filiacaosindical_id = resp[0][0]
            #print s2206_filiacaosindical_id

    if 'alvaraJudicial' in dir(evtAltContratual.altContratual.infoContrato):
        for alvaraJudicial in evtAltContratual.altContratual.infoContrato.alvaraJudicial:
            s2206_alvarajudicial_dados = {}
            s2206_alvarajudicial_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id
       
            if 'nrProcJud' in dir(alvaraJudicial): s2206_alvarajudicial_dados['nrprocjud'] = alvaraJudicial.nrProcJud.cdata
            insert = create_insert('s2206_alvarajudicial', s2206_alvarajudicial_dados)
            resp = executar_sql(insert, True)
            s2206_alvarajudicial_id = resp[0][0]
            #print s2206_alvarajudicial_id

    if 'observacoes' in dir(evtAltContratual.altContratual.infoContrato):
        for observacoes in evtAltContratual.altContratual.infoContrato.observacoes:
            s2206_observacoes_dados = {}
            s2206_observacoes_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id
       
            if 'observacao' in dir(observacoes): s2206_observacoes_dados['observacao'] = observacoes.observacao.cdata
            insert = create_insert('s2206_observacoes', s2206_observacoes_dados)
            resp = executar_sql(insert, True)
            s2206_observacoes_id = resp[0][0]
            #print s2206_observacoes_id

    if 'servPubl' in dir(evtAltContratual.altContratual.infoContrato):
        for servPubl in evtAltContratual.altContratual.infoContrato.servPubl:
            s2206_servpubl_dados = {}
            s2206_servpubl_dados['s2206_evtaltcontratual_id'] = s2206_evtaltcontratual_id
       
            if 'mtvAlter' in dir(servPubl): s2206_servpubl_dados['mtvalter'] = servPubl.mtvAlter.cdata
            insert = create_insert('s2206_servpubl', s2206_servpubl_dados)
            resp = executar_sql(insert, True)
            s2206_servpubl_id = resp[0][0]
            #print s2206_servpubl_id

    from emensageriapro.esocial.views.s2206_evtaltcontratual_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2206_evtaltcontratual_id, 'default')
    return dados