#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s5001.views import s5001_calcterc as s5001_calcterc_views
from emensageriapro.s5001.views import s5001_ideestablot as s5001_ideestablot_views
from emensageriapro.s5001.views import s5001_infobasecs as s5001_infobasecs_views
from emensageriapro.s5001.views import s5001_infocategincid as s5001_infocategincid_views
from emensageriapro.s5001.views import s5001_infocpcalc as s5001_infocpcalc_views
from emensageriapro.s5001.views import s5001_procjudtrab as s5001_procjudtrab_views



"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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



url(r'^s5001-calcterc/apagar/(?P<hash>.*)/$', 
        s5001_calcterc_views.apagar, 
        name='s5001_calcterc_apagar'),

url(r'^s5001-calcterc/api/$',
            s5001_calcterc_views.s5001calcTercList.as_view() ),

        url(r'^s5001-calcterc/api/(?P<pk>[0-9]+)/$',
            s5001_calcterc_views.s5001calcTercDetail.as_view() ),

url(r'^s5001-calcterc/listar/(?P<hash>.*)/$', 
        s5001_calcterc_views.listar, 
        name='s5001_calcterc'),

url(r'^s5001-calcterc/salvar/(?P<hash>.*)/$', 
        s5001_calcterc_views.salvar, 
        name='s5001_calcterc_salvar'),



url(r'^s5001-ideestablot/apagar/(?P<hash>.*)/$', 
        s5001_ideestablot_views.apagar, 
        name='s5001_ideestablot_apagar'),

url(r'^s5001-ideestablot/api/$',
            s5001_ideestablot_views.s5001ideEstabLotList.as_view() ),

        url(r'^s5001-ideestablot/api/(?P<pk>[0-9]+)/$',
            s5001_ideestablot_views.s5001ideEstabLotDetail.as_view() ),

url(r'^s5001-ideestablot/listar/(?P<hash>.*)/$', 
        s5001_ideestablot_views.listar, 
        name='s5001_ideestablot'),

url(r'^s5001-ideestablot/salvar/(?P<hash>.*)/$', 
        s5001_ideestablot_views.salvar, 
        name='s5001_ideestablot_salvar'),



url(r'^s5001-infobasecs/apagar/(?P<hash>.*)/$', 
        s5001_infobasecs_views.apagar, 
        name='s5001_infobasecs_apagar'),

url(r'^s5001-infobasecs/api/$',
            s5001_infobasecs_views.s5001infoBaseCSList.as_view() ),

        url(r'^s5001-infobasecs/api/(?P<pk>[0-9]+)/$',
            s5001_infobasecs_views.s5001infoBaseCSDetail.as_view() ),

url(r'^s5001-infobasecs/listar/(?P<hash>.*)/$', 
        s5001_infobasecs_views.listar, 
        name='s5001_infobasecs'),

url(r'^s5001-infobasecs/salvar/(?P<hash>.*)/$', 
        s5001_infobasecs_views.salvar, 
        name='s5001_infobasecs_salvar'),



url(r'^s5001-infocategincid/apagar/(?P<hash>.*)/$', 
        s5001_infocategincid_views.apagar, 
        name='s5001_infocategincid_apagar'),

url(r'^s5001-infocategincid/api/$',
            s5001_infocategincid_views.s5001infoCategIncidList.as_view() ),

        url(r'^s5001-infocategincid/api/(?P<pk>[0-9]+)/$',
            s5001_infocategincid_views.s5001infoCategIncidDetail.as_view() ),

url(r'^s5001-infocategincid/listar/(?P<hash>.*)/$', 
        s5001_infocategincid_views.listar, 
        name='s5001_infocategincid'),

url(r'^s5001-infocategincid/salvar/(?P<hash>.*)/$', 
        s5001_infocategincid_views.salvar, 
        name='s5001_infocategincid_salvar'),



url(r'^s5001-infocpcalc/apagar/(?P<hash>.*)/$', 
        s5001_infocpcalc_views.apagar, 
        name='s5001_infocpcalc_apagar'),

url(r'^s5001-infocpcalc/api/$',
            s5001_infocpcalc_views.s5001infoCpCalcList.as_view() ),

        url(r'^s5001-infocpcalc/api/(?P<pk>[0-9]+)/$',
            s5001_infocpcalc_views.s5001infoCpCalcDetail.as_view() ),

url(r'^s5001-infocpcalc/listar/(?P<hash>.*)/$', 
        s5001_infocpcalc_views.listar, 
        name='s5001_infocpcalc'),

url(r'^s5001-infocpcalc/salvar/(?P<hash>.*)/$', 
        s5001_infocpcalc_views.salvar, 
        name='s5001_infocpcalc_salvar'),



url(r'^s5001-procjudtrab/apagar/(?P<hash>.*)/$', 
        s5001_procjudtrab_views.apagar, 
        name='s5001_procjudtrab_apagar'),

url(r'^s5001-procjudtrab/api/$',
            s5001_procjudtrab_views.s5001procJudTrabList.as_view() ),

        url(r'^s5001-procjudtrab/api/(?P<pk>[0-9]+)/$',
            s5001_procjudtrab_views.s5001procJudTrabDetail.as_view() ),

url(r'^s5001-procjudtrab/listar/(?P<hash>.*)/$', 
        s5001_procjudtrab_views.listar, 
        name='s5001_procjudtrab'),

url(r'^s5001-procjudtrab/salvar/(?P<hash>.*)/$', 
        s5001_procjudtrab_views.salvar, 
        name='s5001_procjudtrab_salvar'),





]