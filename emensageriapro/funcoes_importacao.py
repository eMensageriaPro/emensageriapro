#coding:utf-8

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

import psycopg2
import datetime
import os
from padrao import ler_arquivo
from emensageriapro.funcoes_validacoes import validar_schema
from emensageriapro.certificado import CERT, CERT_HOST, CERT_PASS





def get_versao_evento(texto):
    texto = texto.replace('/">', '">')
    a = texto.split('">')
    b = a[0].split('/')
    return b[len(b)-1]


def get_identidade_evento(texto):
    texto = texto.replace('/">', '">').replace('id=', 'Id=')
    a = texto.split('Id="')
    b = a[1].split('"')
    return b[0]









def atualizar_tabela(tabela, dados, arquivo):
    from emensageriapro.padrao import executar_sql
    #print dados
    dados['tabela'] = tabela
    dados['arquivo'] = arquivo
    dados['status'] = 1
    executar_sql("""
        UPDATE public.%(tabela)s 
        SET status=%(status)s, arquivo_original=1, arquivo='%(arquivo)s'
        WHERE id=%(identidade)s""" % (dados), False)
    return dados





def importar_arquivo(arquivo, request, validar=0):
    from emensageriapro.settings import BASE_DIR
    from django.contrib import messages
    import untangle
    quant_erros = 0
    error_list = 0
    import os
    dados = {}
    if not os.path.isfile(BASE_DIR+'/'+arquivo):
        messages.error(request, 'Arquivo não encontrado!')
        return dados
    xml = ler_arquivo(arquivo).replace("s:", "")
    
    try:
        doc = untangle.parse(xml)
        dados['status'] = 1
    except:
        messages.error(request, 'Erro na importação. Arquivo XML inválido!')
        dados['status'] = 2
        return dados

    if dados['status'] == 1:

        if 'eSocial' in xml:
            xmlns = doc.eSocial['xmlns'].split('/')
            dados['versao'] = get_versao_evento(xml)
            from emensageriapro.esocial.xml_imports.v02_04_02.s1000_evtinfoempregador import read_s1000_evtinfoempregador
            from emensageriapro.esocial.xml_imports.v02_04_02.s1005_evttabestab import read_s1005_evttabestab
            from emensageriapro.esocial.xml_imports.v02_04_02.s1010_evttabrubrica import read_s1010_evttabrubrica
            from emensageriapro.esocial.xml_imports.v02_04_02.s1020_evttablotacao import read_s1020_evttablotacao
            from emensageriapro.esocial.xml_imports.v02_04_02.s1030_evttabcargo import read_s1030_evttabcargo
            from emensageriapro.esocial.xml_imports.v02_04_02.s1035_evttabcarreira import read_s1035_evttabcarreira
            from emensageriapro.esocial.xml_imports.v02_04_02.s1040_evttabfuncao import read_s1040_evttabfuncao
            from emensageriapro.esocial.xml_imports.v02_04_02.s1050_evttabhortur import read_s1050_evttabhortur
            from emensageriapro.esocial.xml_imports.v02_04_02.s1060_evttabambiente import read_s1060_evttabambiente
            from emensageriapro.esocial.xml_imports.v02_04_02.s1070_evttabprocesso import read_s1070_evttabprocesso
            from emensageriapro.esocial.xml_imports.v02_04_02.s1080_evttaboperport import read_s1080_evttaboperport
            from emensageriapro.esocial.xml_imports.v02_04_02.s1200_evtremun import read_s1200_evtremun
            from emensageriapro.esocial.xml_imports.v02_04_02.s1202_evtrmnrpps import read_s1202_evtrmnrpps
            from emensageriapro.esocial.xml_imports.v02_04_02.s1207_evtbenprrp import read_s1207_evtbenprrp
            from emensageriapro.esocial.xml_imports.v02_04_02.s1210_evtpgtos import read_s1210_evtpgtos
            from emensageriapro.esocial.xml_imports.v02_04_02.s1250_evtaqprod import read_s1250_evtaqprod
            from emensageriapro.esocial.xml_imports.v02_04_02.s1260_evtcomprod import read_s1260_evtcomprod
            from emensageriapro.esocial.xml_imports.v02_04_02.s1270_evtcontratavnp import read_s1270_evtcontratavnp
            from emensageriapro.esocial.xml_imports.v02_04_02.s1280_evtinfocomplper import read_s1280_evtinfocomplper
            from emensageriapro.esocial.xml_imports.v02_04_02.s1295_evttotconting import read_s1295_evttotconting
            from emensageriapro.esocial.xml_imports.v02_04_02.s1298_evtreabreevper import read_s1298_evtreabreevper
            from emensageriapro.esocial.xml_imports.v02_04_02.s1299_evtfechaevper import read_s1299_evtfechaevper
            from emensageriapro.esocial.xml_imports.v02_04_02.s1300_evtcontrsindpatr import read_s1300_evtcontrsindpatr
            from emensageriapro.esocial.xml_imports.v02_04_02.s2190_evtadmprelim import read_s2190_evtadmprelim
            from emensageriapro.esocial.xml_imports.v02_04_02.s2200_evtadmissao import read_s2200_evtadmissao
            from emensageriapro.esocial.xml_imports.v02_04_02.s2205_evtaltcadastral import read_s2205_evtaltcadastral
            from emensageriapro.esocial.xml_imports.v02_04_02.s2206_evtaltcontratual import read_s2206_evtaltcontratual
            from emensageriapro.esocial.xml_imports.v02_04_02.s2210_evtcat import read_s2210_evtcat
            from emensageriapro.esocial.xml_imports.v02_04_02.s2220_evtmonit import read_s2220_evtmonit
            from emensageriapro.esocial.xml_imports.v02_04_02.s2230_evtafasttemp import read_s2230_evtafasttemp
            from emensageriapro.esocial.xml_imports.v02_04_02.s2240_evtexprisco import read_s2240_evtexprisco
            from emensageriapro.esocial.xml_imports.v02_04_02.s2241_evtinsapo import read_s2241_evtinsapo
            from emensageriapro.esocial.xml_imports.v02_04_02.s2250_evtavprevio import read_s2250_evtavprevio
            from emensageriapro.esocial.xml_imports.v02_04_02.s2260_evtconvinterm import read_s2260_evtconvinterm
            from emensageriapro.esocial.xml_imports.v02_04_02.s2298_evtreintegr import read_s2298_evtreintegr
            from emensageriapro.esocial.xml_imports.v02_04_02.s2299_evtdeslig import read_s2299_evtdeslig
            from emensageriapro.esocial.xml_imports.v02_04_02.s2300_evttsvinicio import read_s2300_evttsvinicio
            from emensageriapro.esocial.xml_imports.v02_04_02.s2306_evttsvaltcontr import read_s2306_evttsvaltcontr
            from emensageriapro.esocial.xml_imports.v02_04_02.s2399_evttsvtermino import read_s2399_evttsvtermino
            #from emensageriapro.esocial.xml_imports.v02_04_02.s2400_evtcdbenefin import read_s2400_evtcdbenefin
            from emensageriapro.esocial.xml_imports.v02_04_02.s3000_evtexclusao import read_s3000_evtexclusao
            from emensageriapro.esocial.xml_imports.v02_04_02.s5001_evtbasestrab import read_s5001_evtbasestrab
            from emensageriapro.esocial.xml_imports.v02_04_02.s5002_evtirrfbenef import read_s5002_evtirrfbenef
            from emensageriapro.esocial.xml_imports.v02_04_02.s5011_evtcs import read_s5011_evtcs
            from emensageriapro.esocial.xml_imports.v02_04_02.s5012_evtirrf import read_s5012_evtirrf

            if ('evtInfoEmpregador' in xml) and ('eSocial' in xml):
                dados = read_s1000_evtinfoempregador(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1000_evtinfoempregador', dados, arquivo)

            elif ('evtTabEstab' in xml) and ('eSocial' in xml):
                dados = read_s1005_evttabestab(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1005_evttabestab', dados, arquivo)

            elif ('evtTabRubrica' in xml) and ('eSocial' in xml):
                dados = read_s1010_evttabrubrica(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1010_evttabrubrica', dados, arquivo)

            elif ('evtTabLotacao' in xml) and ('eSocial' in xml):
                dados = read_s1020_evttablotacao(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1020_evttablotacao', dados, arquivo)

            elif ('evtTabCargo' in xml) and ('eSocial' in xml):
                dados = read_s1030_evttabcargo(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1030_evttabcargo', dados, arquivo)

            elif ('evtTabCarreira' in xml) and ('eSocial' in xml):
                dados = read_s1035_evttabcarreira(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1035_evttabcarreira', dados, arquivo)

            elif ('evtTabFuncao' in xml) and ('eSocial' in xml):
                dados = read_s1040_evttabfuncao(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1040_evttabfuncao', dados, arquivo)

            elif ('evtTabHorTur' in xml) and ('eSocial' in xml):
                dados = read_s1050_evttabhortur(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1050_evttabhortur', dados, arquivo)

            elif ('evtTabAmbiente' in xml) and ('eSocial' in xml, validar):
                dados = read_s1060_evttabambiente(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1060_evttabambiente', dados, arquivo)

            elif ('evtTabProcesso' in xml) and ('eSocial' in xml):
                dados = read_s1070_evttabprocesso(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1070_evttabprocesso', dados, arquivo)

            elif ('evtTabOperPort' in xml) and ('eSocial' in xml):
                dados = read_s1080_evttaboperport(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1080_evttaboperport', dados, arquivo)

            elif ('evtRemun' in xml) and ('eSocial' in xml):
                dados = read_s1200_evtremun(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1200_evtremun', dados, arquivo)

            elif ('evtRmnRPPS' in xml) and ('eSocial' in xml):
                dados = read_s1202_evtrmnrpps(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1202_evtrmnrpps', dados, arquivo)

            elif ('evtBenPrRP' in xml) and ('eSocial' in xml):
                dados = read_s1207_evtbenprrp(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1207_evtbenprrp', dados, arquivo)

            elif ('evtPgtos' in xml) and ('eSocial' in xml):
                dados = read_s1210_evtpgtos(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1210_evtpgtos', dados, arquivo)

            elif ('evtAqProd' in xml) and ('eSocial' in xml):
                dados = read_s1250_evtaqprod(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1250_evtaqprod', dados, arquivo)

            elif ('evtComProd' in xml) and ('eSocial' in xml):
                dados = read_s1260_evtcomprod(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1260_evtcomprod', dados, arquivo)

            elif ('evtContratAvNP' in xml) and ('eSocial' in xml):
                dados = read_s1270_evtcontratavnp(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1270_evtcontratavnp', dados, arquivo)

            elif ('evtInfoComplPer' in xml) and ('eSocial' in xml):
                dados = read_s1280_evtinfocomplper(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1280_evtinfocomplper', dados, arquivo)

            elif ('evtTotConting' in xml) and ('eSocial' in xml):
                dados = read_s1295_evttotconting(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1295_evttotconting', dados, arquivo)

            elif ('evtReabreEvPer' in xml) and ('eSocial' in xml):
                dados = read_s1298_evtreabreevper(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1298_evtreabreevper', dados, arquivo)

            elif ('evtFechaEvPer' in xml) and ('eSocial' in xml):
                dados = read_s1299_evtfechaevper(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1299_evtfechaevper', dados, arquivo)

            elif ('evtContrSindPatr' in xml) and ('eSocial' in xml):
                dados = read_s1300_evtcontrsindpatr(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1300_evtcontrsindpatr', dados, arquivo)

            elif ('evtAdmPrelim' in xml) and ('eSocial' in xml):
                dados = read_s2190_evtadmprelim(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2190_evtadmprelim', dados, arquivo)

            elif ('evtAdmissao' in xml) and ('eSocial' in xml):
                dados = read_s2200_evtadmissao(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2200_evtadmissao', dados, arquivo)

            elif ('evtAltCadastral' in xml) and ('eSocial' in xml):
                dados = read_s2205_evtaltcadastral(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2205_evtaltcadastral', dados, arquivo)

            elif ('evtAltContratual' in xml) and ('eSocial' in xml):
                dados = read_s2206_evtaltcontratual(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2206_evtaltcontratual', dados, arquivo)

            elif ('evtCAT' in xml) and ('eSocial' in xml):
                dados = read_s2210_evtcat(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2210_evtcat', dados, arquivo)

            elif ('evtMonit' in xml) and ('eSocial' in xml):
                dados = read_s2220_evtmonit(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2220_evtmonit', dados, arquivo)

            elif ('evtAfastTemp' in xml) and ('eSocial' in xml):
                dados = read_s2230_evtafasttemp(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2230_evtafasttemp', dados, arquivo)

            elif ('evtExpRisco' in xml) and ('eSocial' in xml):
                dados = read_s2240_evtexprisco(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2240_evtexprisco', dados, arquivo)

            elif ('evtInsApo' in xml) and ('eSocial' in xml):
                dados = read_s2241_evtinsapo(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2241_evtinsapo', dados, arquivo)

            elif ('evtAvPrevio' in xml) and ('eSocial' in xml):
                dados = read_s2250_evtavprevio(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2250_evtavprevio', dados, arquivo)

            elif ('evtConvInterm' in xml) and ('eSocial' in xml):
                dados = read_s2260_evtconvinterm(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2260_evtconvinterm', dados, arquivo)

            elif ('evtReintegr' in xml) and ('eSocial' in xml):
                dados = read_s2298_evtreintegr(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2298_evtreintegr', dados, arquivo)

            elif ('evtDeslig' in xml) and ('eSocial' in xml):
                dados = read_s2299_evtdeslig(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2299_evtdeslig', dados, arquivo)

            elif ('evtTSVInicio' in xml) and ('eSocial' in xml):
                dados = read_s2300_evttsvinicio(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2300_evttsvinicio', dados, arquivo)

            elif ('evtTSVAltContr' in xml) and ('eSocial' in xml):
                dados = read_s2306_evttsvaltcontr(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2306_evttsvaltcontr', dados, arquivo)

            elif ('evtTSVTermino' in xml) and ('eSocial' in xml):
                dados = read_s2399_evttsvtermino(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2399_evttsvtermino', dados, arquivo)

            # elif ('evtCdBenPrRP' in xml) and ('eSocial' in xml):
            #     dados = read_s2400_evtcdbenefin(dados, arquivo, validar)
            #     if dados: dados = atualizar_tabela('s2400_evtcdbenefin', dados, arquivo)

            elif ('evtExclusao' in xml) and ('eSocial' in xml):
                dados = read_s3000_evtexclusao(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s3000_evtexclusao', dados, arquivo)

            elif ('evtBasesTrab' in xml) and ('eSocial' in xml):
                dados = read_s5001_evtbasestrab(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s5001_evtbasestrab', dados, arquivo)

            elif ('evtIrrfBenef' in xml) and ('eSocial' in xml):
                dados = read_s5002_evtirrfbenef(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s5002_evtirrfbenef', dados, arquivo)

            elif ('evtCS' in xml) and ('eSocial' in xml):
                dados = read_s5011_evtcs(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s5011_evtcs', dados, arquivo)

            elif ('evtIrrf' in xml) and ('eSocial' in xml):
                dados = read_s5012_evtirrf(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s5012_evtirrf', dados, arquivo)

        elif 'Reinf' in xml:
            xmlns = doc.Reinf['xmlns'].split('/')
            dados['versao'] = get_versao_evento(xml)
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r1000_evtinfocontri import read_r1000_evtinfocontri
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r1070_evttabprocesso import read_r1070_evttabprocesso
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r2010_evtservtom import read_r2010_evtservtom
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r2020_evtservprest import read_r2020_evtservprest
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r2030_evtassocdesprec import read_r2030_evtassocdesprec
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r2040_evtassocdesprep import read_r2040_evtassocdesprep
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r2050_evtcomprod import read_r2050_evtcomprod
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r2060_evtcprb import read_r2060_evtcprb
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r2070_evtpgtosdivs import read_r2070_evtpgtosdivs
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r2098_evtreabreevper import read_r2098_evtreabreevper
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r2099_evtfechaevper import read_r2099_evtfechaevper
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r3010_evtespdesportivo import read_r3010_evtespdesportivo
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r5001_evttotal import read_r5001_evttotal
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r5011_evttotalcontrib import read_r5011_evttotalcontrib
            from emensageriapro.efdreinf.xml_imports.v1_03_02.r9000_evtexclusao import read_r9000_evtexclusao

            if ('evtInfoContri' in xml) and ('Reinf' in xml):
                dados = read_r1000_evtinfocontri(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r1000_evtinfocontri', dados, arquivo)

            elif ('evtTabProcesso' in xml) and ('Reinf' in xml):
                dados = read_r1070_evttabprocesso(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r1070_evttabprocesso', dados, arquivo)

            elif ('evtServTom' in xml) and ('Reinf' in xml):
                dados = read_r2010_evtservtom(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2010_evtservtom', dados, arquivo)

            elif ('evtServPrest' in xml) and ('Reinf' in xml):
                dados = read_r2020_evtservprest(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2020_evtservprest', dados, arquivo)

            elif ('evtAssocDespRec' in xml) and ('Reinf' in xml):
                dados = read_r2030_evtassocdesprec(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2030_evtassocdesprec', dados, arquivo)

            elif ('evtAssocDespRep' in xml) and ('Reinf' in xml):
                dados = read_r2040_evtassocdesprep(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2040_evtassocdesprep', dados, arquivo)

            elif ('evtComProd' in xml) and ('Reinf' in xml):
                dados = read_r2050_evtcomprod(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2050_evtcomprod', dados, arquivo)

            elif ('evtCPRB' in xml) and ('Reinf' in xml):
                dados = read_r2060_evtcprb(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2060_evtcprb', dados, arquivo)

            elif ('evtPgtosDivs' in xml) and ('Reinf' in xml):
                dados = read_r2070_evtpgtosdivs(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2070_evtpgtosdivs', dados, arquivo)

            elif ('evtReabreEvPer' in xml) and ('Reinf' in xml):
                dados = read_r2098_evtreabreevper(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2098_evtreabreevper', dados, arquivo)

            elif ('evtFechaEvPer' in xml) and ('Reinf' in xml):
                dados = read_r2099_evtfechaevper(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2099_evtfechaevper', dados, arquivo)

            elif ('evtEspDesportivo' in xml) and ('Reinf' in xml):
                dados = read_r3010_evtespdesportivo(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r3010_evtespdesportivo', dados, arquivo)

            elif ('evtTotal' in xml) and ('Reinf' in xml):
                dados = read_r5001_evttotal(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r5001_evttotal', dados, arquivo)

            elif ('evtTotalContrib' in xml) and ('Reinf' in xml):
                dados = read_r5011_evttotalcontrib(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r5011_evttotalcontrib', dados, arquivo)

            elif ('evtExclusao' in xml) and ('Reinf' in xml):
                dados = read_r9000_evtexclusao(dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r9000_evtexclusao', dados, arquivo)
        else:
            dados['status'] = 2
            return dados

    return dados

