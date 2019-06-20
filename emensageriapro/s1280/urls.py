#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1280.views import s1280_infosubstpatr_apagar as s1280_infosubstpatr_apagar_views
from emensageriapro.s1280.views import s1280_infosubstpatr_listar as s1280_infosubstpatr_listar_views
from emensageriapro.s1280.views import s1280_infosubstpatr_salvar as s1280_infosubstpatr_salvar_views
from emensageriapro.s1280.views import s1280_infosubstpatr_api as s1280_infosubstpatr_api_views
from emensageriapro.s1280.views import s1280_infosubstpatropport_apagar as s1280_infosubstpatropport_apagar_views
from emensageriapro.s1280.views import s1280_infosubstpatropport_listar as s1280_infosubstpatropport_listar_views
from emensageriapro.s1280.views import s1280_infosubstpatropport_salvar as s1280_infosubstpatropport_salvar_views
from emensageriapro.s1280.views import s1280_infosubstpatropport_api as s1280_infosubstpatropport_api_views
from emensageriapro.s1280.views import s1280_infoativconcom_apagar as s1280_infoativconcom_apagar_views
from emensageriapro.s1280.views import s1280_infoativconcom_listar as s1280_infoativconcom_listar_views
from emensageriapro.s1280.views import s1280_infoativconcom_salvar as s1280_infoativconcom_salvar_views
from emensageriapro.s1280.views import s1280_infoativconcom_api as s1280_infoativconcom_api_views



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


    url(r'^s1280-infosubstpatr/apagar/(?P<pk>[0-9]+)/$', 
        s1280_infosubstpatr_apagar_views.apagar, 
        name='s1280_infosubstpatr_apagar'),

    url(r'^s1280-infosubstpatr/api/$',
        s1280_infosubstpatr_api_views.s1280infoSubstPatrList.as_view() ),

    url(r'^s1280-infosubstpatr/api/(?P<pk>[0-9]+)/$',
        s1280_infosubstpatr_api_views.s1280infoSubstPatrDetail.as_view() ),

    url(r'^s1280-infosubstpatr/$', 
        s1280_infosubstpatr_listar_views.listar, 
        name='s1280_infosubstpatr'),

    url(r'^s1280-infosubstpatr/salvar/(?P<pk>[0-9]+)/$', 
        s1280_infosubstpatr_salvar_views.salvar, 
        name='s1280_infosubstpatr_salvar'),

    url(r'^s1280-infosubstpatr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1280_infosubstpatr_salvar_views.salvar, 
        name='s1280_infosubstpatr_salvar_tab'),
        
    url(r'^s1280-infosubstpatr/cadastrar/$', 
        s1280_infosubstpatr_salvar_views.salvar, 
        name='s1280_infosubstpatr_cadastrar'),

    url(r'^s1280-infosubstpatr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1280_infosubstpatr_salvar_views.salvar, 
        name='s1280_infosubstpatr_salvar_output'),
        
    url(r'^s1280-infosubstpatr/(?P<output>[\w-]+)/$', 
        s1280_infosubstpatr_listar_views.listar, 
        name='s1280_infosubstpatr_output'),

    url(r'^s1280-infosubstpatropport/apagar/(?P<pk>[0-9]+)/$', 
        s1280_infosubstpatropport_apagar_views.apagar, 
        name='s1280_infosubstpatropport_apagar'),

    url(r'^s1280-infosubstpatropport/api/$',
        s1280_infosubstpatropport_api_views.s1280infoSubstPatrOpPortList.as_view() ),

    url(r'^s1280-infosubstpatropport/api/(?P<pk>[0-9]+)/$',
        s1280_infosubstpatropport_api_views.s1280infoSubstPatrOpPortDetail.as_view() ),

    url(r'^s1280-infosubstpatropport/$', 
        s1280_infosubstpatropport_listar_views.listar, 
        name='s1280_infosubstpatropport'),

    url(r'^s1280-infosubstpatropport/salvar/(?P<pk>[0-9]+)/$', 
        s1280_infosubstpatropport_salvar_views.salvar, 
        name='s1280_infosubstpatropport_salvar'),

    url(r'^s1280-infosubstpatropport/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1280_infosubstpatropport_salvar_views.salvar, 
        name='s1280_infosubstpatropport_salvar_tab'),
        
    url(r'^s1280-infosubstpatropport/cadastrar/$', 
        s1280_infosubstpatropport_salvar_views.salvar, 
        name='s1280_infosubstpatropport_cadastrar'),

    url(r'^s1280-infosubstpatropport/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1280_infosubstpatropport_salvar_views.salvar, 
        name='s1280_infosubstpatropport_salvar_output'),
        
    url(r'^s1280-infosubstpatropport/(?P<output>[\w-]+)/$', 
        s1280_infosubstpatropport_listar_views.listar, 
        name='s1280_infosubstpatropport_output'),

    url(r'^s1280-infoativconcom/apagar/(?P<pk>[0-9]+)/$', 
        s1280_infoativconcom_apagar_views.apagar, 
        name='s1280_infoativconcom_apagar'),

    url(r'^s1280-infoativconcom/api/$',
        s1280_infoativconcom_api_views.s1280infoAtivConcomList.as_view() ),

    url(r'^s1280-infoativconcom/api/(?P<pk>[0-9]+)/$',
        s1280_infoativconcom_api_views.s1280infoAtivConcomDetail.as_view() ),

    url(r'^s1280-infoativconcom/$', 
        s1280_infoativconcom_listar_views.listar, 
        name='s1280_infoativconcom'),

    url(r'^s1280-infoativconcom/salvar/(?P<pk>[0-9]+)/$', 
        s1280_infoativconcom_salvar_views.salvar, 
        name='s1280_infoativconcom_salvar'),

    url(r'^s1280-infoativconcom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1280_infoativconcom_salvar_views.salvar, 
        name='s1280_infoativconcom_salvar_tab'),
        
    url(r'^s1280-infoativconcom/cadastrar/$', 
        s1280_infoativconcom_salvar_views.salvar, 
        name='s1280_infoativconcom_cadastrar'),

    url(r'^s1280-infoativconcom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1280_infoativconcom_salvar_views.salvar, 
        name='s1280_infoativconcom_salvar_output'),
        
    url(r'^s1280-infoativconcom/(?P<output>[\w-]+)/$', 
        s1280_infoativconcom_listar_views.listar, 
        name='s1280_infoativconcom_output'),


]