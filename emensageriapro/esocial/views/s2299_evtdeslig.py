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
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
import json
import base64
from emensageriapro.s2299.models import s2299observacoes
from emensageriapro.s2299.models import s2299sucessaoVinc
from emensageriapro.s2299.models import s2299transfTit
from emensageriapro.s2299.models import s2299mudancaCPF
from emensageriapro.s2299.models import s2299dmDev
from emensageriapro.s2299.models import s2299infoTrabIntermprocJudTrab
from emensageriapro.s2299.models import s2299infoTrabInterminfoMV
from emensageriapro.s2299.models import s2299infoTrabIntermprocCS
from emensageriapro.s2299.models import s2299infoTrabIntermquarentena
from emensageriapro.s2299.models import s2299infoTrabIntermconsigFGTS
from emensageriapro.s2299.forms import form_s2299_observacoes
from emensageriapro.s2299.forms import form_s2299_sucessaovinc
from emensageriapro.s2299.forms import form_s2299_transftit
from emensageriapro.s2299.forms import form_s2299_mudancacpf
from emensageriapro.s2299.forms import form_s2299_dmdev
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_procjudtrab
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_infomv
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_proccs
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_quarentena
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_consigfgts

#IMPORTACOES
@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2299_evtdeslig_id = int(dict_hash['id'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2299_evtdeslig')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2299_evtdeslig = get_object_or_404(s2299evtDeslig.objects.using( db_slug ), excluido = False, id = s2299_evtdeslig_id)

    if s2299_evtdeslig_id:
        if s2299_evtdeslig.status != 0:
            dict_permissoes['s2299_evtdeslig_apagar'] = 0
            dict_permissoes['s2299_evtdeslig_editar'] = 0

    if request.method == 'POST':
        if s2299_evtdeslig.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2299_evtdeslig), indent=4, sort_keys=True, default=str)
            s2299evtDeslig.objects.using( db_slug ).filter(id = s2299_evtdeslig_id).delete()
            #s2299_evtdeslig_apagar_custom
            #s2299_evtdeslig_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2299_evtdeslig', s2299_evtdeslig_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's2299_evtdeslig_salvar':
            return redirect('s2299_evtdeslig', hash=request.session['retorno_hash'])
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
    return render(request, 's2299_evtdeslig_apagar.html', context)

class s2299evtDesligList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s2299evtDeslig.objects.using(db_slug).all()
    serializer_class = s2299evtDesligSerializer
    permission_classes = (IsAdminUser,)


class s2299evtDesligDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s2299evtDeslig.objects.using(db_slug).all()
    serializer_class = s2299evtDesligSerializer
    permission_classes = (IsAdminUser,)


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
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2299_evtdeslig')
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
            'show_cpftrab': 1,
            'show_dtdeslig': 1,
            'show_dtprojfimapi': 0,
            'show_evtdeslig': 0,
            'show_ideempregador': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_idevinculo': 0,
            'show_indcumprparc': 1,
            'show_indpagtoapi': 1,
            'show_indretif': 1,
            'show_infodeslig': 0,
            'show_matricula': 1,
            'show_mtvdeslig': 1,
            'show_nistrab': 1,
            'show_nrcertobito': 0,
            'show_nrinsc': 1,
            'show_nrproctrab': 0,
            'show_nrrecibo': 0,
            'show_ocorrencias': 0,
            'show_pensalim': 1,
            'show_percaliment': 0,
            'show_procemi': 1,
            'show_processamento_codigo_resposta': 1,
            'show_processamento_data_hora': 0,
            'show_processamento_descricao_resposta': 1,
            'show_processamento_versao_app_processamento': 0,
            'show_qtddiasinterm': 0,
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
            'show_versao': 0,
            'show_vralim': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'cpftrab__icontains': 'cpftrab__icontains',
                'dtdeslig__range': 'dtdeslig__range',
                'dtprojfimapi__range': 'dtprojfimapi__range',
                'evtdeslig': 'evtdeslig',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'idevinculo': 'idevinculo',
                'indcumprparc': 'indcumprparc',
                'indpagtoapi__icontains': 'indpagtoapi__icontains',
                'indretif': 'indretif',
                'infodeslig': 'infodeslig',
                'matricula__icontains': 'matricula__icontains',
                'mtvdeslig__icontains': 'mtvdeslig__icontains',
                'nistrab__icontains': 'nistrab__icontains',
                'nrcertobito__icontains': 'nrcertobito__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrproctrab__icontains': 'nrproctrab__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'pensalim': 'pensalim',
                'percaliment': 'percaliment',
                'procemi': 'procemi',
                'qtddiasinterm': 'qtddiasinterm',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',
                'vralim': 'vralim',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'cpftrab__icontains': 'cpftrab__icontains',
                'dtdeslig__range': 'dtdeslig__range',
                'dtprojfimapi__range': 'dtprojfimapi__range',
                'evtdeslig': 'evtdeslig',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'idevinculo': 'idevinculo',
                'indcumprparc': 'indcumprparc',
                'indpagtoapi__icontains': 'indpagtoapi__icontains',
                'indretif': 'indretif',
                'infodeslig': 'infodeslig',
                'matricula__icontains': 'matricula__icontains',
                'mtvdeslig__icontains': 'mtvdeslig__icontains',
                'nistrab__icontains': 'nistrab__icontains',
                'nrcertobito__icontains': 'nrcertobito__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrproctrab__icontains': 'nrproctrab__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'pensalim': 'pensalim',
                'percaliment': 'percaliment',
                'procemi': 'procemi',
                'qtddiasinterm': 'qtddiasinterm',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',
                'vralim': 'vralim',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2299_evtdeslig_lista = s2299evtDeslig.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2299_evtdeslig_lista) > 100:
            filtrar = True
            s2299_evtdeslig_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #s2299_evtdeslig_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2299_evtdeslig'
        context = {
            's2299_evtdeslig_lista': s2299_evtdeslig_lista,
  
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
            return render(request, 's2299_evtdeslig_listar.html', context)

        elif for_print == 2:
            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2299_evtdeslig_listar.html',
                filename="s2299_evtdeslig.pdf",
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
            response = render_to_response('s2299_evtdeslig_listar.html', context)
            filename = "s2299_evtdeslig.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response = render_to_response('tables/s2299_evtdeslig_csv.html', context)
            filename = "s2299_evtdeslig.csv"
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

# #view_identidade_evento#
# def identidade_evento(s2299_evtdeslig_id, db_slug):
#     from emensageriapro.mensageiro.models import TransmissorEventosEsocial
#     dados_evento = s2299evtDeslig.objects.using( db_slug ).get(id=s2299_evtdeslig_id)
#     identidade = 'ID'
#     identidade += str(dados_evento.tpinsc)
#     nr_insc = dados_evento.nrinsc
#     while len(nr_insc) != 14:
#         nr_insc = nr_insc+'0'
#     identidade += nr_insc
#     identidade += str(dados_evento.criado_em.year)
#     mes = str(dados_evento.criado_em.month)
#     if len(mes) == 1: mes = '0'+mes
#     identidade += mes
#     dia = str(dados_evento.criado_em.day)
#     if len(dia) == 1: dia = '0'+dia
#     identidade += dia
#     hora = str(dados_evento.criado_em.hour)
#     if len(hora) == 1: hora = '0'+hora
#     identidade += hora
#     minuto = str(dados_evento.criado_em.minute)
#     if len(minuto) == 1: minuto = '0'+minuto
#     identidade += minuto
#     segundo = str(dados_evento.criado_em.second)
#     if len(segundo) == 1: segundo = '0'+segundo
#     identidade += segundo
#     existe = True
#     n = 0
#     while existe:
#         n+=1
#         sequencial = str(n)
#         while len(sequencial) != 5:
#             sequencial = '0'+sequencial
#         identidade_temp = identidade + sequencial
#         lista_eventos = TransmissorEventosEsocial.objects.using(db_slug).filter(criado_em=dados_evento.criado_em,
#                                                                          excluido=False, identidade = identidade_temp).all()
#         if not lista_eventos:
#             s2299evtDeslig.objects.using(db_slug).filter(id=s2299_evtdeslig_id).update(identidade=identidade_temp)
#             existe = False
#     return identidade_temp
# #view_identidade_evento#


def gerar_identidade(request, chave, evento_id):
    from emensageriapro.functions import identidade_evento
    from emensageriapro.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        obj = get_object_or_404(s2299evtDeslig.objects.using( db_slug ), excluido = False, id = evento_id)
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
        s2299_evtdeslig_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2299_evtdeslig')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if s2299_evtdeslig_id:
        s2299_evtdeslig = get_object_or_404(s2299evtDeslig.objects.using( db_slug ), excluido = False, id = s2299_evtdeslig_id)

        if s2299_evtdeslig.status != 0:
            dict_permissoes['s2299_evtdeslig_apagar'] = 0
            dict_permissoes['s2299_evtdeslig_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2299_evtdeslig_id:
            s2299_evtdeslig_form = form_s2299_evtdeslig(request.POST or None, instance = s2299_evtdeslig, slug = db_slug)
        else:
            s2299_evtdeslig_form = form_s2299_evtdeslig(request.POST or None, slug = db_slug, initial={'versao': VERSAO_LAYOUT_ESOCIAL, 'status': 0, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s2299_evtdeslig_form.is_valid():
                dados = s2299_evtdeslig_form.cleaned_data

                if s2299_evtdeslig_id:
                    if s2299_evtdeslig.status == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s2299_evtdeslig_campos_multiple_passo1
                        s2299evtDeslig.objects.using(db_slug).filter(id=s2299_evtdeslig_id).update(**dados)
                        obj = s2299evtDeslig.objects.using(db_slug).get(id=s2299_evtdeslig_id)
                        #s2299_evtdeslig_editar_custom
                        #s2299_evtdeslig_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s2299_evtdeslig), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's2299_evtdeslig', s2299_evtdeslig_id, usuario_id, 2)
                    else:
                        obj = s2299evtDeslig.objects.using(db_slug).get(id=s2299_evtdeslig_id)
                        messages.error(request, 'Não é possível salvar o evento, pois o mesmo não está com o status "Cadastrado"!')

                else:
                    dados['processamento_codigo_resposta'] = '- -'
                    dados['processamento_descricao_resposta'] = '- -'

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s2299_evtdeslig_cadastrar_campos_multiple_passo1
                    obj = s2299evtDeslig(**dados)
                    obj.save(using = db_slug)
                    #s2299_evtdeslig_cadastrar_custom
                    #s2299_evtdeslig_cadastrar_campos_multiple_passo2
                    #identidade_evento(obj.id, db_slug)
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
 
                    messages.success(request, 'Cadastrado com sucesso!')
                    s2299_evtdeslig_form = form_s2299_evtdeslig(request.POST or None, instance = obj, slug = db_slug)
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2299_evtdeslig', obj.id, usuario_id, 1)
                if request.session['retorno_pagina'] not in ('s2299_evtdeslig_apagar', 's2299_evtdeslig_salvar', 's2299_evtdeslig'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2299_evtdeslig_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2299_evtdeslig_salvar', hash=url_hash)

            else:
                messages.error(request, 'Erro ao salvar!')
        s2299_evtdeslig_form = disabled_form_fields(s2299_evtdeslig_form, permissao.permite_editar)

        if s2299_evtdeslig_id:
            if s2299_evtdeslig.status != 0:
                s2299_evtdeslig_form = disabled_form_fields(s2299_evtdeslig_form, False)
        #s2299_evtdeslig_campos_multiple_passo3

        for field in s2299_evtdeslig_form.fields.keys():
            s2299_evtdeslig_form.fields[field].widget.attrs['ng-model'] = 's2299_evtdeslig_'+field
        if int(dict_hash['print']):
            s2299_evtdeslig_form = disabled_form_for_print(s2299_evtdeslig_form)

        s2299_observacoes_form = None
        s2299_observacoes_lista = None
        s2299_sucessaovinc_form = None
        s2299_sucessaovinc_lista = None
        s2299_transftit_form = None
        s2299_transftit_lista = None
        s2299_mudancacpf_form = None
        s2299_mudancacpf_lista = None
        s2299_dmdev_form = None
        s2299_dmdev_lista = None
        s2299_infotrabinterm_procjudtrab_form = None
        s2299_infotrabinterm_procjudtrab_lista = None
        s2299_infotrabinterm_infomv_form = None
        s2299_infotrabinterm_infomv_lista = None
        s2299_infotrabinterm_proccs_form = None
        s2299_infotrabinterm_proccs_lista = None
        s2299_infotrabinterm_quarentena_form = None
        s2299_infotrabinterm_quarentena_lista = None
        s2299_infotrabinterm_consigfgts_form = None
        s2299_infotrabinterm_consigfgts_lista = None
        if s2299_evtdeslig_id:
            s2299_evtdeslig = get_object_or_404(s2299evtDeslig.objects.using( db_slug ), excluido = False, id = s2299_evtdeslig_id)

            s2299_observacoes_form = form_s2299_observacoes(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_observacoes_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_observacoes_lista = s2299observacoes.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_sucessaovinc_form = form_s2299_sucessaovinc(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_sucessaovinc_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_sucessaovinc_lista = s2299sucessaoVinc.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_transftit_form = form_s2299_transftit(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_transftit_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_transftit_lista = s2299transfTit.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_mudancacpf_form = form_s2299_mudancacpf(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_mudancacpf_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_mudancacpf_lista = s2299mudancaCPF.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_dmdev_form = form_s2299_dmdev(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_dmdev_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_dmdev_lista = s2299dmDev.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_infotrabinterm_procjudtrab_form = form_s2299_infotrabinterm_procjudtrab(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_infotrabinterm_procjudtrab_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_infotrabinterm_procjudtrab_lista = s2299infoTrabIntermprocJudTrab.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_infotrabinterm_infomv_form = form_s2299_infotrabinterm_infomv(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_infotrabinterm_infomv_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_infotrabinterm_infomv_lista = s2299infoTrabInterminfoMV.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_infotrabinterm_proccs_form = form_s2299_infotrabinterm_proccs(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_infotrabinterm_proccs_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_infotrabinterm_proccs_lista = s2299infoTrabIntermprocCS.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_infotrabinterm_quarentena_form = form_s2299_infotrabinterm_quarentena(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_infotrabinterm_quarentena_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_infotrabinterm_quarentena_lista = s2299infoTrabIntermquarentena.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_infotrabinterm_consigfgts_form = form_s2299_infotrabinterm_consigfgts(initial={ 's2299_evtdeslig': s2299_evtdeslig }, slug=db_slug)
            s2299_infotrabinterm_consigfgts_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_infotrabinterm_consigfgts_lista = s2299infoTrabIntermconsigFGTS.objects.using( db_slug ).filter(excluido = False, s2299_evtdeslig_id=s2299_evtdeslig.id).all()
        else:
            s2299_evtdeslig = None
        #s2299_evtdeslig_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's2299_evtdeslig'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False

        if dict_hash['tab'] or 's2299_evtdeslig' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2299_evtdeslig_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2299_evtdeslig_id, tabela='s2299_evtdeslig').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2299_evtdeslig': s2299_evtdeslig,
            's2299_evtdeslig_form': s2299_evtdeslig_form,
            'mensagem': mensagem,
            's2299_evtdeslig_id': int(s2299_evtdeslig_id),
            'usuario': usuario,
  
            'hash': hash,

            's2299_observacoes_form': s2299_observacoes_form,
            's2299_observacoes_lista': s2299_observacoes_lista,
            's2299_sucessaovinc_form': s2299_sucessaovinc_form,
            's2299_sucessaovinc_lista': s2299_sucessaovinc_lista,
            's2299_transftit_form': s2299_transftit_form,
            's2299_transftit_lista': s2299_transftit_lista,
            's2299_mudancacpf_form': s2299_mudancacpf_form,
            's2299_mudancacpf_lista': s2299_mudancacpf_lista,
            's2299_dmdev_form': s2299_dmdev_form,
            's2299_dmdev_lista': s2299_dmdev_lista,
            's2299_infotrabinterm_procjudtrab_form': s2299_infotrabinterm_procjudtrab_form,
            's2299_infotrabinterm_procjudtrab_lista': s2299_infotrabinterm_procjudtrab_lista,
            's2299_infotrabinterm_infomv_form': s2299_infotrabinterm_infomv_form,
            's2299_infotrabinterm_infomv_lista': s2299_infotrabinterm_infomv_lista,
            's2299_infotrabinterm_proccs_form': s2299_infotrabinterm_proccs_form,
            's2299_infotrabinterm_proccs_lista': s2299_infotrabinterm_proccs_lista,
            's2299_infotrabinterm_quarentena_form': s2299_infotrabinterm_quarentena_form,
            's2299_infotrabinterm_quarentena_lista': s2299_infotrabinterm_quarentena_lista,
            's2299_infotrabinterm_consigfgts_form': s2299_infotrabinterm_consigfgts_form,
            's2299_infotrabinterm_consigfgts_lista': s2299_infotrabinterm_consigfgts_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2299_evtdeslig_salvar_custom_variaveis_context#
        }

        if for_print in (0,1 ):
            return render(request, 's2299_evtdeslig_salvar.html', context)

        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='s2299_evtdeslig_salvar.html',
                filename="s2299_evtdeslig.pdf",
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
            response = render_to_response('s2299_evtdeslig_salvar.html', context)
            filename = "s2299_evtdeslig.xls"
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

