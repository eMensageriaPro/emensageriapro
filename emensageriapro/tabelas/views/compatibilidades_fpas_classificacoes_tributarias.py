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
        compatibilidades_fpas_classificacoes_tributarias_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='compatibilidades_fpas_classificacoes_tributarias')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    compatibilidades_fpas_classificacoes_tributarias = get_object_or_404(CompatibilidadesFPASClassificacoesTributarias.objects.using( db_slug ), excluido = False, id = compatibilidades_fpas_classificacoes_tributarias_id)
    if request.method == 'POST':
        CompatibilidadesFPASClassificacoesTributarias.objects.using( db_slug ).filter(id = compatibilidades_fpas_classificacoes_tributarias_id).update(excluido = True)
        #compatibilidades_fpas_classificacoes_tributarias_apagar_custom
        #compatibilidades_fpas_classificacoes_tributarias_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'compatibilidades_fpas_classificacoes_tributarias_salvar':
            return redirect('compatibilidades_fpas_classificacoes_tributarias', hash=request.session['retorno_hash'])
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
    return render(request, 'compatibilidades_fpas_classificacoes_tributarias_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        compatibilidades_fpas_classificacoes_tributarias_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='compatibilidades_fpas_classificacoes_tributarias')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if compatibilidades_fpas_classificacoes_tributarias_id:
        compatibilidades_fpas_classificacoes_tributarias = get_object_or_404(CompatibilidadesFPASClassificacoesTributarias.objects.using( db_slug ), excluido = False, id = compatibilidades_fpas_classificacoes_tributarias_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if compatibilidades_fpas_classificacoes_tributarias_id:
            compatibilidades_fpas_classificacoes_tributarias_form = form_compatibilidades_fpas_classificacoes_tributarias(request.POST or None, instance = compatibilidades_fpas_classificacoes_tributarias, slug = db_slug)
        else:
            compatibilidades_fpas_classificacoes_tributarias_form = form_compatibilidades_fpas_classificacoes_tributarias(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if compatibilidades_fpas_classificacoes_tributarias_form.is_valid():
                dados = compatibilidades_fpas_classificacoes_tributarias_form.cleaned_data
                if compatibilidades_fpas_classificacoes_tributarias_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #compatibilidades_fpas_classificacoes_tributarias_campos_multiple_passo1
                    CompatibilidadesFPASClassificacoesTributarias.objects.using(db_slug).filter(id=compatibilidades_fpas_classificacoes_tributarias_id).update(**dados)
                    obj = CompatibilidadesFPASClassificacoesTributarias.objects.using(db_slug).get(id=compatibilidades_fpas_classificacoes_tributarias_id)
                    #compatibilidades_fpas_classificacoes_tributarias_editar_custom
                    #compatibilidades_fpas_classificacoes_tributarias_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #compatibilidades_fpas_classificacoes_tributarias_cadastrar_campos_multiple_passo1
                    obj = CompatibilidadesFPASClassificacoesTributarias(**dados)
                    obj.save(using = db_slug)
                    #compatibilidades_fpas_classificacoes_tributarias_cadastrar_custom
                    #compatibilidades_fpas_classificacoes_tributarias_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('compatibilidades_fpas_classificacoes_tributarias_apagar', 'compatibilidades_fpas_classificacoes_tributarias_salvar', 'compatibilidades_fpas_classificacoes_tributarias'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if compatibilidades_fpas_classificacoes_tributarias_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('compatibilidades_fpas_classificacoes_tributarias_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        compatibilidades_fpas_classificacoes_tributarias_form = disabled_form_fields(compatibilidades_fpas_classificacoes_tributarias_form, permissao.permite_editar)
        #compatibilidades_fpas_classificacoes_tributarias_campos_multiple_passo3

        for field in compatibilidades_fpas_classificacoes_tributarias_form.fields.keys():
            compatibilidades_fpas_classificacoes_tributarias_form.fields[field].widget.attrs['ng-model'] = 'compatibilidades_fpas_classificacoes_tributarias_'+field
        if int(dict_hash['print']):
            compatibilidades_fpas_classificacoes_tributarias_form = disabled_form_for_print(compatibilidades_fpas_classificacoes_tributarias_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if compatibilidades_fpas_classificacoes_tributarias_id:
            compatibilidades_fpas_classificacoes_tributarias = get_object_or_404(CompatibilidadesFPASClassificacoesTributarias.objects.using( db_slug ), excluido = False, id = compatibilidades_fpas_classificacoes_tributarias_id)
            pass
        else:
            compatibilidades_fpas_classificacoes_tributarias = None
        #compatibilidades_fpas_classificacoes_tributarias_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'compatibilidades_fpas_classificacoes_tributarias' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'compatibilidades_fpas_classificacoes_tributarias_salvar'
        context = {
            'compatibilidades_fpas_classificacoes_tributarias': compatibilidades_fpas_classificacoes_tributarias,
            'compatibilidades_fpas_classificacoes_tributarias_form': compatibilidades_fpas_classificacoes_tributarias_form,
            'mensagem': mensagem,
            'compatibilidades_fpas_classificacoes_tributarias_id': int(compatibilidades_fpas_classificacoes_tributarias_id),
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
            #compatibilidades_fpas_classificacoes_tributarias_salvar_custom_variaveis_context#
        }
        return render(request, 'compatibilidades_fpas_classificacoes_tributarias_salvar.html', context)
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
            lista = CompatibilidadesFPASClassificacoesTributarias.objects.using(db_slug).filter(excluido = False).filter(query).all()
        except:
            query = reduce(operator.and_, ((Q(descricao__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = CompatibilidadesFPASClassificacoesTributarias.objects.using(db_slug).filter(excluido = False).filter(query).all()
    else:
        lista = CompatibilidadesFPASClassificacoesTributarias.objects.using(db_slug).filter(excluido=False).all()
    lista_compatibilidades_fpas_classificacoes_tributarias = []
    for a in lista:
        dic = {}
        dic['key'] = a.codigo
        dic['value'] = '%s' % (a)
        lista_compatibilidades_fpas_classificacoes_tributarias.append(dic)
    dicionario['compatibilidades_fpas_classificacoes_tributarias'] = lista_compatibilidades_fpas_classificacoes_tributarias
    return JsonResponse(dicionario)


def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #compatibilidades_fpas_classificacoes_tributarias_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='compatibilidades_fpas_classificacoes_tributarias')
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
            'show_classificacao_tributaria_99': 1,
            'show_classificacao_tributaria_85': 1,
            'show_classificacao_tributaria_80': 1,
            'show_classificacao_tributaria_70': 1,
            'show_classificacao_tributaria_60': 1,
            'show_classificacao_tributaria_22': 1,
            'show_classificacao_tributaria_21': 1,
            'show_classificacao_tributaria_14': 1,
            'show_classificacao_tributaria_13': 1,
            'show_classificacao_tributaria_11': 1,
            'show_classificacao_tributaria_10': 1,
            'show_classificacao_tributaria_09': 1,
            'show_classificacao_tributaria_08': 1,
            'show_classificacao_tributaria_07': 1,
            'show_classificacao_tributaria_06': 1,
            'show_classificacao_tributaria_04': 1,
            'show_classificacao_tributaria_03': 1,
            'show_classificacao_tributaria_02': 1,
            'show_classificacao_tributaria_01': 1,
            'show_codigo': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'classificacao_tributaria_99__icontains': 'classificacao_tributaria_99__icontains',
                'classificacao_tributaria_85__icontains': 'classificacao_tributaria_85__icontains',
                'classificacao_tributaria_80__icontains': 'classificacao_tributaria_80__icontains',
                'classificacao_tributaria_70__icontains': 'classificacao_tributaria_70__icontains',
                'classificacao_tributaria_60__icontains': 'classificacao_tributaria_60__icontains',
                'classificacao_tributaria_22__icontains': 'classificacao_tributaria_22__icontains',
                'classificacao_tributaria_21__icontains': 'classificacao_tributaria_21__icontains',
                'classificacao_tributaria_14__icontains': 'classificacao_tributaria_14__icontains',
                'classificacao_tributaria_13__icontains': 'classificacao_tributaria_13__icontains',
                'classificacao_tributaria_11__icontains': 'classificacao_tributaria_11__icontains',
                'classificacao_tributaria_10__icontains': 'classificacao_tributaria_10__icontains',
                'classificacao_tributaria_09__icontains': 'classificacao_tributaria_09__icontains',
                'classificacao_tributaria_08__icontains': 'classificacao_tributaria_08__icontains',
                'classificacao_tributaria_07__icontains': 'classificacao_tributaria_07__icontains',
                'classificacao_tributaria_06__icontains': 'classificacao_tributaria_06__icontains',
                'classificacao_tributaria_04__icontains': 'classificacao_tributaria_04__icontains',
                'classificacao_tributaria_03__icontains': 'classificacao_tributaria_03__icontains',
                'classificacao_tributaria_02__icontains': 'classificacao_tributaria_02__icontains',
                'classificacao_tributaria_01__icontains': 'classificacao_tributaria_01__icontains',
                'codigo__icontains': 'codigo__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'classificacao_tributaria_99__icontains': 'classificacao_tributaria_99__icontains',
                'classificacao_tributaria_85__icontains': 'classificacao_tributaria_85__icontains',
                'classificacao_tributaria_80__icontains': 'classificacao_tributaria_80__icontains',
                'classificacao_tributaria_70__icontains': 'classificacao_tributaria_70__icontains',
                'classificacao_tributaria_60__icontains': 'classificacao_tributaria_60__icontains',
                'classificacao_tributaria_22__icontains': 'classificacao_tributaria_22__icontains',
                'classificacao_tributaria_21__icontains': 'classificacao_tributaria_21__icontains',
                'classificacao_tributaria_14__icontains': 'classificacao_tributaria_14__icontains',
                'classificacao_tributaria_13__icontains': 'classificacao_tributaria_13__icontains',
                'classificacao_tributaria_11__icontains': 'classificacao_tributaria_11__icontains',
                'classificacao_tributaria_10__icontains': 'classificacao_tributaria_10__icontains',
                'classificacao_tributaria_09__icontains': 'classificacao_tributaria_09__icontains',
                'classificacao_tributaria_08__icontains': 'classificacao_tributaria_08__icontains',
                'classificacao_tributaria_07__icontains': 'classificacao_tributaria_07__icontains',
                'classificacao_tributaria_06__icontains': 'classificacao_tributaria_06__icontains',
                'classificacao_tributaria_04__icontains': 'classificacao_tributaria_04__icontains',
                'classificacao_tributaria_03__icontains': 'classificacao_tributaria_03__icontains',
                'classificacao_tributaria_02__icontains': 'classificacao_tributaria_02__icontains',
                'classificacao_tributaria_01__icontains': 'classificacao_tributaria_01__icontains',
                'codigo__icontains': 'codigo__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        compatibilidades_fpas_classificacoes_tributarias_lista = CompatibilidadesFPASClassificacoesTributarias.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(compatibilidades_fpas_classificacoes_tributarias_lista) > 100:
            filtrar = True
            compatibilidades_fpas_classificacoes_tributarias_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #compatibilidades_fpas_classificacoes_tributarias_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'compatibilidades_fpas_classificacoes_tributarias'
        context = {
            'compatibilidades_fpas_classificacoes_tributarias_lista': compatibilidades_fpas_classificacoes_tributarias_lista,

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
            return render(request, 'compatibilidades_fpas_classificacoes_tributarias_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='compatibilidades_fpas_classificacoes_tributarias_listar.html',
                filename="compatibilidades_fpas_classificacoes_tributarias.pdf",
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
            response = render_to_response('compatibilidades_fpas_classificacoes_tributarias_listar.html', context)
            filename = "compatibilidades_fpas_classificacoes_tributarias.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/compatibilidades_fpas_classificacoes_tributarias_csv.html', context)
            filename = "compatibilidades_fpas_classificacoes_tributarias.csv"
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

