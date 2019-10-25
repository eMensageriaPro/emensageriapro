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
from emensageriapro.r5011.models import r5011RTom
from emensageriapro.r5011.forms import form_r5011_rtom
from emensageriapro.r5011.models import r5011RPrest
from emensageriapro.r5011.forms import form_r5011_rprest
from emensageriapro.r5011.models import r5011RRecRepAD
from emensageriapro.r5011.forms import form_r5011_rrecrepad
from emensageriapro.r5011.models import r5011RComl
from emensageriapro.r5011.forms import form_r5011_rcoml
from emensageriapro.r5011.models import r5011RCPRB
from emensageriapro.r5011.forms import form_r5011_rcprb



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    
    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO
    
    if pk:
    
        r5011_infototalcontrib = get_object_or_404(r5011infoTotalContrib, id=pk)
        evento_dados = r5011_infototalcontrib.evento()

    if request.user.has_perm('r5011.can_see_r5011infoTotalContrib'):
        
        if pk:
        
            r5011_infototalcontrib_form = form_r5011_infototalcontrib(
                request.POST or None, 
                instance=r5011_infototalcontrib)
                                         
        else:
        
            r5011_infototalcontrib_form = form_r5011_infototalcontrib(request.POST or None)
                                         
        if request.method == 'POST':
        
            if r5011_infototalcontrib_form.is_valid():
            
                obj = r5011_infototalcontrib_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    gravar_auditoria(
                        '{}',
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        'r5011_infototalcontrib', 
                        obj.id, 
                        request.user.id, 1)
                                 
                else:
                
                    gravar_auditoria(
                        json.dumps(
                            model_to_dict(r5011_infototalcontrib), 
                            indent=4, 
                            sort_keys=True, 
                            default=str),
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        'r5011_infototalcontrib', 
                        pk, 
                        request.user.id, 2)
                                     
                if request.session['return_page'] not in (
                    'r5011_infototalcontrib_apagar', 
                    'r5011_infototalcontrib_salvar', 
                    'r5011_infototalcontrib'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'])
                    
                if pk != obj.id:
                
                    return redirect(
                        'r5011_infototalcontrib_salvar', 
                        pk=obj.id)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        r5011_infototalcontrib_form = disabled_form_fields(
            r5011_infototalcontrib_form, 
            request.user.has_perm('r5011.change_r5011infoTotalContrib'))
        
        if pk:
        
            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:
            
                r5011_infototalcontrib_form = disabled_form_fields(r5011_infototalcontrib_form, 0)
                
        if output:
        
            r5011_infototalcontrib_form = disabled_form_for_print(r5011_infototalcontrib_form)
            
        
        r5011_rtom_lista = None 
        r5011_rtom_form = None 
        r5011_rprest_lista = None 
        r5011_rprest_form = None 
        r5011_rrecrepad_lista = None 
        r5011_rrecrepad_form = None 
        r5011_rcoml_lista = None 
        r5011_rcoml_form = None 
        r5011_rcprb_lista = None 
        r5011_rcprb_form = None 
        
        if pk:
        
            r5011_infototalcontrib = get_object_or_404(r5011infoTotalContrib, id=pk)
            
            r5011_rtom_form = form_r5011_rtom(
                initial={ 'r5011_infototalcontrib': r5011_infototalcontrib })
            r5011_rtom_form.fields['r5011_infototalcontrib'].widget.attrs['readonly'] = True
            r5011_rtom_lista = r5011RTom.objects.\
                filter(r5011_infototalcontrib_id=r5011_infototalcontrib.id).all()
                
            r5011_rprest_form = form_r5011_rprest(
                initial={ 'r5011_infototalcontrib': r5011_infototalcontrib })
            r5011_rprest_form.fields['r5011_infototalcontrib'].widget.attrs['readonly'] = True
            r5011_rprest_lista = r5011RPrest.objects.\
                filter(r5011_infototalcontrib_id=r5011_infototalcontrib.id).all()
                
            r5011_rrecrepad_form = form_r5011_rrecrepad(
                initial={ 'r5011_infototalcontrib': r5011_infototalcontrib })
            r5011_rrecrepad_form.fields['r5011_infototalcontrib'].widget.attrs['readonly'] = True
            r5011_rrecrepad_lista = r5011RRecRepAD.objects.\
                filter(r5011_infototalcontrib_id=r5011_infototalcontrib.id).all()
                
            r5011_rcoml_form = form_r5011_rcoml(
                initial={ 'r5011_infototalcontrib': r5011_infototalcontrib })
            r5011_rcoml_form.fields['r5011_infototalcontrib'].widget.attrs['readonly'] = True
            r5011_rcoml_lista = r5011RComl.objects.\
                filter(r5011_infototalcontrib_id=r5011_infototalcontrib.id).all()
                
            r5011_rcprb_form = form_r5011_rcprb(
                initial={ 'r5011_infototalcontrib': r5011_infototalcontrib })
            r5011_rcprb_form.fields['r5011_infototalcontrib'].widget.attrs['readonly'] = True
            r5011_rcprb_lista = r5011RCPRB.objects.\
                filter(r5011_infototalcontrib_id=r5011_infototalcontrib.id).all()
                
                
        else:
        
            r5011_infototalcontrib = None
            
        tabelas_secundarias = []
        
        if tab or 'r5011_infototalcontrib' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 'r5011_infototalcontrib_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r5011_infototalcontrib').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes, 
            'r5011_infototalcontrib': r5011_infototalcontrib, 
            'r5011_infototalcontrib_form': r5011_infototalcontrib_form, 
            'modulos': ['r5011', ],
            'paginas': ['r5011_infototalcontrib', ],
            'r5011_rtom_form': r5011_rtom_form,
            'r5011_rtom_lista': r5011_rtom_lista,
            'r5011_rprest_form': r5011_rprest_form,
            'r5011_rprest_lista': r5011_rprest_lista,
            'r5011_rrecrepad_form': r5011_rrecrepad_form,
            'r5011_rrecrepad_lista': r5011_rrecrepad_lista,
            'r5011_rcoml_form': r5011_rcoml_form,
            'r5011_rcoml_lista': r5011_rcoml_lista,
            'r5011_rcprb_form': r5011_rcprb_form,
            'r5011_rcprb_lista': r5011_rcprb_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #r5011_infototalcontrib_salvar_custom_variaveis_context#
        }
        
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='r5011_infototalcontrib_salvar.html',
                filename="r5011_infototalcontrib.pdf",
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
            
            response = render_to_response('r5011_infototalcontrib_salvar.html', context)
            filename = "r5011_infototalcontrib.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 'r5011_infototalcontrib_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['r5011', ],
            'paginas': ['r5011_infototalcontrib', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)