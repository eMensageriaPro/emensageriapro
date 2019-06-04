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
from emensageriapro.controle_de_acesso.forms import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.mensageiro.models import ImportacaoArquivos
from emensageriapro.mensageiro.forms import form_importacao_arquivos


@login_required
def salvar(request, pk=None, tab='master', output=None):
    
    if pk:
    
        usuarios = get_object_or_404(Usuarios, id=pk)
        user = get_object_or_404(User, id=usuarios.user_id)
        
    if request.user.has_perm('controle_de_acesso.can_see_Usuarios'):
        
        if pk:
        
            usuarios_form = form_usuarios(request.POST or None, instance=usuarios)
            users_form = form_users(request.POST or None, instance=user)
            
        else:
        
            usuarios_form = form_usuarios(request.POST or None)
            users_form = form_users(request.POST or None)
            
        if request.method == 'POST':
        
            if usuarios_form.is_valid() and users_form.is_valid():
            
                #usuarios_campos_multiple_passo1
                
                dados = usuarios_form.cleaned_data
                users_dados = users_form.cleaned_data
                
                if pk:
                
                    User.objects.filter(id=usuarios.user_id).update(**users_dados)
                    dados['modificado_por_id'] = request.user.id
                    dados['modificado_em'] = datetime.datetime.now()
                    
                    Usuarios.objects.filter(id=pk).update(**dados)
                    obj = Usuarios.objects.get(id=pk)
                    
                else:
                
                    users_dados['password'] = 'asdkl1231'
                    users_dados['is_superuser'] = False
                    users_dados['is_staff'] = False
                    users_dados['is_active'] = True
                    user_obj = User(**users_dados)
                    user_obj.save()
                    
                    dados['user_id'] = user_obj.pk
                    dados['criado_por_id'] = request.user.id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    obj = Usuarios(**dados)
                    obj.save()
                    
                    from emensageriapro.controle_de_acesso.views.login_recuperar_senha import recuperar_senha_funcao
                    
                    try:
                    
                        recuperar_senha_funcao(users_dados['email'])
                        messages.success(request, 'A senha foi enviada para o e-mail %(email)s!' % users_dados)
                        
                    except:
                    
                        messages.error(request, 'Erro ao enviar o email com a senha!')
                #usuarios_campos_multiple_passo2
                
                if request.session['return_page'] not in (
                    'usuarios_apagar', 
                    'usuarios_salvar', 
                    'usuarios'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'], 
                        tab=request.session['return_tab'])
                    
                if pk != obj.id:
                
                    return redirect(
                        'usuarios_salvar', 
                        pk=obj.id, 
                        tab='master')
                    
            else:
            
                messages.error(request, 'Erro ao salvar!')
                
        usuarios_form = disabled_form_fields(usuarios_form, request.user.has_perm('controle_de_acesso.change_Usuarios'))
        users_form = disabled_form_fields(users_form, request.user.has_perm('controle_de_acesso.change_Usuarios'))
        #usuarios_campos_multiple_passo3
        
        if output:
        
            usuarios_form = disabled_form_for_print(usuarios_form)
            users_form = disabled_form_for_print(users_form)
        
        
        importacao_arquivos_lista = None 
        importacao_arquivos_form = None 
        
        if pk:
        
            usuarios = get_object_or_404(Usuarios, id=pk)
            user = get_object_or_404(User, id=usuarios.user_id)
            
            importacao_arquivos_form = form_importacao_arquivos(
                initial={ 'importado_por': usuarios })
            importacao_arquivos_form.fields['importado_por'].widget.attrs['readonly'] = True
            importacao_arquivos_lista = ImportacaoArquivos.objects.\
                filter(importado_por_id=usuarios.id).all()
                
                
        else:
        
            usuarios = None
            
        #usuarios_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if tab or 'usuarios' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 'usuarios_salvar'
            
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'usuarios': usuarios, 
            'users_form': users_form,
            'usuarios_form': usuarios_form, 
            'importacao_arquivos_form': importacao_arquivos_form,
            'importacao_arquivos_lista': importacao_arquivos_lista,
            'modulos': ['controle_de_acesso', ],
            'paginas': ['usuarios', ],
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            #usuarios_salvar_custom_variaveis_context#
        }
            
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='usuarios_salvar.html',
                filename="usuarios.pdf",
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
            
            response = render_to_response('usuarios_salvar.html', context)
            filename = "usuarios.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
        
        else:
        
            return render(request, 'usuarios_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['controle_de_acesso', ],
            'paginas': ['usuarios', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
            'permissao_negada.html', 
            context)