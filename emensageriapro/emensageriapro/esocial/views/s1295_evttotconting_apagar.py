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

import json
from django.db import connection
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from emensageriapro.padrao import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *

@login_required
def apagar(request, pk):

    s1295_evttotconting = get_object_or_404(s1295evtTotConting, id=pk)

    if request.method == 'POST':

        if s1295_evttotconting.status == STATUS_EVENTO_CADASTRADO:

            situacao_anterior = json.dumps(model_to_dict(s1295_evttotconting), sort_keys=True, default=str)
            obj = s1295evtTotConting.objects.get(id=pk)
            obj.delete(request=request)

            sql_softdelete = ler_arquivo('/database/sql/s1295_softdelete_cascade.sql')
            with connection.cursor() as cursor:
                cursor.execute(sql_softdelete)

            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's1295_evttotconting', pk, request.user.id, 3)
        else:

            messages.error(request, u'''Não foi possivel apagar o evento, somente é
                                        possível apagar os eventos com status "Cadastrado"!''')

        if 'return_page' in request.session and request.session['return_page'] and 's1295-evttotconting' in request.session['return_page']:
            return redirect('s1295_evttotconting')

        else:
            return HttpResponseRedirect(request.session['return_page'])

    context = {
        'usuario': Usuarios.objects.get(user_id=request.user.id),
        'pk': pk,
        's1295_evttotconting': s1295_evttotconting,
        'data': datetime.datetime.now(),
        'modulos': ['esocial', ],
        'paginas': ['s1295_evttotconting', ],
    }

    return render(request, 's1295_evttotconting_apagar.html', context)