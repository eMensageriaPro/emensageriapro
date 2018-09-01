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
from emensageriapro.r2020.forms import *
from emensageriapro.r2020.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        r2020_infoprocretad_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2020_infoprocretad')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if r2020_infoprocretad_id:
        r2020_infoprocretad = get_object_or_404(r2020infoProcRetAd.objects.using( db_slug ), excluido = False, id = r2020_infoprocretad_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if r2020_infoprocretad_id:
        dados_evento = r2020_infoprocretad.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r2020_infoprocretad_apagar'] = 0
            dict_permissoes['r2020_infoprocretad_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r2020_infoprocretad_id:
            r2020_infoprocretad_form = form_r2020_infoprocretad(request.POST or None, instance = r2020_infoprocretad, slug = db_slug)
        else:
            r2020_infoprocretad_form = form_r2020_infoprocretad(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if r2020_infoprocretad_form.is_valid():
                dados = r2020_infoprocretad_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if r2020_infoprocretad_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #r2020_infoprocretad_campos_multiple_passo1
                        r2020infoProcRetAd.objects.using(db_slug).filter(id=r2020_infoprocretad_id).update(**dados)
                        obj = r2020infoProcRetAd.objects.using(db_slug).get(id=r2020_infoprocretad_id)
                        #r2020_infoprocretad_editar_custom
                        #r2020_infoprocretad_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(r2020_infoprocretad), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         'r2020_infoprocretad', r2020_infoprocretad_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #r2020_infoprocretad_cadastrar_campos_multiple_passo1
                    obj = r2020infoProcRetAd(**dados)
                    obj.save(using = db_slug)
                    #r2020_infoprocretad_cadastrar_custom
                    #r2020_infoprocretad_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r2020_infoprocretad', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('r2020_infoprocretad_apagar', 'r2020_infoprocretad_salvar', 'r2020_infoprocretad'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if r2020_infoprocretad_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('r2020_infoprocretad_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        r2020_infoprocretad_form = disabled_form_fields(r2020_infoprocretad_form, permissao.permite_editar)
        if r2020_infoprocretad_id:
            if dados_evento['status'] != 0:
                r2020_infoprocretad_form = disabled_form_fields(r2020_infoprocretad_form, 0)
        #r2020_infoprocretad_campos_multiple_passo3

        for field in r2020_infoprocretad_form.fields.keys():
            r2020_infoprocretad_form.fields[field].widget.attrs['ng-model'] = 'r2020_infoprocretad_'+field
        if int(dict_hash['print']):
            r2020_infoprocretad_form = disabled_form_for_print(r2020_infoprocretad_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if r2020_infoprocretad_id:
            r2020_infoprocretad = get_object_or_404(r2020infoProcRetAd.objects.using( db_slug ), excluido = False, id = r2020_infoprocretad_id)
            pass
        else:
            r2020_infoprocretad = None
        #r2020_infoprocretad_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'r2020_infoprocretad' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r2020_infoprocretad_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r2020_infoprocretad_id, tabela='r2020_infoprocretad').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            'r2020_infoprocretad': r2020_infoprocretad,
            'r2020_infoprocretad_form': r2020_infoprocretad_form,
            'mensagem': mensagem,
            'r2020_infoprocretad_id': int(r2020_infoprocretad_id),
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
            #r2020_infoprocretad_salvar_custom_variaveis_context#
        }
        return render(request, 'r2020_infoprocretad_salvar.html', context)
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

def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        r2020_infoprocretad_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2020_infoprocretad')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r2020_infoprocretad = get_object_or_404(r2020infoProcRetAd.objects.using( db_slug ), excluido = False, id = r2020_infoprocretad_id)
    dados_evento = {}
    if r2020_infoprocretad_id:
        dados_evento = r2020_infoprocretad.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r2020_infoprocretad_apagar'] = 0
            dict_permissoes['r2020_infoprocretad_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r2020_infoprocretad), indent=4, sort_keys=True, default=str)
            r2020infoProcRetAd.objects.using( db_slug ).filter(id = r2020_infoprocretad_id).delete()
            #r2020_infoprocretad_apagar_custom
            #r2020_infoprocretad_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r2020_infoprocretad', r2020_infoprocretad_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 'r2020_infoprocretad_salvar':
            return redirect('r2020_infoprocretad', hash=request.session['retorno_hash'])
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
    return render(request, 'r2020_infoprocretad_apagar.html', context)

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

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #r2020_infoprocretad_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2020_infoprocretad')
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
            'show_valoradic': 1,
            'show_codsuspadic': 0,
            'show_nrprocretadic': 1,
            'show_tpprocretadic': 1,
            'show_r2020_evtservprest': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'valoradic': 'valoradic',
                'codsuspadic': 'codsuspadic',
                'nrprocretadic__icontains': 'nrprocretadic__icontains',
                'tpprocretadic': 'tpprocretadic',
                'r2020_evtservprest': 'r2020_evtservprest',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'valoradic': 'valoradic',
                'codsuspadic': 'codsuspadic',
                'nrprocretadic__icontains': 'nrprocretadic__icontains',
                'tpprocretadic': 'tpprocretadic',
                'r2020_evtservprest': 'r2020_evtservprest',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r2020_infoprocretad_lista = r2020infoProcRetAd.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r2020_infoprocretad_lista) > 100:
            filtrar = True
            r2020_infoprocretad_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #r2020_infoprocretad_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r2020_infoprocretad'
        context = {
            'r2020_infoprocretad_lista': r2020_infoprocretad_lista,

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
            return render(request, 'r2020_infoprocretad_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2020_infoprocretad_listar.html',
                filename="r2020_infoprocretad.pdf",
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
            response = render_to_response('r2020_infoprocretad_listar.html', context)
            filename = "r2020_infoprocretad.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/r2020_infoprocretad_csv.html', context)
            filename = "r2020_infoprocretad.csv"
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

