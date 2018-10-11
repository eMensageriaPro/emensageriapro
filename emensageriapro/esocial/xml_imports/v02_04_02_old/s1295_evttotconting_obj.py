#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s1295_evttotconting_obj(doc):
    s1295_evttotconting_dados = {}
    s1295_evttotconting_dados['versao'] = 'v02_04_02'
    s1295_evttotconting_dados['status'] = 12
    s1295_evttotconting_dados['identidade'] = doc.eSocial.evtTotConting['Id']
    s1295_evttotconting_dados['processamento_codigo_resposta'] = 1
    evtTotConting = doc.eSocial.evtTotConting
    
    if 'indApuracao' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['indapuracao'] = evtTotConting.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['perapur'] = evtTotConting.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['tpamb'] = evtTotConting.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['procemi'] = evtTotConting.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTotConting.ideEvento): s1295_evttotconting_dados['verproc'] = evtTotConting.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTotConting.ideEmpregador): s1295_evttotconting_dados['tpinsc'] = evtTotConting.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTotConting.ideEmpregador): s1295_evttotconting_dados['nrinsc'] = evtTotConting.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTotConting.ideRespInf): s1295_evttotconting_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTotConting.ideRespInf): s1295_evttotconting_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTotConting.ideRespInf): s1295_evttotconting_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1295_evttotconting', s1295_evttotconting_dados)
    resp = executar_sql(insert, True)
    s1295_evttotconting_id = resp[0][0]
    dados = s1295_evttotconting_dados
    dados['evento'] = 's1295'
    dados['id'] = s1295_evttotconting_id
    dados['identidade_evento'] = doc.eSocial.evtTotConting['Id']
    dados['status'] = 1

    if 'ideRespInf' in dir(evtTotConting):
        for ideRespInf in evtTotConting.ideRespInf:
            s1295_iderespinf_dados = {}
            s1295_iderespinf_dados['s1295_evttotconting_id'] = s1295_evttotconting_id
            
            if 'nmResp' in dir(ideRespInf): s1295_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            if 'cpfResp' in dir(ideRespInf): s1295_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            if 'telefone' in dir(ideRespInf): s1295_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            if 'email' in dir(ideRespInf): s1295_iderespinf_dados['email'] = ideRespInf.email.cdata
            insert = create_insert('s1295_iderespinf', s1295_iderespinf_dados)
            resp = executar_sql(insert, True)
            s1295_iderespinf_id = resp[0][0]
            #print s1295_iderespinf_id

    return dados