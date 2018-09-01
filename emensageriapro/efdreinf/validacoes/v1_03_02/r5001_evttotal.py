#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_r5001_evttotal(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtTotal = doc.Reinf.evtTotal
    
    if 'perApur' in dir(evtTotal.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.ideEvento.perApur', evtTotal.ideEvento.perApur.cdata, 1, '')
    if 'tpInsc' in dir(evtTotal.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.ideContri.tpInsc', evtTotal.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtTotal.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.ideContri.nrInsc', evtTotal.ideContri.nrInsc.cdata, 1, '')
    if 'cdRetorno' in dir(evtTotal.ideRecRetorno.ideStatus): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.ideRecRetorno.ideStatus.cdRetorno', evtTotal.ideRecRetorno.ideStatus.cdRetorno.cdata, 1, '')
    if 'descRetorno' in dir(evtTotal.ideRecRetorno.ideStatus): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.ideRecRetorno.ideStatus.descRetorno', evtTotal.ideRecRetorno.ideStatus.descRetorno.cdata, 1, '')
    if 'nrProtEntr' in dir(evtTotal.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.infoRecEv.nrProtEntr', evtTotal.infoRecEv.nrProtEntr.cdata, 0, '')
    if 'dhProcess' in dir(evtTotal.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.infoRecEv.dhProcess', evtTotal.infoRecEv.dhProcess.cdata, 1, '')
    if 'tpEv' in dir(evtTotal.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.infoRecEv.tpEv', evtTotal.infoRecEv.tpEv.cdata, 1, '')
    if 'idEv' in dir(evtTotal.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.infoRecEv.idEv', evtTotal.infoRecEv.idEv.cdata, 1, '')
    if 'hash' in dir(evtTotal.infoRecEv): validacoes_lista = validar_campo(validacoes_lista,'evtTotal.infoRecEv.hash', evtTotal.infoRecEv.hash.cdata, 1, '')
    if 'regOcorrs' in dir(evtTotal.ideRecRetorno.ideStatus):
        for regOcorrs in evtTotal.ideRecRetorno.ideStatus.regOcorrs:
            
            if 'tpOcorr' in dir(regOcorrs): validacoes_lista = validar_campo(validacoes_lista,'regOcorrs.tpOcorr', regOcorrs.tpOcorr.cdata, 1, '1;2')
            if 'localErroAviso' in dir(regOcorrs): validacoes_lista = validar_campo(validacoes_lista,'regOcorrs.localErroAviso', regOcorrs.localErroAviso.cdata, 1, '')
            if 'codResp' in dir(regOcorrs): validacoes_lista = validar_campo(validacoes_lista,'regOcorrs.codResp', regOcorrs.codResp.cdata, 1, '')
            if 'dscResp' in dir(regOcorrs): validacoes_lista = validar_campo(validacoes_lista,'regOcorrs.dscResp', regOcorrs.dscResp.cdata, 1, '')


    if 'infoTotal' in dir(evtTotal):
        for infoTotal in evtTotal.infoTotal:
            
            if 'nrRecArqBase' in dir(infoTotal): validacoes_lista = validar_campo(validacoes_lista,'infoTotal.nrRecArqBase', infoTotal.nrRecArqBase.cdata, 0, '')


            if 'RTom' in dir(infoTotal):
                for RTom in infoTotal.RTom:
                    
                    if 'cnpjPrestador' in dir(RTom): validacoes_lista = validar_campo(validacoes_lista,'RTom.cnpjPrestador', RTom.cnpjPrestador.cdata, 1, '')
                    if 'vlrTotalBaseRet' in dir(RTom): validacoes_lista = validar_campo(validacoes_lista,'RTom.vlrTotalBaseRet', RTom.vlrTotalBaseRet.cdata, 1, '')
        
        
            if 'RPrest' in dir(infoTotal):
                for RPrest in infoTotal.RPrest:
                    
                    if 'tpInscTomador' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.tpInscTomador', RPrest.tpInscTomador.cdata, 1, '1;4')
                    if 'nrInscTomador' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.nrInscTomador', RPrest.nrInscTomador.cdata, 1, '')
                    if 'vlrTotalBaseRet' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalBaseRet', RPrest.vlrTotalBaseRet.cdata, 1, '')
                    if 'vlrTotalRetPrinc' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalRetPrinc', RPrest.vlrTotalRetPrinc.cdata, 1, '')
                    if 'vlrTotalRetAdic' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalRetAdic', RPrest.vlrTotalRetAdic.cdata, 0, '')
                    if 'vlrTotalNRetPrinc' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalNRetPrinc', RPrest.vlrTotalNRetPrinc.cdata, 0, '')
                    if 'vlrTotalNRetAdic' in dir(RPrest): validacoes_lista = validar_campo(validacoes_lista,'RPrest.vlrTotalNRetAdic', RPrest.vlrTotalNRetAdic.cdata, 0, '')
        
        
            if 'RRecRepAD' in dir(infoTotal):
                for RRecRepAD in infoTotal.RRecRepAD:
                    
                    if 'cnpjAssocDesp' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.cnpjAssocDesp', RRecRepAD.cnpjAssocDesp.cdata, 1, '')
                    if 'vlrTotalRep' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.vlrTotalRep', RRecRepAD.vlrTotalRep.cdata, 1, '')
                    if 'CRRecRepAD' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.CRRecRepAD', RRecRepAD.CRRecRepAD.cdata, 1, '')
                    if 'vlrCRRecRepAD' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.vlrCRRecRepAD', RRecRepAD.vlrCRRecRepAD.cdata, 1, '')
                    if 'vlrCRRecRepADSusp' in dir(RRecRepAD): validacoes_lista = validar_campo(validacoes_lista,'RRecRepAD.vlrCRRecRepADSusp', RRecRepAD.vlrCRRecRepADSusp.cdata, 0, '')
        
        
            if 'RComl' in dir(infoTotal):
                for RComl in infoTotal.RComl:
                    
                    if 'CRComl' in dir(RComl): validacoes_lista = validar_campo(validacoes_lista,'RComl.CRComl', RComl.CRComl.cdata, 1, '')
                    if 'vlrCRComl' in dir(RComl): validacoes_lista = validar_campo(validacoes_lista,'RComl.vlrCRComl', RComl.vlrCRComl.cdata, 1, '')
                    if 'vlrCRComlSusp' in dir(RComl): validacoes_lista = validar_campo(validacoes_lista,'RComl.vlrCRComlSusp', RComl.vlrCRComlSusp.cdata, 0, '')
        
        
            if 'RCPRB' in dir(infoTotal):
                for RCPRB in infoTotal.RCPRB:
                    
                    if 'CRCPRB' in dir(RCPRB): validacoes_lista = validar_campo(validacoes_lista,'RCPRB.CRCPRB', RCPRB.CRCPRB.cdata, 1, '')
                    if 'vlrCRCPRB' in dir(RCPRB): validacoes_lista = validar_campo(validacoes_lista,'RCPRB.vlrCRCPRB', RCPRB.vlrCRCPRB.cdata, 1, '')
                    if 'vlrCRCPRBSusp' in dir(RCPRB): validacoes_lista = validar_campo(validacoes_lista,'RCPRB.vlrCRCPRBSusp', RCPRB.vlrCRCPRBSusp.cdata, 0, '')
        
        
            if 'RRecEspetDesp' in dir(infoTotal):
                for RRecEspetDesp in infoTotal.RRecEspetDesp:
                    
                    if 'CRRecEspetDesp' in dir(RRecEspetDesp): validacoes_lista = validar_campo(validacoes_lista,'RRecEspetDesp.CRRecEspetDesp', RRecEspetDesp.CRRecEspetDesp.cdata, 1, '')
                    if 'vlrReceitaTotal' in dir(RRecEspetDesp): validacoes_lista = validar_campo(validacoes_lista,'RRecEspetDesp.vlrReceitaTotal', RRecEspetDesp.vlrReceitaTotal.cdata, 1, '')
                    if 'vlrCRRecEspetDesp' in dir(RRecEspetDesp): validacoes_lista = validar_campo(validacoes_lista,'RRecEspetDesp.vlrCRRecEspetDesp', RRecEspetDesp.vlrCRRecEspetDesp.cdata, 1, '')
                    if 'vlrCRRecEspetDespSusp' in dir(RRecEspetDesp): validacoes_lista = validar_campo(validacoes_lista,'RRecEspetDesp.vlrCRRecEspetDespSusp', RRecEspetDesp.vlrCRRecEspetDespSusp.cdata, 0, '')
        
        
    return validacoes_lista