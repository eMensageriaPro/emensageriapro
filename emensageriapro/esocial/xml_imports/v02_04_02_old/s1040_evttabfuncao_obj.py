#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s1040_evttabfuncao_obj(doc):
    s1040_evttabfuncao_dados = {}
    s1040_evttabfuncao_dados['versao'] = 'v02_04_02'
    s1040_evttabfuncao_dados['status'] = 12
    s1040_evttabfuncao_dados['identidade'] = doc.eSocial.evtTabFuncao['Id']
    s1040_evttabfuncao_dados['processamento_codigo_resposta'] = 1
    evtTabFuncao = doc.eSocial.evtTabFuncao
    
    if 'tpAmb' in dir(evtTabFuncao.ideEvento): s1040_evttabfuncao_dados['tpamb'] = evtTabFuncao.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabFuncao.ideEvento): s1040_evttabfuncao_dados['procemi'] = evtTabFuncao.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabFuncao.ideEvento): s1040_evttabfuncao_dados['verproc'] = evtTabFuncao.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabFuncao.ideEmpregador): s1040_evttabfuncao_dados['tpinsc'] = evtTabFuncao.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabFuncao.ideEmpregador): s1040_evttabfuncao_dados['nrinsc'] = evtTabFuncao.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabFuncao.infoFuncao): s1040_evttabfuncao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabFuncao.infoFuncao): s1040_evttabfuncao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabFuncao.infoFuncao): s1040_evttabfuncao_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1040_evttabfuncao', s1040_evttabfuncao_dados)
    resp = executar_sql(insert, True)
    s1040_evttabfuncao_id = resp[0][0]
    dados = s1040_evttabfuncao_dados
    dados['evento'] = 's1040'
    dados['id'] = s1040_evttabfuncao_id
    dados['identidade_evento'] = doc.eSocial.evtTabFuncao['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabFuncao.infoFuncao):
        for inclusao in evtTabFuncao.infoFuncao.inclusao:
            s1040_inclusao_dados = {}
            s1040_inclusao_dados['s1040_evttabfuncao_id'] = s1040_evttabfuncao_id
            
            if 'codFuncao' in dir(inclusao.ideFuncao): s1040_inclusao_dados['codfuncao'] = inclusao.ideFuncao.codFuncao.cdata
            if 'iniValid' in dir(inclusao.ideFuncao): s1040_inclusao_dados['inivalid'] = inclusao.ideFuncao.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideFuncao): s1040_inclusao_dados['fimvalid'] = inclusao.ideFuncao.fimValid.cdata
            if 'dscFuncao' in dir(inclusao.dadosFuncao): s1040_inclusao_dados['dscfuncao'] = inclusao.dadosFuncao.dscFuncao.cdata
            if 'codCBO' in dir(inclusao.dadosFuncao): s1040_inclusao_dados['codcbo'] = inclusao.dadosFuncao.codCBO.cdata
            insert = create_insert('s1040_inclusao', s1040_inclusao_dados)
            resp = executar_sql(insert, True)
            s1040_inclusao_id = resp[0][0]
            #print s1040_inclusao_id

    if 'alteracao' in dir(evtTabFuncao.infoFuncao):
        for alteracao in evtTabFuncao.infoFuncao.alteracao:
            s1040_alteracao_dados = {}
            s1040_alteracao_dados['s1040_evttabfuncao_id'] = s1040_evttabfuncao_id
            
            if 'codFuncao' in dir(alteracao.ideFuncao): s1040_alteracao_dados['codfuncao'] = alteracao.ideFuncao.codFuncao.cdata
            if 'iniValid' in dir(alteracao.ideFuncao): s1040_alteracao_dados['inivalid'] = alteracao.ideFuncao.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideFuncao): s1040_alteracao_dados['fimvalid'] = alteracao.ideFuncao.fimValid.cdata
            if 'dscFuncao' in dir(alteracao.dadosFuncao): s1040_alteracao_dados['dscfuncao'] = alteracao.dadosFuncao.dscFuncao.cdata
            if 'codCBO' in dir(alteracao.dadosFuncao): s1040_alteracao_dados['codcbo'] = alteracao.dadosFuncao.codCBO.cdata
            insert = create_insert('s1040_alteracao', s1040_alteracao_dados)
            resp = executar_sql(insert, True)
            s1040_alteracao_id = resp[0][0]
            #print s1040_alteracao_id

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1040_alteracao_novavalidade_dados = {}
                    s1040_alteracao_novavalidade_dados['s1040_alteracao_id'] = s1040_alteracao_id
                    
                    if 'iniValid' in dir(novaValidade): s1040_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1040_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1040_alteracao_novavalidade', s1040_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1040_alteracao_novavalidade_id = resp[0][0]
                    #print s1040_alteracao_novavalidade_id
        
    if 'exclusao' in dir(evtTabFuncao.infoFuncao):
        for exclusao in evtTabFuncao.infoFuncao.exclusao:
            s1040_exclusao_dados = {}
            s1040_exclusao_dados['s1040_evttabfuncao_id'] = s1040_evttabfuncao_id
            
            if 'codFuncao' in dir(exclusao.ideFuncao): s1040_exclusao_dados['codfuncao'] = exclusao.ideFuncao.codFuncao.cdata
            if 'iniValid' in dir(exclusao.ideFuncao): s1040_exclusao_dados['inivalid'] = exclusao.ideFuncao.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideFuncao): s1040_exclusao_dados['fimvalid'] = exclusao.ideFuncao.fimValid.cdata
            insert = create_insert('s1040_exclusao', s1040_exclusao_dados)
            resp = executar_sql(insert, True)
            s1040_exclusao_id = resp[0][0]
            #print s1040_exclusao_id

    return dados