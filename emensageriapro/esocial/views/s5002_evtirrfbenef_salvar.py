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
from emensageriapro.s5002.models import s5002infoDep
from emensageriapro.s5002.forms import form_s5002_infodep
from emensageriapro.s5002.models import s5002infoIrrf
from emensageriapro.s5002.forms import form_s5002_infoirrf


@login_required
def salvar(request, hash):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL, TP_AMB
    
    try:
    
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s5002_evtirrfbenef_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    if s5002_evtirrfbenef_id:
    
        s5002_evtirrfbenef = get_object_or_404(s5002evtIrrfBenef, id=s5002_evtirrfbenef_id)

        if s5002_evtirrfbenef.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['s5002_evtirrfbenef_apagar'] = 0
            dict_permissoes['s5002_evtirrfbenef_editar'] = 0
            
    if request.user.has_perm('esocial.can_view_s5002evtIrrfBenef'):
    
        if s5002_evtirrfbenef_id:
        
            s5002_evtirrfbenef_form = form_s5002_evtirrfbenef(request.POST or None, instance = s5002_evtirrfbenef, 
                                         initial={'excluido': False})
                                         
        else:
        
            s5002_evtirrfbenef_form = form_s5002_evtirrfbenef(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
                                                  
        if request.method == 'POST':
        
            if s5002_evtirrfbenef_form.is_valid():
            
                dados = s5002_evtirrfbenef_form.cleaned_data
                obj = s5002_evtirrfbenef_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s5002_evtirrfbenef_id:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's5002_evtirrfbenef', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s5002_evtirrfbenef), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's5002_evtirrfbenef', s5002_evtirrfbenef_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('s5002_evtirrfbenef_apagar', 's5002_evtirrfbenef_salvar', 's5002_evtirrfbenef'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if s5002_evtirrfbenef_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s5002_evtirrfbenef_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
                
        s5002_evtirrfbenef_form = disabled_form_fields(s5002_evtirrfbenef_form, request.user.has_perm('esocial.change_s5002evtIrrfBenef'))
        
        if s5002_evtirrfbenef_id:
            if s5002_evtirrfbenef.status != 0:
                s5002_evtirrfbenef_form = disabled_form_fields(s5002_evtirrfbenef_form, False)
        #s5002_evtirrfbenef_campos_multiple_passo3

        for field in s5002_evtirrfbenef_form.fields.keys():
            s5002_evtirrfbenef_form.fields[field].widget.attrs['ng-model'] = 's5002_evtirrfbenef_'+field
            
        if int(dict_hash['print']):
            s5002_evtirrfbenef_form = disabled_form_for_print(s5002_evtirrfbenef_form)

        
        s5002_infodep_lista = None 
        s5002_infodep_form = None 
        s5002_infoirrf_lista = None 
        s5002_infoirrf_form = None 
        
        if s5002_evtirrfbenef_id:
        
            s5002_evtirrfbenef = get_object_or_404(s5002evtIrrfBenef, id = s5002_evtirrfbenef_id)
            
            s5002_infodep_form = form_s5002_infodep(
                initial={ 's5002_evtirrfbenef': s5002_evtirrfbenef })
            s5002_infodep_form.fields['s5002_evtirrfbenef'].widget.attrs['readonly'] = True
            s5002_infodep_lista = s5002infoDep.objects.\
                filter(s5002_evtirrfbenef_id=s5002_evtirrfbenef.id).all()
            s5002_infoirrf_form = form_s5002_infoirrf(
                initial={ 's5002_evtirrfbenef': s5002_evtirrfbenef })
            s5002_infoirrf_form.fields['s5002_evtirrfbenef'].widget.attrs['readonly'] = True
            s5002_infoirrf_lista = s5002infoIrrf.objects.\
                filter(s5002_evtirrfbenef_id=s5002_evtirrfbenef.id).all()
                
        else:
            s5002_evtirrfbenef = None
            
        #s5002_evtirrfbenef_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 's5002_evtirrfbenef'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 's5002_evtirrfbenef' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's5002_evtirrfbenef_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=s5002_evtirrfbenef_id, tabela='s5002_evtirrfbenef').all()
        
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's5002_evtirrfbenef': s5002_evtirrfbenef, 
            's5002_evtirrfbenef_form': s5002_evtirrfbenef_form, 
            's5002_evtirrfbenef_id': int(s5002_evtirrfbenef_id),
            'usuario': usuario, 
            'hash': hash, 
            
            's5002_infodep_form': s5002_infodep_form,
            's5002_infodep_lista': s5002_infodep_lista,
            's5002_infoirrf_form': s5002_infoirrf_form,
            's5002_infoirrf_lista': s5002_infoirrf_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s5002_evtirrfbenef', ],
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s5002_evtirrfbenef_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 's5002_evtirrfbenef_salvar.html', context)
            
        elif for_print == 2:
        
            response = PDFTemplateResponse(
                request=request,
                template='s5002_evtirrfbenef_salvar.html',
                filename="s5002_evtirrfbenef.pdf",
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
        
            response = render_to_response('s5002_evtirrfbenef_salvar.html', context)
            filename = "s5002_evtirrfbenef.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['esocial', ],
            'paginas': ['s5002_evtirrfbenef', ],
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)