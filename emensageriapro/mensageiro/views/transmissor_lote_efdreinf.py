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
from emensageriapro.efdreinf.models import r1000evtInfoContri
from emensageriapro.efdreinf.models import r1070evtTabProcesso
from emensageriapro.efdreinf.models import r2010evtServTom
from emensageriapro.efdreinf.models import r2020evtServPrest
from emensageriapro.efdreinf.models import r2030evtAssocDespRec
from emensageriapro.efdreinf.models import r2040evtAssocDespRep
from emensageriapro.efdreinf.models import r2050evtComProd
from emensageriapro.efdreinf.models import r2060evtCPRB
from emensageriapro.efdreinf.models import r2070evtPgtosDivs
from emensageriapro.efdreinf.models import r2098evtReabreEvPer
from emensageriapro.efdreinf.models import r2099evtFechaEvPer
from emensageriapro.efdreinf.models import r3010evtEspDesportivo
from emensageriapro.efdreinf.models import r5001evtTotal
from emensageriapro.efdreinf.models import r5011evtTotalContrib
from emensageriapro.efdreinf.models import r9000evtExclusao
from emensageriapro.efdreinf.forms import form_r1000_evtinfocontri
from emensageriapro.efdreinf.forms import form_r1070_evttabprocesso
from emensageriapro.efdreinf.forms import form_r2010_evtservtom
from emensageriapro.efdreinf.forms import form_r2020_evtservprest
from emensageriapro.efdreinf.forms import form_r2030_evtassocdesprec
from emensageriapro.efdreinf.forms import form_r2040_evtassocdesprep
from emensageriapro.efdreinf.forms import form_r2050_evtcomprod
from emensageriapro.efdreinf.forms import form_r2060_evtcprb
from emensageriapro.efdreinf.forms import form_r2070_evtpgtosdivs
from emensageriapro.efdreinf.forms import form_r2098_evtreabreevper
from emensageriapro.efdreinf.forms import form_r2099_evtfechaevper
from emensageriapro.efdreinf.forms import form_r3010_evtespdesportivo
from emensageriapro.efdreinf.forms import form_r5001_evttotal
from emensageriapro.efdreinf.forms import form_r5011_evttotalcontrib
from emensageriapro.efdreinf.forms import form_r9000_evtexclusao

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissor_lote_efdreinf_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_efdreinf')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf.objects.using( db_slug ), excluido = False, id = transmissor_lote_efdreinf_id)
    if request.method == 'POST':
        TransmissorLoteEfdreinf.objects.using( db_slug ).filter(id = transmissor_lote_efdreinf_id).update(excluido = True)
        #transmissor_lote_efdreinf_apagar_custom
        #transmissor_lote_efdreinf_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'transmissor_lote_efdreinf_salvar':
            return redirect('transmissor_lote_efdreinf', hash=request.session['retorno_hash'])
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
    return render(request, 'transmissor_lote_efdreinf_apagar.html', context)

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #transmissor_lote_efdreinf_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_efdreinf')
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
            'show_tempo_estimado_conclusao': 0,
            'show_processamento_versao_aplicativo': 0,
            'show_numero_protocolo_fechamento': 0,
            'show_protocolo': 0,
            'show_recepcao_versao_aplicativo': 0,
            'show_recepcao_data_hora': 0,
            'show_retorno_descricao': 0,
            'show_codigo_status': 1,
            'show_identidade_transmissor': 1,
            'show_status': 1,
            'show_grupo': 1,
            'show_contribuinte_nrinsc': 1,
            'show_contribuinte_tpinsc': 1,
            'show_transmissor': 0, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'tempo_estimado_conclusao': 'tempo_estimado_conclusao',
                'processamento_versao_aplicativo__icontains': 'processamento_versao_aplicativo__icontains',
                'numero_protocolo_fechamento__icontains': 'numero_protocolo_fechamento__icontains',
                'protocolo__icontains': 'protocolo__icontains',
                'recepcao_versao_aplicativo__icontains': 'recepcao_versao_aplicativo__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'codigo_status': 'codigo_status',
                'identidade_transmissor__icontains': 'identidade_transmissor__icontains',
                'status': 'status',
                'grupo': 'grupo',
                'contribuinte_nrinsc__icontains': 'contribuinte_nrinsc__icontains',
                'contribuinte_tpinsc': 'contribuinte_tpinsc',
                'transmissor': 'transmissor',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'tempo_estimado_conclusao': 'tempo_estimado_conclusao',
                'processamento_versao_aplicativo__icontains': 'processamento_versao_aplicativo__icontains',
                'numero_protocolo_fechamento__icontains': 'numero_protocolo_fechamento__icontains',
                'protocolo__icontains': 'protocolo__icontains',
                'recepcao_versao_aplicativo__icontains': 'recepcao_versao_aplicativo__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'codigo_status': 'codigo_status',
                'identidade_transmissor__icontains': 'identidade_transmissor__icontains',
                'status': 'status',
                'grupo': 'grupo',
                'contribuinte_nrinsc__icontains': 'contribuinte_nrinsc__icontains',
                'contribuinte_tpinsc': 'contribuinte_tpinsc',
                'transmissor': 'transmissor',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(transmissor_lote_efdreinf_lista) > 100:
            filtrar = True
            transmissor_lote_efdreinf_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lista = TransmissorLote.objects.using( db_slug ).filter(excluido = False).all()
        #transmissor_lote_efdreinf_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'transmissor_lote_efdreinf'
        context = {
            'transmissor_lote_efdreinf_lista': transmissor_lote_efdreinf_lista,
       
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
  
            'transmissor_lista': transmissor_lista,
        }
        if for_print in (0,1):
            return render(request, 'transmissor_lote_efdreinf_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='transmissor_lote_efdreinf_listar.html',
                filename="transmissor_lote_efdreinf.pdf",
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
            response = render_to_response('transmissor_lote_efdreinf_listar.html', context)
            filename = "transmissor_lote_efdreinf.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/transmissor_lote_efdreinf_csv.html', context)
            filename = "transmissor_lote_efdreinf.csv"
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
        transmissor_lote_efdreinf_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_efdreinf')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if transmissor_lote_efdreinf_id:
        transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf.objects.using( db_slug ), excluido = False, id = transmissor_lote_efdreinf_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if transmissor_lote_efdreinf_id:
            transmissor_lote_efdreinf_form = form_transmissor_lote_efdreinf(request.POST or None, instance = transmissor_lote_efdreinf, slug = db_slug)
        else:
            transmissor_lote_efdreinf_form = form_transmissor_lote_efdreinf(request.POST or None, slug = db_slug, initial={'status': 0})
        if request.method == 'POST':
            if transmissor_lote_efdreinf_form.is_valid():
                dados = transmissor_lote_efdreinf_form.cleaned_data
                if transmissor_lote_efdreinf_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #transmissor_lote_efdreinf_campos_multiple_passo1
                    TransmissorLoteEfdreinf.objects.using(db_slug).filter(id=transmissor_lote_efdreinf_id).update(**dados)
                    obj = TransmissorLoteEfdreinf.objects.using(db_slug).get(id=transmissor_lote_efdreinf_id)
                    #transmissor_lote_efdreinf_editar_custom
                    #transmissor_lote_efdreinf_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #transmissor_lote_efdreinf_cadastrar_campos_multiple_passo1
                    obj = TransmissorLoteEfdreinf(**dados)
                    obj.save(using = db_slug)
                    #transmissor_lote_efdreinf_cadastrar_custom
                    #transmissor_lote_efdreinf_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('transmissor_lote_efdreinf_apagar', 'transmissor_lote_efdreinf_salvar', 'transmissor_lote_efdreinf'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if transmissor_lote_efdreinf_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('transmissor_lote_efdreinf_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        transmissor_lote_efdreinf_form = disabled_form_fields(transmissor_lote_efdreinf_form, permissao.permite_editar)
        #transmissor_lote_efdreinf_campos_multiple_passo3

        for field in transmissor_lote_efdreinf_form.fields.keys():
            transmissor_lote_efdreinf_form.fields[field].widget.attrs['ng-model'] = 'transmissor_lote_efdreinf_'+field
        if int(dict_hash['print']):
            transmissor_lote_efdreinf_form = disabled_form_for_print(transmissor_lote_efdreinf_form)

        transmissor_lote_efdreinf_ocorrencias_form = None
        transmissor_lote_efdreinf_ocorrencias_lista = None
        if transmissor_lote_efdreinf_id:
            transmissor_lote_efdreinf = get_object_or_404(TransmissorLoteEfdreinf.objects.using( db_slug ), excluido = False, id = transmissor_lote_efdreinf_id)
  
            transmissor_lote_efdreinf_ocorrencias_form = form_transmissor_lote_efdreinf_ocorrencias(initial={ 'transmissor_lote_efdreinf': transmissor_lote_efdreinf }, slug=db_slug)
            transmissor_lote_efdreinf_ocorrencias_form.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
            transmissor_lote_efdreinf_ocorrencias_lista = TransmissorLoteEfdreinfOcorrencias.objects.using( db_slug ).filter(excluido = False, transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()
        else:
            transmissor_lote_efdreinf = None
        if transmissor_lote_efdreinf:
            transmissor_eventos_efdreinf_lista = TransmissorEventosEfdreinf.objects.using(db_slug).filter(excluido=False, transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()
            transmissor_eventos_efdreinf_totalizacoes_lista = TransmissorEventosEfdreinfTotalizacoes.objects.using(db_slug).filter(excluido=False, transmissor_lote_efdreinf_id=transmissor_lote_efdreinf.id).all()
        else:
            transmissor_eventos_efdreinf_lista = None
            transmissor_eventos_efdreinf_totalizacoes_lista = None
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'transmissor_lote_efdreinf' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'transmissor_lote_efdreinf_salvar'
        context = {
            'transmissor_lote_efdreinf': transmissor_lote_efdreinf,
            'transmissor_lote_efdreinf_form': transmissor_lote_efdreinf_form,
            'mensagem': mensagem,
            'transmissor_lote_efdreinf_id': int(transmissor_lote_efdreinf_id),
            'usuario': usuario,
       
            'hash': hash,
  
            'transmissor_lote_efdreinf_ocorrencias_form': transmissor_lote_efdreinf_ocorrencias_form,
            'transmissor_lote_efdreinf_ocorrencias_lista': transmissor_lote_efdreinf_ocorrencias_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            'transmissor_eventos_efdreinf_lista': transmissor_eventos_efdreinf_lista,
'transmissor_eventos_efdreinf_totalizacoes_lista': transmissor_eventos_efdreinf_totalizacoes_lista,
        }
        if for_print in (0,1 ):
            return render(request, 'transmissor_lote_efdreinf_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='transmissor_lote_efdreinf_salvar.html',
                filename="transmissor_lote_efdreinf.pdf",
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
            response = render_to_response('transmissor_lote_efdreinf_salvar.html', context)
            filename = "transmissor_lote_efdreinf.xls"
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

