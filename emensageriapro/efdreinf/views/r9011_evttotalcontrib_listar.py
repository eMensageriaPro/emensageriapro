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
import json
import base64
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


@login_required
def listar(request, hash):
    
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')
    
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='r9011_evttotalcontrib')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = { 
            'show_reinf': 0,
            'show_evttotalcontrib': 0,
            'show_identidade': 1,
            'show_ideevento': 0,
            'show_perapur': 1,
            'show_idecontri': 0,
            'show_tpinsc': 1,
            'show_nrinsc': 1,
            'show_iderecretorno': 0,
            'show_idestatus': 0,
            'show_cdretorno': 1,
            'show_descretorno': 1,
            'show_inforecev': 0,
            'show_nrprotentr': 1,
            'show_dhprocess': 1,
            'show_tpev': 1,
            'show_idev': 1,
            'show_hash': 1,
            'show_versao': 0,
            'show_transmissor_lote_efdreinf': 0,
            'show_retornos_r5001': 0,
            'show_retornos_r5011': 0,
            'show_retornos_r9001': 0,
            'show_retornos_r9002': 0,
            'show_retornos_r9011': 0,
            'show_retornos_r9012': 0,
            'show_ocorrencias': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_arquivo_original': 0,
            'show_arquivo': 0,
            'show_status': 1,
            'show_cdretorno': 1,
            'show_descretorno': 0,
            'show_dhprocess': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = { 
                'reinf': 'reinf',
                'evttotalcontrib': 'evttotalcontrib',
                'identidade__icontains': 'identidade__icontains',
                'ideevento': 'ideevento',
                'perapur__icontains': 'perapur__icontains',
                'idecontri': 'idecontri',
                'tpinsc__icontains': 'tpinsc__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'iderecretorno': 'iderecretorno',
                'idestatus': 'idestatus',
                'cdretorno__icontains': 'cdretorno__icontains',
                'descretorno__icontains': 'descretorno__icontains',
                'inforecev': 'inforecev',
                'nrprotentr__icontains': 'nrprotentr__icontains',
                'dhprocess__range': 'dhprocess__range',
                'tpev__icontains': 'tpev__icontains',
                'idev__icontains': 'idev__icontains',
                'hash__icontains': 'hash__icontains',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_efdreinf__icontains': 'transmissor_lote_efdreinf__icontains',
                'status__icontains': 'status__icontains',
                'cdretorno__icontains': 'cdretorno__icontains', }
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = { 
                    'reinf': 'reinf',
                    'evttotalcontrib': 'evttotalcontrib',
                    'identidade__icontains': 'identidade__icontains',
                    'ideevento': 'ideevento',
                    'perapur__icontains': 'perapur__icontains',
                    'idecontri': 'idecontri',
                    'tpinsc__icontains': 'tpinsc__icontains',
                    'nrinsc__icontains': 'nrinsc__icontains',
                    'iderecretorno': 'iderecretorno',
                    'idestatus': 'idestatus',
                    'cdretorno__icontains': 'cdretorno__icontains',
                    'descretorno__icontains': 'descretorno__icontains',
                    'inforecev': 'inforecev',
                    'nrprotentr__icontains': 'nrprotentr__icontains',
                    'dhprocess__range': 'dhprocess__range',
                    'tpev__icontains': 'tpev__icontains',
                    'idev__icontains': 'idev__icontains',
                    'hash__icontains': 'hash__icontains',
                    'versao__icontains': 'versao__icontains',
                    'transmissor_lote_efdreinf__icontains': 'transmissor_lote_efdreinf__icontains',
                    'status__icontains': 'status__icontains',
                    'cdretorno__icontains': 'cdretorno__icontains', }
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r9011_evttotalcontrib_lista = r9011evtTotalContrib.objects.filter(**dict_qs).filter().exclude(id=0).all()
        if not post and len(r9011_evttotalcontrib_lista) > 100:
            filtrar = True
            r9011_evttotalcontrib_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #r9011_evttotalcontrib_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r9011_evttotalcontrib'
        context = {
            'r9011_evttotalcontrib_lista': r9011_evttotalcontrib_lista, 
            
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
            #[VARIAVEIS_FILTRO_RELATORIO]
        }
        
        if for_print in (0,1):
            return render(request, 'r9011_evttotalcontrib_listar.html', context)
            
        elif for_print == 2:
            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r9011_evttotalcontrib_listar.html',
                filename="r9011_evttotalcontrib.pdf",
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
            response = render_to_response('r9011_evttotalcontrib_listar.html', context)
            filename = "r9011_evttotalcontrib.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
        elif for_print == 4:
            response = render_to_response('csv/r9011_evttotalcontrib.csv', context)
            filename = "r9011_evttotalcontrib.csv"
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