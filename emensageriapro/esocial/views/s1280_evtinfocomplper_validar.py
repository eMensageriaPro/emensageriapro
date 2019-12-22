# eMensageriaAI #
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


def validacoes_s1280_evtinfocomplper(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtInfoComplPer = doc.eSocial.evtInfoComplPer
    #variaveis

    if 'ideEvento' in dir(evtInfoComplPer.ideEvento):
        for ideEvento in evtInfoComplPer.ideEvento:

            if 'indRetif' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indRetif',
                                                  ideEvento.indRetif.cdata,
                                                  1, u'1, 2')

            if 'nrRecibo' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.nrRecibo',
                                                  ideEvento.nrRecibo.cdata,
                                                  0, u'None')

            if 'indApuracao' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indApuracao',
                                                  ideEvento.indApuracao.cdata,
                                                  1, u'1, 2')

            if 'perApur' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perApur',
                                                  ideEvento.perApur.cdata,
                                                  1, u'None')

            if 'tpAmb' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.tpAmb',
                                                  ideEvento.tpAmb.cdata,
                                                  1, u'1, 2')

            if 'procEmi' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.procEmi',
                                                  ideEvento.procEmi.cdata,
                                                  1, u'1, 2, 3, 4, 5')

            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc',
                                                  ideEvento.verProc.cdata,
                                                  1, u'None')

    if 'ideEmpregador' in dir(evtInfoComplPer.ideEmpregador):
        for ideEmpregador in evtInfoComplPer.ideEmpregador:

            if 'tpInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.tpInsc',
                                                  ideEmpregador.tpInsc.cdata,
                                                  1, u'1, 2, 3, 4, 5, 6')

            if 'nrInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.nrInsc',
                                                  ideEmpregador.nrInsc.cdata,
                                                  1, u'None')

    if 'infoSubstPatr' in dir(evtInfoComplPer.infoSubstPatr):
        for infoSubstPatr in evtInfoComplPer.infoSubstPatr:

            if 'indSubstPatr' in dir(infoSubstPatr):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoSubstPatr.indSubstPatr',
                                                  infoSubstPatr.indSubstPatr.cdata,
                                                  1, u'1, 2')

            if 'percRedContrib' in dir(infoSubstPatr):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoSubstPatr.percRedContrib',
                                                  infoSubstPatr.percRedContrib.cdata,
                                                  1, u'None')

    if 'infoSubstPatrOpPort' in dir(evtInfoComplPer.infoSubstPatrOpPort):
        for infoSubstPatrOpPort in evtInfoComplPer.infoSubstPatrOpPort:

            if 'cnpjOpPortuario' in dir(infoSubstPatrOpPort):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoSubstPatrOpPort.cnpjOpPortuario',
                                                  infoSubstPatrOpPort.cnpjOpPortuario.cdata,
                                                  1, u'None')

    if 'infoAtivConcom' in dir(evtInfoComplPer.infoAtivConcom):
        for infoAtivConcom in evtInfoComplPer.infoAtivConcom:

            if 'fatorMes' in dir(infoAtivConcom):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoAtivConcom.fatorMes',
                                                  infoAtivConcom.fatorMes.cdata,
                                                  1, u'None')

            if 'fator13' in dir(infoAtivConcom):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoAtivConcom.fator13',
                                                  infoAtivConcom.fator13.cdata,
                                                  1, u'None')
    return validacoes_lista