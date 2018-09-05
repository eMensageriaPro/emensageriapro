#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s2298_evtreintegr(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s2298_evtreintegr_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s2298_evtreintegr_dados['status'] = 1
    else:
        s2298_evtreintegr_dados['status'] = 0
    s2298_evtreintegr_dados['versao'] = xmlns[len(xmlns)-1]
    s2298_evtreintegr_dados['identidade'] = doc.eSocial.evtReintegr['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s2298_evtreintegr_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s2298_evtreintegr_dados['processamento_codigo_resposta'] = 1
    evtReintegr = doc.eSocial.evtReintegr
    
    if 'indRetif' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['indretif'] = evtReintegr.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['nrrecibo'] = evtReintegr.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['tpamb'] = evtReintegr.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['procemi'] = evtReintegr.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtReintegr.ideEvento): s2298_evtreintegr_dados['verproc'] = evtReintegr.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtReintegr.ideEmpregador): s2298_evtreintegr_dados['tpinsc'] = evtReintegr.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtReintegr.ideEmpregador): s2298_evtreintegr_dados['nrinsc'] = evtReintegr.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtReintegr.ideVinculo): s2298_evtreintegr_dados['cpftrab'] = evtReintegr.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtReintegr.ideVinculo): s2298_evtreintegr_dados['nistrab'] = evtReintegr.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtReintegr.ideVinculo): s2298_evtreintegr_dados['matricula'] = evtReintegr.ideVinculo.matricula.cdata
    if 'tpReint' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['tpreint'] = evtReintegr.infoReintegr.tpReint.cdata
    if 'nrProcJud' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['nrprocjud'] = evtReintegr.infoReintegr.nrProcJud.cdata
    if 'nrLeiAnistia' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['nrleianistia'] = evtReintegr.infoReintegr.nrLeiAnistia.cdata
    if 'dtEfetRetorno' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['dtefetretorno'] = evtReintegr.infoReintegr.dtEfetRetorno.cdata
    if 'dtEfeito' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['dtefeito'] = evtReintegr.infoReintegr.dtEfeito.cdata
    if 'indPagtoJuizo' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['indpagtojuizo'] = evtReintegr.infoReintegr.indPagtoJuizo.cdata
    if 'inclusao' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['operacao'] = 1
    elif 'alteracao' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['operacao'] = 2
    elif 'exclusao' in dir(evtReintegr.infoReintegr): s2298_evtreintegr_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2298_evtreintegr', s2298_evtreintegr_dados)
    resp = executar_sql(insert, True)
    s2298_evtreintegr_id = resp[0][0]
    dados['evento'] = 's2298'
    dados['identidade'] = s2298_evtreintegr_id
    dados['identidade_evento'] = doc.eSocial.evtReintegr['Id']
    dados['status'] = 1

    from emensageriapro.esocial.views.s2298_evtreintegr_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2298_evtreintegr_id, 'default')
    return dados