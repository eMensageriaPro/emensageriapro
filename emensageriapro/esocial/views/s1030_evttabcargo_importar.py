#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1030.models import *



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
        s1030_evttabcargo_dados['tpamb'] = evtTabCargo.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s1030_evttabcargo_dados['procemi'] = evtTabCargo.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s1030_evttabcargo_dados['verproc'] = evtTabCargo.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s1030_evttabcargo_dados['tpinsc'] = evtTabCargo.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s1030_evttabcargo_dados['nrinsc'] = evtTabCargo.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    s1030_evttabcargo = s1030evtTabCargo.objects.create(**s1030_evttabcargo_dados)

    if 'infoCargo' in dir(evtTabCargo) and 'inclusao' in dir(evtTabCargo.infoCargo):

        for inclusao in evtTabCargo.infoCargo.inclusao:

            s1030_inclusao_dados = {}
            s1030_inclusao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo.id

            try:
                s1030_inclusao_dados['codcargo'] = inclusao.ideCargo.codCargo.cdata
            except AttributeError:
                pass

            try:
                s1030_inclusao_dados['inivalid'] = inclusao.ideCargo.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1030_inclusao_dados['fimvalid'] = inclusao.ideCargo.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1030_inclusao_dados['nmcargo'] = inclusao.dadosCargo.nmCargo.cdata
            except AttributeError:
                pass

            try:
                s1030_inclusao_dados['codcbo'] = inclusao.dadosCargo.codCBO.cdata
            except AttributeError:
                pass

            s1030_inclusao = s1030inclusao.objects.create(**s1030_inclusao_dados)

            if 'dadosCargo' in dir(inclusao) and 'cargoPublico' in dir(inclusao.dadosCargo):

                for cargoPublico in inclusao.dadosCargo.cargoPublico:

                    s1030_inclusao_cargopublico_dados = {}
                    s1030_inclusao_cargopublico_dados['s1030_inclusao_id'] = s1030_inclusao.id

                    try:
                        s1030_inclusao_cargopublico_dados['acumcargo'] = cargoPublico.acumCargo.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['contagemesp'] = cargoPublico.contagemEsp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['dedicexcl'] = cargoPublico.dedicExcl.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['codcarreira'] = cargoPublico.codCarreira.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['nrlei'] = cargoPublico.leiCargo.nrLei.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['dtlei'] = cargoPublico.leiCargo.dtLei.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_inclusao_cargopublico_dados['sitcargo'] = cargoPublico.leiCargo.sitCargo.cdata
                    except AttributeError:
                        pass

                    s1030_inclusao_cargopublico = s1030inclusaocargoPublico.objects.create(**s1030_inclusao_cargopublico_dados)

    if 'infoCargo' in dir(evtTabCargo) and 'alteracao' in dir(evtTabCargo.infoCargo):

        for alteracao in evtTabCargo.infoCargo.alteracao:

            s1030_alteracao_dados = {}
            s1030_alteracao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo.id

            try:
                s1030_alteracao_dados['codcargo'] = alteracao.ideCargo.codCargo.cdata
            except AttributeError:
                pass

            try:
                s1030_alteracao_dados['inivalid'] = alteracao.ideCargo.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1030_alteracao_dados['fimvalid'] = alteracao.ideCargo.fimValid.cdata
            except AttributeError:
                pass

            try:
                s1030_alteracao_dados['nmcargo'] = alteracao.dadosCargo.nmCargo.cdata
            except AttributeError:
                pass

            try:
                s1030_alteracao_dados['codcbo'] = alteracao.dadosCargo.codCBO.cdata
            except AttributeError:
                pass

            s1030_alteracao = s1030alteracao.objects.create(**s1030_alteracao_dados)

            if 'dadosCargo' in dir(alteracao) and 'cargoPublico' in dir(alteracao.dadosCargo):

                for cargoPublico in alteracao.dadosCargo.cargoPublico:

                    s1030_alteracao_cargopublico_dados = {}
                    s1030_alteracao_cargopublico_dados['s1030_alteracao_id'] = s1030_alteracao.id

                    try:
                        s1030_alteracao_cargopublico_dados['acumcargo'] = cargoPublico.acumCargo.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['contagemesp'] = cargoPublico.contagemEsp.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['dedicexcl'] = cargoPublico.dedicExcl.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['codcarreira'] = cargoPublico.codCarreira.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['nrlei'] = cargoPublico.leiCargo.nrLei.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['dtlei'] = cargoPublico.leiCargo.dtLei.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_cargopublico_dados['sitcargo'] = cargoPublico.leiCargo.sitCargo.cdata
                    except AttributeError:
                        pass

                    s1030_alteracao_cargopublico = s1030alteracaocargoPublico.objects.create(**s1030_alteracao_cargopublico_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1030_alteracao_novavalidade_dados = {}
                    s1030_alteracao_novavalidade_dados['s1030_alteracao_id'] = s1030_alteracao.id

                    try:
                        s1030_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError:
                        pass

                    try:
                        s1030_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError:
                        pass

                    s1030_alteracao_novavalidade = s1030alteracaonovaValidade.objects.create(**s1030_alteracao_novavalidade_dados)

    if 'infoCargo' in dir(evtTabCargo) and 'exclusao' in dir(evtTabCargo.infoCargo):

        for exclusao in evtTabCargo.infoCargo.exclusao:

            s1030_exclusao_dados = {}
            s1030_exclusao_dados['s1030_evttabcargo_id'] = s1030_evttabcargo.id

            try:
                s1030_exclusao_dados['codcargo'] = exclusao.ideCargo.codCargo.cdata
            except AttributeError:
                pass

            try:
                s1030_exclusao_dados['inivalid'] = exclusao.ideCargo.iniValid.cdata
            except AttributeError:
                pass

            try:
                s1030_exclusao_dados['fimvalid'] = exclusao.ideCargo.fimValid.cdata
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