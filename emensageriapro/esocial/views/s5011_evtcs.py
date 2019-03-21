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
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
import json
import base64
from emensageriapro.s5011.models import s5011infoCPSeg
from emensageriapro.s5011.models import s5011infoPJ
from emensageriapro.s5011.models import s5011ideEstab
from emensageriapro.s5011.models import s5011infoCRContrib
from emensageriapro.s5011.forms import form_s5011_infocpseg
from emensageriapro.s5011.forms import form_s5011_infopj
from emensageriapro.s5011.forms import form_s5011_ideestab
from emensageriapro.s5011.forms import form_s5011_infocrcontrib

#IMPORTACOES
@login_required
def apagar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s5011_evtcs_id = int(dict_hash['id'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_evtcs')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s5011_evtcs = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = s5011_evtcs_id)

    if s5011_evtcs_id:
        if s5011_evtcs.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s5011_evtcs_apagar'] = 0
            dict_permissoes['s5011_evtcs_editar'] = 0

    if request.method == 'POST':
        if s5011_evtcs.status == STATUS_EVENTO_CADASTRADO:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s5011_evtcs), indent=4, sort_keys=True, default=str)
            obj = s5011evtCS.objects.using( db_slug ).get(id = s5011_evtcs_id)
            obj.delete(request=request)
            #s5011_evtcs_apagar_custom
            #s5011_evtcs_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's5011_evtcs', s5011_evtcs_id, usuario_id, 3)
        else:
            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's5011_evtcs_salvar':
            return redirect('s5011_evtcs', hash=request.session['retorno_hash'])
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
    return render(request, 's5011_evtcs_apagar.html', context)

class s5011evtCSList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s5011evtCS.objects.using(db_slug).all()
    serializer_class = s5011evtCSSerializer
    # permission_classes = (IsAdminUser,)


class s5011evtCSDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s5011evtCS.objects.using(db_slug).all()
    serializer_class = s5011evtCSSerializer
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
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_evtcs')
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
            'show_classtrib': 0,
            'show_evtcs': 0,
            'show_ideempregador': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_indapuracao': 0,
            'show_indexistinfo': 0,
            'show_infocontrib': 0,
            'show_infocs': 0,
            'show_nrinsc': 0,
            'show_nrrecarqbase': 0,
            'show_ocorrencias': 0,
            'show_perapur': 0,
            'show_retornos_eventos': 0,
            'show_status': 1,
            'show_tpinsc': 0,
            'show_transmissor_lote_esocial': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_versao': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'classtrib__icontains': 'classtrib__icontains',
                'evtcs': 'evtcs',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'indapuracao': 'indapuracao',
                'indexistinfo': 'indexistinfo',
                'infocontrib': 'infocontrib',
                'infocs': 'infocs',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecarqbase__icontains': 'nrrecarqbase__icontains',
                'perapur__icontains': 'perapur__icontains',
                'status': 'status',
                'tpinsc': 'tpinsc',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'versao__icontains': 'versao__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'classtrib__icontains': 'classtrib__icontains',
                'evtcs': 'evtcs',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'indapuracao': 'indapuracao',
                'indexistinfo': 'indexistinfo',
                'infocontrib': 'infocontrib',
                'infocs': 'infocs',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecarqbase__icontains': 'nrrecarqbase__icontains',
                'perapur__icontains': 'perapur__icontains',
                'status': 'status',
                'tpinsc': 'tpinsc',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'versao__icontains': 'versao__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s5011_evtcs_lista = s5011evtCS.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s5011_evtcs_lista) > 100:
            filtrar = True
            s5011_evtcs_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #s5011_evtcs_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5011_evtcs'
        context = {
            's5011_evtcs_lista': s5011_evtcs_lista,
  
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
            return render(request, 's5011_evtcs_listar.html', context)

        elif for_print == 2:
            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s5011_evtcs_listar.html',
                filename="s5011_evtcs.pdf",
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
            response = render_to_response('s5011_evtcs_listar.html', context)
            filename = "s5011_evtcs.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response = render_to_response('tables/s5011_evtcs_csv.html', context)
            filename = "s5011_evtcs.csv"
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
        obj = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = evento_id)
        ident = identidade_evento(obj)
        mensagem = ident
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


@login_required
def salvar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL, TP_AMB
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s5011_evtcs_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_evtcs')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if s5011_evtcs_id:
        s5011_evtcs = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = s5011_evtcs_id)

        if s5011_evtcs.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s5011_evtcs_apagar'] = 0
            dict_permissoes['s5011_evtcs_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s5011_evtcs_id:
            s5011_evtcs_form = form_s5011_evtcs(request.POST or None, instance = s5011_evtcs,
                                         slug = db_slug,
                                         initial={'excluido': False})
        else:
            s5011_evtcs_form = form_s5011_evtcs(request.POST or None, slug = db_slug,
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA,
                                                  'excluido': False})
        if request.method == 'POST':
            if s5011_evtcs_form.is_valid():

                dados = s5011_evtcs_form.cleaned_data
                obj = s5011_evtcs_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not s5011_evtcs_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)

                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 's5011_evtcs', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(s5011_evtcs), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's5011_evtcs', s5011_evtcs_id, usuario_id, 2)
              
                if request.session['retorno_pagina'] not in ('s5011_evtcs_apagar', 's5011_evtcs_salvar', 's5011_evtcs'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s5011_evtcs_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s5011_evtcs_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
        s5011_evtcs_form = disabled_form_fields(s5011_evtcs_form, permissao.permite_editar)

        if s5011_evtcs_id:
            if s5011_evtcs.status != 0:
                s5011_evtcs_form = disabled_form_fields(s5011_evtcs_form, False)
        #s5011_evtcs_campos_multiple_passo3

        for field in s5011_evtcs_form.fields.keys():
            s5011_evtcs_form.fields[field].widget.attrs['ng-model'] = 's5011_evtcs_'+field
        if int(dict_hash['print']):
            s5011_evtcs_form = disabled_form_for_print(s5011_evtcs_form)

        s5011_infocpseg_form = None
        s5011_infocpseg_lista = None
        s5011_infopj_form = None
        s5011_infopj_lista = None
        s5011_ideestab_form = None
        s5011_ideestab_lista = None
        s5011_infocrcontrib_form = None
        s5011_infocrcontrib_lista = None
        if s5011_evtcs_id:
            s5011_evtcs = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = s5011_evtcs_id)

            s5011_infocpseg_form = form_s5011_infocpseg(initial={ 's5011_evtcs': s5011_evtcs }, slug=db_slug)
            s5011_infocpseg_form.fields['s5011_evtcs'].widget.attrs['readonly'] = True
            s5011_infocpseg_lista = s5011infoCPSeg.objects.using( db_slug ).filter(excluido = False, s5011_evtcs_id=s5011_evtcs.id).all()
            s5011_infopj_form = form_s5011_infopj(initial={ 's5011_evtcs': s5011_evtcs }, slug=db_slug)
            s5011_infopj_form.fields['s5011_evtcs'].widget.attrs['readonly'] = True
            s5011_infopj_lista = s5011infoPJ.objects.using( db_slug ).filter(excluido = False, s5011_evtcs_id=s5011_evtcs.id).all()
            s5011_ideestab_form = form_s5011_ideestab(initial={ 's5011_evtcs': s5011_evtcs }, slug=db_slug)
            s5011_ideestab_form.fields['s5011_evtcs'].widget.attrs['readonly'] = True
            s5011_ideestab_lista = s5011ideEstab.objects.using( db_slug ).filter(excluido = False, s5011_evtcs_id=s5011_evtcs.id).all()
            s5011_infocrcontrib_form = form_s5011_infocrcontrib(initial={ 's5011_evtcs': s5011_evtcs }, slug=db_slug)
            s5011_infocrcontrib_form.fields['s5011_evtcs'].widget.attrs['readonly'] = True
            s5011_infocrcontrib_lista = s5011infoCRContrib.objects.using( db_slug ).filter(excluido = False, s5011_evtcs_id=s5011_evtcs.id).all()
        else:
            s5011_evtcs = None
        #s5011_evtcs_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's5011_evtcs'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False

        if dict_hash['tab'] or 's5011_evtcs' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's5011_evtcs_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s5011_evtcs_id, tabela='s5011_evtcs').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's5011_evtcs': s5011_evtcs,
            's5011_evtcs_form': s5011_evtcs_form,
            'mensagem': mensagem,
            's5011_evtcs_id': int(s5011_evtcs_id),
            'usuario': usuario,
  
            'hash': hash,

            's5011_infocpseg_form': s5011_infocpseg_form,
            's5011_infocpseg_lista': s5011_infocpseg_lista,
            's5011_infopj_form': s5011_infopj_form,
            's5011_infopj_lista': s5011_infopj_lista,
            's5011_ideestab_form': s5011_ideestab_form,
            's5011_ideestab_lista': s5011_ideestab_lista,
            's5011_infocrcontrib_form': s5011_infocrcontrib_form,
            's5011_infocrcontrib_lista': s5011_infocrcontrib_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s5011_evtcs_salvar_custom_variaveis_context#
        }

        if for_print in (0, 1):
            return render(request, 's5011_evtcs_salvar.html', context)

        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='s5011_evtcs_salvar.html',
                filename="s5011_evtcs.pdf",
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
            response = render_to_response('s5011_evtcs_salvar.html', context)
            filename = "s5011_evtcs.xls"
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

