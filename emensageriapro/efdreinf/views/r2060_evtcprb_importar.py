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



def read_r2060_evtcprb_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2060_evtcprb_obj(doc, status, validar)
    return dados

def read_r2060_evtcprb(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2060_evtcprb_obj(doc, status, validar)
    return dados



def read_r2060_evtcprb_obj(doc, status, validar=False):
    r2060_evtcprb_dados = {}
    r2060_evtcprb_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r2060_evtcprb_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2060_evtcprb_dados['identidade'] = doc.Reinf.evtCPRB['id']
    evtCPRB = doc.Reinf.evtCPRB

    try: r2060_evtcprb_dados['indretif'] = evtCPRB.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['nrrecibo'] = evtCPRB.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['perapur'] = evtCPRB.ideEvento.perApur.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['tpamb'] = evtCPRB.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['procemi'] = evtCPRB.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['verproc'] = evtCPRB.ideEvento.verProc.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['tpinsc'] = evtCPRB.ideContri.tpInsc.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['nrinsc'] = evtCPRB.ideContri.nrInsc.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['tpinscestab'] = evtCPRB.infoCPRB.ideEstab.tpInscEstab.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['nrinscestab'] = evtCPRB.infoCPRB.ideEstab.nrInscEstab.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['vlrrecbrutatotal'] = evtCPRB.infoCPRB.ideEstab.vlrRecBrutaTotal.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['vlrcpapurtotal'] = evtCPRB.infoCPRB.ideEstab.vlrCPApurTotal.cdata
    except AttributeError: pass
    try: r2060_evtcprb_dados['vlrcprbsusptotal'] = evtCPRB.infoCPRB.ideEstab.vlrCPRBSuspTotal.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtCPRB.infoCPRB): r2060_evtcprb_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCPRB.infoCPRB): r2060_evtcprb_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCPRB.infoCPRB): r2060_evtcprb_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2060_evtcprb', r2060_evtcprb_dados)
    resp = executar_sql(insert, True)
    r2060_evtcprb_id = resp[0][0]
    dados = r2060_evtcprb_dados
    dados['evento'] = 'r2060'
    dados['id'] = r2060_evtcprb_id
    dados['identidade_evento'] = doc.Reinf.evtCPRB['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'tipoCod' in dir(evtCPRB.infoCPRB.ideEstab) and evtCPRB.infoCPRB.ideEstab.tipoCod.cdata != '':
        for tipoCod in evtCPRB.infoCPRB.ideEstab.tipoCod:
            r2060_tipocod_dados = {}
            r2060_tipocod_dados['r2060_evtcprb_id'] = r2060_evtcprb_id

            try: r2060_tipocod_dados['codativecon'] = tipoCod.codAtivEcon.cdata
            except AttributeError: pass
            try: r2060_tipocod_dados['vlrrecbrutaativ'] = tipoCod.vlrRecBrutaAtiv.cdata
            except AttributeError: pass
            try: r2060_tipocod_dados['vlrexcrecbruta'] = tipoCod.vlrExcRecBruta.cdata
            except AttributeError: pass
            try: r2060_tipocod_dados['vlradicrecbruta'] = tipoCod.vlrAdicRecBruta.cdata
            except AttributeError: pass
            try: r2060_tipocod_dados['vlrbccprb'] = tipoCod.vlrBcCPRB.cdata
            except AttributeError: pass
            try: r2060_tipocod_dados['vlrcprbapur'] = tipoCod.vlrCPRBapur.cdata
            except AttributeError: pass
            insert = create_insert('r2060_tipocod', r2060_tipocod_dados)
            resp = executar_sql(insert, True)
            r2060_tipocod_id = resp[0][0]
            #print r2060_tipocod_id

            if 'tipoAjuste' in dir(tipoCod) and tipoCod.tipoAjuste.cdata != '':
                for tipoAjuste in tipoCod.tipoAjuste:
                    r2060_tipoajuste_dados = {}
                    r2060_tipoajuste_dados['r2060_tipocod_id'] = r2060_tipocod_id

                    try: r2060_tipoajuste_dados['tpajuste'] = tipoAjuste.tpAjuste.cdata
                    except AttributeError: pass
                    try: r2060_tipoajuste_dados['codajuste'] = tipoAjuste.codAjuste.cdata
                    except AttributeError: pass
                    try: r2060_tipoajuste_dados['vlrajuste'] = tipoAjuste.vlrAjuste.cdata
                    except AttributeError: pass
                    try: r2060_tipoajuste_dados['descajuste'] = tipoAjuste.descAjuste.cdata
                    except AttributeError: pass
                    try: r2060_tipoajuste_dados['dtajuste'] = tipoAjuste.dtAjuste.cdata
                    except AttributeError: pass
                    insert = create_insert('r2060_tipoajuste', r2060_tipoajuste_dados)
                    resp = executar_sql(insert, True)
                    r2060_tipoajuste_id = resp[0][0]
                    #print r2060_tipoajuste_id

            if 'infoProc' in dir(tipoCod) and tipoCod.infoProc.cdata != '':
                for infoProc in tipoCod.infoProc:
                    r2060_infoproc_dados = {}
                    r2060_infoproc_dados['r2060_tipocod_id'] = r2060_tipocod_id

                    try: r2060_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    except AttributeError: pass
                    try: r2060_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    except AttributeError: pass
                    try: r2060_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    except AttributeError: pass
                    try: r2060_infoproc_dados['vlrcprbsusp'] = infoProc.vlrCPRBSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('r2060_infoproc', r2060_infoproc_dados)
                    resp = executar_sql(insert, True)
                    r2060_infoproc_id = resp[0][0]
                    #print r2060_infoproc_id

    from emensageriapro.efdreinf.views.r2060_evtcprb_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2060_evtcprb_id, 'default')
    return dados