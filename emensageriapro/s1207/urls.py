#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1207.views import s1207_procjudtrab_apagar as s1207_procjudtrab_apagar_views
from emensageriapro.s1207.views import s1207_procjudtrab_listar as s1207_procjudtrab_listar_views
from emensageriapro.s1207.views import s1207_procjudtrab_salvar as s1207_procjudtrab_salvar_views
from emensageriapro.s1207.views import s1207_procjudtrab_api as s1207_procjudtrab_api_views
from emensageriapro.s1207.views import s1207_dmdev_apagar as s1207_dmdev_apagar_views
from emensageriapro.s1207.views import s1207_dmdev_listar as s1207_dmdev_listar_views
from emensageriapro.s1207.views import s1207_dmdev_salvar as s1207_dmdev_salvar_views
from emensageriapro.s1207.views import s1207_dmdev_api as s1207_dmdev_api_views
from emensageriapro.s1207.views import s1207_itens_apagar as s1207_itens_apagar_views
from emensageriapro.s1207.views import s1207_itens_listar as s1207_itens_listar_views
from emensageriapro.s1207.views import s1207_itens_salvar as s1207_itens_salvar_views
from emensageriapro.s1207.views import s1207_itens_api as s1207_itens_api_views
from emensageriapro.s1207.views import s1207_infoperapur_apagar as s1207_infoperapur_apagar_views
from emensageriapro.s1207.views import s1207_infoperapur_listar as s1207_infoperapur_listar_views
from emensageriapro.s1207.views import s1207_infoperapur_salvar as s1207_infoperapur_salvar_views
from emensageriapro.s1207.views import s1207_infoperapur_api as s1207_infoperapur_api_views
from emensageriapro.s1207.views import s1207_infoperapur_ideestab_apagar as s1207_infoperapur_ideestab_apagar_views
from emensageriapro.s1207.views import s1207_infoperapur_ideestab_listar as s1207_infoperapur_ideestab_listar_views
from emensageriapro.s1207.views import s1207_infoperapur_ideestab_salvar as s1207_infoperapur_ideestab_salvar_views
from emensageriapro.s1207.views import s1207_infoperapur_ideestab_api as s1207_infoperapur_ideestab_api_views
from emensageriapro.s1207.views import s1207_infoperapur_remunperapur_apagar as s1207_infoperapur_remunperapur_apagar_views
from emensageriapro.s1207.views import s1207_infoperapur_remunperapur_listar as s1207_infoperapur_remunperapur_listar_views
from emensageriapro.s1207.views import s1207_infoperapur_remunperapur_salvar as s1207_infoperapur_remunperapur_salvar_views
from emensageriapro.s1207.views import s1207_infoperapur_remunperapur_api as s1207_infoperapur_remunperapur_api_views
from emensageriapro.s1207.views import s1207_infoperapur_itensremun_apagar as s1207_infoperapur_itensremun_apagar_views
from emensageriapro.s1207.views import s1207_infoperapur_itensremun_listar as s1207_infoperapur_itensremun_listar_views
from emensageriapro.s1207.views import s1207_infoperapur_itensremun_salvar as s1207_infoperapur_itensremun_salvar_views
from emensageriapro.s1207.views import s1207_infoperapur_itensremun_api as s1207_infoperapur_itensremun_api_views
from emensageriapro.s1207.views import s1207_infoperant_apagar as s1207_infoperant_apagar_views
from emensageriapro.s1207.views import s1207_infoperant_listar as s1207_infoperant_listar_views
from emensageriapro.s1207.views import s1207_infoperant_salvar as s1207_infoperant_salvar_views
from emensageriapro.s1207.views import s1207_infoperant_api as s1207_infoperant_api_views
from emensageriapro.s1207.views import s1207_infoperant_ideadc_apagar as s1207_infoperant_ideadc_apagar_views
from emensageriapro.s1207.views import s1207_infoperant_ideadc_listar as s1207_infoperant_ideadc_listar_views
from emensageriapro.s1207.views import s1207_infoperant_ideadc_salvar as s1207_infoperant_ideadc_salvar_views
from emensageriapro.s1207.views import s1207_infoperant_ideadc_api as s1207_infoperant_ideadc_api_views
from emensageriapro.s1207.views import s1207_infoperant_ideperiodo_apagar as s1207_infoperant_ideperiodo_apagar_views
from emensageriapro.s1207.views import s1207_infoperant_ideperiodo_listar as s1207_infoperant_ideperiodo_listar_views
from emensageriapro.s1207.views import s1207_infoperant_ideperiodo_salvar as s1207_infoperant_ideperiodo_salvar_views
from emensageriapro.s1207.views import s1207_infoperant_ideperiodo_api as s1207_infoperant_ideperiodo_api_views
from emensageriapro.s1207.views import s1207_infoperant_ideestab_apagar as s1207_infoperant_ideestab_apagar_views
from emensageriapro.s1207.views import s1207_infoperant_ideestab_listar as s1207_infoperant_ideestab_listar_views
from emensageriapro.s1207.views import s1207_infoperant_ideestab_salvar as s1207_infoperant_ideestab_salvar_views
from emensageriapro.s1207.views import s1207_infoperant_ideestab_api as s1207_infoperant_ideestab_api_views
from emensageriapro.s1207.views import s1207_infoperant_remunperant_apagar as s1207_infoperant_remunperant_apagar_views
from emensageriapro.s1207.views import s1207_infoperant_remunperant_listar as s1207_infoperant_remunperant_listar_views
from emensageriapro.s1207.views import s1207_infoperant_remunperant_salvar as s1207_infoperant_remunperant_salvar_views
from emensageriapro.s1207.views import s1207_infoperant_remunperant_api as s1207_infoperant_remunperant_api_views
from emensageriapro.s1207.views import s1207_infoperant_itensremun_apagar as s1207_infoperant_itensremun_apagar_views
from emensageriapro.s1207.views import s1207_infoperant_itensremun_listar as s1207_infoperant_itensremun_listar_views
from emensageriapro.s1207.views import s1207_infoperant_itensremun_salvar as s1207_infoperant_itensremun_salvar_views
from emensageriapro.s1207.views import s1207_infoperant_itensremun_api as s1207_infoperant_itensremun_api_views



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


    url(r'^s1207-procjudtrab/apagar/(?P<hash>.*)/$', 
        s1207_procjudtrab_apagar_views.apagar, 
        name='s1207_procjudtrab_apagar'),

    url(r'^s1207-procjudtrab/api/$',
        s1207_procjudtrab_api_views.s1207procJudTrabList.as_view() ),

    url(r'^s1207-procjudtrab/api/(?P<pk>[0-9]+)/$',
        s1207_procjudtrab_api_views.s1207procJudTrabDetail.as_view() ),

    url(r'^s1207-procjudtrab/listar/(?P<hash>.*)/$', 
        s1207_procjudtrab_listar_views.listar, 
        name='s1207_procjudtrab'),

    url(r'^s1207-procjudtrab/salvar/(?P<hash>.*)/$', 
        s1207_procjudtrab_salvar_views.salvar, 
        name='s1207_procjudtrab_salvar'),

    url(r'^s1207-dmdev/apagar/(?P<hash>.*)/$', 
        s1207_dmdev_apagar_views.apagar, 
        name='s1207_dmdev_apagar'),

    url(r'^s1207-dmdev/api/$',
        s1207_dmdev_api_views.s1207dmDevList.as_view() ),

    url(r'^s1207-dmdev/api/(?P<pk>[0-9]+)/$',
        s1207_dmdev_api_views.s1207dmDevDetail.as_view() ),

    url(r'^s1207-dmdev/listar/(?P<hash>.*)/$', 
        s1207_dmdev_listar_views.listar, 
        name='s1207_dmdev'),

    url(r'^s1207-dmdev/salvar/(?P<hash>.*)/$', 
        s1207_dmdev_salvar_views.salvar, 
        name='s1207_dmdev_salvar'),

    url(r'^s1207-itens/apagar/(?P<hash>.*)/$', 
        s1207_itens_apagar_views.apagar, 
        name='s1207_itens_apagar'),

    url(r'^s1207-itens/api/$',
        s1207_itens_api_views.s1207itensList.as_view() ),

    url(r'^s1207-itens/api/(?P<pk>[0-9]+)/$',
        s1207_itens_api_views.s1207itensDetail.as_view() ),

    url(r'^s1207-itens/listar/(?P<hash>.*)/$', 
        s1207_itens_listar_views.listar, 
        name='s1207_itens'),

    url(r'^s1207-itens/salvar/(?P<hash>.*)/$', 
        s1207_itens_salvar_views.salvar, 
        name='s1207_itens_salvar'),

    url(r'^s1207-infoperapur/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_apagar_views.apagar, 
        name='s1207_infoperapur_apagar'),

    url(r'^s1207-infoperapur/api/$',
        s1207_infoperapur_api_views.s1207infoPerApurList.as_view() ),

    url(r'^s1207-infoperapur/api/(?P<pk>[0-9]+)/$',
        s1207_infoperapur_api_views.s1207infoPerApurDetail.as_view() ),

    url(r'^s1207-infoperapur/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_listar_views.listar, 
        name='s1207_infoperapur'),

    url(r'^s1207-infoperapur/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_salvar_views.salvar, 
        name='s1207_infoperapur_salvar'),

    url(r'^s1207-infoperapur-ideestab/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_ideestab_apagar_views.apagar, 
        name='s1207_infoperapur_ideestab_apagar'),

    url(r'^s1207-infoperapur-ideestab/api/$',
        s1207_infoperapur_ideestab_api_views.s1207infoPerApurideEstabList.as_view() ),

    url(r'^s1207-infoperapur-ideestab/api/(?P<pk>[0-9]+)/$',
        s1207_infoperapur_ideestab_api_views.s1207infoPerApurideEstabDetail.as_view() ),

    url(r'^s1207-infoperapur-ideestab/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_ideestab_listar_views.listar, 
        name='s1207_infoperapur_ideestab'),

    url(r'^s1207-infoperapur-ideestab/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_ideestab_salvar_views.salvar, 
        name='s1207_infoperapur_ideestab_salvar'),

    url(r'^s1207-infoperapur-remunperapur/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_remunperapur_apagar_views.apagar, 
        name='s1207_infoperapur_remunperapur_apagar'),

    url(r'^s1207-infoperapur-remunperapur/api/$',
        s1207_infoperapur_remunperapur_api_views.s1207infoPerApurremunPerApurList.as_view() ),

    url(r'^s1207-infoperapur-remunperapur/api/(?P<pk>[0-9]+)/$',
        s1207_infoperapur_remunperapur_api_views.s1207infoPerApurremunPerApurDetail.as_view() ),

    url(r'^s1207-infoperapur-remunperapur/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_remunperapur_listar_views.listar, 
        name='s1207_infoperapur_remunperapur'),

    url(r'^s1207-infoperapur-remunperapur/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_remunperapur_salvar_views.salvar, 
        name='s1207_infoperapur_remunperapur_salvar'),

    url(r'^s1207-infoperapur-itensremun/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_itensremun_apagar_views.apagar, 
        name='s1207_infoperapur_itensremun_apagar'),

    url(r'^s1207-infoperapur-itensremun/api/$',
        s1207_infoperapur_itensremun_api_views.s1207infoPerApuritensRemunList.as_view() ),

    url(r'^s1207-infoperapur-itensremun/api/(?P<pk>[0-9]+)/$',
        s1207_infoperapur_itensremun_api_views.s1207infoPerApuritensRemunDetail.as_view() ),

    url(r'^s1207-infoperapur-itensremun/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_itensremun_listar_views.listar, 
        name='s1207_infoperapur_itensremun'),

    url(r'^s1207-infoperapur-itensremun/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_itensremun_salvar_views.salvar, 
        name='s1207_infoperapur_itensremun_salvar'),

    url(r'^s1207-infoperant/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_apagar_views.apagar, 
        name='s1207_infoperant_apagar'),

    url(r'^s1207-infoperant/api/$',
        s1207_infoperant_api_views.s1207infoPerAntList.as_view() ),

    url(r'^s1207-infoperant/api/(?P<pk>[0-9]+)/$',
        s1207_infoperant_api_views.s1207infoPerAntDetail.as_view() ),

    url(r'^s1207-infoperant/listar/(?P<hash>.*)/$', 
        s1207_infoperant_listar_views.listar, 
        name='s1207_infoperant'),

    url(r'^s1207-infoperant/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_salvar_views.salvar, 
        name='s1207_infoperant_salvar'),

    url(r'^s1207-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_ideadc_apagar_views.apagar, 
        name='s1207_infoperant_ideadc_apagar'),

    url(r'^s1207-infoperant-ideadc/api/$',
        s1207_infoperant_ideadc_api_views.s1207infoPerAntideADCList.as_view() ),

    url(r'^s1207-infoperant-ideadc/api/(?P<pk>[0-9]+)/$',
        s1207_infoperant_ideadc_api_views.s1207infoPerAntideADCDetail.as_view() ),

    url(r'^s1207-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        s1207_infoperant_ideadc_listar_views.listar, 
        name='s1207_infoperant_ideadc'),

    url(r'^s1207-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_ideadc_salvar_views.salvar, 
        name='s1207_infoperant_ideadc_salvar'),

    url(r'^s1207-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_ideperiodo_apagar_views.apagar, 
        name='s1207_infoperant_ideperiodo_apagar'),

    url(r'^s1207-infoperant-ideperiodo/api/$',
        s1207_infoperant_ideperiodo_api_views.s1207infoPerAntidePeriodoList.as_view() ),

    url(r'^s1207-infoperant-ideperiodo/api/(?P<pk>[0-9]+)/$',
        s1207_infoperant_ideperiodo_api_views.s1207infoPerAntidePeriodoDetail.as_view() ),

    url(r'^s1207-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        s1207_infoperant_ideperiodo_listar_views.listar, 
        name='s1207_infoperant_ideperiodo'),

    url(r'^s1207-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_ideperiodo_salvar_views.salvar, 
        name='s1207_infoperant_ideperiodo_salvar'),

    url(r'^s1207-infoperant-ideestab/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_ideestab_apagar_views.apagar, 
        name='s1207_infoperant_ideestab_apagar'),

    url(r'^s1207-infoperant-ideestab/api/$',
        s1207_infoperant_ideestab_api_views.s1207infoPerAntideEstabList.as_view() ),

    url(r'^s1207-infoperant-ideestab/api/(?P<pk>[0-9]+)/$',
        s1207_infoperant_ideestab_api_views.s1207infoPerAntideEstabDetail.as_view() ),

    url(r'^s1207-infoperant-ideestab/listar/(?P<hash>.*)/$', 
        s1207_infoperant_ideestab_listar_views.listar, 
        name='s1207_infoperant_ideestab'),

    url(r'^s1207-infoperant-ideestab/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_ideestab_salvar_views.salvar, 
        name='s1207_infoperant_ideestab_salvar'),

    url(r'^s1207-infoperant-remunperant/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_remunperant_apagar_views.apagar, 
        name='s1207_infoperant_remunperant_apagar'),

    url(r'^s1207-infoperant-remunperant/api/$',
        s1207_infoperant_remunperant_api_views.s1207infoPerAntremunPerAntList.as_view() ),

    url(r'^s1207-infoperant-remunperant/api/(?P<pk>[0-9]+)/$',
        s1207_infoperant_remunperant_api_views.s1207infoPerAntremunPerAntDetail.as_view() ),

    url(r'^s1207-infoperant-remunperant/listar/(?P<hash>.*)/$', 
        s1207_infoperant_remunperant_listar_views.listar, 
        name='s1207_infoperant_remunperant'),

    url(r'^s1207-infoperant-remunperant/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_remunperant_salvar_views.salvar, 
        name='s1207_infoperant_remunperant_salvar'),

    url(r'^s1207-infoperant-itensremun/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_itensremun_apagar_views.apagar, 
        name='s1207_infoperant_itensremun_apagar'),

    url(r'^s1207-infoperant-itensremun/api/$',
        s1207_infoperant_itensremun_api_views.s1207infoPerAntitensRemunList.as_view() ),

    url(r'^s1207-infoperant-itensremun/api/(?P<pk>[0-9]+)/$',
        s1207_infoperant_itensremun_api_views.s1207infoPerAntitensRemunDetail.as_view() ),

    url(r'^s1207-infoperant-itensremun/listar/(?P<hash>.*)/$', 
        s1207_infoperant_itensremun_listar_views.listar, 
        name='s1207_infoperant_itensremun'),

    url(r'^s1207-infoperant-itensremun/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_itensremun_salvar_views.salvar, 
        name='s1207_infoperant_itensremun_salvar'),


]