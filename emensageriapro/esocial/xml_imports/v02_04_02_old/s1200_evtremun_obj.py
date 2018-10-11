#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s1200_evtremun_obj(doc):
    s1200_evtremun_dados = {}
    s1200_evtremun_dados['versao'] = 'v02_04_02'
    s1200_evtremun_dados['status'] = 12
    s1200_evtremun_dados['identidade'] = doc.eSocial.evtRemun['Id']
    s1200_evtremun_dados['processamento_codigo_resposta'] = 1
    evtRemun = doc.eSocial.evtRemun
    
    if 'indRetif' in dir(evtRemun.ideEvento): s1200_evtremun_dados['indretif'] = evtRemun.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtRemun.ideEvento): s1200_evtremun_dados['nrrecibo'] = evtRemun.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtRemun.ideEvento): s1200_evtremun_dados['indapuracao'] = evtRemun.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtRemun.ideEvento): s1200_evtremun_dados['perapur'] = evtRemun.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtRemun.ideEvento): s1200_evtremun_dados['tpamb'] = evtRemun.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtRemun.ideEvento): s1200_evtremun_dados['procemi'] = evtRemun.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtRemun.ideEvento): s1200_evtremun_dados['verproc'] = evtRemun.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtRemun.ideEmpregador): s1200_evtremun_dados['tpinsc'] = evtRemun.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtRemun.ideEmpregador): s1200_evtremun_dados['nrinsc'] = evtRemun.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtRemun.ideTrabalhador): s1200_evtremun_dados['cpftrab'] = evtRemun.ideTrabalhador.cpfTrab.cdata
    if 'nisTrab' in dir(evtRemun.ideTrabalhador): s1200_evtremun_dados['nistrab'] = evtRemun.ideTrabalhador.nisTrab.cdata
    if 'inclusao' in dir(evtRemun.dmDev): s1200_evtremun_dados['operacao'] = 1
    elif 'alteracao' in dir(evtRemun.dmDev): s1200_evtremun_dados['operacao'] = 2
    elif 'exclusao' in dir(evtRemun.dmDev): s1200_evtremun_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1200_evtremun', s1200_evtremun_dados)
    resp = executar_sql(insert, True)
    s1200_evtremun_id = resp[0][0]
    dados = s1200_evtremun_dados
    dados['evento'] = 's1200'
    dados['id'] = s1200_evtremun_id
    dados['identidade_evento'] = doc.eSocial.evtRemun['Id']
    dados['status'] = 1

    if 'infoMV' in dir(evtRemun.ideTrabalhador):
        for infoMV in evtRemun.ideTrabalhador.infoMV:
            s1200_infomv_dados = {}
            s1200_infomv_dados['s1200_evtremun_id'] = s1200_evtremun_id
            
            if 'indMV' in dir(infoMV): s1200_infomv_dados['indmv'] = infoMV.indMV.cdata
            insert = create_insert('s1200_infomv', s1200_infomv_dados)
            resp = executar_sql(insert, True)
            s1200_infomv_id = resp[0][0]
            #print s1200_infomv_id

            if 'remunOutrEmpr' in dir(infoMV):
                for remunOutrEmpr in infoMV.remunOutrEmpr:
                    s1200_remunoutrempr_dados = {}
                    s1200_remunoutrempr_dados['s1200_infomv_id'] = s1200_infomv_id
                    
                    if 'tpInsc' in dir(remunOutrEmpr): s1200_remunoutrempr_dados['tpinsc'] = remunOutrEmpr.tpInsc.cdata
                    if 'nrInsc' in dir(remunOutrEmpr): s1200_remunoutrempr_dados['nrinsc'] = remunOutrEmpr.nrInsc.cdata
                    if 'codCateg' in dir(remunOutrEmpr): s1200_remunoutrempr_dados['codcateg'] = remunOutrEmpr.codCateg.cdata
                    if 'vlrRemunOE' in dir(remunOutrEmpr): s1200_remunoutrempr_dados['vlrremunoe'] = remunOutrEmpr.vlrRemunOE.cdata
                    insert = create_insert('s1200_remunoutrempr', s1200_remunoutrempr_dados)
                    resp = executar_sql(insert, True)
                    s1200_remunoutrempr_id = resp[0][0]
                    #print s1200_remunoutrempr_id
        
    if 'infoComplem' in dir(evtRemun.ideTrabalhador):
        for infoComplem in evtRemun.ideTrabalhador.infoComplem:
            s1200_infocomplem_dados = {}
            s1200_infocomplem_dados['s1200_evtremun_id'] = s1200_evtremun_id
            
            if 'nmTrab' in dir(infoComplem): s1200_infocomplem_dados['nmtrab'] = infoComplem.nmTrab.cdata
            if 'dtNascto' in dir(infoComplem): s1200_infocomplem_dados['dtnascto'] = infoComplem.dtNascto.cdata
            insert = create_insert('s1200_infocomplem', s1200_infocomplem_dados)
            resp = executar_sql(insert, True)
            s1200_infocomplem_id = resp[0][0]
            #print s1200_infocomplem_id

            if 'sucessaoVinc' in dir(infoComplem):
                for sucessaoVinc in infoComplem.sucessaoVinc:
                    s1200_sucessaovinc_dados = {}
                    s1200_sucessaovinc_dados['s1200_infocomplem_id'] = s1200_infocomplem_id
                    
                    if 'cnpjEmpregAnt' in dir(sucessaoVinc): s1200_sucessaovinc_dados['cnpjempregant'] = sucessaoVinc.cnpjEmpregAnt.cdata
                    if 'matricAnt' in dir(sucessaoVinc): s1200_sucessaovinc_dados['matricant'] = sucessaoVinc.matricAnt.cdata
                    if 'dtAdm' in dir(sucessaoVinc): s1200_sucessaovinc_dados['dtadm'] = sucessaoVinc.dtAdm.cdata
                    if 'observacao' in dir(sucessaoVinc): s1200_sucessaovinc_dados['observacao'] = sucessaoVinc.observacao.cdata
                    insert = create_insert('s1200_sucessaovinc', s1200_sucessaovinc_dados)
                    resp = executar_sql(insert, True)
                    s1200_sucessaovinc_id = resp[0][0]
                    #print s1200_sucessaovinc_id
        
    if 'procJudTrab' in dir(evtRemun.ideTrabalhador):
        for procJudTrab in evtRemun.ideTrabalhador.procJudTrab:
            s1200_procjudtrab_dados = {}
            s1200_procjudtrab_dados['s1200_evtremun_id'] = s1200_evtremun_id
            
            if 'tpTrib' in dir(procJudTrab): s1200_procjudtrab_dados['tptrib'] = procJudTrab.tpTrib.cdata
            if 'nrProcJud' in dir(procJudTrab): s1200_procjudtrab_dados['nrprocjud'] = procJudTrab.nrProcJud.cdata
            if 'codSusp' in dir(procJudTrab): s1200_procjudtrab_dados['codsusp'] = procJudTrab.codSusp.cdata
            insert = create_insert('s1200_procjudtrab', s1200_procjudtrab_dados)
            resp = executar_sql(insert, True)
            s1200_procjudtrab_id = resp[0][0]
            #print s1200_procjudtrab_id

    if 'infoInterm' in dir(evtRemun.ideTrabalhador):
        for infoInterm in evtRemun.ideTrabalhador.infoInterm:
            s1200_infointerm_dados = {}
            s1200_infointerm_dados['s1200_evtremun_id'] = s1200_evtremun_id
            
            if 'qtdDiasInterm' in dir(infoInterm): s1200_infointerm_dados['qtddiasinterm'] = infoInterm.qtdDiasInterm.cdata
            insert = create_insert('s1200_infointerm', s1200_infointerm_dados)
            resp = executar_sql(insert, True)
            s1200_infointerm_id = resp[0][0]
            #print s1200_infointerm_id

    if 'dmDev' in dir(evtRemun):
        for dmDev in evtRemun.dmDev:
            s1200_dmdev_dados = {}
            s1200_dmdev_dados['s1200_evtremun_id'] = s1200_evtremun_id
            
            if 'ideDmDev' in dir(dmDev): s1200_dmdev_dados['idedmdev'] = dmDev.ideDmDev.cdata
            if 'codCateg' in dir(dmDev): s1200_dmdev_dados['codcateg'] = dmDev.codCateg.cdata
            insert = create_insert('s1200_dmdev', s1200_dmdev_dados)
            resp = executar_sql(insert, True)
            s1200_dmdev_id = resp[0][0]
            #print s1200_dmdev_id

            if 'infoPerApur' in dir(dmDev):
                for infoPerApur in dmDev.infoPerApur:
                    s1200_infoperapur_dados = {}
                    s1200_infoperapur_dados['s1200_dmdev_id'] = s1200_dmdev_id
                    
                    insert = create_insert('s1200_infoperapur', s1200_infoperapur_dados)
                    resp = executar_sql(insert, True)
                    s1200_infoperapur_id = resp[0][0]
                    #print s1200_infoperapur_id
        
            if 'infoPerAnt' in dir(dmDev):
                for infoPerAnt in dmDev.infoPerAnt:
                    s1200_infoperant_dados = {}
                    s1200_infoperant_dados['s1200_dmdev_id'] = s1200_dmdev_id
                    
                    insert = create_insert('s1200_infoperant', s1200_infoperant_dados)
                    resp = executar_sql(insert, True)
                    s1200_infoperant_id = resp[0][0]
                    #print s1200_infoperant_id
        
            if 'infoComplCont' in dir(dmDev):
                for infoComplCont in dmDev.infoComplCont:
                    s1200_infoperant_infocomplcont_dados = {}
                    s1200_infoperant_infocomplcont_dados['s1200_dmdev_id'] = s1200_dmdev_id
                    
                    if 'codCBO' in dir(infoComplCont): s1200_infoperant_infocomplcont_dados['codcbo'] = infoComplCont.codCBO.cdata
                    if 'natAtividade' in dir(infoComplCont): s1200_infoperant_infocomplcont_dados['natatividade'] = infoComplCont.natAtividade.cdata
                    if 'qtdDiasTrab' in dir(infoComplCont): s1200_infoperant_infocomplcont_dados['qtddiastrab'] = infoComplCont.qtdDiasTrab.cdata
                    insert = create_insert('s1200_infoperant_infocomplcont', s1200_infoperant_infocomplcont_dados)
                    resp = executar_sql(insert, True)
                    s1200_infoperant_infocomplcont_id = resp[0][0]
                    #print s1200_infoperant_infocomplcont_id
        
    return dados