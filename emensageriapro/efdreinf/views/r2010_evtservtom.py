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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
import json
import base64
from emensageriapro.r2010.models import r2010nfs
from emensageriapro.r2010.models import r2010infoProcRetPr
from emensageriapro.r2010.models import r2010infoProcRetAd
from emensageriapro.r2010.forms import form_r2010_nfs
from emensageriapro.r2010.forms import form_r2010_infoprocretpr
from emensageriapro.r2010.forms import form_r2010_infoprocretad

#IMPORTACOES
@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r2010_evtservtom_id = int(dict_hash['id'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2010_evtservtom')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r2010_evtservtom = get_object_or_404(r2010evtServTom.objects.using( db_slug ), excluido = False, id = r2010_evtservtom_id)

    if r2010_evtservtom_id:
        if r2010_evtservtom.status != 0:
            dict_permissoes['r2010_evtservtom_apagar'] = 0
            dict_permissoes['r2010_evtservtom_editar'] = 0

    if request.method == 'POST':
        if r2010_evtservtom.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r2010_evtservtom), indent=4, sort_keys=True, default=str)
            obj = r2010evtServTom.objects.using( db_slug ).get(id = r2010_evtservtom_id)
            obj.delete(request=request)
            #r2010_evtservtom_apagar_custom
            #r2010_evtservtom_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r2010_evtservtom', r2010_evtservtom_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 'r2010_evtservtom_salvar':
            return redirect('r2010_evtservtom', hash=request.session['retorno_hash'])
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
    return render(request, 'r2010_evtservtom_apagar.html', context)

class r2010evtServTomList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = r2010evtServTom.objects.using(db_slug).all()
    serializer_class = r2010evtServTomSerializer
    # permission_classes = (IsAdminUser,)


class r2010evtServTomDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = r2010evtServTom.objects.using(db_slug).all()
    serializer_class = r2010evtServTomSerializer
    # permission_classes = (IsAdminUser,)


@login_required
def listar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2010_evtservtom')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_arquivo': 0,
            'show_arquivo_original': 0,
            'show_cdretorno': 1,
            'show_cnpjprestador': 1,
            'show_descretorno': 0,
            'show_dhprocess': 0,
            'show_evtservtom': 0,
            'show_idecontri': 0,
            'show_ideestabobra': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_ideprestserv': 0,
            'show_indcprb': 1,
            'show_indobra': 1,
            'show_indretif': 1,
            'show_infoservtom': 0,
            'show_nrinsc': 1,
            'show_nrinscestab': 1,
            'show_nrrecibo': 0,
            'show_ocorrencias': 0,
            'show_perapur': 1,
            'show_procemi': 1,
            'show_retornos_evttotal': 0,
            'show_retornos_evttotalcontrib': 0,
            'show_status': 1,
            'show_tpamb': 1,
            'show_tpinsc': 1,
            'show_tpinscestab': 1,
            'show_transmissor_lote_efdreinf': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_verproc': 1,
            'show_versao': 0,
            'show_vlrtotalbaseret': 1,
            'show_vlrtotalbruto': 1,
            'show_vlrtotalnretadic': 0,
            'show_vlrtotalnretprinc': 0,
            'show_vlrtotalretadic': 0,
            'show_vlrtotalretprinc': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'cnpjprestador__icontains': 'cnpjprestador__icontains',
                'evtservtom': 'evtservtom',
                'idecontri': 'idecontri',
                'ideestabobra': 'ideestabobra',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'ideprestserv': 'ideprestserv',
                'indcprb': 'indcprb',
                'indobra': 'indobra',
                'indretif': 'indretif',
                'infoservtom': 'infoservtom',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrinscestab__icontains': 'nrinscestab__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'perapur__icontains': 'perapur__icontains',
                'procemi': 'procemi',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'tpinscestab': 'tpinscestab',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',
                'vlrtotalbaseret': 'vlrtotalbaseret',
                'vlrtotalbruto': 'vlrtotalbruto',
                'vlrtotalnretadic': 'vlrtotalnretadic',
                'vlrtotalnretprinc': 'vlrtotalnretprinc',
                'vlrtotalretadic': 'vlrtotalretadic',
                'vlrtotalretprinc': 'vlrtotalretprinc',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'cnpjprestador__icontains': 'cnpjprestador__icontains',
                'evtservtom': 'evtservtom',
                'idecontri': 'idecontri',
                'ideestabobra': 'ideestabobra',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'ideprestserv': 'ideprestserv',
                'indcprb': 'indcprb',
                'indobra': 'indobra',
                'indretif': 'indretif',
                'infoservtom': 'infoservtom',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrinscestab__icontains': 'nrinscestab__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'perapur__icontains': 'perapur__icontains',
                'procemi': 'procemi',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'tpinscestab': 'tpinscestab',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',
                'vlrtotalbaseret': 'vlrtotalbaseret',
                'vlrtotalbruto': 'vlrtotalbruto',
                'vlrtotalnretadic': 'vlrtotalnretadic',
                'vlrtotalnretprinc': 'vlrtotalnretprinc',
                'vlrtotalretadic': 'vlrtotalretadic',
                'vlrtotalretprinc': 'vlrtotalretprinc',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r2010_evtservtom_lista = r2010evtServTom.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r2010_evtservtom_lista) > 100:
            filtrar = True
            r2010_evtservtom_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.using( db_slug ).filter(excluido = False).all()
        #r2010_evtservtom_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r2010_evtservtom'
        context = {
            'r2010_evtservtom_lista': r2010_evtservtom_lista,
  
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

            'transmissor_lote_efdreinf_lista': transmissor_lote_efdreinf_lista,
        }

        if for_print in (0,1):
            return render(request, 'r2010_evtservtom_listar.html', context)

        elif for_print == 2:
            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2010_evtservtom_listar.html',
                filename="r2010_evtservtom.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             'viewport-size': "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response

        elif for_print == 3:
            response = render_to_response('r2010_evtservtom_listar.html', context)
            filename = "r2010_evtservtom.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response = render_to_response('tables/r2010_evtservtom_csv.html', context)
            filename = "r2010_evtservtom.csv"
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

def gerar_identidade(request, chave, evento_id):
    from emensageriapro.functions import identidade_evento
    from emensageriapro.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        obj = get_object_or_404(r2010evtServTom.objects.using( db_slug ), excluido = False, id = evento_id)
        ident = identidade_evento(obj)
        mensagem = ident
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


@login_required
def salvar(request, hash):
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r2010_evtservtom_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2010_evtservtom')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if r2010_evtservtom_id:
        r2010_evtservtom = get_object_or_404(r2010evtServTom.objects.using( db_slug ), excluido = False, id = r2010_evtservtom_id)

        if r2010_evtservtom.status != 0:
            dict_permissoes['r2010_evtservtom_apagar'] = 0
            dict_permissoes['r2010_evtservtom_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r2010_evtservtom_id:
            r2010_evtservtom_form = form_r2010_evtservtom(request.POST or None, instance = r2010_evtservtom, slug = db_slug)
        else:
            r2010_evtservtom_form = form_r2010_evtservtom(request.POST or None, slug = db_slug, initial={'versao': VERSAO_LAYOUT_EFDREINF, 'status': 0, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if r2010_evtservtom_form.is_valid():

                dados = r2010_evtservtom_form.cleaned_data
                obj = r2010_evtservtom_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')

                if not r2010_evtservtom_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)

                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 'r2010_evtservtom', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(r2010_evtservtom), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r2010_evtservtom', r2010_evtservtom_id, usuario_id, 2)
              
                if request.session['retorno_pagina'] not in ('r2010_evtservtom_apagar', 'r2010_evtservtom_salvar', 'r2010_evtservtom'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if r2010_evtservtom_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r2010_evtservtom_salvar', hash=url_hash)

            else:
                messages.error(request, 'Erro ao salvar!')
        r2010_evtservtom_form = disabled_form_fields(r2010_evtservtom_form, permissao.permite_editar)

        if r2010_evtservtom_id:
            if r2010_evtservtom.status != 0:
                r2010_evtservtom_form = disabled_form_fields(r2010_evtservtom_form, False)
        #r2010_evtservtom_campos_multiple_passo3

        for field in r2010_evtservtom_form.fields.keys():
            r2010_evtservtom_form.fields[field].widget.attrs['ng-model'] = 'r2010_evtservtom_'+field
        if int(dict_hash['print']):
            r2010_evtservtom_form = disabled_form_for_print(r2010_evtservtom_form)

        r2010_nfs_form = None
        r2010_nfs_lista = None
        r2010_infoprocretpr_form = None
        r2010_infoprocretpr_lista = None
        r2010_infoprocretad_form = None
        r2010_infoprocretad_lista = None
        if r2010_evtservtom_id:
            r2010_evtservtom = get_object_or_404(r2010evtServTom.objects.using( db_slug ), excluido = False, id = r2010_evtservtom_id)

            r2010_nfs_form = form_r2010_nfs(initial={ 'r2010_evtservtom': r2010_evtservtom }, slug=db_slug)
            r2010_nfs_form.fields['r2010_evtservtom'].widget.attrs['readonly'] = True
            r2010_nfs_lista = r2010nfs.objects.using( db_slug ).filter(excluido = False, r2010_evtservtom_id=r2010_evtservtom.id).all()
            r2010_infoprocretpr_form = form_r2010_infoprocretpr(initial={ 'r2010_evtservtom': r2010_evtservtom }, slug=db_slug)
            r2010_infoprocretpr_form.fields['r2010_evtservtom'].widget.attrs['readonly'] = True
            r2010_infoprocretpr_lista = r2010infoProcRetPr.objects.using( db_slug ).filter(excluido = False, r2010_evtservtom_id=r2010_evtservtom.id).all()
            r2010_infoprocretad_form = form_r2010_infoprocretad(initial={ 'r2010_evtservtom': r2010_evtservtom }, slug=db_slug)
            r2010_infoprocretad_form.fields['r2010_evtservtom'].widget.attrs['readonly'] = True
            r2010_infoprocretad_lista = r2010infoProcRetAd.objects.using( db_slug ).filter(excluido = False, r2010_evtservtom_id=r2010_evtservtom.id).all()
        else:
            r2010_evtservtom = None
        #r2010_evtservtom_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 'r2010_evtservtom'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False

        if dict_hash['tab'] or 'r2010_evtservtom' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r2010_evtservtom_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r2010_evtservtom_id, tabela='r2010_evtservtom').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r2010_evtservtom': r2010_evtservtom,
            'r2010_evtservtom_form': r2010_evtservtom_form,
            'mensagem': mensagem,
            'r2010_evtservtom_id': int(r2010_evtservtom_id),
            'usuario': usuario,
  
            'hash': hash,

            'r2010_nfs_form': r2010_nfs_form,
            'r2010_nfs_lista': r2010_nfs_lista,
            'r2010_infoprocretpr_form': r2010_infoprocretpr_form,
            'r2010_infoprocretpr_lista': r2010_infoprocretpr_lista,
            'r2010_infoprocretad_form': r2010_infoprocretad_form,
            'r2010_infoprocretad_lista': r2010_infoprocretad_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r2010_evtservtom_salvar_custom_variaveis_context#
        }

        if for_print in (0,1 ):
            return render(request, 'r2010_evtservtom_salvar.html', context)

        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='r2010_evtservtom_salvar.html',
                filename="r2010_evtservtom.pdf",
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
            response = render_to_response('r2010_evtservtom_salvar.html', context)
            filename = "r2010_evtservtom.xls"
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

