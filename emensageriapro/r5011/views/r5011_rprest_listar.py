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
from emensageriapro.r5011.forms import *
from emensageriapro.r5011.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def listar(request, hash):

    for_print = 0
    
    try: 
    
        usuario_id = request.user.id   
        dict_hash = get_hash_url( hash )
        for_print = int(dict_hash['print'])
        
    except: 
    
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)

    if request.user.has_perm('r5011.can_view_r5011RPrest'):
    
        filtrar = False
        
        dict_fields = {}
        show_fields = { 
            'show_r5011_infototalcontrib': 1,
            'show_tpinsctomador': 1,
            'show_nrinsctomador': 1,
            'show_vlrtotalbaseret': 1,
            'show_vlrtotalretprinc': 1,
            'show_vlrtotalretadic': 0,
            'show_vlrtotalnretprinc': 0,
            'show_vlrtotalnretadic': 0, }
            
        post = False
        
        if request.method == 'POST':
        
            post = True
            dict_fields = { 
                'r5011_infototalcontrib__icontains': 'r5011_infototalcontrib__icontains',
                'tpinsctomador__icontains': 'tpinsctomador__icontains',
                'nrinsctomador__icontains': 'nrinsctomador__icontains',
                'vlrtotalbaseret__icontains': 'vlrtotalbaseret__icontains',
                'vlrtotalretprinc__icontains': 'vlrtotalretprinc__icontains',
                'vlrtotalretadic__icontains': 'vlrtotalretadic__icontains',
                'vlrtotalnretprinc__icontains': 'vlrtotalnretprinc__icontains',
                'vlrtotalnretadic__icontains': 'vlrtotalnretadic__icontains', }
                
            for a in dict_fields:
            
                dict_fields[a] = request.POST.get(a or None)
                
            for a in show_fields:
            
                show_fields[a] = request.POST.get(a or None)
                
            if request.method == 'POST':
            
                dict_fields = { 
                    'r5011_infototalcontrib__icontains': 'r5011_infototalcontrib__icontains',
                    'tpinsctomador__icontains': 'tpinsctomador__icontains',
                    'nrinsctomador__icontains': 'nrinsctomador__icontains',
                    'vlrtotalbaseret__icontains': 'vlrtotalbaseret__icontains',
                    'vlrtotalretprinc__icontains': 'vlrtotalretprinc__icontains',
                    'vlrtotalretadic__icontains': 'vlrtotalretadic__icontains',
                    'vlrtotalnretprinc__icontains': 'vlrtotalnretprinc__icontains',
                    'vlrtotalnretadic__icontains': 'vlrtotalnretadic__icontains', }
                    
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
                    
        dict_qs = clear_dict_fields(dict_fields)
        r5011_rprest_lista = r5011RPrest.objects.filter(**dict_qs).filter().exclude(id=0).all()
        
        if not post and len(r5011_rprest_lista) > 100:
        
            filtrar = True
            r5011_rprest_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
            
        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #r5011_rprest_listar_custom
        
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r5011_rprest'
        
        context = {
            'r5011_rprest_lista': r5011_rprest_lista, 
            'usuario': usuario,
            'modulos': ['r5011', ],
            'paginas': ['r5011_rprest', ],
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
            #[VARIAVEIS_FILTRO_RELATORIO]
        }
        
        if for_print in (0,1):
        
            return render(request, 'r5011_rprest_listar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r5011_rprest_listar.html',
                filename="r5011_rprest.pdf",
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
                             "no-stop-slow-scripts": True},
            )
            return response
            
        elif for_print == 3:
        
            from django.shortcuts import render_to_response
            response = render_to_response('r5011_rprest_listar.html', context)
            filename = "r5011_rprest.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
        elif for_print == 4:
        
            from django.shortcuts import render_to_response
            response = render_to_response('csv/r5011_rprest.csv', context)
            filename = "r5011_rprest.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario,
            'data': datetime.datetime.now(),
            'modulos': ['r5011', ],
            'paginas': ['r5011_rprest', ],
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)