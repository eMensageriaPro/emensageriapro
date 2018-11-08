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


def read_r3010_evtespdesportivo_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_r3010_evtespdesportivo_obj(doc, status, validar)
    return dados

def read_r3010_evtespdesportivo(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_r3010_evtespdesportivo_obj(doc, status, validar)
    return dados



def read_r3010_evtespdesportivo_obj(doc, status, validar=False):
    r3010_evtespdesportivo_dados = {}
    r3010_evtespdesportivo_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r3010_evtespdesportivo_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r3010_evtespdesportivo_dados['identidade'] = doc.Reinf.evtEspDesportivo['id']
    r3010_evtespdesportivo_dados['processamento_codigo_resposta'] = 1
    evtEspDesportivo = doc.Reinf.evtEspDesportivo

    if 'indRetif' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['indretif'] = evtEspDesportivo.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['nrrecibo'] = evtEspDesportivo.ideEvento.nrRecibo.cdata
    if 'dtApuracao' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['dtapuracao'] = evtEspDesportivo.ideEvento.dtApuracao.cdata
    if 'tpAmb' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['tpamb'] = evtEspDesportivo.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['procemi'] = evtEspDesportivo.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['verproc'] = evtEspDesportivo.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['tpinsc'] = evtEspDesportivo.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['nrinsc'] = evtEspDesportivo.ideContri.nrInsc.cdata
    if 'inclusao' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['operacao'] = 1
    elif 'alteracao' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['operacao'] = 2
    elif 'exclusao' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['operacao'] = 3
    #print dados
    insert = create_insert('r3010_evtespdesportivo', r3010_evtespdesportivo_dados)
    resp = executar_sql(insert, True)
    r3010_evtespdesportivo_id = resp[0][0]
    dados = r3010_evtespdesportivo_dados
    dados['evento'] = 'r3010'
    dados['id'] = r3010_evtespdesportivo_id
    dados['identidade_evento'] = doc.Reinf.evtEspDesportivo['id']
    dados['status'] = 1

    if 'ideEstab' in dir(evtEspDesportivo.ideContri):
        for ideEstab in evtEspDesportivo.ideContri.ideEstab:
            r3010_ideestab_dados = {}
            r3010_ideestab_dados['r3010_evtespdesportivo_id'] = r3010_evtespdesportivo_id
       
            if 'tpInscEstab' in dir(ideEstab): r3010_ideestab_dados['tpinscestab'] = ideEstab.tpInscEstab.cdata
            if 'nrInscEstab' in dir(ideEstab): r3010_ideestab_dados['nrinscestab'] = ideEstab.nrInscEstab.cdata
            if 'vlrReceitaTotal' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrreceitatotal'] = ideEstab.receitaTotal.vlrReceitaTotal.cdata
            if 'vlrCP' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrcp'] = ideEstab.receitaTotal.vlrCP.cdata
            if 'vlrCPSuspTotal' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrcpsusptotal'] = ideEstab.receitaTotal.vlrCPSuspTotal.cdata
            if 'vlrReceitaClubes' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrreceitaclubes'] = ideEstab.receitaTotal.vlrReceitaClubes.cdata
            if 'vlrRetParc' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrretparc'] = ideEstab.receitaTotal.vlrRetParc.cdata
            insert = create_insert('r3010_ideestab', r3010_ideestab_dados)
            resp = executar_sql(insert, True)
            r3010_ideestab_id = resp[0][0]
            #print r3010_ideestab_id

            if 'boletim' in dir(ideEstab):
                for boletim in ideEstab.boletim:
                    r3010_boletim_dados = {}
                    r3010_boletim_dados['r3010_ideestab_id'] = r3010_ideestab_id
               
                    if 'nrBoletim' in dir(boletim): r3010_boletim_dados['nrboletim'] = boletim.nrBoletim.cdata
                    if 'tpCompeticao' in dir(boletim): r3010_boletim_dados['tpcompeticao'] = boletim.tpCompeticao.cdata
                    if 'categEvento' in dir(boletim): r3010_boletim_dados['categevento'] = boletim.categEvento.cdata
                    if 'modDesportiva' in dir(boletim): r3010_boletim_dados['moddesportiva'] = boletim.modDesportiva.cdata
                    if 'nomeCompeticao' in dir(boletim): r3010_boletim_dados['nomecompeticao'] = boletim.nomeCompeticao.cdata
                    if 'cnpjMandante' in dir(boletim): r3010_boletim_dados['cnpjmandante'] = boletim.cnpjMandante.cdata
                    if 'cnpjVisitante' in dir(boletim): r3010_boletim_dados['cnpjvisitante'] = boletim.cnpjVisitante.cdata
                    if 'nomeVisitante' in dir(boletim): r3010_boletim_dados['nomevisitante'] = boletim.nomeVisitante.cdata
                    if 'pracaDesportiva' in dir(boletim): r3010_boletim_dados['pracadesportiva'] = boletim.pracaDesportiva.cdata
                    if 'codMunic' in dir(boletim): r3010_boletim_dados['codmunic'] = boletim.codMunic.cdata
                    if 'uf' in dir(boletim): r3010_boletim_dados['uf'] = boletim.uf.cdata
                    if 'qtdePagantes' in dir(boletim): r3010_boletim_dados['qtdepagantes'] = boletim.qtdePagantes.cdata
                    if 'qtdeNaoPagantes' in dir(boletim): r3010_boletim_dados['qtdenaopagantes'] = boletim.qtdeNaoPagantes.cdata
                    insert = create_insert('r3010_boletim', r3010_boletim_dados)
                    resp = executar_sql(insert, True)
                    r3010_boletim_id = resp[0][0]
                    #print r3010_boletim_id
   
            if 'infoProc' in dir(ideEstab.receitaTotal):
                for infoProc in ideEstab.receitaTotal.infoProc:
                    r3010_infoproc_dados = {}
                    r3010_infoproc_dados['r3010_ideestab_id'] = r3010_ideestab_id
               
                    if 'tpProc' in dir(infoProc): r3010_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    if 'nrProc' in dir(infoProc): r3010_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    if 'codSusp' in dir(infoProc): r3010_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    if 'vlrCPSusp' in dir(infoProc): r3010_infoproc_dados['vlrcpsusp'] = infoProc.vlrCPSusp.cdata
                    insert = create_insert('r3010_infoproc', r3010_infoproc_dados)
                    resp = executar_sql(insert, True)
                    r3010_infoproc_id = resp[0][0]
                    #print r3010_infoproc_id
   
    from emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r3010_evtespdesportivo_id, 'default')
    return dados