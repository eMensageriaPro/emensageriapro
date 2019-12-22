# eMensageriaAI #
#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2240.views import s2240_iniexprisco_infoamb_apagar as s2240_iniexprisco_infoamb_apagar_views
from emensageriapro.s2240.views import s2240_iniexprisco_infoamb_listar as s2240_iniexprisco_infoamb_listar_views
from emensageriapro.s2240.views import s2240_iniexprisco_infoamb_salvar as s2240_iniexprisco_infoamb_salvar_views
from emensageriapro.s2240.views import s2240_iniexprisco_infoamb_api as s2240_iniexprisco_infoamb_api_views
from emensageriapro.s2240.views import s2240_iniexprisco_ativpericinsal_apagar as s2240_iniexprisco_ativpericinsal_apagar_views
from emensageriapro.s2240.views import s2240_iniexprisco_ativpericinsal_listar as s2240_iniexprisco_ativpericinsal_listar_views
from emensageriapro.s2240.views import s2240_iniexprisco_ativpericinsal_salvar as s2240_iniexprisco_ativpericinsal_salvar_views
from emensageriapro.s2240.views import s2240_iniexprisco_ativpericinsal_api as s2240_iniexprisco_ativpericinsal_api_views
from emensageriapro.s2240.views import s2240_iniexprisco_fatrisco_apagar as s2240_iniexprisco_fatrisco_apagar_views
from emensageriapro.s2240.views import s2240_iniexprisco_fatrisco_listar as s2240_iniexprisco_fatrisco_listar_views
from emensageriapro.s2240.views import s2240_iniexprisco_fatrisco_salvar as s2240_iniexprisco_fatrisco_salvar_views
from emensageriapro.s2240.views import s2240_iniexprisco_fatrisco_api as s2240_iniexprisco_fatrisco_api_views
from emensageriapro.s2240.views import s2240_iniexprisco_epc_apagar as s2240_iniexprisco_epc_apagar_views
from emensageriapro.s2240.views import s2240_iniexprisco_epc_listar as s2240_iniexprisco_epc_listar_views
from emensageriapro.s2240.views import s2240_iniexprisco_epc_salvar as s2240_iniexprisco_epc_salvar_views
from emensageriapro.s2240.views import s2240_iniexprisco_epc_api as s2240_iniexprisco_epc_api_views
from emensageriapro.s2240.views import s2240_iniexprisco_epi_apagar as s2240_iniexprisco_epi_apagar_views
from emensageriapro.s2240.views import s2240_iniexprisco_epi_listar as s2240_iniexprisco_epi_listar_views
from emensageriapro.s2240.views import s2240_iniexprisco_epi_salvar as s2240_iniexprisco_epi_salvar_views
from emensageriapro.s2240.views import s2240_iniexprisco_epi_api as s2240_iniexprisco_epi_api_views
from emensageriapro.s2240.views import s2240_iniexprisco_respreg_apagar as s2240_iniexprisco_respreg_apagar_views
from emensageriapro.s2240.views import s2240_iniexprisco_respreg_listar as s2240_iniexprisco_respreg_listar_views
from emensageriapro.s2240.views import s2240_iniexprisco_respreg_salvar as s2240_iniexprisco_respreg_salvar_views
from emensageriapro.s2240.views import s2240_iniexprisco_respreg_api as s2240_iniexprisco_respreg_api_views
from emensageriapro.s2240.views import s2240_iniexprisco_obs_apagar as s2240_iniexprisco_obs_apagar_views
from emensageriapro.s2240.views import s2240_iniexprisco_obs_listar as s2240_iniexprisco_obs_listar_views
from emensageriapro.s2240.views import s2240_iniexprisco_obs_salvar as s2240_iniexprisco_obs_salvar_views
from emensageriapro.s2240.views import s2240_iniexprisco_obs_api as s2240_iniexprisco_obs_api_views
from emensageriapro.s2240.views import s2240_altexprisco_apagar as s2240_altexprisco_apagar_views
from emensageriapro.s2240.views import s2240_altexprisco_listar as s2240_altexprisco_listar_views
from emensageriapro.s2240.views import s2240_altexprisco_salvar as s2240_altexprisco_salvar_views
from emensageriapro.s2240.views import s2240_altexprisco_api as s2240_altexprisco_api_views
from emensageriapro.s2240.views import s2240_altexprisco_infoamb_apagar as s2240_altexprisco_infoamb_apagar_views
from emensageriapro.s2240.views import s2240_altexprisco_infoamb_listar as s2240_altexprisco_infoamb_listar_views
from emensageriapro.s2240.views import s2240_altexprisco_infoamb_salvar as s2240_altexprisco_infoamb_salvar_views
from emensageriapro.s2240.views import s2240_altexprisco_infoamb_api as s2240_altexprisco_infoamb_api_views
from emensageriapro.s2240.views import s2240_altexprisco_fatrisco_apagar as s2240_altexprisco_fatrisco_apagar_views
from emensageriapro.s2240.views import s2240_altexprisco_fatrisco_listar as s2240_altexprisco_fatrisco_listar_views
from emensageriapro.s2240.views import s2240_altexprisco_fatrisco_salvar as s2240_altexprisco_fatrisco_salvar_views
from emensageriapro.s2240.views import s2240_altexprisco_fatrisco_api as s2240_altexprisco_fatrisco_api_views
from emensageriapro.s2240.views import s2240_altexprisco_epc_apagar as s2240_altexprisco_epc_apagar_views
from emensageriapro.s2240.views import s2240_altexprisco_epc_listar as s2240_altexprisco_epc_listar_views
from emensageriapro.s2240.views import s2240_altexprisco_epc_salvar as s2240_altexprisco_epc_salvar_views
from emensageriapro.s2240.views import s2240_altexprisco_epc_api as s2240_altexprisco_epc_api_views
from emensageriapro.s2240.views import s2240_altexprisco_epi_apagar as s2240_altexprisco_epi_apagar_views
from emensageriapro.s2240.views import s2240_altexprisco_epi_listar as s2240_altexprisco_epi_listar_views
from emensageriapro.s2240.views import s2240_altexprisco_epi_salvar as s2240_altexprisco_epi_salvar_views
from emensageriapro.s2240.views import s2240_altexprisco_epi_api as s2240_altexprisco_epi_api_views
from emensageriapro.s2240.views import s2240_fimexprisco_apagar as s2240_fimexprisco_apagar_views
from emensageriapro.s2240.views import s2240_fimexprisco_listar as s2240_fimexprisco_listar_views
from emensageriapro.s2240.views import s2240_fimexprisco_salvar as s2240_fimexprisco_salvar_views
from emensageriapro.s2240.views import s2240_fimexprisco_api as s2240_fimexprisco_api_views
from emensageriapro.s2240.views import s2240_fimexprisco_infoamb_apagar as s2240_fimexprisco_infoamb_apagar_views
from emensageriapro.s2240.views import s2240_fimexprisco_infoamb_listar as s2240_fimexprisco_infoamb_listar_views
from emensageriapro.s2240.views import s2240_fimexprisco_infoamb_salvar as s2240_fimexprisco_infoamb_salvar_views
from emensageriapro.s2240.views import s2240_fimexprisco_infoamb_api as s2240_fimexprisco_infoamb_api_views
from emensageriapro.s2240.views import s2240_fimexprisco_respreg_apagar as s2240_fimexprisco_respreg_apagar_views
from emensageriapro.s2240.views import s2240_fimexprisco_respreg_listar as s2240_fimexprisco_respreg_listar_views
from emensageriapro.s2240.views import s2240_fimexprisco_respreg_salvar as s2240_fimexprisco_respreg_salvar_views
from emensageriapro.s2240.views import s2240_fimexprisco_respreg_api as s2240_fimexprisco_respreg_api_views


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


    url(r'^s2240-iniexprisco-infoamb/apagar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_infoamb_apagar_views.apagar,
        name='s2240_iniexprisco_infoamb_apagar'),

    url(r'^s2240-iniexprisco-infoamb/api/$',
        s2240_iniexprisco_infoamb_api_views.s2240iniExpRiscoinfoAmbList.as_view() ),

    url(r'^s2240-iniexprisco-infoamb/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_infoamb_api_views.s2240iniExpRiscoinfoAmbDetail.as_view() ),

    url(r'^s2240-iniexprisco-infoamb/$',
        s2240_iniexprisco_infoamb_listar_views.listar,
        name='s2240_iniexprisco_infoamb'),

    url(r'^s2240-iniexprisco-infoamb/salvar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_infoamb_salvar_views.salvar,
        name='s2240_iniexprisco_infoamb_salvar'),

    url(r'^s2240-iniexprisco-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_iniexprisco_infoamb_salvar_views.salvar,
        name='s2240_iniexprisco_infoamb_salvar_tab'),

    url(r'^s2240-iniexprisco-infoamb/cadastrar/$',
        s2240_iniexprisco_infoamb_salvar_views.salvar,
        name='s2240_iniexprisco_infoamb_cadastrar'),

    url(r'^s2240-iniexprisco-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_infoamb_salvar_views.salvar,
        name='s2240_iniexprisco_infoamb_salvar_output'),

    url(r'^s2240-iniexprisco-infoamb/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_infoamb_listar_views.listar,
        name='s2240_iniexprisco_infoamb_output'),

    url(r'^s2240-iniexprisco-ativpericinsal/apagar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_ativpericinsal_apagar_views.apagar,
        name='s2240_iniexprisco_ativpericinsal_apagar'),

    url(r'^s2240-iniexprisco-ativpericinsal/api/$',
        s2240_iniexprisco_ativpericinsal_api_views.s2240iniExpRiscoativPericInsalList.as_view() ),

    url(r'^s2240-iniexprisco-ativpericinsal/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_ativpericinsal_api_views.s2240iniExpRiscoativPericInsalDetail.as_view() ),

    url(r'^s2240-iniexprisco-ativpericinsal/$',
        s2240_iniexprisco_ativpericinsal_listar_views.listar,
        name='s2240_iniexprisco_ativpericinsal'),

    url(r'^s2240-iniexprisco-ativpericinsal/salvar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_ativpericinsal_salvar_views.salvar,
        name='s2240_iniexprisco_ativpericinsal_salvar'),

    url(r'^s2240-iniexprisco-ativpericinsal/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_iniexprisco_ativpericinsal_salvar_views.salvar,
        name='s2240_iniexprisco_ativpericinsal_salvar_tab'),

    url(r'^s2240-iniexprisco-ativpericinsal/cadastrar/$',
        s2240_iniexprisco_ativpericinsal_salvar_views.salvar,
        name='s2240_iniexprisco_ativpericinsal_cadastrar'),

    url(r'^s2240-iniexprisco-ativpericinsal/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_ativpericinsal_salvar_views.salvar,
        name='s2240_iniexprisco_ativpericinsal_salvar_output'),

    url(r'^s2240-iniexprisco-ativpericinsal/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_ativpericinsal_listar_views.listar,
        name='s2240_iniexprisco_ativpericinsal_output'),

    url(r'^s2240-iniexprisco-fatrisco/apagar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_fatrisco_apagar_views.apagar,
        name='s2240_iniexprisco_fatrisco_apagar'),

    url(r'^s2240-iniexprisco-fatrisco/api/$',
        s2240_iniexprisco_fatrisco_api_views.s2240iniExpRiscofatRiscoList.as_view() ),

    url(r'^s2240-iniexprisco-fatrisco/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_fatrisco_api_views.s2240iniExpRiscofatRiscoDetail.as_view() ),

    url(r'^s2240-iniexprisco-fatrisco/$',
        s2240_iniexprisco_fatrisco_listar_views.listar,
        name='s2240_iniexprisco_fatrisco'),

    url(r'^s2240-iniexprisco-fatrisco/salvar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_fatrisco_salvar_views.salvar,
        name='s2240_iniexprisco_fatrisco_salvar'),

    url(r'^s2240-iniexprisco-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_iniexprisco_fatrisco_salvar_views.salvar,
        name='s2240_iniexprisco_fatrisco_salvar_tab'),

    url(r'^s2240-iniexprisco-fatrisco/cadastrar/$',
        s2240_iniexprisco_fatrisco_salvar_views.salvar,
        name='s2240_iniexprisco_fatrisco_cadastrar'),

    url(r'^s2240-iniexprisco-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_fatrisco_salvar_views.salvar,
        name='s2240_iniexprisco_fatrisco_salvar_output'),

    url(r'^s2240-iniexprisco-fatrisco/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_fatrisco_listar_views.listar,
        name='s2240_iniexprisco_fatrisco_output'),

    url(r'^s2240-iniexprisco-epc/apagar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_epc_apagar_views.apagar,
        name='s2240_iniexprisco_epc_apagar'),

    url(r'^s2240-iniexprisco-epc/api/$',
        s2240_iniexprisco_epc_api_views.s2240iniExpRiscoepcList.as_view() ),

    url(r'^s2240-iniexprisco-epc/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_epc_api_views.s2240iniExpRiscoepcDetail.as_view() ),

    url(r'^s2240-iniexprisco-epc/$',
        s2240_iniexprisco_epc_listar_views.listar,
        name='s2240_iniexprisco_epc'),

    url(r'^s2240-iniexprisco-epc/salvar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_epc_salvar_views.salvar,
        name='s2240_iniexprisco_epc_salvar'),

    url(r'^s2240-iniexprisco-epc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_iniexprisco_epc_salvar_views.salvar,
        name='s2240_iniexprisco_epc_salvar_tab'),

    url(r'^s2240-iniexprisco-epc/cadastrar/$',
        s2240_iniexprisco_epc_salvar_views.salvar,
        name='s2240_iniexprisco_epc_cadastrar'),

    url(r'^s2240-iniexprisco-epc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_epc_salvar_views.salvar,
        name='s2240_iniexprisco_epc_salvar_output'),

    url(r'^s2240-iniexprisco-epc/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_epc_listar_views.listar,
        name='s2240_iniexprisco_epc_output'),

    url(r'^s2240-iniexprisco-epi/apagar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_epi_apagar_views.apagar,
        name='s2240_iniexprisco_epi_apagar'),

    url(r'^s2240-iniexprisco-epi/api/$',
        s2240_iniexprisco_epi_api_views.s2240iniExpRiscoepiList.as_view() ),

    url(r'^s2240-iniexprisco-epi/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_epi_api_views.s2240iniExpRiscoepiDetail.as_view() ),

    url(r'^s2240-iniexprisco-epi/$',
        s2240_iniexprisco_epi_listar_views.listar,
        name='s2240_iniexprisco_epi'),

    url(r'^s2240-iniexprisco-epi/salvar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_epi_salvar_views.salvar,
        name='s2240_iniexprisco_epi_salvar'),

    url(r'^s2240-iniexprisco-epi/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_iniexprisco_epi_salvar_views.salvar,
        name='s2240_iniexprisco_epi_salvar_tab'),

    url(r'^s2240-iniexprisco-epi/cadastrar/$',
        s2240_iniexprisco_epi_salvar_views.salvar,
        name='s2240_iniexprisco_epi_cadastrar'),

    url(r'^s2240-iniexprisco-epi/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_epi_salvar_views.salvar,
        name='s2240_iniexprisco_epi_salvar_output'),

    url(r'^s2240-iniexprisco-epi/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_epi_listar_views.listar,
        name='s2240_iniexprisco_epi_output'),

    url(r'^s2240-iniexprisco-respreg/apagar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_respreg_apagar_views.apagar,
        name='s2240_iniexprisco_respreg_apagar'),

    url(r'^s2240-iniexprisco-respreg/api/$',
        s2240_iniexprisco_respreg_api_views.s2240iniExpRiscorespRegList.as_view() ),

    url(r'^s2240-iniexprisco-respreg/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_respreg_api_views.s2240iniExpRiscorespRegDetail.as_view() ),

    url(r'^s2240-iniexprisco-respreg/$',
        s2240_iniexprisco_respreg_listar_views.listar,
        name='s2240_iniexprisco_respreg'),

    url(r'^s2240-iniexprisco-respreg/salvar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_respreg_salvar_views.salvar,
        name='s2240_iniexprisco_respreg_salvar'),

    url(r'^s2240-iniexprisco-respreg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_iniexprisco_respreg_salvar_views.salvar,
        name='s2240_iniexprisco_respreg_salvar_tab'),

    url(r'^s2240-iniexprisco-respreg/cadastrar/$',
        s2240_iniexprisco_respreg_salvar_views.salvar,
        name='s2240_iniexprisco_respreg_cadastrar'),

    url(r'^s2240-iniexprisco-respreg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_respreg_salvar_views.salvar,
        name='s2240_iniexprisco_respreg_salvar_output'),

    url(r'^s2240-iniexprisco-respreg/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_respreg_listar_views.listar,
        name='s2240_iniexprisco_respreg_output'),

    url(r'^s2240-iniexprisco-obs/apagar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_obs_apagar_views.apagar,
        name='s2240_iniexprisco_obs_apagar'),

    url(r'^s2240-iniexprisco-obs/api/$',
        s2240_iniexprisco_obs_api_views.s2240iniExpRiscoobsList.as_view() ),

    url(r'^s2240-iniexprisco-obs/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_obs_api_views.s2240iniExpRiscoobsDetail.as_view() ),

    url(r'^s2240-iniexprisco-obs/$',
        s2240_iniexprisco_obs_listar_views.listar,
        name='s2240_iniexprisco_obs'),

    url(r'^s2240-iniexprisco-obs/salvar/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_obs_salvar_views.salvar,
        name='s2240_iniexprisco_obs_salvar'),

    url(r'^s2240-iniexprisco-obs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_iniexprisco_obs_salvar_views.salvar,
        name='s2240_iniexprisco_obs_salvar_tab'),

    url(r'^s2240-iniexprisco-obs/cadastrar/$',
        s2240_iniexprisco_obs_salvar_views.salvar,
        name='s2240_iniexprisco_obs_cadastrar'),

    url(r'^s2240-iniexprisco-obs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_obs_salvar_views.salvar,
        name='s2240_iniexprisco_obs_salvar_output'),

    url(r'^s2240-iniexprisco-obs/(?P<output>[\w-]+)/$',
        s2240_iniexprisco_obs_listar_views.listar,
        name='s2240_iniexprisco_obs_output'),

    url(r'^s2240-altexprisco/apagar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_apagar_views.apagar,
        name='s2240_altexprisco_apagar'),

    url(r'^s2240-altexprisco/api/$',
        s2240_altexprisco_api_views.s2240altExpRiscoList.as_view() ),

    url(r'^s2240-altexprisco/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_api_views.s2240altExpRiscoDetail.as_view() ),

    url(r'^s2240-altexprisco/$',
        s2240_altexprisco_listar_views.listar,
        name='s2240_altexprisco'),

    url(r'^s2240-altexprisco/salvar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_salvar_views.salvar,
        name='s2240_altexprisco_salvar'),

    url(r'^s2240-altexprisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_altexprisco_salvar_views.salvar,
        name='s2240_altexprisco_salvar_tab'),

    url(r'^s2240-altexprisco/cadastrar/$',
        s2240_altexprisco_salvar_views.salvar,
        name='s2240_altexprisco_cadastrar'),

    url(r'^s2240-altexprisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_altexprisco_salvar_views.salvar,
        name='s2240_altexprisco_salvar_output'),

    url(r'^s2240-altexprisco/(?P<output>[\w-]+)/$',
        s2240_altexprisco_listar_views.listar,
        name='s2240_altexprisco_output'),

    url(r'^s2240-altexprisco-infoamb/apagar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_infoamb_apagar_views.apagar,
        name='s2240_altexprisco_infoamb_apagar'),

    url(r'^s2240-altexprisco-infoamb/api/$',
        s2240_altexprisco_infoamb_api_views.s2240altExpRiscoinfoAmbList.as_view() ),

    url(r'^s2240-altexprisco-infoamb/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_infoamb_api_views.s2240altExpRiscoinfoAmbDetail.as_view() ),

    url(r'^s2240-altexprisco-infoamb/$',
        s2240_altexprisco_infoamb_listar_views.listar,
        name='s2240_altexprisco_infoamb'),

    url(r'^s2240-altexprisco-infoamb/salvar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_infoamb_salvar_views.salvar,
        name='s2240_altexprisco_infoamb_salvar'),

    url(r'^s2240-altexprisco-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_altexprisco_infoamb_salvar_views.salvar,
        name='s2240_altexprisco_infoamb_salvar_tab'),

    url(r'^s2240-altexprisco-infoamb/cadastrar/$',
        s2240_altexprisco_infoamb_salvar_views.salvar,
        name='s2240_altexprisco_infoamb_cadastrar'),

    url(r'^s2240-altexprisco-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_altexprisco_infoamb_salvar_views.salvar,
        name='s2240_altexprisco_infoamb_salvar_output'),

    url(r'^s2240-altexprisco-infoamb/(?P<output>[\w-]+)/$',
        s2240_altexprisco_infoamb_listar_views.listar,
        name='s2240_altexprisco_infoamb_output'),

    url(r'^s2240-altexprisco-fatrisco/apagar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_fatrisco_apagar_views.apagar,
        name='s2240_altexprisco_fatrisco_apagar'),

    url(r'^s2240-altexprisco-fatrisco/api/$',
        s2240_altexprisco_fatrisco_api_views.s2240altExpRiscofatRiscoList.as_view() ),

    url(r'^s2240-altexprisco-fatrisco/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_fatrisco_api_views.s2240altExpRiscofatRiscoDetail.as_view() ),

    url(r'^s2240-altexprisco-fatrisco/$',
        s2240_altexprisco_fatrisco_listar_views.listar,
        name='s2240_altexprisco_fatrisco'),

    url(r'^s2240-altexprisco-fatrisco/salvar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_fatrisco_salvar_views.salvar,
        name='s2240_altexprisco_fatrisco_salvar'),

    url(r'^s2240-altexprisco-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_altexprisco_fatrisco_salvar_views.salvar,
        name='s2240_altexprisco_fatrisco_salvar_tab'),

    url(r'^s2240-altexprisco-fatrisco/cadastrar/$',
        s2240_altexprisco_fatrisco_salvar_views.salvar,
        name='s2240_altexprisco_fatrisco_cadastrar'),

    url(r'^s2240-altexprisco-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_altexprisco_fatrisco_salvar_views.salvar,
        name='s2240_altexprisco_fatrisco_salvar_output'),

    url(r'^s2240-altexprisco-fatrisco/(?P<output>[\w-]+)/$',
        s2240_altexprisco_fatrisco_listar_views.listar,
        name='s2240_altexprisco_fatrisco_output'),

    url(r'^s2240-altexprisco-epc/apagar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_epc_apagar_views.apagar,
        name='s2240_altexprisco_epc_apagar'),

    url(r'^s2240-altexprisco-epc/api/$',
        s2240_altexprisco_epc_api_views.s2240altExpRiscoepcList.as_view() ),

    url(r'^s2240-altexprisco-epc/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_epc_api_views.s2240altExpRiscoepcDetail.as_view() ),

    url(r'^s2240-altexprisco-epc/$',
        s2240_altexprisco_epc_listar_views.listar,
        name='s2240_altexprisco_epc'),

    url(r'^s2240-altexprisco-epc/salvar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_epc_salvar_views.salvar,
        name='s2240_altexprisco_epc_salvar'),

    url(r'^s2240-altexprisco-epc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_altexprisco_epc_salvar_views.salvar,
        name='s2240_altexprisco_epc_salvar_tab'),

    url(r'^s2240-altexprisco-epc/cadastrar/$',
        s2240_altexprisco_epc_salvar_views.salvar,
        name='s2240_altexprisco_epc_cadastrar'),

    url(r'^s2240-altexprisco-epc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_altexprisco_epc_salvar_views.salvar,
        name='s2240_altexprisco_epc_salvar_output'),

    url(r'^s2240-altexprisco-epc/(?P<output>[\w-]+)/$',
        s2240_altexprisco_epc_listar_views.listar,
        name='s2240_altexprisco_epc_output'),

    url(r'^s2240-altexprisco-epi/apagar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_epi_apagar_views.apagar,
        name='s2240_altexprisco_epi_apagar'),

    url(r'^s2240-altexprisco-epi/api/$',
        s2240_altexprisco_epi_api_views.s2240altExpRiscoepiList.as_view() ),

    url(r'^s2240-altexprisco-epi/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_epi_api_views.s2240altExpRiscoepiDetail.as_view() ),

    url(r'^s2240-altexprisco-epi/$',
        s2240_altexprisco_epi_listar_views.listar,
        name='s2240_altexprisco_epi'),

    url(r'^s2240-altexprisco-epi/salvar/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_epi_salvar_views.salvar,
        name='s2240_altexprisco_epi_salvar'),

    url(r'^s2240-altexprisco-epi/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_altexprisco_epi_salvar_views.salvar,
        name='s2240_altexprisco_epi_salvar_tab'),

    url(r'^s2240-altexprisco-epi/cadastrar/$',
        s2240_altexprisco_epi_salvar_views.salvar,
        name='s2240_altexprisco_epi_cadastrar'),

    url(r'^s2240-altexprisco-epi/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_altexprisco_epi_salvar_views.salvar,
        name='s2240_altexprisco_epi_salvar_output'),

    url(r'^s2240-altexprisco-epi/(?P<output>[\w-]+)/$',
        s2240_altexprisco_epi_listar_views.listar,
        name='s2240_altexprisco_epi_output'),

    url(r'^s2240-fimexprisco/apagar/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_apagar_views.apagar,
        name='s2240_fimexprisco_apagar'),

    url(r'^s2240-fimexprisco/api/$',
        s2240_fimexprisco_api_views.s2240fimExpRiscoList.as_view() ),

    url(r'^s2240-fimexprisco/api/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_api_views.s2240fimExpRiscoDetail.as_view() ),

    url(r'^s2240-fimexprisco/$',
        s2240_fimexprisco_listar_views.listar,
        name='s2240_fimexprisco'),

    url(r'^s2240-fimexprisco/salvar/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_salvar_views.salvar,
        name='s2240_fimexprisco_salvar'),

    url(r'^s2240-fimexprisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_fimexprisco_salvar_views.salvar,
        name='s2240_fimexprisco_salvar_tab'),

    url(r'^s2240-fimexprisco/cadastrar/$',
        s2240_fimexprisco_salvar_views.salvar,
        name='s2240_fimexprisco_cadastrar'),

    url(r'^s2240-fimexprisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_fimexprisco_salvar_views.salvar,
        name='s2240_fimexprisco_salvar_output'),

    url(r'^s2240-fimexprisco/(?P<output>[\w-]+)/$',
        s2240_fimexprisco_listar_views.listar,
        name='s2240_fimexprisco_output'),

    url(r'^s2240-fimexprisco-infoamb/apagar/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_infoamb_apagar_views.apagar,
        name='s2240_fimexprisco_infoamb_apagar'),

    url(r'^s2240-fimexprisco-infoamb/api/$',
        s2240_fimexprisco_infoamb_api_views.s2240fimExpRiscoinfoAmbList.as_view() ),

    url(r'^s2240-fimexprisco-infoamb/api/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_infoamb_api_views.s2240fimExpRiscoinfoAmbDetail.as_view() ),

    url(r'^s2240-fimexprisco-infoamb/$',
        s2240_fimexprisco_infoamb_listar_views.listar,
        name='s2240_fimexprisco_infoamb'),

    url(r'^s2240-fimexprisco-infoamb/salvar/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_infoamb_salvar_views.salvar,
        name='s2240_fimexprisco_infoamb_salvar'),

    url(r'^s2240-fimexprisco-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_fimexprisco_infoamb_salvar_views.salvar,
        name='s2240_fimexprisco_infoamb_salvar_tab'),

    url(r'^s2240-fimexprisco-infoamb/cadastrar/$',
        s2240_fimexprisco_infoamb_salvar_views.salvar,
        name='s2240_fimexprisco_infoamb_cadastrar'),

    url(r'^s2240-fimexprisco-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_fimexprisco_infoamb_salvar_views.salvar,
        name='s2240_fimexprisco_infoamb_salvar_output'),

    url(r'^s2240-fimexprisco-infoamb/(?P<output>[\w-]+)/$',
        s2240_fimexprisco_infoamb_listar_views.listar,
        name='s2240_fimexprisco_infoamb_output'),

    url(r'^s2240-fimexprisco-respreg/apagar/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_respreg_apagar_views.apagar,
        name='s2240_fimexprisco_respreg_apagar'),

    url(r'^s2240-fimexprisco-respreg/api/$',
        s2240_fimexprisco_respreg_api_views.s2240fimExpRiscorespRegList.as_view() ),

    url(r'^s2240-fimexprisco-respreg/api/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_respreg_api_views.s2240fimExpRiscorespRegDetail.as_view() ),

    url(r'^s2240-fimexprisco-respreg/$',
        s2240_fimexprisco_respreg_listar_views.listar,
        name='s2240_fimexprisco_respreg'),

    url(r'^s2240-fimexprisco-respreg/salvar/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_respreg_salvar_views.salvar,
        name='s2240_fimexprisco_respreg_salvar'),

    url(r'^s2240-fimexprisco-respreg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2240_fimexprisco_respreg_salvar_views.salvar,
        name='s2240_fimexprisco_respreg_salvar_tab'),

    url(r'^s2240-fimexprisco-respreg/cadastrar/$',
        s2240_fimexprisco_respreg_salvar_views.salvar,
        name='s2240_fimexprisco_respreg_cadastrar'),

    url(r'^s2240-fimexprisco-respreg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2240_fimexprisco_respreg_salvar_views.salvar,
        name='s2240_fimexprisco_respreg_salvar_output'),

    url(r'^s2240-fimexprisco-respreg/(?P<output>[\w-]+)/$',
        s2240_fimexprisco_respreg_listar_views.listar,
        name='s2240_fimexprisco_respreg_output'),


]