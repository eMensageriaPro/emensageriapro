#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1000.views import s1000_inclusao_apagar as s1000_inclusao_apagar_views
from emensageriapro.s1000.views import s1000_inclusao_listar as s1000_inclusao_listar_views
from emensageriapro.s1000.views import s1000_inclusao_salvar as s1000_inclusao_salvar_views
from emensageriapro.s1000.views import s1000_inclusao_api as s1000_inclusao_api_views
from emensageriapro.s1000.views import s1000_inclusao_dadosisencao_apagar as s1000_inclusao_dadosisencao_apagar_views
from emensageriapro.s1000.views import s1000_inclusao_dadosisencao_listar as s1000_inclusao_dadosisencao_listar_views
from emensageriapro.s1000.views import s1000_inclusao_dadosisencao_salvar as s1000_inclusao_dadosisencao_salvar_views
from emensageriapro.s1000.views import s1000_inclusao_dadosisencao_api as s1000_inclusao_dadosisencao_api_views
from emensageriapro.s1000.views import s1000_inclusao_infoop_apagar as s1000_inclusao_infoop_apagar_views
from emensageriapro.s1000.views import s1000_inclusao_infoop_listar as s1000_inclusao_infoop_listar_views
from emensageriapro.s1000.views import s1000_inclusao_infoop_salvar as s1000_inclusao_infoop_salvar_views
from emensageriapro.s1000.views import s1000_inclusao_infoop_api as s1000_inclusao_infoop_api_views
from emensageriapro.s1000.views import s1000_inclusao_infoefr_apagar as s1000_inclusao_infoefr_apagar_views
from emensageriapro.s1000.views import s1000_inclusao_infoefr_listar as s1000_inclusao_infoefr_listar_views
from emensageriapro.s1000.views import s1000_inclusao_infoefr_salvar as s1000_inclusao_infoefr_salvar_views
from emensageriapro.s1000.views import s1000_inclusao_infoefr_api as s1000_inclusao_infoefr_api_views
from emensageriapro.s1000.views import s1000_inclusao_infoente_apagar as s1000_inclusao_infoente_apagar_views
from emensageriapro.s1000.views import s1000_inclusao_infoente_listar as s1000_inclusao_infoente_listar_views
from emensageriapro.s1000.views import s1000_inclusao_infoente_salvar as s1000_inclusao_infoente_salvar_views
from emensageriapro.s1000.views import s1000_inclusao_infoente_api as s1000_inclusao_infoente_api_views
from emensageriapro.s1000.views import s1000_inclusao_infoorginternacional_apagar as s1000_inclusao_infoorginternacional_apagar_views
from emensageriapro.s1000.views import s1000_inclusao_infoorginternacional_listar as s1000_inclusao_infoorginternacional_listar_views
from emensageriapro.s1000.views import s1000_inclusao_infoorginternacional_salvar as s1000_inclusao_infoorginternacional_salvar_views
from emensageriapro.s1000.views import s1000_inclusao_infoorginternacional_api as s1000_inclusao_infoorginternacional_api_views
from emensageriapro.s1000.views import s1000_inclusao_softwarehouse_apagar as s1000_inclusao_softwarehouse_apagar_views
from emensageriapro.s1000.views import s1000_inclusao_softwarehouse_listar as s1000_inclusao_softwarehouse_listar_views
from emensageriapro.s1000.views import s1000_inclusao_softwarehouse_salvar as s1000_inclusao_softwarehouse_salvar_views
from emensageriapro.s1000.views import s1000_inclusao_softwarehouse_api as s1000_inclusao_softwarehouse_api_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopj_apagar as s1000_inclusao_situacaopj_apagar_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopj_listar as s1000_inclusao_situacaopj_listar_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopj_salvar as s1000_inclusao_situacaopj_salvar_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopj_api as s1000_inclusao_situacaopj_api_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopf_apagar as s1000_inclusao_situacaopf_apagar_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopf_listar as s1000_inclusao_situacaopf_listar_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopf_salvar as s1000_inclusao_situacaopf_salvar_views
from emensageriapro.s1000.views import s1000_inclusao_situacaopf_api as s1000_inclusao_situacaopf_api_views
from emensageriapro.s1000.views import s1000_alteracao_apagar as s1000_alteracao_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_listar as s1000_alteracao_listar_views
from emensageriapro.s1000.views import s1000_alteracao_salvar as s1000_alteracao_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_api as s1000_alteracao_api_views
from emensageriapro.s1000.views import s1000_alteracao_dadosisencao_apagar as s1000_alteracao_dadosisencao_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_dadosisencao_listar as s1000_alteracao_dadosisencao_listar_views
from emensageriapro.s1000.views import s1000_alteracao_dadosisencao_salvar as s1000_alteracao_dadosisencao_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_dadosisencao_api as s1000_alteracao_dadosisencao_api_views
from emensageriapro.s1000.views import s1000_alteracao_infoop_apagar as s1000_alteracao_infoop_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_infoop_listar as s1000_alteracao_infoop_listar_views
from emensageriapro.s1000.views import s1000_alteracao_infoop_salvar as s1000_alteracao_infoop_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_infoop_api as s1000_alteracao_infoop_api_views
from emensageriapro.s1000.views import s1000_alteracao_infoefr_apagar as s1000_alteracao_infoefr_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_infoefr_listar as s1000_alteracao_infoefr_listar_views
from emensageriapro.s1000.views import s1000_alteracao_infoefr_salvar as s1000_alteracao_infoefr_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_infoefr_api as s1000_alteracao_infoefr_api_views
from emensageriapro.s1000.views import s1000_alteracao_infoente_apagar as s1000_alteracao_infoente_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_infoente_listar as s1000_alteracao_infoente_listar_views
from emensageriapro.s1000.views import s1000_alteracao_infoente_salvar as s1000_alteracao_infoente_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_infoente_api as s1000_alteracao_infoente_api_views
from emensageriapro.s1000.views import s1000_alteracao_infoorginternacional_apagar as s1000_alteracao_infoorginternacional_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_infoorginternacional_listar as s1000_alteracao_infoorginternacional_listar_views
from emensageriapro.s1000.views import s1000_alteracao_infoorginternacional_salvar as s1000_alteracao_infoorginternacional_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_infoorginternacional_api as s1000_alteracao_infoorginternacional_api_views
from emensageriapro.s1000.views import s1000_alteracao_softwarehouse_apagar as s1000_alteracao_softwarehouse_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_softwarehouse_listar as s1000_alteracao_softwarehouse_listar_views
from emensageriapro.s1000.views import s1000_alteracao_softwarehouse_salvar as s1000_alteracao_softwarehouse_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_softwarehouse_api as s1000_alteracao_softwarehouse_api_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopj_apagar as s1000_alteracao_situacaopj_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopj_listar as s1000_alteracao_situacaopj_listar_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopj_salvar as s1000_alteracao_situacaopj_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopj_api as s1000_alteracao_situacaopj_api_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopf_apagar as s1000_alteracao_situacaopf_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopf_listar as s1000_alteracao_situacaopf_listar_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopf_salvar as s1000_alteracao_situacaopf_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_situacaopf_api as s1000_alteracao_situacaopf_api_views
from emensageriapro.s1000.views import s1000_alteracao_novavalidade_apagar as s1000_alteracao_novavalidade_apagar_views
from emensageriapro.s1000.views import s1000_alteracao_novavalidade_listar as s1000_alteracao_novavalidade_listar_views
from emensageriapro.s1000.views import s1000_alteracao_novavalidade_salvar as s1000_alteracao_novavalidade_salvar_views
from emensageriapro.s1000.views import s1000_alteracao_novavalidade_api as s1000_alteracao_novavalidade_api_views
from emensageriapro.s1000.views import s1000_exclusao_apagar as s1000_exclusao_apagar_views
from emensageriapro.s1000.views import s1000_exclusao_listar as s1000_exclusao_listar_views
from emensageriapro.s1000.views import s1000_exclusao_salvar as s1000_exclusao_salvar_views
from emensageriapro.s1000.views import s1000_exclusao_api as s1000_exclusao_api_views



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


    url(r'^s1000-inclusao/apagar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_apagar_views.apagar, 
        name='s1000_inclusao_apagar'),

    url(r'^s1000-inclusao/api/$',
        s1000_inclusao_api_views.s1000inclusaoList.as_view() ),

    url(r'^s1000-inclusao/api/(?P<pk>[0-9]+)/$',
        s1000_inclusao_api_views.s1000inclusaoDetail.as_view() ),

    url(r'^s1000-inclusao/$', 
        s1000_inclusao_listar_views.listar, 
        name='s1000_inclusao'),

    url(r'^s1000-inclusao/salvar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_salvar_views.salvar, 
        name='s1000_inclusao_salvar'),

    url(r'^s1000-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_inclusao_salvar_views.salvar, 
        name='s1000_inclusao_salvar_tab'),
        
    url(r'^s1000-inclusao/cadastrar/$', 
        s1000_inclusao_salvar_views.salvar, 
        name='s1000_inclusao_cadastrar'),

    url(r'^s1000-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_inclusao_salvar_views.salvar, 
        name='s1000_inclusao_salvar_output'),
        
    url(r'^s1000-inclusao/(?P<output>[\w-]+)/$', 
        s1000_inclusao_listar_views.listar, 
        name='s1000_inclusao_output'),

    url(r'^s1000-inclusao-dadosisencao/apagar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_dadosisencao_apagar_views.apagar, 
        name='s1000_inclusao_dadosisencao_apagar'),

    url(r'^s1000-inclusao-dadosisencao/api/$',
        s1000_inclusao_dadosisencao_api_views.s1000inclusaodadosIsencaoList.as_view() ),

    url(r'^s1000-inclusao-dadosisencao/api/(?P<pk>[0-9]+)/$',
        s1000_inclusao_dadosisencao_api_views.s1000inclusaodadosIsencaoDetail.as_view() ),

    url(r'^s1000-inclusao-dadosisencao/$', 
        s1000_inclusao_dadosisencao_listar_views.listar, 
        name='s1000_inclusao_dadosisencao'),

    url(r'^s1000-inclusao-dadosisencao/salvar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_dadosisencao_salvar_views.salvar, 
        name='s1000_inclusao_dadosisencao_salvar'),

    url(r'^s1000-inclusao-dadosisencao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_inclusao_dadosisencao_salvar_views.salvar, 
        name='s1000_inclusao_dadosisencao_salvar_tab'),
        
    url(r'^s1000-inclusao-dadosisencao/cadastrar/$', 
        s1000_inclusao_dadosisencao_salvar_views.salvar, 
        name='s1000_inclusao_dadosisencao_cadastrar'),

    url(r'^s1000-inclusao-dadosisencao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_inclusao_dadosisencao_salvar_views.salvar, 
        name='s1000_inclusao_dadosisencao_salvar_output'),
        
    url(r'^s1000-inclusao-dadosisencao/(?P<output>[\w-]+)/$', 
        s1000_inclusao_dadosisencao_listar_views.listar, 
        name='s1000_inclusao_dadosisencao_output'),

    url(r'^s1000-inclusao-infoop/apagar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_infoop_apagar_views.apagar, 
        name='s1000_inclusao_infoop_apagar'),

    url(r'^s1000-inclusao-infoop/api/$',
        s1000_inclusao_infoop_api_views.s1000inclusaoinfoOPList.as_view() ),

    url(r'^s1000-inclusao-infoop/api/(?P<pk>[0-9]+)/$',
        s1000_inclusao_infoop_api_views.s1000inclusaoinfoOPDetail.as_view() ),

    url(r'^s1000-inclusao-infoop/$', 
        s1000_inclusao_infoop_listar_views.listar, 
        name='s1000_inclusao_infoop'),

    url(r'^s1000-inclusao-infoop/salvar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_infoop_salvar_views.salvar, 
        name='s1000_inclusao_infoop_salvar'),

    url(r'^s1000-inclusao-infoop/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_inclusao_infoop_salvar_views.salvar, 
        name='s1000_inclusao_infoop_salvar_tab'),
        
    url(r'^s1000-inclusao-infoop/cadastrar/$', 
        s1000_inclusao_infoop_salvar_views.salvar, 
        name='s1000_inclusao_infoop_cadastrar'),

    url(r'^s1000-inclusao-infoop/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_inclusao_infoop_salvar_views.salvar, 
        name='s1000_inclusao_infoop_salvar_output'),
        
    url(r'^s1000-inclusao-infoop/(?P<output>[\w-]+)/$', 
        s1000_inclusao_infoop_listar_views.listar, 
        name='s1000_inclusao_infoop_output'),

    url(r'^s1000-inclusao-infoefr/apagar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_infoefr_apagar_views.apagar, 
        name='s1000_inclusao_infoefr_apagar'),

    url(r'^s1000-inclusao-infoefr/api/$',
        s1000_inclusao_infoefr_api_views.s1000inclusaoinfoEFRList.as_view() ),

    url(r'^s1000-inclusao-infoefr/api/(?P<pk>[0-9]+)/$',
        s1000_inclusao_infoefr_api_views.s1000inclusaoinfoEFRDetail.as_view() ),

    url(r'^s1000-inclusao-infoefr/$', 
        s1000_inclusao_infoefr_listar_views.listar, 
        name='s1000_inclusao_infoefr'),

    url(r'^s1000-inclusao-infoefr/salvar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_infoefr_salvar_views.salvar, 
        name='s1000_inclusao_infoefr_salvar'),

    url(r'^s1000-inclusao-infoefr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_inclusao_infoefr_salvar_views.salvar, 
        name='s1000_inclusao_infoefr_salvar_tab'),
        
    url(r'^s1000-inclusao-infoefr/cadastrar/$', 
        s1000_inclusao_infoefr_salvar_views.salvar, 
        name='s1000_inclusao_infoefr_cadastrar'),

    url(r'^s1000-inclusao-infoefr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_inclusao_infoefr_salvar_views.salvar, 
        name='s1000_inclusao_infoefr_salvar_output'),
        
    url(r'^s1000-inclusao-infoefr/(?P<output>[\w-]+)/$', 
        s1000_inclusao_infoefr_listar_views.listar, 
        name='s1000_inclusao_infoefr_output'),

    url(r'^s1000-inclusao-infoente/apagar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_infoente_apagar_views.apagar, 
        name='s1000_inclusao_infoente_apagar'),

    url(r'^s1000-inclusao-infoente/api/$',
        s1000_inclusao_infoente_api_views.s1000inclusaoinfoEnteList.as_view() ),

    url(r'^s1000-inclusao-infoente/api/(?P<pk>[0-9]+)/$',
        s1000_inclusao_infoente_api_views.s1000inclusaoinfoEnteDetail.as_view() ),

    url(r'^s1000-inclusao-infoente/$', 
        s1000_inclusao_infoente_listar_views.listar, 
        name='s1000_inclusao_infoente'),

    url(r'^s1000-inclusao-infoente/salvar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_infoente_salvar_views.salvar, 
        name='s1000_inclusao_infoente_salvar'),

    url(r'^s1000-inclusao-infoente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_inclusao_infoente_salvar_views.salvar, 
        name='s1000_inclusao_infoente_salvar_tab'),
        
    url(r'^s1000-inclusao-infoente/cadastrar/$', 
        s1000_inclusao_infoente_salvar_views.salvar, 
        name='s1000_inclusao_infoente_cadastrar'),

    url(r'^s1000-inclusao-infoente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_inclusao_infoente_salvar_views.salvar, 
        name='s1000_inclusao_infoente_salvar_output'),
        
    url(r'^s1000-inclusao-infoente/(?P<output>[\w-]+)/$', 
        s1000_inclusao_infoente_listar_views.listar, 
        name='s1000_inclusao_infoente_output'),

    url(r'^s1000-inclusao-infoorginternacional/apagar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_infoorginternacional_apagar_views.apagar, 
        name='s1000_inclusao_infoorginternacional_apagar'),

    url(r'^s1000-inclusao-infoorginternacional/api/$',
        s1000_inclusao_infoorginternacional_api_views.s1000inclusaoinfoOrgInternacionalList.as_view() ),

    url(r'^s1000-inclusao-infoorginternacional/api/(?P<pk>[0-9]+)/$',
        s1000_inclusao_infoorginternacional_api_views.s1000inclusaoinfoOrgInternacionalDetail.as_view() ),

    url(r'^s1000-inclusao-infoorginternacional/$', 
        s1000_inclusao_infoorginternacional_listar_views.listar, 
        name='s1000_inclusao_infoorginternacional'),

    url(r'^s1000-inclusao-infoorginternacional/salvar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_infoorginternacional_salvar_views.salvar, 
        name='s1000_inclusao_infoorginternacional_salvar'),

    url(r'^s1000-inclusao-infoorginternacional/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_inclusao_infoorginternacional_salvar_views.salvar, 
        name='s1000_inclusao_infoorginternacional_salvar_tab'),
        
    url(r'^s1000-inclusao-infoorginternacional/cadastrar/$', 
        s1000_inclusao_infoorginternacional_salvar_views.salvar, 
        name='s1000_inclusao_infoorginternacional_cadastrar'),

    url(r'^s1000-inclusao-infoorginternacional/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_inclusao_infoorginternacional_salvar_views.salvar, 
        name='s1000_inclusao_infoorginternacional_salvar_output'),
        
    url(r'^s1000-inclusao-infoorginternacional/(?P<output>[\w-]+)/$', 
        s1000_inclusao_infoorginternacional_listar_views.listar, 
        name='s1000_inclusao_infoorginternacional_output'),

    url(r'^s1000-inclusao-softwarehouse/apagar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_softwarehouse_apagar_views.apagar, 
        name='s1000_inclusao_softwarehouse_apagar'),

    url(r'^s1000-inclusao-softwarehouse/api/$',
        s1000_inclusao_softwarehouse_api_views.s1000inclusaosoftwareHouseList.as_view() ),

    url(r'^s1000-inclusao-softwarehouse/api/(?P<pk>[0-9]+)/$',
        s1000_inclusao_softwarehouse_api_views.s1000inclusaosoftwareHouseDetail.as_view() ),

    url(r'^s1000-inclusao-softwarehouse/$', 
        s1000_inclusao_softwarehouse_listar_views.listar, 
        name='s1000_inclusao_softwarehouse'),

    url(r'^s1000-inclusao-softwarehouse/salvar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_softwarehouse_salvar_views.salvar, 
        name='s1000_inclusao_softwarehouse_salvar'),

    url(r'^s1000-inclusao-softwarehouse/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_inclusao_softwarehouse_salvar_views.salvar, 
        name='s1000_inclusao_softwarehouse_salvar_tab'),
        
    url(r'^s1000-inclusao-softwarehouse/cadastrar/$', 
        s1000_inclusao_softwarehouse_salvar_views.salvar, 
        name='s1000_inclusao_softwarehouse_cadastrar'),

    url(r'^s1000-inclusao-softwarehouse/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_inclusao_softwarehouse_salvar_views.salvar, 
        name='s1000_inclusao_softwarehouse_salvar_output'),
        
    url(r'^s1000-inclusao-softwarehouse/(?P<output>[\w-]+)/$', 
        s1000_inclusao_softwarehouse_listar_views.listar, 
        name='s1000_inclusao_softwarehouse_output'),

    url(r'^s1000-inclusao-situacaopj/apagar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_situacaopj_apagar_views.apagar, 
        name='s1000_inclusao_situacaopj_apagar'),

    url(r'^s1000-inclusao-situacaopj/api/$',
        s1000_inclusao_situacaopj_api_views.s1000inclusaosituacaoPJList.as_view() ),

    url(r'^s1000-inclusao-situacaopj/api/(?P<pk>[0-9]+)/$',
        s1000_inclusao_situacaopj_api_views.s1000inclusaosituacaoPJDetail.as_view() ),

    url(r'^s1000-inclusao-situacaopj/$', 
        s1000_inclusao_situacaopj_listar_views.listar, 
        name='s1000_inclusao_situacaopj'),

    url(r'^s1000-inclusao-situacaopj/salvar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_situacaopj_salvar_views.salvar, 
        name='s1000_inclusao_situacaopj_salvar'),

    url(r'^s1000-inclusao-situacaopj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_inclusao_situacaopj_salvar_views.salvar, 
        name='s1000_inclusao_situacaopj_salvar_tab'),
        
    url(r'^s1000-inclusao-situacaopj/cadastrar/$', 
        s1000_inclusao_situacaopj_salvar_views.salvar, 
        name='s1000_inclusao_situacaopj_cadastrar'),

    url(r'^s1000-inclusao-situacaopj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_inclusao_situacaopj_salvar_views.salvar, 
        name='s1000_inclusao_situacaopj_salvar_output'),
        
    url(r'^s1000-inclusao-situacaopj/(?P<output>[\w-]+)/$', 
        s1000_inclusao_situacaopj_listar_views.listar, 
        name='s1000_inclusao_situacaopj_output'),

    url(r'^s1000-inclusao-situacaopf/apagar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_situacaopf_apagar_views.apagar, 
        name='s1000_inclusao_situacaopf_apagar'),

    url(r'^s1000-inclusao-situacaopf/api/$',
        s1000_inclusao_situacaopf_api_views.s1000inclusaosituacaoPFList.as_view() ),

    url(r'^s1000-inclusao-situacaopf/api/(?P<pk>[0-9]+)/$',
        s1000_inclusao_situacaopf_api_views.s1000inclusaosituacaoPFDetail.as_view() ),

    url(r'^s1000-inclusao-situacaopf/$', 
        s1000_inclusao_situacaopf_listar_views.listar, 
        name='s1000_inclusao_situacaopf'),

    url(r'^s1000-inclusao-situacaopf/salvar/(?P<pk>[0-9]+)/$', 
        s1000_inclusao_situacaopf_salvar_views.salvar, 
        name='s1000_inclusao_situacaopf_salvar'),

    url(r'^s1000-inclusao-situacaopf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_inclusao_situacaopf_salvar_views.salvar, 
        name='s1000_inclusao_situacaopf_salvar_tab'),
        
    url(r'^s1000-inclusao-situacaopf/cadastrar/$', 
        s1000_inclusao_situacaopf_salvar_views.salvar, 
        name='s1000_inclusao_situacaopf_cadastrar'),

    url(r'^s1000-inclusao-situacaopf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_inclusao_situacaopf_salvar_views.salvar, 
        name='s1000_inclusao_situacaopf_salvar_output'),
        
    url(r'^s1000-inclusao-situacaopf/(?P<output>[\w-]+)/$', 
        s1000_inclusao_situacaopf_listar_views.listar, 
        name='s1000_inclusao_situacaopf_output'),

    url(r'^s1000-alteracao/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_apagar_views.apagar, 
        name='s1000_alteracao_apagar'),

    url(r'^s1000-alteracao/api/$',
        s1000_alteracao_api_views.s1000alteracaoList.as_view() ),

    url(r'^s1000-alteracao/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_api_views.s1000alteracaoDetail.as_view() ),

    url(r'^s1000-alteracao/$', 
        s1000_alteracao_listar_views.listar, 
        name='s1000_alteracao'),

    url(r'^s1000-alteracao/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_salvar_views.salvar, 
        name='s1000_alteracao_salvar'),

    url(r'^s1000-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_salvar_views.salvar, 
        name='s1000_alteracao_salvar_tab'),
        
    url(r'^s1000-alteracao/cadastrar/$', 
        s1000_alteracao_salvar_views.salvar, 
        name='s1000_alteracao_cadastrar'),

    url(r'^s1000-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_salvar_views.salvar, 
        name='s1000_alteracao_salvar_output'),
        
    url(r'^s1000-alteracao/(?P<output>[\w-]+)/$', 
        s1000_alteracao_listar_views.listar, 
        name='s1000_alteracao_output'),

    url(r'^s1000-alteracao-dadosisencao/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_dadosisencao_apagar_views.apagar, 
        name='s1000_alteracao_dadosisencao_apagar'),

    url(r'^s1000-alteracao-dadosisencao/api/$',
        s1000_alteracao_dadosisencao_api_views.s1000alteracaodadosIsencaoList.as_view() ),

    url(r'^s1000-alteracao-dadosisencao/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_dadosisencao_api_views.s1000alteracaodadosIsencaoDetail.as_view() ),

    url(r'^s1000-alteracao-dadosisencao/$', 
        s1000_alteracao_dadosisencao_listar_views.listar, 
        name='s1000_alteracao_dadosisencao'),

    url(r'^s1000-alteracao-dadosisencao/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_dadosisencao_salvar_views.salvar, 
        name='s1000_alteracao_dadosisencao_salvar'),

    url(r'^s1000-alteracao-dadosisencao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_dadosisencao_salvar_views.salvar, 
        name='s1000_alteracao_dadosisencao_salvar_tab'),
        
    url(r'^s1000-alteracao-dadosisencao/cadastrar/$', 
        s1000_alteracao_dadosisencao_salvar_views.salvar, 
        name='s1000_alteracao_dadosisencao_cadastrar'),

    url(r'^s1000-alteracao-dadosisencao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_dadosisencao_salvar_views.salvar, 
        name='s1000_alteracao_dadosisencao_salvar_output'),
        
    url(r'^s1000-alteracao-dadosisencao/(?P<output>[\w-]+)/$', 
        s1000_alteracao_dadosisencao_listar_views.listar, 
        name='s1000_alteracao_dadosisencao_output'),

    url(r'^s1000-alteracao-infoop/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_infoop_apagar_views.apagar, 
        name='s1000_alteracao_infoop_apagar'),

    url(r'^s1000-alteracao-infoop/api/$',
        s1000_alteracao_infoop_api_views.s1000alteracaoinfoOPList.as_view() ),

    url(r'^s1000-alteracao-infoop/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_infoop_api_views.s1000alteracaoinfoOPDetail.as_view() ),

    url(r'^s1000-alteracao-infoop/$', 
        s1000_alteracao_infoop_listar_views.listar, 
        name='s1000_alteracao_infoop'),

    url(r'^s1000-alteracao-infoop/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_infoop_salvar_views.salvar, 
        name='s1000_alteracao_infoop_salvar'),

    url(r'^s1000-alteracao-infoop/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_infoop_salvar_views.salvar, 
        name='s1000_alteracao_infoop_salvar_tab'),
        
    url(r'^s1000-alteracao-infoop/cadastrar/$', 
        s1000_alteracao_infoop_salvar_views.salvar, 
        name='s1000_alteracao_infoop_cadastrar'),

    url(r'^s1000-alteracao-infoop/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_infoop_salvar_views.salvar, 
        name='s1000_alteracao_infoop_salvar_output'),
        
    url(r'^s1000-alteracao-infoop/(?P<output>[\w-]+)/$', 
        s1000_alteracao_infoop_listar_views.listar, 
        name='s1000_alteracao_infoop_output'),

    url(r'^s1000-alteracao-infoefr/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_infoefr_apagar_views.apagar, 
        name='s1000_alteracao_infoefr_apagar'),

    url(r'^s1000-alteracao-infoefr/api/$',
        s1000_alteracao_infoefr_api_views.s1000alteracaoinfoEFRList.as_view() ),

    url(r'^s1000-alteracao-infoefr/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_infoefr_api_views.s1000alteracaoinfoEFRDetail.as_view() ),

    url(r'^s1000-alteracao-infoefr/$', 
        s1000_alteracao_infoefr_listar_views.listar, 
        name='s1000_alteracao_infoefr'),

    url(r'^s1000-alteracao-infoefr/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_infoefr_salvar_views.salvar, 
        name='s1000_alteracao_infoefr_salvar'),

    url(r'^s1000-alteracao-infoefr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_infoefr_salvar_views.salvar, 
        name='s1000_alteracao_infoefr_salvar_tab'),
        
    url(r'^s1000-alteracao-infoefr/cadastrar/$', 
        s1000_alteracao_infoefr_salvar_views.salvar, 
        name='s1000_alteracao_infoefr_cadastrar'),

    url(r'^s1000-alteracao-infoefr/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_infoefr_salvar_views.salvar, 
        name='s1000_alteracao_infoefr_salvar_output'),
        
    url(r'^s1000-alteracao-infoefr/(?P<output>[\w-]+)/$', 
        s1000_alteracao_infoefr_listar_views.listar, 
        name='s1000_alteracao_infoefr_output'),

    url(r'^s1000-alteracao-infoente/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_infoente_apagar_views.apagar, 
        name='s1000_alteracao_infoente_apagar'),

    url(r'^s1000-alteracao-infoente/api/$',
        s1000_alteracao_infoente_api_views.s1000alteracaoinfoEnteList.as_view() ),

    url(r'^s1000-alteracao-infoente/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_infoente_api_views.s1000alteracaoinfoEnteDetail.as_view() ),

    url(r'^s1000-alteracao-infoente/$', 
        s1000_alteracao_infoente_listar_views.listar, 
        name='s1000_alteracao_infoente'),

    url(r'^s1000-alteracao-infoente/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_infoente_salvar_views.salvar, 
        name='s1000_alteracao_infoente_salvar'),

    url(r'^s1000-alteracao-infoente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_infoente_salvar_views.salvar, 
        name='s1000_alteracao_infoente_salvar_tab'),
        
    url(r'^s1000-alteracao-infoente/cadastrar/$', 
        s1000_alteracao_infoente_salvar_views.salvar, 
        name='s1000_alteracao_infoente_cadastrar'),

    url(r'^s1000-alteracao-infoente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_infoente_salvar_views.salvar, 
        name='s1000_alteracao_infoente_salvar_output'),
        
    url(r'^s1000-alteracao-infoente/(?P<output>[\w-]+)/$', 
        s1000_alteracao_infoente_listar_views.listar, 
        name='s1000_alteracao_infoente_output'),

    url(r'^s1000-alteracao-infoorginternacional/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_infoorginternacional_apagar_views.apagar, 
        name='s1000_alteracao_infoorginternacional_apagar'),

    url(r'^s1000-alteracao-infoorginternacional/api/$',
        s1000_alteracao_infoorginternacional_api_views.s1000alteracaoinfoOrgInternacionalList.as_view() ),

    url(r'^s1000-alteracao-infoorginternacional/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_infoorginternacional_api_views.s1000alteracaoinfoOrgInternacionalDetail.as_view() ),

    url(r'^s1000-alteracao-infoorginternacional/$', 
        s1000_alteracao_infoorginternacional_listar_views.listar, 
        name='s1000_alteracao_infoorginternacional'),

    url(r'^s1000-alteracao-infoorginternacional/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_infoorginternacional_salvar_views.salvar, 
        name='s1000_alteracao_infoorginternacional_salvar'),

    url(r'^s1000-alteracao-infoorginternacional/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_infoorginternacional_salvar_views.salvar, 
        name='s1000_alteracao_infoorginternacional_salvar_tab'),
        
    url(r'^s1000-alteracao-infoorginternacional/cadastrar/$', 
        s1000_alteracao_infoorginternacional_salvar_views.salvar, 
        name='s1000_alteracao_infoorginternacional_cadastrar'),

    url(r'^s1000-alteracao-infoorginternacional/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_infoorginternacional_salvar_views.salvar, 
        name='s1000_alteracao_infoorginternacional_salvar_output'),
        
    url(r'^s1000-alteracao-infoorginternacional/(?P<output>[\w-]+)/$', 
        s1000_alteracao_infoorginternacional_listar_views.listar, 
        name='s1000_alteracao_infoorginternacional_output'),

    url(r'^s1000-alteracao-softwarehouse/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_softwarehouse_apagar_views.apagar, 
        name='s1000_alteracao_softwarehouse_apagar'),

    url(r'^s1000-alteracao-softwarehouse/api/$',
        s1000_alteracao_softwarehouse_api_views.s1000alteracaosoftwareHouseList.as_view() ),

    url(r'^s1000-alteracao-softwarehouse/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_softwarehouse_api_views.s1000alteracaosoftwareHouseDetail.as_view() ),

    url(r'^s1000-alteracao-softwarehouse/$', 
        s1000_alteracao_softwarehouse_listar_views.listar, 
        name='s1000_alteracao_softwarehouse'),

    url(r'^s1000-alteracao-softwarehouse/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_softwarehouse_salvar_views.salvar, 
        name='s1000_alteracao_softwarehouse_salvar'),

    url(r'^s1000-alteracao-softwarehouse/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_softwarehouse_salvar_views.salvar, 
        name='s1000_alteracao_softwarehouse_salvar_tab'),
        
    url(r'^s1000-alteracao-softwarehouse/cadastrar/$', 
        s1000_alteracao_softwarehouse_salvar_views.salvar, 
        name='s1000_alteracao_softwarehouse_cadastrar'),

    url(r'^s1000-alteracao-softwarehouse/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_softwarehouse_salvar_views.salvar, 
        name='s1000_alteracao_softwarehouse_salvar_output'),
        
    url(r'^s1000-alteracao-softwarehouse/(?P<output>[\w-]+)/$', 
        s1000_alteracao_softwarehouse_listar_views.listar, 
        name='s1000_alteracao_softwarehouse_output'),

    url(r'^s1000-alteracao-situacaopj/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_situacaopj_apagar_views.apagar, 
        name='s1000_alteracao_situacaopj_apagar'),

    url(r'^s1000-alteracao-situacaopj/api/$',
        s1000_alteracao_situacaopj_api_views.s1000alteracaosituacaoPJList.as_view() ),

    url(r'^s1000-alteracao-situacaopj/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_situacaopj_api_views.s1000alteracaosituacaoPJDetail.as_view() ),

    url(r'^s1000-alteracao-situacaopj/$', 
        s1000_alteracao_situacaopj_listar_views.listar, 
        name='s1000_alteracao_situacaopj'),

    url(r'^s1000-alteracao-situacaopj/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_situacaopj_salvar_views.salvar, 
        name='s1000_alteracao_situacaopj_salvar'),

    url(r'^s1000-alteracao-situacaopj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_situacaopj_salvar_views.salvar, 
        name='s1000_alteracao_situacaopj_salvar_tab'),
        
    url(r'^s1000-alteracao-situacaopj/cadastrar/$', 
        s1000_alteracao_situacaopj_salvar_views.salvar, 
        name='s1000_alteracao_situacaopj_cadastrar'),

    url(r'^s1000-alteracao-situacaopj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_situacaopj_salvar_views.salvar, 
        name='s1000_alteracao_situacaopj_salvar_output'),
        
    url(r'^s1000-alteracao-situacaopj/(?P<output>[\w-]+)/$', 
        s1000_alteracao_situacaopj_listar_views.listar, 
        name='s1000_alteracao_situacaopj_output'),

    url(r'^s1000-alteracao-situacaopf/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_situacaopf_apagar_views.apagar, 
        name='s1000_alteracao_situacaopf_apagar'),

    url(r'^s1000-alteracao-situacaopf/api/$',
        s1000_alteracao_situacaopf_api_views.s1000alteracaosituacaoPFList.as_view() ),

    url(r'^s1000-alteracao-situacaopf/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_situacaopf_api_views.s1000alteracaosituacaoPFDetail.as_view() ),

    url(r'^s1000-alteracao-situacaopf/$', 
        s1000_alteracao_situacaopf_listar_views.listar, 
        name='s1000_alteracao_situacaopf'),

    url(r'^s1000-alteracao-situacaopf/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_situacaopf_salvar_views.salvar, 
        name='s1000_alteracao_situacaopf_salvar'),

    url(r'^s1000-alteracao-situacaopf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_situacaopf_salvar_views.salvar, 
        name='s1000_alteracao_situacaopf_salvar_tab'),
        
    url(r'^s1000-alteracao-situacaopf/cadastrar/$', 
        s1000_alteracao_situacaopf_salvar_views.salvar, 
        name='s1000_alteracao_situacaopf_cadastrar'),

    url(r'^s1000-alteracao-situacaopf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_situacaopf_salvar_views.salvar, 
        name='s1000_alteracao_situacaopf_salvar_output'),
        
    url(r'^s1000-alteracao-situacaopf/(?P<output>[\w-]+)/$', 
        s1000_alteracao_situacaopf_listar_views.listar, 
        name='s1000_alteracao_situacaopf_output'),

    url(r'^s1000-alteracao-novavalidade/apagar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_novavalidade_apagar_views.apagar, 
        name='s1000_alteracao_novavalidade_apagar'),

    url(r'^s1000-alteracao-novavalidade/api/$',
        s1000_alteracao_novavalidade_api_views.s1000alteracaonovaValidadeList.as_view() ),

    url(r'^s1000-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
        s1000_alteracao_novavalidade_api_views.s1000alteracaonovaValidadeDetail.as_view() ),

    url(r'^s1000-alteracao-novavalidade/$', 
        s1000_alteracao_novavalidade_listar_views.listar, 
        name='s1000_alteracao_novavalidade'),

    url(r'^s1000-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/$', 
        s1000_alteracao_novavalidade_salvar_views.salvar, 
        name='s1000_alteracao_novavalidade_salvar'),

    url(r'^s1000-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_alteracao_novavalidade_salvar_views.salvar, 
        name='s1000_alteracao_novavalidade_salvar_tab'),
        
    url(r'^s1000-alteracao-novavalidade/cadastrar/$', 
        s1000_alteracao_novavalidade_salvar_views.salvar, 
        name='s1000_alteracao_novavalidade_cadastrar'),

    url(r'^s1000-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_alteracao_novavalidade_salvar_views.salvar, 
        name='s1000_alteracao_novavalidade_salvar_output'),
        
    url(r'^s1000-alteracao-novavalidade/(?P<output>[\w-]+)/$', 
        s1000_alteracao_novavalidade_listar_views.listar, 
        name='s1000_alteracao_novavalidade_output'),

    url(r'^s1000-exclusao/apagar/(?P<pk>[0-9]+)/$', 
        s1000_exclusao_apagar_views.apagar, 
        name='s1000_exclusao_apagar'),

    url(r'^s1000-exclusao/api/$',
        s1000_exclusao_api_views.s1000exclusaoList.as_view() ),

    url(r'^s1000-exclusao/api/(?P<pk>[0-9]+)/$',
        s1000_exclusao_api_views.s1000exclusaoDetail.as_view() ),

    url(r'^s1000-exclusao/$', 
        s1000_exclusao_listar_views.listar, 
        name='s1000_exclusao'),

    url(r'^s1000-exclusao/salvar/(?P<pk>[0-9]+)/$', 
        s1000_exclusao_salvar_views.salvar, 
        name='s1000_exclusao_salvar'),

    url(r'^s1000-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1000_exclusao_salvar_views.salvar, 
        name='s1000_exclusao_salvar_tab'),
        
    url(r'^s1000-exclusao/cadastrar/$', 
        s1000_exclusao_salvar_views.salvar, 
        name='s1000_exclusao_cadastrar'),

    url(r'^s1000-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1000_exclusao_salvar_views.salvar, 
        name='s1000_exclusao_salvar_output'),
        
    url(r'^s1000-exclusao/(?P<output>[\w-]+)/$', 
        s1000_exclusao_listar_views.listar, 
        name='s1000_exclusao_output'),


]