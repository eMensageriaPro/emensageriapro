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
import json
from django.forms.models import model_to_dict
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
from emensageriapro.s1070.forms import *
from emensageriapro.s1070.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def apagar(request, pk):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO

    s1070_alteracao_novavalidade = get_object_or_404(s1070alteracaonovaValidade, id=pk)
    
    dados_evento = {}
    dados_evento = s1070_alteracao_novavalidade.evento()
            
    if request.method == 'POST':
    
        if dados_evento['status'] == STATUS_EVENTO_CADASTRADO:
            
            situacao_anterior = json.dumps(model_to_dict(s1070_alteracao_novavalidade), indent=4, sort_keys=True, default=str)
            obj = s1070alteracaonovaValidade.objects.get(id=pk)
            obj.delete(request=request)
            #s1070_alteracao_novavalidade_apagar_custom
            #s1070_alteracao_novavalidade_apagar_custom
            messages.success(request, u'Apagado com sucesso!')
            
            gravar_auditoria(situacao_anterior,
                             '', 
                             's1070_alteracao_novavalidade', 
                             pk, 
                             request.user.id, 3)
                             
        else:
        
            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
            
        if 's1070_alteracao_novavalidade' in request.session['return_page']:
        
            return redirect('s1070_alteracao_novavalidade')
            
        else:
        
            return redirect(
                request.session['return_page'], 
                pk=request.session['return_pk'])
            
    context = {
        'usuario': Usuarios.objects.get(user_id=request.user.id),
        'pk': pk,
        'dados_evento': dados_evento, 
        'modulos': ['s1070', ],
        'paginas': ['s1070_alteracao_novavalidade', ],
        'data': datetime.datetime.now(),
    }
    
    return render(request, 
                  's1070_alteracao_novavalidade_apagar.html', 
                  context)