#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"


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


import datetime
import json
import base64
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.mensageiro.models import TransmissorLoteEsocialOcorrencias
from emensageriapro.mensageiro.forms import form_transmissor_lote_esocial_ocorrencias
from emensageriapro.mensageiro.models import RetornosEventos
from emensageriapro.mensageiro.forms import form_retornos_eventos
from emensageriapro.esocial.models import s1000evtInfoEmpregador
from emensageriapro.esocial.forms import form_s1000_evtinfoempregador
from emensageriapro.esocial.models import s1005evtTabEstab
from emensageriapro.esocial.forms import form_s1005_evttabestab
from emensageriapro.esocial.models import s1010evtTabRubrica
from emensageriapro.esocial.forms import form_s1010_evttabrubrica
from emensageriapro.esocial.models import s1020evtTabLotacao
from emensageriapro.esocial.forms import form_s1020_evttablotacao
from emensageriapro.esocial.models import s1030evtTabCargo
from emensageriapro.esocial.forms import form_s1030_evttabcargo
from emensageriapro.esocial.models import s1035evtTabCarreira
from emensageriapro.esocial.forms import form_s1035_evttabcarreira
from emensageriapro.esocial.models import s1040evtTabFuncao
from emensageriapro.esocial.forms import form_s1040_evttabfuncao
from emensageriapro.esocial.models import s1050evtTabHorTur
from emensageriapro.esocial.forms import form_s1050_evttabhortur
from emensageriapro.esocial.models import s1060evtTabAmbiente
from emensageriapro.esocial.forms import form_s1060_evttabambiente
from emensageriapro.esocial.models import s1070evtTabProcesso
from emensageriapro.esocial.forms import form_s1070_evttabprocesso
from emensageriapro.esocial.models import s1080evtTabOperPort
from emensageriapro.esocial.forms import form_s1080_evttaboperport
from emensageriapro.esocial.models import s1200evtRemun
from emensageriapro.esocial.forms import form_s1200_evtremun
from emensageriapro.esocial.models import s1202evtRmnRPPS
from emensageriapro.esocial.forms import form_s1202_evtrmnrpps
from emensageriapro.esocial.models import s1207evtBenPrRP
from emensageriapro.esocial.forms import form_s1207_evtbenprrp
from emensageriapro.esocial.models import s1210evtPgtos
from emensageriapro.esocial.forms import form_s1210_evtpgtos
from emensageriapro.esocial.models import s1250evtAqProd
from emensageriapro.esocial.forms import form_s1250_evtaqprod
from emensageriapro.esocial.models import s1260evtComProd
from emensageriapro.esocial.forms import form_s1260_evtcomprod
from emensageriapro.esocial.models import s1270evtContratAvNP
from emensageriapro.esocial.forms import form_s1270_evtcontratavnp
from emensageriapro.esocial.models import s1280evtInfoComplPer
from emensageriapro.esocial.forms import form_s1280_evtinfocomplper
from emensageriapro.esocial.models import s1295evtTotConting
from emensageriapro.esocial.forms import form_s1295_evttotconting
from emensageriapro.esocial.models import s1298evtReabreEvPer
from emensageriapro.esocial.forms import form_s1298_evtreabreevper
from emensageriapro.esocial.models import s1299evtFechaEvPer
from emensageriapro.esocial.forms import form_s1299_evtfechaevper
from emensageriapro.esocial.models import s1300evtContrSindPatr
from emensageriapro.esocial.forms import form_s1300_evtcontrsindpatr
from emensageriapro.esocial.models import s2190evtAdmPrelim
from emensageriapro.esocial.forms import form_s2190_evtadmprelim
from emensageriapro.esocial.models import s2200evtAdmissao
from emensageriapro.esocial.forms import form_s2200_evtadmissao
from emensageriapro.esocial.models import s2205evtAltCadastral
from emensageriapro.esocial.forms import form_s2205_evtaltcadastral
from emensageriapro.esocial.models import s2206evtAltContratual
from emensageriapro.esocial.forms import form_s2206_evtaltcontratual
from emensageriapro.esocial.models import s2210evtCAT
from emensageriapro.esocial.forms import form_s2210_evtcat
from emensageriapro.esocial.models import s2220evtMonit
from emensageriapro.esocial.forms import form_s2220_evtmonit
from emensageriapro.esocial.models import s2221evtToxic
from emensageriapro.esocial.forms import form_s2221_evttoxic
from emensageriapro.esocial.models import s2230evtAfastTemp
from emensageriapro.esocial.forms import form_s2230_evtafasttemp
from emensageriapro.esocial.models import s2231evtCessao
from emensageriapro.esocial.forms import form_s2231_evtcessao
from emensageriapro.esocial.models import s2240evtExpRisco
from emensageriapro.esocial.forms import form_s2240_evtexprisco
from emensageriapro.esocial.models import s2241evtInsApo
from emensageriapro.esocial.forms import form_s2241_evtinsapo
from emensageriapro.esocial.models import s2245evtTreiCap
from emensageriapro.esocial.forms import form_s2245_evttreicap
from emensageriapro.esocial.models import s2250evtAvPrevio
from emensageriapro.esocial.forms import form_s2250_evtavprevio
from emensageriapro.esocial.models import s2260evtConvInterm
from emensageriapro.esocial.forms import form_s2260_evtconvinterm
from emensageriapro.esocial.models import s2298evtReintegr
from emensageriapro.esocial.forms import form_s2298_evtreintegr
from emensageriapro.esocial.models import s2299evtDeslig
from emensageriapro.esocial.forms import form_s2299_evtdeslig
from emensageriapro.esocial.models import s2300evtTSVInicio
from emensageriapro.esocial.forms import form_s2300_evttsvinicio
from emensageriapro.esocial.models import s2306evtTSVAltContr
from emensageriapro.esocial.forms import form_s2306_evttsvaltcontr
from emensageriapro.esocial.models import s2399evtTSVTermino
from emensageriapro.esocial.forms import form_s2399_evttsvtermino
from emensageriapro.esocial.models import s2400evtCdBenefIn
from emensageriapro.esocial.forms import form_s2400_evtcdbenefin
from emensageriapro.esocial.models import s2405evtCdBenefAlt
from emensageriapro.esocial.forms import form_s2405_evtcdbenefalt
from emensageriapro.esocial.models import s2410evtCdBenIn
from emensageriapro.esocial.forms import form_s2410_evtcdbenin
from emensageriapro.esocial.models import s2416evtCdBenAlt
from emensageriapro.esocial.forms import form_s2416_evtcdbenalt
from emensageriapro.esocial.models import s2420evtCdBenTerm
from emensageriapro.esocial.forms import form_s2420_evtcdbenterm
from emensageriapro.esocial.models import s3000evtExclusao
from emensageriapro.esocial.forms import form_s3000_evtexclusao
from emensageriapro.esocial.models import s5001evtBasesTrab
from emensageriapro.esocial.forms import form_s5001_evtbasestrab
from emensageriapro.esocial.models import s5002evtIrrfBenef
from emensageriapro.esocial.forms import form_s5002_evtirrfbenef
from emensageriapro.esocial.models import s5003evtBasesFGTS
from emensageriapro.esocial.forms import form_s5003_evtbasesfgts
from emensageriapro.esocial.models import s5011evtCS
from emensageriapro.esocial.forms import form_s5011_evtcs
from emensageriapro.esocial.models import s5012evtIrrf
from emensageriapro.esocial.forms import form_s5012_evtirrf
from emensageriapro.esocial.models import s5013evtFGTS
from emensageriapro.esocial.forms import form_s5013_evtfgts


@login_required
def salvar(request, pk=None, tab='master', output=None):

    if pk:

        transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial, id=pk)

    if request.user.has_perm('mensageiro.can_see_TransmissorLoteEsocial'):

        if pk:

            transmissor_lote_esocial_form = form_transmissor_lote_esocial(request.POST or None, instance=transmissor_lote_esocial)

        else:

            transmissor_lote_esocial_form = form_transmissor_lote_esocial(request.POST or None)

        if request.method == 'POST':

            if transmissor_lote_esocial_form.is_valid():

                #transmissor_lote_esocial_campos_multiple_passo1


                obj = transmissor_lote_esocial_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')
                #transmissor_lote_esocial_campos_multiple_passo2

                if 'return_page' in request.session and request.session['return_page'] and 'transmissor-lote-esocial' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        'transmissor_lote_esocial_salvar',
                        pk=obj.id)

            else:

                messages.error(request, 'Erro ao salvar!')

        transmissor_lote_esocial_form = disabled_form_fields(transmissor_lote_esocial_form, request.user.has_perm('mensageiro.change_TransmissorLoteEsocial'))
        #transmissor_lote_esocial_campos_multiple_passo3

        if output:

            transmissor_lote_esocial_form = disabled_form_for_print(transmissor_lote_esocial_form)


        transmissor_lote_esocial_ocorrencias_lista = None
        transmissor_lote_esocial_ocorrencias_form = None
        retornos_eventos_lista = None
        retornos_eventos_form = None
        s1000_evtinfoempregador_lista = None
        s1000_evtinfoempregador_form = None
        s1005_evttabestab_lista = None
        s1005_evttabestab_form = None
        s1010_evttabrubrica_lista = None
        s1010_evttabrubrica_form = None
        s1020_evttablotacao_lista = None
        s1020_evttablotacao_form = None
        s1030_evttabcargo_lista = None
        s1030_evttabcargo_form = None
        s1035_evttabcarreira_lista = None
        s1035_evttabcarreira_form = None
        s1040_evttabfuncao_lista = None
        s1040_evttabfuncao_form = None
        s1050_evttabhortur_lista = None
        s1050_evttabhortur_form = None
        s1060_evttabambiente_lista = None
        s1060_evttabambiente_form = None
        s1070_evttabprocesso_lista = None
        s1070_evttabprocesso_form = None
        s1080_evttaboperport_lista = None
        s1080_evttaboperport_form = None
        s1200_evtremun_lista = None
        s1200_evtremun_form = None
        s1202_evtrmnrpps_lista = None
        s1202_evtrmnrpps_form = None
        s1207_evtbenprrp_lista = None
        s1207_evtbenprrp_form = None
        s1210_evtpgtos_lista = None
        s1210_evtpgtos_form = None
        s1250_evtaqprod_lista = None
        s1250_evtaqprod_form = None
        s1260_evtcomprod_lista = None
        s1260_evtcomprod_form = None
        s1270_evtcontratavnp_lista = None
        s1270_evtcontratavnp_form = None
        s1280_evtinfocomplper_lista = None
        s1280_evtinfocomplper_form = None
        s1295_evttotconting_lista = None
        s1295_evttotconting_form = None
        s1298_evtreabreevper_lista = None
        s1298_evtreabreevper_form = None
        s1299_evtfechaevper_lista = None
        s1299_evtfechaevper_form = None
        s1300_evtcontrsindpatr_lista = None
        s1300_evtcontrsindpatr_form = None
        s2190_evtadmprelim_lista = None
        s2190_evtadmprelim_form = None
        s2200_evtadmissao_lista = None
        s2200_evtadmissao_form = None
        s2205_evtaltcadastral_lista = None
        s2205_evtaltcadastral_form = None
        s2206_evtaltcontratual_lista = None
        s2206_evtaltcontratual_form = None
        s2210_evtcat_lista = None
        s2210_evtcat_form = None
        s2220_evtmonit_lista = None
        s2220_evtmonit_form = None
        s2221_evttoxic_lista = None
        s2221_evttoxic_form = None
        s2230_evtafasttemp_lista = None
        s2230_evtafasttemp_form = None
        s2231_evtcessao_lista = None
        s2231_evtcessao_form = None
        s2240_evtexprisco_lista = None
        s2240_evtexprisco_form = None
        s2241_evtinsapo_lista = None
        s2241_evtinsapo_form = None
        s2245_evttreicap_lista = None
        s2245_evttreicap_form = None
        s2250_evtavprevio_lista = None
        s2250_evtavprevio_form = None
        s2260_evtconvinterm_lista = None
        s2260_evtconvinterm_form = None
        s2298_evtreintegr_lista = None
        s2298_evtreintegr_form = None
        s2299_evtdeslig_lista = None
        s2299_evtdeslig_form = None
        s2300_evttsvinicio_lista = None
        s2300_evttsvinicio_form = None
        s2306_evttsvaltcontr_lista = None
        s2306_evttsvaltcontr_form = None
        s2399_evttsvtermino_lista = None
        s2399_evttsvtermino_form = None
        s2400_evtcdbenefin_lista = None
        s2400_evtcdbenefin_form = None
        s2405_evtcdbenefalt_lista = None
        s2405_evtcdbenefalt_form = None
        s2410_evtcdbenin_lista = None
        s2410_evtcdbenin_form = None
        s2416_evtcdbenalt_lista = None
        s2416_evtcdbenalt_form = None
        s2420_evtcdbenterm_lista = None
        s2420_evtcdbenterm_form = None
        s3000_evtexclusao_lista = None
        s3000_evtexclusao_form = None
        s5001_evtbasestrab_lista = None
        s5001_evtbasestrab_form = None
        s5002_evtirrfbenef_lista = None
        s5002_evtirrfbenef_form = None
        s5003_evtbasesfgts_lista = None
        s5003_evtbasesfgts_form = None
        s5011_evtcs_lista = None
        s5011_evtcs_form = None
        s5012_evtirrf_lista = None
        s5012_evtirrf_form = None
        s5013_evtfgts_lista = None
        s5013_evtfgts_form = None

        if pk:

            transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial, id=pk)

            transmissor_lote_esocial_ocorrencias_form = form_transmissor_lote_esocial_ocorrencias(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            transmissor_lote_esocial_ocorrencias_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            transmissor_lote_esocial_ocorrencias_lista = TransmissorLoteEsocialOcorrencias.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            retornos_eventos_form = form_retornos_eventos(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            retornos_eventos_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            retornos_eventos_lista = RetornosEventos.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1000_evtinfoempregador_form = form_s1000_evtinfoempregador(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1000_evtinfoempregador_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1000_evtinfoempregador_lista = s1000evtInfoEmpregador.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1005_evttabestab_form = form_s1005_evttabestab(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1005_evttabestab_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1005_evttabestab_lista = s1005evtTabEstab.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1010_evttabrubrica_form = form_s1010_evttabrubrica(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1010_evttabrubrica_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1010_evttabrubrica_lista = s1010evtTabRubrica.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1020_evttablotacao_form = form_s1020_evttablotacao(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1020_evttablotacao_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1020_evttablotacao_lista = s1020evtTabLotacao.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1030_evttabcargo_form = form_s1030_evttabcargo(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1030_evttabcargo_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1030_evttabcargo_lista = s1030evtTabCargo.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1035_evttabcarreira_form = form_s1035_evttabcarreira(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1035_evttabcarreira_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1035_evttabcarreira_lista = s1035evtTabCarreira.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1040_evttabfuncao_form = form_s1040_evttabfuncao(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1040_evttabfuncao_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1040_evttabfuncao_lista = s1040evtTabFuncao.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1050_evttabhortur_form = form_s1050_evttabhortur(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1050_evttabhortur_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1050_evttabhortur_lista = s1050evtTabHorTur.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1060_evttabambiente_form = form_s1060_evttabambiente(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1060_evttabambiente_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1060_evttabambiente_lista = s1060evtTabAmbiente.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1070_evttabprocesso_form = form_s1070_evttabprocesso(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1070_evttabprocesso_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1070_evttabprocesso_lista = s1070evtTabProcesso.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1080_evttaboperport_form = form_s1080_evttaboperport(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1080_evttaboperport_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1080_evttaboperport_lista = s1080evtTabOperPort.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1200_evtremun_form = form_s1200_evtremun(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1200_evtremun_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1200_evtremun_lista = s1200evtRemun.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1202_evtrmnrpps_form = form_s1202_evtrmnrpps(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1202_evtrmnrpps_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1202_evtrmnrpps_lista = s1202evtRmnRPPS.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1207_evtbenprrp_form = form_s1207_evtbenprrp(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1207_evtbenprrp_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1207_evtbenprrp_lista = s1207evtBenPrRP.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1210_evtpgtos_form = form_s1210_evtpgtos(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1210_evtpgtos_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1210_evtpgtos_lista = s1210evtPgtos.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1250_evtaqprod_form = form_s1250_evtaqprod(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1250_evtaqprod_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1250_evtaqprod_lista = s1250evtAqProd.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1260_evtcomprod_form = form_s1260_evtcomprod(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1260_evtcomprod_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1260_evtcomprod_lista = s1260evtComProd.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1270_evtcontratavnp_form = form_s1270_evtcontratavnp(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1270_evtcontratavnp_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1270_evtcontratavnp_lista = s1270evtContratAvNP.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1280_evtinfocomplper_form = form_s1280_evtinfocomplper(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1280_evtinfocomplper_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1280_evtinfocomplper_lista = s1280evtInfoComplPer.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1295_evttotconting_form = form_s1295_evttotconting(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1295_evttotconting_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1295_evttotconting_lista = s1295evtTotConting.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1298_evtreabreevper_form = form_s1298_evtreabreevper(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1298_evtreabreevper_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1298_evtreabreevper_lista = s1298evtReabreEvPer.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1299_evtfechaevper_form = form_s1299_evtfechaevper(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1299_evtfechaevper_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1299_evtfechaevper_lista = s1299evtFechaEvPer.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s1300_evtcontrsindpatr_form = form_s1300_evtcontrsindpatr(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s1300_evtcontrsindpatr_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s1300_evtcontrsindpatr_lista = s1300evtContrSindPatr.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2190_evtadmprelim_form = form_s2190_evtadmprelim(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2190_evtadmprelim_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2190_evtadmprelim_lista = s2190evtAdmPrelim.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2200_evtadmissao_form = form_s2200_evtadmissao(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2200_evtadmissao_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2200_evtadmissao_lista = s2200evtAdmissao.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2205_evtaltcadastral_form = form_s2205_evtaltcadastral(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2205_evtaltcadastral_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2205_evtaltcadastral_lista = s2205evtAltCadastral.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2206_evtaltcontratual_form = form_s2206_evtaltcontratual(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2206_evtaltcontratual_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2206_evtaltcontratual_lista = s2206evtAltContratual.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2210_evtcat_form = form_s2210_evtcat(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2210_evtcat_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2210_evtcat_lista = s2210evtCAT.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2220_evtmonit_form = form_s2220_evtmonit(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2220_evtmonit_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2220_evtmonit_lista = s2220evtMonit.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2221_evttoxic_form = form_s2221_evttoxic(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2221_evttoxic_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2221_evttoxic_lista = s2221evtToxic.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2230_evtafasttemp_form = form_s2230_evtafasttemp(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2230_evtafasttemp_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2230_evtafasttemp_lista = s2230evtAfastTemp.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2231_evtcessao_form = form_s2231_evtcessao(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2231_evtcessao_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2231_evtcessao_lista = s2231evtCessao.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2240_evtexprisco_form = form_s2240_evtexprisco(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2240_evtexprisco_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2240_evtexprisco_lista = s2240evtExpRisco.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2241_evtinsapo_form = form_s2241_evtinsapo(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2241_evtinsapo_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2241_evtinsapo_lista = s2241evtInsApo.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2245_evttreicap_form = form_s2245_evttreicap(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2245_evttreicap_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2245_evttreicap_lista = s2245evtTreiCap.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2250_evtavprevio_form = form_s2250_evtavprevio(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2250_evtavprevio_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2250_evtavprevio_lista = s2250evtAvPrevio.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2260_evtconvinterm_form = form_s2260_evtconvinterm(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2260_evtconvinterm_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2260_evtconvinterm_lista = s2260evtConvInterm.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2298_evtreintegr_form = form_s2298_evtreintegr(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2298_evtreintegr_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2298_evtreintegr_lista = s2298evtReintegr.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2299_evtdeslig_form = form_s2299_evtdeslig(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2299_evtdeslig_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2299_evtdeslig_lista = s2299evtDeslig.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2300_evttsvinicio_form = form_s2300_evttsvinicio(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2300_evttsvinicio_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2300_evttsvinicio_lista = s2300evtTSVInicio.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2306_evttsvaltcontr_form = form_s2306_evttsvaltcontr(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2306_evttsvaltcontr_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2306_evttsvaltcontr_lista = s2306evtTSVAltContr.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2399_evttsvtermino_form = form_s2399_evttsvtermino(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2399_evttsvtermino_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2399_evttsvtermino_lista = s2399evtTSVTermino.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2400_evtcdbenefin_form = form_s2400_evtcdbenefin(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2400_evtcdbenefin_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2400_evtcdbenefin_lista = s2400evtCdBenefIn.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2405_evtcdbenefalt_form = form_s2405_evtcdbenefalt(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2405_evtcdbenefalt_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2405_evtcdbenefalt_lista = s2405evtCdBenefAlt.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2410_evtcdbenin_form = form_s2410_evtcdbenin(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2410_evtcdbenin_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2410_evtcdbenin_lista = s2410evtCdBenIn.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2416_evtcdbenalt_form = form_s2416_evtcdbenalt(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2416_evtcdbenalt_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2416_evtcdbenalt_lista = s2416evtCdBenAlt.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s2420_evtcdbenterm_form = form_s2420_evtcdbenterm(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s2420_evtcdbenterm_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s2420_evtcdbenterm_lista = s2420evtCdBenTerm.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s3000_evtexclusao_form = form_s3000_evtexclusao(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s3000_evtexclusao_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s3000_evtexclusao_lista = s3000evtExclusao.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s5001_evtbasestrab_form = form_s5001_evtbasestrab(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s5001_evtbasestrab_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s5001_evtbasestrab_lista = s5001evtBasesTrab.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s5002_evtirrfbenef_form = form_s5002_evtirrfbenef(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s5002_evtirrfbenef_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s5002_evtirrfbenef_lista = s5002evtIrrfBenef.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s5003_evtbasesfgts_form = form_s5003_evtbasesfgts(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s5003_evtbasesfgts_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s5003_evtbasesfgts_lista = s5003evtBasesFGTS.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s5011_evtcs_form = form_s5011_evtcs(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s5011_evtcs_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s5011_evtcs_lista = s5011evtCS.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s5012_evtirrf_form = form_s5012_evtirrf(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s5012_evtirrf_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s5012_evtirrf_lista = s5012evtIrrf.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

            s5013_evtfgts_form = form_s5013_evtfgts(
                initial={ 'transmissor_lote_esocial': transmissor_lote_esocial })
            s5013_evtfgts_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            s5013_evtfgts_lista = s5013evtFGTS.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()


        else:

            transmissor_lote_esocial = None

        from django.db.models import Q

        if transmissor_lote_esocial:
            transmissor_eventos_esocial_lista = TransmissorEventosEsocial.objects.\
                filter(Q(transmissor_lote_esocial_id=transmissor_lote_esocial.id) | Q(transmissor_lote_esocial_error_id=transmissor_lote_esocial.id)).all()
            transmissor_eventos_esocial_totalizacoes_lista = TransmissorEventosEsocialTotalizacoes.objects.\
                filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

        else:
            transmissor_eventos_esocial_lista = None
            transmissor_eventos_esocial_totalizacoes_lista = None

        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'transmissor_lote_esocial': transmissor_lote_esocial,
            'transmissor_lote_esocial_form': transmissor_lote_esocial_form,
            'transmissor_lote_esocial_ocorrencias_form': transmissor_lote_esocial_ocorrencias_form,
            'transmissor_lote_esocial_ocorrencias_lista': transmissor_lote_esocial_ocorrencias_lista,
            'retornos_eventos_form': retornos_eventos_form,
            'retornos_eventos_lista': retornos_eventos_lista,
            's1000_evtinfoempregador_form': s1000_evtinfoempregador_form,
            's1000_evtinfoempregador_lista': s1000_evtinfoempregador_lista,
            's1005_evttabestab_form': s1005_evttabestab_form,
            's1005_evttabestab_lista': s1005_evttabestab_lista,
            's1010_evttabrubrica_form': s1010_evttabrubrica_form,
            's1010_evttabrubrica_lista': s1010_evttabrubrica_lista,
            's1020_evttablotacao_form': s1020_evttablotacao_form,
            's1020_evttablotacao_lista': s1020_evttablotacao_lista,
            's1030_evttabcargo_form': s1030_evttabcargo_form,
            's1030_evttabcargo_lista': s1030_evttabcargo_lista,
            's1035_evttabcarreira_form': s1035_evttabcarreira_form,
            's1035_evttabcarreira_lista': s1035_evttabcarreira_lista,
            's1040_evttabfuncao_form': s1040_evttabfuncao_form,
            's1040_evttabfuncao_lista': s1040_evttabfuncao_lista,
            's1050_evttabhortur_form': s1050_evttabhortur_form,
            's1050_evttabhortur_lista': s1050_evttabhortur_lista,
            's1060_evttabambiente_form': s1060_evttabambiente_form,
            's1060_evttabambiente_lista': s1060_evttabambiente_lista,
            's1070_evttabprocesso_form': s1070_evttabprocesso_form,
            's1070_evttabprocesso_lista': s1070_evttabprocesso_lista,
            's1080_evttaboperport_form': s1080_evttaboperport_form,
            's1080_evttaboperport_lista': s1080_evttaboperport_lista,
            's1200_evtremun_form': s1200_evtremun_form,
            's1200_evtremun_lista': s1200_evtremun_lista,
            's1202_evtrmnrpps_form': s1202_evtrmnrpps_form,
            's1202_evtrmnrpps_lista': s1202_evtrmnrpps_lista,
            's1207_evtbenprrp_form': s1207_evtbenprrp_form,
            's1207_evtbenprrp_lista': s1207_evtbenprrp_lista,
            's1210_evtpgtos_form': s1210_evtpgtos_form,
            's1210_evtpgtos_lista': s1210_evtpgtos_lista,
            's1250_evtaqprod_form': s1250_evtaqprod_form,
            's1250_evtaqprod_lista': s1250_evtaqprod_lista,
            's1260_evtcomprod_form': s1260_evtcomprod_form,
            's1260_evtcomprod_lista': s1260_evtcomprod_lista,
            's1270_evtcontratavnp_form': s1270_evtcontratavnp_form,
            's1270_evtcontratavnp_lista': s1270_evtcontratavnp_lista,
            's1280_evtinfocomplper_form': s1280_evtinfocomplper_form,
            's1280_evtinfocomplper_lista': s1280_evtinfocomplper_lista,
            's1295_evttotconting_form': s1295_evttotconting_form,
            's1295_evttotconting_lista': s1295_evttotconting_lista,
            's1298_evtreabreevper_form': s1298_evtreabreevper_form,
            's1298_evtreabreevper_lista': s1298_evtreabreevper_lista,
            's1299_evtfechaevper_form': s1299_evtfechaevper_form,
            's1299_evtfechaevper_lista': s1299_evtfechaevper_lista,
            's1300_evtcontrsindpatr_form': s1300_evtcontrsindpatr_form,
            's1300_evtcontrsindpatr_lista': s1300_evtcontrsindpatr_lista,
            's2190_evtadmprelim_form': s2190_evtadmprelim_form,
            's2190_evtadmprelim_lista': s2190_evtadmprelim_lista,
            's2200_evtadmissao_form': s2200_evtadmissao_form,
            's2200_evtadmissao_lista': s2200_evtadmissao_lista,
            's2205_evtaltcadastral_form': s2205_evtaltcadastral_form,
            's2205_evtaltcadastral_lista': s2205_evtaltcadastral_lista,
            's2206_evtaltcontratual_form': s2206_evtaltcontratual_form,
            's2206_evtaltcontratual_lista': s2206_evtaltcontratual_lista,
            's2210_evtcat_form': s2210_evtcat_form,
            's2210_evtcat_lista': s2210_evtcat_lista,
            's2220_evtmonit_form': s2220_evtmonit_form,
            's2220_evtmonit_lista': s2220_evtmonit_lista,
            's2221_evttoxic_form': s2221_evttoxic_form,
            's2221_evttoxic_lista': s2221_evttoxic_lista,
            's2230_evtafasttemp_form': s2230_evtafasttemp_form,
            's2230_evtafasttemp_lista': s2230_evtafasttemp_lista,
            's2231_evtcessao_form': s2231_evtcessao_form,
            's2231_evtcessao_lista': s2231_evtcessao_lista,
            's2240_evtexprisco_form': s2240_evtexprisco_form,
            's2240_evtexprisco_lista': s2240_evtexprisco_lista,
            's2241_evtinsapo_form': s2241_evtinsapo_form,
            's2241_evtinsapo_lista': s2241_evtinsapo_lista,
            's2245_evttreicap_form': s2245_evttreicap_form,
            's2245_evttreicap_lista': s2245_evttreicap_lista,
            's2250_evtavprevio_form': s2250_evtavprevio_form,
            's2250_evtavprevio_lista': s2250_evtavprevio_lista,
            's2260_evtconvinterm_form': s2260_evtconvinterm_form,
            's2260_evtconvinterm_lista': s2260_evtconvinterm_lista,
            's2298_evtreintegr_form': s2298_evtreintegr_form,
            's2298_evtreintegr_lista': s2298_evtreintegr_lista,
            's2299_evtdeslig_form': s2299_evtdeslig_form,
            's2299_evtdeslig_lista': s2299_evtdeslig_lista,
            's2300_evttsvinicio_form': s2300_evttsvinicio_form,
            's2300_evttsvinicio_lista': s2300_evttsvinicio_lista,
            's2306_evttsvaltcontr_form': s2306_evttsvaltcontr_form,
            's2306_evttsvaltcontr_lista': s2306_evttsvaltcontr_lista,
            's2399_evttsvtermino_form': s2399_evttsvtermino_form,
            's2399_evttsvtermino_lista': s2399_evttsvtermino_lista,
            's2400_evtcdbenefin_form': s2400_evtcdbenefin_form,
            's2400_evtcdbenefin_lista': s2400_evtcdbenefin_lista,
            's2405_evtcdbenefalt_form': s2405_evtcdbenefalt_form,
            's2405_evtcdbenefalt_lista': s2405_evtcdbenefalt_lista,
            's2410_evtcdbenin_form': s2410_evtcdbenin_form,
            's2410_evtcdbenin_lista': s2410_evtcdbenin_lista,
            's2416_evtcdbenalt_form': s2416_evtcdbenalt_form,
            's2416_evtcdbenalt_lista': s2416_evtcdbenalt_lista,
            's2420_evtcdbenterm_form': s2420_evtcdbenterm_form,
            's2420_evtcdbenterm_lista': s2420_evtcdbenterm_lista,
            's3000_evtexclusao_form': s3000_evtexclusao_form,
            's3000_evtexclusao_lista': s3000_evtexclusao_lista,
            's5001_evtbasestrab_form': s5001_evtbasestrab_form,
            's5001_evtbasestrab_lista': s5001_evtbasestrab_lista,
            's5002_evtirrfbenef_form': s5002_evtirrfbenef_form,
            's5002_evtirrfbenef_lista': s5002_evtirrfbenef_lista,
            's5003_evtbasesfgts_form': s5003_evtbasesfgts_form,
            's5003_evtbasesfgts_lista': s5003_evtbasesfgts_lista,
            's5011_evtcs_form': s5011_evtcs_form,
            's5011_evtcs_lista': s5011_evtcs_lista,
            's5012_evtirrf_form': s5012_evtirrf_form,
            's5012_evtirrf_lista': s5012_evtirrf_lista,
            's5013_evtfgts_form': s5013_evtfgts_form,
            's5013_evtfgts_lista': s5013_evtfgts_lista,
            'modulos': ['mensageiro', ],
            'paginas': ['transmissor_lote_esocial', ],
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'transmissor_eventos_esocial_lista': transmissor_eventos_esocial_lista,
            'transmissor_eventos_esocial_totalizacoes_lista': transmissor_eventos_esocial_totalizacoes_lista,
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='transmissor_lote_esocial_salvar.html',
                filename="transmissor_lote_esocial.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True})
         
            return response

        elif output == 'xls':

            from django.shortcuts import render_to_response

            response = render_to_response('transmissor_lote_esocial_salvar.html', context)
            filename = "transmissor_lote_esocial.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 'transmissor_lote_esocial_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['mensageiro', ],
            'paginas': ['transmissor_lote_esocial', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
            'permissao_negada.html',
            context)