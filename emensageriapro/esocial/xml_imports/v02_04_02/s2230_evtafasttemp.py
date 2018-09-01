#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s2230_evtafasttemp(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s2230_evtafasttemp_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s2230_evtafasttemp_dados['status'] = 1
    else:
        s2230_evtafasttemp_dados['status'] = 0
    s2230_evtafasttemp_dados['versao'] = xmlns[len(xmlns)-1]
    s2230_evtafasttemp_dados['identidade'] = doc.eSocial.evtAfastTemp['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s2230_evtafasttemp_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s2230_evtafasttemp_dados['processamento_codigo_resposta'] = 1
    evtAfastTemp = doc.eSocial.evtAfastTemp
    
    if 'indRetif' in dir(evtAfastTemp.ideEvento): s2230_evtafasttemp_dados['indretif'] = evtAfastTemp.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtAfastTemp.ideEvento): s2230_evtafasttemp_dados['nrrecibo'] = evtAfastTemp.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtAfastTemp.ideEvento): s2230_evtafasttemp_dados['tpamb'] = evtAfastTemp.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAfastTemp.ideEvento): s2230_evtafasttemp_dados['procemi'] = evtAfastTemp.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAfastTemp.ideEvento): s2230_evtafasttemp_dados['verproc'] = evtAfastTemp.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAfastTemp.ideEmpregador): s2230_evtafasttemp_dados['tpinsc'] = evtAfastTemp.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAfastTemp.ideEmpregador): s2230_evtafasttemp_dados['nrinsc'] = evtAfastTemp.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtAfastTemp.ideVinculo): s2230_evtafasttemp_dados['cpftrab'] = evtAfastTemp.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtAfastTemp.ideVinculo): s2230_evtafasttemp_dados['nistrab'] = evtAfastTemp.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtAfastTemp.ideVinculo): s2230_evtafasttemp_dados['matricula'] = evtAfastTemp.ideVinculo.matricula.cdata
    if 'codCateg' in dir(evtAfastTemp.ideVinculo): s2230_evtafasttemp_dados['codcateg'] = evtAfastTemp.ideVinculo.codCateg.cdata
    if 'inclusao' in dir(evtAfastTemp.infoAfastamento): s2230_evtafasttemp_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAfastTemp.infoAfastamento): s2230_evtafasttemp_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAfastTemp.infoAfastamento): s2230_evtafasttemp_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2230_evtafasttemp', s2230_evtafasttemp_dados)
    resp = executar_sql(insert, True)
    s2230_evtafasttemp_id = resp[0][0]
    dados['evento'] = 's2230'
    dados['identidade'] = s2230_evtafasttemp_id
    dados['identidade_evento'] = doc.eSocial.evtAfastTemp['Id']
    dados['status'] = 1

    if 'iniAfastamento' in dir(evtAfastTemp.infoAfastamento):
        for iniAfastamento in evtAfastTemp.infoAfastamento.iniAfastamento:
            s2230_iniafastamento_dados = {}
            s2230_iniafastamento_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp_id
            
            if 'dtIniAfast' in dir(iniAfastamento): s2230_iniafastamento_dados['dtiniafast'] = iniAfastamento.dtIniAfast.cdata
            if 'codMotAfast' in dir(iniAfastamento): s2230_iniafastamento_dados['codmotafast'] = iniAfastamento.codMotAfast.cdata
            if 'infoMesmoMtv' in dir(iniAfastamento): s2230_iniafastamento_dados['infomesmomtv'] = iniAfastamento.infoMesmoMtv.cdata
            if 'tpAcidTransito' in dir(iniAfastamento): s2230_iniafastamento_dados['tpacidtransito'] = iniAfastamento.tpAcidTransito.cdata
            if 'observacao' in dir(iniAfastamento): s2230_iniafastamento_dados['observacao'] = iniAfastamento.observacao.cdata
            insert = create_insert('s2230_iniafastamento', s2230_iniafastamento_dados)
            resp = executar_sql(insert, True)
            s2230_iniafastamento_id = resp[0][0]
            #print s2230_iniafastamento_id

            if 'infoAtestado' in dir(iniAfastamento):
                for infoAtestado in iniAfastamento.infoAtestado:
                    s2230_infoatestado_dados = {}
                    s2230_infoatestado_dados['s2230_iniafastamento_id'] = s2230_iniafastamento_id
                    
                    if 'codCID' in dir(infoAtestado): s2230_infoatestado_dados['codcid'] = infoAtestado.codCID.cdata
                    if 'qtdDiasAfast' in dir(infoAtestado): s2230_infoatestado_dados['qtddiasafast'] = infoAtestado.qtdDiasAfast.cdata
                    insert = create_insert('s2230_infoatestado', s2230_infoatestado_dados)
                    resp = executar_sql(insert, True)
                    s2230_infoatestado_id = resp[0][0]
                    #print s2230_infoatestado_id
        
            if 'infoCessao' in dir(iniAfastamento):
                for infoCessao in iniAfastamento.infoCessao:
                    s2230_infocessao_dados = {}
                    s2230_infocessao_dados['s2230_iniafastamento_id'] = s2230_iniafastamento_id
                    
                    if 'cnpjCess' in dir(infoCessao): s2230_infocessao_dados['cnpjcess'] = infoCessao.cnpjCess.cdata
                    if 'infOnus' in dir(infoCessao): s2230_infocessao_dados['infonus'] = infoCessao.infOnus.cdata
                    insert = create_insert('s2230_infocessao', s2230_infocessao_dados)
                    resp = executar_sql(insert, True)
                    s2230_infocessao_id = resp[0][0]
                    #print s2230_infocessao_id
        
            if 'infoMandSind' in dir(iniAfastamento):
                for infoMandSind in iniAfastamento.infoMandSind:
                    s2230_infomandsind_dados = {}
                    s2230_infomandsind_dados['s2230_iniafastamento_id'] = s2230_iniafastamento_id
                    
                    if 'cnpjSind' in dir(infoMandSind): s2230_infomandsind_dados['cnpjsind'] = infoMandSind.cnpjSind.cdata
                    if 'infOnusRemun' in dir(infoMandSind): s2230_infomandsind_dados['infonusremun'] = infoMandSind.infOnusRemun.cdata
                    insert = create_insert('s2230_infomandsind', s2230_infomandsind_dados)
                    resp = executar_sql(insert, True)
                    s2230_infomandsind_id = resp[0][0]
                    #print s2230_infomandsind_id
        
    if 'infoRetif' in dir(evtAfastTemp.infoAfastamento):
        for infoRetif in evtAfastTemp.infoAfastamento.infoRetif:
            s2230_inforetif_dados = {}
            s2230_inforetif_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp_id
            
            if 'origRetif' in dir(infoRetif): s2230_inforetif_dados['origretif'] = infoRetif.origRetif.cdata
            if 'tpProc' in dir(infoRetif): s2230_inforetif_dados['tpproc'] = infoRetif.tpProc.cdata
            if 'nrProc' in dir(infoRetif): s2230_inforetif_dados['nrproc'] = infoRetif.nrProc.cdata
            insert = create_insert('s2230_inforetif', s2230_inforetif_dados)
            resp = executar_sql(insert, True)
            s2230_inforetif_id = resp[0][0]
            #print s2230_inforetif_id

    if 'fimAfastamento' in dir(evtAfastTemp.infoAfastamento):
        for fimAfastamento in evtAfastTemp.infoAfastamento.fimAfastamento:
            s2230_fimafastamento_dados = {}
            s2230_fimafastamento_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp_id
            
            if 'dtTermAfast' in dir(fimAfastamento): s2230_fimafastamento_dados['dttermafast'] = fimAfastamento.dtTermAfast.cdata
            insert = create_insert('s2230_fimafastamento', s2230_fimafastamento_dados)
            resp = executar_sql(insert, True)
            s2230_fimafastamento_id = resp[0][0]
            #print s2230_fimafastamento_id

    from emensageriapro.esocial.views.s2230_evtafasttemp_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2230_evtafasttemp_id, 'default')
    return dados