#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s2190_evtadmprelim_obj(doc):
    s2190_evtadmprelim_dados = {}
    s2190_evtadmprelim_dados['versao'] = 'v02_04_02'
    s2190_evtadmprelim_dados['status'] = 12
    s2190_evtadmprelim_dados['identidade'] = doc.eSocial.evtAdmPrelim['Id']
    s2190_evtadmprelim_dados['processamento_codigo_resposta'] = 1
    evtAdmPrelim = doc.eSocial.evtAdmPrelim
    
    if 'tpAmb' in dir(evtAdmPrelim.ideEvento): s2190_evtadmprelim_dados['tpamb'] = evtAdmPrelim.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAdmPrelim.ideEvento): s2190_evtadmprelim_dados['procemi'] = evtAdmPrelim.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAdmPrelim.ideEvento): s2190_evtadmprelim_dados['verproc'] = evtAdmPrelim.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAdmPrelim.ideEmpregador): s2190_evtadmprelim_dados['tpinsc'] = evtAdmPrelim.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAdmPrelim.ideEmpregador): s2190_evtadmprelim_dados['nrinsc'] = evtAdmPrelim.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['cpftrab'] = evtAdmPrelim.infoRegPrelim.cpfTrab.cdata
    if 'dtNascto' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['dtnascto'] = evtAdmPrelim.infoRegPrelim.dtNascto.cdata
    if 'dtAdm' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['dtadm'] = evtAdmPrelim.infoRegPrelim.dtAdm.cdata
    if 'inclusao' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2190_evtadmprelim', s2190_evtadmprelim_dados)
    resp = executar_sql(insert, True)
    s2190_evtadmprelim_id = resp[0][0]
    dados = s2190_evtadmprelim_dados
    dados['evento'] = 's2190'
    dados['id'] = s2190_evtadmprelim_id
    dados['identidade_evento'] = doc.eSocial.evtAdmPrelim['Id']
    dados['status'] = 1

    return dados