#coding:utf-8
import psycopg2
import datetime
import os
from django.contrib import messages
from emensageriapro.padrao import ler_arquivo, executar_sql



def create_insert(tabela, dados):
    variaveis = dados.keys()
    campos_numericos = executar_sql("""
        SELECT column_name FROM information_schema.columns 
        WHERE table_name ='%s' 
        AND data_type in ('numeric', 'integer');
        """ % tabela, True)
    campos_numericos_lista = []
    for a in campos_numericos:
        campos_numericos_lista.append(a[0])
    valores = ''
    for a in variaveis:
        if dados[a] or dados[a] == 0 or dados[a] == '':
            if (a in campos_numericos_lista):
                valores += "%s, " % str(dados[a]).replace('.','').replace(',','.')
            else:
                valores += "'%s', " % dados[a]
        else:
            valores += "Null, "
    texto = "INSERT INTO public.%s (%s, criado_em, criado_por_id, excluido) VALUES (%s now(), 1, False) RETURNING id;" % (tabela, ', '.join(variaveis), valores)
    return texto


def read_r5001_evttotal(doc, transmissor_lote_id):
    import untangle
    xmlns = doc.Reinf['xmlns'].split('/')
    r5001_evttotal_dados = {}
    r5001_evttotal_dados['transmissor_lote_efdreinf_id'] = transmissor_lote_id
    r5001_evttotal_dados['status'] = 12
    r5001_evttotal_dados['versao'] = xmlns[len(xmlns) - 1]
    r5001_evttotal_dados['identidade'] = doc.Reinf.evtTotal['id']
    evtTotal = doc.Reinf.evtTotal

    r5001_evttotal_dados['perapur'] = evtTotal.ideEvento.perApur.cdata or ''
    if 'tpInsc' in dir(evtTotal.ideContri): r5001_evttotal_dados['tpinsc'] = evtTotal.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtTotal.ideContri): r5001_evttotal_dados['nrinsc'] = evtTotal.ideContri.nrInsc.cdata
    if 'cdRetorno' in dir(evtTotal.ideRecRetorno.ideStatus): r5001_evttotal_dados[
        'cdretorno'] = evtTotal.ideRecRetorno.ideStatus.cdRetorno.cdata
    if 'descRetorno' in dir(evtTotal.ideRecRetorno.ideStatus): r5001_evttotal_dados[
        'descretorno'] = evtTotal.ideRecRetorno.ideStatus.descRetorno.cdata
    if 'nrProtEntr' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['nrprotentr'] = evtTotal.infoRecEv.nrProtEntr.cdata
    if 'dhProcess' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['dhprocess'] = evtTotal.infoRecEv.dhProcess.cdata
    if 'tpEv' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['tpev'] = evtTotal.infoRecEv.tpEv.cdata or ''
    if 'idEv' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['idev'] = evtTotal.infoRecEv.idEv.cdata or ''
    if 'hash' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['hash'] = evtTotal.infoRecEv.hash.cdata or ''
    # print dados
    insert = create_insert('r5001_evttotal', r5001_evttotal_dados)
    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
    resp = executar_sql(insert, True)
    r5001_evttotal_id = resp[0][0]
    r5001_evttotal_dados['evento'] = 'r5001'
    r5001_evttotal_dados['id'] = r5001_evttotal_id
    r5001_evttotal_dados['identidade'] = r5001_evttotal_id
    r5001_evttotal_dados['identidade_evento'] = doc.Reinf.evtTotal['Id']

    if 'regOcorrs' in dir(evtTotal.ideRecRetorno.ideStatus):
        for regOcorrs in evtTotal.ideRecRetorno.ideStatus.regOcorrs:
            r5001_regocorrs_dados = {}
            r5001_regocorrs_dados['r5001_evttotal_id'] = r5001_evttotal_id

            if 'tpOcorr' in dir(regOcorrs): r5001_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            if 'localErroAviso' in dir(regOcorrs): r5001_regocorrs_dados[
                'localerroaviso'] = regOcorrs.localErroAviso.cdata
            if 'codResp' in dir(regOcorrs): r5001_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            if 'dscResp' in dir(regOcorrs): r5001_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            insert = create_insert('r5001_regocorrs', r5001_regocorrs_dados)
            for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
            resp = executar_sql(insert, True)
            r5001_regocorrs_id = resp[0][0]
            # print r5001_regocorrs_id

    if 'infoTotal' in dir(evtTotal):
        for infoTotal in evtTotal.infoTotal:
            r5001_infototal_dados = {}
            r5001_infototal_dados['r5001_evttotal_id'] = r5001_evttotal_id

            if 'nrRecArqBase' in dir(infoTotal): r5001_infototal_dados['nrrecarqbase'] = infoTotal.nrRecArqBase.cdata
            insert = create_insert('r5001_infototal', r5001_infototal_dados)
            for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
            resp = executar_sql(insert, True)
            r5001_infototal_id = resp[0][0]
            # print r5001_infototal_id

            if 'RTom' in dir(infoTotal):
                for RTom in infoTotal.RTom:
                    r5001_rtom_dados = {}
                    r5001_rtom_dados['r5001_infototal_id'] = r5001_infototal_id

                    if 'cnpjPrestador' in dir(RTom): r5001_rtom_dados['cnpjprestador'] = RTom.cnpjPrestador.cdata
                    if 'vlrTotalBaseRet' in dir(RTom): r5001_rtom_dados['vlrtotalbaseret'] = RTom.vlrTotalBaseRet.cdata
                    insert = create_insert('r5001_rtom', r5001_rtom_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5001_rtom_id = resp[0][0]
                    # print r5001_rtom_id

            if 'RPrest' in dir(infoTotal):
                for RPrest in infoTotal.RPrest:
                    r5001_rprest_dados = {}
                    r5001_rprest_dados['r5001_infototal_id'] = r5001_infototal_id

                    if 'tpInscTomador' in dir(RPrest): r5001_rprest_dados['tpinsctomador'] = RPrest.tpInscTomador.cdata
                    if 'nrInscTomador' in dir(RPrest): r5001_rprest_dados['nrinsctomador'] = RPrest.nrInscTomador.cdata
                    if 'vlrTotalBaseRet' in dir(RPrest): r5001_rprest_dados[
                        'vlrtotalbaseret'] = RPrest.vlrTotalBaseRet.cdata
                    if 'vlrTotalRetPrinc' in dir(RPrest): r5001_rprest_dados[
                        'vlrtotalretprinc'] = RPrest.vlrTotalRetPrinc.cdata
                    if 'vlrTotalRetAdic' in dir(RPrest): r5001_rprest_dados[
                        'vlrtotalretadic'] = RPrest.vlrTotalRetAdic.cdata
                    if 'vlrTotalNRetPrinc' in dir(RPrest): r5001_rprest_dados[
                        'vlrtotalnretprinc'] = RPrest.vlrTotalNRetPrinc.cdata
                    if 'vlrTotalNRetAdic' in dir(RPrest): r5001_rprest_dados[
                        'vlrtotalnretadic'] = RPrest.vlrTotalNRetAdic.cdata
                    insert = create_insert('r5001_rprest', r5001_rprest_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5001_rprest_id = resp[0][0]
                    # print r5001_rprest_id

            if 'RRecRepAD' in dir(infoTotal):
                for RRecRepAD in infoTotal.RRecRepAD:
                    r5001_rrecrepad_dados = {}
                    r5001_rrecrepad_dados['r5001_infototal_id'] = r5001_infototal_id

                    if 'cnpjAssocDesp' in dir(RRecRepAD): r5001_rrecrepad_dados[
                        'cnpjassocdesp'] = RRecRepAD.cnpjAssocDesp.cdata
                    if 'vlrTotalRep' in dir(RRecRepAD): r5001_rrecrepad_dados[
                        'vlrtotalrep'] = RRecRepAD.vlrTotalRep.cdata
                    if 'CRRecRepAD' in dir(RRecRepAD): r5001_rrecrepad_dados['crrecrepad'] = RRecRepAD.CRRecRepAD.cdata
                    if 'vlrCRRecRepAD' in dir(RRecRepAD): r5001_rrecrepad_dados[
                        'vlrcrrecrepad'] = RRecRepAD.vlrCRRecRepAD.cdata
                    if 'vlrCRRecRepADSusp' in dir(RRecRepAD): r5001_rrecrepad_dados[
                        'vlrcrrecrepadsusp'] = RRecRepAD.vlrCRRecRepADSusp.cdata
                    insert = create_insert('r5001_rrecrepad', r5001_rrecrepad_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5001_rrecrepad_id = resp[0][0]
                    # print r5001_rrecrepad_id

            if 'RComl' in dir(infoTotal):
                for RComl in infoTotal.RComl:
                    r5001_rcoml_dados = {}
                    r5001_rcoml_dados['r5001_infototal_id'] = r5001_infototal_id

                    if 'CRComl' in dir(RComl): r5001_rcoml_dados['crcoml'] = RComl.CRComl.cdata
                    if 'vlrCRComl' in dir(RComl): r5001_rcoml_dados['vlrcrcoml'] = RComl.vlrCRComl.cdata
                    if 'vlrCRComlSusp' in dir(RComl): r5001_rcoml_dados['vlrcrcomlsusp'] = RComl.vlrCRComlSusp.cdata
                    insert = create_insert('r5001_rcoml', r5001_rcoml_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5001_rcoml_id = resp[0][0]
                    # print r5001_rcoml_id

            if 'RCPRB' in dir(infoTotal):
                for RCPRB in infoTotal.RCPRB:
                    r5001_rcprb_dados = {}
                    r5001_rcprb_dados['r5001_infototal_id'] = r5001_infototal_id

                    if 'CRCPRB' in dir(RCPRB): r5001_rcprb_dados['crcprb'] = RCPRB.CRCPRB.cdata
                    if 'vlrCRCPRB' in dir(RCPRB): r5001_rcprb_dados['vlrcrcprb'] = RCPRB.vlrCRCPRB.cdata
                    if 'vlrCRCPRBSusp' in dir(RCPRB): r5001_rcprb_dados['vlrcrcprbsusp'] = RCPRB.vlrCRCPRBSusp.cdata
                    insert = create_insert('r5001_rcprb', r5001_rcprb_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5001_rcprb_id = resp[0][0]
                    # print r5001_rcprb_id

            if 'RRecEspetDesp' in dir(infoTotal):
                for RRecEspetDesp in infoTotal.RRecEspetDesp:
                    r5001_rrecespetdesp_dados = {}
                    r5001_rrecespetdesp_dados['r5001_infototal_id'] = r5001_infototal_id

                    if 'CRRecEspetDesp' in dir(RRecEspetDesp): r5001_rrecespetdesp_dados[
                        'crrecespetdesp'] = RRecEspetDesp.CRRecEspetDesp.cdata
                    if 'vlrReceitaTotal' in dir(RRecEspetDesp): r5001_rrecespetdesp_dados[
                        'vlrreceitatotal'] = RRecEspetDesp.vlrReceitaTotal.cdata
                    if 'vlrCRRecEspetDesp' in dir(RRecEspetDesp): r5001_rrecespetdesp_dados[
                        'vlrcrrecespetdesp'] = RRecEspetDesp.vlrCRRecEspetDesp.cdata
                    if 'vlrCRRecEspetDespSusp' in dir(RRecEspetDesp): r5001_rrecespetdesp_dados[
                        'vlrcrrecespetdespsusp'] = RRecEspetDesp.vlrCRRecEspetDespSusp.cdata
                    insert = create_insert('r5001_rrecespetdesp', r5001_rrecespetdesp_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5001_rrecespetdesp_id = resp[0][0]
                    # print r5001_rrecespetdesp_id
    return r5001_evttotal_dados



def read_r5011_evttotalcontrib(doc, transmissor_lote_id):
    import untangle
    r5011_evttotalcontrib_dados = {}
    xmlns = doc.Reinf['xmlns'].split('/')
    r5011_evttotalcontrib_dados['transmissor_lote_efdreinf_id'] = transmissor_lote_id
    r5011_evttotalcontrib_dados['status'] = 12
    r5011_evttotalcontrib_dados['versao'] = xmlns[len(xmlns) - 1]
    r5011_evttotalcontrib_dados['identidade'] = doc.Reinf.evtTotalContrib['id']
    evtTotalContrib = doc.Reinf.evtTotalContrib

    if 'perApur' in dir(evtTotalContrib.ideEvento):
        r5011_evttotalcontrib_dados['perapur'] = evtTotalContrib.ideEvento.perApur.cdata or '-'
    else:
        r5011_evttotalcontrib_dados['perapur'] = '-'
    if 'tpInsc' in dir(evtTotalContrib.ideContri): r5011_evttotalcontrib_dados[
        'tpinsc'] = evtTotalContrib.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtTotalContrib.ideContri): r5011_evttotalcontrib_dados[
        'nrinsc'] = evtTotalContrib.ideContri.nrInsc.cdata
    if 'cdRetorno' in dir(evtTotalContrib.ideRecRetorno.ideStatus): r5011_evttotalcontrib_dados[
        'cdretorno'] = evtTotalContrib.ideRecRetorno.ideStatus.cdRetorno.cdata
    if 'descRetorno' in dir(evtTotalContrib.ideRecRetorno.ideStatus): r5011_evttotalcontrib_dados[
        'descretorno'] = evtTotalContrib.ideRecRetorno.ideStatus.descRetorno.cdata
    if 'nrProtEntr' in dir(evtTotalContrib.infoRecEv):
        r5011_evttotalcontrib_dados['nrprotentr'] = evtTotalContrib.infoRecEv.nrProtEntr.cdata or '-'
    else:
        r5011_evttotalcontrib_dados['nrprotentr'] = '-'
    if 'dhProcess' in dir(evtTotalContrib.infoRecEv):
        r5011_evttotalcontrib_dados['dhprocess'] = evtTotalContrib.infoRecEv.dhProcess.cdata
    if 'tpEv' in dir(evtTotalContrib.infoRecEv):
        r5011_evttotalcontrib_dados['tpev'] = evtTotalContrib.infoRecEv.tpEv.cdata
    if 'idEv' in dir(evtTotalContrib.infoRecEv):
        r5011_evttotalcontrib_dados['idev'] = evtTotalContrib.infoRecEv.idEv.cdata
    if 'hash' in dir(evtTotalContrib.infoRecEv):
        r5011_evttotalcontrib_dados['hash'] = evtTotalContrib.infoRecEv.hash.cdata

    # print dados
    insert = create_insert('r5011_evttotalcontrib', r5011_evttotalcontrib_dados)
    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
    resp = executar_sql(insert, True)
    r5011_evttotalcontrib_id = resp[0][0]
    r5011_evttotalcontrib_dados['evento'] = 'r5011'
    r5011_evttotalcontrib_dados['id'] = r5011_evttotalcontrib_id
    r5011_evttotalcontrib_dados['identidade'] = r5011_evttotalcontrib_id
    r5011_evttotalcontrib_dados['identidade_evento'] = doc.Reinf.evtTotalContrib['Id']
    r5011_evttotalcontrib_dados['status'] = 12

    if 'regOcorrs' in dir(evtTotalContrib.ideRecRetorno.ideStatus):
        for regOcorrs in evtTotalContrib.ideRecRetorno.ideStatus.regOcorrs:
            r5011_regocorrs_dados = {}
            r5011_regocorrs_dados['r5011_evttotalcontrib_id'] = r5011_evttotalcontrib_id

            if 'tpOcorr' in dir(regOcorrs): r5011_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            if 'localErroAviso' in dir(regOcorrs): r5011_regocorrs_dados[
                'localerroaviso'] = regOcorrs.localErroAviso.cdata
            if 'codResp' in dir(regOcorrs): r5011_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            if 'dscResp' in dir(regOcorrs): r5011_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            insert = create_insert('r5011_regocorrs', r5011_regocorrs_dados)
            for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
            resp = executar_sql(insert, True)
            r5011_regocorrs_id = resp[0][0]
            # print r5011_regocorrs_id

    if 'infoTotalContrib' in dir(evtTotalContrib):
        for infoTotalContrib in evtTotalContrib.infoTotalContrib:
            r5011_infototalcontrib_dados = {}
            r5011_infototalcontrib_dados['r5011_evttotalcontrib_id'] = r5011_evttotalcontrib_id

            if 'nrRecArqBase' in dir(infoTotalContrib): r5011_infototalcontrib_dados[
                'nrrecarqbase'] = infoTotalContrib.nrRecArqBase.cdata
            if 'indExistInfo' in dir(infoTotalContrib): r5011_infototalcontrib_dados[
                'indexistinfo'] = infoTotalContrib.indExistInfo.cdata
            insert = create_insert('r5011_infototalcontrib', r5011_infototalcontrib_dados)
            for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
            resp = executar_sql(insert, True)
            r5011_infototalcontrib_id = resp[0][0]
            # print r5011_infototalcontrib_id

            if 'RTom' in dir(infoTotalContrib):
                for RTom in infoTotalContrib.RTom:
                    r5011_rtom_dados = {}
                    r5011_rtom_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'cnpjPrestador' in dir(RTom): r5011_rtom_dados['cnpjprestador'] = RTom.cnpjPrestador.cdata
                    if 'vlrTotalBaseRet' in dir(RTom): r5011_rtom_dados['vlrtotalbaseret'] = RTom.vlrTotalBaseRet.cdata
                    insert = create_insert('r5011_rtom', r5011_rtom_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5011_rtom_id = resp[0][0]
                    # print r5011_rtom_id

            if 'RPrest' in dir(infoTotalContrib):
                for RPrest in infoTotalContrib.RPrest:
                    r5011_rprest_dados = {}
                    r5011_rprest_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'tpInscTomador' in dir(RPrest): r5011_rprest_dados['tpinsctomador'] = RPrest.tpInscTomador.cdata
                    if 'nrInscTomador' in dir(RPrest): r5011_rprest_dados['nrinsctomador'] = RPrest.nrInscTomador.cdata
                    if 'vlrTotalBaseRet' in dir(RPrest): r5011_rprest_dados[
                        'vlrtotalbaseret'] = RPrest.vlrTotalBaseRet.cdata
                    if 'vlrTotalRetPrinc' in dir(RPrest): r5011_rprest_dados[
                        'vlrtotalretprinc'] = RPrest.vlrTotalRetPrinc.cdata
                    if 'vlrTotalRetAdic' in dir(RPrest): r5011_rprest_dados[
                        'vlrtotalretadic'] = RPrest.vlrTotalRetAdic.cdata
                    if 'vlrTotalNRetPrinc' in dir(RPrest): r5011_rprest_dados[
                        'vlrtotalnretprinc'] = RPrest.vlrTotalNRetPrinc.cdata
                    if 'vlrTotalNRetAdic' in dir(RPrest): r5011_rprest_dados[
                        'vlrtotalnretadic'] = RPrest.vlrTotalNRetAdic.cdata
                    insert = create_insert('r5011_rprest', r5011_rprest_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5011_rprest_id = resp[0][0]
                    # print r5011_rprest_id

            if 'RRecRepAD' in dir(infoTotalContrib):
                for RRecRepAD in infoTotalContrib.RRecRepAD:
                    r5011_rrecrepad_dados = {}
                    r5011_rrecrepad_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'cnpjAssocDesp' in dir(RRecRepAD): r5011_rrecrepad_dados[
                        'cnpjassocdesp'] = RRecRepAD.cnpjAssocDesp.cdata
                    if 'vlrTotalRep' in dir(RRecRepAD): r5011_rrecrepad_dados[
                        'vlrtotalrep'] = RRecRepAD.vlrTotalRep.cdata
                    if 'CRRecRepAD' in dir(RRecRepAD): r5011_rrecrepad_dados['crrecrepad'] = RRecRepAD.CRRecRepAD.cdata
                    if 'vlrCRRecRepAD' in dir(RRecRepAD): r5011_rrecrepad_dados[
                        'vlrcrrecrepad'] = RRecRepAD.vlrCRRecRepAD.cdata
                    if 'vlrCRRecRepADSusp' in dir(RRecRepAD): r5011_rrecrepad_dados[
                        'vlrcrrecrepadsusp'] = RRecRepAD.vlrCRRecRepADSusp.cdata
                    insert = create_insert('r5011_rrecrepad', r5011_rrecrepad_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5011_rrecrepad_id = resp[0][0]
                    # print r5011_rrecrepad_id

            if 'RComl' in dir(infoTotalContrib):
                for RComl in infoTotalContrib.RComl:
                    r5011_rcoml_dados = {}
                    r5011_rcoml_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'CRComl' in dir(RComl): r5011_rcoml_dados['crcoml'] = RComl.CRComl.cdata
                    if 'vlrCRComl' in dir(RComl): r5011_rcoml_dados['vlrcrcoml'] = RComl.vlrCRComl.cdata
                    if 'vlrCRComlSusp' in dir(RComl): r5011_rcoml_dados['vlrcrcomlsusp'] = RComl.vlrCRComlSusp.cdata
                    insert = create_insert('r5011_rcoml', r5011_rcoml_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5011_rcoml_id = resp[0][0]
                    # print r5011_rcoml_id

            if 'RCPRB' in dir(infoTotalContrib):
                for RCPRB in infoTotalContrib.RCPRB:
                    r5011_rcprb_dados = {}
                    r5011_rcprb_dados['r5011_infototalcontrib_id'] = r5011_infototalcontrib_id

                    if 'CRCPRB' in dir(RCPRB): r5011_rcprb_dados['crcprb'] = RCPRB.CRCPRB.cdata
                    if 'vlrCRCPRB' in dir(RCPRB): r5011_rcprb_dados['vlrcrcprb'] = RCPRB.vlrCRCPRB.cdata
                    if 'vlrCRCPRBSusp' in dir(RCPRB): r5011_rcprb_dados['vlrcrcprbsusp'] = RCPRB.vlrCRCPRBSusp.cdata
                    insert = create_insert('r5011_rcprb', r5011_rcprb_dados)
                    for y in range(5): insert = insert.replace('\n', '').replace('  ', ' ')
                    resp = executar_sql(insert, True)
                    r5011_rcprb_id = resp[0][0]
                    # print r5011_rcprb_id

    return r5011_evttotalcontrib_dados


def read_envioLoteEventos(arquivo, transmissor_lote_id):
    from emensageriapro.funcoes_efdreinf import ler_arquivo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    child = doc.Envelope.Body.ReceberLoteEventosResponse.ReceberLoteEventosResult.Reinf.retornoLoteEventos
    lote = {}
    lote['transmissor_lote_id'] = transmissor_lote_id
    if 'IdTransmissor' in dir(child.ideTransmissor): lote['identidade_transmissor'] = child.ideTransmissor.IdTransmissor.cdata
    if 'cdStatus' in dir(child.status): lote['codigo_status'] = child.status.cdStatus.cdata
    if 'descRetorno' in dir(child.status): lote['retorno_descricao'] = child.status.descRetorno.cdata

    update = """
        UPDATE public.transmissor_lote_efdreinf 
        SET identidade_transmissor='%(identidade_transmissor)s', 
        codigo_status='%(codigo_status)s', 
        retorno_descricao='%(retorno_descricao)s' 
        WHERE id=%(transmissor_lote_id)s;""" % lote
    resp = executar_sql(update, False)
    transmissor_lote_efdreinf_id = transmissor_lote_id

    executar_sql("""
      DELETE FROM public.transmissor_lote_efdreinf_ocorrencias
           WHERE transmissor_lote_efdreinf_id=%s;""" % transmissor_lote_id, False)


    if 'dadosRegistroOcorrenciaLote' in dir(child.status):
        for ocorrencia in child.status.dadosRegistroOcorrenciaLote.ocorrencias:
            lote_ocorrencias = {}
            if 'tipo' in dir(ocorrencia): lote_ocorrencias['tipo'] = ocorrencia.tipo.cdata
            if 'localizacaoErroAviso' in dir(ocorrencia): lote_ocorrencias['localizacao'] = ocorrencia.localizacaoErroAviso.cdata
            if 'codigo' in dir(ocorrencia): lote_ocorrencias['resposta_codigo'] = ocorrencia.codigo.cdata
            if 'descricao' in dir(ocorrencia): lote_ocorrencias['descricao'] = ocorrencia.descricao.cdata
            lote_ocorrencias['transmissor_lote_efdreinf_id'] = transmissor_lote_efdreinf_id

            insert = create_insert('transmissor_lote_efdreinf_ocorrencias', lote_ocorrencias)
            resp = executar_sql(insert, True)

    if 'retornoEventos' in dir(child):
        for evento in child.retornoEventos.evento:
            if 'evtTotal' in dir(evento.Reinf):
                dados = read_r5001_evttotal(evento, transmissor_lote_id)
                evento_identidade = dados['idev']
                evento_dados = executar_sql("""
                    SELECT id, evento, identidade, tabela
                      FROM public.transmissor_eventos_efdreinf WHERE identidade='%s';
                """ % evento_identidade, True)
                if evento_dados:
                    executar_sql("UPDATE public.%s SET retornos_evttotal_id=%s WHERE id=%s;" % (evento_dados[0][3], dados['id'], evento_dados[0][0]), False)
            if 'evtTotalContrib' in dir(evento.Reinf):
                dados = read_r5011_evttotalcontrib(evento, transmissor_lote_id)
                evento_identidade = dados['idev']
                evento_dados = executar_sql("""
                    SELECT id, evento, identidade, tabela
                      FROM public.transmissor_eventos_efdreinf WHERE identidade='%s';
                """ % evento_identidade, True)
                if evento_dados:
                    executar_sql("UPDATE public.%s SET retornos_evttotalcontrib_id=%s WHERE id=%s;" % (evento_dados[0][3], dados['id'], evento_dados[0][0]), False)







def read_consultaLoteEventos(arquivo, transmissor_lote_id):
    from emensageriapro.funcoes_efdreinf import ler_arquivo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    child = doc.Envelope.Body.ConsultaInformacoesConsolidadasResponse.ConsultaInformacoesConsolidadasResult
    lote = {}
    lote['transmissor_lote_id'] = transmissor_lote_id

    if 'evtTotalContrib' in dir(child.Reinf):
        dados = read_r5011_evttotalcontrib(child, transmissor_lote_id)
        evento_identidade = dados['idev']
        evento_dados = executar_sql("""
            SELECT id, evento, identidade, tabela
              FROM public.transmissor_eventos_efdreinf WHERE identidade='%s';
        """ % evento_identidade, True)
        if evento_dados:
            executar_sql("UPDATE public.%s SET retornos_evttotalcontrib_id=%s WHERE id=%s;" % (evento_dados[0][3], dados['id'], evento_dados[0][0]), False)

