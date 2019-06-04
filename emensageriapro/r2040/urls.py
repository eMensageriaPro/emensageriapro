#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r2040.views import r2040_recursosrep_apagar as r2040_recursosrep_apagar_views
from emensageriapro.r2040.views import r2040_recursosrep_listar as r2040_recursosrep_listar_views
from emensageriapro.r2040.views import r2040_recursosrep_salvar as r2040_recursosrep_salvar_views
from emensageriapro.r2040.views import r2040_recursosrep_api as r2040_recursosrep_api_views
from emensageriapro.r2040.views import r2040_inforecurso_apagar as r2040_inforecurso_apagar_views
from emensageriapro.r2040.views import r2040_inforecurso_listar as r2040_inforecurso_listar_views
from emensageriapro.r2040.views import r2040_inforecurso_salvar as r2040_inforecurso_salvar_views
from emensageriapro.r2040.views import r2040_inforecurso_api as r2040_inforecurso_api_views
from emensageriapro.r2040.views import r2040_infoproc_apagar as r2040_infoproc_apagar_views
from emensageriapro.r2040.views import r2040_infoproc_listar as r2040_infoproc_listar_views
from emensageriapro.r2040.views import r2040_infoproc_salvar as r2040_infoproc_salvar_views
from emensageriapro.r2040.views import r2040_infoproc_api as r2040_infoproc_api_views



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


    url(r'^r2040-recursosrep/apagar/(?P<pk>[0-9]+)/$', 
        r2040_recursosrep_apagar_views.apagar, 
        name='r2040_recursosrep_apagar'),

    url(r'^r2040-recursosrep/api/$',
        r2040_recursosrep_api_views.r2040recursosRepList.as_view() ),

    url(r'^r2040-recursosrep/api/(?P<pk>[0-9]+)/$',
        r2040_recursosrep_api_views.r2040recursosRepDetail.as_view() ),

    url(r'^r2040-recursosrep/$', 
        r2040_recursosrep_listar_views.listar, 
        name='r2040_recursosrep'),

    url(r'^r2040-recursosrep/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2040_recursosrep_salvar_views.salvar, 
        name='r2040_recursosrep_salvar'),
        
    url(r'^r2040-recursosrep/cadastrar/$', 
        r2040_recursosrep_salvar_views.salvar, 
        name='r2040_recursosrep_cadastrar'),

    url(r'^r2040-recursosrep/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2040_recursosrep_salvar_views.salvar, 
        name='r2040_recursosrep_salvar_output'),
        
    url(r'^r2040-recursosrep/(?P<output>[\w-]+)/$', 
        r2040_recursosrep_listar_views.listar, 
        name='r2040_recursosrep_output'),

    url(r'^r2040-inforecurso/apagar/(?P<pk>[0-9]+)/$', 
        r2040_inforecurso_apagar_views.apagar, 
        name='r2040_inforecurso_apagar'),

    url(r'^r2040-inforecurso/api/$',
        r2040_inforecurso_api_views.r2040infoRecursoList.as_view() ),

    url(r'^r2040-inforecurso/api/(?P<pk>[0-9]+)/$',
        r2040_inforecurso_api_views.r2040infoRecursoDetail.as_view() ),

    url(r'^r2040-inforecurso/$', 
        r2040_inforecurso_listar_views.listar, 
        name='r2040_inforecurso'),

    url(r'^r2040-inforecurso/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2040_inforecurso_salvar_views.salvar, 
        name='r2040_inforecurso_salvar'),
        
    url(r'^r2040-inforecurso/cadastrar/$', 
        r2040_inforecurso_salvar_views.salvar, 
        name='r2040_inforecurso_cadastrar'),

    url(r'^r2040-inforecurso/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2040_inforecurso_salvar_views.salvar, 
        name='r2040_inforecurso_salvar_output'),
        
    url(r'^r2040-inforecurso/(?P<output>[\w-]+)/$', 
        r2040_inforecurso_listar_views.listar, 
        name='r2040_inforecurso_output'),

    url(r'^r2040-infoproc/apagar/(?P<pk>[0-9]+)/$', 
        r2040_infoproc_apagar_views.apagar, 
        name='r2040_infoproc_apagar'),

    url(r'^r2040-infoproc/api/$',
        r2040_infoproc_api_views.r2040infoProcList.as_view() ),

    url(r'^r2040-infoproc/api/(?P<pk>[0-9]+)/$',
        r2040_infoproc_api_views.r2040infoProcDetail.as_view() ),

    url(r'^r2040-infoproc/$', 
        r2040_infoproc_listar_views.listar, 
        name='r2040_infoproc'),

    url(r'^r2040-infoproc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r2040_infoproc_salvar_views.salvar, 
        name='r2040_infoproc_salvar'),
        
    url(r'^r2040-infoproc/cadastrar/$', 
        r2040_infoproc_salvar_views.salvar, 
        name='r2040_infoproc_cadastrar'),

    url(r'^r2040-infoproc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r2040_infoproc_salvar_views.salvar, 
        name='r2040_infoproc_salvar_output'),
        
    url(r'^r2040-infoproc/(?P<output>[\w-]+)/$', 
        r2040_infoproc_listar_views.listar, 
        name='r2040_infoproc_output'),


]