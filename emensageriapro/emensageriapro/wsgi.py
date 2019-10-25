# coding:utf-8

"""
WSGI config for emensageria project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""


import os
from django.core.wsgi import get_wsgi_application


"""

eMensageria - Sistema de Gerenciamento de Eventos do eSocial
Link: <www.emensageria.com.br>
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

    Este programa é software livre: você pode redistribuí-lo e / ou modificar
    sob os termos da licença GNU Affero General Public License como
    publicado pela Free Software Foundation, seja versão 3 do
    Licença, ou (a seu critério) qualquer versão posterior.

    Este programa é distribuído na esperança de que seja útil,
    mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
    COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
    Licença Pública Geral GNU Affero para mais detalhes.

    Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
    junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emensageriapro.settings")

try:
    application = get_wsgi_application()
    print 'WSGI without exception'

except Exception as err:
    print(err)
