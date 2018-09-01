#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r2099_evtfechaevper(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    r2099_evtfechaevper_dados = {}
    xmlns = doc.Reinf['xmlns'].split('/')
    if validar:
        r2099_evtfechaevper_dados['status'] = 1
    else:
        r2099_evtfechaevper_dados['status'] = 0
    r2099_evtfechaevper_dados['versao'] = xmlns[len(xmlns)-1]
    r2099_evtfechaevper_dados['identidade'] = doc.Reinf.evtFechaEvPer['id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_efdreinf WHERE identidade = '%s';
    #     """ % r2099_evtfechaevper_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    #r2099_evtfechaevper_dados['processamento_codigo_resposta'] = 1
    evtFechaEvPer = doc.Reinf.evtFechaEvPer
    
    if 'perApur' in dir(evtFechaEvPer.ideEvento): r2099_evtfechaevper_dados['perapur'] = evtFechaEvPer.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtFechaEvPer.ideEvento): r2099_evtfechaevper_dados['tpamb'] = evtFechaEvPer.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtFechaEvPer.ideEvento): r2099_evtfechaevper_dados['procemi'] = evtFechaEvPer.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtFechaEvPer.ideEvento): r2099_evtfechaevper_dados['verproc'] = evtFechaEvPer.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtFechaEvPer.ideContri): r2099_evtfechaevper_dados['tpinsc'] = evtFechaEvPer.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtFechaEvPer.ideContri): r2099_evtfechaevper_dados['nrinsc'] = evtFechaEvPer.ideContri.nrInsc.cdata
    if 'evtServTm' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtservtm'] = evtFechaEvPer.infoFech.evtServTm.cdata
    if 'evtServPr' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtservpr'] = evtFechaEvPer.infoFech.evtServPr.cdata
    if 'evtAssDespRec' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtassdesprec'] = evtFechaEvPer.infoFech.evtAssDespRec.cdata
    if 'evtAssDespRep' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtassdesprep'] = evtFechaEvPer.infoFech.evtAssDespRep.cdata
    if 'evtComProd' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtcomprod'] = evtFechaEvPer.infoFech.evtComProd.cdata
    if 'evtCPRB' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtcprb'] = evtFechaEvPer.infoFech.evtCPRB.cdata
    if 'evtPgtos' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['evtpgtos'] = evtFechaEvPer.infoFech.evtPgtos.cdata
    if 'compSemMovto' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['compsemmovto'] = evtFechaEvPer.infoFech.compSemMovto.cdata
    if 'inclusao' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['operacao'] = 1
    elif 'alteracao' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['operacao'] = 2
    elif 'exclusao' in dir(evtFechaEvPer.infoFech): r2099_evtfechaevper_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2099_evtfechaevper', r2099_evtfechaevper_dados)
    resp = executar_sql(insert, True)
    r2099_evtfechaevper_id = resp[0][0]
    dados['evento'] = 'r2099'
    dados['identidade'] = r2099_evtfechaevper_id
    dados['identidade_evento'] = doc.Reinf.evtFechaEvPer['id']
    dados['status'] = 1


    if 'ideRespInf' in dir(evtFechaEvPer):
        for ideRespInf in evtFechaEvPer.ideRespInf:
            r2099_iderespinf_dados = {}
            r2099_iderespinf_dados['r2099_evtfechaevper_id'] = r2099_evtfechaevper_id
            
            if 'nmResp' in dir(ideRespInf): r2099_iderespinf_dados['nmresp'] = ideRespInf.nmResp.cdata
            if 'cpfResp' in dir(ideRespInf): r2099_iderespinf_dados['cpfresp'] = ideRespInf.cpfResp.cdata
            if 'telefone' in dir(ideRespInf): r2099_iderespinf_dados['telefone'] = ideRespInf.telefone.cdata
            if 'email' in dir(ideRespInf): r2099_iderespinf_dados['email'] = ideRespInf.email.cdata
            insert = create_insert('r2099_iderespinf', r2099_iderespinf_dados)
            resp = executar_sql(insert, True)
            r2099_iderespinf_id = resp[0][0]
            #print r2099_iderespinf_id

    from emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2099_evtfechaevper_id, 'default')
    return dados