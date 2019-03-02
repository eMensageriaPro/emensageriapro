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
from emensageriapro.s2306.models import s2306cargoFuncao
from emensageriapro.s2306.models import s2306remuneracao
from emensageriapro.s2306.models import s2306infoTrabCedido
from emensageriapro.s2306.models import s2306infoEstagiario
from emensageriapro.s2306.forms import form_s2306_cargofuncao
from emensageriapro.s2306.forms import form_s2306_remuneracao
from emensageriapro.s2306.forms import form_s2306_infotrabcedido
from emensageriapro.s2306.forms import form_s2306_infoestagiario

#IMPORTACOES
@login_required
def apagar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2306_evttsvaltcontr_id = int(dict_hash['id'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2306_evttsvaltcontr')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2306_evttsvaltcontr = get_object_or_404(s2306evtTSVAltContr.objects.using( db_slug ), excluido = False, id = s2306_evttsvaltcontr_id)

    if s2306_evttsvaltcontr_id:
        if s2306_evttsvaltcontr.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2306_evttsvaltcontr_apagar'] = 0
            dict_permissoes['s2306_evttsvaltcontr_editar'] = 0

    if request.method == 'POST':
        if s2306_evttsvaltcontr.status == STATUS_EVENTO_CADASTRADO:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2306_evttsvaltcontr), indent=4, sort_keys=True, default=str)
            obj = s2306evtTSVAltContr.objects.using( db_slug ).get(id = s2306_evttsvaltcontr_id)
            obj.delete(request=request)
            #s2306_evttsvaltcontr_apagar_custom
            #s2306_evttsvaltcontr_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2306_evttsvaltcontr', s2306_evttsvaltcontr_id, usuario_id, 3)
        else:
            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's2306_evttsvaltcontr_salvar':
            return redirect('s2306_evttsvaltcontr', hash=request.session['retorno_hash'])
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
    return render(request, 's2306_evttsvaltcontr_apagar.html', context)

class s2306evtTSVAltContrList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s2306evtTSVAltContr.objects.using(db_slug).all()
    serializer_class = s2306evtTSVAltContrSerializer
    # permission_classes = (IsAdminUser,)


class s2306evtTSVAltContrDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s2306evtTSVAltContr.objects.using(db_slug).all()
    serializer_class = s2306evtTSVAltContrSerializer
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
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2306_evttsvaltcontr')
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
            'show_codcateg': 0,
            'show_cpftrab': 0,
            'show_dtalteracao': 0,
            'show_evttsvaltcontr': 0,
            'show_ideempregador': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_idetrabsemvinculo': 0,
            'show_indretif': 0,
            'show_infotsvalteracao': 0,
            'show_natatividade': 0,
            'show_nistrab': 0,
            'show_nrinsc': 0,
            'show_nrrecibo': 0,
            'show_ocorrencias': 0,
            'show_procemi': 0,
            'show_retornos_eventos': 0,
            'show_status': 1,
            'show_tpamb': 0,
            'show_tpinsc': 0,
            'show_transmissor_lote_esocial': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_verproc': 0,
            'show_versao': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'codcateg__icontains': 'codcateg__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'dtalteracao__range': 'dtalteracao__range',
                'evttsvaltcontr': 'evttsvaltcontr',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'idetrabsemvinculo': 'idetrabsemvinculo',
                'indretif': 'indretif',
                'infotsvalteracao': 'infotsvalteracao',
                'natatividade': 'natatividade',
                'nistrab__icontains': 'nistrab__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'procemi': 'procemi',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'codcateg__icontains': 'codcateg__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'dtalteracao__range': 'dtalteracao__range',
                'evttsvaltcontr': 'evttsvaltcontr',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'idetrabsemvinculo': 'idetrabsemvinculo',
                'indretif': 'indretif',
                'infotsvalteracao': 'infotsvalteracao',
                'natatividade': 'natatividade',
                'nistrab__icontains': 'nistrab__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'procemi': 'procemi',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2306_evttsvaltcontr_lista = s2306evtTSVAltContr.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2306_evttsvaltcontr_lista) > 100:
            filtrar = True
            s2306_evttsvaltcontr_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #s2306_evttsvaltcontr_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2306_evttsvaltcontr'
        context = {
            's2306_evttsvaltcontr_lista': s2306_evttsvaltcontr_lista,
  
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
            return render(request, 's2306_evttsvaltcontr_listar.html', context)

        elif for_print == 2:
            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2306_evttsvaltcontr_listar.html',
                filename="s2306_evttsvaltcontr.pdf",
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
            response = render_to_response('s2306_evttsvaltcontr_listar.html', context)
            filename = "s2306_evttsvaltcontr.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response = render_to_response('tables/s2306_evttsvaltcontr_csv.html', context)
            filename = "s2306_evttsvaltcontr.csv"
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
        obj = get_object_or_404(s2306evtTSVAltContr.objects.using( db_slug ), excluido = False, id = evento_id)
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
        s2306_evttsvaltcontr_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2306_evttsvaltcontr')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if s2306_evttsvaltcontr_id:
        s2306_evttsvaltcontr = get_object_or_404(s2306evtTSVAltContr.objects.using( db_slug ), excluido = False, id = s2306_evttsvaltcontr_id)

        if s2306_evttsvaltcontr.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2306_evttsvaltcontr_apagar'] = 0
            dict_permissoes['s2306_evttsvaltcontr_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2306_evttsvaltcontr_id:
            s2306_evttsvaltcontr_form = form_s2306_evttsvaltcontr(request.POST or None, instance = s2306_evttsvaltcontr, slug = db_slug)
        else:
            s2306_evttsvaltcontr_form = form_s2306_evttsvaltcontr(request.POST or None,
                                         slug = db_slug,
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL,
                                                  'status': STATUS_EVENTO_CADASTRADO,
                                                  'tpamb': TP_AMB,
                                                  'procemi': 1,
                                                  'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s2306_evttsvaltcontr_form.is_valid():

                dados = s2306_evttsvaltcontr_form.cleaned_data
                obj = s2306_evttsvaltcontr_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not s2306_evttsvaltcontr_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)

                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 's2306_evttsvaltcontr', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(s2306_evttsvaltcontr), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2306_evttsvaltcontr', s2306_evttsvaltcontr_id, usuario_id, 2)
              
                if request.session['retorno_pagina'] not in ('s2306_evttsvaltcontr_apagar', 's2306_evttsvaltcontr_salvar', 's2306_evttsvaltcontr'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2306_evttsvaltcontr_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2306_evttsvaltcontr_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
        s2306_evttsvaltcontr_form = disabled_form_fields(s2306_evttsvaltcontr_form, permissao.permite_editar)

        if s2306_evttsvaltcontr_id:
            if s2306_evttsvaltcontr.status != 0:
                s2306_evttsvaltcontr_form = disabled_form_fields(s2306_evttsvaltcontr_form, False)
        #s2306_evttsvaltcontr_campos_multiple_passo3

        for field in s2306_evttsvaltcontr_form.fields.keys():
            s2306_evttsvaltcontr_form.fields[field].widget.attrs['ng-model'] = 's2306_evttsvaltcontr_'+field
        if int(dict_hash['print']):
            s2306_evttsvaltcontr_form = disabled_form_for_print(s2306_evttsvaltcontr_form)

        s2306_cargofuncao_form = None
        s2306_cargofuncao_lista = None
        s2306_remuneracao_form = None
        s2306_remuneracao_lista = None
        s2306_infotrabcedido_form = None
        s2306_infotrabcedido_lista = None
        s2306_infoestagiario_form = None
        s2306_infoestagiario_lista = None
        if s2306_evttsvaltcontr_id:
            s2306_evttsvaltcontr = get_object_or_404(s2306evtTSVAltContr.objects.using( db_slug ), excluido = False, id = s2306_evttsvaltcontr_id)

            s2306_cargofuncao_form = form_s2306_cargofuncao(initial={ 's2306_evttsvaltcontr': s2306_evttsvaltcontr }, slug=db_slug)
            s2306_cargofuncao_form.fields['s2306_evttsvaltcontr'].widget.attrs['readonly'] = True
            s2306_cargofuncao_lista = s2306cargoFuncao.objects.using( db_slug ).filter(excluido = False, s2306_evttsvaltcontr_id=s2306_evttsvaltcontr.id).all()
            s2306_remuneracao_form = form_s2306_remuneracao(initial={ 's2306_evttsvaltcontr': s2306_evttsvaltcontr }, slug=db_slug)
            s2306_remuneracao_form.fields['s2306_evttsvaltcontr'].widget.attrs['readonly'] = True
            s2306_remuneracao_lista = s2306remuneracao.objects.using( db_slug ).filter(excluido = False, s2306_evttsvaltcontr_id=s2306_evttsvaltcontr.id).all()
            s2306_infotrabcedido_form = form_s2306_infotrabcedido(initial={ 's2306_evttsvaltcontr': s2306_evttsvaltcontr }, slug=db_slug)
            s2306_infotrabcedido_form.fields['s2306_evttsvaltcontr'].widget.attrs['readonly'] = True
            s2306_infotrabcedido_lista = s2306infoTrabCedido.objects.using( db_slug ).filter(excluido = False, s2306_evttsvaltcontr_id=s2306_evttsvaltcontr.id).all()
            s2306_infoestagiario_form = form_s2306_infoestagiario(initial={ 's2306_evttsvaltcontr': s2306_evttsvaltcontr }, slug=db_slug)
            s2306_infoestagiario_form.fields['s2306_evttsvaltcontr'].widget.attrs['readonly'] = True
            s2306_infoestagiario_lista = s2306infoEstagiario.objects.using( db_slug ).filter(excluido = False, s2306_evttsvaltcontr_id=s2306_evttsvaltcontr.id).all()
        else:
            s2306_evttsvaltcontr = None
        #s2306_evttsvaltcontr_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's2306_evttsvaltcontr'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False

        if dict_hash['tab'] or 's2306_evttsvaltcontr' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2306_evttsvaltcontr_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2306_evttsvaltcontr_id, tabela='s2306_evttsvaltcontr').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2306_evttsvaltcontr': s2306_evttsvaltcontr,
            's2306_evttsvaltcontr_form': s2306_evttsvaltcontr_form,
            'mensagem': mensagem,
            's2306_evttsvaltcontr_id': int(s2306_evttsvaltcontr_id),
            'usuario': usuario,
  
            'hash': hash,

            's2306_cargofuncao_form': s2306_cargofuncao_form,
            's2306_cargofuncao_lista': s2306_cargofuncao_lista,
            's2306_remuneracao_form': s2306_remuneracao_form,
            's2306_remuneracao_lista': s2306_remuneracao_lista,
            's2306_infotrabcedido_form': s2306_infotrabcedido_form,
            's2306_infotrabcedido_lista': s2306_infotrabcedido_lista,
            's2306_infoestagiario_form': s2306_infoestagiario_form,
            's2306_infoestagiario_lista': s2306_infoestagiario_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2306_evttsvaltcontr_salvar_custom_variaveis_context#
        }

        if for_print in (0, 1):
            return render(request, 's2306_evttsvaltcontr_salvar.html', context)

        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='s2306_evttsvaltcontr_salvar.html',
                filename="s2306_evttsvaltcontr.pdf",
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
            response = render_to_response('s2306_evttsvaltcontr_salvar.html', context)
            filename = "s2306_evttsvaltcontr.xls"
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

