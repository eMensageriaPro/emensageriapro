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


def validacoes_s2399_evttsvtermino(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTSVTermino = doc.eSocial.evtTSVTermino
    #variaveis
    
    if 'ideEvento' in dir(evtTSVTermino.ideEvento):
        for ideEvento in evtTSVTermino.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtTSVTermino.ideEmpregador):
        for ideEmpregador in evtTSVTermino.ideEmpregador:
            
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
    
    if 'ideTrabSemVinculo' in dir(evtTSVTermino.ideTrabSemVinculo):
        for ideTrabSemVinculo in evtTSVTermino.ideTrabSemVinculo:
            
            if 'cpfTrab' in dir(ideTrabSemVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabSemVinculo.cpfTrab', 
                                                  ideTrabSemVinculo.cpfTrab.cdata, 
                                                  1, u'None')
            
            if 'nisTrab' in dir(ideTrabSemVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabSemVinculo.nisTrab', 
                                                  ideTrabSemVinculo.nisTrab.cdata, 
                                                  0, u'None')
            
            if 'codCateg' in dir(ideTrabSemVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideTrabSemVinculo.codCateg', 
                                                  ideTrabSemVinculo.codCateg.cdata, 
                                                  1, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
    
    if 'infoTSVTermino' in dir(evtTSVTermino.infoTSVTermino):
        for infoTSVTermino in evtTSVTermino.infoTSVTermino:
            
            if 'dtTerm' in dir(infoTSVTermino):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVTermino.dtTerm', 
                                                  infoTSVTermino.dtTerm.cdata, 
                                                  1, u'None')
            
            if 'mtvDesligTSV' in dir(infoTSVTermino):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVTermino.mtvDesligTSV', 
                                                  infoTSVTermino.mtvDesligTSV.cdata, 
                                                  0, u'01, 02, 03, 04, 05, 06, 07, 99')
            
            if 'pensAlim' in dir(infoTSVTermino):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVTermino.pensAlim', 
                                                  infoTSVTermino.pensAlim.cdata, 
                                                  0, u'0, 1, 2, 3')
            
            if 'percAliment' in dir(infoTSVTermino):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVTermino.percAliment', 
                                                  infoTSVTermino.percAliment.cdata, 
                                                  0, u'None')
            
            if 'vrAlim' in dir(infoTSVTermino):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTSVTermino.vrAlim', 
                                                  infoTSVTermino.vrAlim.cdata, 
                                                  0, u'None')
            
            if 'mudancaCPF' in dir(infoTSVTermino.mudancaCPF):
                for mudancaCPF in infoTSVTermino.mudancaCPF:
                    
                    if 'novoCPF' in dir(mudancaCPF):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'mudancaCPF.novoCPF', 
                                                          mudancaCPF.novoCPF.cdata, 
                                                          1, u'None')
            
            if 'verbasResc' in dir(infoTSVTermino.verbasResc):
                for verbasResc in infoTSVTermino.verbasResc:
                    
                    if 'dmDev' in dir(verbasResc.dmDev):
                        for dmDev in verbasResc.dmDev:
                            
                            if 'ideDmDev' in dir(dmDev):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dmDev.ideDmDev', 
                                                                  dmDev.ideDmDev.cdata, 
                                                                  1, u'None')
                            
                            if 'ideEstabLot' in dir(dmDev.ideEstabLot):
                                for ideEstabLot in dmDev.ideEstabLot:
                                    
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
            
            if 'quarentena' in dir(infoTSVTermino.quarentena):
                for quarentena in infoTSVTermino.quarentena:
                    
                    if 'dtFimQuar' in dir(quarentena):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'quarentena.dtFimQuar', 
                                                          quarentena.dtFimQuar.cdata, 
                                                          1, u'None')
    return validacoes_lista