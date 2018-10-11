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


def validacoes_s2416_evtcdbenalt(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenAlt = doc.eSocial.evtCdBenAlt
    
    if 'indRetif' in dir(evtCdBenAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.ideEvento.indRetif', evtCdBenAlt.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtCdBenAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.ideEvento.nrRecibo', evtCdBenAlt.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtCdBenAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.ideEvento.tpAmb', evtCdBenAlt.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtCdBenAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.ideEvento.procEmi', evtCdBenAlt.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtCdBenAlt.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.ideEvento.verProc', evtCdBenAlt.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtCdBenAlt.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.ideEmpregador.tpInsc', evtCdBenAlt.ideEmpregador.tpInsc.cdata, 1, '1')
    if 'nrInsc' in dir(evtCdBenAlt.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.ideEmpregador.nrInsc', evtCdBenAlt.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfBenef' in dir(evtCdBenAlt.ideBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.ideBeneficio.cpfBenef', evtCdBenAlt.ideBeneficio.cpfBenef.cdata, 1, '')
    if 'nrBeneficio' in dir(evtCdBenAlt.ideBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.ideBeneficio.nrBeneficio', evtCdBenAlt.ideBeneficio.nrBeneficio.cdata, 1, '')
    if 'dtAltBeneficio' in dir(evtCdBenAlt.infoBenAlteracao): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.infoBenAlteracao.dtAltBeneficio', evtCdBenAlt.infoBenAlteracao.dtAltBeneficio.cdata, 1, '')
    if 'tpBeneficio' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpBeneficio', evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpBeneficio.cdata, 1, '')
    if 'tpPlanRP' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpPlanRP', evtCdBenAlt.infoBenAlteracao.dadosBeneficio.tpPlanRP.cdata, 1, '0;1;2;3')
    if 'dsc' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.infoBenAlteracao.dadosBeneficio.dsc', evtCdBenAlt.infoBenAlteracao.dadosBeneficio.dsc.cdata, 0, '')
    if 'indDecJud' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indDecJud', evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indDecJud.cdata, 1, 'S;N')
    if 'indHomologTC' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indHomologTC', evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indHomologTC.cdata, 1, 'S;N')
    if 'indSuspensao' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indSuspensao', evtCdBenAlt.infoBenAlteracao.dadosBeneficio.indSuspensao.cdata, 1, 'S;N')
    if 'infoPenMorte' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):
        for infoPenMorte in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.infoPenMorte:
            
            if 'tpPenMorte' in dir(infoPenMorte): validacoes_lista = validar_campo(validacoes_lista,'infoPenMorte.tpPenMorte', infoPenMorte.tpPenMorte.cdata, 1, '1;2')

    if 'homologTC' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):
        for homologTC in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.homologTC:
            
            if 'nrAtoLegal' in dir(homologTC): validacoes_lista = validar_campo(validacoes_lista,'homologTC.nrAtoLegal', homologTC.nrAtoLegal.cdata, 1, '')

    if 'suspensao' in dir(evtCdBenAlt.infoBenAlteracao.dadosBeneficio):
        for suspensao in evtCdBenAlt.infoBenAlteracao.dadosBeneficio.suspensao:
            
            if 'mtvSuspensao' in dir(suspensao): validacoes_lista = validar_campo(validacoes_lista,'suspensao.mtvSuspensao', suspensao.mtvSuspensao.cdata, 1, '01;99')
            if 'dscSuspensao' in dir(suspensao): validacoes_lista = validar_campo(validacoes_lista,'suspensao.dscSuspensao', suspensao.dscSuspensao.cdata, 0, '')

    return validacoes_lista