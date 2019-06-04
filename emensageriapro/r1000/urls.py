#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r1000.views import r1000_inclusao_apagar as r1000_inclusao_apagar_views
from emensageriapro.r1000.views import r1000_inclusao_listar as r1000_inclusao_listar_views
from emensageriapro.r1000.views import r1000_inclusao_salvar as r1000_inclusao_salvar_views
from emensageriapro.r1000.views import r1000_inclusao_api as r1000_inclusao_api_views
from emensageriapro.r1000.views import r1000_inclusao_softhouse_apagar as r1000_inclusao_softhouse_apagar_views
from emensageriapro.r1000.views import r1000_inclusao_softhouse_listar as r1000_inclusao_softhouse_listar_views
from emensageriapro.r1000.views import r1000_inclusao_softhouse_salvar as r1000_inclusao_softhouse_salvar_views
from emensageriapro.r1000.views import r1000_inclusao_softhouse_api as r1000_inclusao_softhouse_api_views
from emensageriapro.r1000.views import r1000_inclusao_infoefr_apagar as r1000_inclusao_infoefr_apagar_views
from emensageriapro.r1000.views import r1000_inclusao_infoefr_listar as r1000_inclusao_infoefr_listar_views
from emensageriapro.r1000.views import r1000_inclusao_infoefr_salvar as r1000_inclusao_infoefr_salvar_views
from emensageriapro.r1000.views import r1000_inclusao_infoefr_api as r1000_inclusao_infoefr_api_views
from emensageriapro.r1000.views import r1000_alteracao_apagar as r1000_alteracao_apagar_views
from emensageriapro.r1000.views import r1000_alteracao_listar as r1000_alteracao_listar_views
from emensageriapro.r1000.views import r1000_alteracao_salvar as r1000_alteracao_salvar_views
from emensageriapro.r1000.views import r1000_alteracao_api as r1000_alteracao_api_views
from emensageriapro.r1000.views import r1000_alteracao_softhouse_apagar as r1000_alteracao_softhouse_apagar_views
from emensageriapro.r1000.views import r1000_alteracao_softhouse_listar as r1000_alteracao_softhouse_listar_views
from emensageriapro.r1000.views import r1000_alteracao_softhouse_salvar as r1000_alteracao_softhouse_salvar_views
from emensageriapro.r1000.views import r1000_alteracao_softhouse_api as r1000_alteracao_softhouse_api_views
from emensageriapro.r1000.views import r1000_alteracao_infoefr_apagar as r1000_alteracao_infoefr_apagar_views
from emensageriapro.r1000.views import r1000_alteracao_infoefr_listar as r1000_alteracao_infoefr_listar_views
from emensageriapro.r1000.views import r1000_alteracao_infoefr_salvar as r1000_alteracao_infoefr_salvar_views
from emensageriapro.r1000.views import r1000_alteracao_infoefr_api as r1000_alteracao_infoefr_api_views
from emensageriapro.r1000.views import r1000_alteracao_novavalidade_apagar as r1000_alteracao_novavalidade_apagar_views
from emensageriapro.r1000.views import r1000_alteracao_novavalidade_listar as r1000_alteracao_novavalidade_listar_views
from emensageriapro.r1000.views import r1000_alteracao_novavalidade_salvar as r1000_alteracao_novavalidade_salvar_views
from emensageriapro.r1000.views import r1000_alteracao_novavalidade_api as r1000_alteracao_novavalidade_api_views
from emensageriapro.r1000.views import r1000_exclusao_apagar as r1000_exclusao_apagar_views
from emensageriapro.r1000.views import r1000_exclusao_listar as r1000_exclusao_listar_views
from emensageriapro.r1000.views import r1000_exclusao_salvar as r1000_exclusao_salvar_views
from emensageriapro.r1000.views import r1000_exclusao_api as r1000_exclusao_api_views



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


    url(r'^r1000-inclusao/apagar/(?P<pk>[0-9]+)/$', 
        r1000_inclusao_apagar_views.apagar, 
        name='r1000_inclusao_apagar'),

    url(r'^r1000-inclusao/api/$',
        r1000_inclusao_api_views.r1000inclusaoList.as_view() ),

    url(r'^r1000-inclusao/api/(?P<pk>[0-9]+)/$',
        r1000_inclusao_api_views.r1000inclusaoDetail.as_view() ),

    url(r'^r1000-inclusao/$', 
        r1000_inclusao_listar_views.listar, 
        name='r1000_inclusao'),

    url(r'^r1000-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r1000_inclusao_salvar_views.salvar, 
        name='r1000_inclusao_salvar'),
        
    url(r'^r1000-inclusao/cadastrar/$', 
        r1000_inclusao_salvar_views.salvar, 
        name='r1000_inclusao_cadastrar'),

    url(r'^r1000-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r1000_inclusao_salvar_views.salvar, 
        name='r1000_inclusao_salvar_output'),
        
    url(r'^r1000-inclusao/(?P<output>[\w-]+)/$', 
        r1000_inclusao_listar_views.listar, 
        name='r1000_inclusao_output'),

    url(r'^r1000-inclusao-softhouse/apagar/(?P<pk>[0-9]+)/$', 
        r1000_inclusao_softhouse_apagar_views.apagar, 
        name='r1000_inclusao_softhouse_apagar'),

    url(r'^r1000-inclusao-softhouse/api/$',
        r1000_inclusao_softhouse_api_views.r1000inclusaosoftHouseList.as_view() ),

    url(r'^r1000-inclusao-softhouse/api/(?P<pk>[0-9]+)/$',
        r1000_inclusao_softhouse_api_views.r1000inclusaosoftHouseDetail.as_view() ),

    url(r'^r1000-inclusao-softhouse/$', 
        r1000_inclusao_softhouse_listar_views.listar, 
        name='r1000_inclusao_softhouse'),

    url(r'^r1000-inclusao-softhouse/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r1000_inclusao_softhouse_salvar_views.salvar, 
        name='r1000_inclusao_softhouse_salvar'),
        
    url(r'^r1000-inclusao-softhouse/cadastrar/$', 
        r1000_inclusao_softhouse_salvar_views.salvar, 
        name='r1000_inclusao_softhouse_cadastrar'),

    url(r'^r1000-inclusao-softhouse/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r1000_inclusao_softhouse_salvar_views.salvar, 
        name='r1000_inclusao_softhouse_salvar_output'),
        
    url(r'^r1000-inclusao-softhouse/(?P<output>[\w-]+)/$', 
        r1000_inclusao_softhouse_listar_views.listar, 
        name='r1000_inclusao_softhouse_output'),

    url(r'^r1000-inclusao-infoefr/apagar/(?P<pk>[0-9]+)/$', 
        r1000_inclusao_infoefr_apagar_views.apagar, 
        name='r1000_inclusao_infoefr_apagar'),

    url(r'^r1000-inclusao-infoefr/api/$',
        r1000_inclusao_infoefr_api_views.r1000inclusaoinfoEFRList.as_view() ),

    url(r'^r1000-inclusao-infoefr/api/(?P<pk>[0-9]+)/$',
        r1000_inclusao_infoefr_api_views.r1000inclusaoinfoEFRDetail.as_view() ),

    url(r'^r1000-inclusao-infoefr/$', 
        r1000_inclusao_infoefr_listar_views.listar, 
        name='r1000_inclusao_infoefr'),

    url(r'^r1000-inclusao-infoefr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r1000_inclusao_infoefr_salvar_views.salvar, 
        name='r1000_inclusao_infoefr_salvar'),
        
    url(r'^r1000-inclusao-infoefr/cadastrar/$', 
        r1000_inclusao_infoefr_salvar_views.salvar, 
        name='r1000_inclusao_infoefr_cadastrar'),

    url(r'^r1000-inclusao-infoefr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r1000_inclusao_infoefr_salvar_views.salvar, 
        name='r1000_inclusao_infoefr_salvar_output'),
        
    url(r'^r1000-inclusao-infoefr/(?P<output>[\w-]+)/$', 
        r1000_inclusao_infoefr_listar_views.listar, 
        name='r1000_inclusao_infoefr_output'),

    url(r'^r1000-alteracao/apagar/(?P<pk>[0-9]+)/$', 
        r1000_alteracao_apagar_views.apagar, 
        name='r1000_alteracao_apagar'),

    url(r'^r1000-alteracao/api/$',
        r1000_alteracao_api_views.r1000alteracaoList.as_view() ),

    url(r'^r1000-alteracao/api/(?P<pk>[0-9]+)/$',
        r1000_alteracao_api_views.r1000alteracaoDetail.as_view() ),

    url(r'^r1000-alteracao/$', 
        r1000_alteracao_listar_views.listar, 
        name='r1000_alteracao'),

    url(r'^r1000-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r1000_alteracao_salvar_views.salvar, 
        name='r1000_alteracao_salvar'),
        
    url(r'^r1000-alteracao/cadastrar/$', 
        r1000_alteracao_salvar_views.salvar, 
        name='r1000_alteracao_cadastrar'),

    url(r'^r1000-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r1000_alteracao_salvar_views.salvar, 
        name='r1000_alteracao_salvar_output'),
        
    url(r'^r1000-alteracao/(?P<output>[\w-]+)/$', 
        r1000_alteracao_listar_views.listar, 
        name='r1000_alteracao_output'),

    url(r'^r1000-alteracao-softhouse/apagar/(?P<pk>[0-9]+)/$', 
        r1000_alteracao_softhouse_apagar_views.apagar, 
        name='r1000_alteracao_softhouse_apagar'),

    url(r'^r1000-alteracao-softhouse/api/$',
        r1000_alteracao_softhouse_api_views.r1000alteracaosoftHouseList.as_view() ),

    url(r'^r1000-alteracao-softhouse/api/(?P<pk>[0-9]+)/$',
        r1000_alteracao_softhouse_api_views.r1000alteracaosoftHouseDetail.as_view() ),

    url(r'^r1000-alteracao-softhouse/$', 
        r1000_alteracao_softhouse_listar_views.listar, 
        name='r1000_alteracao_softhouse'),

    url(r'^r1000-alteracao-softhouse/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r1000_alteracao_softhouse_salvar_views.salvar, 
        name='r1000_alteracao_softhouse_salvar'),
        
    url(r'^r1000-alteracao-softhouse/cadastrar/$', 
        r1000_alteracao_softhouse_salvar_views.salvar, 
        name='r1000_alteracao_softhouse_cadastrar'),

    url(r'^r1000-alteracao-softhouse/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r1000_alteracao_softhouse_salvar_views.salvar, 
        name='r1000_alteracao_softhouse_salvar_output'),
        
    url(r'^r1000-alteracao-softhouse/(?P<output>[\w-]+)/$', 
        r1000_alteracao_softhouse_listar_views.listar, 
        name='r1000_alteracao_softhouse_output'),

    url(r'^r1000-alteracao-infoefr/apagar/(?P<pk>[0-9]+)/$', 
        r1000_alteracao_infoefr_apagar_views.apagar, 
        name='r1000_alteracao_infoefr_apagar'),

    url(r'^r1000-alteracao-infoefr/api/$',
        r1000_alteracao_infoefr_api_views.r1000alteracaoinfoEFRList.as_view() ),

    url(r'^r1000-alteracao-infoefr/api/(?P<pk>[0-9]+)/$',
        r1000_alteracao_infoefr_api_views.r1000alteracaoinfoEFRDetail.as_view() ),

    url(r'^r1000-alteracao-infoefr/$', 
        r1000_alteracao_infoefr_listar_views.listar, 
        name='r1000_alteracao_infoefr'),

    url(r'^r1000-alteracao-infoefr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r1000_alteracao_infoefr_salvar_views.salvar, 
        name='r1000_alteracao_infoefr_salvar'),
        
    url(r'^r1000-alteracao-infoefr/cadastrar/$', 
        r1000_alteracao_infoefr_salvar_views.salvar, 
        name='r1000_alteracao_infoefr_cadastrar'),

    url(r'^r1000-alteracao-infoefr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r1000_alteracao_infoefr_salvar_views.salvar, 
        name='r1000_alteracao_infoefr_salvar_output'),
        
    url(r'^r1000-alteracao-infoefr/(?P<output>[\w-]+)/$', 
        r1000_alteracao_infoefr_listar_views.listar, 
        name='r1000_alteracao_infoefr_output'),

    url(r'^r1000-alteracao-novavalidade/apagar/(?P<pk>[0-9]+)/$', 
        r1000_alteracao_novavalidade_apagar_views.apagar, 
        name='r1000_alteracao_novavalidade_apagar'),

    url(r'^r1000-alteracao-novavalidade/api/$',
        r1000_alteracao_novavalidade_api_views.r1000alteracaonovaValidadeList.as_view() ),

    url(r'^r1000-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
        r1000_alteracao_novavalidade_api_views.r1000alteracaonovaValidadeDetail.as_view() ),

    url(r'^r1000-alteracao-novavalidade/$', 
        r1000_alteracao_novavalidade_listar_views.listar, 
        name='r1000_alteracao_novavalidade'),

    url(r'^r1000-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r1000_alteracao_novavalidade_salvar_views.salvar, 
        name='r1000_alteracao_novavalidade_salvar'),
        
    url(r'^r1000-alteracao-novavalidade/cadastrar/$', 
        r1000_alteracao_novavalidade_salvar_views.salvar, 
        name='r1000_alteracao_novavalidade_cadastrar'),

    url(r'^r1000-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r1000_alteracao_novavalidade_salvar_views.salvar, 
        name='r1000_alteracao_novavalidade_salvar_output'),
        
    url(r'^r1000-alteracao-novavalidade/(?P<output>[\w-]+)/$', 
        r1000_alteracao_novavalidade_listar_views.listar, 
        name='r1000_alteracao_novavalidade_output'),

    url(r'^r1000-exclusao/apagar/(?P<pk>[0-9]+)/$', 
        r1000_exclusao_apagar_views.apagar, 
        name='r1000_exclusao_apagar'),

    url(r'^r1000-exclusao/api/$',
        r1000_exclusao_api_views.r1000exclusaoList.as_view() ),

    url(r'^r1000-exclusao/api/(?P<pk>[0-9]+)/$',
        r1000_exclusao_api_views.r1000exclusaoDetail.as_view() ),

    url(r'^r1000-exclusao/$', 
        r1000_exclusao_listar_views.listar, 
        name='r1000_exclusao'),

    url(r'^r1000-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        r1000_exclusao_salvar_views.salvar, 
        name='r1000_exclusao_salvar'),
        
    url(r'^r1000-exclusao/cadastrar/$', 
        r1000_exclusao_salvar_views.salvar, 
        name='r1000_exclusao_cadastrar'),

    url(r'^r1000-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        r1000_exclusao_salvar_views.salvar, 
        name='r1000_exclusao_salvar_output'),
        
    url(r'^r1000-exclusao/(?P<output>[\w-]+)/$', 
        r1000_exclusao_listar_views.listar, 
        name='r1000_exclusao_output'),


]