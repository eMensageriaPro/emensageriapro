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


def validacoes_s1270_evtcontratavnp(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtContratAvNP = doc.eSocial.evtContratAvNP
    #variaveis

    if 'ideEvento' in dir(evtContratAvNP.ideEvento):
        for ideEvento in evtContratAvNP.ideEvento:

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
                                                  1, u'1')

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

    if 'ideEmpregador' in dir(evtContratAvNP.ideEmpregador):
        for ideEmpregador in evtContratAvNP.ideEmpregador:

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

    if 'remunAvNP' in dir(evtContratAvNP.remunAvNP):
        for remunAvNP in evtContratAvNP.remunAvNP:

            if 'tpInsc' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.tpInsc',
                                                  remunAvNP.tpInsc.cdata,
                                                  1, u'1, 2, 3, 4, 5, 6')

            if 'nrInsc' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.nrInsc',
                                                  remunAvNP.nrInsc.cdata,
                                                  1, u'None')

            if 'codLotacao' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.codLotacao',
                                                  remunAvNP.codLotacao.cdata,
                                                  1, u'None')

            if 'vrBcCp00' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.vrBcCp00',
                                                  remunAvNP.vrBcCp00.cdata,
                                                  1, u'None')

            if 'vrBcCp15' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.vrBcCp15',
                                                  remunAvNP.vrBcCp15.cdata,
                                                  1, u'None')

            if 'vrBcCp20' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.vrBcCp20',
                                                  remunAvNP.vrBcCp20.cdata,
                                                  1, u'None')

            if 'vrBcCp25' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.vrBcCp25',
                                                  remunAvNP.vrBcCp25.cdata,
                                                  1, u'None')

            if 'vrBcCp13' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.vrBcCp13',
                                                  remunAvNP.vrBcCp13.cdata,
                                                  1, u'None')

            if 'vrBcFgts' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.vrBcFgts',
                                                  remunAvNP.vrBcFgts.cdata,
                                                  1, u'None')

            if 'vrDescCP' in dir(remunAvNP):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'remunAvNP.vrDescCP',
                                                  remunAvNP.vrDescCP.cdata,
                                                  1, u'None')
    return validacoes_lista