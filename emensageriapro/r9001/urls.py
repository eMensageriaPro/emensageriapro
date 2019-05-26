#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r9001.views import r9001_regocorrs_apagar as r9001_regocorrs_apagar_views
from emensageriapro.r9001.views import r9001_regocorrs_listar as r9001_regocorrs_listar_views
from emensageriapro.r9001.views import r9001_regocorrs_salvar as r9001_regocorrs_salvar_views
from emensageriapro.r9001.views import r9001_regocorrs_api as r9001_regocorrs_api_views
from emensageriapro.r9001.views import r9001_infototal_apagar as r9001_infototal_apagar_views
from emensageriapro.r9001.views import r9001_infototal_listar as r9001_infototal_listar_views
from emensageriapro.r9001.views import r9001_infototal_salvar as r9001_infototal_salvar_views
from emensageriapro.r9001.views import r9001_infototal_api as r9001_infototal_api_views
from emensageriapro.r9001.views import r9001_rtom_apagar as r9001_rtom_apagar_views
from emensageriapro.r9001.views import r9001_rtom_listar as r9001_rtom_listar_views
from emensageriapro.r9001.views import r9001_rtom_salvar as r9001_rtom_salvar_views
from emensageriapro.r9001.views import r9001_rtom_api as r9001_rtom_api_views
from emensageriapro.r9001.views import r9001_infocrtom_apagar as r9001_infocrtom_apagar_views
from emensageriapro.r9001.views import r9001_infocrtom_listar as r9001_infocrtom_listar_views
from emensageriapro.r9001.views import r9001_infocrtom_salvar as r9001_infocrtom_salvar_views
from emensageriapro.r9001.views import r9001_infocrtom_api as r9001_infocrtom_api_views
from emensageriapro.r9001.views import r9001_rprest_apagar as r9001_rprest_apagar_views
from emensageriapro.r9001.views import r9001_rprest_listar as r9001_rprest_listar_views
from emensageriapro.r9001.views import r9001_rprest_salvar as r9001_rprest_salvar_views
from emensageriapro.r9001.views import r9001_rprest_api as r9001_rprest_api_views
from emensageriapro.r9001.views import r9001_rrecrepad_apagar as r9001_rrecrepad_apagar_views
from emensageriapro.r9001.views import r9001_rrecrepad_listar as r9001_rrecrepad_listar_views
from emensageriapro.r9001.views import r9001_rrecrepad_salvar as r9001_rrecrepad_salvar_views
from emensageriapro.r9001.views import r9001_rrecrepad_api as r9001_rrecrepad_api_views
from emensageriapro.r9001.views import r9001_rcoml_apagar as r9001_rcoml_apagar_views
from emensageriapro.r9001.views import r9001_rcoml_listar as r9001_rcoml_listar_views
from emensageriapro.r9001.views import r9001_rcoml_salvar as r9001_rcoml_salvar_views
from emensageriapro.r9001.views import r9001_rcoml_api as r9001_rcoml_api_views
from emensageriapro.r9001.views import r9001_rcprb_apagar as r9001_rcprb_apagar_views
from emensageriapro.r9001.views import r9001_rcprb_listar as r9001_rcprb_listar_views
from emensageriapro.r9001.views import r9001_rcprb_salvar as r9001_rcprb_salvar_views
from emensageriapro.r9001.views import r9001_rcprb_api as r9001_rcprb_api_views
from emensageriapro.r9001.views import r9001_rrecespetdesp_apagar as r9001_rrecespetdesp_apagar_views
from emensageriapro.r9001.views import r9001_rrecespetdesp_listar as r9001_rrecespetdesp_listar_views
from emensageriapro.r9001.views import r9001_rrecespetdesp_salvar as r9001_rrecespetdesp_salvar_views
from emensageriapro.r9001.views import r9001_rrecespetdesp_api as r9001_rrecespetdesp_api_views



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


    url(r'^r9001-regocorrs/apagar/(?P<hash>.*)/$', 
        r9001_regocorrs_apagar_views.apagar, 
        name='r9001_regocorrs_apagar'),

    url(r'^r9001-regocorrs/api/$',
        r9001_regocorrs_api_views.r9001regOcorrsList.as_view() ),

    url(r'^r9001-regocorrs/api/(?P<pk>[0-9]+)/$',
        r9001_regocorrs_api_views.r9001regOcorrsDetail.as_view() ),

    url(r'^r9001-regocorrs/listar/(?P<hash>.*)/$', 
        r9001_regocorrs_listar_views.listar, 
        name='r9001_regocorrs'),

    url(r'^r9001-regocorrs/salvar/(?P<hash>.*)/$', 
        r9001_regocorrs_salvar_views.salvar, 
        name='r9001_regocorrs_salvar'),

    url(r'^r9001-infototal/apagar/(?P<hash>.*)/$', 
        r9001_infototal_apagar_views.apagar, 
        name='r9001_infototal_apagar'),

    url(r'^r9001-infototal/api/$',
        r9001_infototal_api_views.r9001infoTotalList.as_view() ),

    url(r'^r9001-infototal/api/(?P<pk>[0-9]+)/$',
        r9001_infototal_api_views.r9001infoTotalDetail.as_view() ),

    url(r'^r9001-infototal/listar/(?P<hash>.*)/$', 
        r9001_infototal_listar_views.listar, 
        name='r9001_infototal'),

    url(r'^r9001-infototal/salvar/(?P<hash>.*)/$', 
        r9001_infototal_salvar_views.salvar, 
        name='r9001_infototal_salvar'),

    url(r'^r9001-rtom/apagar/(?P<hash>.*)/$', 
        r9001_rtom_apagar_views.apagar, 
        name='r9001_rtom_apagar'),

    url(r'^r9001-rtom/api/$',
        r9001_rtom_api_views.r9001RTomList.as_view() ),

    url(r'^r9001-rtom/api/(?P<pk>[0-9]+)/$',
        r9001_rtom_api_views.r9001RTomDetail.as_view() ),

    url(r'^r9001-rtom/listar/(?P<hash>.*)/$', 
        r9001_rtom_listar_views.listar, 
        name='r9001_rtom'),

    url(r'^r9001-rtom/salvar/(?P<hash>.*)/$', 
        r9001_rtom_salvar_views.salvar, 
        name='r9001_rtom_salvar'),

    url(r'^r9001-infocrtom/apagar/(?P<hash>.*)/$', 
        r9001_infocrtom_apagar_views.apagar, 
        name='r9001_infocrtom_apagar'),

    url(r'^r9001-infocrtom/api/$',
        r9001_infocrtom_api_views.r9001infoCRTomList.as_view() ),

    url(r'^r9001-infocrtom/api/(?P<pk>[0-9]+)/$',
        r9001_infocrtom_api_views.r9001infoCRTomDetail.as_view() ),

    url(r'^r9001-infocrtom/listar/(?P<hash>.*)/$', 
        r9001_infocrtom_listar_views.listar, 
        name='r9001_infocrtom'),

    url(r'^r9001-infocrtom/salvar/(?P<hash>.*)/$', 
        r9001_infocrtom_salvar_views.salvar, 
        name='r9001_infocrtom_salvar'),

    url(r'^r9001-rprest/apagar/(?P<hash>.*)/$', 
        r9001_rprest_apagar_views.apagar, 
        name='r9001_rprest_apagar'),

    url(r'^r9001-rprest/api/$',
        r9001_rprest_api_views.r9001RPrestList.as_view() ),

    url(r'^r9001-rprest/api/(?P<pk>[0-9]+)/$',
        r9001_rprest_api_views.r9001RPrestDetail.as_view() ),

    url(r'^r9001-rprest/listar/(?P<hash>.*)/$', 
        r9001_rprest_listar_views.listar, 
        name='r9001_rprest'),

    url(r'^r9001-rprest/salvar/(?P<hash>.*)/$', 
        r9001_rprest_salvar_views.salvar, 
        name='r9001_rprest_salvar'),

    url(r'^r9001-rrecrepad/apagar/(?P<hash>.*)/$', 
        r9001_rrecrepad_apagar_views.apagar, 
        name='r9001_rrecrepad_apagar'),

    url(r'^r9001-rrecrepad/api/$',
        r9001_rrecrepad_api_views.r9001RRecRepADList.as_view() ),

    url(r'^r9001-rrecrepad/api/(?P<pk>[0-9]+)/$',
        r9001_rrecrepad_api_views.r9001RRecRepADDetail.as_view() ),

    url(r'^r9001-rrecrepad/listar/(?P<hash>.*)/$', 
        r9001_rrecrepad_listar_views.listar, 
        name='r9001_rrecrepad'),

    url(r'^r9001-rrecrepad/salvar/(?P<hash>.*)/$', 
        r9001_rrecrepad_salvar_views.salvar, 
        name='r9001_rrecrepad_salvar'),

    url(r'^r9001-rcoml/apagar/(?P<hash>.*)/$', 
        r9001_rcoml_apagar_views.apagar, 
        name='r9001_rcoml_apagar'),

    url(r'^r9001-rcoml/api/$',
        r9001_rcoml_api_views.r9001RComlList.as_view() ),

    url(r'^r9001-rcoml/api/(?P<pk>[0-9]+)/$',
        r9001_rcoml_api_views.r9001RComlDetail.as_view() ),

    url(r'^r9001-rcoml/listar/(?P<hash>.*)/$', 
        r9001_rcoml_listar_views.listar, 
        name='r9001_rcoml'),

    url(r'^r9001-rcoml/salvar/(?P<hash>.*)/$', 
        r9001_rcoml_salvar_views.salvar, 
        name='r9001_rcoml_salvar'),

    url(r'^r9001-rcprb/apagar/(?P<hash>.*)/$', 
        r9001_rcprb_apagar_views.apagar, 
        name='r9001_rcprb_apagar'),

    url(r'^r9001-rcprb/api/$',
        r9001_rcprb_api_views.r9001RCPRBList.as_view() ),

    url(r'^r9001-rcprb/api/(?P<pk>[0-9]+)/$',
        r9001_rcprb_api_views.r9001RCPRBDetail.as_view() ),

    url(r'^r9001-rcprb/listar/(?P<hash>.*)/$', 
        r9001_rcprb_listar_views.listar, 
        name='r9001_rcprb'),

    url(r'^r9001-rcprb/salvar/(?P<hash>.*)/$', 
        r9001_rcprb_salvar_views.salvar, 
        name='r9001_rcprb_salvar'),

    url(r'^r9001-rrecespetdesp/apagar/(?P<hash>.*)/$', 
        r9001_rrecespetdesp_apagar_views.apagar, 
        name='r9001_rrecespetdesp_apagar'),

    url(r'^r9001-rrecespetdesp/api/$',
        r9001_rrecespetdesp_api_views.r9001RRecEspetDespList.as_view() ),

    url(r'^r9001-rrecespetdesp/api/(?P<pk>[0-9]+)/$',
        r9001_rrecespetdesp_api_views.r9001RRecEspetDespDetail.as_view() ),

    url(r'^r9001-rrecespetdesp/listar/(?P<hash>.*)/$', 
        r9001_rrecespetdesp_listar_views.listar, 
        name='r9001_rrecespetdesp'),

    url(r'^r9001-rrecespetdesp/salvar/(?P<hash>.*)/$', 
        r9001_rrecespetdesp_salvar_views.salvar, 
        name='r9001_rrecespetdesp_salvar'),


]