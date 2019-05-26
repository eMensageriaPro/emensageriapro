#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s5013.views import s5013_infobasefgts_apagar as s5013_infobasefgts_apagar_views
from emensageriapro.s5013.views import s5013_infobasefgts_listar as s5013_infobasefgts_listar_views
from emensageriapro.s5013.views import s5013_infobasefgts_salvar as s5013_infobasefgts_salvar_views
from emensageriapro.s5013.views import s5013_infobasefgts_api as s5013_infobasefgts_api_views
from emensageriapro.s5013.views import s5013_baseperapur_apagar as s5013_baseperapur_apagar_views
from emensageriapro.s5013.views import s5013_baseperapur_listar as s5013_baseperapur_listar_views
from emensageriapro.s5013.views import s5013_baseperapur_salvar as s5013_baseperapur_salvar_views
from emensageriapro.s5013.views import s5013_baseperapur_api as s5013_baseperapur_api_views
from emensageriapro.s5013.views import s5013_infobaseperante_apagar as s5013_infobaseperante_apagar_views
from emensageriapro.s5013.views import s5013_infobaseperante_listar as s5013_infobaseperante_listar_views
from emensageriapro.s5013.views import s5013_infobaseperante_salvar as s5013_infobaseperante_salvar_views
from emensageriapro.s5013.views import s5013_infobaseperante_api as s5013_infobaseperante_api_views
from emensageriapro.s5013.views import s5013_baseperante_apagar as s5013_baseperante_apagar_views
from emensageriapro.s5013.views import s5013_baseperante_listar as s5013_baseperante_listar_views
from emensageriapro.s5013.views import s5013_baseperante_salvar as s5013_baseperante_salvar_views
from emensageriapro.s5013.views import s5013_baseperante_api as s5013_baseperante_api_views
from emensageriapro.s5013.views import s5013_infodpsfgts_apagar as s5013_infodpsfgts_apagar_views
from emensageriapro.s5013.views import s5013_infodpsfgts_listar as s5013_infodpsfgts_listar_views
from emensageriapro.s5013.views import s5013_infodpsfgts_salvar as s5013_infodpsfgts_salvar_views
from emensageriapro.s5013.views import s5013_infodpsfgts_api as s5013_infodpsfgts_api_views
from emensageriapro.s5013.views import s5013_dpsperapur_apagar as s5013_dpsperapur_apagar_views
from emensageriapro.s5013.views import s5013_dpsperapur_listar as s5013_dpsperapur_listar_views
from emensageriapro.s5013.views import s5013_dpsperapur_salvar as s5013_dpsperapur_salvar_views
from emensageriapro.s5013.views import s5013_dpsperapur_api as s5013_dpsperapur_api_views
from emensageriapro.s5013.views import s5013_infodpsperante_apagar as s5013_infodpsperante_apagar_views
from emensageriapro.s5013.views import s5013_infodpsperante_listar as s5013_infodpsperante_listar_views
from emensageriapro.s5013.views import s5013_infodpsperante_salvar as s5013_infodpsperante_salvar_views
from emensageriapro.s5013.views import s5013_infodpsperante_api as s5013_infodpsperante_api_views
from emensageriapro.s5013.views import s5013_dpsperante_apagar as s5013_dpsperante_apagar_views
from emensageriapro.s5013.views import s5013_dpsperante_listar as s5013_dpsperante_listar_views
from emensageriapro.s5013.views import s5013_dpsperante_salvar as s5013_dpsperante_salvar_views
from emensageriapro.s5013.views import s5013_dpsperante_api as s5013_dpsperante_api_views



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


    url(r'^s5013-infobasefgts/apagar/(?P<hash>.*)/$', 
        s5013_infobasefgts_apagar_views.apagar, 
        name='s5013_infobasefgts_apagar'),

    url(r'^s5013-infobasefgts/api/$',
        s5013_infobasefgts_api_views.s5013infoBaseFGTSList.as_view() ),

    url(r'^s5013-infobasefgts/api/(?P<pk>[0-9]+)/$',
        s5013_infobasefgts_api_views.s5013infoBaseFGTSDetail.as_view() ),

    url(r'^s5013-infobasefgts/listar/(?P<hash>.*)/$', 
        s5013_infobasefgts_listar_views.listar, 
        name='s5013_infobasefgts'),

    url(r'^s5013-infobasefgts/salvar/(?P<hash>.*)/$', 
        s5013_infobasefgts_salvar_views.salvar, 
        name='s5013_infobasefgts_salvar'),

    url(r'^s5013-baseperapur/apagar/(?P<hash>.*)/$', 
        s5013_baseperapur_apagar_views.apagar, 
        name='s5013_baseperapur_apagar'),

    url(r'^s5013-baseperapur/api/$',
        s5013_baseperapur_api_views.s5013basePerApurList.as_view() ),

    url(r'^s5013-baseperapur/api/(?P<pk>[0-9]+)/$',
        s5013_baseperapur_api_views.s5013basePerApurDetail.as_view() ),

    url(r'^s5013-baseperapur/listar/(?P<hash>.*)/$', 
        s5013_baseperapur_listar_views.listar, 
        name='s5013_baseperapur'),

    url(r'^s5013-baseperapur/salvar/(?P<hash>.*)/$', 
        s5013_baseperapur_salvar_views.salvar, 
        name='s5013_baseperapur_salvar'),

    url(r'^s5013-infobaseperante/apagar/(?P<hash>.*)/$', 
        s5013_infobaseperante_apagar_views.apagar, 
        name='s5013_infobaseperante_apagar'),

    url(r'^s5013-infobaseperante/api/$',
        s5013_infobaseperante_api_views.s5013infoBasePerAntEList.as_view() ),

    url(r'^s5013-infobaseperante/api/(?P<pk>[0-9]+)/$',
        s5013_infobaseperante_api_views.s5013infoBasePerAntEDetail.as_view() ),

    url(r'^s5013-infobaseperante/listar/(?P<hash>.*)/$', 
        s5013_infobaseperante_listar_views.listar, 
        name='s5013_infobaseperante'),

    url(r'^s5013-infobaseperante/salvar/(?P<hash>.*)/$', 
        s5013_infobaseperante_salvar_views.salvar, 
        name='s5013_infobaseperante_salvar'),

    url(r'^s5013-baseperante/apagar/(?P<hash>.*)/$', 
        s5013_baseperante_apagar_views.apagar, 
        name='s5013_baseperante_apagar'),

    url(r'^s5013-baseperante/api/$',
        s5013_baseperante_api_views.s5013basePerAntEList.as_view() ),

    url(r'^s5013-baseperante/api/(?P<pk>[0-9]+)/$',
        s5013_baseperante_api_views.s5013basePerAntEDetail.as_view() ),

    url(r'^s5013-baseperante/listar/(?P<hash>.*)/$', 
        s5013_baseperante_listar_views.listar, 
        name='s5013_baseperante'),

    url(r'^s5013-baseperante/salvar/(?P<hash>.*)/$', 
        s5013_baseperante_salvar_views.salvar, 
        name='s5013_baseperante_salvar'),

    url(r'^s5013-infodpsfgts/apagar/(?P<hash>.*)/$', 
        s5013_infodpsfgts_apagar_views.apagar, 
        name='s5013_infodpsfgts_apagar'),

    url(r'^s5013-infodpsfgts/api/$',
        s5013_infodpsfgts_api_views.s5013infoDpsFGTSList.as_view() ),

    url(r'^s5013-infodpsfgts/api/(?P<pk>[0-9]+)/$',
        s5013_infodpsfgts_api_views.s5013infoDpsFGTSDetail.as_view() ),

    url(r'^s5013-infodpsfgts/listar/(?P<hash>.*)/$', 
        s5013_infodpsfgts_listar_views.listar, 
        name='s5013_infodpsfgts'),

    url(r'^s5013-infodpsfgts/salvar/(?P<hash>.*)/$', 
        s5013_infodpsfgts_salvar_views.salvar, 
        name='s5013_infodpsfgts_salvar'),

    url(r'^s5013-dpsperapur/apagar/(?P<hash>.*)/$', 
        s5013_dpsperapur_apagar_views.apagar, 
        name='s5013_dpsperapur_apagar'),

    url(r'^s5013-dpsperapur/api/$',
        s5013_dpsperapur_api_views.s5013dpsPerApurList.as_view() ),

    url(r'^s5013-dpsperapur/api/(?P<pk>[0-9]+)/$',
        s5013_dpsperapur_api_views.s5013dpsPerApurDetail.as_view() ),

    url(r'^s5013-dpsperapur/listar/(?P<hash>.*)/$', 
        s5013_dpsperapur_listar_views.listar, 
        name='s5013_dpsperapur'),

    url(r'^s5013-dpsperapur/salvar/(?P<hash>.*)/$', 
        s5013_dpsperapur_salvar_views.salvar, 
        name='s5013_dpsperapur_salvar'),

    url(r'^s5013-infodpsperante/apagar/(?P<hash>.*)/$', 
        s5013_infodpsperante_apagar_views.apagar, 
        name='s5013_infodpsperante_apagar'),

    url(r'^s5013-infodpsperante/api/$',
        s5013_infodpsperante_api_views.s5013infoDpsPerAntEList.as_view() ),

    url(r'^s5013-infodpsperante/api/(?P<pk>[0-9]+)/$',
        s5013_infodpsperante_api_views.s5013infoDpsPerAntEDetail.as_view() ),

    url(r'^s5013-infodpsperante/listar/(?P<hash>.*)/$', 
        s5013_infodpsperante_listar_views.listar, 
        name='s5013_infodpsperante'),

    url(r'^s5013-infodpsperante/salvar/(?P<hash>.*)/$', 
        s5013_infodpsperante_salvar_views.salvar, 
        name='s5013_infodpsperante_salvar'),

    url(r'^s5013-dpsperante/apagar/(?P<hash>.*)/$', 
        s5013_dpsperante_apagar_views.apagar, 
        name='s5013_dpsperante_apagar'),

    url(r'^s5013-dpsperante/api/$',
        s5013_dpsperante_api_views.s5013dpsPerAntEList.as_view() ),

    url(r'^s5013-dpsperante/api/(?P<pk>[0-9]+)/$',
        s5013_dpsperante_api_views.s5013dpsPerAntEDetail.as_view() ),

    url(r'^s5013-dpsperante/listar/(?P<hash>.*)/$', 
        s5013_dpsperante_listar_views.listar, 
        name='s5013_dpsperante'),

    url(r'^s5013-dpsperante/salvar/(?P<hash>.*)/$', 
        s5013_dpsperante_salvar_views.salvar, 
        name='s5013_dpsperante_salvar'),


]