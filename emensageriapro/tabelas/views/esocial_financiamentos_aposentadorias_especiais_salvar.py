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
from emensageriapro.tabelas.forms import *
from emensageriapro.tabelas.models import *
from emensageriapro.controle_de_acesso.models import *



@login_required
def salvar(request, hash):

    try: 
        usuario_id = request.user.id 
        dict_hash = get_hash_url( hash )
        esocial_financiamentos_aposentadorias_especiais_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='esocial_financiamentos_aposentadorias_especiais')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    if esocial_financiamentos_aposentadorias_especiais_id:
        esocial_financiamentos_aposentadorias_especiais = get_object_or_404(eSocialFinanciamentosAposentadoriasEspeciais, id = esocial_financiamentos_aposentadorias_especiais_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if esocial_financiamentos_aposentadorias_especiais_id:
            esocial_financiamentos_aposentadorias_especiais_form = form_esocial_financiamentos_aposentadorias_especiais(request.POST or None, instance = esocial_financiamentos_aposentadorias_especiais, 
                                         initial = {'excluido': False})
        else:
            esocial_financiamentos_aposentadorias_especiais_form = form_esocial_financiamentos_aposentadorias_especiais(request.POST or None,
                                         initial = {'excluido': False})
        if request.method == 'POST':
            if esocial_financiamentos_aposentadorias_especiais_form.is_valid():
            
                dados = esocial_financiamentos_aposentadorias_especiais_form.cleaned_data
                obj = esocial_financiamentos_aposentadorias_especiais_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not esocial_financiamentos_aposentadorias_especiais_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'esocial_financiamentos_aposentadorias_especiais', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(esocial_financiamentos_aposentadorias_especiais), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'esocial_financiamentos_aposentadorias_especiais', esocial_financiamentos_aposentadorias_especiais_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('esocial_financiamentos_aposentadorias_especiais_apagar', 'esocial_financiamentos_aposentadorias_especiais_salvar', 'esocial_financiamentos_aposentadorias_especiais'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if esocial_financiamentos_aposentadorias_especiais_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('esocial_financiamentos_aposentadorias_especiais_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        esocial_financiamentos_aposentadorias_especiais_form = disabled_form_fields(esocial_financiamentos_aposentadorias_especiais_form, permissao.permite_editar)
        
        #esocial_financiamentos_aposentadorias_especiais_campos_multiple_passo3
        
        if int(dict_hash['print']):
            esocial_financiamentos_aposentadorias_especiais_form = disabled_form_for_print(esocial_financiamentos_aposentadorias_especiais_form)
            
        #esocial_financiamentos_aposentadorias_especiais_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'esocial_financiamentos_aposentadorias_especiais' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'esocial_financiamentos_aposentadorias_especiais_salvar'
        context = {
            'esocial_financiamentos_aposentadorias_especiais': esocial_financiamentos_aposentadorias_especiais, 
            'esocial_financiamentos_aposentadorias_especiais_form': esocial_financiamentos_aposentadorias_especiais_form, 
            'mensagem': mensagem, 
            'esocial_financiamentos_aposentadorias_especiais_id': int(esocial_financiamentos_aposentadorias_especiais_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #esocial_financiamentos_aposentadorias_especiais_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'esocial_financiamentos_aposentadorias_especiais_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='esocial_financiamentos_aposentadorias_especiais_salvar.html',
                filename="esocial_financiamentos_aposentadorias_especiais.pdf",
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
            response = render_to_response('esocial_financiamentos_aposentadorias_especiais_salvar.html', context)
            filename = "esocial_financiamentos_aposentadorias_especiais.xls"
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
