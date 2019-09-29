#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1200.views import s1200_infomv_apagar as s1200_infomv_apagar_views
from emensageriapro.s1200.views import s1200_infomv_listar as s1200_infomv_listar_views
from emensageriapro.s1200.views import s1200_infomv_salvar as s1200_infomv_salvar_views
from emensageriapro.s1200.views import s1200_infomv_api as s1200_infomv_api_views
from emensageriapro.s1200.views import s1200_remunoutrempr_apagar as s1200_remunoutrempr_apagar_views
from emensageriapro.s1200.views import s1200_remunoutrempr_listar as s1200_remunoutrempr_listar_views
from emensageriapro.s1200.views import s1200_remunoutrempr_salvar as s1200_remunoutrempr_salvar_views
from emensageriapro.s1200.views import s1200_remunoutrempr_api as s1200_remunoutrempr_api_views
from emensageriapro.s1200.views import s1200_infocomplem_apagar as s1200_infocomplem_apagar_views
from emensageriapro.s1200.views import s1200_infocomplem_listar as s1200_infocomplem_listar_views
from emensageriapro.s1200.views import s1200_infocomplem_salvar as s1200_infocomplem_salvar_views
from emensageriapro.s1200.views import s1200_infocomplem_api as s1200_infocomplem_api_views
from emensageriapro.s1200.views import s1200_sucessaovinc_apagar as s1200_sucessaovinc_apagar_views
from emensageriapro.s1200.views import s1200_sucessaovinc_listar as s1200_sucessaovinc_listar_views
from emensageriapro.s1200.views import s1200_sucessaovinc_salvar as s1200_sucessaovinc_salvar_views
from emensageriapro.s1200.views import s1200_sucessaovinc_api as s1200_sucessaovinc_api_views
from emensageriapro.s1200.views import s1200_procjudtrab_apagar as s1200_procjudtrab_apagar_views
from emensageriapro.s1200.views import s1200_procjudtrab_listar as s1200_procjudtrab_listar_views
from emensageriapro.s1200.views import s1200_procjudtrab_salvar as s1200_procjudtrab_salvar_views
from emensageriapro.s1200.views import s1200_procjudtrab_api as s1200_procjudtrab_api_views
from emensageriapro.s1200.views import s1200_infointerm_apagar as s1200_infointerm_apagar_views
from emensageriapro.s1200.views import s1200_infointerm_listar as s1200_infointerm_listar_views
from emensageriapro.s1200.views import s1200_infointerm_salvar as s1200_infointerm_salvar_views
from emensageriapro.s1200.views import s1200_infointerm_api as s1200_infointerm_api_views
from emensageriapro.s1200.views import s1200_dmdev_apagar as s1200_dmdev_apagar_views
from emensageriapro.s1200.views import s1200_dmdev_listar as s1200_dmdev_listar_views
from emensageriapro.s1200.views import s1200_dmdev_salvar as s1200_dmdev_salvar_views
from emensageriapro.s1200.views import s1200_dmdev_api as s1200_dmdev_api_views
from emensageriapro.s1200.views import s1200_infoperapur_apagar as s1200_infoperapur_apagar_views
from emensageriapro.s1200.views import s1200_infoperapur_listar as s1200_infoperapur_listar_views
from emensageriapro.s1200.views import s1200_infoperapur_salvar as s1200_infoperapur_salvar_views
from emensageriapro.s1200.views import s1200_infoperapur_api as s1200_infoperapur_api_views
from emensageriapro.s1200.views import s1200_infoperapur_ideestablot_apagar as s1200_infoperapur_ideestablot_apagar_views
from emensageriapro.s1200.views import s1200_infoperapur_ideestablot_listar as s1200_infoperapur_ideestablot_listar_views
from emensageriapro.s1200.views import s1200_infoperapur_ideestablot_salvar as s1200_infoperapur_ideestablot_salvar_views
from emensageriapro.s1200.views import s1200_infoperapur_ideestablot_api as s1200_infoperapur_ideestablot_api_views
from emensageriapro.s1200.views import s1200_infoperapur_remunperapur_apagar as s1200_infoperapur_remunperapur_apagar_views
from emensageriapro.s1200.views import s1200_infoperapur_remunperapur_listar as s1200_infoperapur_remunperapur_listar_views
from emensageriapro.s1200.views import s1200_infoperapur_remunperapur_salvar as s1200_infoperapur_remunperapur_salvar_views
from emensageriapro.s1200.views import s1200_infoperapur_remunperapur_api as s1200_infoperapur_remunperapur_api_views
from emensageriapro.s1200.views import s1200_infoperapur_itensremun_apagar as s1200_infoperapur_itensremun_apagar_views
from emensageriapro.s1200.views import s1200_infoperapur_itensremun_listar as s1200_infoperapur_itensremun_listar_views
from emensageriapro.s1200.views import s1200_infoperapur_itensremun_salvar as s1200_infoperapur_itensremun_salvar_views
from emensageriapro.s1200.views import s1200_infoperapur_itensremun_api as s1200_infoperapur_itensremun_api_views
from emensageriapro.s1200.views import s1200_infoperapur_infosaudecolet_apagar as s1200_infoperapur_infosaudecolet_apagar_views
from emensageriapro.s1200.views import s1200_infoperapur_infosaudecolet_listar as s1200_infoperapur_infosaudecolet_listar_views
from emensageriapro.s1200.views import s1200_infoperapur_infosaudecolet_salvar as s1200_infoperapur_infosaudecolet_salvar_views
from emensageriapro.s1200.views import s1200_infoperapur_infosaudecolet_api as s1200_infoperapur_infosaudecolet_api_views
from emensageriapro.s1200.views import s1200_infoperapur_detoper_apagar as s1200_infoperapur_detoper_apagar_views
from emensageriapro.s1200.views import s1200_infoperapur_detoper_listar as s1200_infoperapur_detoper_listar_views
from emensageriapro.s1200.views import s1200_infoperapur_detoper_salvar as s1200_infoperapur_detoper_salvar_views
from emensageriapro.s1200.views import s1200_infoperapur_detoper_api as s1200_infoperapur_detoper_api_views
from emensageriapro.s1200.views import s1200_infoperapur_detplano_apagar as s1200_infoperapur_detplano_apagar_views
from emensageriapro.s1200.views import s1200_infoperapur_detplano_listar as s1200_infoperapur_detplano_listar_views
from emensageriapro.s1200.views import s1200_infoperapur_detplano_salvar as s1200_infoperapur_detplano_salvar_views
from emensageriapro.s1200.views import s1200_infoperapur_detplano_api as s1200_infoperapur_detplano_api_views
from emensageriapro.s1200.views import s1200_infoperapur_infoagnocivo_apagar as s1200_infoperapur_infoagnocivo_apagar_views
from emensageriapro.s1200.views import s1200_infoperapur_infoagnocivo_listar as s1200_infoperapur_infoagnocivo_listar_views
from emensageriapro.s1200.views import s1200_infoperapur_infoagnocivo_salvar as s1200_infoperapur_infoagnocivo_salvar_views
from emensageriapro.s1200.views import s1200_infoperapur_infoagnocivo_api as s1200_infoperapur_infoagnocivo_api_views
from emensageriapro.s1200.views import s1200_infoperapur_infotrabinterm_apagar as s1200_infoperapur_infotrabinterm_apagar_views
from emensageriapro.s1200.views import s1200_infoperapur_infotrabinterm_listar as s1200_infoperapur_infotrabinterm_listar_views
from emensageriapro.s1200.views import s1200_infoperapur_infotrabinterm_salvar as s1200_infoperapur_infotrabinterm_salvar_views
from emensageriapro.s1200.views import s1200_infoperapur_infotrabinterm_api as s1200_infoperapur_infotrabinterm_api_views
from emensageriapro.s1200.views import s1200_infoperant_apagar as s1200_infoperant_apagar_views
from emensageriapro.s1200.views import s1200_infoperant_listar as s1200_infoperant_listar_views
from emensageriapro.s1200.views import s1200_infoperant_salvar as s1200_infoperant_salvar_views
from emensageriapro.s1200.views import s1200_infoperant_api as s1200_infoperant_api_views
from emensageriapro.s1200.views import s1200_infoperant_ideadc_apagar as s1200_infoperant_ideadc_apagar_views
from emensageriapro.s1200.views import s1200_infoperant_ideadc_listar as s1200_infoperant_ideadc_listar_views
from emensageriapro.s1200.views import s1200_infoperant_ideadc_salvar as s1200_infoperant_ideadc_salvar_views
from emensageriapro.s1200.views import s1200_infoperant_ideadc_api as s1200_infoperant_ideadc_api_views
from emensageriapro.s1200.views import s1200_infoperant_ideperiodo_apagar as s1200_infoperant_ideperiodo_apagar_views
from emensageriapro.s1200.views import s1200_infoperant_ideperiodo_listar as s1200_infoperant_ideperiodo_listar_views
from emensageriapro.s1200.views import s1200_infoperant_ideperiodo_salvar as s1200_infoperant_ideperiodo_salvar_views
from emensageriapro.s1200.views import s1200_infoperant_ideperiodo_api as s1200_infoperant_ideperiodo_api_views
from emensageriapro.s1200.views import s1200_infoperant_ideestablot_apagar as s1200_infoperant_ideestablot_apagar_views
from emensageriapro.s1200.views import s1200_infoperant_ideestablot_listar as s1200_infoperant_ideestablot_listar_views
from emensageriapro.s1200.views import s1200_infoperant_ideestablot_salvar as s1200_infoperant_ideestablot_salvar_views
from emensageriapro.s1200.views import s1200_infoperant_ideestablot_api as s1200_infoperant_ideestablot_api_views
from emensageriapro.s1200.views import s1200_infoperant_remunperant_apagar as s1200_infoperant_remunperant_apagar_views
from emensageriapro.s1200.views import s1200_infoperant_remunperant_listar as s1200_infoperant_remunperant_listar_views
from emensageriapro.s1200.views import s1200_infoperant_remunperant_salvar as s1200_infoperant_remunperant_salvar_views
from emensageriapro.s1200.views import s1200_infoperant_remunperant_api as s1200_infoperant_remunperant_api_views
from emensageriapro.s1200.views import s1200_infoperant_itensremun_apagar as s1200_infoperant_itensremun_apagar_views
from emensageriapro.s1200.views import s1200_infoperant_itensremun_listar as s1200_infoperant_itensremun_listar_views
from emensageriapro.s1200.views import s1200_infoperant_itensremun_salvar as s1200_infoperant_itensremun_salvar_views
from emensageriapro.s1200.views import s1200_infoperant_itensremun_api as s1200_infoperant_itensremun_api_views
from emensageriapro.s1200.views import s1200_infoperant_infoagnocivo_apagar as s1200_infoperant_infoagnocivo_apagar_views
from emensageriapro.s1200.views import s1200_infoperant_infoagnocivo_listar as s1200_infoperant_infoagnocivo_listar_views
from emensageriapro.s1200.views import s1200_infoperant_infoagnocivo_salvar as s1200_infoperant_infoagnocivo_salvar_views
from emensageriapro.s1200.views import s1200_infoperant_infoagnocivo_api as s1200_infoperant_infoagnocivo_api_views
from emensageriapro.s1200.views import s1200_infoperant_infotrabinterm_apagar as s1200_infoperant_infotrabinterm_apagar_views
from emensageriapro.s1200.views import s1200_infoperant_infotrabinterm_listar as s1200_infoperant_infotrabinterm_listar_views
from emensageriapro.s1200.views import s1200_infoperant_infotrabinterm_salvar as s1200_infoperant_infotrabinterm_salvar_views
from emensageriapro.s1200.views import s1200_infoperant_infotrabinterm_api as s1200_infoperant_infotrabinterm_api_views
from emensageriapro.s1200.views import s1200_infoperant_infocomplcont_apagar as s1200_infoperant_infocomplcont_apagar_views
from emensageriapro.s1200.views import s1200_infoperant_infocomplcont_listar as s1200_infoperant_infocomplcont_listar_views
from emensageriapro.s1200.views import s1200_infoperant_infocomplcont_salvar as s1200_infoperant_infocomplcont_salvar_views
from emensageriapro.s1200.views import s1200_infoperant_infocomplcont_api as s1200_infoperant_infocomplcont_api_views


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


    url(r'^s1200-infomv/apagar/(?P<pk>[0-9]+)/$',
        s1200_infomv_apagar_views.apagar,
        name='s1200_infomv_apagar'),

    url(r'^s1200-infomv/api/$',
        s1200_infomv_api_views.s1200infoMVList.as_view() ),

    url(r'^s1200-infomv/api/(?P<pk>[0-9]+)/$',
        s1200_infomv_api_views.s1200infoMVDetail.as_view() ),

    url(r'^s1200-infomv/$',
        s1200_infomv_listar_views.listar,
        name='s1200_infomv'),

    url(r'^s1200-infomv/salvar/(?P<pk>[0-9]+)/$',
        s1200_infomv_salvar_views.salvar,
        name='s1200_infomv_salvar'),

    url(r'^s1200-infomv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infomv_salvar_views.salvar,
        name='s1200_infomv_salvar_tab'),

    url(r'^s1200-infomv/cadastrar/$',
        s1200_infomv_salvar_views.salvar,
        name='s1200_infomv_cadastrar'),

    url(r'^s1200-infomv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infomv_salvar_views.salvar,
        name='s1200_infomv_salvar_output'),

    url(r'^s1200-infomv/(?P<output>[\w-]+)/$',
        s1200_infomv_listar_views.listar,
        name='s1200_infomv_output'),

    url(r'^s1200-remunoutrempr/apagar/(?P<pk>[0-9]+)/$',
        s1200_remunoutrempr_apagar_views.apagar,
        name='s1200_remunoutrempr_apagar'),

    url(r'^s1200-remunoutrempr/api/$',
        s1200_remunoutrempr_api_views.s1200remunOutrEmprList.as_view() ),

    url(r'^s1200-remunoutrempr/api/(?P<pk>[0-9]+)/$',
        s1200_remunoutrempr_api_views.s1200remunOutrEmprDetail.as_view() ),

    url(r'^s1200-remunoutrempr/$',
        s1200_remunoutrempr_listar_views.listar,
        name='s1200_remunoutrempr'),

    url(r'^s1200-remunoutrempr/salvar/(?P<pk>[0-9]+)/$',
        s1200_remunoutrempr_salvar_views.salvar,
        name='s1200_remunoutrempr_salvar'),

    url(r'^s1200-remunoutrempr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_remunoutrempr_salvar_views.salvar,
        name='s1200_remunoutrempr_salvar_tab'),

    url(r'^s1200-remunoutrempr/cadastrar/$',
        s1200_remunoutrempr_salvar_views.salvar,
        name='s1200_remunoutrempr_cadastrar'),

    url(r'^s1200-remunoutrempr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_remunoutrempr_salvar_views.salvar,
        name='s1200_remunoutrempr_salvar_output'),

    url(r'^s1200-remunoutrempr/(?P<output>[\w-]+)/$',
        s1200_remunoutrempr_listar_views.listar,
        name='s1200_remunoutrempr_output'),

    url(r'^s1200-infocomplem/apagar/(?P<pk>[0-9]+)/$',
        s1200_infocomplem_apagar_views.apagar,
        name='s1200_infocomplem_apagar'),

    url(r'^s1200-infocomplem/api/$',
        s1200_infocomplem_api_views.s1200infoComplemList.as_view() ),

    url(r'^s1200-infocomplem/api/(?P<pk>[0-9]+)/$',
        s1200_infocomplem_api_views.s1200infoComplemDetail.as_view() ),

    url(r'^s1200-infocomplem/$',
        s1200_infocomplem_listar_views.listar,
        name='s1200_infocomplem'),

    url(r'^s1200-infocomplem/salvar/(?P<pk>[0-9]+)/$',
        s1200_infocomplem_salvar_views.salvar,
        name='s1200_infocomplem_salvar'),

    url(r'^s1200-infocomplem/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infocomplem_salvar_views.salvar,
        name='s1200_infocomplem_salvar_tab'),

    url(r'^s1200-infocomplem/cadastrar/$',
        s1200_infocomplem_salvar_views.salvar,
        name='s1200_infocomplem_cadastrar'),

    url(r'^s1200-infocomplem/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infocomplem_salvar_views.salvar,
        name='s1200_infocomplem_salvar_output'),

    url(r'^s1200-infocomplem/(?P<output>[\w-]+)/$',
        s1200_infocomplem_listar_views.listar,
        name='s1200_infocomplem_output'),

    url(r'^s1200-sucessaovinc/apagar/(?P<pk>[0-9]+)/$',
        s1200_sucessaovinc_apagar_views.apagar,
        name='s1200_sucessaovinc_apagar'),

    url(r'^s1200-sucessaovinc/api/$',
        s1200_sucessaovinc_api_views.s1200sucessaoVincList.as_view() ),

    url(r'^s1200-sucessaovinc/api/(?P<pk>[0-9]+)/$',
        s1200_sucessaovinc_api_views.s1200sucessaoVincDetail.as_view() ),

    url(r'^s1200-sucessaovinc/$',
        s1200_sucessaovinc_listar_views.listar,
        name='s1200_sucessaovinc'),

    url(r'^s1200-sucessaovinc/salvar/(?P<pk>[0-9]+)/$',
        s1200_sucessaovinc_salvar_views.salvar,
        name='s1200_sucessaovinc_salvar'),

    url(r'^s1200-sucessaovinc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_sucessaovinc_salvar_views.salvar,
        name='s1200_sucessaovinc_salvar_tab'),

    url(r'^s1200-sucessaovinc/cadastrar/$',
        s1200_sucessaovinc_salvar_views.salvar,
        name='s1200_sucessaovinc_cadastrar'),

    url(r'^s1200-sucessaovinc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_sucessaovinc_salvar_views.salvar,
        name='s1200_sucessaovinc_salvar_output'),

    url(r'^s1200-sucessaovinc/(?P<output>[\w-]+)/$',
        s1200_sucessaovinc_listar_views.listar,
        name='s1200_sucessaovinc_output'),

    url(r'^s1200-procjudtrab/apagar/(?P<pk>[0-9]+)/$',
        s1200_procjudtrab_apagar_views.apagar,
        name='s1200_procjudtrab_apagar'),

    url(r'^s1200-procjudtrab/api/$',
        s1200_procjudtrab_api_views.s1200procJudTrabList.as_view() ),

    url(r'^s1200-procjudtrab/api/(?P<pk>[0-9]+)/$',
        s1200_procjudtrab_api_views.s1200procJudTrabDetail.as_view() ),

    url(r'^s1200-procjudtrab/$',
        s1200_procjudtrab_listar_views.listar,
        name='s1200_procjudtrab'),

    url(r'^s1200-procjudtrab/salvar/(?P<pk>[0-9]+)/$',
        s1200_procjudtrab_salvar_views.salvar,
        name='s1200_procjudtrab_salvar'),

    url(r'^s1200-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_procjudtrab_salvar_views.salvar,
        name='s1200_procjudtrab_salvar_tab'),

    url(r'^s1200-procjudtrab/cadastrar/$',
        s1200_procjudtrab_salvar_views.salvar,
        name='s1200_procjudtrab_cadastrar'),

    url(r'^s1200-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_procjudtrab_salvar_views.salvar,
        name='s1200_procjudtrab_salvar_output'),

    url(r'^s1200-procjudtrab/(?P<output>[\w-]+)/$',
        s1200_procjudtrab_listar_views.listar,
        name='s1200_procjudtrab_output'),

    url(r'^s1200-infointerm/apagar/(?P<pk>[0-9]+)/$',
        s1200_infointerm_apagar_views.apagar,
        name='s1200_infointerm_apagar'),

    url(r'^s1200-infointerm/api/$',
        s1200_infointerm_api_views.s1200infoIntermList.as_view() ),

    url(r'^s1200-infointerm/api/(?P<pk>[0-9]+)/$',
        s1200_infointerm_api_views.s1200infoIntermDetail.as_view() ),

    url(r'^s1200-infointerm/$',
        s1200_infointerm_listar_views.listar,
        name='s1200_infointerm'),

    url(r'^s1200-infointerm/salvar/(?P<pk>[0-9]+)/$',
        s1200_infointerm_salvar_views.salvar,
        name='s1200_infointerm_salvar'),

    url(r'^s1200-infointerm/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infointerm_salvar_views.salvar,
        name='s1200_infointerm_salvar_tab'),

    url(r'^s1200-infointerm/cadastrar/$',
        s1200_infointerm_salvar_views.salvar,
        name='s1200_infointerm_cadastrar'),

    url(r'^s1200-infointerm/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infointerm_salvar_views.salvar,
        name='s1200_infointerm_salvar_output'),

    url(r'^s1200-infointerm/(?P<output>[\w-]+)/$',
        s1200_infointerm_listar_views.listar,
        name='s1200_infointerm_output'),

    url(r'^s1200-dmdev/apagar/(?P<pk>[0-9]+)/$',
        s1200_dmdev_apagar_views.apagar,
        name='s1200_dmdev_apagar'),

    url(r'^s1200-dmdev/api/$',
        s1200_dmdev_api_views.s1200dmDevList.as_view() ),

    url(r'^s1200-dmdev/api/(?P<pk>[0-9]+)/$',
        s1200_dmdev_api_views.s1200dmDevDetail.as_view() ),

    url(r'^s1200-dmdev/$',
        s1200_dmdev_listar_views.listar,
        name='s1200_dmdev'),

    url(r'^s1200-dmdev/salvar/(?P<pk>[0-9]+)/$',
        s1200_dmdev_salvar_views.salvar,
        name='s1200_dmdev_salvar'),

    url(r'^s1200-dmdev/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_dmdev_salvar_views.salvar,
        name='s1200_dmdev_salvar_tab'),

    url(r'^s1200-dmdev/cadastrar/$',
        s1200_dmdev_salvar_views.salvar,
        name='s1200_dmdev_cadastrar'),

    url(r'^s1200-dmdev/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_dmdev_salvar_views.salvar,
        name='s1200_dmdev_salvar_output'),

    url(r'^s1200-dmdev/(?P<output>[\w-]+)/$',
        s1200_dmdev_listar_views.listar,
        name='s1200_dmdev_output'),

    url(r'^s1200-infoperapur/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_apagar_views.apagar,
        name='s1200_infoperapur_apagar'),

    url(r'^s1200-infoperapur/api/$',
        s1200_infoperapur_api_views.s1200infoPerApurList.as_view() ),

    url(r'^s1200-infoperapur/api/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_api_views.s1200infoPerApurDetail.as_view() ),

    url(r'^s1200-infoperapur/$',
        s1200_infoperapur_listar_views.listar,
        name='s1200_infoperapur'),

    url(r'^s1200-infoperapur/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_salvar_views.salvar,
        name='s1200_infoperapur_salvar'),

    url(r'^s1200-infoperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperapur_salvar_views.salvar,
        name='s1200_infoperapur_salvar_tab'),

    url(r'^s1200-infoperapur/cadastrar/$',
        s1200_infoperapur_salvar_views.salvar,
        name='s1200_infoperapur_cadastrar'),

    url(r'^s1200-infoperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperapur_salvar_views.salvar,
        name='s1200_infoperapur_salvar_output'),

    url(r'^s1200-infoperapur/(?P<output>[\w-]+)/$',
        s1200_infoperapur_listar_views.listar,
        name='s1200_infoperapur_output'),

    url(r'^s1200-infoperapur-ideestablot/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_ideestablot_apagar_views.apagar,
        name='s1200_infoperapur_ideestablot_apagar'),

    url(r'^s1200-infoperapur-ideestablot/api/$',
        s1200_infoperapur_ideestablot_api_views.s1200infoPerApurideEstabLotList.as_view() ),

    url(r'^s1200-infoperapur-ideestablot/api/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_ideestablot_api_views.s1200infoPerApurideEstabLotDetail.as_view() ),

    url(r'^s1200-infoperapur-ideestablot/$',
        s1200_infoperapur_ideestablot_listar_views.listar,
        name='s1200_infoperapur_ideestablot'),

    url(r'^s1200-infoperapur-ideestablot/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_ideestablot_salvar_views.salvar,
        name='s1200_infoperapur_ideestablot_salvar'),

    url(r'^s1200-infoperapur-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperapur_ideestablot_salvar_views.salvar,
        name='s1200_infoperapur_ideestablot_salvar_tab'),

    url(r'^s1200-infoperapur-ideestablot/cadastrar/$',
        s1200_infoperapur_ideestablot_salvar_views.salvar,
        name='s1200_infoperapur_ideestablot_cadastrar'),

    url(r'^s1200-infoperapur-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperapur_ideestablot_salvar_views.salvar,
        name='s1200_infoperapur_ideestablot_salvar_output'),

    url(r'^s1200-infoperapur-ideestablot/(?P<output>[\w-]+)/$',
        s1200_infoperapur_ideestablot_listar_views.listar,
        name='s1200_infoperapur_ideestablot_output'),

    url(r'^s1200-infoperapur-remunperapur/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_remunperapur_apagar_views.apagar,
        name='s1200_infoperapur_remunperapur_apagar'),

    url(r'^s1200-infoperapur-remunperapur/api/$',
        s1200_infoperapur_remunperapur_api_views.s1200infoPerApurremunPerApurList.as_view() ),

    url(r'^s1200-infoperapur-remunperapur/api/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_remunperapur_api_views.s1200infoPerApurremunPerApurDetail.as_view() ),

    url(r'^s1200-infoperapur-remunperapur/$',
        s1200_infoperapur_remunperapur_listar_views.listar,
        name='s1200_infoperapur_remunperapur'),

    url(r'^s1200-infoperapur-remunperapur/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_remunperapur_salvar_views.salvar,
        name='s1200_infoperapur_remunperapur_salvar'),

    url(r'^s1200-infoperapur-remunperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperapur_remunperapur_salvar_views.salvar,
        name='s1200_infoperapur_remunperapur_salvar_tab'),

    url(r'^s1200-infoperapur-remunperapur/cadastrar/$',
        s1200_infoperapur_remunperapur_salvar_views.salvar,
        name='s1200_infoperapur_remunperapur_cadastrar'),

    url(r'^s1200-infoperapur-remunperapur/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperapur_remunperapur_salvar_views.salvar,
        name='s1200_infoperapur_remunperapur_salvar_output'),

    url(r'^s1200-infoperapur-remunperapur/(?P<output>[\w-]+)/$',
        s1200_infoperapur_remunperapur_listar_views.listar,
        name='s1200_infoperapur_remunperapur_output'),

    url(r'^s1200-infoperapur-itensremun/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_itensremun_apagar_views.apagar,
        name='s1200_infoperapur_itensremun_apagar'),

    url(r'^s1200-infoperapur-itensremun/api/$',
        s1200_infoperapur_itensremun_api_views.s1200infoPerApuritensRemunList.as_view() ),

    url(r'^s1200-infoperapur-itensremun/api/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_itensremun_api_views.s1200infoPerApuritensRemunDetail.as_view() ),

    url(r'^s1200-infoperapur-itensremun/$',
        s1200_infoperapur_itensremun_listar_views.listar,
        name='s1200_infoperapur_itensremun'),

    url(r'^s1200-infoperapur-itensremun/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_itensremun_salvar_views.salvar,
        name='s1200_infoperapur_itensremun_salvar'),

    url(r'^s1200-infoperapur-itensremun/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperapur_itensremun_salvar_views.salvar,
        name='s1200_infoperapur_itensremun_salvar_tab'),

    url(r'^s1200-infoperapur-itensremun/cadastrar/$',
        s1200_infoperapur_itensremun_salvar_views.salvar,
        name='s1200_infoperapur_itensremun_cadastrar'),

    url(r'^s1200-infoperapur-itensremun/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperapur_itensremun_salvar_views.salvar,
        name='s1200_infoperapur_itensremun_salvar_output'),

    url(r'^s1200-infoperapur-itensremun/(?P<output>[\w-]+)/$',
        s1200_infoperapur_itensremun_listar_views.listar,
        name='s1200_infoperapur_itensremun_output'),

    url(r'^s1200-infoperapur-infosaudecolet/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_infosaudecolet_apagar_views.apagar,
        name='s1200_infoperapur_infosaudecolet_apagar'),

    url(r'^s1200-infoperapur-infosaudecolet/api/$',
        s1200_infoperapur_infosaudecolet_api_views.s1200infoPerApurinfoSaudeColetList.as_view() ),

    url(r'^s1200-infoperapur-infosaudecolet/api/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_infosaudecolet_api_views.s1200infoPerApurinfoSaudeColetDetail.as_view() ),

    url(r'^s1200-infoperapur-infosaudecolet/$',
        s1200_infoperapur_infosaudecolet_listar_views.listar,
        name='s1200_infoperapur_infosaudecolet'),

    url(r'^s1200-infoperapur-infosaudecolet/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s1200_infoperapur_infosaudecolet_salvar'),

    url(r'^s1200-infoperapur-infosaudecolet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s1200_infoperapur_infosaudecolet_salvar_tab'),

    url(r'^s1200-infoperapur-infosaudecolet/cadastrar/$',
        s1200_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s1200_infoperapur_infosaudecolet_cadastrar'),

    url(r'^s1200-infoperapur-infosaudecolet/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperapur_infosaudecolet_salvar_views.salvar,
        name='s1200_infoperapur_infosaudecolet_salvar_output'),

    url(r'^s1200-infoperapur-infosaudecolet/(?P<output>[\w-]+)/$',
        s1200_infoperapur_infosaudecolet_listar_views.listar,
        name='s1200_infoperapur_infosaudecolet_output'),

    url(r'^s1200-infoperapur-detoper/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_detoper_apagar_views.apagar,
        name='s1200_infoperapur_detoper_apagar'),

    url(r'^s1200-infoperapur-detoper/api/$',
        s1200_infoperapur_detoper_api_views.s1200infoPerApurdetOperList.as_view() ),

    url(r'^s1200-infoperapur-detoper/api/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_detoper_api_views.s1200infoPerApurdetOperDetail.as_view() ),

    url(r'^s1200-infoperapur-detoper/$',
        s1200_infoperapur_detoper_listar_views.listar,
        name='s1200_infoperapur_detoper'),

    url(r'^s1200-infoperapur-detoper/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_detoper_salvar_views.salvar,
        name='s1200_infoperapur_detoper_salvar'),

    url(r'^s1200-infoperapur-detoper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperapur_detoper_salvar_views.salvar,
        name='s1200_infoperapur_detoper_salvar_tab'),

    url(r'^s1200-infoperapur-detoper/cadastrar/$',
        s1200_infoperapur_detoper_salvar_views.salvar,
        name='s1200_infoperapur_detoper_cadastrar'),

    url(r'^s1200-infoperapur-detoper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperapur_detoper_salvar_views.salvar,
        name='s1200_infoperapur_detoper_salvar_output'),

    url(r'^s1200-infoperapur-detoper/(?P<output>[\w-]+)/$',
        s1200_infoperapur_detoper_listar_views.listar,
        name='s1200_infoperapur_detoper_output'),

    url(r'^s1200-infoperapur-detplano/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_detplano_apagar_views.apagar,
        name='s1200_infoperapur_detplano_apagar'),

    url(r'^s1200-infoperapur-detplano/api/$',
        s1200_infoperapur_detplano_api_views.s1200infoPerApurdetPlanoList.as_view() ),

    url(r'^s1200-infoperapur-detplano/api/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_detplano_api_views.s1200infoPerApurdetPlanoDetail.as_view() ),

    url(r'^s1200-infoperapur-detplano/$',
        s1200_infoperapur_detplano_listar_views.listar,
        name='s1200_infoperapur_detplano'),

    url(r'^s1200-infoperapur-detplano/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_detplano_salvar_views.salvar,
        name='s1200_infoperapur_detplano_salvar'),

    url(r'^s1200-infoperapur-detplano/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperapur_detplano_salvar_views.salvar,
        name='s1200_infoperapur_detplano_salvar_tab'),

    url(r'^s1200-infoperapur-detplano/cadastrar/$',
        s1200_infoperapur_detplano_salvar_views.salvar,
        name='s1200_infoperapur_detplano_cadastrar'),

    url(r'^s1200-infoperapur-detplano/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperapur_detplano_salvar_views.salvar,
        name='s1200_infoperapur_detplano_salvar_output'),

    url(r'^s1200-infoperapur-detplano/(?P<output>[\w-]+)/$',
        s1200_infoperapur_detplano_listar_views.listar,
        name='s1200_infoperapur_detplano_output'),

    url(r'^s1200-infoperapur-infoagnocivo/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_infoagnocivo_apagar_views.apagar,
        name='s1200_infoperapur_infoagnocivo_apagar'),

    url(r'^s1200-infoperapur-infoagnocivo/api/$',
        s1200_infoperapur_infoagnocivo_api_views.s1200infoPerApurinfoAgNocivoList.as_view() ),

    url(r'^s1200-infoperapur-infoagnocivo/api/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_infoagnocivo_api_views.s1200infoPerApurinfoAgNocivoDetail.as_view() ),

    url(r'^s1200-infoperapur-infoagnocivo/$',
        s1200_infoperapur_infoagnocivo_listar_views.listar,
        name='s1200_infoperapur_infoagnocivo'),

    url(r'^s1200-infoperapur-infoagnocivo/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_infoagnocivo_salvar_views.salvar,
        name='s1200_infoperapur_infoagnocivo_salvar'),

    url(r'^s1200-infoperapur-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperapur_infoagnocivo_salvar_views.salvar,
        name='s1200_infoperapur_infoagnocivo_salvar_tab'),

    url(r'^s1200-infoperapur-infoagnocivo/cadastrar/$',
        s1200_infoperapur_infoagnocivo_salvar_views.salvar,
        name='s1200_infoperapur_infoagnocivo_cadastrar'),

    url(r'^s1200-infoperapur-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperapur_infoagnocivo_salvar_views.salvar,
        name='s1200_infoperapur_infoagnocivo_salvar_output'),

    url(r'^s1200-infoperapur-infoagnocivo/(?P<output>[\w-]+)/$',
        s1200_infoperapur_infoagnocivo_listar_views.listar,
        name='s1200_infoperapur_infoagnocivo_output'),

    url(r'^s1200-infoperapur-infotrabinterm/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_infotrabinterm_apagar_views.apagar,
        name='s1200_infoperapur_infotrabinterm_apagar'),

    url(r'^s1200-infoperapur-infotrabinterm/api/$',
        s1200_infoperapur_infotrabinterm_api_views.s1200infoPerApurinfoTrabIntermList.as_view() ),

    url(r'^s1200-infoperapur-infotrabinterm/api/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_infotrabinterm_api_views.s1200infoPerApurinfoTrabIntermDetail.as_view() ),

    url(r'^s1200-infoperapur-infotrabinterm/$',
        s1200_infoperapur_infotrabinterm_listar_views.listar,
        name='s1200_infoperapur_infotrabinterm'),

    url(r'^s1200-infoperapur-infotrabinterm/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperapur_infotrabinterm_salvar_views.salvar,
        name='s1200_infoperapur_infotrabinterm_salvar'),

    url(r'^s1200-infoperapur-infotrabinterm/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperapur_infotrabinterm_salvar_views.salvar,
        name='s1200_infoperapur_infotrabinterm_salvar_tab'),

    url(r'^s1200-infoperapur-infotrabinterm/cadastrar/$',
        s1200_infoperapur_infotrabinterm_salvar_views.salvar,
        name='s1200_infoperapur_infotrabinterm_cadastrar'),

    url(r'^s1200-infoperapur-infotrabinterm/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperapur_infotrabinterm_salvar_views.salvar,
        name='s1200_infoperapur_infotrabinterm_salvar_output'),

    url(r'^s1200-infoperapur-infotrabinterm/(?P<output>[\w-]+)/$',
        s1200_infoperapur_infotrabinterm_listar_views.listar,
        name='s1200_infoperapur_infotrabinterm_output'),

    url(r'^s1200-infoperant/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_apagar_views.apagar,
        name='s1200_infoperant_apagar'),

    url(r'^s1200-infoperant/api/$',
        s1200_infoperant_api_views.s1200infoPerAntList.as_view() ),

    url(r'^s1200-infoperant/api/(?P<pk>[0-9]+)/$',
        s1200_infoperant_api_views.s1200infoPerAntDetail.as_view() ),

    url(r'^s1200-infoperant/$',
        s1200_infoperant_listar_views.listar,
        name='s1200_infoperant'),

    url(r'^s1200-infoperant/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_salvar_views.salvar,
        name='s1200_infoperant_salvar'),

    url(r'^s1200-infoperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperant_salvar_views.salvar,
        name='s1200_infoperant_salvar_tab'),

    url(r'^s1200-infoperant/cadastrar/$',
        s1200_infoperant_salvar_views.salvar,
        name='s1200_infoperant_cadastrar'),

    url(r'^s1200-infoperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperant_salvar_views.salvar,
        name='s1200_infoperant_salvar_output'),

    url(r'^s1200-infoperant/(?P<output>[\w-]+)/$',
        s1200_infoperant_listar_views.listar,
        name='s1200_infoperant_output'),

    url(r'^s1200-infoperant-ideadc/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_ideadc_apagar_views.apagar,
        name='s1200_infoperant_ideadc_apagar'),

    url(r'^s1200-infoperant-ideadc/api/$',
        s1200_infoperant_ideadc_api_views.s1200infoPerAntideADCList.as_view() ),

    url(r'^s1200-infoperant-ideadc/api/(?P<pk>[0-9]+)/$',
        s1200_infoperant_ideadc_api_views.s1200infoPerAntideADCDetail.as_view() ),

    url(r'^s1200-infoperant-ideadc/$',
        s1200_infoperant_ideadc_listar_views.listar,
        name='s1200_infoperant_ideadc'),

    url(r'^s1200-infoperant-ideadc/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_ideadc_salvar_views.salvar,
        name='s1200_infoperant_ideadc_salvar'),

    url(r'^s1200-infoperant-ideadc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperant_ideadc_salvar_views.salvar,
        name='s1200_infoperant_ideadc_salvar_tab'),

    url(r'^s1200-infoperant-ideadc/cadastrar/$',
        s1200_infoperant_ideadc_salvar_views.salvar,
        name='s1200_infoperant_ideadc_cadastrar'),

    url(r'^s1200-infoperant-ideadc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperant_ideadc_salvar_views.salvar,
        name='s1200_infoperant_ideadc_salvar_output'),

    url(r'^s1200-infoperant-ideadc/(?P<output>[\w-]+)/$',
        s1200_infoperant_ideadc_listar_views.listar,
        name='s1200_infoperant_ideadc_output'),

    url(r'^s1200-infoperant-ideperiodo/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_ideperiodo_apagar_views.apagar,
        name='s1200_infoperant_ideperiodo_apagar'),

    url(r'^s1200-infoperant-ideperiodo/api/$',
        s1200_infoperant_ideperiodo_api_views.s1200infoPerAntidePeriodoList.as_view() ),

    url(r'^s1200-infoperant-ideperiodo/api/(?P<pk>[0-9]+)/$',
        s1200_infoperant_ideperiodo_api_views.s1200infoPerAntidePeriodoDetail.as_view() ),

    url(r'^s1200-infoperant-ideperiodo/$',
        s1200_infoperant_ideperiodo_listar_views.listar,
        name='s1200_infoperant_ideperiodo'),

    url(r'^s1200-infoperant-ideperiodo/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_ideperiodo_salvar_views.salvar,
        name='s1200_infoperant_ideperiodo_salvar'),

    url(r'^s1200-infoperant-ideperiodo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperant_ideperiodo_salvar_views.salvar,
        name='s1200_infoperant_ideperiodo_salvar_tab'),

    url(r'^s1200-infoperant-ideperiodo/cadastrar/$',
        s1200_infoperant_ideperiodo_salvar_views.salvar,
        name='s1200_infoperant_ideperiodo_cadastrar'),

    url(r'^s1200-infoperant-ideperiodo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperant_ideperiodo_salvar_views.salvar,
        name='s1200_infoperant_ideperiodo_salvar_output'),

    url(r'^s1200-infoperant-ideperiodo/(?P<output>[\w-]+)/$',
        s1200_infoperant_ideperiodo_listar_views.listar,
        name='s1200_infoperant_ideperiodo_output'),

    url(r'^s1200-infoperant-ideestablot/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_ideestablot_apagar_views.apagar,
        name='s1200_infoperant_ideestablot_apagar'),

    url(r'^s1200-infoperant-ideestablot/api/$',
        s1200_infoperant_ideestablot_api_views.s1200infoPerAntideEstabLotList.as_view() ),

    url(r'^s1200-infoperant-ideestablot/api/(?P<pk>[0-9]+)/$',
        s1200_infoperant_ideestablot_api_views.s1200infoPerAntideEstabLotDetail.as_view() ),

    url(r'^s1200-infoperant-ideestablot/$',
        s1200_infoperant_ideestablot_listar_views.listar,
        name='s1200_infoperant_ideestablot'),

    url(r'^s1200-infoperant-ideestablot/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_ideestablot_salvar_views.salvar,
        name='s1200_infoperant_ideestablot_salvar'),

    url(r'^s1200-infoperant-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperant_ideestablot_salvar_views.salvar,
        name='s1200_infoperant_ideestablot_salvar_tab'),

    url(r'^s1200-infoperant-ideestablot/cadastrar/$',
        s1200_infoperant_ideestablot_salvar_views.salvar,
        name='s1200_infoperant_ideestablot_cadastrar'),

    url(r'^s1200-infoperant-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperant_ideestablot_salvar_views.salvar,
        name='s1200_infoperant_ideestablot_salvar_output'),

    url(r'^s1200-infoperant-ideestablot/(?P<output>[\w-]+)/$',
        s1200_infoperant_ideestablot_listar_views.listar,
        name='s1200_infoperant_ideestablot_output'),

    url(r'^s1200-infoperant-remunperant/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_remunperant_apagar_views.apagar,
        name='s1200_infoperant_remunperant_apagar'),

    url(r'^s1200-infoperant-remunperant/api/$',
        s1200_infoperant_remunperant_api_views.s1200infoPerAntremunPerAntList.as_view() ),

    url(r'^s1200-infoperant-remunperant/api/(?P<pk>[0-9]+)/$',
        s1200_infoperant_remunperant_api_views.s1200infoPerAntremunPerAntDetail.as_view() ),

    url(r'^s1200-infoperant-remunperant/$',
        s1200_infoperant_remunperant_listar_views.listar,
        name='s1200_infoperant_remunperant'),

    url(r'^s1200-infoperant-remunperant/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_remunperant_salvar_views.salvar,
        name='s1200_infoperant_remunperant_salvar'),

    url(r'^s1200-infoperant-remunperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperant_remunperant_salvar_views.salvar,
        name='s1200_infoperant_remunperant_salvar_tab'),

    url(r'^s1200-infoperant-remunperant/cadastrar/$',
        s1200_infoperant_remunperant_salvar_views.salvar,
        name='s1200_infoperant_remunperant_cadastrar'),

    url(r'^s1200-infoperant-remunperant/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperant_remunperant_salvar_views.salvar,
        name='s1200_infoperant_remunperant_salvar_output'),

    url(r'^s1200-infoperant-remunperant/(?P<output>[\w-]+)/$',
        s1200_infoperant_remunperant_listar_views.listar,
        name='s1200_infoperant_remunperant_output'),

    url(r'^s1200-infoperant-itensremun/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_itensremun_apagar_views.apagar,
        name='s1200_infoperant_itensremun_apagar'),

    url(r'^s1200-infoperant-itensremun/api/$',
        s1200_infoperant_itensremun_api_views.s1200infoPerAntitensRemunList.as_view() ),

    url(r'^s1200-infoperant-itensremun/api/(?P<pk>[0-9]+)/$',
        s1200_infoperant_itensremun_api_views.s1200infoPerAntitensRemunDetail.as_view() ),

    url(r'^s1200-infoperant-itensremun/$',
        s1200_infoperant_itensremun_listar_views.listar,
        name='s1200_infoperant_itensremun'),

    url(r'^s1200-infoperant-itensremun/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_itensremun_salvar_views.salvar,
        name='s1200_infoperant_itensremun_salvar'),

    url(r'^s1200-infoperant-itensremun/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperant_itensremun_salvar_views.salvar,
        name='s1200_infoperant_itensremun_salvar_tab'),

    url(r'^s1200-infoperant-itensremun/cadastrar/$',
        s1200_infoperant_itensremun_salvar_views.salvar,
        name='s1200_infoperant_itensremun_cadastrar'),

    url(r'^s1200-infoperant-itensremun/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperant_itensremun_salvar_views.salvar,
        name='s1200_infoperant_itensremun_salvar_output'),

    url(r'^s1200-infoperant-itensremun/(?P<output>[\w-]+)/$',
        s1200_infoperant_itensremun_listar_views.listar,
        name='s1200_infoperant_itensremun_output'),

    url(r'^s1200-infoperant-infoagnocivo/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_infoagnocivo_apagar_views.apagar,
        name='s1200_infoperant_infoagnocivo_apagar'),

    url(r'^s1200-infoperant-infoagnocivo/api/$',
        s1200_infoperant_infoagnocivo_api_views.s1200infoPerAntinfoAgNocivoList.as_view() ),

    url(r'^s1200-infoperant-infoagnocivo/api/(?P<pk>[0-9]+)/$',
        s1200_infoperant_infoagnocivo_api_views.s1200infoPerAntinfoAgNocivoDetail.as_view() ),

    url(r'^s1200-infoperant-infoagnocivo/$',
        s1200_infoperant_infoagnocivo_listar_views.listar,
        name='s1200_infoperant_infoagnocivo'),

    url(r'^s1200-infoperant-infoagnocivo/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_infoagnocivo_salvar_views.salvar,
        name='s1200_infoperant_infoagnocivo_salvar'),

    url(r'^s1200-infoperant-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperant_infoagnocivo_salvar_views.salvar,
        name='s1200_infoperant_infoagnocivo_salvar_tab'),

    url(r'^s1200-infoperant-infoagnocivo/cadastrar/$',
        s1200_infoperant_infoagnocivo_salvar_views.salvar,
        name='s1200_infoperant_infoagnocivo_cadastrar'),

    url(r'^s1200-infoperant-infoagnocivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperant_infoagnocivo_salvar_views.salvar,
        name='s1200_infoperant_infoagnocivo_salvar_output'),

    url(r'^s1200-infoperant-infoagnocivo/(?P<output>[\w-]+)/$',
        s1200_infoperant_infoagnocivo_listar_views.listar,
        name='s1200_infoperant_infoagnocivo_output'),

    url(r'^s1200-infoperant-infotrabinterm/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_infotrabinterm_apagar_views.apagar,
        name='s1200_infoperant_infotrabinterm_apagar'),

    url(r'^s1200-infoperant-infotrabinterm/api/$',
        s1200_infoperant_infotrabinterm_api_views.s1200infoPerAntinfoTrabIntermList.as_view() ),

    url(r'^s1200-infoperant-infotrabinterm/api/(?P<pk>[0-9]+)/$',
        s1200_infoperant_infotrabinterm_api_views.s1200infoPerAntinfoTrabIntermDetail.as_view() ),

    url(r'^s1200-infoperant-infotrabinterm/$',
        s1200_infoperant_infotrabinterm_listar_views.listar,
        name='s1200_infoperant_infotrabinterm'),

    url(r'^s1200-infoperant-infotrabinterm/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_infotrabinterm_salvar_views.salvar,
        name='s1200_infoperant_infotrabinterm_salvar'),

    url(r'^s1200-infoperant-infotrabinterm/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperant_infotrabinterm_salvar_views.salvar,
        name='s1200_infoperant_infotrabinterm_salvar_tab'),

    url(r'^s1200-infoperant-infotrabinterm/cadastrar/$',
        s1200_infoperant_infotrabinterm_salvar_views.salvar,
        name='s1200_infoperant_infotrabinterm_cadastrar'),

    url(r'^s1200-infoperant-infotrabinterm/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperant_infotrabinterm_salvar_views.salvar,
        name='s1200_infoperant_infotrabinterm_salvar_output'),

    url(r'^s1200-infoperant-infotrabinterm/(?P<output>[\w-]+)/$',
        s1200_infoperant_infotrabinterm_listar_views.listar,
        name='s1200_infoperant_infotrabinterm_output'),

    url(r'^s1200-infoperant-infocomplcont/apagar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_infocomplcont_apagar_views.apagar,
        name='s1200_infoperant_infocomplcont_apagar'),

    url(r'^s1200-infoperant-infocomplcont/api/$',
        s1200_infoperant_infocomplcont_api_views.s1200infoPerAntinfoComplContList.as_view() ),

    url(r'^s1200-infoperant-infocomplcont/api/(?P<pk>[0-9]+)/$',
        s1200_infoperant_infocomplcont_api_views.s1200infoPerAntinfoComplContDetail.as_view() ),

    url(r'^s1200-infoperant-infocomplcont/$',
        s1200_infoperant_infocomplcont_listar_views.listar,
        name='s1200_infoperant_infocomplcont'),

    url(r'^s1200-infoperant-infocomplcont/salvar/(?P<pk>[0-9]+)/$',
        s1200_infoperant_infocomplcont_salvar_views.salvar,
        name='s1200_infoperant_infocomplcont_salvar'),

    url(r'^s1200-infoperant-infocomplcont/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1200_infoperant_infocomplcont_salvar_views.salvar,
        name='s1200_infoperant_infocomplcont_salvar_tab'),

    url(r'^s1200-infoperant-infocomplcont/cadastrar/$',
        s1200_infoperant_infocomplcont_salvar_views.salvar,
        name='s1200_infoperant_infocomplcont_cadastrar'),

    url(r'^s1200-infoperant-infocomplcont/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1200_infoperant_infocomplcont_salvar_views.salvar,
        name='s1200_infoperant_infocomplcont_salvar_output'),

    url(r'^s1200-infoperant-infocomplcont/(?P<output>[\w-]+)/$',
        s1200_infoperant_infocomplcont_listar_views.listar,
        name='s1200_infoperant_infocomplcont_output'),


]