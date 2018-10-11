#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s1299_evtfechaevper(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s1299_evtfechaevper_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s1299_evtfechaevper_dados['status'] = 1
    else:
        s1299_evtfechaevper_dados['status'] = 0
    s1299_evtfechaevper_dados['versao'] = xmlns[len(xmlns)-1]
    s1299_evtfechaevper_dados['identidade'] = doc.eSocial.evtFechaEvPer['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s1299_evtfechaevper_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s1299_evtfechaevper_dados['processamento_codigo_resposta'] = 1
    evtFechaEvPer = doc.eSocial.evtFechaEvPer
    
    if 'indApuracao' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['indapuracao'] = evtFechaEvPer.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['perapur'] = evtFechaEvPer.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['tpamb'] = evtFechaEvPer.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['procemi'] = evtFechaEvPer.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtFechaEvPer.ideEvento): s1299_evtfechaevper_dados['verproc'] = evtFechaEvPer.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtFechaEvPer.ideEmpregador): s1299_evtfechaevper_dados['tpinsc'] = evtFechaEvPer.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtFechaEvPer.ideEmpregador): s1299_evtfechaevper_dados['nrinsc'] = evtFechaEvPer.ideEmpregador.nrInsc.cdata
    if 'evtRemun' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtremun'] = evtFechaEvPer.infoFech.evtRemun.cdata
    if 'evtPgtos' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtpgtos'] = evtFechaEvPer.infoFech.evtPgtos.cdata
    if 'evtAqProd' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtaqprod'] = evtFechaEvPer.infoFech.evtAqProd.cdata
    if 'evtComProd' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtcomprod'] = evtFechaEvPer.infoFech.evtComProd.cdata
    if 'evtContratAvNP' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtcontratavnp'] = evtFechaEvPer.infoFech.evtContratAvNP.cdata
    if 'evtInfoComplPer' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['evtinfocomplper'] = evtFechaEvPer.infoFech.evtInfoComplPer.cdata
    if 'compSemMovto' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['compsemmovto'] = evtFechaEvPer.infoFech.compSemMovto.cdata
    if 'inclusao' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['operacao'] = 1
    elif 'alteracao' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['operacao'] = 2
    elif 'exclusao' in dir(evtFechaEvPer.infoFech): s1299_evtfechaevper_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1299_evtfechaevper', s1299_evtfechaevper_dados)
    resp = executar_sql(insert, True)
    s1299_evtfechaevper_id = resp[0][0]
    dados['evento'] = 's1299'
    dados['identidade'] = s1299_evtfechaevper_id
    dados['identidade_evento'] = doc.eSocial.evtFechaEvPer['Id']
    dados['status'] = 1

    if 'ideRespInf' in dir(evtFechaEvPer):
        for ideRespInf in evtFechaEvPer.ideRespInf:
            s1299_iderespinf_dados = {}
            s1299_iderespinf_dados['s1299_evtfechaevper_id'] = s1299_evtfechaevper_id
            
            if 'nmResp' in dir(ideRespInf): s1299_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            if 'cpfResp' in dir(ideRespInf): s1299_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            if 'telefone' in dir(ideRespInf): s1299_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            if 'email' in dir(ideRespInf): s1299_iderespinf_dados['email'] = ideRespInf.email.cdata
            insert = create_insert('s1299_iderespinf', s1299_iderespinf_dados)
            resp = executar_sql(insert, True)
            s1299_iderespinf_id = resp[0][0]
            #print s1299_iderespinf_id

    from emensageriapro.esocial.views.s1299_evtfechaevper_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1299_evtfechaevper_id, 'default')
    return dados