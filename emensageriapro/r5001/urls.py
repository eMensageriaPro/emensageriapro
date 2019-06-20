#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r5001.views import r5001_regocorrs_apagar as r5001_regocorrs_apagar_views
from emensageriapro.r5001.views import r5001_regocorrs_listar as r5001_regocorrs_listar_views
from emensageriapro.r5001.views import r5001_regocorrs_salvar as r5001_regocorrs_salvar_views
from emensageriapro.r5001.views import r5001_regocorrs_api as r5001_regocorrs_api_views
from emensageriapro.r5001.views import r5001_infototal_apagar as r5001_infototal_apagar_views
from emensageriapro.r5001.views import r5001_infototal_listar as r5001_infototal_listar_views
from emensageriapro.r5001.views import r5001_infototal_salvar as r5001_infototal_salvar_views
from emensageriapro.r5001.views import r5001_infototal_api as r5001_infototal_api_views
from emensageriapro.r5001.views import r5001_rtom_apagar as r5001_rtom_apagar_views
from emensageriapro.r5001.views import r5001_rtom_listar as r5001_rtom_listar_views
from emensageriapro.r5001.views import r5001_rtom_salvar as r5001_rtom_salvar_views
from emensageriapro.r5001.views import r5001_rtom_api as r5001_rtom_api_views
from emensageriapro.r5001.views import r5001_infocrtom_apagar as r5001_infocrtom_apagar_views
from emensageriapro.r5001.views import r5001_infocrtom_listar as r5001_infocrtom_listar_views
from emensageriapro.r5001.views import r5001_infocrtom_salvar as r5001_infocrtom_salvar_views
from emensageriapro.r5001.views import r5001_infocrtom_api as r5001_infocrtom_api_views
from emensageriapro.r5001.views import r5001_rprest_apagar as r5001_rprest_apagar_views
from emensageriapro.r5001.views import r5001_rprest_listar as r5001_rprest_listar_views
from emensageriapro.r5001.views import r5001_rprest_salvar as r5001_rprest_salvar_views
from emensageriapro.r5001.views import r5001_rprest_api as r5001_rprest_api_views
from emensageriapro.r5001.views import r5001_rrecrepad_apagar as r5001_rrecrepad_apagar_views
from emensageriapro.r5001.views import r5001_rrecrepad_listar as r5001_rrecrepad_listar_views
from emensageriapro.r5001.views import r5001_rrecrepad_salvar as r5001_rrecrepad_salvar_views
from emensageriapro.r5001.views import r5001_rrecrepad_api as r5001_rrecrepad_api_views
from emensageriapro.r5001.views import r5001_rcoml_apagar as r5001_rcoml_apagar_views
from emensageriapro.r5001.views import r5001_rcoml_listar as r5001_rcoml_listar_views
from emensageriapro.r5001.views import r5001_rcoml_salvar as r5001_rcoml_salvar_views
from emensageriapro.r5001.views import r5001_rcoml_api as r5001_rcoml_api_views
from emensageriapro.r5001.views import r5001_rcprb_apagar as r5001_rcprb_apagar_views
from emensageriapro.r5001.views import r5001_rcprb_listar as r5001_rcprb_listar_views
from emensageriapro.r5001.views import r5001_rcprb_salvar as r5001_rcprb_salvar_views
from emensageriapro.r5001.views import r5001_rcprb_api as r5001_rcprb_api_views
from emensageriapro.r5001.views import r5001_rrecespetdesp_apagar as r5001_rrecespetdesp_apagar_views
from emensageriapro.r5001.views import r5001_rrecespetdesp_listar as r5001_rrecespetdesp_listar_views
from emensageriapro.r5001.views import r5001_rrecespetdesp_salvar as r5001_rrecespetdesp_salvar_views
from emensageriapro.r5001.views import r5001_rrecespetdesp_api as r5001_rrecespetdesp_api_views



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


    url(r'^r5001-regocorrs/apagar/(?P<pk>[0-9]+)/$', 
        r5001_regocorrs_apagar_views.apagar, 
        name='r5001_regocorrs_apagar'),

    url(r'^r5001-regocorrs/api/$',
        r5001_regocorrs_api_views.r5001regOcorrsList.as_view() ),

    url(r'^r5001-regocorrs/api/(?P<pk>[0-9]+)/$',
        r5001_regocorrs_api_views.r5001regOcorrsDetail.as_view() ),

    url(r'^r5001-regocorrs/$', 
        r5001_regocorrs_listar_views.listar, 
        name='r5001_regocorrs'),

    url(r'^r5001-regocorrs/salvar/(?P<pk>[0-9]+)/$', 
        r5001_regocorrs_salvar_views.salvar, 
        name='r5001_regocorrs_salvar'),

    url(r'^r5001-regocorrs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r5001_regocorrs_salvar_views.salvar, 
        name='r5001_regocorrs_salvar_tab'),
        
    url(r'^r5001-regocorrs/cadastrar/$', 
        r5001_regocorrs_salvar_views.salvar, 
        name='r5001_regocorrs_cadastrar'),

    url(r'^r5001-regocorrs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r5001_regocorrs_salvar_views.salvar, 
        name='r5001_regocorrs_salvar_output'),
        
    url(r'^r5001-regocorrs/(?P<output>[\w-]+)/$', 
        r5001_regocorrs_listar_views.listar, 
        name='r5001_regocorrs_output'),

    url(r'^r5001-infototal/apagar/(?P<pk>[0-9]+)/$', 
        r5001_infototal_apagar_views.apagar, 
        name='r5001_infototal_apagar'),

    url(r'^r5001-infototal/api/$',
        r5001_infototal_api_views.r5001infoTotalList.as_view() ),

    url(r'^r5001-infototal/api/(?P<pk>[0-9]+)/$',
        r5001_infototal_api_views.r5001infoTotalDetail.as_view() ),

    url(r'^r5001-infototal/$', 
        r5001_infototal_listar_views.listar, 
        name='r5001_infototal'),

    url(r'^r5001-infototal/salvar/(?P<pk>[0-9]+)/$', 
        r5001_infototal_salvar_views.salvar, 
        name='r5001_infototal_salvar'),

    url(r'^r5001-infototal/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r5001_infototal_salvar_views.salvar, 
        name='r5001_infototal_salvar_tab'),
        
    url(r'^r5001-infototal/cadastrar/$', 
        r5001_infototal_salvar_views.salvar, 
        name='r5001_infototal_cadastrar'),

    url(r'^r5001-infototal/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r5001_infototal_salvar_views.salvar, 
        name='r5001_infototal_salvar_output'),
        
    url(r'^r5001-infototal/(?P<output>[\w-]+)/$', 
        r5001_infototal_listar_views.listar, 
        name='r5001_infototal_output'),

    url(r'^r5001-rtom/apagar/(?P<pk>[0-9]+)/$', 
        r5001_rtom_apagar_views.apagar, 
        name='r5001_rtom_apagar'),

    url(r'^r5001-rtom/api/$',
        r5001_rtom_api_views.r5001RTomList.as_view() ),

    url(r'^r5001-rtom/api/(?P<pk>[0-9]+)/$',
        r5001_rtom_api_views.r5001RTomDetail.as_view() ),

    url(r'^r5001-rtom/$', 
        r5001_rtom_listar_views.listar, 
        name='r5001_rtom'),

    url(r'^r5001-rtom/salvar/(?P<pk>[0-9]+)/$', 
        r5001_rtom_salvar_views.salvar, 
        name='r5001_rtom_salvar'),

    url(r'^r5001-rtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r5001_rtom_salvar_views.salvar, 
        name='r5001_rtom_salvar_tab'),
        
    url(r'^r5001-rtom/cadastrar/$', 
        r5001_rtom_salvar_views.salvar, 
        name='r5001_rtom_cadastrar'),

    url(r'^r5001-rtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r5001_rtom_salvar_views.salvar, 
        name='r5001_rtom_salvar_output'),
        
    url(r'^r5001-rtom/(?P<output>[\w-]+)/$', 
        r5001_rtom_listar_views.listar, 
        name='r5001_rtom_output'),

    url(r'^r5001-infocrtom/apagar/(?P<pk>[0-9]+)/$', 
        r5001_infocrtom_apagar_views.apagar, 
        name='r5001_infocrtom_apagar'),

    url(r'^r5001-infocrtom/api/$',
        r5001_infocrtom_api_views.r5001infoCRTomList.as_view() ),

    url(r'^r5001-infocrtom/api/(?P<pk>[0-9]+)/$',
        r5001_infocrtom_api_views.r5001infoCRTomDetail.as_view() ),

    url(r'^r5001-infocrtom/$', 
        r5001_infocrtom_listar_views.listar, 
        name='r5001_infocrtom'),

    url(r'^r5001-infocrtom/salvar/(?P<pk>[0-9]+)/$', 
        r5001_infocrtom_salvar_views.salvar, 
        name='r5001_infocrtom_salvar'),

    url(r'^r5001-infocrtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r5001_infocrtom_salvar_views.salvar, 
        name='r5001_infocrtom_salvar_tab'),
        
    url(r'^r5001-infocrtom/cadastrar/$', 
        r5001_infocrtom_salvar_views.salvar, 
        name='r5001_infocrtom_cadastrar'),

    url(r'^r5001-infocrtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r5001_infocrtom_salvar_views.salvar, 
        name='r5001_infocrtom_salvar_output'),
        
    url(r'^r5001-infocrtom/(?P<output>[\w-]+)/$', 
        r5001_infocrtom_listar_views.listar, 
        name='r5001_infocrtom_output'),

    url(r'^r5001-rprest/apagar/(?P<pk>[0-9]+)/$', 
        r5001_rprest_apagar_views.apagar, 
        name='r5001_rprest_apagar'),

    url(r'^r5001-rprest/api/$',
        r5001_rprest_api_views.r5001RPrestList.as_view() ),

    url(r'^r5001-rprest/api/(?P<pk>[0-9]+)/$',
        r5001_rprest_api_views.r5001RPrestDetail.as_view() ),

    url(r'^r5001-rprest/$', 
        r5001_rprest_listar_views.listar, 
        name='r5001_rprest'),

    url(r'^r5001-rprest/salvar/(?P<pk>[0-9]+)/$', 
        r5001_rprest_salvar_views.salvar, 
        name='r5001_rprest_salvar'),

    url(r'^r5001-rprest/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r5001_rprest_salvar_views.salvar, 
        name='r5001_rprest_salvar_tab'),
        
    url(r'^r5001-rprest/cadastrar/$', 
        r5001_rprest_salvar_views.salvar, 
        name='r5001_rprest_cadastrar'),

    url(r'^r5001-rprest/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r5001_rprest_salvar_views.salvar, 
        name='r5001_rprest_salvar_output'),
        
    url(r'^r5001-rprest/(?P<output>[\w-]+)/$', 
        r5001_rprest_listar_views.listar, 
        name='r5001_rprest_output'),

    url(r'^r5001-rrecrepad/apagar/(?P<pk>[0-9]+)/$', 
        r5001_rrecrepad_apagar_views.apagar, 
        name='r5001_rrecrepad_apagar'),

    url(r'^r5001-rrecrepad/api/$',
        r5001_rrecrepad_api_views.r5001RRecRepADList.as_view() ),

    url(r'^r5001-rrecrepad/api/(?P<pk>[0-9]+)/$',
        r5001_rrecrepad_api_views.r5001RRecRepADDetail.as_view() ),

    url(r'^r5001-rrecrepad/$', 
        r5001_rrecrepad_listar_views.listar, 
        name='r5001_rrecrepad'),

    url(r'^r5001-rrecrepad/salvar/(?P<pk>[0-9]+)/$', 
        r5001_rrecrepad_salvar_views.salvar, 
        name='r5001_rrecrepad_salvar'),

    url(r'^r5001-rrecrepad/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r5001_rrecrepad_salvar_views.salvar, 
        name='r5001_rrecrepad_salvar_tab'),
        
    url(r'^r5001-rrecrepad/cadastrar/$', 
        r5001_rrecrepad_salvar_views.salvar, 
        name='r5001_rrecrepad_cadastrar'),

    url(r'^r5001-rrecrepad/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r5001_rrecrepad_salvar_views.salvar, 
        name='r5001_rrecrepad_salvar_output'),
        
    url(r'^r5001-rrecrepad/(?P<output>[\w-]+)/$', 
        r5001_rrecrepad_listar_views.listar, 
        name='r5001_rrecrepad_output'),

    url(r'^r5001-rcoml/apagar/(?P<pk>[0-9]+)/$', 
        r5001_rcoml_apagar_views.apagar, 
        name='r5001_rcoml_apagar'),

    url(r'^r5001-rcoml/api/$',
        r5001_rcoml_api_views.r5001RComlList.as_view() ),

    url(r'^r5001-rcoml/api/(?P<pk>[0-9]+)/$',
        r5001_rcoml_api_views.r5001RComlDetail.as_view() ),

    url(r'^r5001-rcoml/$', 
        r5001_rcoml_listar_views.listar, 
        name='r5001_rcoml'),

    url(r'^r5001-rcoml/salvar/(?P<pk>[0-9]+)/$', 
        r5001_rcoml_salvar_views.salvar, 
        name='r5001_rcoml_salvar'),

    url(r'^r5001-rcoml/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r5001_rcoml_salvar_views.salvar, 
        name='r5001_rcoml_salvar_tab'),
        
    url(r'^r5001-rcoml/cadastrar/$', 
        r5001_rcoml_salvar_views.salvar, 
        name='r5001_rcoml_cadastrar'),

    url(r'^r5001-rcoml/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r5001_rcoml_salvar_views.salvar, 
        name='r5001_rcoml_salvar_output'),
        
    url(r'^r5001-rcoml/(?P<output>[\w-]+)/$', 
        r5001_rcoml_listar_views.listar, 
        name='r5001_rcoml_output'),

    url(r'^r5001-rcprb/apagar/(?P<pk>[0-9]+)/$', 
        r5001_rcprb_apagar_views.apagar, 
        name='r5001_rcprb_apagar'),

    url(r'^r5001-rcprb/api/$',
        r5001_rcprb_api_views.r5001RCPRBList.as_view() ),

    url(r'^r5001-rcprb/api/(?P<pk>[0-9]+)/$',
        r5001_rcprb_api_views.r5001RCPRBDetail.as_view() ),

    url(r'^r5001-rcprb/$', 
        r5001_rcprb_listar_views.listar, 
        name='r5001_rcprb'),

    url(r'^r5001-rcprb/salvar/(?P<pk>[0-9]+)/$', 
        r5001_rcprb_salvar_views.salvar, 
        name='r5001_rcprb_salvar'),

    url(r'^r5001-rcprb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r5001_rcprb_salvar_views.salvar, 
        name='r5001_rcprb_salvar_tab'),
        
    url(r'^r5001-rcprb/cadastrar/$', 
        r5001_rcprb_salvar_views.salvar, 
        name='r5001_rcprb_cadastrar'),

    url(r'^r5001-rcprb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r5001_rcprb_salvar_views.salvar, 
        name='r5001_rcprb_salvar_output'),
        
    url(r'^r5001-rcprb/(?P<output>[\w-]+)/$', 
        r5001_rcprb_listar_views.listar, 
        name='r5001_rcprb_output'),

    url(r'^r5001-rrecespetdesp/apagar/(?P<pk>[0-9]+)/$', 
        r5001_rrecespetdesp_apagar_views.apagar, 
        name='r5001_rrecespetdesp_apagar'),

    url(r'^r5001-rrecespetdesp/api/$',
        r5001_rrecespetdesp_api_views.r5001RRecEspetDespList.as_view() ),

    url(r'^r5001-rrecespetdesp/api/(?P<pk>[0-9]+)/$',
        r5001_rrecespetdesp_api_views.r5001RRecEspetDespDetail.as_view() ),

    url(r'^r5001-rrecespetdesp/$', 
        r5001_rrecespetdesp_listar_views.listar, 
        name='r5001_rrecespetdesp'),

    url(r'^r5001-rrecespetdesp/salvar/(?P<pk>[0-9]+)/$', 
        r5001_rrecespetdesp_salvar_views.salvar, 
        name='r5001_rrecespetdesp_salvar'),

    url(r'^r5001-rrecespetdesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r5001_rrecespetdesp_salvar_views.salvar, 
        name='r5001_rrecespetdesp_salvar_tab'),
        
    url(r'^r5001-rrecespetdesp/cadastrar/$', 
        r5001_rrecespetdesp_salvar_views.salvar, 
        name='r5001_rrecespetdesp_cadastrar'),

    url(r'^r5001-rrecespetdesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r5001_rrecespetdesp_salvar_views.salvar, 
        name='r5001_rrecespetdesp_salvar_output'),
        
    url(r'^r5001-rrecespetdesp/(?P<output>[\w-]+)/$', 
        r5001_rrecespetdesp_listar_views.listar, 
        name='r5001_rrecespetdesp_output'),


]