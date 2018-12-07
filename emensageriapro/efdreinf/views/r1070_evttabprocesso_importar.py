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


def read_r1070_evttabprocesso_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_r1070_evttabprocesso_obj(doc, status, validar)
    return dados

def read_r1070_evttabprocesso(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    dados = read_r1070_evttabprocesso_obj(doc, status, validar)
    return dados



def read_r1070_evttabprocesso_obj(doc, status, validar=False):
    r1070_evttabprocesso_dados = {}
    r1070_evttabprocesso_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r1070_evttabprocesso_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r1070_evttabprocesso_dados['identidade'] = doc.Reinf.evtTabProcesso['id']
    r1070_evttabprocesso_dados['processamento_codigo_resposta'] = 1
    evtTabProcesso = doc.Reinf.evtTabProcesso

    if 'tpAmb' in dir(evtTabProcesso.ideEvento): r1070_evttabprocesso_dados['tpamb'] = evtTabProcesso.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabProcesso.ideEvento): r1070_evttabprocesso_dados['procemi'] = evtTabProcesso.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabProcesso.ideEvento): r1070_evttabprocesso_dados['verproc'] = evtTabProcesso.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabProcesso.ideContri): r1070_evttabprocesso_dados['tpinsc'] = evtTabProcesso.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtTabProcesso.ideContri): r1070_evttabprocesso_dados['nrinsc'] = evtTabProcesso.ideContri.nrInsc.cdata
    if 'inclusao' in dir(evtTabProcesso.infoProcesso): r1070_evttabprocesso_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabProcesso.infoProcesso): r1070_evttabprocesso_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabProcesso.infoProcesso): r1070_evttabprocesso_dados['operacao'] = 3
    #print dados
    insert = create_insert('r1070_evttabprocesso', r1070_evttabprocesso_dados)
    resp = executar_sql(insert, True)
    r1070_evttabprocesso_id = resp[0][0]
    dados = r1070_evttabprocesso_dados
    dados['evento'] = 'r1070'
    dados['id'] = r1070_evttabprocesso_id
    dados['identidade_evento'] = doc.Reinf.evtTabProcesso['id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabProcesso.infoProcesso):
        for inclusao in evtTabProcesso.infoProcesso.inclusao:
            r1070_inclusao_dados = {}
            r1070_inclusao_dados['r1070_evttabprocesso_id'] = r1070_evttabprocesso_id
       
            if 'tpProc' in dir(inclusao.ideProcesso): r1070_inclusao_dados['tpproc'] = inclusao.ideProcesso.tpProc.cdata
            if 'nrProc' in dir(inclusao.ideProcesso): r1070_inclusao_dados['nrproc'] = inclusao.ideProcesso.nrProc.cdata
            if 'iniValid' in dir(inclusao.ideProcesso): r1070_inclusao_dados['inivalid'] = inclusao.ideProcesso.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideProcesso): r1070_inclusao_dados['fimvalid'] = inclusao.ideProcesso.fimValid.cdata
            if 'indAutoria' in dir(inclusao.ideProcesso): r1070_inclusao_dados['indautoria'] = inclusao.ideProcesso.indAutoria.cdata
            insert = create_insert('r1070_inclusao', r1070_inclusao_dados)
            resp = executar_sql(insert, True)
            r1070_inclusao_id = resp[0][0]
            #print r1070_inclusao_id

            if 'infoSusp' in dir(inclusao.ideProcesso):
                for infoSusp in inclusao.ideProcesso.infoSusp:
                    r1070_inclusao_infosusp_dados = {}
                    r1070_inclusao_infosusp_dados['r1070_inclusao_id'] = r1070_inclusao_id
               
                    if 'codSusp' in dir(infoSusp): r1070_inclusao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    if 'indSusp' in dir(infoSusp): r1070_inclusao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    if 'dtDecisao' in dir(infoSusp): r1070_inclusao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    if 'indDeposito' in dir(infoSusp): r1070_inclusao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    insert = create_insert('r1070_inclusao_infosusp', r1070_inclusao_infosusp_dados)
                    resp = executar_sql(insert, True)
                    r1070_inclusao_infosusp_id = resp[0][0]
                    #print r1070_inclusao_infosusp_id
   
            if 'dadosProcJud' in dir(inclusao.ideProcesso):
                for dadosProcJud in inclusao.ideProcesso.dadosProcJud:
                    r1070_inclusao_dadosprocjud_dados = {}
                    r1070_inclusao_dadosprocjud_dados['r1070_inclusao_id'] = r1070_inclusao_id
               
                    if 'ufVara' in dir(dadosProcJud): r1070_inclusao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    if 'codMunic' in dir(dadosProcJud): r1070_inclusao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    if 'idVara' in dir(dadosProcJud): r1070_inclusao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    insert = create_insert('r1070_inclusao_dadosprocjud', r1070_inclusao_dadosprocjud_dados)
                    resp = executar_sql(insert, True)
                    r1070_inclusao_dadosprocjud_id = resp[0][0]
                    #print r1070_inclusao_dadosprocjud_id
   
    if 'alteracao' in dir(evtTabProcesso.infoProcesso):
        for alteracao in evtTabProcesso.infoProcesso.alteracao:
            r1070_alteracao_dados = {}
            r1070_alteracao_dados['r1070_evttabprocesso_id'] = r1070_evttabprocesso_id
       
            if 'tpProc' in dir(alteracao.ideProcesso): r1070_alteracao_dados['tpproc'] = alteracao.ideProcesso.tpProc.cdata
            if 'nrProc' in dir(alteracao.ideProcesso): r1070_alteracao_dados['nrproc'] = alteracao.ideProcesso.nrProc.cdata
            if 'iniValid' in dir(alteracao.ideProcesso): r1070_alteracao_dados['inivalid'] = alteracao.ideProcesso.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideProcesso): r1070_alteracao_dados['fimvalid'] = alteracao.ideProcesso.fimValid.cdata
            if 'indAutoria' in dir(alteracao.ideProcesso): r1070_alteracao_dados['indautoria'] = alteracao.ideProcesso.indAutoria.cdata
            insert = create_insert('r1070_alteracao', r1070_alteracao_dados)
            resp = executar_sql(insert, True)
            r1070_alteracao_id = resp[0][0]
            #print r1070_alteracao_id

            if 'infoSusp' in dir(alteracao.ideProcesso):
                for infoSusp in alteracao.ideProcesso.infoSusp:
                    r1070_alteracao_infosusp_dados = {}
                    r1070_alteracao_infosusp_dados['r1070_alteracao_id'] = r1070_alteracao_id
               
                    if 'codSusp' in dir(infoSusp): r1070_alteracao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    if 'indSusp' in dir(infoSusp): r1070_alteracao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    if 'dtDecisao' in dir(infoSusp): r1070_alteracao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    if 'indDeposito' in dir(infoSusp): r1070_alteracao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    insert = create_insert('r1070_alteracao_infosusp', r1070_alteracao_infosusp_dados)
                    resp = executar_sql(insert, True)
                    r1070_alteracao_infosusp_id = resp[0][0]
                    #print r1070_alteracao_infosusp_id
   
            if 'dadosProcJud' in dir(alteracao.ideProcesso):
                for dadosProcJud in alteracao.ideProcesso.dadosProcJud:
                    r1070_alteracao_dadosprocjud_dados = {}
                    r1070_alteracao_dadosprocjud_dados['r1070_alteracao_id'] = r1070_alteracao_id
               
                    if 'ufVara' in dir(dadosProcJud): r1070_alteracao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    if 'codMunic' in dir(dadosProcJud): r1070_alteracao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    if 'idVara' in dir(dadosProcJud): r1070_alteracao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    insert = create_insert('r1070_alteracao_dadosprocjud', r1070_alteracao_dadosprocjud_dados)
                    resp = executar_sql(insert, True)
                    r1070_alteracao_dadosprocjud_id = resp[0][0]
                    #print r1070_alteracao_dadosprocjud_id
   
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    r1070_alteracao_novavalidade_dados = {}
                    r1070_alteracao_novavalidade_dados['r1070_alteracao_id'] = r1070_alteracao_id
               
                    if 'iniValid' in dir(novaValidade): r1070_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): r1070_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('r1070_alteracao_novavalidade', r1070_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    r1070_alteracao_novavalidade_id = resp[0][0]
                    #print r1070_alteracao_novavalidade_id
   
    if 'exclusao' in dir(evtTabProcesso.infoProcesso):
        for exclusao in evtTabProcesso.infoProcesso.exclusao:
            r1070_exclusao_dados = {}
            r1070_exclusao_dados['r1070_evttabprocesso_id'] = r1070_evttabprocesso_id
       
            if 'tpProc' in dir(exclusao.ideProcesso): r1070_exclusao_dados['tpproc'] = exclusao.ideProcesso.tpProc.cdata
            if 'nrProc' in dir(exclusao.ideProcesso): r1070_exclusao_dados['nrproc'] = exclusao.ideProcesso.nrProc.cdata
            if 'iniValid' in dir(exclusao.ideProcesso): r1070_exclusao_dados['inivalid'] = exclusao.ideProcesso.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideProcesso): r1070_exclusao_dados['fimvalid'] = exclusao.ideProcesso.fimValid.cdata
            insert = create_insert('r1070_exclusao', r1070_exclusao_dados)
            resp = executar_sql(insert, True)
            r1070_exclusao_id = resp[0][0]
            #print r1070_exclusao_id

    from emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r1070_evttabprocesso_id, 'default')
    return dados