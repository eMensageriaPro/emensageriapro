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


def read_s1080_evttaboperport_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1080_evttaboperport_obj(doc, status, validar)
    return dados

def read_s1080_evttaboperport(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1080_evttaboperport_obj(doc, status, validar)
    return dados



def read_s1080_evttaboperport_obj(doc, status, validar=False):
    s1080_evttaboperport_dados = {}
    s1080_evttaboperport_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1080_evttaboperport_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1080_evttaboperport_dados['identidade'] = doc.eSocial.evtTabOperPort['Id']
    s1080_evttaboperport_dados['processamento_codigo_resposta'] = 1
    evtTabOperPort = doc.eSocial.evtTabOperPort

    if 'tpAmb' in dir(evtTabOperPort.ideEvento): s1080_evttaboperport_dados['tpamb'] = evtTabOperPort.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabOperPort.ideEvento): s1080_evttaboperport_dados['procemi'] = evtTabOperPort.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabOperPort.ideEvento): s1080_evttaboperport_dados['verproc'] = evtTabOperPort.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabOperPort.ideEmpregador): s1080_evttaboperport_dados['tpinsc'] = evtTabOperPort.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabOperPort.ideEmpregador): s1080_evttaboperport_dados['nrinsc'] = evtTabOperPort.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1080_evttaboperport', s1080_evttaboperport_dados)
    resp = executar_sql(insert, True)
    s1080_evttaboperport_id = resp[0][0]
    dados = s1080_evttaboperport_dados
    dados['evento'] = 's1080'
    dados['id'] = s1080_evttaboperport_id
    dados['identidade_evento'] = doc.eSocial.evtTabOperPort['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabOperPort.infoOperPortuario):
        for inclusao in evtTabOperPort.infoOperPortuario.inclusao:
            s1080_inclusao_dados = {}
            s1080_inclusao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport_id

            if 'cnpjOpPortuario' in dir(inclusao.ideOperPortuario): s1080_inclusao_dados['cnpjopportuario'] = inclusao.ideOperPortuario.cnpjOpPortuario.cdata
            if 'iniValid' in dir(inclusao.ideOperPortuario): s1080_inclusao_dados['inivalid'] = inclusao.ideOperPortuario.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideOperPortuario): s1080_inclusao_dados['fimvalid'] = inclusao.ideOperPortuario.fimValid.cdata
            if 'aliqRat' in dir(inclusao.dadosOperPortuario): s1080_inclusao_dados['aliqrat'] = inclusao.dadosOperPortuario.aliqRat.cdata
            if 'fap' in dir(inclusao.dadosOperPortuario): s1080_inclusao_dados['fap'] = inclusao.dadosOperPortuario.fap.cdata
            if 'aliqRatAjust' in dir(inclusao.dadosOperPortuario): s1080_inclusao_dados['aliqratajust'] = inclusao.dadosOperPortuario.aliqRatAjust.cdata
            insert = create_insert('s1080_inclusao', s1080_inclusao_dados)
            resp = executar_sql(insert, True)
            s1080_inclusao_id = resp[0][0]
            #print s1080_inclusao_id

    if 'alteracao' in dir(evtTabOperPort.infoOperPortuario):
        for alteracao in evtTabOperPort.infoOperPortuario.alteracao:
            s1080_alteracao_dados = {}
            s1080_alteracao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport_id

            if 'cnpjOpPortuario' in dir(alteracao.ideOperPortuario): s1080_alteracao_dados['cnpjopportuario'] = alteracao.ideOperPortuario.cnpjOpPortuario.cdata
            if 'iniValid' in dir(alteracao.ideOperPortuario): s1080_alteracao_dados['inivalid'] = alteracao.ideOperPortuario.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideOperPortuario): s1080_alteracao_dados['fimvalid'] = alteracao.ideOperPortuario.fimValid.cdata
            if 'aliqRat' in dir(alteracao.dadosOperPortuario): s1080_alteracao_dados['aliqrat'] = alteracao.dadosOperPortuario.aliqRat.cdata
            if 'fap' in dir(alteracao.dadosOperPortuario): s1080_alteracao_dados['fap'] = alteracao.dadosOperPortuario.fap.cdata
            if 'aliqRatAjust' in dir(alteracao.dadosOperPortuario): s1080_alteracao_dados['aliqratajust'] = alteracao.dadosOperPortuario.aliqRatAjust.cdata
            insert = create_insert('s1080_alteracao', s1080_alteracao_dados)
            resp = executar_sql(insert, True)
            s1080_alteracao_id = resp[0][0]
            #print s1080_alteracao_id

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1080_alteracao_novavalidade_dados = {}
                    s1080_alteracao_novavalidade_dados['s1080_alteracao_id'] = s1080_alteracao_id

                    if 'iniValid' in dir(novaValidade): s1080_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1080_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1080_alteracao_novavalidade', s1080_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1080_alteracao_novavalidade_id = resp[0][0]
                    #print s1080_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabOperPort.infoOperPortuario):
        for exclusao in evtTabOperPort.infoOperPortuario.exclusao:
            s1080_exclusao_dados = {}
            s1080_exclusao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport_id

            if 'cnpjOpPortuario' in dir(exclusao.ideOperPortuario): s1080_exclusao_dados['cnpjopportuario'] = exclusao.ideOperPortuario.cnpjOpPortuario.cdata
            if 'iniValid' in dir(exclusao.ideOperPortuario): s1080_exclusao_dados['inivalid'] = exclusao.ideOperPortuario.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideOperPortuario): s1080_exclusao_dados['fimvalid'] = exclusao.ideOperPortuario.fimValid.cdata
            insert = create_insert('s1080_exclusao', s1080_exclusao_dados)
            resp = executar_sql(insert, True)
            s1080_exclusao_id = resp[0][0]
            #print s1080_exclusao_id

    from emensageriapro.esocial.views.s1080_evttaboperport_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1080_evttaboperport_id, 'default')
    return dados