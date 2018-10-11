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


def read_s1207_evtbenprrp(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s1207_evtbenprrp_obj(doc, status)



def read_s1207_evtbenprrp_obj(doc):
    s1207_evtbenprrp_dados = {}
    s1207_evtbenprrp_dados['versao'] = 'v02_04_02'
    s1207_evtbenprrp_dados['status'] = status
    s1207_evtbenprrp_dados['identidade'] = doc.eSocial.evtBenPrRP['Id']
    s1207_evtbenprrp_dados['processamento_codigo_resposta'] = 1
    evtBenPrRP = doc.eSocial.evtBenPrRP
    
    if 'indRetif' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['indretif'] = evtBenPrRP.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['nrrecibo'] = evtBenPrRP.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['indapuracao'] = evtBenPrRP.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['perapur'] = evtBenPrRP.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['tpamb'] = evtBenPrRP.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['procemi'] = evtBenPrRP.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['verproc'] = evtBenPrRP.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtBenPrRP.ideEmpregador): s1207_evtbenprrp_dados['tpinsc'] = evtBenPrRP.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtBenPrRP.ideEmpregador): s1207_evtbenprrp_dados['nrinsc'] = evtBenPrRP.ideEmpregador.nrInsc.cdata
    if 'cpfBenef' in dir(evtBenPrRP.ideBenef): s1207_evtbenprrp_dados['cpfbenef'] = evtBenPrRP.ideBenef.cpfBenef.cdata
    if 'inclusao' in dir(evtBenPrRP.dmDev): s1207_evtbenprrp_dados['operacao'] = 1
    elif 'alteracao' in dir(evtBenPrRP.dmDev): s1207_evtbenprrp_dados['operacao'] = 2
    elif 'exclusao' in dir(evtBenPrRP.dmDev): s1207_evtbenprrp_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1207_evtbenprrp', s1207_evtbenprrp_dados)
    resp = executar_sql(insert, True)
    s1207_evtbenprrp_id = resp[0][0]
    dados = s1207_evtbenprrp_dados
    dados['evento'] = 's1207'
    dados['id'] = s1207_evtbenprrp_id
    dados['identidade_evento'] = doc.eSocial.evtBenPrRP['Id']
    dados['status'] = 1

    if 'procJudTrab' in dir(evtBenPrRP.ideBenef):
        for procJudTrab in evtBenPrRP.ideBenef.procJudTrab:
            s1207_procjudtrab_dados = {}
            s1207_procjudtrab_dados['s1207_evtbenprrp_id'] = s1207_evtbenprrp_id
            
            if 'tpTrib' in dir(procJudTrab): s1207_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            if 'nrProcJud' in dir(procJudTrab): s1207_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            if 'codSusp' in dir(procJudTrab): s1207_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            insert = create_insert('s1207_procjudtrab', s1207_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s1207_procjudtrab_id = resp[0][0]
            #print s1207_procjudtrab_id

    if 'dmDev' in dir(evtBenPrRP):
        for dmDev in evtBenPrRP.dmDev:
            s1207_dmdev_dados = {}
            s1207_dmdev_dados['s1207_evtbenprrp_id'] = s1207_evtbenprrp_id
            
            if 'tpBenef' in dir(dmDev): s1207_dmdev_dados['tpbenef'] = dmDev.tpBenef.cdata
            if 'nrBenefic' in dir(dmDev): s1207_dmdev_dados['nrbenefic'] = dmDev.nrBenefic.cdata
            if 'ideDmDev' in dir(dmDev): s1207_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            insert = create_insert('s1207_dmdev', s1207_dmdev_dados)
            resp = executar_sql(insert, True)
            s1207_dmdev_id = resp[0][0]
            #print s1207_dmdev_id

            if 'itens' in dir(dmDev):
                for itens in dmDev.itens:
                    s1207_itens_dados = {}
                    s1207_itens_dados['s1207_dmdev_id'] = s1207_dmdev_id
                    
                    if 'codRubr' in dir(itens): s1207_itens_dados['codrubr'] = itens.codRubr.cdata
                    if 'ideTabRubr' in dir(itens): s1207_itens_dados['idetabrubr'] = itens.ideTabRubr.cdata
                    if 'vrRubr' in dir(itens): s1207_itens_dados['vrrubr'] = itens.vrRubr.cdata
                    insert = create_insert('s1207_itens', s1207_itens_dados)
                    resp = executar_sql(insert, True)
                    s1207_itens_id = resp[0][0]
                    #print s1207_itens_id
        
            if 'infoPerApur' in dir(dmDev):
                for infoPerApur in dmDev.infoPerApur:
                    s1207_infoperapur_dados = {}
                    s1207_infoperapur_dados['s1207_dmdev_id'] = s1207_dmdev_id
                    
                    insert = create_insert('s1207_infoperapur', s1207_infoperapur_dados)
                    resp = executar_sql(insert, True)
                    s1207_infoperapur_id = resp[0][0]
                    #print s1207_infoperapur_id
        
            if 'infoPerAnt' in dir(dmDev):
                for infoPerAnt in dmDev.infoPerAnt:
                    s1207_infoperant_dados = {}
                    s1207_infoperant_dados['s1207_dmdev_id'] = s1207_dmdev_id
                    
                    insert = create_insert('s1207_infoperant', s1207_infoperant_dados)
                    resp = executar_sql(insert, True)
                    s1207_infoperant_id = resp[0][0]
                    #print s1207_infoperant_id
        
    from emensageriapro.esocial.views.s1207_evtbenprrp_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1207_evtbenprrp_id, 'default')
    return dados