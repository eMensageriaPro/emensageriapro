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
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        retornos_eventos_horarios_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='retornos_eventos_horarios')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if retornos_eventos_horarios_id:
        retornos_eventos_horarios = get_object_or_404(RetornosEventosHorarios.objects.using( db_slug ), excluido = False, id = retornos_eventos_horarios_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if retornos_eventos_horarios_id:
            retornos_eventos_horarios_form = form_retornos_eventos_horarios(request.POST or None, instance = retornos_eventos_horarios, slug = db_slug)
        else:
            retornos_eventos_horarios_form = form_retornos_eventos_horarios(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if retornos_eventos_horarios_form.is_valid():
                dados = retornos_eventos_horarios_form.cleaned_data
                if retornos_eventos_horarios_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #retornos_eventos_horarios_campos_multiple_passo1
                    RetornosEventosHorarios.objects.using(db_slug).filter(id=retornos_eventos_horarios_id).update(**dados)
                    obj = RetornosEventosHorarios.objects.using(db_slug).get(id=retornos_eventos_horarios_id)
                    #retornos_eventos_horarios_editar_custom
                    #retornos_eventos_horarios_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #retornos_eventos_horarios_cadastrar_campos_multiple_passo1
                    obj = RetornosEventosHorarios(**dados)
                    obj.save(using = db_slug)
                    #retornos_eventos_horarios_cadastrar_custom
                    #retornos_eventos_horarios_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('retornos_eventos_horarios_apagar', 'retornos_eventos_horarios_salvar', 'retornos_eventos_horarios'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if retornos_eventos_horarios_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('retornos_eventos_horarios_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        retornos_eventos_horarios_form = disabled_form_fields(retornos_eventos_horarios_form, permissao.permite_editar)
        #retornos_eventos_horarios_campos_multiple_passo3

        for field in retornos_eventos_horarios_form.fields.keys():
            retornos_eventos_horarios_form.fields[field].widget.attrs['ng-model'] = 'retornos_eventos_horarios_'+field
        if int(dict_hash['print']):
            retornos_eventos_horarios_form = disabled_form_for_print(retornos_eventos_horarios_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if retornos_eventos_horarios_id:
            retornos_eventos_horarios = get_object_or_404(RetornosEventosHorarios.objects.using( db_slug ), excluido = False, id = retornos_eventos_horarios_id)
            pass
        else:
            retornos_eventos_horarios = None
        #retornos_eventos_horarios_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'retornos_eventos_horarios' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'retornos_eventos_horarios_salvar'
        context = {
            'retornos_eventos_horarios': retornos_eventos_horarios,
            'retornos_eventos_horarios_form': retornos_eventos_horarios_form,
            'mensagem': mensagem,
            'retornos_eventos_horarios_id': int(retornos_eventos_horarios_id),
            'usuario': usuario,
            
            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #retornos_eventos_horarios_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'retornos_eventos_horarios_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='retornos_eventos_horarios_salvar.html',
                filename="retornos_eventos_horarios.pdf",
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
            response = render_to_response('retornos_eventos_horarios_salvar.html', context)
            filename = "retornos_eventos_horarios.xls"
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

@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        retornos_eventos_horarios_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='retornos_eventos_horarios')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    retornos_eventos_horarios = get_object_or_404(RetornosEventosHorarios.objects.using( db_slug ), excluido = False, id = retornos_eventos_horarios_id)
    if request.method == 'POST':
        RetornosEventosHorarios.objects.using( db_slug ).filter(id = retornos_eventos_horarios_id).update(excluido = True)
        #retornos_eventos_horarios_apagar_custom
        #retornos_eventos_horarios_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'retornos_eventos_horarios_salvar':
            return redirect('retornos_eventos_horarios', hash=request.session['retorno_hash'])
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
    return render(request, 'retornos_eventos_horarios_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class RetornosEventosHorariosList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = RetornosEventosHorarios.objects.using(db_slug).all()
    serializer_class = RetornosEventosHorariosSerializer
    permission_classes = (IsAdminUser,)


class RetornosEventosHorariosDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = RetornosEventosHorarios.objects.using(db_slug).all()
    serializer_class = RetornosEventosHorariosSerializer
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
        #retornos_eventos_horarios_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='retornos_eventos_horarios')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_retornos_eventos': 1,
            'show_dia': 0,
            'show_codhorcontrat': 1,
            'show_hrentr': 0,
            'show_hrsaida': 0,
            'show_durjornada': 0,
            'show_perhorflexivel': 0, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'retornos_eventos': 'retornos_eventos',
                'dia': 'dia',
                'codhorcontrat__icontains': 'codhorcontrat__icontains',
                'hrentr__icontains': 'hrentr__icontains',
                'hrsaida__icontains': 'hrsaida__icontains',
                'durjornada': 'durjornada',
                'perhorflexivel__icontains': 'perhorflexivel__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'retornos_eventos': 'retornos_eventos',
                'dia': 'dia',
                'codhorcontrat__icontains': 'codhorcontrat__icontains',
                'hrentr__icontains': 'hrentr__icontains',
                'hrsaida__icontains': 'hrsaida__icontains',
                'durjornada': 'durjornada',
                'perhorflexivel__icontains': 'perhorflexivel__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        retornos_eventos_horarios_lista = RetornosEventosHorarios.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(retornos_eventos_horarios_lista) > 100:
            filtrar = True
            retornos_eventos_horarios_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        retornos_eventos_lista = RetornosEventos.objects.using( db_slug ).filter(excluido = False).all()
        #retornos_eventos_horarios_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'retornos_eventos_horarios'
        context = {
            'retornos_eventos_horarios_lista': retornos_eventos_horarios_lista,
            
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
       
            'retornos_eventos_lista': retornos_eventos_lista,
        }
        if for_print in (0,1):
            return render(request, 'retornos_eventos_horarios_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='retornos_eventos_horarios_listar.html',
                filename="retornos_eventos_horarios.pdf",
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
            response = render_to_response('retornos_eventos_horarios_listar.html', context)
            filename = "retornos_eventos_horarios.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/retornos_eventos_horarios_csv.html', context)
            filename = "retornos_eventos_horarios.csv"
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

