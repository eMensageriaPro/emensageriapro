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
from constance import config
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
from emensageriapro.s2306.models import s2306infoComplementares
from emensageriapro.s2306.forms import form_s2306_infocomplementares


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    TP_AMB = config.ESOCIAL_TP_AMB
    
    if pk:
    
        s2306_evttsvaltcontr = get_object_or_404(s2306evtTSVAltContr, id=pk)

        if s2306_evttsvaltcontr.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['s2306_evttsvaltcontr_apagar'] = 0
            dict_permissoes['s2306_evttsvaltcontr_editar'] = 0
            
    if request.user.has_perm('esocial.can_see_s2306evtTSVAltContr'):
    
        if pk:
        
            s2306_evttsvaltcontr_form = form_s2306_evttsvaltcontr(request.POST or None, instance = s2306_evttsvaltcontr, 
                                         initial={'excluido': False})
                                         
        else:
        
            s2306_evttsvaltcontr_form = form_s2306_evttsvaltcontr(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
                                                  
        if request.method == 'POST':
        
            if s2306_evttsvaltcontr_form.is_valid():
            
                obj = s2306_evttsvaltcontr_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2306_evttsvaltcontr', obj.id, request.user.id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2306_evttsvaltcontr), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2306_evttsvaltcontr', pk, request.user.id, 2)
                                 
                if request.session['return_page'] not in (
                    's2306_evttsvaltcontr_apagar', 
                    's2306_evttsvaltcontr_salvar', 
                    's2306_evttsvaltcontr'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'], 
                        tab=request.session['return_tab'])
                    
                if pk != obj.id:
                
                    return redirect(
                        's2306_evttsvaltcontr_salvar', 
                        pk=obj.id, 
                        tab='master')

            else:
                messages.error(request, u'Erro ao salvar!')
                
        s2306_evttsvaltcontr_form = disabled_form_fields(
             s2306_evttsvaltcontr_form, 
             request.user.has_perm('esocial.change_s2306evtTSVAltContr'))
        
        if pk:
        
            if s2306_evttsvaltcontr.status != 0:
            
                s2306_evttsvaltcontr_form = disabled_form_fields(s2306_evttsvaltcontr_form, False)
                
        #s2306_evttsvaltcontr_campos_multiple_passo3

        for field in s2306_evttsvaltcontr_form.fields.keys():
        
            s2306_evttsvaltcontr_form.fields[field].widget.attrs['ng-model'] = 's2306_evttsvaltcontr_'+field
            
        if output:
        
            s2306_evttsvaltcontr_form = disabled_form_for_print(s2306_evttsvaltcontr_form)

        
        s2306_infocomplementares_lista = None 
        s2306_infocomplementares_form = None 
        
        if pk:
        
            s2306_evttsvaltcontr = get_object_or_404(s2306evtTSVAltContr, id=pk)
            
            s2306_infocomplementares_form = form_s2306_infocomplementares(
                initial={ 's2306_evttsvaltcontr': s2306_evttsvaltcontr })
            s2306_infocomplementares_form.fields['s2306_evttsvaltcontr'].widget.attrs['readonly'] = True
            s2306_infocomplementares_lista = s2306infoComplementares.objects.\
                filter(s2306_evttsvaltcontr_id=s2306_evttsvaltcontr.id).all()
                
        else:
        
            s2306_evttsvaltcontr = None
            
        #s2306_evttsvaltcontr_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 's2306_evttsvaltcontr'[1] == '5':
            evento_totalizador = True
            
        else:
            evento_totalizador = False
        
        if tab or 's2306_evttsvaltcontr' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 's2306_evttsvaltcontr_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2306_evttsvaltcontr').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2306_evttsvaltcontr': s2306_evttsvaltcontr, 
            's2306_evttsvaltcontr_form': s2306_evttsvaltcontr_form, 
            
            's2306_infocomplementares_form': s2306_infocomplementares_form,
            's2306_infocomplementares_lista': s2306_infocomplementares_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2306_evttsvaltcontr', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s2306_evttsvaltcontr_salvar_custom_variaveis_context#
        }
        
            
        if output == 'pdf':
        
            response = PDFTemplateResponse(
                request=request,
                template='s2306_evttsvaltcontr_salvar.html',
                filename="s2306_evttsvaltcontr.pdf",
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
                             "no-stop-slow-scripts": True}, )
            
            return response
            
        elif output == 'xls':
        
            response = render_to_response('s2306_evttsvaltcontr_salvar.html', context)
            filename = "s2306_evttsvaltcontr.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 's2306_evttsvaltcontr_salvar.html', context)
            
    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['esocial', ],
            'paginas': ['s2306_evttsvaltcontr', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 'permissao_negada.html', context)