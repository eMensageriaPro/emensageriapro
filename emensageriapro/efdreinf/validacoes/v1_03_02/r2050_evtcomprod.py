#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_r2050_evtcomprod(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtComProd = doc.Reinf.evtComProd
    
    if 'indRetif' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.indRetif', evtComProd.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.nrRecibo', evtComProd.ideEvento.nrRecibo.cdata, 0, '')
    if 'perApur' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.perApur', evtComProd.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.tpAmb', evtComProd.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.procEmi', evtComProd.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.verProc', evtComProd.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtComProd.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideContri.tpInsc', evtComProd.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtComProd.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideContri.nrInsc', evtComProd.ideContri.nrInsc.cdata, 1, '')
    if 'tpInscEstab' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.tpInscEstab', evtComProd.infoComProd.ideEstab.tpInscEstab.cdata, 1, '1')
    if 'nrInscEstab' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.nrInscEstab', evtComProd.infoComProd.ideEstab.nrInscEstab.cdata, 1, '')
    if 'vlrRecBrutaTotal' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrRecBrutaTotal', evtComProd.infoComProd.ideEstab.vlrRecBrutaTotal.cdata, 1, '')
    if 'vlrCPApur' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrCPApur', evtComProd.infoComProd.ideEstab.vlrCPApur.cdata, 1, '')
    if 'vlrRatApur' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrRatApur', evtComProd.infoComProd.ideEstab.vlrRatApur.cdata, 1, '')
    if 'vlrSenarApur' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrSenarApur', evtComProd.infoComProd.ideEstab.vlrSenarApur.cdata, 1, '')
    if 'vlrCPSuspTotal' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrCPSuspTotal', evtComProd.infoComProd.ideEstab.vlrCPSuspTotal.cdata, 0, '')
    if 'vlrRatSuspTotal' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrRatSuspTotal', evtComProd.infoComProd.ideEstab.vlrRatSuspTotal.cdata, 0, '')
    if 'vlrSenarSuspTotal' in dir(evtComProd.infoComProd.ideEstab): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstab.vlrSenarSuspTotal', evtComProd.infoComProd.ideEstab.vlrSenarSuspTotal.cdata, 0, '')
    if 'tipoCom' in dir(evtComProd.infoComProd.ideEstab):
        for tipoCom in evtComProd.infoComProd.ideEstab.tipoCom:
            
            if 'indCom' in dir(tipoCom): validacoes_lista = validar_campo(validacoes_lista,'tipoCom.indCom', tipoCom.indCom.cdata, 1, '1;8;9')
            if 'vlrRecBruta' in dir(tipoCom): validacoes_lista = validar_campo(validacoes_lista,'tipoCom.vlrRecBruta', tipoCom.vlrRecBruta.cdata, 1, '')


            if 'infoProc' in dir(tipoCom):
                for infoProc in tipoCom.infoProc:
                    
                    if 'tpProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.tpProc', infoProc.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.nrProc', infoProc.nrProc.cdata, 1, '')
                    if 'codSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.codSusp', infoProc.codSusp.cdata, 0, '')
                    if 'vlrCPSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrCPSusp', infoProc.vlrCPSusp.cdata, 0, '')
                    if 'vlrRatSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrRatSusp', infoProc.vlrRatSusp.cdata, 0, '')
                    if 'vlrSenarSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrSenarSusp', infoProc.vlrSenarSusp.cdata, 0, '')
        
        
    return validacoes_lista