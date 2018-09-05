#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1295_evttotconting(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTotConting = doc.eSocial.evtTotConting
    
    if 'indApuracao' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.indApuracao', evtTotConting.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.perApur', evtTotConting.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.tpAmb', evtTotConting.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.procEmi', evtTotConting.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTotConting.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEvento.verProc', evtTotConting.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTotConting.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEmpregador.tpInsc', evtTotConting.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTotConting.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTotConting.ideEmpregador.nrInsc', evtTotConting.ideEmpregador.nrInsc.cdata, 1, '')
    if 'ideRespInf' in dir(evtTotConting):
        for ideRespInf in evtTotConting.ideRespInf:
            
            if 'nmResp' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.nmResp', ideRespInf.nmResp.cdata, 1, '')
            if 'cpfResp' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.cpfResp', ideRespInf.cpfResp.cdata, 1, '')
            if 'telefone' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.telefone', ideRespInf.telefone.cdata, 1, '')
            if 'email' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.email', ideRespInf.email.cdata, 0, '')

    return validacoes_lista