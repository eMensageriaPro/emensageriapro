#coding: utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from emensageriapro.controle_de_acesso.models import *
from django.shortcuts import get_object_or_404

#
# def json_to_dict(texto):
#     import json
#     dicionario = json.loads(texto)
#     return dicionario
#
#
# def dict_to_json(dicionario):
#     import json
#     json_string = json.dumps(dicionario)
#     return json_string
#
#
#
# def gera_senha(tamanho):
#     from random import choice
#     caracters = '0123456789abcdefghijlmnopqrstuwvxz!?@#$'
#     senha = ''
#     for char in xrange(tamanho):
#         senha += choice(caracters)
#     return senha



@login_required
def alterar_senha(request):

    usuario = get_object_or_404(Usuarios, user_id=request.user.id)

    if request.method == 'POST':

        if request.POST.get('senha') == request.POST.get('senha_repetir'):

            if request.POST.get('senha'):

                from django.contrib.auth.hashers import make_password
                hashed_password = make_password(request.POST.get('senha'))
                User.objects.filter(id=request.user.id).update(password=hashed_password)
                messages.success(request, 'Senha alterada com sucesso!')
        else:
            messages.error(request, 'As duas senhas inseridas estão diferentes, insira duas senhas iguais para alterar a senha corretamente!')

    context = {
        'usuario': usuario,
    }
    return render(request, 'login_alterar_senha.html', context)
