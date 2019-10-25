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


def validacoes_s2420_evtcdbenterm(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCdBenTerm = doc.eSocial.evtCdBenTerm
    #variaveis

    if 'ideEvento' in dir(evtCdBenTerm.ideEvento):
        for ideEvento in evtCdBenTerm.ideEvento:

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

    if 'ideEmpregador' in dir(evtCdBenTerm.ideEmpregador):
        for ideEmpregador in evtCdBenTerm.ideEmpregador:

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

    if 'ideBeneficio' in dir(evtCdBenTerm.ideBeneficio):
        for ideBeneficio in evtCdBenTerm.ideBeneficio:

            if 'cpfBenef' in dir(ideBeneficio):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBeneficio.cpfBenef',
                                                  ideBeneficio.cpfBenef.cdata,
                                                  1, u'None')

            if 'nrBeneficio' in dir(ideBeneficio):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBeneficio.nrBeneficio',
                                                  ideBeneficio.nrBeneficio.cdata,
                                                  1, u'None')

    if 'infoBenTermino' in dir(evtCdBenTerm.infoBenTermino):
        for infoBenTermino in evtCdBenTerm.infoBenTermino:

            if 'dtTermBeneficio' in dir(infoBenTermino):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoBenTermino.dtTermBeneficio',
                                                  infoBenTermino.dtTermBeneficio.cdata,
                                                  1, u'None')

            if 'mtvTermino' in dir(infoBenTermino):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoBenTermino.mtvTermino',
                                                  infoBenTermino.mtvTermino.cdata,
                                                  1, u'1, 2, 3, 4, 5, 6, 7, 8')
    return validacoes_lista