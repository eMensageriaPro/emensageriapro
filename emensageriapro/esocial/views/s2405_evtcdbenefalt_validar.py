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
from emensageriapro.padrao import ler_arquivo


def validacoes_s2405_evtcdbenefalt(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenefAlt = doc.eSocial.evtCdBenefAlt

    if 'indRetif' in dir(evtCdBenefAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.ideEvento.indRetif', evtCdBenefAlt.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtCdBenefAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.ideEvento.nrRecibo', evtCdBenefAlt.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtCdBenefAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.ideEvento.tpAmb', evtCdBenefAlt.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtCdBenefAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.ideEvento.procEmi', evtCdBenefAlt.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtCdBenefAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.ideEvento.verProc', evtCdBenefAlt.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtCdBenefAlt.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.ideEmpregador.tpInsc', evtCdBenefAlt.ideEmpregador.tpInsc.cdata, 1, '1')
    if 'nrInsc' in dir(evtCdBenefAlt.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.ideEmpregador.nrInsc', evtCdBenefAlt.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfBenef' in dir(evtCdBenefAlt.ideBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.ideBenef.cpfBenef', evtCdBenefAlt.ideBenef.cpfBenef.cdata, 1, '')
    if 'dtAlteracao' in dir(evtCdBenefAlt.alteracao): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dtAlteracao', evtCdBenefAlt.alteracao.dtAlteracao.cdata, 1, '')
    if 'nisBenef' in dir(evtCdBenefAlt.alteracao.dadosBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.nisBenef', evtCdBenefAlt.alteracao.dadosBenef.nisBenef.cdata, 0, '')
    if 'nmBenefic' in dir(evtCdBenefAlt.alteracao.dadosBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.nmBenefic', evtCdBenefAlt.alteracao.dadosBenef.nmBenefic.cdata, 1, '')
    if 'sexo' in dir(evtCdBenefAlt.alteracao.dadosBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.sexo', evtCdBenefAlt.alteracao.dadosBenef.sexo.cdata, 1, 'M;F')
    if 'racaCor' in dir(evtCdBenefAlt.alteracao.dadosBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.racaCor', evtCdBenefAlt.alteracao.dadosBenef.racaCor.cdata, 1, '1;2;3;4;5;6')
    if 'estCiv' in dir(evtCdBenefAlt.alteracao.dadosBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.estCiv', evtCdBenefAlt.alteracao.dadosBenef.estCiv.cdata, 0, '1;2;3;4;5')
    if 'incFisMen' in dir(evtCdBenefAlt.alteracao.dadosBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.incFisMen', evtCdBenefAlt.alteracao.dadosBenef.incFisMen.cdata, 1, 'S;N')
    if 'dtIncFisMen' in dir(evtCdBenefAlt.alteracao.dadosBenef): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.dtIncFisMen', evtCdBenefAlt.alteracao.dadosBenef.dtIncFisMen.cdata, 0, '')
    if 'paisNac' in dir(evtCdBenefAlt.alteracao.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.paisNac', evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.paisNac.cdata, 1, '')
    if 'nmMae' in dir(evtCdBenefAlt.alteracao.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmMae', evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmMae.cdata, 0, '')
    if 'nmPai' in dir(evtCdBenefAlt.alteracao.dadosBenef.dadosNasc): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmPai', evtCdBenefAlt.alteracao.dadosBenef.dadosNasc.nmPai.cdata, 0, '')
    if 'endereco' in dir(evtCdBenefAlt.alteracao.dadosBenef):
        for endereco in evtCdBenefAlt.alteracao.dadosBenef.endereco:
       

            if 'brasil' in dir(endereco):
                for brasil in endereco.brasil:
               
                    if 'tpLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.tpLograd', brasil.tpLograd.cdata, 1, '')
                    if 'dscLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.dscLograd', brasil.dscLograd.cdata, 1, '')
                    if 'nrLograd' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.nrLograd', brasil.nrLograd.cdata, 1, '')
                    if 'complemento' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.complemento', brasil.complemento.cdata, 0, '')
                    if 'bairro' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.bairro', brasil.bairro.cdata, 0, '')
                    if 'cep' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.cep', brasil.cep.cdata, 1, '')
                    if 'codMunic' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.codMunic', brasil.codMunic.cdata, 1, '')
                    if 'uf' in dir(brasil): validacoes_lista = validar_campo(validacoes_lista,'brasil.uf', brasil.uf.cdata, 1, '')
   
            if 'exterior' in dir(endereco):
                for exterior in endereco.exterior:
               
                    if 'paisResid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.paisResid', exterior.paisResid.cdata, 1, '')
                    if 'dscLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.dscLograd', exterior.dscLograd.cdata, 1, '')
                    if 'nrLograd' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nrLograd', exterior.nrLograd.cdata, 1, '')
                    if 'complemento' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.complemento', exterior.complemento.cdata, 0, '')
                    if 'bairro' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.bairro', exterior.bairro.cdata, 0, '')
                    if 'nmCid' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.nmCid', exterior.nmCid.cdata, 1, '')
                    if 'codPostal' in dir(exterior): validacoes_lista = validar_campo(validacoes_lista,'exterior.codPostal', exterior.codPostal.cdata, 0, '')
   
    if 'dependente' in dir(evtCdBenefAlt.alteracao.dadosBenef):
        for dependente in evtCdBenefAlt.alteracao.dadosBenef.dependente:
       
            if 'tpDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.tpDep', dependente.tpDep.cdata, 1, '')
            if 'nmDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.nmDep', dependente.nmDep.cdata, 1, '')
            if 'dtNascto' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.dtNascto', dependente.dtNascto.cdata, 1, '')
            if 'cpfDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.cpfDep', dependente.cpfDep.cdata, 0, '')
            if 'sexoDep' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.sexoDep', dependente.sexoDep.cdata, 1, 'M;F')
            if 'depIRRF' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depIRRF', dependente.depIRRF.cdata, 1, 'S;N')
            if 'incFisMen' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.incFisMen', dependente.incFisMen.cdata, 1, 'S;N')
            if 'depFinsPrev' in dir(dependente): validacoes_lista = validar_campo(validacoes_lista,'dependente.depFinsPrev', dependente.depFinsPrev.cdata, 1, 'S;N')

    return validacoes_lista