#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2220_evtmonit(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtMonit = doc.eSocial.evtMonit
    
    if 'indRetif' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.indRetif', evtMonit.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.nrRecibo', evtMonit.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.tpAmb', evtMonit.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.procEmi', evtMonit.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtMonit.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEvento.verProc', evtMonit.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtMonit.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEmpregador.tpInsc', evtMonit.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtMonit.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideEmpregador.nrInsc', evtMonit.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtMonit.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideVinculo.cpfTrab', evtMonit.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtMonit.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideVinculo.nisTrab', evtMonit.ideVinculo.nisTrab.cdata, 0, '')
    if 'matricula' in dir(evtMonit.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.ideVinculo.matricula', evtMonit.ideVinculo.matricula.cdata, 0, '')
    if 'dtAso' in dir(evtMonit.aso): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.aso.dtAso', evtMonit.aso.dtAso.cdata, 1, '')
    if 'tpAso' in dir(evtMonit.aso): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.aso.tpAso', evtMonit.aso.tpAso.cdata, 1, '0;1;2;3;4;8')
    if 'resAso' in dir(evtMonit.aso): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.aso.resAso', evtMonit.aso.resAso.cdata, 1, '1;2')
    if 'codCNES' in dir(evtMonit.aso.ideServSaude): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.aso.ideServSaude.codCNES', evtMonit.aso.ideServSaude.codCNES.cdata, 0, '')
    if 'frmCtt' in dir(evtMonit.aso.ideServSaude): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.aso.ideServSaude.frmCtt', evtMonit.aso.ideServSaude.frmCtt.cdata, 1, '')
    if 'email' in dir(evtMonit.aso.ideServSaude): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.aso.ideServSaude.email', evtMonit.aso.ideServSaude.email.cdata, 0, '')
    if 'nmMed' in dir(evtMonit.aso.ideServSaude.medico): validacoes_lista = validar_campo(validacoes_lista,'evtMonit.aso.ideServSaude.medico.nmMed', evtMonit.aso.ideServSaude.medico.nmMed.cdata, 1, '')
    if 'exame' in dir(evtMonit.aso):
        for exame in evtMonit.aso.exame:
            
            if 'dtExm' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.dtExm', exame.dtExm.cdata, 1, '')
            if 'procRealizado' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.procRealizado', exame.procRealizado.cdata, 0, '')
            if 'obsProc' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.obsProc', exame.obsProc.cdata, 0, '')
            if 'interprExm' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.interprExm', exame.interprExm.cdata, 1, '1;2;3')
            if 'ordExame' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.ordExame', exame.ordExame.cdata, 1, '1;2')
            if 'dtIniMonit' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.dtIniMonit', exame.dtIniMonit.cdata, 1, '')
            if 'dtFimMonit' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.dtFimMonit', exame.dtFimMonit.cdata, 0, '')
            if 'indResult' in dir(exame): validacoes_lista = validar_campo(validacoes_lista,'exame.indResult', exame.indResult.cdata, 0, '1;2;3;4')
            if 'nisResp' in dir(exame.respMonit): validacoes_lista = validar_campo(validacoes_lista,'exame.respMonit.nisResp', exame.respMonit.nisResp.cdata, 1, '')
            if 'nrConsClasse' in dir(exame.respMonit): validacoes_lista = validar_campo(validacoes_lista,'exame.respMonit.nrConsClasse', exame.respMonit.nrConsClasse.cdata, 1, '')
            if 'ufConsClasse' in dir(exame.respMonit): validacoes_lista = validar_campo(validacoes_lista,'exame.respMonit.ufConsClasse', exame.respMonit.ufConsClasse.cdata, 0, '')

    return validacoes_lista