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
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        transmissores_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissores')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if transmissores_id:
        transmissores = get_object_or_404(TransmissorLote.objects.using( db_slug ), excluido = False, id = transmissores_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if transmissores_id:
            transmissores_form = form_transmissores(request.POST or None, instance = transmissores, slug = db_slug)
        else:
            transmissores_form = form_transmissores(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if transmissores_form.is_valid():
                dados = transmissores_form.cleaned_data
                if transmissores_id:
                    if request.FILES:
                        from emensageriapro.settings import BASE_DIR
                        from django.core.files.storage import FileSystemStorage
                        if bool(request.FILES.get('logotipo', False)) == True:
                            myfile = request.FILES['logotipo']
                            fs = FileSystemStorage(location=BASE_DIR+'/media/')
                            filename = fs.save(myfile.name, myfile)
                            dados['logotipo'] = filename
                            messages.success(request, 'Arquivo %s salvo com sucesso!' % filename)

                        files = ['esocial_certificado','efdreinf_certificado']
                        for f in files:
                            if bool(request.FILES.get(f, False)) == True:
                                myfile = request.FILES[f]
                                fs = FileSystemStorage(location=BASE_DIR+'/certificados/')
                                filename = fs.save(myfile.name, myfile)
                                dados[f] = filename
                                messages.success(request, 'Arquivo %s salvo com sucesso!' % filename)
                dados = transmissores_form.cleaned_data
                if transmissores_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #transmissores_campos_multiple_passo1
                    TransmissorLote.objects.using(db_slug).filter(id=transmissores_id).update(**dados)
                    obj = TransmissorLote.objects.using(db_slug).get(id=transmissores_id)
                    #transmissores_editar_custom
                    #transmissores_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #transmissores_cadastrar_campos_multiple_passo1
                    obj = TransmissorLote(**dados)
                    obj.save(using = db_slug)
                    #transmissores_cadastrar_custom
                    #transmissores_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('transmissores_apagar', 'transmissores_salvar', 'transmissores'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if transmissores_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('transmissores_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        transmissores_form = disabled_form_fields(transmissores_form, permissao.permite_editar)
        #transmissores_campos_multiple_passo3

        for field in transmissores_form.fields.keys():
            transmissores_form.fields[field].widget.attrs['ng-model'] = 'transmissores_'+field
        if int(dict_hash['print']):
            transmissores_form = disabled_form_for_print(transmissores_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if transmissores_id:
            transmissores = get_object_or_404(TransmissorLote.objects.using( db_slug ), excluido = False, id = transmissores_id)
            pass
        else:
            transmissores = None
        #transmissores_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'transmissores' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'transmissores_salvar'
        context = {
            'transmissores': transmissores,
            'transmissores_form': transmissores_form,
            'mensagem': mensagem,
            'transmissores_id': int(transmissores_id),
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
            #transmissores_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'transmissores_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='transmissores_salvar.html',
                filename="transmissores.pdf",
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
            response = render_to_response('transmissores_salvar.html', context)
            filename = "transmissores.xls"
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

@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        transmissores_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissores')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    transmissores = get_object_or_404(TransmissorLote.objects.using( db_slug ), excluido = False, id = transmissores_id)
    if request.method == 'POST':
        TransmissorLote.objects.using( db_slug ).filter(id = transmissores_id).update(excluido = True)
        #transmissores_apagar_custom
        #transmissores_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'transmissores_salvar':
            return redirect('transmissores', hash=request.session['retorno_hash'])
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
    return render(request, 'transmissores_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class TransmissorLoteList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = TransmissorLote.objects.using(db_slug).all()
    serializer_class = TransmissorLoteSerializer
    permission_classes = (IsAdminUser,)


class TransmissorLoteDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = TransmissorLote.objects.using(db_slug).all()
    serializer_class = TransmissorLoteSerializer
    permission_classes = (IsAdminUser,)


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #transmissores_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissores')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_efdreinf_pasta': 0,
            'show_efdreinf_senha': 0,
            'show_efdreinf_certificado': 0,
            'show_efdreinf_tempo_prox_envio': 0,
            'show_efdreinf_intervalo': 0,
            'show_efdreinf_timeout': 0,
            'show_efdreinf_lote_max': 0,
            'show_efdreinf_lote_min': 0,
            'show_contribuinte_nrinsc': 1,
            'show_contribuinte_tpinsc': 1,
            'show_efdreinf': 0,
            'show_esocial_pasta': 0,
            'show_esocial_senha': 0,
            'show_esocial_certificado': 0,
            'show_esocial_tempo_prox_envio': 0,
            'show_esocial_intervalo': 0,
            'show_esocial_timeout': 0,
            'show_esocial_lote_max': 0,
            'show_esocial_lote_min': 0,
            'show_empregador_nrinsc': 1,
            'show_empregador_tpinsc': 1,
            'show_eSocial': 0,
            'show_endereco_completo': 0,
            'show_logotipo': 0,
            'show_envio_automatico': 0,
            'show_verificar_predecessao': 0,
            'show_validar_eventos': 0,
            'show_data_abertura': 0,
            'show_nome_empresa': 1,
            'show_empregador_dados': 0,
            'show_transmissor_nrinsc': 1,
            'show_transmissor_tpinsc': 1,
            'show_transmissor_dados': 0, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'efdreinf_tempo_prox_envio': 'efdreinf_tempo_prox_envio',
                'efdreinf_intervalo': 'efdreinf_intervalo',
                'efdreinf_timeout': 'efdreinf_timeout',
                'efdreinf_lote_max': 'efdreinf_lote_max',
                'efdreinf_lote_min': 'efdreinf_lote_min',
                'contribuinte_nrinsc': 'contribuinte_nrinsc',
                'contribuinte_tpinsc__icontains': 'contribuinte_tpinsc__icontains',
                'efdreinf': 'efdreinf',
                'esocial_tempo_prox_envio': 'esocial_tempo_prox_envio',
                'esocial_intervalo': 'esocial_intervalo',
                'esocial_timeout': 'esocial_timeout',
                'esocial_lote_max': 'esocial_lote_max',
                'esocial_lote_min': 'esocial_lote_min',
                'empregador_nrinsc': 'empregador_nrinsc',
                'empregador_tpinsc__icontains': 'empregador_tpinsc__icontains',
                'eSocial': 'eSocial',
                'endereco_completo__icontains': 'endereco_completo__icontains',
                'logotipo': 'logotipo',
                'envio_automatico': 'envio_automatico',
                'verificar_predecessao': 'verificar_predecessao',
                'validar_eventos': 'validar_eventos',
                'data_abertura__range': 'data_abertura__range',
                'nome_empresa__icontains': 'nome_empresa__icontains',
                'empregador_dados': 'empregador_dados',
                'transmissor_nrinsc__icontains': 'transmissor_nrinsc__icontains',
                'transmissor_tpinsc': 'transmissor_tpinsc',
                'transmissor_dados': 'transmissor_dados',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'efdreinf_tempo_prox_envio': 'efdreinf_tempo_prox_envio',
                'efdreinf_intervalo': 'efdreinf_intervalo',
                'efdreinf_timeout': 'efdreinf_timeout',
                'efdreinf_lote_max': 'efdreinf_lote_max',
                'efdreinf_lote_min': 'efdreinf_lote_min',
                'contribuinte_nrinsc': 'contribuinte_nrinsc',
                'contribuinte_tpinsc__icontains': 'contribuinte_tpinsc__icontains',
                'efdreinf': 'efdreinf',
                'esocial_tempo_prox_envio': 'esocial_tempo_prox_envio',
                'esocial_intervalo': 'esocial_intervalo',
                'esocial_timeout': 'esocial_timeout',
                'esocial_lote_max': 'esocial_lote_max',
                'esocial_lote_min': 'esocial_lote_min',
                'empregador_nrinsc': 'empregador_nrinsc',
                'empregador_tpinsc__icontains': 'empregador_tpinsc__icontains',
                'eSocial': 'eSocial',
                'endereco_completo__icontains': 'endereco_completo__icontains',
                'logotipo': 'logotipo',
                'envio_automatico': 'envio_automatico',
                'verificar_predecessao': 'verificar_predecessao',
                'validar_eventos': 'validar_eventos',
                'data_abertura__range': 'data_abertura__range',
                'nome_empresa__icontains': 'nome_empresa__icontains',
                'empregador_dados': 'empregador_dados',
                'transmissor_nrinsc__icontains': 'transmissor_nrinsc__icontains',
                'transmissor_tpinsc': 'transmissor_tpinsc',
                'transmissor_dados': 'transmissor_dados',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        transmissores_lista = TransmissorLote.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(transmissores_lista) > 100:
            filtrar = True
            transmissores_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
    
        #transmissores_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'transmissores'
        context = {
            'transmissores_lista': transmissores_lista,
            
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
            return render(request, 'transmissores_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='transmissores_listar.html',
                filename="transmissores.pdf",
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
            response = render_to_response('transmissores_listar.html', context)
            filename = "transmissores.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/transmissores_csv.html', context)
            filename = "transmissores.csv"
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

