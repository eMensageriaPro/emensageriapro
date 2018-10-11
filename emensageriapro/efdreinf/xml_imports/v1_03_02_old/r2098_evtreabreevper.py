#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r2098_evtreabreevper(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    r2098_evtreabreevper_dados = {}
    xmlns = doc.Reinf['xmlns'].split('/')
    if validar:
        r2098_evtreabreevper_dados['status'] = 1
    else:
        r2098_evtreabreevper_dados['status'] = 0
    r2098_evtreabreevper_dados['versao'] = xmlns[len(xmlns)-1]
    r2098_evtreabreevper_dados['identidade'] = doc.Reinf.evtReabreEvPer['id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_efdreinf WHERE identidade = '%s';
    #     """ % r2098_evtreabreevper_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    #r2098_evtreabreevper_dados['processamento_codigo_resposta'] = 1
    evtReabreEvPer = doc.Reinf.evtReabreEvPer
    
    if 'perApur' in dir(evtReabreEvPer.ideEvento): r2098_evtreabreevper_dados['perapur'] = evtReabreEvPer.ideEvento.perApur.cdata
    if 'tpAmb' in dir(evtReabreEvPer.ideEvento): r2098_evtreabreevper_dados['tpamb'] = evtReabreEvPer.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtReabreEvPer.ideEvento): r2098_evtreabreevper_dados['procemi'] = evtReabreEvPer.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtReabreEvPer.ideEvento): r2098_evtreabreevper_dados['verproc'] = evtReabreEvPer.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtReabreEvPer.ideContri): r2098_evtreabreevper_dados['tpinsc'] = evtReabreEvPer.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtReabreEvPer.ideContri): r2098_evtreabreevper_dados['nrinsc'] = evtReabreEvPer.ideContri.nrInsc.cdata
    if 'inclusao' in dir(evtReabreEvPer.ideContri): r2098_evtreabreevper_dados['operacao'] = 1
    elif 'alteracao' in dir(evtReabreEvPer.ideContri): r2098_evtreabreevper_dados['operacao'] = 2
    elif 'exclusao' in dir(evtReabreEvPer.ideContri): r2098_evtreabreevper_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2098_evtreabreevper', r2098_evtreabreevper_dados)
    resp = executar_sql(insert, True)
    r2098_evtreabreevper_id = resp[0][0]
    dados['evento'] = 'r2098'
    dados['identidade'] = r2098_evtreabreevper_id
    dados['identidade_evento'] = doc.Reinf.evtReabreEvPer['id']
    dados['status'] = 1


    from emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2098_evtreabreevper_id, 'default')
    return dados