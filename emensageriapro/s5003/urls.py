#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s5003.views import s5003_ideestablot_api as s5003_ideestablot_api_views
from emensageriapro.s5003.views import s5003_infotrabfgts_api as s5003_infotrabfgts_api_views
from emensageriapro.s5003.views import s5003_infobasefgts_api as s5003_infobasefgts_api_views
from emensageriapro.s5003.views import s5003_baseperapur_api as s5003_baseperapur_api_views
from emensageriapro.s5003.views import s5003_infobaseperante_api as s5003_infobaseperante_api_views
from emensageriapro.s5003.views import s5003_baseperante_api as s5003_baseperante_api_views
from emensageriapro.s5003.views import s5003_infodpsfgts_api as s5003_infodpsfgts_api_views
from emensageriapro.s5003.views import s5003_infotrabdps_api as s5003_infotrabdps_api_views
from emensageriapro.s5003.views import s5003_dpsperapur_api as s5003_dpsperapur_api_views
from emensageriapro.s5003.views import s5003_infodpsperante_api as s5003_infodpsperante_api_views
from emensageriapro.s5003.views import s5003_dpsperante_api as s5003_dpsperante_api_views


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


    url(r'^s5003-ideestablot/api/$',
        s5003_ideestablot_api_views.s5003ideEstabLotList.as_view() ),

    url(r'^s5003-ideestablot/api/(?P<pk>[0-9]+)/$',
        s5003_ideestablot_api_views.s5003ideEstabLotDetail.as_view() ),

    url(r'^s5003-infotrabfgts/api/$',
        s5003_infotrabfgts_api_views.s5003infoTrabFGTSList.as_view() ),

    url(r'^s5003-infotrabfgts/api/(?P<pk>[0-9]+)/$',
        s5003_infotrabfgts_api_views.s5003infoTrabFGTSDetail.as_view() ),

    url(r'^s5003-infobasefgts/api/$',
        s5003_infobasefgts_api_views.s5003infoBaseFGTSList.as_view() ),

    url(r'^s5003-infobasefgts/api/(?P<pk>[0-9]+)/$',
        s5003_infobasefgts_api_views.s5003infoBaseFGTSDetail.as_view() ),

    url(r'^s5003-baseperapur/api/$',
        s5003_baseperapur_api_views.s5003basePerApurList.as_view() ),

    url(r'^s5003-baseperapur/api/(?P<pk>[0-9]+)/$',
        s5003_baseperapur_api_views.s5003basePerApurDetail.as_view() ),

    url(r'^s5003-infobaseperante/api/$',
        s5003_infobaseperante_api_views.s5003infoBasePerAntEList.as_view() ),

    url(r'^s5003-infobaseperante/api/(?P<pk>[0-9]+)/$',
        s5003_infobaseperante_api_views.s5003infoBasePerAntEDetail.as_view() ),

    url(r'^s5003-baseperante/api/$',
        s5003_baseperante_api_views.s5003basePerAntEList.as_view() ),

    url(r'^s5003-baseperante/api/(?P<pk>[0-9]+)/$',
        s5003_baseperante_api_views.s5003basePerAntEDetail.as_view() ),

    url(r'^s5003-infodpsfgts/api/$',
        s5003_infodpsfgts_api_views.s5003infoDpsFGTSList.as_view() ),

    url(r'^s5003-infodpsfgts/api/(?P<pk>[0-9]+)/$',
        s5003_infodpsfgts_api_views.s5003infoDpsFGTSDetail.as_view() ),

    url(r'^s5003-infotrabdps/api/$',
        s5003_infotrabdps_api_views.s5003infoTrabDpsList.as_view() ),

    url(r'^s5003-infotrabdps/api/(?P<pk>[0-9]+)/$',
        s5003_infotrabdps_api_views.s5003infoTrabDpsDetail.as_view() ),

    url(r'^s5003-dpsperapur/api/$',
        s5003_dpsperapur_api_views.s5003dpsPerApurList.as_view() ),

    url(r'^s5003-dpsperapur/api/(?P<pk>[0-9]+)/$',
        s5003_dpsperapur_api_views.s5003dpsPerApurDetail.as_view() ),

    url(r'^s5003-infodpsperante/api/$',
        s5003_infodpsperante_api_views.s5003infoDpsPerAntEList.as_view() ),

    url(r'^s5003-infodpsperante/api/(?P<pk>[0-9]+)/$',
        s5003_infodpsperante_api_views.s5003infoDpsPerAntEDetail.as_view() ),

    url(r'^s5003-dpsperante/api/$',
        s5003_dpsperante_api_views.s5003dpsPerAntEList.as_view() ),

    url(r'^s5003-dpsperante/api/(?P<pk>[0-9]+)/$',
        s5003_dpsperante_api_views.s5003dpsPerAntEDetail.as_view() ),


]