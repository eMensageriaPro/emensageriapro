#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s2400_evtcdbenprrp(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s2400_evtcdbenprrp_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s2400_evtcdbenprrp_dados['status'] = 1
    else:
        s2400_evtcdbenprrp_dados['status'] = 0
    s2400_evtcdbenprrp_dados['versao'] = xmlns[len(xmlns)-1]
    s2400_evtcdbenprrp_dados['identidade'] = doc.eSocial.evtCdBenPrRP['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s2400_evtcdbenprrp_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s2400_evtcdbenprrp_dados['processamento_codigo_resposta'] = 1
    evtCdBenPrRP = doc.eSocial.evtCdBenPrRP
    
    if 'indRetif' in dir(evtCdBenPrRP.ideEvento): s2400_evtcdbenprrp_dados['indretif'] = evtCdBenPrRP.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtCdBenPrRP.ideEvento): s2400_evtcdbenprrp_dados['nrrecibo'] = evtCdBenPrRP.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtCdBenPrRP.ideEvento): s2400_evtcdbenprrp_dados['tpamb'] = evtCdBenPrRP.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtCdBenPrRP.ideEvento): s2400_evtcdbenprrp_dados['procemi'] = evtCdBenPrRP.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtCdBenPrRP.ideEvento): s2400_evtcdbenprrp_dados['verproc'] = evtCdBenPrRP.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtCdBenPrRP.ideEmpregador): s2400_evtcdbenprrp_dados['tpinsc'] = evtCdBenPrRP.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtCdBenPrRP.ideEmpregador): s2400_evtcdbenprrp_dados['nrinsc'] = evtCdBenPrRP.ideEmpregador.nrInsc.cdata
    if 'cpfBenef' in dir(evtCdBenPrRP.ideBenef): s2400_evtcdbenprrp_dados['cpfbenef'] = evtCdBenPrRP.ideBenef.cpfBenef.cdata
    if 'nmBenefic' in dir(evtCdBenPrRP.ideBenef): s2400_evtcdbenprrp_dados['nmbenefic'] = evtCdBenPrRP.ideBenef.nmBenefic.cdata
    if 'dtNascto' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): s2400_evtcdbenprrp_dados['dtnascto'] = evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.dtNascto.cdata
    if 'codMunic' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): s2400_evtcdbenprrp_dados['codmunic'] = evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.codMunic.cdata
    if 'uf' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): s2400_evtcdbenprrp_dados['uf'] = evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.uf.cdata
    if 'paisNascto' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): s2400_evtcdbenprrp_dados['paisnascto'] = evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.paisNascto.cdata
    if 'paisNac' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): s2400_evtcdbenprrp_dados['paisnac'] = evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.paisNac.cdata
    if 'nmMae' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): s2400_evtcdbenprrp_dados['nmmae'] = evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.nmMae.cdata
    if 'nmPai' in dir(evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc): s2400_evtcdbenprrp_dados['nmpai'] = evtCdBenPrRP.ideBenef.dadosBenef.dadosNasc.nmPai.cdata
    if 'tpPlanRP' in dir(evtCdBenPrRP.infoBeneficio): s2400_evtcdbenprrp_dados['tpplanrp'] = evtCdBenPrRP.infoBeneficio.tpPlanRP.cdata
    if 'inclusao' in dir(evtCdBenPrRP.infoBeneficio): s2400_evtcdbenprrp_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCdBenPrRP.infoBeneficio): s2400_evtcdbenprrp_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCdBenPrRP.infoBeneficio): s2400_evtcdbenprrp_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2400_evtcdbenprrp', s2400_evtcdbenprrp_dados)
    resp = executar_sql(insert, True)
    s2400_evtcdbenprrp_id = resp[0][0]
    dados['evento'] = 's2400'
    dados['identidade'] = s2400_evtcdbenprrp_id
    dados['identidade_evento'] = doc.eSocial.evtCdBenPrRP['Id']
    dados['status'] = 1

    if 'brasil' in dir(evtCdBenPrRP.ideBenef.dadosBenef.endereco):
        for brasil in evtCdBenPrRP.ideBenef.dadosBenef.endereco.brasil:
            s2400_brasil_dados = {}
            s2400_brasil_dados['s2400_evtcdbenprrp_id'] = s2400_evtcdbenprrp_id
            
            if 'tpLograd' in dir(brasil): s2400_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            if 'dscLograd' in dir(brasil): s2400_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            if 'nrLograd' in dir(brasil): s2400_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            if 'complemento' in dir(brasil): s2400_brasil_dados['complemento'] = brasil.complemento.cdata
            if 'bairro' in dir(brasil): s2400_brasil_dados['bairro'] = brasil.bairro.cdata
            if 'cep' in dir(brasil): s2400_brasil_dados['cep'] = brasil.cep.cdata
            if 'codMunic' in dir(brasil): s2400_brasil_dados['codmunic'] = brasil.codMunic.cdata
            if 'uf' in dir(brasil): s2400_brasil_dados['uf'] = brasil.uf.cdata
            insert = create_insert('s2400_brasil', s2400_brasil_dados)
            resp = executar_sql(insert, True)
            s2400_brasil_id = resp[0][0]
            #print s2400_brasil_id

    if 'exterior' in dir(evtCdBenPrRP.ideBenef.dadosBenef.endereco):
        for exterior in evtCdBenPrRP.ideBenef.dadosBenef.endereco.exterior:
            s2400_exterior_dados = {}
            s2400_exterior_dados['s2400_evtcdbenprrp_id'] = s2400_evtcdbenprrp_id
            
            if 'paisResid' in dir(exterior): s2400_exterior_dados['paisresid'] = exterior.paisResid.cdata
            if 'dscLograd' in dir(exterior): s2400_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            if 'nrLograd' in dir(exterior): s2400_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            if 'complemento' in dir(exterior): s2400_exterior_dados['complemento'] = exterior.complemento.cdata
            if 'bairro' in dir(exterior): s2400_exterior_dados['bairro'] = exterior.bairro.cdata
            if 'nmCid' in dir(exterior): s2400_exterior_dados['nmcid'] = exterior.nmCid.cdata
            if 'codPostal' in dir(exterior): s2400_exterior_dados['codpostal'] = exterior.codPostal.cdata
            insert = create_insert('s2400_exterior', s2400_exterior_dados)
            resp = executar_sql(insert, True)
            s2400_exterior_id = resp[0][0]
            #print s2400_exterior_id

    if 'iniBeneficio' in dir(evtCdBenPrRP.infoBeneficio):
        for iniBeneficio in evtCdBenPrRP.infoBeneficio.iniBeneficio:
            s2400_inibeneficio_dados = {}
            s2400_inibeneficio_dados['s2400_evtcdbenprrp_id'] = s2400_evtcdbenprrp_id
            
            if 'tpBenef' in dir(iniBeneficio): s2400_inibeneficio_dados['tpbenef'] = iniBeneficio.tpBenef.cdata
            if 'nrBenefic' in dir(iniBeneficio): s2400_inibeneficio_dados['nrbenefic'] = iniBeneficio.nrBenefic.cdata
            if 'dtIniBenef' in dir(iniBeneficio): s2400_inibeneficio_dados['dtinibenef'] = iniBeneficio.dtIniBenef.cdata
            if 'vrBenef' in dir(iniBeneficio): s2400_inibeneficio_dados['vrbenef'] = iniBeneficio.vrBenef.cdata
            insert = create_insert('s2400_inibeneficio', s2400_inibeneficio_dados)
            resp = executar_sql(insert, True)
            s2400_inibeneficio_id = resp[0][0]
            #print s2400_inibeneficio_id

            if 'infoPenMorte' in dir(iniBeneficio):
                for infoPenMorte in iniBeneficio.infoPenMorte:
                    s2400_inibeneficio_infopenmorte_dados = {}
                    s2400_inibeneficio_infopenmorte_dados['s2400_inibeneficio_id'] = s2400_inibeneficio_id
                    
                    if 'idQuota' in dir(infoPenMorte): s2400_inibeneficio_infopenmorte_dados['idquota'] = infoPenMorte.idQuota.cdata
                    if 'cpfInst' in dir(infoPenMorte): s2400_inibeneficio_infopenmorte_dados['cpfinst'] = infoPenMorte.cpfInst.cdata
                    insert = create_insert('s2400_inibeneficio_infopenmorte', s2400_inibeneficio_infopenmorte_dados)
                    resp = executar_sql(insert, True)
                    s2400_inibeneficio_infopenmorte_id = resp[0][0]
                    #print s2400_inibeneficio_infopenmorte_id
        
    if 'altBeneficio' in dir(evtCdBenPrRP.infoBeneficio):
        for altBeneficio in evtCdBenPrRP.infoBeneficio.altBeneficio:
            s2400_altbeneficio_dados = {}
            s2400_altbeneficio_dados['s2400_evtcdbenprrp_id'] = s2400_evtcdbenprrp_id
            
            if 'tpBenef' in dir(altBeneficio): s2400_altbeneficio_dados['tpbenef'] = altBeneficio.tpBenef.cdata
            if 'nrBenefic' in dir(altBeneficio): s2400_altbeneficio_dados['nrbenefic'] = altBeneficio.nrBenefic.cdata
            if 'dtIniBenef' in dir(altBeneficio): s2400_altbeneficio_dados['dtinibenef'] = altBeneficio.dtIniBenef.cdata
            if 'vrBenef' in dir(altBeneficio): s2400_altbeneficio_dados['vrbenef'] = altBeneficio.vrBenef.cdata
            insert = create_insert('s2400_altbeneficio', s2400_altbeneficio_dados)
            resp = executar_sql(insert, True)
            s2400_altbeneficio_id = resp[0][0]
            #print s2400_altbeneficio_id

            if 'infoPenMorte' in dir(altBeneficio):
                for infoPenMorte in altBeneficio.infoPenMorte:
                    s2400_altbeneficio_infopenmorte_dados = {}
                    s2400_altbeneficio_infopenmorte_dados['s2400_altbeneficio_id'] = s2400_altbeneficio_id
                    
                    if 'idQuota' in dir(infoPenMorte): s2400_altbeneficio_infopenmorte_dados['idquota'] = infoPenMorte.idQuota.cdata
                    if 'cpfInst' in dir(infoPenMorte): s2400_altbeneficio_infopenmorte_dados['cpfinst'] = infoPenMorte.cpfInst.cdata
                    insert = create_insert('s2400_altbeneficio_infopenmorte', s2400_altbeneficio_infopenmorte_dados)
                    resp = executar_sql(insert, True)
                    s2400_altbeneficio_infopenmorte_id = resp[0][0]
                    #print s2400_altbeneficio_infopenmorte_id
        
    if 'fimBeneficio' in dir(evtCdBenPrRP.infoBeneficio):
        for fimBeneficio in evtCdBenPrRP.infoBeneficio.fimBeneficio:
            s2400_fimbeneficio_dados = {}
            s2400_fimbeneficio_dados['s2400_evtcdbenprrp_id'] = s2400_evtcdbenprrp_id
            
            if 'tpBenef' in dir(fimBeneficio): s2400_fimbeneficio_dados['tpbenef'] = fimBeneficio.tpBenef.cdata
            if 'nrBenefic' in dir(fimBeneficio): s2400_fimbeneficio_dados['nrbenefic'] = fimBeneficio.nrBenefic.cdata
            if 'dtFimBenef' in dir(fimBeneficio): s2400_fimbeneficio_dados['dtfimbenef'] = fimBeneficio.dtFimBenef.cdata
            if 'mtvFim' in dir(fimBeneficio): s2400_fimbeneficio_dados['mtvfim'] = fimBeneficio.mtvFim.cdata
            insert = create_insert('s2400_fimbeneficio', s2400_fimbeneficio_dados)
            resp = executar_sql(insert, True)
            s2400_fimbeneficio_id = resp[0][0]
            #print s2400_fimbeneficio_id

    from emensageriapro.esocial.views.s2400_evtcdbenprrp_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2400_evtcdbenprrp_id, 'default')
    return dados