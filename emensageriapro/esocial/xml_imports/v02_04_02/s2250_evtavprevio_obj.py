#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s2250_evtavprevio_obj(doc):
    s2250_evtavprevio_dados = {}
    s2250_evtavprevio_dados['versao'] = 'v02_04_02'
    s2250_evtavprevio_dados['status'] = 12
    s2250_evtavprevio_dados['identidade'] = doc.eSocial.evtAvPrevio['Id']
    s2250_evtavprevio_dados['processamento_codigo_resposta'] = 1
    evtAvPrevio = doc.eSocial.evtAvPrevio
    
    if 'indRetif' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['indretif'] = evtAvPrevio.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['nrrecibo'] = evtAvPrevio.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['tpamb'] = evtAvPrevio.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['procemi'] = evtAvPrevio.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAvPrevio.ideEvento): s2250_evtavprevio_dados['verproc'] = evtAvPrevio.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAvPrevio.ideEmpregador): s2250_evtavprevio_dados['tpinsc'] = evtAvPrevio.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAvPrevio.ideEmpregador): s2250_evtavprevio_dados['nrinsc'] = evtAvPrevio.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtAvPrevio.ideVinculo): s2250_evtavprevio_dados['cpftrab'] = evtAvPrevio.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtAvPrevio.ideVinculo): s2250_evtavprevio_dados['nistrab'] = evtAvPrevio.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtAvPrevio.ideVinculo): s2250_evtavprevio_dados['matricula'] = evtAvPrevio.ideVinculo.matricula.cdata
    if 'inclusao' in dir(evtAvPrevio.infoAvPrevio): s2250_evtavprevio_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAvPrevio.infoAvPrevio): s2250_evtavprevio_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAvPrevio.infoAvPrevio): s2250_evtavprevio_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2250_evtavprevio', s2250_evtavprevio_dados)
    resp = executar_sql(insert, True)
    s2250_evtavprevio_id = resp[0][0]
    dados = s2250_evtavprevio_dados
    dados['evento'] = 's2250'
    dados['id'] = s2250_evtavprevio_id
    dados['identidade_evento'] = doc.eSocial.evtAvPrevio['Id']
    dados['status'] = 1

    if 'detAvPrevio' in dir(evtAvPrevio.infoAvPrevio):
        for detAvPrevio in evtAvPrevio.infoAvPrevio.detAvPrevio:
            s2250_detavprevio_dados = {}
            s2250_detavprevio_dados['s2250_evtavprevio_id'] = s2250_evtavprevio_id
            
            if 'dtAvPrv' in dir(detAvPrevio): s2250_detavprevio_dados['dtavprv'] = detAvPrevio.dtAvPrv.cdata
            if 'dtPrevDeslig' in dir(detAvPrevio): s2250_detavprevio_dados['dtprevdeslig'] = detAvPrevio.dtPrevDeslig.cdata
            if 'tpAvPrevio' in dir(detAvPrevio): s2250_detavprevio_dados['tpavprevio'] = detAvPrevio.tpAvPrevio.cdata
            if 'observacao' in dir(detAvPrevio): s2250_detavprevio_dados['observacao'] = detAvPrevio.observacao.cdata
            insert = create_insert('s2250_detavprevio', s2250_detavprevio_dados)
            resp = executar_sql(insert, True)
            s2250_detavprevio_id = resp[0][0]
            #print s2250_detavprevio_id

    if 'cancAvPrevio' in dir(evtAvPrevio.infoAvPrevio):
        for cancAvPrevio in evtAvPrevio.infoAvPrevio.cancAvPrevio:
            s2250_cancavprevio_dados = {}
            s2250_cancavprevio_dados['s2250_evtavprevio_id'] = s2250_evtavprevio_id
            
            if 'dtCancAvPrv' in dir(cancAvPrevio): s2250_cancavprevio_dados['dtcancavprv'] = cancAvPrevio.dtCancAvPrv.cdata
            if 'observacao' in dir(cancAvPrevio): s2250_cancavprevio_dados['observacao'] = cancAvPrevio.observacao.cdata
            if 'mtvCancAvPrevio' in dir(cancAvPrevio): s2250_cancavprevio_dados['mtvcancavprevio'] = cancAvPrevio.mtvCancAvPrevio.cdata
            insert = create_insert('s2250_cancavprevio', s2250_cancavprevio_dados)
            resp = executar_sql(insert, True)
            s2250_cancavprevio_id = resp[0][0]
            #print s2250_cancavprevio_id

    return dados