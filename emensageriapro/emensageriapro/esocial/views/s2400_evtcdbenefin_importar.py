#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2400.models import *
from emensageriapro.functions import read_from_xml



def read_s2400_evtcdbenefin_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2400_evtcdbenefin_obj(request, doc, status, validar)
    return dados



def read_s2400_evtcdbenefin(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2400_evtcdbenefin_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2400evtCdBenefIn.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2400_evtcdbenefin_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2400_evtcdbenefin_dados = {}
    s2400_evtcdbenefin_dados['status'] = status
    s2400_evtcdbenefin_dados['arquivo_original'] = 1
    if arquivo:
        s2400_evtcdbenefin_dados['arquivo'] = arquivo.arquivo
    s2400_evtcdbenefin_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2400_evtcdbenefin_dados['identidade'] = doc.eSocial.evtCdBenefIn['Id']
    evtCdBenefIn = doc.eSocial.evtCdBenefIn

    try:
        s2400_evtcdbenefin_dados['indretif'] = read_from_xml(evtCdBenefIn.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nrrecibo'] = read_from_xml(evtCdBenefIn.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['tpamb'] = read_from_xml(evtCdBenefIn.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['procemi'] = read_from_xml(evtCdBenefIn.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['verproc'] = read_from_xml(evtCdBenefIn.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['tpinsc'] = read_from_xml(evtCdBenefIn.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nrinsc'] = read_from_xml(evtCdBenefIn.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['cpfbenef'] = read_from_xml(evtCdBenefIn.beneficiario.cpfBenef.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nisbenef'] = read_from_xml(evtCdBenefIn.beneficiario.nisBenef.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nmbenefic'] = read_from_xml(evtCdBenefIn.beneficiario.nmBenefic.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['dtinicio'] = read_from_xml(evtCdBenefIn.beneficiario.dtInicio.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['sexo'] = read_from_xml(evtCdBenefIn.beneficiario.sexo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['racacor'] = read_from_xml(evtCdBenefIn.beneficiario.racaCor.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['estciv'] = read_from_xml(evtCdBenefIn.beneficiario.estCiv.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['incfismen'] = read_from_xml(evtCdBenefIn.beneficiario.incFisMen.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['dtincfismen'] = read_from_xml(evtCdBenefIn.beneficiario.dtIncFisMen.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['dtnascto'] = read_from_xml(evtCdBenefIn.beneficiario.dadosNasc.dtNascto.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['codmunic'] = read_from_xml(evtCdBenefIn.beneficiario.dadosNasc.codMunic.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['uf'] = read_from_xml(evtCdBenefIn.beneficiario.dadosNasc.uf.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['paisnascto'] = read_from_xml(evtCdBenefIn.beneficiario.dadosNasc.paisNascto.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['paisnac'] = read_from_xml(evtCdBenefIn.beneficiario.dadosNasc.paisNac.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nmmae'] = read_from_xml(evtCdBenefIn.beneficiario.dadosNasc.nmMae.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nmpai'] = read_from_xml(evtCdBenefIn.beneficiario.dadosNasc.nmPai.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2400_evtcdbenefin = s2400evtCdBenefIn.objects.create(**s2400_evtcdbenefin_dados)

    if 'beneficiario' in dir(evtCdBenefIn) and 'endereco' in dir(evtCdBenefIn.beneficiario):

        for endereco in evtCdBenefIn.beneficiario.endereco:

            s2400_endereco_dados = {}
            s2400_endereco_dados['s2400_evtcdbenefin_id'] = s2400_evtcdbenefin.id

            s2400_endereco = s2400endereco.objects.create(**s2400_endereco_dados)

            if 'brasil' in dir(endereco):

                for brasil in endereco.brasil:

                    s2400_brasil_dados = {}
                    s2400_brasil_dados['s2400_endereco_id'] = s2400_endereco.id

                    try:
                        s2400_brasil_dados['tplograd'] = read_from_xml(brasil.tpLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['dsclograd'] = read_from_xml(brasil.dscLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['nrlograd'] = read_from_xml(brasil.nrLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['complemento'] = read_from_xml(brasil.complemento.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['bairro'] = read_from_xml(brasil.bairro.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['cep'] = read_from_xml(brasil.cep.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['codmunic'] = read_from_xml(brasil.codMunic.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['uf'] = read_from_xml(brasil.uf.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2400_brasil = s2400brasil.objects.create(**s2400_brasil_dados)

            if 'exterior' in dir(endereco):

                for exterior in endereco.exterior:

                    s2400_exterior_dados = {}
                    s2400_exterior_dados['s2400_endereco_id'] = s2400_endereco.id

                    try:
                        s2400_exterior_dados['paisresid'] = read_from_xml(exterior.paisResid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['dsclograd'] = read_from_xml(exterior.dscLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['nrlograd'] = read_from_xml(exterior.nrLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['complemento'] = read_from_xml(exterior.complemento.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['bairro'] = read_from_xml(exterior.bairro.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['nmcid'] = read_from_xml(exterior.nmCid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['codpostal'] = read_from_xml(exterior.codPostal.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2400_exterior = s2400exterior.objects.create(**s2400_exterior_dados)

    if 'beneficiario' in dir(evtCdBenefIn) and 'dependente' in dir(evtCdBenefIn.beneficiario):

        for dependente in evtCdBenefIn.beneficiario.dependente:

            s2400_dependente_dados = {}
            s2400_dependente_dados['s2400_evtcdbenefin_id'] = s2400_evtcdbenefin.id

            try:
                s2400_dependente_dados['tpdep'] = read_from_xml(dependente.tpDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['nmdep'] = read_from_xml(dependente.nmDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['dtnascto'] = read_from_xml(dependente.dtNascto.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['cpfdep'] = read_from_xml(dependente.cpfDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['sexodep'] = read_from_xml(dependente.sexoDep.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['depirrf'] = read_from_xml(dependente.depIRRF.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['incfismen'] = read_from_xml(dependente.incFisMen.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['depfinsprev'] = read_from_xml(dependente.depFinsPrev.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2400_dependente = s2400dependente.objects.create(**s2400_dependente_dados)
    s2400_evtcdbenefin_dados['evento'] = 's2400'
    s2400_evtcdbenefin_dados['id'] = s2400_evtcdbenefin.id
    s2400_evtcdbenefin_dados['identidade_evento'] = doc.eSocial.evtCdBenefIn['Id']

    from emensageriapro.esocial.views.s2400_evtcdbenefin_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2400_evtcdbenefin.id)

    return s2400_evtcdbenefin_dados