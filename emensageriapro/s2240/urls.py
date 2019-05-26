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


    url(r'^s2240-iniexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_infoamb_apagar_views.apagar, 
        name='s2240_iniexprisco_infoamb_apagar'),

    url(r'^s2240-iniexprisco-infoamb/api/$',
        s2240_iniexprisco_infoamb_api_views.s2240iniExpRiscoinfoAmbList.as_view() ),

    url(r'^s2240-iniexprisco-infoamb/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_infoamb_api_views.s2240iniExpRiscoinfoAmbDetail.as_view() ),

    url(r'^s2240-iniexprisco-infoamb/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_infoamb_listar_views.listar, 
        name='s2240_iniexprisco_infoamb'),

    url(r'^s2240-iniexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_infoamb_salvar_views.salvar, 
        name='s2240_iniexprisco_infoamb_salvar'),

    url(r'^s2240-iniexprisco-ativpericinsal/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_ativpericinsal_apagar_views.apagar, 
        name='s2240_iniexprisco_ativpericinsal_apagar'),

    url(r'^s2240-iniexprisco-ativpericinsal/api/$',
        s2240_iniexprisco_ativpericinsal_api_views.s2240iniExpRiscoativPericInsalList.as_view() ),

    url(r'^s2240-iniexprisco-ativpericinsal/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_ativpericinsal_api_views.s2240iniExpRiscoativPericInsalDetail.as_view() ),

    url(r'^s2240-iniexprisco-ativpericinsal/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_ativpericinsal_listar_views.listar, 
        name='s2240_iniexprisco_ativpericinsal'),

    url(r'^s2240-iniexprisco-ativpericinsal/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_ativpericinsal_salvar_views.salvar, 
        name='s2240_iniexprisco_ativpericinsal_salvar'),

    url(r'^s2240-iniexprisco-fatrisco/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_fatrisco_apagar_views.apagar, 
        name='s2240_iniexprisco_fatrisco_apagar'),

    url(r'^s2240-iniexprisco-fatrisco/api/$',
        s2240_iniexprisco_fatrisco_api_views.s2240iniExpRiscofatRiscoList.as_view() ),

    url(r'^s2240-iniexprisco-fatrisco/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_fatrisco_api_views.s2240iniExpRiscofatRiscoDetail.as_view() ),

    url(r'^s2240-iniexprisco-fatrisco/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_fatrisco_listar_views.listar, 
        name='s2240_iniexprisco_fatrisco'),

    url(r'^s2240-iniexprisco-fatrisco/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_fatrisco_salvar_views.salvar, 
        name='s2240_iniexprisco_fatrisco_salvar'),

    url(r'^s2240-iniexprisco-epc/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epc_apagar_views.apagar, 
        name='s2240_iniexprisco_epc_apagar'),

    url(r'^s2240-iniexprisco-epc/api/$',
        s2240_iniexprisco_epc_api_views.s2240iniExpRiscoepcList.as_view() ),

    url(r'^s2240-iniexprisco-epc/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_epc_api_views.s2240iniExpRiscoepcDetail.as_view() ),

    url(r'^s2240-iniexprisco-epc/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epc_listar_views.listar, 
        name='s2240_iniexprisco_epc'),

    url(r'^s2240-iniexprisco-epc/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epc_salvar_views.salvar, 
        name='s2240_iniexprisco_epc_salvar'),

    url(r'^s2240-iniexprisco-epi/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epi_apagar_views.apagar, 
        name='s2240_iniexprisco_epi_apagar'),

    url(r'^s2240-iniexprisco-epi/api/$',
        s2240_iniexprisco_epi_api_views.s2240iniExpRiscoepiList.as_view() ),

    url(r'^s2240-iniexprisco-epi/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_epi_api_views.s2240iniExpRiscoepiDetail.as_view() ),

    url(r'^s2240-iniexprisco-epi/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epi_listar_views.listar, 
        name='s2240_iniexprisco_epi'),

    url(r'^s2240-iniexprisco-epi/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_epi_salvar_views.salvar, 
        name='s2240_iniexprisco_epi_salvar'),

    url(r'^s2240-iniexprisco-respreg/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_respreg_apagar_views.apagar, 
        name='s2240_iniexprisco_respreg_apagar'),

    url(r'^s2240-iniexprisco-respreg/api/$',
        s2240_iniexprisco_respreg_api_views.s2240iniExpRiscorespRegList.as_view() ),

    url(r'^s2240-iniexprisco-respreg/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_respreg_api_views.s2240iniExpRiscorespRegDetail.as_view() ),

    url(r'^s2240-iniexprisco-respreg/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_respreg_listar_views.listar, 
        name='s2240_iniexprisco_respreg'),

    url(r'^s2240-iniexprisco-respreg/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_respreg_salvar_views.salvar, 
        name='s2240_iniexprisco_respreg_salvar'),

    url(r'^s2240-iniexprisco-obs/apagar/(?P<hash>.*)/$', 
        s2240_iniexprisco_obs_apagar_views.apagar, 
        name='s2240_iniexprisco_obs_apagar'),

    url(r'^s2240-iniexprisco-obs/api/$',
        s2240_iniexprisco_obs_api_views.s2240iniExpRiscoobsList.as_view() ),

    url(r'^s2240-iniexprisco-obs/api/(?P<pk>[0-9]+)/$',
        s2240_iniexprisco_obs_api_views.s2240iniExpRiscoobsDetail.as_view() ),

    url(r'^s2240-iniexprisco-obs/listar/(?P<hash>.*)/$', 
        s2240_iniexprisco_obs_listar_views.listar, 
        name='s2240_iniexprisco_obs'),

    url(r'^s2240-iniexprisco-obs/salvar/(?P<hash>.*)/$', 
        s2240_iniexprisco_obs_salvar_views.salvar, 
        name='s2240_iniexprisco_obs_salvar'),

    url(r'^s2240-altexprisco/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_apagar_views.apagar, 
        name='s2240_altexprisco_apagar'),

    url(r'^s2240-altexprisco/api/$',
        s2240_altexprisco_api_views.s2240altExpRiscoList.as_view() ),

    url(r'^s2240-altexprisco/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_api_views.s2240altExpRiscoDetail.as_view() ),

    url(r'^s2240-altexprisco/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_listar_views.listar, 
        name='s2240_altexprisco'),

    url(r'^s2240-altexprisco/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_salvar_views.salvar, 
        name='s2240_altexprisco_salvar'),

    url(r'^s2240-altexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_infoamb_apagar_views.apagar, 
        name='s2240_altexprisco_infoamb_apagar'),

    url(r'^s2240-altexprisco-infoamb/api/$',
        s2240_altexprisco_infoamb_api_views.s2240altExpRiscoinfoAmbList.as_view() ),

    url(r'^s2240-altexprisco-infoamb/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_infoamb_api_views.s2240altExpRiscoinfoAmbDetail.as_view() ),

    url(r'^s2240-altexprisco-infoamb/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_infoamb_listar_views.listar, 
        name='s2240_altexprisco_infoamb'),

    url(r'^s2240-altexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_infoamb_salvar_views.salvar, 
        name='s2240_altexprisco_infoamb_salvar'),

    url(r'^s2240-altexprisco-fatrisco/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_fatrisco_apagar_views.apagar, 
        name='s2240_altexprisco_fatrisco_apagar'),

    url(r'^s2240-altexprisco-fatrisco/api/$',
        s2240_altexprisco_fatrisco_api_views.s2240altExpRiscofatRiscoList.as_view() ),

    url(r'^s2240-altexprisco-fatrisco/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_fatrisco_api_views.s2240altExpRiscofatRiscoDetail.as_view() ),

    url(r'^s2240-altexprisco-fatrisco/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_fatrisco_listar_views.listar, 
        name='s2240_altexprisco_fatrisco'),

    url(r'^s2240-altexprisco-fatrisco/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_fatrisco_salvar_views.salvar, 
        name='s2240_altexprisco_fatrisco_salvar'),

    url(r'^s2240-altexprisco-epc/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_epc_apagar_views.apagar, 
        name='s2240_altexprisco_epc_apagar'),

    url(r'^s2240-altexprisco-epc/api/$',
        s2240_altexprisco_epc_api_views.s2240altExpRiscoepcList.as_view() ),

    url(r'^s2240-altexprisco-epc/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_epc_api_views.s2240altExpRiscoepcDetail.as_view() ),

    url(r'^s2240-altexprisco-epc/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_epc_listar_views.listar, 
        name='s2240_altexprisco_epc'),

    url(r'^s2240-altexprisco-epc/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_epc_salvar_views.salvar, 
        name='s2240_altexprisco_epc_salvar'),

    url(r'^s2240-altexprisco-epi/apagar/(?P<hash>.*)/$', 
        s2240_altexprisco_epi_apagar_views.apagar, 
        name='s2240_altexprisco_epi_apagar'),

    url(r'^s2240-altexprisco-epi/api/$',
        s2240_altexprisco_epi_api_views.s2240altExpRiscoepiList.as_view() ),

    url(r'^s2240-altexprisco-epi/api/(?P<pk>[0-9]+)/$',
        s2240_altexprisco_epi_api_views.s2240altExpRiscoepiDetail.as_view() ),

    url(r'^s2240-altexprisco-epi/listar/(?P<hash>.*)/$', 
        s2240_altexprisco_epi_listar_views.listar, 
        name='s2240_altexprisco_epi'),

    url(r'^s2240-altexprisco-epi/salvar/(?P<hash>.*)/$', 
        s2240_altexprisco_epi_salvar_views.salvar, 
        name='s2240_altexprisco_epi_salvar'),

    url(r'^s2240-fimexprisco/apagar/(?P<hash>.*)/$', 
        s2240_fimexprisco_apagar_views.apagar, 
        name='s2240_fimexprisco_apagar'),

    url(r'^s2240-fimexprisco/api/$',
        s2240_fimexprisco_api_views.s2240fimExpRiscoList.as_view() ),

    url(r'^s2240-fimexprisco/api/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_api_views.s2240fimExpRiscoDetail.as_view() ),

    url(r'^s2240-fimexprisco/listar/(?P<hash>.*)/$', 
        s2240_fimexprisco_listar_views.listar, 
        name='s2240_fimexprisco'),

    url(r'^s2240-fimexprisco/salvar/(?P<hash>.*)/$', 
        s2240_fimexprisco_salvar_views.salvar, 
        name='s2240_fimexprisco_salvar'),

    url(r'^s2240-fimexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        s2240_fimexprisco_infoamb_apagar_views.apagar, 
        name='s2240_fimexprisco_infoamb_apagar'),

    url(r'^s2240-fimexprisco-infoamb/api/$',
        s2240_fimexprisco_infoamb_api_views.s2240fimExpRiscoinfoAmbList.as_view() ),

    url(r'^s2240-fimexprisco-infoamb/api/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_infoamb_api_views.s2240fimExpRiscoinfoAmbDetail.as_view() ),

    url(r'^s2240-fimexprisco-infoamb/listar/(?P<hash>.*)/$', 
        s2240_fimexprisco_infoamb_listar_views.listar, 
        name='s2240_fimexprisco_infoamb'),

    url(r'^s2240-fimexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        s2240_fimexprisco_infoamb_salvar_views.salvar, 
        name='s2240_fimexprisco_infoamb_salvar'),

    url(r'^s2240-fimexprisco-respreg/apagar/(?P<hash>.*)/$', 
        s2240_fimexprisco_respreg_apagar_views.apagar, 
        name='s2240_fimexprisco_respreg_apagar'),

    url(r'^s2240-fimexprisco-respreg/api/$',
        s2240_fimexprisco_respreg_api_views.s2240fimExpRiscorespRegList.as_view() ),

    url(r'^s2240-fimexprisco-respreg/api/(?P<pk>[0-9]+)/$',
        s2240_fimexprisco_respreg_api_views.s2240fimExpRiscorespRegDetail.as_view() ),

    url(r'^s2240-fimexprisco-respreg/listar/(?P<hash>.*)/$', 
        s2240_fimexprisco_respreg_listar_views.listar, 
        name='s2240_fimexprisco_respreg'),

    url(r'^s2240-fimexprisco-respreg/salvar/(?P<hash>.*)/$', 
        s2240_fimexprisco_respreg_salvar_views.salvar, 
        name='s2240_fimexprisco_respreg_salvar'),


]