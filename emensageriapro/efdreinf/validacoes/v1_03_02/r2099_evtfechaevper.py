#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_r2099_evtfechaevper(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtFechaEvPer = doc.Reinf.evtFechaEvPer
    
    if 'perApur' in dir(evtFechaEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEvento.perApur', evtFechaEvPer.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtFechaEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEvento.tpAmb', evtFechaEvPer.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtFechaEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEvento.procEmi', evtFechaEvPer.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtFechaEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEvento.verProc', evtFechaEvPer.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtFechaEvPer.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideContri.tpInsc', evtFechaEvPer.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtFechaEvPer.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideContri.nrInsc', evtFechaEvPer.ideContri.nrInsc.cdata, 1, '')
    if 'evtServTm' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtServTm', evtFechaEvPer.infoFech.evtServTm.cdata, 1, 'S;N')
    if 'evtServPr' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtServPr', evtFechaEvPer.infoFech.evtServPr.cdata, 1, 'S;N')
    if 'evtAssDespRec' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtAssDespRec', evtFechaEvPer.infoFech.evtAssDespRec.cdata, 1, 'S;N')
    if 'evtAssDespRep' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtAssDespRep', evtFechaEvPer.infoFech.evtAssDespRep.cdata, 1, 'S;N')
    if 'evtComProd' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtComProd', evtFechaEvPer.infoFech.evtComProd.cdata, 1, 'S;N')
    if 'evtCPRB' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtCPRB', evtFechaEvPer.infoFech.evtCPRB.cdata, 1, 'S;N')
    if 'evtPgtos' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtPgtos', evtFechaEvPer.infoFech.evtPgtos.cdata, 1, 'S;N')
    if 'compSemMovto' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.compSemMovto', evtFechaEvPer.infoFech.compSemMovto.cdata, 0, '')
    if 'ideRespInf' in dir(evtFechaEvPer):
        for ideRespInf in evtFechaEvPer.ideRespInf:
            
            if 'nmResp' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.nmResp', ideRespInf.nmResp.cdata, 1, '')
            if 'cpfResp' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.cpfResp', ideRespInf.cpfResp.cdata, 1, '')
            if 'telefone' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.telefone', ideRespInf.telefone.cdata, 0, '')
            if 'email' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.email', ideRespInf.email.cdata, 0, '')


    return validacoes_lista