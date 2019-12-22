# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1060.models import *
from emensageriapro.functions import read_from_xml



def read_s1060_evttabambiente_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1060_evttabambiente_obj(request, doc, status, validar)
    return dados



def read_s1060_evttabambiente(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1060_evttabambiente_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1060evtTabAmbiente.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1060_evttabambiente_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1060_evttabambiente_dados = {}
    s1060_evttabambiente_dados['status'] = status
    s1060_evttabambiente_dados['arquivo_original'] = 1
    if arquivo:
        s1060_evttabambiente_dados['arquivo'] = arquivo.arquivo
    s1060_evttabambiente_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1060_evttabambiente_dados['identidade'] = doc.eSocial.evtTabAmbiente['Id']
    evtTabAmbiente = doc.eSocial.evtTabAmbiente

    if 'inclusao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 3

    try:
        s1060_evttabambiente_dados['tpamb'] = read_from_xml(evtTabAmbiente.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1060_evttabambiente_dados['procemi'] = read_from_xml(evtTabAmbiente.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1060_evttabambiente_dados['verproc'] = read_from_xml(evtTabAmbiente.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1060_evttabambiente_dados['tpinsc'] = read_from_xml(evtTabAmbiente.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1060_evttabambiente_dados['nrinsc'] = read_from_xml(evtTabAmbiente.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1060_evttabambiente = s1060evtTabAmbiente.objects.create(**s1060_evttabambiente_dados)

    if 'infoAmbiente' in dir(evtTabAmbiente) and 'inclusao' in dir(evtTabAmbiente.infoAmbiente):

        for inclusao in evtTabAmbiente.infoAmbiente.inclusao:

            s1060_inclusao_dados = {}
            s1060_inclusao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente.id

            try:
                s1060_inclusao_dados['codamb'] = read_from_xml(inclusao.ideAmbiente.codAmb.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideAmbiente.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideAmbiente.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['nmamb'] = read_from_xml(inclusao.dadosAmbiente.nmAmb.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['dscamb'] = read_from_xml(inclusao.dadosAmbiente.dscAmb.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['localamb'] = read_from_xml(inclusao.dadosAmbiente.localAmb.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['tpinsc'] = read_from_xml(inclusao.dadosAmbiente.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['nrinsc'] = read_from_xml(inclusao.dadosAmbiente.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['codlotacao'] = read_from_xml(inclusao.dadosAmbiente.codLotacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1060_inclusao = s1060inclusao.objects.create(**s1060_inclusao_dados)

    if 'infoAmbiente' in dir(evtTabAmbiente) and 'alteracao' in dir(evtTabAmbiente.infoAmbiente):

        for alteracao in evtTabAmbiente.infoAmbiente.alteracao:

            s1060_alteracao_dados = {}
            s1060_alteracao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente.id

            try:
                s1060_alteracao_dados['codamb'] = read_from_xml(alteracao.ideAmbiente.codAmb.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideAmbiente.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideAmbiente.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['nmamb'] = read_from_xml(alteracao.dadosAmbiente.nmAmb.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['dscamb'] = read_from_xml(alteracao.dadosAmbiente.dscAmb.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['localamb'] = read_from_xml(alteracao.dadosAmbiente.localAmb.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['tpinsc'] = read_from_xml(alteracao.dadosAmbiente.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['nrinsc'] = read_from_xml(alteracao.dadosAmbiente.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['codlotacao'] = read_from_xml(alteracao.dadosAmbiente.codLotacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1060_alteracao = s1060alteracao.objects.create(**s1060_alteracao_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1060_alteracao_novavalidade_dados = {}
                    s1060_alteracao_novavalidade_dados['s1060_alteracao_id'] = s1060_alteracao.id

                    try:
                        s1060_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1060_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1060_alteracao_novavalidade = s1060alteracaonovaValidade.objects.create(**s1060_alteracao_novavalidade_dados)

    if 'infoAmbiente' in dir(evtTabAmbiente) and 'exclusao' in dir(evtTabAmbiente.infoAmbiente):

        for exclusao in evtTabAmbiente.infoAmbiente.exclusao:

            s1060_exclusao_dados = {}
            s1060_exclusao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente.id

            try:
                s1060_exclusao_dados['codamb'] = read_from_xml(exclusao.ideAmbiente.codAmb.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideAmbiente.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1060_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideAmbiente.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1060_exclusao = s1060exclusao.objects.create(**s1060_exclusao_dados)
    s1060_evttabambiente_dados['evento'] = 's1060'
    s1060_evttabambiente_dados['id'] = s1060_evttabambiente.id
    s1060_evttabambiente_dados['identidade_evento'] = doc.eSocial.evtTabAmbiente['Id']

    from emensageriapro.esocial.views.s1060_evttabambiente_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1060_evttabambiente.id)

    return s1060_evttabambiente_dados