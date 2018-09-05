#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_r2098_evtreabreevper(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtReabreEvPer = doc.Reinf.evtReabreEvPer
    
    if 'perApur' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.perApur', evtReabreEvPer.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.tpAmb', evtReabreEvPer.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.procEmi', evtReabreEvPer.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.verProc', evtReabreEvPer.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtReabreEvPer.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideContri.tpInsc', evtReabreEvPer.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtReabreEvPer.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideContri.nrInsc', evtReabreEvPer.ideContri.nrInsc.cdata, 1, '')
    return validacoes_lista