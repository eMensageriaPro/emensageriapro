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


def validacoes_s2210_evtcat(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtCAT = doc.eSocial.evtCAT
    #variaveis
    
    if 'ideEvento' in dir(evtCAT.ideEvento):
        for ideEvento in evtCAT.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtCAT.ideEmpregador):
        for ideEmpregador in evtCAT.ideEmpregador:
            
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
    
    if 'ideVinculo' in dir(evtCAT.ideVinculo):
        for ideVinculo in evtCAT.ideVinculo:
            
            if 'cpfTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.cpfTrab', 
                                                  ideVinculo.cpfTrab.cdata, 
                                                  1, u'None')
            
            if 'nisTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.nisTrab', 
                                                  ideVinculo.nisTrab.cdata, 
                                                  0, u'None')
            
            if 'matricula' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.matricula', 
                                                  ideVinculo.matricula.cdata, 
                                                  0, u'None')
            
            if 'codCateg' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.codCateg', 
                                                  ideVinculo.codCateg.cdata, 
                                                  0, u'None')
    
    if 'cat' in dir(evtCAT.cat):
        for cat in evtCAT.cat:
            
            if 'dtAcid' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.dtAcid', 
                                                  cat.dtAcid.cdata, 
                                                  1, u'None')
            
            if 'tpAcid' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.tpAcid', 
                                                  cat.tpAcid.cdata, 
                                                  1, u'1.001, 1.002, 2.001, 2.002, 2.003, 2.004, 2.005, 2.006, 3.001, 3.002, 3.003, 3.004, 3.005, 3.006, 3.007, 3.008, 3.009, 3.010, 3.011, 4.001, 4.002')
            
            if 'hrAcid' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.hrAcid', 
                                                  cat.hrAcid.cdata, 
                                                  0, u'None')
            
            if 'hrsTrabAntesAcid' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.hrsTrabAntesAcid', 
                                                  cat.hrsTrabAntesAcid.cdata, 
                                                  1, u'None')
            
            if 'tpCat' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.tpCat', 
                                                  cat.tpCat.cdata, 
                                                  1, u'1, 2, 3')
            
            if 'indCatObito' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.indCatObito', 
                                                  cat.indCatObito.cdata, 
                                                  1, u'S, N')
            
            if 'dtObito' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.dtObito', 
                                                  cat.dtObito.cdata, 
                                                  0, u'None')
            
            if 'indComunPolicia' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.indComunPolicia', 
                                                  cat.indComunPolicia.cdata, 
                                                  1, u'S, N')
            
            if 'codSitGeradora' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.codSitGeradora', 
                                                  cat.codSitGeradora.cdata, 
                                                  1, u'200004300, 200004600, 200008300, 200008600, 200008900, 200012200, 200012300, 200012400, 200012500, 200012600, 200012700, 200012900, 200016300, 200016600, 200016900, 200020100, 200020300, 200020500, 200020700, 200020900, 200024300, 200024400, 200024500, 200024600, 200024700, 200024900, 200028300, 200028600, 200032200, 200032400, 200032600, 200032900, 200036000, 200040300, 200040600, 200044300, 200044600, 200048200, 200048400, 200048600, 200048900, 200052000, 200056000, 200060000, 200064000, 200068000, 200072300, 200072600, 200076200, 200076400, 200076600, 200076900, 200080200, 200080400, 200080600, 200080900, 200080901, 209000000, 209500000')
            
            if 'iniciatCAT' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.iniciatCAT', 
                                                  cat.iniciatCAT.cdata, 
                                                  1, u'1, 2, 3')
            
            if 'obsCAT' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.obsCAT', 
                                                  cat.obsCAT.cdata, 
                                                  0, u'None')
            
            if 'observacao' in dir(cat):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'cat.observacao', 
                                                  cat.observacao.cdata, 
                                                  0, u'None')
            
            if 'localAcidente' in dir(cat.localAcidente):
                for localAcidente in cat.localAcidente:
                    
                    if 'tpLocal' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.tpLocal', 
                                                          localAcidente.tpLocal.cdata, 
                                                          1, u'1, 2, 3, 4, 5, 6, 9')
                    
                    if 'dscLocal' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.dscLocal', 
                                                          localAcidente.dscLocal.cdata, 
                                                          0, u'None')
                    
                    if 'codAmb' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.codAmb', 
                                                          localAcidente.codAmb.cdata, 
                                                          0, u'None')
                    
                    if 'tpLograd' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.tpLograd', 
                                                          localAcidente.tpLograd.cdata, 
                                                          1, u'None')
                    
                    if 'dscLograd' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.dscLograd', 
                                                          localAcidente.dscLograd.cdata, 
                                                          1, u'None')
                    
                    if 'nrLograd' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.nrLograd', 
                                                          localAcidente.nrLograd.cdata, 
                                                          1, u'None')
                    
                    if 'complemento' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.complemento', 
                                                          localAcidente.complemento.cdata, 
                                                          0, u'None')
                    
                    if 'bairro' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.bairro', 
                                                          localAcidente.bairro.cdata, 
                                                          0, u'None')
                    
                    if 'cep' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.cep', 
                                                          localAcidente.cep.cdata, 
                                                          0, u'None')
                    
                    if 'codMunic' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.codMunic', 
                                                          localAcidente.codMunic.cdata, 
                                                          0, u'None')
                    
                    if 'uf' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.uf', 
                                                          localAcidente.uf.cdata, 
                                                          0, u'None')
                    
                    if 'pais' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.pais', 
                                                          localAcidente.pais.cdata, 
                                                          0, u'None')
                    
                    if 'codPostal' in dir(localAcidente):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'localAcidente.codPostal', 
                                                          localAcidente.codPostal.cdata, 
                                                          0, u'None')
                    
                    if 'ideLocalAcid' in dir(localAcidente.ideLocalAcid):
                        for ideLocalAcid in localAcidente.ideLocalAcid:
                            
                            if 'tpInsc' in dir(ideLocalAcid):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLocalAcid.tpInsc', 
                                                                  ideLocalAcid.tpInsc.cdata, 
                                                                  1, u'1, 2, 3, 4, 5')
                            
                            if 'nrInsc' in dir(ideLocalAcid):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideLocalAcid.nrInsc', 
                                                                  ideLocalAcid.nrInsc.cdata, 
                                                                  1, u'None')
            
            if 'parteAtingida' in dir(cat.parteAtingida):
                for parteAtingida in cat.parteAtingida:
                    
                    if 'codParteAting' in dir(parteAtingida):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'parteAtingida.codParteAting', 
                                                          parteAtingida.codParteAting.cdata, 
                                                          1, u'753030000, 753050000, 753070100, 753070300, 753070500, 753070700, 753070800, 753080000, 753090000, 753510000, 753510200, 754000000, 755010400, 755010600, 755030000, 755050000, 755070000, 755080000, 755090000, 756020000, 756030000, 756040000, 756050000, 756060000, 756070000, 756090000, 757010000, 757010200, 757010400, 757010600, 757030000, 757050000, 757070000, 757080000, 757090000, 758000000, 758500000, 758520000, 758530000, 758540000, 758550000, 758560000, 758570000, 758590000, 759000000')
                    
                    if 'lateralidade' in dir(parteAtingida):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'parteAtingida.lateralidade', 
                                                          parteAtingida.lateralidade.cdata, 
                                                          1, u'0, 1, 2, 3')
            
            if 'agenteCausador' in dir(cat.agenteCausador):
                for agenteCausador in cat.agenteCausador:
                    
                    if 'codAgntCausador' in dir(agenteCausador):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'agenteCausador.codAgntCausador', 
                                                          agenteCausador.codAgntCausador.cdata, 
                                                          1, u'200004300, 200004600, 200008300, 200008600, 200008900, 200012200, 200012300, 200012400, 200012500, 200012600, 200012700, 200012900, 200016300, 200016600, 200016900, 200020100, 200020300, 200020500, 200020700, 200020900, 200024300, 200024400, 200024500, 200024600, 200024700, 200024900, 200028300, 200028600, 200032200, 200032400, 200032600, 200032900, 200036000, 200040300, 200040600, 200044300, 200044600, 200048200, 200048400, 200048600, 200048900, 200052000, 200056000, 200060000, 200064000, 200068000, 200072300, 200072600, 200076200, 200076400, 200076600, 200076900, 200080200, 200080400, 200080600, 200080900, 200080901, 209000000, 209500000')
            
            if 'atestado' in dir(cat.atestado):
                for atestado in cat.atestado:
                    
                    if 'codCNES' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.codCNES', 
                                                          atestado.codCNES.cdata, 
                                                          0, u'None')
                    
                    if 'dtAtendimento' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.dtAtendimento', 
                                                          atestado.dtAtendimento.cdata, 
                                                          1, u'None')
                    
                    if 'hrAtendimento' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.hrAtendimento', 
                                                          atestado.hrAtendimento.cdata, 
                                                          1, u'None')
                    
                    if 'indInternacao' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.indInternacao', 
                                                          atestado.indInternacao.cdata, 
                                                          1, u'S, N')
                    
                    if 'durTrat' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.durTrat', 
                                                          atestado.durTrat.cdata, 
                                                          1, u'None')
                    
                    if 'indAfast' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.indAfast', 
                                                          atestado.indAfast.cdata, 
                                                          1, u'S, N')
                    
                    if 'dscLesao' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.dscLesao', 
                                                          atestado.dscLesao.cdata, 
                                                          1, u'702000000, 702005000, 702010000, 702015000, 702020000, 702025000, 702030000, 702035000, 702040000, 702042000, 702045000, 702048000, 702050000, 702055000, 702060000, 702065000, 702070000, 702075000, 702080000, 702090000, 704020000, 704030000, 704040000, 704050000, 704060000, 704070000, 704090000, 706050000, 706090000')
                    
                    if 'dscCompLesao' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.dscCompLesao', 
                                                          atestado.dscCompLesao.cdata, 
                                                          0, u'None')
                    
                    if 'diagProvavel' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.diagProvavel', 
                                                          atestado.diagProvavel.cdata, 
                                                          0, u'None')
                    
                    if 'codCID' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.codCID', 
                                                          atestado.codCID.cdata, 
                                                          1, u'None')
                    
                    if 'observacao' in dir(atestado):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'atestado.observacao', 
                                                          atestado.observacao.cdata, 
                                                          0, u'None')
                    
                    if 'emitente' in dir(atestado.emitente):
                        for emitente in atestado.emitente:
                            
                            if 'nmEmit' in dir(emitente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'emitente.nmEmit', 
                                                                  emitente.nmEmit.cdata, 
                                                                  1, u'None')
                            
                            if 'ideOC' in dir(emitente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'emitente.ideOC', 
                                                                  emitente.ideOC.cdata, 
                                                                  1, u'1, 2, 3')
                            
                            if 'nrOC' in dir(emitente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'emitente.nrOC', 
                                                                  emitente.nrOC.cdata, 
                                                                  1, u'None')
                            
                            if 'ufOC' in dir(emitente):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'emitente.ufOC', 
                                                                  emitente.ufOC.cdata, 
                                                                  0, u'None')
            
            if 'catOrigem' in dir(cat.catOrigem):
                for catOrigem in cat.catOrigem:
                    
                    if 'dtCatOrig' in dir(catOrigem):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'catOrigem.dtCatOrig', 
                                                          catOrigem.dtCatOrig.cdata, 
                                                          1, u'None')
                    
                    if 'nrRecCatOrig' in dir(catOrigem):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'catOrigem.nrRecCatOrig', 
                                                          catOrigem.nrRecCatOrig.cdata, 
                                                          1, u'None')
    return validacoes_lista