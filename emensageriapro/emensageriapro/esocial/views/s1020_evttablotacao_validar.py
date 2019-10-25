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


def validacoes_s1020_evttablotacao(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabLotacao = doc.eSocial.evtTabLotacao
    #variaveis

    if 'ideEvento' in dir(evtTabLotacao.ideEvento):
        for ideEvento in evtTabLotacao.ideEvento:

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

    if 'ideEmpregador' in dir(evtTabLotacao.ideEmpregador):
        for ideEmpregador in evtTabLotacao.ideEmpregador:

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

    if 'infoLotacao' in dir(evtTabLotacao.infoLotacao):
        for infoLotacao in evtTabLotacao.infoLotacao:

            if 'inclusao' in dir(infoLotacao.inclusao):
                for inclusao in infoLotacao.inclusao:

                    if 'ideLotacao' in dir(inclusao.ideLotacao):
                        for ideLotacao in inclusao.ideLotacao:
        
                            if 'codLotacao' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.codLotacao',
                                                                  ideLotacao.codLotacao.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.iniValid',
                                                                  ideLotacao.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.fimValid',
                                                                  ideLotacao.fimValid.cdata,
                                                                  0, u'None')

                    if 'dadosLotacao' in dir(inclusao.dadosLotacao):
                        for dadosLotacao in inclusao.dadosLotacao:
        
                            if 'tpLotacao' in dir(dadosLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosLotacao.tpLotacao',
                                                                  dadosLotacao.tpLotacao.cdata,
                                                                  1, u'01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 21, 24, 90, 91')
        
                            if 'tpInsc' in dir(dadosLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosLotacao.tpInsc',
                                                                  dadosLotacao.tpInsc.cdata,
                                                                  0, u'1, 2, 3, 4, 5')
        
                            if 'nrInsc' in dir(dadosLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosLotacao.nrInsc',
                                                                  dadosLotacao.nrInsc.cdata,
                                                                  0, u'None')
        
                            if 'fpasLotacao' in dir(dadosLotacao.fpasLotacao):
                                for fpasLotacao in dadosLotacao.fpasLotacao:
                
                                    if 'fpas' in dir(fpasLotacao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fpasLotacao.fpas',
                                                                          fpasLotacao.fpas.cdata,
                                                                          1, u'507, 515, 523, 531, 540, 558, 566, 574, 582, 590, 604, 612, 620, 639, 647, 655, 680, 736, 744, 779, 787, 795, 825, 833, 868, 876')
                
                                    if 'codTercs' in dir(fpasLotacao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fpasLotacao.codTercs',
                                                                          fpasLotacao.codTercs.cdata,
                                                                          1, u'0000, 0001, 0002, 0003, 0004, 0008, 0016, 0032, 0064, 0067, 0071, 0075, 0079, 0099, 0115, 0128, 0131, 0256, 0259, 0512, 0515, 1024, 2048, 3072, 3139, 4096, 4099, 4163')
                
                                    if 'codTercsSusp' in dir(fpasLotacao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fpasLotacao.codTercsSusp',
                                                                          fpasLotacao.codTercsSusp.cdata,
                                                                          0, u'0000, 0001, 0002, 0003, 0004, 0008, 0016, 0032, 0064, 0067, 0071, 0075, 0079, 0099, 0115, 0128, 0131, 0256, 0259, 0512, 0515, 1024, 2048, 3072, 3139, 4096, 4099, 4163')
                
                                    if 'infoProcJudTerceiros' in dir(fpasLotacao.infoProcJudTerceiros):
                                        for infoProcJudTerceiros in fpasLotacao.infoProcJudTerceiros:
                        
                                            if 'procJudTerceiro' in dir(infoProcJudTerceiros.procJudTerceiro):
                                                for procJudTerceiro in infoProcJudTerceiros.procJudTerceiro:
                                
                                                    if 'codTerc' in dir(procJudTerceiro):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'procJudTerceiro.codTerc',
                                                                                          procJudTerceiro.codTerc.cdata,
                                                                                          1, u'0000, 0001, 0002, 0003, 0004, 0008, 0016, 0032, 0064, 0067, 0071, 0075, 0079, 0099, 0115, 0128, 0131, 0256, 0259, 0512, 0515, 1024, 2048, 3072, 3139, 4096, 4099, 4163')
                                
                                                    if 'nrProcJud' in dir(procJudTerceiro):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'procJudTerceiro.nrProcJud',
                                                                                          procJudTerceiro.nrProcJud.cdata,
                                                                                          1, u'None')
                                
                                                    if 'codSusp' in dir(procJudTerceiro):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'procJudTerceiro.codSusp',
                                                                                          procJudTerceiro.codSusp.cdata,
                                                                                          1, u'None')
        
                            if 'infoEmprParcial' in dir(dadosLotacao.infoEmprParcial):
                                for infoEmprParcial in dadosLotacao.infoEmprParcial:
                
                                    if 'tpInscContrat' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.tpInscContrat',
                                                                          infoEmprParcial.tpInscContrat.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrInscContrat' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.nrInscContrat',
                                                                          infoEmprParcial.nrInscContrat.cdata,
                                                                          1, u'None')
                
                                    if 'tpInscProp' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.tpInscProp',
                                                                          infoEmprParcial.tpInscProp.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrInscProp' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.nrInscProp',
                                                                          infoEmprParcial.nrInscProp.cdata,
                                                                          1, u'None')

            if 'alteracao' in dir(infoLotacao.alteracao):
                for alteracao in infoLotacao.alteracao:

                    if 'ideLotacao' in dir(alteracao.ideLotacao):
                        for ideLotacao in alteracao.ideLotacao:
        
                            if 'codLotacao' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.codLotacao',
                                                                  ideLotacao.codLotacao.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.iniValid',
                                                                  ideLotacao.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.fimValid',
                                                                  ideLotacao.fimValid.cdata,
                                                                  0, u'None')

                    if 'dadosLotacao' in dir(alteracao.dadosLotacao):
                        for dadosLotacao in alteracao.dadosLotacao:
        
                            if 'tpLotacao' in dir(dadosLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosLotacao.tpLotacao',
                                                                  dadosLotacao.tpLotacao.cdata,
                                                                  1, u'01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 21, 24, 90, 91')
        
                            if 'tpInsc' in dir(dadosLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosLotacao.tpInsc',
                                                                  dadosLotacao.tpInsc.cdata,
                                                                  0, u'1, 2, 3, 4, 5')
        
                            if 'nrInsc' in dir(dadosLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosLotacao.nrInsc',
                                                                  dadosLotacao.nrInsc.cdata,
                                                                  0, u'None')
        
                            if 'fpasLotacao' in dir(dadosLotacao.fpasLotacao):
                                for fpasLotacao in dadosLotacao.fpasLotacao:
                
                                    if 'fpas' in dir(fpasLotacao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fpasLotacao.fpas',
                                                                          fpasLotacao.fpas.cdata,
                                                                          1, u'507, 515, 523, 531, 540, 558, 566, 574, 582, 590, 604, 612, 620, 639, 647, 655, 680, 736, 744, 779, 787, 795, 825, 833, 868, 876')
                
                                    if 'codTercs' in dir(fpasLotacao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fpasLotacao.codTercs',
                                                                          fpasLotacao.codTercs.cdata,
                                                                          1, u'0000, 0001, 0002, 0003, 0004, 0008, 0016, 0032, 0064, 0067, 0071, 0075, 0079, 0099, 0115, 0128, 0131, 0256, 0259, 0512, 0515, 1024, 2048, 3072, 3139, 4096, 4099, 4163')
                
                                    if 'codTercsSusp' in dir(fpasLotacao):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fpasLotacao.codTercsSusp',
                                                                          fpasLotacao.codTercsSusp.cdata,
                                                                          0, u'0000, 0001, 0002, 0003, 0004, 0008, 0016, 0032, 0064, 0067, 0071, 0075, 0079, 0099, 0115, 0128, 0131, 0256, 0259, 0512, 0515, 1024, 2048, 3072, 3139, 4096, 4099, 4163')
                
                                    if 'infoProcJudTerceiros' in dir(fpasLotacao.infoProcJudTerceiros):
                                        for infoProcJudTerceiros in fpasLotacao.infoProcJudTerceiros:
                        
                                            if 'procJudTerceiro' in dir(infoProcJudTerceiros.procJudTerceiro):
                                                for procJudTerceiro in infoProcJudTerceiros.procJudTerceiro:
                                
                                                    if 'codTerc' in dir(procJudTerceiro):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'procJudTerceiro.codTerc',
                                                                                          procJudTerceiro.codTerc.cdata,
                                                                                          1, u'0000, 0001, 0002, 0003, 0004, 0008, 0016, 0032, 0064, 0067, 0071, 0075, 0079, 0099, 0115, 0128, 0131, 0256, 0259, 0512, 0515, 1024, 2048, 3072, 3139, 4096, 4099, 4163')
                                
                                                    if 'nrProcJud' in dir(procJudTerceiro):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'procJudTerceiro.nrProcJud',
                                                                                          procJudTerceiro.nrProcJud.cdata,
                                                                                          1, u'None')
                                
                                                    if 'codSusp' in dir(procJudTerceiro):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'procJudTerceiro.codSusp',
                                                                                          procJudTerceiro.codSusp.cdata,
                                                                                          1, u'None')
        
                            if 'infoEmprParcial' in dir(dadosLotacao.infoEmprParcial):
                                for infoEmprParcial in dadosLotacao.infoEmprParcial:
                
                                    if 'tpInscContrat' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.tpInscContrat',
                                                                          infoEmprParcial.tpInscContrat.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrInscContrat' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.nrInscContrat',
                                                                          infoEmprParcial.nrInscContrat.cdata,
                                                                          1, u'None')
                
                                    if 'tpInscProp' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.tpInscProp',
                                                                          infoEmprParcial.tpInscProp.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrInscProp' in dir(infoEmprParcial):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoEmprParcial.nrInscProp',
                                                                          infoEmprParcial.nrInscProp.cdata,
                                                                          1, u'None')

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

            if 'exclusao' in dir(infoLotacao.exclusao):
                for exclusao in infoLotacao.exclusao:

                    if 'ideLotacao' in dir(exclusao.ideLotacao):
                        for ideLotacao in exclusao.ideLotacao:
        
                            if 'codLotacao' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.codLotacao',
                                                                  ideLotacao.codLotacao.cdata,
                                                                  1, u'None')
        
                            if 'iniValid' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.iniValid',
                                                                  ideLotacao.iniValid.cdata,
                                                                  1, u'None')
        
                            if 'fimValid' in dir(ideLotacao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLotacao.fimValid',
                                                                  ideLotacao.fimValid.cdata,
                                                                  0, u'None')
    return validacoes_lista