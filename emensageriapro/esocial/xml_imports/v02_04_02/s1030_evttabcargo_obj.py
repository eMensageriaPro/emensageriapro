#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s1030_evttabcargo_obj(doc):
    s1030_evttabcargo_dados = {}
    s1030_evttabcargo_dados['versao'] = 'v02_04_02'
    s1030_evttabcargo_dados['status'] = 12
    s1030_evttabcargo_dados['identidade'] = doc.eSocial.evtTabCargo['Id']
    s1030_evttabcargo_dados['processamento_codigo_resposta'] = 1
    evtTabCargo = doc.eSocial.evtTabCargo
    
    if 'tpAmb' in dir(evtTabCargo.ideEvento): s1030_evttabcargo_dados['tpamb'] = evtTabCargo.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabCargo.ideEvento): s1030_evttabcargo_dados['procemi'] = evtTabCargo.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabCargo.ideEvento): s1030_evttabcargo_dados['verproc'] = evtTabCargo.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabCargo.ideEmpregador): s1030_evttabcargo_dados['tpinsc'] = evtTabCargo.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabCargo.ideEmpregador): s1030_evttabcargo_dados['nrinsc'] = evtTabCargo.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabCargo.infoCargo): s1030_evttabcargo_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabCargo.infoCargo): s1030_evttabcargo_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabCargo.infoCargo): s1030_evttabcargo_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1030_evttabcargo', s1030_evttabcargo_dados)
    resp = executar_sql(insert, True)
    s1030_evttabcargo_id = resp[0][0]
    dados = s1030_evttabcargo_dados
    dados['evento'] = 's1030'
    dados['id'] = s1030_evttabcargo_id
    dados['identidade_evento'] = doc.eSocial.evtTabCargo['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabCargo.infoCargo):
        for inclusao in evtTabCargo.infoCargo.inclusao:
            s1030_inclusao_dados = {}
            s1030_inclusao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo_id
            
            if 'codCargo' in dir(inclusao.ideCargo): s1030_inclusao_dados['codcargo'] = inclusao.ideCargo.codCargo.cdata
            if 'iniValid' in dir(inclusao.ideCargo): s1030_inclusao_dados['inivalid'] = inclusao.ideCargo.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideCargo): s1030_inclusao_dados['fimvalid'] = inclusao.ideCargo.fimValid.cdata
            if 'nmCargo' in dir(inclusao.dadosCargo): s1030_inclusao_dados['nmcargo'] = inclusao.dadosCargo.nmCargo.cdata
            if 'codCBO' in dir(inclusao.dadosCargo): s1030_inclusao_dados['codcbo'] = inclusao.dadosCargo.codCBO.cdata
            insert = create_insert('s1030_inclusao', s1030_inclusao_dados)
            resp = executar_sql(insert, True)
            s1030_inclusao_id = resp[0][0]
            #print s1030_inclusao_id

            if 'cargoPublico' in dir(inclusao.dadosCargo):
                for cargoPublico in inclusao.dadosCargo.cargoPublico:
                    s1030_inclusao_cargopublico_dados = {}
                    s1030_inclusao_cargopublico_dados['s1030_inclusao_id'] = s1030_inclusao_id
                    
                    if 'acumCargo' in dir(cargoPublico): s1030_inclusao_cargopublico_dados['acumcargo'] = cargoPublico.acumCargo.cdata
                    if 'contagemEsp' in dir(cargoPublico): s1030_inclusao_cargopublico_dados['contagemesp'] = cargoPublico.contagemEsp.cdata
                    if 'dedicExcl' in dir(cargoPublico): s1030_inclusao_cargopublico_dados['dedicexcl'] = cargoPublico.dedicExcl.cdata
                    if 'nrLei' in dir(cargoPublico): s1030_inclusao_cargopublico_dados['nrlei'] = cargoPublico.leiCargo.nrLei.cdata
                    if 'dtLei' in dir(cargoPublico): s1030_inclusao_cargopublico_dados['dtlei'] = cargoPublico.leiCargo.dtLei.cdata
                    if 'sitCargo' in dir(cargoPublico): s1030_inclusao_cargopublico_dados['sitcargo'] = cargoPublico.leiCargo.sitCargo.cdata
                    insert = create_insert('s1030_inclusao_cargopublico', s1030_inclusao_cargopublico_dados)
                    resp = executar_sql(insert, True)
                    s1030_inclusao_cargopublico_id = resp[0][0]
                    #print s1030_inclusao_cargopublico_id
        
    if 'alteracao' in dir(evtTabCargo.infoCargo):
        for alteracao in evtTabCargo.infoCargo.alteracao:
            s1030_alteracao_dados = {}
            s1030_alteracao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo_id
            
            if 'codCargo' in dir(alteracao.ideCargo): s1030_alteracao_dados['codcargo'] = alteracao.ideCargo.codCargo.cdata
            if 'iniValid' in dir(alteracao.ideCargo): s1030_alteracao_dados['inivalid'] = alteracao.ideCargo.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideCargo): s1030_alteracao_dados['fimvalid'] = alteracao.ideCargo.fimValid.cdata
            if 'nmCargo' in dir(alteracao.dadosCargo): s1030_alteracao_dados['nmcargo'] = alteracao.dadosCargo.nmCargo.cdata
            if 'codCBO' in dir(alteracao.dadosCargo): s1030_alteracao_dados['codcbo'] = alteracao.dadosCargo.codCBO.cdata
            insert = create_insert('s1030_alteracao', s1030_alteracao_dados)
            resp = executar_sql(insert, True)
            s1030_alteracao_id = resp[0][0]
            #print s1030_alteracao_id

            if 'cargoPublico' in dir(alteracao.dadosCargo):
                for cargoPublico in alteracao.dadosCargo.cargoPublico:
                    s1030_alteracao_cargopublico_dados = {}
                    s1030_alteracao_cargopublico_dados['s1030_alteracao_id'] = s1030_alteracao_id
                    
                    if 'acumCargo' in dir(cargoPublico): s1030_alteracao_cargopublico_dados['acumcargo'] = cargoPublico.acumCargo.cdata
                    if 'contagemEsp' in dir(cargoPublico): s1030_alteracao_cargopublico_dados['contagemesp'] = cargoPublico.contagemEsp.cdata
                    if 'dedicExcl' in dir(cargoPublico): s1030_alteracao_cargopublico_dados['dedicexcl'] = cargoPublico.dedicExcl.cdata
                    if 'nrLei' in dir(cargoPublico): s1030_alteracao_cargopublico_dados['nrlei'] = cargoPublico.leiCargo.nrLei.cdata
                    if 'dtLei' in dir(cargoPublico): s1030_alteracao_cargopublico_dados['dtlei'] = cargoPublico.leiCargo.dtLei.cdata
                    if 'sitCargo' in dir(cargoPublico): s1030_alteracao_cargopublico_dados['sitcargo'] = cargoPublico.leiCargo.sitCargo.cdata
                    insert = create_insert('s1030_alteracao_cargopublico', s1030_alteracao_cargopublico_dados)
                    resp = executar_sql(insert, True)
                    s1030_alteracao_cargopublico_id = resp[0][0]
                    #print s1030_alteracao_cargopublico_id
        
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1030_alteracao_novavalidade_dados = {}
                    s1030_alteracao_novavalidade_dados['s1030_alteracao_id'] = s1030_alteracao_id
                    
                    if 'iniValid' in dir(novaValidade): s1030_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1030_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1030_alteracao_novavalidade', s1030_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1030_alteracao_novavalidade_id = resp[0][0]
                    #print s1030_alteracao_novavalidade_id
        
    if 'exclusao' in dir(evtTabCargo.infoCargo):
        for exclusao in evtTabCargo.infoCargo.exclusao:
            s1030_exclusao_dados = {}
            s1030_exclusao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo_id
            
            if 'codCargo' in dir(exclusao.ideCargo): s1030_exclusao_dados['codcargo'] = exclusao.ideCargo.codCargo.cdata
            if 'iniValid' in dir(exclusao.ideCargo): s1030_exclusao_dados['inivalid'] = exclusao.ideCargo.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideCargo): s1030_exclusao_dados['fimvalid'] = exclusao.ideCargo.fimValid.cdata
            insert = create_insert('s1030_exclusao', s1030_exclusao_dados)
            resp = executar_sql(insert, True)
            s1030_exclusao_id = resp[0][0]
            #print s1030_exclusao_id

    return dados