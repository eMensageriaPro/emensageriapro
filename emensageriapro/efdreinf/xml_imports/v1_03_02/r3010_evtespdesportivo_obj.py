#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r3010_evtespdesportivo_obj(doc):
    r3010_evtespdesportivo_dados = {}
    r3010_evtespdesportivo_dados['versao'] = 'v1_03_02'
    r3010_evtespdesportivo_dados['status'] = 12
    r3010_evtespdesportivo_dados['identidade'] = doc.Reinf.evtEspDesportivo['id']
    r3010_evtespdesportivo_dados['processamento_codigo_resposta'] = 1
    evtEspDesportivo = doc.Reinf.evtEspDesportivo
    
    if 'indRetif' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['indretif'] = evtEspDesportivo.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['nrrecibo'] = evtEspDesportivo.ideEvento.nrRecibo.cdata
    if 'dtApuracao' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['dtapuracao'] = evtEspDesportivo.ideEvento.dtApuracao.cdata
    if 'tpAmb' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['tpamb'] = evtEspDesportivo.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['procemi'] = evtEspDesportivo.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtEspDesportivo.ideEvento): r3010_evtespdesportivo_dados['verproc'] = evtEspDesportivo.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['tpinsc'] = evtEspDesportivo.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['nrinsc'] = evtEspDesportivo.ideContri.nrInsc.cdata
    if 'inclusao' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['operacao'] = 1
    elif 'alteracao' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['operacao'] = 2
    elif 'exclusao' in dir(evtEspDesportivo.ideContri): r3010_evtespdesportivo_dados['operacao'] = 3
    #print dados
    insert = create_insert('r3010_evtespdesportivo', r3010_evtespdesportivo_dados)
    resp = executar_sql(insert, True)
    r3010_evtespdesportivo_id = resp[0][0]
    dados = r3010_evtespdesportivo_dados
    dados['evento'] = 'r3010'
    dados['id'] = r3010_evtespdesportivo_id
    dados['identidade_evento'] = doc.Reinf.evtEspDesportivo['id']
    dados['status'] = 1


    if 'ideEstab' in dir(evtEspDesportivo.ideContri):
        for ideEstab in evtEspDesportivo.ideContri.ideEstab:
            r3010_ideestab_dados = {}
            r3010_ideestab_dados['r3010_evtespdesportivo_id'] = r3010_evtespdesportivo_id
            
            if 'tpInscEstab' in dir(ideEstab): r3010_ideestab_dados['tpinscestab'] = ideEstab.tpInscEstab.cdata
            if 'nrInscEstab' in dir(ideEstab): r3010_ideestab_dados['nrinscestab'] = ideEstab.nrInscEstab.cdata
            if 'vlrReceitaTotal' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrreceitatotal'] = ideEstab.receitaTotal.vlrReceitaTotal.cdata
            if 'vlrCP' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrcp'] = ideEstab.receitaTotal.vlrCP.cdata
            if 'vlrCPSuspTotal' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrcpsusptotal'] = ideEstab.receitaTotal.vlrCPSuspTotal.cdata
            if 'vlrReceitaClubes' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrreceitaclubes'] = ideEstab.receitaTotal.vlrReceitaClubes.cdata
            if 'vlrRetParc' in dir(ideEstab.receitaTotal): r3010_ideestab_dados['vlrretparc'] = ideEstab.receitaTotal.vlrRetParc.cdata
            insert = create_insert('r3010_ideestab', r3010_ideestab_dados)
            resp = executar_sql(insert, True)
            r3010_ideestab_id = resp[0][0]
            #print r3010_ideestab_id

            if 'boletim' in dir(ideEstab):
                for boletim in ideEstab.boletim:
                    r3010_boletim_dados = {}
                    r3010_boletim_dados['r3010_ideestab_id'] = r3010_ideestab_id
                    
                    if 'nrBoletim' in dir(boletim): r3010_boletim_dados['nrboletim'] = boletim.nrBoletim.cdata
                    if 'tpCompeticao' in dir(boletim): r3010_boletim_dados['tpcompeticao'] = boletim.tpCompeticao.cdata
                    if 'categEvento' in dir(boletim): r3010_boletim_dados['categevento'] = boletim.categEvento.cdata
                    if 'modDesportiva' in dir(boletim): r3010_boletim_dados['moddesportiva'] = boletim.modDesportiva.cdata
                    if 'nomeCompeticao' in dir(boletim): r3010_boletim_dados['nomecompeticao'] = boletim.nomeCompeticao.cdata
                    if 'cnpjMandante' in dir(boletim): r3010_boletim_dados['cnpjmandante'] = boletim.cnpjMandante.cdata
                    if 'cnpjVisitante' in dir(boletim): r3010_boletim_dados['cnpjvisitante'] = boletim.cnpjVisitante.cdata
                    if 'nomeVisitante' in dir(boletim): r3010_boletim_dados['nomevisitante'] = boletim.nomeVisitante.cdata
                    if 'pracaDesportiva' in dir(boletim): r3010_boletim_dados['pracadesportiva'] = boletim.pracaDesportiva.cdata
                    if 'codMunic' in dir(boletim): r3010_boletim_dados['codmunic'] = boletim.codMunic.cdata
                    if 'uf' in dir(boletim): r3010_boletim_dados['uf'] = boletim.uf.cdata
                    if 'qtdePagantes' in dir(boletim): r3010_boletim_dados['qtdepagantes'] = boletim.qtdePagantes.cdata
                    if 'qtdeNaoPagantes' in dir(boletim): r3010_boletim_dados['qtdenaopagantes'] = boletim.qtdeNaoPagantes.cdata
                    insert = create_insert('r3010_boletim', r3010_boletim_dados)
                    resp = executar_sql(insert, True)
                    r3010_boletim_id = resp[0][0]
                    #print r3010_boletim_id
        
            if 'infoProc' in dir(ideEstab.receitaTotal):
                for infoProc in ideEstab.receitaTotal.infoProc:
                    r3010_infoproc_dados = {}
                    r3010_infoproc_dados['r3010_ideestab_id'] = r3010_ideestab_id
                    
                    if 'tpProc' in dir(infoProc): r3010_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    if 'nrProc' in dir(infoProc): r3010_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    if 'codSusp' in dir(infoProc): r3010_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    if 'vlrCPSusp' in dir(infoProc): r3010_infoproc_dados['vlrcpsusp'] = infoProc.vlrCPSusp.cdata
                    insert = create_insert('r3010_infoproc', r3010_infoproc_dados)
                    resp = executar_sql(insert, True)
                    r3010_infoproc_id = resp[0][0]
                    #print r3010_infoproc_id
        
    return dados