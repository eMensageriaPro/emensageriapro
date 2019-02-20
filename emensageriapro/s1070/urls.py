#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1070.views import s1070_alteracao as s1070_alteracao_views
from emensageriapro.s1070.views import s1070_alteracao_dadosprocjud as s1070_alteracao_dadosprocjud_views
from emensageriapro.s1070.views import s1070_alteracao_infosusp as s1070_alteracao_infosusp_views
from emensageriapro.s1070.views import s1070_alteracao_novavalidade as s1070_alteracao_novavalidade_views
from emensageriapro.s1070.views import s1070_exclusao as s1070_exclusao_views
from emensageriapro.s1070.views import s1070_inclusao as s1070_inclusao_views
from emensageriapro.s1070.views import s1070_inclusao_dadosprocjud as s1070_inclusao_dadosprocjud_views
from emensageriapro.s1070.views import s1070_inclusao_infosusp as s1070_inclusao_infosusp_views



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



url(r'^s1070-alteracao/apagar/(?P<hash>.*)/$', 
        s1070_alteracao_views.apagar, 
        name='s1070_alteracao_apagar'),

url(r'^s1070-alteracao/api/$',
            s1070_alteracao_views.s1070alteracaoList.as_view() ),

        url(r'^s1070-alteracao/api/(?P<pk>[0-9]+)/$',
            s1070_alteracao_views.s1070alteracaoDetail.as_view() ),

url(r'^s1070-alteracao/listar/(?P<hash>.*)/$', 
        s1070_alteracao_views.listar, 
        name='s1070_alteracao'),

url(r'^s1070-alteracao/salvar/(?P<hash>.*)/$', 
        s1070_alteracao_views.salvar, 
        name='s1070_alteracao_salvar'),



url(r'^s1070-alteracao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        s1070_alteracao_dadosprocjud_views.apagar, 
        name='s1070_alteracao_dadosprocjud_apagar'),

url(r'^s1070-alteracao-dadosprocjud/api/$',
            s1070_alteracao_dadosprocjud_views.s1070alteracaodadosProcJudList.as_view() ),

        url(r'^s1070-alteracao-dadosprocjud/api/(?P<pk>[0-9]+)/$',
            s1070_alteracao_dadosprocjud_views.s1070alteracaodadosProcJudDetail.as_view() ),

url(r'^s1070-alteracao-dadosprocjud/listar/(?P<hash>.*)/$', 
        s1070_alteracao_dadosprocjud_views.listar, 
        name='s1070_alteracao_dadosprocjud'),

url(r'^s1070-alteracao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        s1070_alteracao_dadosprocjud_views.salvar, 
        name='s1070_alteracao_dadosprocjud_salvar'),



url(r'^s1070-alteracao-infosusp/apagar/(?P<hash>.*)/$', 
        s1070_alteracao_infosusp_views.apagar, 
        name='s1070_alteracao_infosusp_apagar'),

url(r'^s1070-alteracao-infosusp/api/$',
            s1070_alteracao_infosusp_views.s1070alteracaoinfoSuspList.as_view() ),

        url(r'^s1070-alteracao-infosusp/api/(?P<pk>[0-9]+)/$',
            s1070_alteracao_infosusp_views.s1070alteracaoinfoSuspDetail.as_view() ),

url(r'^s1070-alteracao-infosusp/listar/(?P<hash>.*)/$', 
        s1070_alteracao_infosusp_views.listar, 
        name='s1070_alteracao_infosusp'),

url(r'^s1070-alteracao-infosusp/salvar/(?P<hash>.*)/$', 
        s1070_alteracao_infosusp_views.salvar, 
        name='s1070_alteracao_infosusp_salvar'),



url(r'^s1070-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1070_alteracao_novavalidade_views.apagar, 
        name='s1070_alteracao_novavalidade_apagar'),

url(r'^s1070-alteracao-novavalidade/api/$',
            s1070_alteracao_novavalidade_views.s1070alteracaonovaValidadeList.as_view() ),

        url(r'^s1070-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1070_alteracao_novavalidade_views.s1070alteracaonovaValidadeDetail.as_view() ),

url(r'^s1070-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1070_alteracao_novavalidade_views.listar, 
        name='s1070_alteracao_novavalidade'),

url(r'^s1070-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1070_alteracao_novavalidade_views.salvar, 
        name='s1070_alteracao_novavalidade_salvar'),



url(r'^s1070-exclusao/apagar/(?P<hash>.*)/$', 
        s1070_exclusao_views.apagar, 
        name='s1070_exclusao_apagar'),

url(r'^s1070-exclusao/api/$',
            s1070_exclusao_views.s1070exclusaoList.as_view() ),

        url(r'^s1070-exclusao/api/(?P<pk>[0-9]+)/$',
            s1070_exclusao_views.s1070exclusaoDetail.as_view() ),

url(r'^s1070-exclusao/listar/(?P<hash>.*)/$', 
        s1070_exclusao_views.listar, 
        name='s1070_exclusao'),

url(r'^s1070-exclusao/salvar/(?P<hash>.*)/$', 
        s1070_exclusao_views.salvar, 
        name='s1070_exclusao_salvar'),



url(r'^s1070-inclusao/apagar/(?P<hash>.*)/$', 
        s1070_inclusao_views.apagar, 
        name='s1070_inclusao_apagar'),

url(r'^s1070-inclusao/api/$',
            s1070_inclusao_views.s1070inclusaoList.as_view() ),

        url(r'^s1070-inclusao/api/(?P<pk>[0-9]+)/$',
            s1070_inclusao_views.s1070inclusaoDetail.as_view() ),

url(r'^s1070-inclusao/listar/(?P<hash>.*)/$', 
        s1070_inclusao_views.listar, 
        name='s1070_inclusao'),

url(r'^s1070-inclusao/salvar/(?P<hash>.*)/$', 
        s1070_inclusao_views.salvar, 
        name='s1070_inclusao_salvar'),



url(r'^s1070-inclusao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        s1070_inclusao_dadosprocjud_views.apagar, 
        name='s1070_inclusao_dadosprocjud_apagar'),

url(r'^s1070-inclusao-dadosprocjud/api/$',
            s1070_inclusao_dadosprocjud_views.s1070inclusaodadosProcJudList.as_view() ),

        url(r'^s1070-inclusao-dadosprocjud/api/(?P<pk>[0-9]+)/$',
            s1070_inclusao_dadosprocjud_views.s1070inclusaodadosProcJudDetail.as_view() ),

url(r'^s1070-inclusao-dadosprocjud/listar/(?P<hash>.*)/$', 
        s1070_inclusao_dadosprocjud_views.listar, 
        name='s1070_inclusao_dadosprocjud'),

url(r'^s1070-inclusao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        s1070_inclusao_dadosprocjud_views.salvar, 
        name='s1070_inclusao_dadosprocjud_salvar'),



url(r'^s1070-inclusao-infosusp/apagar/(?P<hash>.*)/$', 
        s1070_inclusao_infosusp_views.apagar, 
        name='s1070_inclusao_infosusp_apagar'),

url(r'^s1070-inclusao-infosusp/api/$',
            s1070_inclusao_infosusp_views.s1070inclusaoinfoSuspList.as_view() ),

        url(r'^s1070-inclusao-infosusp/api/(?P<pk>[0-9]+)/$',
            s1070_inclusao_infosusp_views.s1070inclusaoinfoSuspDetail.as_view() ),

url(r'^s1070-inclusao-infosusp/listar/(?P<hash>.*)/$', 
        s1070_inclusao_infosusp_views.listar, 
        name='s1070_inclusao_infosusp'),

url(r'^s1070-inclusao-infosusp/salvar/(?P<hash>.*)/$', 
        s1070_inclusao_infosusp_views.salvar, 
        name='s1070_inclusao_infosusp_salvar'),





]