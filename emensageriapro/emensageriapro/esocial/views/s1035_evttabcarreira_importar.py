#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1035.models import *
from emensageriapro.functions import read_from_xml



def read_s1035_evttabcarreira_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1035_evttabcarreira_obj(request, doc, status, validar)
    return dados



def read_s1035_evttabcarreira(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1035_evttabcarreira_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1035evtTabCarreira.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1035_evttabcarreira_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1035_evttabcarreira_dados = {}
    s1035_evttabcarreira_dados['status'] = status
    s1035_evttabcarreira_dados['arquivo_original'] = 1
    if arquivo:
        s1035_evttabcarreira_dados['arquivo'] = arquivo.arquivo
    s1035_evttabcarreira_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1035_evttabcarreira_dados['identidade'] = doc.eSocial.evtTabCarreira['Id']
    evtTabCarreira = doc.eSocial.evtTabCarreira

    if 'inclusao' in dir(evtTabCarreira.infoCarreira): s1035_evttabcarreira_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabCarreira.infoCarreira): s1035_evttabcarreira_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabCarreira.infoCarreira): s1035_evttabcarreira_dados['operacao'] = 3

    try:
        s1035_evttabcarreira_dados['tpamb'] = read_from_xml(evtTabCarreira.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1035_evttabcarreira_dados['procemi'] = read_from_xml(evtTabCarreira.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1035_evttabcarreira_dados['verproc'] = read_from_xml(evtTabCarreira.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1035_evttabcarreira_dados['tpinsc'] = read_from_xml(evtTabCarreira.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1035_evttabcarreira_dados['nrinsc'] = read_from_xml(evtTabCarreira.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1035_evttabcarreira = s1035evtTabCarreira.objects.create(**s1035_evttabcarreira_dados)

    if 'infoCarreira' in dir(evtTabCarreira) and 'inclusao' in dir(evtTabCarreira.infoCarreira):

        for inclusao in evtTabCarreira.infoCarreira.inclusao:

            s1035_inclusao_dados = {}
            s1035_inclusao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira.id

            try:
                s1035_inclusao_dados['codcarreira'] = read_from_xml(inclusao.ideCarreira.codCarreira.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideCarreira.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideCarreira.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_inclusao_dados['dsccarreira'] = read_from_xml(inclusao.dadosCarreira.dscCarreira.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_inclusao_dados['leicarr'] = read_from_xml(inclusao.dadosCarreira.leiCarr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_inclusao_dados['dtleicarr'] = read_from_xml(inclusao.dadosCarreira.dtLeiCarr.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s1035_inclusao_dados['sitcarr'] = read_from_xml(inclusao.dadosCarreira.sitCarr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s1035_inclusao = s1035inclusao.objects.create(**s1035_inclusao_dados)

    if 'infoCarreira' in dir(evtTabCarreira) and 'alteracao' in dir(evtTabCarreira.infoCarreira):

        for alteracao in evtTabCarreira.infoCarreira.alteracao:

            s1035_alteracao_dados = {}
            s1035_alteracao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira.id

            try:
                s1035_alteracao_dados['codcarreira'] = read_from_xml(alteracao.ideCarreira.codCarreira.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideCarreira.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideCarreira.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_alteracao_dados['dsccarreira'] = read_from_xml(alteracao.dadosCarreira.dscCarreira.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_alteracao_dados['leicarr'] = read_from_xml(alteracao.dadosCarreira.leiCarr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_alteracao_dados['dtleicarr'] = read_from_xml(alteracao.dadosCarreira.dtLeiCarr.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s1035_alteracao_dados['sitcarr'] = read_from_xml(alteracao.dadosCarreira.sitCarr.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s1035_alteracao = s1035alteracao.objects.create(**s1035_alteracao_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1035_alteracao_novavalidade_dados = {}
                    s1035_alteracao_novavalidade_dados['s1035_alteracao_id'] = s1035_alteracao.id

                    try:
                        s1035_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1035_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1035_alteracao_novavalidade = s1035alteracaonovaValidade.objects.create(**s1035_alteracao_novavalidade_dados)

    if 'infoCarreira' in dir(evtTabCarreira) and 'exclusao' in dir(evtTabCarreira.infoCarreira):

        for exclusao in evtTabCarreira.infoCarreira.exclusao:

            s1035_exclusao_dados = {}
            s1035_exclusao_dados['s1035_evttabcarreira_id'] = s1035_evttabcarreira.id

            try:
                s1035_exclusao_dados['codcarreira'] = read_from_xml(exclusao.ideCarreira.codCarreira.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideCarreira.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1035_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideCarreira.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1035_exclusao = s1035exclusao.objects.create(**s1035_exclusao_dados)
    s1035_evttabcarreira_dados['evento'] = 's1035'
    s1035_evttabcarreira_dados['id'] = s1035_evttabcarreira.id
    s1035_evttabcarreira_dados['identidade_evento'] = doc.eSocial.evtTabCarreira['Id']

    from emensageriapro.esocial.views.s1035_evttabcarreira_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1035_evttabcarreira.id)

    return s1035_evttabcarreira_dados