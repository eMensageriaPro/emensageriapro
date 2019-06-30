#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2210.models import *
from emensageriapro.functions import read_from_xml



def read_s2210_evtcat_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2210_evtcat_obj(request, doc, status, validar)
    return dados



def read_s2210_evtcat(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s2210_evtcat_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s2210evtCAT.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s2210_evtcat_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2210_evtcat_dados = {}
    s2210_evtcat_dados['status'] = status
    s2210_evtcat_dados['arquivo_original'] = 1
    if arquivo:
        s2210_evtcat_dados['arquivo'] = arquivo.arquivo
    s2210_evtcat_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2210_evtcat_dados['identidade'] = doc.eSocial.evtCAT['Id']
    evtCAT = doc.eSocial.evtCAT

    try:
        s2210_evtcat_dados['indretif'] = read_from_xml(evtCAT.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['nrrecibo'] = read_from_xml(evtCAT.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tpamb'] = read_from_xml(evtCAT.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['procemi'] = read_from_xml(evtCAT.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['verproc'] = read_from_xml(evtCAT.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tpinsc'] = read_from_xml(evtCAT.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['nrinsc'] = read_from_xml(evtCAT.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['cpftrab'] = read_from_xml(evtCAT.ideVinculo.cpfTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['nistrab'] = read_from_xml(evtCAT.ideVinculo.nisTrab.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['matricula'] = read_from_xml(evtCAT.ideVinculo.matricula.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codcateg'] = read_from_xml(evtCAT.ideVinculo.codCateg.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['dtacid'] = read_from_xml(evtCAT.cat.dtAcid.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tpacid'] = read_from_xml(evtCAT.cat.tpAcid.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['hracid'] = read_from_xml(evtCAT.cat.hrAcid.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['hrstrabantesacid'] = read_from_xml(evtCAT.cat.hrsTrabAntesAcid.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tpcat'] = read_from_xml(evtCAT.cat.tpCat.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['indcatobito'] = read_from_xml(evtCAT.cat.indCatObito.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['dtobito'] = read_from_xml(evtCAT.cat.dtObito.cdata, 'esocial', 'D', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['indcomunpolicia'] = read_from_xml(evtCAT.cat.indComunPolicia.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codsitgeradora'] = read_from_xml(evtCAT.cat.codSitGeradora.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['iniciatcat'] = read_from_xml(evtCAT.cat.iniciatCAT.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['obscat'] = read_from_xml(evtCAT.cat.obsCAT.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['observacao'] = read_from_xml(evtCAT.cat.observacao.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tplocal'] = read_from_xml(evtCAT.cat.localAcidente.tpLocal.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['dsclocal'] = read_from_xml(evtCAT.cat.localAcidente.dscLocal.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codamb'] = read_from_xml(evtCAT.cat.localAcidente.codAmb.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tplograd'] = read_from_xml(evtCAT.cat.localAcidente.tpLograd.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['dsclograd'] = read_from_xml(evtCAT.cat.localAcidente.dscLograd.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['nrlograd'] = read_from_xml(evtCAT.cat.localAcidente.nrLograd.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['complemento'] = read_from_xml(evtCAT.cat.localAcidente.complemento.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['bairro'] = read_from_xml(evtCAT.cat.localAcidente.bairro.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['cep'] = read_from_xml(evtCAT.cat.localAcidente.cep.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codmunic'] = read_from_xml(evtCAT.cat.localAcidente.codMunic.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['uf'] = read_from_xml(evtCAT.cat.localAcidente.uf.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['pais'] = read_from_xml(evtCAT.cat.localAcidente.pais.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codpostal'] = read_from_xml(evtCAT.cat.localAcidente.codPostal.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s2210_evtcat = s2210evtCAT.objects.create(**s2210_evtcat_dados)

    if 'cat' in dir(evtCAT) and 'localAcidente' in dir(evtCAT.cat) and 'ideLocalAcid' in dir(evtCAT.cat.localAcidente):

        for ideLocalAcid in evtCAT.cat.localAcidente.ideLocalAcid:

            s2210_idelocalacid_dados = {}
            s2210_idelocalacid_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_idelocalacid_dados['tpinsc'] = read_from_xml(ideLocalAcid.tpInsc.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2210_idelocalacid_dados['nrinsc'] = read_from_xml(ideLocalAcid.nrInsc.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2210_idelocalacid = s2210ideLocalAcid.objects.create(**s2210_idelocalacid_dados)

    if 'cat' in dir(evtCAT) and 'parteAtingida' in dir(evtCAT.cat):

        for parteAtingida in evtCAT.cat.parteAtingida:

            s2210_parteatingida_dados = {}
            s2210_parteatingida_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_parteatingida_dados['codparteating'] = read_from_xml(parteAtingida.codParteAting.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2210_parteatingida_dados['lateralidade'] = read_from_xml(parteAtingida.lateralidade.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2210_parteatingida = s2210parteAtingida.objects.create(**s2210_parteatingida_dados)

    if 'cat' in dir(evtCAT) and 'agenteCausador' in dir(evtCAT.cat):

        for agenteCausador in evtCAT.cat.agenteCausador:

            s2210_agentecausador_dados = {}
            s2210_agentecausador_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_agentecausador_dados['codagntcausador'] = read_from_xml(agenteCausador.codAgntCausador.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            s2210_agentecausador = s2210agenteCausador.objects.create(**s2210_agentecausador_dados)

    if 'cat' in dir(evtCAT) and 'atestado' in dir(evtCAT.cat):

        for atestado in evtCAT.cat.atestado:

            s2210_atestado_dados = {}
            s2210_atestado_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_atestado_dados['codcnes'] = read_from_xml(atestado.codCNES.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['dtatendimento'] = read_from_xml(atestado.dtAtendimento.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['hratendimento'] = read_from_xml(atestado.hrAtendimento.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['indinternacao'] = read_from_xml(atestado.indInternacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['durtrat'] = read_from_xml(atestado.durTrat.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['indafast'] = read_from_xml(atestado.indAfast.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['dsclesao'] = read_from_xml(atestado.dscLesao.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['dsccomplesao'] = read_from_xml(atestado.dscCompLesao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['diagprovavel'] = read_from_xml(atestado.diagProvavel.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['codcid'] = read_from_xml(atestado.codCID.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['observacao'] = read_from_xml(atestado.observacao.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['nmemit'] = read_from_xml(atestado.emitente.nmEmit.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['ideoc'] = read_from_xml(atestado.emitente.ideOC.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['nroc'] = read_from_xml(atestado.emitente.nrOC.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['ufoc'] = read_from_xml(atestado.emitente.ufOC.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2210_atestado = s2210atestado.objects.create(**s2210_atestado_dados)

    if 'cat' in dir(evtCAT) and 'catOrigem' in dir(evtCAT.cat):

        for catOrigem in evtCAT.cat.catOrigem:

            s2210_catorigem_dados = {}
            s2210_catorigem_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_catorigem_dados['dtcatorig'] = read_from_xml(catOrigem.dtCatOrig.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s2210_catorigem_dados['nrreccatorig'] = read_from_xml(catOrigem.nrRecCatOrig.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s2210_catorigem = s2210catOrigem.objects.create(**s2210_catorigem_dados)
    s2210_evtcat_dados['evento'] = 's2210'
    s2210_evtcat_dados['id'] = s2210_evtcat.id
    s2210_evtcat_dados['identidade_evento'] = doc.eSocial.evtCAT['Id']

    from emensageriapro.esocial.views.s2210_evtcat_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s2210_evtcat.id)

    return s2210_evtcat_dados