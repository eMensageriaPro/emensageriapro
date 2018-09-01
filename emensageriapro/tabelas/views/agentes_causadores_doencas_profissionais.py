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
        agentes_causadores_doencas_profissionais_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='agentes_causadores_doencas_profissionais')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    agentes_causadores_doencas_profissionais = get_object_or_404(AgentesCausadoresDoencasProfissionais.objects.using( db_slug ), excluido = False, id = agentes_causadores_doencas_profissionais_id)
    if request.method == 'POST':
        AgentesCausadoresDoencasProfissionais.objects.using( db_slug ).filter(id = agentes_causadores_doencas_profissionais_id).update(excluido = True)
        #agentes_causadores_doencas_profissionais_apagar_custom
        #agentes_causadores_doencas_profissionais_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'agentes_causadores_doencas_profissionais_salvar':
            return redirect('agentes_causadores_doencas_profissionais', hash=request.session['retorno_hash'])
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
    return render(request, 'agentes_causadores_doencas_profissionais_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        agentes_causadores_doencas_profissionais_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='agentes_causadores_doencas_profissionais')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if agentes_causadores_doencas_profissionais_id:
        agentes_causadores_doencas_profissionais = get_object_or_404(AgentesCausadoresDoencasProfissionais.objects.using( db_slug ), excluido = False, id = agentes_causadores_doencas_profissionais_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if agentes_causadores_doencas_profissionais_id:
            agentes_causadores_doencas_profissionais_form = form_agentes_causadores_doencas_profissionais(request.POST or None, instance = agentes_causadores_doencas_profissionais, slug = db_slug)
        else:
            agentes_causadores_doencas_profissionais_form = form_agentes_causadores_doencas_profissionais(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if agentes_causadores_doencas_profissionais_form.is_valid():
                dados = agentes_causadores_doencas_profissionais_form.cleaned_data
                if agentes_causadores_doencas_profissionais_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #agentes_causadores_doencas_profissionais_campos_multiple_passo1
                    AgentesCausadoresDoencasProfissionais.objects.using(db_slug).filter(id=agentes_causadores_doencas_profissionais_id).update(**dados)
                    obj = AgentesCausadoresDoencasProfissionais.objects.using(db_slug).get(id=agentes_causadores_doencas_profissionais_id)
                    #agentes_causadores_doencas_profissionais_editar_custom
                    #agentes_causadores_doencas_profissionais_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #agentes_causadores_doencas_profissionais_cadastrar_campos_multiple_passo1
                    obj = AgentesCausadoresDoencasProfissionais(**dados)
                    obj.save(using = db_slug)
                    #agentes_causadores_doencas_profissionais_cadastrar_custom
                    #agentes_causadores_doencas_profissionais_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('agentes_causadores_doencas_profissionais_apagar', 'agentes_causadores_doencas_profissionais_salvar', 'agentes_causadores_doencas_profissionais'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if agentes_causadores_doencas_profissionais_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('agentes_causadores_doencas_profissionais_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        agentes_causadores_doencas_profissionais_form = disabled_form_fields(agentes_causadores_doencas_profissionais_form, permissao.permite_editar)
        #agentes_causadores_doencas_profissionais_campos_multiple_passo3

        for field in agentes_causadores_doencas_profissionais_form.fields.keys():
            agentes_causadores_doencas_profissionais_form.fields[field].widget.attrs['ng-model'] = 'agentes_causadores_doencas_profissionais_'+field
        if int(dict_hash['print']):
            agentes_causadores_doencas_profissionais_form = disabled_form_for_print(agentes_causadores_doencas_profissionais_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if agentes_causadores_doencas_profissionais_id:
            agentes_causadores_doencas_profissionais = get_object_or_404(AgentesCausadoresDoencasProfissionais.objects.using( db_slug ), excluido = False, id = agentes_causadores_doencas_profissionais_id)
            pass
        else:
            agentes_causadores_doencas_profissionais = None
        #agentes_causadores_doencas_profissionais_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'agentes_causadores_doencas_profissionais' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'agentes_causadores_doencas_profissionais_salvar'
        context = {
            'agentes_causadores_doencas_profissionais': agentes_causadores_doencas_profissionais,
            'agentes_causadores_doencas_profissionais_form': agentes_causadores_doencas_profissionais_form,
            'mensagem': mensagem,
            'agentes_causadores_doencas_profissionais_id': int(agentes_causadores_doencas_profissionais_id),
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
            #agentes_causadores_doencas_profissionais_salvar_custom_variaveis_context#
        }
        return render(request, 'agentes_causadores_doencas_profissionais_salvar.html', context)
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
            lista = AgentesCausadoresDoencasProfissionais.objects.using(db_slug).filter(excluido = False).filter(query).all()
        except:
            query = reduce(operator.and_, ((Q(descricao__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = AgentesCausadoresDoencasProfissionais.objects.using(db_slug).filter(excluido = False).filter(query).all()
    else:
        lista = AgentesCausadoresDoencasProfissionais.objects.using(db_slug).filter(excluido=False).all()
    lista_agentes_causadores_doencas_profissionais = []
    for a in lista:
        dic = {}
        dic['key'] = a.codigo
        dic['value'] = '%s' % (a)
        lista_agentes_causadores_doencas_profissionais.append(dic)
    dicionario['agentes_causadores_doencas_profissionais'] = lista_agentes_causadores_doencas_profissionais
    return JsonResponse(dicionario)


def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #agentes_causadores_doencas_profissionais_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='agentes_causadores_doencas_profissionais')
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
        agentes_causadores_doencas_profissionais_lista = AgentesCausadoresDoencasProfissionais.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(agentes_causadores_doencas_profissionais_lista) > 100:
            filtrar = True
            agentes_causadores_doencas_profissionais_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #agentes_causadores_doencas_profissionais_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'agentes_causadores_doencas_profissionais'
        context = {
            'agentes_causadores_doencas_profissionais_lista': agentes_causadores_doencas_profissionais_lista,

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
            return render(request, 'agentes_causadores_doencas_profissionais_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='agentes_causadores_doencas_profissionais_listar.html',
                filename="agentes_causadores_doencas_profissionais.pdf",
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
            response = render_to_response('agentes_causadores_doencas_profissionais_listar.html', context)
            filename = "agentes_causadores_doencas_profissionais.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/agentes_causadores_doencas_profissionais_csv.html', context)
            filename = "agentes_causadores_doencas_profissionais.csv"
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

