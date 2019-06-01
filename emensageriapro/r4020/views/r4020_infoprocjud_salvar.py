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
from emensageriapro.r4020.forms import *
from emensageriapro.r4020.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r4020.models import r4020despProcJud
from emensageriapro.r4020.forms import form_r4020_despprocjud
from emensageriapro.r4020.models import r4020origemRec
from emensageriapro.r4020.forms import form_r4020_origemrec



@login_required
def salvar(request, hash):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    
    try: 
    
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        r4020_infoprocjud_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except: 
    
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    
    if r4020_infoprocjud_id:
    
        r4020_infoprocjud = get_object_or_404(r4020infoProcJud, id=r4020_infoprocjud_id)
        dados_evento = r4020_infoprocjud.evento()

    if request.user.has_perm('r4020.can_view_r4020infoProcJud'):
        
        if r4020_infoprocjud_id:
        
            r4020_infoprocjud_form = form_r4020_infoprocjud(request.POST or None, 
                                                          instance=r4020_infoprocjud,  
                                                          initial={'excluido': False})
                                         
        else:
        
            r4020_infoprocjud_form = form_r4020_infoprocjud(request.POST or None, 
                                         initial={'excluido': False})
                                         
        if request.method == 'POST':
        
            if r4020_infoprocjud_form.is_valid():
            
                dados = r4020_infoprocjud_form.cleaned_data
                obj = r4020_infoprocjud_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not r4020_infoprocjud_id:
                
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r4020_infoprocjud', obj.id, usuario_id, 1)
                                 
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r4020_infoprocjud), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r4020_infoprocjud', r4020_infoprocjud_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('r4020_infoprocjud_apagar', 'r4020_infoprocjud_salvar', 'r4020_infoprocjud'):
                    
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if r4020_infoprocjud_id != obj.id:
                
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r4020_infoprocjud_salvar', hash=url_hash)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        r4020_infoprocjud_form = disabled_form_fields(r4020_infoprocjud_form, request.user.has_perm('r4020.change_r4020infoProcJud'))
        
        if r4020_infoprocjud_id:
        
            if dados_evento['status'] != 0:
            
                r4020_infoprocjud_form = disabled_form_fields(r4020_infoprocjud_form, 0)
                
        #r4020_infoprocjud_campos_multiple_passo3
        
        if int(dict_hash['print']):
        
            r4020_infoprocjud_form = disabled_form_for_print(r4020_infoprocjud_form)
            
        
        r4020_despprocjud_lista = None 
        r4020_despprocjud_form = None 
        r4020_origemrec_lista = None 
        r4020_origemrec_form = None 
        
        if r4020_infoprocjud_id:
        
            r4020_infoprocjud = get_object_or_404(r4020infoProcJud, id=r4020_infoprocjud_id)
            
            r4020_despprocjud_form = form_r4020_despprocjud(
                initial={ 'r4020_infoprocjud': r4020_infoprocjud })
            r4020_despprocjud_form.fields['r4020_infoprocjud'].widget.attrs['readonly'] = True
            r4020_despprocjud_lista = r4020despProcJud.objects.\
                filter(r4020_infoprocjud_id=r4020_infoprocjud.id).all()
            r4020_origemrec_form = form_r4020_origemrec(
                initial={ 'r4020_infoprocjud': r4020_infoprocjud })
            r4020_origemrec_form.fields['r4020_infoprocjud'].widget.attrs['readonly'] = True
            r4020_origemrec_lista = r4020origemRec.objects.\
                filter(r4020_infoprocjud_id=r4020_infoprocjud.id).all()
                
        else:
        
            r4020_infoprocjud = None
            
        #r4020_infoprocjud_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if dict_hash['tab'] or 'r4020_infoprocjud' in request.session['retorno_pagina']:
        
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r4020_infoprocjud_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=r4020_infoprocjud_id, tabela='r4020_infoprocjud').all()
        
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'dados_evento': dados_evento,
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            'r4020_infoprocjud': r4020_infoprocjud, 
            'r4020_infoprocjud_form': r4020_infoprocjud_form, 
            'r4020_infoprocjud_id': int(r4020_infoprocjud_id),
            'usuario': usuario, 
            'modulos': ['r4020', ],
            'paginas': ['r4020_infoprocjud', ],
            'hash': hash, 
            
            'r4020_despprocjud_form': r4020_despprocjud_form,
            'r4020_despprocjud_lista': r4020_despprocjud_lista,
            'r4020_origemrec_form': r4020_origemrec_form,
            'r4020_origemrec_lista': r4020_origemrec_lista,
            'data': datetime.datetime.now(),
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r4020_infoprocjud_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 'r4020_infoprocjud_salvar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r4020_infoprocjud_salvar.html',
                filename="r4020_infoprocjud.pdf",
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
            response = render_to_response('r4020_infoprocjud_salvar.html', context)
            filename = "r4020_infoprocjud.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['r4020', ],
            'paginas': ['r4020_infoprocjud', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)
