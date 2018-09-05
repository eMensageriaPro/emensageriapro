#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_r9000_evtexclusao(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtExclusao = doc.Reinf.evtExclusao
    
    if 'tpAmb' in dir(evtExclusao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEvento.tpAmb', evtExclusao.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtExclusao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEvento.procEmi', evtExclusao.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtExclusao.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideEvento.verProc', evtExclusao.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtExclusao.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideContri.tpInsc', evtExclusao.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtExclusao.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.ideContri.nrInsc', evtExclusao.ideContri.nrInsc.cdata, 1, '')
    if 'tpEvento' in dir(evtExclusao.infoExclusao): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.infoExclusao.tpEvento', evtExclusao.infoExclusao.tpEvento.cdata, 1, '')
    if 'nrRecEvt' in dir(evtExclusao.infoExclusao): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.infoExclusao.nrRecEvt', evtExclusao.infoExclusao.nrRecEvt.cdata, 1, '')
    if 'perApur' in dir(evtExclusao.infoExclusao): validacoes_lista = validar_campo(validacoes_lista,'evtExclusao.infoExclusao.perApur', evtExclusao.infoExclusao.perApur.cdata, 1, '')
    return validacoes_lista