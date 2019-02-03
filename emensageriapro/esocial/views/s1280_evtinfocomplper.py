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
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
import json
import base64
from emensageriapro.s1280.models import s1280infoSubstPatr
from emensageriapro.s1280.models import s1280infoSubstPatrOpPort
from emensageriapro.s1280.models import s1280infoAtivConcom
from emensageriapro.s1280.forms import form_s1280_infosubstpatr
from emensageriapro.s1280.forms import form_s1280_infosubstpatropport
from emensageriapro.s1280.forms import form_s1280_infoativconcom

#IMPORTACOES
@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1280_evtinfocomplper_id = int(dict_hash['id'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1280_evtinfocomplper')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s1280_evtinfocomplper = get_object_or_404(s1280evtInfoComplPer.objects.using( db_slug ), excluido = False, id = s1280_evtinfocomplper_id)

    if s1280_evtinfocomplper_id:
        if s1280_evtinfocomplper.status != 0:
            dict_permissoes['s1280_evtinfocomplper_apagar'] = 0
            dict_permissoes['s1280_evtinfocomplper_editar'] = 0

    if request.method == 'POST':
        if s1280_evtinfocomplper.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s1280_evtinfocomplper), indent=4, sort_keys=True, default=str)
            obj = s1280evtInfoComplPer.objects.using( db_slug ).get(id = s1280_evtinfocomplper_id)
            obj.delete(request=request)
            #s1280_evtinfocomplper_apagar_custom
            #s1280_evtinfocomplper_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's1280_evtinfocomplper', s1280_evtinfocomplper_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's1280_evtinfocomplper_salvar':
            return redirect('s1280_evtinfocomplper', hash=request.session['retorno_hash'])
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
    return render(request, 's1280_evtinfocomplper_apagar.html', context)

class s1280evtInfoComplPerList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s1280evtInfoComplPer.objects.using(db_slug).all()
    serializer_class = s1280evtInfoComplPerSerializer
    # permission_classes = (IsAdminUser,)


class s1280evtInfoComplPerDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s1280evtInfoComplPer.objects.using(db_slug).all()
    serializer_class = s1280evtInfoComplPerSerializer
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
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1280_evtinfocomplper')
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
            'show_evtinfocomplper': 0,
            'show_ideempregador': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_indapuracao': 1,
            'show_indretif': 1,
            'show_nrinsc': 1,
            'show_nrrecibo': 0,
            'show_ocorrencias': 0,
            'show_perapur': 1,
            'show_procemi': 1,
            'show_processamento_codigo_resposta': 1,
            'show_processamento_data_hora': 0,
            'show_processamento_descricao_resposta': 1,
            'show_processamento_versao_app_processamento': 0,
            'show_recepcao_data_hora': 0,
            'show_recepcao_protocolo_envio_lote': 0,
            'show_recepcao_tp_amb': 0,
            'show_recepcao_versao_app': 0,
            'show_recibo_hash': 0,
            'show_recibo_numero': 0,
            'show_retornos_eventos': 0,
            'show_status': 1,
            'show_tpamb': 1,
            'show_tpinsc': 1,
            'show_transmissor_lote_esocial': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_verproc': 1,
            'show_versao': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'evtinfocomplper': 'evtinfocomplper',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'indapuracao': 'indapuracao',
                'indretif': 'indretif',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'perapur__icontains': 'perapur__icontains',
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
                'evtinfocomplper': 'evtinfocomplper',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'indapuracao': 'indapuracao',
                'indretif': 'indretif',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'perapur__icontains': 'perapur__icontains',
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
        s1280_evtinfocomplper_lista = s1280evtInfoComplPer.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s1280_evtinfocomplper_lista) > 100:
            filtrar = True
            s1280_evtinfocomplper_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #s1280_evtinfocomplper_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1280_evtinfocomplper'
        context = {
            's1280_evtinfocomplper_lista': s1280_evtinfocomplper_lista,
  
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
            return render(request, 's1280_evtinfocomplper_listar.html', context)

        elif for_print == 2:
            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1280_evtinfocomplper_listar.html',
                filename="s1280_evtinfocomplper.pdf",
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
            response = render_to_response('s1280_evtinfocomplper_listar.html', context)
            filename = "s1280_evtinfocomplper.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response = render_to_response('tables/s1280_evtinfocomplper_csv.html', context)
            filename = "s1280_evtinfocomplper.csv"
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
        obj = get_object_or_404(s1280evtInfoComplPer.objects.using( db_slug ), excluido = False, id = evento_id)
        ident = identidade_evento(obj)
        mensagem = ident
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


@login_required
def salvar(request, hash):
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL, TP_AMB
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1280_evtinfocomplper_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1280_evtinfocomplper')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if s1280_evtinfocomplper_id:
        s1280_evtinfocomplper = get_object_or_404(s1280evtInfoComplPer.objects.using( db_slug ), excluido = False, id = s1280_evtinfocomplper_id)

        if s1280_evtinfocomplper.status != 0:
            dict_permissoes['s1280_evtinfocomplper_apagar'] = 0
            dict_permissoes['s1280_evtinfocomplper_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s1280_evtinfocomplper_id:
            s1280_evtinfocomplper_form = form_s1280_evtinfocomplper(request.POST or None, instance = s1280_evtinfocomplper, slug = db_slug)
        else:
            s1280_evtinfocomplper_form = form_s1280_evtinfocomplper(request.POST or None, slug = db_slug, initial={'versao': VERSAO_LAYOUT_ESOCIAL, 'status': 0, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s1280_evtinfocomplper_form.is_valid():

                dados = s1280_evtinfocomplper_form.cleaned_data
                obj = s1280_evtinfocomplper_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')

                if not s1280_evtinfocomplper_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)

                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 's1280_evtinfocomplper', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(s1280_evtinfocomplper), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's1280_evtinfocomplper', s1280_evtinfocomplper_id, usuario_id, 2)
              
                if request.session['retorno_pagina'] not in ('s1280_evtinfocomplper_apagar', 's1280_evtinfocomplper_salvar', 's1280_evtinfocomplper'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s1280_evtinfocomplper_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s1280_evtinfocomplper_salvar', hash=url_hash)

            else:
                messages.error(request, 'Erro ao salvar!')
        s1280_evtinfocomplper_form = disabled_form_fields(s1280_evtinfocomplper_form, permissao.permite_editar)

        if s1280_evtinfocomplper_id:
            if s1280_evtinfocomplper.status != 0:
                s1280_evtinfocomplper_form = disabled_form_fields(s1280_evtinfocomplper_form, False)
        #s1280_evtinfocomplper_campos_multiple_passo3

        for field in s1280_evtinfocomplper_form.fields.keys():
            s1280_evtinfocomplper_form.fields[field].widget.attrs['ng-model'] = 's1280_evtinfocomplper_'+field
        if int(dict_hash['print']):
            s1280_evtinfocomplper_form = disabled_form_for_print(s1280_evtinfocomplper_form)

        s1280_infosubstpatr_form = None
        s1280_infosubstpatr_lista = None
        s1280_infosubstpatropport_form = None
        s1280_infosubstpatropport_lista = None
        s1280_infoativconcom_form = None
        s1280_infoativconcom_lista = None
        if s1280_evtinfocomplper_id:
            s1280_evtinfocomplper = get_object_or_404(s1280evtInfoComplPer.objects.using( db_slug ), excluido = False, id = s1280_evtinfocomplper_id)

            s1280_infosubstpatr_form = form_s1280_infosubstpatr(initial={ 's1280_evtinfocomplper': s1280_evtinfocomplper }, slug=db_slug)
            s1280_infosubstpatr_form.fields['s1280_evtinfocomplper'].widget.attrs['readonly'] = True
            s1280_infosubstpatr_lista = s1280infoSubstPatr.objects.using( db_slug ).filter(excluido = False, s1280_evtinfocomplper_id=s1280_evtinfocomplper.id).all()
            s1280_infosubstpatropport_form = form_s1280_infosubstpatropport(initial={ 's1280_evtinfocomplper': s1280_evtinfocomplper }, slug=db_slug)
            s1280_infosubstpatropport_form.fields['s1280_evtinfocomplper'].widget.attrs['readonly'] = True
            s1280_infosubstpatropport_lista = s1280infoSubstPatrOpPort.objects.using( db_slug ).filter(excluido = False, s1280_evtinfocomplper_id=s1280_evtinfocomplper.id).all()
            s1280_infoativconcom_form = form_s1280_infoativconcom(initial={ 's1280_evtinfocomplper': s1280_evtinfocomplper }, slug=db_slug)
            s1280_infoativconcom_form.fields['s1280_evtinfocomplper'].widget.attrs['readonly'] = True
            s1280_infoativconcom_lista = s1280infoAtivConcom.objects.using( db_slug ).filter(excluido = False, s1280_evtinfocomplper_id=s1280_evtinfocomplper.id).all()
        else:
            s1280_evtinfocomplper = None
        #s1280_evtinfocomplper_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's1280_evtinfocomplper'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False

        if dict_hash['tab'] or 's1280_evtinfocomplper' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1280_evtinfocomplper_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s1280_evtinfocomplper_id, tabela='s1280_evtinfocomplper').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's1280_evtinfocomplper': s1280_evtinfocomplper,
            's1280_evtinfocomplper_form': s1280_evtinfocomplper_form,
            'mensagem': mensagem,
            's1280_evtinfocomplper_id': int(s1280_evtinfocomplper_id),
            'usuario': usuario,
  
            'hash': hash,

            's1280_infosubstpatr_form': s1280_infosubstpatr_form,
            's1280_infosubstpatr_lista': s1280_infosubstpatr_lista,
            's1280_infosubstpatropport_form': s1280_infosubstpatropport_form,
            's1280_infosubstpatropport_lista': s1280_infosubstpatropport_lista,
            's1280_infoativconcom_form': s1280_infoativconcom_form,
            's1280_infoativconcom_lista': s1280_infoativconcom_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1280_evtinfocomplper_salvar_custom_variaveis_context#
        }

        if for_print in (0,1 ):
            return render(request, 's1280_evtinfocomplper_salvar.html', context)

        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='s1280_evtinfocomplper_salvar.html',
                filename="s1280_evtinfocomplper.pdf",
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
            response = render_to_response('s1280_evtinfocomplper_salvar.html', context)
            filename = "s1280_evtinfocomplper.xls"
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

