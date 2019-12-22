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


def validacoes_s1035_evttabcarreira(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabCarreira = doc.eSocial.evtTabCarreira
    #variaveis

    if 'ideEvento' in dir(evtTabCarreira.ideEvento):
        for ideEvento in evtTabCarreira.ideEvento:

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

    if 'ideEmpregador' in dir(evtTabCarreira.ideEmpregador):
        for ideEmpregador in evtTabCarreira.ideEmpregador:

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

    if 'infoCarreira' in dir(evtTabCarreira.infoCarreira):
        for infoCarreira in evtTabCarreira.infoCarreira:

            if 'inclusao' in dir(infoCarreira.inclusao):
                for inclusao in infoCarreira.inclusao:

                    if 'ideCarreira' in dir(inclusao.ideCarreira):
                        for ideCarreira in inclusao.ideCarreira:
        
                            if 'codCarreira' in dir(ideCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCarreira.codCarreira',
                                                                  ideCarreira.codCarreira.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCarreira.iniValid',
                                                                  ideCarreira.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCarreira.fimValid',
                                                                  ideCarreira.fimValid.cdata,
                                                                  0, u'None')

                    if 'dadosCarreira' in dir(inclusao.dadosCarreira):
                        for dadosCarreira in inclusao.dadosCarreira:
        
                            if 'dscCarreira' in dir(dadosCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCarreira.dscCarreira',
                                                                  dadosCarreira.dscCarreira.cdata,
                                                                  1, u'None')
        
                            if 'leiCarr' in dir(dadosCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCarreira.leiCarr',
                                                                  dadosCarreira.leiCarr.cdata,
                                                                  0, u'None')
        
                            if 'dtLeiCarr' in dir(dadosCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCarreira.dtLeiCarr',
                                                                  dadosCarreira.dtLeiCarr.cdata,
                                                                  1, u'None')
        
                            if 'sitCarr' in dir(dadosCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCarreira.sitCarr',
                                                                  dadosCarreira.sitCarr.cdata,
                                                                  1, u'1, 2, 3')

            if 'alteracao' in dir(infoCarreira.alteracao):
                for alteracao in infoCarreira.alteracao:

                    if 'ideCarreira' in dir(alteracao.ideCarreira):
                        for ideCarreira in alteracao.ideCarreira:
        
                            if 'codCarreira' in dir(ideCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCarreira.codCarreira',
                                                                  ideCarreira.codCarreira.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCarreira.iniValid',
                                                                  ideCarreira.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCarreira.fimValid',
                                                                  ideCarreira.fimValid.cdata,
                                                                  0, u'None')

                    if 'dadosCarreira' in dir(alteracao.dadosCarreira):
                        for dadosCarreira in alteracao.dadosCarreira:
        
                            if 'dscCarreira' in dir(dadosCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCarreira.dscCarreira',
                                                                  dadosCarreira.dscCarreira.cdata,
                                                                  1, u'None')
        
                            if 'leiCarr' in dir(dadosCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCarreira.leiCarr',
                                                                  dadosCarreira.leiCarr.cdata,
                                                                  0, u'None')
        
                            if 'dtLeiCarr' in dir(dadosCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCarreira.dtLeiCarr',
                                                                  dadosCarreira.dtLeiCarr.cdata,
                                                                  1, u'None')
        
                            if 'sitCarr' in dir(dadosCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosCarreira.sitCarr',
                                                                  dadosCarreira.sitCarr.cdata,
                                                                  1, u'1, 2, 3')

                    if 'novaValidade' in dir(alteracao.novaValidade):
                        for novaValidade in alteracao.novaValidade:
        
                            if 'iniValid' in dir(novaValidade):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'novaValidade.iniValid',
                                                                  novaValidade.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(novaValidade):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'novaValidade.fimValid',
                                                                  novaValidade.fimValid.cdata,
                                                                  0, u'None')

            if 'exclusao' in dir(infoCarreira.exclusao):
                for exclusao in infoCarreira.exclusao:

                    if 'ideCarreira' in dir(exclusao.ideCarreira):
                        for ideCarreira in exclusao.ideCarreira:
        
                            if 'codCarreira' in dir(ideCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCarreira.codCarreira',
                                                                  ideCarreira.codCarreira.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCarreira.iniValid',
                                                                  ideCarreira.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideCarreira):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideCarreira.fimValid',
                                                                  ideCarreira.fimValid.cdata,
                                                                  0, u'None')
    return validacoes_lista