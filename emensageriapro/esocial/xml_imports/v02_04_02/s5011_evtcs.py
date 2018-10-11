#coding:utf-8
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
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql


def read_s5011_evtcs(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s5011_evtcs_obj(doc, status)



def read_s5011_evtcs_obj(doc):
    s5011_evtcs_dados = {}
    s5011_evtcs_dados['versao'] = 'v02_04_02'
    s5011_evtcs_dados['status'] = status
    s5011_evtcs_dados['identidade'] = doc.eSocial.evtCS['Id']
    s5011_evtcs_dados['processamento_codigo_resposta'] = 1
    evtCS = doc.eSocial.evtCS
    
    if 'indApuracao' in dir(evtCS.ideEvento): s5011_evtcs_dados['indapuracao'] = evtCS.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtCS.ideEvento): s5011_evtcs_dados['perapur'] = evtCS.ideEvento.perApur.cdata
    if 'tpInsc' in dir(evtCS.ideEmpregador): s5011_evtcs_dados['tpinsc'] = evtCS.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtCS.ideEmpregador): s5011_evtcs_dados['nrinsc'] = evtCS.ideEmpregador.nrInsc.cdata
    if 'nrRecArqBase' in dir(evtCS.infoCS): s5011_evtcs_dados['nrrecarqbase'] = evtCS.infoCS.nrRecArqBase.cdata
    if 'indExistInfo' in dir(evtCS.infoCS): s5011_evtcs_dados['indexistinfo'] = evtCS.infoCS.indExistInfo.cdata
    if 'classTrib' in dir(evtCS.infoCS.infoContrib): s5011_evtcs_dados['classtrib'] = evtCS.infoCS.infoContrib.classTrib.cdata
    if 'inclusao' in dir(evtCS.infoCS): s5011_evtcs_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCS.infoCS): s5011_evtcs_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCS.infoCS): s5011_evtcs_dados['operacao'] = 3
    #print dados
    insert = create_insert('s5011_evtcs', s5011_evtcs_dados)
    resp = executar_sql(insert, True)
    s5011_evtcs_id = resp[0][0]
    dados = s5011_evtcs_dados
    dados['evento'] = 's5011'
    dados['id'] = s5011_evtcs_id
    dados['identidade_evento'] = doc.eSocial.evtCS['Id']
    dados['status'] = 1

    if 'infoCPSeg' in dir(evtCS.infoCS):
        for infoCPSeg in evtCS.infoCS.infoCPSeg:
            s5011_infocpseg_dados = {}
            s5011_infocpseg_dados['s5011_evtcs_id'] = s5011_evtcs_id
            
            if 'vrDescCP' in dir(infoCPSeg): s5011_infocpseg_dados['vrdesccp'] = infoCPSeg.vrDescCP.cdata
            if 'vrCpSeg' in dir(infoCPSeg): s5011_infocpseg_dados['vrcpseg'] = infoCPSeg.vrCpSeg.cdata
            insert = create_insert('s5011_infocpseg', s5011_infocpseg_dados)
            resp = executar_sql(insert, True)
            s5011_infocpseg_id = resp[0][0]
            #print s5011_infocpseg_id

    if 'infoPJ' in dir(evtCS.infoCS.infoContrib):
        for infoPJ in evtCS.infoCS.infoContrib.infoPJ:
            s5011_infopj_dados = {}
            s5011_infopj_dados['s5011_evtcs_id'] = s5011_evtcs_id
            
            if 'indCoop' in dir(infoPJ): s5011_infopj_dados['indcoop'] = infoPJ.indCoop.cdata
            if 'indConstr' in dir(infoPJ): s5011_infopj_dados['indconstr'] = infoPJ.indConstr.cdata
            if 'indSubstPatr' in dir(infoPJ): s5011_infopj_dados['indsubstpatr'] = infoPJ.indSubstPatr.cdata
            if 'percRedContrib' in dir(infoPJ): s5011_infopj_dados['percredcontrib'] = infoPJ.percRedContrib.cdata
            insert = create_insert('s5011_infopj', s5011_infopj_dados)
            resp = executar_sql(insert, True)
            s5011_infopj_id = resp[0][0]
            #print s5011_infopj_id

            if 'infoAtConc' in dir(infoPJ):
                for infoAtConc in infoPJ.infoAtConc:
                    s5011_infoatconc_dados = {}
                    s5011_infoatconc_dados['s5011_infopj_id'] = s5011_infopj_id
                    
                    if 'fatorMes' in dir(infoAtConc): s5011_infoatconc_dados['fatormes'] = infoAtConc.fatorMes.cdata
                    if 'fator13' in dir(infoAtConc): s5011_infoatconc_dados['fator13'] = infoAtConc.fator13.cdata
                    insert = create_insert('s5011_infoatconc', s5011_infoatconc_dados)
                    resp = executar_sql(insert, True)
                    s5011_infoatconc_id = resp[0][0]
                    #print s5011_infoatconc_id
        
    if 'ideEstab' in dir(evtCS.infoCS):
        for ideEstab in evtCS.infoCS.ideEstab:
            s5011_ideestab_dados = {}
            s5011_ideestab_dados['s5011_evtcs_id'] = s5011_evtcs_id
            
            if 'tpInsc' in dir(ideEstab): s5011_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
            if 'nrInsc' in dir(ideEstab): s5011_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
            insert = create_insert('s5011_ideestab', s5011_ideestab_dados)
            resp = executar_sql(insert, True)
            s5011_ideestab_id = resp[0][0]
            #print s5011_ideestab_id

            if 'infoEstab' in dir(ideEstab):
                for infoEstab in ideEstab.infoEstab:
                    s5011_infoestab_dados = {}
                    s5011_infoestab_dados['s5011_ideestab_id'] = s5011_ideestab_id
                    
                    if 'cnaePrep' in dir(infoEstab): s5011_infoestab_dados['cnaeprep'] = infoEstab.cnaePrep.cdata
                    if 'aliqRat' in dir(infoEstab): s5011_infoestab_dados['aliqrat'] = infoEstab.aliqRat.cdata
                    if 'fap' in dir(infoEstab): s5011_infoestab_dados['fap'] = infoEstab.fap.cdata
                    if 'aliqRatAjust' in dir(infoEstab): s5011_infoestab_dados['aliqratajust'] = infoEstab.aliqRatAjust.cdata
                    insert = create_insert('s5011_infoestab', s5011_infoestab_dados)
                    resp = executar_sql(insert, True)
                    s5011_infoestab_id = resp[0][0]
                    #print s5011_infoestab_id
        
            if 'ideLotacao' in dir(ideEstab):
                for ideLotacao in ideEstab.ideLotacao:
                    s5011_idelotacao_dados = {}
                    s5011_idelotacao_dados['s5011_ideestab_id'] = s5011_ideestab_id
                    
                    if 'codLotacao' in dir(ideLotacao): s5011_idelotacao_dados['codlotacao'] = ideLotacao.codLotacao.cdata
                    if 'fpas' in dir(ideLotacao): s5011_idelotacao_dados['fpas'] = ideLotacao.fpas.cdata
                    if 'codTercs' in dir(ideLotacao): s5011_idelotacao_dados['codtercs'] = ideLotacao.codTercs.cdata
                    if 'codTercsSusp' in dir(ideLotacao): s5011_idelotacao_dados['codtercssusp'] = ideLotacao.codTercsSusp.cdata
                    insert = create_insert('s5011_idelotacao', s5011_idelotacao_dados)
                    resp = executar_sql(insert, True)
                    s5011_idelotacao_id = resp[0][0]
                    #print s5011_idelotacao_id
        
            if 'basesAquis' in dir(ideEstab):
                for basesAquis in ideEstab.basesAquis:
                    s5011_basesaquis_dados = {}
                    s5011_basesaquis_dados['s5011_ideestab_id'] = s5011_ideestab_id
                    
                    if 'indAquis' in dir(basesAquis): s5011_basesaquis_dados['indaquis'] = basesAquis.indAquis.cdata
                    if 'vlrAquis' in dir(basesAquis): s5011_basesaquis_dados['vlraquis'] = basesAquis.vlrAquis.cdata
                    if 'vrCPDescPR' in dir(basesAquis): s5011_basesaquis_dados['vrcpdescpr'] = basesAquis.vrCPDescPR.cdata
                    if 'vrCPNRet' in dir(basesAquis): s5011_basesaquis_dados['vrcpnret'] = basesAquis.vrCPNRet.cdata
                    if 'vrRatNRet' in dir(basesAquis): s5011_basesaquis_dados['vrratnret'] = basesAquis.vrRatNRet.cdata
                    if 'vrSenarNRet' in dir(basesAquis): s5011_basesaquis_dados['vrsenarnret'] = basesAquis.vrSenarNRet.cdata
                    if 'vrCPCalcPR' in dir(basesAquis): s5011_basesaquis_dados['vrcpcalcpr'] = basesAquis.vrCPCalcPR.cdata
                    if 'vrRatDescPR' in dir(basesAquis): s5011_basesaquis_dados['vrratdescpr'] = basesAquis.vrRatDescPR.cdata
                    if 'vrRatCalcPR' in dir(basesAquis): s5011_basesaquis_dados['vrratcalcpr'] = basesAquis.vrRatCalcPR.cdata
                    if 'vrSenarDesc' in dir(basesAquis): s5011_basesaquis_dados['vrsenardesc'] = basesAquis.vrSenarDesc.cdata
                    if 'vrSenarCalc' in dir(basesAquis): s5011_basesaquis_dados['vrsenarcalc'] = basesAquis.vrSenarCalc.cdata
                    insert = create_insert('s5011_basesaquis', s5011_basesaquis_dados)
                    resp = executar_sql(insert, True)
                    s5011_basesaquis_id = resp[0][0]
                    #print s5011_basesaquis_id
        
            if 'basesComerc' in dir(ideEstab):
                for basesComerc in ideEstab.basesComerc:
                    s5011_basescomerc_dados = {}
                    s5011_basescomerc_dados['s5011_ideestab_id'] = s5011_ideestab_id
                    
                    if 'indComerc' in dir(basesComerc): s5011_basescomerc_dados['indcomerc'] = basesComerc.indComerc.cdata
                    if 'vrBcComPR' in dir(basesComerc): s5011_basescomerc_dados['vrbccompr'] = basesComerc.vrBcComPR.cdata
                    if 'vrCPSusp' in dir(basesComerc): s5011_basescomerc_dados['vrcpsusp'] = basesComerc.vrCPSusp.cdata
                    if 'vrRatSusp' in dir(basesComerc): s5011_basescomerc_dados['vrratsusp'] = basesComerc.vrRatSusp.cdata
                    if 'vrSenarSusp' in dir(basesComerc): s5011_basescomerc_dados['vrsenarsusp'] = basesComerc.vrSenarSusp.cdata
                    insert = create_insert('s5011_basescomerc', s5011_basescomerc_dados)
                    resp = executar_sql(insert, True)
                    s5011_basescomerc_id = resp[0][0]
                    #print s5011_basescomerc_id
        
            if 'infoCREstab' in dir(ideEstab):
                for infoCREstab in ideEstab.infoCREstab:
                    s5011_infocrestab_dados = {}
                    s5011_infocrestab_dados['s5011_ideestab_id'] = s5011_ideestab_id
                    
                    if 'tpCR' in dir(infoCREstab): s5011_infocrestab_dados['tpcr'] = infoCREstab.tpCR.cdata
                    if 'vrCR' in dir(infoCREstab): s5011_infocrestab_dados['vrcr'] = infoCREstab.vrCR.cdata
                    if 'vrSuspCR' in dir(infoCREstab): s5011_infocrestab_dados['vrsuspcr'] = infoCREstab.vrSuspCR.cdata
                    insert = create_insert('s5011_infocrestab', s5011_infocrestab_dados)
                    resp = executar_sql(insert, True)
                    s5011_infocrestab_id = resp[0][0]
                    #print s5011_infocrestab_id
        
    if 'infoCRContrib' in dir(evtCS.infoCS):
        for infoCRContrib in evtCS.infoCS.infoCRContrib:
            s5011_infocrcontrib_dados = {}
            s5011_infocrcontrib_dados['s5011_evtcs_id'] = s5011_evtcs_id
            
            if 'tpCR' in dir(infoCRContrib): s5011_infocrcontrib_dados['tpcr'] = infoCRContrib.tpCR.cdata
            if 'vrCR' in dir(infoCRContrib): s5011_infocrcontrib_dados['vrcr'] = infoCRContrib.vrCR.cdata
            if 'vrCRSusp' in dir(infoCRContrib): s5011_infocrcontrib_dados['vrcrsusp'] = infoCRContrib.vrCRSusp.cdata
            insert = create_insert('s5011_infocrcontrib', s5011_infocrcontrib_dados)
            resp = executar_sql(insert, True)
            s5011_infocrcontrib_id = resp[0][0]
            #print s5011_infocrcontrib_id

    from emensageriapro.esocial.views.s5011_evtcs_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5011_evtcs_id, 'default')
    return dados