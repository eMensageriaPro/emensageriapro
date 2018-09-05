#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s1250_evtaqprod_obj(doc):
    s1250_evtaqprod_dados = {}
    s1250_evtaqprod_dados['versao'] = 'v02_04_02'
    s1250_evtaqprod_dados['status'] = 12
    s1250_evtaqprod_dados['identidade'] = doc.eSocial.evtAqProd['Id']
    s1250_evtaqprod_dados['processamento_codigo_resposta'] = 1
    evtAqProd = doc.eSocial.evtAqProd
    
    if 'indRetif' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['indretif'] = evtAqProd.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['nrrecibo'] = evtAqProd.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['indapuracao'] = evtAqProd.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['perapur'] = evtAqProd.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['tpamb'] = evtAqProd.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['procemi'] = evtAqProd.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAqProd.ideEvento): s1250_evtaqprod_dados['verproc'] = evtAqProd.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAqProd.ideEmpregador): s1250_evtaqprod_dados['tpinsc'] = evtAqProd.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAqProd.ideEmpregador): s1250_evtaqprod_dados['nrinsc'] = evtAqProd.ideEmpregador.nrInsc.cdata
    if 'tpInscAdq' in dir(evtAqProd.infoAquisProd.ideEstabAdquir): s1250_evtaqprod_dados['tpinscadq'] = evtAqProd.infoAquisProd.ideEstabAdquir.tpInscAdq.cdata
    if 'nrInscAdq' in dir(evtAqProd.infoAquisProd.ideEstabAdquir): s1250_evtaqprod_dados['nrinscadq'] = evtAqProd.infoAquisProd.ideEstabAdquir.nrInscAdq.cdata
    if 'inclusao' in dir(evtAqProd.infoAquisProd): s1250_evtaqprod_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAqProd.infoAquisProd): s1250_evtaqprod_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAqProd.infoAquisProd): s1250_evtaqprod_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1250_evtaqprod', s1250_evtaqprod_dados)
    resp = executar_sql(insert, True)
    s1250_evtaqprod_id = resp[0][0]
    dados = s1250_evtaqprod_dados
    dados['evento'] = 's1250'
    dados['id'] = s1250_evtaqprod_id
    dados['identidade_evento'] = doc.eSocial.evtAqProd['Id']
    dados['status'] = 1

    if 'tpAquis' in dir(evtAqProd.infoAquisProd.ideEstabAdquir):
        for tpAquis in evtAqProd.infoAquisProd.ideEstabAdquir.tpAquis:
            s1250_tpaquis_dados = {}
            s1250_tpaquis_dados['s1250_evtaqprod_id'] = s1250_evtaqprod_id
            
            if 'indAquis' in dir(tpAquis): s1250_tpaquis_dados['indaquis'] = tpAquis.indAquis.cdata
            if 'vlrTotAquis' in dir(tpAquis): s1250_tpaquis_dados['vlrtotaquis'] = tpAquis.vlrTotAquis.cdata
            insert = create_insert('s1250_tpaquis', s1250_tpaquis_dados)
            resp = executar_sql(insert, True)
            s1250_tpaquis_id = resp[0][0]
            #print s1250_tpaquis_id

            if 'ideProdutor' in dir(tpAquis):
                for ideProdutor in tpAquis.ideProdutor:
                    s1250_ideprodutor_dados = {}
                    s1250_ideprodutor_dados['s1250_tpaquis_id'] = s1250_tpaquis_id
                    
                    if 'tpInscProd' in dir(ideProdutor): s1250_ideprodutor_dados['tpinscprod'] = ideProdutor.tpInscProd.cdata
                    if 'nrInscProd' in dir(ideProdutor): s1250_ideprodutor_dados['nrinscprod'] = ideProdutor.nrInscProd.cdata
                    if 'vlrBruto' in dir(ideProdutor): s1250_ideprodutor_dados['vlrbruto'] = ideProdutor.vlrBruto.cdata
                    if 'vrCPDescPR' in dir(ideProdutor): s1250_ideprodutor_dados['vrcpdescpr'] = ideProdutor.vrCPDescPR.cdata
                    if 'vrRatDescPR' in dir(ideProdutor): s1250_ideprodutor_dados['vrratdescpr'] = ideProdutor.vrRatDescPR.cdata
                    if 'vrSenarDesc' in dir(ideProdutor): s1250_ideprodutor_dados['vrsenardesc'] = ideProdutor.vrSenarDesc.cdata
                    insert = create_insert('s1250_ideprodutor', s1250_ideprodutor_dados)
                    resp = executar_sql(insert, True)
                    s1250_ideprodutor_id = resp[0][0]
                    #print s1250_ideprodutor_id
        
    return dados