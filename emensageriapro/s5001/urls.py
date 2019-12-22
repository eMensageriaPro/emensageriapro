# eMensageriaAI #
#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s5001.views import s5001_procjudtrab_api as s5001_procjudtrab_api_views
from emensageriapro.s5001.views import s5001_infocpcalc_api as s5001_infocpcalc_api_views
from emensageriapro.s5001.views import s5001_infocp_api as s5001_infocp_api_views
from emensageriapro.s5001.views import s5001_ideestablot_api as s5001_ideestablot_api_views
from emensageriapro.s5001.views import s5001_infocategincid_api as s5001_infocategincid_api_views
from emensageriapro.s5001.views import s5001_infobasecs_api as s5001_infobasecs_api_views
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


    url(r'^s5001-procjudtrab/api/$',
        s5001_procjudtrab_api_views.s5001procJudTrabList.as_view() ),

    url(r'^s5001-procjudtrab/api/(?P<pk>[0-9]+)/$',
        s5001_procjudtrab_api_views.s5001procJudTrabDetail.as_view() ),

    url(r'^s5001-infocpcalc/api/$',
        s5001_infocpcalc_api_views.s5001infoCpCalcList.as_view() ),

    url(r'^s5001-infocpcalc/api/(?P<pk>[0-9]+)/$',
        s5001_infocpcalc_api_views.s5001infoCpCalcDetail.as_view() ),

    url(r'^s5001-infocp/api/$',
        s5001_infocp_api_views.s5001infoCpList.as_view() ),

    url(r'^s5001-infocp/api/(?P<pk>[0-9]+)/$',
        s5001_infocp_api_views.s5001infoCpDetail.as_view() ),

    url(r'^s5001-ideestablot/api/$',
        s5001_ideestablot_api_views.s5001ideEstabLotList.as_view() ),

    url(r'^s5001-ideestablot/api/(?P<pk>[0-9]+)/$',
        s5001_ideestablot_api_views.s5001ideEstabLotDetail.as_view() ),

    url(r'^s5001-infocategincid/api/$',
        s5001_infocategincid_api_views.s5001infoCategIncidList.as_view() ),

    url(r'^s5001-infocategincid/api/(?P<pk>[0-9]+)/$',
        s5001_infocategincid_api_views.s5001infoCategIncidDetail.as_view() ),

    url(r'^s5001-infobasecs/api/$',
        s5001_infobasecs_api_views.s5001infoBaseCSList.as_view() ),

    url(r'^s5001-infobasecs/api/(?P<pk>[0-9]+)/$',
        s5001_infobasecs_api_views.s5001infoBaseCSDetail.as_view() ),

    url(r'^s5001-calcterc/api/$',
        s5001_calcterc_api_views.s5001calcTercList.as_view() ),

    url(r'^s5001-calcterc/api/(?P<pk>[0-9]+)/$',
        s5001_calcterc_api_views.s5001calcTercDetail.as_view() ),


]