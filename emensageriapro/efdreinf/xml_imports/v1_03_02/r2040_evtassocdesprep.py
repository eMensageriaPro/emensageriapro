#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r2040_evtassocdesprep(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    r2040_evtassocdesprep_dados = {}
    xmlns = doc.Reinf['xmlns'].split('/')
    if validar:
        r2040_evtassocdesprep_dados['status'] = 1
    else:
        r2040_evtassocdesprep_dados['status'] = 0
    r2040_evtassocdesprep_dados['versao'] = xmlns[len(xmlns)-1]
    r2040_evtassocdesprep_dados['identidade'] = doc.Reinf.evtAssocDespRep['id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_efdreinf WHERE identidade = '%s';
    #     """ % r2040_evtassocdesprep_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    #r2040_evtassocdesprep_dados['processamento_codigo_resposta'] = 1
    evtAssocDespRep = doc.Reinf.evtAssocDespRep
    
    if 'indRetif' in dir(evtAssocDespRep.ideEvento): r2040_evtassocdesprep_dados['indretif'] = evtAssocDespRep.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAssocDespRep.ideEvento): r2040_evtassocdesprep_dados['nrrecibo'] = evtAssocDespRep.ideEvento.nrRecibo.cdata
    if 'perApur' in dir(evtAssocDespRep.ideEvento): r2040_evtassocdesprep_dados['perapur'] = evtAssocDespRep.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtAssocDespRep.ideEvento): r2040_evtassocdesprep_dados['tpamb'] = evtAssocDespRep.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAssocDespRep.ideEvento): r2040_evtassocdesprep_dados['procemi'] = evtAssocDespRep.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAssocDespRep.ideEvento): r2040_evtassocdesprep_dados['verproc'] = evtAssocDespRep.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAssocDespRep.ideContri): r2040_evtassocdesprep_dados['tpinsc'] = evtAssocDespRep.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtAssocDespRep.ideContri): r2040_evtassocdesprep_dados['nrinsc'] = evtAssocDespRep.ideContri.nrInsc.cdata
    if 'tpInscEstab' in dir(evtAssocDespRep.ideContri.ideEstab): r2040_evtassocdesprep_dados['tpinscestab'] = evtAssocDespRep.ideContri.ideEstab.tpInscEstab.cdata
    if 'nrInscEstab' in dir(evtAssocDespRep.ideContri.ideEstab): r2040_evtassocdesprep_dados['nrinscestab'] = evtAssocDespRep.ideContri.ideEstab.nrInscEstab.cdata
    if 'inclusao' in dir(evtAssocDespRep.ideContri): r2040_evtassocdesprep_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAssocDespRep.ideContri): r2040_evtassocdesprep_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAssocDespRep.ideContri): r2040_evtassocdesprep_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2040_evtassocdesprep', r2040_evtassocdesprep_dados)
    resp = executar_sql(insert, True)
    r2040_evtassocdesprep_id = resp[0][0]
    dados['evento'] = 'r2040'
    dados['identidade'] = r2040_evtassocdesprep_id
    dados['identidade_evento'] = doc.Reinf.evtAssocDespRep['id']
    dados['status'] = 1


    if 'recursosRep' in dir(evtAssocDespRep.ideContri.ideEstab):
        for recursosRep in evtAssocDespRep.ideContri.ideEstab.recursosRep:
            r2040_recursosrep_dados = {}
            r2040_recursosrep_dados['r2040_evtassocdesprep_id'] = r2040_evtassocdesprep_id
            
            if 'cnpjAssocDesp' in dir(recursosRep): r2040_recursosrep_dados['cnpjassocdesp'] = recursosRep.cnpjAssocDesp.cdata
            if 'vlrTotalRep' in dir(recursosRep): r2040_recursosrep_dados['vlrtotalrep'] = recursosRep.vlrTotalRep.cdata
            if 'vlrTotalRet' in dir(recursosRep): r2040_recursosrep_dados['vlrtotalret'] = recursosRep.vlrTotalRet.cdata
            if 'vlrTotalNRet' in dir(recursosRep): r2040_recursosrep_dados['vlrtotalnret'] = recursosRep.vlrTotalNRet.cdata
            insert = create_insert('r2040_recursosrep', r2040_recursosrep_dados)
            resp = executar_sql(insert, True)
            r2040_recursosrep_id = resp[0][0]
            #print r2040_recursosrep_id

            if 'infoRecurso' in dir(recursosRep):
                for infoRecurso in recursosRep.infoRecurso:
                    r2040_inforecurso_dados = {}
                    r2040_inforecurso_dados['r2040_recursosrep_id'] = r2040_recursosrep_id
                    
                    if 'tpRepasse' in dir(infoRecurso): r2040_inforecurso_dados['tprepasse'] = infoRecurso.tpRepasse.cdata
                    if 'descRecurso' in dir(infoRecurso): r2040_inforecurso_dados['descrecurso'] = infoRecurso.descRecurso.cdata
                    if 'vlrBruto' in dir(infoRecurso): r2040_inforecurso_dados['vlrbruto'] = infoRecurso.vlrBruto.cdata
                    if 'vlrRetApur' in dir(infoRecurso): r2040_inforecurso_dados['vlrretapur'] = infoRecurso.vlrRetApur.cdata
                    insert = create_insert('r2040_inforecurso', r2040_inforecurso_dados)
                    resp = executar_sql(insert, True)
                    r2040_inforecurso_id = resp[0][0]
                    #print r2040_inforecurso_id
        
            if 'infoProc' in dir(recursosRep):
                for infoProc in recursosRep.infoProc:
                    r2040_infoproc_dados = {}
                    r2040_infoproc_dados['r2040_recursosrep_id'] = r2040_recursosrep_id
                    
                    if 'tpProc' in dir(infoProc): r2040_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    if 'nrProc' in dir(infoProc): r2040_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    if 'codSusp' in dir(infoProc): r2040_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    if 'vlrNRet' in dir(infoProc): r2040_infoproc_dados['vlrnret'] = infoProc.vlrNRet.cdata
                    insert = create_insert('r2040_infoproc', r2040_infoproc_dados)
                    resp = executar_sql(insert, True)
                    r2040_infoproc_id = resp[0][0]
                    #print r2040_infoproc_id
        
    from emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2040_evtassocdesprep_id, 'default')
    return dados