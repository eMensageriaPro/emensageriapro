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



def read_r2010_evtservtom_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2010_evtservtom_obj(doc, status, validar)
    return dados

def read_r2010_evtservtom(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2010_evtservtom_obj(doc, status, validar)
    return dados



def read_r2010_evtservtom_obj(doc, status, validar=False):
    r2010_evtservtom_dados = {}
    r2010_evtservtom_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r2010_evtservtom_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2010_evtservtom_dados['identidade'] = doc.Reinf.evtServTom['id']
    evtServTom = doc.Reinf.evtServTom

    if 'indRetif' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['indretif'] = evtServTom.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['nrrecibo'] = evtServTom.ideEvento.nrRecibo.cdata
    if 'perApur' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['perapur'] = evtServTom.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['tpamb'] = evtServTom.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['procemi'] = evtServTom.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtServTom.ideEvento): r2010_evtservtom_dados['verproc'] = evtServTom.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtServTom.ideContri): r2010_evtservtom_dados['tpinsc'] = evtServTom.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtServTom.ideContri): r2010_evtservtom_dados['nrinsc'] = evtServTom.ideContri.nrInsc.cdata
    if 'tpInscEstab' in dir(evtServTom.infoServTom.ideEstabObra): r2010_evtservtom_dados['tpinscestab'] = evtServTom.infoServTom.ideEstabObra.tpInscEstab.cdata
    if 'nrInscEstab' in dir(evtServTom.infoServTom.ideEstabObra): r2010_evtservtom_dados['nrinscestab'] = evtServTom.infoServTom.ideEstabObra.nrInscEstab.cdata
    if 'indObra' in dir(evtServTom.infoServTom.ideEstabObra): r2010_evtservtom_dados['indobra'] = evtServTom.infoServTom.ideEstabObra.indObra.cdata
    if 'cnpjPrestador' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['cnpjprestador'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.cnpjPrestador.cdata
    if 'vlrTotalBruto' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalbruto'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBruto.cdata
    if 'vlrTotalBaseRet' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalbaseret'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalBaseRet.cdata
    if 'vlrTotalRetPrinc' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalretprinc'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetPrinc.cdata
    if 'vlrTotalRetAdic' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalretadic'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalRetAdic.cdata
    if 'vlrTotalNRetPrinc' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalnretprinc'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetPrinc.cdata
    if 'vlrTotalNRetAdic' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['vlrtotalnretadic'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.vlrTotalNRetAdic.cdata
    if 'indCPRB' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ): r2010_evtservtom_dados['indcprb'] = evtServTom.infoServTom.ideEstabObra.idePrestServ.indCPRB.cdata
    if 'inclusao' in dir(evtServTom.infoServTom): r2010_evtservtom_dados['operacao'] = 1
    elif 'alteracao' in dir(evtServTom.infoServTom): r2010_evtservtom_dados['operacao'] = 2
    elif 'exclusao' in dir(evtServTom.infoServTom): r2010_evtservtom_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2010_evtservtom', r2010_evtservtom_dados)
    resp = executar_sql(insert, True)
    r2010_evtservtom_id = resp[0][0]
    dados = r2010_evtservtom_dados
    dados['evento'] = 'r2010'
    dados['id'] = r2010_evtservtom_id
    dados['identidade_evento'] = doc.Reinf.evtServTom['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'nfs' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
        for nfs in evtServTom.infoServTom.ideEstabObra.idePrestServ.nfs:
            r2010_nfs_dados = {}
            r2010_nfs_dados['r2010_evtservtom_id'] = r2010_evtservtom_id

            if 'serie' in dir(nfs): r2010_nfs_dados['serie'] = nfs.serie.cdata
            if 'numDocto' in dir(nfs): r2010_nfs_dados['numdocto'] = nfs.numDocto.cdata
            if 'dtEmissaoNF' in dir(nfs): r2010_nfs_dados['dtemissaonf'] = nfs.dtEmissaoNF.cdata
            if 'vlrBruto' in dir(nfs): r2010_nfs_dados['vlrbruto'] = nfs.vlrBruto.cdata
            if 'obs' in dir(nfs): r2010_nfs_dados['obs'] = nfs.obs.cdata
            insert = create_insert('r2010_nfs', r2010_nfs_dados)
            resp = executar_sql(insert, True)
            r2010_nfs_id = resp[0][0]
            #print r2010_nfs_id

            if 'infoTpServ' in dir(nfs):
                for infoTpServ in nfs.infoTpServ:
                    r2010_infotpserv_dados = {}
                    r2010_infotpserv_dados['r2010_nfs_id'] = r2010_nfs_id

                    if 'tpServico' in dir(infoTpServ): r2010_infotpserv_dados['tpservico'] = infoTpServ.tpServico.cdata
                    if 'vlrBaseRet' in dir(infoTpServ): r2010_infotpserv_dados['vlrbaseret'] = infoTpServ.vlrBaseRet.cdata
                    if 'vlrRetencao' in dir(infoTpServ): r2010_infotpserv_dados['vlrretencao'] = infoTpServ.vlrRetencao.cdata
                    if 'vlrRetSub' in dir(infoTpServ): r2010_infotpserv_dados['vlrretsub'] = infoTpServ.vlrRetSub.cdata
                    if 'vlrNRetPrinc' in dir(infoTpServ): r2010_infotpserv_dados['vlrnretprinc'] = infoTpServ.vlrNRetPrinc.cdata
                    if 'vlrServicos15' in dir(infoTpServ): r2010_infotpserv_dados['vlrservicos15'] = infoTpServ.vlrServicos15.cdata
                    if 'vlrServicos20' in dir(infoTpServ): r2010_infotpserv_dados['vlrservicos20'] = infoTpServ.vlrServicos20.cdata
                    if 'vlrServicos25' in dir(infoTpServ): r2010_infotpserv_dados['vlrservicos25'] = infoTpServ.vlrServicos25.cdata
                    if 'vlrAdicional' in dir(infoTpServ): r2010_infotpserv_dados['vlradicional'] = infoTpServ.vlrAdicional.cdata
                    if 'vlrNRetAdic' in dir(infoTpServ): r2010_infotpserv_dados['vlrnretadic'] = infoTpServ.vlrNRetAdic.cdata
                    insert = create_insert('r2010_infotpserv', r2010_infotpserv_dados)
                    resp = executar_sql(insert, True)
                    r2010_infotpserv_id = resp[0][0]
                    #print r2010_infotpserv_id

    if 'infoProcRetPr' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
        for infoProcRetPr in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetPr:
            r2010_infoprocretpr_dados = {}
            r2010_infoprocretpr_dados['r2010_evtservtom_id'] = r2010_evtservtom_id

            if 'tpProcRetPrinc' in dir(infoProcRetPr): r2010_infoprocretpr_dados['tpprocretprinc'] = infoProcRetPr.tpProcRetPrinc.cdata
            if 'nrProcRetPrinc' in dir(infoProcRetPr): r2010_infoprocretpr_dados['nrprocretprinc'] = infoProcRetPr.nrProcRetPrinc.cdata
            if 'codSuspPrinc' in dir(infoProcRetPr): r2010_infoprocretpr_dados['codsuspprinc'] = infoProcRetPr.codSuspPrinc.cdata
            if 'valorPrinc' in dir(infoProcRetPr): r2010_infoprocretpr_dados['valorprinc'] = infoProcRetPr.valorPrinc.cdata
            insert = create_insert('r2010_infoprocretpr', r2010_infoprocretpr_dados)
            resp = executar_sql(insert, True)
            r2010_infoprocretpr_id = resp[0][0]
            #print r2010_infoprocretpr_id

    if 'infoProcRetAd' in dir(evtServTom.infoServTom.ideEstabObra.idePrestServ):
        for infoProcRetAd in evtServTom.infoServTom.ideEstabObra.idePrestServ.infoProcRetAd:
            r2010_infoprocretad_dados = {}
            r2010_infoprocretad_dados['r2010_evtservtom_id'] = r2010_evtservtom_id

            if 'tpProcRetAdic' in dir(infoProcRetAd): r2010_infoprocretad_dados['tpprocretadic'] = infoProcRetAd.tpProcRetAdic.cdata
            if 'nrProcRetAdic' in dir(infoProcRetAd): r2010_infoprocretad_dados['nrprocretadic'] = infoProcRetAd.nrProcRetAdic.cdata
            if 'codSuspAdic' in dir(infoProcRetAd): r2010_infoprocretad_dados['codsuspadic'] = infoProcRetAd.codSuspAdic.cdata
            if 'valorAdic' in dir(infoProcRetAd): r2010_infoprocretad_dados['valoradic'] = infoProcRetAd.valorAdic.cdata
            insert = create_insert('r2010_infoprocretad', r2010_infoprocretad_dados)
            resp = executar_sql(insert, True)
            r2010_infoprocretad_id = resp[0][0]
            #print r2010_infoprocretad_id

    from emensageriapro.efdreinf.views.r2010_evtservtom_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2010_evtservtom_id, 'default')
    return dados