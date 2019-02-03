#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

import datetime
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.tabelas.forms import *
from emensageriapro.tabelas.models import *
from emensageriapro.controle_de_acesso.models import *
import json
import base64

#IMPORTACOES
@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        esocial_codificacoes_acidente_trabalho_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='esocial_codificacoes_acidente_trabalho')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    esocial_codificacoes_acidente_trabalho = get_object_or_404(eSocialCodificacoesAcidenteTrabalho.objects.using( db_slug ), excluido = False, id = esocial_codificacoes_acidente_trabalho_id)
    if request.method == 'POST':
        obj = eSocialCodificacoesAcidenteTrabalho.objects.using( db_slug ).get(id = esocial_codificacoes_acidente_trabalho_id)
        obj.delete(request=request)
        #esocial_codificacoes_acidente_trabalho_apagar_custom
        #esocial_codificacoes_acidente_trabalho_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'esocial_codificacoes_acidente_trabalho_salvar':
            return redirect('esocial_codificacoes_acidente_trabalho', hash=request.session['retorno_hash'])
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
    return render(request, 'esocial_codificacoes_acidente_trabalho_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class eSocialCodificacoesAcidenteTrabalhoList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = eSocialCodificacoesAcidenteTrabalho.objects.using(db_slug).all()
    serializer_class = eSocialCodificacoesAcidenteTrabalhoSerializer
    # permission_classes = (IsAdminUser,)


class eSocialCodificacoesAcidenteTrabalhoDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = eSocialCodificacoesAcidenteTrabalho.objects.using(db_slug).all()
    serializer_class = eSocialCodificacoesAcidenteTrabalhoSerializer
    # permission_classes = (IsAdminUser,)


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
            lista = eSocialCodificacoesAcidenteTrabalho.objects.using(db_slug).filter(excluido = False).filter(query).all()
        except:
            query = reduce(operator.and_, ((Q(descricao__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = eSocialCodificacoesAcidenteTrabalho.objects.using(db_slug).filter(excluido = False).filter(query).all()
    else:
        lista = eSocialCodificacoesAcidenteTrabalho.objects.using(db_slug).filter(excluido=False).all()
    lista_esocial_codificacoes_acidente_trabalho = []
    for a in lista:
        dic = {}
        dic['key'] = a.codigo
        dic['value'] = '%s' % (a)
        lista_esocial_codificacoes_acidente_trabalho.append(dic)
    dicionario['esocial_codificacoes_acidente_trabalho'] = lista_esocial_codificacoes_acidente_trabalho
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
        #esocial_codificacoes_acidente_trabalho_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='esocial_codificacoes_acidente_trabalho')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_codigo': 1,
            'show_descricao': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'codigo__icontains': 'codigo__icontains',
                'descricao__icontains': 'descricao__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'codigo__icontains': 'codigo__icontains',
                'descricao__icontains': 'descricao__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        esocial_codificacoes_acidente_trabalho_lista = eSocialCodificacoesAcidenteTrabalho.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(esocial_codificacoes_acidente_trabalho_lista) > 100:
            filtrar = True
            esocial_codificacoes_acidente_trabalho_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #esocial_codificacoes_acidente_trabalho_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'esocial_codificacoes_acidente_trabalho'
        context = {
            'esocial_codificacoes_acidente_trabalho_lista': esocial_codificacoes_acidente_trabalho_lista,
  
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
            return render(request, 'esocial_codificacoes_acidente_trabalho_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='esocial_codificacoes_acidente_trabalho_listar.html',
                filename="esocial_codificacoes_acidente_trabalho.pdf",
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
            response = render_to_response('esocial_codificacoes_acidente_trabalho_listar.html', context)
            filename = "esocial_codificacoes_acidente_trabalho.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/esocial_codificacoes_acidente_trabalho_csv.html', context)
            filename = "esocial_codificacoes_acidente_trabalho.csv"
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

@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        esocial_codificacoes_acidente_trabalho_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='esocial_codificacoes_acidente_trabalho')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if esocial_codificacoes_acidente_trabalho_id:
        esocial_codificacoes_acidente_trabalho = get_object_or_404(eSocialCodificacoesAcidenteTrabalho.objects.using( db_slug ), excluido = False, id = esocial_codificacoes_acidente_trabalho_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if esocial_codificacoes_acidente_trabalho_id:
            esocial_codificacoes_acidente_trabalho_form = form_esocial_codificacoes_acidente_trabalho(request.POST or None, instance = esocial_codificacoes_acidente_trabalho, slug = db_slug)
        else:
            esocial_codificacoes_acidente_trabalho_form = form_esocial_codificacoes_acidente_trabalho(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if esocial_codificacoes_acidente_trabalho_form.is_valid():

                dados = esocial_codificacoes_acidente_trabalho_form.cleaned_data
                obj = esocial_codificacoes_acidente_trabalho_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')

                if not esocial_codificacoes_acidente_trabalho_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 'esocial_codificacoes_acidente_trabalho', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(esocial_codificacoes_acidente_trabalho), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'esocial_codificacoes_acidente_trabalho', esocial_codificacoes_acidente_trabalho_id, usuario_id, 2)
                  
                if request.session['retorno_pagina'] not in ('esocial_codificacoes_acidente_trabalho_apagar', 'esocial_codificacoes_acidente_trabalho_salvar', 'esocial_codificacoes_acidente_trabalho'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if esocial_codificacoes_acidente_trabalho_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('esocial_codificacoes_acidente_trabalho_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        esocial_codificacoes_acidente_trabalho_form = disabled_form_fields(esocial_codificacoes_acidente_trabalho_form, permissao.permite_editar)
        #esocial_codificacoes_acidente_trabalho_campos_multiple_passo3

        for field in esocial_codificacoes_acidente_trabalho_form.fields.keys():
            esocial_codificacoes_acidente_trabalho_form.fields[field].widget.attrs['ng-model'] = 'esocial_codificacoes_acidente_trabalho_'+field
        if int(dict_hash['print']):
            esocial_codificacoes_acidente_trabalho_form = disabled_form_for_print(esocial_codificacoes_acidente_trabalho_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if esocial_codificacoes_acidente_trabalho_id:
            esocial_codificacoes_acidente_trabalho = get_object_or_404(eSocialCodificacoesAcidenteTrabalho.objects.using( db_slug ), excluido = False, id = esocial_codificacoes_acidente_trabalho_id)
            pass
        else:
            esocial_codificacoes_acidente_trabalho = None
        #esocial_codificacoes_acidente_trabalho_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'esocial_codificacoes_acidente_trabalho' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'esocial_codificacoes_acidente_trabalho_salvar'
        context = {
            'esocial_codificacoes_acidente_trabalho': esocial_codificacoes_acidente_trabalho,
            'esocial_codificacoes_acidente_trabalho_form': esocial_codificacoes_acidente_trabalho_form,
            'mensagem': mensagem,
            'esocial_codificacoes_acidente_trabalho_id': int(esocial_codificacoes_acidente_trabalho_id),
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
            #esocial_codificacoes_acidente_trabalho_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'esocial_codificacoes_acidente_trabalho_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='esocial_codificacoes_acidente_trabalho_salvar.html',
                filename="esocial_codificacoes_acidente_trabalho.pdf",
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
            response = render_to_response('esocial_codificacoes_acidente_trabalho_salvar.html', context)
            filename = "esocial_codificacoes_acidente_trabalho.xls"
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

