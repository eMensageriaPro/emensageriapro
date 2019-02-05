#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1207.views import s1207_dmdev as s1207_dmdev_views
from emensageriapro.s1207.views import s1207_infoperant_ideadc as s1207_infoperant_ideadc_views
from emensageriapro.s1207.views import s1207_infoperant_ideestab as s1207_infoperant_ideestab_views
from emensageriapro.s1207.views import s1207_infoperant_ideperiodo as s1207_infoperant_ideperiodo_views
from emensageriapro.s1207.views import s1207_infoperant_itensremun as s1207_infoperant_itensremun_views
from emensageriapro.s1207.views import s1207_infoperapur_ideestab as s1207_infoperapur_ideestab_views
from emensageriapro.s1207.views import s1207_infoperapur_itensremun as s1207_infoperapur_itensremun_views
from emensageriapro.s1207.views import s1207_itens as s1207_itens_views
from emensageriapro.s1207.views import s1207_procjudtrab as s1207_procjudtrab_views



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



url(r'^s1207-dmdev/apagar/(?P<hash>.*)/$', 
        s1207_dmdev_views.apagar, 
        name='s1207_dmdev_apagar'),

url(r'^s1207-dmdev/api/$',
            s1207_dmdev_views.s1207dmDevList.as_view() ),

        url(r'^s1207-dmdev/api/(?P<pk>[0-9]+)/$',
            s1207_dmdev_views.s1207dmDevDetail.as_view() ),

url(r'^s1207-dmdev/listar/(?P<hash>.*)/$', 
        s1207_dmdev_views.listar, 
        name='s1207_dmdev'),

url(r'^s1207-dmdev/salvar/(?P<hash>.*)/$', 
        s1207_dmdev_views.salvar, 
        name='s1207_dmdev_salvar'),



url(r'^s1207-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_ideadc_views.apagar, 
        name='s1207_infoperant_ideadc_apagar'),

url(r'^s1207-infoperant-ideadc/api/$',
            s1207_infoperant_ideadc_views.s1207infoPerAntideADCList.as_view() ),

        url(r'^s1207-infoperant-ideadc/api/(?P<pk>[0-9]+)/$',
            s1207_infoperant_ideadc_views.s1207infoPerAntideADCDetail.as_view() ),

url(r'^s1207-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        s1207_infoperant_ideadc_views.listar, 
        name='s1207_infoperant_ideadc'),

url(r'^s1207-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_ideadc_views.salvar, 
        name='s1207_infoperant_ideadc_salvar'),



url(r'^s1207-infoperant-ideestab/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_ideestab_views.apagar, 
        name='s1207_infoperant_ideestab_apagar'),

url(r'^s1207-infoperant-ideestab/api/$',
            s1207_infoperant_ideestab_views.s1207infoPerAntideEstabList.as_view() ),

        url(r'^s1207-infoperant-ideestab/api/(?P<pk>[0-9]+)/$',
            s1207_infoperant_ideestab_views.s1207infoPerAntideEstabDetail.as_view() ),

url(r'^s1207-infoperant-ideestab/listar/(?P<hash>.*)/$', 
        s1207_infoperant_ideestab_views.listar, 
        name='s1207_infoperant_ideestab'),

url(r'^s1207-infoperant-ideestab/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_ideestab_views.salvar, 
        name='s1207_infoperant_ideestab_salvar'),



url(r'^s1207-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_ideperiodo_views.apagar, 
        name='s1207_infoperant_ideperiodo_apagar'),

url(r'^s1207-infoperant-ideperiodo/api/$',
            s1207_infoperant_ideperiodo_views.s1207infoPerAntidePeriodoList.as_view() ),

        url(r'^s1207-infoperant-ideperiodo/api/(?P<pk>[0-9]+)/$',
            s1207_infoperant_ideperiodo_views.s1207infoPerAntidePeriodoDetail.as_view() ),

url(r'^s1207-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        s1207_infoperant_ideperiodo_views.listar, 
        name='s1207_infoperant_ideperiodo'),

url(r'^s1207-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_ideperiodo_views.salvar, 
        name='s1207_infoperant_ideperiodo_salvar'),



url(r'^s1207-infoperant-itensremun/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_itensremun_views.apagar, 
        name='s1207_infoperant_itensremun_apagar'),

url(r'^s1207-infoperant-itensremun/api/$',
            s1207_infoperant_itensremun_views.s1207infoPerAntitensRemunList.as_view() ),

        url(r'^s1207-infoperant-itensremun/api/(?P<pk>[0-9]+)/$',
            s1207_infoperant_itensremun_views.s1207infoPerAntitensRemunDetail.as_view() ),

url(r'^s1207-infoperant-itensremun/listar/(?P<hash>.*)/$', 
        s1207_infoperant_itensremun_views.listar, 
        name='s1207_infoperant_itensremun'),

url(r'^s1207-infoperant-itensremun/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_itensremun_views.salvar, 
        name='s1207_infoperant_itensremun_salvar'),



url(r'^s1207-infoperapur-ideestab/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_ideestab_views.apagar, 
        name='s1207_infoperapur_ideestab_apagar'),

url(r'^s1207-infoperapur-ideestab/api/$',
            s1207_infoperapur_ideestab_views.s1207infoPerApurideEstabList.as_view() ),

        url(r'^s1207-infoperapur-ideestab/api/(?P<pk>[0-9]+)/$',
            s1207_infoperapur_ideestab_views.s1207infoPerApurideEstabDetail.as_view() ),

url(r'^s1207-infoperapur-ideestab/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_ideestab_views.listar, 
        name='s1207_infoperapur_ideestab'),

url(r'^s1207-infoperapur-ideestab/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_ideestab_views.salvar, 
        name='s1207_infoperapur_ideestab_salvar'),



url(r'^s1207-infoperapur-itensremun/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_itensremun_views.apagar, 
        name='s1207_infoperapur_itensremun_apagar'),

url(r'^s1207-infoperapur-itensremun/api/$',
            s1207_infoperapur_itensremun_views.s1207infoPerApuritensRemunList.as_view() ),

        url(r'^s1207-infoperapur-itensremun/api/(?P<pk>[0-9]+)/$',
            s1207_infoperapur_itensremun_views.s1207infoPerApuritensRemunDetail.as_view() ),

url(r'^s1207-infoperapur-itensremun/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_itensremun_views.listar, 
        name='s1207_infoperapur_itensremun'),

url(r'^s1207-infoperapur-itensremun/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_itensremun_views.salvar, 
        name='s1207_infoperapur_itensremun_salvar'),



url(r'^s1207-itens/apagar/(?P<hash>.*)/$', 
        s1207_itens_views.apagar, 
        name='s1207_itens_apagar'),

url(r'^s1207-itens/api/$',
            s1207_itens_views.s1207itensList.as_view() ),

        url(r'^s1207-itens/api/(?P<pk>[0-9]+)/$',
            s1207_itens_views.s1207itensDetail.as_view() ),

url(r'^s1207-itens/listar/(?P<hash>.*)/$', 
        s1207_itens_views.listar, 
        name='s1207_itens'),

url(r'^s1207-itens/salvar/(?P<hash>.*)/$', 
        s1207_itens_views.salvar, 
        name='s1207_itens_salvar'),



url(r'^s1207-procjudtrab/apagar/(?P<hash>.*)/$', 
        s1207_procjudtrab_views.apagar, 
        name='s1207_procjudtrab_apagar'),

url(r'^s1207-procjudtrab/api/$',
            s1207_procjudtrab_views.s1207procJudTrabList.as_view() ),

        url(r'^s1207-procjudtrab/api/(?P<pk>[0-9]+)/$',
            s1207_procjudtrab_views.s1207procJudTrabDetail.as_view() ),

url(r'^s1207-procjudtrab/listar/(?P<hash>.*)/$', 
        s1207_procjudtrab_views.listar, 
        name='s1207_procjudtrab'),

url(r'^s1207-procjudtrab/salvar/(?P<hash>.*)/$', 
        s1207_procjudtrab_views.salvar, 
        name='s1207_procjudtrab_salvar'),





]