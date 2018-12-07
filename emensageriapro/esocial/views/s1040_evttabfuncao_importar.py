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


def read_s1040_evttabfuncao_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1040_evttabfuncao_obj(doc, status, validar)
    return dados

def read_s1040_evttabfuncao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1040_evttabfuncao_obj(doc, status, validar)
    return dados



def read_s1040_evttabfuncao_obj(doc, status, validar=False):
    s1040_evttabfuncao_dados = {}
    s1040_evttabfuncao_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1040_evttabfuncao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1040_evttabfuncao_dados['identidade'] = doc.eSocial.evtTabFuncao['Id']
    s1040_evttabfuncao_dados['processamento_codigo_resposta'] = 1
    evtTabFuncao = doc.eSocial.evtTabFuncao

    if 'tpAmb' in dir(evtTabFuncao.ideEvento): s1040_evttabfuncao_dados['tpamb'] = evtTabFuncao.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabFuncao.ideEvento): s1040_evttabfuncao_dados['procemi'] = evtTabFuncao.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabFuncao.ideEvento): s1040_evttabfuncao_dados['verproc'] = evtTabFuncao.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabFuncao.ideEmpregador): s1040_evttabfuncao_dados['tpinsc'] = evtTabFuncao.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabFuncao.ideEmpregador): s1040_evttabfuncao_dados['nrinsc'] = evtTabFuncao.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabFuncao.infoFuncao): s1040_evttabfuncao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabFuncao.infoFuncao): s1040_evttabfuncao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabFuncao.infoFuncao): s1040_evttabfuncao_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1040_evttabfuncao', s1040_evttabfuncao_dados)
    resp = executar_sql(insert, True)
    s1040_evttabfuncao_id = resp[0][0]
    dados = s1040_evttabfuncao_dados
    dados['evento'] = 's1040'
    dados['id'] = s1040_evttabfuncao_id
    dados['identidade_evento'] = doc.eSocial.evtTabFuncao['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabFuncao.infoFuncao):
        for inclusao in evtTabFuncao.infoFuncao.inclusao:
            s1040_inclusao_dados = {}
            s1040_inclusao_dados['s1040_evttabfuncao_id'] = s1040_evttabfuncao_id
       
            if 'codFuncao' in dir(inclusao.ideFuncao): s1040_inclusao_dados['codfuncao'] = inclusao.ideFuncao.codFuncao.cdata
            if 'iniValid' in dir(inclusao.ideFuncao): s1040_inclusao_dados['inivalid'] = inclusao.ideFuncao.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideFuncao): s1040_inclusao_dados['fimvalid'] = inclusao.ideFuncao.fimValid.cdata
            if 'dscFuncao' in dir(inclusao.dadosFuncao): s1040_inclusao_dados['dscfuncao'] = inclusao.dadosFuncao.dscFuncao.cdata
            if 'codCBO' in dir(inclusao.dadosFuncao): s1040_inclusao_dados['codcbo'] = inclusao.dadosFuncao.codCBO.cdata
            insert = create_insert('s1040_inclusao', s1040_inclusao_dados)
            resp = executar_sql(insert, True)
            s1040_inclusao_id = resp[0][0]
            #print s1040_inclusao_id

    if 'alteracao' in dir(evtTabFuncao.infoFuncao):
        for alteracao in evtTabFuncao.infoFuncao.alteracao:
            s1040_alteracao_dados = {}
            s1040_alteracao_dados['s1040_evttabfuncao_id'] = s1040_evttabfuncao_id
       
            if 'codFuncao' in dir(alteracao.ideFuncao): s1040_alteracao_dados['codfuncao'] = alteracao.ideFuncao.codFuncao.cdata
            if 'iniValid' in dir(alteracao.ideFuncao): s1040_alteracao_dados['inivalid'] = alteracao.ideFuncao.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideFuncao): s1040_alteracao_dados['fimvalid'] = alteracao.ideFuncao.fimValid.cdata
            if 'dscFuncao' in dir(alteracao.dadosFuncao): s1040_alteracao_dados['dscfuncao'] = alteracao.dadosFuncao.dscFuncao.cdata
            if 'codCBO' in dir(alteracao.dadosFuncao): s1040_alteracao_dados['codcbo'] = alteracao.dadosFuncao.codCBO.cdata
            insert = create_insert('s1040_alteracao', s1040_alteracao_dados)
            resp = executar_sql(insert, True)
            s1040_alteracao_id = resp[0][0]
            #print s1040_alteracao_id

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1040_alteracao_novavalidade_dados = {}
                    s1040_alteracao_novavalidade_dados['s1040_alteracao_id'] = s1040_alteracao_id
               
                    if 'iniValid' in dir(novaValidade): s1040_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1040_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1040_alteracao_novavalidade', s1040_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1040_alteracao_novavalidade_id = resp[0][0]
                    #print s1040_alteracao_novavalidade_id
   
    if 'exclusao' in dir(evtTabFuncao.infoFuncao):
        for exclusao in evtTabFuncao.infoFuncao.exclusao:
            s1040_exclusao_dados = {}
            s1040_exclusao_dados['s1040_evttabfuncao_id'] = s1040_evttabfuncao_id
       
            if 'codFuncao' in dir(exclusao.ideFuncao): s1040_exclusao_dados['codfuncao'] = exclusao.ideFuncao.codFuncao.cdata
            if 'iniValid' in dir(exclusao.ideFuncao): s1040_exclusao_dados['inivalid'] = exclusao.ideFuncao.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideFuncao): s1040_exclusao_dados['fimvalid'] = exclusao.ideFuncao.fimValid.cdata
            insert = create_insert('s1040_exclusao', s1040_exclusao_dados)
            resp = executar_sql(insert, True)
            s1040_exclusao_id = resp[0][0]
            #print s1040_exclusao_id

    from emensageriapro.esocial.views.s1040_evttabfuncao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1040_evttabfuncao_id, 'default')
    return dados