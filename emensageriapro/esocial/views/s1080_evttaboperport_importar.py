#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1080.models import *



def read_s1080_evttaboperport_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1080_evttaboperport_obj(doc, status, validar)
    return dados



def read_s1080_evttaboperport(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1080_evttaboperport_obj(doc, status, validar)
    return dados



def read_s1080_evttaboperport_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1080_evttaboperport_dados = {}
    s1080_evttaboperport_dados['status'] = status
    s1080_evttaboperport_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1080_evttaboperport_dados['identidade'] = doc.eSocial.evtTabOperPort['Id']
    evtTabOperPort = doc.eSocial.evtTabOperPort

    if 'inclusao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 3
    
    try:
        s1080_evttaboperport_dados['tpamb'] = evtTabOperPort.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1080_evttaboperport_dados['procemi'] = evtTabOperPort.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1080_evttaboperport_dados['verproc'] = evtTabOperPort.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1080_evttaboperport_dados['tpinsc'] = evtTabOperPort.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1080_evttaboperport_dados['nrinsc'] = evtTabOperPort.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
        
    s1080_evttaboperport = s1080evtTabOperPort.objects.create(**s1080_evttaboperport_dados)
    
    if 'inclusao' in dir(evtTabOperPort.infoOperPortuario):
    
        for inclusao in evtTabOperPort.infoOperPortuario.inclusao:
    
            s1080_inclusao_dados = {}
            s1080_inclusao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport.id
            
            try:
                s1080_inclusao_dados['cnpjopportuario'] = inclusao.ideOperPortuario.cnpjOpPortuario.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_inclusao_dados['inivalid'] = inclusao.ideOperPortuario.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_inclusao_dados['fimvalid'] = inclusao.ideOperPortuario.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_inclusao_dados['aliqrat'] = inclusao.dadosOperPortuario.aliqRat.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_inclusao_dados['fap'] = inclusao.dadosOperPortuario.fap.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_inclusao_dados['aliqratajust'] = inclusao.dadosOperPortuario.aliqRatAjust.cdata
            except AttributeError: 
                pass
    
            s1080_inclusao = s1080inclusao.objects.create(**s1080_inclusao_dados)
    
    if 'alteracao' in dir(evtTabOperPort.infoOperPortuario):
    
        for alteracao in evtTabOperPort.infoOperPortuario.alteracao:
    
            s1080_alteracao_dados = {}
            s1080_alteracao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport.id
            
            try:
                s1080_alteracao_dados['cnpjopportuario'] = alteracao.ideOperPortuario.cnpjOpPortuario.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_alteracao_dados['inivalid'] = alteracao.ideOperPortuario.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_alteracao_dados['fimvalid'] = alteracao.ideOperPortuario.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_alteracao_dados['aliqrat'] = alteracao.dadosOperPortuario.aliqRat.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_alteracao_dados['fap'] = alteracao.dadosOperPortuario.fap.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_alteracao_dados['aliqratajust'] = alteracao.dadosOperPortuario.aliqRatAjust.cdata
            except AttributeError: 
                pass
    
            s1080_alteracao = s1080alteracao.objects.create(**s1080_alteracao_dados)
            
            if 'novaValidade' in dir(alteracao):
            
                for novaValidade in alteracao.novaValidade:
            
                    s1080_alteracao_novavalidade_dados = {}
                    s1080_alteracao_novavalidade_dados['s1080_alteracao_id'] = s1080_alteracao.id
                    
                    try:
                        s1080_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1080_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: 
                        pass
            
                    s1080_alteracao_novavalidade = s1080alteracaonovaValidade.objects.create(**s1080_alteracao_novavalidade_dados)
    
    if 'exclusao' in dir(evtTabOperPort.infoOperPortuario):
    
        for exclusao in evtTabOperPort.infoOperPortuario.exclusao:
    
            s1080_exclusao_dados = {}
            s1080_exclusao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport.id
            
            try:
                s1080_exclusao_dados['cnpjopportuario'] = exclusao.ideOperPortuario.cnpjOpPortuario.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_exclusao_dados['inivalid'] = exclusao.ideOperPortuario.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1080_exclusao_dados['fimvalid'] = exclusao.ideOperPortuario.fimValid.cdata
            except AttributeError: 
                pass
    
            s1080_exclusao = s1080exclusao.objects.create(**s1080_exclusao_dados)    
    s1080_evttaboperport_dados['evento'] = 's1080'
    s1080_evttaboperport_dados['id'] = s1080_evttaboperport.id
    s1080_evttaboperport_dados['identidade_evento'] = doc.eSocial.evtTabOperPort['Id']
    s1080_evttaboperport_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1080_evttaboperport_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s1080_evttaboperport.id)
    return s1080_evttaboperport_dados