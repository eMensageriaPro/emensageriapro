#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos <www.emensageria.com.br>
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


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def read_s1005_evttabestab_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1005_evttabestab_obj(doc, status, validar)
    return dados

def read_s1005_evttabestab(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s1005_evttabestab_obj(doc, status, validar)
    return dados



def read_s1005_evttabestab_obj(doc, status, validar=False):
    s1005_evttabestab_dados = {}
    s1005_evttabestab_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s1005_evttabestab_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1005_evttabestab_dados['identidade'] = doc.eSocial.evtTabEstab['Id']
    evtTabEstab = doc.eSocial.evtTabEstab

    try: s1005_evttabestab_dados['tpamb'] = evtTabEstab.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s1005_evttabestab_dados['procemi'] = evtTabEstab.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s1005_evttabestab_dados['verproc'] = evtTabEstab.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s1005_evttabestab_dados['tpinsc'] = evtTabEstab.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s1005_evttabestab_dados['nrinsc'] = evtTabEstab.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
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
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'inclusao' in dir(evtTabEstab.infoEstab) and evtTabEstab.infoEstab.inclusao.cdata != '':
        for inclusao in evtTabEstab.infoEstab.inclusao:
            s1005_inclusao_dados = {}
            s1005_inclusao_dados['s1005_evttabestab_id'] = s1005_evttabestab_id

            try: s1005_inclusao_dados['tpinsc'] = inclusao.ideEstab.tpInsc.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['nrinsc'] = inclusao.ideEstab.nrInsc.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['inivalid'] = inclusao.ideEstab.iniValid.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['fimvalid'] = inclusao.ideEstab.fimValid.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['cnaeprep'] = inclusao.dadosEstab.cnaePrep.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['aliqrat'] = inclusao.dadosEstab.aliqGilrat.aliqRat.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['fap'] = inclusao.dadosEstab.aliqGilrat.fap.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['aliqratajust'] = inclusao.dadosEstab.aliqGilrat.aliqRatAjust.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['regpt'] = inclusao.dadosEstab.infoTrab.regPt.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['contapr'] = inclusao.dadosEstab.infoTrab.infoApr.contApr.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['nrprocjud'] = inclusao.dadosEstab.infoTrab.infoApr.nrProcJud.cdata
            except AttributeError: pass
            try: s1005_inclusao_dados['contented'] = inclusao.dadosEstab.infoTrab.infoApr.contEntEd.cdata
            except AttributeError: pass
            insert = create_insert('s1005_inclusao', s1005_inclusao_dados)
            resp = executar_sql(insert, True)
            s1005_inclusao_id = resp[0][0]
            #print s1005_inclusao_id

            if 'procAdmJudRat' in dir(inclusao.dadosEstab.aliqGilrat) and inclusao.dadosEstab.aliqGilrat.procAdmJudRat.cdata != '':
                for procAdmJudRat in inclusao.dadosEstab.aliqGilrat.procAdmJudRat:
                    s1005_inclusao_procadmjudrat_dados = {}
                    s1005_inclusao_procadmjudrat_dados['s1005_inclusao_id'] = s1005_inclusao_id

                    try: s1005_inclusao_procadmjudrat_dados['tpproc'] = procAdmJudRat.tpProc.cdata
                    except AttributeError: pass
                    try: s1005_inclusao_procadmjudrat_dados['nrproc'] = procAdmJudRat.nrProc.cdata
                    except AttributeError: pass
                    try: s1005_inclusao_procadmjudrat_dados['codsusp'] = procAdmJudRat.codSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_inclusao_procadmjudrat', s1005_inclusao_procadmjudrat_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_procadmjudrat_id = resp[0][0]
                    #print s1005_inclusao_procadmjudrat_id

            if 'procAdmJudFap' in dir(inclusao.dadosEstab.aliqGilrat) and inclusao.dadosEstab.aliqGilrat.procAdmJudFap.cdata != '':
                for procAdmJudFap in inclusao.dadosEstab.aliqGilrat.procAdmJudFap:
                    s1005_inclusao_procadmjudfap_dados = {}
                    s1005_inclusao_procadmjudfap_dados['s1005_inclusao_id'] = s1005_inclusao_id

                    try: s1005_inclusao_procadmjudfap_dados['tpproc'] = procAdmJudFap.tpProc.cdata
                    except AttributeError: pass
                    try: s1005_inclusao_procadmjudfap_dados['nrproc'] = procAdmJudFap.nrProc.cdata
                    except AttributeError: pass
                    try: s1005_inclusao_procadmjudfap_dados['codsusp'] = procAdmJudFap.codSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_inclusao_procadmjudfap', s1005_inclusao_procadmjudfap_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_procadmjudfap_id = resp[0][0]
                    #print s1005_inclusao_procadmjudfap_id

            if 'infoCaepf' in dir(inclusao.dadosEstab) and inclusao.dadosEstab.infoCaepf.cdata != '':
                for infoCaepf in inclusao.dadosEstab.infoCaepf:
                    s1005_inclusao_infocaepf_dados = {}
                    s1005_inclusao_infocaepf_dados['s1005_inclusao_id'] = s1005_inclusao_id

                    try: s1005_inclusao_infocaepf_dados['tpcaepf'] = infoCaepf.tpCaepf.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_inclusao_infocaepf', s1005_inclusao_infocaepf_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_infocaepf_id = resp[0][0]
                    #print s1005_inclusao_infocaepf_id

            if 'infoObra' in dir(inclusao.dadosEstab) and inclusao.dadosEstab.infoObra.cdata != '':
                for infoObra in inclusao.dadosEstab.infoObra:
                    s1005_inclusao_infoobra_dados = {}
                    s1005_inclusao_infoobra_dados['s1005_inclusao_id'] = s1005_inclusao_id

                    try: s1005_inclusao_infoobra_dados['indsubstpatrobra'] = infoObra.indSubstPatrObra.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_inclusao_infoobra', s1005_inclusao_infoobra_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_infoobra_id = resp[0][0]
                    #print s1005_inclusao_infoobra_id

            if 'infoEntEduc' in dir(inclusao.dadosEstab.infoTrab.infoApr) and inclusao.dadosEstab.infoTrab.infoApr.infoEntEduc.cdata != '':
                for infoEntEduc in inclusao.dadosEstab.infoTrab.infoApr.infoEntEduc:
                    s1005_inclusao_infoenteduc_dados = {}
                    s1005_inclusao_infoenteduc_dados['s1005_inclusao_id'] = s1005_inclusao_id

                    try: s1005_inclusao_infoenteduc_dados['nrinsc'] = infoEntEduc.nrInsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_inclusao_infoenteduc', s1005_inclusao_infoenteduc_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_infoenteduc_id = resp[0][0]
                    #print s1005_inclusao_infoenteduc_id

            if 'infoPCD' in dir(inclusao.dadosEstab.infoTrab) and inclusao.dadosEstab.infoTrab.infoPCD.cdata != '':
                for infoPCD in inclusao.dadosEstab.infoTrab.infoPCD:
                    s1005_inclusao_infopcd_dados = {}
                    s1005_inclusao_infopcd_dados['s1005_inclusao_id'] = s1005_inclusao_id

                    try: s1005_inclusao_infopcd_dados['contpcd'] = infoPCD.contPCD.cdata
                    except AttributeError: pass
                    try: s1005_inclusao_infopcd_dados['nrprocjud'] = infoPCD.nrProcJud.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_inclusao_infopcd', s1005_inclusao_infopcd_dados)
                    resp = executar_sql(insert, True)
                    s1005_inclusao_infopcd_id = resp[0][0]
                    #print s1005_inclusao_infopcd_id

    if 'alteracao' in dir(evtTabEstab.infoEstab) and evtTabEstab.infoEstab.alteracao.cdata != '':
        for alteracao in evtTabEstab.infoEstab.alteracao:
            s1005_alteracao_dados = {}
            s1005_alteracao_dados['s1005_evttabestab_id'] = s1005_evttabestab_id

            try: s1005_alteracao_dados['tpinsc'] = alteracao.ideEstab.tpInsc.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['nrinsc'] = alteracao.ideEstab.nrInsc.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['inivalid'] = alteracao.ideEstab.iniValid.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['fimvalid'] = alteracao.ideEstab.fimValid.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['cnaeprep'] = alteracao.dadosEstab.cnaePrep.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['aliqrat'] = alteracao.dadosEstab.aliqGilrat.aliqRat.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['fap'] = alteracao.dadosEstab.aliqGilrat.fap.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['aliqratajust'] = alteracao.dadosEstab.aliqGilrat.aliqRatAjust.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['regpt'] = alteracao.dadosEstab.infoTrab.regPt.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['contapr'] = alteracao.dadosEstab.infoTrab.infoApr.contApr.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['nrprocjud'] = alteracao.dadosEstab.infoTrab.infoApr.nrProcJud.cdata
            except AttributeError: pass
            try: s1005_alteracao_dados['contented'] = alteracao.dadosEstab.infoTrab.infoApr.contEntEd.cdata
            except AttributeError: pass
            insert = create_insert('s1005_alteracao', s1005_alteracao_dados)
            resp = executar_sql(insert, True)
            s1005_alteracao_id = resp[0][0]
            #print s1005_alteracao_id

            if 'procAdmJudRat' in dir(alteracao.dadosEstab.aliqGilrat) and alteracao.dadosEstab.aliqGilrat.procAdmJudRat.cdata != '':
                for procAdmJudRat in alteracao.dadosEstab.aliqGilrat.procAdmJudRat:
                    s1005_alteracao_procadmjudrat_dados = {}
                    s1005_alteracao_procadmjudrat_dados['s1005_alteracao_id'] = s1005_alteracao_id

                    try: s1005_alteracao_procadmjudrat_dados['tpproc'] = procAdmJudRat.tpProc.cdata
                    except AttributeError: pass
                    try: s1005_alteracao_procadmjudrat_dados['nrproc'] = procAdmJudRat.nrProc.cdata
                    except AttributeError: pass
                    try: s1005_alteracao_procadmjudrat_dados['codsusp'] = procAdmJudRat.codSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_alteracao_procadmjudrat', s1005_alteracao_procadmjudrat_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_procadmjudrat_id = resp[0][0]
                    #print s1005_alteracao_procadmjudrat_id

            if 'procAdmJudFap' in dir(alteracao.dadosEstab.aliqGilrat) and alteracao.dadosEstab.aliqGilrat.procAdmJudFap.cdata != '':
                for procAdmJudFap in alteracao.dadosEstab.aliqGilrat.procAdmJudFap:
                    s1005_alteracao_procadmjudfap_dados = {}
                    s1005_alteracao_procadmjudfap_dados['s1005_alteracao_id'] = s1005_alteracao_id

                    try: s1005_alteracao_procadmjudfap_dados['tpproc'] = procAdmJudFap.tpProc.cdata
                    except AttributeError: pass
                    try: s1005_alteracao_procadmjudfap_dados['nrproc'] = procAdmJudFap.nrProc.cdata
                    except AttributeError: pass
                    try: s1005_alteracao_procadmjudfap_dados['codsusp'] = procAdmJudFap.codSusp.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_alteracao_procadmjudfap', s1005_alteracao_procadmjudfap_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_procadmjudfap_id = resp[0][0]
                    #print s1005_alteracao_procadmjudfap_id

            if 'infoCaepf' in dir(alteracao.dadosEstab) and alteracao.dadosEstab.infoCaepf.cdata != '':
                for infoCaepf in alteracao.dadosEstab.infoCaepf:
                    s1005_alteracao_infocaepf_dados = {}
                    s1005_alteracao_infocaepf_dados['s1005_alteracao_id'] = s1005_alteracao_id

                    try: s1005_alteracao_infocaepf_dados['tpcaepf'] = infoCaepf.tpCaepf.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_alteracao_infocaepf', s1005_alteracao_infocaepf_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_infocaepf_id = resp[0][0]
                    #print s1005_alteracao_infocaepf_id

            if 'infoObra' in dir(alteracao.dadosEstab) and alteracao.dadosEstab.infoObra.cdata != '':
                for infoObra in alteracao.dadosEstab.infoObra:
                    s1005_alteracao_infoobra_dados = {}
                    s1005_alteracao_infoobra_dados['s1005_alteracao_id'] = s1005_alteracao_id

                    try: s1005_alteracao_infoobra_dados['indsubstpatrobra'] = infoObra.indSubstPatrObra.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_alteracao_infoobra', s1005_alteracao_infoobra_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_infoobra_id = resp[0][0]
                    #print s1005_alteracao_infoobra_id

            if 'infoEntEduc' in dir(alteracao.dadosEstab.infoTrab.infoApr) and alteracao.dadosEstab.infoTrab.infoApr.infoEntEduc.cdata != '':
                for infoEntEduc in alteracao.dadosEstab.infoTrab.infoApr.infoEntEduc:
                    s1005_alteracao_infoenteduc_dados = {}
                    s1005_alteracao_infoenteduc_dados['s1005_alteracao_id'] = s1005_alteracao_id

                    try: s1005_alteracao_infoenteduc_dados['nrinsc'] = infoEntEduc.nrInsc.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_alteracao_infoenteduc', s1005_alteracao_infoenteduc_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_infoenteduc_id = resp[0][0]
                    #print s1005_alteracao_infoenteduc_id

            if 'infoPCD' in dir(alteracao.dadosEstab.infoTrab) and alteracao.dadosEstab.infoTrab.infoPCD.cdata != '':
                for infoPCD in alteracao.dadosEstab.infoTrab.infoPCD:
                    s1005_alteracao_infopcd_dados = {}
                    s1005_alteracao_infopcd_dados['s1005_alteracao_id'] = s1005_alteracao_id

                    try: s1005_alteracao_infopcd_dados['contpcd'] = infoPCD.contPCD.cdata
                    except AttributeError: pass
                    try: s1005_alteracao_infopcd_dados['nrprocjud'] = infoPCD.nrProcJud.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_alteracao_infopcd', s1005_alteracao_infopcd_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_infopcd_id = resp[0][0]
                    #print s1005_alteracao_infopcd_id

            if 'novaValidade' in dir(alteracao) and alteracao.novaValidade.cdata != '':
                for novaValidade in alteracao.novaValidade:
                    s1005_alteracao_novavalidade_dados = {}
                    s1005_alteracao_novavalidade_dados['s1005_alteracao_id'] = s1005_alteracao_id

                    try: s1005_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: pass
                    try: s1005_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: pass
                    insert = create_insert('s1005_alteracao_novavalidade', s1005_alteracao_novavalidade_dados)
                    resp = executar_sql(insert, True)
                    s1005_alteracao_novavalidade_id = resp[0][0]
                    #print s1005_alteracao_novavalidade_id

    if 'exclusao' in dir(evtTabEstab.infoEstab) and evtTabEstab.infoEstab.exclusao.cdata != '':
        for exclusao in evtTabEstab.infoEstab.exclusao:
            s1005_exclusao_dados = {}
            s1005_exclusao_dados['s1005_evttabestab_id'] = s1005_evttabestab_id

            try: s1005_exclusao_dados['tpinsc'] = exclusao.ideEstab.tpInsc.cdata
            except AttributeError: pass
            try: s1005_exclusao_dados['nrinsc'] = exclusao.ideEstab.nrInsc.cdata
            except AttributeError: pass
            try: s1005_exclusao_dados['inivalid'] = exclusao.ideEstab.iniValid.cdata
            except AttributeError: pass
            try: s1005_exclusao_dados['fimvalid'] = exclusao.ideEstab.fimValid.cdata
            except AttributeError: pass
            insert = create_insert('s1005_exclusao', s1005_exclusao_dados)
            resp = executar_sql(insert, True)
            s1005_exclusao_id = resp[0][0]
            #print s1005_exclusao_id

    from emensageriapro.esocial.views.s1005_evttabestab_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s1005_evttabestab_id, 'default')
    return dados