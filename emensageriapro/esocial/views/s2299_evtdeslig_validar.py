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


def validacoes_s2299_evtdeslig(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtDeslig = doc.eSocial.evtDeslig
    #variaveis

    if 'ideEvento' in dir(evtDeslig.ideEvento):
        for ideEvento in evtDeslig.ideEvento:

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

    if 'ideEmpregador' in dir(evtDeslig.ideEmpregador):
        for ideEmpregador in evtDeslig.ideEmpregador:

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

    if 'ideVinculo' in dir(evtDeslig.ideVinculo):
        for ideVinculo in evtDeslig.ideVinculo:

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

    if 'infoDeslig' in dir(evtDeslig.infoDeslig):
        for infoDeslig in evtDeslig.infoDeslig:

            if 'mtvDeslig' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.mtvDeslig',
                                                  infoDeslig.mtvDeslig.cdata,
                                                  1, u'01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36')

            if 'dtDeslig' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.dtDeslig',
                                                  infoDeslig.dtDeslig.cdata,
                                                  1, u'None')

            if 'indPagtoAPI' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.indPagtoAPI',
                                                  infoDeslig.indPagtoAPI.cdata,
                                                  1, u'S, N')

            if 'dtProjFimAPI' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.dtProjFimAPI',
                                                  infoDeslig.dtProjFimAPI.cdata,
                                                  0, u'None')

            if 'pensAlim' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.pensAlim',
                                                  infoDeslig.pensAlim.cdata,
                                                  1, u'0, 1, 2, 3')

            if 'percAliment' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.percAliment',
                                                  infoDeslig.percAliment.cdata,
                                                  0, u'None')

            if 'vrAlim' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.vrAlim',
                                                  infoDeslig.vrAlim.cdata,
                                                  0, u'None')

            if 'nrCertObito' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.nrCertObito',
                                                  infoDeslig.nrCertObito.cdata,
                                                  0, u'None')

            if 'nrProcTrab' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.nrProcTrab',
                                                  infoDeslig.nrProcTrab.cdata,
                                                  0, u'None')

            if 'indCumprParc' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.indCumprParc',
                                                  infoDeslig.indCumprParc.cdata,
                                                  1, u'0, 1, 2, 3, 4')

            if 'qtdDiasInterm' in dir(infoDeslig):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoDeslig.qtdDiasInterm',
                                                  infoDeslig.qtdDiasInterm.cdata,
                                                  0, u'None')

            if 'observacoes' in dir(infoDeslig.observacoes):
                for observacoes in infoDeslig.observacoes:

                    if 'observacao' in dir(observacoes):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'observacoes.observacao',
                                                          observacoes.observacao.cdata,
                                                          1, u'None')

            if 'sucessaoVinc' in dir(infoDeslig.sucessaoVinc):
                for sucessaoVinc in infoDeslig.sucessaoVinc:

                    if 'tpInscSuc' in dir(sucessaoVinc):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'sucessaoVinc.tpInscSuc',
                                                          sucessaoVinc.tpInscSuc.cdata,
                                                          1, u'1, 2, 3, 4, 5')

                    if 'cnpjSucessora' in dir(sucessaoVinc):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'sucessaoVinc.cnpjSucessora',
                                                          sucessaoVinc.cnpjSucessora.cdata,
                                                          1, u'None')

            if 'transfTit' in dir(infoDeslig.transfTit):
                for transfTit in infoDeslig.transfTit:

                    if 'cpfSubstituto' in dir(transfTit):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'transfTit.cpfSubstituto',
                                                          transfTit.cpfSubstituto.cdata,
                                                          1, u'None')

                    if 'dtNascto' in dir(transfTit):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'transfTit.dtNascto',
                                                          transfTit.dtNascto.cdata,
                                                          1, u'None')

            if 'mudancaCPF' in dir(infoDeslig.mudancaCPF):
                for mudancaCPF in infoDeslig.mudancaCPF:

                    if 'novoCPF' in dir(mudancaCPF):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'mudancaCPF.novoCPF',
                                                          mudancaCPF.novoCPF.cdata,
                                                          1, u'None')

            if 'verbasResc' in dir(infoDeslig.verbasResc):
                for verbasResc in infoDeslig.verbasResc:

                    if 'dmDev' in dir(verbasResc.dmDev):
                        for dmDev in verbasResc.dmDev:
        
                            if 'ideDmDev' in dir(dmDev):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dmDev.ideDmDev',
                                                                  dmDev.ideDmDev.cdata,
                                                                  1, u'None')
        
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
                        
                                            if 'detVerbas' in dir(ideEstabLot.detVerbas):
                                                for detVerbas in ideEstabLot.detVerbas:
                                
                                                    if 'codRubr' in dir(detVerbas):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detVerbas.codRubr',
                                                                                          detVerbas.codRubr.cdata,
                                                                                          1, u'None')
                                
                                                    if 'ideTabRubr' in dir(detVerbas):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detVerbas.ideTabRubr',
                                                                                          detVerbas.ideTabRubr.cdata,
                                                                                          1, u'None')
                                
                                                    if 'qtdRubr' in dir(detVerbas):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detVerbas.qtdRubr',
                                                                                          detVerbas.qtdRubr.cdata,
                                                                                          0, u'None')
                                
                                                    if 'fatorRubr' in dir(detVerbas):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detVerbas.fatorRubr',
                                                                                          detVerbas.fatorRubr.cdata,
                                                                                          0, u'None')
                                
                                                    if 'vrUnit' in dir(detVerbas):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detVerbas.vrUnit',
                                                                                          detVerbas.vrUnit.cdata,
                                                                                          0, u'None')
                                
                                                    if 'vrRubr' in dir(detVerbas):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'detVerbas.vrRubr',
                                                                                          detVerbas.vrRubr.cdata,
                                                                                          1, u'None')
                        
                                            if 'infoSaudeColet' in dir(ideEstabLot.infoSaudeColet):
                                                for infoSaudeColet in ideEstabLot.infoSaudeColet:
                                
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
                        
                                            if 'infoAgNocivo' in dir(ideEstabLot.infoAgNocivo):
                                                for infoAgNocivo in ideEstabLot.infoAgNocivo:
                                
                                                    if 'grauExp' in dir(infoAgNocivo):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoAgNocivo.grauExp',
                                                                                          infoAgNocivo.grauExp.cdata,
                                                                                          1, u'1, 2, 3, 4')
                        
                                            if 'infoSimples' in dir(ideEstabLot.infoSimples):
                                                for infoSimples in ideEstabLot.infoSimples:
                                
                                                    if 'indSimples' in dir(infoSimples):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'infoSimples.indSimples',
                                                                                          infoSimples.indSimples.cdata,
                                                                                          1, u'1, 2, 3')
        
                            if 'infoPerAnt' in dir(dmDev.infoPerAnt):
                                for infoPerAnt in dmDev.infoPerAnt:
                
                                    if 'ideADC' in dir(infoPerAnt.ideADC):
                                        for ideADC in infoPerAnt.ideADC:
                        
                                            if 'dtAcConv' in dir(ideADC):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'ideADC.dtAcConv',
                                                                                  ideADC.dtAcConv.cdata,
                                                                                  1, u'None')
                        
                                            if 'tpAcConv' in dir(ideADC):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'ideADC.tpAcConv',
                                                                                  ideADC.tpAcConv.cdata,
                                                                                  1, u'A, B, C, D, E')
                        
                                            if 'compAcConv' in dir(ideADC):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'ideADC.compAcConv',
                                                                                  ideADC.compAcConv.cdata,
                                                                                  0, u'None')
                        
                                            if 'dtEfAcConv' in dir(ideADC):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'ideADC.dtEfAcConv',
                                                                                  ideADC.dtEfAcConv.cdata,
                                                                                  1, u'None')
                        
                                            if 'dsc' in dir(ideADC):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'ideADC.dsc',
                                                                                  ideADC.dsc.cdata,
                                                                                  1, u'None')
                        
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
                                        
                                                            if 'detVerbas' in dir(ideEstabLot.detVerbas):
                                                                for detVerbas in ideEstabLot.detVerbas:
                                                
                                                                    if 'codRubr' in dir(detVerbas):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'detVerbas.codRubr',
                                                                                                          detVerbas.codRubr.cdata,
                                                                                                          1, u'None')
                                                
                                                                    if 'ideTabRubr' in dir(detVerbas):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'detVerbas.ideTabRubr',
                                                                                                          detVerbas.ideTabRubr.cdata,
                                                                                                          1, u'None')
                                                
                                                                    if 'qtdRubr' in dir(detVerbas):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'detVerbas.qtdRubr',
                                                                                                          detVerbas.qtdRubr.cdata,
                                                                                                          0, u'None')
                                                
                                                                    if 'fatorRubr' in dir(detVerbas):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'detVerbas.fatorRubr',
                                                                                                          detVerbas.fatorRubr.cdata,
                                                                                                          0, u'None')
                                                
                                                                    if 'vrUnit' in dir(detVerbas):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'detVerbas.vrUnit',
                                                                                                          detVerbas.vrUnit.cdata,
                                                                                                          0, u'None')
                                                
                                                                    if 'vrRubr' in dir(detVerbas):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'detVerbas.vrRubr',
                                                                                                          detVerbas.vrRubr.cdata,
                                                                                                          1, u'None')
                                        
                                                            if 'infoAgNocivo' in dir(ideEstabLot.infoAgNocivo):
                                                                for infoAgNocivo in ideEstabLot.infoAgNocivo:
                                                
                                                                    if 'grauExp' in dir(infoAgNocivo):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'infoAgNocivo.grauExp',
                                                                                                          infoAgNocivo.grauExp.cdata,
                                                                                                          1, u'1, 2, 3, 4')
                                        
                                                            if 'infoSimples' in dir(ideEstabLot.infoSimples):
                                                                for infoSimples in ideEstabLot.infoSimples:
                                                
                                                                    if 'indSimples' in dir(infoSimples):
                                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                                          'infoSimples.indSimples',
                                                                                                          infoSimples.indSimples.cdata,
                                                                                                          1, u'1, 2, 3')
        
                            if 'infoTrabInterm' in dir(dmDev.infoTrabInterm):
                                for infoTrabInterm in dmDev.infoTrabInterm:
                
                                    if 'codConv' in dir(infoTrabInterm):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoTrabInterm.codConv',
                                                                          infoTrabInterm.codConv.cdata,
                                                                          1, u'None')

                    if 'procJudTrab' in dir(verbasResc.procJudTrab):
                        for procJudTrab in verbasResc.procJudTrab:
        
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

                    if 'infoMV' in dir(verbasResc.infoMV):
                        for infoMV in verbasResc.infoMV:
        
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

                    if 'procCS' in dir(verbasResc.procCS):
                        for procCS in verbasResc.procCS:
        
                            if 'nrProcJud' in dir(procCS):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'procCS.nrProcJud',
                                                                  procCS.nrProcJud.cdata,
                                                                  1, u'None')

            if 'quarentena' in dir(infoDeslig.quarentena):
                for quarentena in infoDeslig.quarentena:

                    if 'dtFimQuar' in dir(quarentena):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'quarentena.dtFimQuar',
                                                          quarentena.dtFimQuar.cdata,
                                                          1, u'None')

            if 'consigFGTS' in dir(infoDeslig.consigFGTS):
                for consigFGTS in infoDeslig.consigFGTS:

                    if 'insConsig' in dir(consigFGTS):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'consigFGTS.insConsig',
                                                          consigFGTS.insConsig.cdata,
                                                          1, u'None')

                    if 'nrContr' in dir(consigFGTS):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'consigFGTS.nrContr',
                                                          consigFGTS.nrContr.cdata,
                                                          1, u'None')
    return validacoes_lista