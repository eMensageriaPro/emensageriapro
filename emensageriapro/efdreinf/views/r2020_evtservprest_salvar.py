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
from emensageriapro.r2020.models import r2020nfs
from emensageriapro.r2020.forms import form_r2020_nfs
from emensageriapro.r2020.models import r2020infoProcRetPr
from emensageriapro.r2020.forms import form_r2020_infoprocretpr
from emensageriapro.r2020.models import r2020infoProcRetAd
from emensageriapro.r2020.forms import form_r2020_infoprocretad


@login_required
def salvar(request, hash):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    
    try:
    
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r2020_evtservprest_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    if r2020_evtservprest_id:
    
        r2020_evtservprest = get_object_or_404(r2020evtServPrest, id=r2020_evtservprest_id)

        if r2020_evtservprest.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['r2020_evtservprest_apagar'] = 0
            dict_permissoes['r2020_evtservprest_editar'] = 0
            
    if request.user.has_perm('efdreinf.can_view_r2020evtServPrest'):
    
        if r2020_evtservprest_id:
        
            r2020_evtservprest_form = form_r2020_evtservprest(request.POST or None, instance = r2020_evtservprest, 
                                         initial={'excluido': False})
                                         
        else:
        
            r2020_evtservprest_form = form_r2020_evtservprest(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
                                                  
        if request.method == 'POST':
        
            if r2020_evtservprest_form.is_valid():
            
                dados = r2020_evtservprest_form.cleaned_data
                obj = r2020_evtservprest_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not r2020_evtservprest_id:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r2020_evtservprest', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r2020_evtservprest), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r2020_evtservprest', r2020_evtservprest_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('r2020_evtservprest_apagar', 'r2020_evtservprest_salvar', 'r2020_evtservprest'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if r2020_evtservprest_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r2020_evtservprest_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
                
        r2020_evtservprest_form = disabled_form_fields(r2020_evtservprest_form, request.user.has_perm('efdreinf.change_r2020evtServPrest'))
        
        if r2020_evtservprest_id:
            if r2020_evtservprest.status != 0:
                r2020_evtservprest_form = disabled_form_fields(r2020_evtservprest_form, False)
        #r2020_evtservprest_campos_multiple_passo3

        for field in r2020_evtservprest_form.fields.keys():
            r2020_evtservprest_form.fields[field].widget.attrs['ng-model'] = 'r2020_evtservprest_'+field
            
        if int(dict_hash['print']):
            r2020_evtservprest_form = disabled_form_for_print(r2020_evtservprest_form)

        
        r2020_nfs_lista = None 
        r2020_nfs_form = None 
        r2020_infoprocretpr_lista = None 
        r2020_infoprocretpr_form = None 
        r2020_infoprocretad_lista = None 
        r2020_infoprocretad_form = None 
        
        if r2020_evtservprest_id:
        
            r2020_evtservprest = get_object_or_404(r2020evtServPrest, id = r2020_evtservprest_id)
            
            r2020_nfs_form = form_r2020_nfs(
                initial={ 'r2020_evtservprest': r2020_evtservprest })
            r2020_nfs_form.fields['r2020_evtservprest'].widget.attrs['readonly'] = True
            r2020_nfs_lista = r2020nfs.objects.\
                filter(r2020_evtservprest_id=r2020_evtservprest.id).all()
            r2020_infoprocretpr_form = form_r2020_infoprocretpr(
                initial={ 'r2020_evtservprest': r2020_evtservprest })
            r2020_infoprocretpr_form.fields['r2020_evtservprest'].widget.attrs['readonly'] = True
            r2020_infoprocretpr_lista = r2020infoProcRetPr.objects.\
                filter(r2020_evtservprest_id=r2020_evtservprest.id).all()
            r2020_infoprocretad_form = form_r2020_infoprocretad(
                initial={ 'r2020_evtservprest': r2020_evtservprest })
            r2020_infoprocretad_form.fields['r2020_evtservprest'].widget.attrs['readonly'] = True
            r2020_infoprocretad_lista = r2020infoProcRetAd.objects.\
                filter(r2020_evtservprest_id=r2020_evtservprest.id).all()
                
        else:
            r2020_evtservprest = None
            
        #r2020_evtservprest_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 'r2020_evtservprest'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 'r2020_evtservprest' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r2020_evtservprest_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=r2020_evtservprest_id, tabela='r2020_evtservprest').all()
        
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r2020_evtservprest': r2020_evtservprest, 
            'r2020_evtservprest_form': r2020_evtservprest_form, 
            'r2020_evtservprest_id': int(r2020_evtservprest_id),
            'usuario': usuario, 
            'hash': hash, 
            
            'r2020_nfs_form': r2020_nfs_form,
            'r2020_nfs_lista': r2020_nfs_lista,
            'r2020_infoprocretpr_form': r2020_infoprocretpr_form,
            'r2020_infoprocretpr_lista': r2020_infoprocretpr_lista,
            'r2020_infoprocretad_form': r2020_infoprocretad_form,
            'r2020_infoprocretad_lista': r2020_infoprocretad_lista,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r2020_evtservprest', ],
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r2020_evtservprest_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 'r2020_evtservprest_salvar.html', context)
            
        elif for_print == 2:
        
            response = PDFTemplateResponse(
                request=request,
                template='r2020_evtservprest_salvar.html',
                filename="r2020_evtservprest.pdf",
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
        
            response = render_to_response('r2020_evtservprest_salvar.html', context)
            filename = "r2020_evtservprest.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['efdreinf', ],
            'paginas': ['r2020_evtservprest', ],
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)