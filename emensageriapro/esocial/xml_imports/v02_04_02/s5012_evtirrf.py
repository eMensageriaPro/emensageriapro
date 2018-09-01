#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s5012_evtirrf(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s5012_evtirrf_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s5012_evtirrf_dados['status'] = 1
    else:
        s5012_evtirrf_dados['status'] = 0
    s5012_evtirrf_dados['versao'] = xmlns[len(xmlns)-1]
    s5012_evtirrf_dados['identidade'] = doc.eSocial.evtIrrf['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s5012_evtirrf_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
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
    dados['evento'] = 's5012'
    dados['identidade'] = s5012_evtirrf_id
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

    from emensageriapro.esocial.views.s5012_evtirrf_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s5012_evtirrf_id, 'default')
    return dados