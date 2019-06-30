#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r4040.models import *
from emensageriapro.functions import read_from_xml



def read_r4040_evtbenefnid_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4040_evtbenefnid_obj(request, doc, status, validar)
    return dados



def read_r4040_evtbenefnid(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r4040_evtbenefnid_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r4040evtBenefNId.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r4040_evtbenefnid_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r4040_evtbenefnid_dados = {}
    r4040_evtbenefnid_dados['status'] = status
    r4040_evtbenefnid_dados['arquivo_original'] = 1
    if arquivo:
        r4040_evtbenefnid_dados['arquivo'] = arquivo.arquivo
    r4040_evtbenefnid_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r4040_evtbenefnid_dados['identidade'] = doc.Reinf.evtBenefNId['id']
    evtBenefNId = doc.Reinf.evtBenefNId

    try:
        r4040_evtbenefnid_dados['indretif'] = read_from_xml(evtBenefNId.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4040_evtbenefnid_dados['nrrecibo'] = read_from_xml(evtBenefNId.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4040_evtbenefnid_dados['perapur'] = read_from_xml(evtBenefNId.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4040_evtbenefnid_dados['tpamb'] = read_from_xml(evtBenefNId.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4040_evtbenefnid_dados['procemi'] = read_from_xml(evtBenefNId.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4040_evtbenefnid_dados['verproc'] = read_from_xml(evtBenefNId.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4040_evtbenefnid_dados['tpinsc'] = read_from_xml(evtBenefNId.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4040_evtbenefnid_dados['nrinsc'] = read_from_xml(evtBenefNId.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4040_evtbenefnid_dados['tpinscestab'] = read_from_xml(evtBenefNId.ideEstab.tpInscEstab.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4040_evtbenefnid_dados['nrinscestab'] = read_from_xml(evtBenefNId.ideEstab.nrInscEstab.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r4040_evtbenefnid = r4040evtBenefNId.objects.create(**r4040_evtbenefnid_dados)

    if 'ideEstab' in dir(evtBenefNId) and 'ideNat' in dir(evtBenefNId.ideEstab):

        for ideNat in evtBenefNId.ideEstab.ideNat:

            r4040_idenat_dados = {}
            r4040_idenat_dados['r4040_evtbenefnid_id'] = r4040_evtbenefnid.id

            try:
                r4040_idenat_dados['natrendim'] = read_from_xml(ideNat.natRendim.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            r4040_idenat = r4040ideNat.objects.create(**r4040_idenat_dados)

            if 'infoPgto' in dir(ideNat):

                for infoPgto in ideNat.infoPgto:

                    r4040_infopgto_dados = {}
                    r4040_infopgto_dados['r4040_idenat_id'] = r4040_idenat.id

                    try:
                        r4040_infopgto_dados['dtfg'] = read_from_xml(infoPgto.dtFG.cdata, 'efdreinf', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        r4040_infopgto_dados['vlrliq'] = read_from_xml(infoPgto.vlrLiq.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4040_infopgto_dados['vlrreaj'] = read_from_xml(infoPgto.vlrReaj.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4040_infopgto_dados['vlrir'] = read_from_xml(infoPgto.vlrIR.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4040_infopgto_dados['descr'] = read_from_xml(infoPgto.descr.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r4040_infopgto = r4040infoPgto.objects.create(**r4040_infopgto_dados)
    r4040_evtbenefnid_dados['evento'] = 'r4040'
    r4040_evtbenefnid_dados['id'] = r4040_evtbenefnid.id
    r4040_evtbenefnid_dados['identidade_evento'] = doc.Reinf.evtBenefNId['id']

    from emensageriapro.efdreinf.views.r4040_evtbenefnid_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r4040_evtbenefnid.id)

    return r4040_evtbenefnid_dados