#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1270_evtcontratavnp(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtContratAvNP = doc.eSocial.evtContratAvNP
    
    if 'indRetif' in dir(evtContratAvNP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContratAvNP.ideEvento.indRetif', evtContratAvNP.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtContratAvNP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContratAvNP.ideEvento.nrRecibo', evtContratAvNP.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtContratAvNP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContratAvNP.ideEvento.indApuracao', evtContratAvNP.ideEvento.indApuracao.cdata, 1, '1')
    if 'perApur' in dir(evtContratAvNP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContratAvNP.ideEvento.perApur', evtContratAvNP.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtContratAvNP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContratAvNP.ideEvento.tpAmb', evtContratAvNP.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtContratAvNP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContratAvNP.ideEvento.procEmi', evtContratAvNP.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtContratAvNP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtContratAvNP.ideEvento.verProc', evtContratAvNP.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtContratAvNP.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtContratAvNP.ideEmpregador.tpInsc', evtContratAvNP.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtContratAvNP.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtContratAvNP.ideEmpregador.nrInsc', evtContratAvNP.ideEmpregador.nrInsc.cdata, 1, '')
    if 'remunAvNP' in dir(evtContratAvNP):
        for remunAvNP in evtContratAvNP.remunAvNP:
            
            if 'tpInsc' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.tpInsc', remunAvNP.tpInsc.cdata, 1, '1;2;3;4')
            if 'nrInsc' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.nrInsc', remunAvNP.nrInsc.cdata, 1, '')
            if 'codLotacao' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.codLotacao', remunAvNP.codLotacao.cdata, 1, '')
            if 'vrBcCp00' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.vrBcCp00', remunAvNP.vrBcCp00.cdata, 1, '')
            if 'vrBcCp15' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.vrBcCp15', remunAvNP.vrBcCp15.cdata, 1, '')
            if 'vrBcCp20' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.vrBcCp20', remunAvNP.vrBcCp20.cdata, 1, '')
            if 'vrBcCp25' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.vrBcCp25', remunAvNP.vrBcCp25.cdata, 1, '')
            if 'vrBcCp13' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.vrBcCp13', remunAvNP.vrBcCp13.cdata, 1, '')
            if 'vrBcFgts' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.vrBcFgts', remunAvNP.vrBcFgts.cdata, 1, '')
            if 'vrDescCP' in dir(remunAvNP): validacoes_lista = validar_campo(validacoes_lista,'remunAvNP.vrDescCP', remunAvNP.vrDescCP.cdata, 1, '')

    return validacoes_lista