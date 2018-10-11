#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r2030_evtassocdesprec(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    r2030_evtassocdesprec_dados = {}
    xmlns = doc.Reinf['xmlns'].split('/')
    if validar:
        r2030_evtassocdesprec_dados['status'] = 1
    else:
        r2030_evtassocdesprec_dados['status'] = 0
    r2030_evtassocdesprec_dados['versao'] = xmlns[len(xmlns)-1]
    r2030_evtassocdesprec_dados['identidade'] = doc.Reinf.evtAssocDespRec['id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_efdreinf WHERE identidade = '%s';
    #     """ % r2030_evtassocdesprec_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    #r2030_evtassocdesprec_dados['processamento_codigo_resposta'] = 1
    evtAssocDespRec = doc.Reinf.evtAssocDespRec
    
    if 'indRetif' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['indretif'] = evtAssocDespRec.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['nrrecibo'] = evtAssocDespRec.ideEvento.nrRecibo.cdata
    if 'perApur' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['perapur'] = evtAssocDespRec.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['tpamb'] = evtAssocDespRec.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['procemi'] = evtAssocDespRec.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAssocDespRec.ideEvento): r2030_evtassocdesprec_dados['verproc'] = evtAssocDespRec.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['tpinsc'] = evtAssocDespRec.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['nrinsc'] = evtAssocDespRec.ideContri.nrInsc.cdata
    if 'tpInscEstab' in dir(evtAssocDespRec.ideContri.ideEstab): r2030_evtassocdesprec_dados['tpinscestab'] = evtAssocDespRec.ideContri.ideEstab.tpInscEstab.cdata
    if 'nrInscEstab' in dir(evtAssocDespRec.ideContri.ideEstab): r2030_evtassocdesprec_dados['nrinscestab'] = evtAssocDespRec.ideContri.ideEstab.nrInscEstab.cdata
    if 'inclusao' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAssocDespRec.ideContri): r2030_evtassocdesprec_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2030_evtassocdesprec', r2030_evtassocdesprec_dados)
    resp = executar_sql(insert, True)
    r2030_evtassocdesprec_id = resp[0][0]
    dados['evento'] = 'r2030'
    dados['identidade'] = r2030_evtassocdesprec_id
    dados['identidade_evento'] = doc.Reinf.evtAssocDespRec['id']
    dados['status'] = 1


    if 'recursosRec' in dir(evtAssocDespRec.ideContri.ideEstab):
        for recursosRec in evtAssocDespRec.ideContri.ideEstab.recursosRec:
            r2030_recursosrec_dados = {}
            r2030_recursosrec_dados['r2030_evtassocdesprec_id'] = r2030_evtassocdesprec_id
            
            if 'cnpjOrigRecurso' in dir(recursosRec): r2030_recursosrec_dados['cnpjorigrecurso'] = recursosRec.cnpjOrigRecurso.cdata
            if 'vlrTotalRec' in dir(recursosRec): r2030_recursosrec_dados['vlrtotalrec'] = recursosRec.vlrTotalRec.cdata
            if 'vlrTotalRet' in dir(recursosRec): r2030_recursosrec_dados['vlrtotalret'] = recursosRec.vlrTotalRet.cdata
            if 'vlrTotalNRet' in dir(recursosRec): r2030_recursosrec_dados['vlrtotalnret'] = recursosRec.vlrTotalNRet.cdata
            insert = create_insert('r2030_recursosrec', r2030_recursosrec_dados)
            resp = executar_sql(insert, True)
            r2030_recursosrec_id = resp[0][0]
            #print r2030_recursosrec_id

            if 'infoRecurso' in dir(recursosRec):
                for infoRecurso in recursosRec.infoRecurso:
                    r2030_inforecurso_dados = {}
                    r2030_inforecurso_dados['r2030_recursosrec_id'] = r2030_recursosrec_id
                    
                    if 'tpRepasse' in dir(infoRecurso): r2030_inforecurso_dados['tprepasse'] = infoRecurso.tpRepasse.cdata
                    if 'descRecurso' in dir(infoRecurso): r2030_inforecurso_dados['descrecurso'] = infoRecurso.descRecurso.cdata
                    if 'vlrBruto' in dir(infoRecurso): r2030_inforecurso_dados['vlrbruto'] = infoRecurso.vlrBruto.cdata
                    if 'vlrRetApur' in dir(infoRecurso): r2030_inforecurso_dados['vlrretapur'] = infoRecurso.vlrRetApur.cdata
                    insert = create_insert('r2030_inforecurso', r2030_inforecurso_dados)
                    resp = executar_sql(insert, True)
                    r2030_inforecurso_id = resp[0][0]
                    #print r2030_inforecurso_id
        
            if 'infoProc' in dir(recursosRec):
                for infoProc in recursosRec.infoProc:
                    r2030_infoproc_dados = {}
                    r2030_infoproc_dados['r2030_recursosrec_id'] = r2030_recursosrec_id
                    
                    if 'tpProc' in dir(infoProc): r2030_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    if 'nrProc' in dir(infoProc): r2030_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    if 'codSusp' in dir(infoProc): r2030_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    if 'vlrNRet' in dir(infoProc): r2030_infoproc_dados['vlrnret'] = infoProc.vlrNRet.cdata
                    insert = create_insert('r2030_infoproc', r2030_infoproc_dados)
                    resp = executar_sql(insert, True)
                    r2030_infoproc_id = resp[0][0]
                    #print r2030_infoproc_id
        
    from emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2030_evtassocdesprec_id, 'default')
    return dados