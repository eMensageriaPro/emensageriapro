#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1030.models import *
from emensageriapro.functions import read_from_xml



def read_s1030_evttabcargo_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1030_evttabcargo_obj(request, doc, status, validar)
    return dados



def read_s1030_evttabcargo(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1030_evttabcargo_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1030evtTabCargo.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1030_evttabcargo_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1030_evttabcargo_dados = {}
    s1030_evttabcargo_dados['status'] = status
    s1030_evttabcargo_dados['arquivo_original'] = 1
    if arquivo:
        s1030_evttabcargo_dados['arquivo'] = arquivo.arquivo
    s1030_evttabcargo_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1030_evttabcargo_dados['identidade'] = doc.eSocial.evtTabCargo['Id']
    evtTabCargo = doc.eSocial.evtTabCargo

    if 'inclusao' in dir(evtTabCargo.infoCargo): s1030_evttabcargo_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabCargo.infoCargo): s1030_evttabcargo_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabCargo.infoCargo): s1030_evttabcargo_dados['operacao'] = 3

    try:
        s1030_evttabcargo_dados['tpamb'] = read_from_xml(evtTabCargo.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1030_evttabcargo_dados['procemi'] = read_from_xml(evtTabCargo.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1030_evttabcargo_dados['verproc'] = read_from_xml(evtTabCargo.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1030_evttabcargo_dados['tpinsc'] = read_from_xml(evtTabCargo.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1030_evttabcargo_dados['nrinsc'] = read_from_xml(evtTabCargo.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1030_evttabcargo = s1030evtTabCargo.objects.create(**s1030_evttabcargo_dados)

    if 'infoCargo' in dir(evtTabCargo) and 'inclusao' in dir(evtTabCargo.infoCargo):

        for inclusao in evtTabCargo.infoCargo.inclusao:

            s1030_inclusao_dados = {}
            s1030_inclusao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo.id

            try:
                s1030_inclusao_dados['codcargo'] = read_from_xml(inclusao.ideCargo.codCargo.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideCargo.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideCargo.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_inclusao_dados['nmcargo'] = read_from_xml(inclusao.dadosCargo.nmCargo.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_inclusao_dados['codcbo'] = read_from_xml(inclusao.dadosCargo.codCBO.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1030_inclusao = s1030inclusao.objects.create(**s1030_inclusao_dados)

            if 'dadosCargo' in dir(inclusao) and 'cargoPublico' in dir(inclusao.dadosCargo):

                for cargoPublico in inclusao.dadosCargo.cargoPublico:

                    s1030_inclusao_cargopublico_dados = {}
                    s1030_inclusao_cargopublico_dados['s1030_inclusao_id'] = s1030_inclusao.id

                    try:
                        s1030_inclusao_cargopublico_dados['acumcargo'] = read_from_xml(cargoPublico.acumCargo.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['contagemesp'] = read_from_xml(cargoPublico.contagemEsp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['dedicexcl'] = read_from_xml(cargoPublico.dedicExcl.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['codcarreira'] = read_from_xml(cargoPublico.codCarreira.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['nrlei'] = read_from_xml(cargoPublico.leiCargo.nrLei.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['dtlei'] = read_from_xml(cargoPublico.leiCargo.dtLei.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['sitcargo'] = read_from_xml(cargoPublico.leiCargo.sitCargo.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1030_inclusao_cargopublico = s1030inclusaocargoPublico.objects.create(**s1030_inclusao_cargopublico_dados)

    if 'infoCargo' in dir(evtTabCargo) and 'alteracao' in dir(evtTabCargo.infoCargo):

        for alteracao in evtTabCargo.infoCargo.alteracao:

            s1030_alteracao_dados = {}
            s1030_alteracao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo.id

            try:
                s1030_alteracao_dados['codcargo'] = read_from_xml(alteracao.ideCargo.codCargo.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideCargo.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideCargo.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_alteracao_dados['nmcargo'] = read_from_xml(alteracao.dadosCargo.nmCargo.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_alteracao_dados['codcbo'] = read_from_xml(alteracao.dadosCargo.codCBO.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1030_alteracao = s1030alteracao.objects.create(**s1030_alteracao_dados)

            if 'dadosCargo' in dir(alteracao) and 'cargoPublico' in dir(alteracao.dadosCargo):

                for cargoPublico in alteracao.dadosCargo.cargoPublico:

                    s1030_alteracao_cargopublico_dados = {}
                    s1030_alteracao_cargopublico_dados['s1030_alteracao_id'] = s1030_alteracao.id

                    try:
                        s1030_alteracao_cargopublico_dados['acumcargo'] = read_from_xml(cargoPublico.acumCargo.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['contagemesp'] = read_from_xml(cargoPublico.contagemEsp.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['dedicexcl'] = read_from_xml(cargoPublico.dedicExcl.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['codcarreira'] = read_from_xml(cargoPublico.codCarreira.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['nrlei'] = read_from_xml(cargoPublico.leiCargo.nrLei.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['dtlei'] = read_from_xml(cargoPublico.leiCargo.dtLei.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['sitcargo'] = read_from_xml(cargoPublico.leiCargo.sitCargo.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1030_alteracao_cargopublico = s1030alteracaocargoPublico.objects.create(**s1030_alteracao_cargopublico_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1030_alteracao_novavalidade_dados = {}
                    s1030_alteracao_novavalidade_dados['s1030_alteracao_id'] = s1030_alteracao.id

                    try:
                        s1030_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1030_alteracao_novavalidade = s1030alteracaonovaValidade.objects.create(**s1030_alteracao_novavalidade_dados)

    if 'infoCargo' in dir(evtTabCargo) and 'exclusao' in dir(evtTabCargo.infoCargo):

        for exclusao in evtTabCargo.infoCargo.exclusao:

            s1030_exclusao_dados = {}
            s1030_exclusao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo.id

            try:
                s1030_exclusao_dados['codcargo'] = read_from_xml(exclusao.ideCargo.codCargo.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideCargo.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1030_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideCargo.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1030_exclusao = s1030exclusao.objects.create(**s1030_exclusao_dados)
    s1030_evttabcargo_dados['evento'] = 's1030'
    s1030_evttabcargo_dados['id'] = s1030_evttabcargo.id
    s1030_evttabcargo_dados['identidade_evento'] = doc.eSocial.evtTabCargo['Id']

    from emensageriapro.esocial.views.s1030_evttabcargo_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1030_evttabcargo.id)

    return s1030_evttabcargo_dados