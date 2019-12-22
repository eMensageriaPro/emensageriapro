# eMensageriaAI #
#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1030.views import s1030_inclusao_apagar as s1030_inclusao_apagar_views
from emensageriapro.s1030.views import s1030_inclusao_listar as s1030_inclusao_listar_views
from emensageriapro.s1030.views import s1030_inclusao_salvar as s1030_inclusao_salvar_views
from emensageriapro.s1030.views import s1030_inclusao_api as s1030_inclusao_api_views
from emensageriapro.s1030.views import s1030_inclusao_cargopublico_apagar as s1030_inclusao_cargopublico_apagar_views
from emensageriapro.s1030.views import s1030_inclusao_cargopublico_listar as s1030_inclusao_cargopublico_listar_views
from emensageriapro.s1030.views import s1030_inclusao_cargopublico_salvar as s1030_inclusao_cargopublico_salvar_views
from emensageriapro.s1030.views import s1030_inclusao_cargopublico_api as s1030_inclusao_cargopublico_api_views
from emensageriapro.s1030.views import s1030_alteracao_apagar as s1030_alteracao_apagar_views
from emensageriapro.s1030.views import s1030_alteracao_listar as s1030_alteracao_listar_views
from emensageriapro.s1030.views import s1030_alteracao_salvar as s1030_alteracao_salvar_views
from emensageriapro.s1030.views import s1030_alteracao_api as s1030_alteracao_api_views
from emensageriapro.s1030.views import s1030_alteracao_cargopublico_apagar as s1030_alteracao_cargopublico_apagar_views
from emensageriapro.s1030.views import s1030_alteracao_cargopublico_listar as s1030_alteracao_cargopublico_listar_views
from emensageriapro.s1030.views import s1030_alteracao_cargopublico_salvar as s1030_alteracao_cargopublico_salvar_views
from emensageriapro.s1030.views import s1030_alteracao_cargopublico_api as s1030_alteracao_cargopublico_api_views
from emensageriapro.s1030.views import s1030_alteracao_novavalidade_apagar as s1030_alteracao_novavalidade_apagar_views
from emensageriapro.s1030.views import s1030_alteracao_novavalidade_listar as s1030_alteracao_novavalidade_listar_views
from emensageriapro.s1030.views import s1030_alteracao_novavalidade_salvar as s1030_alteracao_novavalidade_salvar_views
from emensageriapro.s1030.views import s1030_alteracao_novavalidade_api as s1030_alteracao_novavalidade_api_views
from emensageriapro.s1030.views import s1030_exclusao_apagar as s1030_exclusao_apagar_views
from emensageriapro.s1030.views import s1030_exclusao_listar as s1030_exclusao_listar_views
from emensageriapro.s1030.views import s1030_exclusao_salvar as s1030_exclusao_salvar_views
from emensageriapro.s1030.views import s1030_exclusao_api as s1030_exclusao_api_views


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


    url(r'^s1030-inclusao/apagar/(?P<pk>[0-9]+)/$',
        s1030_inclusao_apagar_views.apagar,
        name='s1030_inclusao_apagar'),

    url(r'^s1030-inclusao/api/$',
        s1030_inclusao_api_views.s1030inclusaoList.as_view() ),

    url(r'^s1030-inclusao/api/(?P<pk>[0-9]+)/$',
        s1030_inclusao_api_views.s1030inclusaoDetail.as_view() ),

    url(r'^s1030-inclusao/$',
        s1030_inclusao_listar_views.listar,
        name='s1030_inclusao'),

    url(r'^s1030-inclusao/salvar/(?P<pk>[0-9]+)/$',
        s1030_inclusao_salvar_views.salvar,
        name='s1030_inclusao_salvar'),

    url(r'^s1030-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1030_inclusao_salvar_views.salvar,
        name='s1030_inclusao_salvar_tab'),

    url(r'^s1030-inclusao/cadastrar/$',
        s1030_inclusao_salvar_views.salvar,
        name='s1030_inclusao_cadastrar'),

    url(r'^s1030-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1030_inclusao_salvar_views.salvar,
        name='s1030_inclusao_salvar_output'),

    url(r'^s1030-inclusao/(?P<output>[\w-]+)/$',
        s1030_inclusao_listar_views.listar,
        name='s1030_inclusao_output'),

    url(r'^s1030-inclusao-cargopublico/apagar/(?P<pk>[0-9]+)/$',
        s1030_inclusao_cargopublico_apagar_views.apagar,
        name='s1030_inclusao_cargopublico_apagar'),

    url(r'^s1030-inclusao-cargopublico/api/$',
        s1030_inclusao_cargopublico_api_views.s1030inclusaocargoPublicoList.as_view() ),

    url(r'^s1030-inclusao-cargopublico/api/(?P<pk>[0-9]+)/$',
        s1030_inclusao_cargopublico_api_views.s1030inclusaocargoPublicoDetail.as_view() ),

    url(r'^s1030-inclusao-cargopublico/$',
        s1030_inclusao_cargopublico_listar_views.listar,
        name='s1030_inclusao_cargopublico'),

    url(r'^s1030-inclusao-cargopublico/salvar/(?P<pk>[0-9]+)/$',
        s1030_inclusao_cargopublico_salvar_views.salvar,
        name='s1030_inclusao_cargopublico_salvar'),

    url(r'^s1030-inclusao-cargopublico/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1030_inclusao_cargopublico_salvar_views.salvar,
        name='s1030_inclusao_cargopublico_salvar_tab'),

    url(r'^s1030-inclusao-cargopublico/cadastrar/$',
        s1030_inclusao_cargopublico_salvar_views.salvar,
        name='s1030_inclusao_cargopublico_cadastrar'),

    url(r'^s1030-inclusao-cargopublico/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1030_inclusao_cargopublico_salvar_views.salvar,
        name='s1030_inclusao_cargopublico_salvar_output'),

    url(r'^s1030-inclusao-cargopublico/(?P<output>[\w-]+)/$',
        s1030_inclusao_cargopublico_listar_views.listar,
        name='s1030_inclusao_cargopublico_output'),

    url(r'^s1030-alteracao/apagar/(?P<pk>[0-9]+)/$',
        s1030_alteracao_apagar_views.apagar,
        name='s1030_alteracao_apagar'),

    url(r'^s1030-alteracao/api/$',
        s1030_alteracao_api_views.s1030alteracaoList.as_view() ),

    url(r'^s1030-alteracao/api/(?P<pk>[0-9]+)/$',
        s1030_alteracao_api_views.s1030alteracaoDetail.as_view() ),

    url(r'^s1030-alteracao/$',
        s1030_alteracao_listar_views.listar,
        name='s1030_alteracao'),

    url(r'^s1030-alteracao/salvar/(?P<pk>[0-9]+)/$',
        s1030_alteracao_salvar_views.salvar,
        name='s1030_alteracao_salvar'),

    url(r'^s1030-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1030_alteracao_salvar_views.salvar,
        name='s1030_alteracao_salvar_tab'),

    url(r'^s1030-alteracao/cadastrar/$',
        s1030_alteracao_salvar_views.salvar,
        name='s1030_alteracao_cadastrar'),

    url(r'^s1030-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1030_alteracao_salvar_views.salvar,
        name='s1030_alteracao_salvar_output'),

    url(r'^s1030-alteracao/(?P<output>[\w-]+)/$',
        s1030_alteracao_listar_views.listar,
        name='s1030_alteracao_output'),

    url(r'^s1030-alteracao-cargopublico/apagar/(?P<pk>[0-9]+)/$',
        s1030_alteracao_cargopublico_apagar_views.apagar,
        name='s1030_alteracao_cargopublico_apagar'),

    url(r'^s1030-alteracao-cargopublico/api/$',
        s1030_alteracao_cargopublico_api_views.s1030alteracaocargoPublicoList.as_view() ),

    url(r'^s1030-alteracao-cargopublico/api/(?P<pk>[0-9]+)/$',
        s1030_alteracao_cargopublico_api_views.s1030alteracaocargoPublicoDetail.as_view() ),

    url(r'^s1030-alteracao-cargopublico/$',
        s1030_alteracao_cargopublico_listar_views.listar,
        name='s1030_alteracao_cargopublico'),

    url(r'^s1030-alteracao-cargopublico/salvar/(?P<pk>[0-9]+)/$',
        s1030_alteracao_cargopublico_salvar_views.salvar,
        name='s1030_alteracao_cargopublico_salvar'),

    url(r'^s1030-alteracao-cargopublico/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1030_alteracao_cargopublico_salvar_views.salvar,
        name='s1030_alteracao_cargopublico_salvar_tab'),

    url(r'^s1030-alteracao-cargopublico/cadastrar/$',
        s1030_alteracao_cargopublico_salvar_views.salvar,
        name='s1030_alteracao_cargopublico_cadastrar'),

    url(r'^s1030-alteracao-cargopublico/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1030_alteracao_cargopublico_salvar_views.salvar,
        name='s1030_alteracao_cargopublico_salvar_output'),

    url(r'^s1030-alteracao-cargopublico/(?P<output>[\w-]+)/$',
        s1030_alteracao_cargopublico_listar_views.listar,
        name='s1030_alteracao_cargopublico_output'),

    url(r'^s1030-alteracao-novavalidade/apagar/(?P<pk>[0-9]+)/$',
        s1030_alteracao_novavalidade_apagar_views.apagar,
        name='s1030_alteracao_novavalidade_apagar'),

    url(r'^s1030-alteracao-novavalidade/api/$',
        s1030_alteracao_novavalidade_api_views.s1030alteracaonovaValidadeList.as_view() ),

    url(r'^s1030-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
        s1030_alteracao_novavalidade_api_views.s1030alteracaonovaValidadeDetail.as_view() ),

    url(r'^s1030-alteracao-novavalidade/$',
        s1030_alteracao_novavalidade_listar_views.listar,
        name='s1030_alteracao_novavalidade'),

    url(r'^s1030-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/$',
        s1030_alteracao_novavalidade_salvar_views.salvar,
        name='s1030_alteracao_novavalidade_salvar'),

    url(r'^s1030-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1030_alteracao_novavalidade_salvar_views.salvar,
        name='s1030_alteracao_novavalidade_salvar_tab'),

    url(r'^s1030-alteracao-novavalidade/cadastrar/$',
        s1030_alteracao_novavalidade_salvar_views.salvar,
        name='s1030_alteracao_novavalidade_cadastrar'),

    url(r'^s1030-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1030_alteracao_novavalidade_salvar_views.salvar,
        name='s1030_alteracao_novavalidade_salvar_output'),

    url(r'^s1030-alteracao-novavalidade/(?P<output>[\w-]+)/$',
        s1030_alteracao_novavalidade_listar_views.listar,
        name='s1030_alteracao_novavalidade_output'),

    url(r'^s1030-exclusao/apagar/(?P<pk>[0-9]+)/$',
        s1030_exclusao_apagar_views.apagar,
        name='s1030_exclusao_apagar'),

    url(r'^s1030-exclusao/api/$',
        s1030_exclusao_api_views.s1030exclusaoList.as_view() ),

    url(r'^s1030-exclusao/api/(?P<pk>[0-9]+)/$',
        s1030_exclusao_api_views.s1030exclusaoDetail.as_view() ),

    url(r'^s1030-exclusao/$',
        s1030_exclusao_listar_views.listar,
        name='s1030_exclusao'),

    url(r'^s1030-exclusao/salvar/(?P<pk>[0-9]+)/$',
        s1030_exclusao_salvar_views.salvar,
        name='s1030_exclusao_salvar'),

    url(r'^s1030-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1030_exclusao_salvar_views.salvar,
        name='s1030_exclusao_salvar_tab'),

    url(r'^s1030-exclusao/cadastrar/$',
        s1030_exclusao_salvar_views.salvar,
        name='s1030_exclusao_cadastrar'),

    url(r'^s1030-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1030_exclusao_salvar_views.salvar,
        name='s1030_exclusao_salvar_output'),

    url(r'^s1030-exclusao/(?P<output>[\w-]+)/$',
        s1030_exclusao_listar_views.listar,
        name='s1030_exclusao_output'),


]