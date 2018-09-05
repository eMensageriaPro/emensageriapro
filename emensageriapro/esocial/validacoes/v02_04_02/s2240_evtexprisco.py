#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2240_evtexprisco(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtExpRisco = doc.eSocial.evtExpRisco
    
    if 'indRetif' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.indRetif', evtExpRisco.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.nrRecibo', evtExpRisco.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.tpAmb', evtExpRisco.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.procEmi', evtExpRisco.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtExpRisco.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEvento.verProc', evtExpRisco.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtExpRisco.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEmpregador.tpInsc', evtExpRisco.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtExpRisco.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideEmpregador.nrInsc', evtExpRisco.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtExpRisco.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideVinculo.cpfTrab', evtExpRisco.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtExpRisco.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideVinculo.nisTrab', evtExpRisco.ideVinculo.nisTrab.cdata, 0, '')
    if 'matricula' in dir(evtExpRisco.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtExpRisco.ideVinculo.matricula', evtExpRisco.ideVinculo.matricula.cdata, 0, '')
    if 'iniExpRisco' in dir(evtExpRisco.infoExpRisco):
        for iniExpRisco in evtExpRisco.infoExpRisco.iniExpRisco:
            
            if 'dtIniCondicao' in dir(iniExpRisco): validacoes_lista = validar_campo(validacoes_lista,'iniExpRisco.dtIniCondicao', iniExpRisco.dtIniCondicao.cdata, 1, '')

            if 'infoAmb' in dir(iniExpRisco):
                for infoAmb in iniExpRisco.infoAmb:
                    
                    if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')
                    if 'dscAtivDes' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.dscAtivDes', infoAmb.dscAtivDes.cdata, 1, '')
        
    if 'altExpRisco' in dir(evtExpRisco.infoExpRisco):
        for altExpRisco in evtExpRisco.infoExpRisco.altExpRisco:
            
            if 'dtAltCondicao' in dir(altExpRisco): validacoes_lista = validar_campo(validacoes_lista,'altExpRisco.dtAltCondicao', altExpRisco.dtAltCondicao.cdata, 1, '')

            if 'infoAmb' in dir(altExpRisco):
                for infoAmb in altExpRisco.infoAmb:
                    
                    if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')
                    if 'dscAtivDes' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.dscAtivDes', infoAmb.dscAtivDes.cdata, 1, '')
        
    if 'fimExpRisco' in dir(evtExpRisco.infoExpRisco):
        for fimExpRisco in evtExpRisco.infoExpRisco.fimExpRisco:
            
            if 'dtFimCondicao' in dir(fimExpRisco): validacoes_lista = validar_campo(validacoes_lista,'fimExpRisco.dtFimCondicao', fimExpRisco.dtFimCondicao.cdata, 1, '')

            if 'infoAmb' in dir(fimExpRisco):
                for infoAmb in fimExpRisco.infoAmb:
                    
                    if 'codAmb' in dir(infoAmb): validacoes_lista = validar_campo(validacoes_lista,'infoAmb.codAmb', infoAmb.codAmb.cdata, 1, '')
        
    if 'respReg' in dir(evtExpRisco.infoExpRisco):
        for respReg in evtExpRisco.infoExpRisco.respReg:
            
            if 'dtIni' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.dtIni', respReg.dtIni.cdata, 1, '')
            if 'dtFim' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.dtFim', respReg.dtFim.cdata, 0, '')
            if 'nisResp' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.nisResp', respReg.nisResp.cdata, 1, '')
            if 'nrOc' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.nrOc', respReg.nrOc.cdata, 1, '')
            if 'ufOC' in dir(respReg): validacoes_lista = validar_campo(validacoes_lista,'respReg.ufOC', respReg.ufOC.cdata, 0, '')

    return validacoes_lista