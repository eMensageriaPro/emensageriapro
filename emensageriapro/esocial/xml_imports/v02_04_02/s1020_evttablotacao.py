#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
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


def read_s1020_evttablotacao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s1020_evttablotacao_obj(doc, status)



def read_s1020_evttablotacao_obj(doc):
    s1020_evttablotacao_dados = {}
    s1020_evttablotacao_dados['versao'] = 'v02_04_02'
    s1020_evttablotacao_dados['status'] = status
    s1020_evttablotacao_dados['identidade'] = doc.eSocial.evtTabLotacao['Id']
    s1020_evttablotacao_dados['processamento_codigo_resposta'] = 1
    evtTabLotacao = doc.eSocial.evtTabLotacao
    
    if 'tpAmb' in dir(evtTabLotacao.ideEvento): s1020_evttablotacao_dados['tpamb'] = evtTabLotacao.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabLotacao.ideEvento): s1020_evttablotacao_dados['procemi'] = evtTabLotacao.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabLotacao.ideEvento): s1020_evttablotacao_dados['verproc'] = evtTabLotacao.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabLotacao.ideEmpregador): s1020_evttablotacao_dados['tpinsc'] = evtTabLotacao.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabLotacao.ideEmpregador): s1020_evttablotacao_dados['nrinsc'] = evtTabLotacao.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1020_evttablotacao', s1020_evttablotacao_dados)
    resp = executar_sql(insert, True)
    s1020_evttablotacao_id = resp[0][0]
    dados = s1020_evttablotacao_dados
    dados['evento'] = 's1020'
    dados['id'] = s1020_evttablotacao_id
    dados['identidade_evento'] = doc.eSocial.evtTabLotacao['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabLotacao.infoLotacao):
        for inclusao in evtTabLotacao.infoLotacao.inclusao:
            s1020_inclusao_dados = {}
            s1020_inclusao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao_id
            
            if 'codLotacao' in dir(inclusao.ideLotacao): s1020_inclusao_dados['codlotacao'] = inclusao.ideLotacao.codLotacao.cdata
            if 'iniValid' in dir(inclusao.ideLotacao): s1020_inclusao_dados['inivalid'] = inclusao.ideLotacao.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideLotacao): s1020_inclusao_dados['fimvalid'] = inclusao.ideLotacao.fimValid.cdata
            if 'tpLotacao' in dir(inclusao.dadosLotacao): s1020_inclusao_dados['tplotacao'] = inclusao.dadosLotacao.tpLotacao.cdata
            if 'tpInsc' in dir(inclusao.dadosLotacao): s1020_inclusao_dados['tpinsc'] = inclusao.dadosLotacao.tpInsc.cdata
            if 'nrInsc' in dir(inclusao.dadosLotacao): s1020_inclusao_dados['nrinsc'] = inclusao.dadosLotacao.nrInsc.cdata
            if 'fpas' in dir(inclusao.dadosLotacao.fpasLotacao): s1020_inclusao_dados['fpas'] = inclusao.dadosLotacao.fpasLotacao.fpas.cdata
            if 'codTercs' in dir(inclusao.dadosLotacao.fpasLotacao): s1020_inclusao_dados['codtercs'] = inclusao.dadosLotacao.fpasLotacao.codTercs.cdata
            if 'codTercsSusp' in dir(inclusao.dadosLotacao.fpasLotacao): s1020_inclusao_dados['codtercssusp'] = inclusao.dadosLotacao.fpasLotacao.codTercsSusp.cdata
            insert = create_insert('s1020_inclusao', s1020_inclusao_dados)
            resp = executar_sql(insert, True)
            s1020_inclusao_id = resp[0][0]
            #print s1020_inclusao_id

            if 'infoProcJudTerceiros' in dir(inclusao.dadosLotacao.fpasLotacao):
                for infoProcJudTerceiros in inclusao.dadosLotacao.fpasLotacao.infoProcJudTerceiros:
                    s1020_inclusao_infoprocjudterceiros_dados = {}
                    s1020_inclusao_infoprocjudterceiros_dados['s1020_inclusao_id'] = s1020_inclusao_id
                    
                    insert = create_insert('s1020_inclusao_infoprocjudterceiros', s1020_inclusao_infoprocjudterceiros_dados)
                    resp = executar_sql(insert, True)
                    s1020_inclusao_infoprocjudterceiros_id = resp[0][0]
                    #print s1020_inclusao_infoprocjudterceiros_id
        
            if 'infoEmprParcial' in dir(inclusao.dadosLotacao):
                for infoEmprParcial in inclusao.dadosLotacao.infoEmprParcial:
                    s1020_inclusao_infoemprparcial_dados = {}
                    s1020_inclusao_infoemprparcial_dados['s1020_inclusao_id'] = s1020_inclusao_id
                    
                    if 'tpInscContrat' in dir(infoEmprParcial): s1020_inclusao_infoemprparcial_dados['tpinsccontrat'] = infoEmprParcial.tpInscContrat.cdata
                    if 'nrInscContrat' in dir(infoEmprParcial): s1020_inclusao_infoemprparcial_dados['nrinsccontrat'] = infoEmprParcial.nrInscContrat.cdata
                    if 'tpInscProp' in dir(infoEmprParcial): s1020_inclusao_infoemprparcial_dados['tpinscprop'] = infoEmprParcial.tpInscProp.cdata
                    if 'nrInscProp' in dir(infoEmprParcial): s1020_inclusao_infoemprparcial_dados['nrinscprop'] = infoEmprParcial.nrInscProp.cdata
                    insert = create_insert('s1020_inclusao_infoemprparcial', s1020_inclusao_infoemprparcial_dados)
                    resp = executar_sql(insert, True)
                    s1020_inclusao_infoemprparcial_id = resp[0][0]
                    #print s1020_inclusao_infoemprparcial_id
        
    if 'alteracao' in dir(evtTabLotacao.infoLotacao):
        for alteracao in evtTabLotacao.infoLotacao.alteracao:
            s1020_alteracao_dados = {}
            s1020_alteracao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao_id
            
            if 'codLotacao' in dir(alteracao.ideLotacao): s1020_alteracao_dados['codlotacao'] = alteracao.ideLotacao.codLotacao.cdata
            if 'iniValid' in dir(alteracao.ideLotacao): s1020_alteracao_dados['inivalid'] = alteracao.ideLotacao.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideLotacao): s1020_alteracao_dados['fimvalid'] = alteracao.ideLotacao.fimValid.cdata
            if 'tpLotacao' in dir(alteracao.dadosLotacao): s1020_alteracao_dados['tplotacao'] = alteracao.dadosLotacao.tpLotacao.cdata
            if 'tpInsc' in dir(alteracao.dadosLotacao): s1020_alteracao_dados['tpinsc'] = alteracao.dadosLotacao.tpInsc.cdata
            if 'nrInsc' in dir(alteracao.dadosLotacao): s1020_alteracao_dados['nrinsc'] = alteracao.dadosLotacao.nrInsc.cdata
            if 'fpas' in dir(alteracao.dadosLotacao.fpasLotacao): s1020_alteracao_dados['fpas'] = alteracao.dadosLotacao.fpasLotacao.fpas.cdata
            if 'codTercs' in dir(alteracao.dadosLotacao.fpasLotacao): s1020_alteracao_dados['codtercs'] = alteracao.dadosLotacao.fpasLotacao.codTercs.cdata
            if 'codTercsSusp' in dir(alteracao.dadosLotacao.fpasLotacao): s1020_alteracao_dados['codtercssusp'] = alteracao.dadosLotacao.fpasLotacao.codTercsSusp.cdata
            insert = create_insert('s1020_alteracao', s1020_alteracao_dados)
            resp = executar_sql(insert, True)
            s1020_alteracao_id = resp[0][0]
            #print s1020_alteracao_id

            if 'infoProcJudTerceiros' in dir(alteracao.dadosLotacao.fpasLotacao):
                for infoProcJudTerceiros in alteracao.dadosLotacao.fpasLotacao.infoProcJudTerceiros:
                    s1020_alteracao_infoprocjudterceiros_dados = {}
                    s1020_alteracao_infoprocjudterceiros_dados['s1020_alteracao_id'] = s1020_alteracao_id
                    
                    insert = create_insert('s1020_alteracao_infoprocjudterceiros', s1020_alteracao_infoprocjudterceiros_dados)
                    resp = executar_sql(insert, True)
                    s1020_alteracao_infoprocjudterceiros_id = resp[0][0]
                    #print s1020_alteracao_infoprocjudterceiros_id
        
            if 'infoEmprParcial' in dir(alteracao.dadosLotacao):
                for infoEmprParcial in alteracao.dadosLotacao.infoEmprParcial:
                    s1020_alteracao_infoemprparcial_dados = {}
                    s1020_alteracao_infoemprparcial_dados['s1020_alteracao_id'] = s1020_alteracao_id
                    
                    if 'tpInscContrat' in dir(infoEmprParcial): s1020_alteracao_infoemprparcial_dados['tpinsccontrat'] = infoEmprParcial.tpInscContrat.cdata
                    if 'nrInscContrat' in dir(infoEmprParcial): s1020_alteracao_infoemprparcial_dados['nrinsccontrat'] = infoEmprParcial.nrInscContrat.cdata
                    if 'tpInscProp' in dir(infoEmprParcial): s1020_alteracao_infoemprparcial_dados['tpinscprop'] = infoEmprParcial.tpInscProp.cdata
                    if 'nrInscProp' in dir(infoEmprParcial): s1020_alteracao_infoemprparcial_dados['nrinscprop'] = infoEmprParcial.nrInscProp.cdata
                    insert = create_insert('s1020_alteracao_infoemprparcial', s1020_alteracao_infoemprparcial_dados)
                    resp = executar_sql(insert, True)
                    s1020_alteracao_infoemprparcial_id = resp[0][0]
                    #print s1020_alteracao_infoemprparcial_id
        
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1020_alteracao_novavalidade_dados = {}
                    s1020_alteracao_novavalidade_dados['s1020_alteracao_id'] = s1020_alteracao_id
                    
                    if 'iniValid' in dir(novaValidade): s1020_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1020_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1020_alteracao_novavalidade', s1020_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1020_alteracao_novavalidade_id = resp[0][0]
                    #print s1020_alteracao_novavalidade_id
        
    if 'exclusao' in dir(evtTabLotacao.infoLotacao):
        for exclusao in evtTabLotacao.infoLotacao.exclusao:
            s1020_exclusao_dados = {}
            s1020_exclusao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao_id
            
            if 'codLotacao' in dir(exclusao.ideLotacao): s1020_exclusao_dados['codlotacao'] = exclusao.ideLotacao.codLotacao.cdata
            if 'iniValid' in dir(exclusao.ideLotacao): s1020_exclusao_dados['inivalid'] = exclusao.ideLotacao.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideLotacao): s1020_exclusao_dados['fimvalid'] = exclusao.ideLotacao.fimValid.cdata
            insert = create_insert('s1020_exclusao', s1020_exclusao_dados)
            resp = executar_sql(insert, True)
            s1020_exclusao_id = resp[0][0]
            #print s1020_exclusao_id

    from emensageriapro.esocial.views.s1020_evttablotacao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1020_evttablotacao_id, 'default')
    return dados