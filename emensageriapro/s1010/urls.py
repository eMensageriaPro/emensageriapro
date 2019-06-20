#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1010.views import s1010_inclusao_apagar as s1010_inclusao_apagar_views
from emensageriapro.s1010.views import s1010_inclusao_listar as s1010_inclusao_listar_views
from emensageriapro.s1010.views import s1010_inclusao_salvar as s1010_inclusao_salvar_views
from emensageriapro.s1010.views import s1010_inclusao_api as s1010_inclusao_api_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocp_apagar as s1010_inclusao_ideprocessocp_apagar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocp_listar as s1010_inclusao_ideprocessocp_listar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocp_salvar as s1010_inclusao_ideprocessocp_salvar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocp_api as s1010_inclusao_ideprocessocp_api_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessoirrf_apagar as s1010_inclusao_ideprocessoirrf_apagar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessoirrf_listar as s1010_inclusao_ideprocessoirrf_listar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessoirrf_salvar as s1010_inclusao_ideprocessoirrf_salvar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessoirrf_api as s1010_inclusao_ideprocessoirrf_api_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessofgts_apagar as s1010_inclusao_ideprocessofgts_apagar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessofgts_listar as s1010_inclusao_ideprocessofgts_listar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessofgts_salvar as s1010_inclusao_ideprocessofgts_salvar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessofgts_api as s1010_inclusao_ideprocessofgts_api_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessosind_apagar as s1010_inclusao_ideprocessosind_apagar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessosind_listar as s1010_inclusao_ideprocessosind_listar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessosind_salvar as s1010_inclusao_ideprocessosind_salvar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessosind_api as s1010_inclusao_ideprocessosind_api_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocprp_apagar as s1010_inclusao_ideprocessocprp_apagar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocprp_listar as s1010_inclusao_ideprocessocprp_listar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocprp_salvar as s1010_inclusao_ideprocessocprp_salvar_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocprp_api as s1010_inclusao_ideprocessocprp_api_views
from emensageriapro.s1010.views import s1010_alteracao_apagar as s1010_alteracao_apagar_views
from emensageriapro.s1010.views import s1010_alteracao_listar as s1010_alteracao_listar_views
from emensageriapro.s1010.views import s1010_alteracao_salvar as s1010_alteracao_salvar_views
from emensageriapro.s1010.views import s1010_alteracao_api as s1010_alteracao_api_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocp_apagar as s1010_alteracao_ideprocessocp_apagar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocp_listar as s1010_alteracao_ideprocessocp_listar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocp_salvar as s1010_alteracao_ideprocessocp_salvar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocp_api as s1010_alteracao_ideprocessocp_api_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessoirrf_apagar as s1010_alteracao_ideprocessoirrf_apagar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessoirrf_listar as s1010_alteracao_ideprocessoirrf_listar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessoirrf_salvar as s1010_alteracao_ideprocessoirrf_salvar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessoirrf_api as s1010_alteracao_ideprocessoirrf_api_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessofgts_apagar as s1010_alteracao_ideprocessofgts_apagar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessofgts_listar as s1010_alteracao_ideprocessofgts_listar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessofgts_salvar as s1010_alteracao_ideprocessofgts_salvar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessofgts_api as s1010_alteracao_ideprocessofgts_api_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessosind_apagar as s1010_alteracao_ideprocessosind_apagar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessosind_listar as s1010_alteracao_ideprocessosind_listar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessosind_salvar as s1010_alteracao_ideprocessosind_salvar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessosind_api as s1010_alteracao_ideprocessosind_api_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocprp_apagar as s1010_alteracao_ideprocessocprp_apagar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocprp_listar as s1010_alteracao_ideprocessocprp_listar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocprp_salvar as s1010_alteracao_ideprocessocprp_salvar_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocprp_api as s1010_alteracao_ideprocessocprp_api_views
from emensageriapro.s1010.views import s1010_alteracao_novavalidade_apagar as s1010_alteracao_novavalidade_apagar_views
from emensageriapro.s1010.views import s1010_alteracao_novavalidade_listar as s1010_alteracao_novavalidade_listar_views
from emensageriapro.s1010.views import s1010_alteracao_novavalidade_salvar as s1010_alteracao_novavalidade_salvar_views
from emensageriapro.s1010.views import s1010_alteracao_novavalidade_api as s1010_alteracao_novavalidade_api_views
from emensageriapro.s1010.views import s1010_exclusao_apagar as s1010_exclusao_apagar_views
from emensageriapro.s1010.views import s1010_exclusao_listar as s1010_exclusao_listar_views
from emensageriapro.s1010.views import s1010_exclusao_salvar as s1010_exclusao_salvar_views
from emensageriapro.s1010.views import s1010_exclusao_api as s1010_exclusao_api_views



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


    url(r'^s1010-inclusao/apagar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_apagar_views.apagar, 
        name='s1010_inclusao_apagar'),

    url(r'^s1010-inclusao/api/$',
        s1010_inclusao_api_views.s1010inclusaoList.as_view() ),

    url(r'^s1010-inclusao/api/(?P<pk>[0-9]+)/$',
        s1010_inclusao_api_views.s1010inclusaoDetail.as_view() ),

    url(r'^s1010-inclusao/$', 
        s1010_inclusao_listar_views.listar, 
        name='s1010_inclusao'),

    url(r'^s1010-inclusao/salvar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_salvar_views.salvar, 
        name='s1010_inclusao_salvar'),

    url(r'^s1010-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_inclusao_salvar_views.salvar, 
        name='s1010_inclusao_salvar_tab'),
        
    url(r'^s1010-inclusao/cadastrar/$', 
        s1010_inclusao_salvar_views.salvar, 
        name='s1010_inclusao_cadastrar'),

    url(r'^s1010-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_inclusao_salvar_views.salvar, 
        name='s1010_inclusao_salvar_output'),
        
    url(r'^s1010-inclusao/(?P<output>[\w-]+)/$', 
        s1010_inclusao_listar_views.listar, 
        name='s1010_inclusao_output'),

    url(r'^s1010-inclusao-ideprocessocp/apagar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessocp_apagar_views.apagar, 
        name='s1010_inclusao_ideprocessocp_apagar'),

    url(r'^s1010-inclusao-ideprocessocp/api/$',
        s1010_inclusao_ideprocessocp_api_views.s1010inclusaoideProcessoCPList.as_view() ),

    url(r'^s1010-inclusao-ideprocessocp/api/(?P<pk>[0-9]+)/$',
        s1010_inclusao_ideprocessocp_api_views.s1010inclusaoideProcessoCPDetail.as_view() ),

    url(r'^s1010-inclusao-ideprocessocp/$', 
        s1010_inclusao_ideprocessocp_listar_views.listar, 
        name='s1010_inclusao_ideprocessocp'),

    url(r'^s1010-inclusao-ideprocessocp/salvar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessocp_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessocp_salvar'),

    url(r'^s1010-inclusao-ideprocessocp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_inclusao_ideprocessocp_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessocp_salvar_tab'),
        
    url(r'^s1010-inclusao-ideprocessocp/cadastrar/$', 
        s1010_inclusao_ideprocessocp_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessocp_cadastrar'),

    url(r'^s1010-inclusao-ideprocessocp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessocp_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessocp_salvar_output'),
        
    url(r'^s1010-inclusao-ideprocessocp/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessocp_listar_views.listar, 
        name='s1010_inclusao_ideprocessocp_output'),

    url(r'^s1010-inclusao-ideprocessoirrf/apagar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessoirrf_apagar_views.apagar, 
        name='s1010_inclusao_ideprocessoirrf_apagar'),

    url(r'^s1010-inclusao-ideprocessoirrf/api/$',
        s1010_inclusao_ideprocessoirrf_api_views.s1010inclusaoideProcessoIRRFList.as_view() ),

    url(r'^s1010-inclusao-ideprocessoirrf/api/(?P<pk>[0-9]+)/$',
        s1010_inclusao_ideprocessoirrf_api_views.s1010inclusaoideProcessoIRRFDetail.as_view() ),

    url(r'^s1010-inclusao-ideprocessoirrf/$', 
        s1010_inclusao_ideprocessoirrf_listar_views.listar, 
        name='s1010_inclusao_ideprocessoirrf'),

    url(r'^s1010-inclusao-ideprocessoirrf/salvar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessoirrf_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessoirrf_salvar'),

    url(r'^s1010-inclusao-ideprocessoirrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_inclusao_ideprocessoirrf_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessoirrf_salvar_tab'),
        
    url(r'^s1010-inclusao-ideprocessoirrf/cadastrar/$', 
        s1010_inclusao_ideprocessoirrf_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessoirrf_cadastrar'),

    url(r'^s1010-inclusao-ideprocessoirrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessoirrf_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessoirrf_salvar_output'),
        
    url(r'^s1010-inclusao-ideprocessoirrf/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessoirrf_listar_views.listar, 
        name='s1010_inclusao_ideprocessoirrf_output'),

    url(r'^s1010-inclusao-ideprocessofgts/apagar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessofgts_apagar_views.apagar, 
        name='s1010_inclusao_ideprocessofgts_apagar'),

    url(r'^s1010-inclusao-ideprocessofgts/api/$',
        s1010_inclusao_ideprocessofgts_api_views.s1010inclusaoideProcessoFGTSList.as_view() ),

    url(r'^s1010-inclusao-ideprocessofgts/api/(?P<pk>[0-9]+)/$',
        s1010_inclusao_ideprocessofgts_api_views.s1010inclusaoideProcessoFGTSDetail.as_view() ),

    url(r'^s1010-inclusao-ideprocessofgts/$', 
        s1010_inclusao_ideprocessofgts_listar_views.listar, 
        name='s1010_inclusao_ideprocessofgts'),

    url(r'^s1010-inclusao-ideprocessofgts/salvar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessofgts_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessofgts_salvar'),

    url(r'^s1010-inclusao-ideprocessofgts/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_inclusao_ideprocessofgts_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessofgts_salvar_tab'),
        
    url(r'^s1010-inclusao-ideprocessofgts/cadastrar/$', 
        s1010_inclusao_ideprocessofgts_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessofgts_cadastrar'),

    url(r'^s1010-inclusao-ideprocessofgts/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessofgts_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessofgts_salvar_output'),
        
    url(r'^s1010-inclusao-ideprocessofgts/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessofgts_listar_views.listar, 
        name='s1010_inclusao_ideprocessofgts_output'),

    url(r'^s1010-inclusao-ideprocessosind/apagar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessosind_apagar_views.apagar, 
        name='s1010_inclusao_ideprocessosind_apagar'),

    url(r'^s1010-inclusao-ideprocessosind/api/$',
        s1010_inclusao_ideprocessosind_api_views.s1010inclusaoideProcessoSINDList.as_view() ),

    url(r'^s1010-inclusao-ideprocessosind/api/(?P<pk>[0-9]+)/$',
        s1010_inclusao_ideprocessosind_api_views.s1010inclusaoideProcessoSINDDetail.as_view() ),

    url(r'^s1010-inclusao-ideprocessosind/$', 
        s1010_inclusao_ideprocessosind_listar_views.listar, 
        name='s1010_inclusao_ideprocessosind'),

    url(r'^s1010-inclusao-ideprocessosind/salvar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessosind_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessosind_salvar'),

    url(r'^s1010-inclusao-ideprocessosind/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_inclusao_ideprocessosind_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessosind_salvar_tab'),
        
    url(r'^s1010-inclusao-ideprocessosind/cadastrar/$', 
        s1010_inclusao_ideprocessosind_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessosind_cadastrar'),

    url(r'^s1010-inclusao-ideprocessosind/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessosind_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessosind_salvar_output'),
        
    url(r'^s1010-inclusao-ideprocessosind/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessosind_listar_views.listar, 
        name='s1010_inclusao_ideprocessosind_output'),

    url(r'^s1010-inclusao-ideprocessocprp/apagar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessocprp_apagar_views.apagar, 
        name='s1010_inclusao_ideprocessocprp_apagar'),

    url(r'^s1010-inclusao-ideprocessocprp/api/$',
        s1010_inclusao_ideprocessocprp_api_views.s1010inclusaoideProcessoCPRPList.as_view() ),

    url(r'^s1010-inclusao-ideprocessocprp/api/(?P<pk>[0-9]+)/$',
        s1010_inclusao_ideprocessocprp_api_views.s1010inclusaoideProcessoCPRPDetail.as_view() ),

    url(r'^s1010-inclusao-ideprocessocprp/$', 
        s1010_inclusao_ideprocessocprp_listar_views.listar, 
        name='s1010_inclusao_ideprocessocprp'),

    url(r'^s1010-inclusao-ideprocessocprp/salvar/(?P<pk>[0-9]+)/$', 
        s1010_inclusao_ideprocessocprp_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessocprp_salvar'),

    url(r'^s1010-inclusao-ideprocessocprp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_inclusao_ideprocessocprp_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessocprp_salvar_tab'),
        
    url(r'^s1010-inclusao-ideprocessocprp/cadastrar/$', 
        s1010_inclusao_ideprocessocprp_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessocprp_cadastrar'),

    url(r'^s1010-inclusao-ideprocessocprp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessocprp_salvar_views.salvar, 
        name='s1010_inclusao_ideprocessocprp_salvar_output'),
        
    url(r'^s1010-inclusao-ideprocessocprp/(?P<output>[\w-]+)/$', 
        s1010_inclusao_ideprocessocprp_listar_views.listar, 
        name='s1010_inclusao_ideprocessocprp_output'),

    url(r'^s1010-alteracao/apagar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_apagar_views.apagar, 
        name='s1010_alteracao_apagar'),

    url(r'^s1010-alteracao/api/$',
        s1010_alteracao_api_views.s1010alteracaoList.as_view() ),

    url(r'^s1010-alteracao/api/(?P<pk>[0-9]+)/$',
        s1010_alteracao_api_views.s1010alteracaoDetail.as_view() ),

    url(r'^s1010-alteracao/$', 
        s1010_alteracao_listar_views.listar, 
        name='s1010_alteracao'),

    url(r'^s1010-alteracao/salvar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_salvar_views.salvar, 
        name='s1010_alteracao_salvar'),

    url(r'^s1010-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_alteracao_salvar_views.salvar, 
        name='s1010_alteracao_salvar_tab'),
        
    url(r'^s1010-alteracao/cadastrar/$', 
        s1010_alteracao_salvar_views.salvar, 
        name='s1010_alteracao_cadastrar'),

    url(r'^s1010-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_alteracao_salvar_views.salvar, 
        name='s1010_alteracao_salvar_output'),
        
    url(r'^s1010-alteracao/(?P<output>[\w-]+)/$', 
        s1010_alteracao_listar_views.listar, 
        name='s1010_alteracao_output'),

    url(r'^s1010-alteracao-ideprocessocp/apagar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessocp_apagar_views.apagar, 
        name='s1010_alteracao_ideprocessocp_apagar'),

    url(r'^s1010-alteracao-ideprocessocp/api/$',
        s1010_alteracao_ideprocessocp_api_views.s1010alteracaoideProcessoCPList.as_view() ),

    url(r'^s1010-alteracao-ideprocessocp/api/(?P<pk>[0-9]+)/$',
        s1010_alteracao_ideprocessocp_api_views.s1010alteracaoideProcessoCPDetail.as_view() ),

    url(r'^s1010-alteracao-ideprocessocp/$', 
        s1010_alteracao_ideprocessocp_listar_views.listar, 
        name='s1010_alteracao_ideprocessocp'),

    url(r'^s1010-alteracao-ideprocessocp/salvar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessocp_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessocp_salvar'),

    url(r'^s1010-alteracao-ideprocessocp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_alteracao_ideprocessocp_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessocp_salvar_tab'),
        
    url(r'^s1010-alteracao-ideprocessocp/cadastrar/$', 
        s1010_alteracao_ideprocessocp_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessocp_cadastrar'),

    url(r'^s1010-alteracao-ideprocessocp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessocp_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessocp_salvar_output'),
        
    url(r'^s1010-alteracao-ideprocessocp/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessocp_listar_views.listar, 
        name='s1010_alteracao_ideprocessocp_output'),

    url(r'^s1010-alteracao-ideprocessoirrf/apagar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessoirrf_apagar_views.apagar, 
        name='s1010_alteracao_ideprocessoirrf_apagar'),

    url(r'^s1010-alteracao-ideprocessoirrf/api/$',
        s1010_alteracao_ideprocessoirrf_api_views.s1010alteracaoideProcessoIRRFList.as_view() ),

    url(r'^s1010-alteracao-ideprocessoirrf/api/(?P<pk>[0-9]+)/$',
        s1010_alteracao_ideprocessoirrf_api_views.s1010alteracaoideProcessoIRRFDetail.as_view() ),

    url(r'^s1010-alteracao-ideprocessoirrf/$', 
        s1010_alteracao_ideprocessoirrf_listar_views.listar, 
        name='s1010_alteracao_ideprocessoirrf'),

    url(r'^s1010-alteracao-ideprocessoirrf/salvar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessoirrf_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessoirrf_salvar'),

    url(r'^s1010-alteracao-ideprocessoirrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_alteracao_ideprocessoirrf_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessoirrf_salvar_tab'),
        
    url(r'^s1010-alteracao-ideprocessoirrf/cadastrar/$', 
        s1010_alteracao_ideprocessoirrf_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessoirrf_cadastrar'),

    url(r'^s1010-alteracao-ideprocessoirrf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessoirrf_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessoirrf_salvar_output'),
        
    url(r'^s1010-alteracao-ideprocessoirrf/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessoirrf_listar_views.listar, 
        name='s1010_alteracao_ideprocessoirrf_output'),

    url(r'^s1010-alteracao-ideprocessofgts/apagar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessofgts_apagar_views.apagar, 
        name='s1010_alteracao_ideprocessofgts_apagar'),

    url(r'^s1010-alteracao-ideprocessofgts/api/$',
        s1010_alteracao_ideprocessofgts_api_views.s1010alteracaoideProcessoFGTSList.as_view() ),

    url(r'^s1010-alteracao-ideprocessofgts/api/(?P<pk>[0-9]+)/$',
        s1010_alteracao_ideprocessofgts_api_views.s1010alteracaoideProcessoFGTSDetail.as_view() ),

    url(r'^s1010-alteracao-ideprocessofgts/$', 
        s1010_alteracao_ideprocessofgts_listar_views.listar, 
        name='s1010_alteracao_ideprocessofgts'),

    url(r'^s1010-alteracao-ideprocessofgts/salvar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessofgts_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessofgts_salvar'),

    url(r'^s1010-alteracao-ideprocessofgts/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_alteracao_ideprocessofgts_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessofgts_salvar_tab'),
        
    url(r'^s1010-alteracao-ideprocessofgts/cadastrar/$', 
        s1010_alteracao_ideprocessofgts_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessofgts_cadastrar'),

    url(r'^s1010-alteracao-ideprocessofgts/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessofgts_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessofgts_salvar_output'),
        
    url(r'^s1010-alteracao-ideprocessofgts/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessofgts_listar_views.listar, 
        name='s1010_alteracao_ideprocessofgts_output'),

    url(r'^s1010-alteracao-ideprocessosind/apagar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessosind_apagar_views.apagar, 
        name='s1010_alteracao_ideprocessosind_apagar'),

    url(r'^s1010-alteracao-ideprocessosind/api/$',
        s1010_alteracao_ideprocessosind_api_views.s1010alteracaoideProcessoSINDList.as_view() ),

    url(r'^s1010-alteracao-ideprocessosind/api/(?P<pk>[0-9]+)/$',
        s1010_alteracao_ideprocessosind_api_views.s1010alteracaoideProcessoSINDDetail.as_view() ),

    url(r'^s1010-alteracao-ideprocessosind/$', 
        s1010_alteracao_ideprocessosind_listar_views.listar, 
        name='s1010_alteracao_ideprocessosind'),

    url(r'^s1010-alteracao-ideprocessosind/salvar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessosind_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessosind_salvar'),

    url(r'^s1010-alteracao-ideprocessosind/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_alteracao_ideprocessosind_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessosind_salvar_tab'),
        
    url(r'^s1010-alteracao-ideprocessosind/cadastrar/$', 
        s1010_alteracao_ideprocessosind_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessosind_cadastrar'),

    url(r'^s1010-alteracao-ideprocessosind/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessosind_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessosind_salvar_output'),
        
    url(r'^s1010-alteracao-ideprocessosind/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessosind_listar_views.listar, 
        name='s1010_alteracao_ideprocessosind_output'),

    url(r'^s1010-alteracao-ideprocessocprp/apagar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessocprp_apagar_views.apagar, 
        name='s1010_alteracao_ideprocessocprp_apagar'),

    url(r'^s1010-alteracao-ideprocessocprp/api/$',
        s1010_alteracao_ideprocessocprp_api_views.s1010alteracaoideProcessoCPRPList.as_view() ),

    url(r'^s1010-alteracao-ideprocessocprp/api/(?P<pk>[0-9]+)/$',
        s1010_alteracao_ideprocessocprp_api_views.s1010alteracaoideProcessoCPRPDetail.as_view() ),

    url(r'^s1010-alteracao-ideprocessocprp/$', 
        s1010_alteracao_ideprocessocprp_listar_views.listar, 
        name='s1010_alteracao_ideprocessocprp'),

    url(r'^s1010-alteracao-ideprocessocprp/salvar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_ideprocessocprp_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessocprp_salvar'),

    url(r'^s1010-alteracao-ideprocessocprp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_alteracao_ideprocessocprp_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessocprp_salvar_tab'),
        
    url(r'^s1010-alteracao-ideprocessocprp/cadastrar/$', 
        s1010_alteracao_ideprocessocprp_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessocprp_cadastrar'),

    url(r'^s1010-alteracao-ideprocessocprp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessocprp_salvar_views.salvar, 
        name='s1010_alteracao_ideprocessocprp_salvar_output'),
        
    url(r'^s1010-alteracao-ideprocessocprp/(?P<output>[\w-]+)/$', 
        s1010_alteracao_ideprocessocprp_listar_views.listar, 
        name='s1010_alteracao_ideprocessocprp_output'),

    url(r'^s1010-alteracao-novavalidade/apagar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_novavalidade_apagar_views.apagar, 
        name='s1010_alteracao_novavalidade_apagar'),

    url(r'^s1010-alteracao-novavalidade/api/$',
        s1010_alteracao_novavalidade_api_views.s1010alteracaonovaValidadeList.as_view() ),

    url(r'^s1010-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
        s1010_alteracao_novavalidade_api_views.s1010alteracaonovaValidadeDetail.as_view() ),

    url(r'^s1010-alteracao-novavalidade/$', 
        s1010_alteracao_novavalidade_listar_views.listar, 
        name='s1010_alteracao_novavalidade'),

    url(r'^s1010-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/$', 
        s1010_alteracao_novavalidade_salvar_views.salvar, 
        name='s1010_alteracao_novavalidade_salvar'),

    url(r'^s1010-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_alteracao_novavalidade_salvar_views.salvar, 
        name='s1010_alteracao_novavalidade_salvar_tab'),
        
    url(r'^s1010-alteracao-novavalidade/cadastrar/$', 
        s1010_alteracao_novavalidade_salvar_views.salvar, 
        name='s1010_alteracao_novavalidade_cadastrar'),

    url(r'^s1010-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_alteracao_novavalidade_salvar_views.salvar, 
        name='s1010_alteracao_novavalidade_salvar_output'),
        
    url(r'^s1010-alteracao-novavalidade/(?P<output>[\w-]+)/$', 
        s1010_alteracao_novavalidade_listar_views.listar, 
        name='s1010_alteracao_novavalidade_output'),

    url(r'^s1010-exclusao/apagar/(?P<pk>[0-9]+)/$', 
        s1010_exclusao_apagar_views.apagar, 
        name='s1010_exclusao_apagar'),

    url(r'^s1010-exclusao/api/$',
        s1010_exclusao_api_views.s1010exclusaoList.as_view() ),

    url(r'^s1010-exclusao/api/(?P<pk>[0-9]+)/$',
        s1010_exclusao_api_views.s1010exclusaoDetail.as_view() ),

    url(r'^s1010-exclusao/$', 
        s1010_exclusao_listar_views.listar, 
        name='s1010_exclusao'),

    url(r'^s1010-exclusao/salvar/(?P<pk>[0-9]+)/$', 
        s1010_exclusao_salvar_views.salvar, 
        name='s1010_exclusao_salvar'),

    url(r'^s1010-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1010_exclusao_salvar_views.salvar, 
        name='s1010_exclusao_salvar_tab'),
        
    url(r'^s1010-exclusao/cadastrar/$', 
        s1010_exclusao_salvar_views.salvar, 
        name='s1010_exclusao_cadastrar'),

    url(r'^s1010-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1010_exclusao_salvar_views.salvar, 
        name='s1010_exclusao_salvar_output'),
        
    url(r'^s1010-exclusao/(?P<output>[\w-]+)/$', 
        s1010_exclusao_listar_views.listar, 
        name='s1010_exclusao_output'),


]