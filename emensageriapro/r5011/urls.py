#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r5011.views import r5011_rcprb as r5011_rcprb_views
from emensageriapro.r5011.views import r5011_rcoml as r5011_rcoml_views
from emensageriapro.r5011.views import r5011_rprest as r5011_rprest_views
from emensageriapro.r5011.views import r5011_rrecrepad as r5011_rrecrepad_views
from emensageriapro.r5011.views import r5011_rtom as r5011_rtom_views
from emensageriapro.r5011.views import r5011_infocrtom as r5011_infocrtom_views
from emensageriapro.r5011.views import r5011_infototalcontrib as r5011_infototalcontrib_views
from emensageriapro.r5011.views import r5011_regocorrs as r5011_regocorrs_views



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



url(r'^r5011-rcprb/apagar/(?P<hash>.*)/$', 
        r5011_rcprb_views.apagar, 
        name='r5011_rcprb_apagar'),

url(r'^r5011-rcprb/api/$',
            r5011_rcprb_views.r5011RCPRBList.as_view() ),

        url(r'^r5011-rcprb/api/(?P<pk>[0-9]+)/$',
            r5011_rcprb_views.r5011RCPRBDetail.as_view() ),

url(r'^r5011-rcprb/listar/(?P<hash>.*)/$', 
        r5011_rcprb_views.listar, 
        name='r5011_rcprb'),

url(r'^r5011-rcprb/salvar/(?P<hash>.*)/$', 
        r5011_rcprb_views.salvar, 
        name='r5011_rcprb_salvar'),



url(r'^r5011-rcoml/apagar/(?P<hash>.*)/$', 
        r5011_rcoml_views.apagar, 
        name='r5011_rcoml_apagar'),

url(r'^r5011-rcoml/api/$',
            r5011_rcoml_views.r5011RComlList.as_view() ),

        url(r'^r5011-rcoml/api/(?P<pk>[0-9]+)/$',
            r5011_rcoml_views.r5011RComlDetail.as_view() ),

url(r'^r5011-rcoml/listar/(?P<hash>.*)/$', 
        r5011_rcoml_views.listar, 
        name='r5011_rcoml'),

url(r'^r5011-rcoml/salvar/(?P<hash>.*)/$', 
        r5011_rcoml_views.salvar, 
        name='r5011_rcoml_salvar'),



url(r'^r5011-rprest/apagar/(?P<hash>.*)/$', 
        r5011_rprest_views.apagar, 
        name='r5011_rprest_apagar'),

url(r'^r5011-rprest/api/$',
            r5011_rprest_views.r5011RPrestList.as_view() ),

        url(r'^r5011-rprest/api/(?P<pk>[0-9]+)/$',
            r5011_rprest_views.r5011RPrestDetail.as_view() ),

url(r'^r5011-rprest/listar/(?P<hash>.*)/$', 
        r5011_rprest_views.listar, 
        name='r5011_rprest'),

url(r'^r5011-rprest/salvar/(?P<hash>.*)/$', 
        r5011_rprest_views.salvar, 
        name='r5011_rprest_salvar'),



url(r'^r5011-rrecrepad/apagar/(?P<hash>.*)/$', 
        r5011_rrecrepad_views.apagar, 
        name='r5011_rrecrepad_apagar'),

url(r'^r5011-rrecrepad/api/$',
            r5011_rrecrepad_views.r5011RRecRepADList.as_view() ),

        url(r'^r5011-rrecrepad/api/(?P<pk>[0-9]+)/$',
            r5011_rrecrepad_views.r5011RRecRepADDetail.as_view() ),

url(r'^r5011-rrecrepad/listar/(?P<hash>.*)/$', 
        r5011_rrecrepad_views.listar, 
        name='r5011_rrecrepad'),

url(r'^r5011-rrecrepad/salvar/(?P<hash>.*)/$', 
        r5011_rrecrepad_views.salvar, 
        name='r5011_rrecrepad_salvar'),



url(r'^r5011-rtom/apagar/(?P<hash>.*)/$', 
        r5011_rtom_views.apagar, 
        name='r5011_rtom_apagar'),

url(r'^r5011-rtom/api/$',
            r5011_rtom_views.r5011RTomList.as_view() ),

        url(r'^r5011-rtom/api/(?P<pk>[0-9]+)/$',
            r5011_rtom_views.r5011RTomDetail.as_view() ),

url(r'^r5011-rtom/listar/(?P<hash>.*)/$', 
        r5011_rtom_views.listar, 
        name='r5011_rtom'),

url(r'^r5011-rtom/salvar/(?P<hash>.*)/$', 
        r5011_rtom_views.salvar, 
        name='r5011_rtom_salvar'),



url(r'^r5011-infocrtom/apagar/(?P<hash>.*)/$', 
        r5011_infocrtom_views.apagar, 
        name='r5011_infocrtom_apagar'),

url(r'^r5011-infocrtom/api/$',
            r5011_infocrtom_views.r5011infoCRTomList.as_view() ),

        url(r'^r5011-infocrtom/api/(?P<pk>[0-9]+)/$',
            r5011_infocrtom_views.r5011infoCRTomDetail.as_view() ),

url(r'^r5011-infocrtom/listar/(?P<hash>.*)/$', 
        r5011_infocrtom_views.listar, 
        name='r5011_infocrtom'),

url(r'^r5011-infocrtom/salvar/(?P<hash>.*)/$', 
        r5011_infocrtom_views.salvar, 
        name='r5011_infocrtom_salvar'),



url(r'^r5011-infototalcontrib/apagar/(?P<hash>.*)/$', 
        r5011_infototalcontrib_views.apagar, 
        name='r5011_infototalcontrib_apagar'),

url(r'^r5011-infototalcontrib/api/$',
            r5011_infototalcontrib_views.r5011infoTotalContribList.as_view() ),

        url(r'^r5011-infototalcontrib/api/(?P<pk>[0-9]+)/$',
            r5011_infototalcontrib_views.r5011infoTotalContribDetail.as_view() ),

url(r'^r5011-infototalcontrib/listar/(?P<hash>.*)/$', 
        r5011_infototalcontrib_views.listar, 
        name='r5011_infototalcontrib'),

url(r'^r5011-infototalcontrib/salvar/(?P<hash>.*)/$', 
        r5011_infototalcontrib_views.salvar, 
        name='r5011_infototalcontrib_salvar'),



url(r'^r5011-regocorrs/apagar/(?P<hash>.*)/$', 
        r5011_regocorrs_views.apagar, 
        name='r5011_regocorrs_apagar'),

url(r'^r5011-regocorrs/api/$',
            r5011_regocorrs_views.r5011regOcorrsList.as_view() ),

        url(r'^r5011-regocorrs/api/(?P<pk>[0-9]+)/$',
            r5011_regocorrs_views.r5011regOcorrsDetail.as_view() ),

url(r'^r5011-regocorrs/listar/(?P<hash>.*)/$', 
        r5011_regocorrs_views.listar, 
        name='r5011_regocorrs'),

url(r'^r5011-regocorrs/salvar/(?P<hash>.*)/$', 
        r5011_regocorrs_views.salvar, 
        name='r5011_regocorrs_salvar'),





]