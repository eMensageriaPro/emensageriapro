# eMensageriaAI #
#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s3000.views import s3000_idetrabalhador_apagar as s3000_idetrabalhador_apagar_views
from emensageriapro.s3000.views import s3000_idetrabalhador_listar as s3000_idetrabalhador_listar_views
from emensageriapro.s3000.views import s3000_idetrabalhador_salvar as s3000_idetrabalhador_salvar_views
from emensageriapro.s3000.views import s3000_idetrabalhador_api as s3000_idetrabalhador_api_views
from emensageriapro.s3000.views import s3000_idefolhapagto_apagar as s3000_idefolhapagto_apagar_views
from emensageriapro.s3000.views import s3000_idefolhapagto_listar as s3000_idefolhapagto_listar_views
from emensageriapro.s3000.views import s3000_idefolhapagto_salvar as s3000_idefolhapagto_salvar_views
from emensageriapro.s3000.views import s3000_idefolhapagto_api as s3000_idefolhapagto_api_views


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


    url(r'^s3000-idetrabalhador/apagar/(?P<pk>[0-9]+)/$',
        s3000_idetrabalhador_apagar_views.apagar,
        name='s3000_idetrabalhador_apagar'),

    url(r'^s3000-idetrabalhador/api/$',
        s3000_idetrabalhador_api_views.s3000ideTrabalhadorList.as_view() ),

    url(r'^s3000-idetrabalhador/api/(?P<pk>[0-9]+)/$',
        s3000_idetrabalhador_api_views.s3000ideTrabalhadorDetail.as_view() ),

    url(r'^s3000-idetrabalhador/$',
        s3000_idetrabalhador_listar_views.listar,
        name='s3000_idetrabalhador'),

    url(r'^s3000-idetrabalhador/salvar/(?P<pk>[0-9]+)/$',
        s3000_idetrabalhador_salvar_views.salvar,
        name='s3000_idetrabalhador_salvar'),

    url(r'^s3000-idetrabalhador/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s3000_idetrabalhador_salvar_views.salvar,
        name='s3000_idetrabalhador_salvar_tab'),

    url(r'^s3000-idetrabalhador/cadastrar/$',
        s3000_idetrabalhador_salvar_views.salvar,
        name='s3000_idetrabalhador_cadastrar'),

    url(r'^s3000-idetrabalhador/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s3000_idetrabalhador_salvar_views.salvar,
        name='s3000_idetrabalhador_salvar_output'),

    url(r'^s3000-idetrabalhador/(?P<output>[\w-]+)/$',
        s3000_idetrabalhador_listar_views.listar,
        name='s3000_idetrabalhador_output'),

    url(r'^s3000-idefolhapagto/apagar/(?P<pk>[0-9]+)/$',
        s3000_idefolhapagto_apagar_views.apagar,
        name='s3000_idefolhapagto_apagar'),

    url(r'^s3000-idefolhapagto/api/$',
        s3000_idefolhapagto_api_views.s3000ideFolhaPagtoList.as_view() ),

    url(r'^s3000-idefolhapagto/api/(?P<pk>[0-9]+)/$',
        s3000_idefolhapagto_api_views.s3000ideFolhaPagtoDetail.as_view() ),

    url(r'^s3000-idefolhapagto/$',
        s3000_idefolhapagto_listar_views.listar,
        name='s3000_idefolhapagto'),

    url(r'^s3000-idefolhapagto/salvar/(?P<pk>[0-9]+)/$',
        s3000_idefolhapagto_salvar_views.salvar,
        name='s3000_idefolhapagto_salvar'),

    url(r'^s3000-idefolhapagto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s3000_idefolhapagto_salvar_views.salvar,
        name='s3000_idefolhapagto_salvar_tab'),

    url(r'^s3000-idefolhapagto/cadastrar/$',
        s3000_idefolhapagto_salvar_views.salvar,
        name='s3000_idefolhapagto_cadastrar'),

    url(r'^s3000-idefolhapagto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s3000_idefolhapagto_salvar_views.salvar,
        name='s3000_idefolhapagto_salvar_output'),

    url(r'^s3000-idefolhapagto/(?P<output>[\w-]+)/$',
        s3000_idefolhapagto_listar_views.listar,
        name='s3000_idefolhapagto_output'),


]