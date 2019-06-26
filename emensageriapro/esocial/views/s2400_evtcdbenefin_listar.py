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


@login_required
def listar(request, output=None):

    if request.user.has_perm('esocial.can_see_s2400evtCdBenefIn'):

        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_esocial': 0,
            'show_evtcdbenefin': 0,
            'show_identidade': 1,
            'show_ideevento': 0,
            'show_indretif': 1,
            'show_nrrecibo': 0,
            'show_tpamb': 1,
            'show_procemi': 1,
            'show_verproc': 1,
            'show_ideempregador': 0,
            'show_tpinsc': 1,
            'show_nrinsc': 1,
            'show_beneficiario': 0,
            'show_cpfbenef': 1,
            'show_nisbenef': 0,
            'show_nmbenefic': 1,
            'show_dtinicio': 1,
            'show_sexo': 1,
            'show_racacor': 1,
            'show_estciv': 0,
            'show_incfismen': 1,
            'show_dtincfismen': 0,
            'show_dadosnasc': 0,
            'show_dtnascto': 1,
            'show_codmunic': 0,
            'show_uf': 0,
            'show_paisnascto': 0,
            'show_paisnac': 1,
            'show_nmmae': 0,
            'show_nmpai': 0,
            'show_versao': 0,
            'show_transmissor_lote_esocial': 0,
            'show_retornos_eventos': 0,
            'show_ocorrencias': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_arquivo_original': 0,
            'show_arquivo': 0,
            'show_status': 1, }

        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                'esocial': 'esocial',
                'evtcdbenefin': 'evtcdbenefin',
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
                'beneficiario': 'beneficiario',
                'cpfbenef__icontains': 'cpfbenef__icontains',
                'nisbenef__icontains': 'nisbenef__icontains',
                'nmbenefic__icontains': 'nmbenefic__icontains',
                'dtinicio__range': 'dtinicio__range',
                'sexo__icontains': 'sexo__icontains',
                'racacor__icontains': 'racacor__icontains',
                'estciv__icontains': 'estciv__icontains',
                'incfismen__icontains': 'incfismen__icontains',
                'dtincfismen__range': 'dtincfismen__range',
                'dadosnasc': 'dadosnasc',
                'dtnascto__range': 'dtnascto__range',
                'codmunic__icontains': 'codmunic__icontains',
                'uf__icontains': 'uf__icontains',
                'paisnascto__icontains': 'paisnascto__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'nmpai__icontains': 'nmpai__icontains',
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
                    'evtcdbenefin': 'evtcdbenefin',
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
                    'beneficiario': 'beneficiario',
                    'cpfbenef__icontains': 'cpfbenef__icontains',
                    'nisbenef__icontains': 'nisbenef__icontains',
                    'nmbenefic__icontains': 'nmbenefic__icontains',
                    'dtinicio__range': 'dtinicio__range',
                    'sexo__icontains': 'sexo__icontains',
                    'racacor__icontains': 'racacor__icontains',
                    'estciv__icontains': 'estciv__icontains',
                    'incfismen__icontains': 'incfismen__icontains',
                    'dtincfismen__range': 'dtincfismen__range',
                    'dadosnasc': 'dadosnasc',
                    'dtnascto__range': 'dtnascto__range',
                    'codmunic__icontains': 'codmunic__icontains',
                    'uf__icontains': 'uf__icontains',
                    'paisnascto__icontains': 'paisnascto__icontains',
                    'paisnac__icontains': 'paisnac__icontains',
                    'nmmae__icontains': 'nmmae__icontains',
                    'nmpai__icontains': 'nmpai__icontains',
                    'versao__icontains': 'versao__icontains',
                    'transmissor_lote_esocial__icontains': 'transmissor_lote_esocial__icontains',
                    'status__icontains': 'status__icontains', }
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        s2400_evtcdbenefin_lista = s2400evtCdBenefIn.objects.filter(**dict_qs).filter().exclude(id=0).all()

        if not post and len(s2400_evtcdbenefin_lista) > 100:
            filtrar = True
            s2400_evtcdbenefin_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #s2400_evtcdbenefin_listar_custom

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            's2400_evtcdbenefin_lista': s2400_evtcdbenefin_lista,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2400_evtcdbenefin', ],
            'show_fields': show_fields,
            'filtrar': filtrar,
            #[VARIAVEIS_FILTRO_RELATORIO]
        }

        if output == 'pdf':

            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s2400_evtcdbenefin_listar.html',
                filename="s2400_evtcdbenefin.pdf",
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

            response = render_to_response('s2400_evtcdbenefin_listar.html', context)
            filename = "s2400_evtcdbenefin.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        elif output == 'csv':

            response = render_to_response('csv/s2400_evtcdbenefin.csv', context)
            filename = "s2400_evtcdbenefin.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'

            return response

        else:

            return render(request, 's2400_evtcdbenefin_listar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2400_evtcdbenefin', ],
        }
        return render(request, 'permissao_negada.html', context)