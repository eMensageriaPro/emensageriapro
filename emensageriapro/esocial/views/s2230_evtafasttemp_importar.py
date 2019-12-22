# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2230.models import *
from emensageriapro.functions import read_from_xml



def read_s2230_evtafasttemp_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2230_evtafasttemp_obj(request, doc, status, validar)
    return dados



def read_s2230_evtafasttemp(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2230_evtafasttemp_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2230evtAfastTemp.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2230_evtafasttemp_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2230_evtafasttemp_dados = {}
    s2230_evtafasttemp_dados['status'] = status
    s2230_evtafasttemp_dados['arquivo_original'] = 1
    if arquivo:
        s2230_evtafasttemp_dados['arquivo'] = arquivo.arquivo
    s2230_evtafasttemp_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2230_evtafasttemp_dados['identidade'] = doc.eSocial.evtAfastTemp['Id']
    evtAfastTemp = doc.eSocial.evtAfastTemp

    try:
        s2230_evtafasttemp_dados['indretif'] = read_from_xml(evtAfastTemp.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['nrrecibo'] = read_from_xml(evtAfastTemp.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['tpamb'] = read_from_xml(evtAfastTemp.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['procemi'] = read_from_xml(evtAfastTemp.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['verproc'] = read_from_xml(evtAfastTemp.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['tpinsc'] = read_from_xml(evtAfastTemp.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['nrinsc'] = read_from_xml(evtAfastTemp.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['cpftrab'] = read_from_xml(evtAfastTemp.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['nistrab'] = read_from_xml(evtAfastTemp.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['matricula'] = read_from_xml(evtAfastTemp.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['codcateg'] = read_from_xml(evtAfastTemp.ideVinculo.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    s2230_evtafasttemp = s2230evtAfastTemp.objects.create(**s2230_evtafasttemp_dados)

    if 'infoAfastamento' in dir(evtAfastTemp) and 'iniAfastamento' in dir(evtAfastTemp.infoAfastamento):

        for iniAfastamento in evtAfastTemp.infoAfastamento.iniAfastamento:

            s2230_iniafastamento_dados = {}
            s2230_iniafastamento_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp.id

            try:
                s2230_iniafastamento_dados['dtiniafast'] = read_from_xml(iniAfastamento.dtIniAfast.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2230_iniafastamento_dados['codmotafast'] = read_from_xml(iniAfastamento.codMotAfast.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2230_iniafastamento_dados['infomesmomtv'] = read_from_xml(iniAfastamento.infoMesmoMtv.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2230_iniafastamento_dados['tpacidtransito'] = read_from_xml(iniAfastamento.tpAcidTransito.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2230_iniafastamento_dados['observacao'] = read_from_xml(iniAfastamento.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2230_iniafastamento = s2230iniAfastamento.objects.create(**s2230_iniafastamento_dados)

            if 'infoAtestado' in dir(iniAfastamento):

                for infoAtestado in iniAfastamento.infoAtestado:

                    s2230_infoatestado_dados = {}
                    s2230_infoatestado_dados['s2230_iniafastamento_id'] = s2230_iniafastamento.id

                    try:
                        s2230_infoatestado_dados['codcid'] = read_from_xml(infoAtestado.codCID.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2230_infoatestado_dados['qtddiasafast'] = read_from_xml(infoAtestado.qtdDiasAfast.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s2230_infoatestado = s2230infoAtestado.objects.create(**s2230_infoatestado_dados)

                    if 'emitente' in dir(infoAtestado):

                        for emitente in infoAtestado.emitente:

                            s2230_emitente_dados = {}
                            s2230_emitente_dados['s2230_infoatestado_id'] = s2230_infoatestado.id
        
                            try:
                                s2230_emitente_dados['nmemit'] = read_from_xml(emitente.nmEmit.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2230_emitente_dados['ideoc'] = read_from_xml(emitente.ideOC.cdata, 'esocial', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2230_emitente_dados['nroc'] = read_from_xml(emitente.nrOc.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s2230_emitente_dados['ufoc'] = read_from_xml(emitente.ufOC.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass

                            s2230_emitente = s2230emitente.objects.create(**s2230_emitente_dados)

            if 'infoCessao' in dir(iniAfastamento):

                for infoCessao in iniAfastamento.infoCessao:

                    s2230_infocessao_dados = {}
                    s2230_infocessao_dados['s2230_iniafastamento_id'] = s2230_iniafastamento.id

                    try:
                        s2230_infocessao_dados['cnpjcess'] = read_from_xml(infoCessao.cnpjCess.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2230_infocessao_dados['infonus'] = read_from_xml(infoCessao.infOnus.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s2230_infocessao = s2230infoCessao.objects.create(**s2230_infocessao_dados)

            if 'infoMandSind' in dir(iniAfastamento):

                for infoMandSind in iniAfastamento.infoMandSind:

                    s2230_infomandsind_dados = {}
                    s2230_infomandsind_dados['s2230_iniafastamento_id'] = s2230_iniafastamento.id

                    try:
                        s2230_infomandsind_dados['cnpjsind'] = read_from_xml(infoMandSind.cnpjSind.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s2230_infomandsind_dados['infonusremun'] = read_from_xml(infoMandSind.infOnusRemun.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s2230_infomandsind = s2230infoMandSind.objects.create(**s2230_infomandsind_dados)

    if 'infoAfastamento' in dir(evtAfastTemp) and 'infoRetif' in dir(evtAfastTemp.infoAfastamento):

        for infoRetif in evtAfastTemp.infoAfastamento.infoRetif:

            s2230_inforetif_dados = {}
            s2230_inforetif_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp.id

            try:
                s2230_inforetif_dados['origretif'] = read_from_xml(infoRetif.origRetif.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2230_inforetif_dados['tpproc'] = read_from_xml(infoRetif.tpProc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2230_inforetif_dados['nrproc'] = read_from_xml(infoRetif.nrProc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2230_inforetif = s2230infoRetif.objects.create(**s2230_inforetif_dados)

    if 'infoAfastamento' in dir(evtAfastTemp) and 'fimAfastamento' in dir(evtAfastTemp.infoAfastamento):

        for fimAfastamento in evtAfastTemp.infoAfastamento.fimAfastamento:

            s2230_fimafastamento_dados = {}
            s2230_fimafastamento_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp.id

            try:
                s2230_fimafastamento_dados['dttermafast'] = read_from_xml(fimAfastamento.dtTermAfast.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            s2230_fimafastamento = s2230fimAfastamento.objects.create(**s2230_fimafastamento_dados)
    s2230_evtafasttemp_dados['evento'] = 's2230'
    s2230_evtafasttemp_dados['id'] = s2230_evtafasttemp.id
    s2230_evtafasttemp_dados['identidade_evento'] = doc.eSocial.evtAfastTemp['Id']

    from emensageriapro.esocial.views.s2230_evtafasttemp_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2230_evtafasttemp.id)

    return s2230_evtafasttemp_dados