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
from emensageriapro.s2300.models import s2300CTPS
from emensageriapro.s2300.models import s2300RIC
from emensageriapro.s2300.models import s2300RG
from emensageriapro.s2300.models import s2300RNE
from emensageriapro.s2300.models import s2300OC
from emensageriapro.s2300.models import s2300CNH
from emensageriapro.s2300.models import s2300brasil
from emensageriapro.s2300.models import s2300exterior
from emensageriapro.s2300.models import s2300trabEstrangeiro
from emensageriapro.s2300.models import s2300infoDeficiencia
from emensageriapro.s2300.models import s2300dependente
from emensageriapro.s2300.models import s2300contato
from emensageriapro.s2300.models import s2300cargoFuncao
from emensageriapro.s2300.models import s2300remuneracao
from emensageriapro.s2300.models import s2300fgts
from emensageriapro.s2300.models import s2300infoDirigenteSindical
from emensageriapro.s2300.models import s2300infoTrabCedido
from emensageriapro.s2300.models import s2300infoEstagiario
from emensageriapro.s2300.models import s2300mudancaCPF
from emensageriapro.s2300.models import s2300afastamento
from emensageriapro.s2300.models import s2300termino
from emensageriapro.s2300.forms import form_s2300_ctps
from emensageriapro.s2300.forms import form_s2300_ric
from emensageriapro.s2300.forms import form_s2300_rg
from emensageriapro.s2300.forms import form_s2300_rne
from emensageriapro.s2300.forms import form_s2300_oc
from emensageriapro.s2300.forms import form_s2300_cnh
from emensageriapro.s2300.forms import form_s2300_brasil
from emensageriapro.s2300.forms import form_s2300_exterior
from emensageriapro.s2300.forms import form_s2300_trabestrangeiro
from emensageriapro.s2300.forms import form_s2300_infodeficiencia
from emensageriapro.s2300.forms import form_s2300_dependente
from emensageriapro.s2300.forms import form_s2300_contato
from emensageriapro.s2300.forms import form_s2300_cargofuncao
from emensageriapro.s2300.forms import form_s2300_remuneracao
from emensageriapro.s2300.forms import form_s2300_fgts
from emensageriapro.s2300.forms import form_s2300_infodirigentesindical
from emensageriapro.s2300.forms import form_s2300_infotrabcedido
from emensageriapro.s2300.forms import form_s2300_infoestagiario
from emensageriapro.s2300.forms import form_s2300_mudancacpf
from emensageriapro.s2300.forms import form_s2300_afastamento
from emensageriapro.s2300.forms import form_s2300_termino

#IMPORTACOES
@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2300_evttsvinicio_id = int(dict_hash['id'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2300_evttsvinicio')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2300_evttsvinicio = get_object_or_404(s2300evtTSVInicio.objects.using( db_slug ), excluido = False, id = s2300_evttsvinicio_id)

    if s2300_evttsvinicio_id:
        if s2300_evttsvinicio.status != 0:
            dict_permissoes['s2300_evttsvinicio_apagar'] = 0
            dict_permissoes['s2300_evttsvinicio_editar'] = 0

    if request.method == 'POST':
        if s2300_evttsvinicio.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2300_evttsvinicio), indent=4, sort_keys=True, default=str)
            obj = s2300evtTSVInicio.objects.using( db_slug ).get(id = s2300_evttsvinicio_id)
            obj.delete(request=request)
            #s2300_evttsvinicio_apagar_custom
            #s2300_evttsvinicio_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2300_evttsvinicio', s2300_evttsvinicio_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's2300_evttsvinicio_salvar':
            return redirect('s2300_evttsvinicio', hash=request.session['retorno_hash'])
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
    return render(request, 's2300_evttsvinicio_apagar.html', context)

class s2300evtTSVInicioList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s2300evtTSVInicio.objects.using(db_slug).all()
    serializer_class = s2300evtTSVInicioSerializer
    # permission_classes = (IsAdminUser,)


class s2300evtTSVInicioDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s2300evtTSVInicio.objects.using(db_slug).all()
    serializer_class = s2300evtTSVInicioSerializer
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
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2300_evttsvinicio')
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
            'show_cadini': 0,
            'show_codcateg': 0,
            'show_codmunic': 0,
            'show_cpftrab': 0,
            'show_dtinicio': 0,
            'show_dtnascto': 0,
            'show_endereco': 0,
            'show_estciv': 0,
            'show_evttsvinicio': 0,
            'show_grauinstr': 0,
            'show_ideempregador': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_indretif': 0,
            'show_infotsvinicio': 0,
            'show_nascimento': 0,
            'show_natatividade': 0,
            'show_nistrab': 0,
            'show_nmmae': 0,
            'show_nmpai': 0,
            'show_nmsoc': 0,
            'show_nmtrab': 0,
            'show_nrinsc': 0,
            'show_nrrecibo': 0,
            'show_ocorrencias': 0,
            'show_paisnac': 0,
            'show_paisnascto': 0,
            'show_procemi': 0,
            'show_racacor': 0,
            'show_retornos_eventos': 0,
            'show_sexo': 0,
            'show_status': 1,
            'show_tpamb': 0,
            'show_tpinsc': 0,
            'show_trabalhador': 0,
            'show_transmissor_lote_esocial': 0,
            'show_uf': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_verproc': 0,
            'show_versao': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'cadini__icontains': 'cadini__icontains',
                'codcateg__icontains': 'codcateg__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'dtinicio__range': 'dtinicio__range',
                'dtnascto__range': 'dtnascto__range',
                'endereco': 'endereco',
                'estciv': 'estciv',
                'evttsvinicio': 'evttsvinicio',
                'grauinstr__icontains': 'grauinstr__icontains',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'indretif': 'indretif',
                'infotsvinicio': 'infotsvinicio',
                'nascimento': 'nascimento',
                'natatividade': 'natatividade',
                'nistrab__icontains': 'nistrab__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'nmpai__icontains': 'nmpai__icontains',
                'nmsoc__icontains': 'nmsoc__icontains',
                'nmtrab__icontains': 'nmtrab__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'paisnascto__icontains': 'paisnascto__icontains',
                'procemi': 'procemi',
                'racacor': 'racacor',
                'sexo__icontains': 'sexo__icontains',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'trabalhador': 'trabalhador',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'uf__icontains': 'uf__icontains',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'cadini__icontains': 'cadini__icontains',
                'codcateg__icontains': 'codcateg__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'dtinicio__range': 'dtinicio__range',
                'dtnascto__range': 'dtnascto__range',
                'endereco': 'endereco',
                'estciv': 'estciv',
                'evttsvinicio': 'evttsvinicio',
                'grauinstr__icontains': 'grauinstr__icontains',
                'ideempregador': 'ideempregador',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'indretif': 'indretif',
                'infotsvinicio': 'infotsvinicio',
                'nascimento': 'nascimento',
                'natatividade': 'natatividade',
                'nistrab__icontains': 'nistrab__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'nmpai__icontains': 'nmpai__icontains',
                'nmsoc__icontains': 'nmsoc__icontains',
                'nmtrab__icontains': 'nmtrab__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'paisnascto__icontains': 'paisnascto__icontains',
                'procemi': 'procemi',
                'racacor': 'racacor',
                'sexo__icontains': 'sexo__icontains',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'trabalhador': 'trabalhador',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',
                'uf__icontains': 'uf__icontains',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2300_evttsvinicio_lista = s2300evtTSVInicio.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2300_evttsvinicio_lista) > 100:
            filtrar = True
            s2300_evttsvinicio_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #s2300_evttsvinicio_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2300_evttsvinicio'
        context = {
            's2300_evttsvinicio_lista': s2300_evttsvinicio_lista,
  
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
            return render(request, 's2300_evttsvinicio_listar.html', context)

        elif for_print == 2:
            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2300_evttsvinicio_listar.html',
                filename="s2300_evttsvinicio.pdf",
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
            response = render_to_response('s2300_evttsvinicio_listar.html', context)
            filename = "s2300_evttsvinicio.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response = render_to_response('tables/s2300_evttsvinicio_csv.html', context)
            filename = "s2300_evttsvinicio.csv"
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
        obj = get_object_or_404(s2300evtTSVInicio.objects.using( db_slug ), excluido = False, id = evento_id)
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
        s2300_evttsvinicio_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2300_evttsvinicio')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if s2300_evttsvinicio_id:
        s2300_evttsvinicio = get_object_or_404(s2300evtTSVInicio.objects.using( db_slug ), excluido = False, id = s2300_evttsvinicio_id)

        if s2300_evttsvinicio.status != 0:
            dict_permissoes['s2300_evttsvinicio_apagar'] = 0
            dict_permissoes['s2300_evttsvinicio_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2300_evttsvinicio_id:
            s2300_evttsvinicio_form = form_s2300_evttsvinicio(request.POST or None, instance = s2300_evttsvinicio, slug = db_slug)
        else:
            s2300_evttsvinicio_form = form_s2300_evttsvinicio(request.POST or None, slug = db_slug, initial={'versao': VERSAO_LAYOUT_ESOCIAL, 'status': 0, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s2300_evttsvinicio_form.is_valid():

                dados = s2300_evttsvinicio_form.cleaned_data
                obj = s2300_evttsvinicio_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')

                if not s2300_evttsvinicio_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)

                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 's2300_evttsvinicio', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(s2300_evttsvinicio), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2300_evttsvinicio', s2300_evttsvinicio_id, usuario_id, 2)
              
                if request.session['retorno_pagina'] not in ('s2300_evttsvinicio_apagar', 's2300_evttsvinicio_salvar', 's2300_evttsvinicio'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2300_evttsvinicio_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2300_evttsvinicio_salvar', hash=url_hash)

            else:
                messages.error(request, 'Erro ao salvar!')
        s2300_evttsvinicio_form = disabled_form_fields(s2300_evttsvinicio_form, permissao.permite_editar)

        if s2300_evttsvinicio_id:
            if s2300_evttsvinicio.status != 0:
                s2300_evttsvinicio_form = disabled_form_fields(s2300_evttsvinicio_form, False)
        #s2300_evttsvinicio_campos_multiple_passo3

        for field in s2300_evttsvinicio_form.fields.keys():
            s2300_evttsvinicio_form.fields[field].widget.attrs['ng-model'] = 's2300_evttsvinicio_'+field
        if int(dict_hash['print']):
            s2300_evttsvinicio_form = disabled_form_for_print(s2300_evttsvinicio_form)

        s2300_ctps_form = None
        s2300_ctps_lista = None
        s2300_ric_form = None
        s2300_ric_lista = None
        s2300_rg_form = None
        s2300_rg_lista = None
        s2300_rne_form = None
        s2300_rne_lista = None
        s2300_oc_form = None
        s2300_oc_lista = None
        s2300_cnh_form = None
        s2300_cnh_lista = None
        s2300_brasil_form = None
        s2300_brasil_lista = None
        s2300_exterior_form = None
        s2300_exterior_lista = None
        s2300_trabestrangeiro_form = None
        s2300_trabestrangeiro_lista = None
        s2300_infodeficiencia_form = None
        s2300_infodeficiencia_lista = None
        s2300_dependente_form = None
        s2300_dependente_lista = None
        s2300_contato_form = None
        s2300_contato_lista = None
        s2300_cargofuncao_form = None
        s2300_cargofuncao_lista = None
        s2300_remuneracao_form = None
        s2300_remuneracao_lista = None
        s2300_fgts_form = None
        s2300_fgts_lista = None
        s2300_infodirigentesindical_form = None
        s2300_infodirigentesindical_lista = None
        s2300_infotrabcedido_form = None
        s2300_infotrabcedido_lista = None
        s2300_infoestagiario_form = None
        s2300_infoestagiario_lista = None
        s2300_mudancacpf_form = None
        s2300_mudancacpf_lista = None
        s2300_afastamento_form = None
        s2300_afastamento_lista = None
        s2300_termino_form = None
        s2300_termino_lista = None
        if s2300_evttsvinicio_id:
            s2300_evttsvinicio = get_object_or_404(s2300evtTSVInicio.objects.using( db_slug ), excluido = False, id = s2300_evttsvinicio_id)

            s2300_ctps_form = form_s2300_ctps(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_ctps_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_ctps_lista = s2300CTPS.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_ric_form = form_s2300_ric(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_ric_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_ric_lista = s2300RIC.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_rg_form = form_s2300_rg(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_rg_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_rg_lista = s2300RG.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_rne_form = form_s2300_rne(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_rne_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_rne_lista = s2300RNE.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_oc_form = form_s2300_oc(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_oc_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_oc_lista = s2300OC.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_cnh_form = form_s2300_cnh(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_cnh_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_cnh_lista = s2300CNH.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_brasil_form = form_s2300_brasil(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_brasil_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_brasil_lista = s2300brasil.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_exterior_form = form_s2300_exterior(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_exterior_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_exterior_lista = s2300exterior.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_trabestrangeiro_form = form_s2300_trabestrangeiro(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_trabestrangeiro_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_trabestrangeiro_lista = s2300trabEstrangeiro.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_infodeficiencia_form = form_s2300_infodeficiencia(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_infodeficiencia_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_infodeficiencia_lista = s2300infoDeficiencia.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_dependente_form = form_s2300_dependente(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_dependente_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_dependente_lista = s2300dependente.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_contato_form = form_s2300_contato(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_contato_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_contato_lista = s2300contato.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_cargofuncao_form = form_s2300_cargofuncao(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_cargofuncao_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_cargofuncao_lista = s2300cargoFuncao.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_remuneracao_form = form_s2300_remuneracao(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_remuneracao_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_remuneracao_lista = s2300remuneracao.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_fgts_form = form_s2300_fgts(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_fgts_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_fgts_lista = s2300fgts.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_infodirigentesindical_form = form_s2300_infodirigentesindical(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_infodirigentesindical_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_infodirigentesindical_lista = s2300infoDirigenteSindical.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_infotrabcedido_form = form_s2300_infotrabcedido(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_infotrabcedido_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_infotrabcedido_lista = s2300infoTrabCedido.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_infoestagiario_form = form_s2300_infoestagiario(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_infoestagiario_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_infoestagiario_lista = s2300infoEstagiario.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_mudancacpf_form = form_s2300_mudancacpf(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_mudancacpf_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_mudancacpf_lista = s2300mudancaCPF.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_afastamento_form = form_s2300_afastamento(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_afastamento_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_afastamento_lista = s2300afastamento.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
            s2300_termino_form = form_s2300_termino(initial={ 's2300_evttsvinicio': s2300_evttsvinicio }, slug=db_slug)
            s2300_termino_form.fields['s2300_evttsvinicio'].widget.attrs['readonly'] = True
            s2300_termino_lista = s2300termino.objects.using( db_slug ).filter(excluido = False, s2300_evttsvinicio_id=s2300_evttsvinicio.id).all()
        else:
            s2300_evttsvinicio = None
        #s2300_evttsvinicio_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's2300_evttsvinicio'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False

        if dict_hash['tab'] or 's2300_evttsvinicio' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2300_evttsvinicio_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2300_evttsvinicio_id, tabela='s2300_evttsvinicio').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2300_evttsvinicio': s2300_evttsvinicio,
            's2300_evttsvinicio_form': s2300_evttsvinicio_form,
            'mensagem': mensagem,
            's2300_evttsvinicio_id': int(s2300_evttsvinicio_id),
            'usuario': usuario,
  
            'hash': hash,

            's2300_ctps_form': s2300_ctps_form,
            's2300_ctps_lista': s2300_ctps_lista,
            's2300_ric_form': s2300_ric_form,
            's2300_ric_lista': s2300_ric_lista,
            's2300_rg_form': s2300_rg_form,
            's2300_rg_lista': s2300_rg_lista,
            's2300_rne_form': s2300_rne_form,
            's2300_rne_lista': s2300_rne_lista,
            's2300_oc_form': s2300_oc_form,
            's2300_oc_lista': s2300_oc_lista,
            's2300_cnh_form': s2300_cnh_form,
            's2300_cnh_lista': s2300_cnh_lista,
            's2300_brasil_form': s2300_brasil_form,
            's2300_brasil_lista': s2300_brasil_lista,
            's2300_exterior_form': s2300_exterior_form,
            's2300_exterior_lista': s2300_exterior_lista,
            's2300_trabestrangeiro_form': s2300_trabestrangeiro_form,
            's2300_trabestrangeiro_lista': s2300_trabestrangeiro_lista,
            's2300_infodeficiencia_form': s2300_infodeficiencia_form,
            's2300_infodeficiencia_lista': s2300_infodeficiencia_lista,
            's2300_dependente_form': s2300_dependente_form,
            's2300_dependente_lista': s2300_dependente_lista,
            's2300_contato_form': s2300_contato_form,
            's2300_contato_lista': s2300_contato_lista,
            's2300_cargofuncao_form': s2300_cargofuncao_form,
            's2300_cargofuncao_lista': s2300_cargofuncao_lista,
            's2300_remuneracao_form': s2300_remuneracao_form,
            's2300_remuneracao_lista': s2300_remuneracao_lista,
            's2300_fgts_form': s2300_fgts_form,
            's2300_fgts_lista': s2300_fgts_lista,
            's2300_infodirigentesindical_form': s2300_infodirigentesindical_form,
            's2300_infodirigentesindical_lista': s2300_infodirigentesindical_lista,
            's2300_infotrabcedido_form': s2300_infotrabcedido_form,
            's2300_infotrabcedido_lista': s2300_infotrabcedido_lista,
            's2300_infoestagiario_form': s2300_infoestagiario_form,
            's2300_infoestagiario_lista': s2300_infoestagiario_lista,
            's2300_mudancacpf_form': s2300_mudancacpf_form,
            's2300_mudancacpf_lista': s2300_mudancacpf_lista,
            's2300_afastamento_form': s2300_afastamento_form,
            's2300_afastamento_lista': s2300_afastamento_lista,
            's2300_termino_form': s2300_termino_form,
            's2300_termino_lista': s2300_termino_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2300_evttsvinicio_salvar_custom_variaveis_context#
        }

        if for_print in (0,1 ):
            return render(request, 's2300_evttsvinicio_salvar.html', context)

        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='s2300_evttsvinicio_salvar.html',
                filename="s2300_evttsvinicio.pdf",
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
            response = render_to_response('s2300_evttsvinicio_salvar.html', context)
            filename = "s2300_evttsvinicio.xls"
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

