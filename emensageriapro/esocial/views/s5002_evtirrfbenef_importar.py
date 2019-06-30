#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5002.models import *
from emensageriapro.functions import read_from_xml



def read_s5002_evtirrfbenef_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5002_evtirrfbenef_obj(request, doc, status, validar)
    return dados



def read_s5002_evtirrfbenef(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s5002_evtirrfbenef_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s5002evtIrrfBenef.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s5002_evtirrfbenef_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5002_evtirrfbenef_dados = {}
    s5002_evtirrfbenef_dados['status'] = status
    s5002_evtirrfbenef_dados['arquivo_original'] = 1
    if arquivo:
        s5002_evtirrfbenef_dados['arquivo'] = arquivo.arquivo
    s5002_evtirrfbenef_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5002_evtirrfbenef_dados['identidade'] = doc.eSocial.evtIrrfBenef['Id']
    evtIrrfBenef = doc.eSocial.evtIrrfBenef

    try:
        s5002_evtirrfbenef_dados['nrrecarqbase'] = read_from_xml(evtIrrfBenef.ideEvento.nrRecArqBase.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5002_evtirrfbenef_dados['perapur'] = read_from_xml(evtIrrfBenef.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5002_evtirrfbenef_dados['tpinsc'] = read_from_xml(evtIrrfBenef.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s5002_evtirrfbenef_dados['nrinsc'] = read_from_xml(evtIrrfBenef.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5002_evtirrfbenef_dados['cpftrab'] = read_from_xml(evtIrrfBenef.ideTrabalhador.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s5002_evtirrfbenef = s5002evtIrrfBenef.objects.create(**s5002_evtirrfbenef_dados)

    if 'infoDep' in dir(evtIrrfBenef):

        for infoDep in evtIrrfBenef.infoDep:

            s5002_infodep_dados = {}
            s5002_infodep_dados['s5002_evtirrfbenef_id'] = s5002_evtirrfbenef.id

            try:
                s5002_infodep_dados['vrdeddep'] = read_from_xml(infoDep.vrDedDep.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s5002_infodep = s5002infoDep.objects.create(**s5002_infodep_dados)

    if 'infoIrrf' in dir(evtIrrfBenef):

        for infoIrrf in evtIrrfBenef.infoIrrf:

            s5002_infoirrf_dados = {}
            s5002_infoirrf_dados['s5002_evtirrfbenef_id'] = s5002_evtirrfbenef.id

            try:
                s5002_infoirrf_dados['codcateg'] = read_from_xml(infoIrrf.codCateg.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s5002_infoirrf_dados['indresbr'] = read_from_xml(infoIrrf.indResBr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s5002_infoirrf = s5002infoIrrf.objects.create(**s5002_infoirrf_dados)

            if 'basesIrrf' in dir(infoIrrf):

                for basesIrrf in infoIrrf.basesIrrf:

                    s5002_basesirrf_dados = {}
                    s5002_basesirrf_dados['s5002_infoirrf_id'] = s5002_infoirrf.id

                    try:
                        s5002_basesirrf_dados['tpvalor'] = read_from_xml(basesIrrf.tpValor.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_basesirrf_dados['valor'] = read_from_xml(basesIrrf.valor.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s5002_basesirrf = s5002basesIrrf.objects.create(**s5002_basesirrf_dados)

            if 'irrf' in dir(infoIrrf):

                for irrf in infoIrrf.irrf:

                    s5002_irrf_dados = {}
                    s5002_irrf_dados['s5002_infoirrf_id'] = s5002_infoirrf.id

                    try:
                        s5002_irrf_dados['tpcr'] = read_from_xml(irrf.tpCR.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_irrf_dados['vrirrfdesc'] = read_from_xml(irrf.vrIrrfDesc.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s5002_irrf = s5002irrf.objects.create(**s5002_irrf_dados)

            if 'idePgtoExt' in dir(infoIrrf):

                for idePgtoExt in infoIrrf.idePgtoExt:

                    s5002_idepgtoext_dados = {}
                    s5002_idepgtoext_dados['s5002_infoirrf_id'] = s5002_infoirrf.id

                    try:
                        s5002_idepgtoext_dados['codpais'] = read_from_xml(idePgtoExt.idePais.codPais.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_idepgtoext_dados['indnif'] = read_from_xml(idePgtoExt.idePais.indNIF.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_idepgtoext_dados['nifbenef'] = read_from_xml(idePgtoExt.idePais.nifBenef.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_idepgtoext_dados['dsclograd'] = read_from_xml(idePgtoExt.endExt.dscLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_idepgtoext_dados['nrlograd'] = read_from_xml(idePgtoExt.endExt.nrLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_idepgtoext_dados['complem'] = read_from_xml(idePgtoExt.endExt.complem.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_idepgtoext_dados['bairro'] = read_from_xml(idePgtoExt.endExt.bairro.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_idepgtoext_dados['nmcid'] = read_from_xml(idePgtoExt.endExt.nmCid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s5002_idepgtoext_dados['codpostal'] = read_from_xml(idePgtoExt.endExt.codPostal.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s5002_idepgtoext = s5002idePgtoExt.objects.create(**s5002_idepgtoext_dados)
    s5002_evtirrfbenef_dados['evento'] = 's5002'
    s5002_evtirrfbenef_dados['id'] = s5002_evtirrfbenef.id
    s5002_evtirrfbenef_dados['identidade_evento'] = doc.eSocial.evtIrrfBenef['Id']

    from emensageriapro.esocial.views.s5002_evtirrfbenef_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s5002_evtirrfbenef.id)

    return s5002_evtirrfbenef_dados