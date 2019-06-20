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
from emensageriapro.r9002.forms import *
from emensageriapro.r9002.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r9002.models import r9002totApurMen
from emensageriapro.r9002.forms import form_r9002_totapurmen
from emensageriapro.r9002.models import r9002totApurQui
from emensageriapro.r9002.forms import form_r9002_totapurqui
from emensageriapro.r9002.models import r9002totApurDec
from emensageriapro.r9002.forms import form_r9002_totapurdec
from emensageriapro.r9002.models import r9002totApurSem
from emensageriapro.r9002.forms import form_r9002_totapursem
from emensageriapro.r9002.models import r9002totApurDia
from emensageriapro.r9002.forms import form_r9002_totapurdia



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    
    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO
    
    if pk:
    
        r9002_infototal = get_object_or_404(r9002infoTotal, id=pk)
        evento_dados = r9002_infototal.evento()

    if request.user.has_perm('r9002.can_see_r9002infoTotal'):
        
        if pk:
        
            r9002_infototal_form = form_r9002_infototal(
                request.POST or None, 
                instance=r9002_infototal)
                                         
        else:
        
            r9002_infototal_form = form_r9002_infototal(request.POST or None)
                                         
        if request.method == 'POST':
        
            if r9002_infototal_form.is_valid():
            
                obj = r9002_infototal_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    gravar_auditoria(
                        '{}',
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        'r9002_infototal', 
                        obj.id, 
                        request.user.id, 1)
                                 
                else:
                
                    gravar_auditoria(
                        json.dumps(
                            model_to_dict(r9002_infototal), 
                            indent=4, 
                            sort_keys=True, 
                            default=str),
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        'r9002_infototal', 
                        pk, 
                        request.user.id, 2)
                                     
                if request.session['return_page'] not in (
                    'r9002_infototal_apagar', 
                    'r9002_infototal_salvar', 
                    'r9002_infototal'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'])
                    
                if pk != obj.id:
                
                    return redirect(
                        'r9002_infototal_salvar', 
                        pk=obj.id)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        r9002_infototal_form = disabled_form_fields(
            r9002_infototal_form, 
            request.user.has_perm('r9002.change_r9002infoTotal'))
        
        if pk:
        
            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:
            
                r9002_infototal_form = disabled_form_fields(r9002_infototal_form, 0)
                
        if output:
        
            r9002_infototal_form = disabled_form_for_print(r9002_infototal_form)
            
        
        r9002_totapurmen_lista = None 
        r9002_totapurmen_form = None 
        r9002_totapurqui_lista = None 
        r9002_totapurqui_form = None 
        r9002_totapurdec_lista = None 
        r9002_totapurdec_form = None 
        r9002_totapursem_lista = None 
        r9002_totapursem_form = None 
        r9002_totapurdia_lista = None 
        r9002_totapurdia_form = None 
        
        if pk:
        
            r9002_infototal = get_object_or_404(r9002infoTotal, id=pk)
            
            r9002_totapurmen_form = form_r9002_totapurmen(
                initial={ 'r9002_infototal': r9002_infototal })
            r9002_totapurmen_form.fields['r9002_infototal'].widget.attrs['readonly'] = True
            r9002_totapurmen_lista = r9002totApurMen.objects.\
                filter(r9002_infototal_id=r9002_infototal.id).all()
                
            r9002_totapurqui_form = form_r9002_totapurqui(
                initial={ 'r9002_infototal': r9002_infototal })
            r9002_totapurqui_form.fields['r9002_infototal'].widget.attrs['readonly'] = True
            r9002_totapurqui_lista = r9002totApurQui.objects.\
                filter(r9002_infototal_id=r9002_infototal.id).all()
                
            r9002_totapurdec_form = form_r9002_totapurdec(
                initial={ 'r9002_infototal': r9002_infototal })
            r9002_totapurdec_form.fields['r9002_infototal'].widget.attrs['readonly'] = True
            r9002_totapurdec_lista = r9002totApurDec.objects.\
                filter(r9002_infototal_id=r9002_infototal.id).all()
                
            r9002_totapursem_form = form_r9002_totapursem(
                initial={ 'r9002_infototal': r9002_infototal })
            r9002_totapursem_form.fields['r9002_infototal'].widget.attrs['readonly'] = True
            r9002_totapursem_lista = r9002totApurSem.objects.\
                filter(r9002_infototal_id=r9002_infototal.id).all()
                
            r9002_totapurdia_form = form_r9002_totapurdia(
                initial={ 'r9002_infototal': r9002_infototal })
            r9002_totapurdia_form.fields['r9002_infototal'].widget.attrs['readonly'] = True
            r9002_totapurdia_lista = r9002totApurDia.objects.\
                filter(r9002_infototal_id=r9002_infototal.id).all()
                
                
        else:
        
            r9002_infototal = None
            
        tabelas_secundarias = []
        
        if tab or 'r9002_infototal' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 'r9002_infototal_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r9002_infototal').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes, 
            'r9002_infototal': r9002_infototal, 
            'r9002_infototal_form': r9002_infototal_form, 
            'modulos': ['r9002', ],
            'paginas': ['r9002_infototal', ],
            'r9002_totapurmen_form': r9002_totapurmen_form,
            'r9002_totapurmen_lista': r9002_totapurmen_lista,
            'r9002_totapurqui_form': r9002_totapurqui_form,
            'r9002_totapurqui_lista': r9002_totapurqui_lista,
            'r9002_totapurdec_form': r9002_totapurdec_form,
            'r9002_totapurdec_lista': r9002_totapurdec_lista,
            'r9002_totapursem_form': r9002_totapursem_form,
            'r9002_totapursem_lista': r9002_totapursem_lista,
            'r9002_totapurdia_form': r9002_totapurdia_form,
            'r9002_totapurdia_lista': r9002_totapurdia_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #r9002_infototal_salvar_custom_variaveis_context#
        }
        
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='r9002_infototal_salvar.html',
                filename="r9002_infototal.pdf",
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
            
            response = render_to_response('r9002_infototal_salvar.html', context)
            filename = "r9002_infototal.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 'r9002_infototal_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['r9002', ],
            'paginas': ['r9002_infototal', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)