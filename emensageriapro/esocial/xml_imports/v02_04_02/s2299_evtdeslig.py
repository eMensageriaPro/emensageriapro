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


def read_s2299_evtdeslig(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s2299_evtdeslig_obj(doc, status)



def read_s2299_evtdeslig_obj(doc):
    s2299_evtdeslig_dados = {}
    s2299_evtdeslig_dados['versao'] = 'v02_04_02'
    s2299_evtdeslig_dados['status'] = status
    s2299_evtdeslig_dados['identidade'] = doc.eSocial.evtDeslig['Id']
    s2299_evtdeslig_dados['processamento_codigo_resposta'] = 1
    evtDeslig = doc.eSocial.evtDeslig
    
    if 'indRetif' in dir(evtDeslig.ideEvento): s2299_evtdeslig_dados['indretif'] = evtDeslig.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtDeslig.ideEvento): s2299_evtdeslig_dados['nrrecibo'] = evtDeslig.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtDeslig.ideEvento): s2299_evtdeslig_dados['tpamb'] = evtDeslig.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtDeslig.ideEvento): s2299_evtdeslig_dados['procemi'] = evtDeslig.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtDeslig.ideEvento): s2299_evtdeslig_dados['verproc'] = evtDeslig.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtDeslig.ideEmpregador): s2299_evtdeslig_dados['tpinsc'] = evtDeslig.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtDeslig.ideEmpregador): s2299_evtdeslig_dados['nrinsc'] = evtDeslig.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtDeslig.ideVinculo): s2299_evtdeslig_dados['cpftrab'] = evtDeslig.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtDeslig.ideVinculo): s2299_evtdeslig_dados['nistrab'] = evtDeslig.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtDeslig.ideVinculo): s2299_evtdeslig_dados['matricula'] = evtDeslig.ideVinculo.matricula.cdata
    if 'mtvDeslig' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['mtvdeslig'] = evtDeslig.infoDeslig.mtvDeslig.cdata
    if 'dtDeslig' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['dtdeslig'] = evtDeslig.infoDeslig.dtDeslig.cdata
    if 'indPagtoAPI' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['indpagtoapi'] = evtDeslig.infoDeslig.indPagtoAPI.cdata
    if 'dtProjFimAPI' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['dtprojfimapi'] = evtDeslig.infoDeslig.dtProjFimAPI.cdata
    if 'pensAlim' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['pensalim'] = evtDeslig.infoDeslig.pensAlim.cdata
    if 'percAliment' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['percaliment'] = evtDeslig.infoDeslig.percAliment.cdata
    if 'vrAlim' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['vralim'] = evtDeslig.infoDeslig.vrAlim.cdata
    if 'nrCertObito' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['nrcertobito'] = evtDeslig.infoDeslig.nrCertObito.cdata
    if 'nrProcTrab' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['nrproctrab'] = evtDeslig.infoDeslig.nrProcTrab.cdata
    if 'indCumprParc' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['indcumprparc'] = evtDeslig.infoDeslig.indCumprParc.cdata
    if 'qtdDiasInterm' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['qtddiasinterm'] = evtDeslig.infoDeslig.qtdDiasInterm.cdata
    if 'inclusao' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['operacao'] = 1
    elif 'alteracao' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['operacao'] = 2
    elif 'exclusao' in dir(evtDeslig.infoDeslig): s2299_evtdeslig_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2299_evtdeslig', s2299_evtdeslig_dados)
    resp = executar_sql(insert, True)
    s2299_evtdeslig_id = resp[0][0]
    dados = s2299_evtdeslig_dados
    dados['evento'] = 's2299'
    dados['id'] = s2299_evtdeslig_id
    dados['identidade_evento'] = doc.eSocial.evtDeslig['Id']
    dados['status'] = 1

    if 'observacoes' in dir(evtDeslig.infoDeslig):
        for observacoes in evtDeslig.infoDeslig.observacoes:
            s2299_observacoes_dados = {}
            s2299_observacoes_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id
            
            if 'observacao' in dir(observacoes): s2299_observacoes_dados['observacao'] = observacoes.observacao.cdata
            insert = create_insert('s2299_observacoes', s2299_observacoes_dados)
            resp = executar_sql(insert, True)
            s2299_observacoes_id = resp[0][0]
            #print s2299_observacoes_id

    if 'sucessaoVinc' in dir(evtDeslig.infoDeslig):
        for sucessaoVinc in evtDeslig.infoDeslig.sucessaoVinc:
            s2299_sucessaovinc_dados = {}
            s2299_sucessaovinc_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id
            
            if 'cnpjSucessora' in dir(sucessaoVinc): s2299_sucessaovinc_dados['cnpjsucessora'] = sucessaoVinc.cnpjSucessora.cdata
            insert = create_insert('s2299_sucessaovinc', s2299_sucessaovinc_dados)
            resp = executar_sql(insert, True)
            s2299_sucessaovinc_id = resp[0][0]
            #print s2299_sucessaovinc_id

    if 'transfTit' in dir(evtDeslig.infoDeslig):
        for transfTit in evtDeslig.infoDeslig.transfTit:
            s2299_transftit_dados = {}
            s2299_transftit_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id
            
            if 'cpfSubstituto' in dir(transfTit): s2299_transftit_dados['cpfsubstituto'] = transfTit.cpfSubstituto.cdata
            if 'dtNascto' in dir(transfTit): s2299_transftit_dados['dtnascto'] = transfTit.dtNascto.cdata
            insert = create_insert('s2299_transftit', s2299_transftit_dados)
            resp = executar_sql(insert, True)
            s2299_transftit_id = resp[0][0]
            #print s2299_transftit_id

    if 'verbasResc' in dir(evtDeslig.infoDeslig):
        for verbasResc in evtDeslig.infoDeslig.verbasResc:
            s2299_verbasresc_dados = {}
            s2299_verbasresc_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id
            
            insert = create_insert('s2299_verbasresc', s2299_verbasresc_dados)
            resp = executar_sql(insert, True)
            s2299_verbasresc_id = resp[0][0]
            #print s2299_verbasresc_id

            if 'dmDev' in dir(verbasResc):
                for dmDev in verbasResc.dmDev:
                    s2299_dmdev_dados = {}
                    s2299_dmdev_dados['s2299_verbasresc_id'] = s2299_verbasresc_id
                    
                    if 'ideDmDev' in dir(dmDev): s2299_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
                    insert = create_insert('s2299_dmdev', s2299_dmdev_dados)
                    resp = executar_sql(insert, True)
                    s2299_dmdev_id = resp[0][0]
                    #print s2299_dmdev_id
        
            if 'procJudTrab' in dir(verbasResc):
                for procJudTrab in verbasResc.procJudTrab:
                    s2299_infotrabinterm_procjudtrab_dados = {}
                    s2299_infotrabinterm_procjudtrab_dados['s2299_verbasresc_id'] = s2299_verbasresc_id
                    
                    if 'tpTrib' in dir(procJudTrab): s2299_infotrabinterm_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
                    if 'nrProcJud' in dir(procJudTrab): s2299_infotrabinterm_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
                    if 'codSusp' in dir(procJudTrab): s2299_infotrabinterm_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
                    insert = create_insert('s2299_infotrabinterm_procjudtrab', s2299_infotrabinterm_procjudtrab_dados)
                    resp = executar_sql(insert, True)
                    s2299_infotrabinterm_procjudtrab_id = resp[0][0]
                    #print s2299_infotrabinterm_procjudtrab_id
        
            if 'infoMV' in dir(verbasResc):
                for infoMV in verbasResc.infoMV:
                    s2299_infotrabinterm_infomv_dados = {}
                    s2299_infotrabinterm_infomv_dados['s2299_verbasresc_id'] = s2299_verbasresc_id
                    
                    if 'indMV' in dir(infoMV): s2299_infotrabinterm_infomv_dados['indmv'] = infoMV.indMV.cdata
                    insert = create_insert('s2299_infotrabinterm_infomv', s2299_infotrabinterm_infomv_dados)
                    resp = executar_sql(insert, True)
                    s2299_infotrabinterm_infomv_id = resp[0][0]
                    #print s2299_infotrabinterm_infomv_id
        
            if 'procCS' in dir(verbasResc):
                for procCS in verbasResc.procCS:
                    s2299_infotrabinterm_proccs_dados = {}
                    s2299_infotrabinterm_proccs_dados['s2299_verbasresc_id'] = s2299_verbasresc_id
                    
                    if 'nrProcJud' in dir(procCS): s2299_infotrabinterm_proccs_dados['nrprocjud'] = procCS.nrProcJud.cdata
                    insert = create_insert('s2299_infotrabinterm_proccs', s2299_infotrabinterm_proccs_dados)
                    resp = executar_sql(insert, True)
                    s2299_infotrabinterm_proccs_id = resp[0][0]
                    #print s2299_infotrabinterm_proccs_id
        
    if 'quarentena' in dir(evtDeslig.infoDeslig):
        for quarentena in evtDeslig.infoDeslig.quarentena:
            s2299_infotrabinterm_quarentena_dados = {}
            s2299_infotrabinterm_quarentena_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id
            
            if 'dtFimQuar' in dir(quarentena): s2299_infotrabinterm_quarentena_dados['dtfimquar'] = quarentena.dtFimQuar.cdata
            insert = create_insert('s2299_infotrabinterm_quarentena', s2299_infotrabinterm_quarentena_dados)
            resp = executar_sql(insert, True)
            s2299_infotrabinterm_quarentena_id = resp[0][0]
            #print s2299_infotrabinterm_quarentena_id

    if 'consigFGTS' in dir(evtDeslig.infoDeslig):
        for consigFGTS in evtDeslig.infoDeslig.consigFGTS:
            s2299_infotrabinterm_consigfgts_dados = {}
            s2299_infotrabinterm_consigfgts_dados['s2299_evtdeslig_id'] = s2299_evtdeslig_id
            
            if 'insConsig' in dir(consigFGTS): s2299_infotrabinterm_consigfgts_dados['insconsig'] = consigFGTS.insConsig.cdata
            if 'nrContr' in dir(consigFGTS): s2299_infotrabinterm_consigfgts_dados['nrcontr'] = consigFGTS.nrContr.cdata
            insert = create_insert('s2299_infotrabinterm_consigfgts', s2299_infotrabinterm_consigfgts_dados)
            resp = executar_sql(insert, True)
            s2299_infotrabinterm_consigfgts_id = resp[0][0]
            #print s2299_infotrabinterm_consigfgts_id

    from emensageriapro.esocial.views.s2299_evtdeslig_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2299_evtdeslig_id, 'default')
    return dados