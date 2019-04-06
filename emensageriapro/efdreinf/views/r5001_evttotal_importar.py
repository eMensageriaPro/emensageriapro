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



def read_r5001_evttotal_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r5001_evttotal_obj(doc, status, validar)
    return dados

def read_r5001_evttotal(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r5001_evttotal_obj(doc, status, validar)
    return dados



def read_r5001_evttotal_obj(doc, status, validar=False):
    r5001_evttotal_dados = {}
    r5001_evttotal_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r5001_evttotal_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r5001_evttotal_dados['identidade'] = doc.Reinf.evtTotal['id']
    evtTotal = doc.Reinf.evtTotal

    try: r5001_evttotal_dados['perapur'] = evtTotal.ideEvento.perApur.cdata
    except AttributeError: pass
    try: r5001_evttotal_dados['tpinsc'] = evtTotal.ideContri.tpInsc.cdata
    except AttributeError: pass
    try: r5001_evttotal_dados['nrinsc'] = evtTotal.ideContri.nrInsc.cdata
    except AttributeError: pass
    try: r5001_evttotal_dados['cdretorno'] = evtTotal.ideRecRetorno.ideStatus.cdRetorno.cdata
    except AttributeError: pass
    try: r5001_evttotal_dados['descretorno'] = evtTotal.ideRecRetorno.ideStatus.descRetorno.cdata
    except AttributeError: pass
    try: r5001_evttotal_dados['nrprotentr'] = evtTotal.infoRecEv.nrProtEntr.cdata
    except AttributeError: pass
    try: r5001_evttotal_dados['dhprocess'] = evtTotal.infoRecEv.dhProcess.cdata
    except AttributeError: pass
    try: r5001_evttotal_dados['tpev'] = evtTotal.infoRecEv.tpEv.cdata
    except AttributeError: pass
    try: r5001_evttotal_dados['idev'] = evtTotal.infoRecEv.idEv.cdata
    except AttributeError: pass
    try: r5001_evttotal_dados['hash'] = evtTotal.infoRecEv.hash.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtTotal.infoTotal): r5001_evttotal_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTotal.infoTotal): r5001_evttotal_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTotal.infoTotal): r5001_evttotal_dados['operacao'] = 3
    #print dados
    insert = create_insert('r5001_evttotal', r5001_evttotal_dados)
    resp = executar_sql(insert, True)
    r5001_evttotal_id = resp[0][0]
    dados = r5001_evttotal_dados
    dados['evento'] = 'r5001'
    dados['id'] = r5001_evttotal_id
    dados['identidade_evento'] = doc.Reinf.evtTotal['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'regOcorrs' in dir(evtTotal.ideRecRetorno.ideStatus) and evtTotal.ideRecRetorno.ideStatus.regOcorrs.cdata != '':
        for regOcorrs in evtTotal.ideRecRetorno.ideStatus.regOcorrs:
            r5001_regocorrs_dados = {}
            r5001_regocorrs_dados['r5001_evttotal_id'] = r5001_evttotal_id

            try: r5001_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            except AttributeError: pass
            try: r5001_regocorrs_dados['localerroaviso'] = regOcorrs.localErroAviso.cdata
            except AttributeError: pass
            try: r5001_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            except AttributeError: pass
            try: r5001_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            except AttributeError: pass
            insert = create_insert('r5001_regocorrs', r5001_regocorrs_dados)
            resp = executar_sql(insert, True)
            r5001_regocorrs_id = resp[0][0]
            #print r5001_regocorrs_id

    if 'infoTotal' in dir(evtTotal) and evtTotal.infoTotal.cdata != '':
        for infoTotal in evtTotal.infoTotal:
            r5001_infototal_dados = {}
            r5001_infototal_dados['r5001_evttotal_id'] = r5001_evttotal_id

            try: r5001_infototal_dados['nrrecarqbase'] = infoTotal.nrRecArqBase.cdata
            except AttributeError: pass
            try: r5001_infototal_dados['tpinsc'] = infoTotal.ideEstab.tpInsc.cdata
            except AttributeError: pass
            try: r5001_infototal_dados['nrinsc'] = infoTotal.ideEstab.nrInsc.cdata
            except AttributeError: pass
            insert = create_insert('r5001_infototal', r5001_infototal_dados)
            resp = executar_sql(insert, True)
            r5001_infototal_id = resp[0][0]
            #print r5001_infototal_id

            if 'RTom' in dir(infoTotal.ideEstab) and infoTotal.ideEstab.RTom.cdata != '':
                for RTom in infoTotal.ideEstab.RTom:
                    r5001_rtom_dados = {}
                    r5001_rtom_dados['r5001_infototal_id'] = r5001_infototal_id

                    try: r5001_rtom_dados['cnpjprestador'] = RTom.cnpjPrestador.cdata
                    except AttributeError: pass
                    try: r5001_rtom_dados['cno'] = RTom.cno.cdata
                    except AttributeError: pass
                    try: r5001_rtom_dados['vlrtotalbaseret'] = RTom.vlrTotalBaseRet.cdata
                    except AttributeError: pass
                    insert = create_insert('r5001_rtom', r5001_rtom_dados)
                    resp = executar_sql(insert, True)
                    r5001_rtom_id = resp[0][0]
                    #print r5001_rtom_id

            if 'RPrest' in dir(infoTotal.ideEstab) and infoTotal.ideEstab.RPrest.cdata != '':
                for RPrest in infoTotal.ideEstab.RPrest:
                    r5001_rprest_dados = {}
                    r5001_rprest_dados['r5001_infototal_id'] = r5001_infototal_id

                    try: r5001_rprest_dados['tpinsctomador'] = RPrest.tpInscTomador.cdata
                    except AttributeError: pass
                    try: r5001_rprest_dados['nrinsctomador'] = RPrest.nrInscTomador.cdata
                    except AttributeError: pass
                    try: r5001_rprest_dados['vlrtotalbaseret'] = RPrest.vlrTotalBaseRet.cdata
                    except AttributeError: pass
                    try: r5001_rprest_dados['vlrtotalretprinc'] = RPrest.vlrTotalRetPrinc.cdata
                    except AttributeError: pass
                    try: r5001_rprest_dados['vlrtotalretadic'] = RPrest.vlrTotalRetAdic.cdata
                    except AttributeError: pass
                    try: r5001_rprest_dados['vlrtotalnretprinc'] = RPrest.vlrTotalNRetPrinc.cdata
                    except AttributeError: pass
                    try: r5001_rprest_dados['vlrtotalnretadic'] = RPrest.vlrTotalNRetAdic.cdata
                    except AttributeError: pass
                    insert = create_insert('r5001_rprest', r5001_rprest_dados)
                    resp = executar_sql(insert, True)
                    r5001_rprest_id = resp[0][0]
                    #print r5001_rprest_id

            if 'RRecRepAD' in dir(infoTotal.ideEstab) and infoTotal.ideEstab.RRecRepAD.cdata != '':
                for RRecRepAD in infoTotal.ideEstab.RRecRepAD:
                    r5001_rrecrepad_dados = {}
                    r5001_rrecrepad_dados['r5001_infototal_id'] = r5001_infototal_id

                    try: r5001_rrecrepad_dados['cnpjassocdesp'] = RRecRepAD.cnpjAssocDesp.cdata
                    except AttributeError: pass
                    try: r5001_rrecrepad_dados['vlrtotalrep'] = RRecRepAD.vlrTotalRep.cdata
                    except AttributeError: pass
                    try: r5001_rrecrepad_dados['crrecrepad'] = RRecRepAD.CRRecRepAD.cdata
                    except AttributeError: pass
                    try: r5001_rrecrepad_dados['vlrcrrecrepad'] = RRecRepAD.vlrCRRecRepAD.cdata
                    except AttributeError: pass
                    try: r5001_rrecrepad_dados['vlrcrrecrepadsusp'] = RRecRepAD.vlrCRRecRepADSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('r5001_rrecrepad', r5001_rrecrepad_dados)
                    resp = executar_sql(insert, True)
                    r5001_rrecrepad_id = resp[0][0]
                    #print r5001_rrecrepad_id

            if 'RComl' in dir(infoTotal.ideEstab) and infoTotal.ideEstab.RComl.cdata != '':
                for RComl in infoTotal.ideEstab.RComl:
                    r5001_rcoml_dados = {}
                    r5001_rcoml_dados['r5001_infototal_id'] = r5001_infototal_id

                    try: r5001_rcoml_dados['crcoml'] = RComl.CRComl.cdata
                    except AttributeError: pass
                    try: r5001_rcoml_dados['vlrcrcoml'] = RComl.vlrCRComl.cdata
                    except AttributeError: pass
                    try: r5001_rcoml_dados['vlrcrcomlsusp'] = RComl.vlrCRComlSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('r5001_rcoml', r5001_rcoml_dados)
                    resp = executar_sql(insert, True)
                    r5001_rcoml_id = resp[0][0]
                    #print r5001_rcoml_id

            if 'RCPRB' in dir(infoTotal.ideEstab) and infoTotal.ideEstab.RCPRB.cdata != '':
                for RCPRB in infoTotal.ideEstab.RCPRB:
                    r5001_rcprb_dados = {}
                    r5001_rcprb_dados['r5001_infototal_id'] = r5001_infototal_id

                    try: r5001_rcprb_dados['crcprb'] = RCPRB.CRCPRB.cdata
                    except AttributeError: pass
                    try: r5001_rcprb_dados['vlrcrcprb'] = RCPRB.vlrCRCPRB.cdata
                    except AttributeError: pass
                    try: r5001_rcprb_dados['vlrcrcprbsusp'] = RCPRB.vlrCRCPRBSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('r5001_rcprb', r5001_rcprb_dados)
                    resp = executar_sql(insert, True)
                    r5001_rcprb_id = resp[0][0]
                    #print r5001_rcprb_id

            if 'RRecEspetDesp' in dir(infoTotal.ideEstab) and infoTotal.ideEstab.RRecEspetDesp.cdata != '':
                for RRecEspetDesp in infoTotal.ideEstab.RRecEspetDesp:
                    r5001_rrecespetdesp_dados = {}
                    r5001_rrecespetdesp_dados['r5001_infototal_id'] = r5001_infototal_id

                    try: r5001_rrecespetdesp_dados['crrecespetdesp'] = RRecEspetDesp.CRRecEspetDesp.cdata
                    except AttributeError: pass
                    try: r5001_rrecespetdesp_dados['vlrreceitatotal'] = RRecEspetDesp.vlrReceitaTotal.cdata
                    except AttributeError: pass
                    try: r5001_rrecespetdesp_dados['vlrcrrecespetdesp'] = RRecEspetDesp.vlrCRRecEspetDesp.cdata
                    except AttributeError: pass
                    try: r5001_rrecespetdesp_dados['vlrcrrecespetdespsusp'] = RRecEspetDesp.vlrCRRecEspetDespSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('r5001_rrecespetdesp', r5001_rrecespetdesp_dados)
                    resp = executar_sql(insert, True)
                    r5001_rrecespetdesp_id = resp[0][0]
                    #print r5001_rrecespetdesp_id

    from emensageriapro.efdreinf.views.r5001_evttotal_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r5001_evttotal_id, 'default')
    return dados