#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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
from emensageriapro.s2245.forms import *
from emensageriapro.s2245.models import *
from emensageriapro.controle_de_acesso.models import *
import json
import base64

#IMPORTACOES
@login_required
def apagar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2245_infocomplem_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2245_infocomplem')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2245_infocomplem = get_object_or_404(s2245infoComplem.objects.using( db_slug ), excluido = False, id = s2245_infocomplem_id)
    dados_evento = {}
    if s2245_infocomplem_id:
        dados_evento = s2245_infocomplem.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2245_infocomplem_apagar'] = 0
            dict_permissoes['s2245_infocomplem_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == STATUS_EVENTO_CADASTRADO:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2245_infocomplem), indent=4, sort_keys=True, default=str)
            obj = s2245infoComplem.objects.using( db_slug ).get(id = s2245_infocomplem_id)
            obj.delete(request=request)
            #s2245_infocomplem_apagar_custom
            #s2245_infocomplem_apagar_custom
            messages.success(request, u'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2245_infocomplem', s2245_infocomplem_id, usuario_id, 3)
        else:
            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's2245_infocomplem_salvar':
            return redirect('s2245_infocomplem', hash=request.session['retorno_hash'])
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
    return render(request, 's2245_infocomplem_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class s2245infoComplemList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s2245infoComplem.objects.using(db_slug).all()
    serializer_class = s2245infoComplemSerializer
    # permission_classes = (IsAdminUser,)


class s2245infoComplemDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s2245infoComplem.objects.using(db_slug).all()
    serializer_class = s2245infoComplemSerializer
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
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s2245_infocomplem_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2245_infocomplem')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_dttreicap': 1,
            'show_durtreicap': 1,
            'show_modtreicap': 1,
            'show_s2245_evttreicap': 1,
            'show_tptreicap': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'dttreicap__range': 'dttreicap__range',
                'durtreicap': 'durtreicap',
                'modtreicap': 'modtreicap',
                's2245_evttreicap': 's2245_evttreicap',
                'tptreicap': 'tptreicap',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'dttreicap__range': 'dttreicap__range',
                'durtreicap': 'durtreicap',
                'modtreicap': 'modtreicap',
                's2245_evttreicap': 's2245_evttreicap',
                'tptreicap': 'tptreicap',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2245_infocomplem_lista = s2245infoComplem.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2245_infocomplem_lista) > 100:
            filtrar = True
            s2245_infocomplem_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #s2245_infocomplem_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2245_infocomplem'
        context = {
            's2245_infocomplem_lista': s2245_infocomplem_lista,
  
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
            return render(request, 's2245_infocomplem_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2245_infocomplem_listar.html',
                filename="s2245_infocomplem.pdf",
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
            response = render_to_response('s2245_infocomplem_listar.html', context)
            filename = "s2245_infocomplem.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s2245_infocomplem_csv.html', context)
            filename = "s2245_infocomplem.csv"
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
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2245_infocomplem_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2245_infocomplem')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2245_infocomplem_id:
        s2245_infocomplem = get_object_or_404(s2245infoComplem.objects.using( db_slug ), excluido = False, id = s2245_infocomplem_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    if s2245_infocomplem_id:
        dados_evento = s2245_infocomplem.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2245_infocomplem_apagar'] = 0
            dict_permissoes['s2245_infocomplem_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2245_infocomplem_id:
            s2245_infocomplem_form = form_s2245_infocomplem(request.POST or None, instance = s2245_infocomplem,
                                         slug = db_slug,
                                         initial={'excluido': False})
        else:
            s2245_infocomplem_form = form_s2245_infocomplem(request.POST or None, slug = db_slug,
                                         initial={'excluido': False})
        if request.method == 'POST':
            if s2245_infocomplem_form.is_valid():

                dados = s2245_infocomplem_form.cleaned_data
                obj = s2245_infocomplem_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not s2245_infocomplem_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 's2245_infocomplem', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(s2245_infocomplem), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2245_infocomplem', s2245_infocomplem_id, usuario_id, 2)
                  
                if request.session['retorno_pagina'] not in ('s2245_infocomplem_apagar', 's2245_infocomplem_salvar', 's2245_infocomplem'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2245_infocomplem_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2245_infocomplem_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        s2245_infocomplem_form = disabled_form_fields(s2245_infocomplem_form, permissao.permite_editar)
        if s2245_infocomplem_id:
            if dados_evento['status'] != 0:
                s2245_infocomplem_form = disabled_form_fields(s2245_infocomplem_form, 0)
        #s2245_infocomplem_campos_multiple_passo3

        for field in s2245_infocomplem_form.fields.keys():
            s2245_infocomplem_form.fields[field].widget.attrs['ng-model'] = 's2245_infocomplem_'+field
        if int(dict_hash['print']):
            s2245_infocomplem_form = disabled_form_for_print(s2245_infocomplem_form)

        s2245_ideprofresp_form = None
        s2245_ideprofresp_lista = None
        if s2245_infocomplem_id:
            s2245_infocomplem = get_object_or_404(s2245infoComplem.objects.using( db_slug ), excluido = False, id = s2245_infocomplem_id)

            s2245_ideprofresp_form = form_s2245_ideprofresp(initial={ 's2245_infocomplem': s2245_infocomplem }, slug=db_slug)
            s2245_ideprofresp_form.fields['s2245_infocomplem'].widget.attrs['readonly'] = True
            s2245_ideprofresp_lista = s2245ideProfResp.objects.using( db_slug ).filter(excluido = False, s2245_infocomplem_id=s2245_infocomplem.id).all()
        else:
            s2245_infocomplem = None
        #s2245_infocomplem_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's2245_infocomplem' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2245_infocomplem_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2245_infocomplem_id, tabela='s2245_infocomplem').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's2245_infocomplem': s2245_infocomplem,
            's2245_infocomplem_form': s2245_infocomplem_form,
            'mensagem': mensagem,
            's2245_infocomplem_id': int(s2245_infocomplem_id),
            'usuario': usuario,
  
            'hash': hash,

            's2245_ideprofresp_form': s2245_ideprofresp_form,
            's2245_ideprofresp_lista': s2245_ideprofresp_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2245_infocomplem_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's2245_infocomplem_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2245_infocomplem_salvar.html',
                filename="s2245_infocomplem.pdf",
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
            response = render_to_response('s2245_infocomplem_salvar.html', context)
            filename = "s2245_infocomplem.xls"
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

