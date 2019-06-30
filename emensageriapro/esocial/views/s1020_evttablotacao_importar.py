#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1020.models import *
from emensageriapro.functions import read_from_xml



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
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1020_evttablotacao_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1020evtTabLotacao.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1020_evttablotacao_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1020_evttablotacao_dados = {}
    s1020_evttablotacao_dados['status'] = status
    s1020_evttablotacao_dados['arquivo_original'] = 1
    if arquivo:
        s1020_evttablotacao_dados['arquivo'] = arquivo.arquivo
    s1020_evttablotacao_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1020_evttablotacao_dados['identidade'] = doc.eSocial.evtTabLotacao['Id']
    evtTabLotacao = doc.eSocial.evtTabLotacao

    if 'inclusao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabLotacao.infoLotacao): s1020_evttablotacao_dados['operacao'] = 3

    try:
        s1020_evttablotacao_dados['tpamb'] = read_from_xml(evtTabLotacao.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1020_evttablotacao_dados['procemi'] = read_from_xml(evtTabLotacao.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1020_evttablotacao_dados['verproc'] = read_from_xml(evtTabLotacao.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1020_evttablotacao_dados['tpinsc'] = read_from_xml(evtTabLotacao.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1020_evttablotacao_dados['nrinsc'] = read_from_xml(evtTabLotacao.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1020_evttablotacao = s1020evtTabLotacao.objects.create(**s1020_evttablotacao_dados)

    if 'infoLotacao' in dir(evtTabLotacao) and 'inclusao' in dir(evtTabLotacao.infoLotacao):

        for inclusao in evtTabLotacao.infoLotacao.inclusao:

            s1020_inclusao_dados = {}
            s1020_inclusao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao.id

            try:
                s1020_inclusao_dados['codlotacao'] = read_from_xml(inclusao.ideLotacao.codLotacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideLotacao.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideLotacao.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_inclusao_dados['tplotacao'] = read_from_xml(inclusao.dadosLotacao.tpLotacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_inclusao_dados['tpinsc'] = read_from_xml(inclusao.dadosLotacao.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1020_inclusao_dados['nrinsc'] = read_from_xml(inclusao.dadosLotacao.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_inclusao_dados['fpas'] = read_from_xml(inclusao.dadosLotacao.fpasLotacao.fpas.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1020_inclusao_dados['codtercs'] = read_from_xml(inclusao.dadosLotacao.fpasLotacao.codTercs.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_inclusao_dados['codtercssusp'] = read_from_xml(inclusao.dadosLotacao.fpasLotacao.codTercsSusp.cdata, 'esocial', 'C', None)
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
                                s1020_inclusao_procjudterceiro_dados['codterc'] = read_from_xml(procJudTerceiro.codTerc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1020_inclusao_procjudterceiro_dados['nrprocjud'] = read_from_xml(procJudTerceiro.nrProcJud.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1020_inclusao_procjudterceiro_dados['codsusp'] = read_from_xml(procJudTerceiro.codSusp.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass

                            s1020_inclusao_procjudterceiro = s1020inclusaoprocJudTerceiro.objects.create(**s1020_inclusao_procjudterceiro_dados)

            if 'dadosLotacao' in dir(inclusao) and 'infoEmprParcial' in dir(inclusao.dadosLotacao):

                for infoEmprParcial in inclusao.dadosLotacao.infoEmprParcial:

                    s1020_inclusao_infoemprparcial_dados = {}
                    s1020_inclusao_infoemprparcial_dados['s1020_inclusao_id'] = s1020_inclusao.id

                    try:
                        s1020_inclusao_infoemprparcial_dados['tpinsccontrat'] = read_from_xml(infoEmprParcial.tpInscContrat.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1020_inclusao_infoemprparcial_dados['nrinsccontrat'] = read_from_xml(infoEmprParcial.nrInscContrat.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1020_inclusao_infoemprparcial_dados['tpinscprop'] = read_from_xml(infoEmprParcial.tpInscProp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1020_inclusao_infoemprparcial_dados['nrinscprop'] = read_from_xml(infoEmprParcial.nrInscProp.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1020_inclusao_infoemprparcial = s1020inclusaoinfoEmprParcial.objects.create(**s1020_inclusao_infoemprparcial_dados)

    if 'infoLotacao' in dir(evtTabLotacao) and 'alteracao' in dir(evtTabLotacao.infoLotacao):

        for alteracao in evtTabLotacao.infoLotacao.alteracao:

            s1020_alteracao_dados = {}
            s1020_alteracao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao.id

            try:
                s1020_alteracao_dados['codlotacao'] = read_from_xml(alteracao.ideLotacao.codLotacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideLotacao.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideLotacao.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_alteracao_dados['tplotacao'] = read_from_xml(alteracao.dadosLotacao.tpLotacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_alteracao_dados['tpinsc'] = read_from_xml(alteracao.dadosLotacao.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1020_alteracao_dados['nrinsc'] = read_from_xml(alteracao.dadosLotacao.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_alteracao_dados['fpas'] = read_from_xml(alteracao.dadosLotacao.fpasLotacao.fpas.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1020_alteracao_dados['codtercs'] = read_from_xml(alteracao.dadosLotacao.fpasLotacao.codTercs.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_alteracao_dados['codtercssusp'] = read_from_xml(alteracao.dadosLotacao.fpasLotacao.codTercsSusp.cdata, 'esocial', 'C', None)
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
                                s1020_alteracao_procjudterceiro_dados['codterc'] = read_from_xml(procJudTerceiro.codTerc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1020_alteracao_procjudterceiro_dados['nrprocjud'] = read_from_xml(procJudTerceiro.nrProcJud.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1020_alteracao_procjudterceiro_dados['codsusp'] = read_from_xml(procJudTerceiro.codSusp.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass

                            s1020_alteracao_procjudterceiro = s1020alteracaoprocJudTerceiro.objects.create(**s1020_alteracao_procjudterceiro_dados)

            if 'dadosLotacao' in dir(alteracao) and 'infoEmprParcial' in dir(alteracao.dadosLotacao):

                for infoEmprParcial in alteracao.dadosLotacao.infoEmprParcial:

                    s1020_alteracao_infoemprparcial_dados = {}
                    s1020_alteracao_infoemprparcial_dados['s1020_alteracao_id'] = s1020_alteracao.id

                    try:
                        s1020_alteracao_infoemprparcial_dados['tpinsccontrat'] = read_from_xml(infoEmprParcial.tpInscContrat.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1020_alteracao_infoemprparcial_dados['nrinsccontrat'] = read_from_xml(infoEmprParcial.nrInscContrat.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1020_alteracao_infoemprparcial_dados['tpinscprop'] = read_from_xml(infoEmprParcial.tpInscProp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1020_alteracao_infoemprparcial_dados['nrinscprop'] = read_from_xml(infoEmprParcial.nrInscProp.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1020_alteracao_infoemprparcial = s1020alteracaoinfoEmprParcial.objects.create(**s1020_alteracao_infoemprparcial_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1020_alteracao_novavalidade_dados = {}
                    s1020_alteracao_novavalidade_dados['s1020_alteracao_id'] = s1020_alteracao.id

                    try:
                        s1020_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1020_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1020_alteracao_novavalidade = s1020alteracaonovaValidade.objects.create(**s1020_alteracao_novavalidade_dados)

    if 'infoLotacao' in dir(evtTabLotacao) and 'exclusao' in dir(evtTabLotacao.infoLotacao):

        for exclusao in evtTabLotacao.infoLotacao.exclusao:

            s1020_exclusao_dados = {}
            s1020_exclusao_dados['s1020_evttablotacao_id'] = s1020_evttablotacao.id

            try:
                s1020_exclusao_dados['codlotacao'] = read_from_xml(exclusao.ideLotacao.codLotacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideLotacao.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1020_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideLotacao.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1020_exclusao = s1020exclusao.objects.create(**s1020_exclusao_dados)
    s1020_evttablotacao_dados['evento'] = 's1020'
    s1020_evttablotacao_dados['id'] = s1020_evttablotacao.id
    s1020_evttablotacao_dados['identidade_evento'] = doc.eSocial.evtTabLotacao['Id']

    from emensageriapro.esocial.views.s1020_evttablotacao_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1020_evttablotacao.id)

    return s1020_evttablotacao_dados