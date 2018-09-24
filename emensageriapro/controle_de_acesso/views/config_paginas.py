#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.controle_de_acesso.forms import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        config_paginas_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='config_paginas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if config_paginas_id:
        config_paginas = get_object_or_404(ConfigPaginas.objects.using( db_slug ), excluido = False, id = config_paginas_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if config_paginas_id:
            config_paginas_form = form_config_paginas(request.POST or None, instance = config_paginas, slug = db_slug)
        else:
            config_paginas_form = form_config_paginas(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if config_paginas_form.is_valid():
                dados = config_paginas_form.cleaned_data
                if config_paginas_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #config_paginas_campos_multiple_passo1
                    ConfigPaginas.objects.using(db_slug).filter(id=config_paginas_id).update(**dados)
                    obj = ConfigPaginas.objects.using(db_slug).get(id=config_paginas_id)
                    #config_paginas_editar_custom
                    #config_paginas_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #config_paginas_cadastrar_campos_multiple_passo1
                    obj = ConfigPaginas(**dados)
                    obj.save(using = db_slug)
                    #config_paginas_cadastrar_custom
                    #config_paginas_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('config_paginas_apagar', 'config_paginas_salvar', 'config_paginas'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if config_paginas_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('config_paginas_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        config_paginas_form = disabled_form_fields(config_paginas_form, permissao.permite_editar)
        #config_paginas_campos_multiple_passo3

        for field in config_paginas_form.fields.keys():
            config_paginas_form.fields[field].widget.attrs['ng-model'] = 'config_paginas_'+field
        if int(dict_hash['print']):
            config_paginas_form = disabled_form_for_print(config_paginas_form)

        config_permissoes_form = None
        config_permissoes_lista = None
        if config_paginas_id:
            config_paginas = get_object_or_404(ConfigPaginas.objects.using( db_slug ), excluido = False, id = config_paginas_id)
  
            config_permissoes_form = form_config_permissoes(initial={ 'config_paginas': config_paginas }, slug=db_slug)
            config_permissoes_form.fields['config_paginas'].widget.attrs['readonly'] = True
            config_permissoes_lista = ConfigPermissoes.objects.using( db_slug ).filter(excluido = False, config_paginas_id=config_paginas.id).all()
        else:
            config_paginas = None
        #config_paginas_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'config_paginas' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'config_paginas_salvar'
        context = {
            'config_paginas': config_paginas,
            'config_paginas_form': config_paginas_form,
            'mensagem': mensagem,
            'config_paginas_id': int(config_paginas_id),
            'usuario': usuario,
       
            'hash': hash,
  
            'config_permissoes_form': config_permissoes_form,
            'config_permissoes_lista': config_permissoes_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #config_paginas_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'config_paginas_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='config_paginas_salvar.html',
                filename="config_paginas.pdf",
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
            response = render_to_response('config_paginas_salvar.html', context)
            filename = "config_paginas.xls"
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

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class ConfigPaginasList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = ConfigPaginas.objects.using(db_slug).all()
    serializer_class = ConfigPaginasSerializer
    permission_classes = (IsAdminUser,)


class ConfigPaginasDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = ConfigPaginas.objects.using(db_slug).all()
    serializer_class = ConfigPaginasSerializer
    permission_classes = (IsAdminUser,)


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #config_paginas_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='config_paginas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_ordem': 0,
            'show_tipo': 0,
            'show_exibe_menu': 1,
            'show_endereco': 1,
            'show_titulo': 1,
            'show_config_modulos': 1, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'ordem': 'ordem',
                'tipo': 'tipo',
                'exibe_menu': 'exibe_menu',
                'endereco__icontains': 'endereco__icontains',
                'titulo__icontains': 'titulo__icontains',
                'config_modulos': 'config_modulos',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'ordem': 'ordem',
                'tipo': 'tipo',
                'exibe_menu': 'exibe_menu',
                'endereco__icontains': 'endereco__icontains',
                'titulo__icontains': 'titulo__icontains',
                'config_modulos': 'config_modulos',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        config_paginas_lista = ConfigPaginas.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(config_paginas_lista) > 100:
            filtrar = True
            config_paginas_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        config_modulos_lista = ConfigModulos.objects.using( db_slug ).filter(excluido = False).all()
        #config_paginas_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'config_paginas'
        context = {
            'config_paginas_lista': config_paginas_lista,
       
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
  
            'config_modulos_lista': config_modulos_lista,
        }
        if for_print in (0,1):
            return render(request, 'config_paginas_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='config_paginas_listar.html',
                filename="config_paginas.pdf",
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
            response = render_to_response('config_paginas_listar.html', context)
            filename = "config_paginas.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/config_paginas_csv.html', context)
            filename = "config_paginas.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
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

@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        config_paginas_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='config_paginas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    config_paginas = get_object_or_404(ConfigPaginas.objects.using( db_slug ), excluido = False, id = config_paginas_id)
    if request.method == 'POST':
        ConfigPaginas.objects.using( db_slug ).filter(id = config_paginas_id).update(excluido = True)
        #config_paginas_apagar_custom
        #config_paginas_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'config_paginas_salvar':
            return redirect('config_paginas', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,
   
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,
   
        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'config_paginas_apagar.html', context)

