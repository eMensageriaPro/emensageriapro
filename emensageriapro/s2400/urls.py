#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2400.views import s2400_brasil as s2400_brasil_views
from emensageriapro.s2400.views import s2400_dependente as s2400_dependente_views
from emensageriapro.s2400.views import s2400_exterior as s2400_exterior_views



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



url(r'^s2400-brasil/apagar/(?P<hash>.*)/$', 
        s2400_brasil_views.apagar, 
        name='s2400_brasil_apagar'),

url(r'^s2400-brasil/api/$',
            s2400_brasil_views.s2400brasilList.as_view() ),

        url(r'^s2400-brasil/api/(?P<pk>[0-9]+)/$',
            s2400_brasil_views.s2400brasilDetail.as_view() ),

url(r'^s2400-brasil/listar/(?P<hash>.*)/$', 
        s2400_brasil_views.listar, 
        name='s2400_brasil'),

url(r'^s2400-brasil/salvar/(?P<hash>.*)/$', 
        s2400_brasil_views.salvar, 
        name='s2400_brasil_salvar'),



url(r'^s2400-dependente/apagar/(?P<hash>.*)/$', 
        s2400_dependente_views.apagar, 
        name='s2400_dependente_apagar'),

url(r'^s2400-dependente/api/$',
            s2400_dependente_views.s2400dependenteList.as_view() ),

        url(r'^s2400-dependente/api/(?P<pk>[0-9]+)/$',
            s2400_dependente_views.s2400dependenteDetail.as_view() ),

url(r'^s2400-dependente/listar/(?P<hash>.*)/$', 
        s2400_dependente_views.listar, 
        name='s2400_dependente'),

url(r'^s2400-dependente/salvar/(?P<hash>.*)/$', 
        s2400_dependente_views.salvar, 
        name='s2400_dependente_salvar'),



url(r'^s2400-exterior/apagar/(?P<hash>.*)/$', 
        s2400_exterior_views.apagar, 
        name='s2400_exterior_apagar'),

url(r'^s2400-exterior/api/$',
            s2400_exterior_views.s2400exteriorList.as_view() ),

        url(r'^s2400-exterior/api/(?P<pk>[0-9]+)/$',
            s2400_exterior_views.s2400exteriorDetail.as_view() ),

url(r'^s2400-exterior/listar/(?P<hash>.*)/$', 
        s2400_exterior_views.listar, 
        name='s2400_exterior'),

url(r'^s2400-exterior/salvar/(?P<hash>.*)/$', 
        s2400_exterior_views.salvar, 
        name='s2400_exterior_salvar'),





]