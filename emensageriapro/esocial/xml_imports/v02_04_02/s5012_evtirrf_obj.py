#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s5012_evtirrf_obj(doc):
    s5012_evtirrf_dados = {}
    s5012_evtirrf_dados['versao'] = 'v02_04_02'
    s5012_evtirrf_dados['status'] = 12
    s5012_evtirrf_dados['identidade'] = doc.eSocial.evtIrrf['Id']
    s5012_evtirrf_dados['processamento_codigo_resposta'] = 1
    evtIrrf = doc.eSocial.evtIrrf
    
    if 'perApur' in dir(evtIrrf.ideEvento): s5012_evtirrf_dados['perapur'] = evtIrrf.ideEvento.perApur.cdata
    if 'tpInsc' in dir(evtIrrf.ideEmpregador): s5012_evtirrf_dados['tpinsc'] = evtIrrf.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtIrrf.ideEmpregador): s5012_evtirrf_dados['nrinsc'] = evtIrrf.ideEmpregador.nrInsc.cdata
    if 'nrRecArqBase' in dir(evtIrrf.infoIRRF): s5012_evtirrf_dados['nrrecarqbase'] = evtIrrf.infoIRRF.nrRecArqBase.cdata
    if 'indExistInfo' in dir(evtIrrf.infoIRRF): s5012_evtirrf_dados['indexistinfo'] = evtIrrf.infoIRRF.indExistInfo.cdata
    if 'inclusao' in dir(evtIrrf.infoIRRF): s5012_evtirrf_dados['operacao'] = 1
    elif 'alteracao' in dir(evtIrrf.infoIRRF): s5012_evtirrf_dados['operacao'] = 2
    elif 'exclusao' in dir(evtIrrf.infoIRRF): s5012_evtirrf_dados['operacao'] = 3
    #print dados
    insert = create_insert('s5012_evtirrf', s5012_evtirrf_dados)
    resp = executar_sql(insert, True)
    s5012_evtirrf_id = resp[0][0]
    dados = s5012_evtirrf_dados
    dados['evento'] = 's5012'
    dados['id'] = s5012_evtirrf_id
    dados['identidade_evento'] = doc.eSocial.evtIrrf['Id']
    dados['status'] = 1

    if 'infoCRContrib' in dir(evtIrrf.infoIRRF):
        for infoCRContrib in evtIrrf.infoIRRF.infoCRContrib:
            s5012_infocrcontrib_dados = {}
            s5012_infocrcontrib_dados['s5012_evtirrf_id'] = s5012_evtirrf_id
            
            if 'tpCR' in dir(infoCRContrib): s5012_infocrcontrib_dados['tpcr'] = infoCRContrib.tpCR.cdata
            if 'vrCR' in dir(infoCRContrib): s5012_infocrcontrib_dados['vrcr'] = infoCRContrib.vrCR.cdata
            insert = create_insert('s5012_infocrcontrib', s5012_infocrcontrib_dados)
            resp = executar_sql(insert, True)
            s5012_infocrcontrib_id = resp[0][0]
            #print s5012_infocrcontrib_id

    return dados