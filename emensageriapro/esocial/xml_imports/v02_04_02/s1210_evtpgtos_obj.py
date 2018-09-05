#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s1210_evtpgtos_obj(doc):
    s1210_evtpgtos_dados = {}
    s1210_evtpgtos_dados['versao'] = 'v02_04_02'
    s1210_evtpgtos_dados['status'] = 12
    s1210_evtpgtos_dados['identidade'] = doc.eSocial.evtPgtos['Id']
    s1210_evtpgtos_dados['processamento_codigo_resposta'] = 1
    evtPgtos = doc.eSocial.evtPgtos
    
    if 'indRetif' in dir(evtPgtos.ideEvento): s1210_evtpgtos_dados['indretif'] = evtPgtos.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtPgtos.ideEvento): s1210_evtpgtos_dados['nrrecibo'] = evtPgtos.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtPgtos.ideEvento): s1210_evtpgtos_dados['indapuracao'] = evtPgtos.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtPgtos.ideEvento): s1210_evtpgtos_dados['perapur'] = evtPgtos.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtPgtos.ideEvento): s1210_evtpgtos_dados['tpamb'] = evtPgtos.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtPgtos.ideEvento): s1210_evtpgtos_dados['procemi'] = evtPgtos.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtPgtos.ideEvento): s1210_evtpgtos_dados['verproc'] = evtPgtos.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtPgtos.ideEmpregador): s1210_evtpgtos_dados['tpinsc'] = evtPgtos.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtPgtos.ideEmpregador): s1210_evtpgtos_dados['nrinsc'] = evtPgtos.ideEmpregador.nrInsc.cdata
    if 'cpfBenef' in dir(evtPgtos.ideBenef): s1210_evtpgtos_dados['cpfbenef'] = evtPgtos.ideBenef.cpfBenef.cdata
    if 'inclusao' in dir(evtPgtos.ideBenef): s1210_evtpgtos_dados['operacao'] = 1
    elif 'alteracao' in dir(evtPgtos.ideBenef): s1210_evtpgtos_dados['operacao'] = 2
    elif 'exclusao' in dir(evtPgtos.ideBenef): s1210_evtpgtos_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1210_evtpgtos', s1210_evtpgtos_dados)
    resp = executar_sql(insert, True)
    s1210_evtpgtos_id = resp[0][0]
    dados = s1210_evtpgtos_dados
    dados['evento'] = 's1210'
    dados['id'] = s1210_evtpgtos_id
    dados['identidade_evento'] = doc.eSocial.evtPgtos['Id']
    dados['status'] = 1

    if 'deps' in dir(evtPgtos.ideBenef):
        for deps in evtPgtos.ideBenef.deps:
            s1210_deps_dados = {}
            s1210_deps_dados['s1210_evtpgtos_id'] = s1210_evtpgtos_id
            
            if 'vrDedDep' in dir(deps): s1210_deps_dados['vrdeddep'] = deps.vrDedDep.cdata
            insert = create_insert('s1210_deps', s1210_deps_dados)
            resp = executar_sql(insert, True)
            s1210_deps_id = resp[0][0]
            #print s1210_deps_id

    if 'infoPgto' in dir(evtPgtos.ideBenef):
        for infoPgto in evtPgtos.ideBenef.infoPgto:
            s1210_infopgto_dados = {}
            s1210_infopgto_dados['s1210_evtpgtos_id'] = s1210_evtpgtos_id
            
            if 'dtPgto' in dir(infoPgto): s1210_infopgto_dados['dtpgto'] = infoPgto.dtPgto.cdata
            if 'tpPgto' in dir(infoPgto): s1210_infopgto_dados['tppgto'] = infoPgto.tpPgto.cdata
            if 'indResBr' in dir(infoPgto): s1210_infopgto_dados['indresbr'] = infoPgto.indResBr.cdata
            insert = create_insert('s1210_infopgto', s1210_infopgto_dados)
            resp = executar_sql(insert, True)
            s1210_infopgto_id = resp[0][0]
            #print s1210_infopgto_id

            if 'detPgtoFl' in dir(infoPgto):
                for detPgtoFl in infoPgto.detPgtoFl:
                    s1210_detpgtofl_dados = {}
                    s1210_detpgtofl_dados['s1210_infopgto_id'] = s1210_infopgto_id
                    
                    if 'perRef' in dir(detPgtoFl): s1210_detpgtofl_dados['perref'] = detPgtoFl.perRef.cdata
                    if 'ideDmDev' in dir(detPgtoFl): s1210_detpgtofl_dados['idedmdev'] = detPgtoFl.ideDmDev.cdata
                    if 'indPgtoTt' in dir(detPgtoFl): s1210_detpgtofl_dados['indpgtott'] = detPgtoFl.indPgtoTt.cdata
                    if 'vrLiq' in dir(detPgtoFl): s1210_detpgtofl_dados['vrliq'] = detPgtoFl.vrLiq.cdata
                    if 'nrRecArq' in dir(detPgtoFl): s1210_detpgtofl_dados['nrrecarq'] = detPgtoFl.nrRecArq.cdata
                    insert = create_insert('s1210_detpgtofl', s1210_detpgtofl_dados)
                    resp = executar_sql(insert, True)
                    s1210_detpgtofl_id = resp[0][0]
                    #print s1210_detpgtofl_id
        
            if 'detPgtoBenPr' in dir(infoPgto):
                for detPgtoBenPr in infoPgto.detPgtoBenPr:
                    s1210_detpgtobenpr_dados = {}
                    s1210_detpgtobenpr_dados['s1210_infopgto_id'] = s1210_infopgto_id
                    
                    if 'perRef' in dir(detPgtoBenPr): s1210_detpgtobenpr_dados['perref'] = detPgtoBenPr.perRef.cdata
                    if 'ideDmDev' in dir(detPgtoBenPr): s1210_detpgtobenpr_dados['idedmdev'] = detPgtoBenPr.ideDmDev.cdata
                    if 'indPgtoTt' in dir(detPgtoBenPr): s1210_detpgtobenpr_dados['indpgtott'] = detPgtoBenPr.indPgtoTt.cdata
                    if 'vrLiq' in dir(detPgtoBenPr): s1210_detpgtobenpr_dados['vrliq'] = detPgtoBenPr.vrLiq.cdata
                    insert = create_insert('s1210_detpgtobenpr', s1210_detpgtobenpr_dados)
                    resp = executar_sql(insert, True)
                    s1210_detpgtobenpr_id = resp[0][0]
                    #print s1210_detpgtobenpr_id
        
            if 'detPgtoFer' in dir(infoPgto):
                for detPgtoFer in infoPgto.detPgtoFer:
                    s1210_detpgtofer_dados = {}
                    s1210_detpgtofer_dados['s1210_infopgto_id'] = s1210_infopgto_id
                    
                    if 'codCateg' in dir(detPgtoFer): s1210_detpgtofer_dados['codcateg'] = detPgtoFer.codCateg.cdata
                    if 'matricula' in dir(detPgtoFer): s1210_detpgtofer_dados['matricula'] = detPgtoFer.matricula.cdata
                    if 'dtIniGoz' in dir(detPgtoFer): s1210_detpgtofer_dados['dtinigoz'] = detPgtoFer.dtIniGoz.cdata
                    if 'qtDias' in dir(detPgtoFer): s1210_detpgtofer_dados['qtdias'] = detPgtoFer.qtDias.cdata
                    if 'vrLiq' in dir(detPgtoFer): s1210_detpgtofer_dados['vrliq'] = detPgtoFer.vrLiq.cdata
                    insert = create_insert('s1210_detpgtofer', s1210_detpgtofer_dados)
                    resp = executar_sql(insert, True)
                    s1210_detpgtofer_id = resp[0][0]
                    #print s1210_detpgtofer_id
        
            if 'detPgtoAnt' in dir(infoPgto):
                for detPgtoAnt in infoPgto.detPgtoAnt:
                    s1210_detpgtoant_dados = {}
                    s1210_detpgtoant_dados['s1210_infopgto_id'] = s1210_infopgto_id
                    
                    if 'codCateg' in dir(detPgtoAnt): s1210_detpgtoant_dados['codcateg'] = detPgtoAnt.codCateg.cdata
                    insert = create_insert('s1210_detpgtoant', s1210_detpgtoant_dados)
                    resp = executar_sql(insert, True)
                    s1210_detpgtoant_id = resp[0][0]
                    #print s1210_detpgtoant_id
        
            if 'idePgtoExt' in dir(infoPgto):
                for idePgtoExt in infoPgto.idePgtoExt:
                    s1210_idepgtoext_dados = {}
                    s1210_idepgtoext_dados['s1210_infopgto_id'] = s1210_infopgto_id
                    
                    if 'codPais' in dir(idePgtoExt): s1210_idepgtoext_dados['codpais'] = idePgtoExt.idePais.codPais.cdata
                    if 'indNIF' in dir(idePgtoExt): s1210_idepgtoext_dados['indnif'] = idePgtoExt.idePais.indNIF.cdata
                    if 'nifBenef' in dir(idePgtoExt): s1210_idepgtoext_dados['nifbenef'] = idePgtoExt.idePais.nifBenef.cdata
                    if 'dscLograd' in dir(idePgtoExt): s1210_idepgtoext_dados['dsclograd'] = idePgtoExt.endExt.dscLograd.cdata
                    if 'nrLograd' in dir(idePgtoExt): s1210_idepgtoext_dados['nrlograd'] = idePgtoExt.endExt.nrLograd.cdata
                    if 'complem' in dir(idePgtoExt): s1210_idepgtoext_dados['complem'] = idePgtoExt.endExt.complem.cdata
                    if 'bairro' in dir(idePgtoExt): s1210_idepgtoext_dados['bairro'] = idePgtoExt.endExt.bairro.cdata
                    if 'nmCid' in dir(idePgtoExt): s1210_idepgtoext_dados['nmcid'] = idePgtoExt.endExt.nmCid.cdata
                    if 'codPostal' in dir(idePgtoExt): s1210_idepgtoext_dados['codpostal'] = idePgtoExt.endExt.codPostal.cdata
                    insert = create_insert('s1210_idepgtoext', s1210_idepgtoext_dados)
                    resp = executar_sql(insert, True)
                    s1210_idepgtoext_id = resp[0][0]
                    #print s1210_idepgtoext_id
        
    return dados