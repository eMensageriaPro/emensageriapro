#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1060.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s1060_evttabambiente_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    s1060evtTabAmbiente.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s1060_evttabambiente_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1060_evttabambiente_dados = {}
    s1060_evttabambiente_dados['status'] = status
    s1060_evttabambiente_dados['arquivo_original'] = 1
    if arquivo:
        s1060_evttabambiente_dados['arquivo'] = arquivo
    s1060_evttabambiente_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1060_evttabambiente_dados['identidade'] = doc.eSocial.evtTabAmbiente['Id']
    evtTabAmbiente = doc.eSocial.evtTabAmbiente

    if 'inclusao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabAmbiente.infoAmbiente): s1060_evttabambiente_dados['operacao'] = 3

    try:
        s1060_evttabambiente_dados['tpamb'] = evtTabAmbiente.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1060_evttabambiente_dados['procemi'] = evtTabAmbiente.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1060_evttabambiente_dados['verproc'] = evtTabAmbiente.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1060_evttabambiente_dados['tpinsc'] = evtTabAmbiente.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1060_evttabambiente_dados['nrinsc'] = evtTabAmbiente.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    s1060_evttabambiente = s1060evtTabAmbiente.objects.create(**s1060_evttabambiente_dados)

    if 'infoAmbiente' in dir(evtTabAmbiente) and 'inclusao' in dir(evtTabAmbiente.infoAmbiente):

        for inclusao in evtTabAmbiente.infoAmbiente.inclusao:

            s1060_inclusao_dados = {}
            s1060_inclusao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente.id

            try:
                s1060_inclusao_dados['codamb'] = inclusao.ideAmbiente.codAmb.cdata
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['inivalid'] = inclusao.ideAmbiente.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['fimvalid'] = inclusao.ideAmbiente.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['nmamb'] = inclusao.dadosAmbiente.nmAmb.cdata
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['dscamb'] = inclusao.dadosAmbiente.dscAmb.cdata
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['localamb'] = inclusao.dadosAmbiente.localAmb.cdata
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['tpinsc'] = inclusao.dadosAmbiente.tpInsc.cdata
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['nrinsc'] = inclusao.dadosAmbiente.nrInsc.cdata
            except AttributeError:
                pass

            try:
                s1060_inclusao_dados['codlotacao'] = inclusao.dadosAmbiente.codLotacao.cdata
            except AttributeError:
                pass

            s1060_inclusao = s1060inclusao.objects.create(**s1060_inclusao_dados)

    if 'infoAmbiente' in dir(evtTabAmbiente) and 'alteracao' in dir(evtTabAmbiente.infoAmbiente):

        for alteracao in evtTabAmbiente.infoAmbiente.alteracao:

            s1060_alteracao_dados = {}
            s1060_alteracao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente.id

            try:
                s1060_alteracao_dados['codamb'] = alteracao.ideAmbiente.codAmb.cdata
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['inivalid'] = alteracao.ideAmbiente.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['fimvalid'] = alteracao.ideAmbiente.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['nmamb'] = alteracao.dadosAmbiente.nmAmb.cdata
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['dscamb'] = alteracao.dadosAmbiente.dscAmb.cdata
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['localamb'] = alteracao.dadosAmbiente.localAmb.cdata
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['tpinsc'] = alteracao.dadosAmbiente.tpInsc.cdata
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['nrinsc'] = alteracao.dadosAmbiente.nrInsc.cdata
            except AttributeError:
                pass

            try:
                s1060_alteracao_dados['codlotacao'] = alteracao.dadosAmbiente.codLotacao.cdata
            except AttributeError:
                pass

            s1060_alteracao = s1060alteracao.objects.create(**s1060_alteracao_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1060_alteracao_novavalidade_dados = {}
                    s1060_alteracao_novavalidade_dados['s1060_alteracao_id'] = s1060_alteracao.id

                    try:
                        s1060_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError:
                        pass

                    try:
                        s1060_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError:
                        pass

                    s1060_alteracao_novavalidade = s1060alteracaonovaValidade.objects.create(**s1060_alteracao_novavalidade_dados)

    if 'infoAmbiente' in dir(evtTabAmbiente) and 'exclusao' in dir(evtTabAmbiente.infoAmbiente):

        for exclusao in evtTabAmbiente.infoAmbiente.exclusao:

            s1060_exclusao_dados = {}
            s1060_exclusao_dados['s1060_evttabambiente_id'] = s1060_evttabambiente.id

            try:
                s1060_exclusao_dados['codamb'] = exclusao.ideAmbiente.codAmb.cdata
            except AttributeError:
                pass

            try:
                s1060_exclusao_dados['inivalid'] = exclusao.ideAmbiente.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1060_exclusao_dados['fimvalid'] = exclusao.ideAmbiente.fimValid.cdata
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