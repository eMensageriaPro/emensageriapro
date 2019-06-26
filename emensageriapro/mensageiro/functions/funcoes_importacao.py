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
from emensageriapro.padrao import ler_arquivo
from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_schema

from emensageriapro.mensageiro.models import *
from emensageriapro.esocial.models import *
from emensageriapro.efdreinf.models import *


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def get_evento_nome(texto):
    texto = texto.replace('/">', '">').replace('id="', 'Id="')
    a = texto.split(' Id="')
    b = a[0].split('"><')
    return b[len(b)-1]


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
        WHERE id=%(id)s""" % (dados), False)
    return dados





def importar_arquivo(arquivo, request, validar=0):

    from emensageriapro.settings import BASE_DIR
    from django.contrib import messages
    import untangle
    import os

    quant_erros = 0
    error_list = 0

    dados = {}

    if not os.path.isfile(BASE_DIR + '/' + arquivo):
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
            from emensageriapro.esocial.views.s1000_evtinfoempregador_importar import read_s1000_evtinfoempregador
            from emensageriapro.esocial.views.s1005_evttabestab_importar import read_s1005_evttabestab
            from emensageriapro.esocial.views.s1010_evttabrubrica_importar import read_s1010_evttabrubrica
            from emensageriapro.esocial.views.s1020_evttablotacao_importar import read_s1020_evttablotacao
            from emensageriapro.esocial.views.s1030_evttabcargo_importar import read_s1030_evttabcargo
            from emensageriapro.esocial.views.s1035_evttabcarreira_importar import read_s1035_evttabcarreira
            from emensageriapro.esocial.views.s1040_evttabfuncao_importar import read_s1040_evttabfuncao
            from emensageriapro.esocial.views.s1050_evttabhortur_importar import read_s1050_evttabhortur
            from emensageriapro.esocial.views.s1060_evttabambiente_importar import read_s1060_evttabambiente
            from emensageriapro.esocial.views.s1070_evttabprocesso_importar import read_s1070_evttabprocesso
            from emensageriapro.esocial.views.s1080_evttaboperport_importar import read_s1080_evttaboperport
            from emensageriapro.esocial.views.s1200_evtremun_importar import read_s1200_evtremun
            from emensageriapro.esocial.views.s1202_evtrmnrpps_importar import read_s1202_evtrmnrpps
            from emensageriapro.esocial.views.s1207_evtbenprrp_importar import read_s1207_evtbenprrp
            from emensageriapro.esocial.views.s1210_evtpgtos_importar import read_s1210_evtpgtos
            from emensageriapro.esocial.views.s1250_evtaqprod_importar import read_s1250_evtaqprod
            from emensageriapro.esocial.views.s1260_evtcomprod_importar import read_s1260_evtcomprod
            from emensageriapro.esocial.views.s1270_evtcontratavnp_importar import read_s1270_evtcontratavnp
            from emensageriapro.esocial.views.s1280_evtinfocomplper_importar import read_s1280_evtinfocomplper
            from emensageriapro.esocial.views.s1295_evttotconting_importar import read_s1295_evttotconting
            from emensageriapro.esocial.views.s1298_evtreabreevper_importar import read_s1298_evtreabreevper
            from emensageriapro.esocial.views.s1299_evtfechaevper_importar import read_s1299_evtfechaevper
            from emensageriapro.esocial.views.s1300_evtcontrsindpatr_importar import read_s1300_evtcontrsindpatr
            from emensageriapro.esocial.views.s2190_evtadmprelim_importar import read_s2190_evtadmprelim
            from emensageriapro.esocial.views.s2200_evtadmissao_importar import read_s2200_evtadmissao
            from emensageriapro.esocial.views.s2205_evtaltcadastral_importar import read_s2205_evtaltcadastral
            from emensageriapro.esocial.views.s2206_evtaltcontratual_importar import read_s2206_evtaltcontratual
            from emensageriapro.esocial.views.s2210_evtcat_importar import read_s2210_evtcat
            from emensageriapro.esocial.views.s2220_evtmonit_importar import read_s2220_evtmonit
            from emensageriapro.esocial.views.s2230_evtafasttemp_importar import read_s2230_evtafasttemp
            from emensageriapro.esocial.views.s2240_evtexprisco_importar import read_s2240_evtexprisco
            from emensageriapro.esocial.views.s2241_evtinsapo_importar import read_s2241_evtinsapo
            from emensageriapro.esocial.views.s2250_evtavprevio_importar import read_s2250_evtavprevio
            from emensageriapro.esocial.views.s2260_evtconvinterm_importar import read_s2260_evtconvinterm
            from emensageriapro.esocial.views.s2298_evtreintegr_importar import read_s2298_evtreintegr
            from emensageriapro.esocial.views.s2299_evtdeslig_importar import read_s2299_evtdeslig
            from emensageriapro.esocial.views.s2300_evttsvinicio_importar import read_s2300_evttsvinicio
            from emensageriapro.esocial.views.s2306_evttsvaltcontr_importar import read_s2306_evttsvaltcontr
            from emensageriapro.esocial.views.s2399_evttsvtermino_importar import read_s2399_evttsvtermino
            #from emensageriapro.esocial.views.s2400_evtcdbenefin_importar import read_s2400_evtcdbenefin
            from emensageriapro.esocial.views.s3000_evtexclusao_importar import read_s3000_evtexclusao
            from emensageriapro.esocial.views.s5001_evtbasestrab_importar import read_s5001_evtbasestrab
            from emensageriapro.esocial.views.s5002_evtirrfbenef_importar import read_s5002_evtirrfbenef
            from emensageriapro.esocial.views.s5011_evtcs_importar import read_s5011_evtcs
            from emensageriapro.esocial.views.s5012_evtirrf_importar import read_s5012_evtirrf

            if ('evtInfoEmpregador' in xml) and ('eSocial' in xml):
                dados = read_s1000_evtinfoempregador(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1000_evtinfoempregador', dados, arquivo)

            elif ('evtTabEstab' in xml) and ('eSocial' in xml):
                dados = read_s1005_evttabestab(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1005_evttabestab', dados, arquivo)

            elif ('evtTabRubrica' in xml) and ('eSocial' in xml):
                dados = read_s1010_evttabrubrica(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1010_evttabrubrica', dados, arquivo)

            elif ('evtTabLotacao' in xml) and ('eSocial' in xml):
                dados = read_s1020_evttablotacao(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1020_evttablotacao', dados, arquivo)

            elif ('evtTabCargo' in xml) and ('eSocial' in xml):
                dados = read_s1030_evttabcargo(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1030_evttabcargo', dados, arquivo)

            elif ('evtTabCarreira' in xml) and ('eSocial' in xml):
                dados = read_s1035_evttabcarreira(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1035_evttabcarreira', dados, arquivo)

            elif ('evtTabFuncao' in xml) and ('eSocial' in xml):
                dados = read_s1040_evttabfuncao(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1040_evttabfuncao', dados, arquivo)

            elif ('evtTabHorTur' in xml) and ('eSocial' in xml):
                dados = read_s1050_evttabhortur(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1050_evttabhortur', dados, arquivo)

            elif ('evtTabAmbiente' in xml) and ('eSocial' in xml, validar):
                dados = read_s1060_evttabambiente(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1060_evttabambiente', dados, arquivo)

            elif ('evtTabProcesso' in xml) and ('eSocial' in xml):
                dados = read_s1070_evttabprocesso(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1070_evttabprocesso', dados, arquivo)

            elif ('evtTabOperPort' in xml) and ('eSocial' in xml):
                dados = read_s1080_evttaboperport(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1080_evttaboperport', dados, arquivo)

            elif ('evtRemun' in xml) and ('eSocial' in xml):
                dados = read_s1200_evtremun(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1200_evtremun', dados, arquivo)

            elif ('evtRmnRPPS' in xml) and ('eSocial' in xml):
                dados = read_s1202_evtrmnrpps(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1202_evtrmnrpps', dados, arquivo)

            elif ('evtBenPrRP' in xml) and ('eSocial' in xml):
                dados = read_s1207_evtbenprrp(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1207_evtbenprrp', dados, arquivo)

            elif ('evtPgtos' in xml) and ('eSocial' in xml):
                dados = read_s1210_evtpgtos(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1210_evtpgtos', dados, arquivo)

            elif ('evtAqProd' in xml) and ('eSocial' in xml):
                dados = read_s1250_evtaqprod(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1250_evtaqprod', dados, arquivo)

            elif ('evtComProd' in xml) and ('eSocial' in xml):
                dados = read_s1260_evtcomprod(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1260_evtcomprod', dados, arquivo)

            elif ('evtContratAvNP' in xml) and ('eSocial' in xml):
                dados = read_s1270_evtcontratavnp(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1270_evtcontratavnp', dados, arquivo)

            elif ('evtInfoComplPer' in xml) and ('eSocial' in xml):
                dados = read_s1280_evtinfocomplper(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1280_evtinfocomplper', dados, arquivo)

            elif ('evtTotConting' in xml) and ('eSocial' in xml):
                dados = read_s1295_evttotconting(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1295_evttotconting', dados, arquivo)

            elif ('evtReabreEvPer' in xml) and ('eSocial' in xml):
                dados = read_s1298_evtreabreevper(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1298_evtreabreevper', dados, arquivo)

            elif ('evtFechaEvPer' in xml) and ('eSocial' in xml):
                dados = read_s1299_evtfechaevper(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1299_evtfechaevper', dados, arquivo)

            elif ('evtContrSindPatr' in xml) and ('eSocial' in xml):
                dados = read_s1300_evtcontrsindpatr(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s1300_evtcontrsindpatr', dados, arquivo)

            elif ('evtAdmPrelim' in xml) and ('eSocial' in xml):
                dados = read_s2190_evtadmprelim(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2190_evtadmprelim', dados, arquivo)

            elif ('evtAdmissao' in xml) and ('eSocial' in xml):
                dados = read_s2200_evtadmissao(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2200_evtadmissao', dados, arquivo)

            elif ('evtAltCadastral' in xml) and ('eSocial' in xml):
                dados = read_s2205_evtaltcadastral(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2205_evtaltcadastral', dados, arquivo)

            elif ('evtAltContratual' in xml) and ('eSocial' in xml):
                dados = read_s2206_evtaltcontratual(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2206_evtaltcontratual', dados, arquivo)

            elif ('evtCAT' in xml) and ('eSocial' in xml):
                dados = read_s2210_evtcat(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2210_evtcat', dados, arquivo)

            elif ('evtMonit' in xml) and ('eSocial' in xml):
                dados = read_s2220_evtmonit(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2220_evtmonit', dados, arquivo)

            elif ('evtAfastTemp' in xml) and ('eSocial' in xml):
                dados = read_s2230_evtafasttemp(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2230_evtafasttemp', dados, arquivo)

            elif ('evtExpRisco' in xml) and ('eSocial' in xml):
                dados = read_s2240_evtexprisco(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2240_evtexprisco', dados, arquivo)

            elif ('evtInsApo' in xml) and ('eSocial' in xml):
                dados = read_s2241_evtinsapo(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2241_evtinsapo', dados, arquivo)

            elif ('evtAvPrevio' in xml) and ('eSocial' in xml):
                dados = read_s2250_evtavprevio(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2250_evtavprevio', dados, arquivo)

            elif ('evtConvInterm' in xml) and ('eSocial' in xml):
                dados = read_s2260_evtconvinterm(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2260_evtconvinterm', dados, arquivo)

            elif ('evtReintegr' in xml) and ('eSocial' in xml):
                dados = read_s2298_evtreintegr(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2298_evtreintegr', dados, arquivo)

            elif ('evtDeslig' in xml) and ('eSocial' in xml):
                dados = read_s2299_evtdeslig(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2299_evtdeslig', dados, arquivo)

            elif ('evtTSVInicio' in xml) and ('eSocial' in xml):
                dados = read_s2300_evttsvinicio(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2300_evttsvinicio', dados, arquivo)

            elif ('evtTSVAltContr' in xml) and ('eSocial' in xml):
                dados = read_s2306_evttsvaltcontr(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2306_evttsvaltcontr', dados, arquivo)

            elif ('evtTSVTermino' in xml) and ('eSocial' in xml):
                dados = read_s2399_evttsvtermino(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s2399_evttsvtermino', dados, arquivo)

            # elif ('evtCdBenPrRP' in xml) and ('eSocial' in xml):
            #     dados = read_s2400_evtcdbenefin(request, dados, arquivo, validar)
            #     if dados: dados = atualizar_tabela('s2400_evtcdbenefin', dados, arquivo)

            elif ('evtExclusao' in xml) and ('eSocial' in xml):
                dados = read_s3000_evtexclusao(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s3000_evtexclusao', dados, arquivo)

            elif ('evtBasesTrab' in xml) and ('eSocial' in xml):
                dados = read_s5001_evtbasestrab(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s5001_evtbasestrab', dados, arquivo)

            elif ('evtIrrfBenef' in xml) and ('eSocial' in xml):
                dados = read_s5002_evtirrfbenef(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s5002_evtirrfbenef', dados, arquivo)

            elif ('evtCS' in xml) and ('eSocial' in xml):
                dados = read_s5011_evtcs(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s5011_evtcs', dados, arquivo)

            elif ('evtIrrf' in xml) and ('eSocial' in xml):
                dados = read_s5012_evtirrf(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('s5012_evtirrf', dados, arquivo)

        elif 'Reinf' in xml:
            xmlns = doc.Reinf['xmlns'].split('/')
            dados['versao'] = get_versao_evento(xml)
            from emensageriapro.efdreinf.views.r1000_evtinfocontri_importar import read_r1000_evtinfocontri
            from emensageriapro.efdreinf.views.r1070_evttabprocesso_importar import read_r1070_evttabprocesso
            from emensageriapro.efdreinf.views.r2010_evtservtom_importar import read_r2010_evtservtom
            from emensageriapro.efdreinf.views.r2020_evtservprest_importar import read_r2020_evtservprest
            from emensageriapro.efdreinf.views.r2030_evtassocdesprec_importar import read_r2030_evtassocdesprec
            from emensageriapro.efdreinf.views.r2040_evtassocdesprep_importar import read_r2040_evtassocdesprep
            from emensageriapro.efdreinf.views.r2050_evtcomprod_importar import read_r2050_evtcomprod
            from emensageriapro.efdreinf.views.r2060_evtcprb_importar import read_r2060_evtcprb
            from emensageriapro.efdreinf.views.r2070_evtpgtosdivs_importar import read_r2070_evtpgtosdivs
            from emensageriapro.efdreinf.views.r2098_evtreabreevper_importar import read_r2098_evtreabreevper
            from emensageriapro.efdreinf.views.r2099_evtfechaevper_importar import read_r2099_evtfechaevper
            from emensageriapro.efdreinf.views.r3010_evtespdesportivo_importar import read_r3010_evtespdesportivo
            from emensageriapro.efdreinf.views.r5001_evttotal_importar import read_r5001_evttotal
            from emensageriapro.efdreinf.views.r5011_evttotalcontrib_importar import read_r5011_evttotalcontrib
            from emensageriapro.efdreinf.views.r9000_evtexclusao_importar import read_r9000_evtexclusao

            if ('evtInfoContri' in xml) and ('Reinf' in xml):
                dados = read_r1000_evtinfocontri(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r1000_evtinfocontri', dados, arquivo)

            elif ('evtTabProcesso' in xml) and ('Reinf' in xml):
                dados = read_r1070_evttabprocesso(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r1070_evttabprocesso', dados, arquivo)

            elif ('evtServTom' in xml) and ('Reinf' in xml):
                dados = read_r2010_evtservtom(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2010_evtservtom', dados, arquivo)

            elif ('evtServPrest' in xml) and ('Reinf' in xml):
                dados = read_r2020_evtservprest(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2020_evtservprest', dados, arquivo)

            elif ('evtAssocDespRec' in xml) and ('Reinf' in xml):
                dados = read_r2030_evtassocdesprec(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2030_evtassocdesprec', dados, arquivo)

            elif ('evtAssocDespRep' in xml) and ('Reinf' in xml):
                dados = read_r2040_evtassocdesprep(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2040_evtassocdesprep', dados, arquivo)

            elif ('evtComProd' in xml) and ('Reinf' in xml):
                dados = read_r2050_evtcomprod(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2050_evtcomprod', dados, arquivo)

            elif ('evtCPRB' in xml) and ('Reinf' in xml):
                dados = read_r2060_evtcprb(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2060_evtcprb', dados, arquivo)

            elif ('evtPgtosDivs' in xml) and ('Reinf' in xml):
                dados = read_r2070_evtpgtosdivs(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2070_evtpgtosdivs', dados, arquivo)

            elif ('evtReabreEvPer' in xml) and ('Reinf' in xml):
                dados = read_r2098_evtreabreevper(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2098_evtreabreevper', dados, arquivo)

            elif ('evtFechaEvPer' in xml) and ('Reinf' in xml):
                dados = read_r2099_evtfechaevper(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r2099_evtfechaevper', dados, arquivo)

            elif ('evtEspDesportivo' in xml) and ('Reinf' in xml):
                dados = read_r3010_evtespdesportivo(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r3010_evtespdesportivo', dados, arquivo)

            elif ('evtTotal' in xml) and ('Reinf' in xml):
                dados = read_r5001_evttotal(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r5001_evttotal', dados, arquivo)

            elif ('evtTotalContrib' in xml) and ('Reinf' in xml):
                dados = read_r5011_evttotalcontrib(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r5011_evttotalcontrib', dados, arquivo)

            elif ('evtExclusao' in xml) and ('Reinf' in xml):
                dados = read_r9000_evtexclusao(request, dados, arquivo, validar)
                if dados: dados = atualizar_tabela('r9000_evtexclusao', dados, arquivo)
        else:
            dados['status'] = 2
            return dados

    return dados

