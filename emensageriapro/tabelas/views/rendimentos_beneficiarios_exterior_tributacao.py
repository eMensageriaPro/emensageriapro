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
        rendimentos_beneficiarios_exterior_tributacao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='rendimentos_beneficiarios_exterior_tributacao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    rendimentos_beneficiarios_exterior_tributacao = get_object_or_404(RendimentosBeneficiariosExteriorTributacao.objects.using( db_slug ), excluido = False, id = rendimentos_beneficiarios_exterior_tributacao_id)
    if request.method == 'POST':
        RendimentosBeneficiariosExteriorTributacao.objects.using( db_slug ).filter(id = rendimentos_beneficiarios_exterior_tributacao_id).update(excluido = True)
        #rendimentos_beneficiarios_exterior_tributacao_apagar_custom
        #rendimentos_beneficiarios_exterior_tributacao_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'rendimentos_beneficiarios_exterior_tributacao_salvar':
            return redirect('rendimentos_beneficiarios_exterior_tributacao', hash=request.session['retorno_hash'])
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
    return render(request, 'rendimentos_beneficiarios_exterior_tributacao_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        rendimentos_beneficiarios_exterior_tributacao_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='rendimentos_beneficiarios_exterior_tributacao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if rendimentos_beneficiarios_exterior_tributacao_id:
        rendimentos_beneficiarios_exterior_tributacao = get_object_or_404(RendimentosBeneficiariosExteriorTributacao.objects.using( db_slug ), excluido = False, id = rendimentos_beneficiarios_exterior_tributacao_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if rendimentos_beneficiarios_exterior_tributacao_id:
            rendimentos_beneficiarios_exterior_tributacao_form = form_rendimentos_beneficiarios_exterior_tributacao(request.POST or None, instance = rendimentos_beneficiarios_exterior_tributacao, slug = db_slug)
        else:
            rendimentos_beneficiarios_exterior_tributacao_form = form_rendimentos_beneficiarios_exterior_tributacao(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if rendimentos_beneficiarios_exterior_tributacao_form.is_valid():
                dados = rendimentos_beneficiarios_exterior_tributacao_form.cleaned_data
                if rendimentos_beneficiarios_exterior_tributacao_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #rendimentos_beneficiarios_exterior_tributacao_campos_multiple_passo1
                    RendimentosBeneficiariosExteriorTributacao.objects.using(db_slug).filter(id=rendimentos_beneficiarios_exterior_tributacao_id).update(**dados)
                    obj = RendimentosBeneficiariosExteriorTributacao.objects.using(db_slug).get(id=rendimentos_beneficiarios_exterior_tributacao_id)
                    #rendimentos_beneficiarios_exterior_tributacao_editar_custom
                    #rendimentos_beneficiarios_exterior_tributacao_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #rendimentos_beneficiarios_exterior_tributacao_cadastrar_campos_multiple_passo1
                    obj = RendimentosBeneficiariosExteriorTributacao(**dados)
                    obj.save(using = db_slug)
                    #rendimentos_beneficiarios_exterior_tributacao_cadastrar_custom
                    #rendimentos_beneficiarios_exterior_tributacao_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('rendimentos_beneficiarios_exterior_tributacao_apagar', 'rendimentos_beneficiarios_exterior_tributacao_salvar', 'rendimentos_beneficiarios_exterior_tributacao'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if rendimentos_beneficiarios_exterior_tributacao_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('rendimentos_beneficiarios_exterior_tributacao_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        rendimentos_beneficiarios_exterior_tributacao_form = disabled_form_fields(rendimentos_beneficiarios_exterior_tributacao_form, permissao.permite_editar)
        #rendimentos_beneficiarios_exterior_tributacao_campos_multiple_passo3

        for field in rendimentos_beneficiarios_exterior_tributacao_form.fields.keys():
            rendimentos_beneficiarios_exterior_tributacao_form.fields[field].widget.attrs['ng-model'] = 'rendimentos_beneficiarios_exterior_tributacao_'+field
        if int(dict_hash['print']):
            rendimentos_beneficiarios_exterior_tributacao_form = disabled_form_for_print(rendimentos_beneficiarios_exterior_tributacao_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if rendimentos_beneficiarios_exterior_tributacao_id:
            rendimentos_beneficiarios_exterior_tributacao = get_object_or_404(RendimentosBeneficiariosExteriorTributacao.objects.using( db_slug ), excluido = False, id = rendimentos_beneficiarios_exterior_tributacao_id)
            pass
        else:
            rendimentos_beneficiarios_exterior_tributacao = None
        #rendimentos_beneficiarios_exterior_tributacao_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'rendimentos_beneficiarios_exterior_tributacao' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'rendimentos_beneficiarios_exterior_tributacao_salvar'
        context = {
            'rendimentos_beneficiarios_exterior_tributacao': rendimentos_beneficiarios_exterior_tributacao,
            'rendimentos_beneficiarios_exterior_tributacao_form': rendimentos_beneficiarios_exterior_tributacao_form,
            'mensagem': mensagem,
            'rendimentos_beneficiarios_exterior_tributacao_id': int(rendimentos_beneficiarios_exterior_tributacao_id),
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
            #rendimentos_beneficiarios_exterior_tributacao_salvar_custom_variaveis_context#
        }
        return render(request, 'rendimentos_beneficiarios_exterior_tributacao_salvar.html', context)
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
            lista = RendimentosBeneficiariosExteriorTributacao.objects.using(db_slug).filter(excluido = False).filter(query).all()
        except:
            query = reduce(operator.and_, ((Q(descricao__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = RendimentosBeneficiariosExteriorTributacao.objects.using(db_slug).filter(excluido = False).filter(query).all()
    else:
        lista = RendimentosBeneficiariosExteriorTributacao.objects.using(db_slug).filter(excluido=False).all()
    lista_rendimentos_beneficiarios_exterior_tributacao = []
    for a in lista:
        dic = {}
        dic['key'] = a.codigo
        dic['value'] = '%s' % (a)
        lista_rendimentos_beneficiarios_exterior_tributacao.append(dic)
    dicionario['rendimentos_beneficiarios_exterior_tributacao'] = lista_rendimentos_beneficiarios_exterior_tributacao
    return JsonResponse(dicionario)


def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #rendimentos_beneficiarios_exterior_tributacao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='rendimentos_beneficiarios_exterior_tributacao')
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
        rendimentos_beneficiarios_exterior_tributacao_lista = RendimentosBeneficiariosExteriorTributacao.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(rendimentos_beneficiarios_exterior_tributacao_lista) > 100:
            filtrar = True
            rendimentos_beneficiarios_exterior_tributacao_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #rendimentos_beneficiarios_exterior_tributacao_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'rendimentos_beneficiarios_exterior_tributacao'
        context = {
            'rendimentos_beneficiarios_exterior_tributacao_lista': rendimentos_beneficiarios_exterior_tributacao_lista,

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
            return render(request, 'rendimentos_beneficiarios_exterior_tributacao_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='rendimentos_beneficiarios_exterior_tributacao_listar.html',
                filename="rendimentos_beneficiarios_exterior_tributacao.pdf",
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
            response = render_to_response('rendimentos_beneficiarios_exterior_tributacao_listar.html', context)
            filename = "rendimentos_beneficiarios_exterior_tributacao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/rendimentos_beneficiarios_exterior_tributacao_csv.html', context)
            filename = "rendimentos_beneficiarios_exterior_tributacao.csv"
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

