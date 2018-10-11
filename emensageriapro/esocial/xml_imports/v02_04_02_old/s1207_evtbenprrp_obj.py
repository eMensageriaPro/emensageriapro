#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s1207_evtbenprrp_obj(doc):
    s1207_evtbenprrp_dados = {}
    s1207_evtbenprrp_dados['versao'] = 'v02_04_02'
    s1207_evtbenprrp_dados['status'] = 12
    s1207_evtbenprrp_dados['identidade'] = doc.eSocial.evtBenPrRP['Id']
    s1207_evtbenprrp_dados['processamento_codigo_resposta'] = 1
    evtBenPrRP = doc.eSocial.evtBenPrRP
    
    if 'indRetif' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['indretif'] = evtBenPrRP.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['nrrecibo'] = evtBenPrRP.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['indapuracao'] = evtBenPrRP.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['perapur'] = evtBenPrRP.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['tpamb'] = evtBenPrRP.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['procemi'] = evtBenPrRP.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtBenPrRP.ideEvento): s1207_evtbenprrp_dados['verproc'] = evtBenPrRP.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtBenPrRP.ideEmpregador): s1207_evtbenprrp_dados['tpinsc'] = evtBenPrRP.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtBenPrRP.ideEmpregador): s1207_evtbenprrp_dados['nrinsc'] = evtBenPrRP.ideEmpregador.nrInsc.cdata
    if 'cpfBenef' in dir(evtBenPrRP.ideBenef): s1207_evtbenprrp_dados['cpfbenef'] = evtBenPrRP.ideBenef.cpfBenef.cdata
    if 'inclusao' in dir(evtBenPrRP.dmDev): s1207_evtbenprrp_dados['operacao'] = 1
    elif 'alteracao' in dir(evtBenPrRP.dmDev): s1207_evtbenprrp_dados['operacao'] = 2
    elif 'exclusao' in dir(evtBenPrRP.dmDev): s1207_evtbenprrp_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1207_evtbenprrp', s1207_evtbenprrp_dados)
    resp = executar_sql(insert, True)
    s1207_evtbenprrp_id = resp[0][0]
    dados = s1207_evtbenprrp_dados
    dados['evento'] = 's1207'
    dados['id'] = s1207_evtbenprrp_id
    dados['identidade_evento'] = doc.eSocial.evtBenPrRP['Id']
    dados['status'] = 1

    if 'dmDev' in dir(evtBenPrRP):
        for dmDev in evtBenPrRP.dmDev:
            s1207_dmdev_dados = {}
            s1207_dmdev_dados['s1207_evtbenprrp_id'] = s1207_evtbenprrp_id
            
            if 'tpBenef' in dir(dmDev): s1207_dmdev_dados['tpbenef'] = dmDev.tpBenef.cdata
            if 'nrBenefic' in dir(dmDev): s1207_dmdev_dados['nrbenefic'] = dmDev.nrBenefic.cdata
            if 'ideDmDev' in dir(dmDev): s1207_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            insert = create_insert('s1207_dmdev', s1207_dmdev_dados)
            resp = executar_sql(insert, True)
            s1207_dmdev_id = resp[0][0]
            #print s1207_dmdev_id

            if 'itens' in dir(dmDev):
                for itens in dmDev.itens:
                    s1207_itens_dados = {}
                    s1207_itens_dados['s1207_dmdev_id'] = s1207_dmdev_id
                    
                    if 'codRubr' in dir(itens): s1207_itens_dados['codrubr'] = itens.codRubr.cdata
                    if 'ideTabRubr' in dir(itens): s1207_itens_dados['idetabrubr'] = itens.ideTabRubr.cdata
                    if 'vrRubr' in dir(itens): s1207_itens_dados['vrrubr'] = itens.vrRubr.cdata
                    insert = create_insert('s1207_itens', s1207_itens_dados)
                    resp = executar_sql(insert, True)
                    s1207_itens_id = resp[0][0]
                    #print s1207_itens_id
        
    return dados