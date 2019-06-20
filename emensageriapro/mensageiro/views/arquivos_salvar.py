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


@login_required
def salvar(request, pk=None, tab='master', output=None):
    
    if pk:
    
        arquivos = get_object_or_404(Arquivos, id=pk)
        
    if request.user.has_perm('mensageiro.can_see_Arquivos'):
        
        if pk:
        
            arquivos_form = form_arquivos(request.POST or None, instance=arquivos)
            
        else:
        
            arquivos_form = form_arquivos(request.POST or None)
            
        if request.method == 'POST':
        
            if arquivos_form.is_valid():
            
                #arquivos_campos_multiple_passo1
                
                
                obj = arquivos_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')
                #arquivos_campos_multiple_passo2
                
                if request.session['return_page'] not in (
                    'arquivos_apagar', 
                    'arquivos_salvar', 
                    'arquivos'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'])
                    
                if pk != obj.id:
                
                    return redirect(
                        'arquivos_salvar', 
                        pk=obj.id)
                    
            else:
            
                messages.error(request, 'Erro ao salvar!')
                
        arquivos_form = disabled_form_fields(arquivos_form, request.user.has_perm('mensageiro.change_Arquivos'))
        #arquivos_campos_multiple_passo3
        
        if output:
        
            arquivos_form = disabled_form_for_print(arquivos_form)
        
        
        
        if pk:
        
            arquivos = get_object_or_404(Arquivos, id=pk)
            
                
        else:
        
            arquivos = None
            
        #arquivos_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if tab or 'arquivos' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 'arquivos_salvar'
            
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'arquivos': arquivos, 
            'arquivos_form': arquivos_form, 
            'modulos': ['mensageiro', ],
            'paginas': ['arquivos', ],
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            #arquivos_salvar_custom_variaveis_context#
        }
            
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='arquivos_salvar.html',
                filename="arquivos.pdf",
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
            
            response = render_to_response('arquivos_salvar.html', context)
            filename = "arquivos.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
        
        else:
        
            return render(request, 'arquivos_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['mensageiro', ],
            'paginas': ['arquivos', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
            'permissao_negada.html', 
            context)