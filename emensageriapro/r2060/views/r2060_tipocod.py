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
from emensageriapro.r2060.forms import *
from emensageriapro.r2060.models import *
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
        r2060_tipocod_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2060_tipocod')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r2060_tipocod = get_object_or_404(r2060tipoCod.objects.using( db_slug ), excluido = False, id = r2060_tipocod_id)
    dados_evento = {}
    if r2060_tipocod_id:
        dados_evento = r2060_tipocod.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r2060_tipocod_apagar'] = 0
            dict_permissoes['r2060_tipocod_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r2060_tipocod), indent=4, sort_keys=True, default=str)
            obj = r2060tipoCod.objects.using( db_slug ).get(id = r2060_tipocod_id)
            obj.delete(request=request)
            #r2060_tipocod_apagar_custom
            #r2060_tipocod_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r2060_tipocod', r2060_tipocod_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 'r2060_tipocod_salvar':
            return redirect('r2060_tipocod', hash=request.session['retorno_hash'])
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
    return render(request, 'r2060_tipocod_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class r2060tipoCodList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = r2060tipoCod.objects.using(db_slug).all()
    serializer_class = r2060tipoCodSerializer
    # permission_classes = (IsAdminUser,)


class r2060tipoCodDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = r2060tipoCod.objects.using(db_slug).all()
    serializer_class = r2060tipoCodSerializer
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
        #r2060_tipocod_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2060_tipocod')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_codativecon': 1,
            'show_r2060_evtcprb': 1,
            'show_vlradicrecbruta': 1,
            'show_vlrbccprb': 1,
            'show_vlrcprbapur': 0,
            'show_vlrexcrecbruta': 1,
            'show_vlrrecbrutaativ': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'codativecon__icontains': 'codativecon__icontains',
                'r2060_evtcprb': 'r2060_evtcprb',
                'vlradicrecbruta': 'vlradicrecbruta',
                'vlrbccprb': 'vlrbccprb',
                'vlrcprbapur': 'vlrcprbapur',
                'vlrexcrecbruta': 'vlrexcrecbruta',
                'vlrrecbrutaativ': 'vlrrecbrutaativ',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'codativecon__icontains': 'codativecon__icontains',
                'r2060_evtcprb': 'r2060_evtcprb',
                'vlradicrecbruta': 'vlradicrecbruta',
                'vlrbccprb': 'vlrbccprb',
                'vlrcprbapur': 'vlrcprbapur',
                'vlrexcrecbruta': 'vlrexcrecbruta',
                'vlrrecbrutaativ': 'vlrrecbrutaativ',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r2060_tipocod_lista = r2060tipoCod.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r2060_tipocod_lista) > 100:
            filtrar = True
            r2060_tipocod_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #r2060_tipocod_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r2060_tipocod'
        context = {
            'r2060_tipocod_lista': r2060_tipocod_lista,
  
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
            return render(request, 'r2060_tipocod_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2060_tipocod_listar.html',
                filename="r2060_tipocod.pdf",
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
            response = render_to_response('r2060_tipocod_listar.html', context)
            filename = "r2060_tipocod.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/r2060_tipocod_csv.html', context)
            filename = "r2060_tipocod.csv"
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
        r2060_tipocod_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2060_tipocod')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if r2060_tipocod_id:
        r2060_tipocod = get_object_or_404(r2060tipoCod.objects.using( db_slug ), excluido = False, id = r2060_tipocod_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if r2060_tipocod_id:
        dados_evento = r2060_tipocod.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r2060_tipocod_apagar'] = 0
            dict_permissoes['r2060_tipocod_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r2060_tipocod_id:
            r2060_tipocod_form = form_r2060_tipocod(request.POST or None, instance = r2060_tipocod, slug = db_slug)
        else:
            r2060_tipocod_form = form_r2060_tipocod(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if r2060_tipocod_form.is_valid():

                dados = r2060_tipocod_form.cleaned_data
                obj = r2060_tipocod_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')

                if not r2060_tipocod_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 'r2060_tipocod', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(r2060_tipocod), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r2060_tipocod', r2060_tipocod_id, usuario_id, 2)
                  
                if request.session['retorno_pagina'] not in ('r2060_tipocod_apagar', 'r2060_tipocod_salvar', 'r2060_tipocod'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if r2060_tipocod_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r2060_tipocod_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        r2060_tipocod_form = disabled_form_fields(r2060_tipocod_form, permissao.permite_editar)
        if r2060_tipocod_id:
            if dados_evento['status'] != 0:
                r2060_tipocod_form = disabled_form_fields(r2060_tipocod_form, 0)
        #r2060_tipocod_campos_multiple_passo3

        for field in r2060_tipocod_form.fields.keys():
            r2060_tipocod_form.fields[field].widget.attrs['ng-model'] = 'r2060_tipocod_'+field
        if int(dict_hash['print']):
            r2060_tipocod_form = disabled_form_for_print(r2060_tipocod_form)

        r2060_tipoajuste_form = None
        r2060_tipoajuste_lista = None
        r2060_infoproc_form = None
        r2060_infoproc_lista = None
        if r2060_tipocod_id:
            r2060_tipocod = get_object_or_404(r2060tipoCod.objects.using( db_slug ), excluido = False, id = r2060_tipocod_id)

            r2060_tipoajuste_form = form_r2060_tipoajuste(initial={ 'r2060_tipocod': r2060_tipocod }, slug=db_slug)
            r2060_tipoajuste_form.fields['r2060_tipocod'].widget.attrs['readonly'] = True
            r2060_tipoajuste_lista = r2060tipoAjuste.objects.using( db_slug ).filter(excluido = False, r2060_tipocod_id=r2060_tipocod.id).all()
            r2060_infoproc_form = form_r2060_infoproc(initial={ 'r2060_tipocod': r2060_tipocod }, slug=db_slug)
            r2060_infoproc_form.fields['r2060_tipocod'].widget.attrs['readonly'] = True
            r2060_infoproc_lista = r2060infoProc.objects.using( db_slug ).filter(excluido = False, r2060_tipocod_id=r2060_tipocod.id).all()
        else:
            r2060_tipocod = None
        #r2060_tipocod_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'r2060_tipocod' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r2060_tipocod_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r2060_tipocod_id, tabela='r2060_tipocod').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            'r2060_tipocod': r2060_tipocod,
            'r2060_tipocod_form': r2060_tipocod_form,
            'mensagem': mensagem,
            'r2060_tipocod_id': int(r2060_tipocod_id),
            'usuario': usuario,
  
            'hash': hash,

            'r2060_tipoajuste_form': r2060_tipoajuste_form,
            'r2060_tipoajuste_lista': r2060_tipoajuste_lista,
            'r2060_infoproc_form': r2060_infoproc_form,
            'r2060_infoproc_lista': r2060_infoproc_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r2060_tipocod_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'r2060_tipocod_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2060_tipocod_salvar.html',
                filename="r2060_tipocod.pdf",
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
            response = render_to_response('r2060_tipocod_salvar.html', context)
            filename = "r2060_tipocod.xls"
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

