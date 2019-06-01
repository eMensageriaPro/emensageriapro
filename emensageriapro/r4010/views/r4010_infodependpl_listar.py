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
from emensageriapro.r4010.forms import *
from emensageriapro.r4010.models import *
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

    if request.user.has_perm('r4010.can_view_r4010infoDependPl'):
    
        filtrar = False
        
        dict_fields = {}
        show_fields = { 
            'show_r4010_ideopsaude': 1,
            'show_cpf': 0,
            'show_dtnascto': 0,
            'show_nome': 1,
            'show_reldep': 1,
            'show_vlrsaude': 1, }
            
        post = False
        
        if request.method == 'POST':
        
            post = True
            dict_fields = { 
                'r4010_ideopsaude__icontains': 'r4010_ideopsaude__icontains',
                'cpf__icontains': 'cpf__icontains',
                'dtnascto__range': 'dtnascto__range',
                'nome__icontains': 'nome__icontains',
                'reldep__icontains': 'reldep__icontains',
                'vlrsaude__icontains': 'vlrsaude__icontains', }
                
            for a in dict_fields:
            
                dict_fields[a] = request.POST.get(a or None)
                
            for a in show_fields:
            
                show_fields[a] = request.POST.get(a or None)
                
            if request.method == 'POST':
            
                dict_fields = { 
                    'r4010_ideopsaude__icontains': 'r4010_ideopsaude__icontains',
                    'cpf__icontains': 'cpf__icontains',
                    'dtnascto__range': 'dtnascto__range',
                    'nome__icontains': 'nome__icontains',
                    'reldep__icontains': 'reldep__icontains',
                    'vlrsaude__icontains': 'vlrsaude__icontains', }
                    
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
                    
        dict_qs = clear_dict_fields(dict_fields)
        r4010_infodependpl_lista = r4010infoDependPl.objects.filter(**dict_qs).filter().exclude(id=0).all()
        
        if not post and len(r4010_infodependpl_lista) > 100:
        
            filtrar = True
            r4010_infodependpl_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
            
        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #r4010_infodependpl_listar_custom
        
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r4010_infodependpl'
        
        context = {
            'r4010_infodependpl_lista': r4010_infodependpl_lista, 
            'usuario': usuario,
            'modulos': ['r4010', ],
            'paginas': ['r4010_infodependpl', ],
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
            #[VARIAVEIS_FILTRO_RELATORIO]
        }
        
        if for_print in (0,1):
        
            return render(request, 'r4010_infodependpl_listar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r4010_infodependpl_listar.html',
                filename="r4010_infodependpl.pdf",
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
            response = render_to_response('r4010_infodependpl_listar.html', context)
            filename = "r4010_infodependpl.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
        elif for_print == 4:
        
            from django.shortcuts import render_to_response
            response = render_to_response('csv/r4010_infodependpl.csv', context)
            filename = "r4010_infodependpl.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario,
            'data': datetime.datetime.now(),
            'modulos': ['r4010', ],
            'paginas': ['r4010_infodependpl', ],
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)