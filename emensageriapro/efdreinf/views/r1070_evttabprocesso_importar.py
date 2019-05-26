#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r1070.models import *



def read_r1070_evttabprocesso_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r1070_evttabprocesso_obj(doc, status, validar)
    return dados



def read_r1070_evttabprocesso(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r1070_evttabprocesso_obj(doc, status, validar)
    return dados



def read_r1070_evttabprocesso_obj(doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r1070_evttabprocesso_dados = {}
    r1070_evttabprocesso_dados['status'] = status
    r1070_evttabprocesso_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r1070_evttabprocesso_dados['identidade'] = doc.Reinf.evtTabProcesso['id']
    evtTabProcesso = doc.Reinf.evtTabProcesso

    if 'inclusao' in dir(evtTabProcesso.infoProcesso): r1070_evttabprocesso_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabProcesso.infoProcesso): r1070_evttabprocesso_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabProcesso.infoProcesso): r1070_evttabprocesso_dados['operacao'] = 3
    
    try:
        r1070_evttabprocesso_dados['tpamb'] = evtTabProcesso.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r1070_evttabprocesso_dados['procemi'] = evtTabProcesso.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r1070_evttabprocesso_dados['verproc'] = evtTabProcesso.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r1070_evttabprocesso_dados['tpinsc'] = evtTabProcesso.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r1070_evttabprocesso_dados['nrinsc'] = evtTabProcesso.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
        
    r1070_evttabprocesso = r1070evtTabProcesso.objects.create(**r1070_evttabprocesso_dados)
    
    if 'inclusao' in dir(evtTabProcesso.infoProcesso):
    
        for inclusao in evtTabProcesso.infoProcesso.inclusao:
    
            r1070_inclusao_dados = {}
            r1070_inclusao_dados['r1070_evttabprocesso_id'] = r1070_evttabprocesso.id
            
            try:
                r1070_inclusao_dados['tpproc'] = inclusao.ideProcesso.tpProc.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_inclusao_dados['nrproc'] = inclusao.ideProcesso.nrProc.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_inclusao_dados['inivalid'] = inclusao.ideProcesso.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_inclusao_dados['fimvalid'] = inclusao.ideProcesso.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_inclusao_dados['indautoria'] = inclusao.ideProcesso.indAutoria.cdata
            except AttributeError: 
                pass
    
            r1070_inclusao = r1070inclusao.objects.create(**r1070_inclusao_dados)
            
            if 'infoSusp' in dir(inclusao.ideProcesso):
            
                for infoSusp in inclusao.ideProcesso.infoSusp:
            
                    r1070_inclusao_infosusp_dados = {}
                    r1070_inclusao_infosusp_dados['r1070_inclusao_id'] = r1070_inclusao.id
                    
                    try:
                        r1070_inclusao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_inclusao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_inclusao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_inclusao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    except AttributeError: 
                        pass
            
                    r1070_inclusao_infosusp = r1070inclusaoinfoSusp.objects.create(**r1070_inclusao_infosusp_dados)
            
            if 'dadosProcJud' in dir(inclusao.ideProcesso):
            
                for dadosProcJud in inclusao.ideProcesso.dadosProcJud:
            
                    r1070_inclusao_dadosprocjud_dados = {}
                    r1070_inclusao_dadosprocjud_dados['r1070_inclusao_id'] = r1070_inclusao.id
                    
                    try:
                        r1070_inclusao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_inclusao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_inclusao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    except AttributeError: 
                        pass
            
                    r1070_inclusao_dadosprocjud = r1070inclusaodadosProcJud.objects.create(**r1070_inclusao_dadosprocjud_dados)
    
    if 'alteracao' in dir(evtTabProcesso.infoProcesso):
    
        for alteracao in evtTabProcesso.infoProcesso.alteracao:
    
            r1070_alteracao_dados = {}
            r1070_alteracao_dados['r1070_evttabprocesso_id'] = r1070_evttabprocesso.id
            
            try:
                r1070_alteracao_dados['tpproc'] = alteracao.ideProcesso.tpProc.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_alteracao_dados['nrproc'] = alteracao.ideProcesso.nrProc.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_alteracao_dados['inivalid'] = alteracao.ideProcesso.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_alteracao_dados['fimvalid'] = alteracao.ideProcesso.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_alteracao_dados['indautoria'] = alteracao.ideProcesso.indAutoria.cdata
            except AttributeError: 
                pass
    
            r1070_alteracao = r1070alteracao.objects.create(**r1070_alteracao_dados)
            
            if 'infoSusp' in dir(alteracao.ideProcesso):
            
                for infoSusp in alteracao.ideProcesso.infoSusp:
            
                    r1070_alteracao_infosusp_dados = {}
                    r1070_alteracao_infosusp_dados['r1070_alteracao_id'] = r1070_alteracao.id
                    
                    try:
                        r1070_alteracao_infosusp_dados['codsusp'] = infoSusp.codSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_alteracao_infosusp_dados['indsusp'] = infoSusp.indSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_alteracao_infosusp_dados['dtdecisao'] = infoSusp.dtDecisao.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_alteracao_infosusp_dados['inddeposito'] = infoSusp.indDeposito.cdata
                    except AttributeError: 
                        pass
            
                    r1070_alteracao_infosusp = r1070alteracaoinfoSusp.objects.create(**r1070_alteracao_infosusp_dados)
            
            if 'dadosProcJud' in dir(alteracao.ideProcesso):
            
                for dadosProcJud in alteracao.ideProcesso.dadosProcJud:
            
                    r1070_alteracao_dadosprocjud_dados = {}
                    r1070_alteracao_dadosprocjud_dados['r1070_alteracao_id'] = r1070_alteracao.id
                    
                    try:
                        r1070_alteracao_dadosprocjud_dados['ufvara'] = dadosProcJud.ufVara.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_alteracao_dadosprocjud_dados['codmunic'] = dadosProcJud.codMunic.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_alteracao_dadosprocjud_dados['idvara'] = dadosProcJud.idVara.cdata
                    except AttributeError: 
                        pass
            
                    r1070_alteracao_dadosprocjud = r1070alteracaodadosProcJud.objects.create(**r1070_alteracao_dadosprocjud_dados)
            
            if 'novaValidade' in dir(alteracao):
            
                for novaValidade in alteracao.novaValidade:
            
                    r1070_alteracao_novavalidade_dados = {}
                    r1070_alteracao_novavalidade_dados['r1070_alteracao_id'] = r1070_alteracao.id
                    
                    try:
                        r1070_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1070_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: 
                        pass
            
                    r1070_alteracao_novavalidade = r1070alteracaonovaValidade.objects.create(**r1070_alteracao_novavalidade_dados)
    
    if 'exclusao' in dir(evtTabProcesso.infoProcesso):
    
        for exclusao in evtTabProcesso.infoProcesso.exclusao:
    
            r1070_exclusao_dados = {}
            r1070_exclusao_dados['r1070_evttabprocesso_id'] = r1070_evttabprocesso.id
            
            try:
                r1070_exclusao_dados['tpproc'] = exclusao.ideProcesso.tpProc.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_exclusao_dados['nrproc'] = exclusao.ideProcesso.nrProc.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_exclusao_dados['inivalid'] = exclusao.ideProcesso.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1070_exclusao_dados['fimvalid'] = exclusao.ideProcesso.fimValid.cdata
            except AttributeError: 
                pass
    
            r1070_exclusao = r1070exclusao.objects.create(**r1070_exclusao_dados)    
    r1070_evttabprocesso_dados['evento'] = 'r1070'
    r1070_evttabprocesso_dados['id'] = r1070_evttabprocesso.id
    r1070_evttabprocesso_dados['identidade_evento'] = doc.Reinf.evtTabProcesso['id']
    r1070_evttabprocesso_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r1070_evttabprocesso_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(r1070_evttabprocesso.id)
    return r1070_evttabprocesso_dados