#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s1070_evttabprocesso(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s1070_evttabprocesso_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s1070_evttabprocesso_dados['status'] = 1
    else:
        s1070_evttabprocesso_dados['status'] = 0
    s1070_evttabprocesso_dados['versao'] = xmlns[len(xmlns)-1]
    s1070_evttabprocesso_dados['identidade'] = doc.eSocial.evtTabProcesso['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s1070_evttabprocesso_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s1070_evttabprocesso_dados['processamento_codigo_resposta'] = 1
    evtTabProcesso = doc.eSocial.evtTabProcesso
    
    if 'tpAmb' in dir(evtTabProcesso.ideEvento): s1070_evttabprocesso_dados['tpamb'] = evtTabProcesso.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabProcesso.ideEvento): s1070_evttabprocesso_dados['procemi'] = evtTabProcesso.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabProcesso.ideEvento): s1070_evttabprocesso_dados['verproc'] = evtTabProcesso.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabProcesso.ideEmpregador): s1070_evttabprocesso_dados['tpinsc'] = evtTabProcesso.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabProcesso.ideEmpregador): s1070_evttabprocesso_dados['nrinsc'] = evtTabProcesso.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabProcesso.infoProcesso): s1070_evttabprocesso_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1070_evttabprocesso', s1070_evttabprocesso_dados)
    resp = executar_sql(insert, True)
    s1070_evttabprocesso_id = resp[0][0]
    dados['evento'] = 's1070'
    dados['identidade'] = s1070_evttabprocesso_id
    dados['identidade_evento'] = doc.eSocial.evtTabProcesso['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabProcesso.infoProcesso):
        for inclusao in evtTabProcesso.infoProcesso.inclusao:
            s1070_inclusao_dados = {}
            s1070_inclusao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso_id
            
            if 'tpProc' in dir(inclusao.ideProcesso): s1070_inclusao_dados['tpproc'] = inclusao.ideProcesso.tpProc.cdata
            if 'nrProc' in dir(inclusao.ideProcesso): s1070_inclusao_dados['nrproc'] = inclusao.ideProcesso.nrProc.cdata
            if 'iniValid' in dir(inclusao.ideProcesso): s1070_inclusao_dados['inivalid'] = inclusao.ideProcesso.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideProcesso): s1070_inclusao_dados['fimvalid'] = inclusao.ideProcesso.fimValid.cdata
            if 'indAutoria' in dir(inclusao.dadosProc): s1070_inclusao_dados['indautoria'] = inclusao.dadosProc.indAutoria.cdata
            if 'indMatProc' in dir(inclusao.dadosProc): s1070_inclusao_dados['indmatproc'] = inclusao.dadosProc.indMatProc.cdata
            if 'observacao' in dir(inclusao.dadosProc): s1070_inclusao_dados['observacao'] = inclusao.dadosProc.observacao.cdata
            insert = create_insert('s1070_inclusao', s1070_inclusao_dados)
            resp = executar_sql(insert, True)
            s1070_inclusao_id = resp[0][0]
            #print s1070_inclusao_id

            if 'dadosProcJud' in dir(inclusao.dadosProc):
                for dadosProcJud in inclusao.dadosProc.dadosProcJud:
                    s1070_inclusao_dadosprocjud_dados = {}
                    s1070_inclusao_dadosprocjud_dados['s1070_inclusao_id'] = s1070_inclusao_id
                    
                    if 'ufVara' in dir(dadosProcJud): s1070_inclusao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    if 'codMunic' in dir(dadosProcJud): s1070_inclusao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    if 'idVara' in dir(dadosProcJud): s1070_inclusao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    insert = create_insert('s1070_inclusao_dadosprocjud', s1070_inclusao_dadosprocjud_dados)
                    resp = executar_sql(insert, True)
                    s1070_inclusao_dadosprocjud_id = resp[0][0]
                    #print s1070_inclusao_dadosprocjud_id
        
            if 'infoSusp' in dir(inclusao.dadosProc):
                for infoSusp in inclusao.dadosProc.infoSusp:
                    s1070_inclusao_infosusp_dados = {}
                    s1070_inclusao_infosusp_dados['s1070_inclusao_id'] = s1070_inclusao_id
                    
                    if 'codSusp' in dir(infoSusp): s1070_inclusao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    if 'indSusp' in dir(infoSusp): s1070_inclusao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    if 'dtDecisao' in dir(infoSusp): s1070_inclusao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    if 'indDeposito' in dir(infoSusp): s1070_inclusao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    insert = create_insert('s1070_inclusao_infosusp', s1070_inclusao_infosusp_dados)
                    resp = executar_sql(insert, True)
                    s1070_inclusao_infosusp_id = resp[0][0]
                    #print s1070_inclusao_infosusp_id
        
    if 'alteracao' in dir(evtTabProcesso.infoProcesso):
        for alteracao in evtTabProcesso.infoProcesso.alteracao:
            s1070_alteracao_dados = {}
            s1070_alteracao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso_id
            
            if 'tpProc' in dir(alteracao.ideProcesso): s1070_alteracao_dados['tpproc'] = alteracao.ideProcesso.tpProc.cdata
            if 'nrProc' in dir(alteracao.ideProcesso): s1070_alteracao_dados['nrproc'] = alteracao.ideProcesso.nrProc.cdata
            if 'iniValid' in dir(alteracao.ideProcesso): s1070_alteracao_dados['inivalid'] = alteracao.ideProcesso.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideProcesso): s1070_alteracao_dados['fimvalid'] = alteracao.ideProcesso.fimValid.cdata
            if 'indAutoria' in dir(alteracao.dadosProc): s1070_alteracao_dados['indautoria'] = alteracao.dadosProc.indAutoria.cdata
            if 'indMatProc' in dir(alteracao.dadosProc): s1070_alteracao_dados['indmatproc'] = alteracao.dadosProc.indMatProc.cdata
            if 'observacao' in dir(alteracao.dadosProc): s1070_alteracao_dados['observacao'] = alteracao.dadosProc.observacao.cdata
            insert = create_insert('s1070_alteracao', s1070_alteracao_dados)
            resp = executar_sql(insert, True)
            s1070_alteracao_id = resp[0][0]
            #print s1070_alteracao_id

            if 'dadosProcJud' in dir(alteracao.dadosProc):
                for dadosProcJud in alteracao.dadosProc.dadosProcJud:
                    s1070_alteracao_dadosprocjud_dados = {}
                    s1070_alteracao_dadosprocjud_dados['s1070_alteracao_id'] = s1070_alteracao_id
                    
                    if 'ufVara' in dir(dadosProcJud): s1070_alteracao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    if 'codMunic' in dir(dadosProcJud): s1070_alteracao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    if 'idVara' in dir(dadosProcJud): s1070_alteracao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    insert = create_insert('s1070_alteracao_dadosprocjud', s1070_alteracao_dadosprocjud_dados)
                    resp = executar_sql(insert, True)
                    s1070_alteracao_dadosprocjud_id = resp[0][0]
                    #print s1070_alteracao_dadosprocjud_id
        
            if 'infoSusp' in dir(alteracao.dadosProc):
                for infoSusp in alteracao.dadosProc.infoSusp:
                    s1070_alteracao_infosusp_dados = {}
                    s1070_alteracao_infosusp_dados['s1070_alteracao_id'] = s1070_alteracao_id
                    
                    if 'codSusp' in dir(infoSusp): s1070_alteracao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    if 'indSusp' in dir(infoSusp): s1070_alteracao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    if 'dtDecisao' in dir(infoSusp): s1070_alteracao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    if 'indDeposito' in dir(infoSusp): s1070_alteracao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    insert = create_insert('s1070_alteracao_infosusp', s1070_alteracao_infosusp_dados)
                    resp = executar_sql(insert, True)
                    s1070_alteracao_infosusp_id = resp[0][0]
                    #print s1070_alteracao_infosusp_id
        
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1070_alteracao_novavalidade_dados = {}
                    s1070_alteracao_novavalidade_dados['s1070_alteracao_id'] = s1070_alteracao_id
                    
                    if 'iniValid' in dir(novaValidade): s1070_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1070_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1070_alteracao_novavalidade', s1070_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1070_alteracao_novavalidade_id = resp[0][0]
                    #print s1070_alteracao_novavalidade_id
        
    if 'exclusao' in dir(evtTabProcesso.infoProcesso):
        for exclusao in evtTabProcesso.infoProcesso.exclusao:
            s1070_exclusao_dados = {}
            s1070_exclusao_dados['s1070_evttabprocesso_id'] = s1070_evttabprocesso_id
            
            if 'tpProc' in dir(exclusao.ideProcesso): s1070_exclusao_dados['tpproc'] = exclusao.ideProcesso.tpProc.cdata
            if 'nrProc' in dir(exclusao.ideProcesso): s1070_exclusao_dados['nrproc'] = exclusao.ideProcesso.nrProc.cdata
            if 'iniValid' in dir(exclusao.ideProcesso): s1070_exclusao_dados['inivalid'] = exclusao.ideProcesso.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideProcesso): s1070_exclusao_dados['fimvalid'] = exclusao.ideProcesso.fimValid.cdata
            insert = create_insert('s1070_exclusao', s1070_exclusao_dados)
            resp = executar_sql(insert, True)
            s1070_exclusao_id = resp[0][0]
            #print s1070_exclusao_id

    from emensageriapro.esocial.views.s1070_evttabprocesso_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1070_evttabprocesso_id, 'default')
    return dados