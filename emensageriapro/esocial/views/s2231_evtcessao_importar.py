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



def read_s2231_evtcessao_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2231_evtcessao_obj(doc, status, validar)
    return dados

def read_s2231_evtcessao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2231_evtcessao_obj(doc, status, validar)
    return dados



def read_s2231_evtcessao_obj(doc, status, validar=False):
    s2231_evtcessao_dados = {}
    s2231_evtcessao_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2231_evtcessao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2231_evtcessao_dados['identidade'] = doc.eSocial.evtCessao['Id']
    evtCessao = doc.eSocial.evtCessao

    try: s2231_evtcessao_dados['indretif'] = evtCessao.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2231_evtcessao_dados['nrrecibo'] = evtCessao.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2231_evtcessao_dados['tpamb'] = evtCessao.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2231_evtcessao_dados['procemi'] = evtCessao.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2231_evtcessao_dados['verproc'] = evtCessao.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2231_evtcessao_dados['tpinsc'] = evtCessao.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2231_evtcessao_dados['nrinsc'] = evtCessao.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2231_evtcessao_dados['cpftrab'] = evtCessao.ideVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2231_evtcessao_dados['nistrab'] = evtCessao.ideVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2231_evtcessao_dados['matricula'] = evtCessao.ideVinculo.matricula.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtCessao.infoCessao): s2231_evtcessao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCessao.infoCessao): s2231_evtcessao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCessao.infoCessao): s2231_evtcessao_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2231_evtcessao', s2231_evtcessao_dados)
    resp = executar_sql(insert, True)
    s2231_evtcessao_id = resp[0][0]
    dados = s2231_evtcessao_dados
    dados['evento'] = 's2231'
    dados['id'] = s2231_evtcessao_id
    dados['identidade_evento'] = doc.eSocial.evtCessao['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'iniCessao' in dir(evtCessao.infoCessao) and evtCessao.infoCessao.iniCessao.cdata != '':
        for iniCessao in evtCessao.infoCessao.iniCessao:
            s2231_inicessao_dados = {}
            s2231_inicessao_dados['s2231_evtcessao_id'] = s2231_evtcessao_id

            try: s2231_inicessao_dados['dtinicessao'] = iniCessao.dtIniCessao.cdata
            except AttributeError: pass
            try: s2231_inicessao_dados['cnpjcess'] = iniCessao.cnpjCess.cdata
            except AttributeError: pass
            try: s2231_inicessao_dados['infonus'] = iniCessao.infOnus.cdata
            except AttributeError: pass
            try: s2231_inicessao_dados['indcessao'] = iniCessao.indCessao.cdata
            except AttributeError: pass
            try: s2231_inicessao_dados['dscsituacao'] = iniCessao.dscSituacao.cdata
            except AttributeError: pass
            insert = create_insert('s2231_inicessao', s2231_inicessao_dados)
            resp = executar_sql(insert, True)
            s2231_inicessao_id = resp[0][0]
            #print s2231_inicessao_id

    if 'fimCessao' in dir(evtCessao.infoCessao) and evtCessao.infoCessao.fimCessao.cdata != '':
        for fimCessao in evtCessao.infoCessao.fimCessao:
            s2231_fimcessao_dados = {}
            s2231_fimcessao_dados['s2231_evtcessao_id'] = s2231_evtcessao_id

            try: s2231_fimcessao_dados['dttermcessao'] = fimCessao.dtTermCessao.cdata
            except AttributeError: pass
            insert = create_insert('s2231_fimcessao', s2231_fimcessao_dados)
            resp = executar_sql(insert, True)
            s2231_fimcessao_id = resp[0][0]
            #print s2231_fimcessao_id

    from emensageriapro.esocial.views.s2231_evtcessao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2231_evtcessao_id, 'default')
    return dados