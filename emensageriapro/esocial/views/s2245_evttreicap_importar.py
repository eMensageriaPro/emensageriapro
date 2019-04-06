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



def read_s2245_evttreicap_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2245_evttreicap_obj(doc, status, validar)
    return dados

def read_s2245_evttreicap(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2245_evttreicap_obj(doc, status, validar)
    return dados



def read_s2245_evttreicap_obj(doc, status, validar=False):
    s2245_evttreicap_dados = {}
    s2245_evttreicap_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2245_evttreicap_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2245_evttreicap_dados['identidade'] = doc.eSocial.evtTreiCap['Id']
    evtTreiCap = doc.eSocial.evtTreiCap

    try: s2245_evttreicap_dados['indretif'] = evtTreiCap.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['nrrecibo'] = evtTreiCap.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['tpamb'] = evtTreiCap.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['procemi'] = evtTreiCap.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['verproc'] = evtTreiCap.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['tpinsc'] = evtTreiCap.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['nrinsc'] = evtTreiCap.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['cpftrab'] = evtTreiCap.ideVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['nistrab'] = evtTreiCap.ideVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['matricula'] = evtTreiCap.ideVinculo.matricula.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['codcateg'] = evtTreiCap.ideVinculo.codCateg.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['codtreicap'] = evtTreiCap.treiCap.codTreiCap.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['obstreicap'] = evtTreiCap.treiCap.obsTreiCap.cdata
    except AttributeError: pass
    try: s2245_evttreicap_dados['observacao'] = evtTreiCap.treiCap.observacao.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtTreiCap.treiCap): s2245_evttreicap_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTreiCap.treiCap): s2245_evttreicap_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTreiCap.treiCap): s2245_evttreicap_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2245_evttreicap', s2245_evttreicap_dados)
    resp = executar_sql(insert, True)
    s2245_evttreicap_id = resp[0][0]
    dados = s2245_evttreicap_dados
    dados['evento'] = 's2245'
    dados['id'] = s2245_evttreicap_id
    dados['identidade_evento'] = doc.eSocial.evtTreiCap['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'infoComplem' in dir(evtTreiCap.treiCap) and evtTreiCap.treiCap.infoComplem.cdata != '':
        for infoComplem in evtTreiCap.treiCap.infoComplem:
            s2245_infocomplem_dados = {}
            s2245_infocomplem_dados['s2245_evttreicap_id'] = s2245_evttreicap_id

            try: s2245_infocomplem_dados['dttreicap'] = infoComplem.dtTreiCap.cdata
            except AttributeError: pass
            try: s2245_infocomplem_dados['durtreicap'] = infoComplem.durTreiCap.cdata
            except AttributeError: pass
            try: s2245_infocomplem_dados['modtreicap'] = infoComplem.modTreiCap.cdata
            except AttributeError: pass
            try: s2245_infocomplem_dados['tptreicap'] = infoComplem.tpTreiCap.cdata
            except AttributeError: pass
            insert = create_insert('s2245_infocomplem', s2245_infocomplem_dados)
            resp = executar_sql(insert, True)
            s2245_infocomplem_id = resp[0][0]
            #print s2245_infocomplem_id

            if 'ideProfResp' in dir(infoComplem) and infoComplem.ideProfResp.cdata != '':
                for ideProfResp in infoComplem.ideProfResp:
                    s2245_ideprofresp_dados = {}
                    s2245_ideprofresp_dados['s2245_infocomplem_id'] = s2245_infocomplem_id

                    try: s2245_ideprofresp_dados['cpfprof'] = ideProfResp.cpfProf.cdata
                    except AttributeError: pass
                    try: s2245_ideprofresp_dados['nmprof'] = ideProfResp.nmProf.cdata
                    except AttributeError: pass
                    try: s2245_ideprofresp_dados['tpprof'] = ideProfResp.tpProf.cdata
                    except AttributeError: pass
                    try: s2245_ideprofresp_dados['formprof'] = ideProfResp.formProf.cdata
                    except AttributeError: pass
                    try: s2245_ideprofresp_dados['codcbo'] = ideProfResp.codCBO.cdata
                    except AttributeError: pass
                    try: s2245_ideprofresp_dados['nacprof'] = ideProfResp.nacProf.cdata
                    except AttributeError: pass
                    insert = create_insert('s2245_ideprofresp', s2245_ideprofresp_dados)
                    resp = executar_sql(insert, True)
                    s2245_ideprofresp_id = resp[0][0]
                    #print s2245_ideprofresp_id

    from emensageriapro.esocial.views.s2245_evttreicap_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2245_evttreicap_id, 'default')
    return dados