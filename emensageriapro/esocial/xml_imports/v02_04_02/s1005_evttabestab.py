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
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql


def read_s1005_evttabestab(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = 1
    else:
        status = 0
    read_s1005_evttabestab_obj(doc, status)



def read_s1005_evttabestab_obj(doc):
    s1005_evttabestab_dados = {}
    s1005_evttabestab_dados['versao'] = 'v02_04_02'
    s1005_evttabestab_dados['status'] = status
    s1005_evttabestab_dados['identidade'] = doc.eSocial.evtTabEstab['Id']
    s1005_evttabestab_dados['processamento_codigo_resposta'] = 1
    evtTabEstab = doc.eSocial.evtTabEstab
    
    if 'tpAmb' in dir(evtTabEstab.ideEvento): s1005_evttabestab_dados['tpamb'] = evtTabEstab.ideEvento.tpAmb.cdata
    if 'procEmi' in dir(evtTabEstab.ideEvento): s1005_evttabestab_dados['procemi'] = evtTabEstab.ideEvento.procEmi.cdata
    if 'verProc' in dir(evtTabEstab.ideEvento): s1005_evttabestab_dados['verproc'] = evtTabEstab.ideEvento.verProc.cdata
    if 'tpInsc' in dir(evtTabEstab.ideEmpregador): s1005_evttabestab_dados['tpinsc'] = evtTabEstab.ideEmpregador.tpInsc.cdata
    if 'nrInsc' in dir(evtTabEstab.ideEmpregador): s1005_evttabestab_dados['nrinsc'] = evtTabEstab.ideEmpregador.nrInsc.cdata
    if 'inclusao' in dir(evtTabEstab.infoEstab): s1005_evttabestab_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabEstab.infoEstab): s1005_evttabestab_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabEstab.infoEstab): s1005_evttabestab_dados['operacao'] = 3
    #print dados
    insert = create_insert('s1005_evttabestab', s1005_evttabestab_dados)
    resp = executar_sql(insert, True)
    s1005_evttabestab_id = resp[0][0]
    dados = s1005_evttabestab_dados
    dados['evento'] = 's1005'
    dados['id'] = s1005_evttabestab_id
    dados['identidade_evento'] = doc.eSocial.evtTabEstab['Id']
    dados['status'] = 1

    if 'inclusao' in dir(evtTabEstab.infoEstab):
        for inclusao in evtTabEstab.infoEstab.inclusao:
            s1005_inclusao_dados = {}
            s1005_inclusao_dados['s1005_evttabestab_id'] = s1005_evttabestab_id
            
            if 'tpInsc' in dir(inclusao.ideEstab): s1005_inclusao_dados['tpinsc'] = inclusao.ideEstab.tpInsc.cdata
            if 'nrInsc' in dir(inclusao.ideEstab): s1005_inclusao_dados['nrinsc'] = inclusao.ideEstab.nrInsc.cdata
            if 'iniValid' in dir(inclusao.ideEstab): s1005_inclusao_dados['inivalid'] = inclusao.ideEstab.iniValid.cdata
            if 'fimValid' in dir(inclusao.ideEstab): s1005_inclusao_dados['fimvalid'] = inclusao.ideEstab.fimValid.cdata
            if 'cnaePrep' in dir(inclusao.dadosEstab): s1005_inclusao_dados['cnaeprep'] = inclusao.dadosEstab.cnaePrep.cdata
            if 'aliqRat' in dir(inclusao.dadosEstab.aliqGilrat): s1005_inclusao_dados['aliqrat'] = inclusao.dadosEstab.aliqGilrat.aliqRat.cdata
            if 'fap' in dir(inclusao.dadosEstab.aliqGilrat): s1005_inclusao_dados['fap'] = inclusao.dadosEstab.aliqGilrat.fap.cdata
            if 'aliqRatAjust' in dir(inclusao.dadosEstab.aliqGilrat): s1005_inclusao_dados['aliqratajust'] = inclusao.dadosEstab.aliqGilrat.aliqRatAjust.cdata
            if 'regPt' in dir(inclusao.dadosEstab.infoTrab): s1005_inclusao_dados['regpt'] = inclusao.dadosEstab.infoTrab.regPt.cdata
            if 'contApr' in dir(inclusao.dadosEstab.infoTrab.infoApr): s1005_inclusao_dados['contapr'] = inclusao.dadosEstab.infoTrab.infoApr.contApr.cdata
            if 'nrProcJud' in dir(inclusao.dadosEstab.infoTrab.infoApr): s1005_inclusao_dados['nrprocjud'] = inclusao.dadosEstab.infoTrab.infoApr.nrProcJud.cdata
            if 'contEntEd' in dir(inclusao.dadosEstab.infoTrab.infoApr): s1005_inclusao_dados['contented'] = inclusao.dadosEstab.infoTrab.infoApr.contEntEd.cdata
            insert = create_insert('s1005_inclusao', s1005_inclusao_dados)
            resp = executar_sql(insert, True)
            s1005_inclusao_id = resp[0][0]
            #print s1005_inclusao_id

            if 'procAdmJudRat' in dir(inclusao.dadosEstab.aliqGilrat):
                for procAdmJudRat in inclusao.dadosEstab.aliqGilrat.procAdmJudRat:
                    s1005_inclusao_procadmjudrat_dados = {}
                    s1005_inclusao_procadmjudrat_dados['s1005_inclusao_id'] = s1005_inclusao_id
                    
                    if 'tpProc' in dir(procAdmJudRat): s1005_inclusao_procadmjudrat_dados['tpproc'] = procAdmJudRat.tpProc.cdata
                    if 'nrProc' in dir(procAdmJudRat): s1005_inclusao_procadmjudrat_dados['nrproc'] = procAdmJudRat.nrProc.cdata
                    if 'codSusp' in dir(procAdmJudRat): s1005_inclusao_procadmjudrat_dados['codsusp'] = procAdmJudRat.codSusp.cdata
                    insert = create_insert('s1005_inclusao_procadmjudrat', s1005_inclusao_procadmjudrat_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_procadmjudrat_id = resp[0][0]
                    #print s1005_inclusao_procadmjudrat_id
        
            if 'procAdmJudFap' in dir(inclusao.dadosEstab.aliqGilrat):
                for procAdmJudFap in inclusao.dadosEstab.aliqGilrat.procAdmJudFap:
                    s1005_inclusao_procadmjudfap_dados = {}
                    s1005_inclusao_procadmjudfap_dados['s1005_inclusao_id'] = s1005_inclusao_id
                    
                    if 'tpProc' in dir(procAdmJudFap): s1005_inclusao_procadmjudfap_dados['tpproc'] = procAdmJudFap.tpProc.cdata
                    if 'nrProc' in dir(procAdmJudFap): s1005_inclusao_procadmjudfap_dados['nrproc'] = procAdmJudFap.nrProc.cdata
                    if 'codSusp' in dir(procAdmJudFap): s1005_inclusao_procadmjudfap_dados['codsusp'] = procAdmJudFap.codSusp.cdata
                    insert = create_insert('s1005_inclusao_procadmjudfap', s1005_inclusao_procadmjudfap_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_procadmjudfap_id = resp[0][0]
                    #print s1005_inclusao_procadmjudfap_id
        
            if 'infoCaepf' in dir(inclusao.dadosEstab):
                for infoCaepf in inclusao.dadosEstab.infoCaepf:
                    s1005_inclusao_infocaepf_dados = {}
                    s1005_inclusao_infocaepf_dados['s1005_inclusao_id'] = s1005_inclusao_id
                    
                    if 'tpCaepf' in dir(infoCaepf): s1005_inclusao_infocaepf_dados['tpcaepf'] = infoCaepf.tpCaepf.cdata
                    insert = create_insert('s1005_inclusao_infocaepf', s1005_inclusao_infocaepf_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_infocaepf_id = resp[0][0]
                    #print s1005_inclusao_infocaepf_id
        
            if 'infoObra' in dir(inclusao.dadosEstab):
                for infoObra in inclusao.dadosEstab.infoObra:
                    s1005_inclusao_infoobra_dados = {}
                    s1005_inclusao_infoobra_dados['s1005_inclusao_id'] = s1005_inclusao_id
                    
                    if 'indSubstPatrObra' in dir(infoObra): s1005_inclusao_infoobra_dados['indsubstpatrobra'] = infoObra.indSubstPatrObra.cdata
                    insert = create_insert('s1005_inclusao_infoobra', s1005_inclusao_infoobra_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_infoobra_id = resp[0][0]
                    #print s1005_inclusao_infoobra_id
        
            if 'infoEntEduc' in dir(inclusao.dadosEstab.infoTrab.infoApr):
                for infoEntEduc in inclusao.dadosEstab.infoTrab.infoApr.infoEntEduc:
                    s1005_inclusao_infoenteduc_dados = {}
                    s1005_inclusao_infoenteduc_dados['s1005_inclusao_id'] = s1005_inclusao_id
                    
                    if 'nrInsc' in dir(infoEntEduc): s1005_inclusao_infoenteduc_dados['nrinsc'] = infoEntEduc.nrInsc.cdata
                    insert = create_insert('s1005_inclusao_infoenteduc', s1005_inclusao_infoenteduc_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_infoenteduc_id = resp[0][0]
                    #print s1005_inclusao_infoenteduc_id
        
            if 'infoPCD' in dir(inclusao.dadosEstab.infoTrab):
                for infoPCD in inclusao.dadosEstab.infoTrab.infoPCD:
                    s1005_inclusao_infopcd_dados = {}
                    s1005_inclusao_infopcd_dados['s1005_inclusao_id'] = s1005_inclusao_id
                    
                    if 'contPCD' in dir(infoPCD): s1005_inclusao_infopcd_dados['contpcd'] = infoPCD.contPCD.cdata
                    if 'nrProcJud' in dir(infoPCD): s1005_inclusao_infopcd_dados['nrprocjud'] = infoPCD.nrProcJud.cdata
                    insert = create_insert('s1005_inclusao_infopcd', s1005_inclusao_infopcd_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_infopcd_id = resp[0][0]
                    #print s1005_inclusao_infopcd_id
        
    if 'alteracao' in dir(evtTabEstab.infoEstab):
        for alteracao in evtTabEstab.infoEstab.alteracao:
            s1005_alteracao_dados = {}
            s1005_alteracao_dados['s1005_evttabestab_id'] = s1005_evttabestab_id
            
            if 'tpInsc' in dir(alteracao.ideEstab): s1005_alteracao_dados['tpinsc'] = alteracao.ideEstab.tpInsc.cdata
            if 'nrInsc' in dir(alteracao.ideEstab): s1005_alteracao_dados['nrinsc'] = alteracao.ideEstab.nrInsc.cdata
            if 'iniValid' in dir(alteracao.ideEstab): s1005_alteracao_dados['inivalid'] = alteracao.ideEstab.iniValid.cdata
            if 'fimValid' in dir(alteracao.ideEstab): s1005_alteracao_dados['fimvalid'] = alteracao.ideEstab.fimValid.cdata
            if 'cnaePrep' in dir(alteracao.dadosEstab): s1005_alteracao_dados['cnaeprep'] = alteracao.dadosEstab.cnaePrep.cdata
            if 'aliqRat' in dir(alteracao.dadosEstab.aliqGilrat): s1005_alteracao_dados['aliqrat'] = alteracao.dadosEstab.aliqGilrat.aliqRat.cdata
            if 'fap' in dir(alteracao.dadosEstab.aliqGilrat): s1005_alteracao_dados['fap'] = alteracao.dadosEstab.aliqGilrat.fap.cdata
            if 'aliqRatAjust' in dir(alteracao.dadosEstab.aliqGilrat): s1005_alteracao_dados['aliqratajust'] = alteracao.dadosEstab.aliqGilrat.aliqRatAjust.cdata
            if 'regPt' in dir(alteracao.dadosEstab.infoTrab): s1005_alteracao_dados['regpt'] = alteracao.dadosEstab.infoTrab.regPt.cdata
            if 'contApr' in dir(alteracao.dadosEstab.infoTrab.infoApr): s1005_alteracao_dados['contapr'] = alteracao.dadosEstab.infoTrab.infoApr.contApr.cdata
            if 'nrProcJud' in dir(alteracao.dadosEstab.infoTrab.infoApr): s1005_alteracao_dados['nrprocjud'] = alteracao.dadosEstab.infoTrab.infoApr.nrProcJud.cdata
            if 'contEntEd' in dir(alteracao.dadosEstab.infoTrab.infoApr): s1005_alteracao_dados['contented'] = alteracao.dadosEstab.infoTrab.infoApr.contEntEd.cdata
            insert = create_insert('s1005_alteracao', s1005_alteracao_dados)
            resp = executar_sql(insert, True)
            s1005_alteracao_id = resp[0][0]
            #print s1005_alteracao_id

            if 'procAdmJudRat' in dir(alteracao.dadosEstab.aliqGilrat):
                for procAdmJudRat in alteracao.dadosEstab.aliqGilrat.procAdmJudRat:
                    s1005_alteracao_procadmjudrat_dados = {}
                    s1005_alteracao_procadmjudrat_dados['s1005_alteracao_id'] = s1005_alteracao_id
                    
                    if 'tpProc' in dir(procAdmJudRat): s1005_alteracao_procadmjudrat_dados['tpproc'] = procAdmJudRat.tpProc.cdata
                    if 'nrProc' in dir(procAdmJudRat): s1005_alteracao_procadmjudrat_dados['nrproc'] = procAdmJudRat.nrProc.cdata
                    if 'codSusp' in dir(procAdmJudRat): s1005_alteracao_procadmjudrat_dados['codsusp'] = procAdmJudRat.codSusp.cdata
                    insert = create_insert('s1005_alteracao_procadmjudrat', s1005_alteracao_procadmjudrat_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_procadmjudrat_id = resp[0][0]
                    #print s1005_alteracao_procadmjudrat_id
        
            if 'procAdmJudFap' in dir(alteracao.dadosEstab.aliqGilrat):
                for procAdmJudFap in alteracao.dadosEstab.aliqGilrat.procAdmJudFap:
                    s1005_alteracao_procadmjudfap_dados = {}
                    s1005_alteracao_procadmjudfap_dados['s1005_alteracao_id'] = s1005_alteracao_id
                    
                    if 'tpProc' in dir(procAdmJudFap): s1005_alteracao_procadmjudfap_dados['tpproc'] = procAdmJudFap.tpProc.cdata
                    if 'nrProc' in dir(procAdmJudFap): s1005_alteracao_procadmjudfap_dados['nrproc'] = procAdmJudFap.nrProc.cdata
                    if 'codSusp' in dir(procAdmJudFap): s1005_alteracao_procadmjudfap_dados['codsusp'] = procAdmJudFap.codSusp.cdata
                    insert = create_insert('s1005_alteracao_procadmjudfap', s1005_alteracao_procadmjudfap_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_procadmjudfap_id = resp[0][0]
                    #print s1005_alteracao_procadmjudfap_id
        
            if 'infoCaepf' in dir(alteracao.dadosEstab):
                for infoCaepf in alteracao.dadosEstab.infoCaepf:
                    s1005_alteracao_infocaepf_dados = {}
                    s1005_alteracao_infocaepf_dados['s1005_alteracao_id'] = s1005_alteracao_id
                    
                    if 'tpCaepf' in dir(infoCaepf): s1005_alteracao_infocaepf_dados['tpcaepf'] = infoCaepf.tpCaepf.cdata
                    insert = create_insert('s1005_alteracao_infocaepf', s1005_alteracao_infocaepf_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_infocaepf_id = resp[0][0]
                    #print s1005_alteracao_infocaepf_id
        
            if 'infoObra' in dir(alteracao.dadosEstab):
                for infoObra in alteracao.dadosEstab.infoObra:
                    s1005_alteracao_infoobra_dados = {}
                    s1005_alteracao_infoobra_dados['s1005_alteracao_id'] = s1005_alteracao_id
                    
                    if 'indSubstPatrObra' in dir(infoObra): s1005_alteracao_infoobra_dados['indsubstpatrobra'] = infoObra.indSubstPatrObra.cdata
                    insert = create_insert('s1005_alteracao_infoobra', s1005_alteracao_infoobra_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_infoobra_id = resp[0][0]
                    #print s1005_alteracao_infoobra_id
        
            if 'infoEntEduc' in dir(alteracao.dadosEstab.infoTrab.infoApr):
                for infoEntEduc in alteracao.dadosEstab.infoTrab.infoApr.infoEntEduc:
                    s1005_alteracao_infoenteduc_dados = {}
                    s1005_alteracao_infoenteduc_dados['s1005_alteracao_id'] = s1005_alteracao_id
                    
                    if 'nrInsc' in dir(infoEntEduc): s1005_alteracao_infoenteduc_dados['nrinsc'] = infoEntEduc.nrInsc.cdata
                    insert = create_insert('s1005_alteracao_infoenteduc', s1005_alteracao_infoenteduc_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_infoenteduc_id = resp[0][0]
                    #print s1005_alteracao_infoenteduc_id
        
            if 'infoPCD' in dir(alteracao.dadosEstab.infoTrab):
                for infoPCD in alteracao.dadosEstab.infoTrab.infoPCD:
                    s1005_alteracao_infopcd_dados = {}
                    s1005_alteracao_infopcd_dados['s1005_alteracao_id'] = s1005_alteracao_id
                    
                    if 'contPCD' in dir(infoPCD): s1005_alteracao_infopcd_dados['contpcd'] = infoPCD.contPCD.cdata
                    if 'nrProcJud' in dir(infoPCD): s1005_alteracao_infopcd_dados['nrprocjud'] = infoPCD.nrProcJud.cdata
                    insert = create_insert('s1005_alteracao_infopcd', s1005_alteracao_infopcd_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_infopcd_id = resp[0][0]
                    #print s1005_alteracao_infopcd_id
        
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    s1005_alteracao_novavalidade_dados = {}
                    s1005_alteracao_novavalidade_dados['s1005_alteracao_id'] = s1005_alteracao_id
                    
                    if 'iniValid' in dir(novaValidade): s1005_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    if 'fimValid' in dir(novaValidade): s1005_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    insert = create_insert('s1005_alteracao_novavalidade', s1005_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_novavalidade_id = resp[0][0]
                    #print s1005_alteracao_novavalidade_id
        
    if 'exclusao' in dir(evtTabEstab.infoEstab):
        for exclusao in evtTabEstab.infoEstab.exclusao:
            s1005_exclusao_dados = {}
            s1005_exclusao_dados['s1005_evttabestab_id'] = s1005_evttabestab_id
            
            if 'tpInsc' in dir(exclusao.ideEstab): s1005_exclusao_dados['tpinsc'] = exclusao.ideEstab.tpInsc.cdata
            if 'nrInsc' in dir(exclusao.ideEstab): s1005_exclusao_dados['nrinsc'] = exclusao.ideEstab.nrInsc.cdata
            if 'iniValid' in dir(exclusao.ideEstab): s1005_exclusao_dados['inivalid'] = exclusao.ideEstab.iniValid.cdata
            if 'fimValid' in dir(exclusao.ideEstab): s1005_exclusao_dados['fimvalid'] = exclusao.ideEstab.fimValid.cdata
            insert = create_insert('s1005_exclusao', s1005_exclusao_dados)
            resp = executar_sql(insert, True)
            s1005_exclusao_id = resp[0][0]
            #print s1005_exclusao_id

    from emensageriapro.esocial.views.s1005_evttabestab_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1005_evttabestab_id, 'default')
    return dados