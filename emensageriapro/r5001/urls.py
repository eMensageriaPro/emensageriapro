#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r5001.views import r5001_rcprb as r5001_rcprb_views
from emensageriapro.r5001.views import r5001_rcoml as r5001_rcoml_views
from emensageriapro.r5001.views import r5001_rprest as r5001_rprest_views
from emensageriapro.r5001.views import r5001_rrecespetdesp as r5001_rrecespetdesp_views
from emensageriapro.r5001.views import r5001_rrecrepad as r5001_rrecrepad_views
from emensageriapro.r5001.views import r5001_rtom as r5001_rtom_views
from emensageriapro.r5001.views import r5001_infocrtom as r5001_infocrtom_views
from emensageriapro.r5001.views import r5001_infototal as r5001_infototal_views
from emensageriapro.r5001.views import r5001_regocorrs as r5001_regocorrs_views



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



url(r'^r5001-rcprb/apagar/(?P<hash>.*)/$', 
        r5001_rcprb_views.apagar, 
        name='r5001_rcprb_apagar'),

url(r'^r5001-rcprb/api/$',
            r5001_rcprb_views.r5001RCPRBList.as_view() ),

        url(r'^r5001-rcprb/api/(?P<pk>[0-9]+)/$',
            r5001_rcprb_views.r5001RCPRBDetail.as_view() ),

url(r'^r5001-rcprb/listar/(?P<hash>.*)/$', 
        r5001_rcprb_views.listar, 
        name='r5001_rcprb'),

url(r'^r5001-rcprb/salvar/(?P<hash>.*)/$', 
        r5001_rcprb_views.salvar, 
        name='r5001_rcprb_salvar'),



url(r'^r5001-rcoml/apagar/(?P<hash>.*)/$', 
        r5001_rcoml_views.apagar, 
        name='r5001_rcoml_apagar'),

url(r'^r5001-rcoml/api/$',
            r5001_rcoml_views.r5001RComlList.as_view() ),

        url(r'^r5001-rcoml/api/(?P<pk>[0-9]+)/$',
            r5001_rcoml_views.r5001RComlDetail.as_view() ),

url(r'^r5001-rcoml/listar/(?P<hash>.*)/$', 
        r5001_rcoml_views.listar, 
        name='r5001_rcoml'),

url(r'^r5001-rcoml/salvar/(?P<hash>.*)/$', 
        r5001_rcoml_views.salvar, 
        name='r5001_rcoml_salvar'),



url(r'^r5001-rprest/apagar/(?P<hash>.*)/$', 
        r5001_rprest_views.apagar, 
        name='r5001_rprest_apagar'),

url(r'^r5001-rprest/api/$',
            r5001_rprest_views.r5001RPrestList.as_view() ),

        url(r'^r5001-rprest/api/(?P<pk>[0-9]+)/$',
            r5001_rprest_views.r5001RPrestDetail.as_view() ),

url(r'^r5001-rprest/listar/(?P<hash>.*)/$', 
        r5001_rprest_views.listar, 
        name='r5001_rprest'),

url(r'^r5001-rprest/salvar/(?P<hash>.*)/$', 
        r5001_rprest_views.salvar, 
        name='r5001_rprest_salvar'),



url(r'^r5001-rrecespetdesp/apagar/(?P<hash>.*)/$', 
        r5001_rrecespetdesp_views.apagar, 
        name='r5001_rrecespetdesp_apagar'),

url(r'^r5001-rrecespetdesp/api/$',
            r5001_rrecespetdesp_views.r5001RRecEspetDespList.as_view() ),

        url(r'^r5001-rrecespetdesp/api/(?P<pk>[0-9]+)/$',
            r5001_rrecespetdesp_views.r5001RRecEspetDespDetail.as_view() ),

url(r'^r5001-rrecespetdesp/listar/(?P<hash>.*)/$', 
        r5001_rrecespetdesp_views.listar, 
        name='r5001_rrecespetdesp'),

url(r'^r5001-rrecespetdesp/salvar/(?P<hash>.*)/$', 
        r5001_rrecespetdesp_views.salvar, 
        name='r5001_rrecespetdesp_salvar'),



url(r'^r5001-rrecrepad/apagar/(?P<hash>.*)/$', 
        r5001_rrecrepad_views.apagar, 
        name='r5001_rrecrepad_apagar'),

url(r'^r5001-rrecrepad/api/$',
            r5001_rrecrepad_views.r5001RRecRepADList.as_view() ),

        url(r'^r5001-rrecrepad/api/(?P<pk>[0-9]+)/$',
            r5001_rrecrepad_views.r5001RRecRepADDetail.as_view() ),

url(r'^r5001-rrecrepad/listar/(?P<hash>.*)/$', 
        r5001_rrecrepad_views.listar, 
        name='r5001_rrecrepad'),

url(r'^r5001-rrecrepad/salvar/(?P<hash>.*)/$', 
        r5001_rrecrepad_views.salvar, 
        name='r5001_rrecrepad_salvar'),



url(r'^r5001-rtom/apagar/(?P<hash>.*)/$', 
        r5001_rtom_views.apagar, 
        name='r5001_rtom_apagar'),

url(r'^r5001-rtom/api/$',
            r5001_rtom_views.r5001RTomList.as_view() ),

        url(r'^r5001-rtom/api/(?P<pk>[0-9]+)/$',
            r5001_rtom_views.r5001RTomDetail.as_view() ),

url(r'^r5001-rtom/listar/(?P<hash>.*)/$', 
        r5001_rtom_views.listar, 
        name='r5001_rtom'),

url(r'^r5001-rtom/salvar/(?P<hash>.*)/$', 
        r5001_rtom_views.salvar, 
        name='r5001_rtom_salvar'),



url(r'^r5001-infocrtom/apagar/(?P<hash>.*)/$', 
        r5001_infocrtom_views.apagar, 
        name='r5001_infocrtom_apagar'),

url(r'^r5001-infocrtom/api/$',
            r5001_infocrtom_views.r5001infoCRTomList.as_view() ),

        url(r'^r5001-infocrtom/api/(?P<pk>[0-9]+)/$',
            r5001_infocrtom_views.r5001infoCRTomDetail.as_view() ),

url(r'^r5001-infocrtom/listar/(?P<hash>.*)/$', 
        r5001_infocrtom_views.listar, 
        name='r5001_infocrtom'),

url(r'^r5001-infocrtom/salvar/(?P<hash>.*)/$', 
        r5001_infocrtom_views.salvar, 
        name='r5001_infocrtom_salvar'),



url(r'^r5001-infototal/apagar/(?P<hash>.*)/$', 
        r5001_infototal_views.apagar, 
        name='r5001_infototal_apagar'),

url(r'^r5001-infototal/api/$',
            r5001_infototal_views.r5001infoTotalList.as_view() ),

        url(r'^r5001-infototal/api/(?P<pk>[0-9]+)/$',
            r5001_infototal_views.r5001infoTotalDetail.as_view() ),

url(r'^r5001-infototal/listar/(?P<hash>.*)/$', 
        r5001_infototal_views.listar, 
        name='r5001_infototal'),

url(r'^r5001-infototal/salvar/(?P<hash>.*)/$', 
        r5001_infototal_views.salvar, 
        name='r5001_infototal_salvar'),



url(r'^r5001-regocorrs/apagar/(?P<hash>.*)/$', 
        r5001_regocorrs_views.apagar, 
        name='r5001_regocorrs_apagar'),

url(r'^r5001-regocorrs/api/$',
            r5001_regocorrs_views.r5001regOcorrsList.as_view() ),

        url(r'^r5001-regocorrs/api/(?P<pk>[0-9]+)/$',
            r5001_regocorrs_views.r5001regOcorrsDetail.as_view() ),

url(r'^r5001-regocorrs/listar/(?P<hash>.*)/$', 
        r5001_regocorrs_views.listar, 
        name='r5001_regocorrs'),

url(r'^r5001-regocorrs/salvar/(?P<hash>.*)/$', 
        r5001_regocorrs_views.salvar, 
        name='r5001_regocorrs_salvar'),





]