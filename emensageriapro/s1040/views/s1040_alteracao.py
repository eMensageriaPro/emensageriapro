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
from emensageriapro.s1040.forms import *
from emensageriapro.s1040.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1040_alteracao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1040_alteracao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s1040_alteracao = get_object_or_404(s1040alteracao.objects.using( db_slug ), excluido = False, id = s1040_alteracao_id)
    dados_evento = {}
    if s1040_alteracao_id:
        dados_evento = s1040_alteracao.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s1040_alteracao_apagar'] = 0
            dict_permissoes['s1040_alteracao_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s1040_alteracao), indent=4, sort_keys=True, default=str)
            s1040alteracao.objects.using( db_slug ).filter(id = s1040_alteracao_id).delete()
            #s1040_alteracao_apagar_custom
            #s1040_alteracao_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's1040_alteracao', s1040_alteracao_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
        
        if request.session['retorno_pagina']== 's1040_alteracao_salvar':
            return redirect('s1040_alteracao', hash=request.session['retorno_hash'])
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
    return render(request, 's1040_alteracao_apagar.html', context)

@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1040_alteracao_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1040_alteracao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s1040_alteracao_id:
        s1040_alteracao = get_object_or_404(s1040alteracao.objects.using( db_slug ), excluido = False, id = s1040_alteracao_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if s1040_alteracao_id:
        dados_evento = s1040_alteracao.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s1040_alteracao_apagar'] = 0
            dict_permissoes['s1040_alteracao_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s1040_alteracao_id:
            s1040_alteracao_form = form_s1040_alteracao(request.POST or None, instance = s1040_alteracao, slug = db_slug)
        else:
            s1040_alteracao_form = form_s1040_alteracao(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if s1040_alteracao_form.is_valid():
                dados = s1040_alteracao_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s1040_alteracao_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s1040_alteracao_campos_multiple_passo1
                        s1040alteracao.objects.using(db_slug).filter(id=s1040_alteracao_id).update(**dados)
                        obj = s1040alteracao.objects.using(db_slug).get(id=s1040_alteracao_id)
                        #s1040_alteracao_editar_custom
                        #s1040_alteracao_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s1040_alteracao), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's1040_alteracao', s1040_alteracao_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s1040_alteracao_cadastrar_campos_multiple_passo1
                    obj = s1040alteracao(**dados)
                    obj.save(using = db_slug)
                    #s1040_alteracao_cadastrar_custom
                    #s1040_alteracao_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's1040_alteracao', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('s1040_alteracao_apagar', 's1040_alteracao_salvar', 's1040_alteracao'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if s1040_alteracao_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('s1040_alteracao_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s1040_alteracao_form = disabled_form_fields(s1040_alteracao_form, permissao.permite_editar)
        if s1040_alteracao_id:
            if dados_evento['status'] != 0:
                s1040_alteracao_form = disabled_form_fields(s1040_alteracao_form, 0)
        #s1040_alteracao_campos_multiple_passo3

        for field in s1040_alteracao_form.fields.keys():
            s1040_alteracao_form.fields[field].widget.attrs['ng-model'] = 's1040_alteracao_'+field
        if int(dict_hash['print']):
            s1040_alteracao_form = disabled_form_for_print(s1040_alteracao_form)
   
        s1040_alteracao_novavalidade_form = None
        s1040_alteracao_novavalidade_lista = None
        if s1040_alteracao_id:
            s1040_alteracao = get_object_or_404(s1040alteracao.objects.using( db_slug ), excluido = False, id = s1040_alteracao_id)
       
            s1040_alteracao_novavalidade_form = form_s1040_alteracao_novavalidade(initial={ 's1040_alteracao': s1040_alteracao }, slug=db_slug)
            s1040_alteracao_novavalidade_form.fields['s1040_alteracao'].widget.attrs['readonly'] = True
            s1040_alteracao_novavalidade_lista = s1040alteracaonovaValidade.objects.using( db_slug ).filter(excluido = False, s1040_alteracao_id=s1040_alteracao.id).all()
        else:
            s1040_alteracao = None
        #s1040_alteracao_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's1040_alteracao' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1040_alteracao_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s1040_alteracao_id, tabela='s1040_alteracao').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's1040_alteracao': s1040_alteracao,
            's1040_alteracao_form': s1040_alteracao_form,
            'mensagem': mensagem,
            's1040_alteracao_id': int(s1040_alteracao_id),
            'usuario': usuario,
            
            'hash': hash,
       
            's1040_alteracao_novavalidade_form': s1040_alteracao_novavalidade_form,
            's1040_alteracao_novavalidade_lista': s1040_alteracao_novavalidade_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1040_alteracao_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's1040_alteracao_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1040_alteracao_salvar.html',
                filename="s1040_alteracao.pdf",
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
            response = render_to_response('s1040_alteracao_salvar.html', context)
            filename = "s1040_alteracao.xls"
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


class s1040alteracaoList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s1040alteracao.objects.using(db_slug).all()
    serializer_class = s1040alteracaoSerializer
    permission_classes = (IsAdminUser,)


class s1040alteracaoDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s1040alteracao.objects.using(db_slug).all()
    serializer_class = s1040alteracaoSerializer
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
        #s1040_alteracao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1040_alteracao')
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
            'show_codcbo': 1,
            'show_dscfuncao': 1,
            'show_dadosfuncao': 0,
            'show_fimvalid': 0,
            'show_inivalid': 1,
            'show_codfuncao': 1,
            'show_idefuncao': 0,
            'show_s1040_evttabfuncao': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'codcbo__icontains': 'codcbo__icontains',
                'dscfuncao__icontains': 'dscfuncao__icontains',
                'dadosfuncao': 'dadosfuncao',
                'fimvalid__icontains': 'fimvalid__icontains',
                'inivalid__icontains': 'inivalid__icontains',
                'codfuncao__icontains': 'codfuncao__icontains',
                'idefuncao': 'idefuncao',
                's1040_evttabfuncao': 's1040_evttabfuncao',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'codcbo__icontains': 'codcbo__icontains',
                'dscfuncao__icontains': 'dscfuncao__icontains',
                'dadosfuncao': 'dadosfuncao',
                'fimvalid__icontains': 'fimvalid__icontains',
                'inivalid__icontains': 'inivalid__icontains',
                'codfuncao__icontains': 'codfuncao__icontains',
                'idefuncao': 'idefuncao',
                's1040_evttabfuncao': 's1040_evttabfuncao',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s1040_alteracao_lista = s1040alteracao.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s1040_alteracao_lista) > 100:
            filtrar = True
            s1040_alteracao_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
    
        #s1040_alteracao_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1040_alteracao'
        context = {
            's1040_alteracao_lista': s1040_alteracao_lista,
            
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
            return render(request, 's1040_alteracao_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1040_alteracao_listar.html',
                filename="s1040_alteracao.pdf",
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
            response = render_to_response('s1040_alteracao_listar.html', context)
            filename = "s1040_alteracao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s1040_alteracao_csv.html', context)
            filename = "s1040_alteracao.csv"
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

