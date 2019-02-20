#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s5003.views import s5003_baseperante as s5003_baseperante_views
from emensageriapro.s5003.views import s5003_baseperapur as s5003_baseperapur_views
from emensageriapro.s5003.views import s5003_dpsperante as s5003_dpsperante_views
from emensageriapro.s5003.views import s5003_dpsperapur as s5003_dpsperapur_views
from emensageriapro.s5003.views import s5003_ideestablot as s5003_ideestablot_views
from emensageriapro.s5003.views import s5003_infobaseperante as s5003_infobaseperante_views
from emensageriapro.s5003.views import s5003_infodpsperante as s5003_infodpsperante_views
from emensageriapro.s5003.views import s5003_infofgts as s5003_infofgts_views
from emensageriapro.s5003.views import s5003_infotrabdps as s5003_infotrabdps_views
from emensageriapro.s5003.views import s5003_infotrabfgts as s5003_infotrabfgts_views



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



url(r'^s5003-baseperante/apagar/(?P<hash>.*)/$', 
        s5003_baseperante_views.apagar, 
        name='s5003_baseperante_apagar'),

url(r'^s5003-baseperante/api/$',
            s5003_baseperante_views.s5003basePerAntEList.as_view() ),

        url(r'^s5003-baseperante/api/(?P<pk>[0-9]+)/$',
            s5003_baseperante_views.s5003basePerAntEDetail.as_view() ),

url(r'^s5003-baseperante/listar/(?P<hash>.*)/$', 
        s5003_baseperante_views.listar, 
        name='s5003_baseperante'),

url(r'^s5003-baseperante/salvar/(?P<hash>.*)/$', 
        s5003_baseperante_views.salvar, 
        name='s5003_baseperante_salvar'),



url(r'^s5003-baseperapur/apagar/(?P<hash>.*)/$', 
        s5003_baseperapur_views.apagar, 
        name='s5003_baseperapur_apagar'),

url(r'^s5003-baseperapur/api/$',
            s5003_baseperapur_views.s5003basePerApurList.as_view() ),

        url(r'^s5003-baseperapur/api/(?P<pk>[0-9]+)/$',
            s5003_baseperapur_views.s5003basePerApurDetail.as_view() ),

url(r'^s5003-baseperapur/listar/(?P<hash>.*)/$', 
        s5003_baseperapur_views.listar, 
        name='s5003_baseperapur'),

url(r'^s5003-baseperapur/salvar/(?P<hash>.*)/$', 
        s5003_baseperapur_views.salvar, 
        name='s5003_baseperapur_salvar'),



url(r'^s5003-dpsperante/apagar/(?P<hash>.*)/$', 
        s5003_dpsperante_views.apagar, 
        name='s5003_dpsperante_apagar'),

url(r'^s5003-dpsperante/api/$',
            s5003_dpsperante_views.s5003dpsPerAntEList.as_view() ),

        url(r'^s5003-dpsperante/api/(?P<pk>[0-9]+)/$',
            s5003_dpsperante_views.s5003dpsPerAntEDetail.as_view() ),

url(r'^s5003-dpsperante/listar/(?P<hash>.*)/$', 
        s5003_dpsperante_views.listar, 
        name='s5003_dpsperante'),

url(r'^s5003-dpsperante/salvar/(?P<hash>.*)/$', 
        s5003_dpsperante_views.salvar, 
        name='s5003_dpsperante_salvar'),



url(r'^s5003-dpsperapur/apagar/(?P<hash>.*)/$', 
        s5003_dpsperapur_views.apagar, 
        name='s5003_dpsperapur_apagar'),

url(r'^s5003-dpsperapur/api/$',
            s5003_dpsperapur_views.s5003dpsPerApurList.as_view() ),

        url(r'^s5003-dpsperapur/api/(?P<pk>[0-9]+)/$',
            s5003_dpsperapur_views.s5003dpsPerApurDetail.as_view() ),

url(r'^s5003-dpsperapur/listar/(?P<hash>.*)/$', 
        s5003_dpsperapur_views.listar, 
        name='s5003_dpsperapur'),

url(r'^s5003-dpsperapur/salvar/(?P<hash>.*)/$', 
        s5003_dpsperapur_views.salvar, 
        name='s5003_dpsperapur_salvar'),



url(r'^s5003-ideestablot/apagar/(?P<hash>.*)/$', 
        s5003_ideestablot_views.apagar, 
        name='s5003_ideestablot_apagar'),

url(r'^s5003-ideestablot/api/$',
            s5003_ideestablot_views.s5003ideEstabLotList.as_view() ),

        url(r'^s5003-ideestablot/api/(?P<pk>[0-9]+)/$',
            s5003_ideestablot_views.s5003ideEstabLotDetail.as_view() ),

url(r'^s5003-ideestablot/listar/(?P<hash>.*)/$', 
        s5003_ideestablot_views.listar, 
        name='s5003_ideestablot'),

url(r'^s5003-ideestablot/salvar/(?P<hash>.*)/$', 
        s5003_ideestablot_views.salvar, 
        name='s5003_ideestablot_salvar'),



url(r'^s5003-infobaseperante/apagar/(?P<hash>.*)/$', 
        s5003_infobaseperante_views.apagar, 
        name='s5003_infobaseperante_apagar'),

url(r'^s5003-infobaseperante/api/$',
            s5003_infobaseperante_views.s5003infoBasePerAntEList.as_view() ),

        url(r'^s5003-infobaseperante/api/(?P<pk>[0-9]+)/$',
            s5003_infobaseperante_views.s5003infoBasePerAntEDetail.as_view() ),

url(r'^s5003-infobaseperante/listar/(?P<hash>.*)/$', 
        s5003_infobaseperante_views.listar, 
        name='s5003_infobaseperante'),

url(r'^s5003-infobaseperante/salvar/(?P<hash>.*)/$', 
        s5003_infobaseperante_views.salvar, 
        name='s5003_infobaseperante_salvar'),



url(r'^s5003-infodpsperante/apagar/(?P<hash>.*)/$', 
        s5003_infodpsperante_views.apagar, 
        name='s5003_infodpsperante_apagar'),

url(r'^s5003-infodpsperante/api/$',
            s5003_infodpsperante_views.s5003infoDpsPerAntEList.as_view() ),

        url(r'^s5003-infodpsperante/api/(?P<pk>[0-9]+)/$',
            s5003_infodpsperante_views.s5003infoDpsPerAntEDetail.as_view() ),

url(r'^s5003-infodpsperante/listar/(?P<hash>.*)/$', 
        s5003_infodpsperante_views.listar, 
        name='s5003_infodpsperante'),

url(r'^s5003-infodpsperante/salvar/(?P<hash>.*)/$', 
        s5003_infodpsperante_views.salvar, 
        name='s5003_infodpsperante_salvar'),



url(r'^s5003-infofgts/apagar/(?P<hash>.*)/$', 
        s5003_infofgts_views.apagar, 
        name='s5003_infofgts_apagar'),

url(r'^s5003-infofgts/api/$',
            s5003_infofgts_views.s5003infoFGTSList.as_view() ),

        url(r'^s5003-infofgts/api/(?P<pk>[0-9]+)/$',
            s5003_infofgts_views.s5003infoFGTSDetail.as_view() ),

url(r'^s5003-infofgts/listar/(?P<hash>.*)/$', 
        s5003_infofgts_views.listar, 
        name='s5003_infofgts'),

url(r'^s5003-infofgts/salvar/(?P<hash>.*)/$', 
        s5003_infofgts_views.salvar, 
        name='s5003_infofgts_salvar'),



url(r'^s5003-infotrabdps/apagar/(?P<hash>.*)/$', 
        s5003_infotrabdps_views.apagar, 
        name='s5003_infotrabdps_apagar'),

url(r'^s5003-infotrabdps/api/$',
            s5003_infotrabdps_views.s5003infoTrabDpsList.as_view() ),

        url(r'^s5003-infotrabdps/api/(?P<pk>[0-9]+)/$',
            s5003_infotrabdps_views.s5003infoTrabDpsDetail.as_view() ),

url(r'^s5003-infotrabdps/listar/(?P<hash>.*)/$', 
        s5003_infotrabdps_views.listar, 
        name='s5003_infotrabdps'),

url(r'^s5003-infotrabdps/salvar/(?P<hash>.*)/$', 
        s5003_infotrabdps_views.salvar, 
        name='s5003_infotrabdps_salvar'),



url(r'^s5003-infotrabfgts/apagar/(?P<hash>.*)/$', 
        s5003_infotrabfgts_views.apagar, 
        name='s5003_infotrabfgts_apagar'),

url(r'^s5003-infotrabfgts/api/$',
            s5003_infotrabfgts_views.s5003infoTrabFGTSList.as_view() ),

        url(r'^s5003-infotrabfgts/api/(?P<pk>[0-9]+)/$',
            s5003_infotrabfgts_views.s5003infoTrabFGTSDetail.as_view() ),

url(r'^s5003-infotrabfgts/listar/(?P<hash>.*)/$', 
        s5003_infotrabfgts_views.listar, 
        name='s5003_infotrabfgts'),

url(r'^s5003-infotrabfgts/salvar/(?P<hash>.*)/$', 
        s5003_infotrabfgts_views.salvar, 
        name='s5003_infotrabfgts_salvar'),





]