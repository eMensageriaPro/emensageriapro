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
                                                  1, u'1, 2, 3, 4, 5')
            
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
                                                                  1, u'1, 2, 3, 4, 5')
                            
                            if 'nrInsc' in dir(remunOutrEmpr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remunOutrEmpr.nrInsc', 
                                                                  remunOutrEmpr.nrInsc.cdata, 
                                                                  1, u'None')
                            
                            if 'codCateg' in dir(remunOutrEmpr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remunOutrEmpr.codCateg', 
                                                                  remunOutrEmpr.codCateg.cdata, 
                                                                  1, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
                            
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
                                                                  1, u'1, 2, 3, 4, 5')
                            
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
                                                  1, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
            
            if 'infoPerApur' in dir(dmDev.infoPerApur):
                for infoPerApur in dmDev.infoPerApur:
                    
                    if 'ideEstabLot' in dir(infoPerApur.ideEstabLot):
                        for ideEstabLot in infoPerApur.ideEstabLot:
                            
                            if 'tpInsc' in dir(ideEstabLot):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideEstabLot.tpInsc', 
                                                                  ideEstabLot.tpInsc.cdata, 
                                                                  1, u'1, 2, 3, 4, 5')
                            
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
                                                                  1, u'A, B, C, D, E, F')
                            
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
                                                                                  1, u'1, 2, 3, 4, 5')
                                            
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
                                                          1, u'None')
                    
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