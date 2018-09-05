#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2399_evttsvtermino(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTSVTermino = doc.eSocial.evtTSVTermino
    
    if 'indRetif' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.indRetif', evtTSVTermino.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.nrRecibo', evtTSVTermino.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.tpAmb', evtTSVTermino.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.procEmi', evtTSVTermino.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTSVTermino.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEvento.verProc', evtTSVTermino.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTSVTermino.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEmpregador.tpInsc', evtTSVTermino.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTSVTermino.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideEmpregador.nrInsc', evtTSVTermino.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtTSVTermino.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideTrabSemVinculo.cpfTrab', evtTSVTermino.ideTrabSemVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtTSVTermino.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideTrabSemVinculo.nisTrab', evtTSVTermino.ideTrabSemVinculo.nisTrab.cdata, 0, '')
    if 'codCateg' in dir(evtTSVTermino.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.ideTrabSemVinculo.codCateg', evtTSVTermino.ideTrabSemVinculo.codCateg.cdata, 1, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
    if 'dtTerm' in dir(evtTSVTermino.infoTSVTermino): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.infoTSVTermino.dtTerm', evtTSVTermino.infoTSVTermino.dtTerm.cdata, 1, '')
    if 'mtvDesligTSV' in dir(evtTSVTermino.infoTSVTermino): validacoes_lista = validar_campo(validacoes_lista,'evtTSVTermino.infoTSVTermino.mtvDesligTSV', evtTSVTermino.infoTSVTermino.mtvDesligTSV.cdata, 0, '01;02;03;04;05;06;99')
    if 'verbasResc' in dir(evtTSVTermino.infoTSVTermino):
        for verbasResc in evtTSVTermino.infoTSVTermino.verbasResc:
            

            if 'dmDev' in dir(verbasResc):
                for dmDev in verbasResc.dmDev:
                    
                    if 'ideDmDev' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.ideDmDev', dmDev.ideDmDev.cdata, 1, '')
        
            if 'procJudTrab' in dir(verbasResc):
                for procJudTrab in verbasResc.procJudTrab:
                    
                    if 'tpTrib' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.tpTrib', procJudTrab.tpTrib.cdata, 1, '4;2;3;4')
                    if 'nrProcJud' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.nrProcJud', procJudTrab.nrProcJud.cdata, 1, '')
                    if 'codSusp' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.codSusp', procJudTrab.codSusp.cdata, 0, '')
        
            if 'infoMV' in dir(verbasResc):
                for infoMV in verbasResc.infoMV:
                    
                    if 'indMV' in dir(infoMV): validacoes_lista = validar_campo(validacoes_lista,'infoMV.indMV', infoMV.indMV.cdata, 1, '1;2;3')
        
    if 'quarentena' in dir(evtTSVTermino.infoTSVTermino):
        for quarentena in evtTSVTermino.infoTSVTermino.quarentena:
            
            if 'dtFimQuar' in dir(quarentena): validacoes_lista = validar_campo(validacoes_lista,'quarentena.dtFimQuar', quarentena.dtFimQuar.cdata, 1, '')

    return validacoes_lista