# eMensageriaAI #
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
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s1030.models import s1030alteracaocargoPublico


@login_required
def apagar(request, pk):

    s1030_alteracao_cargopublico = get_object_or_404(s1030alteracaocargoPublico, id=pk)

    dados_evento = s1030_alteracao_cargopublico.evento()

    if request.method == 'POST':

        if dados_evento['status'] == STATUS_EVENTO_CADASTRADO:

            situacao_anterior = json.dumps(model_to_dict(s1030_alteracao_cargopublico), sort_keys=True, default=str)
            obj = s1030alteracaocargoPublico.objects.get(id=pk)
            obj.delete(request=request)

            sql_softdelete = ler_arquivo('/database/sql/s1030_softdelete_cascade.sql')
            with connection.cursor() as cursor:
                cursor.execute(sql_softdelete)

            messages.success(request, u'Apagado com sucesso!')

            gravar_auditoria(situacao_anterior,
                             '',
                             's1030_alteracao_cargopublico',
                             pk,
                             request.user.id, 3)
         
        else:

            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if 'return_page' in request.session and request.session['return_page'] and 's1030-alteracao-cargopublico' in request.session['return_page']:
            return redirect('s1030_alteracao_cargopublico')

        else:
            return HttpResponseRedirect(request.session['return_page'])

    context = {
        'usuario': Usuarios.objects.get(user_id=request.user.id),
        'pk': pk,
        'dados_evento': dados_evento,
        'modulos': ['s1030', ],
        'paginas': ['s1030_alteracao_cargopublico', ],
        'data': datetime.datetime.now(),
    }

    return render(request,
                  's1030_alteracao_cargopublico_apagar.html',
                  context)