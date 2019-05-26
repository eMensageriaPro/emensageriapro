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
from emensageriapro.s2306.forms import *
from emensageriapro.s2306.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2306.models import s2306cargoFuncao
from emensageriapro.s2306.forms import form_s2306_cargofuncao
from emensageriapro.s2306.models import s2306remuneracao
from emensageriapro.s2306.forms import form_s2306_remuneracao
from emensageriapro.s2306.models import s2306infoTrabCedido
from emensageriapro.s2306.forms import form_s2306_infotrabcedido
from emensageriapro.s2306.models import s2306infoEstagiario
from emensageriapro.s2306.forms import form_s2306_infoestagiario



@login_required
def salvar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    try: 
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        s2306_infocomplementares_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='s2306_infocomplementares')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2306_infocomplementares_id:
        s2306_infocomplementares = get_object_or_404(s2306infoComplementares, id = s2306_infocomplementares_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    if s2306_infocomplementares_id:
        dados_evento = s2306_infocomplementares.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2306_infocomplementares_apagar'] = 0
            dict_permissoes['s2306_infocomplementares_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2306_infocomplementares_id:
            s2306_infocomplementares_form = form_s2306_infocomplementares(request.POST or None, instance = s2306_infocomplementares,  
                                         initial={'excluido': False})
        else:
            s2306_infocomplementares_form = form_s2306_infocomplementares(request.POST or None, 
                                         initial={'excluido': False})
        if request.method == 'POST':
            if s2306_infocomplementares_form.is_valid():
            
                dados = s2306_infocomplementares_form.cleaned_data
                obj = s2306_infocomplementares_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s2306_infocomplementares_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2306_infocomplementares', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2306_infocomplementares), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2306_infocomplementares', s2306_infocomplementares_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('s2306_infocomplementares_apagar', 's2306_infocomplementares_salvar', 's2306_infocomplementares'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2306_infocomplementares_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2306_infocomplementares_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        s2306_infocomplementares_form = disabled_form_fields(s2306_infocomplementares_form, permissao.permite_editar)
        
        if s2306_infocomplementares_id:
            if dados_evento['status'] != 0:
                s2306_infocomplementares_form = disabled_form_fields(s2306_infocomplementares_form, 0)
                
        #s2306_infocomplementares_campos_multiple_passo3
        
        if int(dict_hash['print']):
            s2306_infocomplementares_form = disabled_form_for_print(s2306_infocomplementares_form)
            
        
        s2306_cargofuncao_lista = None 
        s2306_cargofuncao_form = None 
        s2306_remuneracao_lista = None 
        s2306_remuneracao_form = None 
        s2306_infotrabcedido_lista = None 
        s2306_infotrabcedido_form = None 
        s2306_infoestagiario_lista = None 
        s2306_infoestagiario_form = None 
        
        if s2306_infocomplementares_id:
            s2306_infocomplementares = get_object_or_404(s2306infoComplementares, id = s2306_infocomplementares_id)
            
            s2306_cargofuncao_form = form_s2306_cargofuncao(
                initial={ 's2306_infocomplementares': s2306_infocomplementares })
            s2306_cargofuncao_form.fields['s2306_infocomplementares'].widget.attrs['readonly'] = True
            s2306_cargofuncao_lista = s2306cargoFuncao.objects.\
                filter(s2306_infocomplementares_id=s2306_infocomplementares.id).all()
            s2306_remuneracao_form = form_s2306_remuneracao(
                initial={ 's2306_infocomplementares': s2306_infocomplementares })
            s2306_remuneracao_form.fields['s2306_infocomplementares'].widget.attrs['readonly'] = True
            s2306_remuneracao_lista = s2306remuneracao.objects.\
                filter(s2306_infocomplementares_id=s2306_infocomplementares.id).all()
            s2306_infotrabcedido_form = form_s2306_infotrabcedido(
                initial={ 's2306_infocomplementares': s2306_infocomplementares })
            s2306_infotrabcedido_form.fields['s2306_infocomplementares'].widget.attrs['readonly'] = True
            s2306_infotrabcedido_lista = s2306infoTrabCedido.objects.\
                filter(s2306_infocomplementares_id=s2306_infocomplementares.id).all()
            s2306_infoestagiario_form = form_s2306_infoestagiario(
                initial={ 's2306_infocomplementares': s2306_infocomplementares })
            s2306_infoestagiario_form.fields['s2306_infocomplementares'].widget.attrs['readonly'] = True
            s2306_infoestagiario_lista = s2306infoEstagiario.objects.\
                filter(s2306_infocomplementares_id=s2306_infocomplementares.id).all()
                
        else:
            s2306_infocomplementares = None
            
        #s2306_infocomplementares_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's2306_infocomplementares' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2306_infocomplementares_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=s2306_infocomplementares_id, tabela='s2306_infocomplementares').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            's2306_infocomplementares': s2306_infocomplementares, 
            's2306_infocomplementares_form': s2306_infocomplementares_form, 
            'mensagem': mensagem, 
            's2306_infocomplementares_id': int(s2306_infocomplementares_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            's2306_cargofuncao_form': s2306_cargofuncao_form,
            's2306_cargofuncao_lista': s2306_cargofuncao_lista,
            's2306_remuneracao_form': s2306_remuneracao_form,
            's2306_remuneracao_lista': s2306_remuneracao_lista,
            's2306_infotrabcedido_form': s2306_infotrabcedido_form,
            's2306_infotrabcedido_lista': s2306_infotrabcedido_lista,
            's2306_infoestagiario_form': s2306_infoestagiario_form,
            's2306_infoestagiario_lista': s2306_infoestagiario_lista,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2306_infocomplementares_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's2306_infocomplementares_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2306_infocomplementares_salvar.html',
                filename="s2306_infocomplementares.pdf",
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
            response = render_to_response('s2306_infocomplementares_salvar.html', context)
            filename = "s2306_infocomplementares.xls"
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
