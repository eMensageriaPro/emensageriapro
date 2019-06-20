#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s5002.views import s5002_infodep_apagar as s5002_infodep_apagar_views
from emensageriapro.s5002.views import s5002_infodep_listar as s5002_infodep_listar_views
from emensageriapro.s5002.views import s5002_infodep_salvar as s5002_infodep_salvar_views
from emensageriapro.s5002.views import s5002_infodep_api as s5002_infodep_api_views
from emensageriapro.s5002.views import s5002_infoirrf_apagar as s5002_infoirrf_apagar_views
from emensageriapro.s5002.views import s5002_infoirrf_listar as s5002_infoirrf_listar_views
from emensageriapro.s5002.views import s5002_infoirrf_salvar as s5002_infoirrf_salvar_views
from emensageriapro.s5002.views import s5002_infoirrf_api as s5002_infoirrf_api_views
from emensageriapro.s5002.views import s5002_basesirrf_apagar as s5002_basesirrf_apagar_views
from emensageriapro.s5002.views import s5002_basesirrf_listar as s5002_basesirrf_listar_views
from emensageriapro.s5002.views import s5002_basesirrf_salvar as s5002_basesirrf_salvar_views
from emensageriapro.s5002.views import s5002_basesirrf_api as s5002_basesirrf_api_views
from emensageriapro.s5002.views import s5002_irrf_apagar as s5002_irrf_apagar_views
from emensageriapro.s5002.views import s5002_irrf_listar as s5002_irrf_listar_views
from emensageriapro.s5002.views import s5002_irrf_salvar as s5002_irrf_salvar_views
from emensageriapro.s5002.views import s5002_irrf_api as s5002_irrf_api_views
from emensageriapro.s5002.views import s5002_idepgtoext_apagar as s5002_idepgtoext_apagar_views
from emensageriapro.s5002.views import s5002_idepgtoext_listar as s5002_idepgtoext_listar_views
from emensageriapro.s5002.views import s5002_idepgtoext_salvar as s5002_idepgtoext_salvar_views
from emensageriapro.s5002.views import s5002_idepgtoext_api as s5002_idepgtoext_api_views



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


    url(r'^s5002-infodep/apagar/(?P<pk>[0-9]+)/$', 
        s5002_infodep_apagar_views.apagar, 
        name='s5002_infodep_apagar'),

    url(r'^s5002-infodep/api/$',
        s5002_infodep_api_views.s5002infoDepList.as_view() ),

    url(r'^s5002-infodep/api/(?P<pk>[0-9]+)/$',
        s5002_infodep_api_views.s5002infoDepDetail.as_view() ),

    url(r'^s5002-infodep/$', 
        s5002_infodep_listar_views.listar, 
        name='s5002_infodep'),

    url(r'^s5002-infodep/salvar/(?P<pk>[0-9]+)/$', 
        s5002_infodep_salvar_views.salvar, 
        name='s5002_infodep_salvar'),

    url(r'^s5002-infodep/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5002_infodep_salvar_views.salvar, 
        name='s5002_infodep_salvar_tab'),
        
    url(r'^s5002-infodep/cadastrar/$', 
        s5002_infodep_salvar_views.salvar, 
        name='s5002_infodep_cadastrar'),

    url(r'^s5002-infodep/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5002_infodep_salvar_views.salvar, 
        name='s5002_infodep_salvar_output'),
        
    url(r'^s5002-infodep/(?P<output>[\w-]+)/$', 
        s5002_infodep_listar_views.listar, 
        name='s5002_infodep_output'),

    url(r'^s5002-infoirrf/apagar/(?P<pk>[0-9]+)/$', 
        s5002_infoirrf_apagar_views.apagar, 
        name='s5002_infoirrf_apagar'),

    url(r'^s5002-infoirrf/api/$',
        s5002_infoirrf_api_views.s5002infoIrrfList.as_view() ),

    url(r'^s5002-infoirrf/api/(?P<pk>[0-9]+)/$',
        s5002_infoirrf_api_views.s5002infoIrrfDetail.as_view() ),

    url(r'^s5002-infoirrf/$', 
        s5002_infoirrf_listar_views.listar, 
        name='s5002_infoirrf'),

    url(r'^s5002-infoirrf/salvar/(?P<pk>[0-9]+)/$', 
        s5002_infoirrf_salvar_views.salvar, 
        name='s5002_infoirrf_salvar'),

    url(r'^s5002-infoirrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5002_infoirrf_salvar_views.salvar, 
        name='s5002_infoirrf_salvar_tab'),
        
    url(r'^s5002-infoirrf/cadastrar/$', 
        s5002_infoirrf_salvar_views.salvar, 
        name='s5002_infoirrf_cadastrar'),

    url(r'^s5002-infoirrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5002_infoirrf_salvar_views.salvar, 
        name='s5002_infoirrf_salvar_output'),
        
    url(r'^s5002-infoirrf/(?P<output>[\w-]+)/$', 
        s5002_infoirrf_listar_views.listar, 
        name='s5002_infoirrf_output'),

    url(r'^s5002-basesirrf/apagar/(?P<pk>[0-9]+)/$', 
        s5002_basesirrf_apagar_views.apagar, 
        name='s5002_basesirrf_apagar'),

    url(r'^s5002-basesirrf/api/$',
        s5002_basesirrf_api_views.s5002basesIrrfList.as_view() ),

    url(r'^s5002-basesirrf/api/(?P<pk>[0-9]+)/$',
        s5002_basesirrf_api_views.s5002basesIrrfDetail.as_view() ),

    url(r'^s5002-basesirrf/$', 
        s5002_basesirrf_listar_views.listar, 
        name='s5002_basesirrf'),

    url(r'^s5002-basesirrf/salvar/(?P<pk>[0-9]+)/$', 
        s5002_basesirrf_salvar_views.salvar, 
        name='s5002_basesirrf_salvar'),

    url(r'^s5002-basesirrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5002_basesirrf_salvar_views.salvar, 
        name='s5002_basesirrf_salvar_tab'),
        
    url(r'^s5002-basesirrf/cadastrar/$', 
        s5002_basesirrf_salvar_views.salvar, 
        name='s5002_basesirrf_cadastrar'),

    url(r'^s5002-basesirrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5002_basesirrf_salvar_views.salvar, 
        name='s5002_basesirrf_salvar_output'),
        
    url(r'^s5002-basesirrf/(?P<output>[\w-]+)/$', 
        s5002_basesirrf_listar_views.listar, 
        name='s5002_basesirrf_output'),

    url(r'^s5002-irrf/apagar/(?P<pk>[0-9]+)/$', 
        s5002_irrf_apagar_views.apagar, 
        name='s5002_irrf_apagar'),

    url(r'^s5002-irrf/api/$',
        s5002_irrf_api_views.s5002irrfList.as_view() ),

    url(r'^s5002-irrf/api/(?P<pk>[0-9]+)/$',
        s5002_irrf_api_views.s5002irrfDetail.as_view() ),

    url(r'^s5002-irrf/$', 
        s5002_irrf_listar_views.listar, 
        name='s5002_irrf'),

    url(r'^s5002-irrf/salvar/(?P<pk>[0-9]+)/$', 
        s5002_irrf_salvar_views.salvar, 
        name='s5002_irrf_salvar'),

    url(r'^s5002-irrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5002_irrf_salvar_views.salvar, 
        name='s5002_irrf_salvar_tab'),
        
    url(r'^s5002-irrf/cadastrar/$', 
        s5002_irrf_salvar_views.salvar, 
        name='s5002_irrf_cadastrar'),

    url(r'^s5002-irrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5002_irrf_salvar_views.salvar, 
        name='s5002_irrf_salvar_output'),
        
    url(r'^s5002-irrf/(?P<output>[\w-]+)/$', 
        s5002_irrf_listar_views.listar, 
        name='s5002_irrf_output'),

    url(r'^s5002-idepgtoext/apagar/(?P<pk>[0-9]+)/$', 
        s5002_idepgtoext_apagar_views.apagar, 
        name='s5002_idepgtoext_apagar'),

    url(r'^s5002-idepgtoext/api/$',
        s5002_idepgtoext_api_views.s5002idePgtoExtList.as_view() ),

    url(r'^s5002-idepgtoext/api/(?P<pk>[0-9]+)/$',
        s5002_idepgtoext_api_views.s5002idePgtoExtDetail.as_view() ),

    url(r'^s5002-idepgtoext/$', 
        s5002_idepgtoext_listar_views.listar, 
        name='s5002_idepgtoext'),

    url(r'^s5002-idepgtoext/salvar/(?P<pk>[0-9]+)/$', 
        s5002_idepgtoext_salvar_views.salvar, 
        name='s5002_idepgtoext_salvar'),

    url(r'^s5002-idepgtoext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s5002_idepgtoext_salvar_views.salvar, 
        name='s5002_idepgtoext_salvar_tab'),
        
    url(r'^s5002-idepgtoext/cadastrar/$', 
        s5002_idepgtoext_salvar_views.salvar, 
        name='s5002_idepgtoext_cadastrar'),

    url(r'^s5002-idepgtoext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s5002_idepgtoext_salvar_views.salvar, 
        name='s5002_idepgtoext_salvar_output'),
        
    url(r'^s5002-idepgtoext/(?P<output>[\w-]+)/$', 
        s5002_idepgtoext_listar_views.listar, 
        name='s5002_idepgtoext_output'),


]