#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1080.views import s1080_inclusao_apagar as s1080_inclusao_apagar_views
from emensageriapro.s1080.views import s1080_inclusao_listar as s1080_inclusao_listar_views
from emensageriapro.s1080.views import s1080_inclusao_salvar as s1080_inclusao_salvar_views
from emensageriapro.s1080.views import s1080_inclusao_api as s1080_inclusao_api_views
from emensageriapro.s1080.views import s1080_alteracao_apagar as s1080_alteracao_apagar_views
from emensageriapro.s1080.views import s1080_alteracao_listar as s1080_alteracao_listar_views
from emensageriapro.s1080.views import s1080_alteracao_salvar as s1080_alteracao_salvar_views
from emensageriapro.s1080.views import s1080_alteracao_api as s1080_alteracao_api_views
from emensageriapro.s1080.views import s1080_alteracao_novavalidade_apagar as s1080_alteracao_novavalidade_apagar_views
from emensageriapro.s1080.views import s1080_alteracao_novavalidade_listar as s1080_alteracao_novavalidade_listar_views
from emensageriapro.s1080.views import s1080_alteracao_novavalidade_salvar as s1080_alteracao_novavalidade_salvar_views
from emensageriapro.s1080.views import s1080_alteracao_novavalidade_api as s1080_alteracao_novavalidade_api_views
from emensageriapro.s1080.views import s1080_exclusao_apagar as s1080_exclusao_apagar_views
from emensageriapro.s1080.views import s1080_exclusao_listar as s1080_exclusao_listar_views
from emensageriapro.s1080.views import s1080_exclusao_salvar as s1080_exclusao_salvar_views
from emensageriapro.s1080.views import s1080_exclusao_api as s1080_exclusao_api_views



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


    url(r'^s1080-inclusao/apagar/(?P<hash>.*)/$', 
        s1080_inclusao_apagar_views.apagar, 
        name='s1080_inclusao_apagar'),

    url(r'^s1080-inclusao/api/$',
        s1080_inclusao_api_views.s1080inclusaoList.as_view() ),

    url(r'^s1080-inclusao/api/(?P<pk>[0-9]+)/$',
        s1080_inclusao_api_views.s1080inclusaoDetail.as_view() ),

    url(r'^s1080-inclusao/listar/(?P<hash>.*)/$', 
        s1080_inclusao_listar_views.listar, 
        name='s1080_inclusao'),

    url(r'^s1080-inclusao/salvar/(?P<hash>.*)/$', 
        s1080_inclusao_salvar_views.salvar, 
        name='s1080_inclusao_salvar'),

    url(r'^s1080-alteracao/apagar/(?P<hash>.*)/$', 
        s1080_alteracao_apagar_views.apagar, 
        name='s1080_alteracao_apagar'),

    url(r'^s1080-alteracao/api/$',
        s1080_alteracao_api_views.s1080alteracaoList.as_view() ),

    url(r'^s1080-alteracao/api/(?P<pk>[0-9]+)/$',
        s1080_alteracao_api_views.s1080alteracaoDetail.as_view() ),

    url(r'^s1080-alteracao/listar/(?P<hash>.*)/$', 
        s1080_alteracao_listar_views.listar, 
        name='s1080_alteracao'),

    url(r'^s1080-alteracao/salvar/(?P<hash>.*)/$', 
        s1080_alteracao_salvar_views.salvar, 
        name='s1080_alteracao_salvar'),

    url(r'^s1080-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1080_alteracao_novavalidade_apagar_views.apagar, 
        name='s1080_alteracao_novavalidade_apagar'),

    url(r'^s1080-alteracao-novavalidade/api/$',
        s1080_alteracao_novavalidade_api_views.s1080alteracaonovaValidadeList.as_view() ),

    url(r'^s1080-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
        s1080_alteracao_novavalidade_api_views.s1080alteracaonovaValidadeDetail.as_view() ),

    url(r'^s1080-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1080_alteracao_novavalidade_listar_views.listar, 
        name='s1080_alteracao_novavalidade'),

    url(r'^s1080-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1080_alteracao_novavalidade_salvar_views.salvar, 
        name='s1080_alteracao_novavalidade_salvar'),

    url(r'^s1080-exclusao/apagar/(?P<hash>.*)/$', 
        s1080_exclusao_apagar_views.apagar, 
        name='s1080_exclusao_apagar'),

    url(r'^s1080-exclusao/api/$',
        s1080_exclusao_api_views.s1080exclusaoList.as_view() ),

    url(r'^s1080-exclusao/api/(?P<pk>[0-9]+)/$',
        s1080_exclusao_api_views.s1080exclusaoDetail.as_view() ),

    url(r'^s1080-exclusao/listar/(?P<hash>.*)/$', 
        s1080_exclusao_listar_views.listar, 
        name='s1080_exclusao'),

    url(r'^s1080-exclusao/salvar/(?P<hash>.*)/$', 
        s1080_exclusao_salvar_views.salvar, 
        name='s1080_exclusao_salvar'),


]