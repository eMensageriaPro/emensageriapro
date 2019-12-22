# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r3010.models import *
from emensageriapro.functions import read_from_xml



def read_r3010_evtespdesportivo_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r3010_evtespdesportivo_obj(request, doc, status, validar)
    return dados



def read_r3010_evtespdesportivo(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r3010_evtespdesportivo_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r3010evtEspDesportivo.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r3010_evtespdesportivo_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r3010_evtespdesportivo_dados = {}
    r3010_evtespdesportivo_dados['status'] = status
    r3010_evtespdesportivo_dados['arquivo_original'] = 1
    if arquivo:
        r3010_evtespdesportivo_dados['arquivo'] = arquivo.arquivo
    r3010_evtespdesportivo_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r3010_evtespdesportivo_dados['identidade'] = doc.Reinf.evtEspDesportivo['id']
    evtEspDesportivo = doc.Reinf.evtEspDesportivo

    try:
        r3010_evtespdesportivo_dados['indretif'] = read_from_xml(evtEspDesportivo.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['nrrecibo'] = read_from_xml(evtEspDesportivo.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['dtapuracao'] = read_from_xml(evtEspDesportivo.ideEvento.dtApuracao.cdata, 'efdreinf', 'D', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['tpamb'] = read_from_xml(evtEspDesportivo.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['procemi'] = read_from_xml(evtEspDesportivo.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['verproc'] = read_from_xml(evtEspDesportivo.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['tpinsc'] = read_from_xml(evtEspDesportivo.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['nrinsc'] = read_from_xml(evtEspDesportivo.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['tpinscestab'] = read_from_xml(evtEspDesportivo.ideContri.ideEstab.tpInscEstab.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['nrinscestab'] = read_from_xml(evtEspDesportivo.ideContri.ideEstab.nrInscEstab.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['vlrreceitatotal'] = read_from_xml(evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrReceitaTotal.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['vlrcp'] = read_from_xml(evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrCP.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['vlrcpsusptotal'] = read_from_xml(evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrCPSuspTotal.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['vlrreceitaclubes'] = read_from_xml(evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrReceitaClubes.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    try:
        r3010_evtespdesportivo_dados['vlrretparc'] = read_from_xml(evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrRetParc.cdata, 'efdreinf', 'N', 2)
    except AttributeError:
        pass

    r3010_evtespdesportivo = r3010evtEspDesportivo.objects.create(**r3010_evtespdesportivo_dados)

    if 'ideContri' in dir(evtEspDesportivo) and 'ideEstab' in dir(evtEspDesportivo.ideContri) and 'boletim' in dir(evtEspDesportivo.ideContri.ideEstab):

        for boletim in evtEspDesportivo.ideContri.ideEstab.boletim:

            r3010_boletim_dados = {}
            r3010_boletim_dados['r3010_evtespdesportivo_id'] = r3010_evtespdesportivo.id

            try:
                r3010_boletim_dados['nrboletim'] = read_from_xml(boletim.nrBoletim.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['tpcompeticao'] = read_from_xml(boletim.tpCompeticao.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['categevento'] = read_from_xml(boletim.categEvento.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['moddesportiva'] = read_from_xml(boletim.modDesportiva.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['nomecompeticao'] = read_from_xml(boletim.nomeCompeticao.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['cnpjmandante'] = read_from_xml(boletim.cnpjMandante.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['cnpjvisitante'] = read_from_xml(boletim.cnpjVisitante.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['nomevisitante'] = read_from_xml(boletim.nomeVisitante.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['pracadesportiva'] = read_from_xml(boletim.pracaDesportiva.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['codmunic'] = read_from_xml(boletim.codMunic.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['uf'] = read_from_xml(boletim.uf.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['qtdepagantes'] = read_from_xml(boletim.qtdePagantes.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r3010_boletim_dados['qtdenaopagantes'] = read_from_xml(boletim.qtdeNaoPagantes.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            r3010_boletim = r3010boletim.objects.create(**r3010_boletim_dados)

            if 'receitaIngressos' in dir(boletim):

                for receitaIngressos in boletim.receitaIngressos:

                    r3010_receitaingressos_dados = {}
                    r3010_receitaingressos_dados['r3010_boletim_id'] = r3010_boletim.id

                    try:
                        r3010_receitaingressos_dados['tpingresso'] = read_from_xml(receitaIngressos.tpIngresso.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r3010_receitaingressos_dados['descingr'] = read_from_xml(receitaIngressos.descIngr.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r3010_receitaingressos_dados['qtdeingrvenda'] = read_from_xml(receitaIngressos.qtdeIngrVenda.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r3010_receitaingressos_dados['qtdeingrvendidos'] = read_from_xml(receitaIngressos.qtdeIngrVendidos.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r3010_receitaingressos_dados['qtdeingrdev'] = read_from_xml(receitaIngressos.qtdeIngrDev.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r3010_receitaingressos_dados['precoindiv'] = read_from_xml(receitaIngressos.precoIndiv.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r3010_receitaingressos_dados['vlrtotal'] = read_from_xml(receitaIngressos.vlrTotal.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r3010_receitaingressos = r3010receitaIngressos.objects.create(**r3010_receitaingressos_dados)

            if 'outrasReceitas' in dir(boletim):

                for outrasReceitas in boletim.outrasReceitas:

                    r3010_outrasreceitas_dados = {}
                    r3010_outrasreceitas_dados['r3010_boletim_id'] = r3010_boletim.id

                    try:
                        r3010_outrasreceitas_dados['tpreceita'] = read_from_xml(outrasReceitas.tpReceita.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r3010_outrasreceitas_dados['vlrreceita'] = read_from_xml(outrasReceitas.vlrReceita.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r3010_outrasreceitas_dados['descreceita'] = read_from_xml(outrasReceitas.descReceita.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r3010_outrasreceitas = r3010outrasReceitas.objects.create(**r3010_outrasreceitas_dados)

    if 'ideContri' in dir(evtEspDesportivo) and 'ideEstab' in dir(evtEspDesportivo.ideContri) and 'receitaTotal' in dir(evtEspDesportivo.ideContri.ideEstab) and 'infoProc' in dir(evtEspDesportivo.ideContri.ideEstab.receitaTotal):

        for infoProc in evtEspDesportivo.ideContri.ideEstab.receitaTotal.infoProc:

            r3010_infoproc_dados = {}
            r3010_infoproc_dados['r3010_evtespdesportivo_id'] = r3010_evtespdesportivo.id

            try:
                r3010_infoproc_dados['tpproc'] = read_from_xml(infoProc.tpProc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r3010_infoproc_dados['nrproc'] = read_from_xml(infoProc.nrProc.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r3010_infoproc_dados['codsusp'] = read_from_xml(infoProc.codSusp.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r3010_infoproc_dados['vlrcpsusp'] = read_from_xml(infoProc.vlrCPSusp.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            r3010_infoproc = r3010infoProc.objects.create(**r3010_infoproc_dados)
    r3010_evtespdesportivo_dados['evento'] = 'r3010'
    r3010_evtespdesportivo_dados['id'] = r3010_evtespdesportivo.id
    r3010_evtespdesportivo_dados['identidade_evento'] = doc.Reinf.evtEspDesportivo['id']

    from emensageriapro.efdreinf.views.r3010_evtespdesportivo_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r3010_evtespdesportivo.id)

    return r3010_evtespdesportivo_dados