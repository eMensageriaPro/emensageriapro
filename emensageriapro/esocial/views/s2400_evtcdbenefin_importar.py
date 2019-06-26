#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2400.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s2400_evtcdbenefin_obj(request, doc, status, validar, arquivo)
    novo_arquivo = arquivo.replace('/aguardando/', '/processado/')
    s2400evtCdBenefIn.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2400_evtcdbenefin_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2400_evtcdbenefin_dados = {}
    s2400_evtcdbenefin_dados['status'] = status
    s2400_evtcdbenefin_dados['arquivo_original'] = 1
    if arquivo:
        s2400_evtcdbenefin_dados['arquivo'] = arquivo
    s2400_evtcdbenefin_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2400_evtcdbenefin_dados['identidade'] = doc.eSocial.evtCdBenefIn['Id']
    evtCdBenefIn = doc.eSocial.evtCdBenefIn

    try:
        s2400_evtcdbenefin_dados['indretif'] = evtCdBenefIn.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nrrecibo'] = evtCdBenefIn.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['tpamb'] = evtCdBenefIn.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['procemi'] = evtCdBenefIn.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['verproc'] = evtCdBenefIn.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['tpinsc'] = evtCdBenefIn.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nrinsc'] = evtCdBenefIn.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['cpfbenef'] = evtCdBenefIn.beneficiario.cpfBenef.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nisbenef'] = evtCdBenefIn.beneficiario.nisBenef.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nmbenefic'] = evtCdBenefIn.beneficiario.nmBenefic.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['dtinicio'] = evtCdBenefIn.beneficiario.dtInicio.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['sexo'] = evtCdBenefIn.beneficiario.sexo.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['racacor'] = evtCdBenefIn.beneficiario.racaCor.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['estciv'] = evtCdBenefIn.beneficiario.estCiv.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['incfismen'] = evtCdBenefIn.beneficiario.incFisMen.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['dtincfismen'] = evtCdBenefIn.beneficiario.dtIncFisMen.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['dtnascto'] = evtCdBenefIn.beneficiario.dadosNasc.dtNascto.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['codmunic'] = evtCdBenefIn.beneficiario.dadosNasc.codMunic.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['uf'] = evtCdBenefIn.beneficiario.dadosNasc.uf.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['paisnascto'] = evtCdBenefIn.beneficiario.dadosNasc.paisNascto.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['paisnac'] = evtCdBenefIn.beneficiario.dadosNasc.paisNac.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nmmae'] = evtCdBenefIn.beneficiario.dadosNasc.nmMae.cdata
    except AttributeError:
        pass

    try:
        s2400_evtcdbenefin_dados['nmpai'] = evtCdBenefIn.beneficiario.dadosNasc.nmPai.cdata
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
                        s2400_brasil_dados['tplograd'] = brasil.tpLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['complemento'] = brasil.complemento.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['bairro'] = brasil.bairro.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['cep'] = brasil.cep.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['codmunic'] = brasil.codMunic.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_brasil_dados['uf'] = brasil.uf.cdata
                    except AttributeError:
                        pass

                    s2400_brasil = s2400brasil.objects.create(**s2400_brasil_dados)

            if 'exterior' in dir(endereco):

                for exterior in endereco.exterior:

                    s2400_exterior_dados = {}
                    s2400_exterior_dados['s2400_endereco_id'] = s2400_endereco.id

                    try:
                        s2400_exterior_dados['paisresid'] = exterior.paisResid.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['complemento'] = exterior.complemento.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['bairro'] = exterior.bairro.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['nmcid'] = exterior.nmCid.cdata
                    except AttributeError:
                        pass

                    try:
                        s2400_exterior_dados['codpostal'] = exterior.codPostal.cdata
                    except AttributeError:
                        pass

                    s2400_exterior = s2400exterior.objects.create(**s2400_exterior_dados)

    if 'beneficiario' in dir(evtCdBenefIn) and 'dependente' in dir(evtCdBenefIn.beneficiario):

        for dependente in evtCdBenefIn.beneficiario.dependente:

            s2400_dependente_dados = {}
            s2400_dependente_dados['s2400_evtcdbenefin_id'] = s2400_evtcdbenefin.id

            try:
                s2400_dependente_dados['tpdep'] = dependente.tpDep.cdata
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['nmdep'] = dependente.nmDep.cdata
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['incfismen'] = dependente.incFisMen.cdata
            except AttributeError:
                pass

            try:
                s2400_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
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