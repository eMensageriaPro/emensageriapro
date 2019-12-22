# eMensageriaAI #
#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2210.views import s2210_idelocalacid_apagar as s2210_idelocalacid_apagar_views
from emensageriapro.s2210.views import s2210_idelocalacid_listar as s2210_idelocalacid_listar_views
from emensageriapro.s2210.views import s2210_idelocalacid_salvar as s2210_idelocalacid_salvar_views
from emensageriapro.s2210.views import s2210_idelocalacid_api as s2210_idelocalacid_api_views
from emensageriapro.s2210.views import s2210_parteatingida_apagar as s2210_parteatingida_apagar_views
from emensageriapro.s2210.views import s2210_parteatingida_listar as s2210_parteatingida_listar_views
from emensageriapro.s2210.views import s2210_parteatingida_salvar as s2210_parteatingida_salvar_views
from emensageriapro.s2210.views import s2210_parteatingida_api as s2210_parteatingida_api_views
from emensageriapro.s2210.views import s2210_agentecausador_apagar as s2210_agentecausador_apagar_views
from emensageriapro.s2210.views import s2210_agentecausador_listar as s2210_agentecausador_listar_views
from emensageriapro.s2210.views import s2210_agentecausador_salvar as s2210_agentecausador_salvar_views
from emensageriapro.s2210.views import s2210_agentecausador_api as s2210_agentecausador_api_views
from emensageriapro.s2210.views import s2210_atestado_apagar as s2210_atestado_apagar_views
from emensageriapro.s2210.views import s2210_atestado_listar as s2210_atestado_listar_views
from emensageriapro.s2210.views import s2210_atestado_salvar as s2210_atestado_salvar_views
from emensageriapro.s2210.views import s2210_atestado_api as s2210_atestado_api_views
from emensageriapro.s2210.views import s2210_catorigem_apagar as s2210_catorigem_apagar_views
from emensageriapro.s2210.views import s2210_catorigem_listar as s2210_catorigem_listar_views
from emensageriapro.s2210.views import s2210_catorigem_salvar as s2210_catorigem_salvar_views
from emensageriapro.s2210.views import s2210_catorigem_api as s2210_catorigem_api_views


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


    url(r'^s2210-idelocalacid/apagar/(?P<pk>[0-9]+)/$',
        s2210_idelocalacid_apagar_views.apagar,
        name='s2210_idelocalacid_apagar'),

    url(r'^s2210-idelocalacid/api/$',
        s2210_idelocalacid_api_views.s2210ideLocalAcidList.as_view() ),

    url(r'^s2210-idelocalacid/api/(?P<pk>[0-9]+)/$',
        s2210_idelocalacid_api_views.s2210ideLocalAcidDetail.as_view() ),

    url(r'^s2210-idelocalacid/$',
        s2210_idelocalacid_listar_views.listar,
        name='s2210_idelocalacid'),

    url(r'^s2210-idelocalacid/salvar/(?P<pk>[0-9]+)/$',
        s2210_idelocalacid_salvar_views.salvar,
        name='s2210_idelocalacid_salvar'),

    url(r'^s2210-idelocalacid/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2210_idelocalacid_salvar_views.salvar,
        name='s2210_idelocalacid_salvar_tab'),

    url(r'^s2210-idelocalacid/cadastrar/$',
        s2210_idelocalacid_salvar_views.salvar,
        name='s2210_idelocalacid_cadastrar'),

    url(r'^s2210-idelocalacid/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2210_idelocalacid_salvar_views.salvar,
        name='s2210_idelocalacid_salvar_output'),

    url(r'^s2210-idelocalacid/(?P<output>[\w-]+)/$',
        s2210_idelocalacid_listar_views.listar,
        name='s2210_idelocalacid_output'),

    url(r'^s2210-parteatingida/apagar/(?P<pk>[0-9]+)/$',
        s2210_parteatingida_apagar_views.apagar,
        name='s2210_parteatingida_apagar'),

    url(r'^s2210-parteatingida/api/$',
        s2210_parteatingida_api_views.s2210parteAtingidaList.as_view() ),

    url(r'^s2210-parteatingida/api/(?P<pk>[0-9]+)/$',
        s2210_parteatingida_api_views.s2210parteAtingidaDetail.as_view() ),

    url(r'^s2210-parteatingida/$',
        s2210_parteatingida_listar_views.listar,
        name='s2210_parteatingida'),

    url(r'^s2210-parteatingida/salvar/(?P<pk>[0-9]+)/$',
        s2210_parteatingida_salvar_views.salvar,
        name='s2210_parteatingida_salvar'),

    url(r'^s2210-parteatingida/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2210_parteatingida_salvar_views.salvar,
        name='s2210_parteatingida_salvar_tab'),

    url(r'^s2210-parteatingida/cadastrar/$',
        s2210_parteatingida_salvar_views.salvar,
        name='s2210_parteatingida_cadastrar'),

    url(r'^s2210-parteatingida/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2210_parteatingida_salvar_views.salvar,
        name='s2210_parteatingida_salvar_output'),

    url(r'^s2210-parteatingida/(?P<output>[\w-]+)/$',
        s2210_parteatingida_listar_views.listar,
        name='s2210_parteatingida_output'),

    url(r'^s2210-agentecausador/apagar/(?P<pk>[0-9]+)/$',
        s2210_agentecausador_apagar_views.apagar,
        name='s2210_agentecausador_apagar'),

    url(r'^s2210-agentecausador/api/$',
        s2210_agentecausador_api_views.s2210agenteCausadorList.as_view() ),

    url(r'^s2210-agentecausador/api/(?P<pk>[0-9]+)/$',
        s2210_agentecausador_api_views.s2210agenteCausadorDetail.as_view() ),

    url(r'^s2210-agentecausador/$',
        s2210_agentecausador_listar_views.listar,
        name='s2210_agentecausador'),

    url(r'^s2210-agentecausador/salvar/(?P<pk>[0-9]+)/$',
        s2210_agentecausador_salvar_views.salvar,
        name='s2210_agentecausador_salvar'),

    url(r'^s2210-agentecausador/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2210_agentecausador_salvar_views.salvar,
        name='s2210_agentecausador_salvar_tab'),

    url(r'^s2210-agentecausador/cadastrar/$',
        s2210_agentecausador_salvar_views.salvar,
        name='s2210_agentecausador_cadastrar'),

    url(r'^s2210-agentecausador/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2210_agentecausador_salvar_views.salvar,
        name='s2210_agentecausador_salvar_output'),

    url(r'^s2210-agentecausador/(?P<output>[\w-]+)/$',
        s2210_agentecausador_listar_views.listar,
        name='s2210_agentecausador_output'),

    url(r'^s2210-atestado/apagar/(?P<pk>[0-9]+)/$',
        s2210_atestado_apagar_views.apagar,
        name='s2210_atestado_apagar'),

    url(r'^s2210-atestado/api/$',
        s2210_atestado_api_views.s2210atestadoList.as_view() ),

    url(r'^s2210-atestado/api/(?P<pk>[0-9]+)/$',
        s2210_atestado_api_views.s2210atestadoDetail.as_view() ),

    url(r'^s2210-atestado/$',
        s2210_atestado_listar_views.listar,
        name='s2210_atestado'),

    url(r'^s2210-atestado/salvar/(?P<pk>[0-9]+)/$',
        s2210_atestado_salvar_views.salvar,
        name='s2210_atestado_salvar'),

    url(r'^s2210-atestado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2210_atestado_salvar_views.salvar,
        name='s2210_atestado_salvar_tab'),

    url(r'^s2210-atestado/cadastrar/$',
        s2210_atestado_salvar_views.salvar,
        name='s2210_atestado_cadastrar'),

    url(r'^s2210-atestado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2210_atestado_salvar_views.salvar,
        name='s2210_atestado_salvar_output'),

    url(r'^s2210-atestado/(?P<output>[\w-]+)/$',
        s2210_atestado_listar_views.listar,
        name='s2210_atestado_output'),

    url(r'^s2210-catorigem/apagar/(?P<pk>[0-9]+)/$',
        s2210_catorigem_apagar_views.apagar,
        name='s2210_catorigem_apagar'),

    url(r'^s2210-catorigem/api/$',
        s2210_catorigem_api_views.s2210catOrigemList.as_view() ),

    url(r'^s2210-catorigem/api/(?P<pk>[0-9]+)/$',
        s2210_catorigem_api_views.s2210catOrigemDetail.as_view() ),

    url(r'^s2210-catorigem/$',
        s2210_catorigem_listar_views.listar,
        name='s2210_catorigem'),

    url(r'^s2210-catorigem/salvar/(?P<pk>[0-9]+)/$',
        s2210_catorigem_salvar_views.salvar,
        name='s2210_catorigem_salvar'),

    url(r'^s2210-catorigem/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2210_catorigem_salvar_views.salvar,
        name='s2210_catorigem_salvar_tab'),

    url(r'^s2210-catorigem/cadastrar/$',
        s2210_catorigem_salvar_views.salvar,
        name='s2210_catorigem_cadastrar'),

    url(r'^s2210-catorigem/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2210_catorigem_salvar_views.salvar,
        name='s2210_catorigem_salvar_output'),

    url(r'^s2210-catorigem/(?P<output>[\w-]+)/$',
        s2210_catorigem_listar_views.listar,
        name='s2210_catorigem_output'),


]