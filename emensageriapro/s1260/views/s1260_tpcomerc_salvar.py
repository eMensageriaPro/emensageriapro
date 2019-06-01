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
from emensageriapro.s1260.forms import *
from emensageriapro.s1260.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s1260.models import s1260ideAdquir
from emensageriapro.s1260.forms import form_s1260_ideadquir
from emensageriapro.s1260.models import s1260infoProcJud
from emensageriapro.s1260.forms import form_s1260_infoprocjud



@login_required
def salvar(request, hash):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    try: 
    
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        s1260_tpcomerc_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except: 
    
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    
    if s1260_tpcomerc_id:
    
        s1260_tpcomerc = get_object_or_404(s1260tpComerc, id=s1260_tpcomerc_id)
        dados_evento = s1260_tpcomerc.evento()

    if request.user.has_perm('s1260.can_view_s1260tpComerc'):
        
        if s1260_tpcomerc_id:
        
            s1260_tpcomerc_form = form_s1260_tpcomerc(request.POST or None, 
                                                          instance=s1260_tpcomerc,  
                                                          initial={'excluido': False})
                                         
        else:
        
            s1260_tpcomerc_form = form_s1260_tpcomerc(request.POST or None, 
                                         initial={'excluido': False})
                                         
        if request.method == 'POST':
        
            if s1260_tpcomerc_form.is_valid():
            
                dados = s1260_tpcomerc_form.cleaned_data
                obj = s1260_tpcomerc_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s1260_tpcomerc_id:
                
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's1260_tpcomerc', obj.id, usuario_id, 1)
                                 
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s1260_tpcomerc), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's1260_tpcomerc', s1260_tpcomerc_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('s1260_tpcomerc_apagar', 's1260_tpcomerc_salvar', 's1260_tpcomerc'):
                    
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if s1260_tpcomerc_id != obj.id:
                
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s1260_tpcomerc_salvar', hash=url_hash)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        s1260_tpcomerc_form = disabled_form_fields(s1260_tpcomerc_form, request.user.has_perm('s1260.change_s1260tpComerc'))
        
        if s1260_tpcomerc_id:
        
            if dados_evento['status'] != 0:
            
                s1260_tpcomerc_form = disabled_form_fields(s1260_tpcomerc_form, 0)
                
        #s1260_tpcomerc_campos_multiple_passo3
        
        if int(dict_hash['print']):
        
            s1260_tpcomerc_form = disabled_form_for_print(s1260_tpcomerc_form)
            
        
        s1260_ideadquir_lista = None 
        s1260_ideadquir_form = None 
        s1260_infoprocjud_lista = None 
        s1260_infoprocjud_form = None 
        
        if s1260_tpcomerc_id:
        
            s1260_tpcomerc = get_object_or_404(s1260tpComerc, id=s1260_tpcomerc_id)
            
            s1260_ideadquir_form = form_s1260_ideadquir(
                initial={ 's1260_tpcomerc': s1260_tpcomerc })
            s1260_ideadquir_form.fields['s1260_tpcomerc'].widget.attrs['readonly'] = True
            s1260_ideadquir_lista = s1260ideAdquir.objects.\
                filter(s1260_tpcomerc_id=s1260_tpcomerc.id).all()
            s1260_infoprocjud_form = form_s1260_infoprocjud(
                initial={ 's1260_tpcomerc': s1260_tpcomerc })
            s1260_infoprocjud_form.fields['s1260_tpcomerc'].widget.attrs['readonly'] = True
            s1260_infoprocjud_lista = s1260infoProcJud.objects.\
                filter(s1260_tpcomerc_id=s1260_tpcomerc.id).all()
                
        else:
        
            s1260_tpcomerc = None
            
        #s1260_tpcomerc_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if dict_hash['tab'] or 's1260_tpcomerc' in request.session['retorno_pagina']:
        
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1260_tpcomerc_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=s1260_tpcomerc_id, tabela='s1260_tpcomerc').all()
        
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'dados_evento': dados_evento,
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            's1260_tpcomerc': s1260_tpcomerc, 
            's1260_tpcomerc_form': s1260_tpcomerc_form, 
            's1260_tpcomerc_id': int(s1260_tpcomerc_id),
            'usuario': usuario, 
            'modulos': ['s1260', ],
            'paginas': ['s1260_tpcomerc', ],
            'hash': hash, 
            
            's1260_ideadquir_form': s1260_ideadquir_form,
            's1260_ideadquir_lista': s1260_ideadquir_lista,
            's1260_infoprocjud_form': s1260_infoprocjud_form,
            's1260_infoprocjud_lista': s1260_infoprocjud_lista,
            'data': datetime.datetime.now(),
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1260_tpcomerc_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 's1260_tpcomerc_salvar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1260_tpcomerc_salvar.html',
                filename="s1260_tpcomerc.pdf",
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
            response = render_to_response('s1260_tpcomerc_salvar.html', context)
            filename = "s1260_tpcomerc.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['s1260', ],
            'paginas': ['s1260_tpcomerc', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)