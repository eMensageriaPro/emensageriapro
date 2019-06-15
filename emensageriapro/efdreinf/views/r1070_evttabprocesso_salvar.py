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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r1070.models import r1070inclusao
from emensageriapro.r1070.forms import form_r1070_inclusao
from emensageriapro.r1070.models import r1070alteracao
from emensageriapro.r1070.forms import form_r1070_alteracao
from emensageriapro.r1070.models import r1070exclusao
from emensageriapro.r1070.forms import form_r1070_exclusao


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF
    TP_AMB = config.EFDREINF_TP_AMB
    
    if pk:
    
        r1070_evttabprocesso = get_object_or_404(r1070evtTabProcesso, id=pk)

        if r1070_evttabprocesso.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['r1070_evttabprocesso_apagar'] = 0
            dict_permissoes['r1070_evttabprocesso_editar'] = 0
            
    if request.user.has_perm('efdreinf.can_see_r1070evtTabProcesso'):
    
        if pk:
        
            r1070_evttabprocesso_form = form_r1070_evttabprocesso(request.POST or None, instance = r1070_evttabprocesso, 
                                         initial={'excluido': False})
                                         
        else:
        
            r1070_evttabprocesso_form = form_r1070_evttabprocesso(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
                                                  
        if request.method == 'POST':
        
            if r1070_evttabprocesso_form.is_valid():
            
                obj = r1070_evttabprocesso_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r1070_evttabprocesso', obj.id, request.user.id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r1070_evttabprocesso), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r1070_evttabprocesso', pk, request.user.id, 2)
                                 
                if request.session['return_page'] not in (
                    'r1070_evttabprocesso_apagar', 
                    'r1070_evttabprocesso_salvar', 
                    'r1070_evttabprocesso'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'], 
                        tab=request.session['return_tab'])
                    
                if pk != obj.id:
                
                    return redirect(
                        'r1070_evttabprocesso_salvar', 
                        pk=obj.id, 
                        tab='master')

            else:
                messages.error(request, u'Erro ao salvar!')
                
        r1070_evttabprocesso_form = disabled_form_fields(
             r1070_evttabprocesso_form, 
             request.user.has_perm('efdreinf.change_r1070evtTabProcesso'))
        
        if pk:
        
            if r1070_evttabprocesso.status != 0:
            
                r1070_evttabprocesso_form = disabled_form_fields(r1070_evttabprocesso_form, False)
                
        #r1070_evttabprocesso_campos_multiple_passo3

        for field in r1070_evttabprocesso_form.fields.keys():
        
            r1070_evttabprocesso_form.fields[field].widget.attrs['ng-model'] = 'r1070_evttabprocesso_'+field
            
        if output:
        
            r1070_evttabprocesso_form = disabled_form_for_print(r1070_evttabprocesso_form)

        
        r1070_inclusao_lista = None 
        r1070_inclusao_form = None 
        r1070_alteracao_lista = None 
        r1070_alteracao_form = None 
        r1070_exclusao_lista = None 
        r1070_exclusao_form = None 
        
        if pk:
        
            r1070_evttabprocesso = get_object_or_404(r1070evtTabProcesso, id=pk)
            
            r1070_inclusao_form = form_r1070_inclusao(
                initial={ 'r1070_evttabprocesso': r1070_evttabprocesso })
            r1070_inclusao_form.fields['r1070_evttabprocesso'].widget.attrs['readonly'] = True
            r1070_inclusao_lista = r1070inclusao.objects.\
                filter(r1070_evttabprocesso_id=r1070_evttabprocesso.id).all()
            r1070_alteracao_form = form_r1070_alteracao(
                initial={ 'r1070_evttabprocesso': r1070_evttabprocesso })
            r1070_alteracao_form.fields['r1070_evttabprocesso'].widget.attrs['readonly'] = True
            r1070_alteracao_lista = r1070alteracao.objects.\
                filter(r1070_evttabprocesso_id=r1070_evttabprocesso.id).all()
            r1070_exclusao_form = form_r1070_exclusao(
                initial={ 'r1070_evttabprocesso': r1070_evttabprocesso })
            r1070_exclusao_form.fields['r1070_evttabprocesso'].widget.attrs['readonly'] = True
            r1070_exclusao_lista = r1070exclusao.objects.\
                filter(r1070_evttabprocesso_id=r1070_evttabprocesso.id).all()
                
        else:
        
            r1070_evttabprocesso = None
            
        #r1070_evttabprocesso_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 'r1070_evttabprocesso'[1] == '5':
            evento_totalizador = True
            
        else:
            evento_totalizador = False
        
        if tab or 'r1070_evttabprocesso' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 'r1070_evttabprocesso_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r1070_evttabprocesso').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r1070_evttabprocesso': r1070_evttabprocesso, 
            'r1070_evttabprocesso_form': r1070_evttabprocesso_form, 
            
            'r1070_inclusao_form': r1070_inclusao_form,
            'r1070_inclusao_lista': r1070_inclusao_lista,
            'r1070_alteracao_form': r1070_alteracao_form,
            'r1070_alteracao_lista': r1070_alteracao_lista,
            'r1070_exclusao_form': r1070_exclusao_form,
            'r1070_exclusao_lista': r1070_exclusao_lista,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r1070_evttabprocesso', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #r1070_evttabprocesso_salvar_custom_variaveis_context#
        }
        
            
        if output == 'pdf':
        
            response = PDFTemplateResponse(
                request=request,
                template='r1070_evttabprocesso_salvar.html',
                filename="r1070_evttabprocesso.pdf",
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
        
            response = render_to_response('r1070_evttabprocesso_salvar.html', context)
            filename = "r1070_evttabprocesso.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 'r1070_evttabprocesso_salvar.html', context)
            
    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['efdreinf', ],
            'paginas': ['r1070_evttabprocesso', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 'permissao_negada.html', context)