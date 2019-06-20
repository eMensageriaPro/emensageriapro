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
from emensageriapro.s2299.models import s2299observacoes
from emensageriapro.s2299.forms import form_s2299_observacoes
from emensageriapro.s2299.models import s2299sucessaoVinc
from emensageriapro.s2299.forms import form_s2299_sucessaovinc
from emensageriapro.s2299.models import s2299transfTit
from emensageriapro.s2299.forms import form_s2299_transftit
from emensageriapro.s2299.models import s2299mudancaCPF
from emensageriapro.s2299.forms import form_s2299_mudancacpf
from emensageriapro.s2299.models import s2299verbasResc
from emensageriapro.s2299.forms import form_s2299_verbasresc
from emensageriapro.s2299.models import s2299infoTrabIntermquarentena
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_quarentena
from emensageriapro.s2299.models import s2299infoTrabIntermconsigFGTS
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_consigfgts


@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    TP_AMB = config.ESOCIAL_TP_AMB
    
    if pk:
    
        s2299_evtdeslig = get_object_or_404(s2299evtDeslig, id=pk)

        if s2299_evtdeslig.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['s2299_evtdeslig_apagar'] = 0
            dict_permissoes['s2299_evtdeslig_editar'] = 0
            
    if request.user.has_perm('esocial.can_see_s2299evtDeslig'):
    
        if pk:
        
            s2299_evtdeslig_form = form_s2299_evtdeslig(request.POST or None, instance = s2299_evtdeslig, 
                                         initial={'ativo': True})
                                         
        else:
        
            s2299_evtdeslig_form = form_s2299_evtdeslig(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'ativo': True})
                                                  
        if request.method == 'POST':
        
            if s2299_evtdeslig_form.is_valid():
            
                obj = s2299_evtdeslig_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2299_evtdeslig', obj.id, request.user.id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2299_evtdeslig), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2299_evtdeslig', pk, request.user.id, 2)
                                 
                if request.session['return_page'] not in (
                    's2299_evtdeslig_apagar', 
                    's2299_evtdeslig_salvar', 
                    's2299_evtdeslig'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'])
                    
                if pk != obj.id:
                
                    return redirect(
                        's2299_evtdeslig_salvar', 
                        pk=obj.id)

            else:
                messages.error(request, u'Erro ao salvar!')
                
        s2299_evtdeslig_form = disabled_form_fields(
             s2299_evtdeslig_form, 
             request.user.has_perm('esocial.change_s2299evtDeslig'))
        
        if pk:
        
            if s2299_evtdeslig.status != 0:
            
                s2299_evtdeslig_form = disabled_form_fields(s2299_evtdeslig_form, False)
                
        #s2299_evtdeslig_campos_multiple_passo3

        for field in s2299_evtdeslig_form.fields.keys():
        
            s2299_evtdeslig_form.fields[field].widget.attrs['ng-model'] = 's2299_evtdeslig_'+field
            
        if output:
        
            s2299_evtdeslig_form = disabled_form_for_print(s2299_evtdeslig_form)

        
        s2299_observacoes_lista = None 
        s2299_observacoes_form = None 
        s2299_sucessaovinc_lista = None 
        s2299_sucessaovinc_form = None 
        s2299_transftit_lista = None 
        s2299_transftit_form = None 
        s2299_mudancacpf_lista = None 
        s2299_mudancacpf_form = None 
        s2299_verbasresc_lista = None 
        s2299_verbasresc_form = None 
        s2299_infotrabinterm_quarentena_lista = None 
        s2299_infotrabinterm_quarentena_form = None 
        s2299_infotrabinterm_consigfgts_lista = None 
        s2299_infotrabinterm_consigfgts_form = None 
        
        if pk:
        
            s2299_evtdeslig = get_object_or_404(s2299evtDeslig, id=pk)
            
            s2299_observacoes_form = form_s2299_observacoes(
                initial={ 's2299_evtdeslig': s2299_evtdeslig })
            s2299_observacoes_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_observacoes_lista = s2299observacoes.objects.\
                filter(s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_sucessaovinc_form = form_s2299_sucessaovinc(
                initial={ 's2299_evtdeslig': s2299_evtdeslig })
            s2299_sucessaovinc_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_sucessaovinc_lista = s2299sucessaoVinc.objects.\
                filter(s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_transftit_form = form_s2299_transftit(
                initial={ 's2299_evtdeslig': s2299_evtdeslig })
            s2299_transftit_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_transftit_lista = s2299transfTit.objects.\
                filter(s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_mudancacpf_form = form_s2299_mudancacpf(
                initial={ 's2299_evtdeslig': s2299_evtdeslig })
            s2299_mudancacpf_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_mudancacpf_lista = s2299mudancaCPF.objects.\
                filter(s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_verbasresc_form = form_s2299_verbasresc(
                initial={ 's2299_evtdeslig': s2299_evtdeslig })
            s2299_verbasresc_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_verbasresc_lista = s2299verbasResc.objects.\
                filter(s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_infotrabinterm_quarentena_form = form_s2299_infotrabinterm_quarentena(
                initial={ 's2299_evtdeslig': s2299_evtdeslig })
            s2299_infotrabinterm_quarentena_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_infotrabinterm_quarentena_lista = s2299infoTrabIntermquarentena.objects.\
                filter(s2299_evtdeslig_id=s2299_evtdeslig.id).all()
            s2299_infotrabinterm_consigfgts_form = form_s2299_infotrabinterm_consigfgts(
                initial={ 's2299_evtdeslig': s2299_evtdeslig })
            s2299_infotrabinterm_consigfgts_form.fields['s2299_evtdeslig'].widget.attrs['readonly'] = True
            s2299_infotrabinterm_consigfgts_lista = s2299infoTrabIntermconsigFGTS.objects.\
                filter(s2299_evtdeslig_id=s2299_evtdeslig.id).all()
                
        else:
        
            s2299_evtdeslig = None
            
        #s2299_evtdeslig_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 's2299_evtdeslig'[1] == '5':
            evento_totalizador = True
            
        else:
            evento_totalizador = False
        
        if tab or 's2299_evtdeslig' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 's2299_evtdeslig_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2299_evtdeslig').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2299_evtdeslig': s2299_evtdeslig, 
            's2299_evtdeslig_form': s2299_evtdeslig_form, 
            
            's2299_observacoes_form': s2299_observacoes_form,
            's2299_observacoes_lista': s2299_observacoes_lista,
            's2299_sucessaovinc_form': s2299_sucessaovinc_form,
            's2299_sucessaovinc_lista': s2299_sucessaovinc_lista,
            's2299_transftit_form': s2299_transftit_form,
            's2299_transftit_lista': s2299_transftit_lista,
            's2299_mudancacpf_form': s2299_mudancacpf_form,
            's2299_mudancacpf_lista': s2299_mudancacpf_lista,
            's2299_verbasresc_form': s2299_verbasresc_form,
            's2299_verbasresc_lista': s2299_verbasresc_lista,
            's2299_infotrabinterm_quarentena_form': s2299_infotrabinterm_quarentena_form,
            's2299_infotrabinterm_quarentena_lista': s2299_infotrabinterm_quarentena_lista,
            's2299_infotrabinterm_consigfgts_form': s2299_infotrabinterm_consigfgts_form,
            's2299_infotrabinterm_consigfgts_lista': s2299_infotrabinterm_consigfgts_lista,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s2299_evtdeslig', ],
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s2299_evtdeslig_salvar_custom_variaveis_context#
        }
        
            
        if output == 'pdf':
        
            response = PDFTemplateResponse(
                request=request,
                template='s2299_evtdeslig_salvar.html',
                filename="s2299_evtdeslig.pdf",
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
        
            response = render_to_response('s2299_evtdeslig_salvar.html', context)
            filename = "s2299_evtdeslig.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 's2299_evtdeslig_salvar.html', context)
            
    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'tab': tab,
            'output': output,
            'modulos': ['esocial', ],
            'paginas': ['s2299_evtdeslig', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 'permissao_negada.html', context)