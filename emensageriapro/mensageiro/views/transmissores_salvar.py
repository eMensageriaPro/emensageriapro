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
from emensageriapro.mensageiro.models import TransmissorLoteEsocial
from emensageriapro.mensageiro.forms import form_transmissor_lote_esocial
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf
from emensageriapro.mensageiro.forms import form_transmissor_lote_efdreinf


@login_required
def salvar(request, hash):
    
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
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    if transmissores_id:
    
        transmissores = get_object_or_404(TransmissorLote, id=transmissores_id)
        
    if request.user.has_perm('mensageiro.can_view_TransmissorLote'):
        
        if transmissores_id:
            transmissores_form = form_transmissores(request.POST or None, instance=transmissores)
            
        else:
            transmissores_form = form_transmissores(request.POST or None)
            
        if request.method == 'POST':
            if transmissores_form.is_valid():
                #transmissores_campos_multiple_passo1
                obj = transmissores_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')
                #transmissores_campos_multiple_passo2
                
                if request.session['retorno_pagina'] not in ('transmissores_apagar', 'transmissores_salvar', 'transmissores'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if transmissores_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('transmissores_salvar', hash=url_hash)
                    
            else:
                messages.error(request, 'Erro ao salvar!')
                
        transmissores_form = disabled_form_fields(transmissores_form, request.user.has_perm('mensageiro.change_TransmissorLote'))
        #transmissores_campos_multiple_passo3
        
        if int(dict_hash['print']):
        
            transmissores_form = disabled_form_for_print(transmissores_form)
        
        
        transmissor_lote_esocial_lista = None 
        transmissor_lote_esocial_form = None 
        transmissor_lote_efdreinf_lista = None 
        transmissor_lote_efdreinf_form = None 
        
        if transmissores_id:
        
            transmissores = get_object_or_404(TransmissorLote, id = transmissores_id)
            
            transmissor_lote_esocial_form = form_transmissor_lote_esocial(
                initial={ 'transmissor': transmissores })
            transmissor_lote_esocial_form.fields['transmissor'].widget.attrs['readonly'] = True
            transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.\
                filter(transmissor_id=transmissores.id).all()
            transmissor_lote_efdreinf_form = form_transmissor_lote_efdreinf(
                initial={ 'transmissor': transmissores })
            transmissor_lote_efdreinf_form.fields['transmissor'].widget.attrs['readonly'] = True
            transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.\
                filter(transmissor_id=transmissores.id).all()
                
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
            'transmissores_id': int(transmissores_id),
            'usuario': usuario, 
            'hash': hash, 
            
            'transmissor_lote_esocial_form': transmissor_lote_esocial_form,
            'transmissor_lote_esocial_lista': transmissor_lote_esocial_lista,
            'transmissor_lote_efdreinf_form': transmissor_lote_efdreinf_form,
            'transmissor_lote_efdreinf_lista': transmissor_lote_efdreinf_lista,
            'modulos': ['mensageiro', ],
            'paginas': ['transmissores', ],
            'data': datetime.datetime.now(),
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #transmissores_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
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
            'modulos': ['mensageiro', ],
            'paginas': ['transmissores', ],
            'data': datetime.datetime.now(),
            'dict_permissoes': dict_permissoes,
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)