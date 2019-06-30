#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1070.views import s1070_inclusao_apagar as s1070_inclusao_apagar_views
from emensageriapro.s1070.views import s1070_inclusao_listar as s1070_inclusao_listar_views
from emensageriapro.s1070.views import s1070_inclusao_salvar as s1070_inclusao_salvar_views
from emensageriapro.s1070.views import s1070_inclusao_api as s1070_inclusao_api_views
from emensageriapro.s1070.views import s1070_inclusao_dadosprocjud_apagar as s1070_inclusao_dadosprocjud_apagar_views
from emensageriapro.s1070.views import s1070_inclusao_dadosprocjud_listar as s1070_inclusao_dadosprocjud_listar_views
from emensageriapro.s1070.views import s1070_inclusao_dadosprocjud_salvar as s1070_inclusao_dadosprocjud_salvar_views
from emensageriapro.s1070.views import s1070_inclusao_dadosprocjud_api as s1070_inclusao_dadosprocjud_api_views
from emensageriapro.s1070.views import s1070_inclusao_infosusp_apagar as s1070_inclusao_infosusp_apagar_views
from emensageriapro.s1070.views import s1070_inclusao_infosusp_listar as s1070_inclusao_infosusp_listar_views
from emensageriapro.s1070.views import s1070_inclusao_infosusp_salvar as s1070_inclusao_infosusp_salvar_views
from emensageriapro.s1070.views import s1070_inclusao_infosusp_api as s1070_inclusao_infosusp_api_views
from emensageriapro.s1070.views import s1070_alteracao_apagar as s1070_alteracao_apagar_views
from emensageriapro.s1070.views import s1070_alteracao_listar as s1070_alteracao_listar_views
from emensageriapro.s1070.views import s1070_alteracao_salvar as s1070_alteracao_salvar_views
from emensageriapro.s1070.views import s1070_alteracao_api as s1070_alteracao_api_views
from emensageriapro.s1070.views import s1070_alteracao_dadosprocjud_apagar as s1070_alteracao_dadosprocjud_apagar_views
from emensageriapro.s1070.views import s1070_alteracao_dadosprocjud_listar as s1070_alteracao_dadosprocjud_listar_views
from emensageriapro.s1070.views import s1070_alteracao_dadosprocjud_salvar as s1070_alteracao_dadosprocjud_salvar_views
from emensageriapro.s1070.views import s1070_alteracao_dadosprocjud_api as s1070_alteracao_dadosprocjud_api_views
from emensageriapro.s1070.views import s1070_alteracao_infosusp_apagar as s1070_alteracao_infosusp_apagar_views
from emensageriapro.s1070.views import s1070_alteracao_infosusp_listar as s1070_alteracao_infosusp_listar_views
from emensageriapro.s1070.views import s1070_alteracao_infosusp_salvar as s1070_alteracao_infosusp_salvar_views
from emensageriapro.s1070.views import s1070_alteracao_infosusp_api as s1070_alteracao_infosusp_api_views
from emensageriapro.s1070.views import s1070_alteracao_novavalidade_apagar as s1070_alteracao_novavalidade_apagar_views
from emensageriapro.s1070.views import s1070_alteracao_novavalidade_listar as s1070_alteracao_novavalidade_listar_views
from emensageriapro.s1070.views import s1070_alteracao_novavalidade_salvar as s1070_alteracao_novavalidade_salvar_views
from emensageriapro.s1070.views import s1070_alteracao_novavalidade_api as s1070_alteracao_novavalidade_api_views
from emensageriapro.s1070.views import s1070_exclusao_apagar as s1070_exclusao_apagar_views
from emensageriapro.s1070.views import s1070_exclusao_listar as s1070_exclusao_listar_views
from emensageriapro.s1070.views import s1070_exclusao_salvar as s1070_exclusao_salvar_views
from emensageriapro.s1070.views import s1070_exclusao_api as s1070_exclusao_api_views



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


    url(r'^s1070-inclusao/apagar/(?P<pk>[0-9]+)/$',
        s1070_inclusao_apagar_views.apagar,
        name='s1070_inclusao_apagar'),

    url(r'^s1070-inclusao/api/$',
        s1070_inclusao_api_views.s1070inclusaoList.as_view() ),

    url(r'^s1070-inclusao/api/(?P<pk>[0-9]+)/$',
        s1070_inclusao_api_views.s1070inclusaoDetail.as_view() ),

    url(r'^s1070-inclusao/$',
        s1070_inclusao_listar_views.listar,
        name='s1070_inclusao'),

    url(r'^s1070-inclusao/salvar/(?P<pk>[0-9]+)/$',
        s1070_inclusao_salvar_views.salvar,
        name='s1070_inclusao_salvar'),

    url(r'^s1070-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1070_inclusao_salvar_views.salvar,
        name='s1070_inclusao_salvar_tab'),

    url(r'^s1070-inclusao/cadastrar/$',
        s1070_inclusao_salvar_views.salvar,
        name='s1070_inclusao_cadastrar'),

    url(r'^s1070-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1070_inclusao_salvar_views.salvar,
        name='s1070_inclusao_salvar_output'),

    url(r'^s1070-inclusao/(?P<output>[\w-]+)/$',
        s1070_inclusao_listar_views.listar,
        name='s1070_inclusao_output'),

    url(r'^s1070-inclusao-dadosprocjud/apagar/(?P<pk>[0-9]+)/$',
        s1070_inclusao_dadosprocjud_apagar_views.apagar,
        name='s1070_inclusao_dadosprocjud_apagar'),

    url(r'^s1070-inclusao-dadosprocjud/api/$',
        s1070_inclusao_dadosprocjud_api_views.s1070inclusaodadosProcJudList.as_view() ),

    url(r'^s1070-inclusao-dadosprocjud/api/(?P<pk>[0-9]+)/$',
        s1070_inclusao_dadosprocjud_api_views.s1070inclusaodadosProcJudDetail.as_view() ),

    url(r'^s1070-inclusao-dadosprocjud/$',
        s1070_inclusao_dadosprocjud_listar_views.listar,
        name='s1070_inclusao_dadosprocjud'),

    url(r'^s1070-inclusao-dadosprocjud/salvar/(?P<pk>[0-9]+)/$',
        s1070_inclusao_dadosprocjud_salvar_views.salvar,
        name='s1070_inclusao_dadosprocjud_salvar'),

    url(r'^s1070-inclusao-dadosprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1070_inclusao_dadosprocjud_salvar_views.salvar,
        name='s1070_inclusao_dadosprocjud_salvar_tab'),

    url(r'^s1070-inclusao-dadosprocjud/cadastrar/$',
        s1070_inclusao_dadosprocjud_salvar_views.salvar,
        name='s1070_inclusao_dadosprocjud_cadastrar'),

    url(r'^s1070-inclusao-dadosprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1070_inclusao_dadosprocjud_salvar_views.salvar,
        name='s1070_inclusao_dadosprocjud_salvar_output'),

    url(r'^s1070-inclusao-dadosprocjud/(?P<output>[\w-]+)/$',
        s1070_inclusao_dadosprocjud_listar_views.listar,
        name='s1070_inclusao_dadosprocjud_output'),

    url(r'^s1070-inclusao-infosusp/apagar/(?P<pk>[0-9]+)/$',
        s1070_inclusao_infosusp_apagar_views.apagar,
        name='s1070_inclusao_infosusp_apagar'),

    url(r'^s1070-inclusao-infosusp/api/$',
        s1070_inclusao_infosusp_api_views.s1070inclusaoinfoSuspList.as_view() ),

    url(r'^s1070-inclusao-infosusp/api/(?P<pk>[0-9]+)/$',
        s1070_inclusao_infosusp_api_views.s1070inclusaoinfoSuspDetail.as_view() ),

    url(r'^s1070-inclusao-infosusp/$',
        s1070_inclusao_infosusp_listar_views.listar,
        name='s1070_inclusao_infosusp'),

    url(r'^s1070-inclusao-infosusp/salvar/(?P<pk>[0-9]+)/$',
        s1070_inclusao_infosusp_salvar_views.salvar,
        name='s1070_inclusao_infosusp_salvar'),

    url(r'^s1070-inclusao-infosusp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1070_inclusao_infosusp_salvar_views.salvar,
        name='s1070_inclusao_infosusp_salvar_tab'),

    url(r'^s1070-inclusao-infosusp/cadastrar/$',
        s1070_inclusao_infosusp_salvar_views.salvar,
        name='s1070_inclusao_infosusp_cadastrar'),

    url(r'^s1070-inclusao-infosusp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1070_inclusao_infosusp_salvar_views.salvar,
        name='s1070_inclusao_infosusp_salvar_output'),

    url(r'^s1070-inclusao-infosusp/(?P<output>[\w-]+)/$',
        s1070_inclusao_infosusp_listar_views.listar,
        name='s1070_inclusao_infosusp_output'),

    url(r'^s1070-alteracao/apagar/(?P<pk>[0-9]+)/$',
        s1070_alteracao_apagar_views.apagar,
        name='s1070_alteracao_apagar'),

    url(r'^s1070-alteracao/api/$',
        s1070_alteracao_api_views.s1070alteracaoList.as_view() ),

    url(r'^s1070-alteracao/api/(?P<pk>[0-9]+)/$',
        s1070_alteracao_api_views.s1070alteracaoDetail.as_view() ),

    url(r'^s1070-alteracao/$',
        s1070_alteracao_listar_views.listar,
        name='s1070_alteracao'),

    url(r'^s1070-alteracao/salvar/(?P<pk>[0-9]+)/$',
        s1070_alteracao_salvar_views.salvar,
        name='s1070_alteracao_salvar'),

    url(r'^s1070-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1070_alteracao_salvar_views.salvar,
        name='s1070_alteracao_salvar_tab'),

    url(r'^s1070-alteracao/cadastrar/$',
        s1070_alteracao_salvar_views.salvar,
        name='s1070_alteracao_cadastrar'),

    url(r'^s1070-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1070_alteracao_salvar_views.salvar,
        name='s1070_alteracao_salvar_output'),

    url(r'^s1070-alteracao/(?P<output>[\w-]+)/$',
        s1070_alteracao_listar_views.listar,
        name='s1070_alteracao_output'),

    url(r'^s1070-alteracao-dadosprocjud/apagar/(?P<pk>[0-9]+)/$',
        s1070_alteracao_dadosprocjud_apagar_views.apagar,
        name='s1070_alteracao_dadosprocjud_apagar'),

    url(r'^s1070-alteracao-dadosprocjud/api/$',
        s1070_alteracao_dadosprocjud_api_views.s1070alteracaodadosProcJudList.as_view() ),

    url(r'^s1070-alteracao-dadosprocjud/api/(?P<pk>[0-9]+)/$',
        s1070_alteracao_dadosprocjud_api_views.s1070alteracaodadosProcJudDetail.as_view() ),

    url(r'^s1070-alteracao-dadosprocjud/$',
        s1070_alteracao_dadosprocjud_listar_views.listar,
        name='s1070_alteracao_dadosprocjud'),

    url(r'^s1070-alteracao-dadosprocjud/salvar/(?P<pk>[0-9]+)/$',
        s1070_alteracao_dadosprocjud_salvar_views.salvar,
        name='s1070_alteracao_dadosprocjud_salvar'),

    url(r'^s1070-alteracao-dadosprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1070_alteracao_dadosprocjud_salvar_views.salvar,
        name='s1070_alteracao_dadosprocjud_salvar_tab'),

    url(r'^s1070-alteracao-dadosprocjud/cadastrar/$',
        s1070_alteracao_dadosprocjud_salvar_views.salvar,
        name='s1070_alteracao_dadosprocjud_cadastrar'),

    url(r'^s1070-alteracao-dadosprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1070_alteracao_dadosprocjud_salvar_views.salvar,
        name='s1070_alteracao_dadosprocjud_salvar_output'),

    url(r'^s1070-alteracao-dadosprocjud/(?P<output>[\w-]+)/$',
        s1070_alteracao_dadosprocjud_listar_views.listar,
        name='s1070_alteracao_dadosprocjud_output'),

    url(r'^s1070-alteracao-infosusp/apagar/(?P<pk>[0-9]+)/$',
        s1070_alteracao_infosusp_apagar_views.apagar,
        name='s1070_alteracao_infosusp_apagar'),

    url(r'^s1070-alteracao-infosusp/api/$',
        s1070_alteracao_infosusp_api_views.s1070alteracaoinfoSuspList.as_view() ),

    url(r'^s1070-alteracao-infosusp/api/(?P<pk>[0-9]+)/$',
        s1070_alteracao_infosusp_api_views.s1070alteracaoinfoSuspDetail.as_view() ),

    url(r'^s1070-alteracao-infosusp/$',
        s1070_alteracao_infosusp_listar_views.listar,
        name='s1070_alteracao_infosusp'),

    url(r'^s1070-alteracao-infosusp/salvar/(?P<pk>[0-9]+)/$',
        s1070_alteracao_infosusp_salvar_views.salvar,
        name='s1070_alteracao_infosusp_salvar'),

    url(r'^s1070-alteracao-infosusp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1070_alteracao_infosusp_salvar_views.salvar,
        name='s1070_alteracao_infosusp_salvar_tab'),

    url(r'^s1070-alteracao-infosusp/cadastrar/$',
        s1070_alteracao_infosusp_salvar_views.salvar,
        name='s1070_alteracao_infosusp_cadastrar'),

    url(r'^s1070-alteracao-infosusp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1070_alteracao_infosusp_salvar_views.salvar,
        name='s1070_alteracao_infosusp_salvar_output'),

    url(r'^s1070-alteracao-infosusp/(?P<output>[\w-]+)/$',
        s1070_alteracao_infosusp_listar_views.listar,
        name='s1070_alteracao_infosusp_output'),

    url(r'^s1070-alteracao-novavalidade/apagar/(?P<pk>[0-9]+)/$',
        s1070_alteracao_novavalidade_apagar_views.apagar,
        name='s1070_alteracao_novavalidade_apagar'),

    url(r'^s1070-alteracao-novavalidade/api/$',
        s1070_alteracao_novavalidade_api_views.s1070alteracaonovaValidadeList.as_view() ),

    url(r'^s1070-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
        s1070_alteracao_novavalidade_api_views.s1070alteracaonovaValidadeDetail.as_view() ),

    url(r'^s1070-alteracao-novavalidade/$',
        s1070_alteracao_novavalidade_listar_views.listar,
        name='s1070_alteracao_novavalidade'),

    url(r'^s1070-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/$',
        s1070_alteracao_novavalidade_salvar_views.salvar,
        name='s1070_alteracao_novavalidade_salvar'),

    url(r'^s1070-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1070_alteracao_novavalidade_salvar_views.salvar,
        name='s1070_alteracao_novavalidade_salvar_tab'),

    url(r'^s1070-alteracao-novavalidade/cadastrar/$',
        s1070_alteracao_novavalidade_salvar_views.salvar,
        name='s1070_alteracao_novavalidade_cadastrar'),

    url(r'^s1070-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1070_alteracao_novavalidade_salvar_views.salvar,
        name='s1070_alteracao_novavalidade_salvar_output'),

    url(r'^s1070-alteracao-novavalidade/(?P<output>[\w-]+)/$',
        s1070_alteracao_novavalidade_listar_views.listar,
        name='s1070_alteracao_novavalidade_output'),

    url(r'^s1070-exclusao/apagar/(?P<pk>[0-9]+)/$',
        s1070_exclusao_apagar_views.apagar,
        name='s1070_exclusao_apagar'),

    url(r'^s1070-exclusao/api/$',
        s1070_exclusao_api_views.s1070exclusaoList.as_view() ),

    url(r'^s1070-exclusao/api/(?P<pk>[0-9]+)/$',
        s1070_exclusao_api_views.s1070exclusaoDetail.as_view() ),

    url(r'^s1070-exclusao/$',
        s1070_exclusao_listar_views.listar,
        name='s1070_exclusao'),

    url(r'^s1070-exclusao/salvar/(?P<pk>[0-9]+)/$',
        s1070_exclusao_salvar_views.salvar,
        name='s1070_exclusao_salvar'),

    url(r'^s1070-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1070_exclusao_salvar_views.salvar,
        name='s1070_exclusao_salvar_tab'),

    url(r'^s1070-exclusao/cadastrar/$',
        s1070_exclusao_salvar_views.salvar,
        name='s1070_exclusao_cadastrar'),

    url(r'^s1070-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1070_exclusao_salvar_views.salvar,
        name='s1070_exclusao_salvar_output'),

    url(r'^s1070-exclusao/(?P<output>[\w-]+)/$',
        s1070_exclusao_listar_views.listar,
        name='s1070_exclusao_output'),


]