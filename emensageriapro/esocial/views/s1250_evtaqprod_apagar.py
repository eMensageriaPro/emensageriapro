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


@login_required
def apagar(request, pk):

    import json
    from django.forms.models import model_to_dict
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO

    s1250_evtaqprod = get_object_or_404(s1250evtAqProd, id=pk)

    if request.method == 'POST':

        if s1250_evtaqprod.status == STATUS_EVENTO_CADASTRADO:

            situacao_anterior = json.dumps(model_to_dict(s1250_evtaqprod), indent=4, sort_keys=True, default=str)
            obj = s1250evtAqProd.objects.get(id=pk)
            obj.delete(request=request)
            #s1250_evtaqprod_apagar_custom
            #s1250_evtaqprod_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's1250_evtaqprod', pk, request.user.id, 3)
        else:

            messages.error(request, u'''Não foi possivel apagar o evento, somente é
                                        possível apagar os eventos com status "Cadastrado"!''')

        if 's1250-evtaqprod' in request.session['return']:
            return redirect('s1250_evtaqprod')

        else:
            return HttpResponseRedirect(request.session['return'])

    else:
        request.session['return'] = request.META.get('HTTP_REFERER')

    context = {
        'usuario': Usuarios.objects.get(user_id=request.user.id),
        'pk': pk,
        's1250_evtaqprod': s1250_evtaqprod,
        'data': datetime.datetime.now(),
        'modulos': ['esocial', ],
        'paginas': ['s1250_evtaqprod', ],
    }

    return render(request, 's1250_evtaqprod_apagar.html', context)