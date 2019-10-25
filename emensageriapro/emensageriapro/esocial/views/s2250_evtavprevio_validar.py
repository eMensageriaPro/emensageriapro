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


def validacoes_s2250_evtavprevio(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAvPrevio = doc.eSocial.evtAvPrevio
    #variaveis

    if 'ideEvento' in dir(evtAvPrevio.ideEvento):
        for ideEvento in evtAvPrevio.ideEvento:

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

    if 'ideEmpregador' in dir(evtAvPrevio.ideEmpregador):
        for ideEmpregador in evtAvPrevio.ideEmpregador:

            if 'tpInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.tpInsc',
                                                  ideEmpregador.tpInsc.cdata,
                                                  1, u'1, 2, 3, 4, 5')

            if 'nrInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.nrInsc',
                                                  ideEmpregador.nrInsc.cdata,
                                                  1, u'None')

    if 'ideVinculo' in dir(evtAvPrevio.ideVinculo):
        for ideVinculo in evtAvPrevio.ideVinculo:

            if 'cpfTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.cpfTrab',
                                                  ideVinculo.cpfTrab.cdata,
                                                  1, u'None')

            if 'nisTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.nisTrab',
                                                  ideVinculo.nisTrab.cdata,
                                                  1, u'None')

            if 'matricula' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.matricula',
                                                  ideVinculo.matricula.cdata,
                                                  1, u'None')

    if 'infoAvPrevio' in dir(evtAvPrevio.infoAvPrevio):
        for infoAvPrevio in evtAvPrevio.infoAvPrevio:

            if 'detAvPrevio' in dir(infoAvPrevio.detAvPrevio):
                for detAvPrevio in infoAvPrevio.detAvPrevio:

                    if 'dtAvPrv' in dir(detAvPrevio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'detAvPrevio.dtAvPrv',
                                                          detAvPrevio.dtAvPrv.cdata,
                                                          1, u'None')

                    if 'dtPrevDeslig' in dir(detAvPrevio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'detAvPrevio.dtPrevDeslig',
                                                          detAvPrevio.dtPrevDeslig.cdata,
                                                          1, u'None')

                    if 'tpAvPrevio' in dir(detAvPrevio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'detAvPrevio.tpAvPrevio',
                                                          detAvPrevio.tpAvPrevio.cdata,
                                                          1, u'1, 2, 4, 5, 6')

                    if 'observacao' in dir(detAvPrevio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'detAvPrevio.observacao',
                                                          detAvPrevio.observacao.cdata,
                                                          0, u'None')

            if 'cancAvPrevio' in dir(infoAvPrevio.cancAvPrevio):
                for cancAvPrevio in infoAvPrevio.cancAvPrevio:

                    if 'dtCancAvPrv' in dir(cancAvPrevio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'cancAvPrevio.dtCancAvPrv',
                                                          cancAvPrevio.dtCancAvPrv.cdata,
                                                          1, u'None')

                    if 'observacao' in dir(cancAvPrevio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'cancAvPrevio.observacao',
                                                          cancAvPrevio.observacao.cdata,
                                                          0, u'None')

                    if 'mtvCancAvPrevio' in dir(cancAvPrevio):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'cancAvPrevio.mtvCancAvPrevio',
                                                          cancAvPrevio.mtvCancAvPrevio.cdata,
                                                          1, u'1, 2, 3, 9')
    return validacoes_lista