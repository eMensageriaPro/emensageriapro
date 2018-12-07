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


def validacoes_s1202_evtrmnrpps(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtRmnRPPS = doc.eSocial.evtRmnRPPS

    if 'indRetif' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.indRetif', evtRmnRPPS.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.nrRecibo', evtRmnRPPS.ideEvento.nrRecibo.cdata, 0, '')
    if 'indApuracao' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.indApuracao', evtRmnRPPS.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.perApur', evtRmnRPPS.ideEvento.perApur.cdata, 1, '')
    if 'tpAmb' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.tpAmb', evtRmnRPPS.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.procEmi', evtRmnRPPS.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtRmnRPPS.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEvento.verProc', evtRmnRPPS.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtRmnRPPS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEmpregador.tpInsc', evtRmnRPPS.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtRmnRPPS.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideEmpregador.nrInsc', evtRmnRPPS.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtRmnRPPS.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideTrabalhador.cpfTrab', evtRmnRPPS.ideTrabalhador.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtRmnRPPS.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideTrabalhador.nisTrab', evtRmnRPPS.ideTrabalhador.nisTrab.cdata, 0, '')
    if 'qtdDepFP' in dir(evtRmnRPPS.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtRmnRPPS.ideTrabalhador.qtdDepFP', evtRmnRPPS.ideTrabalhador.qtdDepFP.cdata, 0, '')
    if 'procJudTrab' in dir(evtRmnRPPS.ideTrabalhador):
        for procJudTrab in evtRmnRPPS.ideTrabalhador.procJudTrab:
       
            if 'tpTrib' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.tpTrib', procJudTrab.tpTrib.cdata, 1, '2;2;3;4')
            if 'nrProcJud' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.nrProcJud', procJudTrab.nrProcJud.cdata, 1, '')
            if 'codSusp' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.codSusp', procJudTrab.codSusp.cdata, 0, '')

    if 'dmDev' in dir(evtRmnRPPS):
        for dmDev in evtRmnRPPS.dmDev:
       
            if 'ideDmDev' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.ideDmDev', dmDev.ideDmDev.cdata, 1, '')
            if 'codCateg' in dir(dmDev): validacoes_lista = validar_campo(validacoes_lista,'dmDev.codCateg', dmDev.codCateg.cdata, 1, '')

            if 'ideEstab' in dir(dmDev.infoPerApur):
                for ideEstab in dmDev.infoPerApur.ideEstab:
               
                    if 'tpInsc' in dir(ideEstab): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.tpInsc', ideEstab.tpInsc.cdata, 1, '1;2;3;4')
                    if 'nrInsc' in dir(ideEstab): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.nrInsc', ideEstab.nrInsc.cdata, 1, '')
   
            if 'ideADC' in dir(dmDev.infoPerAnt):
                for ideADC in dmDev.infoPerAnt.ideADC:
               
                    if 'dtLei' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.dtLei', ideADC.dtLei.cdata, 1, '')
                    if 'nrLei' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.nrLei', ideADC.nrLei.cdata, 1, '')
                    if 'dtEf' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.dtEf', ideADC.dtEf.cdata, 0, '')
                    if 'dtAcConv' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.dtAcConv', ideADC.dtAcConv.cdata, 0, '')
                    if 'tpAcConv' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.tpAcConv', ideADC.tpAcConv.cdata, 1, 'B;F;G;H')
                    if 'compAcConv' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.compAcConv', ideADC.compAcConv.cdata, 0, '')
                    if 'dtEfAcConv' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.dtEfAcConv', ideADC.dtEfAcConv.cdata, 0, '')
                    if 'dsc' in dir(ideADC): validacoes_lista = validar_campo(validacoes_lista,'ideADC.dsc', ideADC.dsc.cdata, 1, '')
   
    return validacoes_lista