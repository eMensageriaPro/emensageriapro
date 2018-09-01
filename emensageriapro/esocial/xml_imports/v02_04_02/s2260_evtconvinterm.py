#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s2260_evtconvinterm(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s2260_evtconvinterm_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s2260_evtconvinterm_dados['status'] = 1
    else:
        s2260_evtconvinterm_dados['status'] = 0
    s2260_evtconvinterm_dados['versao'] = xmlns[len(xmlns)-1]
    s2260_evtconvinterm_dados['identidade'] = doc.eSocial.evtConvInterm['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s2260_evtconvinterm_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s2260_evtconvinterm_dados['processamento_codigo_resposta'] = 1
    evtConvInterm = doc.eSocial.evtConvInterm
    
    if 'indRetif' in dir(evtConvInterm.ideEvento): s2260_evtconvinterm_dados['indretif'] = evtConvInterm.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtConvInterm.ideEvento): s2260_evtconvinterm_dados['nrrecibo'] = evtConvInterm.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtConvInterm.ideEvento): s2260_evtconvinterm_dados['tpamb'] = evtConvInterm.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtConvInterm.ideEvento): s2260_evtconvinterm_dados['procemi'] = evtConvInterm.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtConvInterm.ideEvento): s2260_evtconvinterm_dados['verproc'] = evtConvInterm.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtConvInterm.ideEmpregador): s2260_evtconvinterm_dados['tpinsc'] = evtConvInterm.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtConvInterm.ideEmpregador): s2260_evtconvinterm_dados['nrinsc'] = evtConvInterm.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtConvInterm.ideVinculo): s2260_evtconvinterm_dados['cpftrab'] = evtConvInterm.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtConvInterm.ideVinculo): s2260_evtconvinterm_dados['nistrab'] = evtConvInterm.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtConvInterm.ideVinculo): s2260_evtconvinterm_dados['matricula'] = evtConvInterm.ideVinculo.matricula.cdata
    if 'codConv' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['codconv'] = evtConvInterm.infoConvInterm.codConv.cdata
    if 'dtInicio' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['dtinicio'] = evtConvInterm.infoConvInterm.dtInicio.cdata
    if 'dtFim' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['dtfim'] = evtConvInterm.infoConvInterm.dtFim.cdata
    if 'dtPrevPgto' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['dtprevpgto'] = evtConvInterm.infoConvInterm.dtPrevPgto.cdata
    if 'codHorContrat' in dir(evtConvInterm.infoConvInterm.jornada): s2260_evtconvinterm_dados['codhorcontrat'] = evtConvInterm.infoConvInterm.jornada.codHorContrat.cdata
    if 'dscJornada' in dir(evtConvInterm.infoConvInterm.jornada): s2260_evtconvinterm_dados['dscjornada'] = evtConvInterm.infoConvInterm.jornada.dscJornada.cdata
    if 'indLocal' in dir(evtConvInterm.infoConvInterm.localTrab): s2260_evtconvinterm_dados['indlocal'] = evtConvInterm.infoConvInterm.localTrab.indLocal.cdata
    if 'inclusao' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['operacao'] = 1
    elif 'alteracao' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['operacao'] = 2
    elif 'exclusao' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2260_evtconvinterm', s2260_evtconvinterm_dados)
    resp = executar_sql(insert, True)
    s2260_evtconvinterm_id = resp[0][0]
    dados['evento'] = 's2260'
    dados['identidade'] = s2260_evtconvinterm_id
    dados['identidade_evento'] = doc.eSocial.evtConvInterm['Id']
    dados['status'] = 1

    if 'localTrabInterm' in dir(evtConvInterm.infoConvInterm.localTrab):
        for localTrabInterm in evtConvInterm.infoConvInterm.localTrab.localTrabInterm:
            s2260_localtrabinterm_dados = {}
            s2260_localtrabinterm_dados['s2260_evtconvinterm_id'] = s2260_evtconvinterm_id
            
            if 'tpLograd' in dir(localTrabInterm): s2260_localtrabinterm_dados['tplograd'] = localTrabInterm.tpLograd.cdata
            if 'dscLograd' in dir(localTrabInterm): s2260_localtrabinterm_dados['dsclograd'] = localTrabInterm.dscLograd.cdata
            if 'nrLograd' in dir(localTrabInterm): s2260_localtrabinterm_dados['nrlograd'] = localTrabInterm.nrLograd.cdata
            if 'complem' in dir(localTrabInterm): s2260_localtrabinterm_dados['complem'] = localTrabInterm.complem.cdata
            if 'bairro' in dir(localTrabInterm): s2260_localtrabinterm_dados['bairro'] = localTrabInterm.bairro.cdata
            if 'cep' in dir(localTrabInterm): s2260_localtrabinterm_dados['cep'] = localTrabInterm.cep.cdata
            if 'codMunic' in dir(localTrabInterm): s2260_localtrabinterm_dados['codmunic'] = localTrabInterm.codMunic.cdata
            if 'uf' in dir(localTrabInterm): s2260_localtrabinterm_dados['uf'] = localTrabInterm.uf.cdata
            insert = create_insert('s2260_localtrabinterm', s2260_localtrabinterm_dados)
            resp = executar_sql(insert, True)
            s2260_localtrabinterm_id = resp[0][0]
            #print s2260_localtrabinterm_id

    from emensageriapro.esocial.views.s2260_evtconvinterm_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2260_evtconvinterm_id, 'default')
    return dados