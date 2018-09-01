#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.tabelas.forms import *
from emensageriapro.tabelas.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        arquivos_esocial_tipos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='arquivos_esocial_tipos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    arquivos_esocial_tipos = get_object_or_404(ArquivosEsocialTipos.objects.using( db_slug ), excluido = False, id = arquivos_esocial_tipos_id)
    if request.method == 'POST':
        ArquivosEsocialTipos.objects.using( db_slug ).filter(id = arquivos_esocial_tipos_id).update(excluido = True)
        #arquivos_esocial_tipos_apagar_custom
        #arquivos_esocial_tipos_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'arquivos_esocial_tipos_salvar':
            return redirect('arquivos_esocial_tipos', hash=request.session['retorno_hash'])
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
    return render(request, 'arquivos_esocial_tipos_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        arquivos_esocial_tipos_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='arquivos_esocial_tipos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if arquivos_esocial_tipos_id:
        arquivos_esocial_tipos = get_object_or_404(ArquivosEsocialTipos.objects.using( db_slug ), excluido = False, id = arquivos_esocial_tipos_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if arquivos_esocial_tipos_id:
            arquivos_esocial_tipos_form = form_arquivos_esocial_tipos(request.POST or None, instance = arquivos_esocial_tipos, slug = db_slug)
        else:
            arquivos_esocial_tipos_form = form_arquivos_esocial_tipos(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if arquivos_esocial_tipos_form.is_valid():
                dados = arquivos_esocial_tipos_form.cleaned_data
                if arquivos_esocial_tipos_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #arquivos_esocial_tipos_campos_multiple_passo1
                    ArquivosEsocialTipos.objects.using(db_slug).filter(id=arquivos_esocial_tipos_id).update(**dados)
                    obj = ArquivosEsocialTipos.objects.using(db_slug).get(id=arquivos_esocial_tipos_id)
                    #arquivos_esocial_tipos_editar_custom
                    #arquivos_esocial_tipos_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #arquivos_esocial_tipos_cadastrar_campos_multiple_passo1
                    obj = ArquivosEsocialTipos(**dados)
                    obj.save(using = db_slug)
                    #arquivos_esocial_tipos_cadastrar_custom
                    #arquivos_esocial_tipos_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('arquivos_esocial_tipos_apagar', 'arquivos_esocial_tipos_salvar', 'arquivos_esocial_tipos'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if arquivos_esocial_tipos_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('arquivos_esocial_tipos_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        arquivos_esocial_tipos_form = disabled_form_fields(arquivos_esocial_tipos_form, permissao.permite_editar)
        #arquivos_esocial_tipos_campos_multiple_passo3

        for field in arquivos_esocial_tipos_form.fields.keys():
            arquivos_esocial_tipos_form.fields[field].widget.attrs['ng-model'] = 'arquivos_esocial_tipos_'+field
        if int(dict_hash['print']):
            arquivos_esocial_tipos_form = disabled_form_for_print(arquivos_esocial_tipos_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if arquivos_esocial_tipos_id:
            arquivos_esocial_tipos = get_object_or_404(ArquivosEsocialTipos.objects.using( db_slug ), excluido = False, id = arquivos_esocial_tipos_id)
            pass
        else:
            arquivos_esocial_tipos = None
        #arquivos_esocial_tipos_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'arquivos_esocial_tipos' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'arquivos_esocial_tipos_salvar'
        context = {
            'arquivos_esocial_tipos': arquivos_esocial_tipos,
            'arquivos_esocial_tipos_form': arquivos_esocial_tipos_form,
            'mensagem': mensagem,
            'arquivos_esocial_tipos_id': int(arquivos_esocial_tipos_id),
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
            #arquivos_esocial_tipos_salvar_custom_variaveis_context#
        }
        return render(request, 'arquivos_esocial_tipos_salvar.html', context)
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
            lista = ArquivosEsocialTipos.objects.using(db_slug).filter(excluido = False).filter(query).all()
        except:
            query = reduce(operator.and_, ((Q(descricao__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = ArquivosEsocialTipos.objects.using(db_slug).filter(excluido = False).filter(query).all()
    else:
        lista = ArquivosEsocialTipos.objects.using(db_slug).filter(excluido=False).all()
    lista_arquivos_esocial_tipos = []
    for a in lista:
        dic = {}
        dic['key'] = a.codigo
        dic['value'] = '%s' % (a)
        lista_arquivos_esocial_tipos.append(dic)
    dicionario['arquivos_esocial_tipos'] = lista_arquivos_esocial_tipos
    return JsonResponse(dicionario)


def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #arquivos_esocial_tipos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='arquivos_esocial_tipos')
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
        arquivos_esocial_tipos_lista = ArquivosEsocialTipos.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(arquivos_esocial_tipos_lista) > 100:
            filtrar = True
            arquivos_esocial_tipos_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #arquivos_esocial_tipos_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'arquivos_esocial_tipos'
        context = {
            'arquivos_esocial_tipos_lista': arquivos_esocial_tipos_lista,

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
            return render(request, 'arquivos_esocial_tipos_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='arquivos_esocial_tipos_listar.html',
                filename="arquivos_esocial_tipos.pdf",
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
            response = render_to_response('arquivos_esocial_tipos_listar.html', context)
            filename = "arquivos_esocial_tipos.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/arquivos_esocial_tipos_csv.html', context)
            filename = "arquivos_esocial_tipos.csv"
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

