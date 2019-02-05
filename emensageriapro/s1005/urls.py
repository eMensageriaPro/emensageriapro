#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1005.views import s1005_alteracao as s1005_alteracao_views
from emensageriapro.s1005.views import s1005_alteracao_infocaepf as s1005_alteracao_infocaepf_views
from emensageriapro.s1005.views import s1005_alteracao_infoenteduc as s1005_alteracao_infoenteduc_views
from emensageriapro.s1005.views import s1005_alteracao_infoobra as s1005_alteracao_infoobra_views
from emensageriapro.s1005.views import s1005_alteracao_infopcd as s1005_alteracao_infopcd_views
from emensageriapro.s1005.views import s1005_alteracao_novavalidade as s1005_alteracao_novavalidade_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudfap as s1005_alteracao_procadmjudfap_views
from emensageriapro.s1005.views import s1005_alteracao_procadmjudrat as s1005_alteracao_procadmjudrat_views
from emensageriapro.s1005.views import s1005_exclusao as s1005_exclusao_views
from emensageriapro.s1005.views import s1005_inclusao as s1005_inclusao_views
from emensageriapro.s1005.views import s1005_inclusao_infocaepf as s1005_inclusao_infocaepf_views
from emensageriapro.s1005.views import s1005_inclusao_infoenteduc as s1005_inclusao_infoenteduc_views
from emensageriapro.s1005.views import s1005_inclusao_infoobra as s1005_inclusao_infoobra_views
from emensageriapro.s1005.views import s1005_inclusao_infopcd as s1005_inclusao_infopcd_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudfap as s1005_inclusao_procadmjudfap_views
from emensageriapro.s1005.views import s1005_inclusao_procadmjudrat as s1005_inclusao_procadmjudrat_views



"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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



url(r'^s1005-alteracao/apagar/(?P<hash>.*)/$', 
        s1005_alteracao_views.apagar, 
        name='s1005_alteracao_apagar'),

url(r'^s1005-alteracao/api/$',
            s1005_alteracao_views.s1005alteracaoList.as_view() ),

        url(r'^s1005-alteracao/api/(?P<pk>[0-9]+)/$',
            s1005_alteracao_views.s1005alteracaoDetail.as_view() ),

url(r'^s1005-alteracao/listar/(?P<hash>.*)/$', 
        s1005_alteracao_views.listar, 
        name='s1005_alteracao'),

url(r'^s1005-alteracao/salvar/(?P<hash>.*)/$', 
        s1005_alteracao_views.salvar, 
        name='s1005_alteracao_salvar'),



url(r'^s1005-alteracao-infocaepf/apagar/(?P<hash>.*)/$', 
        s1005_alteracao_infocaepf_views.apagar, 
        name='s1005_alteracao_infocaepf_apagar'),

url(r'^s1005-alteracao-infocaepf/api/$',
            s1005_alteracao_infocaepf_views.s1005alteracaoinfoCaepfList.as_view() ),

        url(r'^s1005-alteracao-infocaepf/api/(?P<pk>[0-9]+)/$',
            s1005_alteracao_infocaepf_views.s1005alteracaoinfoCaepfDetail.as_view() ),

url(r'^s1005-alteracao-infocaepf/listar/(?P<hash>.*)/$', 
        s1005_alteracao_infocaepf_views.listar, 
        name='s1005_alteracao_infocaepf'),

url(r'^s1005-alteracao-infocaepf/salvar/(?P<hash>.*)/$', 
        s1005_alteracao_infocaepf_views.salvar, 
        name='s1005_alteracao_infocaepf_salvar'),



url(r'^s1005-alteracao-infoenteduc/apagar/(?P<hash>.*)/$', 
        s1005_alteracao_infoenteduc_views.apagar, 
        name='s1005_alteracao_infoenteduc_apagar'),

url(r'^s1005-alteracao-infoenteduc/api/$',
            s1005_alteracao_infoenteduc_views.s1005alteracaoinfoEntEducList.as_view() ),

        url(r'^s1005-alteracao-infoenteduc/api/(?P<pk>[0-9]+)/$',
            s1005_alteracao_infoenteduc_views.s1005alteracaoinfoEntEducDetail.as_view() ),

url(r'^s1005-alteracao-infoenteduc/listar/(?P<hash>.*)/$', 
        s1005_alteracao_infoenteduc_views.listar, 
        name='s1005_alteracao_infoenteduc'),

url(r'^s1005-alteracao-infoenteduc/salvar/(?P<hash>.*)/$', 
        s1005_alteracao_infoenteduc_views.salvar, 
        name='s1005_alteracao_infoenteduc_salvar'),



url(r'^s1005-alteracao-infoobra/apagar/(?P<hash>.*)/$', 
        s1005_alteracao_infoobra_views.apagar, 
        name='s1005_alteracao_infoobra_apagar'),

url(r'^s1005-alteracao-infoobra/api/$',
            s1005_alteracao_infoobra_views.s1005alteracaoinfoObraList.as_view() ),

        url(r'^s1005-alteracao-infoobra/api/(?P<pk>[0-9]+)/$',
            s1005_alteracao_infoobra_views.s1005alteracaoinfoObraDetail.as_view() ),

url(r'^s1005-alteracao-infoobra/listar/(?P<hash>.*)/$', 
        s1005_alteracao_infoobra_views.listar, 
        name='s1005_alteracao_infoobra'),

url(r'^s1005-alteracao-infoobra/salvar/(?P<hash>.*)/$', 
        s1005_alteracao_infoobra_views.salvar, 
        name='s1005_alteracao_infoobra_salvar'),



url(r'^s1005-alteracao-infopcd/apagar/(?P<hash>.*)/$', 
        s1005_alteracao_infopcd_views.apagar, 
        name='s1005_alteracao_infopcd_apagar'),

url(r'^s1005-alteracao-infopcd/api/$',
            s1005_alteracao_infopcd_views.s1005alteracaoinfoPCDList.as_view() ),

        url(r'^s1005-alteracao-infopcd/api/(?P<pk>[0-9]+)/$',
            s1005_alteracao_infopcd_views.s1005alteracaoinfoPCDDetail.as_view() ),

url(r'^s1005-alteracao-infopcd/listar/(?P<hash>.*)/$', 
        s1005_alteracao_infopcd_views.listar, 
        name='s1005_alteracao_infopcd'),

url(r'^s1005-alteracao-infopcd/salvar/(?P<hash>.*)/$', 
        s1005_alteracao_infopcd_views.salvar, 
        name='s1005_alteracao_infopcd_salvar'),



url(r'^s1005-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1005_alteracao_novavalidade_views.apagar, 
        name='s1005_alteracao_novavalidade_apagar'),

url(r'^s1005-alteracao-novavalidade/api/$',
            s1005_alteracao_novavalidade_views.s1005alteracaonovaValidadeList.as_view() ),

        url(r'^s1005-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1005_alteracao_novavalidade_views.s1005alteracaonovaValidadeDetail.as_view() ),

url(r'^s1005-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1005_alteracao_novavalidade_views.listar, 
        name='s1005_alteracao_novavalidade'),

url(r'^s1005-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1005_alteracao_novavalidade_views.salvar, 
        name='s1005_alteracao_novavalidade_salvar'),



url(r'^s1005-alteracao-procadmjudfap/apagar/(?P<hash>.*)/$', 
        s1005_alteracao_procadmjudfap_views.apagar, 
        name='s1005_alteracao_procadmjudfap_apagar'),

url(r'^s1005-alteracao-procadmjudfap/api/$',
            s1005_alteracao_procadmjudfap_views.s1005alteracaoprocAdmJudFapList.as_view() ),

        url(r'^s1005-alteracao-procadmjudfap/api/(?P<pk>[0-9]+)/$',
            s1005_alteracao_procadmjudfap_views.s1005alteracaoprocAdmJudFapDetail.as_view() ),

url(r'^s1005-alteracao-procadmjudfap/listar/(?P<hash>.*)/$', 
        s1005_alteracao_procadmjudfap_views.listar, 
        name='s1005_alteracao_procadmjudfap'),

url(r'^s1005-alteracao-procadmjudfap/salvar/(?P<hash>.*)/$', 
        s1005_alteracao_procadmjudfap_views.salvar, 
        name='s1005_alteracao_procadmjudfap_salvar'),



url(r'^s1005-alteracao-procadmjudrat/apagar/(?P<hash>.*)/$', 
        s1005_alteracao_procadmjudrat_views.apagar, 
        name='s1005_alteracao_procadmjudrat_apagar'),

url(r'^s1005-alteracao-procadmjudrat/api/$',
            s1005_alteracao_procadmjudrat_views.s1005alteracaoprocAdmJudRatList.as_view() ),

        url(r'^s1005-alteracao-procadmjudrat/api/(?P<pk>[0-9]+)/$',
            s1005_alteracao_procadmjudrat_views.s1005alteracaoprocAdmJudRatDetail.as_view() ),

url(r'^s1005-alteracao-procadmjudrat/listar/(?P<hash>.*)/$', 
        s1005_alteracao_procadmjudrat_views.listar, 
        name='s1005_alteracao_procadmjudrat'),

url(r'^s1005-alteracao-procadmjudrat/salvar/(?P<hash>.*)/$', 
        s1005_alteracao_procadmjudrat_views.salvar, 
        name='s1005_alteracao_procadmjudrat_salvar'),



url(r'^s1005-exclusao/apagar/(?P<hash>.*)/$', 
        s1005_exclusao_views.apagar, 
        name='s1005_exclusao_apagar'),

url(r'^s1005-exclusao/api/$',
            s1005_exclusao_views.s1005exclusaoList.as_view() ),

        url(r'^s1005-exclusao/api/(?P<pk>[0-9]+)/$',
            s1005_exclusao_views.s1005exclusaoDetail.as_view() ),

url(r'^s1005-exclusao/listar/(?P<hash>.*)/$', 
        s1005_exclusao_views.listar, 
        name='s1005_exclusao'),

url(r'^s1005-exclusao/salvar/(?P<hash>.*)/$', 
        s1005_exclusao_views.salvar, 
        name='s1005_exclusao_salvar'),



url(r'^s1005-inclusao/apagar/(?P<hash>.*)/$', 
        s1005_inclusao_views.apagar, 
        name='s1005_inclusao_apagar'),

url(r'^s1005-inclusao/api/$',
            s1005_inclusao_views.s1005inclusaoList.as_view() ),

        url(r'^s1005-inclusao/api/(?P<pk>[0-9]+)/$',
            s1005_inclusao_views.s1005inclusaoDetail.as_view() ),

url(r'^s1005-inclusao/listar/(?P<hash>.*)/$', 
        s1005_inclusao_views.listar, 
        name='s1005_inclusao'),

url(r'^s1005-inclusao/salvar/(?P<hash>.*)/$', 
        s1005_inclusao_views.salvar, 
        name='s1005_inclusao_salvar'),



url(r'^s1005-inclusao-infocaepf/apagar/(?P<hash>.*)/$', 
        s1005_inclusao_infocaepf_views.apagar, 
        name='s1005_inclusao_infocaepf_apagar'),

url(r'^s1005-inclusao-infocaepf/api/$',
            s1005_inclusao_infocaepf_views.s1005inclusaoinfoCaepfList.as_view() ),

        url(r'^s1005-inclusao-infocaepf/api/(?P<pk>[0-9]+)/$',
            s1005_inclusao_infocaepf_views.s1005inclusaoinfoCaepfDetail.as_view() ),

url(r'^s1005-inclusao-infocaepf/listar/(?P<hash>.*)/$', 
        s1005_inclusao_infocaepf_views.listar, 
        name='s1005_inclusao_infocaepf'),

url(r'^s1005-inclusao-infocaepf/salvar/(?P<hash>.*)/$', 
        s1005_inclusao_infocaepf_views.salvar, 
        name='s1005_inclusao_infocaepf_salvar'),



url(r'^s1005-inclusao-infoenteduc/apagar/(?P<hash>.*)/$', 
        s1005_inclusao_infoenteduc_views.apagar, 
        name='s1005_inclusao_infoenteduc_apagar'),

url(r'^s1005-inclusao-infoenteduc/api/$',
            s1005_inclusao_infoenteduc_views.s1005inclusaoinfoEntEducList.as_view() ),

        url(r'^s1005-inclusao-infoenteduc/api/(?P<pk>[0-9]+)/$',
            s1005_inclusao_infoenteduc_views.s1005inclusaoinfoEntEducDetail.as_view() ),

url(r'^s1005-inclusao-infoenteduc/listar/(?P<hash>.*)/$', 
        s1005_inclusao_infoenteduc_views.listar, 
        name='s1005_inclusao_infoenteduc'),

url(r'^s1005-inclusao-infoenteduc/salvar/(?P<hash>.*)/$', 
        s1005_inclusao_infoenteduc_views.salvar, 
        name='s1005_inclusao_infoenteduc_salvar'),



url(r'^s1005-inclusao-infoobra/apagar/(?P<hash>.*)/$', 
        s1005_inclusao_infoobra_views.apagar, 
        name='s1005_inclusao_infoobra_apagar'),

url(r'^s1005-inclusao-infoobra/api/$',
            s1005_inclusao_infoobra_views.s1005inclusaoinfoObraList.as_view() ),

        url(r'^s1005-inclusao-infoobra/api/(?P<pk>[0-9]+)/$',
            s1005_inclusao_infoobra_views.s1005inclusaoinfoObraDetail.as_view() ),

url(r'^s1005-inclusao-infoobra/listar/(?P<hash>.*)/$', 
        s1005_inclusao_infoobra_views.listar, 
        name='s1005_inclusao_infoobra'),

url(r'^s1005-inclusao-infoobra/salvar/(?P<hash>.*)/$', 
        s1005_inclusao_infoobra_views.salvar, 
        name='s1005_inclusao_infoobra_salvar'),



url(r'^s1005-inclusao-infopcd/apagar/(?P<hash>.*)/$', 
        s1005_inclusao_infopcd_views.apagar, 
        name='s1005_inclusao_infopcd_apagar'),

url(r'^s1005-inclusao-infopcd/api/$',
            s1005_inclusao_infopcd_views.s1005inclusaoinfoPCDList.as_view() ),

        url(r'^s1005-inclusao-infopcd/api/(?P<pk>[0-9]+)/$',
            s1005_inclusao_infopcd_views.s1005inclusaoinfoPCDDetail.as_view() ),

url(r'^s1005-inclusao-infopcd/listar/(?P<hash>.*)/$', 
        s1005_inclusao_infopcd_views.listar, 
        name='s1005_inclusao_infopcd'),

url(r'^s1005-inclusao-infopcd/salvar/(?P<hash>.*)/$', 
        s1005_inclusao_infopcd_views.salvar, 
        name='s1005_inclusao_infopcd_salvar'),



url(r'^s1005-inclusao-procadmjudfap/apagar/(?P<hash>.*)/$', 
        s1005_inclusao_procadmjudfap_views.apagar, 
        name='s1005_inclusao_procadmjudfap_apagar'),

url(r'^s1005-inclusao-procadmjudfap/api/$',
            s1005_inclusao_procadmjudfap_views.s1005inclusaoprocAdmJudFapList.as_view() ),

        url(r'^s1005-inclusao-procadmjudfap/api/(?P<pk>[0-9]+)/$',
            s1005_inclusao_procadmjudfap_views.s1005inclusaoprocAdmJudFapDetail.as_view() ),

url(r'^s1005-inclusao-procadmjudfap/listar/(?P<hash>.*)/$', 
        s1005_inclusao_procadmjudfap_views.listar, 
        name='s1005_inclusao_procadmjudfap'),

url(r'^s1005-inclusao-procadmjudfap/salvar/(?P<hash>.*)/$', 
        s1005_inclusao_procadmjudfap_views.salvar, 
        name='s1005_inclusao_procadmjudfap_salvar'),



url(r'^s1005-inclusao-procadmjudrat/apagar/(?P<hash>.*)/$', 
        s1005_inclusao_procadmjudrat_views.apagar, 
        name='s1005_inclusao_procadmjudrat_apagar'),

url(r'^s1005-inclusao-procadmjudrat/api/$',
            s1005_inclusao_procadmjudrat_views.s1005inclusaoprocAdmJudRatList.as_view() ),

        url(r'^s1005-inclusao-procadmjudrat/api/(?P<pk>[0-9]+)/$',
            s1005_inclusao_procadmjudrat_views.s1005inclusaoprocAdmJudRatDetail.as_view() ),

url(r'^s1005-inclusao-procadmjudrat/listar/(?P<hash>.*)/$', 
        s1005_inclusao_procadmjudrat_views.listar, 
        name='s1005_inclusao_procadmjudrat'),

url(r'^s1005-inclusao-procadmjudrat/salvar/(?P<hash>.*)/$', 
        s1005_inclusao_procadmjudrat_views.salvar, 
        name='s1005_inclusao_procadmjudrat_salvar'),





]