#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r9011.views import r9011_regocorrs_apagar as r9011_regocorrs_apagar_views
from emensageriapro.r9011.views import r9011_regocorrs_listar as r9011_regocorrs_listar_views
from emensageriapro.r9011.views import r9011_regocorrs_salvar as r9011_regocorrs_salvar_views
from emensageriapro.r9011.views import r9011_regocorrs_api as r9011_regocorrs_api_views
from emensageriapro.r9011.views import r9011_infototalcontrib_apagar as r9011_infototalcontrib_apagar_views
from emensageriapro.r9011.views import r9011_infototalcontrib_listar as r9011_infototalcontrib_listar_views
from emensageriapro.r9011.views import r9011_infototalcontrib_salvar as r9011_infototalcontrib_salvar_views
from emensageriapro.r9011.views import r9011_infototalcontrib_api as r9011_infototalcontrib_api_views
from emensageriapro.r9011.views import r9011_rtom_apagar as r9011_rtom_apagar_views
from emensageriapro.r9011.views import r9011_rtom_listar as r9011_rtom_listar_views
from emensageriapro.r9011.views import r9011_rtom_salvar as r9011_rtom_salvar_views
from emensageriapro.r9011.views import r9011_rtom_api as r9011_rtom_api_views
from emensageriapro.r9011.views import r9011_infocrtom_apagar as r9011_infocrtom_apagar_views
from emensageriapro.r9011.views import r9011_infocrtom_listar as r9011_infocrtom_listar_views
from emensageriapro.r9011.views import r9011_infocrtom_salvar as r9011_infocrtom_salvar_views
from emensageriapro.r9011.views import r9011_infocrtom_api as r9011_infocrtom_api_views
from emensageriapro.r9011.views import r9011_rprest_apagar as r9011_rprest_apagar_views
from emensageriapro.r9011.views import r9011_rprest_listar as r9011_rprest_listar_views
from emensageriapro.r9011.views import r9011_rprest_salvar as r9011_rprest_salvar_views
from emensageriapro.r9011.views import r9011_rprest_api as r9011_rprest_api_views
from emensageriapro.r9011.views import r9011_rrecrepad_apagar as r9011_rrecrepad_apagar_views
from emensageriapro.r9011.views import r9011_rrecrepad_listar as r9011_rrecrepad_listar_views
from emensageriapro.r9011.views import r9011_rrecrepad_salvar as r9011_rrecrepad_salvar_views
from emensageriapro.r9011.views import r9011_rrecrepad_api as r9011_rrecrepad_api_views
from emensageriapro.r9011.views import r9011_rcoml_apagar as r9011_rcoml_apagar_views
from emensageriapro.r9011.views import r9011_rcoml_listar as r9011_rcoml_listar_views
from emensageriapro.r9011.views import r9011_rcoml_salvar as r9011_rcoml_salvar_views
from emensageriapro.r9011.views import r9011_rcoml_api as r9011_rcoml_api_views
from emensageriapro.r9011.views import r9011_rcprb_apagar as r9011_rcprb_apagar_views
from emensageriapro.r9011.views import r9011_rcprb_listar as r9011_rcprb_listar_views
from emensageriapro.r9011.views import r9011_rcprb_salvar as r9011_rcprb_salvar_views
from emensageriapro.r9011.views import r9011_rcprb_api as r9011_rcprb_api_views



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


    url(r'^r9011-regocorrs/apagar/(?P<pk>[0-9]+)/$', 
        r9011_regocorrs_apagar_views.apagar, 
        name='r9011_regocorrs_apagar'),

    url(r'^r9011-regocorrs/api/$',
        r9011_regocorrs_api_views.r9011regOcorrsList.as_view() ),

    url(r'^r9011-regocorrs/api/(?P<pk>[0-9]+)/$',
        r9011_regocorrs_api_views.r9011regOcorrsDetail.as_view() ),

    url(r'^r9011-regocorrs/$', 
        r9011_regocorrs_listar_views.listar, 
        name='r9011_regocorrs'),

    url(r'^r9011-regocorrs/salvar/(?P<pk>[0-9]+)/$', 
        r9011_regocorrs_salvar_views.salvar, 
        name='r9011_regocorrs_salvar'),

    url(r'^r9011-regocorrs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r9011_regocorrs_salvar_views.salvar, 
        name='r9011_regocorrs_salvar_tab'),
        
    url(r'^r9011-regocorrs/cadastrar/$', 
        r9011_regocorrs_salvar_views.salvar, 
        name='r9011_regocorrs_cadastrar'),

    url(r'^r9011-regocorrs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r9011_regocorrs_salvar_views.salvar, 
        name='r9011_regocorrs_salvar_output'),
        
    url(r'^r9011-regocorrs/(?P<output>[\w-]+)/$', 
        r9011_regocorrs_listar_views.listar, 
        name='r9011_regocorrs_output'),

    url(r'^r9011-infototalcontrib/apagar/(?P<pk>[0-9]+)/$', 
        r9011_infototalcontrib_apagar_views.apagar, 
        name='r9011_infototalcontrib_apagar'),

    url(r'^r9011-infototalcontrib/api/$',
        r9011_infototalcontrib_api_views.r9011infoTotalContribList.as_view() ),

    url(r'^r9011-infototalcontrib/api/(?P<pk>[0-9]+)/$',
        r9011_infototalcontrib_api_views.r9011infoTotalContribDetail.as_view() ),

    url(r'^r9011-infototalcontrib/$', 
        r9011_infototalcontrib_listar_views.listar, 
        name='r9011_infototalcontrib'),

    url(r'^r9011-infototalcontrib/salvar/(?P<pk>[0-9]+)/$', 
        r9011_infototalcontrib_salvar_views.salvar, 
        name='r9011_infototalcontrib_salvar'),

    url(r'^r9011-infototalcontrib/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r9011_infototalcontrib_salvar_views.salvar, 
        name='r9011_infototalcontrib_salvar_tab'),
        
    url(r'^r9011-infototalcontrib/cadastrar/$', 
        r9011_infototalcontrib_salvar_views.salvar, 
        name='r9011_infototalcontrib_cadastrar'),

    url(r'^r9011-infototalcontrib/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r9011_infototalcontrib_salvar_views.salvar, 
        name='r9011_infototalcontrib_salvar_output'),
        
    url(r'^r9011-infototalcontrib/(?P<output>[\w-]+)/$', 
        r9011_infototalcontrib_listar_views.listar, 
        name='r9011_infototalcontrib_output'),

    url(r'^r9011-rtom/apagar/(?P<pk>[0-9]+)/$', 
        r9011_rtom_apagar_views.apagar, 
        name='r9011_rtom_apagar'),

    url(r'^r9011-rtom/api/$',
        r9011_rtom_api_views.r9011RTomList.as_view() ),

    url(r'^r9011-rtom/api/(?P<pk>[0-9]+)/$',
        r9011_rtom_api_views.r9011RTomDetail.as_view() ),

    url(r'^r9011-rtom/$', 
        r9011_rtom_listar_views.listar, 
        name='r9011_rtom'),

    url(r'^r9011-rtom/salvar/(?P<pk>[0-9]+)/$', 
        r9011_rtom_salvar_views.salvar, 
        name='r9011_rtom_salvar'),

    url(r'^r9011-rtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r9011_rtom_salvar_views.salvar, 
        name='r9011_rtom_salvar_tab'),
        
    url(r'^r9011-rtom/cadastrar/$', 
        r9011_rtom_salvar_views.salvar, 
        name='r9011_rtom_cadastrar'),

    url(r'^r9011-rtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r9011_rtom_salvar_views.salvar, 
        name='r9011_rtom_salvar_output'),
        
    url(r'^r9011-rtom/(?P<output>[\w-]+)/$', 
        r9011_rtom_listar_views.listar, 
        name='r9011_rtom_output'),

    url(r'^r9011-infocrtom/apagar/(?P<pk>[0-9]+)/$', 
        r9011_infocrtom_apagar_views.apagar, 
        name='r9011_infocrtom_apagar'),

    url(r'^r9011-infocrtom/api/$',
        r9011_infocrtom_api_views.r9011infoCRTomList.as_view() ),

    url(r'^r9011-infocrtom/api/(?P<pk>[0-9]+)/$',
        r9011_infocrtom_api_views.r9011infoCRTomDetail.as_view() ),

    url(r'^r9011-infocrtom/$', 
        r9011_infocrtom_listar_views.listar, 
        name='r9011_infocrtom'),

    url(r'^r9011-infocrtom/salvar/(?P<pk>[0-9]+)/$', 
        r9011_infocrtom_salvar_views.salvar, 
        name='r9011_infocrtom_salvar'),

    url(r'^r9011-infocrtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r9011_infocrtom_salvar_views.salvar, 
        name='r9011_infocrtom_salvar_tab'),
        
    url(r'^r9011-infocrtom/cadastrar/$', 
        r9011_infocrtom_salvar_views.salvar, 
        name='r9011_infocrtom_cadastrar'),

    url(r'^r9011-infocrtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r9011_infocrtom_salvar_views.salvar, 
        name='r9011_infocrtom_salvar_output'),
        
    url(r'^r9011-infocrtom/(?P<output>[\w-]+)/$', 
        r9011_infocrtom_listar_views.listar, 
        name='r9011_infocrtom_output'),

    url(r'^r9011-rprest/apagar/(?P<pk>[0-9]+)/$', 
        r9011_rprest_apagar_views.apagar, 
        name='r9011_rprest_apagar'),

    url(r'^r9011-rprest/api/$',
        r9011_rprest_api_views.r9011RPrestList.as_view() ),

    url(r'^r9011-rprest/api/(?P<pk>[0-9]+)/$',
        r9011_rprest_api_views.r9011RPrestDetail.as_view() ),

    url(r'^r9011-rprest/$', 
        r9011_rprest_listar_views.listar, 
        name='r9011_rprest'),

    url(r'^r9011-rprest/salvar/(?P<pk>[0-9]+)/$', 
        r9011_rprest_salvar_views.salvar, 
        name='r9011_rprest_salvar'),

    url(r'^r9011-rprest/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r9011_rprest_salvar_views.salvar, 
        name='r9011_rprest_salvar_tab'),
        
    url(r'^r9011-rprest/cadastrar/$', 
        r9011_rprest_salvar_views.salvar, 
        name='r9011_rprest_cadastrar'),

    url(r'^r9011-rprest/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r9011_rprest_salvar_views.salvar, 
        name='r9011_rprest_salvar_output'),
        
    url(r'^r9011-rprest/(?P<output>[\w-]+)/$', 
        r9011_rprest_listar_views.listar, 
        name='r9011_rprest_output'),

    url(r'^r9011-rrecrepad/apagar/(?P<pk>[0-9]+)/$', 
        r9011_rrecrepad_apagar_views.apagar, 
        name='r9011_rrecrepad_apagar'),

    url(r'^r9011-rrecrepad/api/$',
        r9011_rrecrepad_api_views.r9011RRecRepADList.as_view() ),

    url(r'^r9011-rrecrepad/api/(?P<pk>[0-9]+)/$',
        r9011_rrecrepad_api_views.r9011RRecRepADDetail.as_view() ),

    url(r'^r9011-rrecrepad/$', 
        r9011_rrecrepad_listar_views.listar, 
        name='r9011_rrecrepad'),

    url(r'^r9011-rrecrepad/salvar/(?P<pk>[0-9]+)/$', 
        r9011_rrecrepad_salvar_views.salvar, 
        name='r9011_rrecrepad_salvar'),

    url(r'^r9011-rrecrepad/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r9011_rrecrepad_salvar_views.salvar, 
        name='r9011_rrecrepad_salvar_tab'),
        
    url(r'^r9011-rrecrepad/cadastrar/$', 
        r9011_rrecrepad_salvar_views.salvar, 
        name='r9011_rrecrepad_cadastrar'),

    url(r'^r9011-rrecrepad/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r9011_rrecrepad_salvar_views.salvar, 
        name='r9011_rrecrepad_salvar_output'),
        
    url(r'^r9011-rrecrepad/(?P<output>[\w-]+)/$', 
        r9011_rrecrepad_listar_views.listar, 
        name='r9011_rrecrepad_output'),

    url(r'^r9011-rcoml/apagar/(?P<pk>[0-9]+)/$', 
        r9011_rcoml_apagar_views.apagar, 
        name='r9011_rcoml_apagar'),

    url(r'^r9011-rcoml/api/$',
        r9011_rcoml_api_views.r9011RComlList.as_view() ),

    url(r'^r9011-rcoml/api/(?P<pk>[0-9]+)/$',
        r9011_rcoml_api_views.r9011RComlDetail.as_view() ),

    url(r'^r9011-rcoml/$', 
        r9011_rcoml_listar_views.listar, 
        name='r9011_rcoml'),

    url(r'^r9011-rcoml/salvar/(?P<pk>[0-9]+)/$', 
        r9011_rcoml_salvar_views.salvar, 
        name='r9011_rcoml_salvar'),

    url(r'^r9011-rcoml/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r9011_rcoml_salvar_views.salvar, 
        name='r9011_rcoml_salvar_tab'),
        
    url(r'^r9011-rcoml/cadastrar/$', 
        r9011_rcoml_salvar_views.salvar, 
        name='r9011_rcoml_cadastrar'),

    url(r'^r9011-rcoml/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r9011_rcoml_salvar_views.salvar, 
        name='r9011_rcoml_salvar_output'),
        
    url(r'^r9011-rcoml/(?P<output>[\w-]+)/$', 
        r9011_rcoml_listar_views.listar, 
        name='r9011_rcoml_output'),

    url(r'^r9011-rcprb/apagar/(?P<pk>[0-9]+)/$', 
        r9011_rcprb_apagar_views.apagar, 
        name='r9011_rcprb_apagar'),

    url(r'^r9011-rcprb/api/$',
        r9011_rcprb_api_views.r9011RCPRBList.as_view() ),

    url(r'^r9011-rcprb/api/(?P<pk>[0-9]+)/$',
        r9011_rcprb_api_views.r9011RCPRBDetail.as_view() ),

    url(r'^r9011-rcprb/$', 
        r9011_rcprb_listar_views.listar, 
        name='r9011_rcprb'),

    url(r'^r9011-rcprb/salvar/(?P<pk>[0-9]+)/$', 
        r9011_rcprb_salvar_views.salvar, 
        name='r9011_rcprb_salvar'),

    url(r'^r9011-rcprb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r9011_rcprb_salvar_views.salvar, 
        name='r9011_rcprb_salvar_tab'),
        
    url(r'^r9011-rcprb/cadastrar/$', 
        r9011_rcprb_salvar_views.salvar, 
        name='r9011_rcprb_cadastrar'),

    url(r'^r9011-rcprb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r9011_rcprb_salvar_views.salvar, 
        name='r9011_rcprb_salvar_output'),
        
    url(r'^r9011-rcprb/(?P<output>[\w-]+)/$', 
        r9011_rcprb_listar_views.listar, 
        name='r9011_rcprb_output'),


]