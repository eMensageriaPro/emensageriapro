#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

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

"""

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404


@login_required
def create_token(request, pk):

    from rest_framework.authtoken.models import Token
    from emensageriapro.controle_de_acesso.models import Usuarios
    from django.contrib.auth.models import User

    usuario = get_object_or_404(Usuarios, id=pk)
    user = get_object_or_404(User, id=usuario.user_id)

    try:

        token = Token.objects.create(user=user)

    except:

        token = Token.objects.get(user=user)

    messages.success(request, 'Token criado com sucesso! Token: %s' % token.key)

    return redirect('usuarios_salvar', pk=pk)