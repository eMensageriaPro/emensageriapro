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
from emensageriapro.s2400.forms import *
from emensageriapro.s2400.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2400_endereco_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2400_endereco')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2400_endereco = get_object_or_404(s2400endereco.objects.using( db_slug ), excluido = False, id = s2400_endereco_id)
    dados_evento = {}
    if s2400_endereco_id:
        dados_evento = s2400_endereco.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s2400_endereco_apagar'] = 0
            dict_permissoes['s2400_endereco_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2400_endereco), indent=4, sort_keys=True, default=str)
            s2400endereco.objects.using( db_slug ).filter(id = s2400_endereco_id).delete()
            #s2400_endereco_apagar_custom
            #s2400_endereco_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2400_endereco', s2400_endereco_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's2400_endereco_salvar':
            return redirect('s2400_endereco', hash=request.session['retorno_hash'])
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
    return render(request, 's2400_endereco_apagar.html', context)

@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2400_endereco_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2400_endereco')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2400_endereco_id:
        s2400_endereco = get_object_or_404(s2400endereco.objects.using( db_slug ), excluido = False, id = s2400_endereco_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if s2400_endereco_id:
        dados_evento = s2400_endereco.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s2400_endereco_apagar'] = 0
            dict_permissoes['s2400_endereco_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2400_endereco_id:
            s2400_endereco_form = form_s2400_endereco(request.POST or None, instance = s2400_endereco, slug = db_slug)
        else:
            s2400_endereco_form = form_s2400_endereco(request.POST or None, slug = db_slug, initial={'s2400_evtcdbenefin': '1'})
        if request.method == 'POST':
            if s2400_endereco_form.is_valid():
                dados = s2400_endereco_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s2400_endereco_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s2400_endereco_campos_multiple_passo1
                        s2400endereco.objects.using(db_slug).filter(id=s2400_endereco_id).update(**dados)
                        obj = s2400endereco.objects.using(db_slug).get(id=s2400_endereco_id)
                        #s2400_endereco_editar_custom
                        #s2400_endereco_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s2400_endereco), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's2400_endereco', s2400_endereco_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s2400_endereco_cadastrar_campos_multiple_passo1
                    obj = s2400endereco(**dados)
                    obj.save(using = db_slug)
                    #s2400_endereco_cadastrar_custom
                    #s2400_endereco_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2400_endereco', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('s2400_endereco_apagar', 's2400_endereco_salvar', 's2400_endereco'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if s2400_endereco_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('s2400_endereco_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s2400_endereco_form = disabled_form_fields(s2400_endereco_form, permissao.permite_editar)
        if s2400_endereco_id:
            if dados_evento['status'] != 0:
                s2400_endereco_form = disabled_form_fields(s2400_endereco_form, 0)
        #s2400_endereco_campos_multiple_passo3

        for field in s2400_endereco_form.fields.keys():
            s2400_endereco_form.fields[field].widget.attrs['ng-model'] = 's2400_endereco_'+field
        if int(dict_hash['print']):
            s2400_endereco_form = disabled_form_for_print(s2400_endereco_form)

        s2400_brasil_form = None
        s2400_brasil_lista = None
        s2400_exterior_form = None
        s2400_exterior_lista = None
        if s2400_endereco_id:
            s2400_endereco = get_object_or_404(s2400endereco.objects.using( db_slug ), excluido = False, id = s2400_endereco_id)

            s2400_brasil_form = form_s2400_brasil(initial={ 's2400_endereco': s2400_endereco , 's2400_endereco': '1'}, slug=db_slug)
            s2400_brasil_form.fields['s2400_endereco'].widget.attrs['readonly'] = True
            s2400_brasil_lista = s2400brasil.objects.using( db_slug ).filter(excluido = False, s2400_endereco_id=s2400_endereco.id).all()
            s2400_exterior_form = form_s2400_exterior(initial={ 's2400_endereco': s2400_endereco , 's2400_endereco': '1'}, slug=db_slug)
            s2400_exterior_form.fields['s2400_endereco'].widget.attrs['readonly'] = True
            s2400_exterior_lista = s2400exterior.objects.using( db_slug ).filter(excluido = False, s2400_endereco_id=s2400_endereco.id).all()
        else:
            s2400_endereco = None
        #s2400_endereco_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's2400_endereco' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2400_endereco_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2400_endereco_id, tabela='s2400_endereco').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's2400_endereco': s2400_endereco,
            's2400_endereco_form': s2400_endereco_form,
            'mensagem': mensagem,
            's2400_endereco_id': int(s2400_endereco_id),
            'usuario': usuario,

            'hash': hash,

            's2400_brasil_form': s2400_brasil_form,
            's2400_brasil_lista': s2400_brasil_lista,
            's2400_exterior_form': s2400_exterior_form,
            's2400_exterior_lista': s2400_exterior_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2400_endereco_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's2400_endereco_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2400_endereco_salvar.html',
                filename="s2400_endereco.pdf",
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
            response = render_to_response('s2400_endereco_salvar.html', context)
            filename = "s2400_endereco.xls"
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


class s2400enderecoList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s2400endereco.objects.using(db_slug).all()
    serializer_class = s2400enderecoSerializer
    permission_classes = (IsAdminUser,)


class s2400enderecoDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s2400endereco.objects.using(db_slug).all()
    serializer_class = s2400enderecoSerializer
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
        #s2400_endereco_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2400_endereco')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_s2400_evtcdbenefin': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                's2400_evtcdbenefin': 's2400_evtcdbenefin',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                's2400_evtcdbenefin': 's2400_evtcdbenefin',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2400_endereco_lista = s2400endereco.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2400_endereco_lista) > 100:
            filtrar = True
            s2400_endereco_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #s2400_endereco_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2400_endereco'
        context = {
            's2400_endereco_lista': s2400_endereco_lista,

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
            return render(request, 's2400_endereco_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2400_endereco_listar.html',
                filename="s2400_endereco.pdf",
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
            response = render_to_response('s2400_endereco_listar.html', context)
            filename = "s2400_endereco.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s2400_endereco_csv.html', context)
            filename = "s2400_endereco.csv"
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

