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
from emensageriapro.s2240.forms import *
from emensageriapro.s2240.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2240.models import s2240altExpRiscofatRisco
from emensageriapro.s2240.forms import form_s2240_altexprisco_fatrisco



@login_required
def salvar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    try: 
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        s2240_altexprisco_infoamb_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='s2240_altexprisco_infoamb')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2240_altexprisco_infoamb_id:
        s2240_altexprisco_infoamb = get_object_or_404(s2240altExpRiscoinfoAmb, id = s2240_altexprisco_infoamb_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    if s2240_altexprisco_infoamb_id:
        dados_evento = s2240_altexprisco_infoamb.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2240_altexprisco_infoamb_apagar'] = 0
            dict_permissoes['s2240_altexprisco_infoamb_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2240_altexprisco_infoamb_id:
            s2240_altexprisco_infoamb_form = form_s2240_altexprisco_infoamb(request.POST or None, instance = s2240_altexprisco_infoamb,  
                                         initial={'excluido': False})
        else:
            s2240_altexprisco_infoamb_form = form_s2240_altexprisco_infoamb(request.POST or None, 
                                         initial={'excluido': False})
        if request.method == 'POST':
            if s2240_altexprisco_infoamb_form.is_valid():
            
                dados = s2240_altexprisco_infoamb_form.cleaned_data
                obj = s2240_altexprisco_infoamb_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s2240_altexprisco_infoamb_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2240_altexprisco_infoamb', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2240_altexprisco_infoamb), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2240_altexprisco_infoamb', s2240_altexprisco_infoamb_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('s2240_altexprisco_infoamb_apagar', 's2240_altexprisco_infoamb_salvar', 's2240_altexprisco_infoamb'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2240_altexprisco_infoamb_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2240_altexprisco_infoamb_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        s2240_altexprisco_infoamb_form = disabled_form_fields(s2240_altexprisco_infoamb_form, permissao.permite_editar)
        
        if s2240_altexprisco_infoamb_id:
            if dados_evento['status'] != 0:
                s2240_altexprisco_infoamb_form = disabled_form_fields(s2240_altexprisco_infoamb_form, 0)
                
        #s2240_altexprisco_infoamb_campos_multiple_passo3
        
        if int(dict_hash['print']):
            s2240_altexprisco_infoamb_form = disabled_form_for_print(s2240_altexprisco_infoamb_form)
            
        
        s2240_altexprisco_fatrisco_lista = None 
        s2240_altexprisco_fatrisco_form = None 
        
        if s2240_altexprisco_infoamb_id:
            s2240_altexprisco_infoamb = get_object_or_404(s2240altExpRiscoinfoAmb, id = s2240_altexprisco_infoamb_id)
            
            s2240_altexprisco_fatrisco_form = form_s2240_altexprisco_fatrisco(
                initial={ 's2240_altexprisco_infoamb': s2240_altexprisco_infoamb })
            s2240_altexprisco_fatrisco_form.fields['s2240_altexprisco_infoamb'].widget.attrs['readonly'] = True
            s2240_altexprisco_fatrisco_lista = s2240altExpRiscofatRisco.objects.\
                filter(s2240_altexprisco_infoamb_id=s2240_altexprisco_infoamb.id).all()
                
        else:
            s2240_altexprisco_infoamb = None
            
        #s2240_altexprisco_infoamb_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's2240_altexprisco_infoamb' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2240_altexprisco_infoamb_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=s2240_altexprisco_infoamb_id, tabela='s2240_altexprisco_infoamb').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            's2240_altexprisco_infoamb': s2240_altexprisco_infoamb, 
            's2240_altexprisco_infoamb_form': s2240_altexprisco_infoamb_form, 
            'mensagem': mensagem, 
            's2240_altexprisco_infoamb_id': int(s2240_altexprisco_infoamb_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            's2240_altexprisco_fatrisco_form': s2240_altexprisco_fatrisco_form,
            's2240_altexprisco_fatrisco_lista': s2240_altexprisco_fatrisco_lista,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2240_altexprisco_infoamb_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's2240_altexprisco_infoamb_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2240_altexprisco_infoamb_salvar.html',
                filename="s2240_altexprisco_infoamb.pdf",
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
            response = render_to_response('s2240_altexprisco_infoamb_salvar.html', context)
            filename = "s2240_altexprisco_infoamb.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
        context = {
            'usuario': usuario, 
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)
