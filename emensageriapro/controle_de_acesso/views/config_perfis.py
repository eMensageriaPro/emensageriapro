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
import json
import base64

#IMPORTACOES
@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        config_perfis_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='config_perfis')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    config_perfis = get_object_or_404(ConfigPerfis.objects.using( db_slug ), excluido = False, id = config_perfis_id)
    if request.method == 'POST':
        obj = ConfigPerfis.objects.using( db_slug ).get(id = config_perfis_id)
        obj.delete(request=request)
        #config_perfis_apagar_custom
        #config_perfis_apagar_custom
        messages.success(request, u'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'config_perfis_salvar':
            return redirect('config_perfis', hash=request.session['retorno_hash'])
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
    return render(request, 'config_perfis_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class ConfigPerfisList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = ConfigPerfis.objects.using(db_slug).all()
    serializer_class = ConfigPerfisSerializer
    # permission_classes = (IsAdminUser,)


class ConfigPerfisDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = ConfigPerfis.objects.using(db_slug).all()
    serializer_class = ConfigPerfisSerializer
    # permission_classes = (IsAdminUser,)


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #config_perfis_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='config_perfis')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_modulos_permitidos': 0,
            'show_paginas_permitidas': 0,
            'show_permissoes': 0,
            'show_titulo': 1, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'titulo__icontains': 'titulo__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'titulo__icontains': 'titulo__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        config_perfis_lista = ConfigPerfis.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(config_perfis_lista) > 100:
            filtrar = True
            config_perfis_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #config_perfis_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'config_perfis'
        context = {
            'config_perfis_lista': config_perfis_lista,
  
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

        }
        if for_print in (0,1):
            return render(request, 'config_perfis_listar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='config_perfis_listar.html',
                filename="config_perfis.pdf",
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
            response = render_to_response('config_perfis_listar.html', context)
            filename = "config_perfis.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/config_perfis_csv.html', context)
            filename = "config_perfis.csv"
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
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        config_perfis_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='config_perfis')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if config_perfis_id:
        config_perfis = get_object_or_404(ConfigPerfis.objects.using( db_slug ), excluido = False, id = config_perfis_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if config_perfis_id:
            config_perfis_form = form_config_perfis(request.POST or None,
                                instance = config_perfis,
                                slug = db_slug,
                                initial = {'excluido': False})
        else:
            config_perfis_form = form_config_perfis(request.POST or None,
                                slug = db_slug,
                                initial = {'excluido': False})
        if request.method == 'POST':
            if config_perfis_form.is_valid():
                #config_perfis_campos_multiple_passo1
                obj = config_perfis_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')
                from emensageriapro.controle_de_acesso.views.login import criar_permissoes
                criar_permissoes(db_slug)

                if request.session['retorno_pagina'] not in ('config_perfis_apagar', 'config_perfis_salvar', 'config_perfis'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if config_perfis_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('config_perfis_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        config_perfis_form = disabled_form_fields(config_perfis_form, permissao.permite_editar)
        #config_perfis_campos_multiple_passo3

        for field in config_perfis_form.fields.keys():
            config_perfis_form.fields[field].widget.attrs['ng-model'] = 'config_perfis_'+field
        if int(dict_hash['print']):
            config_perfis_form = disabled_form_for_print(config_perfis_form)

        config_permissoes_form = None
        config_permissoes_lista = None
        usuarios_form = None
        usuarios_lista = None
        if config_perfis_id:
            config_perfis = get_object_or_404(ConfigPerfis.objects.using( db_slug ), excluido = False, id = config_perfis_id)

            config_permissoes_form = form_config_permissoes(initial={ 'config_perfis': config_perfis }, slug=db_slug)
            config_permissoes_form.fields['config_perfis'].widget.attrs['readonly'] = True
            config_permissoes_lista = ConfigPermissoes.objects.using( db_slug ).filter(excluido = False, config_perfis_id=config_perfis.id).all()
            usuarios_form = form_usuarios(initial={ 'config_perfis': config_perfis , 'foto': 'data:image/png;base64,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', 'password': 'asdkl1231'}, slug=db_slug)
            usuarios_form.fields['config_perfis'].widget.attrs['readonly'] = True
            usuarios_lista = Usuarios.objects.using( db_slug ).filter(excluido = False, config_perfis_id=config_perfis.id).all()
        else:
            config_perfis = None
        #config_perfis_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'config_perfis' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'config_perfis_salvar'
        context = {
            'config_perfis': config_perfis,
            'config_perfis_form': config_perfis_form,
            'mensagem': mensagem,
            'config_perfis_id': int(config_perfis_id),
            'usuario': usuario,
  
            'hash': hash,

            'config_permissoes_form': config_permissoes_form,
            'config_permissoes_lista': config_permissoes_lista,
            'usuarios_form': usuarios_form,
            'usuarios_lista': usuarios_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #config_perfis_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'config_perfis_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='config_perfis_salvar.html',
                filename="config_perfis.pdf",
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
            response = render_to_response('config_perfis_salvar.html', context)
            filename = "config_perfis.xls"
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

