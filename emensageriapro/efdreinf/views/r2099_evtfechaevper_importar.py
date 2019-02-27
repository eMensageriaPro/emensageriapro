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



def read_r2099_evtfechaevper_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2099_evtfechaevper_obj(doc, status, validar)
    return dados

def read_r2099_evtfechaevper(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2099_evtfechaevper_obj(doc, status, validar)
    return dados



def read_r2099_evtfechaevper_obj(doc, status, validar=False):
    r2099_evtfechaevper_dados = {}
    r2099_evtfechaevper_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r2099_evtfechaevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2099_evtfechaevper_dados['identidade'] = doc.Reinf.evtFechaEvPer['id']
    evtFechaEvPer = doc.Reinf.evtFechaEvPer

    if 'perApur' in dir(evtFechaEvPer.ideEvento): r2099_evtfechaevper_dados['perapur'] = evtFechaEvPer.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtFechaEvPer.ideEvento): r2099_evtfechaevper_dados['tpamb'] = evtFechaEvPer.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtFechaEvPer.ideEvento): r2099_evtfechaevper_dados['procemi'] = evtFechaEvPer.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtFechaEvPer.ideEvento): r2099_evtfechaevper_dados['verproc'] = evtFechaEvPer.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtFechaEvPer.ideContri): r2099_evtfechaevper_dados['tpinsc'] = evtFechaEvPer.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtFechaEvPer.ideContri): r2099_evtfechaevper_dados['nrinsc'] = evtFechaEvPer.ideContri.nrInsc.cdata
    if 'evtServTm' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtservtm'] = evtFechaEvPer.infoFech.evtServTm.cdata
    if 'evtServPr' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtservpr'] = evtFechaEvPer.infoFech.evtServPr.cdata
    if 'evtAssDespRec' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtassdesprec'] = evtFechaEvPer.infoFech.evtAssDespRec.cdata
    if 'evtAssDespRep' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtassdesprep'] = evtFechaEvPer.infoFech.evtAssDespRep.cdata
    if 'evtComProd' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtcomprod'] = evtFechaEvPer.infoFech.evtComProd.cdata
    if 'evtCPRB' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtcprb'] = evtFechaEvPer.infoFech.evtCPRB.cdata
    if 'evtPgtos' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtpgtos'] = evtFechaEvPer.infoFech.evtPgtos.cdata
    if 'compSemMovto' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['compsemmovto'] = evtFechaEvPer.infoFech.compSemMovto.cdata
    if 'inclusao' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['operacao'] = 1
    elif 'alteracao' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['operacao'] = 2
    elif 'exclusao' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2099_evtfechaevper', r2099_evtfechaevper_dados)
    resp = executar_sql(insert, True)
    r2099_evtfechaevper_id = resp[0][0]
    dados = r2099_evtfechaevper_dados
    dados['evento'] = 'r2099'
    dados['id'] = r2099_evtfechaevper_id
    dados['identidade_evento'] = doc.Reinf.evtFechaEvPer['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'ideRespInf' in dir(evtFechaEvPer):
        for ideRespInf in evtFechaEvPer.ideRespInf:
            r2099_iderespinf_dados = {}
            r2099_iderespinf_dados['r2099_evtfechaevper_id'] = r2099_evtfechaevper_id

            if 'nmResp' in dir(ideRespInf): r2099_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            if 'cpfResp' in dir(ideRespInf): r2099_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            if 'telefone' in dir(ideRespInf): r2099_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            if 'email' in dir(ideRespInf): r2099_iderespinf_dados['email'] = ideRespInf.email.cdata
            insert = create_insert('r2099_iderespinf', r2099_iderespinf_dados)
            resp = executar_sql(insert, True)
            r2099_iderespinf_id = resp[0][0]
            #print r2099_iderespinf_id

    from emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2099_evtfechaevper_id, 'default')
    return dados