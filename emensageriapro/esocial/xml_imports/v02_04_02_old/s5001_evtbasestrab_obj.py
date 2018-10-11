#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s5001_evtbasestrab_obj(doc):
    s5001_evtbasestrab_dados = {}
    s5001_evtbasestrab_dados['versao'] = 'v02_04_02'
    s5001_evtbasestrab_dados['status'] = 12
    s5001_evtbasestrab_dados['identidade'] = doc.eSocial.evtBasesTrab['Id']
    s5001_evtbasestrab_dados['processamento_codigo_resposta'] = 1
    evtBasesTrab = doc.eSocial.evtBasesTrab
    
    if 'nrRecArqBase' in dir(evtBasesTrab.ideEvento): s5001_evtbasestrab_dados['nrrecarqbase'] = evtBasesTrab.ideEvento.nrRecArqBase.cdata
    if 'indApuracao' in dir(evtBasesTrab.ideEvento): s5001_evtbasestrab_dados['indapuracao'] = evtBasesTrab.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtBasesTrab.ideEvento): s5001_evtbasestrab_dados['perapur'] = evtBasesTrab.ideEvento.perApur.cdata
    if 'tpInsc' in dir(evtBasesTrab.ideEmpregador): s5001_evtbasestrab_dados['tpinsc'] = evtBasesTrab.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtBasesTrab.ideEmpregador): s5001_evtbasestrab_dados['nrinsc'] = evtBasesTrab.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtBasesTrab.ideTrabalhador): s5001_evtbasestrab_dados['cpftrab'] = evtBasesTrab.ideTrabalhador.cpfTrab.cdata
    if 'inclusao' in dir(evtBasesTrab.infoCp): s5001_evtbasestrab_dados['operacao'] = 1
    elif 'alteracao' in dir(evtBasesTrab.infoCp): s5001_evtbasestrab_dados['operacao'] = 2
    elif 'exclusao' in dir(evtBasesTrab.infoCp): s5001_evtbasestrab_dados['operacao'] = 3
    #print dados
    insert = create_insert('s5001_evtbasestrab', s5001_evtbasestrab_dados)
    resp = executar_sql(insert, True)
    s5001_evtbasestrab_id = resp[0][0]
    dados = s5001_evtbasestrab_dados
    dados['evento'] = 's5001'
    dados['id'] = s5001_evtbasestrab_id
    dados['identidade_evento'] = doc.eSocial.evtBasesTrab['Id']
    dados['status'] = 1

    if 'procJudTrab' in dir(evtBasesTrab.ideTrabalhador):
        for procJudTrab in evtBasesTrab.ideTrabalhador.procJudTrab:
            s5001_procjudtrab_dados = {}
            s5001_procjudtrab_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab_id
            
            if 'nrProcJud' in dir(procJudTrab): s5001_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            if 'codSusp' in dir(procJudTrab): s5001_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            insert = create_insert('s5001_procjudtrab', s5001_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s5001_procjudtrab_id = resp[0][0]
            #print s5001_procjudtrab_id

    if 'infoCpCalc' in dir(evtBasesTrab):
        for infoCpCalc in evtBasesTrab.infoCpCalc:
            s5001_infocpcalc_dados = {}
            s5001_infocpcalc_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab_id
            
            if 'tpCR' in dir(infoCpCalc): s5001_infocpcalc_dados['tpcr'] = infoCpCalc.tpCR.cdata
            if 'vrCpSeg' in dir(infoCpCalc): s5001_infocpcalc_dados['vrcpseg'] = infoCpCalc.vrCpSeg.cdata
            if 'vrDescSeg' in dir(infoCpCalc): s5001_infocpcalc_dados['vrdescseg'] = infoCpCalc.vrDescSeg.cdata
            insert = create_insert('s5001_infocpcalc', s5001_infocpcalc_dados)
            resp = executar_sql(insert, True)
            s5001_infocpcalc_id = resp[0][0]
            #print s5001_infocpcalc_id

    if 'infoCp' in dir(evtBasesTrab):
        for infoCp in evtBasesTrab.infoCp:
            s5001_infocp_dados = {}
            s5001_infocp_dados['s5001_evtbasestrab_id'] = s5001_evtbasestrab_id
            
            insert = create_insert('s5001_infocp', s5001_infocp_dados)
            resp = executar_sql(insert, True)
            s5001_infocp_id = resp[0][0]
            #print s5001_infocp_id

            if 'ideEstabLot' in dir(infoCp):
                for ideEstabLot in infoCp.ideEstabLot:
                    s5001_ideestablot_dados = {}
                    s5001_ideestablot_dados['s5001_infocp_id'] = s5001_infocp_id
                    
                    if 'tpInsc' in dir(ideEstabLot): s5001_ideestablot_dados['tpinsc'] = ideEstabLot.tpInsc.cdata
                    if 'nrInsc' in dir(ideEstabLot): s5001_ideestablot_dados['nrinsc'] = ideEstabLot.nrInsc.cdata
                    if 'codLotacao' in dir(ideEstabLot): s5001_ideestablot_dados['codlotacao'] = ideEstabLot.codLotacao.cdata
                    insert = create_insert('s5001_ideestablot', s5001_ideestablot_dados)
                    resp = executar_sql(insert, True)
                    s5001_ideestablot_id = resp[0][0]
                    #print s5001_ideestablot_id
        
    return dados