#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r2060.views import r2060_tipocod_apagar as r2060_tipocod_apagar_views
from emensageriapro.r2060.views import r2060_tipocod_listar as r2060_tipocod_listar_views
from emensageriapro.r2060.views import r2060_tipocod_salvar as r2060_tipocod_salvar_views
from emensageriapro.r2060.views import r2060_tipocod_api as r2060_tipocod_api_views
from emensageriapro.r2060.views import r2060_tipoajuste_apagar as r2060_tipoajuste_apagar_views
from emensageriapro.r2060.views import r2060_tipoajuste_listar as r2060_tipoajuste_listar_views
from emensageriapro.r2060.views import r2060_tipoajuste_salvar as r2060_tipoajuste_salvar_views
from emensageriapro.r2060.views import r2060_tipoajuste_api as r2060_tipoajuste_api_views
from emensageriapro.r2060.views import r2060_infoproc_apagar as r2060_infoproc_apagar_views
from emensageriapro.r2060.views import r2060_infoproc_listar as r2060_infoproc_listar_views
from emensageriapro.r2060.views import r2060_infoproc_salvar as r2060_infoproc_salvar_views
from emensageriapro.r2060.views import r2060_infoproc_api as r2060_infoproc_api_views



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


    url(r'^r2060-tipocod/apagar/(?P<pk>[0-9]+)/$', 
        r2060_tipocod_apagar_views.apagar, 
        name='r2060_tipocod_apagar'),

    url(r'^r2060-tipocod/api/$',
        r2060_tipocod_api_views.r2060tipoCodList.as_view() ),

    url(r'^r2060-tipocod/api/(?P<pk>[0-9]+)/$',
        r2060_tipocod_api_views.r2060tipoCodDetail.as_view() ),

    url(r'^r2060-tipocod/$', 
        r2060_tipocod_listar_views.listar, 
        name='r2060_tipocod'),

    url(r'^r2060-tipocod/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2060_tipocod_salvar_views.salvar, 
        name='r2060_tipocod_salvar'),
        
    url(r'^r2060-tipocod/cadastrar/$', 
        r2060_tipocod_salvar_views.salvar, 
        name='r2060_tipocod_cadastrar'),

    url(r'^r2060-tipocod/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2060_tipocod_salvar_views.salvar, 
        name='r2060_tipocod_salvar_output'),
        
    url(r'^r2060-tipocod/(?P<output>[\w-]+)/$', 
        r2060_tipocod_listar_views.listar, 
        name='r2060_tipocod_output'),

    url(r'^r2060-tipoajuste/apagar/(?P<pk>[0-9]+)/$', 
        r2060_tipoajuste_apagar_views.apagar, 
        name='r2060_tipoajuste_apagar'),

    url(r'^r2060-tipoajuste/api/$',
        r2060_tipoajuste_api_views.r2060tipoAjusteList.as_view() ),

    url(r'^r2060-tipoajuste/api/(?P<pk>[0-9]+)/$',
        r2060_tipoajuste_api_views.r2060tipoAjusteDetail.as_view() ),

    url(r'^r2060-tipoajuste/$', 
        r2060_tipoajuste_listar_views.listar, 
        name='r2060_tipoajuste'),

    url(r'^r2060-tipoajuste/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2060_tipoajuste_salvar_views.salvar, 
        name='r2060_tipoajuste_salvar'),
        
    url(r'^r2060-tipoajuste/cadastrar/$', 
        r2060_tipoajuste_salvar_views.salvar, 
        name='r2060_tipoajuste_cadastrar'),

    url(r'^r2060-tipoajuste/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2060_tipoajuste_salvar_views.salvar, 
        name='r2060_tipoajuste_salvar_output'),
        
    url(r'^r2060-tipoajuste/(?P<output>[\w-]+)/$', 
        r2060_tipoajuste_listar_views.listar, 
        name='r2060_tipoajuste_output'),

    url(r'^r2060-infoproc/apagar/(?P<pk>[0-9]+)/$', 
        r2060_infoproc_apagar_views.apagar, 
        name='r2060_infoproc_apagar'),

    url(r'^r2060-infoproc/api/$',
        r2060_infoproc_api_views.r2060infoProcList.as_view() ),

    url(r'^r2060-infoproc/api/(?P<pk>[0-9]+)/$',
        r2060_infoproc_api_views.r2060infoProcDetail.as_view() ),

    url(r'^r2060-infoproc/$', 
        r2060_infoproc_listar_views.listar, 
        name='r2060_infoproc'),

    url(r'^r2060-infoproc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2060_infoproc_salvar_views.salvar, 
        name='r2060_infoproc_salvar'),
        
    url(r'^r2060-infoproc/cadastrar/$', 
        r2060_infoproc_salvar_views.salvar, 
        name='r2060_infoproc_cadastrar'),

    url(r'^r2060-infoproc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2060_infoproc_salvar_views.salvar, 
        name='r2060_infoproc_salvar_output'),
        
    url(r'^r2060-infoproc/(?P<output>[\w-]+)/$', 
        r2060_infoproc_listar_views.listar, 
        name='r2060_infoproc_output'),


]