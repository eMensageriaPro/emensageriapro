# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2410.models import *
from emensageriapro.functions import read_from_xml



def read_s2410_evtcdbenin_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2410_evtcdbenin_obj(request, doc, status, validar)
    return dados



def read_s2410_evtcdbenin(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2410_evtcdbenin_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2410evtCdBenIn.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2410_evtcdbenin_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2410_evtcdbenin_dados = {}
    s2410_evtcdbenin_dados['status'] = status
    s2410_evtcdbenin_dados['arquivo_original'] = 1
    if arquivo:
        s2410_evtcdbenin_dados['arquivo'] = arquivo.arquivo
    s2410_evtcdbenin_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2410_evtcdbenin_dados['identidade'] = doc.eSocial.evtCdBenIn['Id']
    evtCdBenIn = doc.eSocial.evtCdBenIn

    try:
        s2410_evtcdbenin_dados['indretif'] = read_from_xml(evtCdBenIn.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['nrrecibo'] = read_from_xml(evtCdBenIn.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['tpamb'] = read_from_xml(evtCdBenIn.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['procemi'] = read_from_xml(evtCdBenIn.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['verproc'] = read_from_xml(evtCdBenIn.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['tpinsc'] = read_from_xml(evtCdBenIn.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['nrinsc'] = read_from_xml(evtCdBenIn.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['cpfbenef'] = read_from_xml(evtCdBenIn.beneficiario.cpfBenef.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['matricula'] = read_from_xml(evtCdBenIn.beneficiario.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['cnpjorigem'] = read_from_xml(evtCdBenIn.beneficiario.cnpjOrigem.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['cadini'] = read_from_xml(evtCdBenIn.infoBenInicio.cadIni.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['nrbeneficio'] = read_from_xml(evtCdBenIn.infoBenInicio.nrBeneficio.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['dtinibeneficio'] = read_from_xml(evtCdBenIn.infoBenInicio.dtIniBeneficio.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['tpbeneficio'] = read_from_xml(evtCdBenIn.infoBenInicio.dadosBeneficio.tpBeneficio.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['vrbeneficio'] = read_from_xml(evtCdBenIn.infoBenInicio.dadosBeneficio.vrBeneficio.cdata, 'esocial', 'N', 2)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['tpplanrp'] = read_from_xml(evtCdBenIn.infoBenInicio.dadosBeneficio.tpPlanRP.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['dsc'] = read_from_xml(evtCdBenIn.infoBenInicio.dadosBeneficio.dsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['inddecjud'] = read_from_xml(evtCdBenIn.infoBenInicio.dadosBeneficio.indDecJud.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2410_evtcdbenin_dados['indhomologtc'] = read_from_xml(evtCdBenIn.infoBenInicio.dadosBeneficio.indHomologTC.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2410_evtcdbenin = s2410evtCdBenIn.objects.create(**s2410_evtcdbenin_dados)

    if 'infoBenInicio' in dir(evtCdBenIn) and 'dadosBeneficio' in dir(evtCdBenIn.infoBenInicio) and 'infoPenMorte' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio):

        for infoPenMorte in evtCdBenIn.infoBenInicio.dadosBeneficio.infoPenMorte:

            s2410_infopenmorte_dados = {}
            s2410_infopenmorte_dados['s2410_evtcdbenin_id'] = s2410_evtcdbenin.id

            try:
                s2410_infopenmorte_dados['tppenmorte'] = read_from_xml(infoPenMorte.tpPenMorte.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2410_infopenmorte = s2410infoPenMorte.objects.create(**s2410_infopenmorte_dados)

            if 'instPenMorte' in dir(infoPenMorte):

                for instPenMorte in infoPenMorte.instPenMorte:

                    s2410_instpenmorte_dados = {}
                    s2410_instpenmorte_dados['s2410_infopenmorte_id'] = s2410_infopenmorte.id

                    try:
                        s2410_instpenmorte_dados['cpfinst'] = read_from_xml(instPenMorte.cpfInst.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2410_instpenmorte_dados['dtinst'] = read_from_xml(instPenMorte.dtInst.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s2410_instpenmorte_dados['intaposentado'] = read_from_xml(instPenMorte.intAposentado.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s2410_instpenmorte = s2410instPenMorte.objects.create(**s2410_instpenmorte_dados)

    if 'infoBenInicio' in dir(evtCdBenIn) and 'dadosBeneficio' in dir(evtCdBenIn.infoBenInicio) and 'homologTC' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio):

        for homologTC in evtCdBenIn.infoBenInicio.dadosBeneficio.homologTC:

            s2410_homologtc_dados = {}
            s2410_homologtc_dados['s2410_evtcdbenin_id'] = s2410_evtcdbenin.id

            try:
                s2410_homologtc_dados['dthomol'] = read_from_xml(homologTC.dtHomol.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2410_homologtc_dados['nratolegal'] = read_from_xml(homologTC.nrAtoLegal.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2410_homologtc = s2410homologTC.objects.create(**s2410_homologtc_dados)
    s2410_evtcdbenin_dados['evento'] = 's2410'
    s2410_evtcdbenin_dados['id'] = s2410_evtcdbenin.id
    s2410_evtcdbenin_dados['identidade_evento'] = doc.eSocial.evtCdBenIn['Id']

    from emensageriapro.esocial.views.s2410_evtcdbenin_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2410_evtcdbenin.id)

    return s2410_evtcdbenin_dados