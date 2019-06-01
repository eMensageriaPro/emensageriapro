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
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2245.models import s2245ideProfResp
from emensageriapro.s2245.forms import form_s2245_ideprofresp


@login_required
def salvar(request, hash):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL, TP_AMB
    
    try:
    
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2245_evttreicap_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    if s2245_evttreicap_id:
    
        s2245_evttreicap = get_object_or_404(s2245evtTreiCap, id=s2245_evttreicap_id)

        if s2245_evttreicap.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['s2245_evttreicap_apagar'] = 0
            dict_permissoes['s2245_evttreicap_editar'] = 0
            
    if request.user.has_perm('esocial.can_view_s2245evtTreiCap'):
    
        if s2245_evttreicap_id:
        
            s2245_evttreicap_form = form_s2245_evttreicap(request.POST or None, instance = s2245_evttreicap, 
                                         initial={'excluido': False})
                                         
        else:
        
            s2245_evttreicap_form = form_s2245_evttreicap(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
                                                  
        if request.method == 'POST':
        
            if s2245_evttreicap_form.is_valid():
            
                dados = s2245_evttreicap_form.cleaned_data
                obj = s2245_evttreicap_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s2245_evttreicap_id:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2245_evttreicap', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2245_evttreicap), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2245_evttreicap', s2245_evttreicap_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('s2245_evttreicap_apagar', 's2245_evttreicap_salvar', 's2245_evttreicap'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if s2245_evttreicap_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2245_evttreicap_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
                
        s2245_evttreicap_form = disabled_form_fields(s2245_evttreicap_form, request.user.has_perm('esocial.change_s2245evtTreiCap'))
        
        if s2245_evttreicap_id:
            if s2245_evttreicap.status != 0:
                s2245_evttreicap_form = disabled_form_fields(s2245_evttreicap_form, False)
        #s2245_evttreicap_campos_multiple_passo3

        for field in s2245_evttreicap_form.fields.keys():
            s2245_evttreicap_form.fields[field].widget.attrs['ng-model'] = 's2245_evttreicap_'+field
            
        if int(dict_hash['print']):
            s2245_evttreicap_form = disabled_form_for_print(s2245_evttreicap_form)

        
        s2245_ideprofresp_lista = None 
        s2245_ideprofresp_form = None 
        
        if s2245_evttreicap_id:
        
            s2245_evttreicap = get_object_or_404(s2245evtTreiCap, id = s2245_evttreicap_id)
            
            s2245_ideprofresp_form = form_s2245_ideprofresp(
                initial={ 's2245_evttreicap': s2245_evttreicap })
            s2245_ideprofresp_form.fields['s2245_evttreicap'].widget.attrs['readonly'] = True
            s2245_ideprofresp_lista = s2245ideProfResp.objects.\
                filter(s2245_evttreicap_id=s2245_evttreicap.id).all()
                
        else:
            s2245_evttreicap = None
            
        #s2245_evttreicap_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 's2245_evttreicap'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 's2245_evttreicap' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2245_evttreicap_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=s2245_evttreicap_id, tabela='s2245_evttreicap').all()
        
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2245_evttreicap': s2245_evttreicap, 
            's2245_evttreicap_form': s2245_evttreicap_form, 
            's2245_evttreicap_id': int(s2245_evttreicap_id),
            'usuario': usuario, 
            'hash': hash, 
            
            's2245_ideprofresp_form': s2245_ideprofresp_form,
            's2245_ideprofresp_lista': s2245_ideprofresp_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2245_evttreicap', ],
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2245_evttreicap_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 's2245_evttreicap_salvar.html', context)
            
        elif for_print == 2:
        
            response = PDFTemplateResponse(
                request=request,
                template='s2245_evttreicap_salvar.html',
                filename="s2245_evttreicap.pdf",
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
        
            response = render_to_response('s2245_evttreicap_salvar.html', context)
            filename = "s2245_evttreicap.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['esocial', ],
            'paginas': ['s2245_evttreicap', ],
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)
