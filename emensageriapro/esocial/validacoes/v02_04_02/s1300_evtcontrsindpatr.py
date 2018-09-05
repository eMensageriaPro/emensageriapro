#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1300_evtcontrsindpatr(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtContrSindPatr = doc.eSocial.evtContrSindPatr
    
    if 'indRetif' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.indRetif', evtContrSindPatr.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.nrRecibo', evtContrSindPatr.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.indApuracao', evtContrSindPatr.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.perApur', evtContrSindPatr.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.tpAmb', evtContrSindPatr.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.procEmi', evtContrSindPatr.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtContrSindPatr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEvento.verProc', evtContrSindPatr.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtContrSindPatr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEmpregador.tpInsc', evtContrSindPatr.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtContrSindPatr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtContrSindPatr.ideEmpregador.nrInsc', evtContrSindPatr.ideEmpregador.nrInsc.cdata, 1, '')
    if 'contribSind' in dir(evtContrSindPatr):
        for contribSind in evtContrSindPatr.contribSind:
            
            if 'cnpjSindic' in dir(contribSind): validacoes_lista = validar_campo(validacoes_lista,'contribSind.cnpjSindic', contribSind.cnpjSindic.cdata, 1, '')
            if 'tpContribSind' in dir(contribSind): validacoes_lista = validar_campo(validacoes_lista,'contribSind.tpContribSind', contribSind.tpContribSind.cdata, 1, '1;2;3;4')
            if 'vlrContribSind' in dir(contribSind): validacoes_lista = validar_campo(validacoes_lista,'contribSind.vlrContribSind', contribSind.vlrContribSind.cdata, 1, '')

    return validacoes_lista