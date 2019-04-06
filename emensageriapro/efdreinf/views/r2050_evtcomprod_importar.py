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



def read_r2050_evtcomprod_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2050_evtcomprod_obj(doc, status, validar)
    return dados

def read_r2050_evtcomprod(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2050_evtcomprod_obj(doc, status, validar)
    return dados



def read_r2050_evtcomprod_obj(doc, status, validar=False):
    r2050_evtcomprod_dados = {}
    r2050_evtcomprod_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r2050_evtcomprod_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2050_evtcomprod_dados['identidade'] = doc.Reinf.evtComProd['id']
    evtComProd = doc.Reinf.evtComProd

    try: r2050_evtcomprod_dados['indretif'] = evtComProd.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['nrrecibo'] = evtComProd.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['perapur'] = evtComProd.ideEvento.perApur.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['tpamb'] = evtComProd.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['procemi'] = evtComProd.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['verproc'] = evtComProd.ideEvento.verProc.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['tpinsc'] = evtComProd.ideContri.tpInsc.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['nrinsc'] = evtComProd.ideContri.nrInsc.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['tpinscestab'] = evtComProd.infoComProd.ideEstab.tpInscEstab.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['nrinscestab'] = evtComProd.infoComProd.ideEstab.nrInscEstab.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['vlrrecbrutatotal'] = evtComProd.infoComProd.ideEstab.vlrRecBrutaTotal.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['vlrcpapur'] = evtComProd.infoComProd.ideEstab.vlrCPApur.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['vlrratapur'] = evtComProd.infoComProd.ideEstab.vlrRatApur.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['vlrsenarapur'] = evtComProd.infoComProd.ideEstab.vlrSenarApur.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['vlrcpsusptotal'] = evtComProd.infoComProd.ideEstab.vlrCPSuspTotal.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['vlrratsusptotal'] = evtComProd.infoComProd.ideEstab.vlrRatSuspTotal.cdata
    except AttributeError: pass
    try: r2050_evtcomprod_dados['vlrsenarsusptotal'] = evtComProd.infoComProd.ideEstab.vlrSenarSuspTotal.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtComProd.infoComProd): r2050_evtcomprod_dados['operacao'] = 1
    elif 'alteracao' in dir(evtComProd.infoComProd): r2050_evtcomprod_dados['operacao'] = 2
    elif 'exclusao' in dir(evtComProd.infoComProd): r2050_evtcomprod_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2050_evtcomprod', r2050_evtcomprod_dados)
    resp = executar_sql(insert, True)
    r2050_evtcomprod_id = resp[0][0]
    dados = r2050_evtcomprod_dados
    dados['evento'] = 'r2050'
    dados['id'] = r2050_evtcomprod_id
    dados['identidade_evento'] = doc.Reinf.evtComProd['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'tipoCom' in dir(evtComProd.infoComProd.ideEstab) and evtComProd.infoComProd.ideEstab.tipoCom.cdata != '':
        for tipoCom in evtComProd.infoComProd.ideEstab.tipoCom:
            r2050_tipocom_dados = {}
            r2050_tipocom_dados['r2050_evtcomprod_id'] = r2050_evtcomprod_id

            try: r2050_tipocom_dados['indcom'] = tipoCom.indCom.cdata
            except AttributeError: pass
            try: r2050_tipocom_dados['vlrrecbruta'] = tipoCom.vlrRecBruta.cdata
            except AttributeError: pass
            insert = create_insert('r2050_tipocom', r2050_tipocom_dados)
            resp = executar_sql(insert, True)
            r2050_tipocom_id = resp[0][0]
            #print r2050_tipocom_id

            if 'infoProc' in dir(tipoCom) and tipoCom.infoProc.cdata != '':
                for infoProc in tipoCom.infoProc:
                    r2050_infoproc_dados = {}
                    r2050_infoproc_dados['r2050_tipocom_id'] = r2050_tipocom_id

                    try: r2050_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    except AttributeError: pass
                    try: r2050_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    except AttributeError: pass
                    try: r2050_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    except AttributeError: pass
                    try: r2050_infoproc_dados['vlrcpsusp'] = infoProc.vlrCPSusp.cdata
                    except AttributeError: pass
                    try: r2050_infoproc_dados['vlrratsusp'] = infoProc.vlrRatSusp.cdata
                    except AttributeError: pass
                    try: r2050_infoproc_dados['vlrsenarsusp'] = infoProc.vlrSenarSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('r2050_infoproc', r2050_infoproc_dados)
                    resp = executar_sql(insert, True)
                    r2050_infoproc_id = resp[0][0]
                    #print r2050_infoproc_id

    from emensageriapro.efdreinf.views.r2050_evtcomprod_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2050_evtcomprod_id, 'default')
    return dados