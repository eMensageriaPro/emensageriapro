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
from emensageriapro.controle_de_acesso.forms import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.mensageiro.models import ImportacaoArquivos
from emensageriapro.mensageiro.forms import form_importacao_arquivos


@login_required
def salvar(request, hash):
    
    try: 
        usuario_id = request.user.id  
        dict_hash = get_hash_url( hash )
        usuarios_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except: 
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    pagina = ConfigPaginas.objects.get(endereco='usuarios')
    permissao = ConfigPermissoes.objects.get(config_paginas=pagina, config_perfis=usuario.config_perfis)
    
    if usuarios_id:
        usuarios = get_object_or_404(Usuarios, id=usuarios_id)
        user = get_object_or_404(User, id=usuarios.user_id)
        
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        
        if usuarios_id:
            users_form = form_users(request.POST or None, instance=user)
            usuarios_form = form_usuarios(request.POST or None, instance=usuarios)
            
        else:
            users_form = form_users(request.POST or None)
            usuarios_form = form_usuarios(request.POST or None)
            
        if request.method == 'POST':
            if usuarios_form.is_valid() and users_form.is_valid():
                #usuarios_campos_multiple_passo1
                dados = usuarios_form.cleaned_data
                users_dados = users_form.cleaned_data
                if usuarios_id:
                    User.objects.filter(id=usuarios.user_id).update(**users_dados)
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    
                    Usuarios.objects.filter(id=usuarios_id).update(**dados)
                    obj = Usuarios.objects.get(id=usuarios_id)
                else:
                    users_dados['password'] = 'asdkl1231'
                    users_dados['is_superuser'] = False
                    users_dados['is_staff'] = False
                    users_dados['is_active'] = True
                    user_obj = User(**users_dados)
                    user_obj.save()
                    dados['user_id'] = user_obj.pk
                    dados['criado_por_id'] = usuario_id
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
                messages.success(request, 'Salvo com sucesso!')
                #usuarios_campos_multiple_passo2
                
                if request.session['retorno_pagina'] not in ('usuarios_apagar', 'usuarios_salvar', 'usuarios'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if usuarios_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('usuarios_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        usuarios_form = disabled_form_fields(usuarios_form, permissao.permite_editar)
        #usuarios_campos_multiple_passo3
        
        if int(dict_hash['print']):
            usuarios_form = disabled_form_for_print(usuarios_form)
        
        
        importacao_arquivos_lista = None 
        importacao_arquivos_form = None 
        
        if usuarios_id:
            usuarios = get_object_or_404(Usuarios, id = usuarios_id)
            
            auditoria_form = form_auditoria(
                initial={ 'operador': usuarios })
            auditoria_form.fields['operador'].widget.attrs['readonly'] = True
            auditoria_lista = Auditoria.objects.\
                filter(operador_id=usuarios.id).all()
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
        if dict_hash['tab'] or 'usuarios' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'usuarios_salvar'
        context = {
            'usuarios': usuarios, 
            'usuarios_form': usuarios_form,
            'users_form': users_form, 
            'usuarios_id': int(usuarios_id),
            'usuario': usuario, 
            'hash': hash, 
            
            'importacao_arquivos_form': importacao_arquivos_form,
            'importacao_arquivos_lista': importacao_arquivos_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #usuarios_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 'usuarios_salvar.html', context)
            
        elif for_print == 2:
        
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
                             "no-stop-slow-scripts": True},
            )
            return response
            
        elif for_print == 3:
        
            from django.shortcuts import render_to_response
            response = render_to_response('usuarios_salvar.html', context)
            filename = "usuarios.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
    
        context = {
            'usuario': usuario, 
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        
        return render(request, 'permissao_negada.html', context)