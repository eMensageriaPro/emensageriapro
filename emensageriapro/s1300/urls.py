#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1300.views import s1300_contribsind_apagar as s1300_contribsind_apagar_views
from emensageriapro.s1300.views import s1300_contribsind_listar as s1300_contribsind_listar_views
from emensageriapro.s1300.views import s1300_contribsind_salvar as s1300_contribsind_salvar_views
from emensageriapro.s1300.views import s1300_contribsind_api as s1300_contribsind_api_views


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


    url(r'^s1300-contribsind/apagar/(?P<pk>[0-9]+)/$',
        s1300_contribsind_apagar_views.apagar,
        name='s1300_contribsind_apagar'),

    url(r'^s1300-contribsind/api/$',
        s1300_contribsind_api_views.s1300contribSindList.as_view() ),

    url(r'^s1300-contribsind/api/(?P<pk>[0-9]+)/$',
        s1300_contribsind_api_views.s1300contribSindDetail.as_view() ),

    url(r'^s1300-contribsind/$',
        s1300_contribsind_listar_views.listar,
        name='s1300_contribsind'),

    url(r'^s1300-contribsind/salvar/(?P<pk>[0-9]+)/$',
        s1300_contribsind_salvar_views.salvar,
        name='s1300_contribsind_salvar'),

    url(r'^s1300-contribsind/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1300_contribsind_salvar_views.salvar,
        name='s1300_contribsind_salvar_tab'),

    url(r'^s1300-contribsind/cadastrar/$',
        s1300_contribsind_salvar_views.salvar,
        name='s1300_contribsind_cadastrar'),

    url(r'^s1300-contribsind/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1300_contribsind_salvar_views.salvar,
        name='s1300_contribsind_salvar_output'),

    url(r'^s1300-contribsind/(?P<output>[\w-]+)/$',
        s1300_contribsind_listar_views.listar,
        name='s1300_contribsind_output'),


]