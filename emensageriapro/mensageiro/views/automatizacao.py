#coding: utf-8

import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64


def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def scripts_validacao_automatica(request):
    db_slug = 'default'

    from emensageriapro.esocial.models import s1000evtInfoEmpregador
    lista = s1000evtInfoEmpregador.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1000_evtinfoempregador_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1005evtTabEstab
    lista = s1005evtTabEstab.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1005_evttabestab_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1010evtTabRubrica
    lista = s1010evtTabRubrica.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1010_evttabrubrica_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1020evtTabLotacao
    lista = s1020evtTabLotacao.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1020_evttablotacao_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1030evtTabCargo
    lista = s1030evtTabCargo.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1030_evttabcargo_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1035evtTabCarreira
    lista = s1035evtTabCarreira.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1035_evttabcarreira_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1040evtTabFuncao
    lista = s1040evtTabFuncao.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1040_evttabfuncao_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1050evtTabHorTur
    lista = s1050evtTabHorTur.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1050_evttabhortur_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1060evtTabAmbiente
    lista = s1060evtTabAmbiente.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1060_evttabambiente_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1070evtTabProcesso
    lista = s1070evtTabProcesso.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1070_evttabprocesso_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1080evtTabOperPort
    lista = s1080evtTabOperPort.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1080_evttaboperport_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1200evtRemun
    lista = s1200evtRemun.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1200_evtremun_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1202evtRmnRPPS
    lista = s1202evtRmnRPPS.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1202_evtrmnrpps_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1207evtBenPrRP
    lista = s1207evtBenPrRP.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1207_evtbenprrp_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1210evtPgtos
    lista = s1210evtPgtos.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1210_evtpgtos_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1250evtAqProd
    lista = s1250evtAqProd.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1250_evtaqprod_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1260evtComProd
    lista = s1260evtComProd.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1260_evtcomprod_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1270evtContratAvNP
    lista = s1270evtContratAvNP.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1270_evtcontratavnp_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1280evtInfoComplPer
    lista = s1280evtInfoComplPer.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1280_evtinfocomplper_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1295evtTotConting
    lista = s1295evtTotConting.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1295_evttotconting_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1298evtReabreEvPer
    lista = s1298evtReabreEvPer.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1298_evtreabreevper_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1299evtFechaEvPer
    lista = s1299evtFechaEvPer.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1299_evtfechaevper_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s1300evtContrSindPatr
    lista = s1300evtContrSindPatr.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2190evtAdmPrelim
    lista = s2190evtAdmPrelim.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2190_evtadmprelim_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2200evtAdmissao
    lista = s2200evtAdmissao.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2200_evtadmissao_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2205evtAltCadastral
    lista = s2205evtAltCadastral.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2205_evtaltcadastral_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2206evtAltContratual
    lista = s2206evtAltContratual.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2206_evtaltcontratual_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2210evtCAT
    lista = s2210evtCAT.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2210_evtcat_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2220evtMonit
    lista = s2220evtMonit.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2220_evtmonit_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2230evtAfastTemp
    lista = s2230evtAfastTemp.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2230_evtafasttemp_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2240evtExpRisco
    lista = s2240evtExpRisco.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2240_evtexprisco_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2241evtInsApo
    lista = s2241evtInsApo.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2241_evtinsapo_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2250evtAvPrevio
    lista = s2250evtAvPrevio.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2250_evtavprevio_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2260evtConvInterm
    lista = s2260evtConvInterm.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2260_evtconvinterm_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2298evtReintegr
    lista = s2298evtReintegr.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2298_evtreintegr_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2299evtDeslig
    lista = s2299evtDeslig.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2299_evtdeslig_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2300evtTSVInicio
    lista = s2300evtTSVInicio.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2300_evttsvinicio_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2306evtTSVAltContr
    lista = s2306evtTSVAltContr.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2399evtTSVTermino
    lista = s2399evtTSVTermino.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2399_evttsvtermino_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s2400evtCdBenPrRP
    lista = s2400evtCdBenPrRP.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s2400_evtcdbenprrp_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.esocial.models import s3000evtExclusao
    lista = s3000evtExclusao.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.esocial.views.s3000_evtexclusao_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    # from emensageriapro.esocial.models import s5001evtBasesTrab
    # lista = s5001evtBasesTrab.objects.using( db_slug ).filter(status__in=[1,4]).all()
    # if lista:
    #     from emensageriapro.esocial.views.s5001_evtbasestrab_verificar import validar_evento_funcao
    # for a in lista:
    #     validar_evento_funcao(a.id, db_slug)
    #
    #
    # from emensageriapro.esocial.models import s5002evtIrrfBenef
    # lista = s5002evtIrrfBenef.objects.using( db_slug ).filter(status__in=[1,4]).all()
    # if lista:
    #     from emensageriapro.esocial.views.s5002_evtirrfbenef_verificar import validar_evento_funcao
    # for a in lista:
    #     validar_evento_funcao(a.id, db_slug)
    #
    #
    # from emensageriapro.esocial.models import s5011evtCS
    # lista = s5011evtCS.objects.using( db_slug ).filter(status__in=[1,4]).all()
    # if lista:
    #     from emensageriapro.esocial.views.s5011_evtcs_verificar import validar_evento_funcao
    # for a in lista:
    #     validar_evento_funcao(a.id, db_slug)
    #
    #
    # from emensageriapro.esocial.models import s5012evtIrrf
    # lista = s5012evtIrrf.objects.using( db_slug ).filter(status__in=[1,4]).all()
    # if lista:
    #     from emensageriapro.esocial.views.s5012_evtirrf_verificar import validar_evento_funcao
    # for a in lista:
    #     validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r1000evtInfoContri
    lista = r1000evtInfoContri.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r1070evtTabProcesso
    lista = r1070evtTabProcesso.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r2010evtServTom
    lista = r2010evtServTom.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r2010_evtservtom_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r2020evtServPrest
    lista = r2020evtServPrest.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r2020_evtservprest_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r2030evtAssocDespRec
    lista = r2030evtAssocDespRec.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r2040evtAssocDespRep
    lista = r2040evtAssocDespRep.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r2050evtComProd
    lista = r2050evtComProd.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r2050_evtcomprod_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r2060evtCPRB
    lista = r2060evtCPRB.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r2060_evtcprb_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r2070evtPgtosDivs
    lista = r2070evtPgtosDivs.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r2098evtReabreEvPer
    lista = r2098evtReabreEvPer.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r2099evtFechaEvPer
    lista = r2099evtFechaEvPer.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r3010evtEspDesportivo
    lista = r3010evtEspDesportivo.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)

    #
    # from emensageriapro.efdreinf.models import r5001evtTotal
    # lista = r5001evtTotal.objects.using( db_slug ).filter(status__in=[1,4]).all()
    # if lista:
    #     from emensageriapro.efdreinf.views.r5001_evttotal_verificar import validar_evento_funcao
    # for a in lista:
    #     validar_evento_funcao(a.id, db_slug)
    #
    #
    # from emensageriapro.efdreinf.models import r5011evtTotalContrib
    # lista = r5011evtTotalContrib.objects.using( db_slug ).filter(status__in=[1,4]).all()
    # if lista:
    #     from emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar import validar_evento_funcao
    # for a in lista:
    #     validar_evento_funcao(a.id, db_slug)


    from emensageriapro.efdreinf.models import r9000evtExclusao
    lista = r9000evtExclusao.objects.using( db_slug ).filter(status__in=[1,4]).all()
    if lista:
        from emensageriapro.efdreinf.views.r9000_evtexclusao_verificar import validar_evento_funcao
    for a in lista:
        validar_evento_funcao(a.id, db_slug)

    return HttpResponse('')





def script_criar_lote_esocial(transmissor_id, grupo):
    from emensageriapro.mensageiro.models import TransmissorLote, TransmissorLoteEsocial
    from datetime import datetime
    db_slug = 'default'
    transmissor = get_object_or_404(TransmissorLote.objects.using(db_slug),
                                    excluido=False, id=1)
    dados = {}
    dados['transmissor'] = transmissor
    dados['empregador_tpinsc'] = transmissor.tipo_inscricao
    dados['empregador_nrinsc'] = transmissor.cpf_cnpj
    dados['grupo'] = grupo
    dados['status'] = 0
    dados['resposta_codigo'] = 0
    dados['criado_em'] = datetime.now()
    dados['criado_por_id'] = 1
    dados['excluido'] = False
    obj = TransmissorLoteEsocial(**dados)
    obj.save(using=db_slug)
    return obj.id


def script_criar_lote_efdreinf(transmissor_id, grupo):
    from emensageriapro.mensageiro.models import TransmissorLote, TransmissorLoteEfdreinf
    from datetime import datetime
    db_slug = 'default'
    transmissor = get_object_or_404(TransmissorLote.objects.using(db_slug),
                                    excluido=False, id=1)
    dados = {}
    dados['transmissor'] = transmissor
    dados['contribuinte_tpinsc'] = transmissor.tipo_inscricao
    dados['contribuinte_nrinsc'] = transmissor.cpf_cnpj
    dados['grupo'] = grupo
    dados['status'] = 0
    dados['codigo_status'] = 0
    dados['retorno_descricao'] = '-'
    dados['criado_em'] = datetime.now()
    dados['criado_por_id'] = 1
    dados['excluido'] = False
    obj = TransmissorLoteEfdreinf(**dados)
    obj.save(using=db_slug)
    return obj.id





def scripts_transmissao_automatica_esocial(request):
    from emensageriapro.mensageiro.models import TransmissorLote, TransmissorLoteEsocial
    from emensageriapro.mensageiro.views.transmissor_esocial import vincular_eventos_esocial_transmissor
    db_slug = 'default'
    transmissor = get_object_or_404(TransmissorLote.objects.using(db_slug),
                                    excluido=False, id=1)

    #
    # Consultando eventos automaticamente
    #

    transmissores_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(status=7, excluido=False).all()
    from emensageriapro.funcoes_esocial import send_xml
    for tel in transmissores_esocial_lista:
        a = send_xml(request, tel.id, 'WsConsultarLoteEventos')

    #
    # Vinculando eventos a lotes criados
    #

    transmissores_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(status=0, excluido=False).all()
    for tel in transmissores_esocial_lista:
        vincular_eventos_esocial_transmissor(tel.id)

    #
    # Criando lotes de eventos não vinculados
    #

    grupos = [1,2,3]

    for grupo in grupos:

        esocial_lista = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(status=4, grupo=grupo, excluido=False).all()
        quant = int(len(esocial_lista)/transmissor.esocial_lote_max)
        if len(esocial_lista) and quant == 0:
            quant = 1
        for c in range(quant):
            transmissor_esocial_id = script_criar_lote_esocial(1, grupo)
            vincular_eventos_esocial_transmissor(transmissor_esocial_id)

    #
    # Transmitindo os lotes
    #

    transmissores_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(
        status=0, excluido=False).all()
    for tel in transmissores_esocial_lista:
        a = send_xml(request, tel.id, 'WsEnviarLoteEventos')





def scripts_transmissao_automatica_efdreinf(request):
    from emensageriapro.mensageiro.models import TransmissorLote, TransmissorLoteEfdreinf
    from emensageriapro.mensageiro.views.transmissor_efdreinf import vincular_eventos_efdreinf_transmissor
    db_slug = 'default'
    transmissor = get_object_or_404(TransmissorLote.objects.using(db_slug),
                                    excluido=False, id=1)

    #
    # Consultando eventos automaticamente
    #

    transmissores_efdreinf_lista = TransmissorLoteEfdreinf.objects.using( db_slug ).\
        filter(status=7, excluido=False).all()
    from emensageriapro.funcoes_efdreinf import send_xml
    for tel in transmissores_efdreinf_lista:
        a = send_xml(request, tel.id, 'ConsultasReinf')

    #
    # Vinculando eventos a lotes criados
    #

    transmissores_efdreinf_lista = TransmissorLoteEfdreinf.objects.using( db_slug ).\
        filter(status=0, excluido=False).all()
    for tel in transmissores_efdreinf_lista:
        vincular_eventos_efdreinf_transmissor(tel.id)

    #
    # Criando lotes de eventos não vinculados
    #

    grupos = [1,2,3]

    for grupo in grupos:

        efdreinf_lista = TransmissorEventosEfdreinf.objects.using( db_slug ).filter(status=4, grupo=grupo, excluido=False).all()
        quant = int(len(efdreinf_lista)/transmissor.efdreinf_lote_max)
        if len(efdreinf_lista) and quant == 0:
            quant = 1
        for c in range(quant):
            transmissor_efdreinf_id = script_criar_lote_efdreinf(1, grupo)
            vincular_eventos_efdreinf_transmissor(transmissor_efdreinf_id)
    #
    # Transmitindo os lotes
    #

    transmissores_efdreinf_lista = TransmissorLoteEfdreinf.objects.using( db_slug ).filter(status=0, excluido=False).all()
    for tel in transmissores_efdreinf_lista:
        a = send_xml(request, tel.id, 'RecepcaoLoteReinf')





def scripts_transmissao_automatica(request):
    from emensageriapro.mensageiro.models import TransmissorLote
    db_slug = 'default'
    scripts_validacao_automatica(request)
    transmissor = get_object_or_404(TransmissorLote.objects.using(db_slug),
                                    excluido=False, id=1)
    #
    # eSocial
    #

    tempo_prox_envio = transmissor.esocial_tempo_prox_envio or 1
    tempo = tempo_prox_envio - 1

    if tempo == 0:
        scripts_transmissao_automatica_esocial(request)
        TransmissorLote.objects.using(db_slug).filter(id=1).\
            update(esocial_tempo_prox_envio=transmissor.esocial_intervalo)
    else:
        TransmissorLote.objects.using(db_slug).filter(id=1).\
            update(esocial_tempo_prox_envio=tempo)

    #
    # EFD-Reinf
    #

    tempo_prox_envio = transmissor.efdreinf_tempo_prox_envio or 1
    tempo = tempo_prox_envio - 1

    if tempo == 0:
        scripts_transmissao_automatica_efdreinf(request)
        TransmissorLote.objects.using(db_slug).filter(id=1).\
            update(efdreinf_tempo_prox_envio=transmissor.efdreinf_intervalo)
    else:
        TransmissorLote.objects.using(db_slug).filter(id=1).\
            update(efdreinf_tempo_prox_envio=tempo)
    from emensageriapro.padrao import executar_sql
    executar_sql("""
    update public.transmissores SET esocial_tempo_prox_envio = esocial_intervalo
        WHERE esocial_tempo_prox_envio > esocial_intervalo;

        update public.transmissores SET efdreinf_tempo_prox_envio = efdreinf_intervalo
        WHERE efdreinf_tempo_prox_envio > efdreinf_intervalo;
    """, False)

    return HttpResponse('')



