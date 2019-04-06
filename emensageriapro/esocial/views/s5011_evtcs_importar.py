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



def read_s5011_evtcs_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5011_evtcs_obj(doc, status, validar)
    return dados

def read_s5011_evtcs(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s5011_evtcs_obj(doc, status, validar)
    return dados



def read_s5011_evtcs_obj(doc, status, validar=False):
    s5011_evtcs_dados = {}
    s5011_evtcs_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s5011_evtcs_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5011_evtcs_dados['identidade'] = doc.eSocial.evtCS['Id']
    evtCS = doc.eSocial.evtCS

    try: s5011_evtcs_dados['indapuracao'] = evtCS.ideEvento.indApuracao.cdata
    except AttributeError: pass
    try: s5011_evtcs_dados['perapur'] = evtCS.ideEvento.perApur.cdata
    except AttributeError: pass
    try: s5011_evtcs_dados['tpinsc'] = evtCS.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s5011_evtcs_dados['nrinsc'] = evtCS.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s5011_evtcs_dados['nrrecarqbase'] = evtCS.infoCS.nrRecArqBase.cdata
    except AttributeError: pass
    try: s5011_evtcs_dados['indexistinfo'] = evtCS.infoCS.indExistInfo.cdata
    except AttributeError: pass
    try: s5011_evtcs_dados['classtrib'] = evtCS.infoCS.infoContrib.classTrib.cdata
    except AttributeError: pass
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
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'infoCPSeg' in dir(evtCS.infoCS) and evtCS.infoCS.infoCPSeg.cdata != '':
        for infoCPSeg in evtCS.infoCS.infoCPSeg:
            s5011_infocpseg_dados = {}
            s5011_infocpseg_dados['s5011_evtcs_id'] = s5011_evtcs_id

            try: s5011_infocpseg_dados['vrdesccp'] = infoCPSeg.vrDescCP.cdata
            except AttributeError: pass
            try: s5011_infocpseg_dados['vrcpseg'] = infoCPSeg.vrCpSeg.cdata
            except AttributeError: pass
            insert = create_insert('s5011_infocpseg', s5011_infocpseg_dados)
            resp = executar_sql(insert, True)
            s5011_infocpseg_id = resp[0][0]
            #print s5011_infocpseg_id

    if 'infoPJ' in dir(evtCS.infoCS.infoContrib) and evtCS.infoCS.infoContrib.infoPJ.cdata != '':
        for infoPJ in evtCS.infoCS.infoContrib.infoPJ:
            s5011_infopj_dados = {}
            s5011_infopj_dados['s5011_evtcs_id'] = s5011_evtcs_id

            try: s5011_infopj_dados['indcoop'] = infoPJ.indCoop.cdata
            except AttributeError: pass
            try: s5011_infopj_dados['indconstr'] = infoPJ.indConstr.cdata
            except AttributeError: pass
            try: s5011_infopj_dados['indsubstpatr'] = infoPJ.indSubstPatr.cdata
            except AttributeError: pass
            try: s5011_infopj_dados['percredcontrib'] = infoPJ.percRedContrib.cdata
            except AttributeError: pass
            insert = create_insert('s5011_infopj', s5011_infopj_dados)
            resp = executar_sql(insert, True)
            s5011_infopj_id = resp[0][0]
            #print s5011_infopj_id

            if 'infoAtConc' in dir(infoPJ) and infoPJ.infoAtConc.cdata != '':
                for infoAtConc in infoPJ.infoAtConc:
                    s5011_infoatconc_dados = {}
                    s5011_infoatconc_dados['s5011_infopj_id'] = s5011_infopj_id

                    try: s5011_infoatconc_dados['fatormes'] = infoAtConc.fatorMes.cdata
                    except AttributeError: pass
                    try: s5011_infoatconc_dados['fator13'] = infoAtConc.fator13.cdata
                    except AttributeError: pass
                    insert = create_insert('s5011_infoatconc', s5011_infoatconc_dados)
                    resp = executar_sql(insert, True)
                    s5011_infoatconc_id = resp[0][0]
                    #print s5011_infoatconc_id

    if 'ideEstab' in dir(evtCS.infoCS) and evtCS.infoCS.ideEstab.cdata != '':
        for ideEstab in evtCS.infoCS.ideEstab:
            s5011_ideestab_dados = {}
            s5011_ideestab_dados['s5011_evtcs_id'] = s5011_evtcs_id

            try: s5011_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
            except AttributeError: pass
            try: s5011_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
            except AttributeError: pass
            insert = create_insert('s5011_ideestab', s5011_ideestab_dados)
            resp = executar_sql(insert, True)
            s5011_ideestab_id = resp[0][0]
            #print s5011_ideestab_id

            if 'infoEstab' in dir(ideEstab) and ideEstab.infoEstab.cdata != '':
                for infoEstab in ideEstab.infoEstab:
                    s5011_infoestab_dados = {}
                    s5011_infoestab_dados['s5011_ideestab_id'] = s5011_ideestab_id

                    try: s5011_infoestab_dados['cnaeprep'] = infoEstab.cnaePrep.cdata
                    except AttributeError: pass
                    try: s5011_infoestab_dados['aliqrat'] = infoEstab.aliqRat.cdata
                    except AttributeError: pass
                    try: s5011_infoestab_dados['fap'] = infoEstab.fap.cdata
                    except AttributeError: pass
                    try: s5011_infoestab_dados['aliqratajust'] = infoEstab.aliqRatAjust.cdata
                    except AttributeError: pass
                    insert = create_insert('s5011_infoestab', s5011_infoestab_dados)
                    resp = executar_sql(insert, True)
                    s5011_infoestab_id = resp[0][0]
                    #print s5011_infoestab_id

            if 'ideLotacao' in dir(ideEstab) and ideEstab.ideLotacao.cdata != '':
                for ideLotacao in ideEstab.ideLotacao:
                    s5011_idelotacao_dados = {}
                    s5011_idelotacao_dados['s5011_ideestab_id'] = s5011_ideestab_id

                    try: s5011_idelotacao_dados['codlotacao'] = ideLotacao.codLotacao.cdata
                    except AttributeError: pass
                    try: s5011_idelotacao_dados['fpas'] = ideLotacao.fpas.cdata
                    except AttributeError: pass
                    try: s5011_idelotacao_dados['codtercs'] = ideLotacao.codTercs.cdata
                    except AttributeError: pass
                    try: s5011_idelotacao_dados['codtercssusp'] = ideLotacao.codTercsSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('s5011_idelotacao', s5011_idelotacao_dados)
                    resp = executar_sql(insert, True)
                    s5011_idelotacao_id = resp[0][0]
                    #print s5011_idelotacao_id

            if 'basesAquis' in dir(ideEstab) and ideEstab.basesAquis.cdata != '':
                for basesAquis in ideEstab.basesAquis:
                    s5011_basesaquis_dados = {}
                    s5011_basesaquis_dados['s5011_ideestab_id'] = s5011_ideestab_id

                    try: s5011_basesaquis_dados['indaquis'] = basesAquis.indAquis.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vlraquis'] = basesAquis.vlrAquis.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vrcpdescpr'] = basesAquis.vrCPDescPR.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vrcpnret'] = basesAquis.vrCPNRet.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vrratnret'] = basesAquis.vrRatNRet.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vrsenarnret'] = basesAquis.vrSenarNRet.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vrcpcalcpr'] = basesAquis.vrCPCalcPR.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vrratdescpr'] = basesAquis.vrRatDescPR.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vrratcalcpr'] = basesAquis.vrRatCalcPR.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vrsenardesc'] = basesAquis.vrSenarDesc.cdata
                    except AttributeError: pass
                    try: s5011_basesaquis_dados['vrsenarcalc'] = basesAquis.vrSenarCalc.cdata
                    except AttributeError: pass
                    insert = create_insert('s5011_basesaquis', s5011_basesaquis_dados)
                    resp = executar_sql(insert, True)
                    s5011_basesaquis_id = resp[0][0]
                    #print s5011_basesaquis_id

            if 'basesComerc' in dir(ideEstab) and ideEstab.basesComerc.cdata != '':
                for basesComerc in ideEstab.basesComerc:
                    s5011_basescomerc_dados = {}
                    s5011_basescomerc_dados['s5011_ideestab_id'] = s5011_ideestab_id

                    try: s5011_basescomerc_dados['indcomerc'] = basesComerc.indComerc.cdata
                    except AttributeError: pass
                    try: s5011_basescomerc_dados['vrbccompr'] = basesComerc.vrBcComPR.cdata
                    except AttributeError: pass
                    try: s5011_basescomerc_dados['vrcpsusp'] = basesComerc.vrCPSusp.cdata
                    except AttributeError: pass
                    try: s5011_basescomerc_dados['vrratsusp'] = basesComerc.vrRatSusp.cdata
                    except AttributeError: pass
                    try: s5011_basescomerc_dados['vrsenarsusp'] = basesComerc.vrSenarSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('s5011_basescomerc', s5011_basescomerc_dados)
                    resp = executar_sql(insert, True)
                    s5011_basescomerc_id = resp[0][0]
                    #print s5011_basescomerc_id

            if 'infoCREstab' in dir(ideEstab) and ideEstab.infoCREstab.cdata != '':
                for infoCREstab in ideEstab.infoCREstab:
                    s5011_infocrestab_dados = {}
                    s5011_infocrestab_dados['s5011_ideestab_id'] = s5011_ideestab_id

                    try: s5011_infocrestab_dados['tpcr'] = infoCREstab.tpCR.cdata
                    except AttributeError: pass
                    try: s5011_infocrestab_dados['vrcr'] = infoCREstab.vrCR.cdata
                    except AttributeError: pass
                    try: s5011_infocrestab_dados['vrsuspcr'] = infoCREstab.vrSuspCR.cdata
                    except AttributeError: pass
                    insert = create_insert('s5011_infocrestab', s5011_infocrestab_dados)
                    resp = executar_sql(insert, True)
                    s5011_infocrestab_id = resp[0][0]
                    #print s5011_infocrestab_id

    if 'infoCRContrib' in dir(evtCS.infoCS) and evtCS.infoCS.infoCRContrib.cdata != '':
        for infoCRContrib in evtCS.infoCS.infoCRContrib:
            s5011_infocrcontrib_dados = {}
            s5011_infocrcontrib_dados['s5011_evtcs_id'] = s5011_evtcs_id

            try: s5011_infocrcontrib_dados['tpcr'] = infoCRContrib.tpCR.cdata
            except AttributeError: pass
            try: s5011_infocrcontrib_dados['vrcr'] = infoCRContrib.vrCR.cdata
            except AttributeError: pass
            try: s5011_infocrcontrib_dados['vrcrsusp'] = infoCRContrib.vrCRSusp.cdata
            except AttributeError: pass
            insert = create_insert('s5011_infocrcontrib', s5011_infocrcontrib_dados)
            resp = executar_sql(insert, True)
            s5011_infocrcontrib_id = resp[0][0]
            #print s5011_infocrcontrib_id

    from emensageriapro.esocial.views.s5011_evtcs_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5011_evtcs_id, 'default')
    return dados