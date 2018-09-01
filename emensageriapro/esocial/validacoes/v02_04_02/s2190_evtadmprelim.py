#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2190_evtadmprelim(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAdmPrelim = doc.eSocial.evtAdmPrelim
    
    if 'tpAmb' in dir(evtAdmPrelim.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEvento.tpAmb', evtAdmPrelim.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtAdmPrelim.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEvento.procEmi', evtAdmPrelim.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtAdmPrelim.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEvento.verProc', evtAdmPrelim.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtAdmPrelim.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEmpregador.tpInsc', evtAdmPrelim.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtAdmPrelim.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.ideEmpregador.nrInsc', evtAdmPrelim.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtAdmPrelim.infoRegPrelim): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.infoRegPrelim.cpfTrab', evtAdmPrelim.infoRegPrelim.cpfTrab.cdata, 1, '')
    if 'dtNascto' in dir(evtAdmPrelim.infoRegPrelim): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.infoRegPrelim.dtNascto', evtAdmPrelim.infoRegPrelim.dtNascto.cdata, 1, '')
    if 'dtAdm' in dir(evtAdmPrelim.infoRegPrelim): validacoes_lista = validar_campo(validacoes_lista,'evtAdmPrelim.infoRegPrelim.dtAdm', evtAdmPrelim.infoRegPrelim.dtAdm.cdata, 1, '')
    return validacoes_lista