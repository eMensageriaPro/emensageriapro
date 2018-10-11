#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s3000_evtexclusao(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s3000_evtexclusao_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s3000_evtexclusao_dados['status'] = 1
    else:
        s3000_evtexclusao_dados['status'] = 0
    s3000_evtexclusao_dados['versao'] = xmlns[len(xmlns)-1]
    s3000_evtexclusao_dados['identidade'] = doc.eSocial.evtExclusao['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s3000_evtexclusao_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s3000_evtexclusao_dados['processamento_codigo_resposta'] = 1
    evtExclusao = doc.eSocial.evtExclusao
    
    if 'tpAmb' in dir(evtExclusao.ideEvento): s3000_evtexclusao_dados['tpamb'] = evtExclusao.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtExclusao.ideEvento): s3000_evtexclusao_dados['procemi'] = evtExclusao.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtExclusao.ideEvento): s3000_evtexclusao_dados['verproc'] = evtExclusao.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtExclusao.ideEmpregador): s3000_evtexclusao_dados['tpinsc'] = evtExclusao.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtExclusao.ideEmpregador): s3000_evtexclusao_dados['nrinsc'] = evtExclusao.ideEmpregador.nrInsc.cdata
    if 'tpEvento' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['tpevento'] = evtExclusao.infoExclusao.tpEvento.cdata
    if 'nrRecEvt' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['nrrecevt'] = evtExclusao.infoExclusao.nrRecEvt.cdata
    if 'inclusao' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtExclusao.infoExclusao): s3000_evtexclusao_dados['operacao'] = 3
    #print dados
    insert = create_insert('s3000_evtexclusao', s3000_evtexclusao_dados)
    resp = executar_sql(insert, True)
    s3000_evtexclusao_id = resp[0][0]
    dados['evento'] = 's3000'
    dados['identidade'] = s3000_evtexclusao_id
    dados['identidade_evento'] = doc.eSocial.evtExclusao['Id']
    dados['status'] = 1

    if 'ideTrabalhador' in dir(evtExclusao.infoExclusao):
        for ideTrabalhador in evtExclusao.infoExclusao.ideTrabalhador:
            s3000_idetrabalhador_dados = {}
            s3000_idetrabalhador_dados['s3000_evtexclusao_id'] = s3000_evtexclusao_id
            
            if 'cpfTrab' in dir(ideTrabalhador): s3000_idetrabalhador_dados['cpftrab'] = ideTrabalhador.cpfTrab.cdata
            if 'nisTrab' in dir(ideTrabalhador): s3000_idetrabalhador_dados['nistrab'] = ideTrabalhador.nisTrab.cdata
            insert = create_insert('s3000_idetrabalhador', s3000_idetrabalhador_dados)
            resp = executar_sql(insert, True)
            s3000_idetrabalhador_id = resp[0][0]
            #print s3000_idetrabalhador_id

    if 'ideFolhaPagto' in dir(evtExclusao.infoExclusao):
        for ideFolhaPagto in evtExclusao.infoExclusao.ideFolhaPagto:
            s3000_idefolhapagto_dados = {}
            s3000_idefolhapagto_dados['s3000_evtexclusao_id'] = s3000_evtexclusao_id
            
            if 'indApuracao' in dir(ideFolhaPagto): s3000_idefolhapagto_dados['indapuracao'] = ideFolhaPagto.indApuracao.cdata
            if 'perApur' in dir(ideFolhaPagto): s3000_idefolhapagto_dados['perapur'] = ideFolhaPagto.perApur.cdata
            insert = create_insert('s3000_idefolhapagto', s3000_idefolhapagto_dados)
            resp = executar_sql(insert, True)
            s3000_idefolhapagto_id = resp[0][0]
            #print s3000_idefolhapagto_id

    from emensageriapro.esocial.views.s3000_evtexclusao_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s3000_evtexclusao_id, 'default')
    return dados