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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
import json
import base64
from emensageriapro.r5001.models import r5001regOcorrs
from emensageriapro.r5001.models import r5001infoTotal
from emensageriapro.r5001.forms import form_r5001_regocorrs
from emensageriapro.r5001.forms import form_r5001_infototal

#IMPORTACOES
@login_required
def apagar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r5001_evttotal_id = int(dict_hash['id'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r5001_evttotal')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r5001_evttotal = get_object_or_404(r5001evtTotal.objects.using( db_slug ), excluido = False, id = r5001_evttotal_id)

    if r5001_evttotal_id:
        if r5001_evttotal.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['r5001_evttotal_apagar'] = 0
            dict_permissoes['r5001_evttotal_editar'] = 0

    if request.method == 'POST':
        if r5001_evttotal.status == STATUS_EVENTO_CADASTRADO:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r5001_evttotal), indent=4, sort_keys=True, default=str)
            obj = r5001evtTotal.objects.using( db_slug ).get(id = r5001_evttotal_id)
            obj.delete(request=request)
            #r5001_evttotal_apagar_custom
            #r5001_evttotal_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r5001_evttotal', r5001_evttotal_id, usuario_id, 3)
        else:
            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 'r5001_evttotal_salvar':
            return redirect('r5001_evttotal', hash=request.session['retorno_hash'])
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
    return render(request, 'r5001_evttotal_apagar.html', context)

class r5001evtTotalList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = r5001evtTotal.objects.using(db_slug).all()
    serializer_class = r5001evtTotalSerializer
    # permission_classes = (IsAdminUser,)


class r5001evtTotalDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = r5001evtTotal.objects.using(db_slug).all()
    serializer_class = r5001evtTotalSerializer
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
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r5001_evttotal')
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
            'show_cdretorno': 0,
            'show_descretorno': 0,
            'show_dhprocess': 0,
            'show_evttotal': 0,
            'show_hash': 0,
            'show_idecontri': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_iderecretorno': 0,
            'show_idestatus': 0,
            'show_idev': 0,
            'show_inforecev': 0,
            'show_nrinsc': 0,
            'show_nrprotentr': 0,
            'show_ocorrencias': 0,
            'show_perapur': 0,
            'show_retornos_evttotal': 0,
            'show_retornos_evttotalcontrib': 0,
            'show_status': 1,
            'show_tpev': 0,
            'show_tpinsc': 0,
            'show_transmissor_lote_efdreinf': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_versao': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'cdretorno__icontains': 'cdretorno__icontains',
                'descretorno__icontains': 'descretorno__icontains',
                'dhprocess__range': 'dhprocess__range',
                'evttotal': 'evttotal',
                'hash__icontains': 'hash__icontains',
                'idecontri': 'idecontri',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'iderecretorno': 'iderecretorno',
                'idestatus': 'idestatus',
                'idev__icontains': 'idev__icontains',
                'inforecev': 'inforecev',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrprotentr__icontains': 'nrprotentr__icontains',
                'perapur__icontains': 'perapur__icontains',
                'status': 'status',
                'tpev__icontains': 'tpev__icontains',
                'tpinsc': 'tpinsc',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',
                'versao__icontains': 'versao__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'cdretorno__icontains': 'cdretorno__icontains',
                'descretorno__icontains': 'descretorno__icontains',
                'dhprocess__range': 'dhprocess__range',
                'evttotal': 'evttotal',
                'hash__icontains': 'hash__icontains',
                'idecontri': 'idecontri',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'iderecretorno': 'iderecretorno',
                'idestatus': 'idestatus',
                'idev__icontains': 'idev__icontains',
                'inforecev': 'inforecev',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrprotentr__icontains': 'nrprotentr__icontains',
                'perapur__icontains': 'perapur__icontains',
                'status': 'status',
                'tpev__icontains': 'tpev__icontains',
                'tpinsc': 'tpinsc',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',
                'versao__icontains': 'versao__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r5001_evttotal_lista = r5001evtTotal.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r5001_evttotal_lista) > 100:
            filtrar = True
            r5001_evttotal_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.using( db_slug ).filter(excluido = False).all()
        #r5001_evttotal_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r5001_evttotal'
        context = {
            'r5001_evttotal_lista': r5001_evttotal_lista,
  
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
            return render(request, 'r5001_evttotal_listar.html', context)

        elif for_print == 2:
            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r5001_evttotal_listar.html',
                filename="r5001_evttotal.pdf",
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
            response = render_to_response('r5001_evttotal_listar.html', context)
            filename = "r5001_evttotal.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response = render_to_response('tables/r5001_evttotal_csv.html', context)
            filename = "r5001_evttotal.csv"
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
        obj = get_object_or_404(r5001evtTotal.objects.using( db_slug ), excluido = False, id = evento_id)
        ident = identidade_evento(obj)
        mensagem = ident
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


@login_required
def salvar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r5001_evttotal_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r5001_evttotal')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if r5001_evttotal_id:
        r5001_evttotal = get_object_or_404(r5001evtTotal.objects.using( db_slug ), excluido = False, id = r5001_evttotal_id)

        if r5001_evttotal.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['r5001_evttotal_apagar'] = 0
            dict_permissoes['r5001_evttotal_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r5001_evttotal_id:
            r5001_evttotal_form = form_r5001_evttotal(request.POST or None,
                                         instance = r5001_evttotal,
                                         slug = db_slug,
                                         initial={'excluido': False})
        else:
            r5001_evttotal_form = form_r5001_evttotal(request.POST or None,
                                         slug = db_slug,
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA,
                                                  'excluido': False})
        if request.method == 'POST':
            if r5001_evttotal_form.is_valid():

                dados = r5001_evttotal_form.cleaned_data
                obj = r5001_evttotal_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not r5001_evttotal_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)

                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 'r5001_evttotal', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(r5001_evttotal), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r5001_evttotal', r5001_evttotal_id, usuario_id, 2)
              
                if request.session['retorno_pagina'] not in ('r5001_evttotal_apagar', 'r5001_evttotal_salvar', 'r5001_evttotal'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if r5001_evttotal_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r5001_evttotal_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
        r5001_evttotal_form = disabled_form_fields(r5001_evttotal_form, permissao.permite_editar)

        if r5001_evttotal_id:
            if r5001_evttotal.status != 0:
                r5001_evttotal_form = disabled_form_fields(r5001_evttotal_form, False)
        #r5001_evttotal_campos_multiple_passo3

        for field in r5001_evttotal_form.fields.keys():
            r5001_evttotal_form.fields[field].widget.attrs['ng-model'] = 'r5001_evttotal_'+field
        if int(dict_hash['print']):
            r5001_evttotal_form = disabled_form_for_print(r5001_evttotal_form)

        r5001_regocorrs_form = None
        r5001_regocorrs_lista = None
        r5001_infototal_form = None
        r5001_infototal_lista = None
        if r5001_evttotal_id:
            r5001_evttotal = get_object_or_404(r5001evtTotal.objects.using( db_slug ), excluido = False, id = r5001_evttotal_id)

            r5001_regocorrs_form = form_r5001_regocorrs(initial={ 'r5001_evttotal': r5001_evttotal }, slug=db_slug)
            r5001_regocorrs_form.fields['r5001_evttotal'].widget.attrs['readonly'] = True
            r5001_regocorrs_lista = r5001regOcorrs.objects.using( db_slug ).filter(excluido = False, r5001_evttotal_id=r5001_evttotal.id).all()
            r5001_infototal_form = form_r5001_infototal(initial={ 'r5001_evttotal': r5001_evttotal }, slug=db_slug)
            r5001_infototal_form.fields['r5001_evttotal'].widget.attrs['readonly'] = True
            r5001_infototal_lista = r5001infoTotal.objects.using( db_slug ).filter(excluido = False, r5001_evttotal_id=r5001_evttotal.id).all()
        else:
            r5001_evttotal = None
        #r5001_evttotal_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 'r5001_evttotal'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False

        if dict_hash['tab'] or 'r5001_evttotal' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r5001_evttotal_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r5001_evttotal_id, tabela='r5001_evttotal').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r5001_evttotal': r5001_evttotal,
            'r5001_evttotal_form': r5001_evttotal_form,
            'mensagem': mensagem,
            'r5001_evttotal_id': int(r5001_evttotal_id),
            'usuario': usuario,
  
            'hash': hash,

            'r5001_regocorrs_form': r5001_regocorrs_form,
            'r5001_regocorrs_lista': r5001_regocorrs_lista,
            'r5001_infototal_form': r5001_infototal_form,
            'r5001_infototal_lista': r5001_infototal_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r5001_evttotal_salvar_custom_variaveis_context#
        }

        if for_print in (0, 1):
            return render(request, 'r5001_evttotal_salvar.html', context)

        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='r5001_evttotal_salvar.html',
                filename="r5001_evttotal.pdf",
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
            response = render_to_response('r5001_evttotal_salvar.html', context)
            filename = "r5001_evttotal.xls"
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

