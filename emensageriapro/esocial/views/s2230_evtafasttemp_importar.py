#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2230.models import *



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
        s2230_evtafasttemp_dados['indretif'] = evtAfastTemp.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['nrrecibo'] = evtAfastTemp.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['tpamb'] = evtAfastTemp.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['procemi'] = evtAfastTemp.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['verproc'] = evtAfastTemp.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['tpinsc'] = evtAfastTemp.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['nrinsc'] = evtAfastTemp.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['cpftrab'] = evtAfastTemp.ideVinculo.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['nistrab'] = evtAfastTemp.ideVinculo.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['matricula'] = evtAfastTemp.ideVinculo.matricula.cdata
    except AttributeError:
        pass

    try:
        s2230_evtafasttemp_dados['codcateg'] = evtAfastTemp.ideVinculo.codCateg.cdata
    except AttributeError:
        pass

    s2230_evtafasttemp = s2230evtAfastTemp.objects.create(**s2230_evtafasttemp_dados)

    if 'infoAfastamento' in dir(evtAfastTemp) and 'iniAfastamento' in dir(evtAfastTemp.infoAfastamento):

        for iniAfastamento in evtAfastTemp.infoAfastamento.iniAfastamento:

            s2230_iniafastamento_dados = {}
            s2230_iniafastamento_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp.id

            try:
                s2230_iniafastamento_dados['dtiniafast'] = iniAfastamento.dtIniAfast.cdata
            except AttributeError:
                pass

            try:
                s2230_iniafastamento_dados['codmotafast'] = iniAfastamento.codMotAfast.cdata
            except AttributeError:
                pass

            try:
                s2230_iniafastamento_dados['infomesmomtv'] = iniAfastamento.infoMesmoMtv.cdata
            except AttributeError:
                pass

            try:
                s2230_iniafastamento_dados['tpacidtransito'] = iniAfastamento.tpAcidTransito.cdata
            except AttributeError:
                pass

            try:
                s2230_iniafastamento_dados['observacao'] = iniAfastamento.observacao.cdata
            except AttributeError:
                pass

            s2230_iniafastamento = s2230iniAfastamento.objects.create(**s2230_iniafastamento_dados)

            if 'infoAtestado' in dir(iniAfastamento):

                for infoAtestado in iniAfastamento.infoAtestado:

                    s2230_infoatestado_dados = {}
                    s2230_infoatestado_dados['s2230_iniafastamento_id'] = s2230_iniafastamento.id

                    try:
                        s2230_infoatestado_dados['codcid'] = infoAtestado.codCID.cdata
                    except AttributeError:
                        pass

                    try:
                        s2230_infoatestado_dados['qtddiasafast'] = infoAtestado.qtdDiasAfast.cdata
                    except AttributeError:
                        pass

                    s2230_infoatestado = s2230infoAtestado.objects.create(**s2230_infoatestado_dados)

                    if 'emitente' in dir(infoAtestado):

                        for emitente in infoAtestado.emitente:

                            s2230_emitente_dados = {}
                            s2230_emitente_dados['s2230_infoatestado_id'] = s2230_infoatestado.id
        
                            try:
                                s2230_emitente_dados['nmemit'] = emitente.nmEmit.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2230_emitente_dados['ideoc'] = emitente.ideOC.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2230_emitente_dados['nroc'] = emitente.nrOc.cdata
                            except AttributeError:
                                pass
        
                            try:
                                s2230_emitente_dados['ufoc'] = emitente.ufOC.cdata
                            except AttributeError:
                                pass

                            s2230_emitente = s2230emitente.objects.create(**s2230_emitente_dados)

            if 'infoCessao' in dir(iniAfastamento):

                for infoCessao in iniAfastamento.infoCessao:

                    s2230_infocessao_dados = {}
                    s2230_infocessao_dados['s2230_iniafastamento_id'] = s2230_iniafastamento.id

                    try:
                        s2230_infocessao_dados['cnpjcess'] = infoCessao.cnpjCess.cdata
                    except AttributeError:
                        pass

                    try:
                        s2230_infocessao_dados['infonus'] = infoCessao.infOnus.cdata
                    except AttributeError:
                        pass

                    s2230_infocessao = s2230infoCessao.objects.create(**s2230_infocessao_dados)

            if 'infoMandSind' in dir(iniAfastamento):

                for infoMandSind in iniAfastamento.infoMandSind:

                    s2230_infomandsind_dados = {}
                    s2230_infomandsind_dados['s2230_iniafastamento_id'] = s2230_iniafastamento.id

                    try:
                        s2230_infomandsind_dados['cnpjsind'] = infoMandSind.cnpjSind.cdata
                    except AttributeError:
                        pass

                    try:
                        s2230_infomandsind_dados['infonusremun'] = infoMandSind.infOnusRemun.cdata
                    except AttributeError:
                        pass

                    s2230_infomandsind = s2230infoMandSind.objects.create(**s2230_infomandsind_dados)

    if 'infoAfastamento' in dir(evtAfastTemp) and 'infoRetif' in dir(evtAfastTemp.infoAfastamento):

        for infoRetif in evtAfastTemp.infoAfastamento.infoRetif:

            s2230_inforetif_dados = {}
            s2230_inforetif_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp.id

            try:
                s2230_inforetif_dados['origretif'] = infoRetif.origRetif.cdata
            except AttributeError:
                pass

            try:
                s2230_inforetif_dados['tpproc'] = infoRetif.tpProc.cdata
            except AttributeError:
                pass

            try:
                s2230_inforetif_dados['nrproc'] = infoRetif.nrProc.cdata
            except AttributeError:
                pass

            s2230_inforetif = s2230infoRetif.objects.create(**s2230_inforetif_dados)

    if 'infoAfastamento' in dir(evtAfastTemp) and 'fimAfastamento' in dir(evtAfastTemp.infoAfastamento):

        for fimAfastamento in evtAfastTemp.infoAfastamento.fimAfastamento:

            s2230_fimafastamento_dados = {}
            s2230_fimafastamento_dados['s2230_evtafasttemp_id'] = s2230_evtafasttemp.id

            try:
                s2230_fimafastamento_dados['dttermafast'] = fimAfastamento.dtTermAfast.cdata
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