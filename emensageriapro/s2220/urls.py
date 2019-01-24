#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2220.views import s2220_exame as s2220_exame_views



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

urlpatterns = [



url(r'^s2220-exame/apagar/(?P<hash>.*)/$', 
        s2220_exame_views.apagar, 
        name='s2220_exame_apagar'),

url(r'^s2220-exame/api/$',
            s2220_exame_views.s2220exameList.as_view() ),

        url(r'^s2220-exame/api/(?P<pk>[0-9]+)/$',
            s2220_exame_views.s2220exameDetail.as_view() ),

url(r'^s2220-exame/listar/(?P<hash>.*)/$', 
        s2220_exame_views.listar, 
        name='s2220_exame'),

url(r'^s2220-exame/salvar/(?P<hash>.*)/$', 
        s2220_exame_views.salvar, 
        name='s2220_exame_salvar'),





]