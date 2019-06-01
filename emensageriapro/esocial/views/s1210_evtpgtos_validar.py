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


def validacoes_s1210_evtpgtos(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtPgtos = doc.eSocial.evtPgtos
    #variaveis
    
    if 'ideEvento' in dir(evtPgtos.ideEvento):
        for ideEvento in evtPgtos.ideEvento:
            
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
                                                  1, u'1')
            
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
    
    if 'ideEmpregador' in dir(evtPgtos.ideEmpregador):
        for ideEmpregador in evtPgtos.ideEmpregador:
            
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
    
    if 'ideBenef' in dir(evtPgtos.ideBenef):
        for ideBenef in evtPgtos.ideBenef:
            
            if 'cpfBenef' in dir(ideBenef):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideBenef.cpfBenef', 
                                                  ideBenef.cpfBenef.cdata, 
                                                  1, u'None')
            
            if 'deps' in dir(ideBenef.deps):
                for deps in ideBenef.deps:
                    
                    if 'vrDedDep' in dir(deps):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'deps.vrDedDep', 
                                                          deps.vrDedDep.cdata, 
                                                          1, u'None')
            
            if 'infoPgto' in dir(ideBenef.infoPgto):
                for infoPgto in ideBenef.infoPgto:
                    
                    if 'dtPgto' in dir(infoPgto):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoPgto.dtPgto', 
                                                          infoPgto.dtPgto.cdata, 
                                                          1, u'None')
                    
                    if 'tpPgto' in dir(infoPgto):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoPgto.tpPgto', 
                                                          infoPgto.tpPgto.cdata, 
                                                          1, u'1, 2, 3, 5, 6, 7, 9')
                    
                    if 'indResBr' in dir(infoPgto):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoPgto.indResBr', 
                                                          infoPgto.indResBr.cdata, 
                                                          1, u'S, N')
                    
                    if 'detPgtoFl' in dir(infoPgto.detPgtoFl):
                        for detPgtoFl in infoPgto.detPgtoFl:
                            
                            if 'perRef' in dir(detPgtoFl):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFl.perRef', 
                                                                  detPgtoFl.perRef.cdata, 
                                                                  0, u'None')
                            
                            if 'ideDmDev' in dir(detPgtoFl):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFl.ideDmDev', 
                                                                  detPgtoFl.ideDmDev.cdata, 
                                                                  1, u'None')
                            
                            if 'indPgtoTt' in dir(detPgtoFl):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFl.indPgtoTt', 
                                                                  detPgtoFl.indPgtoTt.cdata, 
                                                                  1, u'S, N')
                            
                            if 'vrLiq' in dir(detPgtoFl):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFl.vrLiq', 
                                                                  detPgtoFl.vrLiq.cdata, 
                                                                  1, u'None')
                            
                            if 'nrRecArq' in dir(detPgtoFl):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFl.nrRecArq', 
                                                                  detPgtoFl.nrRecArq.cdata, 
                                                                  0, u'None')
                            
                            if 'retPgtoTot' in dir(detPgtoFl.retPgtoTot):
                                for retPgtoTot in detPgtoFl.retPgtoTot:
                                    
                                    if 'codRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.codRubr', 
                                                                          retPgtoTot.codRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'ideTabRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.ideTabRubr', 
                                                                          retPgtoTot.ideTabRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'qtdRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.qtdRubr', 
                                                                          retPgtoTot.qtdRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'fatorRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.fatorRubr', 
                                                                          retPgtoTot.fatorRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrUnit' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.vrUnit', 
                                                                          retPgtoTot.vrUnit.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.vrRubr', 
                                                                          retPgtoTot.vrRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'penAlim' in dir(retPgtoTot.penAlim):
                                        for penAlim in retPgtoTot.penAlim:
                                            
                                            if 'cpfBenef' in dir(penAlim):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'penAlim.cpfBenef', 
                                                                                  penAlim.cpfBenef.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'dtNasctoBenef' in dir(penAlim):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'penAlim.dtNasctoBenef', 
                                                                                  penAlim.dtNasctoBenef.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'nmBenefic' in dir(penAlim):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'penAlim.nmBenefic', 
                                                                                  penAlim.nmBenefic.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrPensao' in dir(penAlim):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'penAlim.vlrPensao', 
                                                                                  penAlim.vlrPensao.cdata, 
                                                                                  1, u'None')
                            
                            if 'infoPgtoParc' in dir(detPgtoFl.infoPgtoParc):
                                for infoPgtoParc in detPgtoFl.infoPgtoParc:
                                    
                                    if 'matricula' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.matricula', 
                                                                          infoPgtoParc.matricula.cdata, 
                                                                          0, u'None')
                                    
                                    if 'codRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.codRubr', 
                                                                          infoPgtoParc.codRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'ideTabRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.ideTabRubr', 
                                                                          infoPgtoParc.ideTabRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'qtdRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.qtdRubr', 
                                                                          infoPgtoParc.qtdRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'fatorRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.fatorRubr', 
                                                                          infoPgtoParc.fatorRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrUnit' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.vrUnit', 
                                                                          infoPgtoParc.vrUnit.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.vrRubr', 
                                                                          infoPgtoParc.vrRubr.cdata, 
                                                                          1, u'None')
                    
                    if 'detPgtoBenPr' in dir(infoPgto.detPgtoBenPr):
                        for detPgtoBenPr in infoPgto.detPgtoBenPr:
                            
                            if 'perRef' in dir(detPgtoBenPr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoBenPr.perRef', 
                                                                  detPgtoBenPr.perRef.cdata, 
                                                                  1, u'None')
                            
                            if 'ideDmDev' in dir(detPgtoBenPr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoBenPr.ideDmDev', 
                                                                  detPgtoBenPr.ideDmDev.cdata, 
                                                                  1, u'None')
                            
                            if 'indPgtoTt' in dir(detPgtoBenPr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoBenPr.indPgtoTt', 
                                                                  detPgtoBenPr.indPgtoTt.cdata, 
                                                                  1, u'S, N')
                            
                            if 'vrLiq' in dir(detPgtoBenPr):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoBenPr.vrLiq', 
                                                                  detPgtoBenPr.vrLiq.cdata, 
                                                                  1, u'None')
                            
                            if 'retPgtoTot' in dir(detPgtoBenPr.retPgtoTot):
                                for retPgtoTot in detPgtoBenPr.retPgtoTot:
                                    
                                    if 'codRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.codRubr', 
                                                                          retPgtoTot.codRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'ideTabRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.ideTabRubr', 
                                                                          retPgtoTot.ideTabRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'qtdRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.qtdRubr', 
                                                                          retPgtoTot.qtdRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'fatorRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.fatorRubr', 
                                                                          retPgtoTot.fatorRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrUnit' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.vrUnit', 
                                                                          retPgtoTot.vrUnit.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrRubr' in dir(retPgtoTot):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'retPgtoTot.vrRubr', 
                                                                          retPgtoTot.vrRubr.cdata, 
                                                                          1, u'None')
                            
                            if 'infoPgtoParc' in dir(detPgtoBenPr.infoPgtoParc):
                                for infoPgtoParc in detPgtoBenPr.infoPgtoParc:
                                    
                                    if 'codRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.codRubr', 
                                                                          infoPgtoParc.codRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'ideTabRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.ideTabRubr', 
                                                                          infoPgtoParc.ideTabRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'qtdRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.qtdRubr', 
                                                                          infoPgtoParc.qtdRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'fatorRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.fatorRubr', 
                                                                          infoPgtoParc.fatorRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrUnit' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.vrUnit', 
                                                                          infoPgtoParc.vrUnit.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrRubr' in dir(infoPgtoParc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoParc.vrRubr', 
                                                                          infoPgtoParc.vrRubr.cdata, 
                                                                          1, u'None')
                    
                    if 'detPgtoFer' in dir(infoPgto.detPgtoFer):
                        for detPgtoFer in infoPgto.detPgtoFer:
                            
                            if 'codCateg' in dir(detPgtoFer):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFer.codCateg', 
                                                                  detPgtoFer.codCateg.cdata, 
                                                                  1, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
                            
                            if 'matricula' in dir(detPgtoFer):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFer.matricula', 
                                                                  detPgtoFer.matricula.cdata, 
                                                                  0, u'None')
                            
                            if 'dtIniGoz' in dir(detPgtoFer):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFer.dtIniGoz', 
                                                                  detPgtoFer.dtIniGoz.cdata, 
                                                                  1, u'None')
                            
                            if 'qtDias' in dir(detPgtoFer):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFer.qtDias', 
                                                                  detPgtoFer.qtDias.cdata, 
                                                                  1, u'None')
                            
                            if 'vrLiq' in dir(detPgtoFer):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoFer.vrLiq', 
                                                                  detPgtoFer.vrLiq.cdata, 
                                                                  1, u'None')
                            
                            if 'detRubrFer' in dir(detPgtoFer.detRubrFer):
                                for detRubrFer in detPgtoFer.detRubrFer:
                                    
                                    if 'codRubr' in dir(detRubrFer):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'detRubrFer.codRubr', 
                                                                          detRubrFer.codRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'ideTabRubr' in dir(detRubrFer):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'detRubrFer.ideTabRubr', 
                                                                          detRubrFer.ideTabRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'qtdRubr' in dir(detRubrFer):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'detRubrFer.qtdRubr', 
                                                                          detRubrFer.qtdRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'fatorRubr' in dir(detRubrFer):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'detRubrFer.fatorRubr', 
                                                                          detRubrFer.fatorRubr.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrUnit' in dir(detRubrFer):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'detRubrFer.vrUnit', 
                                                                          detRubrFer.vrUnit.cdata, 
                                                                          0, u'None')
                                    
                                    if 'vrRubr' in dir(detRubrFer):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'detRubrFer.vrRubr', 
                                                                          detRubrFer.vrRubr.cdata, 
                                                                          1, u'None')
                                    
                                    if 'penAlim' in dir(detRubrFer.penAlim):
                                        for penAlim in detRubrFer.penAlim:
                                            
                                            if 'cpfBenef' in dir(penAlim):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'penAlim.cpfBenef', 
                                                                                  penAlim.cpfBenef.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'dtNasctoBenef' in dir(penAlim):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'penAlim.dtNasctoBenef', 
                                                                                  penAlim.dtNasctoBenef.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'nmBenefic' in dir(penAlim):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'penAlim.nmBenefic', 
                                                                                  penAlim.nmBenefic.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrPensao' in dir(penAlim):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'penAlim.vlrPensao', 
                                                                                  penAlim.vlrPensao.cdata, 
                                                                                  1, u'None')
                    
                    if 'detPgtoAnt' in dir(infoPgto.detPgtoAnt):
                        for detPgtoAnt in infoPgto.detPgtoAnt:
                            
                            if 'codCateg' in dir(detPgtoAnt):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'detPgtoAnt.codCateg', 
                                                                  detPgtoAnt.codCateg.cdata, 
                                                                  1, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
                            
                            if 'infoPgtoAnt' in dir(detPgtoAnt.infoPgtoAnt):
                                for infoPgtoAnt in detPgtoAnt.infoPgtoAnt:
                                    
                                    if 'tpBcIRRF' in dir(infoPgtoAnt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoAnt.tpBcIRRF', 
                                                                          infoPgtoAnt.tpBcIRRF.cdata, 
                                                                          1, u'00, 01, 09, 11, 12, 13, 14, 15, 31, 32, 33, 34, 35, 41, 42, 43, 44, 46, 47, 51, 52, 53, 54, 55, 61, 62, 63, 64, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 91, 92, 93, 94, 95')
                                    
                                    if 'vrBcIRRF' in dir(infoPgtoAnt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgtoAnt.vrBcIRRF', 
                                                                          infoPgtoAnt.vrBcIRRF.cdata, 
                                                                          1, u'None')
                    
                    if 'idePgtoExt' in dir(infoPgto.idePgtoExt):
                        for idePgtoExt in infoPgto.idePgtoExt:
                            
                            if 'idePais' in dir(idePgtoExt.idePais):
                                for idePais in idePgtoExt.idePais:
                                    
                                    if 'codPais' in dir(idePais):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'idePais.codPais', 
                                                                          idePais.codPais.cdata, 
                                                                          1, u'008, 009, 013, 015, 017, 020, 023, 025, 031, 037, 040, 041, 042, 043, 047, 053, 059, 063, 064, 065, 069, 072, 073, 077, 080, 081, 083, 085, 087, 088, 090, 093, 097, 098, 099, 100, 101, 102, 105, 106, 108, 111, 115, 119, 127, 131, 137, 141, 145, 149, 150, 151, 152, 153, 154, 158, 160, 161, 163, 165, 169, 173, 177, 183, 187, 190, 193, 195, 196, 198, 199, 200, 229, 232, 235, 237, 239, 240, 243, 244, 245, 246, 247, 249, 251, 253, 255, 259, 263, 267, 271, 275, 281, 285, 289, 291, 292, 293, 297, 301, 305, 309, 313, 317, 321, 325, 329, 331, 334, 337, 341, 343, 345, 351, 355, 357, 358, 359, 361, 365, 367, 369, 372, 375, 379, 383, 386, 388, 391, 393, 395, 396, 399, 403, 411, 420, 423, 426, 427, 431, 434, 438, 440, 442, 445, 447, 449, 450, 452, 455, 458, 461, 464, 467, 472, 474, 476, 477, 485, 488, 489, 490, 493, 494, 495, 497, 498, 499, 501, 505, 507, 508, 511, 517, 521, 525, 528, 531, 535, 538, 542, 545, 548, 551, 556, 563, 566, 569, 573, 575, 576, 578, 580, 583, 586, 589, 593, 599, 603, 607, 611, 623, 625, 628, 640, 647, 660, 665, 670, 675, 676, 677, 678, 685, 687, 690, 691, 693, 695, 697, 698, 699, 700, 705, 710, 715, 720, 728, 731, 735, 737, 738, 741, 744, 748, 750, 754, 755, 756, 759, 760, 764, 767, 770, 772, 776, 780, 781, 782, 783, 785, 788, 790, 791, 795, 800, 805, 810, 815, 820, 823, 824, 827, 828, 831, 833, 840, 845, 847, 848, 850, 855, 858, 863, 866, 870, 873, 875, 888, 890, 895')
                                    
                                    if 'indNIF' in dir(idePais):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'idePais.indNIF', 
                                                                          idePais.indNIF.cdata, 
                                                                          1, u'1, 2, 3')
                                    
                                    if 'nifBenef' in dir(idePais):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'idePais.nifBenef', 
                                                                          idePais.nifBenef.cdata, 
                                                                          0, u'None')
                            
                            if 'endExt' in dir(idePgtoExt.endExt):
                                for endExt in idePgtoExt.endExt:
                                    
                                    if 'dscLograd' in dir(endExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'endExt.dscLograd', 
                                                                          endExt.dscLograd.cdata, 
                                                                          1, u'None')
                                    
                                    if 'nrLograd' in dir(endExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'endExt.nrLograd', 
                                                                          endExt.nrLograd.cdata, 
                                                                          0, u'None')
                                    
                                    if 'complem' in dir(endExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'endExt.complem', 
                                                                          endExt.complem.cdata, 
                                                                          0, u'None')
                                    
                                    if 'bairro' in dir(endExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'endExt.bairro', 
                                                                          endExt.bairro.cdata, 
                                                                          0, u'None')
                                    
                                    if 'nmCid' in dir(endExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'endExt.nmCid', 
                                                                          endExt.nmCid.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codPostal' in dir(endExt):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'endExt.codPostal', 
                                                                          endExt.codPostal.cdata, 
                                                                          0, u'None')
    return validacoes_lista