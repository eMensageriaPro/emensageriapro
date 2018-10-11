#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r2060_evtcprb(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    r2060_evtcprb_dados = {}
    xmlns = doc.Reinf['xmlns'].split('/')
    if validar:
        r2060_evtcprb_dados['status'] = 1
    else:
        r2060_evtcprb_dados['status'] = 0
    r2060_evtcprb_dados['versao'] = xmlns[len(xmlns)-1]
    r2060_evtcprb_dados['identidade'] = doc.Reinf.evtCPRB['id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_efdreinf WHERE identidade = '%s';
    #     """ % r2060_evtcprb_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    #r2060_evtcprb_dados['processamento_codigo_resposta'] = 1
    evtCPRB = doc.Reinf.evtCPRB
    
    if 'indRetif' in dir(evtCPRB.ideEvento): r2060_evtcprb_dados['indretif'] = evtCPRB.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtCPRB.ideEvento): r2060_evtcprb_dados['nrrecibo'] = evtCPRB.ideEvento.nrRecibo.cdata
    if 'perApur' in dir(evtCPRB.ideEvento): r2060_evtcprb_dados['perapur'] = evtCPRB.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtCPRB.ideEvento): r2060_evtcprb_dados['tpamb'] = evtCPRB.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtCPRB.ideEvento): r2060_evtcprb_dados['procemi'] = evtCPRB.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtCPRB.ideEvento): r2060_evtcprb_dados['verproc'] = evtCPRB.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtCPRB.ideContri): r2060_evtcprb_dados['tpinsc'] = evtCPRB.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtCPRB.ideContri): r2060_evtcprb_dados['nrinsc'] = evtCPRB.ideContri.nrInsc.cdata
    if 'tpInscEstab' in dir(evtCPRB.infoCPRB.ideEstab): r2060_evtcprb_dados['tpinscestab'] = evtCPRB.infoCPRB.ideEstab.tpInscEstab.cdata
    if 'nrInscEstab' in dir(evtCPRB.infoCPRB.ideEstab): r2060_evtcprb_dados['nrinscestab'] = evtCPRB.infoCPRB.ideEstab.nrInscEstab.cdata
    if 'vlrRecBrutaTotal' in dir(evtCPRB.infoCPRB.ideEstab): r2060_evtcprb_dados['vlrrecbrutatotal'] = evtCPRB.infoCPRB.ideEstab.vlrRecBrutaTotal.cdata
    if 'vlrCPApurTotal' in dir(evtCPRB.infoCPRB.ideEstab): r2060_evtcprb_dados['vlrcpapurtotal'] = evtCPRB.infoCPRB.ideEstab.vlrCPApurTotal.cdata
    if 'vlrCPRBSuspTotal' in dir(evtCPRB.infoCPRB.ideEstab): r2060_evtcprb_dados['vlrcprbsusptotal'] = evtCPRB.infoCPRB.ideEstab.vlrCPRBSuspTotal.cdata
    if 'inclusao' in dir(evtCPRB.infoCPRB): r2060_evtcprb_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCPRB.infoCPRB): r2060_evtcprb_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCPRB.infoCPRB): r2060_evtcprb_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2060_evtcprb', r2060_evtcprb_dados)
    resp = executar_sql(insert, True)
    r2060_evtcprb_id = resp[0][0]
    dados['evento'] = 'r2060'
    dados['identidade'] = r2060_evtcprb_id
    dados['identidade_evento'] = doc.Reinf.evtCPRB['id']
    dados['status'] = 1


    if 'tipoCod' in dir(evtCPRB.infoCPRB.ideEstab):
        for tipoCod in evtCPRB.infoCPRB.ideEstab.tipoCod:
            r2060_tipocod_dados = {}
            r2060_tipocod_dados['r2060_evtcprb_id'] = r2060_evtcprb_id
            
            if 'codAtivEcon' in dir(tipoCod): r2060_tipocod_dados['codativecon'] = tipoCod.codAtivEcon.cdata
            if 'vlrRecBrutaAtiv' in dir(tipoCod): r2060_tipocod_dados['vlrrecbrutaativ'] = tipoCod.vlrRecBrutaAtiv.cdata
            if 'vlrExcRecBruta' in dir(tipoCod): r2060_tipocod_dados['vlrexcrecbruta'] = tipoCod.vlrExcRecBruta.cdata
            if 'vlrAdicRecBruta' in dir(tipoCod): r2060_tipocod_dados['vlradicrecbruta'] = tipoCod.vlrAdicRecBruta.cdata
            if 'vlrBcCPRB' in dir(tipoCod): r2060_tipocod_dados['vlrbccprb'] = tipoCod.vlrBcCPRB.cdata
            if 'vlrCPRBapur' in dir(tipoCod): r2060_tipocod_dados['vlrcprbapur'] = tipoCod.vlrCPRBapur.cdata
            insert = create_insert('r2060_tipocod', r2060_tipocod_dados)
            resp = executar_sql(insert, True)
            r2060_tipocod_id = resp[0][0]
            #print r2060_tipocod_id

            if 'tipoAjuste' in dir(tipoCod):
                for tipoAjuste in tipoCod.tipoAjuste:
                    r2060_tipoajuste_dados = {}
                    r2060_tipoajuste_dados['r2060_tipocod_id'] = r2060_tipocod_id
                    
                    if 'tpAjuste' in dir(tipoAjuste): r2060_tipoajuste_dados['tpajuste'] = tipoAjuste.tpAjuste.cdata
                    if 'codAjuste' in dir(tipoAjuste): r2060_tipoajuste_dados['codajuste'] = tipoAjuste.codAjuste.cdata
                    if 'vlrAjuste' in dir(tipoAjuste): r2060_tipoajuste_dados['vlrajuste'] = tipoAjuste.vlrAjuste.cdata
                    if 'descAjuste' in dir(tipoAjuste): r2060_tipoajuste_dados['descajuste'] = tipoAjuste.descAjuste.cdata
                    if 'dtAjuste' in dir(tipoAjuste): r2060_tipoajuste_dados['dtajuste'] = tipoAjuste.dtAjuste.cdata
                    insert = create_insert('r2060_tipoajuste', r2060_tipoajuste_dados)
                    resp = executar_sql(insert, True)
                    r2060_tipoajuste_id = resp[0][0]
                    #print r2060_tipoajuste_id
        
            if 'infoProc' in dir(tipoCod):
                for infoProc in tipoCod.infoProc:
                    r2060_infoproc_dados = {}
                    r2060_infoproc_dados['r2060_tipocod_id'] = r2060_tipocod_id
                    
                    if 'tpProc' in dir(infoProc): r2060_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
                    if 'nrProc' in dir(infoProc): r2060_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
                    if 'codSusp' in dir(infoProc): r2060_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
                    if 'vlrCPRBSusp' in dir(infoProc): r2060_infoproc_dados['vlrcprbsusp'] = infoProc.vlrCPRBSusp.cdata
                    insert = create_insert('r2060_infoproc', r2060_infoproc_dados)
                    resp = executar_sql(insert, True)
                    r2060_infoproc_id = resp[0][0]
                    #print r2060_infoproc_id
        
    from emensageriapro.efdreinf.views.r2060_evtcprb_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2060_evtcprb_id, 'default')
    return dados