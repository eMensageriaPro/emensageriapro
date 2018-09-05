#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r9000_evtexclusao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    r9000_evtexclusao_dados = {}
    xmlns = doc.Reinf['xmlns'].split('/')
    if validar:
        r9000_evtexclusao_dados['status'] = 1
    else:
        r9000_evtexclusao_dados['status'] = 0
    r9000_evtexclusao_dados['versao'] = xmlns[len(xmlns)-1]
    r9000_evtexclusao_dados['identidade'] = doc.Reinf.evtExclusao['id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_efdreinf WHERE identidade = '%s';
    #     """ % r9000_evtexclusao_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    #r9000_evtexclusao_dados['processamento_codigo_resposta'] = 1
    evtExclusao = doc.Reinf.evtExclusao
    
    if 'tpAmb' in dir(evtExclusao.ideEvento): r9000_evtexclusao_dados['tpamb'] = evtExclusao.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtExclusao.ideEvento): r9000_evtexclusao_dados['procemi'] = evtExclusao.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtExclusao.ideEvento): r9000_evtexclusao_dados['verproc'] = evtExclusao.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtExclusao.ideContri): r9000_evtexclusao_dados['tpinsc'] = evtExclusao.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtExclusao.ideContri): r9000_evtexclusao_dados['nrinsc'] = evtExclusao.ideContri.nrInsc.cdata
    if 'tpEvento' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['tpevento'] = evtExclusao.infoExclusao.tpEvento.cdata
    if 'nrRecEvt' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['nrrecevt'] = evtExclusao.infoExclusao.nrRecEvt.cdata
    if 'perApur' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['perapur'] = evtExclusao.infoExclusao.perApur.cdata
    if 'inclusao' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtExclusao.infoExclusao): r9000_evtexclusao_dados['operacao'] = 3
    #print dados
    insert = create_insert('r9000_evtexclusao', r9000_evtexclusao_dados)
    resp = executar_sql(insert, True)
    r9000_evtexclusao_id = resp[0][0]
    dados['evento'] = 'r9000'
    dados['identidade'] = r9000_evtexclusao_id
    dados['identidade_evento'] = doc.Reinf.evtExclusao['id']
    dados['status'] = 1


    from emensageriapro.efdreinf.views.r9000_evtexclusao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r9000_evtexclusao_id, 'default')
    return dados