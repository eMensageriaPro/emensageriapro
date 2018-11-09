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


def validacoes_s2410_evtcdbenin(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenIn = doc.eSocial.evtCdBenIn

    if 'indRetif' in dir(evtCdBenIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.ideEvento.indRetif', evtCdBenIn.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtCdBenIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.ideEvento.nrRecibo', evtCdBenIn.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtCdBenIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.ideEvento.tpAmb', evtCdBenIn.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtCdBenIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.ideEvento.procEmi', evtCdBenIn.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtCdBenIn.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.ideEvento.verProc', evtCdBenIn.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtCdBenIn.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.ideEmpregador.tpInsc', evtCdBenIn.ideEmpregador.tpInsc.cdata, 1, '1')
    if 'nrInsc' in dir(evtCdBenIn.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.ideEmpregador.nrInsc', evtCdBenIn.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfBenef' in dir(evtCdBenIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.beneficiario.cpfBenef', evtCdBenIn.beneficiario.cpfBenef.cdata, 1, '')
    if 'matricula' in dir(evtCdBenIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.beneficiario.matricula', evtCdBenIn.beneficiario.matricula.cdata, 0, '')
    if 'cnpjOrigem' in dir(evtCdBenIn.beneficiario): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.beneficiario.cnpjOrigem', evtCdBenIn.beneficiario.cnpjOrigem.cdata, 0, '')
    if 'cadIni' in dir(evtCdBenIn.infoBenInicio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.infoBenInicio.cadIni', evtCdBenIn.infoBenInicio.cadIni.cdata, 1, 'S;N')
    if 'nrBeneficio' in dir(evtCdBenIn.infoBenInicio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.infoBenInicio.nrBeneficio', evtCdBenIn.infoBenInicio.nrBeneficio.cdata, 1, '')
    if 'dtIniBeneficio' in dir(evtCdBenIn.infoBenInicio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.infoBenInicio.dtIniBeneficio', evtCdBenIn.infoBenInicio.dtIniBeneficio.cdata, 1, '')
    if 'tpBeneficio' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.infoBenInicio.dadosBeneficio.tpBeneficio', evtCdBenIn.infoBenInicio.dadosBeneficio.tpBeneficio.cdata, 1, '')
    if 'vrBeneficio' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.infoBenInicio.dadosBeneficio.vrBeneficio', evtCdBenIn.infoBenInicio.dadosBeneficio.vrBeneficio.cdata, 1, '')
    if 'tpPlanRP' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.infoBenInicio.dadosBeneficio.tpPlanRP', evtCdBenIn.infoBenInicio.dadosBeneficio.tpPlanRP.cdata, 1, '0;1;2;3')
    if 'dsc' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.infoBenInicio.dadosBeneficio.dsc', evtCdBenIn.infoBenInicio.dadosBeneficio.dsc.cdata, 0, '')
    if 'indDecJud' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.infoBenInicio.dadosBeneficio.indDecJud', evtCdBenIn.infoBenInicio.dadosBeneficio.indDecJud.cdata, 1, 'S;N')
    if 'indHomologTC' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio): validacoes_lista = validar_campo(validacoes_lista,'evtCdBenIn.infoBenInicio.dadosBeneficio.indHomologTC', evtCdBenIn.infoBenInicio.dadosBeneficio.indHomologTC.cdata, 1, 'S;N')
    if 'infoPenMorte' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio):
        for infoPenMorte in evtCdBenIn.infoBenInicio.dadosBeneficio.infoPenMorte:
       
            if 'tpPenMorte' in dir(infoPenMorte): validacoes_lista = validar_campo(validacoes_lista,'infoPenMorte.tpPenMorte', infoPenMorte.tpPenMorte.cdata, 1, '1;2')

            if 'instPenMorte' in dir(infoPenMorte):
                for instPenMorte in infoPenMorte.instPenMorte:
               
                    if 'cpfInst' in dir(instPenMorte): validacoes_lista = validar_campo(validacoes_lista,'instPenMorte.cpfInst', instPenMorte.cpfInst.cdata, 1, '')
                    if 'dtInst' in dir(instPenMorte): validacoes_lista = validar_campo(validacoes_lista,'instPenMorte.dtInst', instPenMorte.dtInst.cdata, 1, '')
                    if 'intAposentado' in dir(instPenMorte): validacoes_lista = validar_campo(validacoes_lista,'instPenMorte.intAposentado', instPenMorte.intAposentado.cdata, 1, 'S;N')
   
    if 'homologTC' in dir(evtCdBenIn.infoBenInicio.dadosBeneficio):
        for homologTC in evtCdBenIn.infoBenInicio.dadosBeneficio.homologTC:
       
            if 'dtHomol' in dir(homologTC): validacoes_lista = validar_campo(validacoes_lista,'homologTC.dtHomol', homologTC.dtHomol.cdata, 1, '')
            if 'nrAtoLegal' in dir(homologTC): validacoes_lista = validar_campo(validacoes_lista,'homologTC.nrAtoLegal', homologTC.nrAtoLegal.cdata, 1, '')

    return validacoes_lista