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


def read_s2240_evtexprisco_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2240_evtexprisco_obj(doc, status, validar)
    return dados

def read_s2240_evtexprisco(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s2240_evtexprisco_obj(doc, status, validar)
    return dados



def read_s2240_evtexprisco_obj(doc, status, validar=False):
    s2240_evtexprisco_dados = {}
    s2240_evtexprisco_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2240_evtexprisco_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2240_evtexprisco_dados['identidade'] = doc.eSocial.evtExpRisco['Id']
    s2240_evtexprisco_dados['processamento_codigo_resposta'] = 1
    evtExpRisco = doc.eSocial.evtExpRisco

    if 'indRetif' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['indretif'] = evtExpRisco.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['nrrecibo'] = evtExpRisco.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['tpamb'] = evtExpRisco.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['procemi'] = evtExpRisco.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['verproc'] = evtExpRisco.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtExpRisco.ideEmpregador): s2240_evtexprisco_dados['tpinsc'] = evtExpRisco.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtExpRisco.ideEmpregador): s2240_evtexprisco_dados['nrinsc'] = evtExpRisco.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtExpRisco.ideVinculo): s2240_evtexprisco_dados['cpftrab'] = evtExpRisco.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtExpRisco.ideVinculo): s2240_evtexprisco_dados['nistrab'] = evtExpRisco.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtExpRisco.ideVinculo): s2240_evtexprisco_dados['matricula'] = evtExpRisco.ideVinculo.matricula.cdata
    if 'codCateg' in dir(evtExpRisco.ideVinculo): s2240_evtexprisco_dados['codcateg'] = evtExpRisco.ideVinculo.codCateg.cdata
    if 'dtIniCondicao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['dtinicondicao'] = evtExpRisco.infoExpRisco.dtIniCondicao.cdata
    if 'dscAtivDes' in dir(evtExpRisco.infoExpRisco.infoAtiv): s2240_evtexprisco_dados['dscativdes'] = evtExpRisco.infoExpRisco.infoAtiv.dscAtivDes.cdata
    if 'inclusao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['operacao'] = 1
    elif 'alteracao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['operacao'] = 2
    elif 'exclusao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2240_evtexprisco', s2240_evtexprisco_dados)
    resp = executar_sql(insert, True)
    s2240_evtexprisco_id = resp[0][0]
    dados = s2240_evtexprisco_dados
    dados['evento'] = 's2240'
    dados['id'] = s2240_evtexprisco_id
    dados['identidade_evento'] = doc.eSocial.evtExpRisco['Id']
    dados['status'] = 1

    if 'infoAmb' in dir(evtExpRisco.infoExpRisco):
        for infoAmb in evtExpRisco.infoExpRisco.infoAmb:
            s2240_iniexprisco_infoamb_dados = {}
            s2240_iniexprisco_infoamb_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            if 'codAmb' in dir(infoAmb): s2240_iniexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
            insert = create_insert('s2240_iniexprisco_infoamb', s2240_iniexprisco_infoamb_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_infoamb_id = resp[0][0]
            #print s2240_iniexprisco_infoamb_id

    if 'ativPericInsal' in dir(evtExpRisco.infoExpRisco.infoAtiv):
        for ativPericInsal in evtExpRisco.infoExpRisco.infoAtiv.ativPericInsal:
            s2240_iniexprisco_ativpericinsal_dados = {}
            s2240_iniexprisco_ativpericinsal_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            if 'codAtiv' in dir(ativPericInsal): s2240_iniexprisco_ativpericinsal_dados['codativ'] = ativPericInsal.codAtiv.cdata
            insert = create_insert('s2240_iniexprisco_ativpericinsal', s2240_iniexprisco_ativpericinsal_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_ativpericinsal_id = resp[0][0]
            #print s2240_iniexprisco_ativpericinsal_id

    if 'fatRisco' in dir(evtExpRisco.infoExpRisco):
        for fatRisco in evtExpRisco.infoExpRisco.fatRisco:
            s2240_iniexprisco_fatrisco_dados = {}
            s2240_iniexprisco_fatrisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            if 'codFatRis' in dir(fatRisco): s2240_iniexprisco_fatrisco_dados['codfatris'] = fatRisco.codFatRis.cdata
            if 'tpAval' in dir(fatRisco): s2240_iniexprisco_fatrisco_dados['tpaval'] = fatRisco.tpAval.cdata
            if 'intConc' in dir(fatRisco): s2240_iniexprisco_fatrisco_dados['intconc'] = fatRisco.intConc.cdata
            if 'limTol' in dir(fatRisco): s2240_iniexprisco_fatrisco_dados['limtol'] = fatRisco.limTol.cdata
            if 'unMed' in dir(fatRisco): s2240_iniexprisco_fatrisco_dados['unmed'] = fatRisco.unMed.cdata
            if 'tecMedicao' in dir(fatRisco): s2240_iniexprisco_fatrisco_dados['tecmedicao'] = fatRisco.tecMedicao.cdata
            if 'insalubridade' in dir(fatRisco): s2240_iniexprisco_fatrisco_dados['insalubridade'] = fatRisco.insalubridade.cdata
            if 'periculosidade' in dir(fatRisco): s2240_iniexprisco_fatrisco_dados['periculosidade'] = fatRisco.periculosidade.cdata
            if 'aposentEsp' in dir(fatRisco): s2240_iniexprisco_fatrisco_dados['aposentesp'] = fatRisco.aposentEsp.cdata
            if 'utilizEPC' in dir(fatRisco.epcEpi): s2240_iniexprisco_fatrisco_dados['utilizepc'] = fatRisco.epcEpi.utilizEPC.cdata
            if 'eficEpc' in dir(fatRisco.epcEpi): s2240_iniexprisco_fatrisco_dados['eficepc'] = fatRisco.epcEpi.eficEpc.cdata
            if 'utilizEPI' in dir(fatRisco.epcEpi): s2240_iniexprisco_fatrisco_dados['utilizepi'] = fatRisco.epcEpi.utilizEPI.cdata
            insert = create_insert('s2240_iniexprisco_fatrisco', s2240_iniexprisco_fatrisco_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_fatrisco_id = resp[0][0]
            #print s2240_iniexprisco_fatrisco_id

            if 'epc' in dir(fatRisco.epcEpi):
                for epc in fatRisco.epcEpi.epc:
                    s2240_iniexprisco_epc_dados = {}
                    s2240_iniexprisco_epc_dados['s2240_iniexprisco_fatrisco_id'] = s2240_iniexprisco_fatrisco_id

                    if 'codEP' in dir(epc): s2240_iniexprisco_epc_dados['codep'] = epc.codEP.cdata
                    if 'dscEpc' in dir(epc): s2240_iniexprisco_epc_dados['dscepc'] = epc.dscEpc.cdata
                    if 'eficEpc' in dir(epc): s2240_iniexprisco_epc_dados['eficepc'] = epc.eficEpc.cdata
                    insert = create_insert('s2240_iniexprisco_epc', s2240_iniexprisco_epc_dados)
                    resp = executar_sql(insert, True)
                    s2240_iniexprisco_epc_id = resp[0][0]
                    #print s2240_iniexprisco_epc_id

            if 'epi' in dir(fatRisco.epcEpi):
                for epi in fatRisco.epcEpi.epi:
                    s2240_iniexprisco_epi_dados = {}
                    s2240_iniexprisco_epi_dados['s2240_iniexprisco_fatrisco_id'] = s2240_iniexprisco_fatrisco_id

                    if 'caEPI' in dir(epi): s2240_iniexprisco_epi_dados['caepi'] = epi.caEPI.cdata
                    if 'dscEPI' in dir(epi): s2240_iniexprisco_epi_dados['dscepi'] = epi.dscEPI.cdata
                    if 'eficEpi' in dir(epi): s2240_iniexprisco_epi_dados['eficepi'] = epi.eficEpi.cdata
                    if 'medProtecao' in dir(epi): s2240_iniexprisco_epi_dados['medprotecao'] = epi.medProtecao.cdata
                    if 'condFuncto' in dir(epi): s2240_iniexprisco_epi_dados['condfuncto'] = epi.condFuncto.cdata
                    if 'usoInint' in dir(epi): s2240_iniexprisco_epi_dados['usoinint'] = epi.usoInint.cdata
                    if 'przValid' in dir(epi): s2240_iniexprisco_epi_dados['przvalid'] = epi.przValid.cdata
                    if 'periodicTroca' in dir(epi): s2240_iniexprisco_epi_dados['periodictroca'] = epi.periodicTroca.cdata
                    if 'higienizacao' in dir(epi): s2240_iniexprisco_epi_dados['higienizacao'] = epi.higienizacao.cdata
                    insert = create_insert('s2240_iniexprisco_epi', s2240_iniexprisco_epi_dados)
                    resp = executar_sql(insert, True)
                    s2240_iniexprisco_epi_id = resp[0][0]
                    #print s2240_iniexprisco_epi_id

    if 'respReg' in dir(evtExpRisco.infoExpRisco):
        for respReg in evtExpRisco.infoExpRisco.respReg:
            s2240_iniexprisco_respreg_dados = {}
            s2240_iniexprisco_respreg_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            if 'cpfResp' in dir(respReg): s2240_iniexprisco_respreg_dados['cpfresp'] = respReg.cpfResp.cdata
            if 'nisResp' in dir(respReg): s2240_iniexprisco_respreg_dados['nisresp'] = respReg.nisResp.cdata
            if 'nmResp' in dir(respReg): s2240_iniexprisco_respreg_dados['nmresp'] = respReg.nmResp.cdata
            if 'ideOC' in dir(respReg): s2240_iniexprisco_respreg_dados['ideoc'] = respReg.ideOC.cdata
            if 'dscOC' in dir(respReg): s2240_iniexprisco_respreg_dados['dscoc'] = respReg.dscOC.cdata
            if 'nrOC' in dir(respReg): s2240_iniexprisco_respreg_dados['nroc'] = respReg.nrOC.cdata
            if 'ufOC' in dir(respReg): s2240_iniexprisco_respreg_dados['ufoc'] = respReg.ufOC.cdata
            insert = create_insert('s2240_iniexprisco_respreg', s2240_iniexprisco_respreg_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_respreg_id = resp[0][0]
            #print s2240_iniexprisco_respreg_id

    if 'obs' in dir(evtExpRisco.infoExpRisco):
        for obs in evtExpRisco.infoExpRisco.obs:
            s2240_iniexprisco_obs_dados = {}
            s2240_iniexprisco_obs_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            if 'metErg' in dir(obs): s2240_iniexprisco_obs_dados['meterg'] = obs.metErg.cdata
            if 'obsCompl' in dir(obs): s2240_iniexprisco_obs_dados['obscompl'] = obs.obsCompl.cdata
            if 'observacao' in dir(obs): s2240_iniexprisco_obs_dados['observacao'] = obs.observacao.cdata
            insert = create_insert('s2240_iniexprisco_obs', s2240_iniexprisco_obs_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_obs_id = resp[0][0]
            #print s2240_iniexprisco_obs_id

    if 'altExpRisco' in dir(evtExpRisco.infoExpRisco):
        for altExpRisco in evtExpRisco.infoExpRisco.altExpRisco:
            s2240_altexprisco_dados = {}
            s2240_altexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            if 'dtAltCondicao' in dir(altExpRisco): s2240_altexprisco_dados['dtaltcondicao'] = altExpRisco.dtAltCondicao.cdata
            insert = create_insert('s2240_altexprisco', s2240_altexprisco_dados)
            resp = executar_sql(insert, True)
            s2240_altexprisco_id = resp[0][0]
            #print s2240_altexprisco_id

            if 'infoAmb' in dir(altExpRisco):
                for infoAmb in altExpRisco.infoAmb:
                    s2240_altexprisco_infoamb_dados = {}
                    s2240_altexprisco_infoamb_dados['s2240_altexprisco_id'] = s2240_altexprisco_id

                    if 'codAmb' in dir(infoAmb): s2240_altexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    if 'dscAtivDes' in dir(infoAmb): s2240_altexprisco_infoamb_dados['dscativdes'] = infoAmb.infoAtiv.dscAtivDes.cdata
                    insert = create_insert('s2240_altexprisco_infoamb', s2240_altexprisco_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2240_altexprisco_infoamb_id = resp[0][0]
                    #print s2240_altexprisco_infoamb_id

    if 'fimExpRisco' in dir(evtExpRisco.infoExpRisco):
        for fimExpRisco in evtExpRisco.infoExpRisco.fimExpRisco:
            s2240_fimexprisco_dados = {}
            s2240_fimexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            if 'dtFimCondicao' in dir(fimExpRisco): s2240_fimexprisco_dados['dtfimcondicao'] = fimExpRisco.dtFimCondicao.cdata
            insert = create_insert('s2240_fimexprisco', s2240_fimexprisco_dados)
            resp = executar_sql(insert, True)
            s2240_fimexprisco_id = resp[0][0]
            #print s2240_fimexprisco_id

            if 'infoAmb' in dir(fimExpRisco):
                for infoAmb in fimExpRisco.infoAmb:
                    s2240_fimexprisco_infoamb_dados = {}
                    s2240_fimexprisco_infoamb_dados['s2240_fimexprisco_id'] = s2240_fimexprisco_id

                    if 'codAmb' in dir(infoAmb): s2240_fimexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    insert = create_insert('s2240_fimexprisco_infoamb', s2240_fimexprisco_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2240_fimexprisco_infoamb_id = resp[0][0]
                    #print s2240_fimexprisco_infoamb_id

    if 'respReg' in dir(evtExpRisco.infoExpRisco):
        for respReg in evtExpRisco.infoExpRisco.respReg:
            s2240_fimexprisco_respreg_dados = {}
            s2240_fimexprisco_respreg_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            if 'dtIni' in dir(respReg): s2240_fimexprisco_respreg_dados['dtini'] = respReg.dtIni.cdata
            if 'dtFim' in dir(respReg): s2240_fimexprisco_respreg_dados['dtfim'] = respReg.dtFim.cdata
            if 'nisResp' in dir(respReg): s2240_fimexprisco_respreg_dados['nisresp'] = respReg.nisResp.cdata
            if 'nrOc' in dir(respReg): s2240_fimexprisco_respreg_dados['nroc'] = respReg.nrOc.cdata
            if 'ufOC' in dir(respReg): s2240_fimexprisco_respreg_dados['ufoc'] = respReg.ufOC.cdata
            insert = create_insert('s2240_fimexprisco_respreg', s2240_fimexprisco_respreg_dados)
            resp = executar_sql(insert, True)
            s2240_fimexprisco_respreg_id = resp[0][0]
            #print s2240_fimexprisco_respreg_id

    from emensageriapro.esocial.views.s2240_evtexprisco_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2240_evtexprisco_id, 'default')
    return dados