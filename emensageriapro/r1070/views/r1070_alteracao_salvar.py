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
from emensageriapro.r1070.forms import *
from emensageriapro.r1070.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r1070.models import r1070alteracaoinfoSusp
from emensageriapro.r1070.forms import form_r1070_alteracao_infosusp
from emensageriapro.r1070.models import r1070alteracaodadosProcJud
from emensageriapro.r1070.forms import form_r1070_alteracao_dadosprocjud
from emensageriapro.r1070.models import r1070alteracaonovaValidade
from emensageriapro.r1070.forms import form_r1070_alteracao_novavalidade



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    
    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO
    
    if pk:
    
        r1070_alteracao = get_object_or_404(r1070alteracao, id=pk)
        evento_dados = r1070_alteracao.evento()

    if request.user.has_perm('r1070.can_see_r1070alteracao'):
        
        if pk:
        
            r1070_alteracao_form = form_r1070_alteracao(
                request.POST or None, 
                instance=r1070_alteracao)
                                         
        else:
        
            r1070_alteracao_form = form_r1070_alteracao(request.POST or None)
                                         
        if request.method == 'POST':
        
            if r1070_alteracao_form.is_valid():
            
                obj = r1070_alteracao_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    gravar_auditoria(
                        '{}',
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        'r1070_alteracao', 
                        obj.id, 
                        request.user.id, 1)
                                 
                else:
                
                    gravar_auditoria(
                        json.dumps(
                            model_to_dict(r1070_alteracao), 
                            indent=4, 
                            sort_keys=True, 
                            default=str),
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        'r1070_alteracao', 
                        pk, 
                        request.user.id, 2)
                                     
                if request.session['return_page'] not in (
                    'r1070_alteracao_apagar', 
                    'r1070_alteracao_salvar', 
                    'r1070_alteracao'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'])
                    
                if pk != obj.id:
                
                    return redirect(
                        'r1070_alteracao_salvar', 
                        pk=obj.id)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        r1070_alteracao_form = disabled_form_fields(
            r1070_alteracao_form, 
            request.user.has_perm('r1070.change_r1070alteracao'))
        
        if pk:
        
            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:
            
                r1070_alteracao_form = disabled_form_fields(r1070_alteracao_form, 0)
                
        if output:
        
            r1070_alteracao_form = disabled_form_for_print(r1070_alteracao_form)
            
        
        r1070_alteracao_infosusp_lista = None 
        r1070_alteracao_infosusp_form = None 
        r1070_alteracao_dadosprocjud_lista = None 
        r1070_alteracao_dadosprocjud_form = None 
        r1070_alteracao_novavalidade_lista = None 
        r1070_alteracao_novavalidade_form = None 
        
        if pk:
        
            r1070_alteracao = get_object_or_404(r1070alteracao, id=pk)
            
            r1070_alteracao_infosusp_form = form_r1070_alteracao_infosusp(
                initial={ 'r1070_alteracao': r1070_alteracao })
            r1070_alteracao_infosusp_form.fields['r1070_alteracao'].widget.attrs['readonly'] = True
            r1070_alteracao_infosusp_lista = r1070alteracaoinfoSusp.objects.\
                filter(r1070_alteracao_id=r1070_alteracao.id).all()
                
            r1070_alteracao_dadosprocjud_form = form_r1070_alteracao_dadosprocjud(
                initial={ 'r1070_alteracao': r1070_alteracao })
            r1070_alteracao_dadosprocjud_form.fields['r1070_alteracao'].widget.attrs['readonly'] = True
            r1070_alteracao_dadosprocjud_lista = r1070alteracaodadosProcJud.objects.\
                filter(r1070_alteracao_id=r1070_alteracao.id).all()
                
            r1070_alteracao_novavalidade_form = form_r1070_alteracao_novavalidade(
                initial={ 'r1070_alteracao': r1070_alteracao })
            r1070_alteracao_novavalidade_form.fields['r1070_alteracao'].widget.attrs['readonly'] = True
            r1070_alteracao_novavalidade_lista = r1070alteracaonovaValidade.objects.\
                filter(r1070_alteracao_id=r1070_alteracao.id).all()
                
                
        else:
        
            r1070_alteracao = None
            
        tabelas_secundarias = []
        
        if tab or 'r1070_alteracao' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 'r1070_alteracao_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r1070_alteracao').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes, 
            'r1070_alteracao': r1070_alteracao, 
            'r1070_alteracao_form': r1070_alteracao_form, 
            'modulos': ['r1070', ],
            'paginas': ['r1070_alteracao', ],
            'r1070_alteracao_infosusp_form': r1070_alteracao_infosusp_form,
            'r1070_alteracao_infosusp_lista': r1070_alteracao_infosusp_lista,
            'r1070_alteracao_dadosprocjud_form': r1070_alteracao_dadosprocjud_form,
            'r1070_alteracao_dadosprocjud_lista': r1070_alteracao_dadosprocjud_lista,
            'r1070_alteracao_novavalidade_form': r1070_alteracao_novavalidade_form,
            'r1070_alteracao_novavalidade_lista': r1070_alteracao_novavalidade_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #r1070_alteracao_salvar_custom_variaveis_context#
        }
        
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='r1070_alteracao_salvar.html',
                filename="r1070_alteracao.pdf",
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
            
            response = render_to_response('r1070_alteracao_salvar.html', context)
            filename = "r1070_alteracao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 'r1070_alteracao_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['r1070', ],
            'paginas': ['r1070_alteracao', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)