#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2405.views import s2405_brasil as s2405_brasil_views
from emensageriapro.s2405.views import s2405_dependente as s2405_dependente_views
from emensageriapro.s2405.views import s2405_exterior as s2405_exterior_views



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

urlpatterns = [



url(r'^s2405-brasil/apagar/(?P<hash>.*)/$', 
        s2405_brasil_views.apagar, 
        name='s2405_brasil_apagar'),

url(r'^s2405-brasil/api/$',
            s2405_brasil_views.s2405brasilList.as_view() ),

        url(r'^s2405-brasil/api/(?P<pk>[0-9]+)/$',
            s2405_brasil_views.s2405brasilDetail.as_view() ),

url(r'^s2405-brasil/listar/(?P<hash>.*)/$', 
        s2405_brasil_views.listar, 
        name='s2405_brasil'),

url(r'^s2405-brasil/salvar/(?P<hash>.*)/$', 
        s2405_brasil_views.salvar, 
        name='s2405_brasil_salvar'),



url(r'^s2405-dependente/apagar/(?P<hash>.*)/$', 
        s2405_dependente_views.apagar, 
        name='s2405_dependente_apagar'),

url(r'^s2405-dependente/api/$',
            s2405_dependente_views.s2405dependenteList.as_view() ),

        url(r'^s2405-dependente/api/(?P<pk>[0-9]+)/$',
            s2405_dependente_views.s2405dependenteDetail.as_view() ),

url(r'^s2405-dependente/listar/(?P<hash>.*)/$', 
        s2405_dependente_views.listar, 
        name='s2405_dependente'),

url(r'^s2405-dependente/salvar/(?P<hash>.*)/$', 
        s2405_dependente_views.salvar, 
        name='s2405_dependente_salvar'),



url(r'^s2405-exterior/apagar/(?P<hash>.*)/$', 
        s2405_exterior_views.apagar, 
        name='s2405_exterior_apagar'),

url(r'^s2405-exterior/api/$',
            s2405_exterior_views.s2405exteriorList.as_view() ),

        url(r'^s2405-exterior/api/(?P<pk>[0-9]+)/$',
            s2405_exterior_views.s2405exteriorDetail.as_view() ),

url(r'^s2405-exterior/listar/(?P<hash>.*)/$', 
        s2405_exterior_views.listar, 
        name='s2405_exterior'),

url(r'^s2405-exterior/salvar/(?P<hash>.*)/$', 
        s2405_exterior_views.salvar, 
        name='s2405_exterior_salvar'),





]