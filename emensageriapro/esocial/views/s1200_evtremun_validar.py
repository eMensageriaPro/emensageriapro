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


def validacoes_s1200_evtremun(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtRemun = doc.eSocial.evtRemun
    #variaveis

    if 'ideEvento' in dir(evtRemun.ideEvento):
        for ideEvento in evtRemun.ideEvento:

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

    if 'ideEmpregador' in dir(evtRemun.ideEmpregador):
        for ideEmpregador in evtRemun.ideEmpregador:

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

    if 'ideTrabalhador' in dir(evtRemun.ideTrabalhador):
        for ideTrabalhador in evtRemun.ideTrabalhador:

            if 'cpfTrab' in dir(ideTrabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabalhador.cpfTrab',
                                                  ideTrabalhador.cpfTrab.cdata,
                                                  1, u'None')

            if 'nisTrab' in dir(ideTrabalhador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabalhador.nisTrab',
                                                  ideTrabalhador.nisTrab.cdata,
                                                  0, u'None')

            if 'infoMV' in dir(ideTrabalhador.infoMV):
                for infoMV in ideTrabalhador.infoMV:

                    if 'indMV' in dir(infoMV):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoMV.indMV',
                                                          infoMV.indMV.cdata,
                                                          1, u'1, 2, 3')

                    if 'remunOutrEmpr' in dir(infoMV.remunOutrEmpr):
                        for remunOutrEmpr in infoMV.remunOutrEmpr:
        
                            if 'tpInsc' in dir(remunOutrEmpr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remunOutrEmpr.tpInsc',
                                                                  remunOutrEmpr.tpInsc.cdata,
                                                                  1, u'1, 2, 3, 4, 5, 6')
        
                            if 'nrInsc' in dir(remunOutrEmpr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remunOutrEmpr.nrInsc',
                                                                  remunOutrEmpr.nrInsc.cdata,
                                                                  1, u'None')
        
                            if 'codCateg' in dir(remunOutrEmpr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remunOutrEmpr.codCateg',
                                                                  remunOutrEmpr.codCateg.cdata,
                                                                  1, u'101, 102, 103, 104, 105, 106, 107, 108, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
        
                            if 'vlrRemunOE' in dir(remunOutrEmpr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remunOutrEmpr.vlrRemunOE',
                                                                  remunOutrEmpr.vlrRemunOE.cdata,
                                                                  1, u'None')

            if 'infoComplem' in dir(ideTrabalhador.infoComplem):
                for infoComplem in ideTrabalhador.infoComplem:

                    if 'nmTrab' in dir(infoComplem):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplem.nmTrab',
                                                          infoComplem.nmTrab.cdata,
                                                          1, u'None')

                    if 'dtNascto' in dir(infoComplem):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplem.dtNascto',
                                                          infoComplem.dtNascto.cdata,
                                                          1, u'None')

                    if 'sucessaoVinc' in dir(infoComplem.sucessaoVinc):
                        for sucessaoVinc in infoComplem.sucessaoVinc:
        
                            if 'tpInscAnt' in dir(sucessaoVinc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'sucessaoVinc.tpInscAnt',
                                                                  sucessaoVinc.tpInscAnt.cdata,
                                                                  1, u'1, 2, 3, 4, 5, 6')
        
                            if 'cnpjEmpregAnt' in dir(sucessaoVinc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'sucessaoVinc.cnpjEmpregAnt',
                                                                  sucessaoVinc.cnpjEmpregAnt.cdata,
                                                                  1, u'None')
        
                            if 'matricAnt' in dir(sucessaoVinc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'sucessaoVinc.matricAnt',
                                                                  sucessaoVinc.matricAnt.cdata,
                                                                  0, u'None')
        
                            if 'dtAdm' in dir(sucessaoVinc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'sucessaoVinc.dtAdm',
                                                                  sucessaoVinc.dtAdm.cdata,
                                                                  1, u'None')
        
                            if 'observacao' in dir(sucessaoVinc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'sucessaoVinc.observacao',
                                                                  sucessaoVinc.observacao.cdata,
                                                                  0, u'None')

            if 'procJudTrab' in dir(ideTrabalhador.procJudTrab):
                for procJudTrab in ideTrabalhador.procJudTrab:

                    if 'tpTrib' in dir(procJudTrab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'procJudTrab.tpTrib',
                                                          procJudTrab.tpTrib.cdata,
                                                          1, u'1, 2, 3, 4')

                    if 'nrProcJud' in dir(procJudTrab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'procJudTrab.nrProcJud',
                                                          procJudTrab.nrProcJud.cdata,
                                                          1, u'None')

                    if 'codSusp' in dir(procJudTrab):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'procJudTrab.codSusp',
                                                          procJudTrab.codSusp.cdata,
                                                          0, u'None')

            if 'infoInterm' in dir(ideTrabalhador.infoInterm):
                for infoInterm in ideTrabalhador.infoInterm:

                    if 'qtdDiasInterm' in dir(infoInterm):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoInterm.qtdDiasInterm',
                                                          infoInterm.qtdDiasInterm.cdata,
                                                          1, u'None')

    if 'dmDev' in dir(evtRemun.dmDev):
        for dmDev in evtRemun.dmDev:

            if 'ideDmDev' in dir(dmDev):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'dmDev.ideDmDev',
                                                  dmDev.ideDmDev.cdata,
                                                  1, u'None')

            if 'codCateg' in dir(dmDev):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'dmDev.codCateg',
                                                  dmDev.codCateg.cdata,
                                                  1, u'101, 102, 103, 104, 105, 106, 107, 108, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')

            if 'infoPerApur' in dir(dmDev.infoPerApur):
                for infoPerApur in dmDev.infoPerApur:

                    if 'ideEstabLot' in dir(infoPerApur.ideEstabLot):
                        for ideEstabLot in infoPerApur.ideEstabLot:
        
                            if 'tpInsc' in dir(ideEstabLot):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstabLot.tpInsc',
                                                                  ideEstabLot.tpInsc.cdata,
                                                                  1, u'1, 2, 3, 4, 5, 6')
        
                            if 'nrInsc' in dir(ideEstabLot):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstabLot.nrInsc',
                                                                  ideEstabLot.nrInsc.cdata,
                                                                  1, u'None')
        
                            if 'codLotacao' in dir(ideEstabLot):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstabLot.codLotacao',
                                                                  ideEstabLot.codLotacao.cdata,
                                                                  1, u'None')
        
                            if 'qtdDiasAv' in dir(ideEstabLot):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstabLot.qtdDiasAv',
                                                                  ideEstabLot.qtdDiasAv.cdata,
                                                                  0, u'None')
        
                            if 'remunPerApur' in dir(ideEstabLot.remunPerApur):
                                for remunPerApur in ideEstabLot.remunPerApur:
                
                                    if 'matricula' in dir(remunPerApur):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'remunPerApur.matricula',
                                                                          remunPerApur.matricula.cdata,
                                                                          0, u'None')
                
                                    if 'indSimples' in dir(remunPerApur):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'remunPerApur.indSimples',
                                                                          remunPerApur.indSimples.cdata,
                                                                          0, u'1, 2, 3')
                
                                    if 'itensRemun' in dir(remunPerApur.itensRemun):
                                        for itensRemun in remunPerApur.itensRemun:
                        
                                            if 'codRubr' in dir(itensRemun):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'itensRemun.codRubr',
                                                                                  itensRemun.codRubr.cdata,
                                                                                  1, u'None')
                        
                                            if 'ideTabRubr' in dir(itensRemun):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'itensRemun.ideTabRubr',
                                                                                  itensRemun.ideTabRubr.cdata,
                                                                                  1, u'None')
                        
                                            if 'qtdRubr' in dir(itensRemun):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'itensRemun.qtdRubr',
                                                                                  itensRemun.qtdRubr.cdata,
                                                                                  0, u'None')
                        
                                            if 'fatorRubr' in dir(itensRemun):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'itensRemun.fatorRubr',
                                                                                  itensRemun.fatorRubr.cdata,
                                                                                  0, u'None')
                        
                                            if 'vrUnit' in dir(itensRemun):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'itensRemun.vrUnit',
                                                                                  itensRemun.vrUnit.cdata,
                                                                                  0, u'None')
                        
                                            if 'vrRubr' in dir(itensRemun):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'itensRemun.vrRubr',
                                                                                  itensRemun.vrRubr.cdata,
                                                                                  1, u'None')
                
                                    if 'infoSaudeColet' in dir(remunPerApur.infoSaudeColet):
                                        for infoSaudeColet in remunPerApur.infoSaudeColet:
                        
                                            if 'detOper' in dir(infoSaudeColet.detOper):
                                                for detOper in infoSaudeColet.detOper:
                                
                                                    if 'cnpjOper' in dir(detOper):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detOper.cnpjOper',
                                                                                          detOper.cnpjOper.cdata,
                                                                                          1, u'None')
                                
                                                    if 'regANS' in dir(detOper):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detOper.regANS',
                                                                                          detOper.regANS.cdata,
                                                                                          1, u'None')
                                
                                                    if 'vrPgTit' in dir(detOper):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detOper.vrPgTit',
                                                                                          detOper.vrPgTit.cdata,
                                                                                          1, u'None')
                                
                                                    if 'detPlano' in dir(detOper.detPlano):
                                                        for detPlano in detOper.detPlano:
                                        
                                                            if 'tpDep' in dir(detPlano):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'detPlano.tpDep',
                                                                                                  detPlano.tpDep.cdata,
                                                                                                  1, u'01, 02, 03, 04, 06, 07, 09, 10, 11, 12, 99')
                                        
                                                            if 'cpfDep' in dir(detPlano):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'detPlano.cpfDep',
                                                                                                  detPlano.cpfDep.cdata,
                                                                                                  0, u'None')
                                        
                                                            if 'nmDep' in dir(detPlano):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'detPlano.nmDep',
                                                                                                  detPlano.nmDep.cdata,
                                                                                                  1, u'None')
                                        
                                                            if 'dtNascto' in dir(detPlano):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'detPlano.dtNascto',
                                                                                                  detPlano.dtNascto.cdata,
                                                                                                  1, u'None')
                                        
                                                            if 'vlrPgDep' in dir(detPlano):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'detPlano.vlrPgDep',
                                                                                                  detPlano.vlrPgDep.cdata,
                                                                                                  1, u'None')
                
                                    if 'infoAgNocivo' in dir(remunPerApur.infoAgNocivo):
                                        for infoAgNocivo in remunPerApur.infoAgNocivo:
                        
                                            if 'grauExp' in dir(infoAgNocivo):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoAgNocivo.grauExp',
                                                                                  infoAgNocivo.grauExp.cdata,
                                                                                  1, u'1, 2, 3, 4')
                
                                    if 'infoTrabInterm' in dir(remunPerApur.infoTrabInterm):
                                        for infoTrabInterm in remunPerApur.infoTrabInterm:
                        
                                            if 'codConv' in dir(infoTrabInterm):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoTrabInterm.codConv',
                                                                                  infoTrabInterm.codConv.cdata,
                                                                                  1, u'None')

            if 'infoPerAnt' in dir(dmDev.infoPerAnt):
                for infoPerAnt in dmDev.infoPerAnt:

                    if 'ideADC' in dir(infoPerAnt.ideADC):
                        for ideADC in infoPerAnt.ideADC:
        
                            if 'dtAcConv' in dir(ideADC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideADC.dtAcConv',
                                                                  ideADC.dtAcConv.cdata,
                                                                  0, u'None')
        
                            if 'tpAcConv' in dir(ideADC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideADC.tpAcConv',
                                                                  ideADC.tpAcConv.cdata,
                                                                  1, u'A, B, C, D, E, F, G')
        
                            if 'compAcConv' in dir(ideADC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideADC.compAcConv',
                                                                  ideADC.compAcConv.cdata,
                                                                  0, u'None')
        
                            if 'dtEfAcConv' in dir(ideADC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideADC.dtEfAcConv',
                                                                  ideADC.dtEfAcConv.cdata,
                                                                  0, u'None')
        
                            if 'dsc' in dir(ideADC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideADC.dsc',
                                                                  ideADC.dsc.cdata,
                                                                  1, u'None')
        
                            if 'remunSuc' in dir(ideADC):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideADC.remunSuc',
                                                                  ideADC.remunSuc.cdata,
                                                                  1, u'S, N')
        
                            if 'idePeriodo' in dir(ideADC.idePeriodo):
                                for idePeriodo in ideADC.idePeriodo:
                
                                    if 'perRef' in dir(idePeriodo):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'idePeriodo.perRef',
                                                                          idePeriodo.perRef.cdata,
                                                                          1, u'None')
                
                                    if 'ideEstabLot' in dir(idePeriodo.ideEstabLot):
                                        for ideEstabLot in idePeriodo.ideEstabLot:
                        
                                            if 'tpInsc' in dir(ideEstabLot):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'ideEstabLot.tpInsc',
                                                                                  ideEstabLot.tpInsc.cdata,
                                                                                  1, u'1, 2, 3, 4, 5, 6')
                        
                                            if 'nrInsc' in dir(ideEstabLot):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'ideEstabLot.nrInsc',
                                                                                  ideEstabLot.nrInsc.cdata,
                                                                                  1, u'None')
                        
                                            if 'codLotacao' in dir(ideEstabLot):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'ideEstabLot.codLotacao',
                                                                                  ideEstabLot.codLotacao.cdata,
                                                                                  1, u'None')
                        
                                            if 'remunPerAnt' in dir(ideEstabLot.remunPerAnt):
                                                for remunPerAnt in ideEstabLot.remunPerAnt:
                                
                                                    if 'matricula' in dir(remunPerAnt):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'remunPerAnt.matricula',
                                                                                          remunPerAnt.matricula.cdata,
                                                                                          0, u'None')
                                
                                                    if 'indSimples' in dir(remunPerAnt):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'remunPerAnt.indSimples',
                                                                                          remunPerAnt.indSimples.cdata,
                                                                                          0, u'1, 2, 3')
                                
                                                    if 'itensRemun' in dir(remunPerAnt.itensRemun):
                                                        for itensRemun in remunPerAnt.itensRemun:
                                        
                                                            if 'codRubr' in dir(itensRemun):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'itensRemun.codRubr',
                                                                                                  itensRemun.codRubr.cdata,
                                                                                                  1, u'None')
                                        
                                                            if 'ideTabRubr' in dir(itensRemun):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'itensRemun.ideTabRubr',
                                                                                                  itensRemun.ideTabRubr.cdata,
                                                                                                  1, u'None')
                                        
                                                            if 'qtdRubr' in dir(itensRemun):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'itensRemun.qtdRubr',
                                                                                                  itensRemun.qtdRubr.cdata,
                                                                                                  0, u'None')
                                        
                                                            if 'fatorRubr' in dir(itensRemun):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'itensRemun.fatorRubr',
                                                                                                  itensRemun.fatorRubr.cdata,
                                                                                                  0, u'None')
                                        
                                                            if 'vrUnit' in dir(itensRemun):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'itensRemun.vrUnit',
                                                                                                  itensRemun.vrUnit.cdata,
                                                                                                  0, u'None')
                                        
                                                            if 'vrRubr' in dir(itensRemun):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'itensRemun.vrRubr',
                                                                                                  itensRemun.vrRubr.cdata,
                                                                                                  1, u'None')
                                
                                                    if 'infoAgNocivo' in dir(remunPerAnt.infoAgNocivo):
                                                        for infoAgNocivo in remunPerAnt.infoAgNocivo:
                                        
                                                            if 'grauExp' in dir(infoAgNocivo):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'infoAgNocivo.grauExp',
                                                                                                  infoAgNocivo.grauExp.cdata,
                                                                                                  1, u'1, 2, 3, 4')
                                
                                                    if 'infoTrabInterm' in dir(remunPerAnt.infoTrabInterm):
                                                        for infoTrabInterm in remunPerAnt.infoTrabInterm:
                                        
                                                            if 'codConv' in dir(infoTrabInterm):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'infoTrabInterm.codConv',
                                                                                                  infoTrabInterm.codConv.cdata,
                                                                                                  1, u'None')

            if 'infoComplCont' in dir(dmDev.infoComplCont):
                for infoComplCont in dmDev.infoComplCont:

                    if 'codCBO' in dir(infoComplCont):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplCont.codCBO',
                                                          infoComplCont.codCBO.cdata,
                                                          1, u'010105, 010110, 010115, 010205, 010210, 010215, 010305, 010310, 010315, 020105, 020110, 020115, 020205, 020305, 020310, 021105, 021110, 021205, 021210, 030105, 030110, 030115, 030205, 030305, 031105, 031110, 031205, 031210, 111105, 111110, 111115, 111120, 111205, 111210, 111215, 111220, 111225, 111230, 111235, 111240, 111245, 111250, 111255, 111305, 111310, 111315, 111320, 111325, 111330, 111335, 111340, 111345, 111405, 111410, 111415, 111505, 111510, 113005, 113010, 113015, 114105, 114205, 114210, 114305, 114405, 121005, 121010, 122105, 122110, 122115, 122120, 122205, 122305, 122405, 122505, 122510, 122515, 122520, 122605, 122610, 122615, 122620, 122705, 122710, 122715, 122720, 122725, 122730, 122735, 122740, 122745, 122750, 122755, 123105, 123110, 123115, 123205, 123210, 123305, 123310, 123405, 123410, 123605, 123705, 123805, 131105, 131110, 131115, 131120, 131205, 131210, 131215, 131220, 131225, 131305, 131310, 131315, 131320, 141105, 141110, 141115, 141120, 141205, 141305, 141405, 141410, 141415, 141420, 141505, 141510, 141515, 141520, 141525, 141605, 141610, 141615, 141705, 141710, 141715, 141720, 141725, 141730, 141735, 142105, 142110, 142115, 142120, 142205, 142210, 142305, 142310, 142315, 142320, 142325, 142330, 142335, 142340, 142345, 142405, 142410, 142415, 142505, 142510, 142515, 142520, 142525, 142530, 142535, 142605, 142610, 142705, 142710, 201105, 201110, 201115, 201205, 201210, 201215, 201220, 201225, 202105, 202110, 202115, 202120, 203005, 203010, 203015, 203020, 203025, 203105, 203110, 203115, 203120, 203125, 203205, 203210, 203215, 203220, 203225, 203230, 203305, 203310, 203315, 203320, 203405, 203410, 203415, 203420, 203505, 203510, 203515, 203520, 203525, 204105, 211105, 211110, 211115, 211120, 211205, 211210, 211215, 212205, 212210, 212215, 212305, 212310, 212315, 212320, 212405, 212410, 212415, 212420, 213105, 213110, 213115, 213120, 213125, 213130, 213135, 213140, 213145, 213150, 213155, 213160, 213165, 213170, 213175, 213205, 213210, 213215, 213305, 213310, 213315, 213405, 213410, 213415, 213420, 213425, 213430, 213435, 213440, 214005, 214010, 214105, 214110, 214115, 214120, 214125, 214130, 214205, 214210, 214215, 214220, 214225, 214230, 214235, 214240, 214245, 214250, 214255, 214260, 214265, 214270, 214280, 214305, 214310, 214315, 214320, 214325, 214330, 214335, 214340, 214345, 214350, 214360, 214365, 214370, 214405, 214410, 214415, 214420, 214425, 214430, 214435, 214505, 214510, 214515, 214520, 214525, 214530, 214535, 214605, 214610, 214615, 214705, 214710, 214715, 214720, 214725, 214730, 214735, 214740, 214745, 214750, 214805, 214810, 214905, 214910, 214915, 214920, 214925, 214930, 214935, 214940, 214945, 215105, 215110, 215115, 215120, 215125, 215130, 215135, 215140, 215145, 215150, 215205, 215210, 215215, 215220, 215305, 215310, 215315, 221105, 221205, 222105, 222110, 222115, 222120, 222205, 222215, 223204, 223208, 223212, 223216, 223220, 223224, 223228, 223232, 223236, 223240, 223244, 223248, 223252, 223256, 223260, 223264, 223268, 223272, 223276, 223280, 223284, 223288, 223293, 223305, 223310, 223405, 223415, 223420, 223425, 223430, 223435, 223440, 223445, 223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540, 223545, 223550, 223555, 223560, 223565, 223570, 223605, 223625, 223630, 223635, 223640, 223645, 223650, 223655, 223660, 223705, 223710, 223810, 223815, 223820, 223825, 223830, 223835, 223840, 223845, 223905, 223910, 224105, 224110, 224115, 224120, 224125, 224130, 224135, 225103, 225105, 225106, 225109, 225110, 225112, 225115, 225118, 225120, 225121, 225122, 225124, 225125, 225127, 225130, 225133, 225135, 225136, 225139, 225140, 225142, 225145, 225148, 225150, 225151, 225154, 225155, 225160, 225165, 225170, 225175, 225180, 225185, 225195, 225203, 225210, 225215, 225220, 225225, 225230, 225235, 225240, 225250, 225255, 225260, 225265, 225270, 225275, 225280, 225285, 225290, 225295, 225305, 225310, 225315, 225320, 225325, 225330, 225335, 225340, 225345, 225350, 226105, 226110, 226305, 226310, 226315, 226320, 231105, 231110, 231205, 231210, 231305, 231310, 231315, 231320, 231325, 231330, 231335, 231340, 232105, 232110, 232115, 232120, 232125, 232130, 232135, 232140, 232145, 232150, 232155, 232160, 232165, 232170, 233105, 233110, 233115, 233120, 233125, 233130, 233135, 233205, 233210, 233215, 233220, 233225, 234105, 234110, 234115, 234120, 234125, 234205, 234210, 234215, 234305, 234310, 234315, 234320, 234405, 234410, 234415, 234420, 234425, 234430, 234435, 234440, 234445, 234450, 234455, 234460, 234505, 234510, 234515, 234520, 234604, 234608, 234612, 234616, 234620, 234624, 234628, 234632, 234636, 234640, 234644, 234648, 234652, 234656, 234660, 234664, 234668, 234672, 234676, 234680, 234684, 234705, 234710, 234715, 234720, 234725, 234730, 234735, 234740, 234745, 234750, 234755, 234760, 234765, 234770, 234805, 234810, 234815, 234905, 234910, 234915, 239205, 239210, 239215, 239220, 239225, 239405, 239410, 239415, 239420, 239425, 239430, 239435, 241005, 241010, 241015, 241020, 241025, 241030, 241035, 241040, 241205, 241210, 241215, 241220, 241225, 241230, 241235, 241305, 241310, 241315, 241320, 241325, 241330, 241335, 241340, 242205, 242210, 242215, 242220, 242225, 242230, 242235, 242240, 242245, 242250, 242305, 242405, 242410, 242905, 242910, 251105, 251110, 251115, 251120, 251205, 251210, 251215, 251220, 251225, 251230, 251235, 251305, 251405, 251505, 251510, 251515, 251520, 251525, 251530, 251535, 251540, 251545, 251550, 251555, 251605, 251610, 252105, 252205, 252210, 252215, 252305, 252310, 252315, 252320, 252405, 252505, 252510, 252515, 252525, 252530, 252535, 252540, 252545, 252550, 252605, 252705, 252710, 252715, 252720, 252725, 253110, 253115, 253120, 253125, 253130, 253135, 253140, 253205, 253210, 253215, 253220, 253225, 253305, 254105, 254110, 254205, 254305, 254310, 254405, 254410, 254415, 254420, 254505, 261105, 261110, 261115, 261120, 261125, 261130, 261135, 261140, 261205, 261210, 261215, 261305, 261310, 261405, 261410, 261415, 261420, 261425, 261430, 261505, 261510, 261515, 261520, 261525, 261530, 261605, 261610, 261615, 261620, 261625, 261705, 261705, 261710, 261710, 261715, 261715, 261720, 261725, 261730, 261730, 261805, 261810, 261815, 261820, 261905, 261910, 262105, 262110, 262115, 262120, 262125, 262130, 262135, 262205, 262210, 262215, 262220, 262225, 262230, 262235, 262305, 262310, 262315, 262320, 262325, 262330, 262405, 262410, 262415, 262420, 262425, 262505, 262605, 262610, 262615, 262620, 262705, 262710, 262805, 262810, 262815, 262820, 262825, 262830, 262905, 263105, 263110, 263115, 271105, 271110, 300105, 300110, 300305, 301105, 301110, 301115, 301205, 311105, 311110, 311115, 311205, 311305, 311405, 311410, 311505, 311510, 311515, 311520, 311605, 311610, 311615, 311620, 311625, 311705, 311710, 311715, 311720, 311725, 312105, 312205, 312210, 312305, 312310, 312315, 312320, 313105, 313110, 313115, 313120, 313125, 313130, 313205, 313210, 313215, 313220, 313305, 313310, 313315, 313320, 313405, 313410, 313415, 313505, 314105, 314110, 314115, 314120, 314125, 314205, 314210, 314305, 314310, 314315, 314405, 314410, 314605, 314610, 314615, 314620, 314625, 314705, 314710, 314715, 314720, 314725, 314730, 316105, 316110, 316115, 316120, 316305, 316310, 316315, 316320, 316325, 316330, 316335, 316340, 317105, 317110, 317115, 317120, 317205, 317210, 318005, 318010, 318015, 318105, 318110, 318115, 318120, 318205, 318210, 318215, 318305, 318310, 318405, 318410, 318415, 318420, 318425, 318430, 318505, 318510, 318605, 318610, 318705, 318710, 318805, 318810, 318815, 319105, 319110, 319205, 320105, 320110, 321105, 321110, 321205, 321210, 321305, 321310, 321315, 321320, 322105, 322110, 322115, 322120, 322125, 322130, 322135, 322205, 322210, 322215, 322220, 322225, 322230, 322235, 322240, 322245, 322250, 322305, 322405, 322410, 322415, 322420, 322425, 322430, 322505, 322605, 323105, 324105, 324110, 324115, 324120, 324125, 324130, 324205, 324215, 324220, 325005, 325010, 325015, 325105, 325110, 325115, 325205, 325210, 325305, 325310, 328105, 328110, 331105, 331110, 331205, 331305, 332105, 332205, 333105, 333110, 333115, 334105, 334110, 334115, 341105, 341110, 341115, 341120, 341205, 341210, 341215, 341220, 341225, 341230, 341235, 341240, 341245, 341250, 341305, 341310, 341315, 341320, 341325, 342105, 342110, 342115, 342120, 342125, 342205, 342210, 342215, 342305, 342310, 342315, 342405, 342410, 342505, 342510, 342515, 342520, 342525, 342530, 342535, 342540, 342545, 342550, 342605, 342610, 351105, 351110, 351115, 351305, 351310, 351315, 351405, 351410, 351415, 351420, 351425, 351430, 351505, 351510, 351515, 351605, 351610, 351705, 351710, 351715, 351720, 351725, 351730, 351735, 351740, 351805, 351810, 351815, 351905, 351910, 352205, 352210, 352305, 352310, 352315, 352320, 352405, 352410, 352420, 353205, 353210, 353215, 353220, 353225, 353230, 353235, 354120, 354125, 354130, 354135, 354140, 354145, 354150, 354205, 354210, 354305, 354405, 354410, 354415, 354505, 354605, 354705, 354805, 354810, 354815, 354820, 354825, 371105, 371110, 371205, 371210, 371305, 371310, 371405, 371410, 372105, 372110, 372115, 372205, 372210, 373105, 373105, 373110, 373115, 373120, 373125, 373130, 373135, 373140, 373145, 373205, 373210, 373215, 373220, 373225, 373230, 374105, 374110, 374115, 374120, 374125, 374130, 374135, 374140, 374145, 374150, 374155, 374205, 374210, 374215, 374305, 374310, 374405, 374405, 374410, 374415, 374420, 374425, 375105, 375110, 375115, 375120, 376105, 376110, 376205, 376210, 376215, 376220, 376225, 376230, 376235, 376240, 376245, 376250, 376255, 376305, 376310, 376315, 376320, 376325, 376330, 376405, 376410, 376415, 377105, 377110, 377115, 377120, 377125, 377130, 377135, 377140, 377145, 377205, 377210, 377215, 377220, 377225, 377230, 377235, 377240, 377245, 391105, 391110, 391115, 391120, 391125, 391130, 391135, 391205, 391210, 391215, 391220, 391225, 391230, 395105, 395110, 410105, 410205, 410210, 410215, 410220, 410225, 410230, 410235, 410240, 411005, 411010, 411015, 411020, 411025, 411030, 411035, 411040, 411045, 411050, 412105, 412110, 412115, 412120, 412205, 413105, 413110, 413115, 413205, 413210, 413215, 413220, 413225, 413230, 414105, 414110, 414115, 414120, 414125, 414135, 414140, 414205, 414210, 414215, 415105, 415115, 415120, 415125, 415130, 415205, 415210, 415215, 415305, 420105, 420110, 420115, 420120, 420125, 420130, 420135, 421105, 421110, 421115, 421120, 421125, 421205, 421210, 421305, 421310, 421315, 422105, 422110, 422115, 422120, 422125, 422130, 422205, 422210, 422215, 422220, 422305, 422310, 422315, 422320, 423105, 423110, 424105, 424110, 424115, 424120, 424125, 424130, 424205, 424210, 510105, 510110, 510115, 510120, 510130, 510135, 510205, 510305, 510310, 511105, 511110, 511115, 511205, 511210, 511215, 511220, 511405, 511505, 511510, 512105, 512110, 512115, 512120, 513105, 513110, 513115, 513205, 513210, 513215, 513220, 513225, 513305, 513310, 513315, 513320, 513325, 513405, 513410, 513415, 513420, 513425, 513430, 513435, 513440, 513505, 513605, 513610, 513615, 514105, 514110, 514115, 514120, 514205, 514215, 514225, 514230, 514305, 514310, 514315, 514320, 514325, 514330, 515105, 515110, 515115, 515120, 515125, 515130, 515135, 515140, 515205, 515210, 515215, 515220, 515225, 515305, 515310, 515315, 515320, 515325, 515330, 516105, 516110, 516120, 516125, 516130, 516140, 516205, 516210, 516215, 516220, 516305, 516310, 516315, 516320, 516325, 516330, 516335, 516340, 516345, 516405, 516410, 516415, 516505, 516605, 516610, 516705, 516710, 516805, 516810, 517105, 517110, 517115, 517205, 517210, 517215, 517220, 517225, 517305, 517310, 517315, 517320, 517325, 517330, 517335, 517405, 517410, 517415, 517420, 517425, 519105, 519110, 519115, 519205, 519210, 519215, 519305, 519310, 519315, 519320, 519805, 519905, 519910, 519915, 519920, 519925, 519930, 519935, 519940, 519945, 520105, 520110, 521105, 521110, 521115, 521120, 521125, 521130, 521135, 521140, 523105, 523110, 523115, 524105, 524205, 524210, 524215, 524305, 524310, 524315, 611005, 612005, 612105, 612110, 612115, 612120, 612125, 612205, 612210, 612215, 612220, 612225, 612305, 612310, 612315, 612320, 612405, 612410, 612415, 612420, 612505, 612510, 612515, 612605, 612610, 612615, 612620, 612625, 612705, 612710, 612715, 612720, 612725, 612730, 612735, 612740, 612805, 612810, 613005, 613010, 613105, 613110, 613115, 613120, 613125, 613130, 613205, 613210, 613215, 613305, 613310, 613405, 613410, 613415, 613420, 620105, 620110, 620115, 621005, 622005, 622010, 622015, 622020, 622105, 622110, 622115, 622120, 622205, 622210, 622215, 622305, 622310, 622315, 622320, 622405, 622410, 622415, 622420, 622425, 622505, 622510, 622515, 622605, 622610, 622615, 622620, 622625, 622705, 622710, 622715, 622720, 622725, 622730, 622735, 622740, 622805, 622810, 623005, 623010, 623015, 623020, 623025, 623030, 623105, 623110, 623115, 623120, 623125, 623205, 623210, 623215, 623305, 623310, 623315, 623320, 623325, 623405, 623410, 623415, 623420, 630105, 630110, 631005, 631010, 631015, 631020, 631105, 631205, 631210, 631305, 631310, 631315, 631320, 631325, 631330, 631335, 631405, 631410, 631415, 631420, 632005, 632010, 632015, 632105, 632110, 632115, 632120, 632125, 632205, 632210, 632215, 632305, 632310, 632315, 632320, 632325, 632330, 632335, 632340, 632345, 632350, 632355, 632360, 632365, 632370, 632405, 632410, 632415, 632420, 632505, 632510, 632515, 632520, 632525, 632605, 632610, 632615, 641005, 641010, 641015, 642005, 642010, 642015, 643005, 643010, 643015, 643020, 643025, 710105, 710110, 710115, 710120, 710125, 710205, 710210, 710215, 710220, 710225, 711105, 711110, 711115, 711120, 711125, 711130, 711205, 711210, 711215, 711220, 711225, 711230, 711235, 711240, 711245, 711305, 711310, 711315, 711320, 711325, 711330, 711405, 711410, 712105, 712110, 712115, 712120, 712125, 712130, 712135, 712205, 712210, 712215, 712220, 712225, 712230, 715105, 715110, 715115, 715120, 715125, 715130, 715135, 715140, 715145, 715205, 715210, 715215, 715220, 715225, 715230, 715305, 715310, 715315, 715405, 715410, 715415, 715505, 715510, 715515, 715520, 715525, 715530, 715535, 715540, 715545, 715605, 715610, 715615, 715705, 715710, 715715, 715720, 715725, 715730, 716105, 716110, 716205, 716210, 716215, 716220, 716305, 716310, 716315, 716405, 716505, 716510, 716510, 716515, 716520, 716525, 716530, 716535, 716540, 716605, 716610, 716615, 717005, 717010, 717015, 717020, 717025, 720105, 720110, 720115, 720120, 720125, 720130, 720135, 720140, 720145, 720150, 720155, 720160, 720205, 720210, 720215, 720220, 721105, 721110, 721115, 721205, 721210, 721215, 721220, 721225, 721305, 721310, 721315, 721320, 721325, 721405, 721410, 721415, 721420, 721425, 721430, 722105, 722110, 722115, 722205, 722210, 722215, 722220, 722225, 722230, 722235, 722305, 722310, 722315, 722320, 722325, 722330, 722405, 722410, 722415, 723105, 723110, 723115, 723120, 723125, 723205, 723210, 723215, 723220, 723225, 723230, 723235, 723240, 723305, 723310, 723315, 723320, 723325, 723330, 724105, 724110, 724115, 724120, 724125, 724130, 724135, 724205, 724210, 724215, 724220, 724225, 724230, 724305, 724310, 724315, 724320, 724325, 724405, 724410, 724415, 724420, 724425, 724430, 724435, 724440, 724505, 724510, 724515, 724605, 724610, 725005, 725010, 725015, 725020, 725025, 725105, 725205, 725210, 725215, 725220, 725225, 725305, 725310, 725315, 725320, 725405, 725410, 725415, 725420, 725505, 725510, 725605, 725610, 725705, 730105, 731105, 731110, 731115, 731120, 731125, 731130, 731135, 731140, 731145, 731150, 731155, 731160, 731165, 731170, 731175, 731180, 731205, 731305, 731310, 731315, 731320, 731325, 731330, 732105, 732110, 732115, 732120, 732125, 732130, 732135, 732140, 740105, 740110, 741105, 741110, 741115, 741120, 741125, 742105, 742110, 742115, 742120, 742125, 742130, 742135, 742140, 750105, 750205, 751005, 751010, 751015, 751020, 751105, 751110, 751115, 751120, 751125, 751130, 752105, 752110, 752115, 752120, 752205, 752210, 752215, 752220, 752225, 752230, 752235, 752305, 752310, 752315, 752320, 752325, 752330, 752405, 752410, 752415, 752420, 752425, 752430, 760105, 760110, 760115, 760120, 760125, 760205, 760305, 760310, 760405, 760505, 760605, 761005, 761105, 761110, 761205, 761210, 761215, 761220, 761225, 761230, 761235, 761240, 761245, 761250, 761255, 761260, 761303, 761306, 761309, 761312, 761315, 761318, 761321, 761324, 761327, 761330, 761333, 761336, 761339, 761342, 761345, 761348, 761351, 761354, 761357, 761360, 761363, 761366, 761405, 761410, 761415, 761420, 761425, 761430, 761435, 761805, 761810, 761815, 761820, 762005, 762105, 762110, 762115, 762120, 762125, 762205, 762210, 762215, 762220, 762305, 762310, 762315, 762320, 762325, 762330, 762335, 762340, 762345, 763005, 763010, 763015, 763020, 763105, 763110, 763115, 763120, 763125, 763205, 763210, 763215, 763305, 763310, 763315, 763320, 763325, 764005, 764105, 764110, 764115, 764120, 764205, 764210, 764305, 765005, 765010, 765015, 765105, 765110, 765205, 765215, 765225, 765230, 765235, 765240, 765310, 765315, 765405, 766105, 766115, 766120, 766125, 766130, 766135, 766140, 766145, 766150, 766155, 766205, 766210, 766215, 766220, 766225, 766230, 766235, 766240, 766245, 766250, 766305, 766310, 766315, 766320, 766325, 766405, 766410, 766415, 766420, 768105, 768110, 768115, 768120, 768125, 768130, 768205, 768210, 768305, 768310, 768315, 768320, 768325, 768605, 768610, 768615, 768620, 768625, 768630, 768705, 768710, 770105, 770110, 771105, 771110, 771115, 771120, 772105, 772110, 772115, 773105, 773110, 773115, 773120, 773125, 773130, 773205, 773210, 773215, 773220, 773305, 773310, 773315, 773320, 773325, 773330, 773335, 773340, 773345, 773350, 773355, 773405, 773410, 773415, 773420, 773505, 773510, 774105, 775105, 775110, 775115, 775120, 776405, 776410, 776415, 776420, 776425, 776430, 777105, 777110, 777115, 777205, 777210, 780105, 781105, 781110, 781305, 781705, 782105, 782110, 782115, 782120, 782125, 782130, 782135, 782140, 782145, 782205, 782210, 782220, 782305, 782310, 782315, 782320, 782405, 782410, 782415, 782505, 782510, 782515, 782605, 782610, 782615, 782620, 782625, 782630, 782705, 782710, 782715, 782720, 782725, 782730, 782735, 782805, 782810, 782815, 782820, 783105, 783110, 783205, 783210, 783215, 783220, 783225, 783230, 783235, 783240, 784105, 784110, 784115, 784120, 784125, 784205, 791105, 791110, 791115, 791120, 791125, 791130, 791135, 791140, 791145, 791150, 791155, 791160, 810105, 810110, 810205, 810305, 811005, 811010, 811105, 811110, 811115, 811120, 811125, 811130, 811205, 811215, 811305, 811310, 811315, 811320, 811325, 811330, 811335, 811405, 811410, 811415, 811420, 811425, 811430, 811505, 811510, 811605, 811610, 811615, 811620, 811625, 811630, 811635, 811640, 811645, 811650, 811705, 811710, 811715, 811725, 811735, 811745, 811750, 811760, 811770, 811775, 811805, 811810, 811815, 811820, 812105, 812110, 813105, 813110, 813115, 813120, 813125, 813130, 818105, 818110, 820105, 820110, 820115, 820120, 820125, 820205, 820210, 821105, 821110, 821205, 821210, 821215, 821220, 821225, 821230, 821235, 821240, 821245, 821250, 821255, 821305, 821310, 821315, 821320, 821325, 821330, 821335, 821405, 821410, 821415, 821420, 821425, 821430, 821435, 821440, 821445, 821450, 822105, 822110, 822115, 822120, 822125, 823105, 823110, 823115, 823120, 823125, 823130, 823135, 823210, 823215, 823220, 823230, 823235, 823240, 823245, 823250, 823255, 823265, 823305, 823315, 823320, 823325, 823330, 828105, 828110, 830105, 831105, 831110, 831115, 831120, 831125, 832105, 832110, 832115, 832120, 832125, 832135, 833105, 833110, 833115, 833120, 833125, 833205, 840105, 840110, 840115, 840120, 841105, 841110, 841115, 841205, 841210, 841305, 841310, 841315, 841320, 841408, 841416, 841420, 841428, 841432, 841440, 841444, 841448, 841456, 841460, 841464, 841468, 841472, 841476, 841484, 841505, 841605, 841610, 841615, 841620, 841625, 841630, 841705, 841710, 841715, 841720, 841725, 841730, 841735, 841740, 841745, 841805, 841810, 841815, 842105, 842110, 842115, 842120, 842125, 842135, 842205, 842210, 842215, 842220, 842225, 842230, 842235, 848105, 848110, 848115, 848205, 848210, 848215, 848305, 848310, 848315, 848325, 848405, 848410, 848415, 848420, 848425, 848505, 848510, 848515, 848520, 848525, 848605, 860105, 860110, 860115, 861105, 861110, 861115, 861120, 861205, 862105, 862110, 862115, 862120, 862130, 862140, 862150, 862155, 862160, 862205, 862305, 862310, 862405, 862505, 862510, 862515, 910105, 910110, 910115, 910120, 910125, 910130, 910205, 910210, 910905, 910910, 911105, 911110, 911115, 911120, 911125, 911130, 911135, 911205, 911305, 911310, 911315, 911320, 911325, 913105, 913110, 913115, 913120, 914105, 914110, 914205, 914305, 914405, 914410, 914415, 914420, 914425, 915105, 915110, 915115, 915205, 915210, 915215, 915305, 915405, 919105, 919110, 919115, 919205, 919305, 919310, 919315, 950105, 950110, 950205, 950305, 951105, 951305, 951310, 951315, 951320, 953105, 953110, 953115, 954105, 954110, 954115, 954120, 954125, 954205, 954210, 954305, 991105, 991110, 991115, 991120, 991205, 991305, 991310, 991315, 992105, 992110, 992115, 992120, 992205, 992210, 992215, 992220, 992225')

                    if 'natAtividade' in dir(infoComplCont):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplCont.natAtividade',
                                                          infoComplCont.natAtividade.cdata,
                                                          0, u'1, 2')

                    if 'qtdDiasTrab' in dir(infoComplCont):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoComplCont.qtdDiasTrab',
                                                          infoComplCont.qtdDiasTrab.cdata,
                                                          0, u'None')
    return validacoes_lista