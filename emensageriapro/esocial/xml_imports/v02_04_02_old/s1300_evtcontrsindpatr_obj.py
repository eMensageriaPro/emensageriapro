#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s1300_evtcontrsindpatr_obj(doc):
    s1300_evtcontrsindpatr_dados = {}
    s1300_evtcontrsindpatr_dados['versao'] = 'v02_04_02'
    s1300_evtcontrsindpatr_dados['status'] = 12
    s1300_evtcontrsindpatr_dados['identidade'] = doc.eSocial.evtContrSindPatr['Id']
    s1300_evtcontrsindpatr_dados['processamento_codigo_resposta'] = 1
    evtContrSindPatr = doc.eSocial.evtContrSindPatr
    
    if 'indRetif' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['indretif'] = evtContrSindPatr.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['nrrecibo'] = evtContrSindPatr.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['indapuracao'] = evtContrSindPatr.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['perapur'] = evtContrSindPatr.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['tpamb'] = evtContrSindPatr.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['procemi'] = evtContrSindPatr.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtContrSindPatr.ideEvento): s1300_evtcontrsindpatr_dados['verproc'] = evtContrSindPatr.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtContrSindPatr.ideEmpregador): s1300_evtcontrsindpatr_dados['tpinsc'] = evtContrSindPatr.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtContrSindPatr.ideEmpregador): s1300_evtcontrsindpatr_dados['nrinsc'] = evtContrSindPatr.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtContrSindPatr.contribSind): s1300_evtcontrsindpatr_dados['operacao'] = 1
    elif 'alteracao' in dir(evtContrSindPatr.contribSind): s1300_evtcontrsindpatr_dados['operacao'] = 2
    elif 'exclusao' in dir(evtContrSindPatr.contribSind): s1300_evtcontrsindpatr_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1300_evtcontrsindpatr', s1300_evtcontrsindpatr_dados)
    resp = executar_sql(insert, True)
    s1300_evtcontrsindpatr_id = resp[0][0]
    dados = s1300_evtcontrsindpatr_dados
    dados['evento'] = 's1300'
    dados['id'] = s1300_evtcontrsindpatr_id
    dados['identidade_evento'] = doc.eSocial.evtContrSindPatr['Id']
    dados['status'] = 1

    if 'contribSind' in dir(evtContrSindPatr):
        for contribSind in evtContrSindPatr.contribSind:
            s1300_contribsind_dados = {}
            s1300_contribsind_dados['s1300_evtcontrsindpatr_id'] = s1300_evtcontrsindpatr_id
            
            if 'cnpjSindic' in dir(contribSind): s1300_contribsind_dados['cnpjsindic'] = contribSind.cnpjSindic.cdata
            if 'tpContribSind' in dir(contribSind): s1300_contribsind_dados['tpcontribsind'] = contribSind.tpContribSind.cdata
            if 'vlrContribSind' in dir(contribSind): s1300_contribsind_dados['vlrcontribsind'] = contribSind.vlrContribSind.cdata
            insert = create_insert('s1300_contribsind', s1300_contribsind_dados)
            resp = executar_sql(insert, True)
            s1300_contribsind_id = resp[0][0]
            #print s1300_contribsind_id

    return dados