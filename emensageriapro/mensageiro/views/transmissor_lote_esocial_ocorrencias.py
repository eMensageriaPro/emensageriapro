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
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissor_lote_esocial_ocorrencias_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_esocial_ocorrencias')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    transmissor_lote_esocial_ocorrencias = get_object_or_404(TransmissorLoteEsocialOcorrencias.objects.using( db_slug ), excluido = False, id = transmissor_lote_esocial_ocorrencias_id)
    if request.method == 'POST':
        TransmissorLoteEsocialOcorrencias.objects.using( db_slug ).filter(id = transmissor_lote_esocial_ocorrencias_id).update(excluido = True)
        #transmissor_lote_esocial_ocorrencias_apagar_custom
        #transmissor_lote_esocial_ocorrencias_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'transmissor_lote_esocial_ocorrencias_salvar':
            return redirect('transmissor_lote_esocial_ocorrencias', hash=request.session['retorno_hash'])
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
    return render(request, 'transmissor_lote_esocial_ocorrencias_apagar.html', context)

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #transmissor_lote_esocial_ocorrencias_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_esocial_ocorrencias')
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
            'show_localizacao': 0,
            'show_tipo': 1,
            'show_descricao': 0,
            'show_resposta_codigo': 1,
            'show_transmissor_lote_esocial': 1, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'localizacao__icontains': 'localizacao__icontains',
                'tipo': 'tipo',
                'resposta_codigo': 'resposta_codigo',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'localizacao__icontains': 'localizacao__icontains',
                'tipo': 'tipo',
                'resposta_codigo': 'resposta_codigo',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        transmissor_lote_esocial_ocorrencias_lista = TransmissorLoteEsocialOcorrencias.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(transmissor_lote_esocial_ocorrencias_lista) > 100:
            filtrar = True
            transmissor_lote_esocial_ocorrencias_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #transmissor_lote_esocial_ocorrencias_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'transmissor_lote_esocial_ocorrencias'
        context = {
            'transmissor_lote_esocial_ocorrencias_lista': transmissor_lote_esocial_ocorrencias_lista,
            
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
       
            'transmissor_lote_esocial_lista': transmissor_lote_esocial_lista,
        }
        if for_print in (0,1):
            return render(request, 'transmissor_lote_esocial_ocorrencias_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='transmissor_lote_esocial_ocorrencias_listar.html',
                filename="transmissor_lote_esocial_ocorrencias.pdf",
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
            response = render_to_response('transmissor_lote_esocial_ocorrencias_listar.html', context)
            filename = "transmissor_lote_esocial_ocorrencias.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/transmissor_lote_esocial_ocorrencias_csv.html', context)
            filename = "transmissor_lote_esocial_ocorrencias.csv"
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

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissor_lote_esocial_ocorrencias_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_esocial_ocorrencias')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if transmissor_lote_esocial_ocorrencias_id:
        transmissor_lote_esocial_ocorrencias = get_object_or_404(TransmissorLoteEsocialOcorrencias.objects.using( db_slug ), excluido = False, id = transmissor_lote_esocial_ocorrencias_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if transmissor_lote_esocial_ocorrencias_id:
            transmissor_lote_esocial_ocorrencias_form = form_transmissor_lote_esocial_ocorrencias(request.POST or None, instance = transmissor_lote_esocial_ocorrencias, slug = db_slug)
        else:
            transmissor_lote_esocial_ocorrencias_form = form_transmissor_lote_esocial_ocorrencias(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if transmissor_lote_esocial_ocorrencias_form.is_valid():
                dados = transmissor_lote_esocial_ocorrencias_form.cleaned_data
                if transmissor_lote_esocial_ocorrencias_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #transmissor_lote_esocial_ocorrencias_campos_multiple_passo1
                    TransmissorLoteEsocialOcorrencias.objects.using(db_slug).filter(id=transmissor_lote_esocial_ocorrencias_id).update(**dados)
                    obj = TransmissorLoteEsocialOcorrencias.objects.using(db_slug).get(id=transmissor_lote_esocial_ocorrencias_id)
                    #transmissor_lote_esocial_ocorrencias_editar_custom
                    #transmissor_lote_esocial_ocorrencias_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #transmissor_lote_esocial_ocorrencias_cadastrar_campos_multiple_passo1
                    obj = TransmissorLoteEsocialOcorrencias(**dados)
                    obj.save(using = db_slug)
                    #transmissor_lote_esocial_ocorrencias_cadastrar_custom
                    #transmissor_lote_esocial_ocorrencias_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('transmissor_lote_esocial_ocorrencias_apagar', 'transmissor_lote_esocial_ocorrencias_salvar', 'transmissor_lote_esocial_ocorrencias'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if transmissor_lote_esocial_ocorrencias_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('transmissor_lote_esocial_ocorrencias_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        transmissor_lote_esocial_ocorrencias_form = disabled_form_fields(transmissor_lote_esocial_ocorrencias_form, permissao.permite_editar)
        #transmissor_lote_esocial_ocorrencias_campos_multiple_passo3

        for field in transmissor_lote_esocial_ocorrencias_form.fields.keys():
            transmissor_lote_esocial_ocorrencias_form.fields[field].widget.attrs['ng-model'] = 'transmissor_lote_esocial_ocorrencias_'+field
        if int(dict_hash['print']):
            transmissor_lote_esocial_ocorrencias_form = disabled_form_for_print(transmissor_lote_esocial_ocorrencias_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if transmissor_lote_esocial_ocorrencias_id:
            transmissor_lote_esocial_ocorrencias = get_object_or_404(TransmissorLoteEsocialOcorrencias.objects.using( db_slug ), excluido = False, id = transmissor_lote_esocial_ocorrencias_id)
            pass
        else:
            transmissor_lote_esocial_ocorrencias = None
        #transmissor_lote_esocial_ocorrencias_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'transmissor_lote_esocial_ocorrencias' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'transmissor_lote_esocial_ocorrencias_salvar'
        context = {
            'transmissor_lote_esocial_ocorrencias': transmissor_lote_esocial_ocorrencias,
            'transmissor_lote_esocial_ocorrencias_form': transmissor_lote_esocial_ocorrencias_form,
            'mensagem': mensagem,
            'transmissor_lote_esocial_ocorrencias_id': int(transmissor_lote_esocial_ocorrencias_id),
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
            #transmissor_lote_esocial_ocorrencias_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'transmissor_lote_esocial_ocorrencias_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='transmissor_lote_esocial_ocorrencias_salvar.html',
                filename="transmissor_lote_esocial_ocorrencias.pdf",
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
            response = render_to_response('transmissor_lote_esocial_ocorrencias_salvar.html', context)
            filename = "transmissor_lote_esocial_ocorrencias.xls"
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

