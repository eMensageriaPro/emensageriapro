#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r9000_evtexclusao_obj(doc):
    r9000_evtexclusao_dados = {}
    r9000_evtexclusao_dados['versao'] = 'v1_03_02'
    r9000_evtexclusao_dados['status'] = 12
    r9000_evtexclusao_dados['identidade'] = doc.Reinf.evtExclusao['id']
    r9000_evtexclusao_dados['processamento_codigo_resposta'] = 1
    evtExclusao = doc.Reinf.evtExclusao
    
    if 'tpAmb' in dir(evtExclusao.ideEvento): r9000_evtexclusao_dados['tpamb'] = evtExclusao.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtExclusao.ideEvento): r9000_evtexclusao_dados['procemi'] = evtExclusao.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtExclusao.ideEvento): r9000_evtexclusao_dados['verproc'] = evtExclusao.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtExclusao.ideContri): r9000_evtexclusao_dados['tpinsc'] = evtExclusao.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtExclusao.ideContri): r9000_evtexclusao_dados['nrinsc'] = evtExclusao.ideContri.nrInsc.cdata
    if 'tpEvento' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['tpevento'] = evtExclusao.infoExclusao.tpEvento.cdata
    if 'nrRecEvt' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['nrrecevt'] = evtExclusao.infoExclusao.nrRecEvt.cdata
    if 'perApur' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['perapur'] = evtExclusao.infoExclusao.perApur.cdata
    if 'inclusao' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['operacao'] = 3
    #print dados
    insert = create_insert('r9000_evtexclusao', r9000_evtexclusao_dados)
    resp = executar_sql(insert, True)
    r9000_evtexclusao_id = resp[0][0]
    dados = r9000_evtexclusao_dados
    dados['evento'] = 'r9000'
    dados['id'] = r9000_evtexclusao_id
    dados['identidade_evento'] = doc.Reinf.evtExclusao['id']
    dados['status'] = 1


    return dados