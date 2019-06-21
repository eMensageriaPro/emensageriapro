#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1020.models import *



def read_s1020_evttablotacao_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1020_evttablotacao_obj(request, doc, status, validar)
    return dados



def read_s1020_evttablotacao(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1020_evttablotacao_obj(request, doc, status, validar)

    s1020evtTabLotacao.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1020_evttablotacao_obj(request, doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1020_evttablotacao_dados = {}
    s1020_evttablotacao_dados['status'] = status
    s1020_evttablotacao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1020_evttablotacao_dados['identidade'] = doc.eSocial.evtTabLotacao['Id']
    evtTabLotacao = doc.eSocial.evtTabLotacao

    if 'inclusao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 3
    
    try:
        s1020_evttablotacao_dados['tpamb'] = evtTabLotacao.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1020_evttablotacao_dados['procemi'] = evtTabLotacao.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1020_evttablotacao_dados['verproc'] = evtTabLotacao.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1020_evttablotacao_dados['tpinsc'] = evtTabLotacao.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1020_evttablotacao_dados['nrinsc'] = evtTabLotacao.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
        
    s1020_evttablotacao = s1020evtTabLotacao.objects.create(**s1020_evttablotacao_dados)
    
    if 'infoLotacao' in dir(evtTabLotacao) and 'inclusao' in dir(evtTabLotacao.infoLotacao):
    
        for inclusao in evtTabLotacao.infoLotacao.inclusao:
    
            s1020_inclusao_dados = {}
            s1020_inclusao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao.id
            
            try:
                s1020_inclusao_dados['codlotacao'] = inclusao.ideLotacao.codLotacao.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_inclusao_dados['inivalid'] = inclusao.ideLotacao.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_inclusao_dados['fimvalid'] = inclusao.ideLotacao.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_inclusao_dados['tplotacao'] = inclusao.dadosLotacao.tpLotacao.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_inclusao_dados['tpinsc'] = inclusao.dadosLotacao.tpInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_inclusao_dados['nrinsc'] = inclusao.dadosLotacao.nrInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_inclusao_dados['fpas'] = inclusao.dadosLotacao.fpasLotacao.fpas.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_inclusao_dados['codtercs'] = inclusao.dadosLotacao.fpasLotacao.codTercs.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_inclusao_dados['codtercssusp'] = inclusao.dadosLotacao.fpasLotacao.codTercsSusp.cdata
            except AttributeError: 
                pass
    
            s1020_inclusao = s1020inclusao.objects.create(**s1020_inclusao_dados)
            
            if 'dadosLotacao' in dir(inclusao) and 'fpasLotacao' in dir(inclusao.dadosLotacao) and 'infoProcJudTerceiros' in dir(inclusao.dadosLotacao.fpasLotacao):
            
                for infoProcJudTerceiros in inclusao.dadosLotacao.fpasLotacao.infoProcJudTerceiros:
            
                    s1020_inclusao_infoprocjudterceiros_dados = {}
                    s1020_inclusao_infoprocjudterceiros_dados['s1020_inclusao_id'] = s1020_inclusao.id
            
                    s1020_inclusao_infoprocjudterceiros = s1020inclusaoinfoProcJudTerceiros.objects.create(**s1020_inclusao_infoprocjudterceiros_dados)
                    
                    if 'procJudTerceiro' in dir(infoProcJudTerceiros):
                    
                        for procJudTerceiro in infoProcJudTerceiros.procJudTerceiro:
                    
                            s1020_inclusao_procjudterceiro_dados = {}
                            s1020_inclusao_procjudterceiro_dados['s1020_inclusao_infoprocjudterceiros_id'] = s1020_inclusao_infoprocjudterceiros.id
                            
                            try:
                                s1020_inclusao_procjudterceiro_dados['codterc'] = procJudTerceiro.codTerc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1020_inclusao_procjudterceiro_dados['nrprocjud'] = procJudTerceiro.nrProcJud.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1020_inclusao_procjudterceiro_dados['codsusp'] = procJudTerceiro.codSusp.cdata
                            except AttributeError: 
                                pass
                    
                            s1020_inclusao_procjudterceiro = s1020inclusaoprocJudTerceiro.objects.create(**s1020_inclusao_procjudterceiro_dados)
            
            if 'dadosLotacao' in dir(inclusao) and 'infoEmprParcial' in dir(inclusao.dadosLotacao):
            
                for infoEmprParcial in inclusao.dadosLotacao.infoEmprParcial:
            
                    s1020_inclusao_infoemprparcial_dados = {}
                    s1020_inclusao_infoemprparcial_dados['s1020_inclusao_id'] = s1020_inclusao.id
                    
                    try:
                        s1020_inclusao_infoemprparcial_dados['tpinsccontrat'] = infoEmprParcial.tpInscContrat.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1020_inclusao_infoemprparcial_dados['nrinsccontrat'] = infoEmprParcial.nrInscContrat.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1020_inclusao_infoemprparcial_dados['tpinscprop'] = infoEmprParcial.tpInscProp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1020_inclusao_infoemprparcial_dados['nrinscprop'] = infoEmprParcial.nrInscProp.cdata
                    except AttributeError: 
                        pass
            
                    s1020_inclusao_infoemprparcial = s1020inclusaoinfoEmprParcial.objects.create(**s1020_inclusao_infoemprparcial_dados)
    
    if 'infoLotacao' in dir(evtTabLotacao) and 'alteracao' in dir(evtTabLotacao.infoLotacao):
    
        for alteracao in evtTabLotacao.infoLotacao.alteracao:
    
            s1020_alteracao_dados = {}
            s1020_alteracao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao.id
            
            try:
                s1020_alteracao_dados['codlotacao'] = alteracao.ideLotacao.codLotacao.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_alteracao_dados['inivalid'] = alteracao.ideLotacao.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_alteracao_dados['fimvalid'] = alteracao.ideLotacao.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_alteracao_dados['tplotacao'] = alteracao.dadosLotacao.tpLotacao.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_alteracao_dados['tpinsc'] = alteracao.dadosLotacao.tpInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_alteracao_dados['nrinsc'] = alteracao.dadosLotacao.nrInsc.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_alteracao_dados['fpas'] = alteracao.dadosLotacao.fpasLotacao.fpas.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_alteracao_dados['codtercs'] = alteracao.dadosLotacao.fpasLotacao.codTercs.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_alteracao_dados['codtercssusp'] = alteracao.dadosLotacao.fpasLotacao.codTercsSusp.cdata
            except AttributeError: 
                pass
    
            s1020_alteracao = s1020alteracao.objects.create(**s1020_alteracao_dados)
            
            if 'dadosLotacao' in dir(alteracao) and 'fpasLotacao' in dir(alteracao.dadosLotacao) and 'infoProcJudTerceiros' in dir(alteracao.dadosLotacao.fpasLotacao):
            
                for infoProcJudTerceiros in alteracao.dadosLotacao.fpasLotacao.infoProcJudTerceiros:
            
                    s1020_alteracao_infoprocjudterceiros_dados = {}
                    s1020_alteracao_infoprocjudterceiros_dados['s1020_alteracao_id'] = s1020_alteracao.id
            
                    s1020_alteracao_infoprocjudterceiros = s1020alteracaoinfoProcJudTerceiros.objects.create(**s1020_alteracao_infoprocjudterceiros_dados)
                    
                    if 'procJudTerceiro' in dir(infoProcJudTerceiros):
                    
                        for procJudTerceiro in infoProcJudTerceiros.procJudTerceiro:
                    
                            s1020_alteracao_procjudterceiro_dados = {}
                            s1020_alteracao_procjudterceiro_dados['s1020_alteracao_infoprocjudterceiros_id'] = s1020_alteracao_infoprocjudterceiros.id
                            
                            try:
                                s1020_alteracao_procjudterceiro_dados['codterc'] = procJudTerceiro.codTerc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1020_alteracao_procjudterceiro_dados['nrprocjud'] = procJudTerceiro.nrProcJud.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1020_alteracao_procjudterceiro_dados['codsusp'] = procJudTerceiro.codSusp.cdata
                            except AttributeError: 
                                pass
                    
                            s1020_alteracao_procjudterceiro = s1020alteracaoprocJudTerceiro.objects.create(**s1020_alteracao_procjudterceiro_dados)
            
            if 'dadosLotacao' in dir(alteracao) and 'infoEmprParcial' in dir(alteracao.dadosLotacao):
            
                for infoEmprParcial in alteracao.dadosLotacao.infoEmprParcial:
            
                    s1020_alteracao_infoemprparcial_dados = {}
                    s1020_alteracao_infoemprparcial_dados['s1020_alteracao_id'] = s1020_alteracao.id
                    
                    try:
                        s1020_alteracao_infoemprparcial_dados['tpinsccontrat'] = infoEmprParcial.tpInscContrat.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1020_alteracao_infoemprparcial_dados['nrinsccontrat'] = infoEmprParcial.nrInscContrat.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1020_alteracao_infoemprparcial_dados['tpinscprop'] = infoEmprParcial.tpInscProp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1020_alteracao_infoemprparcial_dados['nrinscprop'] = infoEmprParcial.nrInscProp.cdata
                    except AttributeError: 
                        pass
            
                    s1020_alteracao_infoemprparcial = s1020alteracaoinfoEmprParcial.objects.create(**s1020_alteracao_infoemprparcial_dados)
            
            if 'novaValidade' in dir(alteracao):
            
                for novaValidade in alteracao.novaValidade:
            
                    s1020_alteracao_novavalidade_dados = {}
                    s1020_alteracao_novavalidade_dados['s1020_alteracao_id'] = s1020_alteracao.id
                    
                    try:
                        s1020_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1020_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: 
                        pass
            
                    s1020_alteracao_novavalidade = s1020alteracaonovaValidade.objects.create(**s1020_alteracao_novavalidade_dados)
    
    if 'infoLotacao' in dir(evtTabLotacao) and 'exclusao' in dir(evtTabLotacao.infoLotacao):
    
        for exclusao in evtTabLotacao.infoLotacao.exclusao:
    
            s1020_exclusao_dados = {}
            s1020_exclusao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao.id
            
            try:
                s1020_exclusao_dados['codlotacao'] = exclusao.ideLotacao.codLotacao.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_exclusao_dados['inivalid'] = exclusao.ideLotacao.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                s1020_exclusao_dados['fimvalid'] = exclusao.ideLotacao.fimValid.cdata
            except AttributeError: 
                pass
    
            s1020_exclusao = s1020exclusao.objects.create(**s1020_exclusao_dados)    
    s1020_evttablotacao_dados['evento'] = 's1020'
    s1020_evttablotacao_dados['id'] = s1020_evttablotacao.id
    s1020_evttablotacao_dados['identidade_evento'] = doc.eSocial.evtTabLotacao['Id']
    s1020_evttablotacao_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1020_evttablotacao_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, s1020_evttablotacao.id)
    
    return s1020_evttablotacao_dados