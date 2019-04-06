#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def read_s2210_evtcat_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2210_evtcat_obj(doc, status, validar)
    return dados

def read_s2210_evtcat(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2210_evtcat_obj(doc, status, validar)
    return dados



def read_s2210_evtcat_obj(doc, status, validar=False):
    s2210_evtcat_dados = {}
    s2210_evtcat_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2210_evtcat_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2210_evtcat_dados['identidade'] = doc.eSocial.evtCAT['Id']
    evtCAT = doc.eSocial.evtCAT

    try: s2210_evtcat_dados['indretif'] = evtCAT.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['nrrecibo'] = evtCAT.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['tpamb'] = evtCAT.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['procemi'] = evtCAT.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['verproc'] = evtCAT.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['tpinsc'] = evtCAT.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['nrinsc'] = evtCAT.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['cpftrab'] = evtCAT.ideVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['nistrab'] = evtCAT.ideVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['matricula'] = evtCAT.ideVinculo.matricula.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['codcateg'] = evtCAT.ideVinculo.codCateg.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['dtacid'] = evtCAT.cat.dtAcid.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['tpacid'] = evtCAT.cat.tpAcid.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['hracid'] = evtCAT.cat.hrAcid.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['hrstrabantesacid'] = evtCAT.cat.hrsTrabAntesAcid.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['tpcat'] = evtCAT.cat.tpCat.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['indcatobito'] = evtCAT.cat.indCatObito.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['dtobito'] = evtCAT.cat.dtObito.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['indcomunpolicia'] = evtCAT.cat.indComunPolicia.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['codsitgeradora'] = evtCAT.cat.codSitGeradora.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['iniciatcat'] = evtCAT.cat.iniciatCAT.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['obscat'] = evtCAT.cat.obsCAT.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['observacao'] = evtCAT.cat.observacao.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['tplocal'] = evtCAT.cat.localAcidente.tpLocal.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['dsclocal'] = evtCAT.cat.localAcidente.dscLocal.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['codamb'] = evtCAT.cat.localAcidente.codAmb.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['tplograd'] = evtCAT.cat.localAcidente.tpLograd.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['dsclograd'] = evtCAT.cat.localAcidente.dscLograd.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['nrlograd'] = evtCAT.cat.localAcidente.nrLograd.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['complemento'] = evtCAT.cat.localAcidente.complemento.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['bairro'] = evtCAT.cat.localAcidente.bairro.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['cep'] = evtCAT.cat.localAcidente.cep.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['codmunic'] = evtCAT.cat.localAcidente.codMunic.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['uf'] = evtCAT.cat.localAcidente.uf.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['pais'] = evtCAT.cat.localAcidente.pais.cdata
    except AttributeError: pass
    try: s2210_evtcat_dados['codpostal'] = evtCAT.cat.localAcidente.codPostal.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtCAT.cat): s2210_evtcat_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCAT.cat): s2210_evtcat_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCAT.cat): s2210_evtcat_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2210_evtcat', s2210_evtcat_dados)
    resp = executar_sql(insert, True)
    s2210_evtcat_id = resp[0][0]
    dados = s2210_evtcat_dados
    dados['evento'] = 's2210'
    dados['id'] = s2210_evtcat_id
    dados['identidade_evento'] = doc.eSocial.evtCAT['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'ideLocalAcid' in dir(evtCAT.cat.localAcidente) and evtCAT.cat.localAcidente.ideLocalAcid.cdata != '':
        for ideLocalAcid in evtCAT.cat.localAcidente.ideLocalAcid:
            s2210_idelocalacid_dados = {}
            s2210_idelocalacid_dados['s2210_evtcat_id'] = s2210_evtcat_id

            try: s2210_idelocalacid_dados['tpinsc'] = ideLocalAcid.tpInsc.cdata
            except AttributeError: pass
            try: s2210_idelocalacid_dados['nrinsc'] = ideLocalAcid.nrInsc.cdata
            except AttributeError: pass
            insert = create_insert('s2210_idelocalacid', s2210_idelocalacid_dados)
            resp = executar_sql(insert, True)
            s2210_idelocalacid_id = resp[0][0]
            #print s2210_idelocalacid_id

    if 'parteAtingida' in dir(evtCAT.cat) and evtCAT.cat.parteAtingida.cdata != '':
        for parteAtingida in evtCAT.cat.parteAtingida:
            s2210_parteatingida_dados = {}
            s2210_parteatingida_dados['s2210_evtcat_id'] = s2210_evtcat_id

            try: s2210_parteatingida_dados['codparteating'] = parteAtingida.codParteAting.cdata
            except AttributeError: pass
            try: s2210_parteatingida_dados['lateralidade'] = parteAtingida.lateralidade.cdata
            except AttributeError: pass
            insert = create_insert('s2210_parteatingida', s2210_parteatingida_dados)
            resp = executar_sql(insert, True)
            s2210_parteatingida_id = resp[0][0]
            #print s2210_parteatingida_id

    if 'agenteCausador' in dir(evtCAT.cat) and evtCAT.cat.agenteCausador.cdata != '':
        for agenteCausador in evtCAT.cat.agenteCausador:
            s2210_agentecausador_dados = {}
            s2210_agentecausador_dados['s2210_evtcat_id'] = s2210_evtcat_id

            try: s2210_agentecausador_dados['codagntcausador'] = agenteCausador.codAgntCausador.cdata
            except AttributeError: pass
            insert = create_insert('s2210_agentecausador', s2210_agentecausador_dados)
            resp = executar_sql(insert, True)
            s2210_agentecausador_id = resp[0][0]
            #print s2210_agentecausador_id

    if 'atestado' in dir(evtCAT.cat) and evtCAT.cat.atestado.cdata != '':
        for atestado in evtCAT.cat.atestado:
            s2210_atestado_dados = {}
            s2210_atestado_dados['s2210_evtcat_id'] = s2210_evtcat_id

            try: s2210_atestado_dados['codcnes'] = atestado.codCNES.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['dtatendimento'] = atestado.dtAtendimento.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['hratendimento'] = atestado.hrAtendimento.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['indinternacao'] = atestado.indInternacao.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['durtrat'] = atestado.durTrat.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['indafast'] = atestado.indAfast.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['dsclesao'] = atestado.dscLesao.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['dsccomplesao'] = atestado.dscCompLesao.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['diagprovavel'] = atestado.diagProvavel.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['codcid'] = atestado.codCID.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['observacao'] = atestado.observacao.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['nmemit'] = atestado.emitente.nmEmit.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['ideoc'] = atestado.emitente.ideOC.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['nroc'] = atestado.emitente.nrOC.cdata
            except AttributeError: pass
            try: s2210_atestado_dados['ufoc'] = atestado.emitente.ufOC.cdata
            except AttributeError: pass
            insert = create_insert('s2210_atestado', s2210_atestado_dados)
            resp = executar_sql(insert, True)
            s2210_atestado_id = resp[0][0]
            #print s2210_atestado_id

    if 'catOrigem' in dir(evtCAT.cat) and evtCAT.cat.catOrigem.cdata != '':
        for catOrigem in evtCAT.cat.catOrigem:
            s2210_catorigem_dados = {}
            s2210_catorigem_dados['s2210_evtcat_id'] = s2210_evtcat_id

            try: s2210_catorigem_dados['dtcatorig'] = catOrigem.dtCatOrig.cdata
            except AttributeError: pass
            try: s2210_catorigem_dados['nrreccatorig'] = catOrigem.nrRecCatOrig.cdata
            except AttributeError: pass
            insert = create_insert('s2210_catorigem', s2210_catorigem_dados)
            resp = executar_sql(insert, True)
            s2210_catorigem_id = resp[0][0]
            #print s2210_catorigem_id

    from emensageriapro.esocial.views.s2210_evtcat_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2210_evtcat_id, 'default')
    return dados