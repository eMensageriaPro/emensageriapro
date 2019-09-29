#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1060.views import s1060_inclusao_apagar as s1060_inclusao_apagar_views
from emensageriapro.s1060.views import s1060_inclusao_listar as s1060_inclusao_listar_views
from emensageriapro.s1060.views import s1060_inclusao_salvar as s1060_inclusao_salvar_views
from emensageriapro.s1060.views import s1060_inclusao_api as s1060_inclusao_api_views
from emensageriapro.s1060.views import s1060_alteracao_apagar as s1060_alteracao_apagar_views
from emensageriapro.s1060.views import s1060_alteracao_listar as s1060_alteracao_listar_views
from emensageriapro.s1060.views import s1060_alteracao_salvar as s1060_alteracao_salvar_views
from emensageriapro.s1060.views import s1060_alteracao_api as s1060_alteracao_api_views
from emensageriapro.s1060.views import s1060_alteracao_novavalidade_apagar as s1060_alteracao_novavalidade_apagar_views
from emensageriapro.s1060.views import s1060_alteracao_novavalidade_listar as s1060_alteracao_novavalidade_listar_views
from emensageriapro.s1060.views import s1060_alteracao_novavalidade_salvar as s1060_alteracao_novavalidade_salvar_views
from emensageriapro.s1060.views import s1060_alteracao_novavalidade_api as s1060_alteracao_novavalidade_api_views
from emensageriapro.s1060.views import s1060_exclusao_apagar as s1060_exclusao_apagar_views
from emensageriapro.s1060.views import s1060_exclusao_listar as s1060_exclusao_listar_views
from emensageriapro.s1060.views import s1060_exclusao_salvar as s1060_exclusao_salvar_views
from emensageriapro.s1060.views import s1060_exclusao_api as s1060_exclusao_api_views


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


    url(r'^s1060-inclusao/apagar/(?P<pk>[0-9]+)/$',
        s1060_inclusao_apagar_views.apagar,
        name='s1060_inclusao_apagar'),

    url(r'^s1060-inclusao/api/$',
        s1060_inclusao_api_views.s1060inclusaoList.as_view() ),

    url(r'^s1060-inclusao/api/(?P<pk>[0-9]+)/$',
        s1060_inclusao_api_views.s1060inclusaoDetail.as_view() ),

    url(r'^s1060-inclusao/$',
        s1060_inclusao_listar_views.listar,
        name='s1060_inclusao'),

    url(r'^s1060-inclusao/salvar/(?P<pk>[0-9]+)/$',
        s1060_inclusao_salvar_views.salvar,
        name='s1060_inclusao_salvar'),

    url(r'^s1060-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1060_inclusao_salvar_views.salvar,
        name='s1060_inclusao_salvar_tab'),

    url(r'^s1060-inclusao/cadastrar/$',
        s1060_inclusao_salvar_views.salvar,
        name='s1060_inclusao_cadastrar'),

    url(r'^s1060-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1060_inclusao_salvar_views.salvar,
        name='s1060_inclusao_salvar_output'),

    url(r'^s1060-inclusao/(?P<output>[\w-]+)/$',
        s1060_inclusao_listar_views.listar,
        name='s1060_inclusao_output'),

    url(r'^s1060-alteracao/apagar/(?P<pk>[0-9]+)/$',
        s1060_alteracao_apagar_views.apagar,
        name='s1060_alteracao_apagar'),

    url(r'^s1060-alteracao/api/$',
        s1060_alteracao_api_views.s1060alteracaoList.as_view() ),

    url(r'^s1060-alteracao/api/(?P<pk>[0-9]+)/$',
        s1060_alteracao_api_views.s1060alteracaoDetail.as_view() ),

    url(r'^s1060-alteracao/$',
        s1060_alteracao_listar_views.listar,
        name='s1060_alteracao'),

    url(r'^s1060-alteracao/salvar/(?P<pk>[0-9]+)/$',
        s1060_alteracao_salvar_views.salvar,
        name='s1060_alteracao_salvar'),

    url(r'^s1060-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1060_alteracao_salvar_views.salvar,
        name='s1060_alteracao_salvar_tab'),

    url(r'^s1060-alteracao/cadastrar/$',
        s1060_alteracao_salvar_views.salvar,
        name='s1060_alteracao_cadastrar'),

    url(r'^s1060-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1060_alteracao_salvar_views.salvar,
        name='s1060_alteracao_salvar_output'),

    url(r'^s1060-alteracao/(?P<output>[\w-]+)/$',
        s1060_alteracao_listar_views.listar,
        name='s1060_alteracao_output'),

    url(r'^s1060-alteracao-novavalidade/apagar/(?P<pk>[0-9]+)/$',
        s1060_alteracao_novavalidade_apagar_views.apagar,
        name='s1060_alteracao_novavalidade_apagar'),

    url(r'^s1060-alteracao-novavalidade/api/$',
        s1060_alteracao_novavalidade_api_views.s1060alteracaonovaValidadeList.as_view() ),

    url(r'^s1060-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
        s1060_alteracao_novavalidade_api_views.s1060alteracaonovaValidadeDetail.as_view() ),

    url(r'^s1060-alteracao-novavalidade/$',
        s1060_alteracao_novavalidade_listar_views.listar,
        name='s1060_alteracao_novavalidade'),

    url(r'^s1060-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/$',
        s1060_alteracao_novavalidade_salvar_views.salvar,
        name='s1060_alteracao_novavalidade_salvar'),

    url(r'^s1060-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1060_alteracao_novavalidade_salvar_views.salvar,
        name='s1060_alteracao_novavalidade_salvar_tab'),

    url(r'^s1060-alteracao-novavalidade/cadastrar/$',
        s1060_alteracao_novavalidade_salvar_views.salvar,
        name='s1060_alteracao_novavalidade_cadastrar'),

    url(r'^s1060-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1060_alteracao_novavalidade_salvar_views.salvar,
        name='s1060_alteracao_novavalidade_salvar_output'),

    url(r'^s1060-alteracao-novavalidade/(?P<output>[\w-]+)/$',
        s1060_alteracao_novavalidade_listar_views.listar,
        name='s1060_alteracao_novavalidade_output'),

    url(r'^s1060-exclusao/apagar/(?P<pk>[0-9]+)/$',
        s1060_exclusao_apagar_views.apagar,
        name='s1060_exclusao_apagar'),

    url(r'^s1060-exclusao/api/$',
        s1060_exclusao_api_views.s1060exclusaoList.as_view() ),

    url(r'^s1060-exclusao/api/(?P<pk>[0-9]+)/$',
        s1060_exclusao_api_views.s1060exclusaoDetail.as_view() ),

    url(r'^s1060-exclusao/$',
        s1060_exclusao_listar_views.listar,
        name='s1060_exclusao'),

    url(r'^s1060-exclusao/salvar/(?P<pk>[0-9]+)/$',
        s1060_exclusao_salvar_views.salvar,
        name='s1060_exclusao_salvar'),

    url(r'^s1060-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1060_exclusao_salvar_views.salvar,
        name='s1060_exclusao_salvar_tab'),

    url(r'^s1060-exclusao/cadastrar/$',
        s1060_exclusao_salvar_views.salvar,
        name='s1060_exclusao_cadastrar'),

    url(r'^s1060-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1060_exclusao_salvar_views.salvar,
        name='s1060_exclusao_salvar_output'),

    url(r'^s1060-exclusao/(?P<output>[\w-]+)/$',
        s1060_exclusao_listar_views.listar,
        name='s1060_exclusao_output'),


]