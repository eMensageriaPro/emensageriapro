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


def validacoes_s1207_evtbenprrp(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtBenPrRP = doc.eSocial.evtBenPrRP
    
    if 'indRetif' in dir(evtBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideEvento.indRetif', evtBenPrRP.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideEvento.nrRecibo', evtBenPrRP.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideEvento.indApuracao', evtBenPrRP.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideEvento.perApur', evtBenPrRP.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideEvento.tpAmb', evtBenPrRP.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideEvento.procEmi', evtBenPrRP.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtBenPrRP.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideEvento.verProc', evtBenPrRP.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtBenPrRP.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideEmpregador.tpInsc', evtBenPrRP.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtBenPrRP.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideEmpregador.nrInsc', evtBenPrRP.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfBenef' in dir(evtBenPrRP.ideBenef): validacoes_lista = validar_campo(validacoes_lista,'evtBenPrRP.ideBenef.cpfBenef', evtBenPrRP.ideBenef.cpfBenef.cdata, 1, '')
    if 'procJudTrab' in dir(evtBenPrRP.ideBenef):
        for procJudTrab in evtBenPrRP.ideBenef.procJudTrab:
            
            if 'tpTrib' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.tpTrib', procJudTrab.tpTrib.cdata, 1, '1;5')
            if 'nrProcJud' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.nrProcJud', procJudTrab.nrProcJud.cdata, 1, '')
            if 'codSusp' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.codSusp', procJudTrab.codSusp.cdata, 0, '')

    if 'dmDev' in dir(evtBenPrRP):
        for dmDev in evtBenPrRP.dmDev:
            
            if 'tpBenef' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.tpBenef', dmDev.tpBenef.cdata, 1, '1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;91;92;93;94;95;96;97;98;99')
            if 'nrBenefic' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.nrBenefic', dmDev.nrBenefic.cdata, 1, '')
            if 'ideDmDev' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.ideDmDev', dmDev.ideDmDev.cdata, 1, '')

            if 'itens' in dir(dmDev):
                for itens in dmDev.itens:
                    
                    if 'codRubr' in dir(itens): validacoes_lista = validar_campo(validacoes_lista,'itens.codRubr', itens.codRubr.cdata, 1, '')
                    if 'ideTabRubr' in dir(itens): validacoes_lista = validar_campo(validacoes_lista,'itens.ideTabRubr', itens.ideTabRubr.cdata, 1, '')
                    if 'vrRubr' in dir(itens): validacoes_lista = validar_campo(validacoes_lista,'itens.vrRubr', itens.vrRubr.cdata, 1, '')
        
            if 'infoPerApur' in dir(dmDev):
                for infoPerApur in dmDev.infoPerApur:
                    
        
            if 'infoPerAnt' in dir(dmDev):
                for infoPerAnt in dmDev.infoPerAnt:
                    
        
    return validacoes_lista