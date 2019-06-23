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
from emensageriapro.r2050.forms import *
from emensageriapro.r2050.models import *
from emensageriapro.controle_de_acesso.models import *



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    
    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO
    
    if pk:
    
        r2050_infoproc = get_object_or_404(r2050infoProc, id=pk)
        evento_dados = r2050_infoproc.evento()

    if request.user.has_perm('r2050.can_see_r2050infoProc'):
        
        if pk:
        
            r2050_infoproc_form = form_r2050_infoproc(
                request.POST or None, 
                instance=r2050_infoproc)
                                         
        else:
        
            r2050_infoproc_form = form_r2050_infoproc(request.POST or None)
                                         
        if request.method == 'POST':
        
            if r2050_infoproc_form.is_valid():
            
                obj = r2050_infoproc_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                #if not pk:
                #
                #    gravar_auditoria(
                #        '{}',
                #        json.dumps(
                #            model_to_dict(obj), 
                #            indent=4, 
                #            sort_keys=True, 
                #            default=str), 
                #        'r2050_infoproc', 
                #        obj.id, 
                #        request.user.id, 1)
                #                 
                #else:
                #
                #    gravar_auditoria(
                #        json.dumps(
                #            model_to_dict(r2050_infoproc), 
                #            indent=4, 
                #            sort_keys=True, 
                #            default=str),
                #        json.dumps(
                #            model_to_dict(obj), 
                #            indent=4, 
                #            sort_keys=True, 
                #            default=str), 
                #        'r2050_infoproc', 
                #        pk, 
                #        request.user.id, 2)
                                     
                if request.session['return_page'] not in (
                    'r2050_infoproc_apagar', 
                    'r2050_infoproc_salvar', 
                    'r2050_infoproc'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'])
                    
                if pk != obj.id:
                
                    return redirect(
                        'r2050_infoproc_salvar', 
                        pk=obj.id)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        r2050_infoproc_form = disabled_form_fields(
            r2050_infoproc_form, 
            request.user.has_perm('r2050.change_r2050infoProc'))
        
        if pk:
        
            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:
            
                r2050_infoproc_form = disabled_form_fields(r2050_infoproc_form, 0)
                
        if output:
        
            r2050_infoproc_form = disabled_form_for_print(r2050_infoproc_form)
            
        
        
        if pk:
        
            r2050_infoproc = get_object_or_404(r2050infoProc, id=pk)
            
                
        else:
        
            r2050_infoproc = None
            
        tabelas_secundarias = []
        
        if tab or 'r2050_infoproc' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 'r2050_infoproc_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r2050_infoproc').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes, 
            'r2050_infoproc': r2050_infoproc, 
            'r2050_infoproc_form': r2050_infoproc_form, 
            'modulos': ['r2050', ],
            'paginas': ['r2050_infoproc', ],
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #r2050_infoproc_salvar_custom_variaveis_context#
        }
        
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='r2050_infoproc_salvar.html',
                filename="r2050_infoproc.pdf",
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
            
            response = render_to_response('r2050_infoproc_salvar.html', context)
            filename = "r2050_infoproc.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 'r2050_infoproc_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['r2050', ],
            'paginas': ['r2050_infoproc', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)