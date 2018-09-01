#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s1280_evtinfocomplper(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s1280_evtinfocomplper_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s1280_evtinfocomplper_dados['status'] = 1
    else:
        s1280_evtinfocomplper_dados['status'] = 0
    s1280_evtinfocomplper_dados['versao'] = xmlns[len(xmlns)-1]
    s1280_evtinfocomplper_dados['identidade'] = doc.eSocial.evtInfoComplPer['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s1280_evtinfocomplper_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s1280_evtinfocomplper_dados['processamento_codigo_resposta'] = 1
    evtInfoComplPer = doc.eSocial.evtInfoComplPer
    
    if 'indRetif' in dir(evtInfoComplPer.ideEvento): s1280_evtinfocomplper_dados['indretif'] = evtInfoComplPer.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtInfoComplPer.ideEvento): s1280_evtinfocomplper_dados['nrrecibo'] = evtInfoComplPer.ideEvento.nrRecibo.cdata
    if 'indApuracao' in dir(evtInfoComplPer.ideEvento): s1280_evtinfocomplper_dados['indapuracao'] = evtInfoComplPer.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtInfoComplPer.ideEvento): s1280_evtinfocomplper_dados['perapur'] = evtInfoComplPer.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtInfoComplPer.ideEvento): s1280_evtinfocomplper_dados['tpamb'] = evtInfoComplPer.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtInfoComplPer.ideEvento): s1280_evtinfocomplper_dados['procemi'] = evtInfoComplPer.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtInfoComplPer.ideEvento): s1280_evtinfocomplper_dados['verproc'] = evtInfoComplPer.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtInfoComplPer.ideEmpregador): s1280_evtinfocomplper_dados['tpinsc'] = evtInfoComplPer.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtInfoComplPer.ideEmpregador): s1280_evtinfocomplper_dados['nrinsc'] = evtInfoComplPer.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtInfoComplPer.infoAtivConcom): s1280_evtinfocomplper_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInfoComplPer.infoAtivConcom): s1280_evtinfocomplper_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInfoComplPer.infoAtivConcom): s1280_evtinfocomplper_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1280_evtinfocomplper', s1280_evtinfocomplper_dados)
    resp = executar_sql(insert, True)
    s1280_evtinfocomplper_id = resp[0][0]
    dados['evento'] = 's1280'
    dados['identidade'] = s1280_evtinfocomplper_id
    dados['identidade_evento'] = doc.eSocial.evtInfoComplPer['Id']
    dados['status'] = 1

    if 'infoSubstPatr' in dir(evtInfoComplPer):
        for infoSubstPatr in evtInfoComplPer.infoSubstPatr:
            s1280_infosubstpatr_dados = {}
            s1280_infosubstpatr_dados['s1280_evtinfocomplper_id'] = s1280_evtinfocomplper_id
            
            if 'indSubstPatr' in dir(infoSubstPatr): s1280_infosubstpatr_dados['indsubstpatr'] = infoSubstPatr.indSubstPatr.cdata
            if 'percRedContrib' in dir(infoSubstPatr): s1280_infosubstpatr_dados['percredcontrib'] = infoSubstPatr.percRedContrib.cdata
            insert = create_insert('s1280_infosubstpatr', s1280_infosubstpatr_dados)
            resp = executar_sql(insert, True)
            s1280_infosubstpatr_id = resp[0][0]
            #print s1280_infosubstpatr_id

    if 'infoSubstPatrOpPort' in dir(evtInfoComplPer):
        for infoSubstPatrOpPort in evtInfoComplPer.infoSubstPatrOpPort:
            s1280_infosubstpatropport_dados = {}
            s1280_infosubstpatropport_dados['s1280_evtinfocomplper_id'] = s1280_evtinfocomplper_id
            
            if 'cnpjOpPortuario' in dir(infoSubstPatrOpPort): s1280_infosubstpatropport_dados['cnpjopportuario'] = infoSubstPatrOpPort.cnpjOpPortuario.cdata
            insert = create_insert('s1280_infosubstpatropport', s1280_infosubstpatropport_dados)
            resp = executar_sql(insert, True)
            s1280_infosubstpatropport_id = resp[0][0]
            #print s1280_infosubstpatropport_id

    if 'infoAtivConcom' in dir(evtInfoComplPer):
        for infoAtivConcom in evtInfoComplPer.infoAtivConcom:
            s1280_infoativconcom_dados = {}
            s1280_infoativconcom_dados['s1280_evtinfocomplper_id'] = s1280_evtinfocomplper_id
            
            if 'fatorMes' in dir(infoAtivConcom): s1280_infoativconcom_dados['fatormes'] = infoAtivConcom.fatorMes.cdata
            if 'fator13' in dir(infoAtivConcom): s1280_infoativconcom_dados['fator13'] = infoAtivConcom.fator13.cdata
            insert = create_insert('s1280_infoativconcom', s1280_infoativconcom_dados)
            resp = executar_sql(insert, True)
            s1280_infoativconcom_id = resp[0][0]
            #print s1280_infoativconcom_id

    from emensageriapro.esocial.views.s1280_evtinfocomplper_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1280_evtinfocomplper_id, 'default')
    return dados