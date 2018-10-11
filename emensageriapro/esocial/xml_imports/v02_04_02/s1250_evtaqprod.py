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


def read_s1250_evtaqprod(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s1250_evtaqprod_obj(doc, status)



def read_s1250_evtaqprod_obj(doc):
    s1250_evtaqprod_dados = {}
    s1250_evtaqprod_dados['versao'] = 'v02_04_02'
    s1250_evtaqprod_dados['status'] = status
    s1250_evtaqprod_dados['identidade'] = doc.eSocial.evtAqProd['Id']
    s1250_evtaqprod_dados['processamento_codigo_resposta'] = 1
    evtAqProd = doc.eSocial.evtAqProd
    
    if 'indRetif' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['indretif'] = evtAqProd.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['nrrecibo'] = evtAqProd.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['indapuracao'] = evtAqProd.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['perapur'] = evtAqProd.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['tpamb'] = evtAqProd.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['procemi'] = evtAqProd.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['verproc'] = evtAqProd.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAqProd.ideEmpregador): s1250_evtaqprod_dados['tpinsc'] = evtAqProd.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAqProd.ideEmpregador): s1250_evtaqprod_dados['nrinsc'] = evtAqProd.ideEmpregador.nrInsc.cdata
    if 'tpInscAdq' in dir(evtAqProd.infoAquisProd.ideEstabAdquir): s1250_evtaqprod_dados['tpinscadq'] = evtAqProd.infoAquisProd.ideEstabAdquir.tpInscAdq.cdata
    if 'nrInscAdq' in dir(evtAqProd.infoAquisProd.ideEstabAdquir): s1250_evtaqprod_dados['nrinscadq'] = evtAqProd.infoAquisProd.ideEstabAdquir.nrInscAdq.cdata
    if 'inclusao' in dir(evtAqProd.infoAquisProd): s1250_evtaqprod_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAqProd.infoAquisProd): s1250_evtaqprod_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAqProd.infoAquisProd): s1250_evtaqprod_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1250_evtaqprod', s1250_evtaqprod_dados)
    resp = executar_sql(insert, True)
    s1250_evtaqprod_id = resp[0][0]
    dados = s1250_evtaqprod_dados
    dados['evento'] = 's1250'
    dados['id'] = s1250_evtaqprod_id
    dados['identidade_evento'] = doc.eSocial.evtAqProd['Id']
    dados['status'] = 1

    if 'tpAquis' in dir(evtAqProd.infoAquisProd.ideEstabAdquir):
        for tpAquis in evtAqProd.infoAquisProd.ideEstabAdquir.tpAquis:
            s1250_tpaquis_dados = {}
            s1250_tpaquis_dados['s1250_evtaqprod_id'] = s1250_evtaqprod_id
            
            if 'indAquis' in dir(tpAquis): s1250_tpaquis_dados['indaquis'] = tpAquis.indAquis.cdata
            if 'vlrTotAquis' in dir(tpAquis): s1250_tpaquis_dados['vlrtotaquis'] = tpAquis.vlrTotAquis.cdata
            insert = create_insert('s1250_tpaquis', s1250_tpaquis_dados)
            resp = executar_sql(insert, True)
            s1250_tpaquis_id = resp[0][0]
            #print s1250_tpaquis_id

            if 'ideProdutor' in dir(tpAquis):
                for ideProdutor in tpAquis.ideProdutor:
                    s1250_ideprodutor_dados = {}
                    s1250_ideprodutor_dados['s1250_tpaquis_id'] = s1250_tpaquis_id
                    
                    if 'tpInscProd' in dir(ideProdutor): s1250_ideprodutor_dados['tpinscprod'] = ideProdutor.tpInscProd.cdata
                    if 'nrInscProd' in dir(ideProdutor): s1250_ideprodutor_dados['nrinscprod'] = ideProdutor.nrInscProd.cdata
                    if 'vlrBruto' in dir(ideProdutor): s1250_ideprodutor_dados['vlrbruto'] = ideProdutor.vlrBruto.cdata
                    if 'vrCPDescPR' in dir(ideProdutor): s1250_ideprodutor_dados['vrcpdescpr'] = ideProdutor.vrCPDescPR.cdata
                    if 'vrRatDescPR' in dir(ideProdutor): s1250_ideprodutor_dados['vrratdescpr'] = ideProdutor.vrRatDescPR.cdata
                    if 'vrSenarDesc' in dir(ideProdutor): s1250_ideprodutor_dados['vrsenardesc'] = ideProdutor.vrSenarDesc.cdata
                    insert = create_insert('s1250_ideprodutor', s1250_ideprodutor_dados)
                    resp = executar_sql(insert, True)
                    s1250_ideprodutor_id = resp[0][0]
                    #print s1250_ideprodutor_id
        
    from emensageriapro.esocial.views.s1250_evtaqprod_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1250_evtaqprod_id, 'default')
    return dados