#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1050.models import *



def read_s1050_evttabhortur_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1050_evttabhortur_obj(request, doc, status, validar)
    return dados



def read_s1050_evttabhortur(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1050_evttabhortur_obj(request, doc, status, validar)

    s1050evtTabHorTur.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1050_evttabhortur_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1050_evttabhortur_dados = {}
    s1050_evttabhortur_dados['status'] = status
    s1050_evttabhortur_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1050_evttabhortur_dados['identidade'] = doc.eSocial.evtTabHorTur['Id']
    evtTabHorTur = doc.eSocial.evtTabHorTur

    if 'inclusao' in dir(evtTabHorTur.infoHorContratual): s1050_evttabhortur_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabHorTur.infoHorContratual): s1050_evttabhortur_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabHorTur.infoHorContratual): s1050_evttabhortur_dados['operacao'] = 3
    
    try:
        s1050_evttabhortur_dados['tpamb'] = evtTabHorTur.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1050_evttabhortur_dados['procemi'] = evtTabHorTur.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1050_evttabhortur_dados['verproc'] = evtTabHorTur.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1050_evttabhortur_dados['tpinsc'] = evtTabHorTur.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1050_evttabhortur_dados['nrinsc'] = evtTabHorTur.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
        
    s1050_evttabhortur = s1050evtTabHorTur.objects.create(**s1050_evttabhortur_dados)
    
    if 'infoHorContratual' in dir(evtTabHorTur) and 'inclusao' in dir(evtTabHorTur.infoHorContratual):
    
        for inclusao in evtTabHorTur.infoHorContratual.inclusao:
    
            s1050_inclusao_dados = {}
            s1050_inclusao_dados['s1050_evttabhortur_id'] = s1050_evttabhortur.id
            
            try:
                s1050_inclusao_dados['codhorcontrat'] = inclusao.ideHorContratual.codHorContrat.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_inclusao_dados['inivalid'] = inclusao.ideHorContratual.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_inclusao_dados['fimvalid'] = inclusao.ideHorContratual.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_inclusao_dados['hrentr'] = inclusao.dadosHorContratual.hrEntr.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_inclusao_dados['hrsaida'] = inclusao.dadosHorContratual.hrSaida.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_inclusao_dados['durjornada'] = inclusao.dadosHorContratual.durJornada.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_inclusao_dados['perhorflexivel'] = inclusao.dadosHorContratual.perHorFlexivel.cdata
            except AttributeError: 
                pass
    
            s1050_inclusao = s1050inclusao.objects.create(**s1050_inclusao_dados)
            
            if 'dadosHorContratual' in dir(inclusao) and 'horarioIntervalo' in dir(inclusao.dadosHorContratual):
            
                for horarioIntervalo in inclusao.dadosHorContratual.horarioIntervalo:
            
                    s1050_inclusao_horariointervalo_dados = {}
                    s1050_inclusao_horariointervalo_dados['s1050_inclusao_id'] = s1050_inclusao.id
                    
                    try:
                        s1050_inclusao_horariointervalo_dados['tpinterv'] = horarioIntervalo.tpInterv.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1050_inclusao_horariointervalo_dados['durinterv'] = horarioIntervalo.durInterv.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1050_inclusao_horariointervalo_dados['iniinterv'] = horarioIntervalo.iniInterv.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1050_inclusao_horariointervalo_dados['terminterv'] = horarioIntervalo.termInterv.cdata
                    except AttributeError: 
                        pass
            
                    s1050_inclusao_horariointervalo = s1050inclusaohorarioIntervalo.objects.create(**s1050_inclusao_horariointervalo_dados)
    
    if 'infoHorContratual' in dir(evtTabHorTur) and 'alteracao' in dir(evtTabHorTur.infoHorContratual):
    
        for alteracao in evtTabHorTur.infoHorContratual.alteracao:
    
            s1050_alteracao_dados = {}
            s1050_alteracao_dados['s1050_evttabhortur_id'] = s1050_evttabhortur.id
            
            try:
                s1050_alteracao_dados['codhorcontrat'] = alteracao.ideHorContratual.codHorContrat.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_alteracao_dados['inivalid'] = alteracao.ideHorContratual.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_alteracao_dados['fimvalid'] = alteracao.ideHorContratual.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_alteracao_dados['hrentr'] = alteracao.dadosHorContratual.hrEntr.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_alteracao_dados['hrsaida'] = alteracao.dadosHorContratual.hrSaida.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_alteracao_dados['durjornada'] = alteracao.dadosHorContratual.durJornada.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_alteracao_dados['perhorflexivel'] = alteracao.dadosHorContratual.perHorFlexivel.cdata
            except AttributeError: 
                pass
    
            s1050_alteracao = s1050alteracao.objects.create(**s1050_alteracao_dados)
            
            if 'dadosHorContratual' in dir(alteracao) and 'horarioIntervalo' in dir(alteracao.dadosHorContratual):
            
                for horarioIntervalo in alteracao.dadosHorContratual.horarioIntervalo:
            
                    s1050_alteracao_horariointervalo_dados = {}
                    s1050_alteracao_horariointervalo_dados['s1050_alteracao_id'] = s1050_alteracao.id
                    
                    try:
                        s1050_alteracao_horariointervalo_dados['tpinterv'] = horarioIntervalo.tpInterv.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1050_alteracao_horariointervalo_dados['durinterv'] = horarioIntervalo.durInterv.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1050_alteracao_horariointervalo_dados['iniinterv'] = horarioIntervalo.iniInterv.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1050_alteracao_horariointervalo_dados['terminterv'] = horarioIntervalo.termInterv.cdata
                    except AttributeError: 
                        pass
            
                    s1050_alteracao_horariointervalo = s1050alteracaohorarioIntervalo.objects.create(**s1050_alteracao_horariointervalo_dados)
            
            if 'novaValidade' in dir(alteracao):
            
                for novaValidade in alteracao.novaValidade:
            
                    s1050_alteracao_novavalidade_dados = {}
                    s1050_alteracao_novavalidade_dados['s1050_alteracao_id'] = s1050_alteracao.id
                    
                    try:
                        s1050_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1050_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: 
                        pass
            
                    s1050_alteracao_novavalidade = s1050alteracaonovaValidade.objects.create(**s1050_alteracao_novavalidade_dados)
    
    if 'infoHorContratual' in dir(evtTabHorTur) and 'exclusao' in dir(evtTabHorTur.infoHorContratual):
    
        for exclusao in evtTabHorTur.infoHorContratual.exclusao:
    
            s1050_exclusao_dados = {}
            s1050_exclusao_dados['s1050_evttabhortur_id'] = s1050_evttabhortur.id
            
            try:
                s1050_exclusao_dados['codhorcontrat'] = exclusao.ideHorContratual.codHorContrat.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_exclusao_dados['inivalid'] = exclusao.ideHorContratual.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1050_exclusao_dados['fimvalid'] = exclusao.ideHorContratual.fimValid.cdata
            except AttributeError: 
                pass
    
            s1050_exclusao = s1050exclusao.objects.create(**s1050_exclusao_dados)    
    s1050_evttabhortur_dados['evento'] = 's1050'
    s1050_evttabhortur_dados['id'] = s1050_evttabhortur.id
    s1050_evttabhortur_dados['identidade_evento'] = doc.eSocial.evtTabHorTur['Id']
    s1050_evttabhortur_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1050_evttabhortur_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s1050_evttabhortur.id)
    
    return s1050_evttabhortur_dados