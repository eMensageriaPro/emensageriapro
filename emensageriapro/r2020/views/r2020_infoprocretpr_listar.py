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
from emensageriapro.r2020.forms import *
from emensageriapro.r2020.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def listar(request, output=None):

    if request.user.has_perm('r2020.can_see_r2020infoProcRetPr'):

        filtrar = False

        dict_fields = {}
        show_fields = {
            'show_r2020_evtservprest': 1,
            'show_tpprocretprinc': 1,
            'show_nrprocretprinc': 1,
            'show_codsuspprinc': 0,
            'show_valorprinc': 0, }

        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                'r2020_evtservprest__icontains': 'r2020_evtservprest__icontains',
                'tpprocretprinc__icontains': 'tpprocretprinc__icontains',
                'nrprocretprinc__icontains': 'nrprocretprinc__icontains',
                'codsuspprinc__icontains': 'codsuspprinc__icontains',
                'valorprinc__icontains': 'valorprinc__icontains', }

            for a in dict_fields:

                dict_fields[a] = request.POST.get(a or None)

            for a in show_fields:

                show_fields[a] = request.POST.get(a or None)

            if request.method == 'POST':

                dict_fields = {
                    'r2020_evtservprest__icontains': 'r2020_evtservprest__icontains',
                    'tpprocretprinc__icontains': 'tpprocretprinc__icontains',
                    'nrprocretprinc__icontains': 'nrprocretprinc__icontains',
                    'codsuspprinc__icontains': 'codsuspprinc__icontains',
                    'valorprinc__icontains': 'valorprinc__icontains', }

                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        r2020_infoprocretpr_lista = r2020infoProcRetPr.objects.filter(**dict_qs).filter().exclude(id=0).all()

        if not post and len(r2020_infoprocretpr_lista) > 100:

            filtrar = True
            r2020_infoprocretpr_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #r2020_infoprocretpr_listar_custom

        request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'r2020_infoprocretpr_lista': r2020_infoprocretpr_lista,
            'modulos': ['r2020', ],
            'paginas': ['r2020_infoprocretpr', ],
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'filtrar': filtrar,
            #[VARIAVEIS_FILTRO_RELATORIO]
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='r2020_infoprocretpr_listar.html',
                filename="r2020_infoprocretpr.pdf",
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
                             "no-stop-slow-scripts": True}, )
         
            return response

        elif output == 'xls':

            from django.shortcuts import render_to_response
            response = render_to_response('r2020_infoprocretpr_listar.html', context)
            filename = "r2020_infoprocretpr.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif output == 'csv':

            from django.shortcuts import render_to_response
            response = render_to_response('csv/r2020_infoprocretpr.csv', context)
            filename = "r2020_infoprocretpr.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:

            return render(request, 'r2020_infoprocretpr_listar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'data': datetime.datetime.now(),
            'modulos': ['r2020', ],
            'paginas': ['r2020_infoprocretpr', ],
        }

        return render(request,
                      'permissao_negada.html',
                      context)