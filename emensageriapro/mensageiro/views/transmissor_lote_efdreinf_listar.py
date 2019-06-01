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
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def listar(request, hash):

    for_print = 0
    
    try: 
    
        usuario_id = request.user.id   
        dict_hash = get_hash_url( hash )
        for_print = int(dict_hash['print'])
        
    except: 
    
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)

    if request.user.has_perm('mensageiro.can_view_TransmissorLoteEfdreinf'):
    
        filtrar = False
        
        dict_fields = {}
        show_fields = { 
            'show_transmissor': 0,
            'show_contribuinte_tpinsc': 1,
            'show_contribuinte_nrinsc': 1,
            'show_grupo': 1,
            'show_status': 1,
            'show_identidade_transmissor': 1,
            'show_codigo_status': 1,
            'show_retorno_descricao': 0,
            'show_recepcao_data_hora': 0,
            'show_recepcao_versao_aplicativo': 0,
            'show_protocolo': 0,
            'show_numero_protocolo_fechamento': 0,
            'show_processamento_versao_aplicativo': 0,
            'show_tempo_estimado_conclusao': 0,
            'show_arquivo_header': 0,
            'show_arquivo_request': 0,
            'show_arquivo_response': 0, }
            
        post = False
        #ANTES-POST-LISTAGEM
        
        if request.method == 'POST':
        
            post = True
            
            dict_fields = { 
                'transmissor__icontains': 'transmissor__icontains',
                'contribuinte_tpinsc__icontains': 'contribuinte_tpinsc__icontains',
                'contribuinte_nrinsc__icontains': 'contribuinte_nrinsc__icontains',
                'grupo__icontains': 'grupo__icontains',
                'status__icontains': 'status__icontains',
                'identidade_transmissor__icontains': 'identidade_transmissor__icontains',
                'codigo_status__icontains': 'codigo_status__icontains',
                'protocolo__icontains': 'protocolo__icontains',
                'numero_protocolo_fechamento__icontains': 'numero_protocolo_fechamento__icontains', }
                
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
                
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
                
            if request.method == 'POST':
            
                dict_fields = { 
                    'transmissor__icontains': 'transmissor__icontains',
                    'contribuinte_tpinsc__icontains': 'contribuinte_tpinsc__icontains',
                    'contribuinte_nrinsc__icontains': 'contribuinte_nrinsc__icontains',
                    'grupo__icontains': 'grupo__icontains',
                    'status__icontains': 'status__icontains',
                    'identidade_transmissor__icontains': 'identidade_transmissor__icontains',
                    'codigo_status__icontains': 'codigo_status__icontains',
                    'protocolo__icontains': 'protocolo__icontains',
                    'numero_protocolo_fechamento__icontains': 'numero_protocolo_fechamento__icontains', }
                    
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
                    
        dict_qs = clear_dict_fields(dict_fields)
        
        transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.filter(**dict_qs).exclude(id=0).all()
        
        if not post and len(transmissor_lote_efdreinf_lista) > 100:
        
            filtrar = True
            transmissor_lote_efdreinf_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
            
        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #transmissor_lote_efdreinf_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'transmissor_lote_efdreinf'
        
        context = {
            'transmissor_lote_efdreinf_lista': transmissor_lote_efdreinf_lista, 
            'usuario': usuario,
            'modulos': ['mensageiro', ],
            'paginas': ['transmissor_lote_efdreinf', ],
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
            #[VARIAVEIS_FILTRO_RELATORIO]
        }
        
        if for_print in (0,1):
        
            return render(request, 'transmissor_lote_efdreinf_listar.html', context)
            
        elif for_print == 2:
        
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
            response = render_to_response('csv/transmissor_lote_efdreinf.csv', context)
            filename = "transmissor_lote_efdreinf.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario, 
            'data': datetime.datetime.now(),
            'modulos': ['mensageiro', ],
            'paginas': ['transmissor_lote_efdreinf', ],
        }
        return render(request, 
                      'permissao_negada.html', 
                      context)