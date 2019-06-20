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
from emensageriapro.s2400.models import s2400endereco
from emensageriapro.s2400.forms import form_s2400_endereco
from emensageriapro.s2400.models import s2400dependente
from emensageriapro.s2400.forms import form_s2400_dependente


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    TP_AMB = config.ESOCIAL_TP_AMB
    
    if pk:
    
        s2400_evtcdbenefin = get_object_or_404(s2400evtCdBenefIn, id=pk)

        if s2400_evtcdbenefin.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['s2400_evtcdbenefin_apagar'] = 0
            dict_permissoes['s2400_evtcdbenefin_editar'] = 0
            
    if request.user.has_perm('esocial.can_see_s2400evtCdBenefIn'):
    
        if pk:
        
            s2400_evtcdbenefin_form = form_s2400_evtcdbenefin(request.POST or None, instance = s2400_evtcdbenefin, 
                                         initial={'ativo': True})
                                         
        else:
        
            s2400_evtcdbenefin_form = form_s2400_evtcdbenefin(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'ativo': True})
                                                  
        if request.method == 'POST':
        
            if s2400_evtcdbenefin_form.is_valid():
            
                obj = s2400_evtcdbenefin_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2400_evtcdbenefin', obj.id, request.user.id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2400_evtcdbenefin), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2400_evtcdbenefin', pk, request.user.id, 2)
                                 
                if request.session['return_page'] not in (
                    's2400_evtcdbenefin_apagar', 
                    's2400_evtcdbenefin_salvar', 
                    's2400_evtcdbenefin'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'], 
                        tab=request.session['return_tab'])
                    
                if pk != obj.id:
                
                    return redirect(
                        's2400_evtcdbenefin_salvar', 
                        pk=obj.id, 
                        tab='master')

            else:
                messages.error(request, u'Erro ao salvar!')
                
        s2400_evtcdbenefin_form = disabled_form_fields(
             s2400_evtcdbenefin_form, 
             request.user.has_perm('esocial.change_s2400evtCdBenefIn'))
        
        if pk:
        
            if s2400_evtcdbenefin.status != 0:
            
                s2400_evtcdbenefin_form = disabled_form_fields(s2400_evtcdbenefin_form, False)
                
        #s2400_evtcdbenefin_campos_multiple_passo3

        for field in s2400_evtcdbenefin_form.fields.keys():
        
            s2400_evtcdbenefin_form.fields[field].widget.attrs['ng-model'] = 's2400_evtcdbenefin_'+field
            
        if output:
        
            s2400_evtcdbenefin_form = disabled_form_for_print(s2400_evtcdbenefin_form)

        
        s2400_endereco_lista = None 
        s2400_endereco_form = None 
        s2400_dependente_lista = None 
        s2400_dependente_form = None 
        
        if pk:
        
            s2400_evtcdbenefin = get_object_or_404(s2400evtCdBenefIn, id=pk)
            
            s2400_endereco_form = form_s2400_endereco(
                initial={ 's2400_evtcdbenefin': s2400_evtcdbenefin })
            s2400_endereco_form.fields['s2400_evtcdbenefin'].widget.attrs['readonly'] = True
            s2400_endereco_lista = s2400endereco.objects.\
                filter(s2400_evtcdbenefin_id=s2400_evtcdbenefin.id).all()
            s2400_dependente_form = form_s2400_dependente(
                initial={ 's2400_evtcdbenefin': s2400_evtcdbenefin })
            s2400_dependente_form.fields['s2400_evtcdbenefin'].widget.attrs['readonly'] = True
            s2400_dependente_lista = s2400dependente.objects.\
                filter(s2400_evtcdbenefin_id=s2400_evtcdbenefin.id).all()
                
        else:
        
            s2400_evtcdbenefin = None
            
        #s2400_evtcdbenefin_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 's2400_evtcdbenefin'[1] == '5':
            evento_totalizador = True
            
        else:
            evento_totalizador = False
        
        if tab or 's2400_evtcdbenefin' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 's2400_evtcdbenefin_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2400_evtcdbenefin').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2400_evtcdbenefin': s2400_evtcdbenefin, 
            's2400_evtcdbenefin_form': s2400_evtcdbenefin_form, 
            
            's2400_endereco_form': s2400_endereco_form,
            's2400_endereco_lista': s2400_endereco_lista,
            's2400_dependente_form': s2400_dependente_form,
            's2400_dependente_lista': s2400_dependente_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2400_evtcdbenefin', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s2400_evtcdbenefin_salvar_custom_variaveis_context#
        }
        
            
        if output == 'pdf':
        
            response = PDFTemplateResponse(
                request=request,
                template='s2400_evtcdbenefin_salvar.html',
                filename="s2400_evtcdbenefin.pdf",
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
        
            response = render_to_response('s2400_evtcdbenefin_salvar.html', context)
            filename = "s2400_evtcdbenefin.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 's2400_evtcdbenefin_salvar.html', context)
            
    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['esocial', ],
            'paginas': ['s2400_evtcdbenefin', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 'permissao_negada.html', context)