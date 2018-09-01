#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_r1000_evtinfocontri(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtInfoContri = doc.Reinf.evtInfoContri
    
    if 'tpAmb' in dir(evtInfoContri.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoContri.ideEvento.tpAmb', evtInfoContri.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtInfoContri.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoContri.ideEvento.procEmi', evtInfoContri.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtInfoContri.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtInfoContri.ideEvento.verProc', evtInfoContri.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtInfoContri.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtInfoContri.ideContri.tpInsc', evtInfoContri.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtInfoContri.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtInfoContri.ideContri.nrInsc', evtInfoContri.ideContri.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtInfoContri.infoContri):
        for inclusao in evtInfoContri.infoContri.inclusao:
            
            if 'iniValid' in dir(inclusao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'inclusao.idePeriodo.iniValid', inclusao.idePeriodo.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'inclusao.idePeriodo.fimValid', inclusao.idePeriodo.fimValid.cdata, 0, '')
            if 'classTrib' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.classTrib', inclusao.infoCadastro.classTrib.cdata, 1, '')
            if 'indEscrituracao' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indEscrituracao', inclusao.infoCadastro.indEscrituracao.cdata, 1, '0;1')
            if 'indDesoneracao' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indDesoneracao', inclusao.infoCadastro.indDesoneracao.cdata, 1, '0;1')
            if 'indAcordoIsenMulta' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indAcordoIsenMulta', inclusao.infoCadastro.indAcordoIsenMulta.cdata, 1, '0;1')
            if 'indSitPJ' in dir(inclusao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.indSitPJ', inclusao.infoCadastro.indSitPJ.cdata, 0, '0;1;2;3;4')
            if 'nmCtt' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.nmCtt', inclusao.infoCadastro.contato.nmCtt.cdata, 1, '')
            if 'cpfCtt' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.cpfCtt', inclusao.infoCadastro.contato.cpfCtt.cdata, 1, '')
            if 'foneFixo' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.foneFixo', inclusao.infoCadastro.contato.foneFixo.cdata, 0, '')
            if 'foneCel' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.foneCel', inclusao.infoCadastro.contato.foneCel.cdata, 0, '')
            if 'email' in dir(inclusao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'inclusao.infoCadastro.contato.email', inclusao.infoCadastro.contato.email.cdata, 0, '')


            if 'softHouse' in dir(inclusao.infoCadastro):
                for softHouse in inclusao.infoCadastro.softHouse:
                    
                    if 'cnpjSoftHouse' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.cnpjSoftHouse', softHouse.cnpjSoftHouse.cdata, 1, '')
                    if 'nmRazao' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.nmRazao', softHouse.nmRazao.cdata, 1, '')
                    if 'nmCont' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.nmCont', softHouse.nmCont.cdata, 1, '')
                    if 'telefone' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.telefone', softHouse.telefone.cdata, 0, '')
                    if 'email' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.email', softHouse.email.cdata, 0, '')
        
        
            if 'infoEFR' in dir(inclusao.infoCadastro):
                for infoEFR in inclusao.infoCadastro.infoEFR:
                    
                    if 'ideEFR' in dir(infoEFR): validacoes_lista = validar_campo(validacoes_lista,'infoEFR.ideEFR', infoEFR.ideEFR.cdata, 1, 'S;N')
                    if 'cnpjEFR' in dir(infoEFR): validacoes_lista = validar_campo(validacoes_lista,'infoEFR.cnpjEFR', infoEFR.cnpjEFR.cdata, 0, '')
        
        
    if 'alteracao' in dir(evtInfoContri.infoContri):
        for alteracao in evtInfoContri.infoContri.alteracao:
            
            if 'iniValid' in dir(alteracao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'alteracao.idePeriodo.iniValid', alteracao.idePeriodo.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'alteracao.idePeriodo.fimValid', alteracao.idePeriodo.fimValid.cdata, 0, '')
            if 'classTrib' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.classTrib', alteracao.infoCadastro.classTrib.cdata, 1, '')
            if 'indEscrituracao' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indEscrituracao', alteracao.infoCadastro.indEscrituracao.cdata, 1, '0;1')
            if 'indDesoneracao' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indDesoneracao', alteracao.infoCadastro.indDesoneracao.cdata, 1, '0;1')
            if 'indAcordoIsenMulta' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indAcordoIsenMulta', alteracao.infoCadastro.indAcordoIsenMulta.cdata, 1, '0;1')
            if 'indSitPJ' in dir(alteracao.infoCadastro): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.indSitPJ', alteracao.infoCadastro.indSitPJ.cdata, 0, '0;1;2;3;4')
            if 'nmCtt' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.nmCtt', alteracao.infoCadastro.contato.nmCtt.cdata, 1, '')
            if 'cpfCtt' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.cpfCtt', alteracao.infoCadastro.contato.cpfCtt.cdata, 1, '')
            if 'foneFixo' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.foneFixo', alteracao.infoCadastro.contato.foneFixo.cdata, 0, '')
            if 'foneCel' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.foneCel', alteracao.infoCadastro.contato.foneCel.cdata, 0, '')
            if 'email' in dir(alteracao.infoCadastro.contato): validacoes_lista = validar_campo(validacoes_lista,'alteracao.infoCadastro.contato.email', alteracao.infoCadastro.contato.email.cdata, 0, '')


            if 'softHouse' in dir(alteracao.infoCadastro):
                for softHouse in alteracao.infoCadastro.softHouse:
                    
                    if 'cnpjSoftHouse' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.cnpjSoftHouse', softHouse.cnpjSoftHouse.cdata, 1, '')
                    if 'nmRazao' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.nmRazao', softHouse.nmRazao.cdata, 1, '')
                    if 'nmCont' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.nmCont', softHouse.nmCont.cdata, 1, '')
                    if 'telefone' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.telefone', softHouse.telefone.cdata, 0, '')
                    if 'email' in dir(softHouse): validacoes_lista = validar_campo(validacoes_lista,'softHouse.email', softHouse.email.cdata, 0, '')
        
        
            if 'infoEFR' in dir(alteracao.infoCadastro):
                for infoEFR in alteracao.infoCadastro.infoEFR:
                    
                    if 'ideEFR' in dir(infoEFR): validacoes_lista = validar_campo(validacoes_lista,'infoEFR.ideEFR', infoEFR.ideEFR.cdata, 1, 'S;N')
                    if 'cnpjEFR' in dir(infoEFR): validacoes_lista = validar_campo(validacoes_lista,'infoEFR.cnpjEFR', infoEFR.cnpjEFR.cdata, 0, '')
        
        
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    
                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')
        
        
    if 'exclusao' in dir(evtInfoContri.infoContri):
        for exclusao in evtInfoContri.infoContri.exclusao:
            
            if 'iniValid' in dir(exclusao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'exclusao.idePeriodo.iniValid', exclusao.idePeriodo.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.idePeriodo): validacoes_lista = validar_campo(validacoes_lista,'exclusao.idePeriodo.fimValid', exclusao.idePeriodo.fimValid.cdata, 0, '')


    return validacoes_lista