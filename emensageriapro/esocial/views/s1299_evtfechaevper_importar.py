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



def read_s1299_evtfechaevper_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1299_evtfechaevper_obj(doc, status, validar)
    return dados

def read_s1299_evtfechaevper(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1299_evtfechaevper_obj(doc, status, validar)
    return dados



def read_s1299_evtfechaevper_obj(doc, status, validar=False):
    s1299_evtfechaevper_dados = {}
    s1299_evtfechaevper_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1299_evtfechaevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1299_evtfechaevper_dados['identidade'] = doc.eSocial.evtFechaEvPer['Id']
    evtFechaEvPer = doc.eSocial.evtFechaEvPer

    if 'indApuracao' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['indapuracao'] = evtFechaEvPer.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['perapur'] = evtFechaEvPer.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['tpamb'] = evtFechaEvPer.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['procemi'] = evtFechaEvPer.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['verproc'] = evtFechaEvPer.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtFechaEvPer.ideEmpregador): s1299_evtfechaevper_dados['tpinsc'] = evtFechaEvPer.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtFechaEvPer.ideEmpregador): s1299_evtfechaevper_dados['nrinsc'] = evtFechaEvPer.ideEmpregador.nrInsc.cdata
    if 'evtRemun' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtremun'] = evtFechaEvPer.infoFech.evtRemun.cdata
    if 'evtPgtos' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtpgtos'] = evtFechaEvPer.infoFech.evtPgtos.cdata
    if 'evtAqProd' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtaqprod'] = evtFechaEvPer.infoFech.evtAqProd.cdata
    if 'evtComProd' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtcomprod'] = evtFechaEvPer.infoFech.evtComProd.cdata
    if 'evtContratAvNP' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtcontratavnp'] = evtFechaEvPer.infoFech.evtContratAvNP.cdata
    if 'evtInfoComplPer' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtinfocomplper'] = evtFechaEvPer.infoFech.evtInfoComplPer.cdata
    if 'compSemMovto' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['compsemmovto'] = evtFechaEvPer.infoFech.compSemMovto.cdata
    if 'inclusao' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['operacao'] = 1
    elif 'alteracao' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['operacao'] = 2
    elif 'exclusao' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1299_evtfechaevper', s1299_evtfechaevper_dados)
    resp = executar_sql(insert, True)
    s1299_evtfechaevper_id = resp[0][0]
    dados = s1299_evtfechaevper_dados
    dados['evento'] = 's1299'
    dados['id'] = s1299_evtfechaevper_id
    dados['identidade_evento'] = doc.eSocial.evtFechaEvPer['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'ideRespInf' in dir(evtFechaEvPer):
        for ideRespInf in evtFechaEvPer.ideRespInf:
            s1299_iderespinf_dados = {}
            s1299_iderespinf_dados['s1299_evtfechaevper_id'] = s1299_evtfechaevper_id

            if 'nmResp' in dir(ideRespInf): s1299_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            if 'cpfResp' in dir(ideRespInf): s1299_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            if 'telefone' in dir(ideRespInf): s1299_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            if 'email' in dir(ideRespInf): s1299_iderespinf_dados['email'] = ideRespInf.email.cdata
            insert = create_insert('s1299_iderespinf', s1299_iderespinf_dados)
            resp = executar_sql(insert, True)
            s1299_iderespinf_id = resp[0][0]
            #print s1299_iderespinf_id

    from emensageriapro.esocial.views.s1299_evtfechaevper_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1299_evtfechaevper_id, 'default')
    return dados