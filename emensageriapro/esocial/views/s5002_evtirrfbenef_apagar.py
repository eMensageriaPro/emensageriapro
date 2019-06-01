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
from emensageriapro.s1000.models import s1000inclusao
from emensageriapro.s1000.models import s1000alteracao
from emensageriapro.s1000.models import s1000exclusao
from emensageriapro.s1000.forms import form_s1000_inclusao
from emensageriapro.s1000.forms import form_s1000_alteracao
from emensageriapro.s1000.forms import form_s1000_exclusao


@login_required
def apagar(request, hash):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s5002_evtirrfbenef_id = int(dict_hash['id'])
        
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    
    s5002_evtirrfbenef = get_object_or_404(s5002evtIrrfBenef, id=s5002_evtirrfbenef_id)
    
    if request.method == 'POST':
    
        if s5002_evtirrfbenef.status == STATUS_EVENTO_CADASTRADO:
        
            import json
            from django.forms.models import model_to_dict
            
            situacao_anterior = json.dumps(model_to_dict(s5002_evtirrfbenef), indent=4, sort_keys=True, default=str)
            obj = s5002evtIrrfBenef.objects.get(id = s5002_evtirrfbenef_id)
            obj.delete(request=request)
            #s5002_evtirrfbenef_apagar_custom
            #s5002_evtirrfbenef_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '', 
                             's5002_evtirrfbenef', s5002_evtirrfbenef_id, usuario_id, 3)
        else:
            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
            
        if request.session['retorno_pagina']== 's5002_evtirrfbenef_salvar':
        
            return redirect('s5002_evtirrfbenef', 
                            hash=request.session['retorno_hash'])
            
        else:
        
            return redirect(request.session['retorno_pagina'], 
                            hash=request.session['retorno_hash'])
            
    context = {
        's5002_evtirrfbenef': s5002_evtirrfbenef, 
        'usuario': usuario, 
        'data': datetime.datetime.now(),
        'modulos': ['esocial', ],
        'paginas': ['s5002_evtirrfbenef', ],
        'hash': hash,
    }
    
    return render(request, 's5002_evtirrfbenef_apagar.html', context)