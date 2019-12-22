# eMensageriaAI #
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
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf
from emensageriapro.efdreinf.models import r5001evtTotal
from emensageriapro.efdreinf.models import r5011evtTotalContrib
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf


@login_required
def listar(request, output=None):

    if request.user.has_perm('efdreinf.can_see_r1000evtInfoContri'):

        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_reinf': 0,
            'show_evtinfocontri': 0,
            'show_identidade': 1,
            'show_ideevento': 0,
            'show_tpamb': 0,
            'show_procemi': 0,
            'show_verproc': 0,
            'show_idecontri': 0,
            'show_tpinsc': 1,
            'show_nrinsc': 1,
            'show_infocontri': 0,
            'show_versao': 0,
            'show_transmissor_lote_efdreinf': 0,
            'show_retornos_r5001': 0,
            'show_retornos_r5011': 0,
            'show_ocorrencias': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_arquivo_original': 0,
            'show_arquivo': 0,
            'show_status': 1,
            'show_cdretorno': 1,
            'show_descretorno': 0,
            'show_dhprocess': 0,
            'show_operacao': 1,
            'show_transmissor_lote_efdreinf_error': 0, }

        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                'reinf': 'reinf',
                'evtinfocontri': 'evtinfocontri',
                'identidade__icontains': 'identidade__icontains',
                'ideevento': 'ideevento',
                'tpamb__icontains': 'tpamb__icontains',
                'procemi__icontains': 'procemi__icontains',
                'verproc__icontains': 'verproc__icontains',
                'idecontri': 'idecontri',
                'tpinsc__icontains': 'tpinsc__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'infocontri': 'infocontri',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_efdreinf__icontains': 'transmissor_lote_efdreinf__icontains',
                'status__icontains': 'status__icontains',
                'cdretorno__icontains': 'cdretorno__icontains',
                'operacao__icontains': 'operacao__icontains', }

            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)

            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)

            if request.method == 'POST':
                dict_fields = {
                    'reinf': 'reinf',
                    'evtinfocontri': 'evtinfocontri',
                    'identidade__icontains': 'identidade__icontains',
                    'ideevento': 'ideevento',
                    'tpamb__icontains': 'tpamb__icontains',
                    'procemi__icontains': 'procemi__icontains',
                    'verproc__icontains': 'verproc__icontains',
                    'idecontri': 'idecontri',
                    'tpinsc__icontains': 'tpinsc__icontains',
                    'nrinsc__icontains': 'nrinsc__icontains',
                    'infocontri': 'infocontri',
                    'versao__icontains': 'versao__icontains',
                    'transmissor_lote_efdreinf__icontains': 'transmissor_lote_efdreinf__icontains',
                    'status__icontains': 'status__icontains',
                    'cdretorno__icontains': 'cdretorno__icontains',
                    'operacao__icontains': 'operacao__icontains', }
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        r1000_evtinfocontri_lista = r1000evtInfoContri.objects.filter(**dict_qs).filter().exclude(id=0).all()

        if not post and len(r1000_evtinfocontri_lista) > 100:
            filtrar = True
            r1000_evtinfocontri_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.all()
        retornos_r5001_lista = r5001evtTotal.objects.all()
        retornos_r5011_lista = r5011evtTotalContrib.objects.all()
        transmissor_lote_efdreinf_error_lista = TransmissorLoteEfdreinf.objects.all()
        #r1000_evtinfocontri_listar_custom

        request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'r1000_evtinfocontri_lista': r1000_evtinfocontri_lista,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r1000_evtinfocontri', ],
            'show_fields': show_fields,
            'filtrar': filtrar,
            'transmissor_lote_efdreinf_lista': transmissor_lote_efdreinf_lista,
            'retornos_r5001_lista': retornos_r5001_lista,
            'retornos_r5011_lista': retornos_r5011_lista,
            'transmissor_lote_efdreinf_error_lista': transmissor_lote_efdreinf_error_lista,
        }

        if output == 'pdf':

            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='r1000_evtinfocontri_listar.html',
                filename="r1000_evtinfocontri.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             'viewport-size': "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response

        elif output == 'xls':

            response = render_to_response('r1000_evtinfocontri_listar.html', context)
            filename = "r1000_evtinfocontri.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        elif output == 'csv':

            response = render_to_response('csv/r1000_evtinfocontri.csv', context)
            filename = "r1000_evtinfocontri.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'

            return response

        else:

            return render(request, 'r1000_evtinfocontri_listar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r1000_evtinfocontri', ],
        }
        return render(request, 'permissao_negada.html', context)