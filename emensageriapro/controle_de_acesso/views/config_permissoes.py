#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



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
        config_permissoes_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='config_permissoes')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if config_permissoes_id:
        config_permissoes = get_object_or_404(ConfigPermissoes.objects.using( db_slug ), excluido = False, id = config_permissoes_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if config_permissoes_id:
            config_permissoes_form = form_config_permissoes(request.POST or None, instance = config_permissoes, slug = db_slug)
        else:
            config_permissoes_form = form_config_permissoes(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if config_permissoes_form.is_valid():
                dados = config_permissoes_form.cleaned_data
                if config_permissoes_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #config_permissoes_campos_multiple_passo1
                    ConfigPermissoes.objects.using(db_slug).filter(id=config_permissoes_id).update(**dados)
                    obj = ConfigPermissoes.objects.using(db_slug).get(id=config_permissoes_id)
                    #config_permissoes_editar_custom
                    #config_permissoes_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #config_permissoes_cadastrar_campos_multiple_passo1
                    obj = ConfigPermissoes(**dados)
                    obj.save(using = db_slug)
                    #config_permissoes_cadastrar_custom
                    #config_permissoes_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('config_permissoes_apagar', 'config_permissoes_salvar', 'config_permissoes'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if config_permissoes_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('config_permissoes_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        config_permissoes_form = disabled_form_fields(config_permissoes_form, permissao.permite_editar)
        #config_permissoes_campos_multiple_passo3

        for field in config_permissoes_form.fields.keys():
            config_permissoes_form.fields[field].widget.attrs['ng-model'] = 'config_permissoes_'+field
        if int(dict_hash['print']):
            config_permissoes_form = disabled_form_for_print(config_permissoes_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if config_permissoes_id:
            config_permissoes = get_object_or_404(ConfigPermissoes.objects.using( db_slug ), excluido = False, id = config_permissoes_id)
            pass
        else:
            config_permissoes = None
        #config_permissoes_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'config_permissoes' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'config_permissoes_salvar'
        context = {
            'config_permissoes': config_permissoes,
            'config_permissoes_form': config_permissoes_form,
            'mensagem': mensagem,
            'config_permissoes_id': int(config_permissoes_id),
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
            #config_permissoes_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'config_permissoes_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='config_permissoes_salvar.html',
                filename="config_permissoes.pdf",
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
            response = render_to_response('config_permissoes_salvar.html', context)
            filename = "config_permissoes.xls"
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
        config_permissoes_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='config_permissoes')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    config_permissoes = get_object_or_404(ConfigPermissoes.objects.using( db_slug ), excluido = False, id = config_permissoes_id)
    if request.method == 'POST':
        ConfigPermissoes.objects.using( db_slug ).filter(id = config_permissoes_id).update(excluido = True)
        #config_permissoes_apagar_custom
        #config_permissoes_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'config_permissoes_salvar':
            return redirect('config_permissoes', hash=request.session['retorno_hash'])
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
    return render(request, 'config_permissoes_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class ConfigPermissoesList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = ConfigPermissoes.objects.using(db_slug).all()
    serializer_class = ConfigPermissoesSerializer
    permission_classes = (IsAdminUser,)


class ConfigPermissoesDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = ConfigPermissoes.objects.using(db_slug).all()
    serializer_class = ConfigPermissoesSerializer
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
        #config_permissoes_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='config_permissoes')
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
            'show_permite_apagar': 0,
            'show_permite_visualizar': 0,
            'show_permite_editar': 0,
            'show_permite_cadastrar': 0,
            'show_permite_listar': 0,
            'show_config_paginas': 1,
            'show_config_perfis': 1, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'permite_apagar': 'permite_apagar',
                'permite_visualizar': 'permite_visualizar',
                'permite_editar': 'permite_editar',
                'permite_cadastrar': 'permite_cadastrar',
                'permite_listar': 'permite_listar',
                'config_paginas': 'config_paginas',
                'config_perfis': 'config_perfis',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'permite_apagar': 'permite_apagar',
                'permite_visualizar': 'permite_visualizar',
                'permite_editar': 'permite_editar',
                'permite_cadastrar': 'permite_cadastrar',
                'permite_listar': 'permite_listar',
                'config_paginas': 'config_paginas',
                'config_perfis': 'config_perfis',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        config_permissoes_lista = ConfigPermissoes.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(config_permissoes_lista) > 100:
            filtrar = True
            config_permissoes_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        config_paginas_lista = ConfigPaginas.objects.using( db_slug ).filter(excluido = False).all()
        config_perfis_lista = ConfigPerfis.objects.using( db_slug ).filter(excluido = False).all()
        #config_permissoes_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'config_permissoes'
        context = {
            'config_permissoes_lista': config_permissoes_lista,
            
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
       
            'config_paginas_lista': config_paginas_lista,
            'config_perfis_lista': config_perfis_lista,
        }
        if for_print in (0,1):
            return render(request, 'config_permissoes_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='config_permissoes_listar.html',
                filename="config_permissoes.pdf",
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
            response = render_to_response('config_permissoes_listar.html', context)
            filename = "config_permissoes.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/config_permissoes_csv.html', context)
            filename = "config_permissoes.csv"
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

