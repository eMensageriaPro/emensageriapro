# eMensageriaAI #
#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1005.views import s1005_inclusao_apagar as s1005_inclusao_apagar_views
from emensageriapro.s1005.views import s1005_inclusao_listar as s1005_inclusao_listar_views
from emensageriapro.s1005.views import s1005_inclusao_salvar as s1005_inclusao_salvar_views
from emensageriapro.s1005.views import s1005_inclusao_api as s1005_inclusao_api_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudrat_apagar as s1005_inclusao_procadmjudrat_apagar_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudrat_listar as s1005_inclusao_procadmjudrat_listar_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudrat_salvar as s1005_inclusao_procadmjudrat_salvar_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudrat_api as s1005_inclusao_procadmjudrat_api_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudfap_apagar as s1005_inclusao_procadmjudfap_apagar_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudfap_listar as s1005_inclusao_procadmjudfap_listar_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudfap_salvar as s1005_inclusao_procadmjudfap_salvar_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudfap_api as s1005_inclusao_procadmjudfap_api_views
from emensageriapro.s1005.views import s1005_inclusao_infocaepf_apagar as s1005_inclusao_infocaepf_apagar_views
from emensageriapro.s1005.views import s1005_inclusao_infocaepf_listar as s1005_inclusao_infocaepf_listar_views
from emensageriapro.s1005.views import s1005_inclusao_infocaepf_salvar as s1005_inclusao_infocaepf_salvar_views
from emensageriapro.s1005.views import s1005_inclusao_infocaepf_api as s1005_inclusao_infocaepf_api_views
from emensageriapro.s1005.views import s1005_inclusao_infoobra_apagar as s1005_inclusao_infoobra_apagar_views
from emensageriapro.s1005.views import s1005_inclusao_infoobra_listar as s1005_inclusao_infoobra_listar_views
from emensageriapro.s1005.views import s1005_inclusao_infoobra_salvar as s1005_inclusao_infoobra_salvar_views
from emensageriapro.s1005.views import s1005_inclusao_infoobra_api as s1005_inclusao_infoobra_api_views
from emensageriapro.s1005.views import s1005_inclusao_infoenteduc_apagar as s1005_inclusao_infoenteduc_apagar_views
from emensageriapro.s1005.views import s1005_inclusao_infoenteduc_listar as s1005_inclusao_infoenteduc_listar_views
from emensageriapro.s1005.views import s1005_inclusao_infoenteduc_salvar as s1005_inclusao_infoenteduc_salvar_views
from emensageriapro.s1005.views import s1005_inclusao_infoenteduc_api as s1005_inclusao_infoenteduc_api_views
from emensageriapro.s1005.views import s1005_inclusao_infopcd_apagar as s1005_inclusao_infopcd_apagar_views
from emensageriapro.s1005.views import s1005_inclusao_infopcd_listar as s1005_inclusao_infopcd_listar_views
from emensageriapro.s1005.views import s1005_inclusao_infopcd_salvar as s1005_inclusao_infopcd_salvar_views
from emensageriapro.s1005.views import s1005_inclusao_infopcd_api as s1005_inclusao_infopcd_api_views
from emensageriapro.s1005.views import s1005_alteracao_apagar as s1005_alteracao_apagar_views
from emensageriapro.s1005.views import s1005_alteracao_listar as s1005_alteracao_listar_views
from emensageriapro.s1005.views import s1005_alteracao_salvar as s1005_alteracao_salvar_views
from emensageriapro.s1005.views import s1005_alteracao_api as s1005_alteracao_api_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudrat_apagar as s1005_alteracao_procadmjudrat_apagar_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudrat_listar as s1005_alteracao_procadmjudrat_listar_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudrat_salvar as s1005_alteracao_procadmjudrat_salvar_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudrat_api as s1005_alteracao_procadmjudrat_api_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudfap_apagar as s1005_alteracao_procadmjudfap_apagar_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudfap_listar as s1005_alteracao_procadmjudfap_listar_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudfap_salvar as s1005_alteracao_procadmjudfap_salvar_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudfap_api as s1005_alteracao_procadmjudfap_api_views
from emensageriapro.s1005.views import s1005_alteracao_infocaepf_apagar as s1005_alteracao_infocaepf_apagar_views
from emensageriapro.s1005.views import s1005_alteracao_infocaepf_listar as s1005_alteracao_infocaepf_listar_views
from emensageriapro.s1005.views import s1005_alteracao_infocaepf_salvar as s1005_alteracao_infocaepf_salvar_views
from emensageriapro.s1005.views import s1005_alteracao_infocaepf_api as s1005_alteracao_infocaepf_api_views
from emensageriapro.s1005.views import s1005_alteracao_infoobra_apagar as s1005_alteracao_infoobra_apagar_views
from emensageriapro.s1005.views import s1005_alteracao_infoobra_listar as s1005_alteracao_infoobra_listar_views
from emensageriapro.s1005.views import s1005_alteracao_infoobra_salvar as s1005_alteracao_infoobra_salvar_views
from emensageriapro.s1005.views import s1005_alteracao_infoobra_api as s1005_alteracao_infoobra_api_views
from emensageriapro.s1005.views import s1005_alteracao_infoenteduc_apagar as s1005_alteracao_infoenteduc_apagar_views
from emensageriapro.s1005.views import s1005_alteracao_infoenteduc_listar as s1005_alteracao_infoenteduc_listar_views
from emensageriapro.s1005.views import s1005_alteracao_infoenteduc_salvar as s1005_alteracao_infoenteduc_salvar_views
from emensageriapro.s1005.views import s1005_alteracao_infoenteduc_api as s1005_alteracao_infoenteduc_api_views
from emensageriapro.s1005.views import s1005_alteracao_infopcd_apagar as s1005_alteracao_infopcd_apagar_views
from emensageriapro.s1005.views import s1005_alteracao_infopcd_listar as s1005_alteracao_infopcd_listar_views
from emensageriapro.s1005.views import s1005_alteracao_infopcd_salvar as s1005_alteracao_infopcd_salvar_views
from emensageriapro.s1005.views import s1005_alteracao_infopcd_api as s1005_alteracao_infopcd_api_views
from emensageriapro.s1005.views import s1005_alteracao_novavalidade_apagar as s1005_alteracao_novavalidade_apagar_views
from emensageriapro.s1005.views import s1005_alteracao_novavalidade_listar as s1005_alteracao_novavalidade_listar_views
from emensageriapro.s1005.views import s1005_alteracao_novavalidade_salvar as s1005_alteracao_novavalidade_salvar_views
from emensageriapro.s1005.views import s1005_alteracao_novavalidade_api as s1005_alteracao_novavalidade_api_views
from emensageriapro.s1005.views import s1005_exclusao_apagar as s1005_exclusao_apagar_views
from emensageriapro.s1005.views import s1005_exclusao_listar as s1005_exclusao_listar_views
from emensageriapro.s1005.views import s1005_exclusao_salvar as s1005_exclusao_salvar_views
from emensageriapro.s1005.views import s1005_exclusao_api as s1005_exclusao_api_views


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


    url(r'^s1005-inclusao/apagar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_apagar_views.apagar,
        name='s1005_inclusao_apagar'),

    url(r'^s1005-inclusao/api/$',
        s1005_inclusao_api_views.s1005inclusaoList.as_view() ),

    url(r'^s1005-inclusao/api/(?P<pk>[0-9]+)/$',
        s1005_inclusao_api_views.s1005inclusaoDetail.as_view() ),

    url(r'^s1005-inclusao/$',
        s1005_inclusao_listar_views.listar,
        name='s1005_inclusao'),

    url(r'^s1005-inclusao/salvar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_salvar_views.salvar,
        name='s1005_inclusao_salvar'),

    url(r'^s1005-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_inclusao_salvar_views.salvar,
        name='s1005_inclusao_salvar_tab'),

    url(r'^s1005-inclusao/cadastrar/$',
        s1005_inclusao_salvar_views.salvar,
        name='s1005_inclusao_cadastrar'),

    url(r'^s1005-inclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_inclusao_salvar_views.salvar,
        name='s1005_inclusao_salvar_output'),

    url(r'^s1005-inclusao/(?P<output>[\w-]+)/$',
        s1005_inclusao_listar_views.listar,
        name='s1005_inclusao_output'),

    url(r'^s1005-inclusao-procadmjudrat/apagar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_procadmjudrat_apagar_views.apagar,
        name='s1005_inclusao_procadmjudrat_apagar'),

    url(r'^s1005-inclusao-procadmjudrat/api/$',
        s1005_inclusao_procadmjudrat_api_views.s1005inclusaoprocAdmJudRatList.as_view() ),

    url(r'^s1005-inclusao-procadmjudrat/api/(?P<pk>[0-9]+)/$',
        s1005_inclusao_procadmjudrat_api_views.s1005inclusaoprocAdmJudRatDetail.as_view() ),

    url(r'^s1005-inclusao-procadmjudrat/$',
        s1005_inclusao_procadmjudrat_listar_views.listar,
        name='s1005_inclusao_procadmjudrat'),

    url(r'^s1005-inclusao-procadmjudrat/salvar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_procadmjudrat_salvar_views.salvar,
        name='s1005_inclusao_procadmjudrat_salvar'),

    url(r'^s1005-inclusao-procadmjudrat/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_inclusao_procadmjudrat_salvar_views.salvar,
        name='s1005_inclusao_procadmjudrat_salvar_tab'),

    url(r'^s1005-inclusao-procadmjudrat/cadastrar/$',
        s1005_inclusao_procadmjudrat_salvar_views.salvar,
        name='s1005_inclusao_procadmjudrat_cadastrar'),

    url(r'^s1005-inclusao-procadmjudrat/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_inclusao_procadmjudrat_salvar_views.salvar,
        name='s1005_inclusao_procadmjudrat_salvar_output'),

    url(r'^s1005-inclusao-procadmjudrat/(?P<output>[\w-]+)/$',
        s1005_inclusao_procadmjudrat_listar_views.listar,
        name='s1005_inclusao_procadmjudrat_output'),

    url(r'^s1005-inclusao-procadmjudfap/apagar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_procadmjudfap_apagar_views.apagar,
        name='s1005_inclusao_procadmjudfap_apagar'),

    url(r'^s1005-inclusao-procadmjudfap/api/$',
        s1005_inclusao_procadmjudfap_api_views.s1005inclusaoprocAdmJudFapList.as_view() ),

    url(r'^s1005-inclusao-procadmjudfap/api/(?P<pk>[0-9]+)/$',
        s1005_inclusao_procadmjudfap_api_views.s1005inclusaoprocAdmJudFapDetail.as_view() ),

    url(r'^s1005-inclusao-procadmjudfap/$',
        s1005_inclusao_procadmjudfap_listar_views.listar,
        name='s1005_inclusao_procadmjudfap'),

    url(r'^s1005-inclusao-procadmjudfap/salvar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_procadmjudfap_salvar_views.salvar,
        name='s1005_inclusao_procadmjudfap_salvar'),

    url(r'^s1005-inclusao-procadmjudfap/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_inclusao_procadmjudfap_salvar_views.salvar,
        name='s1005_inclusao_procadmjudfap_salvar_tab'),

    url(r'^s1005-inclusao-procadmjudfap/cadastrar/$',
        s1005_inclusao_procadmjudfap_salvar_views.salvar,
        name='s1005_inclusao_procadmjudfap_cadastrar'),

    url(r'^s1005-inclusao-procadmjudfap/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_inclusao_procadmjudfap_salvar_views.salvar,
        name='s1005_inclusao_procadmjudfap_salvar_output'),

    url(r'^s1005-inclusao-procadmjudfap/(?P<output>[\w-]+)/$',
        s1005_inclusao_procadmjudfap_listar_views.listar,
        name='s1005_inclusao_procadmjudfap_output'),

    url(r'^s1005-inclusao-infocaepf/apagar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infocaepf_apagar_views.apagar,
        name='s1005_inclusao_infocaepf_apagar'),

    url(r'^s1005-inclusao-infocaepf/api/$',
        s1005_inclusao_infocaepf_api_views.s1005inclusaoinfoCaepfList.as_view() ),

    url(r'^s1005-inclusao-infocaepf/api/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infocaepf_api_views.s1005inclusaoinfoCaepfDetail.as_view() ),

    url(r'^s1005-inclusao-infocaepf/$',
        s1005_inclusao_infocaepf_listar_views.listar,
        name='s1005_inclusao_infocaepf'),

    url(r'^s1005-inclusao-infocaepf/salvar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infocaepf_salvar_views.salvar,
        name='s1005_inclusao_infocaepf_salvar'),

    url(r'^s1005-inclusao-infocaepf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_inclusao_infocaepf_salvar_views.salvar,
        name='s1005_inclusao_infocaepf_salvar_tab'),

    url(r'^s1005-inclusao-infocaepf/cadastrar/$',
        s1005_inclusao_infocaepf_salvar_views.salvar,
        name='s1005_inclusao_infocaepf_cadastrar'),

    url(r'^s1005-inclusao-infocaepf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_inclusao_infocaepf_salvar_views.salvar,
        name='s1005_inclusao_infocaepf_salvar_output'),

    url(r'^s1005-inclusao-infocaepf/(?P<output>[\w-]+)/$',
        s1005_inclusao_infocaepf_listar_views.listar,
        name='s1005_inclusao_infocaepf_output'),

    url(r'^s1005-inclusao-infoobra/apagar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infoobra_apagar_views.apagar,
        name='s1005_inclusao_infoobra_apagar'),

    url(r'^s1005-inclusao-infoobra/api/$',
        s1005_inclusao_infoobra_api_views.s1005inclusaoinfoObraList.as_view() ),

    url(r'^s1005-inclusao-infoobra/api/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infoobra_api_views.s1005inclusaoinfoObraDetail.as_view() ),

    url(r'^s1005-inclusao-infoobra/$',
        s1005_inclusao_infoobra_listar_views.listar,
        name='s1005_inclusao_infoobra'),

    url(r'^s1005-inclusao-infoobra/salvar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infoobra_salvar_views.salvar,
        name='s1005_inclusao_infoobra_salvar'),

    url(r'^s1005-inclusao-infoobra/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_inclusao_infoobra_salvar_views.salvar,
        name='s1005_inclusao_infoobra_salvar_tab'),

    url(r'^s1005-inclusao-infoobra/cadastrar/$',
        s1005_inclusao_infoobra_salvar_views.salvar,
        name='s1005_inclusao_infoobra_cadastrar'),

    url(r'^s1005-inclusao-infoobra/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_inclusao_infoobra_salvar_views.salvar,
        name='s1005_inclusao_infoobra_salvar_output'),

    url(r'^s1005-inclusao-infoobra/(?P<output>[\w-]+)/$',
        s1005_inclusao_infoobra_listar_views.listar,
        name='s1005_inclusao_infoobra_output'),

    url(r'^s1005-inclusao-infoenteduc/apagar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infoenteduc_apagar_views.apagar,
        name='s1005_inclusao_infoenteduc_apagar'),

    url(r'^s1005-inclusao-infoenteduc/api/$',
        s1005_inclusao_infoenteduc_api_views.s1005inclusaoinfoEntEducList.as_view() ),

    url(r'^s1005-inclusao-infoenteduc/api/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infoenteduc_api_views.s1005inclusaoinfoEntEducDetail.as_view() ),

    url(r'^s1005-inclusao-infoenteduc/$',
        s1005_inclusao_infoenteduc_listar_views.listar,
        name='s1005_inclusao_infoenteduc'),

    url(r'^s1005-inclusao-infoenteduc/salvar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infoenteduc_salvar_views.salvar,
        name='s1005_inclusao_infoenteduc_salvar'),

    url(r'^s1005-inclusao-infoenteduc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_inclusao_infoenteduc_salvar_views.salvar,
        name='s1005_inclusao_infoenteduc_salvar_tab'),

    url(r'^s1005-inclusao-infoenteduc/cadastrar/$',
        s1005_inclusao_infoenteduc_salvar_views.salvar,
        name='s1005_inclusao_infoenteduc_cadastrar'),

    url(r'^s1005-inclusao-infoenteduc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_inclusao_infoenteduc_salvar_views.salvar,
        name='s1005_inclusao_infoenteduc_salvar_output'),

    url(r'^s1005-inclusao-infoenteduc/(?P<output>[\w-]+)/$',
        s1005_inclusao_infoenteduc_listar_views.listar,
        name='s1005_inclusao_infoenteduc_output'),

    url(r'^s1005-inclusao-infopcd/apagar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infopcd_apagar_views.apagar,
        name='s1005_inclusao_infopcd_apagar'),

    url(r'^s1005-inclusao-infopcd/api/$',
        s1005_inclusao_infopcd_api_views.s1005inclusaoinfoPCDList.as_view() ),

    url(r'^s1005-inclusao-infopcd/api/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infopcd_api_views.s1005inclusaoinfoPCDDetail.as_view() ),

    url(r'^s1005-inclusao-infopcd/$',
        s1005_inclusao_infopcd_listar_views.listar,
        name='s1005_inclusao_infopcd'),

    url(r'^s1005-inclusao-infopcd/salvar/(?P<pk>[0-9]+)/$',
        s1005_inclusao_infopcd_salvar_views.salvar,
        name='s1005_inclusao_infopcd_salvar'),

    url(r'^s1005-inclusao-infopcd/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_inclusao_infopcd_salvar_views.salvar,
        name='s1005_inclusao_infopcd_salvar_tab'),

    url(r'^s1005-inclusao-infopcd/cadastrar/$',
        s1005_inclusao_infopcd_salvar_views.salvar,
        name='s1005_inclusao_infopcd_cadastrar'),

    url(r'^s1005-inclusao-infopcd/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_inclusao_infopcd_salvar_views.salvar,
        name='s1005_inclusao_infopcd_salvar_output'),

    url(r'^s1005-inclusao-infopcd/(?P<output>[\w-]+)/$',
        s1005_inclusao_infopcd_listar_views.listar,
        name='s1005_inclusao_infopcd_output'),

    url(r'^s1005-alteracao/apagar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_apagar_views.apagar,
        name='s1005_alteracao_apagar'),

    url(r'^s1005-alteracao/api/$',
        s1005_alteracao_api_views.s1005alteracaoList.as_view() ),

    url(r'^s1005-alteracao/api/(?P<pk>[0-9]+)/$',
        s1005_alteracao_api_views.s1005alteracaoDetail.as_view() ),

    url(r'^s1005-alteracao/$',
        s1005_alteracao_listar_views.listar,
        name='s1005_alteracao'),

    url(r'^s1005-alteracao/salvar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_salvar_views.salvar,
        name='s1005_alteracao_salvar'),

    url(r'^s1005-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_alteracao_salvar_views.salvar,
        name='s1005_alteracao_salvar_tab'),

    url(r'^s1005-alteracao/cadastrar/$',
        s1005_alteracao_salvar_views.salvar,
        name='s1005_alteracao_cadastrar'),

    url(r'^s1005-alteracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_alteracao_salvar_views.salvar,
        name='s1005_alteracao_salvar_output'),

    url(r'^s1005-alteracao/(?P<output>[\w-]+)/$',
        s1005_alteracao_listar_views.listar,
        name='s1005_alteracao_output'),

    url(r'^s1005-alteracao-procadmjudrat/apagar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_procadmjudrat_apagar_views.apagar,
        name='s1005_alteracao_procadmjudrat_apagar'),

    url(r'^s1005-alteracao-procadmjudrat/api/$',
        s1005_alteracao_procadmjudrat_api_views.s1005alteracaoprocAdmJudRatList.as_view() ),

    url(r'^s1005-alteracao-procadmjudrat/api/(?P<pk>[0-9]+)/$',
        s1005_alteracao_procadmjudrat_api_views.s1005alteracaoprocAdmJudRatDetail.as_view() ),

    url(r'^s1005-alteracao-procadmjudrat/$',
        s1005_alteracao_procadmjudrat_listar_views.listar,
        name='s1005_alteracao_procadmjudrat'),

    url(r'^s1005-alteracao-procadmjudrat/salvar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_procadmjudrat_salvar_views.salvar,
        name='s1005_alteracao_procadmjudrat_salvar'),

    url(r'^s1005-alteracao-procadmjudrat/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_alteracao_procadmjudrat_salvar_views.salvar,
        name='s1005_alteracao_procadmjudrat_salvar_tab'),

    url(r'^s1005-alteracao-procadmjudrat/cadastrar/$',
        s1005_alteracao_procadmjudrat_salvar_views.salvar,
        name='s1005_alteracao_procadmjudrat_cadastrar'),

    url(r'^s1005-alteracao-procadmjudrat/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_alteracao_procadmjudrat_salvar_views.salvar,
        name='s1005_alteracao_procadmjudrat_salvar_output'),

    url(r'^s1005-alteracao-procadmjudrat/(?P<output>[\w-]+)/$',
        s1005_alteracao_procadmjudrat_listar_views.listar,
        name='s1005_alteracao_procadmjudrat_output'),

    url(r'^s1005-alteracao-procadmjudfap/apagar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_procadmjudfap_apagar_views.apagar,
        name='s1005_alteracao_procadmjudfap_apagar'),

    url(r'^s1005-alteracao-procadmjudfap/api/$',
        s1005_alteracao_procadmjudfap_api_views.s1005alteracaoprocAdmJudFapList.as_view() ),

    url(r'^s1005-alteracao-procadmjudfap/api/(?P<pk>[0-9]+)/$',
        s1005_alteracao_procadmjudfap_api_views.s1005alteracaoprocAdmJudFapDetail.as_view() ),

    url(r'^s1005-alteracao-procadmjudfap/$',
        s1005_alteracao_procadmjudfap_listar_views.listar,
        name='s1005_alteracao_procadmjudfap'),

    url(r'^s1005-alteracao-procadmjudfap/salvar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_procadmjudfap_salvar_views.salvar,
        name='s1005_alteracao_procadmjudfap_salvar'),

    url(r'^s1005-alteracao-procadmjudfap/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_alteracao_procadmjudfap_salvar_views.salvar,
        name='s1005_alteracao_procadmjudfap_salvar_tab'),

    url(r'^s1005-alteracao-procadmjudfap/cadastrar/$',
        s1005_alteracao_procadmjudfap_salvar_views.salvar,
        name='s1005_alteracao_procadmjudfap_cadastrar'),

    url(r'^s1005-alteracao-procadmjudfap/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_alteracao_procadmjudfap_salvar_views.salvar,
        name='s1005_alteracao_procadmjudfap_salvar_output'),

    url(r'^s1005-alteracao-procadmjudfap/(?P<output>[\w-]+)/$',
        s1005_alteracao_procadmjudfap_listar_views.listar,
        name='s1005_alteracao_procadmjudfap_output'),

    url(r'^s1005-alteracao-infocaepf/apagar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infocaepf_apagar_views.apagar,
        name='s1005_alteracao_infocaepf_apagar'),

    url(r'^s1005-alteracao-infocaepf/api/$',
        s1005_alteracao_infocaepf_api_views.s1005alteracaoinfoCaepfList.as_view() ),

    url(r'^s1005-alteracao-infocaepf/api/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infocaepf_api_views.s1005alteracaoinfoCaepfDetail.as_view() ),

    url(r'^s1005-alteracao-infocaepf/$',
        s1005_alteracao_infocaepf_listar_views.listar,
        name='s1005_alteracao_infocaepf'),

    url(r'^s1005-alteracao-infocaepf/salvar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infocaepf_salvar_views.salvar,
        name='s1005_alteracao_infocaepf_salvar'),

    url(r'^s1005-alteracao-infocaepf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_alteracao_infocaepf_salvar_views.salvar,
        name='s1005_alteracao_infocaepf_salvar_tab'),

    url(r'^s1005-alteracao-infocaepf/cadastrar/$',
        s1005_alteracao_infocaepf_salvar_views.salvar,
        name='s1005_alteracao_infocaepf_cadastrar'),

    url(r'^s1005-alteracao-infocaepf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_alteracao_infocaepf_salvar_views.salvar,
        name='s1005_alteracao_infocaepf_salvar_output'),

    url(r'^s1005-alteracao-infocaepf/(?P<output>[\w-]+)/$',
        s1005_alteracao_infocaepf_listar_views.listar,
        name='s1005_alteracao_infocaepf_output'),

    url(r'^s1005-alteracao-infoobra/apagar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infoobra_apagar_views.apagar,
        name='s1005_alteracao_infoobra_apagar'),

    url(r'^s1005-alteracao-infoobra/api/$',
        s1005_alteracao_infoobra_api_views.s1005alteracaoinfoObraList.as_view() ),

    url(r'^s1005-alteracao-infoobra/api/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infoobra_api_views.s1005alteracaoinfoObraDetail.as_view() ),

    url(r'^s1005-alteracao-infoobra/$',
        s1005_alteracao_infoobra_listar_views.listar,
        name='s1005_alteracao_infoobra'),

    url(r'^s1005-alteracao-infoobra/salvar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infoobra_salvar_views.salvar,
        name='s1005_alteracao_infoobra_salvar'),

    url(r'^s1005-alteracao-infoobra/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_alteracao_infoobra_salvar_views.salvar,
        name='s1005_alteracao_infoobra_salvar_tab'),

    url(r'^s1005-alteracao-infoobra/cadastrar/$',
        s1005_alteracao_infoobra_salvar_views.salvar,
        name='s1005_alteracao_infoobra_cadastrar'),

    url(r'^s1005-alteracao-infoobra/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_alteracao_infoobra_salvar_views.salvar,
        name='s1005_alteracao_infoobra_salvar_output'),

    url(r'^s1005-alteracao-infoobra/(?P<output>[\w-]+)/$',
        s1005_alteracao_infoobra_listar_views.listar,
        name='s1005_alteracao_infoobra_output'),

    url(r'^s1005-alteracao-infoenteduc/apagar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infoenteduc_apagar_views.apagar,
        name='s1005_alteracao_infoenteduc_apagar'),

    url(r'^s1005-alteracao-infoenteduc/api/$',
        s1005_alteracao_infoenteduc_api_views.s1005alteracaoinfoEntEducList.as_view() ),

    url(r'^s1005-alteracao-infoenteduc/api/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infoenteduc_api_views.s1005alteracaoinfoEntEducDetail.as_view() ),

    url(r'^s1005-alteracao-infoenteduc/$',
        s1005_alteracao_infoenteduc_listar_views.listar,
        name='s1005_alteracao_infoenteduc'),

    url(r'^s1005-alteracao-infoenteduc/salvar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infoenteduc_salvar_views.salvar,
        name='s1005_alteracao_infoenteduc_salvar'),

    url(r'^s1005-alteracao-infoenteduc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_alteracao_infoenteduc_salvar_views.salvar,
        name='s1005_alteracao_infoenteduc_salvar_tab'),

    url(r'^s1005-alteracao-infoenteduc/cadastrar/$',
        s1005_alteracao_infoenteduc_salvar_views.salvar,
        name='s1005_alteracao_infoenteduc_cadastrar'),

    url(r'^s1005-alteracao-infoenteduc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_alteracao_infoenteduc_salvar_views.salvar,
        name='s1005_alteracao_infoenteduc_salvar_output'),

    url(r'^s1005-alteracao-infoenteduc/(?P<output>[\w-]+)/$',
        s1005_alteracao_infoenteduc_listar_views.listar,
        name='s1005_alteracao_infoenteduc_output'),

    url(r'^s1005-alteracao-infopcd/apagar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infopcd_apagar_views.apagar,
        name='s1005_alteracao_infopcd_apagar'),

    url(r'^s1005-alteracao-infopcd/api/$',
        s1005_alteracao_infopcd_api_views.s1005alteracaoinfoPCDList.as_view() ),

    url(r'^s1005-alteracao-infopcd/api/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infopcd_api_views.s1005alteracaoinfoPCDDetail.as_view() ),

    url(r'^s1005-alteracao-infopcd/$',
        s1005_alteracao_infopcd_listar_views.listar,
        name='s1005_alteracao_infopcd'),

    url(r'^s1005-alteracao-infopcd/salvar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_infopcd_salvar_views.salvar,
        name='s1005_alteracao_infopcd_salvar'),

    url(r'^s1005-alteracao-infopcd/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_alteracao_infopcd_salvar_views.salvar,
        name='s1005_alteracao_infopcd_salvar_tab'),

    url(r'^s1005-alteracao-infopcd/cadastrar/$',
        s1005_alteracao_infopcd_salvar_views.salvar,
        name='s1005_alteracao_infopcd_cadastrar'),

    url(r'^s1005-alteracao-infopcd/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_alteracao_infopcd_salvar_views.salvar,
        name='s1005_alteracao_infopcd_salvar_output'),

    url(r'^s1005-alteracao-infopcd/(?P<output>[\w-]+)/$',
        s1005_alteracao_infopcd_listar_views.listar,
        name='s1005_alteracao_infopcd_output'),

    url(r'^s1005-alteracao-novavalidade/apagar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_novavalidade_apagar_views.apagar,
        name='s1005_alteracao_novavalidade_apagar'),

    url(r'^s1005-alteracao-novavalidade/api/$',
        s1005_alteracao_novavalidade_api_views.s1005alteracaonovaValidadeList.as_view() ),

    url(r'^s1005-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
        s1005_alteracao_novavalidade_api_views.s1005alteracaonovaValidadeDetail.as_view() ),

    url(r'^s1005-alteracao-novavalidade/$',
        s1005_alteracao_novavalidade_listar_views.listar,
        name='s1005_alteracao_novavalidade'),

    url(r'^s1005-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/$',
        s1005_alteracao_novavalidade_salvar_views.salvar,
        name='s1005_alteracao_novavalidade_salvar'),

    url(r'^s1005-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_alteracao_novavalidade_salvar_views.salvar,
        name='s1005_alteracao_novavalidade_salvar_tab'),

    url(r'^s1005-alteracao-novavalidade/cadastrar/$',
        s1005_alteracao_novavalidade_salvar_views.salvar,
        name='s1005_alteracao_novavalidade_cadastrar'),

    url(r'^s1005-alteracao-novavalidade/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_alteracao_novavalidade_salvar_views.salvar,
        name='s1005_alteracao_novavalidade_salvar_output'),

    url(r'^s1005-alteracao-novavalidade/(?P<output>[\w-]+)/$',
        s1005_alteracao_novavalidade_listar_views.listar,
        name='s1005_alteracao_novavalidade_output'),

    url(r'^s1005-exclusao/apagar/(?P<pk>[0-9]+)/$',
        s1005_exclusao_apagar_views.apagar,
        name='s1005_exclusao_apagar'),

    url(r'^s1005-exclusao/api/$',
        s1005_exclusao_api_views.s1005exclusaoList.as_view() ),

    url(r'^s1005-exclusao/api/(?P<pk>[0-9]+)/$',
        s1005_exclusao_api_views.s1005exclusaoDetail.as_view() ),

    url(r'^s1005-exclusao/$',
        s1005_exclusao_listar_views.listar,
        name='s1005_exclusao'),

    url(r'^s1005-exclusao/salvar/(?P<pk>[0-9]+)/$',
        s1005_exclusao_salvar_views.salvar,
        name='s1005_exclusao_salvar'),

    url(r'^s1005-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1005_exclusao_salvar_views.salvar,
        name='s1005_exclusao_salvar_tab'),

    url(r'^s1005-exclusao/cadastrar/$',
        s1005_exclusao_salvar_views.salvar,
        name='s1005_exclusao_cadastrar'),

    url(r'^s1005-exclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1005_exclusao_salvar_views.salvar,
        name='s1005_exclusao_salvar_output'),

    url(r'^s1005-exclusao/(?P<output>[\w-]+)/$',
        s1005_exclusao_listar_views.listar,
        name='s1005_exclusao_output'),


]