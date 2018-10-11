#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql




def read_s2210_evtcat(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    s2210_evtcat_dados = {}
    xmlns = doc.eSocial['xmlns'].split('/')
    if validar:
        s2210_evtcat_dados['status'] = 1
    else:
        s2210_evtcat_dados['status'] = 0
    s2210_evtcat_dados['versao'] = xmlns[len(xmlns)-1]
    s2210_evtcat_dados['identidade'] = doc.eSocial.evtCAT['Id']
    # verificacao = executar_sql("""SELECT count(*)
    #     FROM public.transmissor_eventos_esocial WHERE identidade = '%s';
    #     """ % s2210_evtcat_dados['identidade'], True)
    # if validar and verificacao[0][0] != 0:
    #     return False
    s2210_evtcat_dados['processamento_codigo_resposta'] = 1
    evtCAT = doc.eSocial.evtCAT
    
    if 'indRetif' in dir(evtCAT.ideEvento): s2210_evtcat_dados['indretif'] = evtCAT.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtCAT.ideEvento): s2210_evtcat_dados['nrrecibo'] = evtCAT.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtCAT.ideEvento): s2210_evtcat_dados['tpamb'] = evtCAT.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtCAT.ideEvento): s2210_evtcat_dados['procemi'] = evtCAT.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtCAT.ideEvento): s2210_evtcat_dados['verproc'] = evtCAT.ideEvento.verProc.cdata
    if 'tpRegistrador' in dir(evtCAT.ideRegistrador): s2210_evtcat_dados['tpregistrador'] = evtCAT.ideRegistrador.tpRegistrador.cdata
    if 'tpInsc' in dir(evtCAT.ideRegistrador): s2210_evtcat_dados['tpinsc'] = evtCAT.ideRegistrador.tpInsc.cdata
    if 'nrInsc' in dir(evtCAT.ideRegistrador): s2210_evtcat_dados['nrinsc'] = evtCAT.ideRegistrador.nrInsc.cdata
    if 'tpInsc' in dir(evtCAT.ideEmpregador): s2210_evtcat_dados['tpinsc'] = evtCAT.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtCAT.ideEmpregador): s2210_evtcat_dados['nrinsc'] = evtCAT.ideEmpregador.nrInsc.cdata
    if 'cpfTrab' in dir(evtCAT.ideTrabalhador): s2210_evtcat_dados['cpftrab'] = evtCAT.ideTrabalhador.cpfTrab.cdata
    if 'nisTrab' in dir(evtCAT.ideTrabalhador): s2210_evtcat_dados['nistrab'] = evtCAT.ideTrabalhador.nisTrab.cdata
    if 'dtAcid' in dir(evtCAT.cat): s2210_evtcat_dados['dtacid'] = evtCAT.cat.dtAcid.cdata
    if 'tpAcid' in dir(evtCAT.cat): s2210_evtcat_dados['tpacid'] = evtCAT.cat.tpAcid.cdata
    if 'hrAcid' in dir(evtCAT.cat): s2210_evtcat_dados['hracid'] = evtCAT.cat.hrAcid.cdata
    if 'hrsTrabAntesAcid' in dir(evtCAT.cat): s2210_evtcat_dados['hrstrabantesacid'] = evtCAT.cat.hrsTrabAntesAcid.cdata
    if 'tpCat' in dir(evtCAT.cat): s2210_evtcat_dados['tpcat'] = evtCAT.cat.tpCat.cdata
    if 'indCatObito' in dir(evtCAT.cat): s2210_evtcat_dados['indcatobito'] = evtCAT.cat.indCatObito.cdata
    if 'dtObito' in dir(evtCAT.cat): s2210_evtcat_dados['dtobito'] = evtCAT.cat.dtObito.cdata
    if 'indComunPolicia' in dir(evtCAT.cat): s2210_evtcat_dados['indcomunpolicia'] = evtCAT.cat.indComunPolicia.cdata
    if 'codSitGeradora' in dir(evtCAT.cat): s2210_evtcat_dados['codsitgeradora'] = evtCAT.cat.codSitGeradora.cdata
    if 'iniciatCAT' in dir(evtCAT.cat): s2210_evtcat_dados['iniciatcat'] = evtCAT.cat.iniciatCAT.cdata
    if 'observacao' in dir(evtCAT.cat): s2210_evtcat_dados['observacao'] = evtCAT.cat.observacao.cdata
    if 'tpLocal' in dir(evtCAT.cat.localAcidente): s2210_evtcat_dados['tplocal'] = evtCAT.cat.localAcidente.tpLocal.cdata
    if 'dscLocal' in dir(evtCAT.cat.localAcidente): s2210_evtcat_dados['dsclocal'] = evtCAT.cat.localAcidente.dscLocal.cdata
    if 'dscLograd' in dir(evtCAT.cat.localAcidente): s2210_evtcat_dados['dsclograd'] = evtCAT.cat.localAcidente.dscLograd.cdata
    if 'nrLograd' in dir(evtCAT.cat.localAcidente): s2210_evtcat_dados['nrlograd'] = evtCAT.cat.localAcidente.nrLograd.cdata
    if 'codMunic' in dir(evtCAT.cat.localAcidente): s2210_evtcat_dados['codmunic'] = evtCAT.cat.localAcidente.codMunic.cdata
    if 'uf' in dir(evtCAT.cat.localAcidente): s2210_evtcat_dados['uf'] = evtCAT.cat.localAcidente.uf.cdata
    if 'cnpjLocalAcid' in dir(evtCAT.cat.localAcidente): s2210_evtcat_dados['cnpjlocalacid'] = evtCAT.cat.localAcidente.cnpjLocalAcid.cdata
    if 'pais' in dir(evtCAT.cat.localAcidente): s2210_evtcat_dados['pais'] = evtCAT.cat.localAcidente.pais.cdata
    if 'codPostal' in dir(evtCAT.cat.localAcidente): s2210_evtcat_dados['codpostal'] = evtCAT.cat.localAcidente.codPostal.cdata
    if 'inclusao' in dir(evtCAT.cat): s2210_evtcat_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCAT.cat): s2210_evtcat_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCAT.cat): s2210_evtcat_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2210_evtcat', s2210_evtcat_dados)
    resp = executar_sql(insert, True)
    s2210_evtcat_id = resp[0][0]
    dados['evento'] = 's2210'
    dados['identidade'] = s2210_evtcat_id
    dados['identidade_evento'] = doc.eSocial.evtCAT['Id']
    dados['status'] = 1

    if 'parteAtingida' in dir(evtCAT.cat):
        for parteAtingida in evtCAT.cat.parteAtingida:
            s2210_parteatingida_dados = {}
            s2210_parteatingida_dados['s2210_evtcat_id'] = s2210_evtcat_id
            
            if 'codParteAting' in dir(parteAtingida): s2210_parteatingida_dados['codparteating'] = parteAtingida.codParteAting.cdata
            if 'lateralidade' in dir(parteAtingida): s2210_parteatingida_dados['lateralidade'] = parteAtingida.lateralidade.cdata
            insert = create_insert('s2210_parteatingida', s2210_parteatingida_dados)
            resp = executar_sql(insert, True)
            s2210_parteatingida_id = resp[0][0]
            #print s2210_parteatingida_id

    if 'agenteCausador' in dir(evtCAT.cat):
        for agenteCausador in evtCAT.cat.agenteCausador:
            s2210_agentecausador_dados = {}
            s2210_agentecausador_dados['s2210_evtcat_id'] = s2210_evtcat_id
            
            if 'codAgntCausador' in dir(agenteCausador): s2210_agentecausador_dados['codagntcausador'] = agenteCausador.codAgntCausador.cdata
            insert = create_insert('s2210_agentecausador', s2210_agentecausador_dados)
            resp = executar_sql(insert, True)
            s2210_agentecausador_id = resp[0][0]
            #print s2210_agentecausador_id

    if 'atestado' in dir(evtCAT.cat):
        for atestado in evtCAT.cat.atestado:
            s2210_atestado_dados = {}
            s2210_atestado_dados['s2210_evtcat_id'] = s2210_evtcat_id
            
            if 'codCNES' in dir(atestado): s2210_atestado_dados['codcnes'] = atestado.codCNES.cdata
            if 'dtAtendimento' in dir(atestado): s2210_atestado_dados['dtatendimento'] = atestado.dtAtendimento.cdata
            if 'hrAtendimento' in dir(atestado): s2210_atestado_dados['hratendimento'] = atestado.hrAtendimento.cdata
            if 'indInternacao' in dir(atestado): s2210_atestado_dados['indinternacao'] = atestado.indInternacao.cdata
            if 'durTrat' in dir(atestado): s2210_atestado_dados['durtrat'] = atestado.durTrat.cdata
            if 'indAfast' in dir(atestado): s2210_atestado_dados['indafast'] = atestado.indAfast.cdata
            if 'dscLesao' in dir(atestado): s2210_atestado_dados['dsclesao'] = atestado.dscLesao.cdata
            if 'dscCompLesao' in dir(atestado): s2210_atestado_dados['dsccomplesao'] = atestado.dscCompLesao.cdata
            if 'diagProvavel' in dir(atestado): s2210_atestado_dados['diagprovavel'] = atestado.diagProvavel.cdata
            if 'codCID' in dir(atestado): s2210_atestado_dados['codcid'] = atestado.codCID.cdata
            if 'observacao' in dir(atestado): s2210_atestado_dados['observacao'] = atestado.observacao.cdata
            if 'nmEmit' in dir(atestado.emitente): s2210_atestado_dados['nmemit'] = atestado.emitente.nmEmit.cdata
            if 'ideOC' in dir(atestado.emitente): s2210_atestado_dados['ideoc'] = atestado.emitente.ideOC.cdata
            if 'nrOc' in dir(atestado.emitente): s2210_atestado_dados['nroc'] = atestado.emitente.nrOc.cdata
            if 'ufOC' in dir(atestado.emitente): s2210_atestado_dados['ufoc'] = atestado.emitente.ufOC.cdata
            insert = create_insert('s2210_atestado', s2210_atestado_dados)
            resp = executar_sql(insert, True)
            s2210_atestado_id = resp[0][0]
            #print s2210_atestado_id

    if 'catOrigem' in dir(evtCAT.cat):
        for catOrigem in evtCAT.cat.catOrigem:
            s2210_catorigem_dados = {}
            s2210_catorigem_dados['s2210_evtcat_id'] = s2210_evtcat_id
            
            if 'dtCatOrig' in dir(catOrigem): s2210_catorigem_dados['dtcatorig'] = catOrigem.dtCatOrig.cdata
            if 'nrCatOrig' in dir(catOrigem): s2210_catorigem_dados['nrcatorig'] = catOrigem.nrCatOrig.cdata
            insert = create_insert('s2210_catorigem', s2210_catorigem_dados)
            resp = executar_sql(insert, True)
            s2210_catorigem_id = resp[0][0]
            #print s2210_catorigem_id

    from emensageriapro.esocial.views.s2210_evtcat_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2210_evtcat_id, 'default')
    return dados