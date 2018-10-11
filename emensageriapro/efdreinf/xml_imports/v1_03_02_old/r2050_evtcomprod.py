#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r2050_evtcomprod(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    r2050_evtcomprod_dados = {}
    xmlns = doc.Reinf['xmlns'].split('/')
    if validar:
        r2050_evtcomprod_dados['status'] = 1
    else:
        r2050_evtcomprod_dados['status'] = 0
    r2050_evtcomprod_dados['versao'] = xmlns[len(xmlns)-1]
    r2050_evtcomprod_dados['identidade'] = doc.Reinf.evtComProd['id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_efdreinf WHERE identidade = '%s';
    #     """ % r2050_evtcomprod_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    #r2050_evtcomprod_dados['processamento_codigo_resposta'] = 1
    evtComProd = doc.Reinf.evtComProd
    
    if 'indRetif' in dir(evtComProd.ideEvento): r2050_evtcomprod_dados['indretif'] = evtComProd.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtComProd.ideEvento): r2050_evtcomprod_dados['nrrecibo'] = evtComProd.ideEvento.nrRecibo.cdata
    if 'perApur' in dir(evtComProd.ideEvento): r2050_evtcomprod_dados['perapur'] = evtComProd.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtComProd.ideEvento): r2050_evtcomprod_dados['tpamb'] = evtComProd.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtComProd.ideEvento): r2050_evtcomprod_dados['procemi'] = evtComProd.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtComProd.ideEvento): r2050_evtcomprod_dados['verproc'] = evtComProd.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtComProd.ideContri): r2050_evtcomprod_dados['tpinsc'] = evtComProd.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtComProd.ideContri): r2050_evtcomprod_dados['nrinsc'] = evtComProd.ideContri.nrInsc.cdata
    if 'tpInscEstab' in dir(evtComProd.infoComProd.ideEstab): r2050_evtcomprod_dados['tpinscestab'] = evtComProd.infoComProd.ideEstab.tpInscEstab.cdata
    if 'nrInscEstab' in dir(evtComProd.infoComProd.ideEstab): r2050_evtcomprod_dados['nrinscestab'] = evtComProd.infoComProd.ideEstab.nrInscEstab.cdata
    if 'vlrRecBrutaTotal' in dir(evtComProd.infoComProd.ideEstab): r2050_evtcomprod_dados['vlrrecbrutatotal'] = evtComProd.infoComProd.ideEstab.vlrRecBrutaTotal.cdata
    if 'vlrCPApur' in dir(evtComProd.infoComProd.ideEstab): r2050_evtcomprod_dados['vlrcpapur'] = evtComProd.infoComProd.ideEstab.vlrCPApur.cdata
    if 'vlrRatApur' in dir(evtComProd.infoComProd.ideEstab): r2050_evtcomprod_dados['vlrratapur'] = evtComProd.infoComProd.ideEstab.vlrRatApur.cdata
    if 'vlrSenarApur' in dir(evtComProd.infoComProd.ideEstab): r2050_evtcomprod_dados['vlrsenarapur'] = evtComProd.infoComProd.ideEstab.vlrSenarApur.cdata
    if 'vlrCPSuspTotal' in dir(evtComProd.infoComProd.ideEstab): r2050_evtcomprod_dados['vlrcpsusptotal'] = evtComProd.infoComProd.ideEstab.vlrCPSuspTotal.cdata
    if 'vlrRatSuspTotal' in dir(evtComProd.infoComProd.ideEstab): r2050_evtcomprod_dados['vlrratsusptotal'] = evtComProd.infoComProd.ideEstab.vlrRatSuspTotal.cdata
    if 'vlrSenarSuspTotal' in dir(evtComProd.infoComProd.ideEstab): r2050_evtcomprod_dados['vlrsenarsusptotal'] = evtComProd.infoComProd.ideEstab.vlrSenarSuspTotal.cdata
    if 'inclusao' in dir(evtComProd.infoComProd): r2050_evtcomprod_dados['operacao'] = 1
    elif 'alteracao' in dir(evtComProd.infoComProd): r2050_evtcomprod_dados['operacao'] = 2
    elif 'exclusao' in dir(evtComProd.infoComProd): r2050_evtcomprod_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2050_evtcomprod', r2050_evtcomprod_dados)
    resp = executar_sql(insert, True)
    r2050_evtcomprod_id = resp[0][0]
    dados['evento'] = 'r2050'
    dados['identidade'] = r2050_evtcomprod_id
    dados['identidade_evento'] = doc.Reinf.evtComProd['id']
    dados['status'] = 1


    if 'tipoCom' in dir(evtComProd.infoComProd.ideEstab):
        for tipoCom in evtComProd.infoComProd.ideEstab.tipoCom:
            r2050_tipocom_dados = {}
            r2050_tipocom_dados['r2050_evtcomprod_id'] = r2050_evtcomprod_id
            
            if 'indCom' in dir(tipoCom): r2050_tipocom_dados['indcom'] = tipoCom.indCom.cdata
            if 'vlrRecBruta' in dir(tipoCom): r2050_tipocom_dados['vlrrecbruta'] = tipoCom.vlrRecBruta.cdata
            insert = create_insert('r2050_tipocom', r2050_tipocom_dados)
            resp = executar_sql(insert, True)
            r2050_tipocom_id = resp[0][0]
            #print r2050_tipocom_id

            if 'infoProc' in dir(tipoCom):
                for infoProc in tipoCom.infoProc:
                    r2050_infoproc_dados = {}
                    r2050_infoproc_dados['r2050_tipocom_id'] = r2050_tipocom_id
                    
                    if 'tpProc' in dir(infoProc): r2050_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    if 'nrProc' in dir(infoProc): r2050_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    if 'codSusp' in dir(infoProc): r2050_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    if 'vlrCPSusp' in dir(infoProc): r2050_infoproc_dados['vlrcpsusp'] = infoProc.vlrCPSusp.cdata
                    if 'vlrRatSusp' in dir(infoProc): r2050_infoproc_dados['vlrratsusp'] = infoProc.vlrRatSusp.cdata
                    if 'vlrSenarSusp' in dir(infoProc): r2050_infoproc_dados['vlrsenarsusp'] = infoProc.vlrSenarSusp.cdata
                    insert = create_insert('r2050_infoproc', r2050_infoproc_dados)
                    resp = executar_sql(insert, True)
                    r2050_infoproc_id = resp[0][0]
                    #print r2050_infoproc_id
        
    from emensageriapro.efdreinf.views.r2050_evtcomprod_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2050_evtcomprod_id, 'default')
    return dados