#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1210.views import s1210_deps_apagar as s1210_deps_apagar_views
from emensageriapro.s1210.views import s1210_deps_listar as s1210_deps_listar_views
from emensageriapro.s1210.views import s1210_deps_salvar as s1210_deps_salvar_views
from emensageriapro.s1210.views import s1210_deps_api as s1210_deps_api_views
from emensageriapro.s1210.views import s1210_infopgto_apagar as s1210_infopgto_apagar_views
from emensageriapro.s1210.views import s1210_infopgto_listar as s1210_infopgto_listar_views
from emensageriapro.s1210.views import s1210_infopgto_salvar as s1210_infopgto_salvar_views
from emensageriapro.s1210.views import s1210_infopgto_api as s1210_infopgto_api_views
from emensageriapro.s1210.views import s1210_detpgtofl_apagar as s1210_detpgtofl_apagar_views
from emensageriapro.s1210.views import s1210_detpgtofl_listar as s1210_detpgtofl_listar_views
from emensageriapro.s1210.views import s1210_detpgtofl_salvar as s1210_detpgtofl_salvar_views
from emensageriapro.s1210.views import s1210_detpgtofl_api as s1210_detpgtofl_api_views
from emensageriapro.s1210.views import s1210_detpgtofl_retpgtotot_apagar as s1210_detpgtofl_retpgtotot_apagar_views
from emensageriapro.s1210.views import s1210_detpgtofl_retpgtotot_listar as s1210_detpgtofl_retpgtotot_listar_views
from emensageriapro.s1210.views import s1210_detpgtofl_retpgtotot_salvar as s1210_detpgtofl_retpgtotot_salvar_views
from emensageriapro.s1210.views import s1210_detpgtofl_retpgtotot_api as s1210_detpgtofl_retpgtotot_api_views
from emensageriapro.s1210.views import s1210_detpgtofl_penalim_apagar as s1210_detpgtofl_penalim_apagar_views
from emensageriapro.s1210.views import s1210_detpgtofl_penalim_listar as s1210_detpgtofl_penalim_listar_views
from emensageriapro.s1210.views import s1210_detpgtofl_penalim_salvar as s1210_detpgtofl_penalim_salvar_views
from emensageriapro.s1210.views import s1210_detpgtofl_penalim_api as s1210_detpgtofl_penalim_api_views
from emensageriapro.s1210.views import s1210_detpgtofl_infopgtoparc_apagar as s1210_detpgtofl_infopgtoparc_apagar_views
from emensageriapro.s1210.views import s1210_detpgtofl_infopgtoparc_listar as s1210_detpgtofl_infopgtoparc_listar_views
from emensageriapro.s1210.views import s1210_detpgtofl_infopgtoparc_salvar as s1210_detpgtofl_infopgtoparc_salvar_views
from emensageriapro.s1210.views import s1210_detpgtofl_infopgtoparc_api as s1210_detpgtofl_infopgtoparc_api_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_apagar as s1210_detpgtobenpr_apagar_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_listar as s1210_detpgtobenpr_listar_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_salvar as s1210_detpgtobenpr_salvar_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_api as s1210_detpgtobenpr_api_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_retpgtotot_apagar as s1210_detpgtobenpr_retpgtotot_apagar_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_retpgtotot_listar as s1210_detpgtobenpr_retpgtotot_listar_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_retpgtotot_salvar as s1210_detpgtobenpr_retpgtotot_salvar_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_retpgtotot_api as s1210_detpgtobenpr_retpgtotot_api_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_infopgtoparc_apagar as s1210_detpgtobenpr_infopgtoparc_apagar_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_infopgtoparc_listar as s1210_detpgtobenpr_infopgtoparc_listar_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_infopgtoparc_salvar as s1210_detpgtobenpr_infopgtoparc_salvar_views
from emensageriapro.s1210.views import s1210_detpgtobenpr_infopgtoparc_api as s1210_detpgtobenpr_infopgtoparc_api_views
from emensageriapro.s1210.views import s1210_detpgtofer_apagar as s1210_detpgtofer_apagar_views
from emensageriapro.s1210.views import s1210_detpgtofer_listar as s1210_detpgtofer_listar_views
from emensageriapro.s1210.views import s1210_detpgtofer_salvar as s1210_detpgtofer_salvar_views
from emensageriapro.s1210.views import s1210_detpgtofer_api as s1210_detpgtofer_api_views
from emensageriapro.s1210.views import s1210_detpgtofer_detrubrfer_apagar as s1210_detpgtofer_detrubrfer_apagar_views
from emensageriapro.s1210.views import s1210_detpgtofer_detrubrfer_listar as s1210_detpgtofer_detrubrfer_listar_views
from emensageriapro.s1210.views import s1210_detpgtofer_detrubrfer_salvar as s1210_detpgtofer_detrubrfer_salvar_views
from emensageriapro.s1210.views import s1210_detpgtofer_detrubrfer_api as s1210_detpgtofer_detrubrfer_api_views
from emensageriapro.s1210.views import s1210_detpgtofer_penalim_apagar as s1210_detpgtofer_penalim_apagar_views
from emensageriapro.s1210.views import s1210_detpgtofer_penalim_listar as s1210_detpgtofer_penalim_listar_views
from emensageriapro.s1210.views import s1210_detpgtofer_penalim_salvar as s1210_detpgtofer_penalim_salvar_views
from emensageriapro.s1210.views import s1210_detpgtofer_penalim_api as s1210_detpgtofer_penalim_api_views
from emensageriapro.s1210.views import s1210_detpgtoant_apagar as s1210_detpgtoant_apagar_views
from emensageriapro.s1210.views import s1210_detpgtoant_listar as s1210_detpgtoant_listar_views
from emensageriapro.s1210.views import s1210_detpgtoant_salvar as s1210_detpgtoant_salvar_views
from emensageriapro.s1210.views import s1210_detpgtoant_api as s1210_detpgtoant_api_views
from emensageriapro.s1210.views import s1210_detpgtoant_infopgtoant_apagar as s1210_detpgtoant_infopgtoant_apagar_views
from emensageriapro.s1210.views import s1210_detpgtoant_infopgtoant_listar as s1210_detpgtoant_infopgtoant_listar_views
from emensageriapro.s1210.views import s1210_detpgtoant_infopgtoant_salvar as s1210_detpgtoant_infopgtoant_salvar_views
from emensageriapro.s1210.views import s1210_detpgtoant_infopgtoant_api as s1210_detpgtoant_infopgtoant_api_views
from emensageriapro.s1210.views import s1210_idepgtoext_apagar as s1210_idepgtoext_apagar_views
from emensageriapro.s1210.views import s1210_idepgtoext_listar as s1210_idepgtoext_listar_views
from emensageriapro.s1210.views import s1210_idepgtoext_salvar as s1210_idepgtoext_salvar_views
from emensageriapro.s1210.views import s1210_idepgtoext_api as s1210_idepgtoext_api_views



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


    url(r'^s1210-deps/apagar/(?P<hash>.*)/$', 
        s1210_deps_apagar_views.apagar, 
        name='s1210_deps_apagar'),

    url(r'^s1210-deps/api/$',
        s1210_deps_api_views.s1210depsList.as_view() ),

    url(r'^s1210-deps/api/(?P<pk>[0-9]+)/$',
        s1210_deps_api_views.s1210depsDetail.as_view() ),

    url(r'^s1210-deps/listar/(?P<hash>.*)/$', 
        s1210_deps_listar_views.listar, 
        name='s1210_deps'),

    url(r'^s1210-deps/salvar/(?P<hash>.*)/$', 
        s1210_deps_salvar_views.salvar, 
        name='s1210_deps_salvar'),

    url(r'^s1210-infopgto/apagar/(?P<hash>.*)/$', 
        s1210_infopgto_apagar_views.apagar, 
        name='s1210_infopgto_apagar'),

    url(r'^s1210-infopgto/api/$',
        s1210_infopgto_api_views.s1210infoPgtoList.as_view() ),

    url(r'^s1210-infopgto/api/(?P<pk>[0-9]+)/$',
        s1210_infopgto_api_views.s1210infoPgtoDetail.as_view() ),

    url(r'^s1210-infopgto/listar/(?P<hash>.*)/$', 
        s1210_infopgto_listar_views.listar, 
        name='s1210_infopgto'),

    url(r'^s1210-infopgto/salvar/(?P<hash>.*)/$', 
        s1210_infopgto_salvar_views.salvar, 
        name='s1210_infopgto_salvar'),

    url(r'^s1210-detpgtofl/apagar/(?P<hash>.*)/$', 
        s1210_detpgtofl_apagar_views.apagar, 
        name='s1210_detpgtofl_apagar'),

    url(r'^s1210-detpgtofl/api/$',
        s1210_detpgtofl_api_views.s1210detPgtoFlList.as_view() ),

    url(r'^s1210-detpgtofl/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtofl_api_views.s1210detPgtoFlDetail.as_view() ),

    url(r'^s1210-detpgtofl/listar/(?P<hash>.*)/$', 
        s1210_detpgtofl_listar_views.listar, 
        name='s1210_detpgtofl'),

    url(r'^s1210-detpgtofl/salvar/(?P<hash>.*)/$', 
        s1210_detpgtofl_salvar_views.salvar, 
        name='s1210_detpgtofl_salvar'),

    url(r'^s1210-detpgtofl-retpgtotot/apagar/(?P<hash>.*)/$', 
        s1210_detpgtofl_retpgtotot_apagar_views.apagar, 
        name='s1210_detpgtofl_retpgtotot_apagar'),

    url(r'^s1210-detpgtofl-retpgtotot/api/$',
        s1210_detpgtofl_retpgtotot_api_views.s1210detPgtoFlretPgtoTotList.as_view() ),

    url(r'^s1210-detpgtofl-retpgtotot/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtofl_retpgtotot_api_views.s1210detPgtoFlretPgtoTotDetail.as_view() ),

    url(r'^s1210-detpgtofl-retpgtotot/listar/(?P<hash>.*)/$', 
        s1210_detpgtofl_retpgtotot_listar_views.listar, 
        name='s1210_detpgtofl_retpgtotot'),

    url(r'^s1210-detpgtofl-retpgtotot/salvar/(?P<hash>.*)/$', 
        s1210_detpgtofl_retpgtotot_salvar_views.salvar, 
        name='s1210_detpgtofl_retpgtotot_salvar'),

    url(r'^s1210-detpgtofl-penalim/apagar/(?P<hash>.*)/$', 
        s1210_detpgtofl_penalim_apagar_views.apagar, 
        name='s1210_detpgtofl_penalim_apagar'),

    url(r'^s1210-detpgtofl-penalim/api/$',
        s1210_detpgtofl_penalim_api_views.s1210detPgtoFlpenAlimList.as_view() ),

    url(r'^s1210-detpgtofl-penalim/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtofl_penalim_api_views.s1210detPgtoFlpenAlimDetail.as_view() ),

    url(r'^s1210-detpgtofl-penalim/listar/(?P<hash>.*)/$', 
        s1210_detpgtofl_penalim_listar_views.listar, 
        name='s1210_detpgtofl_penalim'),

    url(r'^s1210-detpgtofl-penalim/salvar/(?P<hash>.*)/$', 
        s1210_detpgtofl_penalim_salvar_views.salvar, 
        name='s1210_detpgtofl_penalim_salvar'),

    url(r'^s1210-detpgtofl-infopgtoparc/apagar/(?P<hash>.*)/$', 
        s1210_detpgtofl_infopgtoparc_apagar_views.apagar, 
        name='s1210_detpgtofl_infopgtoparc_apagar'),

    url(r'^s1210-detpgtofl-infopgtoparc/api/$',
        s1210_detpgtofl_infopgtoparc_api_views.s1210detPgtoFlinfoPgtoParcList.as_view() ),

    url(r'^s1210-detpgtofl-infopgtoparc/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtofl_infopgtoparc_api_views.s1210detPgtoFlinfoPgtoParcDetail.as_view() ),

    url(r'^s1210-detpgtofl-infopgtoparc/listar/(?P<hash>.*)/$', 
        s1210_detpgtofl_infopgtoparc_listar_views.listar, 
        name='s1210_detpgtofl_infopgtoparc'),

    url(r'^s1210-detpgtofl-infopgtoparc/salvar/(?P<hash>.*)/$', 
        s1210_detpgtofl_infopgtoparc_salvar_views.salvar, 
        name='s1210_detpgtofl_infopgtoparc_salvar'),

    url(r'^s1210-detpgtobenpr/apagar/(?P<hash>.*)/$', 
        s1210_detpgtobenpr_apagar_views.apagar, 
        name='s1210_detpgtobenpr_apagar'),

    url(r'^s1210-detpgtobenpr/api/$',
        s1210_detpgtobenpr_api_views.s1210detPgtoBenPrList.as_view() ),

    url(r'^s1210-detpgtobenpr/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtobenpr_api_views.s1210detPgtoBenPrDetail.as_view() ),

    url(r'^s1210-detpgtobenpr/listar/(?P<hash>.*)/$', 
        s1210_detpgtobenpr_listar_views.listar, 
        name='s1210_detpgtobenpr'),

    url(r'^s1210-detpgtobenpr/salvar/(?P<hash>.*)/$', 
        s1210_detpgtobenpr_salvar_views.salvar, 
        name='s1210_detpgtobenpr_salvar'),

    url(r'^s1210-detpgtobenpr-retpgtotot/apagar/(?P<hash>.*)/$', 
        s1210_detpgtobenpr_retpgtotot_apagar_views.apagar, 
        name='s1210_detpgtobenpr_retpgtotot_apagar'),

    url(r'^s1210-detpgtobenpr-retpgtotot/api/$',
        s1210_detpgtobenpr_retpgtotot_api_views.s1210detPgtoBenPrretPgtoTotList.as_view() ),

    url(r'^s1210-detpgtobenpr-retpgtotot/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtobenpr_retpgtotot_api_views.s1210detPgtoBenPrretPgtoTotDetail.as_view() ),

    url(r'^s1210-detpgtobenpr-retpgtotot/listar/(?P<hash>.*)/$', 
        s1210_detpgtobenpr_retpgtotot_listar_views.listar, 
        name='s1210_detpgtobenpr_retpgtotot'),

    url(r'^s1210-detpgtobenpr-retpgtotot/salvar/(?P<hash>.*)/$', 
        s1210_detpgtobenpr_retpgtotot_salvar_views.salvar, 
        name='s1210_detpgtobenpr_retpgtotot_salvar'),

    url(r'^s1210-detpgtobenpr-infopgtoparc/apagar/(?P<hash>.*)/$', 
        s1210_detpgtobenpr_infopgtoparc_apagar_views.apagar, 
        name='s1210_detpgtobenpr_infopgtoparc_apagar'),

    url(r'^s1210-detpgtobenpr-infopgtoparc/api/$',
        s1210_detpgtobenpr_infopgtoparc_api_views.s1210detPgtoBenPrinfoPgtoParcList.as_view() ),

    url(r'^s1210-detpgtobenpr-infopgtoparc/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtobenpr_infopgtoparc_api_views.s1210detPgtoBenPrinfoPgtoParcDetail.as_view() ),

    url(r'^s1210-detpgtobenpr-infopgtoparc/listar/(?P<hash>.*)/$', 
        s1210_detpgtobenpr_infopgtoparc_listar_views.listar, 
        name='s1210_detpgtobenpr_infopgtoparc'),

    url(r'^s1210-detpgtobenpr-infopgtoparc/salvar/(?P<hash>.*)/$', 
        s1210_detpgtobenpr_infopgtoparc_salvar_views.salvar, 
        name='s1210_detpgtobenpr_infopgtoparc_salvar'),

    url(r'^s1210-detpgtofer/apagar/(?P<hash>.*)/$', 
        s1210_detpgtofer_apagar_views.apagar, 
        name='s1210_detpgtofer_apagar'),

    url(r'^s1210-detpgtofer/api/$',
        s1210_detpgtofer_api_views.s1210detPgtoFerList.as_view() ),

    url(r'^s1210-detpgtofer/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtofer_api_views.s1210detPgtoFerDetail.as_view() ),

    url(r'^s1210-detpgtofer/listar/(?P<hash>.*)/$', 
        s1210_detpgtofer_listar_views.listar, 
        name='s1210_detpgtofer'),

    url(r'^s1210-detpgtofer/salvar/(?P<hash>.*)/$', 
        s1210_detpgtofer_salvar_views.salvar, 
        name='s1210_detpgtofer_salvar'),

    url(r'^s1210-detpgtofer-detrubrfer/apagar/(?P<hash>.*)/$', 
        s1210_detpgtofer_detrubrfer_apagar_views.apagar, 
        name='s1210_detpgtofer_detrubrfer_apagar'),

    url(r'^s1210-detpgtofer-detrubrfer/api/$',
        s1210_detpgtofer_detrubrfer_api_views.s1210detPgtoFerdetRubrFerList.as_view() ),

    url(r'^s1210-detpgtofer-detrubrfer/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtofer_detrubrfer_api_views.s1210detPgtoFerdetRubrFerDetail.as_view() ),

    url(r'^s1210-detpgtofer-detrubrfer/listar/(?P<hash>.*)/$', 
        s1210_detpgtofer_detrubrfer_listar_views.listar, 
        name='s1210_detpgtofer_detrubrfer'),

    url(r'^s1210-detpgtofer-detrubrfer/salvar/(?P<hash>.*)/$', 
        s1210_detpgtofer_detrubrfer_salvar_views.salvar, 
        name='s1210_detpgtofer_detrubrfer_salvar'),

    url(r'^s1210-detpgtofer-penalim/apagar/(?P<hash>.*)/$', 
        s1210_detpgtofer_penalim_apagar_views.apagar, 
        name='s1210_detpgtofer_penalim_apagar'),

    url(r'^s1210-detpgtofer-penalim/api/$',
        s1210_detpgtofer_penalim_api_views.s1210detPgtoFerpenAlimList.as_view() ),

    url(r'^s1210-detpgtofer-penalim/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtofer_penalim_api_views.s1210detPgtoFerpenAlimDetail.as_view() ),

    url(r'^s1210-detpgtofer-penalim/listar/(?P<hash>.*)/$', 
        s1210_detpgtofer_penalim_listar_views.listar, 
        name='s1210_detpgtofer_penalim'),

    url(r'^s1210-detpgtofer-penalim/salvar/(?P<hash>.*)/$', 
        s1210_detpgtofer_penalim_salvar_views.salvar, 
        name='s1210_detpgtofer_penalim_salvar'),

    url(r'^s1210-detpgtoant/apagar/(?P<hash>.*)/$', 
        s1210_detpgtoant_apagar_views.apagar, 
        name='s1210_detpgtoant_apagar'),

    url(r'^s1210-detpgtoant/api/$',
        s1210_detpgtoant_api_views.s1210detPgtoAntList.as_view() ),

    url(r'^s1210-detpgtoant/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtoant_api_views.s1210detPgtoAntDetail.as_view() ),

    url(r'^s1210-detpgtoant/listar/(?P<hash>.*)/$', 
        s1210_detpgtoant_listar_views.listar, 
        name='s1210_detpgtoant'),

    url(r'^s1210-detpgtoant/salvar/(?P<hash>.*)/$', 
        s1210_detpgtoant_salvar_views.salvar, 
        name='s1210_detpgtoant_salvar'),

    url(r'^s1210-detpgtoant-infopgtoant/apagar/(?P<hash>.*)/$', 
        s1210_detpgtoant_infopgtoant_apagar_views.apagar, 
        name='s1210_detpgtoant_infopgtoant_apagar'),

    url(r'^s1210-detpgtoant-infopgtoant/api/$',
        s1210_detpgtoant_infopgtoant_api_views.s1210detPgtoAntinfoPgtoAntList.as_view() ),

    url(r'^s1210-detpgtoant-infopgtoant/api/(?P<pk>[0-9]+)/$',
        s1210_detpgtoant_infopgtoant_api_views.s1210detPgtoAntinfoPgtoAntDetail.as_view() ),

    url(r'^s1210-detpgtoant-infopgtoant/listar/(?P<hash>.*)/$', 
        s1210_detpgtoant_infopgtoant_listar_views.listar, 
        name='s1210_detpgtoant_infopgtoant'),

    url(r'^s1210-detpgtoant-infopgtoant/salvar/(?P<hash>.*)/$', 
        s1210_detpgtoant_infopgtoant_salvar_views.salvar, 
        name='s1210_detpgtoant_infopgtoant_salvar'),

    url(r'^s1210-idepgtoext/apagar/(?P<hash>.*)/$', 
        s1210_idepgtoext_apagar_views.apagar, 
        name='s1210_idepgtoext_apagar'),

    url(r'^s1210-idepgtoext/api/$',
        s1210_idepgtoext_api_views.s1210idePgtoExtList.as_view() ),

    url(r'^s1210-idepgtoext/api/(?P<pk>[0-9]+)/$',
        s1210_idepgtoext_api_views.s1210idePgtoExtDetail.as_view() ),

    url(r'^s1210-idepgtoext/listar/(?P<hash>.*)/$', 
        s1210_idepgtoext_listar_views.listar, 
        name='s1210_idepgtoext'),

    url(r'^s1210-idepgtoext/salvar/(?P<hash>.*)/$', 
        s1210_idepgtoext_salvar_views.salvar, 
        name='s1210_idepgtoext_salvar'),


]