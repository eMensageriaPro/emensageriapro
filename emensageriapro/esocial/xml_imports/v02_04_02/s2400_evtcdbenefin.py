#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
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


def read_s2400_evtcdbenefin(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s2400_evtcdbenefin_obj(doc, status)



def read_s2400_evtcdbenefin_obj(doc):
    s2400_evtcdbenefin_dados = {}
    s2400_evtcdbenefin_dados['versao'] = 'v02_04_02'
    s2400_evtcdbenefin_dados['status'] = status
    s2400_evtcdbenefin_dados['identidade'] = doc.eSocial.evtCdBenefIn['Id']
    s2400_evtcdbenefin_dados['processamento_codigo_resposta'] = 1
    evtCdBenefIn = doc.eSocial.evtCdBenefIn
    
    if 'indRetif' in dir(evtCdBenefIn.ideEvento): s2400_evtcdbenefin_dados['indretif'] = evtCdBenefIn.ideEvento.indRetif.cdata
    if 'nrRecibo' in dir(evtCdBenefIn.ideEvento): s2400_evtcdbenefin_dados['nrrecibo'] = evtCdBenefIn.ideEvento.nrRecibo.cdata
    if 'tpAmb' in dir(evtCdBenefIn.ideEvento): s2400_evtcdbenefin_dados['tpamb'] = evtCdBenefIn.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtCdBenefIn.ideEvento): s2400_evtcdbenefin_dados['procemi'] = evtCdBenefIn.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtCdBenefIn.ideEvento): s2400_evtcdbenefin_dados['verproc'] = evtCdBenefIn.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtCdBenefIn.ideEmpregador): s2400_evtcdbenefin_dados['tpinsc'] = evtCdBenefIn.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtCdBenefIn.ideEmpregador): s2400_evtcdbenefin_dados['nrinsc'] = evtCdBenefIn.ideEmpregador.nrInsc.cdata
    if 'cpfBenef' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['cpfbenef'] = evtCdBenefIn.beneficiario.cpfBenef.cdata
    if 'nisBenef' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['nisbenef'] = evtCdBenefIn.beneficiario.nisBenef.cdata
    if 'nmBenefic' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['nmbenefic'] = evtCdBenefIn.beneficiario.nmBenefic.cdata
    if 'dtInicio' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['dtinicio'] = evtCdBenefIn.beneficiario.dtInicio.cdata
    if 'sexo' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['sexo'] = evtCdBenefIn.beneficiario.sexo.cdata
    if 'racaCor' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['racacor'] = evtCdBenefIn.beneficiario.racaCor.cdata
    if 'estCiv' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['estciv'] = evtCdBenefIn.beneficiario.estCiv.cdata
    if 'incFisMen' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['incfismen'] = evtCdBenefIn.beneficiario.incFisMen.cdata
    if 'dtIncFisMen' in dir(evtCdBenefIn.beneficiario): s2400_evtcdbenefin_dados['dtincfismen'] = evtCdBenefIn.beneficiario.dtIncFisMen.cdata
    if 'dtNascto' in dir(evtCdBenefIn.beneficiario.dadosNasc): s2400_evtcdbenefin_dados['dtnascto'] = evtCdBenefIn.beneficiario.dadosNasc.dtNascto.cdata
    if 'codMunic' in dir(evtCdBenefIn.beneficiario.dadosNasc): s2400_evtcdbenefin_dados['codmunic'] = evtCdBenefIn.beneficiario.dadosNasc.codMunic.cdata
    if 'uf' in dir(evtCdBenefIn.beneficiario.dadosNasc): s2400_evtcdbenefin_dados['uf'] = evtCdBenefIn.beneficiario.dadosNasc.uf.cdata
    if 'paisNascto' in dir(evtCdBenefIn.beneficiario.dadosNasc): s2400_evtcdbenefin_dados['paisnascto'] = evtCdBenefIn.beneficiario.dadosNasc.paisNascto.cdata
    if 'paisNac' in dir(evtCdBenefIn.beneficiario.dadosNasc): s2400_evtcdbenefin_dados['paisnac'] = evtCdBenefIn.beneficiario.dadosNasc.paisNac.cdata
    if 'nmMae' in dir(evtCdBenefIn.beneficiario.dadosNasc): s2400_evtcdbenefin_dados['nmmae'] = evtCdBenefIn.beneficiario.dadosNasc.nmMae.cdata
    if 'nmPai' in dir(evtCdBenefIn.beneficiario.dadosNasc): s2400_evtcdbenefin_dados['nmpai'] = evtCdBenefIn.beneficiario.dadosNasc.nmPai.cdata
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
    dados['status'] = 1

    if 'endereco' in dir(evtCdBenefIn.beneficiario):
        for endereco in evtCdBenefIn.beneficiario.endereco:
            s2400_endereco_dados = {}
            s2400_endereco_dados['s2400_evtcdbenefin_id'] = s2400_evtcdbenefin_id
            
            insert = create_insert('s2400_endereco', s2400_endereco_dados)
            resp = executar_sql(insert, True)
            s2400_endereco_id = resp[0][0]
            #print s2400_endereco_id

            if 'brasil' in dir(endereco):
                for brasil in endereco.brasil:
                    s2400_brasil_dados = {}
                    s2400_brasil_dados['s2400_endereco_id'] = s2400_endereco_id
                    
                    if 'tpLograd' in dir(brasil): s2400_brasil_dados['tplograd'] = brasil.tpLograd.cdata
                    if 'dscLograd' in dir(brasil): s2400_brasil_dados['dsclograd'] = brasil.dscLograd.cdata
                    if 'nrLograd' in dir(brasil): s2400_brasil_dados['nrlograd'] = brasil.nrLograd.cdata
                    if 'complemento' in dir(brasil): s2400_brasil_dados['complemento'] = brasil.complemento.cdata
                    if 'bairro' in dir(brasil): s2400_brasil_dados['bairro'] = brasil.bairro.cdata
                    if 'cep' in dir(brasil): s2400_brasil_dados['cep'] = brasil.cep.cdata
                    if 'codMunic' in dir(brasil): s2400_brasil_dados['codmunic'] = brasil.codMunic.cdata
                    if 'uf' in dir(brasil): s2400_brasil_dados['uf'] = brasil.uf.cdata
                    insert = create_insert('s2400_brasil', s2400_brasil_dados)
                    resp = executar_sql(insert, True)
                    s2400_brasil_id = resp[0][0]
                    #print s2400_brasil_id
        
            if 'exterior' in dir(endereco):
                for exterior in endereco.exterior:
                    s2400_exterior_dados = {}
                    s2400_exterior_dados['s2400_endereco_id'] = s2400_endereco_id
                    
                    if 'paisResid' in dir(exterior): s2400_exterior_dados['paisresid'] = exterior.paisResid.cdata
                    if 'dscLograd' in dir(exterior): s2400_exterior_dados['dsclograd'] = exterior.dscLograd.cdata
                    if 'nrLograd' in dir(exterior): s2400_exterior_dados['nrlograd'] = exterior.nrLograd.cdata
                    if 'complemento' in dir(exterior): s2400_exterior_dados['complemento'] = exterior.complemento.cdata
                    if 'bairro' in dir(exterior): s2400_exterior_dados['bairro'] = exterior.bairro.cdata
                    if 'nmCid' in dir(exterior): s2400_exterior_dados['nmcid'] = exterior.nmCid.cdata
                    if 'codPostal' in dir(exterior): s2400_exterior_dados['codpostal'] = exterior.codPostal.cdata
                    insert = create_insert('s2400_exterior', s2400_exterior_dados)
                    resp = executar_sql(insert, True)
                    s2400_exterior_id = resp[0][0]
                    #print s2400_exterior_id
        
    if 'dependente' in dir(evtCdBenefIn.beneficiario):
        for dependente in evtCdBenefIn.beneficiario.dependente:
            s2400_dependente_dados = {}
            s2400_dependente_dados['s2400_evtcdbenefin_id'] = s2400_evtcdbenefin_id
            
            if 'tpDep' in dir(dependente): s2400_dependente_dados['tpdep'] = dependente.tpDep.cdata
            if 'nmDep' in dir(dependente): s2400_dependente_dados['nmdep'] = dependente.nmDep.cdata
            if 'dtNascto' in dir(dependente): s2400_dependente_dados['dtnascto'] = dependente.dtNascto.cdata
            if 'cpfDep' in dir(dependente): s2400_dependente_dados['cpfdep'] = dependente.cpfDep.cdata
            if 'sexoDep' in dir(dependente): s2400_dependente_dados['sexodep'] = dependente.sexoDep.cdata
            if 'depIRRF' in dir(dependente): s2400_dependente_dados['depirrf'] = dependente.depIRRF.cdata
            if 'incFisMen' in dir(dependente): s2400_dependente_dados['incfismen'] = dependente.incFisMen.cdata
            if 'depFinsPrev' in dir(dependente): s2400_dependente_dados['depfinsprev'] = dependente.depFinsPrev.cdata
            insert = create_insert('s2400_dependente', s2400_dependente_dados)
            resp = executar_sql(insert, True)
            s2400_dependente_id = resp[0][0]
            #print s2400_dependente_id

    from emensageriapro.esocial.views.s2400_evtcdbenefin_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2400_evtcdbenefin_id, 'default')
    return dados