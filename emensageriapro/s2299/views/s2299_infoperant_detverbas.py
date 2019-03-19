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
from emensageriapro.s2299.forms import *
from emensageriapro.s2299.models import *
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
        s2299_infoperant_detverbas_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2299_infoperant_detverbas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2299_infoperant_detverbas = get_object_or_404(s2299infoPerAntdetVerbas.objects.using( db_slug ), excluido = False, id = s2299_infoperant_detverbas_id)
    dados_evento = {}
    if s2299_infoperant_detverbas_id:
        dados_evento = s2299_infoperant_detverbas.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2299_infoperant_detverbas_apagar'] = 0
            dict_permissoes['s2299_infoperant_detverbas_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == STATUS_EVENTO_CADASTRADO:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2299_infoperant_detverbas), indent=4, sort_keys=True, default=str)
            obj = s2299infoPerAntdetVerbas.objects.using( db_slug ).get(id = s2299_infoperant_detverbas_id)
            obj.delete(request=request)
            #s2299_infoperant_detverbas_apagar_custom
            #s2299_infoperant_detverbas_apagar_custom
            messages.success(request, u'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2299_infoperant_detverbas', s2299_infoperant_detverbas_id, usuario_id, 3)
        else:
            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's2299_infoperant_detverbas_salvar':
            return redirect('s2299_infoperant_detverbas', hash=request.session['retorno_hash'])
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
    return render(request, 's2299_infoperant_detverbas_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class s2299infoPerAntdetVerbasList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s2299infoPerAntdetVerbas.objects.using(db_slug).all()
    serializer_class = s2299infoPerAntdetVerbasSerializer
    # permission_classes = (IsAdminUser,)


class s2299infoPerAntdetVerbasDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s2299infoPerAntdetVerbas.objects.using(db_slug).all()
    serializer_class = s2299infoPerAntdetVerbasSerializer
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
        #s2299_infoperant_detverbas_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2299_infoperant_detverbas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_codrubr': 1,
            'show_fatorrubr': 0,
            'show_idetabrubr': 1,
            'show_qtdrubr': 0,
            'show_s2299_infoperant_ideestablot': 1,
            'show_vrrubr': 1,
            'show_vrunit': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'codrubr__icontains': 'codrubr__icontains',
                'fatorrubr': 'fatorrubr',
                'idetabrubr__icontains': 'idetabrubr__icontains',
                'qtdrubr': 'qtdrubr',
                's2299_infoperant_ideestablot': 's2299_infoperant_ideestablot',
                'vrrubr': 'vrrubr',
                'vrunit': 'vrunit',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'codrubr__icontains': 'codrubr__icontains',
                'fatorrubr': 'fatorrubr',
                'idetabrubr__icontains': 'idetabrubr__icontains',
                'qtdrubr': 'qtdrubr',
                's2299_infoperant_ideestablot': 's2299_infoperant_ideestablot',
                'vrrubr': 'vrrubr',
                'vrunit': 'vrunit',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2299_infoperant_detverbas_lista = s2299infoPerAntdetVerbas.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2299_infoperant_detverbas_lista) > 100:
            filtrar = True
            s2299_infoperant_detverbas_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #s2299_infoperant_detverbas_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2299_infoperant_detverbas'
        context = {
            's2299_infoperant_detverbas_lista': s2299_infoperant_detverbas_lista,
  
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
            return render(request, 's2299_infoperant_detverbas_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2299_infoperant_detverbas_listar.html',
                filename="s2299_infoperant_detverbas.pdf",
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
            response = render_to_response('s2299_infoperant_detverbas_listar.html', context)
            filename = "s2299_infoperant_detverbas.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s2299_infoperant_detverbas_csv.html', context)
            filename = "s2299_infoperant_detverbas.csv"
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
        s2299_infoperant_detverbas_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2299_infoperant_detverbas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2299_infoperant_detverbas_id:
        s2299_infoperant_detverbas = get_object_or_404(s2299infoPerAntdetVerbas.objects.using( db_slug ), excluido = False, id = s2299_infoperant_detverbas_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    if s2299_infoperant_detverbas_id:
        dados_evento = s2299_infoperant_detverbas.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2299_infoperant_detverbas_apagar'] = 0
            dict_permissoes['s2299_infoperant_detverbas_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2299_infoperant_detverbas_id:
            s2299_infoperant_detverbas_form = form_s2299_infoperant_detverbas(request.POST or None,
                                         instance = s2299_infoperant_detverbas,
                                         slug = db_slug,
                                         initial={'excluido': False})
        else:
            s2299_infoperant_detverbas_form = form_s2299_infoperant_detverbas(request.POST or None,
                                         slug = db_slug,
                                         initial={'excluido': False})
        if request.method == 'POST':
            if s2299_infoperant_detverbas_form.is_valid():

                dados = s2299_infoperant_detverbas_form.cleaned_data
                obj = s2299_infoperant_detverbas_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not s2299_infoperant_detverbas_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 's2299_infoperant_detverbas', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(s2299_infoperant_detverbas), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2299_infoperant_detverbas', s2299_infoperant_detverbas_id, usuario_id, 2)
                  
                if request.session['retorno_pagina'] not in ('s2299_infoperant_detverbas_apagar', 's2299_infoperant_detverbas_salvar', 's2299_infoperant_detverbas'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2299_infoperant_detverbas_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2299_infoperant_detverbas_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        s2299_infoperant_detverbas_form = disabled_form_fields(s2299_infoperant_detverbas_form, permissao.permite_editar)
        if s2299_infoperant_detverbas_id:
            if dados_evento['status'] != 0:
                s2299_infoperant_detverbas_form = disabled_form_fields(s2299_infoperant_detverbas_form, 0)
        #s2299_infoperant_detverbas_campos_multiple_passo3

        for field in s2299_infoperant_detverbas_form.fields.keys():
            s2299_infoperant_detverbas_form.fields[field].widget.attrs['ng-model'] = 's2299_infoperant_detverbas_'+field
        if int(dict_hash['print']):
            s2299_infoperant_detverbas_form = disabled_form_for_print(s2299_infoperant_detverbas_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if s2299_infoperant_detverbas_id:
            s2299_infoperant_detverbas = get_object_or_404(s2299infoPerAntdetVerbas.objects.using( db_slug ), excluido = False, id = s2299_infoperant_detverbas_id)
            pass
        else:
            s2299_infoperant_detverbas = None
        #s2299_infoperant_detverbas_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's2299_infoperant_detverbas' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2299_infoperant_detverbas_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2299_infoperant_detverbas_id, tabela='s2299_infoperant_detverbas').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's2299_infoperant_detverbas': s2299_infoperant_detverbas,
            's2299_infoperant_detverbas_form': s2299_infoperant_detverbas_form,
            'mensagem': mensagem,
            's2299_infoperant_detverbas_id': int(s2299_infoperant_detverbas_id),
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
            #s2299_infoperant_detverbas_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's2299_infoperant_detverbas_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2299_infoperant_detverbas_salvar.html',
                filename="s2299_infoperant_detverbas.pdf",
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
            response = render_to_response('s2299_infoperant_detverbas_salvar.html', context)
            filename = "s2299_infoperant_detverbas.xls"
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

