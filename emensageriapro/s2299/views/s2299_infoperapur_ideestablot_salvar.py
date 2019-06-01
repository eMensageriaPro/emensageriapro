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
from emensageriapro.s2299.forms import *
from emensageriapro.s2299.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2299.models import s2299infoPerApurdetVerbas
from emensageriapro.s2299.forms import form_s2299_infoperapur_detverbas
from emensageriapro.s2299.models import s2299infoPerApurinfoSaudeColet
from emensageriapro.s2299.forms import form_s2299_infoperapur_infosaudecolet
from emensageriapro.s2299.models import s2299infoPerApurinfoAgNocivo
from emensageriapro.s2299.forms import form_s2299_infoperapur_infoagnocivo
from emensageriapro.s2299.models import s2299infoPerApurinfoSimples
from emensageriapro.s2299.forms import form_s2299_infoperapur_infosimples



@login_required
def salvar(request, hash):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    try: 
    
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        s2299_infoperapur_ideestablot_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except: 
    
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    
    if s2299_infoperapur_ideestablot_id:
    
        s2299_infoperapur_ideestablot = get_object_or_404(s2299infoPerApurideEstabLot, id=s2299_infoperapur_ideestablot_id)
        dados_evento = s2299_infoperapur_ideestablot.evento()

    if request.user.has_perm('s2299.can_view_s2299infoPerApurideEstabLot'):
        
        if s2299_infoperapur_ideestablot_id:
        
            s2299_infoperapur_ideestablot_form = form_s2299_infoperapur_ideestablot(request.POST or None, 
                                                          instance=s2299_infoperapur_ideestablot,  
                                                          initial={'excluido': False})
                                         
        else:
        
            s2299_infoperapur_ideestablot_form = form_s2299_infoperapur_ideestablot(request.POST or None, 
                                         initial={'excluido': False})
                                         
        if request.method == 'POST':
        
            if s2299_infoperapur_ideestablot_form.is_valid():
            
                dados = s2299_infoperapur_ideestablot_form.cleaned_data
                obj = s2299_infoperapur_ideestablot_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s2299_infoperapur_ideestablot_id:
                
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2299_infoperapur_ideestablot', obj.id, usuario_id, 1)
                                 
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2299_infoperapur_ideestablot), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2299_infoperapur_ideestablot', s2299_infoperapur_ideestablot_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('s2299_infoperapur_ideestablot_apagar', 's2299_infoperapur_ideestablot_salvar', 's2299_infoperapur_ideestablot'):
                    
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if s2299_infoperapur_ideestablot_id != obj.id:
                
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2299_infoperapur_ideestablot_salvar', hash=url_hash)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        s2299_infoperapur_ideestablot_form = disabled_form_fields(s2299_infoperapur_ideestablot_form, request.user.has_perm('s2299.change_s2299infoPerApurideEstabLot'))
        
        if s2299_infoperapur_ideestablot_id:
        
            if dados_evento['status'] != 0:
            
                s2299_infoperapur_ideestablot_form = disabled_form_fields(s2299_infoperapur_ideestablot_form, 0)
                
        #s2299_infoperapur_ideestablot_campos_multiple_passo3
        
        if int(dict_hash['print']):
        
            s2299_infoperapur_ideestablot_form = disabled_form_for_print(s2299_infoperapur_ideestablot_form)
            
        
        s2299_infoperapur_detverbas_lista = None 
        s2299_infoperapur_detverbas_form = None 
        s2299_infoperapur_infosaudecolet_lista = None 
        s2299_infoperapur_infosaudecolet_form = None 
        s2299_infoperapur_infoagnocivo_lista = None 
        s2299_infoperapur_infoagnocivo_form = None 
        s2299_infoperapur_infosimples_lista = None 
        s2299_infoperapur_infosimples_form = None 
        
        if s2299_infoperapur_ideestablot_id:
        
            s2299_infoperapur_ideestablot = get_object_or_404(s2299infoPerApurideEstabLot, id=s2299_infoperapur_ideestablot_id)
            
            s2299_infoperapur_detverbas_form = form_s2299_infoperapur_detverbas(
                initial={ 's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot })
            s2299_infoperapur_detverbas_form.fields['s2299_infoperapur_ideestablot'].widget.attrs['readonly'] = True
            s2299_infoperapur_detverbas_lista = s2299infoPerApurdetVerbas.objects.\
                filter(s2299_infoperapur_ideestablot_id=s2299_infoperapur_ideestablot.id).all()
            s2299_infoperapur_infosaudecolet_form = form_s2299_infoperapur_infosaudecolet(
                initial={ 's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot })
            s2299_infoperapur_infosaudecolet_form.fields['s2299_infoperapur_ideestablot'].widget.attrs['readonly'] = True
            s2299_infoperapur_infosaudecolet_lista = s2299infoPerApurinfoSaudeColet.objects.\
                filter(s2299_infoperapur_ideestablot_id=s2299_infoperapur_ideestablot.id).all()
            s2299_infoperapur_infoagnocivo_form = form_s2299_infoperapur_infoagnocivo(
                initial={ 's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot })
            s2299_infoperapur_infoagnocivo_form.fields['s2299_infoperapur_ideestablot'].widget.attrs['readonly'] = True
            s2299_infoperapur_infoagnocivo_lista = s2299infoPerApurinfoAgNocivo.objects.\
                filter(s2299_infoperapur_ideestablot_id=s2299_infoperapur_ideestablot.id).all()
            s2299_infoperapur_infosimples_form = form_s2299_infoperapur_infosimples(
                initial={ 's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot })
            s2299_infoperapur_infosimples_form.fields['s2299_infoperapur_ideestablot'].widget.attrs['readonly'] = True
            s2299_infoperapur_infosimples_lista = s2299infoPerApurinfoSimples.objects.\
                filter(s2299_infoperapur_ideestablot_id=s2299_infoperapur_ideestablot.id).all()
                
        else:
        
            s2299_infoperapur_ideestablot = None
            
        #s2299_infoperapur_ideestablot_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if dict_hash['tab'] or 's2299_infoperapur_ideestablot' in request.session['retorno_pagina']:
        
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2299_infoperapur_ideestablot_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=s2299_infoperapur_ideestablot_id, tabela='s2299_infoperapur_ideestablot').all()
        
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'dados_evento': dados_evento,
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            's2299_infoperapur_ideestablot': s2299_infoperapur_ideestablot, 
            's2299_infoperapur_ideestablot_form': s2299_infoperapur_ideestablot_form, 
            's2299_infoperapur_ideestablot_id': int(s2299_infoperapur_ideestablot_id),
            'usuario': usuario, 
            'modulos': ['s2299', ],
            'paginas': ['s2299_infoperapur_ideestablot', ],
            'hash': hash, 
            
            's2299_infoperapur_detverbas_form': s2299_infoperapur_detverbas_form,
            's2299_infoperapur_detverbas_lista': s2299_infoperapur_detverbas_lista,
            's2299_infoperapur_infosaudecolet_form': s2299_infoperapur_infosaudecolet_form,
            's2299_infoperapur_infosaudecolet_lista': s2299_infoperapur_infosaudecolet_lista,
            's2299_infoperapur_infoagnocivo_form': s2299_infoperapur_infoagnocivo_form,
            's2299_infoperapur_infoagnocivo_lista': s2299_infoperapur_infoagnocivo_lista,
            's2299_infoperapur_infosimples_form': s2299_infoperapur_infosimples_form,
            's2299_infoperapur_infosimples_lista': s2299_infoperapur_infosimples_lista,
            'data': datetime.datetime.now(),
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2299_infoperapur_ideestablot_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 's2299_infoperapur_ideestablot_salvar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2299_infoperapur_ideestablot_salvar.html',
                filename="s2299_infoperapur_ideestablot.pdf",
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
            response = render_to_response('s2299_infoperapur_ideestablot_salvar.html', context)
            filename = "s2299_infoperapur_ideestablot.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['s2299', ],
            'paginas': ['s2299_infoperapur_ideestablot', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)
