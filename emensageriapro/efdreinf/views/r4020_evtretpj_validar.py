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


def validacoes_r4020_evtretpj(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtRetPJ = doc.Reinf.evtRetPJ
    #variaveis
    
    if 'ideEvento' in dir(evtRetPJ.ideEvento):
        for ideEvento in evtRetPJ.ideEvento:
            
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
                                                  1, u'1, 2')
            
            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc', 
                                                  ideEvento.verProc.cdata, 
                                                  1, u'None')
    
    if 'ideContri' in dir(evtRetPJ.ideContri):
        for ideContri in evtRetPJ.ideContri:
            
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
    
    if 'ideEstab' in dir(evtRetPJ.ideEstab):
        for ideEstab in evtRetPJ.ideEstab:
            
            if 'tpInscEstab' in dir(ideEstab):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEstab.tpInscEstab', 
                                                  ideEstab.tpInscEstab.cdata, 
                                                  1, u'1')
            
            if 'nrInscEstab' in dir(ideEstab):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEstab.nrInscEstab', 
                                                  ideEstab.nrInscEstab.cdata, 
                                                  1, u'None')
            
            if 'ideBenef' in dir(ideEstab.ideBenef):
                for ideBenef in ideEstab.ideBenef:
                    
                    if 'cnpjBenef' in dir(ideBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideBenef.cnpjBenef', 
                                                          ideBenef.cnpjBenef.cdata, 
                                                          0, u'None')
                    
                    if 'nmBenef' in dir(ideBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideBenef.nmBenef', 
                                                          ideBenef.nmBenef.cdata, 
                                                          0, u'None')
                    
                    if 'isenImun' in dir(ideBenef):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideBenef.isenImun', 
                                                          ideBenef.isenImun.cdata, 
                                                          1, u'None')
                    
                    if 'idePgto' in dir(ideBenef.idePgto):
                        for idePgto in ideBenef.idePgto:
                            
                            if 'natRend' in dir(idePgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePgto.natRend', 
                                                                  idePgto.natRend.cdata, 
                                                                  1, u'000000001, 000000002, 000000003, 000000004, 000000005, 000000006, 000000007, 000000008, 000000009, 000000010, 000000011, 000000012, 000000013, 000000014, 000000015, 000000016, 000000017, 000000018, 000000019, 000000020, 000000021, 000000022, 000000023, 000000024, 000000025, 000000026, 000000027, 000000028, 000000029, 000000030, 000000031, 000000032, 000000033, 000000034, 000000035, 000000036, 000000037, 000000038, 000000039, 000000040, 000000041, 000000042, 000000043, 000000044, 000000045, 000000046, 000000047, 000000048, 000000049, 000000050, 000000051, 000000052, 000000053, 000000054, 000000055, 000000056, 000000057, 000000058, 000000059, 000000060, 000000061, 000000062, 000000063, 000000064, 000000065, 000000066, 000000067, 000000068, 000000069, 000000070, 000000071, 000000072, 000000073, 000000074, 000000075, 000000076, 000000077, 000000078, 000000079, 000000080, 000000081, 000000082, 000000083, 000000084, 000000085, 000000086, 000000087, 000000088, 000000089, 000000090, 000000091, 000000092, 000000093, 000000094, 000000095, 000000096, 000000097, 000000098, 000000099, 000000100, 000000101, 000000102, 000000103, 000000104, 000000105, 000000106, 000000107, 000000108, 000000109, 000000110, 000000111, 000000112, 000000113, 000000114, 000000115, 000000116, 000000117, 000000118, 000000119, 000000120, 000000121, 000000122, 000000123, 000000124, 000000125, 000000126, 000000127, 000000128, 000000129, 000000130, 000000131, 000000132, 000000133, 000000134, 000000135, 200000001, 200000002, 200000003, 200000004, 200000005, 200000006, 200000007, 200000008, 200000009, 200000010, 200000011, 200000012, 200000013, 200000014, 200000015, 200000016, 200000017, 200000018, 200000019, 200000020, 200000021, 200000022, 200000023, 200000024, 200000025, 200000026, 200000027, 200000028, 200000029, 200000030, 200000031, 200000032, 200000033, 200000034, 200000035, 200000036, 200000037, 200000038')
                            
                            if 'paisResid' in dir(idePgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePgto.paisResid', 
                                                                  idePgto.paisResid.cdata, 
                                                                  1, u'None')
                            
                            if 'observ' in dir(idePgto):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'idePgto.observ', 
                                                                  idePgto.observ.cdata, 
                                                                  0, u'None')
                            
                            if 'infoPgto' in dir(idePgto.infoPgto):
                                for infoPgto in idePgto.infoPgto:
                                    
                                    if 'dtFG' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.dtFG', 
                                                                          infoPgto.dtFG.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vlrTotalPag' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrTotalPag', 
                                                                          infoPgto.vlrTotalPag.cdata, 
                                                                          1, u'None')
                                    
                                    if 'vlrTotalCred' in dir(infoPgto):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoPgto.vlrTotalCred', 
                                                                          infoPgto.vlrTotalCred.cdata, 
                                                                          1, u'None')
                                    
                                    if 'IR' in dir(infoPgto.IR):
                                        for IR in infoPgto.IR:
                                            
                                            if 'vlrBaseIR' in dir(IR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'IR.vlrBaseIR', 
                                                                                  IR.vlrBaseIR.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrIR' in dir(IR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'IR.vlrIR', 
                                                                                  IR.vlrIR.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrBaseNIR' in dir(IR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'IR.vlrBaseNIR', 
                                                                                  IR.vlrBaseNIR.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrNIR' in dir(IR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'IR.vlrNIR', 
                                                                                  IR.vlrNIR.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrDepIR' in dir(IR):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'IR.vlrDepIR', 
                                                                                  IR.vlrDepIR.cdata, 
                                                                                  0, u'None')
                                    
                                    if 'CSLL' in dir(infoPgto.CSLL):
                                        for CSLL in infoPgto.CSLL:
                                            
                                            if 'vlrBaseCSLL' in dir(CSLL):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'CSLL.vlrBaseCSLL', 
                                                                                  CSLL.vlrBaseCSLL.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrCSLL' in dir(CSLL):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'CSLL.vlrCSLL', 
                                                                                  CSLL.vlrCSLL.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrBaseNCSLL' in dir(CSLL):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'CSLL.vlrBaseNCSLL', 
                                                                                  CSLL.vlrBaseNCSLL.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrNCSLL' in dir(CSLL):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'CSLL.vlrNCSLL', 
                                                                                  CSLL.vlrNCSLL.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrDepCSLL' in dir(CSLL):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'CSLL.vlrDepCSLL', 
                                                                                  CSLL.vlrDepCSLL.cdata, 
                                                                                  0, u'None')
                                    
                                    if 'Cofins' in dir(infoPgto.Cofins):
                                        for Cofins in infoPgto.Cofins:
                                            
                                            if 'vlrBaseCofins' in dir(Cofins):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'Cofins.vlrBaseCofins', 
                                                                                  Cofins.vlrBaseCofins.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrCofins' in dir(Cofins):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'Cofins.vlrCofins', 
                                                                                  Cofins.vlrCofins.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrBaseNCofins' in dir(Cofins):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'Cofins.vlrBaseNCofins', 
                                                                                  Cofins.vlrBaseNCofins.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrNCofins' in dir(Cofins):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'Cofins.vlrNCofins', 
                                                                                  Cofins.vlrNCofins.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrDepCofins' in dir(Cofins):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'Cofins.vlrDepCofins', 
                                                                                  Cofins.vlrDepCofins.cdata, 
                                                                                  0, u'None')
                                    
                                    if 'PP' in dir(infoPgto.PP):
                                        for PP in infoPgto.PP:
                                            
                                            if 'vlrBasePP' in dir(PP):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'PP.vlrBasePP', 
                                                                                  PP.vlrBasePP.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrPP' in dir(PP):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'PP.vlrPP', 
                                                                                  PP.vlrPP.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'vlrBaseNPP' in dir(PP):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'PP.vlrBaseNPP', 
                                                                                  PP.vlrBaseNPP.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrNPP' in dir(PP):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'PP.vlrNPP', 
                                                                                  PP.vlrNPP.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'vlrDepPP' in dir(PP):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'PP.vlrDepPP', 
                                                                                  PP.vlrDepPP.cdata, 
                                                                                  0, u'None')
                                    
                                    if 'FCI' in dir(infoPgto.FCI):
                                        for FCI in infoPgto.FCI:
                                            
                                            if 'nrInscFCI' in dir(FCI):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'FCI.nrInscFCI', 
                                                                                  FCI.nrInscFCI.cdata, 
                                                                                  1, u'None')
                                    
                                    if 'SCP' in dir(infoPgto.SCP):
                                        for SCP in infoPgto.SCP:
                                            
                                            if 'nrInscSCP' in dir(SCP):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'SCP.nrInscSCP', 
                                                                                  SCP.nrInscSCP.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'percSCP' in dir(SCP):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'SCP.percSCP', 
                                                                                  SCP.percSCP.cdata, 
                                                                                  1, u'None')
                                    
                                    if 'infoProcRet' in dir(infoPgto.infoProcRet):
                                        for infoProcRet in infoPgto.infoProcRet:
                                            
                                            if 'tpProcRet' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.tpProcRet', 
                                                                                  infoProcRet.tpProcRet.cdata, 
                                                                                  1, u'1, 2')
                                            
                                            if 'nrProcRet' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.nrProcRet', 
                                                                                  infoProcRet.nrProcRet.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'codSusp' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.codSusp', 
                                                                                  infoProcRet.codSusp.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'nIR' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.nIR', 
                                                                                  infoProcRet.nIR.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'depIR' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.depIR', 
                                                                                  infoProcRet.depIR.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'nCSLL' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.nCSLL', 
                                                                                  infoProcRet.nCSLL.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'depCSLL' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.depCSLL', 
                                                                                  infoProcRet.depCSLL.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'nCofins' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.nCofins', 
                                                                                  infoProcRet.nCofins.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'depCofins' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.depCofins', 
                                                                                  infoProcRet.depCofins.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'nPP' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.nPP', 
                                                                                  infoProcRet.nPP.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'depPP' in dir(infoProcRet):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcRet.depPP', 
                                                                                  infoProcRet.depPP.cdata, 
                                                                                  0, u'None')
                                    
                                    if 'infoProcJud' in dir(infoPgto.infoProcJud):
                                        for infoProcJud in infoPgto.infoProcJud:
                                            
                                            if 'nrProc' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.nrProc', 
                                                                                  infoProcJud.nrProc.cdata, 
                                                                                  1, u'None')
                                            
                                            if 'indOrigemRecursos' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.indOrigemRecursos', 
                                                                                  infoProcJud.indOrigemRecursos.cdata, 
                                                                                  1, u'1, 2')
                                            
                                            if 'desc' in dir(infoProcJud):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoProcJud.desc', 
                                                                                  infoProcJud.desc.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'despProcJud' in dir(infoProcJud.despProcJud):
                                                for despProcJud in infoProcJud.despProcJud:
                                                    
                                                    if 'vlrDespCustas' in dir(despProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'despProcJud.vlrDespCustas', 
                                                                                          despProcJud.vlrDespCustas.cdata, 
                                                                                          1, u'None')
                                                    
                                                    if 'vlrDespAdvogados' in dir(despProcJud):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'despProcJud.vlrDespAdvogados', 
                                                                                          despProcJud.vlrDespAdvogados.cdata, 
                                                                                          1, u'None')
                                                    
                                                    if 'ideAdv' in dir(despProcJud.ideAdv):
                                                        for ideAdv in despProcJud.ideAdv:
                                                            
                                                            if 'tpInscAdv' in dir(ideAdv):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'ideAdv.tpInscAdv', 
                                                                                                  ideAdv.tpInscAdv.cdata, 
                                                                                                  1, u'1, 2')
                                                            
                                                            if 'nrInscAdv' in dir(ideAdv):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'ideAdv.nrInscAdv', 
                                                                                                  ideAdv.nrInscAdv.cdata, 
                                                                                                  1, u'None')
                                                            
                                                            if 'vlrAdv' in dir(ideAdv):
                                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                                  'ideAdv.vlrAdv', 
                                                                                                  ideAdv.vlrAdv.cdata, 
                                                                                                  1, u'None')
                                            
                                            if 'origemRec' in dir(infoProcJud.origemRec):
                                                for origemRec in infoProcJud.origemRec:
                                                    
                                                    if 'cnpjOrigRecurso' in dir(origemRec):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'origemRec.cnpjOrigRecurso', 
                                                                                          origemRec.cnpjOrigRecurso.cdata, 
                                                                                          1, u'None')
                            
                            if 'infoPgtoExt' in dir(idePgto.infoPgtoExt):
                                for infoPgtoExt in idePgto.infoPgtoExt:
                                    
                                    if 'endExt' in dir(infoPgtoExt.endExt):
                                        for endExt in infoPgtoExt.endExt:
                                            
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
                                            
                                            if 'cidade' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.cidade', 
                                                                                  endExt.cidade.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'estado' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.estado', 
                                                                                  endExt.estado.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'codPostal' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.codPostal', 
                                                                                  endExt.codPostal.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'telef' in dir(endExt):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'endExt.telef', 
                                                                                  endExt.telef.cdata, 
                                                                                  0, u'None')
                                    
                                    if 'infoFiscal' in dir(infoPgtoExt.infoFiscal):
                                        for infoFiscal in infoPgtoExt.infoFiscal:
                                            
                                            if 'indNIF' in dir(infoFiscal):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoFiscal.indNIF', 
                                                                                  infoFiscal.indNIF.cdata, 
                                                                                  1, u'1, 2, 3')
                                            
                                            if 'nifBenef' in dir(infoFiscal):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoFiscal.nifBenef', 
                                                                                  infoFiscal.nifBenef.cdata, 
                                                                                  0, u'None')
                                            
                                            if 'relFontPg' in dir(infoFiscal):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoFiscal.relFontPg', 
                                                                                  infoFiscal.relFontPg.cdata, 
                                                                                  1, u'500, 510, 520, 530, 540, 550, 560, 570, 900')
                                            
                                            if 'frmTribut' in dir(infoFiscal):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'infoFiscal.frmTribut', 
                                                                                  infoFiscal.frmTribut.cdata, 
                                                                                  1, u'10, 11, 12, 13, 30, 40, 41, 42, 43, 44, 50')
    return validacoes_lista