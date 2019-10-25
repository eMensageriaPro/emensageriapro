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


def validacoes_s2231_evtcessao(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCessao = doc.eSocial.evtCessao
    #variaveis

    if 'ideEvento' in dir(evtCessao.ideEvento):
        for ideEvento in evtCessao.ideEvento:

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

    if 'ideEmpregador' in dir(evtCessao.ideEmpregador):
        for ideEmpregador in evtCessao.ideEmpregador:

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

    if 'ideVinculo' in dir(evtCessao.ideVinculo):
        for ideVinculo in evtCessao.ideVinculo:

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

    if 'infoCessao' in dir(evtCessao.infoCessao):
        for infoCessao in evtCessao.infoCessao:

            if 'iniCessao' in dir(infoCessao.iniCessao):
                for iniCessao in infoCessao.iniCessao:

                    if 'dtIniCessao' in dir(iniCessao):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniCessao.dtIniCessao',
                                                          iniCessao.dtIniCessao.cdata,
                                                          1, u'None')

                    if 'cnpjCess' in dir(iniCessao):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniCessao.cnpjCess',
                                                          iniCessao.cnpjCess.cdata,
                                                          1, u'None')

                    if 'infOnus' in dir(iniCessao):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniCessao.infOnus',
                                                          iniCessao.infOnus.cdata,
                                                          1, u'1, 2, 3, 4')

                    if 'indCessao' in dir(iniCessao):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniCessao.indCessao',
                                                          iniCessao.indCessao.cdata,
                                                          1, u'1, 2, 3')

                    if 'dscSituacao' in dir(iniCessao):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'iniCessao.dscSituacao',
                                                          iniCessao.dscSituacao.cdata,
                                                          0, u'None')

            if 'fimCessao' in dir(infoCessao.fimCessao):
                for fimCessao in infoCessao.fimCessao:

                    if 'dtTermCessao' in dir(fimCessao):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fimCessao.dtTermCessao',
                                                          fimCessao.dtTermCessao.cdata,
                                                          1, u'None')
    return validacoes_lista