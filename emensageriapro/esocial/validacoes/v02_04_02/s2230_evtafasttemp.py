#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2230_evtafasttemp(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAfastTemp = doc.eSocial.evtAfastTemp
    
    if 'indRetif' in dir(evtAfastTemp.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideEvento.indRetif', evtAfastTemp.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtAfastTemp.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideEvento.nrRecibo', evtAfastTemp.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtAfastTemp.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideEvento.tpAmb', evtAfastTemp.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtAfastTemp.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideEvento.procEmi', evtAfastTemp.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtAfastTemp.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideEvento.verProc', evtAfastTemp.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtAfastTemp.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideEmpregador.tpInsc', evtAfastTemp.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtAfastTemp.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideEmpregador.nrInsc', evtAfastTemp.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtAfastTemp.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideVinculo.cpfTrab', evtAfastTemp.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtAfastTemp.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideVinculo.nisTrab', evtAfastTemp.ideVinculo.nisTrab.cdata, 0, '')
    if 'matricula' in dir(evtAfastTemp.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideVinculo.matricula', evtAfastTemp.ideVinculo.matricula.cdata, 0, '')
    if 'codCateg' in dir(evtAfastTemp.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtAfastTemp.ideVinculo.codCateg', evtAfastTemp.ideVinculo.codCateg.cdata, 0, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
    if 'iniAfastamento' in dir(evtAfastTemp.infoAfastamento):
        for iniAfastamento in evtAfastTemp.infoAfastamento.iniAfastamento:
            
            if 'dtIniAfast' in dir(iniAfastamento): validacoes_lista = validar_campo(validacoes_lista,'iniAfastamento.dtIniAfast', iniAfastamento.dtIniAfast.cdata, 1, '')
            if 'codMotAfast' in dir(iniAfastamento): validacoes_lista = validar_campo(validacoes_lista,'iniAfastamento.codMotAfast', iniAfastamento.codMotAfast.cdata, 1, '01;03;05;06;07;08;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;33;34')
            if 'infoMesmoMtv' in dir(iniAfastamento): validacoes_lista = validar_campo(validacoes_lista,'iniAfastamento.infoMesmoMtv', iniAfastamento.infoMesmoMtv.cdata, 0, 'S;N')
            if 'tpAcidTransito' in dir(iniAfastamento): validacoes_lista = validar_campo(validacoes_lista,'iniAfastamento.tpAcidTransito', iniAfastamento.tpAcidTransito.cdata, 0, '1;2;3')
            if 'observacao' in dir(iniAfastamento): validacoes_lista = validar_campo(validacoes_lista,'iniAfastamento.observacao', iniAfastamento.observacao.cdata, 0, '')

            if 'infoAtestado' in dir(iniAfastamento):
                for infoAtestado in iniAfastamento.infoAtestado:
                    
                    if 'codCID' in dir(infoAtestado): validacoes_lista = validar_campo(validacoes_lista,'infoAtestado.codCID', infoAtestado.codCID.cdata, 0, '')
                    if 'qtdDiasAfast' in dir(infoAtestado): validacoes_lista = validar_campo(validacoes_lista,'infoAtestado.qtdDiasAfast', infoAtestado.qtdDiasAfast.cdata, 1, '')
        
            if 'infoCessao' in dir(iniAfastamento):
                for infoCessao in iniAfastamento.infoCessao:
                    
                    if 'cnpjCess' in dir(infoCessao): validacoes_lista = validar_campo(validacoes_lista,'infoCessao.cnpjCess', infoCessao.cnpjCess.cdata, 1, '')
                    if 'infOnus' in dir(infoCessao): validacoes_lista = validar_campo(validacoes_lista,'infoCessao.infOnus', infoCessao.infOnus.cdata, 1, '1;2;3')
        
            if 'infoMandSind' in dir(iniAfastamento):
                for infoMandSind in iniAfastamento.infoMandSind:
                    
                    if 'cnpjSind' in dir(infoMandSind): validacoes_lista = validar_campo(validacoes_lista,'infoMandSind.cnpjSind', infoMandSind.cnpjSind.cdata, 1, '')
                    if 'infOnusRemun' in dir(infoMandSind): validacoes_lista = validar_campo(validacoes_lista,'infoMandSind.infOnusRemun', infoMandSind.infOnusRemun.cdata, 1, '1;2;3')
        
    if 'infoRetif' in dir(evtAfastTemp.infoAfastamento):
        for infoRetif in evtAfastTemp.infoAfastamento.infoRetif:
            
            if 'origRetif' in dir(infoRetif): validacoes_lista = validar_campo(validacoes_lista,'infoRetif.origRetif', infoRetif.origRetif.cdata, 1, '1;2;3')
            if 'tpProc' in dir(infoRetif): validacoes_lista = validar_campo(validacoes_lista,'infoRetif.tpProc', infoRetif.tpProc.cdata, 0, '1;2;3')
            if 'nrProc' in dir(infoRetif): validacoes_lista = validar_campo(validacoes_lista,'infoRetif.nrProc', infoRetif.nrProc.cdata, 0, '')

    if 'fimAfastamento' in dir(evtAfastTemp.infoAfastamento):
        for fimAfastamento in evtAfastTemp.infoAfastamento.fimAfastamento:
            
            if 'dtTermAfast' in dir(fimAfastamento): validacoes_lista = validar_campo(validacoes_lista,'fimAfastamento.dtTermAfast', fimAfastamento.dtTermAfast.cdata, 1, '')

    return validacoes_lista