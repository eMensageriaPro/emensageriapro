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
from emensageriapro.r2070.models import r2070infoResidExt
from emensageriapro.r2070.forms import form_r2070_inforesidext
from emensageriapro.r2070.models import r2070infoMolestia
from emensageriapro.r2070.forms import form_r2070_infomolestia
from emensageriapro.r2070.models import r2070ideEstab
from emensageriapro.r2070.forms import form_r2070_ideestab


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF
    TP_AMB = config.EFDREINF_TP_AMB
    
    if pk:
    
        r2070_evtpgtosdivs = get_object_or_404(r2070evtPgtosDivs, id=pk)

        #if r2070_evtpgtosdivs.status != STATUS_EVENTO_CADASTRADO:
        #
        #    dict_permissoes = {}
        #    dict_permissoes['r2070_evtpgtosdivs_apagar'] = 0
        #    dict_permissoes['r2070_evtpgtosdivs_editar'] = 0
            
    if request.user.has_perm('efdreinf.can_see_r2070evtPgtosDivs'):
    
        if pk:
        
            r2070_evtpgtosdivs_form = form_r2070_evtpgtosdivs(request.POST or None, instance = r2070_evtpgtosdivs, 
                                         initial={'ativo': True})
                                         
        else:
        
            r2070_evtpgtosdivs_form = form_r2070_evtpgtosdivs(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'ativo': True})
                                                  
        if request.method == 'POST':
        
            if r2070_evtpgtosdivs_form.is_valid():
            
                obj = r2070_evtpgtosdivs_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                #    gravar_auditoria('{}',
                #                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                #                 'r2070_evtpgtosdivs', obj.id, request.user.id, 1)
                #else:
                # 
                #    gravar_auditoria(json.dumps(model_to_dict(r2070_evtpgtosdivs), indent=4, sort_keys=True, default=str),
                #                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                #                     'r2070_evtpgtosdivs', pk, request.user.id, 2)
                                 
                if request.session['return_page'] not in (
                    'r2070_evtpgtosdivs_apagar', 
                    'r2070_evtpgtosdivs_salvar', 
                    'r2070_evtpgtosdivs'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'])
                    
                if pk != obj.id:
                
                    return redirect(
                        'r2070_evtpgtosdivs_salvar', 
                        pk=obj.id)

            else:
                messages.error(request, u'Erro ao salvar!')
                
        r2070_evtpgtosdivs_form = disabled_form_fields(
             r2070_evtpgtosdivs_form, 
             request.user.has_perm('efdreinf.change_r2070evtPgtosDivs'))
        
        if pk:
        
            if r2070_evtpgtosdivs.status != 0:
            
                r2070_evtpgtosdivs_form = disabled_form_fields(r2070_evtpgtosdivs_form, False)
                
        #r2070_evtpgtosdivs_campos_multiple_passo3

        for field in r2070_evtpgtosdivs_form.fields.keys():
        
            r2070_evtpgtosdivs_form.fields[field].widget.attrs['ng-model'] = 'r2070_evtpgtosdivs_'+field
            
        if output:
        
            r2070_evtpgtosdivs_form = disabled_form_for_print(r2070_evtpgtosdivs_form)

        
        r2070_inforesidext_lista = None 
        r2070_inforesidext_form = None 
        r2070_infomolestia_lista = None 
        r2070_infomolestia_form = None 
        r2070_ideestab_lista = None 
        r2070_ideestab_form = None 
        
        if pk:
        
            r2070_evtpgtosdivs = get_object_or_404(r2070evtPgtosDivs, id=pk)
            
            r2070_inforesidext_form = form_r2070_inforesidext(
                initial={ 'r2070_evtpgtosdivs': r2070_evtpgtosdivs })
            r2070_inforesidext_form.fields['r2070_evtpgtosdivs'].widget.attrs['readonly'] = True
            r2070_inforesidext_lista = r2070infoResidExt.objects.\
                filter(r2070_evtpgtosdivs_id=r2070_evtpgtosdivs.id).all()
            r2070_infomolestia_form = form_r2070_infomolestia(
                initial={ 'r2070_evtpgtosdivs': r2070_evtpgtosdivs })
            r2070_infomolestia_form.fields['r2070_evtpgtosdivs'].widget.attrs['readonly'] = True
            r2070_infomolestia_lista = r2070infoMolestia.objects.\
                filter(r2070_evtpgtosdivs_id=r2070_evtpgtosdivs.id).all()
            r2070_ideestab_form = form_r2070_ideestab(
                initial={ 'r2070_evtpgtosdivs': r2070_evtpgtosdivs })
            r2070_ideestab_form.fields['r2070_evtpgtosdivs'].widget.attrs['readonly'] = True
            r2070_ideestab_lista = r2070ideEstab.objects.\
                filter(r2070_evtpgtosdivs_id=r2070_evtpgtosdivs.id).all()
                
        else:
        
            r2070_evtpgtosdivs = None
            
        #r2070_evtpgtosdivs_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 'r2070_evtpgtosdivs'[1] == '5':
            evento_totalizador = True
            
        else:
            evento_totalizador = False
        
        if tab or 'r2070_evtpgtosdivs' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 'r2070_evtpgtosdivs_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='r2070_evtpgtosdivs').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r2070_evtpgtosdivs': r2070_evtpgtosdivs, 
            'r2070_evtpgtosdivs_form': r2070_evtpgtosdivs_form, 
            
            'r2070_inforesidext_form': r2070_inforesidext_form,
            'r2070_inforesidext_lista': r2070_inforesidext_lista,
            'r2070_infomolestia_form': r2070_infomolestia_form,
            'r2070_infomolestia_lista': r2070_infomolestia_lista,
            'r2070_ideestab_form': r2070_ideestab_form,
            'r2070_ideestab_lista': r2070_ideestab_lista,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r2070_evtpgtosdivs', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #r2070_evtpgtosdivs_salvar_custom_variaveis_context#
        }
        
            
        if output == 'pdf':
        
            response = PDFTemplateResponse(
                request=request,
                template='r2070_evtpgtosdivs_salvar.html',
                filename="r2070_evtpgtosdivs.pdf",
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
        
            response = render_to_response('r2070_evtpgtosdivs_salvar.html', context)
            filename = "r2070_evtpgtosdivs.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 'r2070_evtpgtosdivs_salvar.html', context)
            
    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['efdreinf', ],
            'paginas': ['r2070_evtpgtosdivs', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 'permissao_negada.html', context)