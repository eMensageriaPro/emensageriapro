#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s1298_evtreabreevper(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s1298_evtreabreevper_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s1298_evtreabreevper_dados['status'] = 1
    else:
        s1298_evtreabreevper_dados['status'] = 0
    s1298_evtreabreevper_dados['versao'] = xmlns[len(xmlns)-1]
    s1298_evtreabreevper_dados['identidade'] = doc.eSocial.evtReabreEvPer['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s1298_evtreabreevper_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s1298_evtreabreevper_dados['processamento_codigo_resposta'] = 1
    evtReabreEvPer = doc.eSocial.evtReabreEvPer
    
    if 'indApuracao' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['indapuracao'] = evtReabreEvPer.ideEvento.indApuracao.cdata
    if 'perApur' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['perapur'] = evtReabreEvPer.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['tpamb'] = evtReabreEvPer.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['procemi'] = evtReabreEvPer.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtReabreEvPer.ideEvento): s1298_evtreabreevper_dados['verproc'] = evtReabreEvPer.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['tpinsc'] = evtReabreEvPer.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['nrinsc'] = evtReabreEvPer.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['operacao'] = 1
    elif 'alteracao' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['operacao'] = 2
    elif 'exclusao' in dir(evtReabreEvPer.ideEmpregador): s1298_evtreabreevper_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1298_evtreabreevper', s1298_evtreabreevper_dados)
    resp = executar_sql(insert, True)
    s1298_evtreabreevper_id = resp[0][0]
    dados['evento'] = 's1298'
    dados['identidade'] = s1298_evtreabreevper_id
    dados['identidade_evento'] = doc.eSocial.evtReabreEvPer['Id']
    dados['status'] = 1

    from emensageriapro.esocial.views.s1298_evtreabreevper_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1298_evtreabreevper_id, 'default')
    return dados