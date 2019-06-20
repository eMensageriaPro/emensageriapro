#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s5001.views import s5001_procjudtrab_apagar as s5001_procjudtrab_apagar_views
from emensageriapro.s5001.views import s5001_procjudtrab_listar as s5001_procjudtrab_listar_views
from emensageriapro.s5001.views import s5001_procjudtrab_salvar as s5001_procjudtrab_salvar_views
from emensageriapro.s5001.views import s5001_procjudtrab_api as s5001_procjudtrab_api_views
from emensageriapro.s5001.views import s5001_infocpcalc_apagar as s5001_infocpcalc_apagar_views
from emensageriapro.s5001.views import s5001_infocpcalc_listar as s5001_infocpcalc_listar_views
from emensageriapro.s5001.views import s5001_infocpcalc_salvar as s5001_infocpcalc_salvar_views
from emensageriapro.s5001.views import s5001_infocpcalc_api as s5001_infocpcalc_api_views
from emensageriapro.s5001.views import s5001_infocp_apagar as s5001_infocp_apagar_views
from emensageriapro.s5001.views import s5001_infocp_listar as s5001_infocp_listar_views
from emensageriapro.s5001.views import s5001_infocp_salvar as s5001_infocp_salvar_views
from emensageriapro.s5001.views import s5001_infocp_api as s5001_infocp_api_views
from emensageriapro.s5001.views import s5001_ideestablot_apagar as s5001_ideestablot_apagar_views
from emensageriapro.s5001.views import s5001_ideestablot_listar as s5001_ideestablot_listar_views
from emensageriapro.s5001.views import s5001_ideestablot_salvar as s5001_ideestablot_salvar_views
from emensageriapro.s5001.views import s5001_ideestablot_api as s5001_ideestablot_api_views
from emensageriapro.s5001.views import s5001_infocategincid_apagar as s5001_infocategincid_apagar_views
from emensageriapro.s5001.views import s5001_infocategincid_listar as s5001_infocategincid_listar_views
from emensageriapro.s5001.views import s5001_infocategincid_salvar as s5001_infocategincid_salvar_views
from emensageriapro.s5001.views import s5001_infocategincid_api as s5001_infocategincid_api_views
from emensageriapro.s5001.views import s5001_infobasecs_apagar as s5001_infobasecs_apagar_views
from emensageriapro.s5001.views import s5001_infobasecs_listar as s5001_infobasecs_listar_views
from emensageriapro.s5001.views import s5001_infobasecs_salvar as s5001_infobasecs_salvar_views
from emensageriapro.s5001.views import s5001_infobasecs_api as s5001_infobasecs_api_views
from emensageriapro.s5001.views import s5001_calcterc_apagar as s5001_calcterc_apagar_views
from emensageriapro.s5001.views import s5001_calcterc_listar as s5001_calcterc_listar_views
from emensageriapro.s5001.views import s5001_calcterc_salvar as s5001_calcterc_salvar_views
from emensageriapro.s5001.views import s5001_calcterc_api as s5001_calcterc_api_views



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


    url(r'^s5001-procjudtrab/apagar/(?P<pk>[0-9]+)/$', 
        s5001_procjudtrab_apagar_views.apagar, 
        name='s5001_procjudtrab_apagar'),

    url(r'^s5001-procjudtrab/api/$',
        s5001_procjudtrab_api_views.s5001procJudTrabList.as_view() ),

    url(r'^s5001-procjudtrab/api/(?P<pk>[0-9]+)/$',
        s5001_procjudtrab_api_views.s5001procJudTrabDetail.as_view() ),

    url(r'^s5001-procjudtrab/$', 
        s5001_procjudtrab_listar_views.listar, 
        name='s5001_procjudtrab'),

    url(r'^s5001-procjudtrab/salvar/(?P<pk>[0-9]+)/$', 
        s5001_procjudtrab_salvar_views.salvar, 
        name='s5001_procjudtrab_salvar'),

    url(r'^s5001-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5001_procjudtrab_salvar_views.salvar, 
        name='s5001_procjudtrab_salvar_tab'),
        
    url(r'^s5001-procjudtrab/cadastrar/$', 
        s5001_procjudtrab_salvar_views.salvar, 
        name='s5001_procjudtrab_cadastrar'),

    url(r'^s5001-procjudtrab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5001_procjudtrab_salvar_views.salvar, 
        name='s5001_procjudtrab_salvar_output'),
        
    url(r'^s5001-procjudtrab/(?P<output>[\w-]+)/$', 
        s5001_procjudtrab_listar_views.listar, 
        name='s5001_procjudtrab_output'),

    url(r'^s5001-infocpcalc/apagar/(?P<pk>[0-9]+)/$', 
        s5001_infocpcalc_apagar_views.apagar, 
        name='s5001_infocpcalc_apagar'),

    url(r'^s5001-infocpcalc/api/$',
        s5001_infocpcalc_api_views.s5001infoCpCalcList.as_view() ),

    url(r'^s5001-infocpcalc/api/(?P<pk>[0-9]+)/$',
        s5001_infocpcalc_api_views.s5001infoCpCalcDetail.as_view() ),

    url(r'^s5001-infocpcalc/$', 
        s5001_infocpcalc_listar_views.listar, 
        name='s5001_infocpcalc'),

    url(r'^s5001-infocpcalc/salvar/(?P<pk>[0-9]+)/$', 
        s5001_infocpcalc_salvar_views.salvar, 
        name='s5001_infocpcalc_salvar'),

    url(r'^s5001-infocpcalc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5001_infocpcalc_salvar_views.salvar, 
        name='s5001_infocpcalc_salvar_tab'),
        
    url(r'^s5001-infocpcalc/cadastrar/$', 
        s5001_infocpcalc_salvar_views.salvar, 
        name='s5001_infocpcalc_cadastrar'),

    url(r'^s5001-infocpcalc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5001_infocpcalc_salvar_views.salvar, 
        name='s5001_infocpcalc_salvar_output'),
        
    url(r'^s5001-infocpcalc/(?P<output>[\w-]+)/$', 
        s5001_infocpcalc_listar_views.listar, 
        name='s5001_infocpcalc_output'),

    url(r'^s5001-infocp/apagar/(?P<pk>[0-9]+)/$', 
        s5001_infocp_apagar_views.apagar, 
        name='s5001_infocp_apagar'),

    url(r'^s5001-infocp/api/$',
        s5001_infocp_api_views.s5001infoCpList.as_view() ),

    url(r'^s5001-infocp/api/(?P<pk>[0-9]+)/$',
        s5001_infocp_api_views.s5001infoCpDetail.as_view() ),

    url(r'^s5001-infocp/$', 
        s5001_infocp_listar_views.listar, 
        name='s5001_infocp'),

    url(r'^s5001-infocp/salvar/(?P<pk>[0-9]+)/$', 
        s5001_infocp_salvar_views.salvar, 
        name='s5001_infocp_salvar'),

    url(r'^s5001-infocp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5001_infocp_salvar_views.salvar, 
        name='s5001_infocp_salvar_tab'),
        
    url(r'^s5001-infocp/cadastrar/$', 
        s5001_infocp_salvar_views.salvar, 
        name='s5001_infocp_cadastrar'),

    url(r'^s5001-infocp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5001_infocp_salvar_views.salvar, 
        name='s5001_infocp_salvar_output'),
        
    url(r'^s5001-infocp/(?P<output>[\w-]+)/$', 
        s5001_infocp_listar_views.listar, 
        name='s5001_infocp_output'),

    url(r'^s5001-ideestablot/apagar/(?P<pk>[0-9]+)/$', 
        s5001_ideestablot_apagar_views.apagar, 
        name='s5001_ideestablot_apagar'),

    url(r'^s5001-ideestablot/api/$',
        s5001_ideestablot_api_views.s5001ideEstabLotList.as_view() ),

    url(r'^s5001-ideestablot/api/(?P<pk>[0-9]+)/$',
        s5001_ideestablot_api_views.s5001ideEstabLotDetail.as_view() ),

    url(r'^s5001-ideestablot/$', 
        s5001_ideestablot_listar_views.listar, 
        name='s5001_ideestablot'),

    url(r'^s5001-ideestablot/salvar/(?P<pk>[0-9]+)/$', 
        s5001_ideestablot_salvar_views.salvar, 
        name='s5001_ideestablot_salvar'),

    url(r'^s5001-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5001_ideestablot_salvar_views.salvar, 
        name='s5001_ideestablot_salvar_tab'),
        
    url(r'^s5001-ideestablot/cadastrar/$', 
        s5001_ideestablot_salvar_views.salvar, 
        name='s5001_ideestablot_cadastrar'),

    url(r'^s5001-ideestablot/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5001_ideestablot_salvar_views.salvar, 
        name='s5001_ideestablot_salvar_output'),
        
    url(r'^s5001-ideestablot/(?P<output>[\w-]+)/$', 
        s5001_ideestablot_listar_views.listar, 
        name='s5001_ideestablot_output'),

    url(r'^s5001-infocategincid/apagar/(?P<pk>[0-9]+)/$', 
        s5001_infocategincid_apagar_views.apagar, 
        name='s5001_infocategincid_apagar'),

    url(r'^s5001-infocategincid/api/$',
        s5001_infocategincid_api_views.s5001infoCategIncidList.as_view() ),

    url(r'^s5001-infocategincid/api/(?P<pk>[0-9]+)/$',
        s5001_infocategincid_api_views.s5001infoCategIncidDetail.as_view() ),

    url(r'^s5001-infocategincid/$', 
        s5001_infocategincid_listar_views.listar, 
        name='s5001_infocategincid'),

    url(r'^s5001-infocategincid/salvar/(?P<pk>[0-9]+)/$', 
        s5001_infocategincid_salvar_views.salvar, 
        name='s5001_infocategincid_salvar'),

    url(r'^s5001-infocategincid/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5001_infocategincid_salvar_views.salvar, 
        name='s5001_infocategincid_salvar_tab'),
        
    url(r'^s5001-infocategincid/cadastrar/$', 
        s5001_infocategincid_salvar_views.salvar, 
        name='s5001_infocategincid_cadastrar'),

    url(r'^s5001-infocategincid/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5001_infocategincid_salvar_views.salvar, 
        name='s5001_infocategincid_salvar_output'),
        
    url(r'^s5001-infocategincid/(?P<output>[\w-]+)/$', 
        s5001_infocategincid_listar_views.listar, 
        name='s5001_infocategincid_output'),

    url(r'^s5001-infobasecs/apagar/(?P<pk>[0-9]+)/$', 
        s5001_infobasecs_apagar_views.apagar, 
        name='s5001_infobasecs_apagar'),

    url(r'^s5001-infobasecs/api/$',
        s5001_infobasecs_api_views.s5001infoBaseCSList.as_view() ),

    url(r'^s5001-infobasecs/api/(?P<pk>[0-9]+)/$',
        s5001_infobasecs_api_views.s5001infoBaseCSDetail.as_view() ),

    url(r'^s5001-infobasecs/$', 
        s5001_infobasecs_listar_views.listar, 
        name='s5001_infobasecs'),

    url(r'^s5001-infobasecs/salvar/(?P<pk>[0-9]+)/$', 
        s5001_infobasecs_salvar_views.salvar, 
        name='s5001_infobasecs_salvar'),

    url(r'^s5001-infobasecs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5001_infobasecs_salvar_views.salvar, 
        name='s5001_infobasecs_salvar_tab'),
        
    url(r'^s5001-infobasecs/cadastrar/$', 
        s5001_infobasecs_salvar_views.salvar, 
        name='s5001_infobasecs_cadastrar'),

    url(r'^s5001-infobasecs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5001_infobasecs_salvar_views.salvar, 
        name='s5001_infobasecs_salvar_output'),
        
    url(r'^s5001-infobasecs/(?P<output>[\w-]+)/$', 
        s5001_infobasecs_listar_views.listar, 
        name='s5001_infobasecs_output'),

    url(r'^s5001-calcterc/apagar/(?P<pk>[0-9]+)/$', 
        s5001_calcterc_apagar_views.apagar, 
        name='s5001_calcterc_apagar'),

    url(r'^s5001-calcterc/api/$',
        s5001_calcterc_api_views.s5001calcTercList.as_view() ),

    url(r'^s5001-calcterc/api/(?P<pk>[0-9]+)/$',
        s5001_calcterc_api_views.s5001calcTercDetail.as_view() ),

    url(r'^s5001-calcterc/$', 
        s5001_calcterc_listar_views.listar, 
        name='s5001_calcterc'),

    url(r'^s5001-calcterc/salvar/(?P<pk>[0-9]+)/$', 
        s5001_calcterc_salvar_views.salvar, 
        name='s5001_calcterc_salvar'),

    url(r'^s5001-calcterc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5001_calcterc_salvar_views.salvar, 
        name='s5001_calcterc_salvar_tab'),
        
    url(r'^s5001-calcterc/cadastrar/$', 
        s5001_calcterc_salvar_views.salvar, 
        name='s5001_calcterc_cadastrar'),

    url(r'^s5001-calcterc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5001_calcterc_salvar_views.salvar, 
        name='s5001_calcterc_salvar_output'),
        
    url(r'^s5001-calcterc/(?P<output>[\w-]+)/$', 
        s5001_calcterc_listar_views.listar, 
        name='s5001_calcterc_output'),


]