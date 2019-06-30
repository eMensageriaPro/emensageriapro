#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r4040.views import r4040_idenat_apagar as r4040_idenat_apagar_views
from emensageriapro.r4040.views import r4040_idenat_listar as r4040_idenat_listar_views
from emensageriapro.r4040.views import r4040_idenat_salvar as r4040_idenat_salvar_views
from emensageriapro.r4040.views import r4040_idenat_api as r4040_idenat_api_views
from emensageriapro.r4040.views import r4040_infopgto_apagar as r4040_infopgto_apagar_views
from emensageriapro.r4040.views import r4040_infopgto_listar as r4040_infopgto_listar_views
from emensageriapro.r4040.views import r4040_infopgto_salvar as r4040_infopgto_salvar_views
from emensageriapro.r4040.views import r4040_infopgto_api as r4040_infopgto_api_views



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


    url(r'^r4040-idenat/apagar/(?P<pk>[0-9]+)/$',
        r4040_idenat_apagar_views.apagar,
        name='r4040_idenat_apagar'),

    url(r'^r4040-idenat/api/$',
        r4040_idenat_api_views.r4040ideNatList.as_view() ),

    url(r'^r4040-idenat/api/(?P<pk>[0-9]+)/$',
        r4040_idenat_api_views.r4040ideNatDetail.as_view() ),

    url(r'^r4040-idenat/$',
        r4040_idenat_listar_views.listar,
        name='r4040_idenat'),

    url(r'^r4040-idenat/salvar/(?P<pk>[0-9]+)/$',
        r4040_idenat_salvar_views.salvar,
        name='r4040_idenat_salvar'),

    url(r'^r4040-idenat/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4040_idenat_salvar_views.salvar,
        name='r4040_idenat_salvar_tab'),

    url(r'^r4040-idenat/cadastrar/$',
        r4040_idenat_salvar_views.salvar,
        name='r4040_idenat_cadastrar'),

    url(r'^r4040-idenat/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4040_idenat_salvar_views.salvar,
        name='r4040_idenat_salvar_output'),

    url(r'^r4040-idenat/(?P<output>[\w-]+)/$',
        r4040_idenat_listar_views.listar,
        name='r4040_idenat_output'),

    url(r'^r4040-infopgto/apagar/(?P<pk>[0-9]+)/$',
        r4040_infopgto_apagar_views.apagar,
        name='r4040_infopgto_apagar'),

    url(r'^r4040-infopgto/api/$',
        r4040_infopgto_api_views.r4040infoPgtoList.as_view() ),

    url(r'^r4040-infopgto/api/(?P<pk>[0-9]+)/$',
        r4040_infopgto_api_views.r4040infoPgtoDetail.as_view() ),

    url(r'^r4040-infopgto/$',
        r4040_infopgto_listar_views.listar,
        name='r4040_infopgto'),

    url(r'^r4040-infopgto/salvar/(?P<pk>[0-9]+)/$',
        r4040_infopgto_salvar_views.salvar,
        name='r4040_infopgto_salvar'),

    url(r'^r4040-infopgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4040_infopgto_salvar_views.salvar,
        name='r4040_infopgto_salvar_tab'),

    url(r'^r4040-infopgto/cadastrar/$',
        r4040_infopgto_salvar_views.salvar,
        name='r4040_infopgto_cadastrar'),

    url(r'^r4040-infopgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4040_infopgto_salvar_views.salvar,
        name='r4040_infopgto_salvar_output'),

    url(r'^r4040-infopgto/(?P<output>[\w-]+)/$',
        r4040_infopgto_listar_views.listar,
        name='r4040_infopgto_output'),


]