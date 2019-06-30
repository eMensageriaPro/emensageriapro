#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2210.models import *



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
        s2210_evtcat_dados['indretif'] = evtCAT.ideEvento.indRetif.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['nrrecibo'] = evtCAT.ideEvento.nrRecibo.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tpamb'] = evtCAT.ideEvento.tpAmb.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['procemi'] = evtCAT.ideEvento.procEmi.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['verproc'] = evtCAT.ideEvento.verProc.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tpinsc'] = evtCAT.ideEmpregador.tpInsc.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['nrinsc'] = evtCAT.ideEmpregador.nrInsc.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['cpftrab'] = evtCAT.ideVinculo.cpfTrab.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['nistrab'] = evtCAT.ideVinculo.nisTrab.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['matricula'] = evtCAT.ideVinculo.matricula.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codcateg'] = evtCAT.ideVinculo.codCateg.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['dtacid'] = evtCAT.cat.dtAcid.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tpacid'] = evtCAT.cat.tpAcid.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['hracid'] = evtCAT.cat.hrAcid.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['hrstrabantesacid'] = evtCAT.cat.hrsTrabAntesAcid.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tpcat'] = evtCAT.cat.tpCat.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['indcatobito'] = evtCAT.cat.indCatObito.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['dtobito'] = evtCAT.cat.dtObito.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['indcomunpolicia'] = evtCAT.cat.indComunPolicia.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codsitgeradora'] = evtCAT.cat.codSitGeradora.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['iniciatcat'] = evtCAT.cat.iniciatCAT.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['obscat'] = evtCAT.cat.obsCAT.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['observacao'] = evtCAT.cat.observacao.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tplocal'] = evtCAT.cat.localAcidente.tpLocal.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['dsclocal'] = evtCAT.cat.localAcidente.dscLocal.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codamb'] = evtCAT.cat.localAcidente.codAmb.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['tplograd'] = evtCAT.cat.localAcidente.tpLograd.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['dsclograd'] = evtCAT.cat.localAcidente.dscLograd.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['nrlograd'] = evtCAT.cat.localAcidente.nrLograd.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['complemento'] = evtCAT.cat.localAcidente.complemento.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['bairro'] = evtCAT.cat.localAcidente.bairro.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['cep'] = evtCAT.cat.localAcidente.cep.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codmunic'] = evtCAT.cat.localAcidente.codMunic.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['uf'] = evtCAT.cat.localAcidente.uf.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['pais'] = evtCAT.cat.localAcidente.pais.cdata
    except AttributeError:
        pass

    try:
        s2210_evtcat_dados['codpostal'] = evtCAT.cat.localAcidente.codPostal.cdata
    except AttributeError:
        pass

    s2210_evtcat = s2210evtCAT.objects.create(**s2210_evtcat_dados)

    if 'cat' in dir(evtCAT) and 'localAcidente' in dir(evtCAT.cat) and 'ideLocalAcid' in dir(evtCAT.cat.localAcidente):

        for ideLocalAcid in evtCAT.cat.localAcidente.ideLocalAcid:

            s2210_idelocalacid_dados = {}
            s2210_idelocalacid_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_idelocalacid_dados['tpinsc'] = ideLocalAcid.tpInsc.cdata
            except AttributeError:
                pass

            try:
                s2210_idelocalacid_dados['nrinsc'] = ideLocalAcid.nrInsc.cdata
            except AttributeError:
                pass

            s2210_idelocalacid = s2210ideLocalAcid.objects.create(**s2210_idelocalacid_dados)

    if 'cat' in dir(evtCAT) and 'parteAtingida' in dir(evtCAT.cat):

        for parteAtingida in evtCAT.cat.parteAtingida:

            s2210_parteatingida_dados = {}
            s2210_parteatingida_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_parteatingida_dados['codparteating'] = parteAtingida.codParteAting.cdata
            except AttributeError:
                pass

            try:
                s2210_parteatingida_dados['lateralidade'] = parteAtingida.lateralidade.cdata
            except AttributeError:
                pass

            s2210_parteatingida = s2210parteAtingida.objects.create(**s2210_parteatingida_dados)

    if 'cat' in dir(evtCAT) and 'agenteCausador' in dir(evtCAT.cat):

        for agenteCausador in evtCAT.cat.agenteCausador:

            s2210_agentecausador_dados = {}
            s2210_agentecausador_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_agentecausador_dados['codagntcausador'] = agenteCausador.codAgntCausador.cdata
            except AttributeError:
                pass

            s2210_agentecausador = s2210agenteCausador.objects.create(**s2210_agentecausador_dados)

    if 'cat' in dir(evtCAT) and 'atestado' in dir(evtCAT.cat):

        for atestado in evtCAT.cat.atestado:

            s2210_atestado_dados = {}
            s2210_atestado_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_atestado_dados['codcnes'] = atestado.codCNES.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['dtatendimento'] = atestado.dtAtendimento.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['hratendimento'] = atestado.hrAtendimento.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['indinternacao'] = atestado.indInternacao.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['durtrat'] = atestado.durTrat.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['indafast'] = atestado.indAfast.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['dsclesao'] = atestado.dscLesao.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['dsccomplesao'] = atestado.dscCompLesao.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['diagprovavel'] = atestado.diagProvavel.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['codcid'] = atestado.codCID.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['observacao'] = atestado.observacao.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['nmemit'] = atestado.emitente.nmEmit.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['ideoc'] = atestado.emitente.ideOC.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['nroc'] = atestado.emitente.nrOC.cdata
            except AttributeError:
                pass

            try:
                s2210_atestado_dados['ufoc'] = atestado.emitente.ufOC.cdata
            except AttributeError:
                pass

            s2210_atestado = s2210atestado.objects.create(**s2210_atestado_dados)

    if 'cat' in dir(evtCAT) and 'catOrigem' in dir(evtCAT.cat):

        for catOrigem in evtCAT.cat.catOrigem:

            s2210_catorigem_dados = {}
            s2210_catorigem_dados['s2210_evtcat_id'] = s2210_evtcat.id

            try:
                s2210_catorigem_dados['dtcatorig'] = catOrigem.dtCatOrig.cdata
            except AttributeError:
                pass

            try:
                s2210_catorigem_dados['nrreccatorig'] = catOrigem.nrRecCatOrig.cdata
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