#coding:utf-8


"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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


def importar_arquivo(arquivo, request, validar=0):

    import os
    import untangle
    from django.contrib import messages
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.functions import get_versao_evento
    from emensageriapro.padrao import ler_arquivo

    dados = {}

    if not os.path.isfile(BASE_DIR + '/' + arquivo.arquivo):
        messages.error(request, 'Arquivo não encontrado!')
        return dados

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")

    try:
        doc = untangle.parse(xml)
        dados['status'] = 1

    except:
        messages.error(request, 'Erro na importação. Arquivo XML inválido!')
        dados['status'] = 2
        return dados

    if dados['status'] == 1:

        xmlns = doc.eSocial['xmlns'].split('/')
        dados['versao'] = get_versao_evento(xml)

        if ('evtInfoEmpregador' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1000_evtinfoempregador_importar import read_s1000_evtinfoempregador
            dados = read_s1000_evtinfoempregador(request, dados, arquivo, validar)

        elif ('evtTabEstab' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1005_evttabestab_importar import read_s1005_evttabestab
            dados = read_s1005_evttabestab(request, dados, arquivo, validar)

        elif ('evtTabRubrica' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1010_evttabrubrica_importar import read_s1010_evttabrubrica
            dados = read_s1010_evttabrubrica(request, dados, arquivo, validar)

        elif ('evtTabLotacao' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1020_evttablotacao_importar import read_s1020_evttablotacao
            dados = read_s1020_evttablotacao(request, dados, arquivo, validar)

        elif ('evtTabCargo' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1030_evttabcargo_importar import read_s1030_evttabcargo
            dados = read_s1030_evttabcargo(request, dados, arquivo, validar)

        elif ('evtTabCarreira' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1035_evttabcarreira_importar import read_s1035_evttabcarreira
            dados = read_s1035_evttabcarreira(request, dados, arquivo, validar)

        elif ('evtTabFuncao' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1040_evttabfuncao_importar import read_s1040_evttabfuncao
            dados = read_s1040_evttabfuncao(request, dados, arquivo, validar)

        elif ('evtTabHorTur' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1050_evttabhortur_importar import read_s1050_evttabhortur
            dados = read_s1050_evttabhortur(request, dados, arquivo, validar)

        elif ('evtTabAmbiente' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1060_evttabambiente_importar import read_s1060_evttabambiente
            dados = read_s1060_evttabambiente(request, dados, arquivo, validar)

        elif ('evtTabProcesso' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1070_evttabprocesso_importar import read_s1070_evttabprocesso
            dados = read_s1070_evttabprocesso(request, dados, arquivo, validar)

        elif ('evtTabOperPort' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1080_evttaboperport_importar import read_s1080_evttaboperport
            dados = read_s1080_evttaboperport(request, dados, arquivo, validar)

        elif ('evtRemun' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1200_evtremun_importar import read_s1200_evtremun
            dados = read_s1200_evtremun(request, dados, arquivo, validar)

        elif ('evtRmnRPPS' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1202_evtrmnrpps_importar import read_s1202_evtrmnrpps
            dados = read_s1202_evtrmnrpps(request, dados, arquivo, validar)

        elif ('evtBenPrRP' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1207_evtbenprrp_importar import read_s1207_evtbenprrp
            dados = read_s1207_evtbenprrp(request, dados, arquivo, validar)

        elif ('evtPgtos' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1210_evtpgtos_importar import read_s1210_evtpgtos
            dados = read_s1210_evtpgtos(request, dados, arquivo, validar)

        elif ('evtAqProd' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1250_evtaqprod_importar import read_s1250_evtaqprod
            dados = read_s1250_evtaqprod(request, dados, arquivo, validar)

        elif ('evtComProd' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1260_evtcomprod_importar import read_s1260_evtcomprod
            dados = read_s1260_evtcomprod(request, dados, arquivo, validar)

        elif ('evtContratAvNP' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1270_evtcontratavnp_importar import read_s1270_evtcontratavnp
            dados = read_s1270_evtcontratavnp(request, dados, arquivo, validar)

        elif ('evtInfoComplPer' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1280_evtinfocomplper_importar import read_s1280_evtinfocomplper
            dados = read_s1280_evtinfocomplper(request, dados, arquivo, validar)

        elif ('evtTotConting' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1295_evttotconting_importar import read_s1295_evttotconting
            dados = read_s1295_evttotconting(request, dados, arquivo, validar)

        elif ('evtReabreEvPer' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1298_evtreabreevper_importar import read_s1298_evtreabreevper
            dados = read_s1298_evtreabreevper(request, dados, arquivo, validar)

        elif ('evtFechaEvPer' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1299_evtfechaevper_importar import read_s1299_evtfechaevper
            dados = read_s1299_evtfechaevper(request, dados, arquivo, validar)

        elif ('evtContrSindPatr' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s1300_evtcontrsindpatr_importar import read_s1300_evtcontrsindpatr
            dados = read_s1300_evtcontrsindpatr(request, dados, arquivo, validar)

        elif ('evtAdmPrelim' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2190_evtadmprelim_importar import read_s2190_evtadmprelim
            dados = read_s2190_evtadmprelim(request, dados, arquivo, validar)

        elif ('evtAdmissao' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2200_evtadmissao_importar import read_s2200_evtadmissao
            dados = read_s2200_evtadmissao(request, dados, arquivo, validar)

        elif ('evtAltCadastral' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2205_evtaltcadastral_importar import read_s2205_evtaltcadastral
            dados = read_s2205_evtaltcadastral(request, dados, arquivo, validar)

        elif ('evtAltContratual' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2206_evtaltcontratual_importar import read_s2206_evtaltcontratual
            dados = read_s2206_evtaltcontratual(request, dados, arquivo, validar)

        elif ('evtCAT' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2210_evtcat_importar import read_s2210_evtcat
            dados = read_s2210_evtcat(request, dados, arquivo, validar)

        elif ('evtMonit' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2220_evtmonit_importar import read_s2220_evtmonit
            dados = read_s2220_evtmonit(request, dados, arquivo, validar)

        elif ('evtToxic' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2221_evttoxic_importar import read_s2221_evttoxic
            dados = read_s2221_evttoxic(request, dados, arquivo, validar)

        elif ('evtAfastTemp' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2230_evtafasttemp_importar import read_s2230_evtafasttemp
            dados = read_s2230_evtafasttemp(request, dados, arquivo, validar)

        elif ('evtCessao' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2231_evtcessao_importar import read_s2231_evtcessao
            dados = read_s2231_evtcessao(request, dados, arquivo, validar)

        elif ('evtExpRisco' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2240_evtexprisco_importar import read_s2240_evtexprisco
            dados = read_s2240_evtexprisco(request, dados, arquivo, validar)

        elif ('evtInsApo' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2241_evtinsapo_importar import read_s2241_evtinsapo
            dados = read_s2241_evtinsapo(request, dados, arquivo, validar)

        elif ('evtTreiCap' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2245_evttreicap_importar import read_s2245_evttreicap
            dados = read_s2245_evttreicap(request, dados, arquivo, validar)

        elif ('evtAvPrevio' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2250_evtavprevio_importar import read_s2250_evtavprevio
            dados = read_s2250_evtavprevio(request, dados, arquivo, validar)

        elif ('evtConvInterm' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2260_evtconvinterm_importar import read_s2260_evtconvinterm
            dados = read_s2260_evtconvinterm(request, dados, arquivo, validar)

        elif ('evtReintegr' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2298_evtreintegr_importar import read_s2298_evtreintegr
            dados = read_s2298_evtreintegr(request, dados, arquivo, validar)

        elif ('evtDeslig' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2299_evtdeslig_importar import read_s2299_evtdeslig
            dados = read_s2299_evtdeslig(request, dados, arquivo, validar)

        elif ('evtTSVInicio' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2300_evttsvinicio_importar import read_s2300_evttsvinicio
            dados = read_s2300_evttsvinicio(request, dados, arquivo, validar)

        elif ('evtTSVAltContr' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2306_evttsvaltcontr_importar import read_s2306_evttsvaltcontr
            dados = read_s2306_evttsvaltcontr(request, dados, arquivo, validar)

        elif ('evtTSVTermino' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2399_evttsvtermino_importar import read_s2399_evttsvtermino
            dados = read_s2399_evttsvtermino(request, dados, arquivo, validar)

        elif ('evtCdBenefIn' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2400_evtcdbenefin_importar import read_s2400_evtcdbenefin
            dados = read_s2400_evtcdbenefin(request, dados, arquivo, validar)

        elif ('evtCdBenefAlt' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2405_evtcdbenefalt_importar import read_s2405_evtcdbenefalt
            dados = read_s2405_evtcdbenefalt(request, dados, arquivo, validar)

        elif ('evtCdBenIn' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2410_evtcdbenin_importar import read_s2410_evtcdbenin
            dados = read_s2410_evtcdbenin(request, dados, arquivo, validar)

        elif ('evtCdBenAlt' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2416_evtcdbenalt_importar import read_s2416_evtcdbenalt
            dados = read_s2416_evtcdbenalt(request, dados, arquivo, validar)

        elif ('evtCdBenTerm' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s2420_evtcdbenterm_importar import read_s2420_evtcdbenterm
            dados = read_s2420_evtcdbenterm(request, dados, arquivo, validar)

        elif ('evtExclusao' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s3000_evtexclusao_importar import read_s3000_evtexclusao
            dados = read_s3000_evtexclusao(request, dados, arquivo, validar)

        elif ('evtBasesTrab' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s5001_evtbasestrab_importar import read_s5001_evtbasestrab
            dados = read_s5001_evtbasestrab(request, dados, arquivo, validar)

        elif ('evtIrrfBenef' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s5002_evtirrfbenef_importar import read_s5002_evtirrfbenef
            dados = read_s5002_evtirrfbenef(request, dados, arquivo, validar)

        elif ('evtBasesFGTS' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s5003_evtbasesfgts_importar import read_s5003_evtbasesfgts
            dados = read_s5003_evtbasesfgts(request, dados, arquivo, validar)

        elif ('evtCS' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s5011_evtcs_importar import read_s5011_evtcs
            dados = read_s5011_evtcs(request, dados, arquivo, validar)

        elif ('evtIrrf' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s5012_evtirrf_importar import read_s5012_evtirrf
            dados = read_s5012_evtirrf(request, dados, arquivo, validar)

        elif ('evtFGTS' in xml) and ('eSocial' in xml):
            from emensageriapro.esocial.views.s5013_evtfgts_importar import read_s5013_evtfgts
            dados = read_s5013_evtfgts(request, dados, arquivo, validar)

        elif ('evtInfoContri' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r1000_evtinfocontri_importar import read_r1000_evtinfocontri
            dados = read_r1000_evtinfocontri(request, dados, arquivo, validar)

        elif ('evtTabProcesso' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r1070_evttabprocesso_importar import read_r1070_evttabprocesso
            dados = read_r1070_evttabprocesso(request, dados, arquivo, validar)

        elif ('evtServTom' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r2010_evtservtom_importar import read_r2010_evtservtom
            dados = read_r2010_evtservtom(request, dados, arquivo, validar)

        elif ('evtServPrest' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r2020_evtservprest_importar import read_r2020_evtservprest
            dados = read_r2020_evtservprest(request, dados, arquivo, validar)

        elif ('evtAssocDespRec' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r2030_evtassocdesprec_importar import read_r2030_evtassocdesprec
            dados = read_r2030_evtassocdesprec(request, dados, arquivo, validar)

        elif ('evtAssocDespRep' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r2040_evtassocdesprep_importar import read_r2040_evtassocdesprep
            dados = read_r2040_evtassocdesprep(request, dados, arquivo, validar)

        elif ('evtComProd' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r2050_evtcomprod_importar import read_r2050_evtcomprod
            dados = read_r2050_evtcomprod(request, dados, arquivo, validar)

        elif ('evtCPRB' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r2060_evtcprb_importar import read_r2060_evtcprb
            dados = read_r2060_evtcprb(request, dados, arquivo, validar)

        elif ('evtPgtosDivs' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r2070_evtpgtosdivs_importar import read_r2070_evtpgtosdivs
            dados = read_r2070_evtpgtosdivs(request, dados, arquivo, validar)

        elif ('evtReabreEvPer' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r2098_evtreabreevper_importar import read_r2098_evtreabreevper
            dados = read_r2098_evtreabreevper(request, dados, arquivo, validar)

        elif ('evtFechaEvPer' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r2099_evtfechaevper_importar import read_r2099_evtfechaevper
            dados = read_r2099_evtfechaevper(request, dados, arquivo, validar)

        elif ('evtEspDesportivo' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r3010_evtespdesportivo_importar import read_r3010_evtespdesportivo
            dados = read_r3010_evtespdesportivo(request, dados, arquivo, validar)

        elif ('evtRetPF' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r4010_evtretpf_importar import read_r4010_evtretpf
            dados = read_r4010_evtretpf(request, dados, arquivo, validar)

        elif ('evtRetPJ' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r4020_evtretpj_importar import read_r4020_evtretpj
            dados = read_r4020_evtretpj(request, dados, arquivo, validar)

        elif ('evtBenefNId' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r4040_evtbenefnid_importar import read_r4040_evtbenefnid
            dados = read_r4040_evtbenefnid(request, dados, arquivo, validar)

        elif ('evtReab' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r4098_evtreab_importar import read_r4098_evtreab
            dados = read_r4098_evtreab(request, dados, arquivo, validar)

        elif ('evtFech' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r4099_evtfech_importar import read_r4099_evtfech
            dados = read_r4099_evtfech(request, dados, arquivo, validar)

        elif ('evtTotal' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r5001_evttotal_importar import read_r5001_evttotal
            dados = read_r5001_evttotal(request, dados, arquivo, validar)

        elif ('evtTotalContrib' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r5011_evttotalcontrib_importar import read_r5011_evttotalcontrib
            dados = read_r5011_evttotalcontrib(request, dados, arquivo, validar)

        elif ('evtExclusao' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r9000_evtexclusao_importar import read_r9000_evtexclusao
            dados = read_r9000_evtexclusao(request, dados, arquivo, validar)

        elif ('evtTotal' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r9001_evttotal_importar import read_r9001_evttotal
            dados = read_r9001_evttotal(request, dados, arquivo, validar)

        elif ('evtRet' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r9002_evtret_importar import read_r9002_evtret
            dados = read_r9002_evtret(request, dados, arquivo, validar)

        elif ('evtTotalContrib' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r9011_evttotalcontrib_importar import read_r9011_evttotalcontrib
            dados = read_r9011_evttotalcontrib(request, dados, arquivo, validar)

        elif ('evtRetCons' in xml) and ('Reinf' in xml):
            from emensageriapro.efdreinf.views.r9012_evtretcons_importar import read_r9012_evtretcons
            dados = read_r9012_evtretcons(request, dados, arquivo, validar)

    return dados