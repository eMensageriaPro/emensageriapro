#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1035.models import *



def read_s1035_evttabcarreira_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1035_evttabcarreira_obj(doc, status, validar)
    return dados



def read_s1035_evttabcarreira(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1035_evttabcarreira_obj(doc, status, validar)
    return dados



def read_s1035_evttabcarreira_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1035_evttabcarreira_dados = {}
    s1035_evttabcarreira_dados['status'] = status
    s1035_evttabcarreira_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1035_evttabcarreira_dados['identidade'] = doc.eSocial.evtTabCarreira['Id']
    evtTabCarreira = doc.eSocial.evtTabCarreira

    if 'inclusao' in dir(evtTabCarreira.infoCarreira): s1035_evttabcarreira_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabCarreira.infoCarreira): s1035_evttabcarreira_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabCarreira.infoCarreira): s1035_evttabcarreira_dados['operacao'] = 3
    
    try:
        s1035_evttabcarreira_dados['tpamb'] = evtTabCarreira.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1035_evttabcarreira_dados['procemi'] = evtTabCarreira.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1035_evttabcarreira_dados['verproc'] = evtTabCarreira.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1035_evttabcarreira_dados['tpinsc'] = evtTabCarreira.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1035_evttabcarreira_dados['nrinsc'] = evtTabCarreira.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
        
    s1035_evttabcarreira = s1035evtTabCarreira.objects.create(**s1035_evttabcarreira_dados)
    
    if 'inclusao' in dir(evtTabCarreira.infoCarreira):
    
        for inclusao in evtTabCarreira.infoCarreira.inclusao:
    
            s1035_inclusao_dados = {}
            s1035_inclusao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira.id
            
            try:
                s1035_inclusao_dados['codcarreira'] = inclusao.ideCarreira.codCarreira.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_inclusao_dados['inivalid'] = inclusao.ideCarreira.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_inclusao_dados['fimvalid'] = inclusao.ideCarreira.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_inclusao_dados['dsccarreira'] = inclusao.dadosCarreira.dscCarreira.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_inclusao_dados['leicarr'] = inclusao.dadosCarreira.leiCarr.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_inclusao_dados['dtleicarr'] = inclusao.dadosCarreira.dtLeiCarr.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_inclusao_dados['sitcarr'] = inclusao.dadosCarreira.sitCarr.cdata
            except AttributeError: 
                pass
    
            s1035_inclusao = s1035inclusao.objects.create(**s1035_inclusao_dados)
    
    if 'alteracao' in dir(evtTabCarreira.infoCarreira):
    
        for alteracao in evtTabCarreira.infoCarreira.alteracao:
    
            s1035_alteracao_dados = {}
            s1035_alteracao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira.id
            
            try:
                s1035_alteracao_dados['codcarreira'] = alteracao.ideCarreira.codCarreira.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_alteracao_dados['inivalid'] = alteracao.ideCarreira.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_alteracao_dados['fimvalid'] = alteracao.ideCarreira.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_alteracao_dados['dsccarreira'] = alteracao.dadosCarreira.dscCarreira.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_alteracao_dados['leicarr'] = alteracao.dadosCarreira.leiCarr.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_alteracao_dados['dtleicarr'] = alteracao.dadosCarreira.dtLeiCarr.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_alteracao_dados['sitcarr'] = alteracao.dadosCarreira.sitCarr.cdata
            except AttributeError: 
                pass
    
            s1035_alteracao = s1035alteracao.objects.create(**s1035_alteracao_dados)
            
            if 'novaValidade' in dir(alteracao):
            
                for novaValidade in alteracao.novaValidade:
            
                    s1035_alteracao_novavalidade_dados = {}
                    s1035_alteracao_novavalidade_dados['s1035_alteracao_id'] = s1035_alteracao.id
                    
                    try:
                        s1035_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1035_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: 
                        pass
            
                    s1035_alteracao_novavalidade = s1035alteracaonovaValidade.objects.create(**s1035_alteracao_novavalidade_dados)
    
    if 'exclusao' in dir(evtTabCarreira.infoCarreira):
    
        for exclusao in evtTabCarreira.infoCarreira.exclusao:
    
            s1035_exclusao_dados = {}
            s1035_exclusao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira.id
            
            try:
                s1035_exclusao_dados['codcarreira'] = exclusao.ideCarreira.codCarreira.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_exclusao_dados['inivalid'] = exclusao.ideCarreira.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1035_exclusao_dados['fimvalid'] = exclusao.ideCarreira.fimValid.cdata
            except AttributeError: 
                pass
    
            s1035_exclusao = s1035exclusao.objects.create(**s1035_exclusao_dados)    
    s1035_evttabcarreira_dados['evento'] = 's1035'
    s1035_evttabcarreira_dados['id'] = s1035_evttabcarreira.id
    s1035_evttabcarreira_dados['identidade_evento'] = doc.eSocial.evtTabCarreira['Id']
    s1035_evttabcarreira_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1035_evttabcarreira_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s1035_evttabcarreira.id)
    return s1035_evttabcarreira_dados