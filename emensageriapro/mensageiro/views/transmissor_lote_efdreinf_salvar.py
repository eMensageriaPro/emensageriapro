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
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinfOcorrencias
from emensageriapro.mensageiro.forms import form_transmissor_lote_efdreinf_ocorrencias
from emensageriapro.efdreinf.models import r1000evtInfoContri
from emensageriapro.efdreinf.forms import form_r1000_evtinfocontri
from emensageriapro.efdreinf.models import r1070evtTabProcesso
from emensageriapro.efdreinf.forms import form_r1070_evttabprocesso
from emensageriapro.efdreinf.models import r2010evtServTom
from emensageriapro.efdreinf.forms import form_r2010_evtservtom
from emensageriapro.efdreinf.models import r2020evtServPrest
from emensageriapro.efdreinf.forms import form_r2020_evtservprest
from emensageriapro.efdreinf.models import r2030evtAssocDespRec
from emensageriapro.efdreinf.forms import form_r2030_evtassocdesprec
from emensageriapro.efdreinf.models import r2040evtAssocDespRep
from emensageriapro.efdreinf.forms import form_r2040_evtassocdesprep
from emensageriapro.efdreinf.models import r2050evtComProd
from emensageriapro.efdreinf.forms import form_r2050_evtcomprod
from emensageriapro.efdreinf.models import r2060evtCPRB
from emensageriapro.efdreinf.forms import form_r2060_evtcprb
from emensageriapro.efdreinf.models import r2070evtPgtosDivs
from emensageriapro.efdreinf.forms import form_r2070_evtpgtosdivs
from emensageriapro.efdreinf.models import r2098evtReabreEvPer
from emensageriapro.efdreinf.forms import form_r2098_evtreabreevper
from emensageriapro.efdreinf.models import r2099evtFechaEvPer
from emensageriapro.efdreinf.forms import form_r2099_evtfechaevper
from emensageriapro.efdreinf.models import r3010evtEspDesportivo
from emensageriapro.efdreinf.forms import form_r3010_evtespdesportivo
from emensageriapro.efdreinf.models import r4010evtRetPF
from emensageriapro.efdreinf.forms import form_r4010_evtretpf
from emensageriapro.efdreinf.models import r4020evtRetPJ
from emensageriapro.efdreinf.forms import form_r4020_evtretpj
from emensageriapro.efdreinf.models import r4040evtBenefNId
from emensageriapro.efdreinf.forms import form_r4040_evtbenefnid
from emensageriapro.efdreinf.models import r4098evtReab
from emensageriapro.efdreinf.forms import form_r4098_evtreab
from emensageriapro.efdreinf.models import r4099evtFech
from emensageriapro.efdreinf.forms import form_r4099_evtfech
from emensageriapro.efdreinf.models import r5001evtTotal
from emensageriapro.efdreinf.forms import form_r5001_evttotal
from emensageriapro.efdreinf.models import r5011evtTotalContrib
from emensageriapro.efdreinf.forms import form_r5011_evttotalcontrib
from emensageriapro.efdreinf.models import r9000evtExclusao
from emensageriapro.efdreinf.forms import form_r9000_evtexclusao
from emensageriapro.efdreinf.models import r9001evtTotal
from emensageriapro.efdreinf.forms import form_r9001_evttotal
from emensageriapro.efdreinf.models import r9002evtRet
from emensageriapro.efdreinf.forms import form_r9002_evtret
from emensageriapro.efdreinf.models import r9011evtTotalContrib
from emensageriapro.efdreinf.forms import form_r9011_evttotalcontrib
from emensageriapro.efdreinf.models import r9012evtRetCons
from emensageriapro.efdreinf.forms import form_r9012_evtretcons


@login_required
def salvar(request, pk=None, tab='master', output=None):

    if pk:

        transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf, id=pk)

    if request.user.has_perm('mensageiro.can_see_TransmissorLoteEfdreinf'):

        if pk:

            transmissor_lote_efdreinf_form = form_transmissor_lote_efdreinf(request.POST or None, instance=transmissor_lote_efdreinf)

        else:

            transmissor_lote_efdreinf_form = form_transmissor_lote_efdreinf(request.POST or None)

        if request.method == 'POST':

            if transmissor_lote_efdreinf_form.is_valid():

                #transmissor_lote_efdreinf_campos_multiple_passo1


                obj = transmissor_lote_efdreinf_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')
                #transmissor_lote_efdreinf_campos_multiple_passo2

                if 'return_page' in request.session and request.session['return_page'] and 'transmissor-lote-efdreinf' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        'transmissor_lote_efdreinf_salvar',
                        pk=obj.id)

            else:

                messages.error(request, 'Erro ao salvar!')

        transmissor_lote_efdreinf_form = disabled_form_fields(transmissor_lote_efdreinf_form, request.user.has_perm('mensageiro.change_TransmissorLoteEfdreinf'))
        #transmissor_lote_efdreinf_campos_multiple_passo3

        if output:

            transmissor_lote_efdreinf_form = disabled_form_for_print(transmissor_lote_efdreinf_form)


        transmissor_lote_efdreinf_ocorrencias_lista = None
        transmissor_lote_efdreinf_ocorrencias_form = None
        r1000_evtinfocontri_lista = None
        r1000_evtinfocontri_form = None
        r1070_evttabprocesso_lista = None
        r1070_evttabprocesso_form = None
        r2010_evtservtom_lista = None
        r2010_evtservtom_form = None
        r2020_evtservprest_lista = None
        r2020_evtservprest_form = None
        r2030_evtassocdesprec_lista = None
        r2030_evtassocdesprec_form = None
        r2040_evtassocdesprep_lista = None
        r2040_evtassocdesprep_form = None
        r2050_evtcomprod_lista = None
        r2050_evtcomprod_form = None
        r2060_evtcprb_lista = None
        r2060_evtcprb_form = None
        r2070_evtpgtosdivs_lista = None
        r2070_evtpgtosdivs_form = None
        r2098_evtreabreevper_lista = None
        r2098_evtreabreevper_form = None
        r2099_evtfechaevper_lista = None
        r2099_evtfechaevper_form = None
        r3010_evtespdesportivo_lista = None
        r3010_evtespdesportivo_form = None
        r4010_evtretpf_lista = None
        r4010_evtretpf_form = None
        r4020_evtretpj_lista = None
        r4020_evtretpj_form = None
        r4040_evtbenefnid_lista = None
        r4040_evtbenefnid_form = None
        r4098_evtreab_lista = None
        r4098_evtreab_form = None
        r4099_evtfech_lista = None
        r4099_evtfech_form = None
        r5001_evttotal_lista = None
        r5001_evttotal_form = None
        r5011_evttotalcontrib_lista = None
        r5011_evttotalcontrib_form = None
        r9000_evtexclusao_lista = None
        r9000_evtexclusao_form = None
        r9001_evttotal_lista = None
        r9001_evttotal_form = None
        r9002_evtret_lista = None
        r9002_evtret_form = None
        r9011_evttotalcontrib_lista = None
        r9011_evttotalcontrib_form = None
        r9012_evtretcons_lista = None
        r9012_evtretcons_form = None

        if pk:

            transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf, id=pk)

            transmissor_lote_efdreinf_ocorrencias_form = form_transmissor_lote_efdreinf_ocorrencias(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            transmissor_lote_efdreinf_ocorrencias_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            transmissor_lote_efdreinf_ocorrencias_lista = TransmissorLoteEfdreinfOcorrencias.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r1000_evtinfocontri_form = form_r1000_evtinfocontri(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r1000_evtinfocontri_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r1000_evtinfocontri_lista = r1000evtInfoContri.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r1070_evttabprocesso_form = form_r1070_evttabprocesso(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r1070_evttabprocesso_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r1070_evttabprocesso_lista = r1070evtTabProcesso.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r2010_evtservtom_form = form_r2010_evtservtom(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r2010_evtservtom_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r2010_evtservtom_lista = r2010evtServTom.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r2020_evtservprest_form = form_r2020_evtservprest(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r2020_evtservprest_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r2020_evtservprest_lista = r2020evtServPrest.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r2030_evtassocdesprec_form = form_r2030_evtassocdesprec(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r2030_evtassocdesprec_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r2030_evtassocdesprec_lista = r2030evtAssocDespRec.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r2040_evtassocdesprep_form = form_r2040_evtassocdesprep(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r2040_evtassocdesprep_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r2040_evtassocdesprep_lista = r2040evtAssocDespRep.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r2050_evtcomprod_form = form_r2050_evtcomprod(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r2050_evtcomprod_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r2050_evtcomprod_lista = r2050evtComProd.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r2060_evtcprb_form = form_r2060_evtcprb(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r2060_evtcprb_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r2060_evtcprb_lista = r2060evtCPRB.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r2070_evtpgtosdivs_form = form_r2070_evtpgtosdivs(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r2070_evtpgtosdivs_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r2070_evtpgtosdivs_lista = r2070evtPgtosDivs.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r2098_evtreabreevper_form = form_r2098_evtreabreevper(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r2098_evtreabreevper_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r2098_evtreabreevper_lista = r2098evtReabreEvPer.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r2099_evtfechaevper_form = form_r2099_evtfechaevper(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r2099_evtfechaevper_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r2099_evtfechaevper_lista = r2099evtFechaEvPer.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r3010_evtespdesportivo_form = form_r3010_evtespdesportivo(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r3010_evtespdesportivo_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r3010_evtespdesportivo_lista = r3010evtEspDesportivo.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r4010_evtretpf_form = form_r4010_evtretpf(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r4010_evtretpf_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r4010_evtretpf_lista = r4010evtRetPF.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r4020_evtretpj_form = form_r4020_evtretpj(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r4020_evtretpj_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r4020_evtretpj_lista = r4020evtRetPJ.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r4040_evtbenefnid_form = form_r4040_evtbenefnid(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r4040_evtbenefnid_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r4040_evtbenefnid_lista = r4040evtBenefNId.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r4098_evtreab_form = form_r4098_evtreab(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r4098_evtreab_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r4098_evtreab_lista = r4098evtReab.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r4099_evtfech_form = form_r4099_evtfech(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r4099_evtfech_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r4099_evtfech_lista = r4099evtFech.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r5001_evttotal_form = form_r5001_evttotal(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r5001_evttotal_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r5001_evttotal_lista = r5001evtTotal.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r5011_evttotalcontrib_form = form_r5011_evttotalcontrib(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r5011_evttotalcontrib_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r5011_evttotalcontrib_lista = r5011evtTotalContrib.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r9000_evtexclusao_form = form_r9000_evtexclusao(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r9000_evtexclusao_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r9000_evtexclusao_lista = r9000evtExclusao.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r9001_evttotal_form = form_r9001_evttotal(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r9001_evttotal_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r9001_evttotal_lista = r9001evtTotal.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r9002_evtret_form = form_r9002_evtret(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r9002_evtret_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r9002_evtret_lista = r9002evtRet.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r9011_evttotalcontrib_form = form_r9011_evttotalcontrib(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r9011_evttotalcontrib_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r9011_evttotalcontrib_lista = r9011evtTotalContrib.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()

            r9012_evtretcons_form = form_r9012_evtretcons(
                initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf })
            r9012_evtretcons_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            r9012_evtretcons_lista = r9012evtRetCons.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()


        else:

            transmissor_lote_efdreinf = None

        from django.db.models import Q

        if transmissor_lote_efdreinf:
            transmissor_eventos_efdreinf_lista = TransmissorEventosEfdreinf.objects.\
                filter(Q(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id) | Q(transmissor_lote_efdreinf_error_id=transmissor_lote_efdreinf.id)).all()
            transmissor_eventos_efdreinf_totalizacoes_lista = TransmissorEventosEfdreinfTotalizacoes.objects.\
                filter(transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()
        else:
            transmissor_eventos_efdreinf_lista = None
            transmissor_eventos_efdreinf_totalizacoes_lista = None
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'transmissor_lote_efdreinf': transmissor_lote_efdreinf,
            'transmissor_lote_efdreinf_form': transmissor_lote_efdreinf_form,
            'transmissor_lote_efdreinf_ocorrencias_form': transmissor_lote_efdreinf_ocorrencias_form,
            'transmissor_lote_efdreinf_ocorrencias_lista': transmissor_lote_efdreinf_ocorrencias_lista,
            'r1000_evtinfocontri_form': r1000_evtinfocontri_form,
            'r1000_evtinfocontri_lista': r1000_evtinfocontri_lista,
            'r1070_evttabprocesso_form': r1070_evttabprocesso_form,
            'r1070_evttabprocesso_lista': r1070_evttabprocesso_lista,
            'r2010_evtservtom_form': r2010_evtservtom_form,
            'r2010_evtservtom_lista': r2010_evtservtom_lista,
            'r2020_evtservprest_form': r2020_evtservprest_form,
            'r2020_evtservprest_lista': r2020_evtservprest_lista,
            'r2030_evtassocdesprec_form': r2030_evtassocdesprec_form,
            'r2030_evtassocdesprec_lista': r2030_evtassocdesprec_lista,
            'r2040_evtassocdesprep_form': r2040_evtassocdesprep_form,
            'r2040_evtassocdesprep_lista': r2040_evtassocdesprep_lista,
            'r2050_evtcomprod_form': r2050_evtcomprod_form,
            'r2050_evtcomprod_lista': r2050_evtcomprod_lista,
            'r2060_evtcprb_form': r2060_evtcprb_form,
            'r2060_evtcprb_lista': r2060_evtcprb_lista,
            'r2070_evtpgtosdivs_form': r2070_evtpgtosdivs_form,
            'r2070_evtpgtosdivs_lista': r2070_evtpgtosdivs_lista,
            'r2098_evtreabreevper_form': r2098_evtreabreevper_form,
            'r2098_evtreabreevper_lista': r2098_evtreabreevper_lista,
            'r2099_evtfechaevper_form': r2099_evtfechaevper_form,
            'r2099_evtfechaevper_lista': r2099_evtfechaevper_lista,
            'r3010_evtespdesportivo_form': r3010_evtespdesportivo_form,
            'r3010_evtespdesportivo_lista': r3010_evtespdesportivo_lista,
            'r4010_evtretpf_form': r4010_evtretpf_form,
            'r4010_evtretpf_lista': r4010_evtretpf_lista,
            'r4020_evtretpj_form': r4020_evtretpj_form,
            'r4020_evtretpj_lista': r4020_evtretpj_lista,
            'r4040_evtbenefnid_form': r4040_evtbenefnid_form,
            'r4040_evtbenefnid_lista': r4040_evtbenefnid_lista,
            'r4098_evtreab_form': r4098_evtreab_form,
            'r4098_evtreab_lista': r4098_evtreab_lista,
            'r4099_evtfech_form': r4099_evtfech_form,
            'r4099_evtfech_lista': r4099_evtfech_lista,
            'r5001_evttotal_form': r5001_evttotal_form,
            'r5001_evttotal_lista': r5001_evttotal_lista,
            'r5011_evttotalcontrib_form': r5011_evttotalcontrib_form,
            'r5011_evttotalcontrib_lista': r5011_evttotalcontrib_lista,
            'r9000_evtexclusao_form': r9000_evtexclusao_form,
            'r9000_evtexclusao_lista': r9000_evtexclusao_lista,
            'r9001_evttotal_form': r9001_evttotal_form,
            'r9001_evttotal_lista': r9001_evttotal_lista,
            'r9002_evtret_form': r9002_evtret_form,
            'r9002_evtret_lista': r9002_evtret_lista,
            'r9011_evttotalcontrib_form': r9011_evttotalcontrib_form,
            'r9011_evttotalcontrib_lista': r9011_evttotalcontrib_lista,
            'r9012_evtretcons_form': r9012_evtretcons_form,
            'r9012_evtretcons_lista': r9012_evtretcons_lista,
            'modulos': ['mensageiro', ],
            'paginas': ['transmissor_lote_efdreinf', ],
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'transmissor_eventos_efdreinf_lista': transmissor_eventos_efdreinf_lista,
'transmissor_eventos_efdreinf_totalizacoes_lista': transmissor_eventos_efdreinf_totalizacoes_lista,
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='transmissor_lote_efdreinf_salvar.html',
                filename="transmissor_lote_efdreinf.pdf",
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

            response = render_to_response('transmissor_lote_efdreinf_salvar.html', context)
            filename = "transmissor_lote_efdreinf.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 'transmissor_lote_efdreinf_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['mensageiro', ],
            'paginas': ['transmissor_lote_efdreinf', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
            'permissao_negada.html',
            context)