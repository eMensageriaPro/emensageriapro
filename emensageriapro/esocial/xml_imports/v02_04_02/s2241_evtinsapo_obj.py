#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s2241_evtinsapo_obj(doc):
    s2241_evtinsapo_dados = {}
    s2241_evtinsapo_dados['versao'] = 'v02_04_02'
    s2241_evtinsapo_dados['status'] = 12
    s2241_evtinsapo_dados['identidade'] = doc.eSocial.evtInsApo['Id']
    s2241_evtinsapo_dados['processamento_codigo_resposta'] = 1
    evtInsApo = doc.eSocial.evtInsApo
    
    if 'indRetif' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['indretif'] = evtInsApo.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['nrrecibo'] = evtInsApo.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['tpamb'] = evtInsApo.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['procemi'] = evtInsApo.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtInsApo.ideEvento): s2241_evtinsapo_dados['verproc'] = evtInsApo.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtInsApo.ideEmpregador): s2241_evtinsapo_dados['tpinsc'] = evtInsApo.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtInsApo.ideEmpregador): s2241_evtinsapo_dados['nrinsc'] = evtInsApo.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtInsApo.ideVinculo): s2241_evtinsapo_dados['cpftrab'] = evtInsApo.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtInsApo.ideVinculo): s2241_evtinsapo_dados['nistrab'] = evtInsApo.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtInsApo.ideVinculo): s2241_evtinsapo_dados['matricula'] = evtInsApo.ideVinculo.matricula.cdata
    if 'inclusao' in dir(evtInsApo.aposentEsp): s2241_evtinsapo_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInsApo.aposentEsp): s2241_evtinsapo_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInsApo.aposentEsp): s2241_evtinsapo_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2241_evtinsapo', s2241_evtinsapo_dados)
    resp = executar_sql(insert, True)
    s2241_evtinsapo_id = resp[0][0]
    dados = s2241_evtinsapo_dados
    dados['evento'] = 's2241'
    dados['id'] = s2241_evtinsapo_id
    dados['identidade_evento'] = doc.eSocial.evtInsApo['Id']
    dados['status'] = 1

    if 'insalPeric' in dir(evtInsApo):
        for insalPeric in evtInsApo.insalPeric:
            s2241_insalperic_dados = {}
            s2241_insalperic_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id
            
            insert = create_insert('s2241_insalperic', s2241_insalperic_dados)
            resp = executar_sql(insert, True)
            s2241_insalperic_id = resp[0][0]
            #print s2241_insalperic_id

            if 'iniInsalPeric' in dir(insalPeric):
                for iniInsalPeric in insalPeric.iniInsalPeric:
                    s2241_iniinsalperic_dados = {}
                    s2241_iniinsalperic_dados['s2241_insalperic_id'] = s2241_insalperic_id
                    
                    if 'dtIniCondicao' in dir(iniInsalPeric): s2241_iniinsalperic_dados['dtinicondicao'] = iniInsalPeric.dtIniCondicao.cdata
                    insert = create_insert('s2241_iniinsalperic', s2241_iniinsalperic_dados)
                    resp = executar_sql(insert, True)
                    s2241_iniinsalperic_id = resp[0][0]
                    #print s2241_iniinsalperic_id
        
            if 'altInsalPeric' in dir(insalPeric):
                for altInsalPeric in insalPeric.altInsalPeric:
                    s2241_altinsalperic_dados = {}
                    s2241_altinsalperic_dados['s2241_insalperic_id'] = s2241_insalperic_id
                    
                    if 'dtAltCondicao' in dir(altInsalPeric): s2241_altinsalperic_dados['dtaltcondicao'] = altInsalPeric.dtAltCondicao.cdata
                    insert = create_insert('s2241_altinsalperic', s2241_altinsalperic_dados)
                    resp = executar_sql(insert, True)
                    s2241_altinsalperic_id = resp[0][0]
                    #print s2241_altinsalperic_id
        
            if 'fimInsalPeric' in dir(insalPeric):
                for fimInsalPeric in insalPeric.fimInsalPeric:
                    s2241_fiminsalperic_dados = {}
                    s2241_fiminsalperic_dados['s2241_insalperic_id'] = s2241_insalperic_id
                    
                    if 'dtFimCondicao' in dir(fimInsalPeric): s2241_fiminsalperic_dados['dtfimcondicao'] = fimInsalPeric.dtFimCondicao.cdata
                    insert = create_insert('s2241_fiminsalperic', s2241_fiminsalperic_dados)
                    resp = executar_sql(insert, True)
                    s2241_fiminsalperic_id = resp[0][0]
                    #print s2241_fiminsalperic_id
        
    if 'aposentEsp' in dir(evtInsApo):
        for aposentEsp in evtInsApo.aposentEsp:
            s2241_aposentesp_dados = {}
            s2241_aposentesp_dados['s2241_evtinsapo_id'] = s2241_evtinsapo_id
            
            insert = create_insert('s2241_aposentesp', s2241_aposentesp_dados)
            resp = executar_sql(insert, True)
            s2241_aposentesp_id = resp[0][0]
            #print s2241_aposentesp_id

            if 'iniAposentEsp' in dir(aposentEsp):
                for iniAposentEsp in aposentEsp.iniAposentEsp:
                    s2241_iniaposentesp_dados = {}
                    s2241_iniaposentesp_dados['s2241_aposentesp_id'] = s2241_aposentesp_id
                    
                    if 'dtIniCondicao' in dir(iniAposentEsp): s2241_iniaposentesp_dados['dtinicondicao'] = iniAposentEsp.dtIniCondicao.cdata
                    insert = create_insert('s2241_iniaposentesp', s2241_iniaposentesp_dados)
                    resp = executar_sql(insert, True)
                    s2241_iniaposentesp_id = resp[0][0]
                    #print s2241_iniaposentesp_id
        
            if 'altAposentEsp' in dir(aposentEsp):
                for altAposentEsp in aposentEsp.altAposentEsp:
                    s2241_altaposentesp_dados = {}
                    s2241_altaposentesp_dados['s2241_aposentesp_id'] = s2241_aposentesp_id
                    
                    if 'dtAltCondicao' in dir(altAposentEsp): s2241_altaposentesp_dados['dtaltcondicao'] = altAposentEsp.dtAltCondicao.cdata
                    insert = create_insert('s2241_altaposentesp', s2241_altaposentesp_dados)
                    resp = executar_sql(insert, True)
                    s2241_altaposentesp_id = resp[0][0]
                    #print s2241_altaposentesp_id
        
            if 'fimAposentEsp' in dir(aposentEsp):
                for fimAposentEsp in aposentEsp.fimAposentEsp:
                    s2241_fimaposentesp_dados = {}
                    s2241_fimaposentesp_dados['s2241_aposentesp_id'] = s2241_aposentesp_id
                    
                    if 'dtFimCondicao' in dir(fimAposentEsp): s2241_fimaposentesp_dados['dtfimcondicao'] = fimAposentEsp.dtFimCondicao.cdata
                    insert = create_insert('s2241_fimaposentesp', s2241_fimaposentesp_dados)
                    resp = executar_sql(insert, True)
                    s2241_fimaposentesp_id = resp[0][0]
                    #print s2241_fimaposentesp_id
        
    return dados