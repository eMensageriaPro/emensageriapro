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



def read_s1030_evttabcargo_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1030_evttabcargo_obj(doc, status, validar)
    return dados

def read_s1030_evttabcargo(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1030_evttabcargo_obj(doc, status, validar)
    return dados



def read_s1030_evttabcargo_obj(doc, status, validar=False):
    s1030_evttabcargo_dados = {}
    s1030_evttabcargo_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1030_evttabcargo_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1030_evttabcargo_dados['identidade'] = doc.eSocial.evtTabCargo['Id']
    evtTabCargo = doc.eSocial.evtTabCargo

    try: s1030_evttabcargo_dados['tpamb'] = evtTabCargo.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1030_evttabcargo_dados['procemi'] = evtTabCargo.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1030_evttabcargo_dados['verproc'] = evtTabCargo.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1030_evttabcargo_dados['tpinsc'] = evtTabCargo.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1030_evttabcargo_dados['nrinsc'] = evtTabCargo.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtTabCargo.infoCargo): s1030_evttabcargo_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabCargo.infoCargo): s1030_evttabcargo_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabCargo.infoCargo): s1030_evttabcargo_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1030_evttabcargo', s1030_evttabcargo_dados)
    resp = executar_sql(insert, True)
    s1030_evttabcargo_id = resp[0][0]
    dados = s1030_evttabcargo_dados
    dados['evento'] = 's1030'
    dados['id'] = s1030_evttabcargo_id
    dados['identidade_evento'] = doc.eSocial.evtTabCargo['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'inclusao' in dir(evtTabCargo.infoCargo) and evtTabCargo.infoCargo.inclusao.cdata != '':
        for inclusao in evtTabCargo.infoCargo.inclusao:
            s1030_inclusao_dados = {}
            s1030_inclusao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo_id

            try: s1030_inclusao_dados['codcargo'] = inclusao.ideCargo.codCargo.cdata
            except AttributeError: pass
            try: s1030_inclusao_dados['inivalid'] = inclusao.ideCargo.iniValid.cdata
            except AttributeError: pass
            try: s1030_inclusao_dados['fimvalid'] = inclusao.ideCargo.fimValid.cdata
            except AttributeError: pass
            try: s1030_inclusao_dados['nmcargo'] = inclusao.dadosCargo.nmCargo.cdata
            except AttributeError: pass
            try: s1030_inclusao_dados['codcbo'] = inclusao.dadosCargo.codCBO.cdata
            except AttributeError: pass
            insert = create_insert('s1030_inclusao', s1030_inclusao_dados)
            resp = executar_sql(insert, True)
            s1030_inclusao_id = resp[0][0]
            #print s1030_inclusao_id

            if 'cargoPublico' in dir(inclusao.dadosCargo) and inclusao.dadosCargo.cargoPublico.cdata != '':
                for cargoPublico in inclusao.dadosCargo.cargoPublico:
                    s1030_inclusao_cargopublico_dados = {}
                    s1030_inclusao_cargopublico_dados['s1030_inclusao_id'] = s1030_inclusao_id

                    try: s1030_inclusao_cargopublico_dados['acumcargo'] = cargoPublico.acumCargo.cdata
                    except AttributeError: pass
                    try: s1030_inclusao_cargopublico_dados['contagemesp'] = cargoPublico.contagemEsp.cdata
                    except AttributeError: pass
                    try: s1030_inclusao_cargopublico_dados['dedicexcl'] = cargoPublico.dedicExcl.cdata
                    except AttributeError: pass
                    try: s1030_inclusao_cargopublico_dados['codcarreira'] = cargoPublico.codCarreira.cdata
                    except AttributeError: pass
                    try: s1030_inclusao_cargopublico_dados['nrlei'] = cargoPublico.leiCargo.nrLei.cdata
                    except AttributeError: pass
                    try: s1030_inclusao_cargopublico_dados['dtlei'] = cargoPublico.leiCargo.dtLei.cdata
                    except AttributeError: pass
                    try: s1030_inclusao_cargopublico_dados['sitcargo'] = cargoPublico.leiCargo.sitCargo.cdata
                    except AttributeError: pass
                    insert = create_insert('s1030_inclusao_cargopublico', s1030_inclusao_cargopublico_dados)
                    resp = executar_sql(insert, True)
                    s1030_inclusao_cargopublico_id = resp[0][0]
                    #print s1030_inclusao_cargopublico_id

    if 'alteracao' in dir(evtTabCargo.infoCargo) and evtTabCargo.infoCargo.alteracao.cdata != '':
        for alteracao in evtTabCargo.infoCargo.alteracao:
            s1030_alteracao_dados = {}
            s1030_alteracao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo_id

            try: s1030_alteracao_dados['codcargo'] = alteracao.ideCargo.codCargo.cdata
            except AttributeError: pass
            try: s1030_alteracao_dados['inivalid'] = alteracao.ideCargo.iniValid.cdata
            except AttributeError: pass
            try: s1030_alteracao_dados['fimvalid'] = alteracao.ideCargo.fimValid.cdata
            except AttributeError: pass
            try: s1030_alteracao_dados['nmcargo'] = alteracao.dadosCargo.nmCargo.cdata
            except AttributeError: pass
            try: s1030_alteracao_dados['codcbo'] = alteracao.dadosCargo.codCBO.cdata
            except AttributeError: pass
            insert = create_insert('s1030_alteracao', s1030_alteracao_dados)
            resp = executar_sql(insert, True)
            s1030_alteracao_id = resp[0][0]
            #print s1030_alteracao_id

            if 'cargoPublico' in dir(alteracao.dadosCargo) and alteracao.dadosCargo.cargoPublico.cdata != '':
                for cargoPublico in alteracao.dadosCargo.cargoPublico:
                    s1030_alteracao_cargopublico_dados = {}
                    s1030_alteracao_cargopublico_dados['s1030_alteracao_id'] = s1030_alteracao_id

                    try: s1030_alteracao_cargopublico_dados['acumcargo'] = cargoPublico.acumCargo.cdata
                    except AttributeError: pass
                    try: s1030_alteracao_cargopublico_dados['contagemesp'] = cargoPublico.contagemEsp.cdata
                    except AttributeError: pass
                    try: s1030_alteracao_cargopublico_dados['dedicexcl'] = cargoPublico.dedicExcl.cdata
                    except AttributeError: pass
                    try: s1030_alteracao_cargopublico_dados['codcarreira'] = cargoPublico.codCarreira.cdata
                    except AttributeError: pass
                    try: s1030_alteracao_cargopublico_dados['nrlei'] = cargoPublico.leiCargo.nrLei.cdata
                    except AttributeError: pass
                    try: s1030_alteracao_cargopublico_dados['dtlei'] = cargoPublico.leiCargo.dtLei.cdata
                    except AttributeError: pass
                    try: s1030_alteracao_cargopublico_dados['sitcargo'] = cargoPublico.leiCargo.sitCargo.cdata
                    except AttributeError: pass
                    insert = create_insert('s1030_alteracao_cargopublico', s1030_alteracao_cargopublico_dados)
                    resp = executar_sql(insert, True)
                    s1030_alteracao_cargopublico_id = resp[0][0]
                    #print s1030_alteracao_cargopublico_id

            if 'novaValidade' in dir(alteracao) and alteracao.novaValidade.cdata != '':
                for novaValidade in alteracao.novaValidade:
                    s1030_alteracao_novavalidade_dados = {}
                    s1030_alteracao_novavalidade_dados['s1030_alteracao_id'] = s1030_alteracao_id

                    try: s1030_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: pass
                    try: s1030_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: pass
                    insert = create_insert('s1030_alteracao_novavalidade', s1030_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1030_alteracao_novavalidade_id = resp[0][0]
                    #print s1030_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabCargo.infoCargo) and evtTabCargo.infoCargo.exclusao.cdata != '':
        for exclusao in evtTabCargo.infoCargo.exclusao:
            s1030_exclusao_dados = {}
            s1030_exclusao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo_id

            try: s1030_exclusao_dados['codcargo'] = exclusao.ideCargo.codCargo.cdata
            except AttributeError: pass
            try: s1030_exclusao_dados['inivalid'] = exclusao.ideCargo.iniValid.cdata
            except AttributeError: pass
            try: s1030_exclusao_dados['fimvalid'] = exclusao.ideCargo.fimValid.cdata
            except AttributeError: pass
            insert = create_insert('s1030_exclusao', s1030_exclusao_dados)
            resp = executar_sql(insert, True)
            s1030_exclusao_id = resp[0][0]
            #print s1030_exclusao_id

    from emensageriapro.esocial.views.s1030_evttabcargo_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1030_evttabcargo_id, 'default')
    return dados