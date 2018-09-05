#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s2190_evtadmprelim(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s2190_evtadmprelim_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s2190_evtadmprelim_dados['status'] = 1
    else:
        s2190_evtadmprelim_dados['status'] = 0
    s2190_evtadmprelim_dados['versao'] = xmlns[len(xmlns)-1]
    s2190_evtadmprelim_dados['identidade'] = doc.eSocial.evtAdmPrelim['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s2190_evtadmprelim_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s2190_evtadmprelim_dados['processamento_codigo_resposta'] = 1
    evtAdmPrelim = doc.eSocial.evtAdmPrelim
    
    if 'tpAmb' in dir(evtAdmPrelim.ideEvento): s2190_evtadmprelim_dados['tpamb'] = evtAdmPrelim.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtAdmPrelim.ideEvento): s2190_evtadmprelim_dados['procemi'] = evtAdmPrelim.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtAdmPrelim.ideEvento): s2190_evtadmprelim_dados['verproc'] = evtAdmPrelim.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtAdmPrelim.ideEmpregador): s2190_evtadmprelim_dados['tpinsc'] = evtAdmPrelim.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtAdmPrelim.ideEmpregador): s2190_evtadmprelim_dados['nrinsc'] = evtAdmPrelim.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['cpftrab'] = evtAdmPrelim.infoRegPrelim.cpfTrab.cdata
    if 'dtNascto' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['dtnascto'] = evtAdmPrelim.infoRegPrelim.dtNascto.cdata
    if 'dtAdm' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['dtadm'] = evtAdmPrelim.infoRegPrelim.dtAdm.cdata
    if 'inclusao' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['operacao'] = 1
    elif 'alteracao' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['operacao'] = 2
    elif 'exclusao' in dir(evtAdmPrelim.infoRegPrelim): s2190_evtadmprelim_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2190_evtadmprelim', s2190_evtadmprelim_dados)
    resp = executar_sql(insert, True)
    s2190_evtadmprelim_id = resp[0][0]
    dados['evento'] = 's2190'
    dados['identidade'] = s2190_evtadmprelim_id
    dados['identidade_evento'] = doc.eSocial.evtAdmPrelim['Id']
    dados['status'] = 1

    from emensageriapro.esocial.views.s2190_evtadmprelim_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2190_evtadmprelim_id, 'default')
    return dados