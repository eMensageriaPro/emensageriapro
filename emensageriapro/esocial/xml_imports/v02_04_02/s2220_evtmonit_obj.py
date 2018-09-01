#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_s2220_evtmonit_obj(doc):
    s2220_evtmonit_dados = {}
    s2220_evtmonit_dados['versao'] = 'v02_04_02'
    s2220_evtmonit_dados['status'] = 12
    s2220_evtmonit_dados['identidade'] = doc.eSocial.evtMonit['Id']
    s2220_evtmonit_dados['processamento_codigo_resposta'] = 1
    evtMonit = doc.eSocial.evtMonit
    
    if 'indRetif' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['indretif'] = evtMonit.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['nrrecibo'] = evtMonit.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['tpamb'] = evtMonit.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['procemi'] = evtMonit.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtMonit.ideEvento): s2220_evtmonit_dados['verproc'] = evtMonit.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtMonit.ideEmpregador): s2220_evtmonit_dados['tpinsc'] = evtMonit.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtMonit.ideEmpregador): s2220_evtmonit_dados['nrinsc'] = evtMonit.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtMonit.ideVinculo): s2220_evtmonit_dados['cpftrab'] = evtMonit.ideVinculo.cpfTrab.cdata
    if 'nisTrab' in dir(evtMonit.ideVinculo): s2220_evtmonit_dados['nistrab'] = evtMonit.ideVinculo.nisTrab.cdata
    if 'matricula' in dir(evtMonit.ideVinculo): s2220_evtmonit_dados['matricula'] = evtMonit.ideVinculo.matricula.cdata
    if 'dtAso' in dir(evtMonit.aso): s2220_evtmonit_dados['dtaso'] = evtMonit.aso.dtAso.cdata
    if 'tpAso' in dir(evtMonit.aso): s2220_evtmonit_dados['tpaso'] = evtMonit.aso.tpAso.cdata
    if 'resAso' in dir(evtMonit.aso): s2220_evtmonit_dados['resaso'] = evtMonit.aso.resAso.cdata
    if 'codCNES' in dir(evtMonit.aso.ideServSaude): s2220_evtmonit_dados['codcnes'] = evtMonit.aso.ideServSaude.codCNES.cdata
    if 'frmCtt' in dir(evtMonit.aso.ideServSaude): s2220_evtmonit_dados['frmctt'] = evtMonit.aso.ideServSaude.frmCtt.cdata
    if 'email' in dir(evtMonit.aso.ideServSaude): s2220_evtmonit_dados['email'] = evtMonit.aso.ideServSaude.email.cdata
    if 'nmMed' in dir(evtMonit.aso.ideServSaude.medico): s2220_evtmonit_dados['nmmed'] = evtMonit.aso.ideServSaude.medico.nmMed.cdata
    if 'inclusao' in dir(evtMonit.aso): s2220_evtmonit_dados['operacao'] = 1
    elif 'alteracao' in dir(evtMonit.aso): s2220_evtmonit_dados['operacao'] = 2
    elif 'exclusao' in dir(evtMonit.aso): s2220_evtmonit_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2220_evtmonit', s2220_evtmonit_dados)
    resp = executar_sql(insert, True)
    s2220_evtmonit_id = resp[0][0]
    dados = s2220_evtmonit_dados
    dados['evento'] = 's2220'
    dados['id'] = s2220_evtmonit_id
    dados['identidade_evento'] = doc.eSocial.evtMonit['Id']
    dados['status'] = 1

    if 'exame' in dir(evtMonit.aso):
        for exame in evtMonit.aso.exame:
            s2220_exame_dados = {}
            s2220_exame_dados['s2220_evtmonit_id'] = s2220_evtmonit_id
            
            if 'dtExm' in dir(exame): s2220_exame_dados['dtexm'] = exame.dtExm.cdata
            if 'procRealizado' in dir(exame): s2220_exame_dados['procrealizado'] = exame.procRealizado.cdata
            if 'obsProc' in dir(exame): s2220_exame_dados['obsproc'] = exame.obsProc.cdata
            if 'interprExm' in dir(exame): s2220_exame_dados['interprexm'] = exame.interprExm.cdata
            if 'ordExame' in dir(exame): s2220_exame_dados['ordexame'] = exame.ordExame.cdata
            if 'dtIniMonit' in dir(exame): s2220_exame_dados['dtinimonit'] = exame.dtIniMonit.cdata
            if 'dtFimMonit' in dir(exame): s2220_exame_dados['dtfimmonit'] = exame.dtFimMonit.cdata
            if 'indResult' in dir(exame): s2220_exame_dados['indresult'] = exame.indResult.cdata
            if 'nisResp' in dir(exame.respMonit): s2220_exame_dados['nisresp'] = exame.respMonit.nisResp.cdata
            if 'nrConsClasse' in dir(exame.respMonit): s2220_exame_dados['nrconsclasse'] = exame.respMonit.nrConsClasse.cdata
            if 'ufConsClasse' in dir(exame.respMonit): s2220_exame_dados['ufconsclasse'] = exame.respMonit.ufConsClasse.cdata
            insert = create_insert('s2220_exame', s2220_exame_dados)
            resp = executar_sql(insert, True)
            s2220_exame_id = resp[0][0]
            #print s2220_exame_id

    return dados