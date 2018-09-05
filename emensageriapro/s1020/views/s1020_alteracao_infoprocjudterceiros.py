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
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.s1020.forms import *
from emensageriapro.s1020.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s1020_alteracao_infoprocjudterceiros_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1020_alteracao_infoprocjudterceiros')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s1020_alteracao_infoprocjudterceiros_id:
        s1020_alteracao_infoprocjudterceiros = get_object_or_404(s1020alteracaoinfoProcJudTerceiros.objects.using( db_slug ), excluido = False, id = s1020_alteracao_infoprocjudterceiros_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if s1020_alteracao_infoprocjudterceiros_id:
        dados_evento = s1020_alteracao_infoprocjudterceiros.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s1020_alteracao_infoprocjudterceiros_apagar'] = 0
            dict_permissoes['s1020_alteracao_infoprocjudterceiros_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s1020_alteracao_infoprocjudterceiros_id:
            s1020_alteracao_infoprocjudterceiros_form = form_s1020_alteracao_infoprocjudterceiros(request.POST or None, instance = s1020_alteracao_infoprocjudterceiros, slug = db_slug)
        else:
            s1020_alteracao_infoprocjudterceiros_form = form_s1020_alteracao_infoprocjudterceiros(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if s1020_alteracao_infoprocjudterceiros_form.is_valid():
                dados = s1020_alteracao_infoprocjudterceiros_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s1020_alteracao_infoprocjudterceiros_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s1020_alteracao_infoprocjudterceiros_campos_multiple_passo1
                        s1020alteracaoinfoProcJudTerceiros.objects.using(db_slug).filter(id=s1020_alteracao_infoprocjudterceiros_id).update(**dados)
                        obj = s1020alteracaoinfoProcJudTerceiros.objects.using(db_slug).get(id=s1020_alteracao_infoprocjudterceiros_id)
                        #s1020_alteracao_infoprocjudterceiros_editar_custom
                        #s1020_alteracao_infoprocjudterceiros_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s1020_alteracao_infoprocjudterceiros), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's1020_alteracao_infoprocjudterceiros', s1020_alteracao_infoprocjudterceiros_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s1020_alteracao_infoprocjudterceiros_cadastrar_campos_multiple_passo1
                    obj = s1020alteracaoinfoProcJudTerceiros(**dados)
                    obj.save(using = db_slug)
                    #s1020_alteracao_infoprocjudterceiros_cadastrar_custom
                    #s1020_alteracao_infoprocjudterceiros_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's1020_alteracao_infoprocjudterceiros', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('s1020_alteracao_infoprocjudterceiros_apagar', 's1020_alteracao_infoprocjudterceiros_salvar', 's1020_alteracao_infoprocjudterceiros'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if s1020_alteracao_infoprocjudterceiros_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('s1020_alteracao_infoprocjudterceiros_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s1020_alteracao_infoprocjudterceiros_form = disabled_form_fields(s1020_alteracao_infoprocjudterceiros_form, permissao.permite_editar)
        if s1020_alteracao_infoprocjudterceiros_id:
            if dados_evento['status'] != 0:
                s1020_alteracao_infoprocjudterceiros_form = disabled_form_fields(s1020_alteracao_infoprocjudterceiros_form, 0)
        #s1020_alteracao_infoprocjudterceiros_campos_multiple_passo3

        for field in s1020_alteracao_infoprocjudterceiros_form.fields.keys():
            s1020_alteracao_infoprocjudterceiros_form.fields[field].widget.attrs['ng-model'] = 's1020_alteracao_infoprocjudterceiros_'+field
        if int(dict_hash['print']):
            s1020_alteracao_infoprocjudterceiros_form = disabled_form_for_print(s1020_alteracao_infoprocjudterceiros_form)

        s1020_alteracao_procjudterceiro_form = None
        s1020_alteracao_procjudterceiro_lista = None
        if s1020_alteracao_infoprocjudterceiros_id:
            s1020_alteracao_infoprocjudterceiros = get_object_or_404(s1020alteracaoinfoProcJudTerceiros.objects.using( db_slug ), excluido = False, id = s1020_alteracao_infoprocjudterceiros_id)
  
            s1020_alteracao_procjudterceiro_form = form_s1020_alteracao_procjudterceiro(initial={ 's1020_alteracao_infoprocjudterceiros': s1020_alteracao_infoprocjudterceiros }, slug=db_slug)
            s1020_alteracao_procjudterceiro_form.fields['s1020_alteracao_infoprocjudterceiros'].widget.attrs['readonly'] = True
            s1020_alteracao_procjudterceiro_lista = s1020alteracaoprocJudTerceiro.objects.using( db_slug ).filter(excluido = False, s1020_alteracao_infoprocjudterceiros_id=s1020_alteracao_infoprocjudterceiros.id).all()
        else:
            s1020_alteracao_infoprocjudterceiros = None
        #s1020_alteracao_infoprocjudterceiros_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's1020_alteracao_infoprocjudterceiros' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1020_alteracao_infoprocjudterceiros_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s1020_alteracao_infoprocjudterceiros_id, tabela='s1020_alteracao_infoprocjudterceiros').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's1020_alteracao_infoprocjudterceiros': s1020_alteracao_infoprocjudterceiros,
            's1020_alteracao_infoprocjudterceiros_form': s1020_alteracao_infoprocjudterceiros_form,
            'mensagem': mensagem,
            's1020_alteracao_infoprocjudterceiros_id': int(s1020_alteracao_infoprocjudterceiros_id),
            'usuario': usuario,
       
            'hash': hash,
  
            's1020_alteracao_procjudterceiro_form': s1020_alteracao_procjudterceiro_form,
            's1020_alteracao_procjudterceiro_lista': s1020_alteracao_procjudterceiro_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1020_alteracao_infoprocjudterceiros_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's1020_alteracao_infoprocjudterceiros_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1020_alteracao_infoprocjudterceiros_salvar.html',
                filename="s1020_alteracao_infoprocjudterceiros.pdf",
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
            response = render_to_response('s1020_alteracao_infoprocjudterceiros_salvar.html', context)
            filename = "s1020_alteracao_infoprocjudterceiros.xls"
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

def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s1020_alteracao_infoprocjudterceiros_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1020_alteracao_infoprocjudterceiros')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s1020_alteracao_infoprocjudterceiros = get_object_or_404(s1020alteracaoinfoProcJudTerceiros.objects.using( db_slug ), excluido = False, id = s1020_alteracao_infoprocjudterceiros_id)
    dados_evento = {}
    if s1020_alteracao_infoprocjudterceiros_id:
        dados_evento = s1020_alteracao_infoprocjudterceiros.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s1020_alteracao_infoprocjudterceiros_apagar'] = 0
            dict_permissoes['s1020_alteracao_infoprocjudterceiros_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s1020_alteracao_infoprocjudterceiros), indent=4, sort_keys=True, default=str)
            s1020alteracaoinfoProcJudTerceiros.objects.using( db_slug ).filter(id = s1020_alteracao_infoprocjudterceiros_id).delete()
            #s1020_alteracao_infoprocjudterceiros_apagar_custom
            #s1020_alteracao_infoprocjudterceiros_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's1020_alteracao_infoprocjudterceiros', s1020_alteracao_infoprocjudterceiros_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
   
        if request.session['retorno_pagina']== 's1020_alteracao_infoprocjudterceiros_salvar':
            return redirect('s1020_alteracao_infoprocjudterceiros', hash=request.session['retorno_hash'])
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
    return render(request, 's1020_alteracao_infoprocjudterceiros_apagar.html', context)

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
        #s1020_alteracao_infoprocjudterceiros_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1020_alteracao_infoprocjudterceiros')
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
            'show_s1020_alteracao': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                's1020_alteracao': 's1020_alteracao',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                's1020_alteracao': 's1020_alteracao',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s1020_alteracao_infoprocjudterceiros_lista = s1020alteracaoinfoProcJudTerceiros.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s1020_alteracao_infoprocjudterceiros_lista) > 100:
            filtrar = True
            s1020_alteracao_infoprocjudterceiros_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #s1020_alteracao_infoprocjudterceiros_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1020_alteracao_infoprocjudterceiros'
        context = {
            's1020_alteracao_infoprocjudterceiros_lista': s1020_alteracao_infoprocjudterceiros_lista,
       
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
            return render(request, 's1020_alteracao_infoprocjudterceiros_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1020_alteracao_infoprocjudterceiros_listar.html',
                filename="s1020_alteracao_infoprocjudterceiros.pdf",
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
            response = render_to_response('s1020_alteracao_infoprocjudterceiros_listar.html', context)
            filename = "s1020_alteracao_infoprocjudterceiros.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s1020_alteracao_infoprocjudterceiros_csv.html', context)
            filename = "s1020_alteracao_infoprocjudterceiros.csv"
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

