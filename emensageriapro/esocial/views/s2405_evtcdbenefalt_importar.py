# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2405.models import *
from emensageriapro.functions import read_from_xml



def read_s2405_evtcdbenefalt_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2405_evtcdbenefalt_obj(request, doc, status, validar)
    return dados



def read_s2405_evtcdbenefalt(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2405_evtcdbenefalt_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2405evtCdBenefAlt.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2405_evtcdbenefalt_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2405_evtcdbenefalt_dados = {}
    s2405_evtcdbenefalt_dados['status'] = status
    s2405_evtcdbenefalt_dados['arquivo_original'] = 1
    if arquivo:
        s2405_evtcdbenefalt_dados['arquivo'] = arquivo.arquivo
    s2405_evtcdbenefalt_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2405_evtcdbenefalt_dados['identidade'] = doc.eSocial.evtCdBenefAlt['Id']
    evtCdBenefAlt = doc.eSocial.evtCdBenefAlt

    try:
        s2405_evtcdbenefalt_dados['indretif'] = read_from_xml(evtCdBenefAlt.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nrrecibo'] = read_from_xml(evtCdBenefAlt.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['tpamb'] = read_from_xml(evtCdBenefAlt.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['procemi'] = read_from_xml(evtCdBenefAlt.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['verproc'] = read_from_xml(evtCdBenefAlt.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['tpinsc'] = read_from_xml(evtCdBenefAlt.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nrinsc'] = read_from_xml(evtCdBenefAlt.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['cpfbenef'] = read_from_xml(evtCdBenefAlt.ideBenef.cpfBenef.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['dtalteracao'] = read_from_xml(evtCdBenefAlt.alteracao.dtAlteracao.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nisbenef'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.nisBenef.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nmbenefic'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.nmBenefic.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['sexo'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.sexo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['racacor'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.racaCor.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['estciv'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.estCiv.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['incfismen'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.incFisMen.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['dtincfismen'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.dtIncFisMen.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['paisnac'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.paisNac.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nmmae'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmMae.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nmpai'] = read_from_xml(evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmPai.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2405_evtcdbenefalt = s2405evtCdBenefAlt.objects.create(**s2405_evtcdbenefalt_dados)

    if 'alteracao' in dir(evtCdBenefAlt) and 'dadosBenef' in dir(evtCdBenefAlt.alteracao) and 'endereco' in dir(evtCdBenefAlt.alteracao.dadosBenef):

        for endereco in evtCdBenefAlt.alteracao.dadosBenef.endereco:

            s2405_endereco_dados = {}
            s2405_endereco_dados['s2405_evtcdbenefalt_id'] = s2405_evtcdbenefalt.id

            s2405_endereco = s2405endereco.objects.create(**s2405_endereco_dados)

            if 'brasil' in dir(endereco):

                for brasil in endereco.brasil:

                    s2405_brasil_dados = {}
                    s2405_brasil_dados['s2405_endereco_id'] = s2405_endereco.id

                    try:
                        s2405_brasil_dados['tplograd'] = read_from_xml(brasil.tpLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['dsclograd'] = read_from_xml(brasil.dscLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['nrlograd'] = read_from_xml(brasil.nrLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['complemento'] = read_from_xml(brasil.complemento.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['bairro'] = read_from_xml(brasil.bairro.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['cep'] = read_from_xml(brasil.cep.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['codmunic'] = read_from_xml(brasil.codMunic.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['uf'] = read_from_xml(brasil.uf.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2405_brasil = s2405brasil.objects.create(**s2405_brasil_dados)

            if 'exterior' in dir(endereco):

                for exterior in endereco.exterior:

                    s2405_exterior_dados = {}
                    s2405_exterior_dados['s2405_endereco_id'] = s2405_endereco.id

                    try:
                        s2405_exterior_dados['paisresid'] = read_from_xml(exterior.paisResid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['dsclograd'] = read_from_xml(exterior.dscLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['nrlograd'] = read_from_xml(exterior.nrLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['complemento'] = read_from_xml(exterior.complemento.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['bairro'] = read_from_xml(exterior.bairro.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['nmcid'] = read_from_xml(exterior.nmCid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['codpostal'] = read_from_xml(exterior.codPostal.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2405_exterior = s2405exterior.objects.create(**s2405_exterior_dados)

    if 'alteracao' in dir(evtCdBenefAlt) and 'dadosBenef' in dir(evtCdBenefAlt.alteracao) and 'dependente' in dir(evtCdBenefAlt.alteracao.dadosBenef):

        for dependente in evtCdBenefAlt.alteracao.dadosBenef.dependente:

            s2405_dependente_dados = {}
            s2405_dependente_dados['s2405_evtcdbenefalt_id'] = s2405_evtcdbenefalt.id

            try:
                s2405_dependente_dados['tpdep'] = read_from_xml(dependente.tpDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['nmdep'] = read_from_xml(dependente.nmDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['dtnascto'] = read_from_xml(dependente.dtNascto.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['cpfdep'] = read_from_xml(dependente.cpfDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['sexodep'] = read_from_xml(dependente.sexoDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['depirrf'] = read_from_xml(dependente.depIRRF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['incfismen'] = read_from_xml(dependente.incFisMen.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['depfinsprev'] = read_from_xml(dependente.depFinsPrev.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2405_dependente = s2405dependente.objects.create(**s2405_dependente_dados)
    s2405_evtcdbenefalt_dados['evento'] = 's2405'
    s2405_evtcdbenefalt_dados['id'] = s2405_evtcdbenefalt.id
    s2405_evtcdbenefalt_dados['identidade_evento'] = doc.eSocial.evtCdBenefAlt['Id']

    from emensageriapro.esocial.views.s2405_evtcdbenefalt_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2405_evtcdbenefalt.id)

    return s2405_evtcdbenefalt_dados