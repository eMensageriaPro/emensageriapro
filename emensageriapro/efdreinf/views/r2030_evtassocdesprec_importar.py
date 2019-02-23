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



def read_r2030_evtassocdesprec_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2030_evtassocdesprec_obj(doc, status, validar)
    return dados

def read_r2030_evtassocdesprec(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2030_evtassocdesprec_obj(doc, status, validar)
    return dados



def read_r2030_evtassocdesprec_obj(doc, status, validar=False):
    r2030_evtassocdesprec_dados = {}
    r2030_evtassocdesprec_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r2030_evtassocdesprec_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2030_evtassocdesprec_dados['identidade'] = doc.Reinf.evtAssocDespRec['id']
    r2030_evtassocdesprec_dados['processamento_codigo_resposta'] = 1
    evtAssocDespRec = doc.Reinf.evtAssocDespRec

    if 'indRetif' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['indretif'] = evtAssocDespRec.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['nrrecibo'] = evtAssocDespRec.ideEvento.nrRecibo.cdata
    if 'perApur' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['perapur'] = evtAssocDespRec.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['tpamb'] = evtAssocDespRec.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['procemi'] = evtAssocDespRec.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['verproc'] = evtAssocDespRec.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['tpinsc'] = evtAssocDespRec.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['nrinsc'] = evtAssocDespRec.ideContri.nrInsc.cdata
    if 'tpInscEstab' in dir(evtAssocDespRec.ideContri.ideEstab): r2030_evtassocdesprec_dados['tpinscestab'] = evtAssocDespRec.ideContri.ideEstab.tpInscEstab.cdata
    if 'nrInscEstab' in dir(evtAssocDespRec.ideContri.ideEstab): r2030_evtassocdesprec_dados['nrinscestab'] = evtAssocDespRec.ideContri.ideEstab.nrInscEstab.cdata
    if 'inclusao' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2030_evtassocdesprec', r2030_evtassocdesprec_dados)
    resp = executar_sql(insert, True)
    r2030_evtassocdesprec_id = resp[0][0]
    dados = r2030_evtassocdesprec_dados
    dados['evento'] = 'r2030'
    dados['id'] = r2030_evtassocdesprec_id
    dados['identidade_evento'] = doc.Reinf.evtAssocDespRec['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'recursosRec' in dir(evtAssocDespRec.ideContri.ideEstab):
        for recursosRec in evtAssocDespRec.ideContri.ideEstab.recursosRec:
            r2030_recursosrec_dados = {}
            r2030_recursosrec_dados['r2030_evtassocdesprec_id'] = r2030_evtassocdesprec_id

            if 'cnpjOrigRecurso' in dir(recursosRec): r2030_recursosrec_dados['cnpjorigrecurso'] = recursosRec.cnpjOrigRecurso.cdata
            if 'vlrTotalRec' in dir(recursosRec): r2030_recursosrec_dados['vlrtotalrec'] = recursosRec.vlrTotalRec.cdata
            if 'vlrTotalRet' in dir(recursosRec): r2030_recursosrec_dados['vlrtotalret'] = recursosRec.vlrTotalRet.cdata
            if 'vlrTotalNRet' in dir(recursosRec): r2030_recursosrec_dados['vlrtotalnret'] = recursosRec.vlrTotalNRet.cdata
            insert = create_insert('r2030_recursosrec', r2030_recursosrec_dados)
            resp = executar_sql(insert, True)
            r2030_recursosrec_id = resp[0][0]
            #print r2030_recursosrec_id

            if 'infoRecurso' in dir(recursosRec):
                for infoRecurso in recursosRec.infoRecurso:
                    r2030_inforecurso_dados = {}
                    r2030_inforecurso_dados['r2030_recursosrec_id'] = r2030_recursosrec_id

                    if 'tpRepasse' in dir(infoRecurso): r2030_inforecurso_dados['tprepasse'] = infoRecurso.tpRepasse.cdata
                    if 'descRecurso' in dir(infoRecurso): r2030_inforecurso_dados['descrecurso'] = infoRecurso.descRecurso.cdata
                    if 'vlrBruto' in dir(infoRecurso): r2030_inforecurso_dados['vlrbruto'] = infoRecurso.vlrBruto.cdata
                    if 'vlrRetApur' in dir(infoRecurso): r2030_inforecurso_dados['vlrretapur'] = infoRecurso.vlrRetApur.cdata
                    insert = create_insert('r2030_inforecurso', r2030_inforecurso_dados)
                    resp = executar_sql(insert, True)
                    r2030_inforecurso_id = resp[0][0]
                    #print r2030_inforecurso_id

            if 'infoProc' in dir(recursosRec):
                for infoProc in recursosRec.infoProc:
                    r2030_infoproc_dados = {}
                    r2030_infoproc_dados['r2030_recursosrec_id'] = r2030_recursosrec_id

                    if 'tpProc' in dir(infoProc): r2030_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    if 'nrProc' in dir(infoProc): r2030_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    if 'codSusp' in dir(infoProc): r2030_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    if 'vlrNRet' in dir(infoProc): r2030_infoproc_dados['vlrnret'] = infoProc.vlrNRet.cdata
                    insert = create_insert('r2030_infoproc', r2030_infoproc_dados)
                    resp = executar_sql(insert, True)
                    r2030_infoproc_id = resp[0][0]
                    #print r2030_infoproc_id

    from emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2030_evtassocdesprec_id, 'default')
    return dados