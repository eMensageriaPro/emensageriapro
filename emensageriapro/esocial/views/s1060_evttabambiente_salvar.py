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
from emensageriapro.s1060.models import s1060inclusao
from emensageriapro.s1060.forms import form_s1060_inclusao
from emensageriapro.s1060.models import s1060alteracao
from emensageriapro.s1060.forms import form_s1060_alteracao
from emensageriapro.s1060.models import s1060exclusao
from emensageriapro.s1060.forms import form_s1060_exclusao


@login_required
def salvar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL, TP_AMB
    
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1060_evttabambiente_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='s1060_evttabambiente')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    
    if s1060_evttabambiente_id:
        s1060_evttabambiente = get_object_or_404(s1060evtTabAmbiente, id = s1060_evttabambiente_id)
        
        if s1060_evttabambiente.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s1060_evttabambiente_apagar'] = 0
            dict_permissoes['s1060_evttabambiente_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s1060_evttabambiente_id:
            s1060_evttabambiente_form = form_s1060_evttabambiente(request.POST or None, instance = s1060_evttabambiente, 
                                         initial={'excluido': False})
        else:
            s1060_evttabambiente_form = form_s1060_evttabambiente(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
        if request.method == 'POST':
            if s1060_evttabambiente_form.is_valid():
            
                dados = s1060_evttabambiente_form.cleaned_data
                obj = s1060_evttabambiente_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s1060_evttabambiente_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's1060_evttabambiente', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s1060_evttabambiente), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's1060_evttabambiente', s1060_evttabambiente_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('s1060_evttabambiente_apagar', 's1060_evttabambiente_salvar', 's1060_evttabambiente'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s1060_evttabambiente_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s1060_evttabambiente_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
        s1060_evttabambiente_form = disabled_form_fields(s1060_evttabambiente_form, permissao.permite_editar)
        
        if s1060_evttabambiente_id:
            if s1060_evttabambiente.status != 0:
                s1060_evttabambiente_form = disabled_form_fields(s1060_evttabambiente_form, False)
        #s1060_evttabambiente_campos_multiple_passo3

        for field in s1060_evttabambiente_form.fields.keys():
            s1060_evttabambiente_form.fields[field].widget.attrs['ng-model'] = 's1060_evttabambiente_'+field
        if int(dict_hash['print']):
            s1060_evttabambiente_form = disabled_form_for_print(s1060_evttabambiente_form)

        
        s1060_inclusao_lista = None 
        s1060_inclusao_form = None 
        s1060_alteracao_lista = None 
        s1060_alteracao_form = None 
        s1060_exclusao_lista = None 
        s1060_exclusao_form = None 
        
        if s1060_evttabambiente_id:
            s1060_evttabambiente = get_object_or_404(s1060evtTabAmbiente, id = s1060_evttabambiente_id)
            
            s1060_inclusao_form = form_s1060_inclusao(
                initial={ 's1060_evttabambiente': s1060_evttabambiente })
            s1060_inclusao_form.fields['s1060_evttabambiente'].widget.attrs['readonly'] = True
            s1060_inclusao_lista = s1060inclusao.objects.\
                filter(s1060_evttabambiente_id=s1060_evttabambiente.id).all()
            s1060_alteracao_form = form_s1060_alteracao(
                initial={ 's1060_evttabambiente': s1060_evttabambiente })
            s1060_alteracao_form.fields['s1060_evttabambiente'].widget.attrs['readonly'] = True
            s1060_alteracao_lista = s1060alteracao.objects.\
                filter(s1060_evttabambiente_id=s1060_evttabambiente.id).all()
            s1060_exclusao_form = form_s1060_exclusao(
                initial={ 's1060_evttabambiente': s1060_evttabambiente })
            s1060_exclusao_form.fields['s1060_evttabambiente'].widget.attrs['readonly'] = True
            s1060_exclusao_lista = s1060exclusao.objects.\
                filter(s1060_evttabambiente_id=s1060_evttabambiente.id).all()
                
        else:
            s1060_evttabambiente = None
        #s1060_evttabambiente_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's1060_evttabambiente'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 's1060_evttabambiente' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1060_evttabambiente_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=s1060_evttabambiente_id, tabela='s1060_evttabambiente').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's1060_evttabambiente': s1060_evttabambiente, 
            's1060_evttabambiente_form': s1060_evttabambiente_form, 
            'mensagem': mensagem, 
            's1060_evttabambiente_id': int(s1060_evttabambiente_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            's1060_inclusao_form': s1060_inclusao_form,
            's1060_inclusao_lista': s1060_inclusao_lista,
            's1060_alteracao_form': s1060_alteracao_form,
            's1060_alteracao_lista': s1060_alteracao_lista,
            's1060_exclusao_form': s1060_exclusao_form,
            's1060_exclusao_lista': s1060_exclusao_lista,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1060_evttabambiente_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
            return render(request, 's1060_evttabambiente_salvar.html', context)
            
        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='s1060_evttabambiente_salvar.html',
                filename="s1060_evttabambiente.pdf",
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
            response = render_to_response('s1060_evttabambiente_salvar.html', context)
            filename = "s1060_evttabambiente.xls"
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
