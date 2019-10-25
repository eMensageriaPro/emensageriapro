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
from emensageriapro.s5011.forms import *
from emensageriapro.s5011.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s5011.models import s5011infoTercSusp
from emensageriapro.s5011.forms import form_s5011_infotercsusp
from emensageriapro.s5011.models import s5011infoEmprParcial
from emensageriapro.s5011.forms import form_s5011_infoemprparcial
from emensageriapro.s5011.models import s5011dadosOpPort
from emensageriapro.s5011.forms import form_s5011_dadosopport
from emensageriapro.s5011.models import s5011basesRemun
from emensageriapro.s5011.forms import form_s5011_basesremun
from emensageriapro.s5011.models import s5011basesAvNPort
from emensageriapro.s5011.forms import form_s5011_basesavnport
from emensageriapro.s5011.models import s5011infoSubstPatrOpPort
from emensageriapro.s5011.forms import form_s5011_infosubstpatropport



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO
    
    if pk:
    
        s5011_idelotacao = get_object_or_404(s5011ideLotacao, id=pk)
        evento_dados = s5011_idelotacao.evento()

    if request.user.has_perm('s5011.can_see_s5011ideLotacao'):
        
        if pk:
        
            s5011_idelotacao_form = form_s5011_idelotacao(
                request.POST or None, 
                instance=s5011_idelotacao)
                                         
        else:
        
            s5011_idelotacao_form = form_s5011_idelotacao(request.POST or None)
                                         
        if request.method == 'POST':
        
            if s5011_idelotacao_form.is_valid():
            
                obj = s5011_idelotacao_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    gravar_auditoria(
                        '{}',
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        's5011_idelotacao', 
                        obj.id, 
                        request.user.id, 1)
                                 
                else:
                
                    gravar_auditoria(
                        json.dumps(
                            model_to_dict(s5011_idelotacao), 
                            indent=4, 
                            sort_keys=True, 
                            default=str),
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        's5011_idelotacao', 
                        pk, 
                        request.user.id, 2)
                                     
                if request.session['return_page'] not in (
                    's5011_idelotacao_apagar', 
                    's5011_idelotacao_salvar', 
                    's5011_idelotacao'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'])
                    
                if pk != obj.id:
                
                    return redirect(
                        's5011_idelotacao_salvar', 
                        pk=obj.id)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        s5011_idelotacao_form = disabled_form_fields(
            s5011_idelotacao_form, 
            request.user.has_perm('s5011.change_s5011ideLotacao'))
        
        if pk:
        
            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:
            
                s5011_idelotacao_form = disabled_form_fields(s5011_idelotacao_form, 0)
                
        if output:
        
            s5011_idelotacao_form = disabled_form_for_print(s5011_idelotacao_form)
            
        
        s5011_infotercsusp_lista = None 
        s5011_infotercsusp_form = None 
        s5011_infoemprparcial_lista = None 
        s5011_infoemprparcial_form = None 
        s5011_dadosopport_lista = None 
        s5011_dadosopport_form = None 
        s5011_basesremun_lista = None 
        s5011_basesremun_form = None 
        s5011_basesavnport_lista = None 
        s5011_basesavnport_form = None 
        s5011_infosubstpatropport_lista = None 
        s5011_infosubstpatropport_form = None 
        
        if pk:
        
            s5011_idelotacao = get_object_or_404(s5011ideLotacao, id=pk)
            
            s5011_infotercsusp_form = form_s5011_infotercsusp(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_infotercsusp_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_infotercsusp_lista = s5011infoTercSusp.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
                
            s5011_infoemprparcial_form = form_s5011_infoemprparcial(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_infoemprparcial_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_infoemprparcial_lista = s5011infoEmprParcial.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
                
            s5011_dadosopport_form = form_s5011_dadosopport(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_dadosopport_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_dadosopport_lista = s5011dadosOpPort.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
                
            s5011_basesremun_form = form_s5011_basesremun(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_basesremun_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_basesremun_lista = s5011basesRemun.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
                
            s5011_basesavnport_form = form_s5011_basesavnport(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_basesavnport_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_basesavnport_lista = s5011basesAvNPort.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
                
            s5011_infosubstpatropport_form = form_s5011_infosubstpatropport(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_infosubstpatropport_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_infosubstpatropport_lista = s5011infoSubstPatrOpPort.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
                
                
        else:
        
            s5011_idelotacao = None
            
        tabelas_secundarias = []
        
        if tab or 's5011_idelotacao' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 's5011_idelotacao_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s5011_idelotacao').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes, 
            's5011_idelotacao': s5011_idelotacao, 
            's5011_idelotacao_form': s5011_idelotacao_form, 
            'modulos': ['s5011', ],
            'paginas': ['s5011_idelotacao', ],
            's5011_infotercsusp_form': s5011_infotercsusp_form,
            's5011_infotercsusp_lista': s5011_infotercsusp_lista,
            's5011_infoemprparcial_form': s5011_infoemprparcial_form,
            's5011_infoemprparcial_lista': s5011_infoemprparcial_lista,
            's5011_dadosopport_form': s5011_dadosopport_form,
            's5011_dadosopport_lista': s5011_dadosopport_lista,
            's5011_basesremun_form': s5011_basesremun_form,
            's5011_basesremun_lista': s5011_basesremun_lista,
            's5011_basesavnport_form': s5011_basesavnport_form,
            's5011_basesavnport_lista': s5011_basesavnport_lista,
            's5011_infosubstpatropport_form': s5011_infosubstpatropport_form,
            's5011_infosubstpatropport_lista': s5011_infosubstpatropport_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s5011_idelotacao_salvar_custom_variaveis_context#
        }
        
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='s5011_idelotacao_salvar.html',
                filename="s5011_idelotacao.pdf",
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
            
            response = render_to_response('s5011_idelotacao_salvar.html', context)
            filename = "s5011_idelotacao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 's5011_idelotacao_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s5011', ],
            'paginas': ['s5011_idelotacao', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)