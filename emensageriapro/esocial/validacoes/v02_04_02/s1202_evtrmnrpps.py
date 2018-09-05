#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1202_evtrmnrpps(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtRmnRPPS = doc.eSocial.evtRmnRPPS
    
    if 'indRetif' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.indRetif', evtRmnRPPS.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.nrRecibo', evtRmnRPPS.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.indApuracao', evtRmnRPPS.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.perApur', evtRmnRPPS.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.tpAmb', evtRmnRPPS.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.procEmi', evtRmnRPPS.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.verProc', evtRmnRPPS.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtRmnRPPS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEmpregador.tpInsc', evtRmnRPPS.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtRmnRPPS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEmpregador.nrInsc', evtRmnRPPS.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtRmnRPPS.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideTrabalhador.cpfTrab', evtRmnRPPS.ideTrabalhador.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtRmnRPPS.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideTrabalhador.nisTrab', evtRmnRPPS.ideTrabalhador.nisTrab.cdata, 0, '')
    if 'qtdDepFP' in dir(evtRmnRPPS.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideTrabalhador.qtdDepFP', evtRmnRPPS.ideTrabalhador.qtdDepFP.cdata, 0, '')
    if 'procJudTrab' in dir(evtRmnRPPS.ideTrabalhador):
        for procJudTrab in evtRmnRPPS.ideTrabalhador.procJudTrab:
            
            if 'tpTrib' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.tpTrib', procJudTrab.tpTrib.cdata, 1, '2;2;3;4')
            if 'nrProcJud' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.nrProcJud', procJudTrab.nrProcJud.cdata, 1, '')
            if 'codSusp' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.codSusp', procJudTrab.codSusp.cdata, 0, '')

    if 'dmDev' in dir(evtRmnRPPS):
        for dmDev in evtRmnRPPS.dmDev:
            
            if 'ideDmDev' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.ideDmDev', dmDev.ideDmDev.cdata, 1, '')

            if 'infoPerApur' in dir(dmDev):
                for infoPerApur in dmDev.infoPerApur:
                    
        
            if 'infoPerAnt' in dir(dmDev):
                for infoPerAnt in dmDev.infoPerAnt:
                    
        
    return validacoes_lista