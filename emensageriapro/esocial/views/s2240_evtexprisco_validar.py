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


def validacoes_s2240_evtexprisco(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtExpRisco = doc.eSocial.evtExpRisco
    #variaveis
    
    if 'ideEvento' in dir(evtExpRisco.ideEvento):
        for ideEvento in evtExpRisco.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtExpRisco.ideEmpregador):
        for ideEmpregador in evtExpRisco.ideEmpregador:
            
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
    
    if 'ideVinculo' in dir(evtExpRisco.ideVinculo):
        for ideVinculo in evtExpRisco.ideVinculo:
            
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
    
    if 'infoExpRisco' in dir(evtExpRisco.infoExpRisco):
        for infoExpRisco in evtExpRisco.infoExpRisco:
            
            if 'dtIniCondicao' in dir(infoExpRisco):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoExpRisco.dtIniCondicao', 
                                                  infoExpRisco.dtIniCondicao.cdata, 
                                                  1, u'None')
            
            if 'infoAmb' in dir(infoExpRisco.infoAmb):
                for infoAmb in infoExpRisco.infoAmb:
                    
                    if 'codAmb' in dir(infoAmb):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoAmb.codAmb', 
                                                          infoAmb.codAmb.cdata, 
                                                          1, u'None')
            
            if 'infoAtiv' in dir(infoExpRisco.infoAtiv):
                for infoAtiv in infoExpRisco.infoAtiv:
                    
                    if 'dscAtivDes' in dir(infoAtiv):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoAtiv.dscAtivDes', 
                                                          infoAtiv.dscAtivDes.cdata, 
                                                          1, u'None')
                    
                    if 'ativPericInsal' in dir(infoAtiv.ativPericInsal):
                        for ativPericInsal in infoAtiv.ativPericInsal:
                            
                            if 'codAtiv' in dir(ativPericInsal):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ativPericInsal.codAtiv', 
                                                                  ativPericInsal.codAtiv.cdata, 
                                                                  1, u'01.001, 01.002, 01.003, 01.004, 01.005, 01.006, 01.007, 01.008, 01.009, 01.010, 01.011, 01.012, 01.013, 01.014, 02.001, 02.002, 02.003, 02.004, 02.005, 02.006, 02.007, 02.008, 02.009, 02.010, 02.011, 02.012, 02.013, 02.014, 02.015, 02.016, 02.017, 02.018, 02.019, 02.020, 02.021, 02.022, 02.023, 02.024, 02.025, 02.026, 02.027, 02.028, 02.029, 02.030, 02.031, 02.032, 02.033, 02.034, 02.035, 02.036, 02.037, 02.038, 02.039, 02.040, 02.041, 02.042, 02.043, 02.044, 02.045, 02.046, 02.047, 02.048, 02.049, 02.050, 02.051, 02.052, 02.053, 02.054, 02.055, 02.056, 02.057, 02.058, 02.059, 02.060, 02.061, 02.062, 02.063, 02.064, 02.065, 02.066, 02.067, 02.068, 02.069, 02.070, 02.071, 02.072, 02.073, 02.074, 02.075, 02.076, 02.077, 02.078, 02.079, 02.080, 02.081, 02.082, 02.083, 02.084, 02.085, 02.086, 02.087, 02.088, 02.089, 02.090, 02.091, 02.092, 02.093, 02.094, 02.095, 02.096, 02.097, 02.098, 02.099, 02.100, 02.101, 02.102, 03.001, 03.002, 03.003, 03.004, 03.005, 03.006, 03.007, 03.008, 04.001, 04.002, 04.003, 04.004, 04.005, 04.006, 04.007, 04.008, 04.009, 04.010, 04.011, 04.012, 04.013, 04.014, 04.015, 04.016, 04.017, 04.018, 04.019, 04.020, 04.021, 04.022, 04.023, 04.024, 04.025, 04.026, 04.027, 04.028, 04.029, 04.030, 04.031, 05.001, 05.002, 05.003, 05.004, 05.005, 05.006, 05.007, 05.008, 05.009, 05.010, 05.011, 06.001, 06.002, 06.003, 06.004, 06.005, 06.006, 06.007, 06.008, 06.009, 07.001, 07.002, 07.003, 07.004, 07.005, 07.006, 07.007, 08.001, 09.001, 09.002, 09.003, 09.004, 09.005, 09.006, 09.007, 09.008, 09.009, 09.010, 09.011, 10.001, 10.002, 10.003, 10.005, 10.006, 10.007, 10.008, 10.009, 11.001, 11.002, 99.999')
            
            if 'fatRisco' in dir(infoExpRisco.fatRisco):
                for fatRisco in infoExpRisco.fatRisco:
                    
                    if 'codFatRis' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.codFatRis', 
                                                          fatRisco.codFatRis.cdata, 
                                                          1, u'None')
                    
                    if 'tpAval' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.tpAval', 
                                                          fatRisco.tpAval.cdata, 
                                                          1, u'1, 2')
                    
                    if 'intConc' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.intConc', 
                                                          fatRisco.intConc.cdata, 
                                                          0, u'None')
                    
                    if 'limTol' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.limTol', 
                                                          fatRisco.limTol.cdata, 
                                                          0, u'None')
                    
                    if 'unMed' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.unMed', 
                                                          fatRisco.unMed.cdata, 
                                                          0, u'1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 26, 27, 28, 29, 30, 31, 32, 35, 36, 37, 39, 43')
                    
                    if 'tecMedicao' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.tecMedicao', 
                                                          fatRisco.tecMedicao.cdata, 
                                                          0, u'None')
                    
                    if 'insalubridade' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.insalubridade', 
                                                          fatRisco.insalubridade.cdata, 
                                                          0, u'S, N')
                    
                    if 'periculosidade' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.periculosidade', 
                                                          fatRisco.periculosidade.cdata, 
                                                          0, u'S, N')
                    
                    if 'aposentEsp' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.aposentEsp', 
                                                          fatRisco.aposentEsp.cdata, 
                                                          0, u'S, N')
                    
                    if 'dscFatRisc' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.dscFatRisc', 
                                                          fatRisco.dscFatRisc.cdata, 
                                                          0, u'None')
                    
                    if 'epcEpi' in dir(fatRisco.epcEpi):
                        for epcEpi in fatRisco.epcEpi:
                            
                            if 'utilizEPC' in dir(epcEpi):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'epcEpi.utilizEPC', 
                                                                  epcEpi.utilizEPC.cdata, 
                                                                  1, u'0, 1, 2')
                            
                            if 'eficEpc' in dir(epcEpi):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'epcEpi.eficEpc', 
                                                                  epcEpi.eficEpc.cdata, 
                                                                  0, u'S, N')
                            
                            if 'utilizEPI' in dir(epcEpi):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'epcEpi.utilizEPI', 
                                                                  epcEpi.utilizEPI.cdata, 
                                                                  1, u'0, 1, 2')
                            
                            if 'epc' in dir(epcEpi.epc):
                                for epc in epcEpi.epc:
                                    
                                    if 'codEP' in dir(epc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epc.codEP', 
                                                                          epc.codEP.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dscEpc' in dir(epc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epc.dscEpc', 
                                                                          epc.dscEpc.cdata, 
                                                                          1, u'None')
                                    
                                    if 'eficEpc' in dir(epc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epc.eficEpc', 
                                                                          epc.eficEpc.cdata, 
                                                                          0, u'S, N')
                            
                            if 'epi' in dir(epcEpi.epi):
                                for epi in epcEpi.epi:
                                    
                                    if 'caEPI' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.caEPI', 
                                                                          epi.caEPI.cdata, 
                                                                          0, u'None')
                                    
                                    if 'dscEPI' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.dscEPI', 
                                                                          epi.dscEPI.cdata, 
                                                                          0, u'None')
                                    
                                    if 'eficEpi' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.eficEpi', 
                                                                          epi.eficEpi.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'medProtecao' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.medProtecao', 
                                                                          epi.medProtecao.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'condFuncto' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.condFuncto', 
                                                                          epi.condFuncto.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'usoInint' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.usoInint', 
                                                                          epi.usoInint.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'przValid' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.przValid', 
                                                                          epi.przValid.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'periodicTroca' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.periodicTroca', 
                                                                          epi.periodicTroca.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'higienizacao' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.higienizacao', 
                                                                          epi.higienizacao.cdata, 
                                                                          1, u'S, N')
            
            if 'respReg' in dir(infoExpRisco.respReg):
                for respReg in infoExpRisco.respReg:
                    
                    if 'cpfResp' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.cpfResp', 
                                                          respReg.cpfResp.cdata, 
                                                          1, u'None')
                    
                    if 'nisResp' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nisResp', 
                                                          respReg.nisResp.cdata, 
                                                          1, u'None')
                    
                    if 'nmResp' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nmResp', 
                                                          respReg.nmResp.cdata, 
                                                          1, u'None')
                    
                    if 'ideOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.ideOC', 
                                                          respReg.ideOC.cdata, 
                                                          1, u'1, 4, 9')
                    
                    if 'dscOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.dscOC', 
                                                          respReg.dscOC.cdata, 
                                                          0, u'None')
                    
                    if 'nrOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nrOC', 
                                                          respReg.nrOC.cdata, 
                                                          1, u'None')
                    
                    if 'ufOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.ufOC', 
                                                          respReg.ufOC.cdata, 
                                                          1, u'None')
            
            if 'obs' in dir(infoExpRisco.obs):
                for obs in infoExpRisco.obs:
                    
                    if 'metErg' in dir(obs):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'obs.metErg', 
                                                          obs.metErg.cdata, 
                                                          0, u'None')
                    
                    if 'obsCompl' in dir(obs):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'obs.obsCompl', 
                                                          obs.obsCompl.cdata, 
                                                          0, u'None')
                    
                    if 'observacao' in dir(obs):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'obs.observacao', 
                                                          obs.observacao.cdata, 
                                                          0, u'None')
            
            if 'altExpRisco' in dir(infoExpRisco.altExpRisco):
                for altExpRisco in infoExpRisco.altExpRisco:
                    
                    if 'dtAltCondicao' in dir(altExpRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'altExpRisco.dtAltCondicao', 
                                                          altExpRisco.dtAltCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoAmb' in dir(altExpRisco.infoAmb):
                        for infoAmb in altExpRisco.infoAmb:
                            
                            if 'codAmb' in dir(infoAmb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAmb.codAmb', 
                                                                  infoAmb.codAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'infoAtiv' in dir(infoAmb.infoAtiv):
                                for infoAtiv in infoAmb.infoAtiv:
                                    
                                    if 'dscAtivDes' in dir(infoAtiv):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoAtiv.dscAtivDes', 
                                                                          infoAtiv.dscAtivDes.cdata, 
                                                                          1, u'None')
                            
                            if 'fatRisco' in dir(infoAmb.fatRisco):
                                for fatRisco in infoAmb.fatRisco:
                                    
                                    if 'codFatRis' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.codFatRis', 
                                                                          fatRisco.codFatRis.cdata, 
                                                                          1, u'None')
                                    
                                    if 'intConc' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.intConc', 
                                                                          fatRisco.intConc.cdata, 
                                                                          0, u'None')
                                    
                                    if 'tecMedicao' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.tecMedicao', 
                                                                          fatRisco.tecMedicao.cdata, 
                                                                          0, u'None')
                                    
                                    if 'epcEpi' in dir(fatRisco.epcEpi):
                                        for epcEpi in fatRisco.epcEpi:
                                            
                                            if 'utilizEPC' in dir(epcEpi):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'epcEpi.utilizEPC', 
                                                                                  epcEpi.utilizEPC.cdata, 
                                                                                  1, u'0, 1, 2')
                                            
                                            if 'utilizEPI' in dir(epcEpi):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'epcEpi.utilizEPI', 
                                                                                  epcEpi.utilizEPI.cdata, 
                                                                                  1, u'0, 1, 2')
                                            
                                            if 'epc' in dir(epcEpi.epc):
                                                for epc in epcEpi.epc:
                                                    
                                                    if 'dscEpc' in dir(epc):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epc.dscEpc', 
                                                                                          epc.dscEpc.cdata, 
                                                                                          1, u'None')
                                                    
                                                    if 'eficEpc' in dir(epc):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epc.eficEpc', 
                                                                                          epc.eficEpc.cdata, 
                                                                                          0, u'S, N')
                                            
                                            if 'epi' in dir(epcEpi.epi):
                                                for epi in epcEpi.epi:
                                                    
                                                    if 'caEPI' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.caEPI', 
                                                                                          epi.caEPI.cdata, 
                                                                                          0, u'None')
                                                    
                                                    if 'eficEpi' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.eficEpi', 
                                                                                          epi.eficEpi.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'medProtecao' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.medProtecao', 
                                                                                          epi.medProtecao.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'condFuncto' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.condFuncto', 
                                                                                          epi.condFuncto.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'przValid' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.przValid', 
                                                                                          epi.przValid.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'periodicTroca' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.periodicTroca', 
                                                                                          epi.periodicTroca.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'higienizacao' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.higienizacao', 
                                                                                          epi.higienizacao.cdata, 
                                                                                          1, u'S, N')
            
            if 'fimExpRisco' in dir(infoExpRisco.fimExpRisco):
                for fimExpRisco in infoExpRisco.fimExpRisco:
                    
                    if 'dtFimCondicao' in dir(fimExpRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fimExpRisco.dtFimCondicao', 
                                                          fimExpRisco.dtFimCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoAmb' in dir(fimExpRisco.infoAmb):
                        for infoAmb in fimExpRisco.infoAmb:
                            
                            if 'codAmb' in dir(infoAmb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAmb.codAmb', 
                                                                  infoAmb.codAmb.cdata, 
                                                                  1, u'None')
            
            if 'respReg' in dir(infoExpRisco.respReg):
                for respReg in infoExpRisco.respReg:
                    
                    if 'dtIni' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.dtIni', 
                                                          respReg.dtIni.cdata, 
                                                          1, u'None')
                    
                    if 'dtFim' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.dtFim', 
                                                          respReg.dtFim.cdata, 
                                                          0, u'None')
                    
                    if 'nisResp' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nisResp', 
                                                          respReg.nisResp.cdata, 
                                                          1, u'None')
                    
                    if 'nrOc' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nrOc', 
                                                          respReg.nrOc.cdata, 
                                                          1, u'None')
                    
                    if 'ufOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.ufOC', 
                                                          respReg.ufOC.cdata, 
                                                          0, u'None')
    return validacoes_lista