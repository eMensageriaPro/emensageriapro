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

    if request.user.has_perm('mensageiro.can_view_RetornosEventos'):
    
        filtrar = False
        
        dict_fields = {}
        show_fields = { 
            'show_transmissor_lote_esocial': 1,
            'show_identidade': 1,
            'show_processamento': 0,
            'show_recepcao_tp_amb': 0,
            'show_recepcao_data_hora': 0,
            'show_recepcao_versao_app': 0,
            'show_recepcao_protocolo_envio_lote': 0,
            'show_processamento': 0,
            'show_processamento_codigo_resposta': 1,
            'show_processamento_descricao_resposta': 0,
            'show_processamento_versao_app_processamento': 0,
            'show_processamento_data_hora': 0,
            'show_recibo': 0,
            'show_recibo_numero': 0,
            'show_recibo_hash': 0,
            'show_empregador': 0,
            'show_tpinsc': 1,
            'show_empregador_tpinsc': 1,
            'show_nrinsc': 1,
            'show_empregador_nrinsc': 1,
            'show_trabalhador': 0,
            'show_cpftrab': 1,
            'show_nistrab': 0,
            'show_nmtrab': 1,
            'show_deficiencia': 0,
            'show_infocota': 0,
            'show_vinculo': 0,
            'show_matricula': 0,
            'show_celetista': 0,
            'show_dtadm': 0,
            'show_tpregjor': 0,
            'show_dtbase': 0,
            'show_cnpjsindcategprof': 0,
            'show_estatutario': 0,
            'show_dtposse': 0,
            'show_dtexercicio': 0,
            'show_cargo': 0,
            'show_codcargo': 0,
            'show_nmcargo': 0,
            'show_codcbocargo': 0,
            'show_funcao': 0,
            'show_codfuncao': 0,
            'show_dscfuncao': 0,
            'show_codcbofuncao': 0,
            'show_categoria': 0,
            'show_codcateg': 0,
            'show_remuneracao': 0,
            'show_vrsalfx': 0,
            'show_undsalfixo': 0,
            'show_dscsalvar': 0,
            'show_duracao': 0,
            'show_tpcontr': 0,
            'show_dtterm': 0,
            'show_clauasseg': 0,
            'show_local_trab': 0,
            'show_local_tpinsc': 0,
            'show_local_nrinsc': 0,
            'show_local_cnae': 0,
            'show_horarios_contratuais': 0,
            'show_qtdhrssem': 0,
            'show_tpjornada': 0,
            'show_dsctpjorn': 0,
            'show_tmpparc': 0, }
            
        post = False
        #ANTES-POST-LISTAGEM
        
        if request.method == 'POST':
        
            post = True
            
            dict_fields = { 
                'transmissor_lote_esocial__icontains': 'transmissor_lote_esocial__icontains',
                'identidade__icontains': 'identidade__icontains',
                'processamento_codigo_resposta__icontains': 'processamento_codigo_resposta__icontains',
                'tpinsc__icontains': 'tpinsc__icontains',
                'empregador_tpinsc__icontains': 'empregador_tpinsc__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'empregador_nrinsc__icontains': 'empregador_nrinsc__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'nmtrab__icontains': 'nmtrab__icontains',
                'infocota__icontains': 'infocota__icontains',
                'dtadm__range': 'dtadm__range',
                'tpregjor__icontains': 'tpregjor__icontains',
                'cnpjsindcategprof__icontains': 'cnpjsindcategprof__icontains',
                'dtposse__range': 'dtposse__range',
                'dtexercicio__range': 'dtexercicio__range',
                'codcargo__icontains': 'codcargo__icontains',
                'nmcargo__icontains': 'nmcargo__icontains',
                'codcbocargo__icontains': 'codcbocargo__icontains',
                'dscfuncao__icontains': 'dscfuncao__icontains',
                'codcbofuncao__icontains': 'codcbofuncao__icontains',
                'codcateg__icontains': 'codcateg__icontains',
                'vrsalfx__icontains': 'vrsalfx__icontains',
                'undsalfixo__icontains': 'undsalfixo__icontains',
                'tpcontr__icontains': 'tpcontr__icontains',
                'local_tpinsc__icontains': 'local_tpinsc__icontains',
                'local_nrinsc__icontains': 'local_nrinsc__icontains',
                'local_cnae__icontains': 'local_cnae__icontains',
                'tpjornada__icontains': 'tpjornada__icontains',
                'tmpparc__icontains': 'tmpparc__icontains', }
                
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
                
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
                
            if request.method == 'POST':
            
                dict_fields = { 
                    'transmissor_lote_esocial__icontains': 'transmissor_lote_esocial__icontains',
                    'identidade__icontains': 'identidade__icontains',
                    'processamento_codigo_resposta__icontains': 'processamento_codigo_resposta__icontains',
                    'tpinsc__icontains': 'tpinsc__icontains',
                    'empregador_tpinsc__icontains': 'empregador_tpinsc__icontains',
                    'nrinsc__icontains': 'nrinsc__icontains',
                    'empregador_nrinsc__icontains': 'empregador_nrinsc__icontains',
                    'cpftrab__icontains': 'cpftrab__icontains',
                    'nmtrab__icontains': 'nmtrab__icontains',
                    'infocota__icontains': 'infocota__icontains',
                    'dtadm__range': 'dtadm__range',
                    'tpregjor__icontains': 'tpregjor__icontains',
                    'cnpjsindcategprof__icontains': 'cnpjsindcategprof__icontains',
                    'dtposse__range': 'dtposse__range',
                    'dtexercicio__range': 'dtexercicio__range',
                    'codcargo__icontains': 'codcargo__icontains',
                    'nmcargo__icontains': 'nmcargo__icontains',
                    'codcbocargo__icontains': 'codcbocargo__icontains',
                    'dscfuncao__icontains': 'dscfuncao__icontains',
                    'codcbofuncao__icontains': 'codcbofuncao__icontains',
                    'codcateg__icontains': 'codcateg__icontains',
                    'vrsalfx__icontains': 'vrsalfx__icontains',
                    'undsalfixo__icontains': 'undsalfixo__icontains',
                    'tpcontr__icontains': 'tpcontr__icontains',
                    'local_tpinsc__icontains': 'local_tpinsc__icontains',
                    'local_nrinsc__icontains': 'local_nrinsc__icontains',
                    'local_cnae__icontains': 'local_cnae__icontains',
                    'tpjornada__icontains': 'tpjornada__icontains',
                    'tmpparc__icontains': 'tmpparc__icontains', }
                    
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
                    
        dict_qs = clear_dict_fields(dict_fields)
        
        retornos_eventos_lista = RetornosEventos.objects.filter(**dict_qs).exclude(id=0).all()
        
        if not post and len(retornos_eventos_lista) > 100:
        
            filtrar = True
            retornos_eventos_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
            
        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #retornos_eventos_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'retornos_eventos'
        
        context = {
            'retornos_eventos_lista': retornos_eventos_lista, 
            'usuario': usuario,
            'modulos': ['mensageiro', ],
            'paginas': ['retornos_eventos', ],
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
            #[VARIAVEIS_FILTRO_RELATORIO]
        }
        
        if for_print in (0,1):
        
            return render(request, 'retornos_eventos_listar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='retornos_eventos_listar.html',
                filename="retornos_eventos.pdf",
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
            response = render_to_response('retornos_eventos_listar.html', context)
            filename = "retornos_eventos.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
        elif for_print == 4:
        
            from django.shortcuts import render_to_response
            response = render_to_response('csv/retornos_eventos.csv', context)
            filename = "retornos_eventos.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario, 
            'data': datetime.datetime.now(),
            'modulos': ['mensageiro', ],
            'paginas': ['retornos_eventos', ],
        }
        return render(request, 
                      'permissao_negada.html', 
                      context)