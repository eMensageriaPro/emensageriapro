#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r2070_evtpgtosdivs_obj(doc):
    r2070_evtpgtosdivs_dados = {}
    r2070_evtpgtosdivs_dados['versao'] = 'v1_03_02'
    r2070_evtpgtosdivs_dados['status'] = 12
    r2070_evtpgtosdivs_dados['identidade'] = doc.Reinf.evtPgtosDivs['id']
    r2070_evtpgtosdivs_dados['processamento_codigo_resposta'] = 1
    evtPgtosDivs = doc.Reinf.evtPgtosDivs
    
    if 'indRetif' in dir(evtPgtosDivs.ideEvento): r2070_evtpgtosdivs_dados['indretif'] = evtPgtosDivs.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtPgtosDivs.ideEvento): r2070_evtpgtosdivs_dados['nrrecibo'] = evtPgtosDivs.ideEvento.nrRecibo.cdata
    if 'perApur' in dir(evtPgtosDivs.ideEvento): r2070_evtpgtosdivs_dados['perapur'] = evtPgtosDivs.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtPgtosDivs.ideEvento): r2070_evtpgtosdivs_dados['tpamb'] = evtPgtosDivs.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtPgtosDivs.ideEvento): r2070_evtpgtosdivs_dados['procemi'] = evtPgtosDivs.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtPgtosDivs.ideEvento): r2070_evtpgtosdivs_dados['verproc'] = evtPgtosDivs.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtPgtosDivs.ideContri): r2070_evtpgtosdivs_dados['tpinsc'] = evtPgtosDivs.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtPgtosDivs.ideContri): r2070_evtpgtosdivs_dados['nrinsc'] = evtPgtosDivs.ideContri.nrInsc.cdata
    if 'codPgto' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['codpgto'] = evtPgtosDivs.ideBenef.codPgto.cdata
    if 'tpInscBenef' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['tpinscbenef'] = evtPgtosDivs.ideBenef.tpInscBenef.cdata
    if 'nrInscBenef' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['nrinscbenef'] = evtPgtosDivs.ideBenef.nrInscBenef.cdata
    if 'nmRazaoBenef' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['nmrazaobenef'] = evtPgtosDivs.ideBenef.nmRazaoBenef.cdata
    if 'inclusao' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['operacao'] = 1
    elif 'alteracao' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['operacao'] = 2
    elif 'exclusao' in dir(evtPgtosDivs.ideBenef): r2070_evtpgtosdivs_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2070_evtpgtosdivs', r2070_evtpgtosdivs_dados)
    resp = executar_sql(insert, True)
    r2070_evtpgtosdivs_id = resp[0][0]
    dados = r2070_evtpgtosdivs_dados
    dados['evento'] = 'r2070'
    dados['id'] = r2070_evtpgtosdivs_id
    dados['identidade_evento'] = doc.Reinf.evtPgtosDivs['id']
    dados['status'] = 1


    if 'infoResidExt' in dir(evtPgtosDivs.ideBenef):
        for infoResidExt in evtPgtosDivs.ideBenef.infoResidExt:
            r2070_inforesidext_dados = {}
            r2070_inforesidext_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs_id
            
            if 'paisResid' in dir(infoResidExt.infoEnder): r2070_inforesidext_dados['paisresid'] = infoResidExt.infoEnder.paisResid.cdata
            if 'dscLograd' in dir(infoResidExt.infoEnder): r2070_inforesidext_dados['dsclograd'] = infoResidExt.infoEnder.dscLograd.cdata
            if 'nrLograd' in dir(infoResidExt.infoEnder): r2070_inforesidext_dados['nrlograd'] = infoResidExt.infoEnder.nrLograd.cdata
            if 'complem' in dir(infoResidExt.infoEnder): r2070_inforesidext_dados['complem'] = infoResidExt.infoEnder.complem.cdata
            if 'bairro' in dir(infoResidExt.infoEnder): r2070_inforesidext_dados['bairro'] = infoResidExt.infoEnder.bairro.cdata
            if 'cidade' in dir(infoResidExt.infoEnder): r2070_inforesidext_dados['cidade'] = infoResidExt.infoEnder.cidade.cdata
            if 'codPostal' in dir(infoResidExt.infoEnder): r2070_inforesidext_dados['codpostal'] = infoResidExt.infoEnder.codPostal.cdata
            if 'indNIF' in dir(infoResidExt.infoFiscal): r2070_inforesidext_dados['indnif'] = infoResidExt.infoFiscal.indNIF.cdata
            if 'nifBenef' in dir(infoResidExt.infoFiscal): r2070_inforesidext_dados['nifbenef'] = infoResidExt.infoFiscal.nifBenef.cdata
            if 'relFontePagad' in dir(infoResidExt.infoFiscal): r2070_inforesidext_dados['relfontepagad'] = infoResidExt.infoFiscal.relFontePagad.cdata
            insert = create_insert('r2070_inforesidext', r2070_inforesidext_dados)
            resp = executar_sql(insert, True)
            r2070_inforesidext_id = resp[0][0]
            #print r2070_inforesidext_id

    if 'infoMolestia' in dir(evtPgtosDivs.ideBenef):
        for infoMolestia in evtPgtosDivs.ideBenef.infoMolestia:
            r2070_infomolestia_dados = {}
            r2070_infomolestia_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs_id
            
            if 'dtLaudo' in dir(infoMolestia): r2070_infomolestia_dados['dtlaudo'] = infoMolestia.dtLaudo.cdata
            insert = create_insert('r2070_infomolestia', r2070_infomolestia_dados)
            resp = executar_sql(insert, True)
            r2070_infomolestia_id = resp[0][0]
            #print r2070_infomolestia_id

    if 'ideEstab' in dir(evtPgtosDivs.ideBenef.infoPgto):
        for ideEstab in evtPgtosDivs.ideBenef.infoPgto.ideEstab:
            r2070_ideestab_dados = {}
            r2070_ideestab_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs_id
            
            if 'tpInsc' in dir(ideEstab): r2070_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
            if 'nrInsc' in dir(ideEstab): r2070_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
            insert = create_insert('r2070_ideestab', r2070_ideestab_dados)
            resp = executar_sql(insert, True)
            r2070_ideestab_id = resp[0][0]
            #print r2070_ideestab_id

            if 'pgtoResidBR' in dir(ideEstab):
                for pgtoResidBR in ideEstab.pgtoResidBR:
                    r2070_pgtoresidbr_dados = {}
                    r2070_pgtoresidbr_dados['r2070_ideestab_id'] = r2070_ideestab_id
                    
                    insert = create_insert('r2070_pgtoresidbr', r2070_pgtoresidbr_dados)
                    resp = executar_sql(insert, True)
                    r2070_pgtoresidbr_id = resp[0][0]
                    #print r2070_pgtoresidbr_id
        
            if 'pgtoResidExt' in dir(ideEstab):
                for pgtoResidExt in ideEstab.pgtoResidExt:
                    r2070_pgtoresidext_dados = {}
                    r2070_pgtoresidext_dados['r2070_ideestab_id'] = r2070_ideestab_id
                    
                    if 'dtPagto' in dir(pgtoResidExt): r2070_pgtoresidext_dados['dtpagto'] = pgtoResidExt.dtPagto.cdata
                    if 'tpRendimento' in dir(pgtoResidExt): r2070_pgtoresidext_dados['tprendimento'] = pgtoResidExt.tpRendimento.cdata
                    if 'formaTributacao' in dir(pgtoResidExt): r2070_pgtoresidext_dados['formatributacao'] = pgtoResidExt.formaTributacao.cdata
                    if 'vlrPgto' in dir(pgtoResidExt): r2070_pgtoresidext_dados['vlrpgto'] = pgtoResidExt.vlrPgto.cdata
                    if 'vlrRet' in dir(pgtoResidExt): r2070_pgtoresidext_dados['vlrret'] = pgtoResidExt.vlrRet.cdata
                    insert = create_insert('r2070_pgtoresidext', r2070_pgtoresidext_dados)
                    resp = executar_sql(insert, True)
                    r2070_pgtoresidext_id = resp[0][0]
                    #print r2070_pgtoresidext_id
        
    return dados