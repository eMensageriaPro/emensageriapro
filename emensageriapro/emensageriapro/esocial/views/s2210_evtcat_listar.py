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
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.mensageiro.models import TransmissorLoteEsocial
from emensageriapro.mensageiro.models import RetornosEventos
from emensageriapro.mensageiro.models import TransmissorLoteEsocial


@login_required
def listar(request, output=None):

    if request.user.has_perm('esocial.can_see_s2210evtCAT'):

        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_esocial': 0,
            'show_evtcat': 0,
            'show_identidade': 1,
            'show_ideevento': 0,
            'show_indretif': 1,
            'show_nrrecibo': 0,
            'show_tpamb': 0,
            'show_procemi': 0,
            'show_verproc': 0,
            'show_ideempregador': 0,
            'show_tpinsc': 1,
            'show_nrinsc': 0,
            'show_idevinculo': 0,
            'show_cpftrab': 0,
            'show_nistrab': 0,
            'show_matricula': 0,
            'show_codcateg': 0,
            'show_cat': 0,
            'show_dtacid': 0,
            'show_tpacid': 0,
            'show_hracid': 0,
            'show_hrstrabantesacid': 0,
            'show_tpcat': 0,
            'show_indcatobito': 0,
            'show_dtobito': 0,
            'show_indcomunpolicia': 0,
            'show_codsitgeradora': 0,
            'show_iniciatcat': 0,
            'show_obscat': 0,
            'show_observacao': 0,
            'show_localacidente': 0,
            'show_tplocal': 0,
            'show_dsclocal': 0,
            'show_codamb': 0,
            'show_tplograd': 0,
            'show_dsclograd': 0,
            'show_nrlograd': 0,
            'show_complemento': 0,
            'show_bairro': 0,
            'show_cep': 0,
            'show_codmunic': 0,
            'show_uf': 0,
            'show_pais': 0,
            'show_codpostal': 0,
            'show_versao': 0,
            'show_transmissor_lote_esocial': 0,
            'show_retornos_eventos': 0,
            'show_ocorrencias': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_arquivo_original': 0,
            'show_arquivo': 0,
            'show_status': 1,
            'show_transmissor_lote_esocial_error': 0, }

        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                'esocial': 'esocial',
                'evtcat': 'evtcat',
                'identidade__icontains': 'identidade__icontains',
                'ideevento': 'ideevento',
                'indretif__icontains': 'indretif__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'tpamb__icontains': 'tpamb__icontains',
                'procemi__icontains': 'procemi__icontains',
                'verproc__icontains': 'verproc__icontains',
                'ideempregador': 'ideempregador',
                'tpinsc__icontains': 'tpinsc__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'idevinculo': 'idevinculo',
                'cpftrab__icontains': 'cpftrab__icontains',
                'nistrab__icontains': 'nistrab__icontains',
                'matricula__icontains': 'matricula__icontains',
                'codcateg__icontains': 'codcateg__icontains',
                'cat': 'cat',
                'dtacid__range': 'dtacid__range',
                'tpacid__icontains': 'tpacid__icontains',
                'hracid__icontains': 'hracid__icontains',
                'hrstrabantesacid__icontains': 'hrstrabantesacid__icontains',
                'tpcat__icontains': 'tpcat__icontains',
                'indcatobito__icontains': 'indcatobito__icontains',
                'dtobito__range': 'dtobito__range',
                'indcomunpolicia__icontains': 'indcomunpolicia__icontains',
                'codsitgeradora__icontains': 'codsitgeradora__icontains',
                'iniciatcat__icontains': 'iniciatcat__icontains',
                'obscat__icontains': 'obscat__icontains',
                'observacao__icontains': 'observacao__icontains',
                'localacidente': 'localacidente',
                'tplocal__icontains': 'tplocal__icontains',
                'dsclocal__icontains': 'dsclocal__icontains',
                'codamb__icontains': 'codamb__icontains',
                'tplograd__icontains': 'tplograd__icontains',
                'dsclograd__icontains': 'dsclograd__icontains',
                'nrlograd__icontains': 'nrlograd__icontains',
                'complemento__icontains': 'complemento__icontains',
                'bairro__icontains': 'bairro__icontains',
                'cep__icontains': 'cep__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'uf__icontains': 'uf__icontains',
                'pais__icontains': 'pais__icontains',
                'codpostal__icontains': 'codpostal__icontains',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_esocial__icontains': 'transmissor_lote_esocial__icontains',
                'status__icontains': 'status__icontains', }

            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)

            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)

            if request.method == 'POST':
                dict_fields = {
                    'esocial': 'esocial',
                    'evtcat': 'evtcat',
                    'identidade__icontains': 'identidade__icontains',
                    'ideevento': 'ideevento',
                    'indretif__icontains': 'indretif__icontains',
                    'nrrecibo__icontains': 'nrrecibo__icontains',
                    'tpamb__icontains': 'tpamb__icontains',
                    'procemi__icontains': 'procemi__icontains',
                    'verproc__icontains': 'verproc__icontains',
                    'ideempregador': 'ideempregador',
                    'tpinsc__icontains': 'tpinsc__icontains',
                    'nrinsc__icontains': 'nrinsc__icontains',
                    'idevinculo': 'idevinculo',
                    'cpftrab__icontains': 'cpftrab__icontains',
                    'nistrab__icontains': 'nistrab__icontains',
                    'matricula__icontains': 'matricula__icontains',
                    'codcateg__icontains': 'codcateg__icontains',
                    'cat': 'cat',
                    'dtacid__range': 'dtacid__range',
                    'tpacid__icontains': 'tpacid__icontains',
                    'hracid__icontains': 'hracid__icontains',
                    'hrstrabantesacid__icontains': 'hrstrabantesacid__icontains',
                    'tpcat__icontains': 'tpcat__icontains',
                    'indcatobito__icontains': 'indcatobito__icontains',
                    'dtobito__range': 'dtobito__range',
                    'indcomunpolicia__icontains': 'indcomunpolicia__icontains',
                    'codsitgeradora__icontains': 'codsitgeradora__icontains',
                    'iniciatcat__icontains': 'iniciatcat__icontains',
                    'obscat__icontains': 'obscat__icontains',
                    'observacao__icontains': 'observacao__icontains',
                    'localacidente': 'localacidente',
                    'tplocal__icontains': 'tplocal__icontains',
                    'dsclocal__icontains': 'dsclocal__icontains',
                    'codamb__icontains': 'codamb__icontains',
                    'tplograd__icontains': 'tplograd__icontains',
                    'dsclograd__icontains': 'dsclograd__icontains',
                    'nrlograd__icontains': 'nrlograd__icontains',
                    'complemento__icontains': 'complemento__icontains',
                    'bairro__icontains': 'bairro__icontains',
                    'cep__icontains': 'cep__icontains',
                    'codmunic__icontains': 'codmunic__icontains',
                    'uf__icontains': 'uf__icontains',
                    'pais__icontains': 'pais__icontains',
                    'codpostal__icontains': 'codpostal__icontains',
                    'versao__icontains': 'versao__icontains',
                    'transmissor_lote_esocial__icontains': 'transmissor_lote_esocial__icontains',
                    'status__icontains': 'status__icontains', }
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        s2210_evtcat_lista = s2210evtCAT.objects.filter(**dict_qs).filter().exclude(id=0).all()

        if not post and len(s2210_evtcat_lista) > 100:
            filtrar = True
            s2210_evtcat_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.all()
        retornos_eventos_lista = RetornosEventos.objects.all()
        transmissor_lote_esocial_error_lista = TransmissorLoteEsocial.objects.all()
        #s2210_evtcat_listar_custom

        request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            's2210_evtcat_lista': s2210_evtcat_lista,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2210_evtcat', ],
            'show_fields': show_fields,
            'filtrar': filtrar,
            'transmissor_lote_esocial_lista': transmissor_lote_esocial_lista,
            'retornos_eventos_lista': retornos_eventos_lista,
            'transmissor_lote_esocial_error_lista': transmissor_lote_esocial_error_lista,
        }

        if output == 'pdf':

            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s2210_evtcat_listar.html',
                filename="s2210_evtcat.pdf",
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

            response = render_to_response('s2210_evtcat_listar.html', context)
            filename = "s2210_evtcat.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        elif output == 'csv':

            response = render_to_response('csv/s2210_evtcat.csv', context)
            filename = "s2210_evtcat.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'

            return response

        else:

            return render(request, 's2210_evtcat_listar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2210_evtcat', ],
        }
        return render(request, 'permissao_negada.html', context)