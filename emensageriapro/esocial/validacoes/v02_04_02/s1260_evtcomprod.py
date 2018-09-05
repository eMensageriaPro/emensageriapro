#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1260_evtcomprod(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtComProd = doc.eSocial.evtComProd
    
    if 'indRetif' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.indRetif', evtComProd.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.nrRecibo', evtComProd.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.indApuracao', evtComProd.ideEvento.indApuracao.cdata, 1, '1')
    if 'perApur' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.perApur', evtComProd.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.tpAmb', evtComProd.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.procEmi', evtComProd.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtComProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEvento.verProc', evtComProd.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtComProd.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEmpregador.tpInsc', evtComProd.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtComProd.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.ideEmpregador.nrInsc', evtComProd.ideEmpregador.nrInsc.cdata, 1, '')
    if 'nrInscEstabRural' in dir(evtComProd.infoComProd.ideEstabel): validacoes_lista = validar_campo(validacoes_lista,'evtComProd.infoComProd.ideEstabel.nrInscEstabRural', evtComProd.infoComProd.ideEstabel.nrInscEstabRural.cdata, 1, '')
    if 'tpComerc' in dir(evtComProd.infoComProd.ideEstabel):
        for tpComerc in evtComProd.infoComProd.ideEstabel.tpComerc:
            
            if 'indComerc' in dir(tpComerc): validacoes_lista = validar_campo(validacoes_lista,'tpComerc.indComerc', tpComerc.indComerc.cdata, 1, '2;3;7;8;9')
            if 'vrTotCom' in dir(tpComerc): validacoes_lista = validar_campo(validacoes_lista,'tpComerc.vrTotCom', tpComerc.vrTotCom.cdata, 1, '')

            if 'ideAdquir' in dir(tpComerc):
                for ideAdquir in tpComerc.ideAdquir:
                    
                    if 'tpInsc' in dir(ideAdquir): validacoes_lista = validar_campo(validacoes_lista,'ideAdquir.tpInsc', ideAdquir.tpInsc.cdata, 1, '1;2;3;4')
                    if 'nrInsc' in dir(ideAdquir): validacoes_lista = validar_campo(validacoes_lista,'ideAdquir.nrInsc', ideAdquir.nrInsc.cdata, 1, '')
                    if 'vrComerc' in dir(ideAdquir): validacoes_lista = validar_campo(validacoes_lista,'ideAdquir.vrComerc', ideAdquir.vrComerc.cdata, 1, '')
        
            if 'infoProcJud' in dir(tpComerc):
                for infoProcJud in tpComerc.infoProcJud:
                    
                    if 'tpProc' in dir(infoProcJud): validacoes_lista = validar_campo(validacoes_lista,'infoProcJud.tpProc', infoProcJud.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(infoProcJud): validacoes_lista = validar_campo(validacoes_lista,'infoProcJud.nrProc', infoProcJud.nrProc.cdata, 1, '')
                    if 'codSusp' in dir(infoProcJud): validacoes_lista = validar_campo(validacoes_lista,'infoProcJud.codSusp', infoProcJud.codSusp.cdata, 1, '')
                    if 'vrCPSusp' in dir(infoProcJud): validacoes_lista = validar_campo(validacoes_lista,'infoProcJud.vrCPSusp', infoProcJud.vrCPSusp.cdata, 0, '')
                    if 'vrRatSusp' in dir(infoProcJud): validacoes_lista = validar_campo(validacoes_lista,'infoProcJud.vrRatSusp', infoProcJud.vrRatSusp.cdata, 0, '')
                    if 'vrSenarSusp' in dir(infoProcJud): validacoes_lista = validar_campo(validacoes_lista,'infoProcJud.vrSenarSusp', infoProcJud.vrSenarSusp.cdata, 0, '')
        
    return validacoes_lista