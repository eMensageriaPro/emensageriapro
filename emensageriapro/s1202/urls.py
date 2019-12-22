# eMensageriaAI #
#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1202.views import s1202_procjudtrab_apagar as s1202_procjudtrab_apagar_views
from emensageriapro.s1202.views import s1202_procjudtrab_listar as s1202_procjudtrab_listar_views
from emensageriapro.s1202.views import s1202_procjudtrab_salvar as s1202_procjudtrab_salvar_views
from emensageriapro.s1202.views import s1202_procjudtrab_api as s1202_procjudtrab_api_views
from emensageriapro.s1202.views import s1202_dmdev_apagar as s1202_dmdev_apagar_views
from emensageriapro.s1202.views import s1202_dmdev_listar as s1202_dmdev_listar_views
from emensageriapro.s1202.views import s1202_dmdev_salvar as s1202_dmdev_salvar_views
from emensageriapro.s1202.views import s1202_dmdev_api as s1202_dmdev_api_views
from emensageriapro.s1202.views import s1202_infoperapur_apagar as s1202_infoperapur_apagar_views
from emensageriapro.s1202.views import s1202_infoperapur_listar as s1202_infoperapur_listar_views
from emensageriapro.s1202.views import s1202_infoperapur_salvar as s1202_infoperapur_salvar_views
from emensageriapro.s1202.views import s1202_infoperapur_api as s1202_infoperapur_api_views
from emensageriapro.s1202.views import s1202_infoperapur_ideestab_apagar as s1202_infoperapur_ideestab_apagar_views
from emensageriapro.s1202.views import s1202_infoperapur_ideestab_listar as s1202_infoperapur_ideestab_listar_views
from emensageriapro.s1202.views import s1202_infoperapur_ideestab_salvar as s1202_infoperapur_ideestab_salvar_views
from emensageriapro.s1202.views import s1202_infoperapur_ideestab_api as s1202_infoperapur_ideestab_api_views
from emensageriapro.s1202.views import s1202_infoperapur_remunperapur_apagar as s1202_infoperapur_remunperapur_apagar_views
from emensageriapro.s1202.views import s1202_infoperapur_remunperapur_listar as s1202_infoperapur_remunperapur_listar_views
from emensageriapro.s1202.views import s1202_infoperapur_remunperapur_salvar as s1202_infoperapur_remunperapur_salvar_views
from emensageriapro.s1202.views import s1202_infoperapur_remunperapur_api as s1202_infoperapur_remunperapur_api_views
from emensageriapro.s1202.views import s1202_infoperapur_itensremun_apagar as s1202_infoperapur_itensremun_apagar_views
from emensageriapro.s1202.views import s1202_infoperapur_itensremun_listar as s1202_infoperapur_itensremun_listar_views
from emensageriapro.s1202.views import s1202_infoperapur_itensremun_salvar as s1202_infoperapur_itensremun_salvar_views
from emensageriapro.s1202.views import s1202_infoperapur_itensremun_api as s1202_infoperapur_itensremun_api_views
from emensageriapro.s1202.views import s1202_infoperapur_infosaudecolet_apagar as s1202_infoperapur_infosaudecolet_apagar_views
from emensageriapro.s1202.views import s1202_infoperapur_infosaudecolet_listar as s1202_infoperapur_infosaudecolet_listar_views
from emensageriapro.s1202.views import s1202_infoperapur_infosaudecolet_salvar as s1202_infoperapur_infosaudecolet_salvar_views
from emensageriapro.s1202.views import s1202_infoperapur_infosaudecolet_api as s1202_infoperapur_infosaudecolet_api_views
from emensageriapro.s1202.views import s1202_infoperapur_detoper_apagar as s1202_infoperapur_detoper_apagar_views
from emensageriapro.s1202.views import s1202_infoperapur_detoper_listar as s1202_infoperapur_detoper_listar_views
from emensageriapro.s1202.views import s1202_infoperapur_detoper_salvar as s1202_infoperapur_detoper_salvar_views
from emensageriapro.s1202.views import s1202_infoperapur_detoper_api as s1202_infoperapur_detoper_api_views
from emensageriapro.s1202.views import s1202_infoperapur_detplano_apagar as s1202_infoperapur_detplano_apagar_views
from emensageriapro.s1202.views import s1202_infoperapur_detplano_listar as s1202_infoperapur_detplano_listar_views
from emensageriapro.s1202.views import s1202_infoperapur_detplano_salvar as s1202_infoperapur_detplano_salvar_views
from emensageriapro.s1202.views import s1202_infoperapur_detplano_api as s1202_infoperapur_detplano_api_views
from emensageriapro.s1202.views import s1202_infoperant_apagar as s1202_infoperant_apagar_views
from emensageriapro.s1202.views import s1202_infoperant_listar as s1202_infoperant_listar_views
from emensageriapro.s1202.views import s1202_infoperant_salvar as s1202_infoperant_salvar_views
from emensageriapro.s1202.views import s1202_infoperant_api as s1202_infoperant_api_views
from emensageriapro.s1202.views import s1202_infoperant_ideadc_apagar as s1202_infoperant_ideadc_apagar_views
from emensageriapro.s1202.views import s1202_infoperant_ideadc_listar as s1202_infoperant_ideadc_listar_views
from emensageriapro.s1202.views import s1202_infoperant_ideadc_salvar as s1202_infoperant_ideadc_salvar_views
from emensageriapro.s1202.views import s1202_infoperant_ideadc_api as s1202_infoperant_ideadc_api_views
from emensageriapro.s1202.views import s1202_infoperant_ideperiodo_apagar as s1202_infoperant_ideperiodo_apagar_views
from emensageriapro.s1202.views import s1202_infoperant_ideperiodo_listar as s1202_infoperant_ideperiodo_listar_views
from emensageriapro.s1202.views import s1202_infoperant_ideperiodo_salvar as s1202_infoperant_ideperiodo_salvar_views
from emensageriapro.s1202.views import s1202_infoperant_ideperiodo_api as s1202_infoperant_ideperiodo_api_views
from emensageriapro.s1202.views import s1202_infoperant_ideestab_apagar as s1202_infoperant_ideestab_apagar_views
from emensageriapro.s1202.views import s1202_infoperant_ideestab_listar as s1202_infoperant_ideestab_listar_views
from emensageriapro.s1202.views import s1202_infoperant_ideestab_salvar as s1202_infoperant_ideestab_salvar_views
from emensageriapro.s1202.views import s1202_infoperant_ideestab_api as s1202_infoperant_ideestab_api_views
from emensageriapro.s1202.views import s1202_infoperant_remunperant_apagar as s1202_infoperant_remunperant_apagar_views
from emensageriapro.s1202.views import s1202_infoperant_remunperant_listar as s1202_infoperant_remunperant_listar_views
from emensageriapro.s1202.views import s1202_infoperant_remunperant_salvar as s1202_infoperant_remunperant_salvar_views
from emensageriapro.s1202.views import s1202_infoperant_remunperant_api as s1202_infoperant_remunperant_api_views
from emensageriapro.s1202.views import s1202_infoperant_itensremun_apagar as s1202_infoperant_itensremun_apagar_views
from emensageriapro.s1202.views import s1202_infoperant_itensremun_listar as s1202_infoperant_itensremun_listar_views
from emensageriapro.s1202.views import s1202_infoperant_itensremun_salvar as s1202_infoperant_itensremun_salvar_views
from emensageriapro.s1202.views import s1202_infoperant_itensremun_api as s1202_infoperant_itensremun_api_views


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


    url(r'^s1202-procjudtrab/apagar/(?P<pk>[0-9]+)/$',
        s1202_procjudtrab_apagar_views.apagar,
        name='s1202_procjudtrab_apagar'),

    url(r'^s1202-procjudtrab/api/$',
        s1202_procjudtrab_api_views.s1202procJudTrabList.as_view() ),

    url(r'^s1202-procjudtrab/api/(?P<pk>[0-9]+)/$',
        s1202_procjudtrab_api_views.s1202procJudTrabDetail.as_view() ),

    url(r'^s1202-procjudtrab/$',
        s1202_procjudtrab_listar_views.listar,
        name='s1202_procjudtrab'),

    url(r'^s1202-procjudtrab/salvar/(?P<pk>[0-9]+)/$',
        s1202_procjudtrab_salvar_views.salvar,
        name='s1202_procjudtrab_salvar'),

    url(r'^s1202-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_procjudtrab_salvar_views.salvar,
        name='s1202_procjudtrab_salvar_tab'),

    url(r'^s1202-procjudtrab/cadastrar/$',
        s1202_procjudtrab_salvar_views.salvar,
        name='s1202_procjudtrab_cadastrar'),

    url(r'^s1202-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_procjudtrab_salvar_views.salvar,
        name='s1202_procjudtrab_salvar_output'),

    url(r'^s1202-procjudtrab/(?P<output>[\w-]+)/$',
        s1202_procjudtrab_listar_views.listar,
        name='s1202_procjudtrab_output'),

    url(r'^s1202-dmdev/apagar/(?P<pk>[0-9]+)/$',
        s1202_dmdev_apagar_views.apagar,
        name='s1202_dmdev_apagar'),

    url(r'^s1202-dmdev/api/$',
        s1202_dmdev_api_views.s1202dmDevList.as_view() ),

    url(r'^s1202-dmdev/api/(?P<pk>[0-9]+)/$',
        s1202_dmdev_api_views.s1202dmDevDetail.as_view() ),

    url(r'^s1202-dmdev/$',
        s1202_dmdev_listar_views.listar,
        name='s1202_dmdev'),

    url(r'^s1202-dmdev/salvar/(?P<pk>[0-9]+)/$',
        s1202_dmdev_salvar_views.salvar,
        name='s1202_dmdev_salvar'),

    url(r'^s1202-dmdev/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_dmdev_salvar_views.salvar,
        name='s1202_dmdev_salvar_tab'),

    url(r'^s1202-dmdev/cadastrar/$',
        s1202_dmdev_salvar_views.salvar,
        name='s1202_dmdev_cadastrar'),

    url(r'^s1202-dmdev/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_dmdev_salvar_views.salvar,
        name='s1202_dmdev_salvar_output'),

    url(r'^s1202-dmdev/(?P<output>[\w-]+)/$',
        s1202_dmdev_listar_views.listar,
        name='s1202_dmdev_output'),

    url(r'^s1202-infoperapur/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_apagar_views.apagar,
        name='s1202_infoperapur_apagar'),

    url(r'^s1202-infoperapur/api/$',
        s1202_infoperapur_api_views.s1202infoPerApurList.as_view() ),

    url(r'^s1202-infoperapur/api/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_api_views.s1202infoPerApurDetail.as_view() ),

    url(r'^s1202-infoperapur/$',
        s1202_infoperapur_listar_views.listar,
        name='s1202_infoperapur'),

    url(r'^s1202-infoperapur/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_salvar_views.salvar,
        name='s1202_infoperapur_salvar'),

    url(r'^s1202-infoperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperapur_salvar_views.salvar,
        name='s1202_infoperapur_salvar_tab'),

    url(r'^s1202-infoperapur/cadastrar/$',
        s1202_infoperapur_salvar_views.salvar,
        name='s1202_infoperapur_cadastrar'),

    url(r'^s1202-infoperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperapur_salvar_views.salvar,
        name='s1202_infoperapur_salvar_output'),

    url(r'^s1202-infoperapur/(?P<output>[\w-]+)/$',
        s1202_infoperapur_listar_views.listar,
        name='s1202_infoperapur_output'),

    url(r'^s1202-infoperapur-ideestab/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_ideestab_apagar_views.apagar,
        name='s1202_infoperapur_ideestab_apagar'),

    url(r'^s1202-infoperapur-ideestab/api/$',
        s1202_infoperapur_ideestab_api_views.s1202infoPerApurideEstabList.as_view() ),

    url(r'^s1202-infoperapur-ideestab/api/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_ideestab_api_views.s1202infoPerApurideEstabDetail.as_view() ),

    url(r'^s1202-infoperapur-ideestab/$',
        s1202_infoperapur_ideestab_listar_views.listar,
        name='s1202_infoperapur_ideestab'),

    url(r'^s1202-infoperapur-ideestab/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_ideestab_salvar_views.salvar,
        name='s1202_infoperapur_ideestab_salvar'),

    url(r'^s1202-infoperapur-ideestab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperapur_ideestab_salvar_views.salvar,
        name='s1202_infoperapur_ideestab_salvar_tab'),

    url(r'^s1202-infoperapur-ideestab/cadastrar/$',
        s1202_infoperapur_ideestab_salvar_views.salvar,
        name='s1202_infoperapur_ideestab_cadastrar'),

    url(r'^s1202-infoperapur-ideestab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperapur_ideestab_salvar_views.salvar,
        name='s1202_infoperapur_ideestab_salvar_output'),

    url(r'^s1202-infoperapur-ideestab/(?P<output>[\w-]+)/$',
        s1202_infoperapur_ideestab_listar_views.listar,
        name='s1202_infoperapur_ideestab_output'),

    url(r'^s1202-infoperapur-remunperapur/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_remunperapur_apagar_views.apagar,
        name='s1202_infoperapur_remunperapur_apagar'),

    url(r'^s1202-infoperapur-remunperapur/api/$',
        s1202_infoperapur_remunperapur_api_views.s1202infoPerApurremunPerApurList.as_view() ),

    url(r'^s1202-infoperapur-remunperapur/api/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_remunperapur_api_views.s1202infoPerApurremunPerApurDetail.as_view() ),

    url(r'^s1202-infoperapur-remunperapur/$',
        s1202_infoperapur_remunperapur_listar_views.listar,
        name='s1202_infoperapur_remunperapur'),

    url(r'^s1202-infoperapur-remunperapur/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_remunperapur_salvar_views.salvar,
        name='s1202_infoperapur_remunperapur_salvar'),

    url(r'^s1202-infoperapur-remunperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperapur_remunperapur_salvar_views.salvar,
        name='s1202_infoperapur_remunperapur_salvar_tab'),

    url(r'^s1202-infoperapur-remunperapur/cadastrar/$',
        s1202_infoperapur_remunperapur_salvar_views.salvar,
        name='s1202_infoperapur_remunperapur_cadastrar'),

    url(r'^s1202-infoperapur-remunperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperapur_remunperapur_salvar_views.salvar,
        name='s1202_infoperapur_remunperapur_salvar_output'),

    url(r'^s1202-infoperapur-remunperapur/(?P<output>[\w-]+)/$',
        s1202_infoperapur_remunperapur_listar_views.listar,
        name='s1202_infoperapur_remunperapur_output'),

    url(r'^s1202-infoperapur-itensremun/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_itensremun_apagar_views.apagar,
        name='s1202_infoperapur_itensremun_apagar'),

    url(r'^s1202-infoperapur-itensremun/api/$',
        s1202_infoperapur_itensremun_api_views.s1202infoPerApuritensRemunList.as_view() ),

    url(r'^s1202-infoperapur-itensremun/api/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_itensremun_api_views.s1202infoPerApuritensRemunDetail.as_view() ),

    url(r'^s1202-infoperapur-itensremun/$',
        s1202_infoperapur_itensremun_listar_views.listar,
        name='s1202_infoperapur_itensremun'),

    url(r'^s1202-infoperapur-itensremun/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_itensremun_salvar_views.salvar,
        name='s1202_infoperapur_itensremun_salvar'),

    url(r'^s1202-infoperapur-itensremun/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperapur_itensremun_salvar_views.salvar,
        name='s1202_infoperapur_itensremun_salvar_tab'),

    url(r'^s1202-infoperapur-itensremun/cadastrar/$',
        s1202_infoperapur_itensremun_salvar_views.salvar,
        name='s1202_infoperapur_itensremun_cadastrar'),

    url(r'^s1202-infoperapur-itensremun/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperapur_itensremun_salvar_views.salvar,
        name='s1202_infoperapur_itensremun_salvar_output'),

    url(r'^s1202-infoperapur-itensremun/(?P<output>[\w-]+)/$',
        s1202_infoperapur_itensremun_listar_views.listar,
        name='s1202_infoperapur_itensremun_output'),

    url(r'^s1202-infoperapur-infosaudecolet/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_infosaudecolet_apagar_views.apagar,
        name='s1202_infoperapur_infosaudecolet_apagar'),

    url(r'^s1202-infoperapur-infosaudecolet/api/$',
        s1202_infoperapur_infosaudecolet_api_views.s1202infoPerApurinfoSaudeColetList.as_view() ),

    url(r'^s1202-infoperapur-infosaudecolet/api/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_infosaudecolet_api_views.s1202infoPerApurinfoSaudeColetDetail.as_view() ),

    url(r'^s1202-infoperapur-infosaudecolet/$',
        s1202_infoperapur_infosaudecolet_listar_views.listar,
        name='s1202_infoperapur_infosaudecolet'),

    url(r'^s1202-infoperapur-infosaudecolet/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s1202_infoperapur_infosaudecolet_salvar'),

    url(r'^s1202-infoperapur-infosaudecolet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s1202_infoperapur_infosaudecolet_salvar_tab'),

    url(r'^s1202-infoperapur-infosaudecolet/cadastrar/$',
        s1202_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s1202_infoperapur_infosaudecolet_cadastrar'),

    url(r'^s1202-infoperapur-infosaudecolet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s1202_infoperapur_infosaudecolet_salvar_output'),

    url(r'^s1202-infoperapur-infosaudecolet/(?P<output>[\w-]+)/$',
        s1202_infoperapur_infosaudecolet_listar_views.listar,
        name='s1202_infoperapur_infosaudecolet_output'),

    url(r'^s1202-infoperapur-detoper/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_detoper_apagar_views.apagar,
        name='s1202_infoperapur_detoper_apagar'),

    url(r'^s1202-infoperapur-detoper/api/$',
        s1202_infoperapur_detoper_api_views.s1202infoPerApurdetOperList.as_view() ),

    url(r'^s1202-infoperapur-detoper/api/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_detoper_api_views.s1202infoPerApurdetOperDetail.as_view() ),

    url(r'^s1202-infoperapur-detoper/$',
        s1202_infoperapur_detoper_listar_views.listar,
        name='s1202_infoperapur_detoper'),

    url(r'^s1202-infoperapur-detoper/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_detoper_salvar_views.salvar,
        name='s1202_infoperapur_detoper_salvar'),

    url(r'^s1202-infoperapur-detoper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperapur_detoper_salvar_views.salvar,
        name='s1202_infoperapur_detoper_salvar_tab'),

    url(r'^s1202-infoperapur-detoper/cadastrar/$',
        s1202_infoperapur_detoper_salvar_views.salvar,
        name='s1202_infoperapur_detoper_cadastrar'),

    url(r'^s1202-infoperapur-detoper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperapur_detoper_salvar_views.salvar,
        name='s1202_infoperapur_detoper_salvar_output'),

    url(r'^s1202-infoperapur-detoper/(?P<output>[\w-]+)/$',
        s1202_infoperapur_detoper_listar_views.listar,
        name='s1202_infoperapur_detoper_output'),

    url(r'^s1202-infoperapur-detplano/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_detplano_apagar_views.apagar,
        name='s1202_infoperapur_detplano_apagar'),

    url(r'^s1202-infoperapur-detplano/api/$',
        s1202_infoperapur_detplano_api_views.s1202infoPerApurdetPlanoList.as_view() ),

    url(r'^s1202-infoperapur-detplano/api/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_detplano_api_views.s1202infoPerApurdetPlanoDetail.as_view() ),

    url(r'^s1202-infoperapur-detplano/$',
        s1202_infoperapur_detplano_listar_views.listar,
        name='s1202_infoperapur_detplano'),

    url(r'^s1202-infoperapur-detplano/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperapur_detplano_salvar_views.salvar,
        name='s1202_infoperapur_detplano_salvar'),

    url(r'^s1202-infoperapur-detplano/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperapur_detplano_salvar_views.salvar,
        name='s1202_infoperapur_detplano_salvar_tab'),

    url(r'^s1202-infoperapur-detplano/cadastrar/$',
        s1202_infoperapur_detplano_salvar_views.salvar,
        name='s1202_infoperapur_detplano_cadastrar'),

    url(r'^s1202-infoperapur-detplano/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperapur_detplano_salvar_views.salvar,
        name='s1202_infoperapur_detplano_salvar_output'),

    url(r'^s1202-infoperapur-detplano/(?P<output>[\w-]+)/$',
        s1202_infoperapur_detplano_listar_views.listar,
        name='s1202_infoperapur_detplano_output'),

    url(r'^s1202-infoperant/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_apagar_views.apagar,
        name='s1202_infoperant_apagar'),

    url(r'^s1202-infoperant/api/$',
        s1202_infoperant_api_views.s1202infoPerAntList.as_view() ),

    url(r'^s1202-infoperant/api/(?P<pk>[0-9]+)/$',
        s1202_infoperant_api_views.s1202infoPerAntDetail.as_view() ),

    url(r'^s1202-infoperant/$',
        s1202_infoperant_listar_views.listar,
        name='s1202_infoperant'),

    url(r'^s1202-infoperant/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_salvar_views.salvar,
        name='s1202_infoperant_salvar'),

    url(r'^s1202-infoperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperant_salvar_views.salvar,
        name='s1202_infoperant_salvar_tab'),

    url(r'^s1202-infoperant/cadastrar/$',
        s1202_infoperant_salvar_views.salvar,
        name='s1202_infoperant_cadastrar'),

    url(r'^s1202-infoperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperant_salvar_views.salvar,
        name='s1202_infoperant_salvar_output'),

    url(r'^s1202-infoperant/(?P<output>[\w-]+)/$',
        s1202_infoperant_listar_views.listar,
        name='s1202_infoperant_output'),

    url(r'^s1202-infoperant-ideadc/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_ideadc_apagar_views.apagar,
        name='s1202_infoperant_ideadc_apagar'),

    url(r'^s1202-infoperant-ideadc/api/$',
        s1202_infoperant_ideadc_api_views.s1202infoPerAntideADCList.as_view() ),

    url(r'^s1202-infoperant-ideadc/api/(?P<pk>[0-9]+)/$',
        s1202_infoperant_ideadc_api_views.s1202infoPerAntideADCDetail.as_view() ),

    url(r'^s1202-infoperant-ideadc/$',
        s1202_infoperant_ideadc_listar_views.listar,
        name='s1202_infoperant_ideadc'),

    url(r'^s1202-infoperant-ideadc/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_ideadc_salvar_views.salvar,
        name='s1202_infoperant_ideadc_salvar'),

    url(r'^s1202-infoperant-ideadc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperant_ideadc_salvar_views.salvar,
        name='s1202_infoperant_ideadc_salvar_tab'),

    url(r'^s1202-infoperant-ideadc/cadastrar/$',
        s1202_infoperant_ideadc_salvar_views.salvar,
        name='s1202_infoperant_ideadc_cadastrar'),

    url(r'^s1202-infoperant-ideadc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperant_ideadc_salvar_views.salvar,
        name='s1202_infoperant_ideadc_salvar_output'),

    url(r'^s1202-infoperant-ideadc/(?P<output>[\w-]+)/$',
        s1202_infoperant_ideadc_listar_views.listar,
        name='s1202_infoperant_ideadc_output'),

    url(r'^s1202-infoperant-ideperiodo/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_ideperiodo_apagar_views.apagar,
        name='s1202_infoperant_ideperiodo_apagar'),

    url(r'^s1202-infoperant-ideperiodo/api/$',
        s1202_infoperant_ideperiodo_api_views.s1202infoPerAntidePeriodoList.as_view() ),

    url(r'^s1202-infoperant-ideperiodo/api/(?P<pk>[0-9]+)/$',
        s1202_infoperant_ideperiodo_api_views.s1202infoPerAntidePeriodoDetail.as_view() ),

    url(r'^s1202-infoperant-ideperiodo/$',
        s1202_infoperant_ideperiodo_listar_views.listar,
        name='s1202_infoperant_ideperiodo'),

    url(r'^s1202-infoperant-ideperiodo/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_ideperiodo_salvar_views.salvar,
        name='s1202_infoperant_ideperiodo_salvar'),

    url(r'^s1202-infoperant-ideperiodo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperant_ideperiodo_salvar_views.salvar,
        name='s1202_infoperant_ideperiodo_salvar_tab'),

    url(r'^s1202-infoperant-ideperiodo/cadastrar/$',
        s1202_infoperant_ideperiodo_salvar_views.salvar,
        name='s1202_infoperant_ideperiodo_cadastrar'),

    url(r'^s1202-infoperant-ideperiodo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperant_ideperiodo_salvar_views.salvar,
        name='s1202_infoperant_ideperiodo_salvar_output'),

    url(r'^s1202-infoperant-ideperiodo/(?P<output>[\w-]+)/$',
        s1202_infoperant_ideperiodo_listar_views.listar,
        name='s1202_infoperant_ideperiodo_output'),

    url(r'^s1202-infoperant-ideestab/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_ideestab_apagar_views.apagar,
        name='s1202_infoperant_ideestab_apagar'),

    url(r'^s1202-infoperant-ideestab/api/$',
        s1202_infoperant_ideestab_api_views.s1202infoPerAntideEstabList.as_view() ),

    url(r'^s1202-infoperant-ideestab/api/(?P<pk>[0-9]+)/$',
        s1202_infoperant_ideestab_api_views.s1202infoPerAntideEstabDetail.as_view() ),

    url(r'^s1202-infoperant-ideestab/$',
        s1202_infoperant_ideestab_listar_views.listar,
        name='s1202_infoperant_ideestab'),

    url(r'^s1202-infoperant-ideestab/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_ideestab_salvar_views.salvar,
        name='s1202_infoperant_ideestab_salvar'),

    url(r'^s1202-infoperant-ideestab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperant_ideestab_salvar_views.salvar,
        name='s1202_infoperant_ideestab_salvar_tab'),

    url(r'^s1202-infoperant-ideestab/cadastrar/$',
        s1202_infoperant_ideestab_salvar_views.salvar,
        name='s1202_infoperant_ideestab_cadastrar'),

    url(r'^s1202-infoperant-ideestab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperant_ideestab_salvar_views.salvar,
        name='s1202_infoperant_ideestab_salvar_output'),

    url(r'^s1202-infoperant-ideestab/(?P<output>[\w-]+)/$',
        s1202_infoperant_ideestab_listar_views.listar,
        name='s1202_infoperant_ideestab_output'),

    url(r'^s1202-infoperant-remunperant/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_remunperant_apagar_views.apagar,
        name='s1202_infoperant_remunperant_apagar'),

    url(r'^s1202-infoperant-remunperant/api/$',
        s1202_infoperant_remunperant_api_views.s1202infoPerAntremunPerAntList.as_view() ),

    url(r'^s1202-infoperant-remunperant/api/(?P<pk>[0-9]+)/$',
        s1202_infoperant_remunperant_api_views.s1202infoPerAntremunPerAntDetail.as_view() ),

    url(r'^s1202-infoperant-remunperant/$',
        s1202_infoperant_remunperant_listar_views.listar,
        name='s1202_infoperant_remunperant'),

    url(r'^s1202-infoperant-remunperant/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_remunperant_salvar_views.salvar,
        name='s1202_infoperant_remunperant_salvar'),

    url(r'^s1202-infoperant-remunperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperant_remunperant_salvar_views.salvar,
        name='s1202_infoperant_remunperant_salvar_tab'),

    url(r'^s1202-infoperant-remunperant/cadastrar/$',
        s1202_infoperant_remunperant_salvar_views.salvar,
        name='s1202_infoperant_remunperant_cadastrar'),

    url(r'^s1202-infoperant-remunperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperant_remunperant_salvar_views.salvar,
        name='s1202_infoperant_remunperant_salvar_output'),

    url(r'^s1202-infoperant-remunperant/(?P<output>[\w-]+)/$',
        s1202_infoperant_remunperant_listar_views.listar,
        name='s1202_infoperant_remunperant_output'),

    url(r'^s1202-infoperant-itensremun/apagar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_itensremun_apagar_views.apagar,
        name='s1202_infoperant_itensremun_apagar'),

    url(r'^s1202-infoperant-itensremun/api/$',
        s1202_infoperant_itensremun_api_views.s1202infoPerAntitensRemunList.as_view() ),

    url(r'^s1202-infoperant-itensremun/api/(?P<pk>[0-9]+)/$',
        s1202_infoperant_itensremun_api_views.s1202infoPerAntitensRemunDetail.as_view() ),

    url(r'^s1202-infoperant-itensremun/$',
        s1202_infoperant_itensremun_listar_views.listar,
        name='s1202_infoperant_itensremun'),

    url(r'^s1202-infoperant-itensremun/salvar/(?P<pk>[0-9]+)/$',
        s1202_infoperant_itensremun_salvar_views.salvar,
        name='s1202_infoperant_itensremun_salvar'),

    url(r'^s1202-infoperant-itensremun/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1202_infoperant_itensremun_salvar_views.salvar,
        name='s1202_infoperant_itensremun_salvar_tab'),

    url(r'^s1202-infoperant-itensremun/cadastrar/$',
        s1202_infoperant_itensremun_salvar_views.salvar,
        name='s1202_infoperant_itensremun_cadastrar'),

    url(r'^s1202-infoperant-itensremun/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1202_infoperant_itensremun_salvar_views.salvar,
        name='s1202_infoperant_itensremun_salvar_output'),

    url(r'^s1202-infoperant-itensremun/(?P<output>[\w-]+)/$',
        s1202_infoperant_itensremun_listar_views.listar,
        name='s1202_infoperant_itensremun_output'),


]