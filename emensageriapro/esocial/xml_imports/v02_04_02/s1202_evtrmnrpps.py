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


def read_s1202_evtrmnrpps(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s1202_evtrmnrpps_obj(doc, status)



def read_s1202_evtrmnrpps_obj(doc):
    s1202_evtrmnrpps_dados = {}
    s1202_evtrmnrpps_dados['versao'] = 'v02_04_02'
    s1202_evtrmnrpps_dados['status'] = status
    s1202_evtrmnrpps_dados['identidade'] = doc.eSocial.evtRmnRPPS['Id']
    s1202_evtrmnrpps_dados['processamento_codigo_resposta'] = 1
    evtRmnRPPS = doc.eSocial.evtRmnRPPS
    
    if 'indRetif' in dir(evtRmnRPPS.ideEvento): s1202_evtrmnrpps_dados['indretif'] = evtRmnRPPS.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtRmnRPPS.ideEvento): s1202_evtrmnrpps_dados['nrrecibo'] = evtRmnRPPS.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtRmnRPPS.ideEvento): s1202_evtrmnrpps_dados['indapuracao'] = evtRmnRPPS.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtRmnRPPS.ideEvento): s1202_evtrmnrpps_dados['perapur'] = evtRmnRPPS.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtRmnRPPS.ideEvento): s1202_evtrmnrpps_dados['tpamb'] = evtRmnRPPS.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtRmnRPPS.ideEvento): s1202_evtrmnrpps_dados['procemi'] = evtRmnRPPS.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtRmnRPPS.ideEvento): s1202_evtrmnrpps_dados['verproc'] = evtRmnRPPS.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtRmnRPPS.ideEmpregador): s1202_evtrmnrpps_dados['tpinsc'] = evtRmnRPPS.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtRmnRPPS.ideEmpregador): s1202_evtrmnrpps_dados['nrinsc'] = evtRmnRPPS.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtRmnRPPS.ideTrabalhador): s1202_evtrmnrpps_dados['cpftrab'] = evtRmnRPPS.ideTrabalhador.cpfTrab.cdata
    if 'nisTrab' in dir(evtRmnRPPS.ideTrabalhador): s1202_evtrmnrpps_dados['nistrab'] = evtRmnRPPS.ideTrabalhador.nisTrab.cdata
    if 'qtdDepFP' in dir(evtRmnRPPS.ideTrabalhador): s1202_evtrmnrpps_dados['qtddepfp'] = evtRmnRPPS.ideTrabalhador.qtdDepFP.cdata
    if 'inclusao' in dir(evtRmnRPPS.dmDev): s1202_evtrmnrpps_dados['operacao'] = 1
    elif 'alteracao' in dir(evtRmnRPPS.dmDev): s1202_evtrmnrpps_dados['operacao'] = 2
    elif 'exclusao' in dir(evtRmnRPPS.dmDev): s1202_evtrmnrpps_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1202_evtrmnrpps', s1202_evtrmnrpps_dados)
    resp = executar_sql(insert, True)
    s1202_evtrmnrpps_id = resp[0][0]
    dados = s1202_evtrmnrpps_dados
    dados['evento'] = 's1202'
    dados['id'] = s1202_evtrmnrpps_id
    dados['identidade_evento'] = doc.eSocial.evtRmnRPPS['Id']
    dados['status'] = 1

    if 'procJudTrab' in dir(evtRmnRPPS.ideTrabalhador):
        for procJudTrab in evtRmnRPPS.ideTrabalhador.procJudTrab:
            s1202_procjudtrab_dados = {}
            s1202_procjudtrab_dados['s1202_evtrmnrpps_id'] = s1202_evtrmnrpps_id
            
            if 'tpTrib' in dir(procJudTrab): s1202_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            if 'nrProcJud' in dir(procJudTrab): s1202_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            if 'codSusp' in dir(procJudTrab): s1202_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            insert = create_insert('s1202_procjudtrab', s1202_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s1202_procjudtrab_id = resp[0][0]
            #print s1202_procjudtrab_id

    if 'dmDev' in dir(evtRmnRPPS):
        for dmDev in evtRmnRPPS.dmDev:
            s1202_dmdev_dados = {}
            s1202_dmdev_dados['s1202_evtrmnrpps_id'] = s1202_evtrmnrpps_id
            
            if 'ideDmDev' in dir(dmDev): s1202_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            if 'codCateg' in dir(dmDev): s1202_dmdev_dados['codcateg'] = dmDev.codCateg.cdata
            insert = create_insert('s1202_dmdev', s1202_dmdev_dados)
            resp = executar_sql(insert, True)
            s1202_dmdev_id = resp[0][0]
            #print s1202_dmdev_id

            if 'infoPerApur' in dir(dmDev):
                for infoPerApur in dmDev.infoPerApur:
                    s1202_infoperapur_dados = {}
                    s1202_infoperapur_dados['s1202_dmdev_id'] = s1202_dmdev_id
                    
                    insert = create_insert('s1202_infoperapur', s1202_infoperapur_dados)
                    resp = executar_sql(insert, True)
                    s1202_infoperapur_id = resp[0][0]
                    #print s1202_infoperapur_id
        
            if 'infoPerAnt' in dir(dmDev):
                for infoPerAnt in dmDev.infoPerAnt:
                    s1202_infoperant_dados = {}
                    s1202_infoperant_dados['s1202_dmdev_id'] = s1202_dmdev_id
                    
                    insert = create_insert('s1202_infoperant', s1202_infoperant_dados)
                    resp = executar_sql(insert, True)
                    s1202_infoperant_id = resp[0][0]
                    #print s1202_infoperant_id
        
    from emensageriapro.esocial.views.s1202_evtrmnrpps_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1202_evtrmnrpps_id, 'default')
    return dados