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
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def salvar(request, hash):
    
    try: 
    
        usuario_id = request.user.id  
        dict_hash = get_hash_url( hash )
        retornos_eventos_ocorrencias_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except: 
    
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    if retornos_eventos_ocorrencias_id:
    
        retornos_eventos_ocorrencias = get_object_or_404(RetornosEventosOcorrencias, id=retornos_eventos_ocorrencias_id)
        
    if request.user.has_perm('mensageiro.can_view_RetornosEventosOcorrencias'):
        
        if retornos_eventos_ocorrencias_id:
            retornos_eventos_ocorrencias_form = form_retornos_eventos_ocorrencias(request.POST or None, instance=retornos_eventos_ocorrencias)
            
        else:
            retornos_eventos_ocorrencias_form = form_retornos_eventos_ocorrencias(request.POST or None)
            
        if request.method == 'POST':
            if retornos_eventos_ocorrencias_form.is_valid():
                #retornos_eventos_ocorrencias_campos_multiple_passo1
                obj = retornos_eventos_ocorrencias_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')
                #retornos_eventos_ocorrencias_campos_multiple_passo2
                
                if request.session['retorno_pagina'] not in ('retornos_eventos_ocorrencias_apagar', 'retornos_eventos_ocorrencias_salvar', 'retornos_eventos_ocorrencias'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if retornos_eventos_ocorrencias_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('retornos_eventos_ocorrencias_salvar', hash=url_hash)
                    
            else:
                messages.error(request, 'Erro ao salvar!')
                
        retornos_eventos_ocorrencias_form = disabled_form_fields(retornos_eventos_ocorrencias_form, request.user.has_perm('mensageiro.change_RetornosEventosOcorrencias'))
        #retornos_eventos_ocorrencias_campos_multiple_passo3
        
        if int(dict_hash['print']):
        
            retornos_eventos_ocorrencias_form = disabled_form_for_print(retornos_eventos_ocorrencias_form)
        
        
        
        if retornos_eventos_ocorrencias_id:
        
            retornos_eventos_ocorrencias = get_object_or_404(RetornosEventosOcorrencias, id = retornos_eventos_ocorrencias_id)
            
                
        else:
        
            retornos_eventos_ocorrencias = None
            
        #retornos_eventos_ocorrencias_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if dict_hash['tab'] or 'retornos_eventos_ocorrencias' in request.session['retorno_pagina']:
        
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'retornos_eventos_ocorrencias_salvar'
            
        context = {
            'retornos_eventos_ocorrencias': retornos_eventos_ocorrencias, 
            'retornos_eventos_ocorrencias_form': retornos_eventos_ocorrencias_form, 
            'retornos_eventos_ocorrencias_id': int(retornos_eventos_ocorrencias_id),
            'usuario': usuario, 
            'hash': hash, 
            
            'modulos': ['mensageiro', ],
            'paginas': ['retornos_eventos_ocorrencias', ],
            'data': datetime.datetime.now(),
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #retornos_eventos_ocorrencias_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 'retornos_eventos_ocorrencias_salvar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='retornos_eventos_ocorrencias_salvar.html',
                filename="retornos_eventos_ocorrencias.pdf",
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
            response = render_to_response('retornos_eventos_ocorrencias_salvar.html', context)
            filename = "retornos_eventos_ocorrencias.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['mensageiro', ],
            'paginas': ['retornos_eventos_ocorrencias', ],
            'data': datetime.datetime.now(),
            'dict_permissoes': dict_permissoes,
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)