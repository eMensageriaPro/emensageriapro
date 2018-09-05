#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s1298_evtreabreevper_obj(doc):
    s1298_evtreabreevper_dados = {}
    s1298_evtreabreevper_dados['versao'] = 'v02_04_02'
    s1298_evtreabreevper_dados['status'] = 12
    s1298_evtreabreevper_dados['identidade'] = doc.eSocial.evtReabreEvPer['Id']
    s1298_evtreabreevper_dados['processamento_codigo_resposta'] = 1
    evtReabreEvPer = doc.eSocial.evtReabreEvPer
    
    if 'indApuracao' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['indapuracao'] = evtReabreEvPer.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['perapur'] = evtReabreEvPer.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['tpamb'] = evtReabreEvPer.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['procemi'] = evtReabreEvPer.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['verproc'] = evtReabreEvPer.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['tpinsc'] = evtReabreEvPer.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['nrinsc'] = evtReabreEvPer.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['operacao'] = 1
    elif 'alteracao' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['operacao'] = 2
    elif 'exclusao' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1298_evtreabreevper', s1298_evtreabreevper_dados)
    resp = executar_sql(insert, True)
    s1298_evtreabreevper_id = resp[0][0]
    dados = s1298_evtreabreevper_dados
    dados['evento'] = 's1298'
    dados['id'] = s1298_evtreabreevper_id
    dados['identidade_evento'] = doc.eSocial.evtReabreEvPer['Id']
    dados['status'] = 1

    return dados