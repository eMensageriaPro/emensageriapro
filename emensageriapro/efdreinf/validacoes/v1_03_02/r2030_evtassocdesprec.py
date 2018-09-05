#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_r2030_evtassocdesprec(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtAssocDespRec = doc.Reinf.evtAssocDespRec
    
    if 'indRetif' in dir(evtAssocDespRec.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideEvento.indRetif', evtAssocDespRec.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtAssocDespRec.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideEvento.nrRecibo', evtAssocDespRec.ideEvento.nrRecibo.cdata, 0, '')
    if 'perApur' in dir(evtAssocDespRec.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideEvento.perApur', evtAssocDespRec.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtAssocDespRec.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideEvento.tpAmb', evtAssocDespRec.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtAssocDespRec.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideEvento.procEmi', evtAssocDespRec.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtAssocDespRec.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideEvento.verProc', evtAssocDespRec.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtAssocDespRec.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideContri.tpInsc', evtAssocDespRec.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtAssocDespRec.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideContri.nrInsc', evtAssocDespRec.ideContri.nrInsc.cdata, 1, '')
    if 'tpInscEstab' in dir(evtAssocDespRec.ideContri.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideContri.ideEstab.tpInscEstab', evtAssocDespRec.ideContri.ideEstab.tpInscEstab.cdata, 1, '1')
    if 'nrInscEstab' in dir(evtAssocDespRec.ideContri.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtAssocDespRec.ideContri.ideEstab.nrInscEstab', evtAssocDespRec.ideContri.ideEstab.nrInscEstab.cdata, 1, '')
    if 'recursosRec' in dir(evtAssocDespRec.ideContri.ideEstab):
        for recursosRec in evtAssocDespRec.ideContri.ideEstab.recursosRec:
            
            if 'cnpjOrigRecurso' in dir(recursosRec): validacoes_lista = validar_campo(validacoes_lista,'recursosRec.cnpjOrigRecurso', recursosRec.cnpjOrigRecurso.cdata, 1, '')
            if 'vlrTotalRec' in dir(recursosRec): validacoes_lista = validar_campo(validacoes_lista,'recursosRec.vlrTotalRec', recursosRec.vlrTotalRec.cdata, 1, '')
            if 'vlrTotalRet' in dir(recursosRec): validacoes_lista = validar_campo(validacoes_lista,'recursosRec.vlrTotalRet', recursosRec.vlrTotalRet.cdata, 1, '')
            if 'vlrTotalNRet' in dir(recursosRec): validacoes_lista = validar_campo(validacoes_lista,'recursosRec.vlrTotalNRet', recursosRec.vlrTotalNRet.cdata, 0, '')


            if 'infoRecurso' in dir(recursosRec):
                for infoRecurso in recursosRec.infoRecurso:
                    
                    if 'tpRepasse' in dir(infoRecurso): validacoes_lista = validar_campo(validacoes_lista,'infoRecurso.tpRepasse', infoRecurso.tpRepasse.cdata, 1, '1;2;3;4;5')
                    if 'descRecurso' in dir(infoRecurso): validacoes_lista = validar_campo(validacoes_lista,'infoRecurso.descRecurso', infoRecurso.descRecurso.cdata, 1, '')
                    if 'vlrBruto' in dir(infoRecurso): validacoes_lista = validar_campo(validacoes_lista,'infoRecurso.vlrBruto', infoRecurso.vlrBruto.cdata, 1, '')
                    if 'vlrRetApur' in dir(infoRecurso): validacoes_lista = validar_campo(validacoes_lista,'infoRecurso.vlrRetApur', infoRecurso.vlrRetApur.cdata, 1, '')
        
        
            if 'infoProc' in dir(recursosRec):
                for infoProc in recursosRec.infoProc:
                    
                    if 'tpProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.tpProc', infoProc.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.nrProc', infoProc.nrProc.cdata, 1, '')
                    if 'codSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.codSusp', infoProc.codSusp.cdata, 0, '')
                    if 'vlrNRet' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrNRet', infoProc.vlrNRet.cdata, 1, '')
        
        
    return validacoes_lista