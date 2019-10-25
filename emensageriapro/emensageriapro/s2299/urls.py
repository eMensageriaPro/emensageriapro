#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2299.views import s2299_observacoes_apagar as s2299_observacoes_apagar_views
from emensageriapro.s2299.views import s2299_observacoes_listar as s2299_observacoes_listar_views
from emensageriapro.s2299.views import s2299_observacoes_salvar as s2299_observacoes_salvar_views
from emensageriapro.s2299.views import s2299_observacoes_api as s2299_observacoes_api_views
from emensageriapro.s2299.views import s2299_sucessaovinc_apagar as s2299_sucessaovinc_apagar_views
from emensageriapro.s2299.views import s2299_sucessaovinc_listar as s2299_sucessaovinc_listar_views
from emensageriapro.s2299.views import s2299_sucessaovinc_salvar as s2299_sucessaovinc_salvar_views
from emensageriapro.s2299.views import s2299_sucessaovinc_api as s2299_sucessaovinc_api_views
from emensageriapro.s2299.views import s2299_transftit_apagar as s2299_transftit_apagar_views
from emensageriapro.s2299.views import s2299_transftit_listar as s2299_transftit_listar_views
from emensageriapro.s2299.views import s2299_transftit_salvar as s2299_transftit_salvar_views
from emensageriapro.s2299.views import s2299_transftit_api as s2299_transftit_api_views
from emensageriapro.s2299.views import s2299_mudancacpf_apagar as s2299_mudancacpf_apagar_views
from emensageriapro.s2299.views import s2299_mudancacpf_listar as s2299_mudancacpf_listar_views
from emensageriapro.s2299.views import s2299_mudancacpf_salvar as s2299_mudancacpf_salvar_views
from emensageriapro.s2299.views import s2299_mudancacpf_api as s2299_mudancacpf_api_views
from emensageriapro.s2299.views import s2299_verbasresc_apagar as s2299_verbasresc_apagar_views
from emensageriapro.s2299.views import s2299_verbasresc_listar as s2299_verbasresc_listar_views
from emensageriapro.s2299.views import s2299_verbasresc_salvar as s2299_verbasresc_salvar_views
from emensageriapro.s2299.views import s2299_verbasresc_api as s2299_verbasresc_api_views
from emensageriapro.s2299.views import s2299_dmdev_apagar as s2299_dmdev_apagar_views
from emensageriapro.s2299.views import s2299_dmdev_listar as s2299_dmdev_listar_views
from emensageriapro.s2299.views import s2299_dmdev_salvar as s2299_dmdev_salvar_views
from emensageriapro.s2299.views import s2299_dmdev_api as s2299_dmdev_api_views
from emensageriapro.s2299.views import s2299_infoperapur_apagar as s2299_infoperapur_apagar_views
from emensageriapro.s2299.views import s2299_infoperapur_listar as s2299_infoperapur_listar_views
from emensageriapro.s2299.views import s2299_infoperapur_salvar as s2299_infoperapur_salvar_views
from emensageriapro.s2299.views import s2299_infoperapur_api as s2299_infoperapur_api_views
from emensageriapro.s2299.views import s2299_infoperapur_ideestablot_apagar as s2299_infoperapur_ideestablot_apagar_views
from emensageriapro.s2299.views import s2299_infoperapur_ideestablot_listar as s2299_infoperapur_ideestablot_listar_views
from emensageriapro.s2299.views import s2299_infoperapur_ideestablot_salvar as s2299_infoperapur_ideestablot_salvar_views
from emensageriapro.s2299.views import s2299_infoperapur_ideestablot_api as s2299_infoperapur_ideestablot_api_views
from emensageriapro.s2299.views import s2299_infoperapur_detverbas_apagar as s2299_infoperapur_detverbas_apagar_views
from emensageriapro.s2299.views import s2299_infoperapur_detverbas_listar as s2299_infoperapur_detverbas_listar_views
from emensageriapro.s2299.views import s2299_infoperapur_detverbas_salvar as s2299_infoperapur_detverbas_salvar_views
from emensageriapro.s2299.views import s2299_infoperapur_detverbas_api as s2299_infoperapur_detverbas_api_views
from emensageriapro.s2299.views import s2299_infoperapur_infosaudecolet_apagar as s2299_infoperapur_infosaudecolet_apagar_views
from emensageriapro.s2299.views import s2299_infoperapur_infosaudecolet_listar as s2299_infoperapur_infosaudecolet_listar_views
from emensageriapro.s2299.views import s2299_infoperapur_infosaudecolet_salvar as s2299_infoperapur_infosaudecolet_salvar_views
from emensageriapro.s2299.views import s2299_infoperapur_infosaudecolet_api as s2299_infoperapur_infosaudecolet_api_views
from emensageriapro.s2299.views import s2299_infoperapur_detoper_apagar as s2299_infoperapur_detoper_apagar_views
from emensageriapro.s2299.views import s2299_infoperapur_detoper_listar as s2299_infoperapur_detoper_listar_views
from emensageriapro.s2299.views import s2299_infoperapur_detoper_salvar as s2299_infoperapur_detoper_salvar_views
from emensageriapro.s2299.views import s2299_infoperapur_detoper_api as s2299_infoperapur_detoper_api_views
from emensageriapro.s2299.views import s2299_infoperapur_detplano_apagar as s2299_infoperapur_detplano_apagar_views
from emensageriapro.s2299.views import s2299_infoperapur_detplano_listar as s2299_infoperapur_detplano_listar_views
from emensageriapro.s2299.views import s2299_infoperapur_detplano_salvar as s2299_infoperapur_detplano_salvar_views
from emensageriapro.s2299.views import s2299_infoperapur_detplano_api as s2299_infoperapur_detplano_api_views
from emensageriapro.s2299.views import s2299_infoperapur_infoagnocivo_apagar as s2299_infoperapur_infoagnocivo_apagar_views
from emensageriapro.s2299.views import s2299_infoperapur_infoagnocivo_listar as s2299_infoperapur_infoagnocivo_listar_views
from emensageriapro.s2299.views import s2299_infoperapur_infoagnocivo_salvar as s2299_infoperapur_infoagnocivo_salvar_views
from emensageriapro.s2299.views import s2299_infoperapur_infoagnocivo_api as s2299_infoperapur_infoagnocivo_api_views
from emensageriapro.s2299.views import s2299_infoperapur_infosimples_apagar as s2299_infoperapur_infosimples_apagar_views
from emensageriapro.s2299.views import s2299_infoperapur_infosimples_listar as s2299_infoperapur_infosimples_listar_views
from emensageriapro.s2299.views import s2299_infoperapur_infosimples_salvar as s2299_infoperapur_infosimples_salvar_views
from emensageriapro.s2299.views import s2299_infoperapur_infosimples_api as s2299_infoperapur_infosimples_api_views
from emensageriapro.s2299.views import s2299_infoperant_apagar as s2299_infoperant_apagar_views
from emensageriapro.s2299.views import s2299_infoperant_listar as s2299_infoperant_listar_views
from emensageriapro.s2299.views import s2299_infoperant_salvar as s2299_infoperant_salvar_views
from emensageriapro.s2299.views import s2299_infoperant_api as s2299_infoperant_api_views
from emensageriapro.s2299.views import s2299_infoperant_ideadc_apagar as s2299_infoperant_ideadc_apagar_views
from emensageriapro.s2299.views import s2299_infoperant_ideadc_listar as s2299_infoperant_ideadc_listar_views
from emensageriapro.s2299.views import s2299_infoperant_ideadc_salvar as s2299_infoperant_ideadc_salvar_views
from emensageriapro.s2299.views import s2299_infoperant_ideadc_api as s2299_infoperant_ideadc_api_views
from emensageriapro.s2299.views import s2299_infoperant_ideperiodo_apagar as s2299_infoperant_ideperiodo_apagar_views
from emensageriapro.s2299.views import s2299_infoperant_ideperiodo_listar as s2299_infoperant_ideperiodo_listar_views
from emensageriapro.s2299.views import s2299_infoperant_ideperiodo_salvar as s2299_infoperant_ideperiodo_salvar_views
from emensageriapro.s2299.views import s2299_infoperant_ideperiodo_api as s2299_infoperant_ideperiodo_api_views
from emensageriapro.s2299.views import s2299_infoperant_ideestablot_apagar as s2299_infoperant_ideestablot_apagar_views
from emensageriapro.s2299.views import s2299_infoperant_ideestablot_listar as s2299_infoperant_ideestablot_listar_views
from emensageriapro.s2299.views import s2299_infoperant_ideestablot_salvar as s2299_infoperant_ideestablot_salvar_views
from emensageriapro.s2299.views import s2299_infoperant_ideestablot_api as s2299_infoperant_ideestablot_api_views
from emensageriapro.s2299.views import s2299_infoperant_detverbas_apagar as s2299_infoperant_detverbas_apagar_views
from emensageriapro.s2299.views import s2299_infoperant_detverbas_listar as s2299_infoperant_detverbas_listar_views
from emensageriapro.s2299.views import s2299_infoperant_detverbas_salvar as s2299_infoperant_detverbas_salvar_views
from emensageriapro.s2299.views import s2299_infoperant_detverbas_api as s2299_infoperant_detverbas_api_views
from emensageriapro.s2299.views import s2299_infoperant_infoagnocivo_apagar as s2299_infoperant_infoagnocivo_apagar_views
from emensageriapro.s2299.views import s2299_infoperant_infoagnocivo_listar as s2299_infoperant_infoagnocivo_listar_views
from emensageriapro.s2299.views import s2299_infoperant_infoagnocivo_salvar as s2299_infoperant_infoagnocivo_salvar_views
from emensageriapro.s2299.views import s2299_infoperant_infoagnocivo_api as s2299_infoperant_infoagnocivo_api_views
from emensageriapro.s2299.views import s2299_infoperant_infosimples_apagar as s2299_infoperant_infosimples_apagar_views
from emensageriapro.s2299.views import s2299_infoperant_infosimples_listar as s2299_infoperant_infosimples_listar_views
from emensageriapro.s2299.views import s2299_infoperant_infosimples_salvar as s2299_infoperant_infosimples_salvar_views
from emensageriapro.s2299.views import s2299_infoperant_infosimples_api as s2299_infoperant_infosimples_api_views
from emensageriapro.s2299.views import s2299_infotrabinterm_apagar as s2299_infotrabinterm_apagar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_listar as s2299_infotrabinterm_listar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_salvar as s2299_infotrabinterm_salvar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_api as s2299_infotrabinterm_api_views
from emensageriapro.s2299.views import s2299_infotrabinterm_procjudtrab_apagar as s2299_infotrabinterm_procjudtrab_apagar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_procjudtrab_listar as s2299_infotrabinterm_procjudtrab_listar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_procjudtrab_salvar as s2299_infotrabinterm_procjudtrab_salvar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_procjudtrab_api as s2299_infotrabinterm_procjudtrab_api_views
from emensageriapro.s2299.views import s2299_infotrabinterm_infomv_apagar as s2299_infotrabinterm_infomv_apagar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_infomv_listar as s2299_infotrabinterm_infomv_listar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_infomv_salvar as s2299_infotrabinterm_infomv_salvar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_infomv_api as s2299_infotrabinterm_infomv_api_views
from emensageriapro.s2299.views import s2299_infotrabinterm_remunoutrempr_apagar as s2299_infotrabinterm_remunoutrempr_apagar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_remunoutrempr_listar as s2299_infotrabinterm_remunoutrempr_listar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_remunoutrempr_salvar as s2299_infotrabinterm_remunoutrempr_salvar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_remunoutrempr_api as s2299_infotrabinterm_remunoutrempr_api_views
from emensageriapro.s2299.views import s2299_infotrabinterm_proccs_apagar as s2299_infotrabinterm_proccs_apagar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_proccs_listar as s2299_infotrabinterm_proccs_listar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_proccs_salvar as s2299_infotrabinterm_proccs_salvar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_proccs_api as s2299_infotrabinterm_proccs_api_views
from emensageriapro.s2299.views import s2299_infotrabinterm_quarentena_apagar as s2299_infotrabinterm_quarentena_apagar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_quarentena_listar as s2299_infotrabinterm_quarentena_listar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_quarentena_salvar as s2299_infotrabinterm_quarentena_salvar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_quarentena_api as s2299_infotrabinterm_quarentena_api_views
from emensageriapro.s2299.views import s2299_infotrabinterm_consigfgts_apagar as s2299_infotrabinterm_consigfgts_apagar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_consigfgts_listar as s2299_infotrabinterm_consigfgts_listar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_consigfgts_salvar as s2299_infotrabinterm_consigfgts_salvar_views
from emensageriapro.s2299.views import s2299_infotrabinterm_consigfgts_api as s2299_infotrabinterm_consigfgts_api_views


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


    url(r'^s2299-observacoes/apagar/(?P<pk>[0-9]+)/$',
        s2299_observacoes_apagar_views.apagar,
        name='s2299_observacoes_apagar'),

    url(r'^s2299-observacoes/api/$',
        s2299_observacoes_api_views.s2299observacoesList.as_view() ),

    url(r'^s2299-observacoes/api/(?P<pk>[0-9]+)/$',
        s2299_observacoes_api_views.s2299observacoesDetail.as_view() ),

    url(r'^s2299-observacoes/$',
        s2299_observacoes_listar_views.listar,
        name='s2299_observacoes'),

    url(r'^s2299-observacoes/salvar/(?P<pk>[0-9]+)/$',
        s2299_observacoes_salvar_views.salvar,
        name='s2299_observacoes_salvar'),

    url(r'^s2299-observacoes/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_observacoes_salvar_views.salvar,
        name='s2299_observacoes_salvar_tab'),

    url(r'^s2299-observacoes/cadastrar/$',
        s2299_observacoes_salvar_views.salvar,
        name='s2299_observacoes_cadastrar'),

    url(r'^s2299-observacoes/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_observacoes_salvar_views.salvar,
        name='s2299_observacoes_salvar_output'),

    url(r'^s2299-observacoes/(?P<output>[\w-]+)/$',
        s2299_observacoes_listar_views.listar,
        name='s2299_observacoes_output'),

    url(r'^s2299-sucessaovinc/apagar/(?P<pk>[0-9]+)/$',
        s2299_sucessaovinc_apagar_views.apagar,
        name='s2299_sucessaovinc_apagar'),

    url(r'^s2299-sucessaovinc/api/$',
        s2299_sucessaovinc_api_views.s2299sucessaoVincList.as_view() ),

    url(r'^s2299-sucessaovinc/api/(?P<pk>[0-9]+)/$',
        s2299_sucessaovinc_api_views.s2299sucessaoVincDetail.as_view() ),

    url(r'^s2299-sucessaovinc/$',
        s2299_sucessaovinc_listar_views.listar,
        name='s2299_sucessaovinc'),

    url(r'^s2299-sucessaovinc/salvar/(?P<pk>[0-9]+)/$',
        s2299_sucessaovinc_salvar_views.salvar,
        name='s2299_sucessaovinc_salvar'),

    url(r'^s2299-sucessaovinc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_sucessaovinc_salvar_views.salvar,
        name='s2299_sucessaovinc_salvar_tab'),

    url(r'^s2299-sucessaovinc/cadastrar/$',
        s2299_sucessaovinc_salvar_views.salvar,
        name='s2299_sucessaovinc_cadastrar'),

    url(r'^s2299-sucessaovinc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_sucessaovinc_salvar_views.salvar,
        name='s2299_sucessaovinc_salvar_output'),

    url(r'^s2299-sucessaovinc/(?P<output>[\w-]+)/$',
        s2299_sucessaovinc_listar_views.listar,
        name='s2299_sucessaovinc_output'),

    url(r'^s2299-transftit/apagar/(?P<pk>[0-9]+)/$',
        s2299_transftit_apagar_views.apagar,
        name='s2299_transftit_apagar'),

    url(r'^s2299-transftit/api/$',
        s2299_transftit_api_views.s2299transfTitList.as_view() ),

    url(r'^s2299-transftit/api/(?P<pk>[0-9]+)/$',
        s2299_transftit_api_views.s2299transfTitDetail.as_view() ),

    url(r'^s2299-transftit/$',
        s2299_transftit_listar_views.listar,
        name='s2299_transftit'),

    url(r'^s2299-transftit/salvar/(?P<pk>[0-9]+)/$',
        s2299_transftit_salvar_views.salvar,
        name='s2299_transftit_salvar'),

    url(r'^s2299-transftit/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_transftit_salvar_views.salvar,
        name='s2299_transftit_salvar_tab'),

    url(r'^s2299-transftit/cadastrar/$',
        s2299_transftit_salvar_views.salvar,
        name='s2299_transftit_cadastrar'),

    url(r'^s2299-transftit/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_transftit_salvar_views.salvar,
        name='s2299_transftit_salvar_output'),

    url(r'^s2299-transftit/(?P<output>[\w-]+)/$',
        s2299_transftit_listar_views.listar,
        name='s2299_transftit_output'),

    url(r'^s2299-mudancacpf/apagar/(?P<pk>[0-9]+)/$',
        s2299_mudancacpf_apagar_views.apagar,
        name='s2299_mudancacpf_apagar'),

    url(r'^s2299-mudancacpf/api/$',
        s2299_mudancacpf_api_views.s2299mudancaCPFList.as_view() ),

    url(r'^s2299-mudancacpf/api/(?P<pk>[0-9]+)/$',
        s2299_mudancacpf_api_views.s2299mudancaCPFDetail.as_view() ),

    url(r'^s2299-mudancacpf/$',
        s2299_mudancacpf_listar_views.listar,
        name='s2299_mudancacpf'),

    url(r'^s2299-mudancacpf/salvar/(?P<pk>[0-9]+)/$',
        s2299_mudancacpf_salvar_views.salvar,
        name='s2299_mudancacpf_salvar'),

    url(r'^s2299-mudancacpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_mudancacpf_salvar_views.salvar,
        name='s2299_mudancacpf_salvar_tab'),

    url(r'^s2299-mudancacpf/cadastrar/$',
        s2299_mudancacpf_salvar_views.salvar,
        name='s2299_mudancacpf_cadastrar'),

    url(r'^s2299-mudancacpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_mudancacpf_salvar_views.salvar,
        name='s2299_mudancacpf_salvar_output'),

    url(r'^s2299-mudancacpf/(?P<output>[\w-]+)/$',
        s2299_mudancacpf_listar_views.listar,
        name='s2299_mudancacpf_output'),

    url(r'^s2299-verbasresc/apagar/(?P<pk>[0-9]+)/$',
        s2299_verbasresc_apagar_views.apagar,
        name='s2299_verbasresc_apagar'),

    url(r'^s2299-verbasresc/api/$',
        s2299_verbasresc_api_views.s2299verbasRescList.as_view() ),

    url(r'^s2299-verbasresc/api/(?P<pk>[0-9]+)/$',
        s2299_verbasresc_api_views.s2299verbasRescDetail.as_view() ),

    url(r'^s2299-verbasresc/$',
        s2299_verbasresc_listar_views.listar,
        name='s2299_verbasresc'),

    url(r'^s2299-verbasresc/salvar/(?P<pk>[0-9]+)/$',
        s2299_verbasresc_salvar_views.salvar,
        name='s2299_verbasresc_salvar'),

    url(r'^s2299-verbasresc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_verbasresc_salvar_views.salvar,
        name='s2299_verbasresc_salvar_tab'),

    url(r'^s2299-verbasresc/cadastrar/$',
        s2299_verbasresc_salvar_views.salvar,
        name='s2299_verbasresc_cadastrar'),

    url(r'^s2299-verbasresc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_verbasresc_salvar_views.salvar,
        name='s2299_verbasresc_salvar_output'),

    url(r'^s2299-verbasresc/(?P<output>[\w-]+)/$',
        s2299_verbasresc_listar_views.listar,
        name='s2299_verbasresc_output'),

    url(r'^s2299-dmdev/apagar/(?P<pk>[0-9]+)/$',
        s2299_dmdev_apagar_views.apagar,
        name='s2299_dmdev_apagar'),

    url(r'^s2299-dmdev/api/$',
        s2299_dmdev_api_views.s2299dmDevList.as_view() ),

    url(r'^s2299-dmdev/api/(?P<pk>[0-9]+)/$',
        s2299_dmdev_api_views.s2299dmDevDetail.as_view() ),

    url(r'^s2299-dmdev/$',
        s2299_dmdev_listar_views.listar,
        name='s2299_dmdev'),

    url(r'^s2299-dmdev/salvar/(?P<pk>[0-9]+)/$',
        s2299_dmdev_salvar_views.salvar,
        name='s2299_dmdev_salvar'),

    url(r'^s2299-dmdev/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_dmdev_salvar_views.salvar,
        name='s2299_dmdev_salvar_tab'),

    url(r'^s2299-dmdev/cadastrar/$',
        s2299_dmdev_salvar_views.salvar,
        name='s2299_dmdev_cadastrar'),

    url(r'^s2299-dmdev/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_dmdev_salvar_views.salvar,
        name='s2299_dmdev_salvar_output'),

    url(r'^s2299-dmdev/(?P<output>[\w-]+)/$',
        s2299_dmdev_listar_views.listar,
        name='s2299_dmdev_output'),

    url(r'^s2299-infoperapur/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_apagar_views.apagar,
        name='s2299_infoperapur_apagar'),

    url(r'^s2299-infoperapur/api/$',
        s2299_infoperapur_api_views.s2299infoPerApurList.as_view() ),

    url(r'^s2299-infoperapur/api/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_api_views.s2299infoPerApurDetail.as_view() ),

    url(r'^s2299-infoperapur/$',
        s2299_infoperapur_listar_views.listar,
        name='s2299_infoperapur'),

    url(r'^s2299-infoperapur/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_salvar_views.salvar,
        name='s2299_infoperapur_salvar'),

    url(r'^s2299-infoperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperapur_salvar_views.salvar,
        name='s2299_infoperapur_salvar_tab'),

    url(r'^s2299-infoperapur/cadastrar/$',
        s2299_infoperapur_salvar_views.salvar,
        name='s2299_infoperapur_cadastrar'),

    url(r'^s2299-infoperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperapur_salvar_views.salvar,
        name='s2299_infoperapur_salvar_output'),

    url(r'^s2299-infoperapur/(?P<output>[\w-]+)/$',
        s2299_infoperapur_listar_views.listar,
        name='s2299_infoperapur_output'),

    url(r'^s2299-infoperapur-ideestablot/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_ideestablot_apagar_views.apagar,
        name='s2299_infoperapur_ideestablot_apagar'),

    url(r'^s2299-infoperapur-ideestablot/api/$',
        s2299_infoperapur_ideestablot_api_views.s2299infoPerApurideEstabLotList.as_view() ),

    url(r'^s2299-infoperapur-ideestablot/api/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_ideestablot_api_views.s2299infoPerApurideEstabLotDetail.as_view() ),

    url(r'^s2299-infoperapur-ideestablot/$',
        s2299_infoperapur_ideestablot_listar_views.listar,
        name='s2299_infoperapur_ideestablot'),

    url(r'^s2299-infoperapur-ideestablot/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_ideestablot_salvar_views.salvar,
        name='s2299_infoperapur_ideestablot_salvar'),

    url(r'^s2299-infoperapur-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperapur_ideestablot_salvar_views.salvar,
        name='s2299_infoperapur_ideestablot_salvar_tab'),

    url(r'^s2299-infoperapur-ideestablot/cadastrar/$',
        s2299_infoperapur_ideestablot_salvar_views.salvar,
        name='s2299_infoperapur_ideestablot_cadastrar'),

    url(r'^s2299-infoperapur-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperapur_ideestablot_salvar_views.salvar,
        name='s2299_infoperapur_ideestablot_salvar_output'),

    url(r'^s2299-infoperapur-ideestablot/(?P<output>[\w-]+)/$',
        s2299_infoperapur_ideestablot_listar_views.listar,
        name='s2299_infoperapur_ideestablot_output'),

    url(r'^s2299-infoperapur-detverbas/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_detverbas_apagar_views.apagar,
        name='s2299_infoperapur_detverbas_apagar'),

    url(r'^s2299-infoperapur-detverbas/api/$',
        s2299_infoperapur_detverbas_api_views.s2299infoPerApurdetVerbasList.as_view() ),

    url(r'^s2299-infoperapur-detverbas/api/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_detverbas_api_views.s2299infoPerApurdetVerbasDetail.as_view() ),

    url(r'^s2299-infoperapur-detverbas/$',
        s2299_infoperapur_detverbas_listar_views.listar,
        name='s2299_infoperapur_detverbas'),

    url(r'^s2299-infoperapur-detverbas/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_detverbas_salvar_views.salvar,
        name='s2299_infoperapur_detverbas_salvar'),

    url(r'^s2299-infoperapur-detverbas/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperapur_detverbas_salvar_views.salvar,
        name='s2299_infoperapur_detverbas_salvar_tab'),

    url(r'^s2299-infoperapur-detverbas/cadastrar/$',
        s2299_infoperapur_detverbas_salvar_views.salvar,
        name='s2299_infoperapur_detverbas_cadastrar'),

    url(r'^s2299-infoperapur-detverbas/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperapur_detverbas_salvar_views.salvar,
        name='s2299_infoperapur_detverbas_salvar_output'),

    url(r'^s2299-infoperapur-detverbas/(?P<output>[\w-]+)/$',
        s2299_infoperapur_detverbas_listar_views.listar,
        name='s2299_infoperapur_detverbas_output'),

    url(r'^s2299-infoperapur-infosaudecolet/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_infosaudecolet_apagar_views.apagar,
        name='s2299_infoperapur_infosaudecolet_apagar'),

    url(r'^s2299-infoperapur-infosaudecolet/api/$',
        s2299_infoperapur_infosaudecolet_api_views.s2299infoPerApurinfoSaudeColetList.as_view() ),

    url(r'^s2299-infoperapur-infosaudecolet/api/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_infosaudecolet_api_views.s2299infoPerApurinfoSaudeColetDetail.as_view() ),

    url(r'^s2299-infoperapur-infosaudecolet/$',
        s2299_infoperapur_infosaudecolet_listar_views.listar,
        name='s2299_infoperapur_infosaudecolet'),

    url(r'^s2299-infoperapur-infosaudecolet/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s2299_infoperapur_infosaudecolet_salvar'),

    url(r'^s2299-infoperapur-infosaudecolet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s2299_infoperapur_infosaudecolet_salvar_tab'),

    url(r'^s2299-infoperapur-infosaudecolet/cadastrar/$',
        s2299_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s2299_infoperapur_infosaudecolet_cadastrar'),

    url(r'^s2299-infoperapur-infosaudecolet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s2299_infoperapur_infosaudecolet_salvar_output'),

    url(r'^s2299-infoperapur-infosaudecolet/(?P<output>[\w-]+)/$',
        s2299_infoperapur_infosaudecolet_listar_views.listar,
        name='s2299_infoperapur_infosaudecolet_output'),

    url(r'^s2299-infoperapur-detoper/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_detoper_apagar_views.apagar,
        name='s2299_infoperapur_detoper_apagar'),

    url(r'^s2299-infoperapur-detoper/api/$',
        s2299_infoperapur_detoper_api_views.s2299infoPerApurdetOperList.as_view() ),

    url(r'^s2299-infoperapur-detoper/api/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_detoper_api_views.s2299infoPerApurdetOperDetail.as_view() ),

    url(r'^s2299-infoperapur-detoper/$',
        s2299_infoperapur_detoper_listar_views.listar,
        name='s2299_infoperapur_detoper'),

    url(r'^s2299-infoperapur-detoper/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_detoper_salvar_views.salvar,
        name='s2299_infoperapur_detoper_salvar'),

    url(r'^s2299-infoperapur-detoper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperapur_detoper_salvar_views.salvar,
        name='s2299_infoperapur_detoper_salvar_tab'),

    url(r'^s2299-infoperapur-detoper/cadastrar/$',
        s2299_infoperapur_detoper_salvar_views.salvar,
        name='s2299_infoperapur_detoper_cadastrar'),

    url(r'^s2299-infoperapur-detoper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperapur_detoper_salvar_views.salvar,
        name='s2299_infoperapur_detoper_salvar_output'),

    url(r'^s2299-infoperapur-detoper/(?P<output>[\w-]+)/$',
        s2299_infoperapur_detoper_listar_views.listar,
        name='s2299_infoperapur_detoper_output'),

    url(r'^s2299-infoperapur-detplano/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_detplano_apagar_views.apagar,
        name='s2299_infoperapur_detplano_apagar'),

    url(r'^s2299-infoperapur-detplano/api/$',
        s2299_infoperapur_detplano_api_views.s2299infoPerApurdetPlanoList.as_view() ),

    url(r'^s2299-infoperapur-detplano/api/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_detplano_api_views.s2299infoPerApurdetPlanoDetail.as_view() ),

    url(r'^s2299-infoperapur-detplano/$',
        s2299_infoperapur_detplano_listar_views.listar,
        name='s2299_infoperapur_detplano'),

    url(r'^s2299-infoperapur-detplano/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_detplano_salvar_views.salvar,
        name='s2299_infoperapur_detplano_salvar'),

    url(r'^s2299-infoperapur-detplano/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperapur_detplano_salvar_views.salvar,
        name='s2299_infoperapur_detplano_salvar_tab'),

    url(r'^s2299-infoperapur-detplano/cadastrar/$',
        s2299_infoperapur_detplano_salvar_views.salvar,
        name='s2299_infoperapur_detplano_cadastrar'),

    url(r'^s2299-infoperapur-detplano/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperapur_detplano_salvar_views.salvar,
        name='s2299_infoperapur_detplano_salvar_output'),

    url(r'^s2299-infoperapur-detplano/(?P<output>[\w-]+)/$',
        s2299_infoperapur_detplano_listar_views.listar,
        name='s2299_infoperapur_detplano_output'),

    url(r'^s2299-infoperapur-infoagnocivo/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_infoagnocivo_apagar_views.apagar,
        name='s2299_infoperapur_infoagnocivo_apagar'),

    url(r'^s2299-infoperapur-infoagnocivo/api/$',
        s2299_infoperapur_infoagnocivo_api_views.s2299infoPerApurinfoAgNocivoList.as_view() ),

    url(r'^s2299-infoperapur-infoagnocivo/api/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_infoagnocivo_api_views.s2299infoPerApurinfoAgNocivoDetail.as_view() ),

    url(r'^s2299-infoperapur-infoagnocivo/$',
        s2299_infoperapur_infoagnocivo_listar_views.listar,
        name='s2299_infoperapur_infoagnocivo'),

    url(r'^s2299-infoperapur-infoagnocivo/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_infoagnocivo_salvar_views.salvar,
        name='s2299_infoperapur_infoagnocivo_salvar'),

    url(r'^s2299-infoperapur-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperapur_infoagnocivo_salvar_views.salvar,
        name='s2299_infoperapur_infoagnocivo_salvar_tab'),

    url(r'^s2299-infoperapur-infoagnocivo/cadastrar/$',
        s2299_infoperapur_infoagnocivo_salvar_views.salvar,
        name='s2299_infoperapur_infoagnocivo_cadastrar'),

    url(r'^s2299-infoperapur-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperapur_infoagnocivo_salvar_views.salvar,
        name='s2299_infoperapur_infoagnocivo_salvar_output'),

    url(r'^s2299-infoperapur-infoagnocivo/(?P<output>[\w-]+)/$',
        s2299_infoperapur_infoagnocivo_listar_views.listar,
        name='s2299_infoperapur_infoagnocivo_output'),

    url(r'^s2299-infoperapur-infosimples/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_infosimples_apagar_views.apagar,
        name='s2299_infoperapur_infosimples_apagar'),

    url(r'^s2299-infoperapur-infosimples/api/$',
        s2299_infoperapur_infosimples_api_views.s2299infoPerApurinfoSimplesList.as_view() ),

    url(r'^s2299-infoperapur-infosimples/api/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_infosimples_api_views.s2299infoPerApurinfoSimplesDetail.as_view() ),

    url(r'^s2299-infoperapur-infosimples/$',
        s2299_infoperapur_infosimples_listar_views.listar,
        name='s2299_infoperapur_infosimples'),

    url(r'^s2299-infoperapur-infosimples/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperapur_infosimples_salvar_views.salvar,
        name='s2299_infoperapur_infosimples_salvar'),

    url(r'^s2299-infoperapur-infosimples/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperapur_infosimples_salvar_views.salvar,
        name='s2299_infoperapur_infosimples_salvar_tab'),

    url(r'^s2299-infoperapur-infosimples/cadastrar/$',
        s2299_infoperapur_infosimples_salvar_views.salvar,
        name='s2299_infoperapur_infosimples_cadastrar'),

    url(r'^s2299-infoperapur-infosimples/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperapur_infosimples_salvar_views.salvar,
        name='s2299_infoperapur_infosimples_salvar_output'),

    url(r'^s2299-infoperapur-infosimples/(?P<output>[\w-]+)/$',
        s2299_infoperapur_infosimples_listar_views.listar,
        name='s2299_infoperapur_infosimples_output'),

    url(r'^s2299-infoperant/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_apagar_views.apagar,
        name='s2299_infoperant_apagar'),

    url(r'^s2299-infoperant/api/$',
        s2299_infoperant_api_views.s2299infoPerAntList.as_view() ),

    url(r'^s2299-infoperant/api/(?P<pk>[0-9]+)/$',
        s2299_infoperant_api_views.s2299infoPerAntDetail.as_view() ),

    url(r'^s2299-infoperant/$',
        s2299_infoperant_listar_views.listar,
        name='s2299_infoperant'),

    url(r'^s2299-infoperant/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_salvar_views.salvar,
        name='s2299_infoperant_salvar'),

    url(r'^s2299-infoperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperant_salvar_views.salvar,
        name='s2299_infoperant_salvar_tab'),

    url(r'^s2299-infoperant/cadastrar/$',
        s2299_infoperant_salvar_views.salvar,
        name='s2299_infoperant_cadastrar'),

    url(r'^s2299-infoperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperant_salvar_views.salvar,
        name='s2299_infoperant_salvar_output'),

    url(r'^s2299-infoperant/(?P<output>[\w-]+)/$',
        s2299_infoperant_listar_views.listar,
        name='s2299_infoperant_output'),

    url(r'^s2299-infoperant-ideadc/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_ideadc_apagar_views.apagar,
        name='s2299_infoperant_ideadc_apagar'),

    url(r'^s2299-infoperant-ideadc/api/$',
        s2299_infoperant_ideadc_api_views.s2299infoPerAntideADCList.as_view() ),

    url(r'^s2299-infoperant-ideadc/api/(?P<pk>[0-9]+)/$',
        s2299_infoperant_ideadc_api_views.s2299infoPerAntideADCDetail.as_view() ),

    url(r'^s2299-infoperant-ideadc/$',
        s2299_infoperant_ideadc_listar_views.listar,
        name='s2299_infoperant_ideadc'),

    url(r'^s2299-infoperant-ideadc/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_ideadc_salvar_views.salvar,
        name='s2299_infoperant_ideadc_salvar'),

    url(r'^s2299-infoperant-ideadc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperant_ideadc_salvar_views.salvar,
        name='s2299_infoperant_ideadc_salvar_tab'),

    url(r'^s2299-infoperant-ideadc/cadastrar/$',
        s2299_infoperant_ideadc_salvar_views.salvar,
        name='s2299_infoperant_ideadc_cadastrar'),

    url(r'^s2299-infoperant-ideadc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperant_ideadc_salvar_views.salvar,
        name='s2299_infoperant_ideadc_salvar_output'),

    url(r'^s2299-infoperant-ideadc/(?P<output>[\w-]+)/$',
        s2299_infoperant_ideadc_listar_views.listar,
        name='s2299_infoperant_ideadc_output'),

    url(r'^s2299-infoperant-ideperiodo/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_ideperiodo_apagar_views.apagar,
        name='s2299_infoperant_ideperiodo_apagar'),

    url(r'^s2299-infoperant-ideperiodo/api/$',
        s2299_infoperant_ideperiodo_api_views.s2299infoPerAntidePeriodoList.as_view() ),

    url(r'^s2299-infoperant-ideperiodo/api/(?P<pk>[0-9]+)/$',
        s2299_infoperant_ideperiodo_api_views.s2299infoPerAntidePeriodoDetail.as_view() ),

    url(r'^s2299-infoperant-ideperiodo/$',
        s2299_infoperant_ideperiodo_listar_views.listar,
        name='s2299_infoperant_ideperiodo'),

    url(r'^s2299-infoperant-ideperiodo/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_ideperiodo_salvar_views.salvar,
        name='s2299_infoperant_ideperiodo_salvar'),

    url(r'^s2299-infoperant-ideperiodo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperant_ideperiodo_salvar_views.salvar,
        name='s2299_infoperant_ideperiodo_salvar_tab'),

    url(r'^s2299-infoperant-ideperiodo/cadastrar/$',
        s2299_infoperant_ideperiodo_salvar_views.salvar,
        name='s2299_infoperant_ideperiodo_cadastrar'),

    url(r'^s2299-infoperant-ideperiodo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperant_ideperiodo_salvar_views.salvar,
        name='s2299_infoperant_ideperiodo_salvar_output'),

    url(r'^s2299-infoperant-ideperiodo/(?P<output>[\w-]+)/$',
        s2299_infoperant_ideperiodo_listar_views.listar,
        name='s2299_infoperant_ideperiodo_output'),

    url(r'^s2299-infoperant-ideestablot/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_ideestablot_apagar_views.apagar,
        name='s2299_infoperant_ideestablot_apagar'),

    url(r'^s2299-infoperant-ideestablot/api/$',
        s2299_infoperant_ideestablot_api_views.s2299infoPerAntideEstabLotList.as_view() ),

    url(r'^s2299-infoperant-ideestablot/api/(?P<pk>[0-9]+)/$',
        s2299_infoperant_ideestablot_api_views.s2299infoPerAntideEstabLotDetail.as_view() ),

    url(r'^s2299-infoperant-ideestablot/$',
        s2299_infoperant_ideestablot_listar_views.listar,
        name='s2299_infoperant_ideestablot'),

    url(r'^s2299-infoperant-ideestablot/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_ideestablot_salvar_views.salvar,
        name='s2299_infoperant_ideestablot_salvar'),

    url(r'^s2299-infoperant-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperant_ideestablot_salvar_views.salvar,
        name='s2299_infoperant_ideestablot_salvar_tab'),

    url(r'^s2299-infoperant-ideestablot/cadastrar/$',
        s2299_infoperant_ideestablot_salvar_views.salvar,
        name='s2299_infoperant_ideestablot_cadastrar'),

    url(r'^s2299-infoperant-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperant_ideestablot_salvar_views.salvar,
        name='s2299_infoperant_ideestablot_salvar_output'),

    url(r'^s2299-infoperant-ideestablot/(?P<output>[\w-]+)/$',
        s2299_infoperant_ideestablot_listar_views.listar,
        name='s2299_infoperant_ideestablot_output'),

    url(r'^s2299-infoperant-detverbas/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_detverbas_apagar_views.apagar,
        name='s2299_infoperant_detverbas_apagar'),

    url(r'^s2299-infoperant-detverbas/api/$',
        s2299_infoperant_detverbas_api_views.s2299infoPerAntdetVerbasList.as_view() ),

    url(r'^s2299-infoperant-detverbas/api/(?P<pk>[0-9]+)/$',
        s2299_infoperant_detverbas_api_views.s2299infoPerAntdetVerbasDetail.as_view() ),

    url(r'^s2299-infoperant-detverbas/$',
        s2299_infoperant_detverbas_listar_views.listar,
        name='s2299_infoperant_detverbas'),

    url(r'^s2299-infoperant-detverbas/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_detverbas_salvar_views.salvar,
        name='s2299_infoperant_detverbas_salvar'),

    url(r'^s2299-infoperant-detverbas/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperant_detverbas_salvar_views.salvar,
        name='s2299_infoperant_detverbas_salvar_tab'),

    url(r'^s2299-infoperant-detverbas/cadastrar/$',
        s2299_infoperant_detverbas_salvar_views.salvar,
        name='s2299_infoperant_detverbas_cadastrar'),

    url(r'^s2299-infoperant-detverbas/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperant_detverbas_salvar_views.salvar,
        name='s2299_infoperant_detverbas_salvar_output'),

    url(r'^s2299-infoperant-detverbas/(?P<output>[\w-]+)/$',
        s2299_infoperant_detverbas_listar_views.listar,
        name='s2299_infoperant_detverbas_output'),

    url(r'^s2299-infoperant-infoagnocivo/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_infoagnocivo_apagar_views.apagar,
        name='s2299_infoperant_infoagnocivo_apagar'),

    url(r'^s2299-infoperant-infoagnocivo/api/$',
        s2299_infoperant_infoagnocivo_api_views.s2299infoPerAntinfoAgNocivoList.as_view() ),

    url(r'^s2299-infoperant-infoagnocivo/api/(?P<pk>[0-9]+)/$',
        s2299_infoperant_infoagnocivo_api_views.s2299infoPerAntinfoAgNocivoDetail.as_view() ),

    url(r'^s2299-infoperant-infoagnocivo/$',
        s2299_infoperant_infoagnocivo_listar_views.listar,
        name='s2299_infoperant_infoagnocivo'),

    url(r'^s2299-infoperant-infoagnocivo/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_infoagnocivo_salvar_views.salvar,
        name='s2299_infoperant_infoagnocivo_salvar'),

    url(r'^s2299-infoperant-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperant_infoagnocivo_salvar_views.salvar,
        name='s2299_infoperant_infoagnocivo_salvar_tab'),

    url(r'^s2299-infoperant-infoagnocivo/cadastrar/$',
        s2299_infoperant_infoagnocivo_salvar_views.salvar,
        name='s2299_infoperant_infoagnocivo_cadastrar'),

    url(r'^s2299-infoperant-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperant_infoagnocivo_salvar_views.salvar,
        name='s2299_infoperant_infoagnocivo_salvar_output'),

    url(r'^s2299-infoperant-infoagnocivo/(?P<output>[\w-]+)/$',
        s2299_infoperant_infoagnocivo_listar_views.listar,
        name='s2299_infoperant_infoagnocivo_output'),

    url(r'^s2299-infoperant-infosimples/apagar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_infosimples_apagar_views.apagar,
        name='s2299_infoperant_infosimples_apagar'),

    url(r'^s2299-infoperant-infosimples/api/$',
        s2299_infoperant_infosimples_api_views.s2299infoPerAntinfoSimplesList.as_view() ),

    url(r'^s2299-infoperant-infosimples/api/(?P<pk>[0-9]+)/$',
        s2299_infoperant_infosimples_api_views.s2299infoPerAntinfoSimplesDetail.as_view() ),

    url(r'^s2299-infoperant-infosimples/$',
        s2299_infoperant_infosimples_listar_views.listar,
        name='s2299_infoperant_infosimples'),

    url(r'^s2299-infoperant-infosimples/salvar/(?P<pk>[0-9]+)/$',
        s2299_infoperant_infosimples_salvar_views.salvar,
        name='s2299_infoperant_infosimples_salvar'),

    url(r'^s2299-infoperant-infosimples/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infoperant_infosimples_salvar_views.salvar,
        name='s2299_infoperant_infosimples_salvar_tab'),

    url(r'^s2299-infoperant-infosimples/cadastrar/$',
        s2299_infoperant_infosimples_salvar_views.salvar,
        name='s2299_infoperant_infosimples_cadastrar'),

    url(r'^s2299-infoperant-infosimples/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infoperant_infosimples_salvar_views.salvar,
        name='s2299_infoperant_infosimples_salvar_output'),

    url(r'^s2299-infoperant-infosimples/(?P<output>[\w-]+)/$',
        s2299_infoperant_infosimples_listar_views.listar,
        name='s2299_infoperant_infosimples_output'),

    url(r'^s2299-infotrabinterm/apagar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_apagar_views.apagar,
        name='s2299_infotrabinterm_apagar'),

    url(r'^s2299-infotrabinterm/api/$',
        s2299_infotrabinterm_api_views.s2299infoTrabIntermList.as_view() ),

    url(r'^s2299-infotrabinterm/api/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_api_views.s2299infoTrabIntermDetail.as_view() ),

    url(r'^s2299-infotrabinterm/$',
        s2299_infotrabinterm_listar_views.listar,
        name='s2299_infotrabinterm'),

    url(r'^s2299-infotrabinterm/salvar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_salvar_views.salvar,
        name='s2299_infotrabinterm_salvar'),

    url(r'^s2299-infotrabinterm/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infotrabinterm_salvar_views.salvar,
        name='s2299_infotrabinterm_salvar_tab'),

    url(r'^s2299-infotrabinterm/cadastrar/$',
        s2299_infotrabinterm_salvar_views.salvar,
        name='s2299_infotrabinterm_cadastrar'),

    url(r'^s2299-infotrabinterm/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_salvar_views.salvar,
        name='s2299_infotrabinterm_salvar_output'),

    url(r'^s2299-infotrabinterm/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_listar_views.listar,
        name='s2299_infotrabinterm_output'),

    url(r'^s2299-infotrabinterm-procjudtrab/apagar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_procjudtrab_apagar_views.apagar,
        name='s2299_infotrabinterm_procjudtrab_apagar'),

    url(r'^s2299-infotrabinterm-procjudtrab/api/$',
        s2299_infotrabinterm_procjudtrab_api_views.s2299infoTrabIntermprocJudTrabList.as_view() ),

    url(r'^s2299-infotrabinterm-procjudtrab/api/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_procjudtrab_api_views.s2299infoTrabIntermprocJudTrabDetail.as_view() ),

    url(r'^s2299-infotrabinterm-procjudtrab/$',
        s2299_infotrabinterm_procjudtrab_listar_views.listar,
        name='s2299_infotrabinterm_procjudtrab'),

    url(r'^s2299-infotrabinterm-procjudtrab/salvar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_procjudtrab_salvar_views.salvar,
        name='s2299_infotrabinterm_procjudtrab_salvar'),

    url(r'^s2299-infotrabinterm-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infotrabinterm_procjudtrab_salvar_views.salvar,
        name='s2299_infotrabinterm_procjudtrab_salvar_tab'),

    url(r'^s2299-infotrabinterm-procjudtrab/cadastrar/$',
        s2299_infotrabinterm_procjudtrab_salvar_views.salvar,
        name='s2299_infotrabinterm_procjudtrab_cadastrar'),

    url(r'^s2299-infotrabinterm-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_procjudtrab_salvar_views.salvar,
        name='s2299_infotrabinterm_procjudtrab_salvar_output'),

    url(r'^s2299-infotrabinterm-procjudtrab/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_procjudtrab_listar_views.listar,
        name='s2299_infotrabinterm_procjudtrab_output'),

    url(r'^s2299-infotrabinterm-infomv/apagar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_infomv_apagar_views.apagar,
        name='s2299_infotrabinterm_infomv_apagar'),

    url(r'^s2299-infotrabinterm-infomv/api/$',
        s2299_infotrabinterm_infomv_api_views.s2299infoTrabInterminfoMVList.as_view() ),

    url(r'^s2299-infotrabinterm-infomv/api/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_infomv_api_views.s2299infoTrabInterminfoMVDetail.as_view() ),

    url(r'^s2299-infotrabinterm-infomv/$',
        s2299_infotrabinterm_infomv_listar_views.listar,
        name='s2299_infotrabinterm_infomv'),

    url(r'^s2299-infotrabinterm-infomv/salvar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_infomv_salvar_views.salvar,
        name='s2299_infotrabinterm_infomv_salvar'),

    url(r'^s2299-infotrabinterm-infomv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infotrabinterm_infomv_salvar_views.salvar,
        name='s2299_infotrabinterm_infomv_salvar_tab'),

    url(r'^s2299-infotrabinterm-infomv/cadastrar/$',
        s2299_infotrabinterm_infomv_salvar_views.salvar,
        name='s2299_infotrabinterm_infomv_cadastrar'),

    url(r'^s2299-infotrabinterm-infomv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_infomv_salvar_views.salvar,
        name='s2299_infotrabinterm_infomv_salvar_output'),

    url(r'^s2299-infotrabinterm-infomv/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_infomv_listar_views.listar,
        name='s2299_infotrabinterm_infomv_output'),

    url(r'^s2299-infotrabinterm-remunoutrempr/apagar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_remunoutrempr_apagar_views.apagar,
        name='s2299_infotrabinterm_remunoutrempr_apagar'),

    url(r'^s2299-infotrabinterm-remunoutrempr/api/$',
        s2299_infotrabinterm_remunoutrempr_api_views.s2299infoTrabIntermremunOutrEmprList.as_view() ),

    url(r'^s2299-infotrabinterm-remunoutrempr/api/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_remunoutrempr_api_views.s2299infoTrabIntermremunOutrEmprDetail.as_view() ),

    url(r'^s2299-infotrabinterm-remunoutrempr/$',
        s2299_infotrabinterm_remunoutrempr_listar_views.listar,
        name='s2299_infotrabinterm_remunoutrempr'),

    url(r'^s2299-infotrabinterm-remunoutrempr/salvar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_remunoutrempr_salvar_views.salvar,
        name='s2299_infotrabinterm_remunoutrempr_salvar'),

    url(r'^s2299-infotrabinterm-remunoutrempr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infotrabinterm_remunoutrempr_salvar_views.salvar,
        name='s2299_infotrabinterm_remunoutrempr_salvar_tab'),

    url(r'^s2299-infotrabinterm-remunoutrempr/cadastrar/$',
        s2299_infotrabinterm_remunoutrempr_salvar_views.salvar,
        name='s2299_infotrabinterm_remunoutrempr_cadastrar'),

    url(r'^s2299-infotrabinterm-remunoutrempr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_remunoutrempr_salvar_views.salvar,
        name='s2299_infotrabinterm_remunoutrempr_salvar_output'),

    url(r'^s2299-infotrabinterm-remunoutrempr/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_remunoutrempr_listar_views.listar,
        name='s2299_infotrabinterm_remunoutrempr_output'),

    url(r'^s2299-infotrabinterm-proccs/apagar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_proccs_apagar_views.apagar,
        name='s2299_infotrabinterm_proccs_apagar'),

    url(r'^s2299-infotrabinterm-proccs/api/$',
        s2299_infotrabinterm_proccs_api_views.s2299infoTrabIntermprocCSList.as_view() ),

    url(r'^s2299-infotrabinterm-proccs/api/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_proccs_api_views.s2299infoTrabIntermprocCSDetail.as_view() ),

    url(r'^s2299-infotrabinterm-proccs/$',
        s2299_infotrabinterm_proccs_listar_views.listar,
        name='s2299_infotrabinterm_proccs'),

    url(r'^s2299-infotrabinterm-proccs/salvar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_proccs_salvar_views.salvar,
        name='s2299_infotrabinterm_proccs_salvar'),

    url(r'^s2299-infotrabinterm-proccs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infotrabinterm_proccs_salvar_views.salvar,
        name='s2299_infotrabinterm_proccs_salvar_tab'),

    url(r'^s2299-infotrabinterm-proccs/cadastrar/$',
        s2299_infotrabinterm_proccs_salvar_views.salvar,
        name='s2299_infotrabinterm_proccs_cadastrar'),

    url(r'^s2299-infotrabinterm-proccs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_proccs_salvar_views.salvar,
        name='s2299_infotrabinterm_proccs_salvar_output'),

    url(r'^s2299-infotrabinterm-proccs/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_proccs_listar_views.listar,
        name='s2299_infotrabinterm_proccs_output'),

    url(r'^s2299-infotrabinterm-quarentena/apagar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_quarentena_apagar_views.apagar,
        name='s2299_infotrabinterm_quarentena_apagar'),

    url(r'^s2299-infotrabinterm-quarentena/api/$',
        s2299_infotrabinterm_quarentena_api_views.s2299infoTrabIntermquarentenaList.as_view() ),

    url(r'^s2299-infotrabinterm-quarentena/api/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_quarentena_api_views.s2299infoTrabIntermquarentenaDetail.as_view() ),

    url(r'^s2299-infotrabinterm-quarentena/$',
        s2299_infotrabinterm_quarentena_listar_views.listar,
        name='s2299_infotrabinterm_quarentena'),

    url(r'^s2299-infotrabinterm-quarentena/salvar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_quarentena_salvar_views.salvar,
        name='s2299_infotrabinterm_quarentena_salvar'),

    url(r'^s2299-infotrabinterm-quarentena/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infotrabinterm_quarentena_salvar_views.salvar,
        name='s2299_infotrabinterm_quarentena_salvar_tab'),

    url(r'^s2299-infotrabinterm-quarentena/cadastrar/$',
        s2299_infotrabinterm_quarentena_salvar_views.salvar,
        name='s2299_infotrabinterm_quarentena_cadastrar'),

    url(r'^s2299-infotrabinterm-quarentena/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_quarentena_salvar_views.salvar,
        name='s2299_infotrabinterm_quarentena_salvar_output'),

    url(r'^s2299-infotrabinterm-quarentena/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_quarentena_listar_views.listar,
        name='s2299_infotrabinterm_quarentena_output'),

    url(r'^s2299-infotrabinterm-consigfgts/apagar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_consigfgts_apagar_views.apagar,
        name='s2299_infotrabinterm_consigfgts_apagar'),

    url(r'^s2299-infotrabinterm-consigfgts/api/$',
        s2299_infotrabinterm_consigfgts_api_views.s2299infoTrabIntermconsigFGTSList.as_view() ),

    url(r'^s2299-infotrabinterm-consigfgts/api/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_consigfgts_api_views.s2299infoTrabIntermconsigFGTSDetail.as_view() ),

    url(r'^s2299-infotrabinterm-consigfgts/$',
        s2299_infotrabinterm_consigfgts_listar_views.listar,
        name='s2299_infotrabinterm_consigfgts'),

    url(r'^s2299-infotrabinterm-consigfgts/salvar/(?P<pk>[0-9]+)/$',
        s2299_infotrabinterm_consigfgts_salvar_views.salvar,
        name='s2299_infotrabinterm_consigfgts_salvar'),

    url(r'^s2299-infotrabinterm-consigfgts/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2299_infotrabinterm_consigfgts_salvar_views.salvar,
        name='s2299_infotrabinterm_consigfgts_salvar_tab'),

    url(r'^s2299-infotrabinterm-consigfgts/cadastrar/$',
        s2299_infotrabinterm_consigfgts_salvar_views.salvar,
        name='s2299_infotrabinterm_consigfgts_cadastrar'),

    url(r'^s2299-infotrabinterm-consigfgts/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_consigfgts_salvar_views.salvar,
        name='s2299_infotrabinterm_consigfgts_salvar_output'),

    url(r'^s2299-infotrabinterm-consigfgts/(?P<output>[\w-]+)/$',
        s2299_infotrabinterm_consigfgts_listar_views.listar,
        name='s2299_infotrabinterm_consigfgts_output'),


]