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
        regras_pagamentos_codigos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='regras_pagamentos_codigos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    regras_pagamentos_codigos = get_object_or_404(RegrasPagamentosCodigos.objects.using( db_slug ), excluido = False, id = regras_pagamentos_codigos_id)
    if request.method == 'POST':
        RegrasPagamentosCodigos.objects.using( db_slug ).filter(id = regras_pagamentos_codigos_id).update(excluido = True)
        #regras_pagamentos_codigos_apagar_custom
        #regras_pagamentos_codigos_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'regras_pagamentos_codigos_salvar':
            return redirect('regras_pagamentos_codigos', hash=request.session['retorno_hash'])
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
    return render(request, 'regras_pagamentos_codigos_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        regras_pagamentos_codigos_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='regras_pagamentos_codigos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if regras_pagamentos_codigos_id:
        regras_pagamentos_codigos = get_object_or_404(RegrasPagamentosCodigos.objects.using( db_slug ), excluido = False, id = regras_pagamentos_codigos_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if regras_pagamentos_codigos_id:
            regras_pagamentos_codigos_form = form_regras_pagamentos_codigos(request.POST or None, instance = regras_pagamentos_codigos, slug = db_slug)
        else:
            regras_pagamentos_codigos_form = form_regras_pagamentos_codigos(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if regras_pagamentos_codigos_form.is_valid():
                dados = regras_pagamentos_codigos_form.cleaned_data
                if regras_pagamentos_codigos_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #regras_pagamentos_codigos_campos_multiple_passo1
                    RegrasPagamentosCodigos.objects.using(db_slug).filter(id=regras_pagamentos_codigos_id).update(**dados)
                    obj = RegrasPagamentosCodigos.objects.using(db_slug).get(id=regras_pagamentos_codigos_id)
                    #regras_pagamentos_codigos_editar_custom
                    #regras_pagamentos_codigos_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #regras_pagamentos_codigos_cadastrar_campos_multiple_passo1
                    obj = RegrasPagamentosCodigos(**dados)
                    obj.save(using = db_slug)
                    #regras_pagamentos_codigos_cadastrar_custom
                    #regras_pagamentos_codigos_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('regras_pagamentos_codigos_apagar', 'regras_pagamentos_codigos_salvar', 'regras_pagamentos_codigos'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if regras_pagamentos_codigos_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('regras_pagamentos_codigos_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        regras_pagamentos_codigos_form = disabled_form_fields(regras_pagamentos_codigos_form, permissao.permite_editar)
        #regras_pagamentos_codigos_campos_multiple_passo3

        for field in regras_pagamentos_codigos_form.fields.keys():
            regras_pagamentos_codigos_form.fields[field].widget.attrs['ng-model'] = 'regras_pagamentos_codigos_'+field
        if int(dict_hash['print']):
            regras_pagamentos_codigos_form = disabled_form_for_print(regras_pagamentos_codigos_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if regras_pagamentos_codigos_id:
            regras_pagamentos_codigos = get_object_or_404(RegrasPagamentosCodigos.objects.using( db_slug ), excluido = False, id = regras_pagamentos_codigos_id)
            pass
        else:
            regras_pagamentos_codigos = None
        #regras_pagamentos_codigos_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'regras_pagamentos_codigos' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'regras_pagamentos_codigos_salvar'
        context = {
            'regras_pagamentos_codigos': regras_pagamentos_codigos,
            'regras_pagamentos_codigos_form': regras_pagamentos_codigos_form,
            'mensagem': mensagem,
            'regras_pagamentos_codigos_id': int(regras_pagamentos_codigos_id),
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
            #regras_pagamentos_codigos_salvar_custom_variaveis_context#
        }
        return render(request, 'regras_pagamentos_codigos_salvar.html', context)
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
            lista = RegrasPagamentosCodigos.objects.using(db_slug).filter(excluido = False).filter(query).all()
        except:
            query = reduce(operator.and_, ((Q(descricao__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = RegrasPagamentosCodigos.objects.using(db_slug).filter(excluido = False).filter(query).all()
    else:
        lista = RegrasPagamentosCodigos.objects.using(db_slug).filter(excluido=False).all()
    lista_regras_pagamentos_codigos = []
    for a in lista:
        dic = {}
        dic['key'] = a.codigo
        dic['value'] = '%s' % (a)
        lista_regras_pagamentos_codigos.append(dic)
    dicionario['regras_pagamentos_codigos'] = lista_regras_pagamentos_codigos
    return JsonResponse(dicionario)


def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #regras_pagamentos_codigos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='regras_pagamentos_codigos')
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
            'show_tributacao_com_exigibilidade_suspensa': 1,
            'show_compensacao_imposto_por_decisao_judicial': 1,
            'show_rendimentos_isentos': 1,
            'show_deducoes': 1,
            'show_decimo_terceiro': 1,
            'show_descricao': 0,
            'show_codigo': 1,
            'show_classificacao': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'tributacao_com_exigibilidade_suspensa__icontains': 'tributacao_com_exigibilidade_suspensa__icontains',
                'compensacao_imposto_por_decisao_judicial__icontains': 'compensacao_imposto_por_decisao_judicial__icontains',
                'rendimentos_isentos__icontains': 'rendimentos_isentos__icontains',
                'deducoes__icontains': 'deducoes__icontains',
                'decimo_terceiro__icontains': 'decimo_terceiro__icontains',
                'codigo__icontains': 'codigo__icontains',
                'classificacao': 'classificacao',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'tributacao_com_exigibilidade_suspensa__icontains': 'tributacao_com_exigibilidade_suspensa__icontains',
                'compensacao_imposto_por_decisao_judicial__icontains': 'compensacao_imposto_por_decisao_judicial__icontains',
                'rendimentos_isentos__icontains': 'rendimentos_isentos__icontains',
                'deducoes__icontains': 'deducoes__icontains',
                'decimo_terceiro__icontains': 'decimo_terceiro__icontains',
                'codigo__icontains': 'codigo__icontains',
                'classificacao': 'classificacao',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        regras_pagamentos_codigos_lista = RegrasPagamentosCodigos.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(regras_pagamentos_codigos_lista) > 100:
            filtrar = True
            regras_pagamentos_codigos_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #regras_pagamentos_codigos_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'regras_pagamentos_codigos'
        context = {
            'regras_pagamentos_codigos_lista': regras_pagamentos_codigos_lista,

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
            return render(request, 'regras_pagamentos_codigos_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='regras_pagamentos_codigos_listar.html',
                filename="regras_pagamentos_codigos.pdf",
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
            response = render_to_response('regras_pagamentos_codigos_listar.html', context)
            filename = "regras_pagamentos_codigos.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/regras_pagamentos_codigos_csv.html', context)
            filename = "regras_pagamentos_codigos.csv"
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

