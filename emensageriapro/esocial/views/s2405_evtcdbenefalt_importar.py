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



def read_s2405_evtcdbenefalt_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2405_evtcdbenefalt_obj(doc, status, validar)
    return dados

def read_s2405_evtcdbenefalt(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2405_evtcdbenefalt_obj(doc, status, validar)
    return dados



def read_s2405_evtcdbenefalt_obj(doc, status, validar=False):
    s2405_evtcdbenefalt_dados = {}
    s2405_evtcdbenefalt_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2405_evtcdbenefalt_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2405_evtcdbenefalt_dados['identidade'] = doc.eSocial.evtCdBenefAlt['Id']
    evtCdBenefAlt = doc.eSocial.evtCdBenefAlt

    if 'indRetif' in dir(evtCdBenefAlt.ideEvento): s2405_evtcdbenefalt_dados['indretif'] = evtCdBenefAlt.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtCdBenefAlt.ideEvento): s2405_evtcdbenefalt_dados['nrrecibo'] = evtCdBenefAlt.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtCdBenefAlt.ideEvento): s2405_evtcdbenefalt_dados['tpamb'] = evtCdBenefAlt.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtCdBenefAlt.ideEvento): s2405_evtcdbenefalt_dados['procemi'] = evtCdBenefAlt.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtCdBenefAlt.ideEvento): s2405_evtcdbenefalt_dados['verproc'] = evtCdBenefAlt.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtCdBenefAlt.ideEmpregador): s2405_evtcdbenefalt_dados['tpinsc'] = evtCdBenefAlt.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtCdBenefAlt.ideEmpregador): s2405_evtcdbenefalt_dados['nrinsc'] = evtCdBenefAlt.ideEmpregador.nrInsc.cdata
    if 'cpfBenef' in dir(evtCdBenefAlt.ideBenef): s2405_evtcdbenefalt_dados['cpfbenef'] = evtCdBenefAlt.ideBenef.cpfBenef.cdata
    if 'dtAlteracao' in dir(evtCdBenefAlt.alteracao): s2405_evtcdbenefalt_dados['dtalteracao'] = evtCdBenefAlt.alteracao.dtAlteracao.cdata
    if 'nisBenef' in dir(evtCdBenefAlt.alteracao.dadosBenef): s2405_evtcdbenefalt_dados['nisbenef'] = evtCdBenefAlt.alteracao.dadosBenef.nisBenef.cdata
    if 'nmBenefic' in dir(evtCdBenefAlt.alteracao.dadosBenef): s2405_evtcdbenefalt_dados['nmbenefic'] = evtCdBenefAlt.alteracao.dadosBenef.nmBenefic.cdata
    if 'sexo' in dir(evtCdBenefAlt.alteracao.dadosBenef): s2405_evtcdbenefalt_dados['sexo'] = evtCdBenefAlt.alteracao.dadosBenef.sexo.cdata
    if 'racaCor' in dir(evtCdBenefAlt.alteracao.dadosBenef): s2405_evtcdbenefalt_dados['racacor'] = evtCdBenefAlt.alteracao.dadosBenef.racaCor.cdata
    if 'estCiv' in dir(evtCdBenefAlt.alteracao.dadosBenef): s2405_evtcdbenefalt_dados['estciv'] = evtCdBenefAlt.alteracao.dadosBenef.estCiv.cdata
    if 'incFisMen' in dir(evtCdBenefAlt.alteracao.dadosBenef): s2405_evtcdbenefalt_dados['incfismen'] = evtCdBenefAlt.alteracao.dadosBenef.incFisMen.cdata
    if 'dtIncFisMen' in dir(evtCdBenefAlt.alteracao.dadosBenef): s2405_evtcdbenefalt_dados['dtincfismen'] = evtCdBenefAlt.alteracao.dadosBenef.dtIncFisMen.cdata
    if 'paisNac' in dir(evtCdBenefAlt.alteracao.dadosBenef.dadosNasc): s2405_evtcdbenefalt_dados['paisnac'] = evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.paisNac.cdata
    if 'nmMae' in dir(evtCdBenefAlt.alteracao.dadosBenef.dadosNasc): s2405_evtcdbenefalt_dados['nmmae'] = evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmMae.cdata
    if 'nmPai' in dir(evtCdBenefAlt.alteracao.dadosBenef.dadosNasc): s2405_evtcdbenefalt_dados['nmpai'] = evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmPai.cdata
    if 'inclusao' in dir(evtCdBenefAlt.alteracao): s2405_evtcdbenefalt_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCdBenefAlt.alteracao): s2405_evtcdbenefalt_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCdBenefAlt.alteracao): s2405_evtcdbenefalt_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2405_evtcdbenefalt', s2405_evtcdbenefalt_dados)
    resp = executar_sql(insert, True)
    s2405_evtcdbenefalt_id = resp[0][0]
    dados = s2405_evtcdbenefalt_dados
    dados['evento'] = 's2405'
    dados['id'] = s2405_evtcdbenefalt_id
    dados['identidade_evento'] = doc.eSocial.evtCdBenefAlt['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'brasil' in dir(evtCdBenefAlt.alteracao.dadosBenef.endereco):
        for brasil in evtCdBenefAlt.alteracao.dadosBenef.endereco.brasil:
            s2405_brasil_dados = {}
            s2405_brasil_dados['s2405_evtcdbenefalt_id'] = s2405_evtcdbenefalt_id

            if 'tpLograd' in dir(brasil): s2405_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            if 'dscLograd' in dir(brasil): s2405_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            if 'nrLograd' in dir(brasil): s2405_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            if 'complemento' in dir(brasil): s2405_brasil_dados['complemento'] = brasil.complemento.cdata
            if 'bairro' in dir(brasil): s2405_brasil_dados['bairro'] = brasil.bairro.cdata
            if 'cep' in dir(brasil): s2405_brasil_dados['cep'] = brasil.cep.cdata
            if 'codMunic' in dir(brasil): s2405_brasil_dados['codmunic'] = brasil.codMunic.cdata
            if 'uf' in dir(brasil): s2405_brasil_dados['uf'] = brasil.uf.cdata
            insert = create_insert('s2405_brasil', s2405_brasil_dados)
            resp = executar_sql(insert, True)
            s2405_brasil_id = resp[0][0]
            #print s2405_brasil_id

    if 'exterior' in dir(evtCdBenefAlt.alteracao.dadosBenef.endereco):
        for exterior in evtCdBenefAlt.alteracao.dadosBenef.endereco.exterior:
            s2405_exterior_dados = {}
            s2405_exterior_dados['s2405_evtcdbenefalt_id'] = s2405_evtcdbenefalt_id

            if 'paisResid' in dir(exterior): s2405_exterior_dados['paisresid'] = exterior.paisResid.cdata
            if 'dscLograd' in dir(exterior): s2405_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            if 'nrLograd' in dir(exterior): s2405_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            if 'complemento' in dir(exterior): s2405_exterior_dados['complemento'] = exterior.complemento.cdata
            if 'bairro' in dir(exterior): s2405_exterior_dados['bairro'] = exterior.bairro.cdata
            if 'nmCid' in dir(exterior): s2405_exterior_dados['nmcid'] = exterior.nmCid.cdata
            if 'codPostal' in dir(exterior): s2405_exterior_dados['codpostal'] = exterior.codPostal.cdata
            insert = create_insert('s2405_exterior', s2405_exterior_dados)
            resp = executar_sql(insert, True)
            s2405_exterior_id = resp[0][0]
            #print s2405_exterior_id

    if 'dependente' in dir(evtCdBenefAlt.alteracao.dadosBenef):
        for dependente in evtCdBenefAlt.alteracao.dadosBenef.dependente:
            s2405_dependente_dados = {}
            s2405_dependente_dados['s2405_evtcdbenefalt_id'] = s2405_evtcdbenefalt_id

            if 'tpDep' in dir(dependente): s2405_dependente_dados['tpdep'] = dependente.tpDep.cdata
            if 'nmDep' in dir(dependente): s2405_dependente_dados['nmdep'] = dependente.nmDep.cdata
            if 'dtNascto' in dir(dependente): s2405_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            if 'cpfDep' in dir(dependente): s2405_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            if 'sexoDep' in dir(dependente): s2405_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            if 'depIRRF' in dir(dependente): s2405_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            if 'incFisMen' in dir(dependente): s2405_dependente_dados['incfismen'] = dependente.incFisMen.cdata
            if 'depFinsPrev' in dir(dependente): s2405_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            insert = create_insert('s2405_dependente', s2405_dependente_dados)
            resp = executar_sql(insert, True)
            s2405_dependente_id = resp[0][0]
            #print s2405_dependente_id

    from emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2405_evtcdbenefalt_id, 'default')
    return dados