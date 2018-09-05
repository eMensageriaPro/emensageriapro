#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s1260_evtcomprod(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s1260_evtcomprod_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s1260_evtcomprod_dados['status'] = 1
    else:
        s1260_evtcomprod_dados['status'] = 0
    s1260_evtcomprod_dados['versao'] = xmlns[len(xmlns)-1]
    s1260_evtcomprod_dados['identidade'] = doc.eSocial.evtComProd['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s1260_evtcomprod_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s1260_evtcomprod_dados['processamento_codigo_resposta'] = 1
    evtComProd = doc.eSocial.evtComProd
    
    if 'indRetif' in dir(evtComProd.ideEvento): s1260_evtcomprod_dados['indretif'] = evtComProd.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtComProd.ideEvento): s1260_evtcomprod_dados['nrrecibo'] = evtComProd.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtComProd.ideEvento): s1260_evtcomprod_dados['indapuracao'] = evtComProd.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtComProd.ideEvento): s1260_evtcomprod_dados['perapur'] = evtComProd.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtComProd.ideEvento): s1260_evtcomprod_dados['tpamb'] = evtComProd.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtComProd.ideEvento): s1260_evtcomprod_dados['procemi'] = evtComProd.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtComProd.ideEvento): s1260_evtcomprod_dados['verproc'] = evtComProd.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtComProd.ideEmpregador): s1260_evtcomprod_dados['tpinsc'] = evtComProd.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtComProd.ideEmpregador): s1260_evtcomprod_dados['nrinsc'] = evtComProd.ideEmpregador.nrInsc.cdata
    if 'nrInscEstabRural' in dir(evtComProd.infoComProd.ideEstabel): s1260_evtcomprod_dados['nrinscestabrural'] = evtComProd.infoComProd.ideEstabel.nrInscEstabRural.cdata
    if 'inclusao' in dir(evtComProd.infoComProd): s1260_evtcomprod_dados['operacao'] = 1
    elif 'alteracao' in dir(evtComProd.infoComProd): s1260_evtcomprod_dados['operacao'] = 2
    elif 'exclusao' in dir(evtComProd.infoComProd): s1260_evtcomprod_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1260_evtcomprod', s1260_evtcomprod_dados)
    resp = executar_sql(insert, True)
    s1260_evtcomprod_id = resp[0][0]
    dados['evento'] = 's1260'
    dados['identidade'] = s1260_evtcomprod_id
    dados['identidade_evento'] = doc.eSocial.evtComProd['Id']
    dados['status'] = 1

    if 'tpComerc' in dir(evtComProd.infoComProd.ideEstabel):
        for tpComerc in evtComProd.infoComProd.ideEstabel.tpComerc:
            s1260_tpcomerc_dados = {}
            s1260_tpcomerc_dados['s1260_evtcomprod_id'] = s1260_evtcomprod_id
            
            if 'indComerc' in dir(tpComerc): s1260_tpcomerc_dados['indcomerc'] = tpComerc.indComerc.cdata
            if 'vrTotCom' in dir(tpComerc): s1260_tpcomerc_dados['vrtotcom'] = tpComerc.vrTotCom.cdata
            insert = create_insert('s1260_tpcomerc', s1260_tpcomerc_dados)
            resp = executar_sql(insert, True)
            s1260_tpcomerc_id = resp[0][0]
            #print s1260_tpcomerc_id

            if 'ideAdquir' in dir(tpComerc):
                for ideAdquir in tpComerc.ideAdquir:
                    s1260_ideadquir_dados = {}
                    s1260_ideadquir_dados['s1260_tpcomerc_id'] = s1260_tpcomerc_id
                    
                    if 'tpInsc' in dir(ideAdquir): s1260_ideadquir_dados['tpinsc'] = ideAdquir.tpInsc.cdata
                    if 'nrInsc' in dir(ideAdquir): s1260_ideadquir_dados['nrinsc'] = ideAdquir.nrInsc.cdata
                    if 'vrComerc' in dir(ideAdquir): s1260_ideadquir_dados['vrcomerc'] = ideAdquir.vrComerc.cdata
                    insert = create_insert('s1260_ideadquir', s1260_ideadquir_dados)
                    resp = executar_sql(insert, True)
                    s1260_ideadquir_id = resp[0][0]
                    #print s1260_ideadquir_id
        
            if 'infoProcJud' in dir(tpComerc):
                for infoProcJud in tpComerc.infoProcJud:
                    s1260_infoprocjud_dados = {}
                    s1260_infoprocjud_dados['s1260_tpcomerc_id'] = s1260_tpcomerc_id
                    
                    if 'tpProc' in dir(infoProcJud): s1260_infoprocjud_dados['tpproc'] = infoProcJud.tpProc.cdata
                    if 'nrProc' in dir(infoProcJud): s1260_infoprocjud_dados['nrproc'] = infoProcJud.nrProc.cdata
                    if 'codSusp' in dir(infoProcJud): s1260_infoprocjud_dados['codsusp'] = infoProcJud.codSusp.cdata
                    if 'vrCPSusp' in dir(infoProcJud): s1260_infoprocjud_dados['vrcpsusp'] = infoProcJud.vrCPSusp.cdata
                    if 'vrRatSusp' in dir(infoProcJud): s1260_infoprocjud_dados['vrratsusp'] = infoProcJud.vrRatSusp.cdata
                    if 'vrSenarSusp' in dir(infoProcJud): s1260_infoprocjud_dados['vrsenarsusp'] = infoProcJud.vrSenarSusp.cdata
                    insert = create_insert('s1260_infoprocjud', s1260_infoprocjud_dados)
                    resp = executar_sql(insert, True)
                    s1260_infoprocjud_id = resp[0][0]
                    #print s1260_infoprocjud_id
        
    from emensageriapro.esocial.views.s1260_evtcomprod_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1260_evtcomprod_id, 'default')
    return dados