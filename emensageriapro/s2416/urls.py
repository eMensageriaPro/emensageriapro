#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2416.views import s2416_infopenmorte_apagar as s2416_infopenmorte_apagar_views
from emensageriapro.s2416.views import s2416_infopenmorte_listar as s2416_infopenmorte_listar_views
from emensageriapro.s2416.views import s2416_infopenmorte_salvar as s2416_infopenmorte_salvar_views
from emensageriapro.s2416.views import s2416_infopenmorte_api as s2416_infopenmorte_api_views
from emensageriapro.s2416.views import s2416_homologtc_apagar as s2416_homologtc_apagar_views
from emensageriapro.s2416.views import s2416_homologtc_listar as s2416_homologtc_listar_views
from emensageriapro.s2416.views import s2416_homologtc_salvar as s2416_homologtc_salvar_views
from emensageriapro.s2416.views import s2416_homologtc_api as s2416_homologtc_api_views
from emensageriapro.s2416.views import s2416_suspensao_apagar as s2416_suspensao_apagar_views
from emensageriapro.s2416.views import s2416_suspensao_listar as s2416_suspensao_listar_views
from emensageriapro.s2416.views import s2416_suspensao_salvar as s2416_suspensao_salvar_views
from emensageriapro.s2416.views import s2416_suspensao_api as s2416_suspensao_api_views



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


    url(r'^s2416-infopenmorte/apagar/(?P<pk>[0-9]+)/$', 
        s2416_infopenmorte_apagar_views.apagar, 
        name='s2416_infopenmorte_apagar'),

    url(r'^s2416-infopenmorte/api/$',
        s2416_infopenmorte_api_views.s2416infoPenMorteList.as_view() ),

    url(r'^s2416-infopenmorte/api/(?P<pk>[0-9]+)/$',
        s2416_infopenmorte_api_views.s2416infoPenMorteDetail.as_view() ),

    url(r'^s2416-infopenmorte/$', 
        s2416_infopenmorte_listar_views.listar, 
        name='s2416_infopenmorte'),

    url(r'^s2416-infopenmorte/salvar/(?P<pk>[0-9]+)/$', 
        s2416_infopenmorte_salvar_views.salvar, 
        name='s2416_infopenmorte_salvar'),

    url(r'^s2416-infopenmorte/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2416_infopenmorte_salvar_views.salvar, 
        name='s2416_infopenmorte_salvar_tab'),
        
    url(r'^s2416-infopenmorte/cadastrar/$', 
        s2416_infopenmorte_salvar_views.salvar, 
        name='s2416_infopenmorte_cadastrar'),

    url(r'^s2416-infopenmorte/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2416_infopenmorte_salvar_views.salvar, 
        name='s2416_infopenmorte_salvar_output'),
        
    url(r'^s2416-infopenmorte/(?P<output>[\w-]+)/$', 
        s2416_infopenmorte_listar_views.listar, 
        name='s2416_infopenmorte_output'),

    url(r'^s2416-homologtc/apagar/(?P<pk>[0-9]+)/$', 
        s2416_homologtc_apagar_views.apagar, 
        name='s2416_homologtc_apagar'),

    url(r'^s2416-homologtc/api/$',
        s2416_homologtc_api_views.s2416homologTCList.as_view() ),

    url(r'^s2416-homologtc/api/(?P<pk>[0-9]+)/$',
        s2416_homologtc_api_views.s2416homologTCDetail.as_view() ),

    url(r'^s2416-homologtc/$', 
        s2416_homologtc_listar_views.listar, 
        name='s2416_homologtc'),

    url(r'^s2416-homologtc/salvar/(?P<pk>[0-9]+)/$', 
        s2416_homologtc_salvar_views.salvar, 
        name='s2416_homologtc_salvar'),

    url(r'^s2416-homologtc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2416_homologtc_salvar_views.salvar, 
        name='s2416_homologtc_salvar_tab'),
        
    url(r'^s2416-homologtc/cadastrar/$', 
        s2416_homologtc_salvar_views.salvar, 
        name='s2416_homologtc_cadastrar'),

    url(r'^s2416-homologtc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2416_homologtc_salvar_views.salvar, 
        name='s2416_homologtc_salvar_output'),
        
    url(r'^s2416-homologtc/(?P<output>[\w-]+)/$', 
        s2416_homologtc_listar_views.listar, 
        name='s2416_homologtc_output'),

    url(r'^s2416-suspensao/apagar/(?P<pk>[0-9]+)/$', 
        s2416_suspensao_apagar_views.apagar, 
        name='s2416_suspensao_apagar'),

    url(r'^s2416-suspensao/api/$',
        s2416_suspensao_api_views.s2416suspensaoList.as_view() ),

    url(r'^s2416-suspensao/api/(?P<pk>[0-9]+)/$',
        s2416_suspensao_api_views.s2416suspensaoDetail.as_view() ),

    url(r'^s2416-suspensao/$', 
        s2416_suspensao_listar_views.listar, 
        name='s2416_suspensao'),

    url(r'^s2416-suspensao/salvar/(?P<pk>[0-9]+)/$', 
        s2416_suspensao_salvar_views.salvar, 
        name='s2416_suspensao_salvar'),

    url(r'^s2416-suspensao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2416_suspensao_salvar_views.salvar, 
        name='s2416_suspensao_salvar_tab'),
        
    url(r'^s2416-suspensao/cadastrar/$', 
        s2416_suspensao_salvar_views.salvar, 
        name='s2416_suspensao_cadastrar'),

    url(r'^s2416-suspensao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2416_suspensao_salvar_views.salvar, 
        name='s2416_suspensao_salvar_output'),
        
    url(r'^s2416-suspensao/(?P<output>[\w-]+)/$', 
        s2416_suspensao_listar_views.listar, 
        name='s2416_suspensao_output'),


]