#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2405.models import *



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

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    # if validar:
    #     status = STATUS_EVENTO_IMPORTADO
    #
    # else:
    #     status = STATUS_EVENTO_CADASTRADO

    status = STATUS_EVENTO_IMPORTADO
    dados = read_s2405_evtcdbenefalt_obj(request, doc, status, validar, arquivo)

    s2405evtCdBenefAlt.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_s2405_evtcdbenefalt_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2405_evtcdbenefalt_dados = {}
    s2405_evtcdbenefalt_dados['status'] = status
    s2405_evtcdbenefalt_dados['arquivo_original'] = 1
    if arquivo:
        s2405_evtcdbenefalt_dados['arquivo'] = arquivo
    s2405_evtcdbenefalt_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2405_evtcdbenefalt_dados['identidade'] = doc.eSocial.evtCdBenefAlt['Id']
    evtCdBenefAlt = doc.eSocial.evtCdBenefAlt

    try:
        s2405_evtcdbenefalt_dados['indretif'] = evtCdBenefAlt.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nrrecibo'] = evtCdBenefAlt.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['tpamb'] = evtCdBenefAlt.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['procemi'] = evtCdBenefAlt.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['verproc'] = evtCdBenefAlt.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['tpinsc'] = evtCdBenefAlt.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nrinsc'] = evtCdBenefAlt.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['cpfbenef'] = evtCdBenefAlt.ideBenef.cpfBenef.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['dtalteracao'] = evtCdBenefAlt.alteracao.dtAlteracao.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nisbenef'] = evtCdBenefAlt.alteracao.dadosBenef.nisBenef.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nmbenefic'] = evtCdBenefAlt.alteracao.dadosBenef.nmBenefic.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['sexo'] = evtCdBenefAlt.alteracao.dadosBenef.sexo.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['racacor'] = evtCdBenefAlt.alteracao.dadosBenef.racaCor.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['estciv'] = evtCdBenefAlt.alteracao.dadosBenef.estCiv.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['incfismen'] = evtCdBenefAlt.alteracao.dadosBenef.incFisMen.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['dtincfismen'] = evtCdBenefAlt.alteracao.dadosBenef.dtIncFisMen.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['paisnac'] = evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.paisNac.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nmmae'] = evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmMae.cdata
    except AttributeError:
        pass

    try:
        s2405_evtcdbenefalt_dados['nmpai'] = evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmPai.cdata
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
                        s2405_brasil_dados['tplograd'] = brasil.tpLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['complemento'] = brasil.complemento.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['bairro'] = brasil.bairro.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['cep'] = brasil.cep.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['codmunic'] = brasil.codMunic.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_brasil_dados['uf'] = brasil.uf.cdata
                    except AttributeError:
                        pass

                    s2405_brasil = s2405brasil.objects.create(**s2405_brasil_dados)

            if 'exterior' in dir(endereco):

                for exterior in endereco.exterior:

                    s2405_exterior_dados = {}
                    s2405_exterior_dados['s2405_endereco_id'] = s2405_endereco.id

                    try:
                        s2405_exterior_dados['paisresid'] = exterior.paisResid.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['complemento'] = exterior.complemento.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['bairro'] = exterior.bairro.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['nmcid'] = exterior.nmCid.cdata
                    except AttributeError:
                        pass

                    try:
                        s2405_exterior_dados['codpostal'] = exterior.codPostal.cdata
                    except AttributeError:
                        pass

                    s2405_exterior = s2405exterior.objects.create(**s2405_exterior_dados)

    if 'alteracao' in dir(evtCdBenefAlt) and 'dadosBenef' in dir(evtCdBenefAlt.alteracao) and 'dependente' in dir(evtCdBenefAlt.alteracao.dadosBenef):

        for dependente in evtCdBenefAlt.alteracao.dadosBenef.dependente:

            s2405_dependente_dados = {}
            s2405_dependente_dados['s2405_evtcdbenefalt_id'] = s2405_evtcdbenefalt.id

            try:
                s2405_dependente_dados['tpdep'] = dependente.tpDep.cdata
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['nmdep'] = dependente.nmDep.cdata
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['incfismen'] = dependente.incFisMen.cdata
            except AttributeError:
                pass

            try:
                s2405_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
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