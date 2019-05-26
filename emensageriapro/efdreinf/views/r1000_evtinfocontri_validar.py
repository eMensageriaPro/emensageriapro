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


def validacoes_r1000_evtinfocontri(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtInfoContri = doc.Reinf.evtInfoContri
    #variaveis
    
    if 'ideEvento' in dir(evtInfoContri.ideEvento):
        for ideEvento in evtInfoContri.ideEvento:
            
            if 'tpAmb' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.tpAmb', 
                                                  ideEvento.tpAmb.cdata, 
                                                  1, u'1, 2')
            
            if 'procEmi' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.procEmi', 
                                                  ideEvento.procEmi.cdata, 
                                                  1, u'1, 2')
            
            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc', 
                                                  ideEvento.verProc.cdata, 
                                                  1, u'None')
    
    if 'ideContri' in dir(evtInfoContri.ideContri):
        for ideContri in evtInfoContri.ideContri:
            
            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc', 
                                                  ideContri.tpInsc.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc', 
                                                  ideContri.nrInsc.cdata, 
                                                  1, u'None')
    
    if 'infoContri' in dir(evtInfoContri.infoContri):
        for infoContri in evtInfoContri.infoContri:
            
            if 'inclusao' in dir(infoContri.inclusao):
                for inclusao in infoContri.inclusao:
                    
                    if 'idePeriodo' in dir(inclusao.idePeriodo):
                        for idePeriodo in inclusao.idePeriodo:
                            
                            if 'iniValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.iniValid', 
                                                                  idePeriodo.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.fimValid', 
                                                                  idePeriodo.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'infoCadastro' in dir(inclusao.infoCadastro):
                        for infoCadastro in inclusao.infoCadastro:
                            
                            if 'classTrib' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.classTrib', 
                                                                  infoCadastro.classTrib.cdata, 
                                                                  1, u'01, 02, 03, 04, 06, 07, 08, 09, 10, 11, 13, 14, 21, 22, 60, 70, 80, 85, 99')
                            
                            if 'indEscrituracao' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indEscrituracao', 
                                                                  infoCadastro.indEscrituracao.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indDesoneracao' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indDesoneracao', 
                                                                  infoCadastro.indDesoneracao.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indAcordoIsenMulta' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indAcordoIsenMulta', 
                                                                  infoCadastro.indAcordoIsenMulta.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indSitPJ' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indSitPJ', 
                                                                  infoCadastro.indSitPJ.cdata, 
                                                                  0, u'0, 1, 2, 3, 4')
                            
                            if 'contato' in dir(infoCadastro.contato):
                                for contato in infoCadastro.contato:
                                    
                                    if 'nmCtt' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.nmCtt', 
                                                                          contato.nmCtt.cdata, 
                                                                          1, u'None')
                                    
                                    if 'cpfCtt' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.cpfCtt', 
                                                                          contato.cpfCtt.cdata, 
                                                                          1, u'None')
                                    
                                    if 'foneFixo' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.foneFixo', 
                                                                          contato.foneFixo.cdata, 
                                                                          0, u'None')
                                    
                                    if 'foneCel' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.foneCel', 
                                                                          contato.foneCel.cdata, 
                                                                          0, u'None')
                                    
                                    if 'email' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.email', 
                                                                          contato.email.cdata, 
                                                                          0, u'None')
                            
                            if 'softHouse' in dir(infoCadastro.softHouse):
                                for softHouse in infoCadastro.softHouse:
                                    
                                    if 'cnpjSoftHouse' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.cnpjSoftHouse', 
                                                                          softHouse.cnpjSoftHouse.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmRazao' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.nmRazao', 
                                                                          softHouse.nmRazao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmCont' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.nmCont', 
                                                                          softHouse.nmCont.cdata, 
                                                                          1, u'None')
                                    
                                    if 'telefone' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.telefone', 
                                                                          softHouse.telefone.cdata, 
                                                                          0, u'None')
                                    
                                    if 'email' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.email', 
                                                                          softHouse.email.cdata, 
                                                                          0, u'None')
                            
                            if 'infoEFR' in dir(infoCadastro.infoEFR):
                                for infoEFR in infoCadastro.infoEFR:
                                    
                                    if 'ideEFR' in dir(infoEFR):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEFR.ideEFR', 
                                                                          infoEFR.ideEFR.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'cnpjEFR' in dir(infoEFR):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEFR.cnpjEFR', 
                                                                          infoEFR.cnpjEFR.cdata, 
                                                                          0, u'None')
            
            if 'alteracao' in dir(infoContri.alteracao):
                for alteracao in infoContri.alteracao:
                    
                    if 'idePeriodo' in dir(alteracao.idePeriodo):
                        for idePeriodo in alteracao.idePeriodo:
                            
                            if 'iniValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.iniValid', 
                                                                  idePeriodo.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.fimValid', 
                                                                  idePeriodo.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'infoCadastro' in dir(alteracao.infoCadastro):
                        for infoCadastro in alteracao.infoCadastro:
                            
                            if 'classTrib' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.classTrib', 
                                                                  infoCadastro.classTrib.cdata, 
                                                                  1, u'01, 02, 03, 04, 06, 07, 08, 09, 10, 11, 13, 14, 21, 22, 60, 70, 80, 85, 99')
                            
                            if 'indEscrituracao' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indEscrituracao', 
                                                                  infoCadastro.indEscrituracao.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indDesoneracao' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indDesoneracao', 
                                                                  infoCadastro.indDesoneracao.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indAcordoIsenMulta' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indAcordoIsenMulta', 
                                                                  infoCadastro.indAcordoIsenMulta.cdata, 
                                                                  1, u'0, 1')
                            
                            if 'indSitPJ' in dir(infoCadastro):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCadastro.indSitPJ', 
                                                                  infoCadastro.indSitPJ.cdata, 
                                                                  0, u'0, 1, 2, 3, 4')
                            
                            if 'contato' in dir(infoCadastro.contato):
                                for contato in infoCadastro.contato:
                                    
                                    if 'nmCtt' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.nmCtt', 
                                                                          contato.nmCtt.cdata, 
                                                                          1, u'None')
                                    
                                    if 'cpfCtt' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.cpfCtt', 
                                                                          contato.cpfCtt.cdata, 
                                                                          1, u'None')
                                    
                                    if 'foneFixo' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.foneFixo', 
                                                                          contato.foneFixo.cdata, 
                                                                          0, u'None')
                                    
                                    if 'foneCel' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.foneCel', 
                                                                          contato.foneCel.cdata, 
                                                                          0, u'None')
                                    
                                    if 'email' in dir(contato):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'contato.email', 
                                                                          contato.email.cdata, 
                                                                          0, u'None')
                            
                            if 'softHouse' in dir(infoCadastro.softHouse):
                                for softHouse in infoCadastro.softHouse:
                                    
                                    if 'cnpjSoftHouse' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.cnpjSoftHouse', 
                                                                          softHouse.cnpjSoftHouse.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmRazao' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.nmRazao', 
                                                                          softHouse.nmRazao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nmCont' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.nmCont', 
                                                                          softHouse.nmCont.cdata, 
                                                                          1, u'None')
                                    
                                    if 'telefone' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.telefone', 
                                                                          softHouse.telefone.cdata, 
                                                                          0, u'None')
                                    
                                    if 'email' in dir(softHouse):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'softHouse.email', 
                                                                          softHouse.email.cdata, 
                                                                          0, u'None')
                            
                            if 'infoEFR' in dir(infoCadastro.infoEFR):
                                for infoEFR in infoCadastro.infoEFR:
                                    
                                    if 'ideEFR' in dir(infoEFR):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEFR.ideEFR', 
                                                                          infoEFR.ideEFR.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'cnpjEFR' in dir(infoEFR):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEFR.cnpjEFR', 
                                                                          infoEFR.cnpjEFR.cdata, 
                                                                          0, u'None')
                    
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
            
            if 'exclusao' in dir(infoContri.exclusao):
                for exclusao in infoContri.exclusao:
                    
                    if 'idePeriodo' in dir(exclusao.idePeriodo):
                        for idePeriodo in exclusao.idePeriodo:
                            
                            if 'iniValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.iniValid', 
                                                                  idePeriodo.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(idePeriodo):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePeriodo.fimValid', 
                                                                  idePeriodo.fimValid.cdata, 
                                                                  0, u'None')
    return validacoes_lista