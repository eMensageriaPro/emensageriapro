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
from emensageriapro.r4020.models import r4020idePgto
from emensageriapro.r4020.forms import form_r4020_idepgto


@login_required
def salvar(request, hash):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    
    try:
    
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r4020_evtretpj_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    if r4020_evtretpj_id:
    
        r4020_evtretpj = get_object_or_404(r4020evtRetPJ, id=r4020_evtretpj_id)

        if r4020_evtretpj.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['r4020_evtretpj_apagar'] = 0
            dict_permissoes['r4020_evtretpj_editar'] = 0
            
    if request.user.has_perm('efdreinf.can_view_r4020evtRetPJ'):
    
        if r4020_evtretpj_id:
        
            r4020_evtretpj_form = form_r4020_evtretpj(request.POST or None, instance = r4020_evtretpj, 
                                         initial={'excluido': False})
                                         
        else:
        
            r4020_evtretpj_form = form_r4020_evtretpj(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
                                                  
        if request.method == 'POST':
        
            if r4020_evtretpj_form.is_valid():
            
                dados = r4020_evtretpj_form.cleaned_data
                obj = r4020_evtretpj_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not r4020_evtretpj_id:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r4020_evtretpj', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r4020_evtretpj), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r4020_evtretpj', r4020_evtretpj_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('r4020_evtretpj_apagar', 'r4020_evtretpj_salvar', 'r4020_evtretpj'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if r4020_evtretpj_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r4020_evtretpj_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
                
        r4020_evtretpj_form = disabled_form_fields(r4020_evtretpj_form, request.user.has_perm('efdreinf.change_r4020evtRetPJ'))
        
        if r4020_evtretpj_id:
            if r4020_evtretpj.status != 0:
                r4020_evtretpj_form = disabled_form_fields(r4020_evtretpj_form, False)
        #r4020_evtretpj_campos_multiple_passo3

        for field in r4020_evtretpj_form.fields.keys():
            r4020_evtretpj_form.fields[field].widget.attrs['ng-model'] = 'r4020_evtretpj_'+field
            
        if int(dict_hash['print']):
            r4020_evtretpj_form = disabled_form_for_print(r4020_evtretpj_form)

        
        r4020_idepgto_lista = None 
        r4020_idepgto_form = None 
        
        if r4020_evtretpj_id:
        
            r4020_evtretpj = get_object_or_404(r4020evtRetPJ, id = r4020_evtretpj_id)
            
            r4020_idepgto_form = form_r4020_idepgto(
                initial={ 'r4020_evtretpj': r4020_evtretpj })
            r4020_idepgto_form.fields['r4020_evtretpj'].widget.attrs['readonly'] = True
            r4020_idepgto_lista = r4020idePgto.objects.\
                filter(r4020_evtretpj_id=r4020_evtretpj.id).all()
                
        else:
            r4020_evtretpj = None
            
        #r4020_evtretpj_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 'r4020_evtretpj'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 'r4020_evtretpj' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r4020_evtretpj_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=r4020_evtretpj_id, tabela='r4020_evtretpj').all()
        
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r4020_evtretpj': r4020_evtretpj, 
            'r4020_evtretpj_form': r4020_evtretpj_form, 
            'r4020_evtretpj_id': int(r4020_evtretpj_id),
            'usuario': usuario, 
            'hash': hash, 
            
            'r4020_idepgto_form': r4020_idepgto_form,
            'r4020_idepgto_lista': r4020_idepgto_lista,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r4020_evtretpj', ],
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r4020_evtretpj_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 'r4020_evtretpj_salvar.html', context)
            
        elif for_print == 2:
        
            response = PDFTemplateResponse(
                request=request,
                template='r4020_evtretpj_salvar.html',
                filename="r4020_evtretpj.pdf",
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
        
            response = render_to_response('r4020_evtretpj_salvar.html', context)
            filename = "r4020_evtretpj.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['efdreinf', ],
            'paginas': ['r4020_evtretpj', ],
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)
