# eMensageriaAI #
#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2399.views import s2399_mudancacpf_apagar as s2399_mudancacpf_apagar_views
from emensageriapro.s2399.views import s2399_mudancacpf_listar as s2399_mudancacpf_listar_views
from emensageriapro.s2399.views import s2399_mudancacpf_salvar as s2399_mudancacpf_salvar_views
from emensageriapro.s2399.views import s2399_mudancacpf_api as s2399_mudancacpf_api_views
from emensageriapro.s2399.views import s2399_verbasresc_apagar as s2399_verbasresc_apagar_views
from emensageriapro.s2399.views import s2399_verbasresc_listar as s2399_verbasresc_listar_views
from emensageriapro.s2399.views import s2399_verbasresc_salvar as s2399_verbasresc_salvar_views
from emensageriapro.s2399.views import s2399_verbasresc_api as s2399_verbasresc_api_views
from emensageriapro.s2399.views import s2399_dmdev_apagar as s2399_dmdev_apagar_views
from emensageriapro.s2399.views import s2399_dmdev_listar as s2399_dmdev_listar_views
from emensageriapro.s2399.views import s2399_dmdev_salvar as s2399_dmdev_salvar_views
from emensageriapro.s2399.views import s2399_dmdev_api as s2399_dmdev_api_views
from emensageriapro.s2399.views import s2399_ideestablot_apagar as s2399_ideestablot_apagar_views
from emensageriapro.s2399.views import s2399_ideestablot_listar as s2399_ideestablot_listar_views
from emensageriapro.s2399.views import s2399_ideestablot_salvar as s2399_ideestablot_salvar_views
from emensageriapro.s2399.views import s2399_ideestablot_api as s2399_ideestablot_api_views
from emensageriapro.s2399.views import s2399_detverbas_apagar as s2399_detverbas_apagar_views
from emensageriapro.s2399.views import s2399_detverbas_listar as s2399_detverbas_listar_views
from emensageriapro.s2399.views import s2399_detverbas_salvar as s2399_detverbas_salvar_views
from emensageriapro.s2399.views import s2399_detverbas_api as s2399_detverbas_api_views
from emensageriapro.s2399.views import s2399_infosaudecolet_apagar as s2399_infosaudecolet_apagar_views
from emensageriapro.s2399.views import s2399_infosaudecolet_listar as s2399_infosaudecolet_listar_views
from emensageriapro.s2399.views import s2399_infosaudecolet_salvar as s2399_infosaudecolet_salvar_views
from emensageriapro.s2399.views import s2399_infosaudecolet_api as s2399_infosaudecolet_api_views
from emensageriapro.s2399.views import s2399_detoper_apagar as s2399_detoper_apagar_views
from emensageriapro.s2399.views import s2399_detoper_listar as s2399_detoper_listar_views
from emensageriapro.s2399.views import s2399_detoper_salvar as s2399_detoper_salvar_views
from emensageriapro.s2399.views import s2399_detoper_api as s2399_detoper_api_views
from emensageriapro.s2399.views import s2399_detplano_apagar as s2399_detplano_apagar_views
from emensageriapro.s2399.views import s2399_detplano_listar as s2399_detplano_listar_views
from emensageriapro.s2399.views import s2399_detplano_salvar as s2399_detplano_salvar_views
from emensageriapro.s2399.views import s2399_detplano_api as s2399_detplano_api_views
from emensageriapro.s2399.views import s2399_infoagnocivo_apagar as s2399_infoagnocivo_apagar_views
from emensageriapro.s2399.views import s2399_infoagnocivo_listar as s2399_infoagnocivo_listar_views
from emensageriapro.s2399.views import s2399_infoagnocivo_salvar as s2399_infoagnocivo_salvar_views
from emensageriapro.s2399.views import s2399_infoagnocivo_api as s2399_infoagnocivo_api_views
from emensageriapro.s2399.views import s2399_infosimples_apagar as s2399_infosimples_apagar_views
from emensageriapro.s2399.views import s2399_infosimples_listar as s2399_infosimples_listar_views
from emensageriapro.s2399.views import s2399_infosimples_salvar as s2399_infosimples_salvar_views
from emensageriapro.s2399.views import s2399_infosimples_api as s2399_infosimples_api_views
from emensageriapro.s2399.views import s2399_procjudtrab_apagar as s2399_procjudtrab_apagar_views
from emensageriapro.s2399.views import s2399_procjudtrab_listar as s2399_procjudtrab_listar_views
from emensageriapro.s2399.views import s2399_procjudtrab_salvar as s2399_procjudtrab_salvar_views
from emensageriapro.s2399.views import s2399_procjudtrab_api as s2399_procjudtrab_api_views
from emensageriapro.s2399.views import s2399_infomv_apagar as s2399_infomv_apagar_views
from emensageriapro.s2399.views import s2399_infomv_listar as s2399_infomv_listar_views
from emensageriapro.s2399.views import s2399_infomv_salvar as s2399_infomv_salvar_views
from emensageriapro.s2399.views import s2399_infomv_api as s2399_infomv_api_views
from emensageriapro.s2399.views import s2399_remunoutrempr_apagar as s2399_remunoutrempr_apagar_views
from emensageriapro.s2399.views import s2399_remunoutrempr_listar as s2399_remunoutrempr_listar_views
from emensageriapro.s2399.views import s2399_remunoutrempr_salvar as s2399_remunoutrempr_salvar_views
from emensageriapro.s2399.views import s2399_remunoutrempr_api as s2399_remunoutrempr_api_views
from emensageriapro.s2399.views import s2399_quarentena_apagar as s2399_quarentena_apagar_views
from emensageriapro.s2399.views import s2399_quarentena_listar as s2399_quarentena_listar_views
from emensageriapro.s2399.views import s2399_quarentena_salvar as s2399_quarentena_salvar_views
from emensageriapro.s2399.views import s2399_quarentena_api as s2399_quarentena_api_views


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


    url(r'^s2399-mudancacpf/apagar/(?P<pk>[0-9]+)/$',
        s2399_mudancacpf_apagar_views.apagar,
        name='s2399_mudancacpf_apagar'),

    url(r'^s2399-mudancacpf/api/$',
        s2399_mudancacpf_api_views.s2399mudancaCPFList.as_view() ),

    url(r'^s2399-mudancacpf/api/(?P<pk>[0-9]+)/$',
        s2399_mudancacpf_api_views.s2399mudancaCPFDetail.as_view() ),

    url(r'^s2399-mudancacpf/$',
        s2399_mudancacpf_listar_views.listar,
        name='s2399_mudancacpf'),

    url(r'^s2399-mudancacpf/salvar/(?P<pk>[0-9]+)/$',
        s2399_mudancacpf_salvar_views.salvar,
        name='s2399_mudancacpf_salvar'),

    url(r'^s2399-mudancacpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_mudancacpf_salvar_views.salvar,
        name='s2399_mudancacpf_salvar_tab'),

    url(r'^s2399-mudancacpf/cadastrar/$',
        s2399_mudancacpf_salvar_views.salvar,
        name='s2399_mudancacpf_cadastrar'),

    url(r'^s2399-mudancacpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_mudancacpf_salvar_views.salvar,
        name='s2399_mudancacpf_salvar_output'),

    url(r'^s2399-mudancacpf/(?P<output>[\w-]+)/$',
        s2399_mudancacpf_listar_views.listar,
        name='s2399_mudancacpf_output'),

    url(r'^s2399-verbasresc/apagar/(?P<pk>[0-9]+)/$',
        s2399_verbasresc_apagar_views.apagar,
        name='s2399_verbasresc_apagar'),

    url(r'^s2399-verbasresc/api/$',
        s2399_verbasresc_api_views.s2399verbasRescList.as_view() ),

    url(r'^s2399-verbasresc/api/(?P<pk>[0-9]+)/$',
        s2399_verbasresc_api_views.s2399verbasRescDetail.as_view() ),

    url(r'^s2399-verbasresc/$',
        s2399_verbasresc_listar_views.listar,
        name='s2399_verbasresc'),

    url(r'^s2399-verbasresc/salvar/(?P<pk>[0-9]+)/$',
        s2399_verbasresc_salvar_views.salvar,
        name='s2399_verbasresc_salvar'),

    url(r'^s2399-verbasresc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_verbasresc_salvar_views.salvar,
        name='s2399_verbasresc_salvar_tab'),

    url(r'^s2399-verbasresc/cadastrar/$',
        s2399_verbasresc_salvar_views.salvar,
        name='s2399_verbasresc_cadastrar'),

    url(r'^s2399-verbasresc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_verbasresc_salvar_views.salvar,
        name='s2399_verbasresc_salvar_output'),

    url(r'^s2399-verbasresc/(?P<output>[\w-]+)/$',
        s2399_verbasresc_listar_views.listar,
        name='s2399_verbasresc_output'),

    url(r'^s2399-dmdev/apagar/(?P<pk>[0-9]+)/$',
        s2399_dmdev_apagar_views.apagar,
        name='s2399_dmdev_apagar'),

    url(r'^s2399-dmdev/api/$',
        s2399_dmdev_api_views.s2399dmDevList.as_view() ),

    url(r'^s2399-dmdev/api/(?P<pk>[0-9]+)/$',
        s2399_dmdev_api_views.s2399dmDevDetail.as_view() ),

    url(r'^s2399-dmdev/$',
        s2399_dmdev_listar_views.listar,
        name='s2399_dmdev'),

    url(r'^s2399-dmdev/salvar/(?P<pk>[0-9]+)/$',
        s2399_dmdev_salvar_views.salvar,
        name='s2399_dmdev_salvar'),

    url(r'^s2399-dmdev/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_dmdev_salvar_views.salvar,
        name='s2399_dmdev_salvar_tab'),

    url(r'^s2399-dmdev/cadastrar/$',
        s2399_dmdev_salvar_views.salvar,
        name='s2399_dmdev_cadastrar'),

    url(r'^s2399-dmdev/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_dmdev_salvar_views.salvar,
        name='s2399_dmdev_salvar_output'),

    url(r'^s2399-dmdev/(?P<output>[\w-]+)/$',
        s2399_dmdev_listar_views.listar,
        name='s2399_dmdev_output'),

    url(r'^s2399-ideestablot/apagar/(?P<pk>[0-9]+)/$',
        s2399_ideestablot_apagar_views.apagar,
        name='s2399_ideestablot_apagar'),

    url(r'^s2399-ideestablot/api/$',
        s2399_ideestablot_api_views.s2399ideEstabLotList.as_view() ),

    url(r'^s2399-ideestablot/api/(?P<pk>[0-9]+)/$',
        s2399_ideestablot_api_views.s2399ideEstabLotDetail.as_view() ),

    url(r'^s2399-ideestablot/$',
        s2399_ideestablot_listar_views.listar,
        name='s2399_ideestablot'),

    url(r'^s2399-ideestablot/salvar/(?P<pk>[0-9]+)/$',
        s2399_ideestablot_salvar_views.salvar,
        name='s2399_ideestablot_salvar'),

    url(r'^s2399-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_ideestablot_salvar_views.salvar,
        name='s2399_ideestablot_salvar_tab'),

    url(r'^s2399-ideestablot/cadastrar/$',
        s2399_ideestablot_salvar_views.salvar,
        name='s2399_ideestablot_cadastrar'),

    url(r'^s2399-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_ideestablot_salvar_views.salvar,
        name='s2399_ideestablot_salvar_output'),

    url(r'^s2399-ideestablot/(?P<output>[\w-]+)/$',
        s2399_ideestablot_listar_views.listar,
        name='s2399_ideestablot_output'),

    url(r'^s2399-detverbas/apagar/(?P<pk>[0-9]+)/$',
        s2399_detverbas_apagar_views.apagar,
        name='s2399_detverbas_apagar'),

    url(r'^s2399-detverbas/api/$',
        s2399_detverbas_api_views.s2399detVerbasList.as_view() ),

    url(r'^s2399-detverbas/api/(?P<pk>[0-9]+)/$',
        s2399_detverbas_api_views.s2399detVerbasDetail.as_view() ),

    url(r'^s2399-detverbas/$',
        s2399_detverbas_listar_views.listar,
        name='s2399_detverbas'),

    url(r'^s2399-detverbas/salvar/(?P<pk>[0-9]+)/$',
        s2399_detverbas_salvar_views.salvar,
        name='s2399_detverbas_salvar'),

    url(r'^s2399-detverbas/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_detverbas_salvar_views.salvar,
        name='s2399_detverbas_salvar_tab'),

    url(r'^s2399-detverbas/cadastrar/$',
        s2399_detverbas_salvar_views.salvar,
        name='s2399_detverbas_cadastrar'),

    url(r'^s2399-detverbas/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_detverbas_salvar_views.salvar,
        name='s2399_detverbas_salvar_output'),

    url(r'^s2399-detverbas/(?P<output>[\w-]+)/$',
        s2399_detverbas_listar_views.listar,
        name='s2399_detverbas_output'),

    url(r'^s2399-infosaudecolet/apagar/(?P<pk>[0-9]+)/$',
        s2399_infosaudecolet_apagar_views.apagar,
        name='s2399_infosaudecolet_apagar'),

    url(r'^s2399-infosaudecolet/api/$',
        s2399_infosaudecolet_api_views.s2399infoSaudeColetList.as_view() ),

    url(r'^s2399-infosaudecolet/api/(?P<pk>[0-9]+)/$',
        s2399_infosaudecolet_api_views.s2399infoSaudeColetDetail.as_view() ),

    url(r'^s2399-infosaudecolet/$',
        s2399_infosaudecolet_listar_views.listar,
        name='s2399_infosaudecolet'),

    url(r'^s2399-infosaudecolet/salvar/(?P<pk>[0-9]+)/$',
        s2399_infosaudecolet_salvar_views.salvar,
        name='s2399_infosaudecolet_salvar'),

    url(r'^s2399-infosaudecolet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_infosaudecolet_salvar_views.salvar,
        name='s2399_infosaudecolet_salvar_tab'),

    url(r'^s2399-infosaudecolet/cadastrar/$',
        s2399_infosaudecolet_salvar_views.salvar,
        name='s2399_infosaudecolet_cadastrar'),

    url(r'^s2399-infosaudecolet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_infosaudecolet_salvar_views.salvar,
        name='s2399_infosaudecolet_salvar_output'),

    url(r'^s2399-infosaudecolet/(?P<output>[\w-]+)/$',
        s2399_infosaudecolet_listar_views.listar,
        name='s2399_infosaudecolet_output'),

    url(r'^s2399-detoper/apagar/(?P<pk>[0-9]+)/$',
        s2399_detoper_apagar_views.apagar,
        name='s2399_detoper_apagar'),

    url(r'^s2399-detoper/api/$',
        s2399_detoper_api_views.s2399detOperList.as_view() ),

    url(r'^s2399-detoper/api/(?P<pk>[0-9]+)/$',
        s2399_detoper_api_views.s2399detOperDetail.as_view() ),

    url(r'^s2399-detoper/$',
        s2399_detoper_listar_views.listar,
        name='s2399_detoper'),

    url(r'^s2399-detoper/salvar/(?P<pk>[0-9]+)/$',
        s2399_detoper_salvar_views.salvar,
        name='s2399_detoper_salvar'),

    url(r'^s2399-detoper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_detoper_salvar_views.salvar,
        name='s2399_detoper_salvar_tab'),

    url(r'^s2399-detoper/cadastrar/$',
        s2399_detoper_salvar_views.salvar,
        name='s2399_detoper_cadastrar'),

    url(r'^s2399-detoper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_detoper_salvar_views.salvar,
        name='s2399_detoper_salvar_output'),

    url(r'^s2399-detoper/(?P<output>[\w-]+)/$',
        s2399_detoper_listar_views.listar,
        name='s2399_detoper_output'),

    url(r'^s2399-detplano/apagar/(?P<pk>[0-9]+)/$',
        s2399_detplano_apagar_views.apagar,
        name='s2399_detplano_apagar'),

    url(r'^s2399-detplano/api/$',
        s2399_detplano_api_views.s2399detPlanoList.as_view() ),

    url(r'^s2399-detplano/api/(?P<pk>[0-9]+)/$',
        s2399_detplano_api_views.s2399detPlanoDetail.as_view() ),

    url(r'^s2399-detplano/$',
        s2399_detplano_listar_views.listar,
        name='s2399_detplano'),

    url(r'^s2399-detplano/salvar/(?P<pk>[0-9]+)/$',
        s2399_detplano_salvar_views.salvar,
        name='s2399_detplano_salvar'),

    url(r'^s2399-detplano/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_detplano_salvar_views.salvar,
        name='s2399_detplano_salvar_tab'),

    url(r'^s2399-detplano/cadastrar/$',
        s2399_detplano_salvar_views.salvar,
        name='s2399_detplano_cadastrar'),

    url(r'^s2399-detplano/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_detplano_salvar_views.salvar,
        name='s2399_detplano_salvar_output'),

    url(r'^s2399-detplano/(?P<output>[\w-]+)/$',
        s2399_detplano_listar_views.listar,
        name='s2399_detplano_output'),

    url(r'^s2399-infoagnocivo/apagar/(?P<pk>[0-9]+)/$',
        s2399_infoagnocivo_apagar_views.apagar,
        name='s2399_infoagnocivo_apagar'),

    url(r'^s2399-infoagnocivo/api/$',
        s2399_infoagnocivo_api_views.s2399infoAgNocivoList.as_view() ),

    url(r'^s2399-infoagnocivo/api/(?P<pk>[0-9]+)/$',
        s2399_infoagnocivo_api_views.s2399infoAgNocivoDetail.as_view() ),

    url(r'^s2399-infoagnocivo/$',
        s2399_infoagnocivo_listar_views.listar,
        name='s2399_infoagnocivo'),

    url(r'^s2399-infoagnocivo/salvar/(?P<pk>[0-9]+)/$',
        s2399_infoagnocivo_salvar_views.salvar,
        name='s2399_infoagnocivo_salvar'),

    url(r'^s2399-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_infoagnocivo_salvar_views.salvar,
        name='s2399_infoagnocivo_salvar_tab'),

    url(r'^s2399-infoagnocivo/cadastrar/$',
        s2399_infoagnocivo_salvar_views.salvar,
        name='s2399_infoagnocivo_cadastrar'),

    url(r'^s2399-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_infoagnocivo_salvar_views.salvar,
        name='s2399_infoagnocivo_salvar_output'),

    url(r'^s2399-infoagnocivo/(?P<output>[\w-]+)/$',
        s2399_infoagnocivo_listar_views.listar,
        name='s2399_infoagnocivo_output'),

    url(r'^s2399-infosimples/apagar/(?P<pk>[0-9]+)/$',
        s2399_infosimples_apagar_views.apagar,
        name='s2399_infosimples_apagar'),

    url(r'^s2399-infosimples/api/$',
        s2399_infosimples_api_views.s2399infoSimplesList.as_view() ),

    url(r'^s2399-infosimples/api/(?P<pk>[0-9]+)/$',
        s2399_infosimples_api_views.s2399infoSimplesDetail.as_view() ),

    url(r'^s2399-infosimples/$',
        s2399_infosimples_listar_views.listar,
        name='s2399_infosimples'),

    url(r'^s2399-infosimples/salvar/(?P<pk>[0-9]+)/$',
        s2399_infosimples_salvar_views.salvar,
        name='s2399_infosimples_salvar'),

    url(r'^s2399-infosimples/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_infosimples_salvar_views.salvar,
        name='s2399_infosimples_salvar_tab'),

    url(r'^s2399-infosimples/cadastrar/$',
        s2399_infosimples_salvar_views.salvar,
        name='s2399_infosimples_cadastrar'),

    url(r'^s2399-infosimples/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_infosimples_salvar_views.salvar,
        name='s2399_infosimples_salvar_output'),

    url(r'^s2399-infosimples/(?P<output>[\w-]+)/$',
        s2399_infosimples_listar_views.listar,
        name='s2399_infosimples_output'),

    url(r'^s2399-procjudtrab/apagar/(?P<pk>[0-9]+)/$',
        s2399_procjudtrab_apagar_views.apagar,
        name='s2399_procjudtrab_apagar'),

    url(r'^s2399-procjudtrab/api/$',
        s2399_procjudtrab_api_views.s2399procJudTrabList.as_view() ),

    url(r'^s2399-procjudtrab/api/(?P<pk>[0-9]+)/$',
        s2399_procjudtrab_api_views.s2399procJudTrabDetail.as_view() ),

    url(r'^s2399-procjudtrab/$',
        s2399_procjudtrab_listar_views.listar,
        name='s2399_procjudtrab'),

    url(r'^s2399-procjudtrab/salvar/(?P<pk>[0-9]+)/$',
        s2399_procjudtrab_salvar_views.salvar,
        name='s2399_procjudtrab_salvar'),

    url(r'^s2399-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_procjudtrab_salvar_views.salvar,
        name='s2399_procjudtrab_salvar_tab'),

    url(r'^s2399-procjudtrab/cadastrar/$',
        s2399_procjudtrab_salvar_views.salvar,
        name='s2399_procjudtrab_cadastrar'),

    url(r'^s2399-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_procjudtrab_salvar_views.salvar,
        name='s2399_procjudtrab_salvar_output'),

    url(r'^s2399-procjudtrab/(?P<output>[\w-]+)/$',
        s2399_procjudtrab_listar_views.listar,
        name='s2399_procjudtrab_output'),

    url(r'^s2399-infomv/apagar/(?P<pk>[0-9]+)/$',
        s2399_infomv_apagar_views.apagar,
        name='s2399_infomv_apagar'),

    url(r'^s2399-infomv/api/$',
        s2399_infomv_api_views.s2399infoMVList.as_view() ),

    url(r'^s2399-infomv/api/(?P<pk>[0-9]+)/$',
        s2399_infomv_api_views.s2399infoMVDetail.as_view() ),

    url(r'^s2399-infomv/$',
        s2399_infomv_listar_views.listar,
        name='s2399_infomv'),

    url(r'^s2399-infomv/salvar/(?P<pk>[0-9]+)/$',
        s2399_infomv_salvar_views.salvar,
        name='s2399_infomv_salvar'),

    url(r'^s2399-infomv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_infomv_salvar_views.salvar,
        name='s2399_infomv_salvar_tab'),

    url(r'^s2399-infomv/cadastrar/$',
        s2399_infomv_salvar_views.salvar,
        name='s2399_infomv_cadastrar'),

    url(r'^s2399-infomv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_infomv_salvar_views.salvar,
        name='s2399_infomv_salvar_output'),

    url(r'^s2399-infomv/(?P<output>[\w-]+)/$',
        s2399_infomv_listar_views.listar,
        name='s2399_infomv_output'),

    url(r'^s2399-remunoutrempr/apagar/(?P<pk>[0-9]+)/$',
        s2399_remunoutrempr_apagar_views.apagar,
        name='s2399_remunoutrempr_apagar'),

    url(r'^s2399-remunoutrempr/api/$',
        s2399_remunoutrempr_api_views.s2399remunOutrEmprList.as_view() ),

    url(r'^s2399-remunoutrempr/api/(?P<pk>[0-9]+)/$',
        s2399_remunoutrempr_api_views.s2399remunOutrEmprDetail.as_view() ),

    url(r'^s2399-remunoutrempr/$',
        s2399_remunoutrempr_listar_views.listar,
        name='s2399_remunoutrempr'),

    url(r'^s2399-remunoutrempr/salvar/(?P<pk>[0-9]+)/$',
        s2399_remunoutrempr_salvar_views.salvar,
        name='s2399_remunoutrempr_salvar'),

    url(r'^s2399-remunoutrempr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_remunoutrempr_salvar_views.salvar,
        name='s2399_remunoutrempr_salvar_tab'),

    url(r'^s2399-remunoutrempr/cadastrar/$',
        s2399_remunoutrempr_salvar_views.salvar,
        name='s2399_remunoutrempr_cadastrar'),

    url(r'^s2399-remunoutrempr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_remunoutrempr_salvar_views.salvar,
        name='s2399_remunoutrempr_salvar_output'),

    url(r'^s2399-remunoutrempr/(?P<output>[\w-]+)/$',
        s2399_remunoutrempr_listar_views.listar,
        name='s2399_remunoutrempr_output'),

    url(r'^s2399-quarentena/apagar/(?P<pk>[0-9]+)/$',
        s2399_quarentena_apagar_views.apagar,
        name='s2399_quarentena_apagar'),

    url(r'^s2399-quarentena/api/$',
        s2399_quarentena_api_views.s2399quarentenaList.as_view() ),

    url(r'^s2399-quarentena/api/(?P<pk>[0-9]+)/$',
        s2399_quarentena_api_views.s2399quarentenaDetail.as_view() ),

    url(r'^s2399-quarentena/$',
        s2399_quarentena_listar_views.listar,
        name='s2399_quarentena'),

    url(r'^s2399-quarentena/salvar/(?P<pk>[0-9]+)/$',
        s2399_quarentena_salvar_views.salvar,
        name='s2399_quarentena_salvar'),

    url(r'^s2399-quarentena/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2399_quarentena_salvar_views.salvar,
        name='s2399_quarentena_salvar_tab'),

    url(r'^s2399-quarentena/cadastrar/$',
        s2399_quarentena_salvar_views.salvar,
        name='s2399_quarentena_cadastrar'),

    url(r'^s2399-quarentena/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2399_quarentena_salvar_views.salvar,
        name='s2399_quarentena_salvar_output'),

    url(r'^s2399-quarentena/(?P<output>[\w-]+)/$',
        s2399_quarentena_listar_views.listar,
        name='s2399_quarentena_output'),


]