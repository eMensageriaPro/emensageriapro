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
from emensageriapro.tabelas.forms import *
from emensageriapro.tabelas.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        esocial_partes_corpo_atingidas_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='esocial_partes_corpo_atingidas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    esocial_partes_corpo_atingidas = get_object_or_404(eSocialPartesCorpoAtingidas.objects.using( db_slug ), excluido = False, id = esocial_partes_corpo_atingidas_id)
    if request.method == 'POST':
        eSocialPartesCorpoAtingidas.objects.using( db_slug ).filter(id = esocial_partes_corpo_atingidas_id).update(excluido = True)
        #esocial_partes_corpo_atingidas_apagar_custom
        #esocial_partes_corpo_atingidas_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'esocial_partes_corpo_atingidas_salvar':
            return redirect('esocial_partes_corpo_atingidas', hash=request.session['retorno_hash'])
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
    return render(request, 'esocial_partes_corpo_atingidas_apagar.html', context)

@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        esocial_partes_corpo_atingidas_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='esocial_partes_corpo_atingidas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if esocial_partes_corpo_atingidas_id:
        esocial_partes_corpo_atingidas = get_object_or_404(eSocialPartesCorpoAtingidas.objects.using( db_slug ), excluido = False, id = esocial_partes_corpo_atingidas_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if esocial_partes_corpo_atingidas_id:
            esocial_partes_corpo_atingidas_form = form_esocial_partes_corpo_atingidas(request.POST or None, instance = esocial_partes_corpo_atingidas, slug = db_slug)
        else:
            esocial_partes_corpo_atingidas_form = form_esocial_partes_corpo_atingidas(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if esocial_partes_corpo_atingidas_form.is_valid():
                dados = esocial_partes_corpo_atingidas_form.cleaned_data
                if esocial_partes_corpo_atingidas_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #esocial_partes_corpo_atingidas_campos_multiple_passo1
                    eSocialPartesCorpoAtingidas.objects.using(db_slug).filter(id=esocial_partes_corpo_atingidas_id).update(**dados)
                    obj = eSocialPartesCorpoAtingidas.objects.using(db_slug).get(id=esocial_partes_corpo_atingidas_id)
                    #esocial_partes_corpo_atingidas_editar_custom
                    #esocial_partes_corpo_atingidas_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #esocial_partes_corpo_atingidas_cadastrar_campos_multiple_passo1
                    obj = eSocialPartesCorpoAtingidas(**dados)
                    obj.save(using = db_slug)
                    #esocial_partes_corpo_atingidas_cadastrar_custom
                    #esocial_partes_corpo_atingidas_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('esocial_partes_corpo_atingidas_apagar', 'esocial_partes_corpo_atingidas_salvar', 'esocial_partes_corpo_atingidas'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if esocial_partes_corpo_atingidas_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('esocial_partes_corpo_atingidas_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        esocial_partes_corpo_atingidas_form = disabled_form_fields(esocial_partes_corpo_atingidas_form, permissao.permite_editar)
        #esocial_partes_corpo_atingidas_campos_multiple_passo3

        for field in esocial_partes_corpo_atingidas_form.fields.keys():
            esocial_partes_corpo_atingidas_form.fields[field].widget.attrs['ng-model'] = 'esocial_partes_corpo_atingidas_'+field
        if int(dict_hash['print']):
            esocial_partes_corpo_atingidas_form = disabled_form_for_print(esocial_partes_corpo_atingidas_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if esocial_partes_corpo_atingidas_id:
            esocial_partes_corpo_atingidas = get_object_or_404(eSocialPartesCorpoAtingidas.objects.using( db_slug ), excluido = False, id = esocial_partes_corpo_atingidas_id)
            pass
        else:
            esocial_partes_corpo_atingidas = None
        #esocial_partes_corpo_atingidas_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'esocial_partes_corpo_atingidas' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'esocial_partes_corpo_atingidas_salvar'
        context = {
            'esocial_partes_corpo_atingidas': esocial_partes_corpo_atingidas,
            'esocial_partes_corpo_atingidas_form': esocial_partes_corpo_atingidas_form,
            'mensagem': mensagem,
            'esocial_partes_corpo_atingidas_id': int(esocial_partes_corpo_atingidas_id),
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
            #esocial_partes_corpo_atingidas_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'esocial_partes_corpo_atingidas_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='esocial_partes_corpo_atingidas_salvar.html',
                filename="esocial_partes_corpo_atingidas.pdf",
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
            response = render_to_response('esocial_partes_corpo_atingidas_salvar.html', context)
            filename = "esocial_partes_corpo_atingidas.xls"
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


class eSocialPartesCorpoAtingidasList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = eSocialPartesCorpoAtingidas.objects.using(db_slug).all()
    serializer_class = eSocialPartesCorpoAtingidasSerializer
    permission_classes = (IsAdminUser,)


class eSocialPartesCorpoAtingidasDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = eSocialPartesCorpoAtingidas.objects.using(db_slug).all()
    serializer_class = eSocialPartesCorpoAtingidasSerializer
    permission_classes = (IsAdminUser,)


def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required
def json_search(request, search):
    from django.http import JsonResponse
    import operator
    from django.db.models import Count, Q
    import urllib
    db_slug = 'default'
    search = urllib.unquote(search)
    lista = search.split(" ")
    dicionario = {}
    if search.strip():
        try:
            query = reduce(operator.and_, ((Q(titulo__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = eSocialPartesCorpoAtingidas.objects.using(db_slug).filter(excluido = False).filter(query).all()
        except:
            query = reduce(operator.and_, ((Q(descricao__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = eSocialPartesCorpoAtingidas.objects.using(db_slug).filter(excluido = False).filter(query).all()
    else:
        lista = eSocialPartesCorpoAtingidas.objects.using(db_slug).filter(excluido=False).all()
    lista_esocial_partes_corpo_atingidas = []
    for a in lista:
        dic = {}
        dic['key'] = a.codigo
        dic['value'] = '%s' % (a)
        lista_esocial_partes_corpo_atingidas.append(dic)
    dicionario['esocial_partes_corpo_atingidas'] = lista_esocial_partes_corpo_atingidas
    return JsonResponse(dicionario)


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #esocial_partes_corpo_atingidas_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='esocial_partes_corpo_atingidas')
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
            'show_descricao': 1,
            'show_codigo': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'descricao__icontains': 'descricao__icontains',
                'codigo__icontains': 'codigo__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'descricao__icontains': 'descricao__icontains',
                'codigo__icontains': 'codigo__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        esocial_partes_corpo_atingidas_lista = eSocialPartesCorpoAtingidas.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(esocial_partes_corpo_atingidas_lista) > 100:
            filtrar = True
            esocial_partes_corpo_atingidas_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
    
        #esocial_partes_corpo_atingidas_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'esocial_partes_corpo_atingidas'
        context = {
            'esocial_partes_corpo_atingidas_lista': esocial_partes_corpo_atingidas_lista,
            
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
            return render(request, 'esocial_partes_corpo_atingidas_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='esocial_partes_corpo_atingidas_listar.html',
                filename="esocial_partes_corpo_atingidas.pdf",
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
            response = render_to_response('esocial_partes_corpo_atingidas_listar.html', context)
            filename = "esocial_partes_corpo_atingidas.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/esocial_partes_corpo_atingidas_csv.html', context)
            filename = "esocial_partes_corpo_atingidas.csv"
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

