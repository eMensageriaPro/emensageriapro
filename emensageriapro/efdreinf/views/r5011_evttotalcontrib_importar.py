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



def read_r5011_evttotalcontrib_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r5011_evttotalcontrib_obj(doc, status, validar)
    return dados

def read_r5011_evttotalcontrib(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r5011_evttotalcontrib_obj(doc, status, validar)
    return dados



def read_r5011_evttotalcontrib_obj(doc, status, validar=False):
    r5011_evttotalcontrib_dados = {}
    r5011_evttotalcontrib_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r5011_evttotalcontrib_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r5011_evttotalcontrib_dados['identidade'] = doc.Reinf.evtTotalContrib['id']
    evtTotalContrib = doc.Reinf.evtTotalContrib

    if 'perApur' in dir(evtTotalContrib.ideEvento): r5011_evttotalcontrib_dados['perapur'] = evtTotalContrib.ideEvento.perApur.cdata
    if 'tpInsc' in dir(evtTotalContrib.ideContri): r5011_evttotalcontrib_dados['tpinsc'] = evtTotalContrib.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtTotalContrib.ideContri): r5011_evttotalcontrib_dados['nrinsc'] = evtTotalContrib.ideContri.nrInsc.cdata
    if 'cdRetorno' in dir(evtTotalContrib.ideRecRetorno.ideStatus): r5011_evttotalcontrib_dados['cdretorno'] = evtTotalContrib.ideRecRetorno.ideStatus.cdRetorno.cdata
    if 'descRetorno' in dir(evtTotalContrib.ideRecRetorno.ideStatus): r5011_evttotalcontrib_dados['descretorno'] = evtTotalContrib.ideRecRetorno.ideStatus.descRetorno.cdata
    if 'nrProtEntr' in dir(evtTotalContrib.infoRecEv): r5011_evttotalcontrib_dados['nrprotentr'] = evtTotalContrib.infoRecEv.nrProtEntr.cdata
    if 'dhProcess' in dir(evtTotalContrib.infoRecEv): r5011_evttotalcontrib_dados['dhprocess'] = evtTotalContrib.infoRecEv.dhProcess.cdata
    if 'tpEv' in dir(evtTotalContrib.infoRecEv): r5011_evttotalcontrib_dados['tpev'] = evtTotalContrib.infoRecEv.tpEv.cdata
    if 'idEv' in dir(evtTotalContrib.infoRecEv): r5011_evttotalcontrib_dados['idev'] = evtTotalContrib.infoRecEv.idEv.cdata
    if 'hash' in dir(evtTotalContrib.infoRecEv): r5011_evttotalcontrib_dados['hash'] = evtTotalContrib.infoRecEv.hash.cdata
    if 'inclusao' in dir(evtTotalContrib.infoTotalContrib): r5011_evttotalcontrib_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTotalContrib.infoTotalContrib): r5011_evttotalcontrib_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTotalContrib.infoTotalContrib): r5011_evttotalcontrib_dados['operacao'] = 3
    #print dados
    insert = create_insert('r5011_evttotalcontrib', r5011_evttotalcontrib_dados)
    resp = executar_sql(insert, True)
    r5011_evttotalcontrib_id = resp[0][0]
    dados = r5011_evttotalcontrib_dados
    dados['evento'] = 'r5011'
    dados['id'] = r5011_evttotalcontrib_id
    dados['identidade_evento'] = doc.Reinf.evtTotalContrib['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'regOcorrs' in dir(evtTotalContrib.ideRecRetorno.ideStatus):
        for regOcorrs in evtTotalContrib.ideRecRetorno.ideStatus.regOcorrs:
            r5011_regocorrs_dados = {}
            r5011_regocorrs_dados['r5011_evttotalcontrib_id'] = r5011_evttotalcontrib_id

            if 'tpOcorr' in dir(regOcorrs): r5011_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            if 'localErroAviso' in dir(regOcorrs): r5011_regocorrs_dados['localerroaviso'] = regOcorrs.localErroAviso.cdata
            if 'codResp' in dir(regOcorrs): r5011_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            if 'dscResp' in dir(regOcorrs): r5011_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            insert = create_insert('r5011_regocorrs', r5011_regocorrs_dados)
            resp = executar_sql(insert, True)
            r5011_regocorrs_id = resp[0][0]
            #print r5011_regocorrs_id

    if 'infoTotalContrib' in dir(evtTotalContrib):
        for infoTotalContrib in evtTotalContrib.infoTotalContrib:
            r5011_infototalcontrib_dados = {}
            r5011_infototalcontrib_dados['r5011_evttotalcontrib_id'] = r5011_evttotalcontrib_id

            if 'nrRecArqBase' in dir(infoTotalContrib): r5011_infototalcontrib_dados['nrrecarqbase'] = infoTotalContrib.nrRecArqBase.cdata
            if 'indExistInfo' in dir(infoTotalContrib): r5011_infototalcontrib_dados['indexistinfo'] = infoTotalContrib.indExistInfo.cdata
            insert = create_insert('r5011_infototalcontrib', r5011_infototalcontrib_dados)
            resp = executar_sql(insert, True)
            r5011_infototalcontrib_id = resp[0][0]
            #print r5011_infototalcontrib_id

            if 'RTom' in dir(infoTotalContrib):
                for RTom in infoTotalContrib.RTom:
                    r5011_rtom_dados = {}
                    r5011_rtom_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'cnpjPrestador' in dir(RTom): r5011_rtom_dados['cnpjprestador'] = RTom.cnpjPrestador.cdata
                    if 'cno' in dir(RTom): r5011_rtom_dados['cno'] = RTom.cno.cdata
                    if 'vlrTotalBaseRet' in dir(RTom): r5011_rtom_dados['vlrtotalbaseret'] = RTom.vlrTotalBaseRet.cdata
                    insert = create_insert('r5011_rtom', r5011_rtom_dados)
                    resp = executar_sql(insert, True)
                    r5011_rtom_id = resp[0][0]
                    #print r5011_rtom_id

            if 'RPrest' in dir(infoTotalContrib):
                for RPrest in infoTotalContrib.RPrest:
                    r5011_rprest_dados = {}
                    r5011_rprest_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'tpInscTomador' in dir(RPrest): r5011_rprest_dados['tpinsctomador'] = RPrest.tpInscTomador.cdata
                    if 'nrInscTomador' in dir(RPrest): r5011_rprest_dados['nrinsctomador'] = RPrest.nrInscTomador.cdata
                    if 'vlrTotalBaseRet' in dir(RPrest): r5011_rprest_dados['vlrtotalbaseret'] = RPrest.vlrTotalBaseRet.cdata
                    if 'vlrTotalRetPrinc' in dir(RPrest): r5011_rprest_dados['vlrtotalretprinc'] = RPrest.vlrTotalRetPrinc.cdata
                    if 'vlrTotalRetAdic' in dir(RPrest): r5011_rprest_dados['vlrtotalretadic'] = RPrest.vlrTotalRetAdic.cdata
                    if 'vlrTotalNRetPrinc' in dir(RPrest): r5011_rprest_dados['vlrtotalnretprinc'] = RPrest.vlrTotalNRetPrinc.cdata
                    if 'vlrTotalNRetAdic' in dir(RPrest): r5011_rprest_dados['vlrtotalnretadic'] = RPrest.vlrTotalNRetAdic.cdata
                    insert = create_insert('r5011_rprest', r5011_rprest_dados)
                    resp = executar_sql(insert, True)
                    r5011_rprest_id = resp[0][0]
                    #print r5011_rprest_id

            if 'RRecRepAD' in dir(infoTotalContrib):
                for RRecRepAD in infoTotalContrib.RRecRepAD:
                    r5011_rrecrepad_dados = {}
                    r5011_rrecrepad_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'cnpjAssocDesp' in dir(RRecRepAD): r5011_rrecrepad_dados['cnpjassocdesp'] = RRecRepAD.cnpjAssocDesp.cdata
                    if 'vlrTotalRep' in dir(RRecRepAD): r5011_rrecrepad_dados['vlrtotalrep'] = RRecRepAD.vlrTotalRep.cdata
                    if 'CRRecRepAD' in dir(RRecRepAD): r5011_rrecrepad_dados['crrecrepad'] = RRecRepAD.CRRecRepAD.cdata
                    if 'vlrCRRecRepAD' in dir(RRecRepAD): r5011_rrecrepad_dados['vlrcrrecrepad'] = RRecRepAD.vlrCRRecRepAD.cdata
                    if 'vlrCRRecRepADSusp' in dir(RRecRepAD): r5011_rrecrepad_dados['vlrcrrecrepadsusp'] = RRecRepAD.vlrCRRecRepADSusp.cdata
                    insert = create_insert('r5011_rrecrepad', r5011_rrecrepad_dados)
                    resp = executar_sql(insert, True)
                    r5011_rrecrepad_id = resp[0][0]
                    #print r5011_rrecrepad_id

            if 'RComl' in dir(infoTotalContrib):
                for RComl in infoTotalContrib.RComl:
                    r5011_rcoml_dados = {}
                    r5011_rcoml_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'CRComl' in dir(RComl): r5011_rcoml_dados['crcoml'] = RComl.CRComl.cdata
                    if 'vlrCRComl' in dir(RComl): r5011_rcoml_dados['vlrcrcoml'] = RComl.vlrCRComl.cdata
                    if 'vlrCRComlSusp' in dir(RComl): r5011_rcoml_dados['vlrcrcomlsusp'] = RComl.vlrCRComlSusp.cdata
                    insert = create_insert('r5011_rcoml', r5011_rcoml_dados)
                    resp = executar_sql(insert, True)
                    r5011_rcoml_id = resp[0][0]
                    #print r5011_rcoml_id

            if 'RCPRB' in dir(infoTotalContrib):
                for RCPRB in infoTotalContrib.RCPRB:
                    r5011_rcprb_dados = {}
                    r5011_rcprb_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'CRCPRB' in dir(RCPRB): r5011_rcprb_dados['crcprb'] = RCPRB.CRCPRB.cdata
                    if 'vlrCRCPRB' in dir(RCPRB): r5011_rcprb_dados['vlrcrcprb'] = RCPRB.vlrCRCPRB.cdata
                    if 'vlrCRCPRBSusp' in dir(RCPRB): r5011_rcprb_dados['vlrcrcprbsusp'] = RCPRB.vlrCRCPRBSusp.cdata
                    insert = create_insert('r5011_rcprb', r5011_rcprb_dados)
                    resp = executar_sql(insert, True)
                    r5011_rcprb_id = resp[0][0]
                    #print r5011_rcprb_id

    from emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r5011_evttotalcontrib_id, 'default')
    return dados