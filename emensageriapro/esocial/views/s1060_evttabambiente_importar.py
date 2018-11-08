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


def read_s1060_evttabambiente_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1060_evttabambiente_obj(doc, status, validar)
    return dados

def read_s1060_evttabambiente(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_s1060_evttabambiente_obj(doc, status, validar)
    return dados



def read_s1060_evttabambiente_obj(doc, status, validar=False):
    s1060_evttabambiente_dados = {}
    s1060_evttabambiente_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1060_evttabambiente_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1060_evttabambiente_dados['identidade'] = doc.eSocial.evtTabAmbiente['Id']
    s1060_evttabambiente_dados['processamento_codigo_resposta'] = 1
    evtTabAmbiente = doc.eSocial.evtTabAmbiente

    if 'tpAmb' in dir(evtTabAmbiente.ideEvento): s1060_evttabambiente_dados['tpamb'] = evtTabAmbiente.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabAmbiente.ideEvento): s1060_evttabambiente_dados['procemi'] = evtTabAmbiente.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabAmbiente.ideEvento): s1060_evttabambiente_dados['verproc'] = evtTabAmbiente.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabAmbiente.ideEmpregador): s1060_evttabambiente_dados['tpinsc'] = evtTabAmbiente.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabAmbiente.ideEmpregador): s1060_evttabambiente_dados['nrinsc'] = evtTabAmbiente.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1060_evttabambiente', s1060_evttabambiente_dados)
    resp = executar_sql(insert, True)
    s1060_evttabambiente_id = resp[0][0]
    dados = s1060_evttabambiente_dados
    dados['evento'] = 's1060'
    dados['id'] = s1060_evttabambiente_id
    dados['identidade_evento'] = doc.eSocial.evtTabAmbiente['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabAmbiente.infoAmbiente):
        for inclusao in evtTabAmbiente.infoAmbiente.inclusao:
            s1060_inclusao_dados = {}
            s1060_inclusao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente_id
       
            if 'codAmb' in dir(inclusao.ideAmbiente): s1060_inclusao_dados['codamb'] = inclusao.ideAmbiente.codAmb.cdata
            if 'iniValid' in dir(inclusao.ideAmbiente): s1060_inclusao_dados['inivalid'] = inclusao.ideAmbiente.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideAmbiente): s1060_inclusao_dados['fimvalid'] = inclusao.ideAmbiente.fimValid.cdata
            if 'dscAmb' in dir(inclusao.dadosAmbiente): s1060_inclusao_dados['dscamb'] = inclusao.dadosAmbiente.dscAmb.cdata
            if 'localAmb' in dir(inclusao.dadosAmbiente): s1060_inclusao_dados['localamb'] = inclusao.dadosAmbiente.localAmb.cdata
            if 'tpInsc' in dir(inclusao.dadosAmbiente): s1060_inclusao_dados['tpinsc'] = inclusao.dadosAmbiente.tpInsc.cdata
            if 'nrInsc' in dir(inclusao.dadosAmbiente): s1060_inclusao_dados['nrinsc'] = inclusao.dadosAmbiente.nrInsc.cdata
            if 'codLotacao' in dir(inclusao.dadosAmbiente): s1060_inclusao_dados['codlotacao'] = inclusao.dadosAmbiente.codLotacao.cdata
            insert = create_insert('s1060_inclusao', s1060_inclusao_dados)
            resp = executar_sql(insert, True)
            s1060_inclusao_id = resp[0][0]
            #print s1060_inclusao_id

    if 'alteracao' in dir(evtTabAmbiente.infoAmbiente):
        for alteracao in evtTabAmbiente.infoAmbiente.alteracao:
            s1060_alteracao_dados = {}
            s1060_alteracao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente_id
       
            if 'codAmb' in dir(alteracao.ideAmbiente): s1060_alteracao_dados['codamb'] = alteracao.ideAmbiente.codAmb.cdata
            if 'iniValid' in dir(alteracao.ideAmbiente): s1060_alteracao_dados['inivalid'] = alteracao.ideAmbiente.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideAmbiente): s1060_alteracao_dados['fimvalid'] = alteracao.ideAmbiente.fimValid.cdata
            if 'dscAmb' in dir(alteracao.dadosAmbiente): s1060_alteracao_dados['dscamb'] = alteracao.dadosAmbiente.dscAmb.cdata
            if 'localAmb' in dir(alteracao.dadosAmbiente): s1060_alteracao_dados['localamb'] = alteracao.dadosAmbiente.localAmb.cdata
            if 'tpInsc' in dir(alteracao.dadosAmbiente): s1060_alteracao_dados['tpinsc'] = alteracao.dadosAmbiente.tpInsc.cdata
            if 'nrInsc' in dir(alteracao.dadosAmbiente): s1060_alteracao_dados['nrinsc'] = alteracao.dadosAmbiente.nrInsc.cdata
            if 'codLotacao' in dir(alteracao.dadosAmbiente): s1060_alteracao_dados['codlotacao'] = alteracao.dadosAmbiente.codLotacao.cdata
            insert = create_insert('s1060_alteracao', s1060_alteracao_dados)
            resp = executar_sql(insert, True)
            s1060_alteracao_id = resp[0][0]
            #print s1060_alteracao_id

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1060_alteracao_novavalidade_dados = {}
                    s1060_alteracao_novavalidade_dados['s1060_alteracao_id'] = s1060_alteracao_id
               
                    if 'iniValid' in dir(novaValidade): s1060_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1060_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1060_alteracao_novavalidade', s1060_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1060_alteracao_novavalidade_id = resp[0][0]
                    #print s1060_alteracao_novavalidade_id
   
    if 'exclusao' in dir(evtTabAmbiente.infoAmbiente):
        for exclusao in evtTabAmbiente.infoAmbiente.exclusao:
            s1060_exclusao_dados = {}
            s1060_exclusao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente_id
       
            if 'codAmb' in dir(exclusao.ideAmbiente): s1060_exclusao_dados['codamb'] = exclusao.ideAmbiente.codAmb.cdata
            if 'iniValid' in dir(exclusao.ideAmbiente): s1060_exclusao_dados['inivalid'] = exclusao.ideAmbiente.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideAmbiente): s1060_exclusao_dados['fimvalid'] = exclusao.ideAmbiente.fimValid.cdata
            insert = create_insert('s1060_exclusao', s1060_exclusao_dados)
            resp = executar_sql(insert, True)
            s1060_exclusao_id = resp[0][0]
            #print s1060_exclusao_id

    from emensageriapro.esocial.views.s1060_evttabambiente_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1060_evttabambiente_id, 'default')
    return dados