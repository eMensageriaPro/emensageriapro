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


def validacoes_s1250_evtaqprod(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAqProd = doc.eSocial.evtAqProd

    if 'indRetif' in dir(evtAqProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.ideEvento.indRetif', evtAqProd.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtAqProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.ideEvento.nrRecibo', evtAqProd.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtAqProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.ideEvento.indApuracao', evtAqProd.ideEvento.indApuracao.cdata, 1, '1')
    if 'perApur' in dir(evtAqProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.ideEvento.perApur', evtAqProd.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtAqProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.ideEvento.tpAmb', evtAqProd.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtAqProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.ideEvento.procEmi', evtAqProd.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtAqProd.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.ideEvento.verProc', evtAqProd.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtAqProd.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.ideEmpregador.tpInsc', evtAqProd.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtAqProd.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.ideEmpregador.nrInsc', evtAqProd.ideEmpregador.nrInsc.cdata, 1, '')
    if 'tpInscAdq' in dir(evtAqProd.infoAquisProd.ideEstabAdquir): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.infoAquisProd.ideEstabAdquir.tpInscAdq', evtAqProd.infoAquisProd.ideEstabAdquir.tpInscAdq.cdata, 1, '1;2;3;4')
    if 'nrInscAdq' in dir(evtAqProd.infoAquisProd.ideEstabAdquir): validacoes_lista = validar_campo(validacoes_lista,'evtAqProd.infoAquisProd.ideEstabAdquir.nrInscAdq', evtAqProd.infoAquisProd.ideEstabAdquir.nrInscAdq.cdata, 1, '')
    if 'tpAquis' in dir(evtAqProd.infoAquisProd.ideEstabAdquir):
        for tpAquis in evtAqProd.infoAquisProd.ideEstabAdquir.tpAquis:


            if 'ideProdutor' in dir(tpAquis):
                for ideProdutor in tpAquis.ideProdutor:


            if 'infoProcJ' in dir(tpAquis):
                for infoProcJ in tpAquis.infoProcJ:


    return validacoes_lista