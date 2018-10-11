#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s2240_evtexprisco_obj(doc):
    s2240_evtexprisco_dados = {}
    s2240_evtexprisco_dados['versao'] = 'v02_04_02'
    s2240_evtexprisco_dados['status'] = 12
    s2240_evtexprisco_dados['identidade'] = doc.eSocial.evtExpRisco['Id']
    s2240_evtexprisco_dados['processamento_codigo_resposta'] = 1
    evtExpRisco = doc.eSocial.evtExpRisco
    
    if 'indRetif' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['indretif'] = evtExpRisco.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['nrrecibo'] = evtExpRisco.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['tpamb'] = evtExpRisco.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['procemi'] = evtExpRisco.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtExpRisco.ideEvento): s2240_evtexprisco_dados['verproc'] = evtExpRisco.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtExpRisco.ideEmpregador): s2240_evtexprisco_dados['tpinsc'] = evtExpRisco.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtExpRisco.ideEmpregador): s2240_evtexprisco_dados['nrinsc'] = evtExpRisco.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtExpRisco.ideVinculo): s2240_evtexprisco_dados['cpftrab'] = evtExpRisco.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtExpRisco.ideVinculo): s2240_evtexprisco_dados['nistrab'] = evtExpRisco.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtExpRisco.ideVinculo): s2240_evtexprisco_dados['matricula'] = evtExpRisco.ideVinculo.matricula.cdata
    if 'inclusao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['operacao'] = 1
    elif 'alteracao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['operacao'] = 2
    elif 'exclusao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2240_evtexprisco', s2240_evtexprisco_dados)
    resp = executar_sql(insert, True)
    s2240_evtexprisco_id = resp[0][0]
    dados = s2240_evtexprisco_dados
    dados['evento'] = 's2240'
    dados['id'] = s2240_evtexprisco_id
    dados['identidade_evento'] = doc.eSocial.evtExpRisco['Id']
    dados['status'] = 1

    if 'iniExpRisco' in dir(evtExpRisco.infoExpRisco):
        for iniExpRisco in evtExpRisco.infoExpRisco.iniExpRisco:
            s2240_iniexprisco_dados = {}
            s2240_iniexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id
            
            if 'dtIniCondicao' in dir(iniExpRisco): s2240_iniexprisco_dados['dtinicondicao'] = iniExpRisco.dtIniCondicao.cdata
            insert = create_insert('s2240_iniexprisco', s2240_iniexprisco_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_id = resp[0][0]
            #print s2240_iniexprisco_id

            if 'infoAmb' in dir(iniExpRisco):
                for infoAmb in iniExpRisco.infoAmb:
                    s2240_iniexprisco_infoamb_dados = {}
                    s2240_iniexprisco_infoamb_dados['s2240_iniexprisco_id'] = s2240_iniexprisco_id
                    
                    if 'codAmb' in dir(infoAmb): s2240_iniexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    if 'dscAtivDes' in dir(infoAmb): s2240_iniexprisco_infoamb_dados['dscativdes'] = infoAmb.infoAtiv.dscAtivDes.cdata
                    insert = create_insert('s2240_iniexprisco_infoamb', s2240_iniexprisco_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2240_iniexprisco_infoamb_id = resp[0][0]
                    #print s2240_iniexprisco_infoamb_id
        
    if 'altExpRisco' in dir(evtExpRisco.infoExpRisco):
        for altExpRisco in evtExpRisco.infoExpRisco.altExpRisco:
            s2240_altexprisco_dados = {}
            s2240_altexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id
            
            if 'dtAltCondicao' in dir(altExpRisco): s2240_altexprisco_dados['dtaltcondicao'] = altExpRisco.dtAltCondicao.cdata
            insert = create_insert('s2240_altexprisco', s2240_altexprisco_dados)
            resp = executar_sql(insert, True)
            s2240_altexprisco_id = resp[0][0]
            #print s2240_altexprisco_id

            if 'infoAmb' in dir(altExpRisco):
                for infoAmb in altExpRisco.infoAmb:
                    s2240_altexprisco_infoamb_dados = {}
                    s2240_altexprisco_infoamb_dados['s2240_altexprisco_id'] = s2240_altexprisco_id
                    
                    if 'codAmb' in dir(infoAmb): s2240_altexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    if 'dscAtivDes' in dir(infoAmb): s2240_altexprisco_infoamb_dados['dscativdes'] = infoAmb.infoAtiv.dscAtivDes.cdata
                    insert = create_insert('s2240_altexprisco_infoamb', s2240_altexprisco_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2240_altexprisco_infoamb_id = resp[0][0]
                    #print s2240_altexprisco_infoamb_id
        
    if 'fimExpRisco' in dir(evtExpRisco.infoExpRisco):
        for fimExpRisco in evtExpRisco.infoExpRisco.fimExpRisco:
            s2240_fimexprisco_dados = {}
            s2240_fimexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id
            
            if 'dtFimCondicao' in dir(fimExpRisco): s2240_fimexprisco_dados['dtfimcondicao'] = fimExpRisco.dtFimCondicao.cdata
            insert = create_insert('s2240_fimexprisco', s2240_fimexprisco_dados)
            resp = executar_sql(insert, True)
            s2240_fimexprisco_id = resp[0][0]
            #print s2240_fimexprisco_id

            if 'infoAmb' in dir(fimExpRisco):
                for infoAmb in fimExpRisco.infoAmb:
                    s2240_fimexprisco_infoamb_dados = {}
                    s2240_fimexprisco_infoamb_dados['s2240_fimexprisco_id'] = s2240_fimexprisco_id
                    
                    if 'codAmb' in dir(infoAmb): s2240_fimexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    insert = create_insert('s2240_fimexprisco_infoamb', s2240_fimexprisco_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2240_fimexprisco_infoamb_id = resp[0][0]
                    #print s2240_fimexprisco_infoamb_id
        
    if 'respReg' in dir(evtExpRisco.infoExpRisco):
        for respReg in evtExpRisco.infoExpRisco.respReg:
            s2240_fimexprisco_respreg_dados = {}
            s2240_fimexprisco_respreg_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id
            
            if 'dtIni' in dir(respReg): s2240_fimexprisco_respreg_dados['dtini'] = respReg.dtIni.cdata
            if 'dtFim' in dir(respReg): s2240_fimexprisco_respreg_dados['dtfim'] = respReg.dtFim.cdata
            if 'nisResp' in dir(respReg): s2240_fimexprisco_respreg_dados['nisresp'] = respReg.nisResp.cdata
            if 'nrOc' in dir(respReg): s2240_fimexprisco_respreg_dados['nroc'] = respReg.nrOc.cdata
            if 'ufOC' in dir(respReg): s2240_fimexprisco_respreg_dados['ufoc'] = respReg.ufOC.cdata
            insert = create_insert('s2240_fimexprisco_respreg', s2240_fimexprisco_respreg_dados)
            resp = executar_sql(insert, True)
            s2240_fimexprisco_respreg_id = resp[0][0]
            #print s2240_fimexprisco_respreg_id

    return dados