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



def read_s2400_evtcdbenefin_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2400_evtcdbenefin_obj(doc, status, validar)
    return dados

def read_s2400_evtcdbenefin(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2400_evtcdbenefin_obj(doc, status, validar)
    return dados



def read_s2400_evtcdbenefin_obj(doc, status, validar=False):
    s2400_evtcdbenefin_dados = {}
    s2400_evtcdbenefin_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2400_evtcdbenefin_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2400_evtcdbenefin_dados['identidade'] = doc.eSocial.evtCdBenefIn['Id']
    evtCdBenefIn = doc.eSocial.evtCdBenefIn

    try: s2400_evtcdbenefin_dados['indretif'] = evtCdBenefIn.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['nrrecibo'] = evtCdBenefIn.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['tpamb'] = evtCdBenefIn.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['procemi'] = evtCdBenefIn.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['verproc'] = evtCdBenefIn.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['tpinsc'] = evtCdBenefIn.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['nrinsc'] = evtCdBenefIn.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['cpfbenef'] = evtCdBenefIn.beneficiario.cpfBenef.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['nisbenef'] = evtCdBenefIn.beneficiario.nisBenef.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['nmbenefic'] = evtCdBenefIn.beneficiario.nmBenefic.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['dtinicio'] = evtCdBenefIn.beneficiario.dtInicio.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['sexo'] = evtCdBenefIn.beneficiario.sexo.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['racacor'] = evtCdBenefIn.beneficiario.racaCor.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['estciv'] = evtCdBenefIn.beneficiario.estCiv.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['incfismen'] = evtCdBenefIn.beneficiario.incFisMen.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['dtincfismen'] = evtCdBenefIn.beneficiario.dtIncFisMen.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['dtnascto'] = evtCdBenefIn.beneficiario.dadosNasc.dtNascto.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['codmunic'] = evtCdBenefIn.beneficiario.dadosNasc.codMunic.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['uf'] = evtCdBenefIn.beneficiario.dadosNasc.uf.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['paisnascto'] = evtCdBenefIn.beneficiario.dadosNasc.paisNascto.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['paisnac'] = evtCdBenefIn.beneficiario.dadosNasc.paisNac.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['nmmae'] = evtCdBenefIn.beneficiario.dadosNasc.nmMae.cdata
    except AttributeError: pass
    try: s2400_evtcdbenefin_dados['nmpai'] = evtCdBenefIn.beneficiario.dadosNasc.nmPai.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['operacao'] = 1
    elif 'alteracao' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['operacao'] = 2
    elif 'exclusao' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2400_evtcdbenefin', s2400_evtcdbenefin_dados)
    resp = executar_sql(insert, True)
    s2400_evtcdbenefin_id = resp[0][0]
    dados = s2400_evtcdbenefin_dados
    dados['evento'] = 's2400'
    dados['id'] = s2400_evtcdbenefin_id
    dados['identidade_evento'] = doc.eSocial.evtCdBenefIn['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'brasil' in dir(evtCdBenefIn.beneficiario.endereco) and evtCdBenefIn.beneficiario.endereco.brasil.cdata != '':
        for brasil in evtCdBenefIn.beneficiario.endereco.brasil:
            s2400_brasil_dados = {}
            s2400_brasil_dados['s2400_evtcdbenefin_id'] = s2400_evtcdbenefin_id

            try: s2400_brasil_dados['tplograd'] = brasil.tpLograd.cdata
            except AttributeError: pass
            try: s2400_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
            except AttributeError: pass
            try: s2400_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
            except AttributeError: pass
            try: s2400_brasil_dados['complemento'] = brasil.complemento.cdata
            except AttributeError: pass
            try: s2400_brasil_dados['bairro'] = brasil.bairro.cdata
            except AttributeError: pass
            try: s2400_brasil_dados['cep'] = brasil.cep.cdata
            except AttributeError: pass
            try: s2400_brasil_dados['codmunic'] = brasil.codMunic.cdata
            except AttributeError: pass
            try: s2400_brasil_dados['uf'] = brasil.uf.cdata
            except AttributeError: pass
            insert = create_insert('s2400_brasil', s2400_brasil_dados)
            resp = executar_sql(insert, True)
            s2400_brasil_id = resp[0][0]
            #print s2400_brasil_id

    if 'exterior' in dir(evtCdBenefIn.beneficiario.endereco) and evtCdBenefIn.beneficiario.endereco.exterior.cdata != '':
        for exterior in evtCdBenefIn.beneficiario.endereco.exterior:
            s2400_exterior_dados = {}
            s2400_exterior_dados['s2400_evtcdbenefin_id'] = s2400_evtcdbenefin_id

            try: s2400_exterior_dados['paisresid'] = exterior.paisResid.cdata
            except AttributeError: pass
            try: s2400_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
            except AttributeError: pass
            try: s2400_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
            except AttributeError: pass
            try: s2400_exterior_dados['complemento'] = exterior.complemento.cdata
            except AttributeError: pass
            try: s2400_exterior_dados['bairro'] = exterior.bairro.cdata
            except AttributeError: pass
            try: s2400_exterior_dados['nmcid'] = exterior.nmCid.cdata
            except AttributeError: pass
            try: s2400_exterior_dados['codpostal'] = exterior.codPostal.cdata
            except AttributeError: pass
            insert = create_insert('s2400_exterior', s2400_exterior_dados)
            resp = executar_sql(insert, True)
            s2400_exterior_id = resp[0][0]
            #print s2400_exterior_id

    if 'dependente' in dir(evtCdBenefIn.beneficiario) and evtCdBenefIn.beneficiario.dependente.cdata != '':
        for dependente in evtCdBenefIn.beneficiario.dependente:
            s2400_dependente_dados = {}
            s2400_dependente_dados['s2400_evtcdbenefin_id'] = s2400_evtcdbenefin_id

            try: s2400_dependente_dados['tpdep'] = dependente.tpDep.cdata
            except AttributeError: pass
            try: s2400_dependente_dados['nmdep'] = dependente.nmDep.cdata
            except AttributeError: pass
            try: s2400_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            except AttributeError: pass
            try: s2400_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            except AttributeError: pass
            try: s2400_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            except AttributeError: pass
            try: s2400_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            except AttributeError: pass
            try: s2400_dependente_dados['incfismen'] = dependente.incFisMen.cdata
            except AttributeError: pass
            try: s2400_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            except AttributeError: pass
            insert = create_insert('s2400_dependente', s2400_dependente_dados)
            resp = executar_sql(insert, True)
            s2400_dependente_id = resp[0][0]
            #print s2400_dependente_id

    from emensageriapro.esocial.views.s2400_evtcdbenefin_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2400_evtcdbenefin_id, 'default')
    return dados