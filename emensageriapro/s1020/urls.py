#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1020.views import s1020_inclusao_apagar as s1020_inclusao_apagar_views
from emensageriapro.s1020.views import s1020_inclusao_listar as s1020_inclusao_listar_views
from emensageriapro.s1020.views import s1020_inclusao_salvar as s1020_inclusao_salvar_views
from emensageriapro.s1020.views import s1020_inclusao_api as s1020_inclusao_api_views
from emensageriapro.s1020.views import s1020_inclusao_infoprocjudterceiros_apagar as s1020_inclusao_infoprocjudterceiros_apagar_views
from emensageriapro.s1020.views import s1020_inclusao_infoprocjudterceiros_listar as s1020_inclusao_infoprocjudterceiros_listar_views
from emensageriapro.s1020.views import s1020_inclusao_infoprocjudterceiros_salvar as s1020_inclusao_infoprocjudterceiros_salvar_views
from emensageriapro.s1020.views import s1020_inclusao_infoprocjudterceiros_api as s1020_inclusao_infoprocjudterceiros_api_views
from emensageriapro.s1020.views import s1020_inclusao_procjudterceiro_apagar as s1020_inclusao_procjudterceiro_apagar_views
from emensageriapro.s1020.views import s1020_inclusao_procjudterceiro_listar as s1020_inclusao_procjudterceiro_listar_views
from emensageriapro.s1020.views import s1020_inclusao_procjudterceiro_salvar as s1020_inclusao_procjudterceiro_salvar_views
from emensageriapro.s1020.views import s1020_inclusao_procjudterceiro_api as s1020_inclusao_procjudterceiro_api_views
from emensageriapro.s1020.views import s1020_inclusao_infoemprparcial_apagar as s1020_inclusao_infoemprparcial_apagar_views
from emensageriapro.s1020.views import s1020_inclusao_infoemprparcial_listar as s1020_inclusao_infoemprparcial_listar_views
from emensageriapro.s1020.views import s1020_inclusao_infoemprparcial_salvar as s1020_inclusao_infoemprparcial_salvar_views
from emensageriapro.s1020.views import s1020_inclusao_infoemprparcial_api as s1020_inclusao_infoemprparcial_api_views
from emensageriapro.s1020.views import s1020_alteracao_apagar as s1020_alteracao_apagar_views
from emensageriapro.s1020.views import s1020_alteracao_listar as s1020_alteracao_listar_views
from emensageriapro.s1020.views import s1020_alteracao_salvar as s1020_alteracao_salvar_views
from emensageriapro.s1020.views import s1020_alteracao_api as s1020_alteracao_api_views
from emensageriapro.s1020.views import s1020_alteracao_infoprocjudterceiros_apagar as s1020_alteracao_infoprocjudterceiros_apagar_views
from emensageriapro.s1020.views import s1020_alteracao_infoprocjudterceiros_listar as s1020_alteracao_infoprocjudterceiros_listar_views
from emensageriapro.s1020.views import s1020_alteracao_infoprocjudterceiros_salvar as s1020_alteracao_infoprocjudterceiros_salvar_views
from emensageriapro.s1020.views import s1020_alteracao_infoprocjudterceiros_api as s1020_alteracao_infoprocjudterceiros_api_views
from emensageriapro.s1020.views import s1020_alteracao_procjudterceiro_apagar as s1020_alteracao_procjudterceiro_apagar_views
from emensageriapro.s1020.views import s1020_alteracao_procjudterceiro_listar as s1020_alteracao_procjudterceiro_listar_views
from emensageriapro.s1020.views import s1020_alteracao_procjudterceiro_salvar as s1020_alteracao_procjudterceiro_salvar_views
from emensageriapro.s1020.views import s1020_alteracao_procjudterceiro_api as s1020_alteracao_procjudterceiro_api_views
from emensageriapro.s1020.views import s1020_alteracao_infoemprparcial_apagar as s1020_alteracao_infoemprparcial_apagar_views
from emensageriapro.s1020.views import s1020_alteracao_infoemprparcial_listar as s1020_alteracao_infoemprparcial_listar_views
from emensageriapro.s1020.views import s1020_alteracao_infoemprparcial_salvar as s1020_alteracao_infoemprparcial_salvar_views
from emensageriapro.s1020.views import s1020_alteracao_infoemprparcial_api as s1020_alteracao_infoemprparcial_api_views
from emensageriapro.s1020.views import s1020_alteracao_novavalidade_apagar as s1020_alteracao_novavalidade_apagar_views
from emensageriapro.s1020.views import s1020_alteracao_novavalidade_listar as s1020_alteracao_novavalidade_listar_views
from emensageriapro.s1020.views import s1020_alteracao_novavalidade_salvar as s1020_alteracao_novavalidade_salvar_views
from emensageriapro.s1020.views import s1020_alteracao_novavalidade_api as s1020_alteracao_novavalidade_api_views
from emensageriapro.s1020.views import s1020_exclusao_apagar as s1020_exclusao_apagar_views
from emensageriapro.s1020.views import s1020_exclusao_listar as s1020_exclusao_listar_views
from emensageriapro.s1020.views import s1020_exclusao_salvar as s1020_exclusao_salvar_views
from emensageriapro.s1020.views import s1020_exclusao_api as s1020_exclusao_api_views



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


    url(r'^s1020-inclusao/apagar/(?P<pk>[0-9]+)/$', 
        s1020_inclusao_apagar_views.apagar, 
        name='s1020_inclusao_apagar'),

    url(r'^s1020-inclusao/api/$',
        s1020_inclusao_api_views.s1020inclusaoList.as_view() ),

    url(r'^s1020-inclusao/api/(?P<pk>[0-9]+)/$',
        s1020_inclusao_api_views.s1020inclusaoDetail.as_view() ),

    url(r'^s1020-inclusao/$', 
        s1020_inclusao_listar_views.listar, 
        name='s1020_inclusao'),

    url(r'^s1020-inclusao/salvar/(?P<pk>[0-9]+)/$', 
        s1020_inclusao_salvar_views.salvar, 
        name='s1020_inclusao_salvar'),

    url(r'^s1020-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_inclusao_salvar_views.salvar, 
        name='s1020_inclusao_salvar_tab'),
        
    url(r'^s1020-inclusao/cadastrar/$', 
        s1020_inclusao_salvar_views.salvar, 
        name='s1020_inclusao_cadastrar'),

    url(r'^s1020-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_inclusao_salvar_views.salvar, 
        name='s1020_inclusao_salvar_output'),
        
    url(r'^s1020-inclusao/(?P<output>[\w-]+)/$', 
        s1020_inclusao_listar_views.listar, 
        name='s1020_inclusao_output'),

    url(r'^s1020-inclusao-infoprocjudterceiros/apagar/(?P<pk>[0-9]+)/$', 
        s1020_inclusao_infoprocjudterceiros_apagar_views.apagar, 
        name='s1020_inclusao_infoprocjudterceiros_apagar'),

    url(r'^s1020-inclusao-infoprocjudterceiros/api/$',
        s1020_inclusao_infoprocjudterceiros_api_views.s1020inclusaoinfoProcJudTerceirosList.as_view() ),

    url(r'^s1020-inclusao-infoprocjudterceiros/api/(?P<pk>[0-9]+)/$',
        s1020_inclusao_infoprocjudterceiros_api_views.s1020inclusaoinfoProcJudTerceirosDetail.as_view() ),

    url(r'^s1020-inclusao-infoprocjudterceiros/$', 
        s1020_inclusao_infoprocjudterceiros_listar_views.listar, 
        name='s1020_inclusao_infoprocjudterceiros'),

    url(r'^s1020-inclusao-infoprocjudterceiros/salvar/(?P<pk>[0-9]+)/$', 
        s1020_inclusao_infoprocjudterceiros_salvar_views.salvar, 
        name='s1020_inclusao_infoprocjudterceiros_salvar'),

    url(r'^s1020-inclusao-infoprocjudterceiros/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_inclusao_infoprocjudterceiros_salvar_views.salvar, 
        name='s1020_inclusao_infoprocjudterceiros_salvar_tab'),
        
    url(r'^s1020-inclusao-infoprocjudterceiros/cadastrar/$', 
        s1020_inclusao_infoprocjudterceiros_salvar_views.salvar, 
        name='s1020_inclusao_infoprocjudterceiros_cadastrar'),

    url(r'^s1020-inclusao-infoprocjudterceiros/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_inclusao_infoprocjudterceiros_salvar_views.salvar, 
        name='s1020_inclusao_infoprocjudterceiros_salvar_output'),
        
    url(r'^s1020-inclusao-infoprocjudterceiros/(?P<output>[\w-]+)/$', 
        s1020_inclusao_infoprocjudterceiros_listar_views.listar, 
        name='s1020_inclusao_infoprocjudterceiros_output'),

    url(r'^s1020-inclusao-procjudterceiro/apagar/(?P<pk>[0-9]+)/$', 
        s1020_inclusao_procjudterceiro_apagar_views.apagar, 
        name='s1020_inclusao_procjudterceiro_apagar'),

    url(r'^s1020-inclusao-procjudterceiro/api/$',
        s1020_inclusao_procjudterceiro_api_views.s1020inclusaoprocJudTerceiroList.as_view() ),

    url(r'^s1020-inclusao-procjudterceiro/api/(?P<pk>[0-9]+)/$',
        s1020_inclusao_procjudterceiro_api_views.s1020inclusaoprocJudTerceiroDetail.as_view() ),

    url(r'^s1020-inclusao-procjudterceiro/$', 
        s1020_inclusao_procjudterceiro_listar_views.listar, 
        name='s1020_inclusao_procjudterceiro'),

    url(r'^s1020-inclusao-procjudterceiro/salvar/(?P<pk>[0-9]+)/$', 
        s1020_inclusao_procjudterceiro_salvar_views.salvar, 
        name='s1020_inclusao_procjudterceiro_salvar'),

    url(r'^s1020-inclusao-procjudterceiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_inclusao_procjudterceiro_salvar_views.salvar, 
        name='s1020_inclusao_procjudterceiro_salvar_tab'),
        
    url(r'^s1020-inclusao-procjudterceiro/cadastrar/$', 
        s1020_inclusao_procjudterceiro_salvar_views.salvar, 
        name='s1020_inclusao_procjudterceiro_cadastrar'),

    url(r'^s1020-inclusao-procjudterceiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_inclusao_procjudterceiro_salvar_views.salvar, 
        name='s1020_inclusao_procjudterceiro_salvar_output'),
        
    url(r'^s1020-inclusao-procjudterceiro/(?P<output>[\w-]+)/$', 
        s1020_inclusao_procjudterceiro_listar_views.listar, 
        name='s1020_inclusao_procjudterceiro_output'),

    url(r'^s1020-inclusao-infoemprparcial/apagar/(?P<pk>[0-9]+)/$', 
        s1020_inclusao_infoemprparcial_apagar_views.apagar, 
        name='s1020_inclusao_infoemprparcial_apagar'),

    url(r'^s1020-inclusao-infoemprparcial/api/$',
        s1020_inclusao_infoemprparcial_api_views.s1020inclusaoinfoEmprParcialList.as_view() ),

    url(r'^s1020-inclusao-infoemprparcial/api/(?P<pk>[0-9]+)/$',
        s1020_inclusao_infoemprparcial_api_views.s1020inclusaoinfoEmprParcialDetail.as_view() ),

    url(r'^s1020-inclusao-infoemprparcial/$', 
        s1020_inclusao_infoemprparcial_listar_views.listar, 
        name='s1020_inclusao_infoemprparcial'),

    url(r'^s1020-inclusao-infoemprparcial/salvar/(?P<pk>[0-9]+)/$', 
        s1020_inclusao_infoemprparcial_salvar_views.salvar, 
        name='s1020_inclusao_infoemprparcial_salvar'),

    url(r'^s1020-inclusao-infoemprparcial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_inclusao_infoemprparcial_salvar_views.salvar, 
        name='s1020_inclusao_infoemprparcial_salvar_tab'),
        
    url(r'^s1020-inclusao-infoemprparcial/cadastrar/$', 
        s1020_inclusao_infoemprparcial_salvar_views.salvar, 
        name='s1020_inclusao_infoemprparcial_cadastrar'),

    url(r'^s1020-inclusao-infoemprparcial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_inclusao_infoemprparcial_salvar_views.salvar, 
        name='s1020_inclusao_infoemprparcial_salvar_output'),
        
    url(r'^s1020-inclusao-infoemprparcial/(?P<output>[\w-]+)/$', 
        s1020_inclusao_infoemprparcial_listar_views.listar, 
        name='s1020_inclusao_infoemprparcial_output'),

    url(r'^s1020-alteracao/apagar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_apagar_views.apagar, 
        name='s1020_alteracao_apagar'),

    url(r'^s1020-alteracao/api/$',
        s1020_alteracao_api_views.s1020alteracaoList.as_view() ),

    url(r'^s1020-alteracao/api/(?P<pk>[0-9]+)/$',
        s1020_alteracao_api_views.s1020alteracaoDetail.as_view() ),

    url(r'^s1020-alteracao/$', 
        s1020_alteracao_listar_views.listar, 
        name='s1020_alteracao'),

    url(r'^s1020-alteracao/salvar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_salvar_views.salvar, 
        name='s1020_alteracao_salvar'),

    url(r'^s1020-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_alteracao_salvar_views.salvar, 
        name='s1020_alteracao_salvar_tab'),
        
    url(r'^s1020-alteracao/cadastrar/$', 
        s1020_alteracao_salvar_views.salvar, 
        name='s1020_alteracao_cadastrar'),

    url(r'^s1020-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_alteracao_salvar_views.salvar, 
        name='s1020_alteracao_salvar_output'),
        
    url(r'^s1020-alteracao/(?P<output>[\w-]+)/$', 
        s1020_alteracao_listar_views.listar, 
        name='s1020_alteracao_output'),

    url(r'^s1020-alteracao-infoprocjudterceiros/apagar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_infoprocjudterceiros_apagar_views.apagar, 
        name='s1020_alteracao_infoprocjudterceiros_apagar'),

    url(r'^s1020-alteracao-infoprocjudterceiros/api/$',
        s1020_alteracao_infoprocjudterceiros_api_views.s1020alteracaoinfoProcJudTerceirosList.as_view() ),

    url(r'^s1020-alteracao-infoprocjudterceiros/api/(?P<pk>[0-9]+)/$',
        s1020_alteracao_infoprocjudterceiros_api_views.s1020alteracaoinfoProcJudTerceirosDetail.as_view() ),

    url(r'^s1020-alteracao-infoprocjudterceiros/$', 
        s1020_alteracao_infoprocjudterceiros_listar_views.listar, 
        name='s1020_alteracao_infoprocjudterceiros'),

    url(r'^s1020-alteracao-infoprocjudterceiros/salvar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_infoprocjudterceiros_salvar_views.salvar, 
        name='s1020_alteracao_infoprocjudterceiros_salvar'),

    url(r'^s1020-alteracao-infoprocjudterceiros/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_alteracao_infoprocjudterceiros_salvar_views.salvar, 
        name='s1020_alteracao_infoprocjudterceiros_salvar_tab'),
        
    url(r'^s1020-alteracao-infoprocjudterceiros/cadastrar/$', 
        s1020_alteracao_infoprocjudterceiros_salvar_views.salvar, 
        name='s1020_alteracao_infoprocjudterceiros_cadastrar'),

    url(r'^s1020-alteracao-infoprocjudterceiros/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_alteracao_infoprocjudterceiros_salvar_views.salvar, 
        name='s1020_alteracao_infoprocjudterceiros_salvar_output'),
        
    url(r'^s1020-alteracao-infoprocjudterceiros/(?P<output>[\w-]+)/$', 
        s1020_alteracao_infoprocjudterceiros_listar_views.listar, 
        name='s1020_alteracao_infoprocjudterceiros_output'),

    url(r'^s1020-alteracao-procjudterceiro/apagar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_procjudterceiro_apagar_views.apagar, 
        name='s1020_alteracao_procjudterceiro_apagar'),

    url(r'^s1020-alteracao-procjudterceiro/api/$',
        s1020_alteracao_procjudterceiro_api_views.s1020alteracaoprocJudTerceiroList.as_view() ),

    url(r'^s1020-alteracao-procjudterceiro/api/(?P<pk>[0-9]+)/$',
        s1020_alteracao_procjudterceiro_api_views.s1020alteracaoprocJudTerceiroDetail.as_view() ),

    url(r'^s1020-alteracao-procjudterceiro/$', 
        s1020_alteracao_procjudterceiro_listar_views.listar, 
        name='s1020_alteracao_procjudterceiro'),

    url(r'^s1020-alteracao-procjudterceiro/salvar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_procjudterceiro_salvar_views.salvar, 
        name='s1020_alteracao_procjudterceiro_salvar'),

    url(r'^s1020-alteracao-procjudterceiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_alteracao_procjudterceiro_salvar_views.salvar, 
        name='s1020_alteracao_procjudterceiro_salvar_tab'),
        
    url(r'^s1020-alteracao-procjudterceiro/cadastrar/$', 
        s1020_alteracao_procjudterceiro_salvar_views.salvar, 
        name='s1020_alteracao_procjudterceiro_cadastrar'),

    url(r'^s1020-alteracao-procjudterceiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_alteracao_procjudterceiro_salvar_views.salvar, 
        name='s1020_alteracao_procjudterceiro_salvar_output'),
        
    url(r'^s1020-alteracao-procjudterceiro/(?P<output>[\w-]+)/$', 
        s1020_alteracao_procjudterceiro_listar_views.listar, 
        name='s1020_alteracao_procjudterceiro_output'),

    url(r'^s1020-alteracao-infoemprparcial/apagar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_infoemprparcial_apagar_views.apagar, 
        name='s1020_alteracao_infoemprparcial_apagar'),

    url(r'^s1020-alteracao-infoemprparcial/api/$',
        s1020_alteracao_infoemprparcial_api_views.s1020alteracaoinfoEmprParcialList.as_view() ),

    url(r'^s1020-alteracao-infoemprparcial/api/(?P<pk>[0-9]+)/$',
        s1020_alteracao_infoemprparcial_api_views.s1020alteracaoinfoEmprParcialDetail.as_view() ),

    url(r'^s1020-alteracao-infoemprparcial/$', 
        s1020_alteracao_infoemprparcial_listar_views.listar, 
        name='s1020_alteracao_infoemprparcial'),

    url(r'^s1020-alteracao-infoemprparcial/salvar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_infoemprparcial_salvar_views.salvar, 
        name='s1020_alteracao_infoemprparcial_salvar'),

    url(r'^s1020-alteracao-infoemprparcial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_alteracao_infoemprparcial_salvar_views.salvar, 
        name='s1020_alteracao_infoemprparcial_salvar_tab'),
        
    url(r'^s1020-alteracao-infoemprparcial/cadastrar/$', 
        s1020_alteracao_infoemprparcial_salvar_views.salvar, 
        name='s1020_alteracao_infoemprparcial_cadastrar'),

    url(r'^s1020-alteracao-infoemprparcial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_alteracao_infoemprparcial_salvar_views.salvar, 
        name='s1020_alteracao_infoemprparcial_salvar_output'),
        
    url(r'^s1020-alteracao-infoemprparcial/(?P<output>[\w-]+)/$', 
        s1020_alteracao_infoemprparcial_listar_views.listar, 
        name='s1020_alteracao_infoemprparcial_output'),

    url(r'^s1020-alteracao-novavalidade/apagar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_novavalidade_apagar_views.apagar, 
        name='s1020_alteracao_novavalidade_apagar'),

    url(r'^s1020-alteracao-novavalidade/api/$',
        s1020_alteracao_novavalidade_api_views.s1020alteracaonovaValidadeList.as_view() ),

    url(r'^s1020-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
        s1020_alteracao_novavalidade_api_views.s1020alteracaonovaValidadeDetail.as_view() ),

    url(r'^s1020-alteracao-novavalidade/$', 
        s1020_alteracao_novavalidade_listar_views.listar, 
        name='s1020_alteracao_novavalidade'),

    url(r'^s1020-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/$', 
        s1020_alteracao_novavalidade_salvar_views.salvar, 
        name='s1020_alteracao_novavalidade_salvar'),

    url(r'^s1020-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_alteracao_novavalidade_salvar_views.salvar, 
        name='s1020_alteracao_novavalidade_salvar_tab'),
        
    url(r'^s1020-alteracao-novavalidade/cadastrar/$', 
        s1020_alteracao_novavalidade_salvar_views.salvar, 
        name='s1020_alteracao_novavalidade_cadastrar'),

    url(r'^s1020-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_alteracao_novavalidade_salvar_views.salvar, 
        name='s1020_alteracao_novavalidade_salvar_output'),
        
    url(r'^s1020-alteracao-novavalidade/(?P<output>[\w-]+)/$', 
        s1020_alteracao_novavalidade_listar_views.listar, 
        name='s1020_alteracao_novavalidade_output'),

    url(r'^s1020-exclusao/apagar/(?P<pk>[0-9]+)/$', 
        s1020_exclusao_apagar_views.apagar, 
        name='s1020_exclusao_apagar'),

    url(r'^s1020-exclusao/api/$',
        s1020_exclusao_api_views.s1020exclusaoList.as_view() ),

    url(r'^s1020-exclusao/api/(?P<pk>[0-9]+)/$',
        s1020_exclusao_api_views.s1020exclusaoDetail.as_view() ),

    url(r'^s1020-exclusao/$', 
        s1020_exclusao_listar_views.listar, 
        name='s1020_exclusao'),

    url(r'^s1020-exclusao/salvar/(?P<pk>[0-9]+)/$', 
        s1020_exclusao_salvar_views.salvar, 
        name='s1020_exclusao_salvar'),

    url(r'^s1020-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s1020_exclusao_salvar_views.salvar, 
        name='s1020_exclusao_salvar_tab'),
        
    url(r'^s1020-exclusao/cadastrar/$', 
        s1020_exclusao_salvar_views.salvar, 
        name='s1020_exclusao_cadastrar'),

    url(r'^s1020-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s1020_exclusao_salvar_views.salvar, 
        name='s1020_exclusao_salvar_output'),
        
    url(r'^s1020-exclusao/(?P<output>[\w-]+)/$', 
        s1020_exclusao_listar_views.listar, 
        name='s1020_exclusao_output'),


]