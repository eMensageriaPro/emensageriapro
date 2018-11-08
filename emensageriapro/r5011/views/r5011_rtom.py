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
from emensageriapro.r5011.forms import *
from emensageriapro.r5011.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r5011_rtom_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r5011_rtom')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if r5011_rtom_id:
        r5011_rtom = get_object_or_404(r5011RTom.objects.using( db_slug ), excluido = False, id = r5011_rtom_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if r5011_rtom_id:
        dados_evento = r5011_rtom.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r5011_rtom_apagar'] = 0
            dict_permissoes['r5011_rtom_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r5011_rtom_id:
            r5011_rtom_form = form_r5011_rtom(request.POST or None, instance = r5011_rtom, slug = db_slug)
        else:
            r5011_rtom_form = form_r5011_rtom(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if r5011_rtom_form.is_valid():
                dados = r5011_rtom_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if r5011_rtom_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #r5011_rtom_campos_multiple_passo1
                        r5011RTom.objects.using(db_slug).filter(id=r5011_rtom_id).update(**dados)
                        obj = r5011RTom.objects.using(db_slug).get(id=r5011_rtom_id)
                        #r5011_rtom_editar_custom
                        #r5011_rtom_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(r5011_rtom), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         'r5011_rtom', r5011_rtom_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #r5011_rtom_cadastrar_campos_multiple_passo1
                    obj = r5011RTom(**dados)
                    obj.save(using = db_slug)
                    #r5011_rtom_cadastrar_custom
                    #r5011_rtom_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r5011_rtom', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('r5011_rtom_apagar', 'r5011_rtom_salvar', 'r5011_rtom'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if r5011_rtom_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('r5011_rtom_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        r5011_rtom_form = disabled_form_fields(r5011_rtom_form, permissao.permite_editar)
        if r5011_rtom_id:
            if dados_evento['status'] != 0:
                r5011_rtom_form = disabled_form_fields(r5011_rtom_form, 0)
        #r5011_rtom_campos_multiple_passo3

        for field in r5011_rtom_form.fields.keys():
            r5011_rtom_form.fields[field].widget.attrs['ng-model'] = 'r5011_rtom_'+field
        if int(dict_hash['print']):
            r5011_rtom_form = disabled_form_for_print(r5011_rtom_form)

        r5011_infocrtom_form = None
        r5011_infocrtom_lista = None
        if r5011_rtom_id:
            r5011_rtom = get_object_or_404(r5011RTom.objects.using( db_slug ), excluido = False, id = r5011_rtom_id)
  
            r5011_infocrtom_form = form_r5011_infocrtom(initial={ 'r5011_rtom': r5011_rtom }, slug=db_slug)
            r5011_infocrtom_form.fields['r5011_rtom'].widget.attrs['readonly'] = True
            r5011_infocrtom_lista = r5011infoCRTom.objects.using( db_slug ).filter(excluido = False, r5011_rtom_id=r5011_rtom.id).all()
        else:
            r5011_rtom = None
        #r5011_rtom_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'r5011_rtom' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r5011_rtom_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r5011_rtom_id, tabela='r5011_rtom').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            'r5011_rtom': r5011_rtom,
            'r5011_rtom_form': r5011_rtom_form,
            'mensagem': mensagem,
            'r5011_rtom_id': int(r5011_rtom_id),
            'usuario': usuario,
       
            'hash': hash,
  
            'r5011_infocrtom_form': r5011_infocrtom_form,
            'r5011_infocrtom_lista': r5011_infocrtom_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r5011_rtom_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'r5011_rtom_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r5011_rtom_salvar.html',
                filename="r5011_rtom.pdf",
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
            response = render_to_response('r5011_rtom_salvar.html', context)
            filename = "r5011_rtom.xls"
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
        r5011_rtom_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r5011_rtom')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r5011_rtom = get_object_or_404(r5011RTom.objects.using( db_slug ), excluido = False, id = r5011_rtom_id)
    dados_evento = {}
    if r5011_rtom_id:
        dados_evento = r5011_rtom.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r5011_rtom_apagar'] = 0
            dict_permissoes['r5011_rtom_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r5011_rtom), indent=4, sort_keys=True, default=str)
            r5011RTom.objects.using( db_slug ).filter(id = r5011_rtom_id).delete()
            #r5011_rtom_apagar_custom
            #r5011_rtom_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r5011_rtom', r5011_rtom_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
   
        if request.session['retorno_pagina']== 'r5011_rtom_salvar':
            return redirect('r5011_rtom', hash=request.session['retorno_hash'])
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
    return render(request, 'r5011_rtom_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class r5011RTomList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = r5011RTom.objects.using(db_slug).all()
    serializer_class = r5011RTomSerializer
    permission_classes = (IsAdminUser,)


class r5011RTomDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = r5011RTom.objects.using(db_slug).all()
    serializer_class = r5011RTomSerializer
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
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #r5011_rtom_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r5011_rtom')
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
            'show_vlrtotalbaseret': 1,
            'show_cnpjprestador': 1,
            'show_r5011_infototalcontrib': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'vlrtotalbaseret': 'vlrtotalbaseret',
                'cnpjprestador__icontains': 'cnpjprestador__icontains',
                'r5011_infototalcontrib': 'r5011_infototalcontrib',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'vlrtotalbaseret': 'vlrtotalbaseret',
                'cnpjprestador__icontains': 'cnpjprestador__icontains',
                'r5011_infototalcontrib': 'r5011_infototalcontrib',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r5011_rtom_lista = r5011RTom.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r5011_rtom_lista) > 100:
            filtrar = True
            r5011_rtom_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #r5011_rtom_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r5011_rtom'
        context = {
            'r5011_rtom_lista': r5011_rtom_lista,
       
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
            return render(request, 'r5011_rtom_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r5011_rtom_listar.html',
                filename="r5011_rtom.pdf",
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
            response = render_to_response('r5011_rtom_listar.html', context)
            filename = "r5011_rtom.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/r5011_rtom_csv.html', context)
            filename = "r5011_rtom.csv"
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

