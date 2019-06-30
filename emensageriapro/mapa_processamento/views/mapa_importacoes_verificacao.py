#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def verificacao_importacao_funcao(arquivo):

    from emensageriapro.padrao import ler_arquivo
    xml_imp = ler_arquivo(arquivo.arquivo)

    if arquivo.evento == 's1000':

        from emensageriapro.esocial.models import s1000evtInfoEmpregador
        from emensageriapro.esocial.views.s1000_evtinfoempregador_gerar_xml import gerar_xml_s1000_func
        evento = s1000evtInfoEmpregador.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1000_func(pk=evento.id)

    elif arquivo.evento == 's1005':

        from emensageriapro.esocial.models import s1005evtTabEstab
        from emensageriapro.esocial.views.s1005_evttabestab_gerar_xml import gerar_xml_s1005_func
        evento = s1005evtTabEstab.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1005_func(pk=evento.id)

    elif arquivo.evento == 's1010':

        from emensageriapro.esocial.models import s1010evtTabRubrica
        from emensageriapro.esocial.views.s1010_evttabrubrica_gerar_xml import gerar_xml_s1010_func
        evento = s1010evtTabRubrica.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1010_func(pk=evento.id)

    elif arquivo.evento == 's1020':

        from emensageriapro.esocial.models import s1020evtTabLotacao
        from emensageriapro.esocial.views.s1020_evttablotacao_gerar_xml import gerar_xml_s1020_func
        evento = s1020evtTabLotacao.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1020_func(pk=evento.id)

    elif arquivo.evento == 's1030':

        from emensageriapro.esocial.models import s1030evtTabCargo
        from emensageriapro.esocial.views.s1030_evttabcargo_gerar_xml import gerar_xml_s1030_func
        evento = s1030evtTabCargo.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1030_func(pk=evento.id)

    elif arquivo.evento == 's1035':

        from emensageriapro.esocial.models import s1035evtTabCarreira
        from emensageriapro.esocial.views.s1035_evttabcarreira_gerar_xml import gerar_xml_s1035_func
        evento = s1035evtTabCarreira.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1035_func(pk=evento.id)

    elif arquivo.evento == 's1040':

        from emensageriapro.esocial.models import s1040evtTabFuncao
        from emensageriapro.esocial.views.s1040_evttabfuncao_gerar_xml import gerar_xml_s1040_func
        evento = s1040evtTabFuncao.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1040_func(pk=evento.id)

    elif arquivo.evento == 's1050':

        from emensageriapro.esocial.models import s1050evtTabHorTur
        from emensageriapro.esocial.views.s1050_evttabhortur_gerar_xml import gerar_xml_s1050_func
        evento = s1050evtTabHorTur.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1050_func(pk=evento.id)

    elif arquivo.evento == 's1060':

        from emensageriapro.esocial.models import s1060evtTabAmbiente
        from emensageriapro.esocial.views.s1060_evttabambiente_gerar_xml import gerar_xml_s1060_func
        evento = s1060evtTabAmbiente.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1060_func(pk=evento.id)

    elif arquivo.evento == 's1070':

        from emensageriapro.esocial.models import s1070evtTabProcesso
        from emensageriapro.esocial.views.s1070_evttabprocesso_gerar_xml import gerar_xml_s1070_func
        evento = s1070evtTabProcesso.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1070_func(pk=evento.id)

    elif arquivo.evento == 's1080':

        from emensageriapro.esocial.models import s1080evtTabOperPort
        from emensageriapro.esocial.views.s1080_evttaboperport_gerar_xml import gerar_xml_s1080_func
        evento = s1080evtTabOperPort.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1080_func(pk=evento.id)

    elif arquivo.evento == 's1200':

        from emensageriapro.esocial.models import s1200evtRemun
        from emensageriapro.esocial.views.s1200_evtremun_gerar_xml import gerar_xml_s1200_func
        evento = s1200evtRemun.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1200_func(pk=evento.id)

    elif arquivo.evento == 's1202':

        from emensageriapro.esocial.models import s1202evtRmnRPPS
        from emensageriapro.esocial.views.s1202_evtrmnrpps_gerar_xml import gerar_xml_s1202_func
        evento = s1202evtRmnRPPS.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1202_func(pk=evento.id)

    elif arquivo.evento == 's1207':

        from emensageriapro.esocial.models import s1207evtBenPrRP
        from emensageriapro.esocial.views.s1207_evtbenprrp_gerar_xml import gerar_xml_s1207_func
        evento = s1207evtBenPrRP.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1207_func(pk=evento.id)

    elif arquivo.evento == 's1210':

        from emensageriapro.esocial.models import s1210evtPgtos
        from emensageriapro.esocial.views.s1210_evtpgtos_gerar_xml import gerar_xml_s1210_func
        evento = s1210evtPgtos.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1210_func(pk=evento.id)

    elif arquivo.evento == 's1250':

        from emensageriapro.esocial.models import s1250evtAqProd
        from emensageriapro.esocial.views.s1250_evtaqprod_gerar_xml import gerar_xml_s1250_func
        evento = s1250evtAqProd.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1250_func(pk=evento.id)

    elif arquivo.evento == 's1260':

        from emensageriapro.esocial.models import s1260evtComProd
        from emensageriapro.esocial.views.s1260_evtcomprod_gerar_xml import gerar_xml_s1260_func
        evento = s1260evtComProd.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1260_func(pk=evento.id)

    elif arquivo.evento == 's1270':

        from emensageriapro.esocial.models import s1270evtContratAvNP
        from emensageriapro.esocial.views.s1270_evtcontratavnp_gerar_xml import gerar_xml_s1270_func
        evento = s1270evtContratAvNP.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1270_func(pk=evento.id)

    elif arquivo.evento == 's1280':

        from emensageriapro.esocial.models import s1280evtInfoComplPer
        from emensageriapro.esocial.views.s1280_evtinfocomplper_gerar_xml import gerar_xml_s1280_func
        evento = s1280evtInfoComplPer.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1280_func(pk=evento.id)

    elif arquivo.evento == 's1295':

        from emensageriapro.esocial.models import s1295evtTotConting
        from emensageriapro.esocial.views.s1295_evttotconting_gerar_xml import gerar_xml_s1295_func
        evento = s1295evtTotConting.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1295_func(pk=evento.id)

    elif arquivo.evento == 's1298':

        from emensageriapro.esocial.models import s1298evtReabreEvPer
        from emensageriapro.esocial.views.s1298_evtreabreevper_gerar_xml import gerar_xml_s1298_func
        evento = s1298evtReabreEvPer.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1298_func(pk=evento.id)

    elif arquivo.evento == 's1299':

        from emensageriapro.esocial.models import s1299evtFechaEvPer
        from emensageriapro.esocial.views.s1299_evtfechaevper_gerar_xml import gerar_xml_s1299_func
        evento = s1299evtFechaEvPer.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1299_func(pk=evento.id)

    elif arquivo.evento == 's1300':

        from emensageriapro.esocial.models import s1300evtContrSindPatr
        from emensageriapro.esocial.views.s1300_evtcontrsindpatr_gerar_xml import gerar_xml_s1300_func
        evento = s1300evtContrSindPatr.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s1300_func(pk=evento.id)

    elif arquivo.evento == 's2190':

        from emensageriapro.esocial.models import s2190evtAdmPrelim
        from emensageriapro.esocial.views.s2190_evtadmprelim_gerar_xml import gerar_xml_s2190_func
        evento = s2190evtAdmPrelim.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2190_func(pk=evento.id)

    elif arquivo.evento == 's2200':

        from emensageriapro.esocial.models import s2200evtAdmissao
        from emensageriapro.esocial.views.s2200_evtadmissao_gerar_xml import gerar_xml_s2200_func
        evento = s2200evtAdmissao.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2200_func(pk=evento.id)

    elif arquivo.evento == 's2205':

        from emensageriapro.esocial.models import s2205evtAltCadastral
        from emensageriapro.esocial.views.s2205_evtaltcadastral_gerar_xml import gerar_xml_s2205_func
        evento = s2205evtAltCadastral.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2205_func(pk=evento.id)

    elif arquivo.evento == 's2206':

        from emensageriapro.esocial.models import s2206evtAltContratual
        from emensageriapro.esocial.views.s2206_evtaltcontratual_gerar_xml import gerar_xml_s2206_func
        evento = s2206evtAltContratual.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2206_func(pk=evento.id)

    elif arquivo.evento == 's2210':

        from emensageriapro.esocial.models import s2210evtCAT
        from emensageriapro.esocial.views.s2210_evtcat_gerar_xml import gerar_xml_s2210_func
        evento = s2210evtCAT.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2210_func(pk=evento.id)

    elif arquivo.evento == 's2220':

        from emensageriapro.esocial.models import s2220evtMonit
        from emensageriapro.esocial.views.s2220_evtmonit_gerar_xml import gerar_xml_s2220_func
        evento = s2220evtMonit.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2220_func(pk=evento.id)

    elif arquivo.evento == 's2221':

        from emensageriapro.esocial.models import s2221evtToxic
        from emensageriapro.esocial.views.s2221_evttoxic_gerar_xml import gerar_xml_s2221_func
        evento = s2221evtToxic.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2221_func(pk=evento.id)

    elif arquivo.evento == 's2230':

        from emensageriapro.esocial.models import s2230evtAfastTemp
        from emensageriapro.esocial.views.s2230_evtafasttemp_gerar_xml import gerar_xml_s2230_func
        evento = s2230evtAfastTemp.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2230_func(pk=evento.id)

    elif arquivo.evento == 's2231':

        from emensageriapro.esocial.models import s2231evtCessao
        from emensageriapro.esocial.views.s2231_evtcessao_gerar_xml import gerar_xml_s2231_func
        evento = s2231evtCessao.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2231_func(pk=evento.id)

    elif arquivo.evento == 's2240':

        from emensageriapro.esocial.models import s2240evtExpRisco
        from emensageriapro.esocial.views.s2240_evtexprisco_gerar_xml import gerar_xml_s2240_func
        evento = s2240evtExpRisco.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2240_func(pk=evento.id)

    elif arquivo.evento == 's2241':

        from emensageriapro.esocial.models import s2241evtInsApo
        from emensageriapro.esocial.views.s2241_evtinsapo_gerar_xml import gerar_xml_s2241_func
        evento = s2241evtInsApo.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2241_func(pk=evento.id)

    elif arquivo.evento == 's2245':

        from emensageriapro.esocial.models import s2245evtTreiCap
        from emensageriapro.esocial.views.s2245_evttreicap_gerar_xml import gerar_xml_s2245_func
        evento = s2245evtTreiCap.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2245_func(pk=evento.id)

    elif arquivo.evento == 's2250':

        from emensageriapro.esocial.models import s2250evtAvPrevio
        from emensageriapro.esocial.views.s2250_evtavprevio_gerar_xml import gerar_xml_s2250_func
        evento = s2250evtAvPrevio.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2250_func(pk=evento.id)

    elif arquivo.evento == 's2260':

        from emensageriapro.esocial.models import s2260evtConvInterm
        from emensageriapro.esocial.views.s2260_evtconvinterm_gerar_xml import gerar_xml_s2260_func
        evento = s2260evtConvInterm.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2260_func(pk=evento.id)

    elif arquivo.evento == 's2298':

        from emensageriapro.esocial.models import s2298evtReintegr
        from emensageriapro.esocial.views.s2298_evtreintegr_gerar_xml import gerar_xml_s2298_func
        evento = s2298evtReintegr.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2298_func(pk=evento.id)

    elif arquivo.evento == 's2299':

        from emensageriapro.esocial.models import s2299evtDeslig
        from emensageriapro.esocial.views.s2299_evtdeslig_gerar_xml import gerar_xml_s2299_func
        evento = s2299evtDeslig.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2299_func(pk=evento.id)

    elif arquivo.evento == 's2300':

        from emensageriapro.esocial.models import s2300evtTSVInicio
        from emensageriapro.esocial.views.s2300_evttsvinicio_gerar_xml import gerar_xml_s2300_func
        evento = s2300evtTSVInicio.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2300_func(pk=evento.id)

    elif arquivo.evento == 's2306':

        from emensageriapro.esocial.models import s2306evtTSVAltContr
        from emensageriapro.esocial.views.s2306_evttsvaltcontr_gerar_xml import gerar_xml_s2306_func
        evento = s2306evtTSVAltContr.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2306_func(pk=evento.id)

    elif arquivo.evento == 's2399':

        from emensageriapro.esocial.models import s2399evtTSVTermino
        from emensageriapro.esocial.views.s2399_evttsvtermino_gerar_xml import gerar_xml_s2399_func
        evento = s2399evtTSVTermino.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2399_func(pk=evento.id)

    elif arquivo.evento == 's2400':

        from emensageriapro.esocial.models import s2400evtCdBenefIn
        from emensageriapro.esocial.views.s2400_evtcdbenefin_gerar_xml import gerar_xml_s2400_func
        evento = s2400evtCdBenefIn.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2400_func(pk=evento.id)

    elif arquivo.evento == 's2405':

        from emensageriapro.esocial.models import s2405evtCdBenefAlt
        from emensageriapro.esocial.views.s2405_evtcdbenefalt_gerar_xml import gerar_xml_s2405_func
        evento = s2405evtCdBenefAlt.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2405_func(pk=evento.id)

    elif arquivo.evento == 's2410':

        from emensageriapro.esocial.models import s2410evtCdBenIn
        from emensageriapro.esocial.views.s2410_evtcdbenin_gerar_xml import gerar_xml_s2410_func
        evento = s2410evtCdBenIn.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2410_func(pk=evento.id)

    elif arquivo.evento == 's2416':

        from emensageriapro.esocial.models import s2416evtCdBenAlt
        from emensageriapro.esocial.views.s2416_evtcdbenalt_gerar_xml import gerar_xml_s2416_func
        evento = s2416evtCdBenAlt.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2416_func(pk=evento.id)

    elif arquivo.evento == 's2420':

        from emensageriapro.esocial.models import s2420evtCdBenTerm
        from emensageriapro.esocial.views.s2420_evtcdbenterm_gerar_xml import gerar_xml_s2420_func
        evento = s2420evtCdBenTerm.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s2420_func(pk=evento.id)

    elif arquivo.evento == 's3000':

        from emensageriapro.esocial.models import s3000evtExclusao
        from emensageriapro.esocial.views.s3000_evtexclusao_gerar_xml import gerar_xml_s3000_func
        evento = s3000evtExclusao.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s3000_func(pk=evento.id)

    elif arquivo.evento == 's5001':

        from emensageriapro.esocial.models import s5001evtBasesTrab
        from emensageriapro.esocial.views.s5001_evtbasestrab_gerar_xml import gerar_xml_s5001_func
        evento = s5001evtBasesTrab.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s5001_func(pk=evento.id)

    elif arquivo.evento == 's5002':

        from emensageriapro.esocial.models import s5002evtIrrfBenef
        from emensageriapro.esocial.views.s5002_evtirrfbenef_gerar_xml import gerar_xml_s5002_func
        evento = s5002evtIrrfBenef.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s5002_func(pk=evento.id)

    elif arquivo.evento == 's5003':

        from emensageriapro.esocial.models import s5003evtBasesFGTS
        from emensageriapro.esocial.views.s5003_evtbasesfgts_gerar_xml import gerar_xml_s5003_func
        evento = s5003evtBasesFGTS.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s5003_func(pk=evento.id)

    elif arquivo.evento == 's5011':

        from emensageriapro.esocial.models import s5011evtCS
        from emensageriapro.esocial.views.s5011_evtcs_gerar_xml import gerar_xml_s5011_func
        evento = s5011evtCS.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s5011_func(pk=evento.id)

    elif arquivo.evento == 's5012':

        from emensageriapro.esocial.models import s5012evtIrrf
        from emensageriapro.esocial.views.s5012_evtirrf_gerar_xml import gerar_xml_s5012_func
        evento = s5012evtIrrf.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s5012_func(pk=evento.id)

    elif arquivo.evento == 's5013':

        from emensageriapro.esocial.models import s5013evtFGTS
        from emensageriapro.esocial.views.s5013_evtfgts_gerar_xml import gerar_xml_s5013_func
        evento = s5013evtFGTS.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_s5013_func(pk=evento.id)

    elif arquivo.evento == 'r1000':

        from emensageriapro.efdreinf.models import r1000evtInfoContri
        from emensageriapro.efdreinf.views.r1000_evtinfocontri_gerar_xml import gerar_xml_r1000_func
        evento = r1000evtInfoContri.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r1000_func(pk=evento.id)

    elif arquivo.evento == 'r1070':

        from emensageriapro.efdreinf.models import r1070evtTabProcesso
        from emensageriapro.efdreinf.views.r1070_evttabprocesso_gerar_xml import gerar_xml_r1070_func
        evento = r1070evtTabProcesso.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r1070_func(pk=evento.id)

    elif arquivo.evento == 'r2010':

        from emensageriapro.efdreinf.models import r2010evtServTom
        from emensageriapro.efdreinf.views.r2010_evtservtom_gerar_xml import gerar_xml_r2010_func
        evento = r2010evtServTom.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r2010_func(pk=evento.id)

    elif arquivo.evento == 'r2020':

        from emensageriapro.efdreinf.models import r2020evtServPrest
        from emensageriapro.efdreinf.views.r2020_evtservprest_gerar_xml import gerar_xml_r2020_func
        evento = r2020evtServPrest.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r2020_func(pk=evento.id)

    elif arquivo.evento == 'r2030':

        from emensageriapro.efdreinf.models import r2030evtAssocDespRec
        from emensageriapro.efdreinf.views.r2030_evtassocdesprec_gerar_xml import gerar_xml_r2030_func
        evento = r2030evtAssocDespRec.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r2030_func(pk=evento.id)

    elif arquivo.evento == 'r2040':

        from emensageriapro.efdreinf.models import r2040evtAssocDespRep
        from emensageriapro.efdreinf.views.r2040_evtassocdesprep_gerar_xml import gerar_xml_r2040_func
        evento = r2040evtAssocDespRep.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r2040_func(pk=evento.id)

    elif arquivo.evento == 'r2050':

        from emensageriapro.efdreinf.models import r2050evtComProd
        from emensageriapro.efdreinf.views.r2050_evtcomprod_gerar_xml import gerar_xml_r2050_func
        evento = r2050evtComProd.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r2050_func(pk=evento.id)

    elif arquivo.evento == 'r2060':

        from emensageriapro.efdreinf.models import r2060evtCPRB
        from emensageriapro.efdreinf.views.r2060_evtcprb_gerar_xml import gerar_xml_r2060_func
        evento = r2060evtCPRB.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r2060_func(pk=evento.id)

    elif arquivo.evento == 'r2070':

        from emensageriapro.efdreinf.models import r2070evtPgtosDivs
        from emensageriapro.efdreinf.views.r2070_evtpgtosdivs_gerar_xml import gerar_xml_r2070_func
        evento = r2070evtPgtosDivs.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r2070_func(pk=evento.id)

    elif arquivo.evento == 'r2098':

        from emensageriapro.efdreinf.models import r2098evtReabreEvPer
        from emensageriapro.efdreinf.views.r2098_evtreabreevper_gerar_xml import gerar_xml_r2098_func
        evento = r2098evtReabreEvPer.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r2098_func(pk=evento.id)

    elif arquivo.evento == 'r2099':

        from emensageriapro.efdreinf.models import r2099evtFechaEvPer
        from emensageriapro.efdreinf.views.r2099_evtfechaevper_gerar_xml import gerar_xml_r2099_func
        evento = r2099evtFechaEvPer.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r2099_func(pk=evento.id)

    elif arquivo.evento == 'r3010':

        from emensageriapro.efdreinf.models import r3010evtEspDesportivo
        from emensageriapro.efdreinf.views.r3010_evtespdesportivo_gerar_xml import gerar_xml_r3010_func
        evento = r3010evtEspDesportivo.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r3010_func(pk=evento.id)

    elif arquivo.evento == 'r4010':

        from emensageriapro.efdreinf.models import r4010evtRetPF
        from emensageriapro.efdreinf.views.r4010_evtretpf_gerar_xml import gerar_xml_r4010_func
        evento = r4010evtRetPF.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r4010_func(pk=evento.id)

    elif arquivo.evento == 'r4020':

        from emensageriapro.efdreinf.models import r4020evtRetPJ
        from emensageriapro.efdreinf.views.r4020_evtretpj_gerar_xml import gerar_xml_r4020_func
        evento = r4020evtRetPJ.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r4020_func(pk=evento.id)

    elif arquivo.evento == 'r4040':

        from emensageriapro.efdreinf.models import r4040evtBenefNId
        from emensageriapro.efdreinf.views.r4040_evtbenefnid_gerar_xml import gerar_xml_r4040_func
        evento = r4040evtBenefNId.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r4040_func(pk=evento.id)

    elif arquivo.evento == 'r4098':

        from emensageriapro.efdreinf.models import r4098evtReab
        from emensageriapro.efdreinf.views.r4098_evtreab_gerar_xml import gerar_xml_r4098_func
        evento = r4098evtReab.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r4098_func(pk=evento.id)

    elif arquivo.evento == 'r4099':

        from emensageriapro.efdreinf.models import r4099evtFech
        from emensageriapro.efdreinf.views.r4099_evtfech_gerar_xml import gerar_xml_r4099_func
        evento = r4099evtFech.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r4099_func(pk=evento.id)

    elif arquivo.evento == 'r5001':

        from emensageriapro.efdreinf.models import r5001evtTotal
        from emensageriapro.efdreinf.views.r5001_evttotal_gerar_xml import gerar_xml_r5001_func
        evento = r5001evtTotal.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r5001_func(pk=evento.id)

    elif arquivo.evento == 'r5011':

        from emensageriapro.efdreinf.models import r5011evtTotalContrib
        from emensageriapro.efdreinf.views.r5011_evttotalcontrib_gerar_xml import gerar_xml_r5011_func
        evento = r5011evtTotalContrib.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r5011_func(pk=evento.id)

    elif arquivo.evento == 'r9000':

        from emensageriapro.efdreinf.models import r9000evtExclusao
        from emensageriapro.efdreinf.views.r9000_evtexclusao_gerar_xml import gerar_xml_r9000_func
        evento = r9000evtExclusao.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r9000_func(pk=evento.id)

    elif arquivo.evento == 'r9001':

        from emensageriapro.efdreinf.models import r9001evtTotal
        from emensageriapro.efdreinf.views.r9001_evttotal_gerar_xml import gerar_xml_r9001_func
        evento = r9001evtTotal.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r9001_func(pk=evento.id)

    elif arquivo.evento == 'r9002':

        from emensageriapro.efdreinf.models import r9002evtRet
        from emensageriapro.efdreinf.views.r9002_evtret_gerar_xml import gerar_xml_r9002_func
        evento = r9002evtRet.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r9002_func(pk=evento.id)

    elif arquivo.evento == 'r9011':

        from emensageriapro.efdreinf.models import r9011evtTotalContrib
        from emensageriapro.efdreinf.views.r9011_evttotalcontrib_gerar_xml import gerar_xml_r9011_func
        evento = r9011evtTotalContrib.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r9011_func(pk=evento.id)

    elif arquivo.evento == 'r9012':

        from emensageriapro.efdreinf.models import r9012evtRetCons
        from emensageriapro.efdreinf.views.r9012_evtretcons_gerar_xml import gerar_xml_r9012_func
        evento = r9012evtRetCons.objects.get(arquivo=arquivo.arquivo)
        xml_ger = gerar_xml_r9012_func(pk=evento.id)

    for a in range(100):
        xml_ger = xml_ger.replace('> ', '>').replace(' <', '<').replace('\n', '\n')
        xml_imp = xml_imp.replace('> ', '>').replace(' <', '<').replace('\n', '\n')

    xml_ger = xml_ger.replace('</Reinf>', '').replace('</eSocial>', '')
    xml_imp = xml_imp.replace('</Reinf>', '').replace('</eSocial>', '')

    return xml_ger, xml_imp




def verificacao_importacao(request, pk):
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos

    arquivo = get_object_or_404(ImportacaoArquivosEventos, id=pk)

    xml_ger, xml_imp = verificacao_importacao_funcao(arquivo)

    if xml_ger in xml_imp:
        return HttpResponse("Correto!")

    else:
        return HttpResponse("Incorreto!")