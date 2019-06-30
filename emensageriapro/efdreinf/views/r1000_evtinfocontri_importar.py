#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r1000.models import *
from emensageriapro.functions import read_from_xml



def read_r1000_evtinfocontri_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r1000_evtinfocontri_obj(request, doc, status, validar)
    return dados



def read_r1000_evtinfocontri(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r1000_evtinfocontri_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r1000evtInfoContri.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r1000_evtinfocontri_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r1000_evtinfocontri_dados = {}
    r1000_evtinfocontri_dados['status'] = status
    r1000_evtinfocontri_dados['arquivo_original'] = 1
    if arquivo:
        r1000_evtinfocontri_dados['arquivo'] = arquivo.arquivo
    r1000_evtinfocontri_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r1000_evtinfocontri_dados['identidade'] = doc.Reinf.evtInfoContri['id']
    evtInfoContri = doc.Reinf.evtInfoContri

    if 'inclusao' in dir(evtInfoContri.infoContri): r1000_evtinfocontri_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInfoContri.infoContri): r1000_evtinfocontri_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInfoContri.infoContri): r1000_evtinfocontri_dados['operacao'] = 3

    try:
        r1000_evtinfocontri_dados['tpamb'] = read_from_xml(evtInfoContri.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r1000_evtinfocontri_dados['procemi'] = read_from_xml(evtInfoContri.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r1000_evtinfocontri_dados['verproc'] = read_from_xml(evtInfoContri.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r1000_evtinfocontri_dados['tpinsc'] = read_from_xml(evtInfoContri.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r1000_evtinfocontri_dados['nrinsc'] = read_from_xml(evtInfoContri.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r1000_evtinfocontri = r1000evtInfoContri.objects.create(**r1000_evtinfocontri_dados)

    if 'infoContri' in dir(evtInfoContri) and 'inclusao' in dir(evtInfoContri.infoContri):

        for inclusao in evtInfoContri.infoContri.inclusao:

            r1000_inclusao_dados = {}
            r1000_inclusao_dados['r1000_evtinfocontri_id'] = r1000_evtinfocontri.id

            try:
                r1000_inclusao_dados['inivalid'] = read_from_xml(inclusao.idePeriodo.iniValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['fimvalid'] = read_from_xml(inclusao.idePeriodo.fimValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['classtrib'] = read_from_xml(inclusao.infoCadastro.classTrib.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['indescrituracao'] = read_from_xml(inclusao.infoCadastro.indEscrituracao.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['inddesoneracao'] = read_from_xml(inclusao.infoCadastro.indDesoneracao.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['indacordoisenmulta'] = read_from_xml(inclusao.infoCadastro.indAcordoIsenMulta.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['indsitpj'] = read_from_xml(inclusao.infoCadastro.indSitPJ.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['nmctt'] = read_from_xml(inclusao.infoCadastro.contato.nmCtt.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['cpfctt'] = read_from_xml(inclusao.infoCadastro.contato.cpfCtt.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['fonefixo'] = read_from_xml(inclusao.infoCadastro.contato.foneFixo.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['fonecel'] = read_from_xml(inclusao.infoCadastro.contato.foneCel.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_inclusao_dados['email'] = read_from_xml(inclusao.infoCadastro.contato.email.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r1000_inclusao = r1000inclusao.objects.create(**r1000_inclusao_dados)

            if 'infoCadastro' in dir(inclusao) and 'softHouse' in dir(inclusao.infoCadastro):

                for softHouse in inclusao.infoCadastro.softHouse:

                    r1000_inclusao_softhouse_dados = {}
                    r1000_inclusao_softhouse_dados['r1000_inclusao_id'] = r1000_inclusao.id

                    try:
                        r1000_inclusao_softhouse_dados['cnpjsofthouse'] = read_from_xml(softHouse.cnpjSoftHouse.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_inclusao_softhouse_dados['nmrazao'] = read_from_xml(softHouse.nmRazao.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_inclusao_softhouse_dados['nmcont'] = read_from_xml(softHouse.nmCont.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_inclusao_softhouse_dados['telefone'] = read_from_xml(softHouse.telefone.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_inclusao_softhouse_dados['email'] = read_from_xml(softHouse.email.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1000_inclusao_softhouse = r1000inclusaosoftHouse.objects.create(**r1000_inclusao_softhouse_dados)

            if 'infoCadastro' in dir(inclusao) and 'infoEFR' in dir(inclusao.infoCadastro):

                for infoEFR in inclusao.infoCadastro.infoEFR:

                    r1000_inclusao_infoefr_dados = {}
                    r1000_inclusao_infoefr_dados['r1000_inclusao_id'] = r1000_inclusao.id

                    try:
                        r1000_inclusao_infoefr_dados['ideefr'] = read_from_xml(infoEFR.ideEFR.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_inclusao_infoefr_dados['cnpjefr'] = read_from_xml(infoEFR.cnpjEFR.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1000_inclusao_infoefr = r1000inclusaoinfoEFR.objects.create(**r1000_inclusao_infoefr_dados)

    if 'infoContri' in dir(evtInfoContri) and 'alteracao' in dir(evtInfoContri.infoContri):

        for alteracao in evtInfoContri.infoContri.alteracao:

            r1000_alteracao_dados = {}
            r1000_alteracao_dados['r1000_evtinfocontri_id'] = r1000_evtinfocontri.id

            try:
                r1000_alteracao_dados['inivalid'] = read_from_xml(alteracao.idePeriodo.iniValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['fimvalid'] = read_from_xml(alteracao.idePeriodo.fimValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['classtrib'] = read_from_xml(alteracao.infoCadastro.classTrib.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['indescrituracao'] = read_from_xml(alteracao.infoCadastro.indEscrituracao.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['inddesoneracao'] = read_from_xml(alteracao.infoCadastro.indDesoneracao.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['indacordoisenmulta'] = read_from_xml(alteracao.infoCadastro.indAcordoIsenMulta.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['indsitpj'] = read_from_xml(alteracao.infoCadastro.indSitPJ.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['nmctt'] = read_from_xml(alteracao.infoCadastro.contato.nmCtt.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['cpfctt'] = read_from_xml(alteracao.infoCadastro.contato.cpfCtt.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['fonefixo'] = read_from_xml(alteracao.infoCadastro.contato.foneFixo.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['fonecel'] = read_from_xml(alteracao.infoCadastro.contato.foneCel.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_alteracao_dados['email'] = read_from_xml(alteracao.infoCadastro.contato.email.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r1000_alteracao = r1000alteracao.objects.create(**r1000_alteracao_dados)

            if 'infoCadastro' in dir(alteracao) and 'softHouse' in dir(alteracao.infoCadastro):

                for softHouse in alteracao.infoCadastro.softHouse:

                    r1000_alteracao_softhouse_dados = {}
                    r1000_alteracao_softhouse_dados['r1000_alteracao_id'] = r1000_alteracao.id

                    try:
                        r1000_alteracao_softhouse_dados['cnpjsofthouse'] = read_from_xml(softHouse.cnpjSoftHouse.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_alteracao_softhouse_dados['nmrazao'] = read_from_xml(softHouse.nmRazao.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_alteracao_softhouse_dados['nmcont'] = read_from_xml(softHouse.nmCont.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_alteracao_softhouse_dados['telefone'] = read_from_xml(softHouse.telefone.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_alteracao_softhouse_dados['email'] = read_from_xml(softHouse.email.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1000_alteracao_softhouse = r1000alteracaosoftHouse.objects.create(**r1000_alteracao_softhouse_dados)

            if 'infoCadastro' in dir(alteracao) and 'infoEFR' in dir(alteracao.infoCadastro):

                for infoEFR in alteracao.infoCadastro.infoEFR:

                    r1000_alteracao_infoefr_dados = {}
                    r1000_alteracao_infoefr_dados['r1000_alteracao_id'] = r1000_alteracao.id

                    try:
                        r1000_alteracao_infoefr_dados['ideefr'] = read_from_xml(infoEFR.ideEFR.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_alteracao_infoefr_dados['cnpjefr'] = read_from_xml(infoEFR.cnpjEFR.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1000_alteracao_infoefr = r1000alteracaoinfoEFR.objects.create(**r1000_alteracao_infoefr_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    r1000_alteracao_novavalidade_dados = {}
                    r1000_alteracao_novavalidade_dados['r1000_alteracao_id'] = r1000_alteracao.id

                    try:
                        r1000_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r1000_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r1000_alteracao_novavalidade = r1000alteracaonovaValidade.objects.create(**r1000_alteracao_novavalidade_dados)

    if 'infoContri' in dir(evtInfoContri) and 'exclusao' in dir(evtInfoContri.infoContri):

        for exclusao in evtInfoContri.infoContri.exclusao:

            r1000_exclusao_dados = {}
            r1000_exclusao_dados['r1000_evtinfocontri_id'] = r1000_evtinfocontri.id

            try:
                r1000_exclusao_dados['inivalid'] = read_from_xml(exclusao.idePeriodo.iniValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r1000_exclusao_dados['fimvalid'] = read_from_xml(exclusao.idePeriodo.fimValid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r1000_exclusao = r1000exclusao.objects.create(**r1000_exclusao_dados)
    r1000_evtinfocontri_dados['evento'] = 'r1000'
    r1000_evtinfocontri_dados['id'] = r1000_evtinfocontri.id
    r1000_evtinfocontri_dados['identidade_evento'] = doc.Reinf.evtInfoContri['id']

    from emensageriapro.efdreinf.views.r1000_evtinfocontri_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r1000_evtinfocontri.id)

    return r1000_evtinfocontri_dados