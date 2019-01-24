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
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.s5011.forms import *
from emensageriapro.s5011.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s5011_infoemprparcial_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_infoemprparcial')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s5011_infoemprparcial = get_object_or_404(s5011infoEmprParcial.objects.using( db_slug ), excluido = False, id = s5011_infoemprparcial_id)
    dados_evento = {}
    if s5011_infoemprparcial_id:
        dados_evento = s5011_infoemprparcial.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s5011_infoemprparcial_apagar'] = 0
            dict_permissoes['s5011_infoemprparcial_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s5011_infoemprparcial), indent=4, sort_keys=True, default=str)
            s5011infoEmprParcial.objects.using( db_slug ).filter(id = s5011_infoemprparcial_id).delete()
            #s5011_infoemprparcial_apagar_custom
            #s5011_infoemprparcial_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's5011_infoemprparcial', s5011_infoemprparcial_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's5011_infoemprparcial_salvar':
            return redirect('s5011_infoemprparcial', hash=request.session['retorno_hash'])
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
    return render(request, 's5011_infoemprparcial_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class s5011infoEmprParcialList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s5011infoEmprParcial.objects.using(db_slug).all()
    serializer_class = s5011infoEmprParcialSerializer
    permission_classes = (IsAdminUser,)


class s5011infoEmprParcialDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s5011infoEmprParcial.objects.using(db_slug).all()
    serializer_class = s5011infoEmprParcialSerializer
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
        #s5011_infoemprparcial_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_infoemprparcial')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_nrinsccontrat': 1,
            'show_nrinscprop': 1,
            'show_s5011_idelotacao': 1,
            'show_tpinsccontrat': 1,
            'show_tpinscprop': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'nrinsccontrat__icontains': 'nrinsccontrat__icontains',
                'nrinscprop__icontains': 'nrinscprop__icontains',
                's5011_idelotacao': 's5011_idelotacao',
                'tpinsccontrat': 'tpinsccontrat',
                'tpinscprop': 'tpinscprop',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'nrinsccontrat__icontains': 'nrinsccontrat__icontains',
                'nrinscprop__icontains': 'nrinscprop__icontains',
                's5011_idelotacao': 's5011_idelotacao',
                'tpinsccontrat': 'tpinsccontrat',
                'tpinscprop': 'tpinscprop',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s5011_infoemprparcial_lista = s5011infoEmprParcial.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s5011_infoemprparcial_lista) > 100:
            filtrar = True
            s5011_infoemprparcial_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #s5011_infoemprparcial_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5011_infoemprparcial'
        context = {
            's5011_infoemprparcial_lista': s5011_infoemprparcial_lista,
  
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
            return render(request, 's5011_infoemprparcial_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s5011_infoemprparcial_listar.html',
                filename="s5011_infoemprparcial.pdf",
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
            response = render_to_response('s5011_infoemprparcial_listar.html', context)
            filename = "s5011_infoemprparcial.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s5011_infoemprparcial_csv.html', context)
            filename = "s5011_infoemprparcial.csv"
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
        s5011_infoemprparcial_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_infoemprparcial')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s5011_infoemprparcial_id:
        s5011_infoemprparcial = get_object_or_404(s5011infoEmprParcial.objects.using( db_slug ), excluido = False, id = s5011_infoemprparcial_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if s5011_infoemprparcial_id:
        dados_evento = s5011_infoemprparcial.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s5011_infoemprparcial_apagar'] = 0
            dict_permissoes['s5011_infoemprparcial_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s5011_infoemprparcial_id:
            s5011_infoemprparcial_form = form_s5011_infoemprparcial(request.POST or None, instance = s5011_infoemprparcial, slug = db_slug)
        else:
            s5011_infoemprparcial_form = form_s5011_infoemprparcial(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if s5011_infoemprparcial_form.is_valid():
                dados = s5011_infoemprparcial_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s5011_infoemprparcial_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s5011_infoemprparcial_campos_multiple_passo1
                        s5011infoEmprParcial.objects.using(db_slug).filter(id=s5011_infoemprparcial_id).update(**dados)
                        obj = s5011infoEmprParcial.objects.using(db_slug).get(id=s5011_infoemprparcial_id)
                        #s5011_infoemprparcial_editar_custom
                        #s5011_infoemprparcial_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s5011_infoemprparcial), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's5011_infoemprparcial', s5011_infoemprparcial_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s5011_infoemprparcial_cadastrar_campos_multiple_passo1
                    obj = s5011infoEmprParcial(**dados)
                    obj.save(using = db_slug)
                    #s5011_infoemprparcial_cadastrar_custom
                    #s5011_infoemprparcial_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's5011_infoemprparcial', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('s5011_infoemprparcial_apagar', 's5011_infoemprparcial_salvar', 's5011_infoemprparcial'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if s5011_infoemprparcial_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('s5011_infoemprparcial_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s5011_infoemprparcial_form = disabled_form_fields(s5011_infoemprparcial_form, permissao.permite_editar)
        if s5011_infoemprparcial_id:
            if dados_evento['status'] != 0:
                s5011_infoemprparcial_form = disabled_form_fields(s5011_infoemprparcial_form, 0)
        #s5011_infoemprparcial_campos_multiple_passo3

        for field in s5011_infoemprparcial_form.fields.keys():
            s5011_infoemprparcial_form.fields[field].widget.attrs['ng-model'] = 's5011_infoemprparcial_'+field
        if int(dict_hash['print']):
            s5011_infoemprparcial_form = disabled_form_for_print(s5011_infoemprparcial_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if s5011_infoemprparcial_id:
            s5011_infoemprparcial = get_object_or_404(s5011infoEmprParcial.objects.using( db_slug ), excluido = False, id = s5011_infoemprparcial_id)
            pass
        else:
            s5011_infoemprparcial = None
        #s5011_infoemprparcial_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's5011_infoemprparcial' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's5011_infoemprparcial_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s5011_infoemprparcial_id, tabela='s5011_infoemprparcial').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's5011_infoemprparcial': s5011_infoemprparcial,
            's5011_infoemprparcial_form': s5011_infoemprparcial_form,
            'mensagem': mensagem,
            's5011_infoemprparcial_id': int(s5011_infoemprparcial_id),
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
            #s5011_infoemprparcial_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's5011_infoemprparcial_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s5011_infoemprparcial_salvar.html',
                filename="s5011_infoemprparcial.pdf",
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
            response = render_to_response('s5011_infoemprparcial_salvar.html', context)
            filename = "s5011_infoemprparcial.xls"
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

