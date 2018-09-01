#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1299_evtfechaevper(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtFechaEvPer = doc.eSocial.evtFechaEvPer
    
    if 'indApuracao' in dir(evtFechaEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEvento.indApuracao', evtFechaEvPer.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtFechaEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEvento.perApur', evtFechaEvPer.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtFechaEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEvento.tpAmb', evtFechaEvPer.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtFechaEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEvento.procEmi', evtFechaEvPer.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtFechaEvPer.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEvento.verProc', evtFechaEvPer.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtFechaEvPer.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEmpregador.tpInsc', evtFechaEvPer.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtFechaEvPer.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.ideEmpregador.nrInsc', evtFechaEvPer.ideEmpregador.nrInsc.cdata, 1, '')
    if 'evtRemun' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtRemun', evtFechaEvPer.infoFech.evtRemun.cdata, 1, 'S;N')
    if 'evtPgtos' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtPgtos', evtFechaEvPer.infoFech.evtPgtos.cdata, 1, 'S;N')
    if 'evtAqProd' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtAqProd', evtFechaEvPer.infoFech.evtAqProd.cdata, 1, 'S;N')
    if 'evtComProd' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtComProd', evtFechaEvPer.infoFech.evtComProd.cdata, 1, 'S;N')
    if 'evtContratAvNP' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtContratAvNP', evtFechaEvPer.infoFech.evtContratAvNP.cdata, 1, 'S;N')
    if 'evtInfoComplPer' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.evtInfoComplPer', evtFechaEvPer.infoFech.evtInfoComplPer.cdata, 1, 'S;N')
    if 'compSemMovto' in dir(evtFechaEvPer.infoFech): validacoes_lista = validar_campo(validacoes_lista,'evtFechaEvPer.infoFech.compSemMovto', evtFechaEvPer.infoFech.compSemMovto.cdata, 0, '')
    if 'ideRespInf' in dir(evtFechaEvPer):
        for ideRespInf in evtFechaEvPer.ideRespInf:
            
            if 'nmResp' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.nmResp', ideRespInf.nmResp.cdata, 1, '')
            if 'cpfResp' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.cpfResp', ideRespInf.cpfResp.cdata, 1, '')
            if 'telefone' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.telefone', ideRespInf.telefone.cdata, 1, '')
            if 'email' in dir(ideRespInf): validacoes_lista = validar_campo(validacoes_lista,'ideRespInf.email', ideRespInf.email.cdata, 0, '')

    return validacoes_lista