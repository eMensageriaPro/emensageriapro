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
from emensageriapro.r1000.forms import *
from emensageriapro.r1000.models import *
from emensageriapro.controle_de_acesso.models import *



@login_required
def salvar(request, hash):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    
    try: 
    
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        r1000_alteracao_softhouse_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except: 
    
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    
    if r1000_alteracao_softhouse_id:
    
        r1000_alteracao_softhouse = get_object_or_404(r1000alteracaosoftHouse, id=r1000_alteracao_softhouse_id)
        dados_evento = r1000_alteracao_softhouse.evento()

    if request.user.has_perm('r1000.can_view_r1000alteracaosoftHouse'):
        
        if r1000_alteracao_softhouse_id:
        
            r1000_alteracao_softhouse_form = form_r1000_alteracao_softhouse(request.POST or None, 
                                                          instance=r1000_alteracao_softhouse,  
                                                          initial={'excluido': False})
                                         
        else:
        
            r1000_alteracao_softhouse_form = form_r1000_alteracao_softhouse(request.POST or None, 
                                         initial={'excluido': False})
                                         
        if request.method == 'POST':
        
            if r1000_alteracao_softhouse_form.is_valid():
            
                dados = r1000_alteracao_softhouse_form.cleaned_data
                obj = r1000_alteracao_softhouse_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not r1000_alteracao_softhouse_id:
                
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r1000_alteracao_softhouse', obj.id, usuario_id, 1)
                                 
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r1000_alteracao_softhouse), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r1000_alteracao_softhouse', r1000_alteracao_softhouse_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('r1000_alteracao_softhouse_apagar', 'r1000_alteracao_softhouse_salvar', 'r1000_alteracao_softhouse'):
                    
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if r1000_alteracao_softhouse_id != obj.id:
                
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r1000_alteracao_softhouse_salvar', hash=url_hash)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        r1000_alteracao_softhouse_form = disabled_form_fields(r1000_alteracao_softhouse_form, request.user.has_perm('r1000.change_r1000alteracaosoftHouse'))
        
        if r1000_alteracao_softhouse_id:
        
            if dados_evento['status'] != 0:
            
                r1000_alteracao_softhouse_form = disabled_form_fields(r1000_alteracao_softhouse_form, 0)
                
        #r1000_alteracao_softhouse_campos_multiple_passo3
        
        if int(dict_hash['print']):
        
            r1000_alteracao_softhouse_form = disabled_form_for_print(r1000_alteracao_softhouse_form)
            
        
        
        if r1000_alteracao_softhouse_id:
        
            r1000_alteracao_softhouse = get_object_or_404(r1000alteracaosoftHouse, id=r1000_alteracao_softhouse_id)
            
                
        else:
        
            r1000_alteracao_softhouse = None
            
        #r1000_alteracao_softhouse_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if dict_hash['tab'] or 'r1000_alteracao_softhouse' in request.session['retorno_pagina']:
        
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r1000_alteracao_softhouse_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=r1000_alteracao_softhouse_id, tabela='r1000_alteracao_softhouse').all()
        
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'dados_evento': dados_evento,
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            'r1000_alteracao_softhouse': r1000_alteracao_softhouse, 
            'r1000_alteracao_softhouse_form': r1000_alteracao_softhouse_form, 
            'r1000_alteracao_softhouse_id': int(r1000_alteracao_softhouse_id),
            'usuario': usuario, 
            'modulos': ['r1000', ],
            'paginas': ['r1000_alteracao_softhouse', ],
            'hash': hash, 
            
            'data': datetime.datetime.now(),
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r1000_alteracao_softhouse_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 'r1000_alteracao_softhouse_salvar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r1000_alteracao_softhouse_salvar.html',
                filename="r1000_alteracao_softhouse.pdf",
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
            response = render_to_response('r1000_alteracao_softhouse_salvar.html', context)
            filename = "r1000_alteracao_softhouse.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['r1000', ],
            'paginas': ['r1000_alteracao_softhouse', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)