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
from emensageriapro.s2416.models import s2416infoPenMorte
from emensageriapro.s2416.forms import form_s2416_infopenmorte
from emensageriapro.s2416.models import s2416homologTC
from emensageriapro.s2416.forms import form_s2416_homologtc
from emensageriapro.s2416.models import s2416suspensao
from emensageriapro.s2416.forms import form_s2416_suspensao


@login_required
def salvar(request, hash):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL, TP_AMB
    
    try:
    
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2416_evtcdbenalt_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    if s2416_evtcdbenalt_id:
    
        s2416_evtcdbenalt = get_object_or_404(s2416evtCdBenAlt, id=s2416_evtcdbenalt_id)

        if s2416_evtcdbenalt.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['s2416_evtcdbenalt_apagar'] = 0
            dict_permissoes['s2416_evtcdbenalt_editar'] = 0
            
    if request.user.has_perm('esocial.can_view_s2416evtCdBenAlt'):
    
        if s2416_evtcdbenalt_id:
        
            s2416_evtcdbenalt_form = form_s2416_evtcdbenalt(request.POST or None, instance = s2416_evtcdbenalt, 
                                         initial={'excluido': False})
                                         
        else:
        
            s2416_evtcdbenalt_form = form_s2416_evtcdbenalt(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
                                                  
        if request.method == 'POST':
        
            if s2416_evtcdbenalt_form.is_valid():
            
                dados = s2416_evtcdbenalt_form.cleaned_data
                obj = s2416_evtcdbenalt_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s2416_evtcdbenalt_id:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2416_evtcdbenalt', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2416_evtcdbenalt), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2416_evtcdbenalt', s2416_evtcdbenalt_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('s2416_evtcdbenalt_apagar', 's2416_evtcdbenalt_salvar', 's2416_evtcdbenalt'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if s2416_evtcdbenalt_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2416_evtcdbenalt_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
                
        s2416_evtcdbenalt_form = disabled_form_fields(s2416_evtcdbenalt_form, request.user.has_perm('esocial.change_s2416evtCdBenAlt'))
        
        if s2416_evtcdbenalt_id:
            if s2416_evtcdbenalt.status != 0:
                s2416_evtcdbenalt_form = disabled_form_fields(s2416_evtcdbenalt_form, False)
        #s2416_evtcdbenalt_campos_multiple_passo3

        for field in s2416_evtcdbenalt_form.fields.keys():
            s2416_evtcdbenalt_form.fields[field].widget.attrs['ng-model'] = 's2416_evtcdbenalt_'+field
            
        if int(dict_hash['print']):
            s2416_evtcdbenalt_form = disabled_form_for_print(s2416_evtcdbenalt_form)

        
        s2416_infopenmorte_lista = None 
        s2416_infopenmorte_form = None 
        s2416_homologtc_lista = None 
        s2416_homologtc_form = None 
        s2416_suspensao_lista = None 
        s2416_suspensao_form = None 
        
        if s2416_evtcdbenalt_id:
        
            s2416_evtcdbenalt = get_object_or_404(s2416evtCdBenAlt, id = s2416_evtcdbenalt_id)
            
            s2416_infopenmorte_form = form_s2416_infopenmorte(
                initial={ 's2416_evtcdbenalt': s2416_evtcdbenalt })
            s2416_infopenmorte_form.fields['s2416_evtcdbenalt'].widget.attrs['readonly'] = True
            s2416_infopenmorte_lista = s2416infoPenMorte.objects.\
                filter(s2416_evtcdbenalt_id=s2416_evtcdbenalt.id).all()
            s2416_homologtc_form = form_s2416_homologtc(
                initial={ 's2416_evtcdbenalt': s2416_evtcdbenalt })
            s2416_homologtc_form.fields['s2416_evtcdbenalt'].widget.attrs['readonly'] = True
            s2416_homologtc_lista = s2416homologTC.objects.\
                filter(s2416_evtcdbenalt_id=s2416_evtcdbenalt.id).all()
            s2416_suspensao_form = form_s2416_suspensao(
                initial={ 's2416_evtcdbenalt': s2416_evtcdbenalt })
            s2416_suspensao_form.fields['s2416_evtcdbenalt'].widget.attrs['readonly'] = True
            s2416_suspensao_lista = s2416suspensao.objects.\
                filter(s2416_evtcdbenalt_id=s2416_evtcdbenalt.id).all()
                
        else:
            s2416_evtcdbenalt = None
            
        #s2416_evtcdbenalt_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 's2416_evtcdbenalt'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 's2416_evtcdbenalt' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2416_evtcdbenalt_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=s2416_evtcdbenalt_id, tabela='s2416_evtcdbenalt').all()
        
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2416_evtcdbenalt': s2416_evtcdbenalt, 
            's2416_evtcdbenalt_form': s2416_evtcdbenalt_form, 
            's2416_evtcdbenalt_id': int(s2416_evtcdbenalt_id),
            'usuario': usuario, 
            'hash': hash, 
            
            's2416_infopenmorte_form': s2416_infopenmorte_form,
            's2416_infopenmorte_lista': s2416_infopenmorte_lista,
            's2416_homologtc_form': s2416_homologtc_form,
            's2416_homologtc_lista': s2416_homologtc_lista,
            's2416_suspensao_form': s2416_suspensao_form,
            's2416_suspensao_lista': s2416_suspensao_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2416_evtcdbenalt', ],
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2416_evtcdbenalt_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 's2416_evtcdbenalt_salvar.html', context)
            
        elif for_print == 2:
        
            response = PDFTemplateResponse(
                request=request,
                template='s2416_evtcdbenalt_salvar.html',
                filename="s2416_evtcdbenalt.pdf",
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
        
            response = render_to_response('s2416_evtcdbenalt_salvar.html', context)
            filename = "s2416_evtcdbenalt.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['esocial', ],
            'paginas': ['s2416_evtcdbenalt', ],
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)
