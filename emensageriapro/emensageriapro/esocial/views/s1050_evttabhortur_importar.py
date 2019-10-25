#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1050.models import *
from emensageriapro.functions import read_from_xml



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
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1050_evttabhortur_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1050evtTabHorTur.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1050_evttabhortur_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1050_evttabhortur_dados = {}
    s1050_evttabhortur_dados['status'] = status
    s1050_evttabhortur_dados['arquivo_original'] = 1
    if arquivo:
        s1050_evttabhortur_dados['arquivo'] = arquivo.arquivo
    s1050_evttabhortur_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1050_evttabhortur_dados['identidade'] = doc.eSocial.evtTabHorTur['Id']
    evtTabHorTur = doc.eSocial.evtTabHorTur

    if 'inclusao' in dir(evtTabHorTur.infoHorContratual): s1050_evttabhortur_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabHorTur.infoHorContratual): s1050_evttabhortur_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabHorTur.infoHorContratual): s1050_evttabhortur_dados['operacao'] = 3

    try:
        s1050_evttabhortur_dados['tpamb'] = read_from_xml(evtTabHorTur.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1050_evttabhortur_dados['procemi'] = read_from_xml(evtTabHorTur.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1050_evttabhortur_dados['verproc'] = read_from_xml(evtTabHorTur.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1050_evttabhortur_dados['tpinsc'] = read_from_xml(evtTabHorTur.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1050_evttabhortur_dados['nrinsc'] = read_from_xml(evtTabHorTur.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1050_evttabhortur = s1050evtTabHorTur.objects.create(**s1050_evttabhortur_dados)

    if 'infoHorContratual' in dir(evtTabHorTur) and 'inclusao' in dir(evtTabHorTur.infoHorContratual):

        for inclusao in evtTabHorTur.infoHorContratual.inclusao:

            s1050_inclusao_dados = {}
            s1050_inclusao_dados['s1050_evttabhortur_id'] = s1050_evttabhortur.id

            try:
                s1050_inclusao_dados['codhorcontrat'] = read_from_xml(inclusao.ideHorContratual.codHorContrat.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideHorContratual.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideHorContratual.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_inclusao_dados['hrentr'] = read_from_xml(inclusao.dadosHorContratual.hrEntr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_inclusao_dados['hrsaida'] = read_from_xml(inclusao.dadosHorContratual.hrSaida.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_inclusao_dados['durjornada'] = read_from_xml(inclusao.dadosHorContratual.durJornada.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1050_inclusao_dados['perhorflexivel'] = read_from_xml(inclusao.dadosHorContratual.perHorFlexivel.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1050_inclusao = s1050inclusao.objects.create(**s1050_inclusao_dados)

            if 'dadosHorContratual' in dir(inclusao) and 'horarioIntervalo' in dir(inclusao.dadosHorContratual):

                for horarioIntervalo in inclusao.dadosHorContratual.horarioIntervalo:

                    s1050_inclusao_horariointervalo_dados = {}
                    s1050_inclusao_horariointervalo_dados['s1050_inclusao_id'] = s1050_inclusao.id

                    try:
                        s1050_inclusao_horariointervalo_dados['tpinterv'] = read_from_xml(horarioIntervalo.tpInterv.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1050_inclusao_horariointervalo_dados['durinterv'] = read_from_xml(horarioIntervalo.durInterv.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1050_inclusao_horariointervalo_dados['iniinterv'] = read_from_xml(horarioIntervalo.iniInterv.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1050_inclusao_horariointervalo_dados['terminterv'] = read_from_xml(horarioIntervalo.termInterv.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1050_inclusao_horariointervalo = s1050inclusaohorarioIntervalo.objects.create(**s1050_inclusao_horariointervalo_dados)

    if 'infoHorContratual' in dir(evtTabHorTur) and 'alteracao' in dir(evtTabHorTur.infoHorContratual):

        for alteracao in evtTabHorTur.infoHorContratual.alteracao:

            s1050_alteracao_dados = {}
            s1050_alteracao_dados['s1050_evttabhortur_id'] = s1050_evttabhortur.id

            try:
                s1050_alteracao_dados['codhorcontrat'] = read_from_xml(alteracao.ideHorContratual.codHorContrat.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideHorContratual.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideHorContratual.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_alteracao_dados['hrentr'] = read_from_xml(alteracao.dadosHorContratual.hrEntr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_alteracao_dados['hrsaida'] = read_from_xml(alteracao.dadosHorContratual.hrSaida.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_alteracao_dados['durjornada'] = read_from_xml(alteracao.dadosHorContratual.durJornada.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1050_alteracao_dados['perhorflexivel'] = read_from_xml(alteracao.dadosHorContratual.perHorFlexivel.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1050_alteracao = s1050alteracao.objects.create(**s1050_alteracao_dados)

            if 'dadosHorContratual' in dir(alteracao) and 'horarioIntervalo' in dir(alteracao.dadosHorContratual):

                for horarioIntervalo in alteracao.dadosHorContratual.horarioIntervalo:

                    s1050_alteracao_horariointervalo_dados = {}
                    s1050_alteracao_horariointervalo_dados['s1050_alteracao_id'] = s1050_alteracao.id

                    try:
                        s1050_alteracao_horariointervalo_dados['tpinterv'] = read_from_xml(horarioIntervalo.tpInterv.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1050_alteracao_horariointervalo_dados['durinterv'] = read_from_xml(horarioIntervalo.durInterv.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1050_alteracao_horariointervalo_dados['iniinterv'] = read_from_xml(horarioIntervalo.iniInterv.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1050_alteracao_horariointervalo_dados['terminterv'] = read_from_xml(horarioIntervalo.termInterv.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1050_alteracao_horariointervalo = s1050alteracaohorarioIntervalo.objects.create(**s1050_alteracao_horariointervalo_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1050_alteracao_novavalidade_dados = {}
                    s1050_alteracao_novavalidade_dados['s1050_alteracao_id'] = s1050_alteracao.id

                    try:
                        s1050_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1050_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1050_alteracao_novavalidade = s1050alteracaonovaValidade.objects.create(**s1050_alteracao_novavalidade_dados)

    if 'infoHorContratual' in dir(evtTabHorTur) and 'exclusao' in dir(evtTabHorTur.infoHorContratual):

        for exclusao in evtTabHorTur.infoHorContratual.exclusao:

            s1050_exclusao_dados = {}
            s1050_exclusao_dados['s1050_evttabhortur_id'] = s1050_evttabhortur.id

            try:
                s1050_exclusao_dados['codhorcontrat'] = read_from_xml(exclusao.ideHorContratual.codHorContrat.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideHorContratual.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1050_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideHorContratual.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1050_exclusao = s1050exclusao.objects.create(**s1050_exclusao_dados)
    s1050_evttabhortur_dados['evento'] = 's1050'
    s1050_evttabhortur_dados['id'] = s1050_evttabhortur.id
    s1050_evttabhortur_dados['identidade_evento'] = doc.eSocial.evtTabHorTur['Id']

    from emensageriapro.esocial.views.s1050_evttabhortur_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1050_evttabhortur.id)

    return s1050_evttabhortur_dados