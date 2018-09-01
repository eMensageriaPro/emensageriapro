#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1035_evttabcarreira(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabCarreira = doc.eSocial.evtTabCarreira
    
    if 'tpAmb' in dir(evtTabCarreira.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEvento.tpAmb', evtTabCarreira.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTabCarreira.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEvento.procEmi', evtTabCarreira.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTabCarreira.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEvento.verProc', evtTabCarreira.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTabCarreira.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEmpregador.tpInsc', evtTabCarreira.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTabCarreira.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabCarreira.ideEmpregador.nrInsc', evtTabCarreira.ideEmpregador.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtTabCarreira.infoCarreira):
        for inclusao in evtTabCarreira.infoCarreira.inclusao:
            
            if 'codCarreira' in dir(inclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideCarreira.codCarreira', inclusao.ideCarreira.codCarreira.cdata, 1, '')
            if 'iniValid' in dir(inclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideCarreira.iniValid', inclusao.ideCarreira.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideCarreira.fimValid', inclusao.ideCarreira.fimValid.cdata, 0, '')
            if 'dscCarreira' in dir(inclusao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCarreira.dscCarreira', inclusao.dadosCarreira.dscCarreira.cdata, 1, '')
            if 'leiCarr' in dir(inclusao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCarreira.leiCarr', inclusao.dadosCarreira.leiCarr.cdata, 0, '')
            if 'dtLeiCarr' in dir(inclusao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCarreira.dtLeiCarr', inclusao.dadosCarreira.dtLeiCarr.cdata, 1, '')
            if 'sitCarr' in dir(inclusao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCarreira.sitCarr', inclusao.dadosCarreira.sitCarr.cdata, 1, '1;2;3')

    if 'alteracao' in dir(evtTabCarreira.infoCarreira):
        for alteracao in evtTabCarreira.infoCarreira.alteracao:
            
            if 'codCarreira' in dir(alteracao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideCarreira.codCarreira', alteracao.ideCarreira.codCarreira.cdata, 1, '')
            if 'iniValid' in dir(alteracao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideCarreira.iniValid', alteracao.ideCarreira.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideCarreira.fimValid', alteracao.ideCarreira.fimValid.cdata, 0, '')
            if 'dscCarreira' in dir(alteracao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCarreira.dscCarreira', alteracao.dadosCarreira.dscCarreira.cdata, 1, '')
            if 'leiCarr' in dir(alteracao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCarreira.leiCarr', alteracao.dadosCarreira.leiCarr.cdata, 0, '')
            if 'dtLeiCarr' in dir(alteracao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCarreira.dtLeiCarr', alteracao.dadosCarreira.dtLeiCarr.cdata, 1, '')
            if 'sitCarr' in dir(alteracao.dadosCarreira): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCarreira.sitCarr', alteracao.dadosCarreira.sitCarr.cdata, 1, '1;2;3')

            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    
                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')
        
    if 'exclusao' in dir(evtTabCarreira.infoCarreira):
        for exclusao in evtTabCarreira.infoCarreira.exclusao:
            
            if 'codCarreira' in dir(exclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideCarreira.codCarreira', exclusao.ideCarreira.codCarreira.cdata, 1, '')
            if 'iniValid' in dir(exclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideCarreira.iniValid', exclusao.ideCarreira.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.ideCarreira): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideCarreira.fimValid', exclusao.ideCarreira.fimValid.cdata, 0, '')

    return validacoes_lista