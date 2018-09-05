#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1298_evtreabreevper(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtReabreEvPer = doc.eSocial.evtReabreEvPer
    
    if 'indApuracao' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.indApuracao', evtReabreEvPer.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.perApur', evtReabreEvPer.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.tpAmb', evtReabreEvPer.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.procEmi', evtReabreEvPer.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtReabreEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEvento.verProc', evtReabreEvPer.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtReabreEvPer.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEmpregador.tpInsc', evtReabreEvPer.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtReabreEvPer.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtReabreEvPer.ideEmpregador.nrInsc', evtReabreEvPer.ideEmpregador.nrInsc.cdata, 1, '')
    return validacoes_lista