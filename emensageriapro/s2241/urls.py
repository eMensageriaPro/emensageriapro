#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2241.views import s2241_insalperic_apagar as s2241_insalperic_apagar_views
from emensageriapro.s2241.views import s2241_insalperic_listar as s2241_insalperic_listar_views
from emensageriapro.s2241.views import s2241_insalperic_salvar as s2241_insalperic_salvar_views
from emensageriapro.s2241.views import s2241_insalperic_api as s2241_insalperic_api_views
from emensageriapro.s2241.views import s2241_iniinsalperic_apagar as s2241_iniinsalperic_apagar_views
from emensageriapro.s2241.views import s2241_iniinsalperic_listar as s2241_iniinsalperic_listar_views
from emensageriapro.s2241.views import s2241_iniinsalperic_salvar as s2241_iniinsalperic_salvar_views
from emensageriapro.s2241.views import s2241_iniinsalperic_api as s2241_iniinsalperic_api_views
from emensageriapro.s2241.views import s2241_iniinsalperic_infoamb_apagar as s2241_iniinsalperic_infoamb_apagar_views
from emensageriapro.s2241.views import s2241_iniinsalperic_infoamb_listar as s2241_iniinsalperic_infoamb_listar_views
from emensageriapro.s2241.views import s2241_iniinsalperic_infoamb_salvar as s2241_iniinsalperic_infoamb_salvar_views
from emensageriapro.s2241.views import s2241_iniinsalperic_infoamb_api as s2241_iniinsalperic_infoamb_api_views
from emensageriapro.s2241.views import s2241_iniinsalperic_fatrisco_apagar as s2241_iniinsalperic_fatrisco_apagar_views
from emensageriapro.s2241.views import s2241_iniinsalperic_fatrisco_listar as s2241_iniinsalperic_fatrisco_listar_views
from emensageriapro.s2241.views import s2241_iniinsalperic_fatrisco_salvar as s2241_iniinsalperic_fatrisco_salvar_views
from emensageriapro.s2241.views import s2241_iniinsalperic_fatrisco_api as s2241_iniinsalperic_fatrisco_api_views
from emensageriapro.s2241.views import s2241_altinsalperic_apagar as s2241_altinsalperic_apagar_views
from emensageriapro.s2241.views import s2241_altinsalperic_listar as s2241_altinsalperic_listar_views
from emensageriapro.s2241.views import s2241_altinsalperic_salvar as s2241_altinsalperic_salvar_views
from emensageriapro.s2241.views import s2241_altinsalperic_api as s2241_altinsalperic_api_views
from emensageriapro.s2241.views import s2241_altinsalperic_infoamb_apagar as s2241_altinsalperic_infoamb_apagar_views
from emensageriapro.s2241.views import s2241_altinsalperic_infoamb_listar as s2241_altinsalperic_infoamb_listar_views
from emensageriapro.s2241.views import s2241_altinsalperic_infoamb_salvar as s2241_altinsalperic_infoamb_salvar_views
from emensageriapro.s2241.views import s2241_altinsalperic_infoamb_api as s2241_altinsalperic_infoamb_api_views
from emensageriapro.s2241.views import s2241_altinsalperic_fatrisco_apagar as s2241_altinsalperic_fatrisco_apagar_views
from emensageriapro.s2241.views import s2241_altinsalperic_fatrisco_listar as s2241_altinsalperic_fatrisco_listar_views
from emensageriapro.s2241.views import s2241_altinsalperic_fatrisco_salvar as s2241_altinsalperic_fatrisco_salvar_views
from emensageriapro.s2241.views import s2241_altinsalperic_fatrisco_api as s2241_altinsalperic_fatrisco_api_views
from emensageriapro.s2241.views import s2241_fiminsalperic_apagar as s2241_fiminsalperic_apagar_views
from emensageriapro.s2241.views import s2241_fiminsalperic_listar as s2241_fiminsalperic_listar_views
from emensageriapro.s2241.views import s2241_fiminsalperic_salvar as s2241_fiminsalperic_salvar_views
from emensageriapro.s2241.views import s2241_fiminsalperic_api as s2241_fiminsalperic_api_views
from emensageriapro.s2241.views import s2241_fiminsalperic_infoamb_apagar as s2241_fiminsalperic_infoamb_apagar_views
from emensageriapro.s2241.views import s2241_fiminsalperic_infoamb_listar as s2241_fiminsalperic_infoamb_listar_views
from emensageriapro.s2241.views import s2241_fiminsalperic_infoamb_salvar as s2241_fiminsalperic_infoamb_salvar_views
from emensageriapro.s2241.views import s2241_fiminsalperic_infoamb_api as s2241_fiminsalperic_infoamb_api_views
from emensageriapro.s2241.views import s2241_aposentesp_apagar as s2241_aposentesp_apagar_views
from emensageriapro.s2241.views import s2241_aposentesp_listar as s2241_aposentesp_listar_views
from emensageriapro.s2241.views import s2241_aposentesp_salvar as s2241_aposentesp_salvar_views
from emensageriapro.s2241.views import s2241_aposentesp_api as s2241_aposentesp_api_views
from emensageriapro.s2241.views import s2241_iniaposentesp_apagar as s2241_iniaposentesp_apagar_views
from emensageriapro.s2241.views import s2241_iniaposentesp_listar as s2241_iniaposentesp_listar_views
from emensageriapro.s2241.views import s2241_iniaposentesp_salvar as s2241_iniaposentesp_salvar_views
from emensageriapro.s2241.views import s2241_iniaposentesp_api as s2241_iniaposentesp_api_views
from emensageriapro.s2241.views import s2241_iniaposentesp_infoamb_apagar as s2241_iniaposentesp_infoamb_apagar_views
from emensageriapro.s2241.views import s2241_iniaposentesp_infoamb_listar as s2241_iniaposentesp_infoamb_listar_views
from emensageriapro.s2241.views import s2241_iniaposentesp_infoamb_salvar as s2241_iniaposentesp_infoamb_salvar_views
from emensageriapro.s2241.views import s2241_iniaposentesp_infoamb_api as s2241_iniaposentesp_infoamb_api_views
from emensageriapro.s2241.views import s2241_iniaposentesp_fatrisco_apagar as s2241_iniaposentesp_fatrisco_apagar_views
from emensageriapro.s2241.views import s2241_iniaposentesp_fatrisco_listar as s2241_iniaposentesp_fatrisco_listar_views
from emensageriapro.s2241.views import s2241_iniaposentesp_fatrisco_salvar as s2241_iniaposentesp_fatrisco_salvar_views
from emensageriapro.s2241.views import s2241_iniaposentesp_fatrisco_api as s2241_iniaposentesp_fatrisco_api_views
from emensageriapro.s2241.views import s2241_altaposentesp_apagar as s2241_altaposentesp_apagar_views
from emensageriapro.s2241.views import s2241_altaposentesp_listar as s2241_altaposentesp_listar_views
from emensageriapro.s2241.views import s2241_altaposentesp_salvar as s2241_altaposentesp_salvar_views
from emensageriapro.s2241.views import s2241_altaposentesp_api as s2241_altaposentesp_api_views
from emensageriapro.s2241.views import s2241_altaposentesp_infoamb_apagar as s2241_altaposentesp_infoamb_apagar_views
from emensageriapro.s2241.views import s2241_altaposentesp_infoamb_listar as s2241_altaposentesp_infoamb_listar_views
from emensageriapro.s2241.views import s2241_altaposentesp_infoamb_salvar as s2241_altaposentesp_infoamb_salvar_views
from emensageriapro.s2241.views import s2241_altaposentesp_infoamb_api as s2241_altaposentesp_infoamb_api_views
from emensageriapro.s2241.views import s2241_altaposentesp_fatrisco_apagar as s2241_altaposentesp_fatrisco_apagar_views
from emensageriapro.s2241.views import s2241_altaposentesp_fatrisco_listar as s2241_altaposentesp_fatrisco_listar_views
from emensageriapro.s2241.views import s2241_altaposentesp_fatrisco_salvar as s2241_altaposentesp_fatrisco_salvar_views
from emensageriapro.s2241.views import s2241_altaposentesp_fatrisco_api as s2241_altaposentesp_fatrisco_api_views
from emensageriapro.s2241.views import s2241_fimaposentesp_apagar as s2241_fimaposentesp_apagar_views
from emensageriapro.s2241.views import s2241_fimaposentesp_listar as s2241_fimaposentesp_listar_views
from emensageriapro.s2241.views import s2241_fimaposentesp_salvar as s2241_fimaposentesp_salvar_views
from emensageriapro.s2241.views import s2241_fimaposentesp_api as s2241_fimaposentesp_api_views
from emensageriapro.s2241.views import s2241_fimaposentesp_infoamb_apagar as s2241_fimaposentesp_infoamb_apagar_views
from emensageriapro.s2241.views import s2241_fimaposentesp_infoamb_listar as s2241_fimaposentesp_infoamb_listar_views
from emensageriapro.s2241.views import s2241_fimaposentesp_infoamb_salvar as s2241_fimaposentesp_infoamb_salvar_views
from emensageriapro.s2241.views import s2241_fimaposentesp_infoamb_api as s2241_fimaposentesp_infoamb_api_views



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


    url(r'^s2241-insalperic/apagar/(?P<pk>[0-9]+)/$',
        s2241_insalperic_apagar_views.apagar,
        name='s2241_insalperic_apagar'),

    url(r'^s2241-insalperic/api/$',
        s2241_insalperic_api_views.s2241insalPericList.as_view() ),

    url(r'^s2241-insalperic/api/(?P<pk>[0-9]+)/$',
        s2241_insalperic_api_views.s2241insalPericDetail.as_view() ),

    url(r'^s2241-insalperic/$',
        s2241_insalperic_listar_views.listar,
        name='s2241_insalperic'),

    url(r'^s2241-insalperic/salvar/(?P<pk>[0-9]+)/$',
        s2241_insalperic_salvar_views.salvar,
        name='s2241_insalperic_salvar'),

    url(r'^s2241-insalperic/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_insalperic_salvar_views.salvar,
        name='s2241_insalperic_salvar_tab'),

    url(r'^s2241-insalperic/cadastrar/$',
        s2241_insalperic_salvar_views.salvar,
        name='s2241_insalperic_cadastrar'),

    url(r'^s2241-insalperic/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_insalperic_salvar_views.salvar,
        name='s2241_insalperic_salvar_output'),

    url(r'^s2241-insalperic/(?P<output>[\w-]+)/$',
        s2241_insalperic_listar_views.listar,
        name='s2241_insalperic_output'),

    url(r'^s2241-iniinsalperic/apagar/(?P<pk>[0-9]+)/$',
        s2241_iniinsalperic_apagar_views.apagar,
        name='s2241_iniinsalperic_apagar'),

    url(r'^s2241-iniinsalperic/api/$',
        s2241_iniinsalperic_api_views.s2241iniInsalPericList.as_view() ),

    url(r'^s2241-iniinsalperic/api/(?P<pk>[0-9]+)/$',
        s2241_iniinsalperic_api_views.s2241iniInsalPericDetail.as_view() ),

    url(r'^s2241-iniinsalperic/$',
        s2241_iniinsalperic_listar_views.listar,
        name='s2241_iniinsalperic'),

    url(r'^s2241-iniinsalperic/salvar/(?P<pk>[0-9]+)/$',
        s2241_iniinsalperic_salvar_views.salvar,
        name='s2241_iniinsalperic_salvar'),

    url(r'^s2241-iniinsalperic/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_iniinsalperic_salvar_views.salvar,
        name='s2241_iniinsalperic_salvar_tab'),

    url(r'^s2241-iniinsalperic/cadastrar/$',
        s2241_iniinsalperic_salvar_views.salvar,
        name='s2241_iniinsalperic_cadastrar'),

    url(r'^s2241-iniinsalperic/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_iniinsalperic_salvar_views.salvar,
        name='s2241_iniinsalperic_salvar_output'),

    url(r'^s2241-iniinsalperic/(?P<output>[\w-]+)/$',
        s2241_iniinsalperic_listar_views.listar,
        name='s2241_iniinsalperic_output'),

    url(r'^s2241-iniinsalperic-infoamb/apagar/(?P<pk>[0-9]+)/$',
        s2241_iniinsalperic_infoamb_apagar_views.apagar,
        name='s2241_iniinsalperic_infoamb_apagar'),

    url(r'^s2241-iniinsalperic-infoamb/api/$',
        s2241_iniinsalperic_infoamb_api_views.s2241iniInsalPericinfoAmbList.as_view() ),

    url(r'^s2241-iniinsalperic-infoamb/api/(?P<pk>[0-9]+)/$',
        s2241_iniinsalperic_infoamb_api_views.s2241iniInsalPericinfoAmbDetail.as_view() ),

    url(r'^s2241-iniinsalperic-infoamb/$',
        s2241_iniinsalperic_infoamb_listar_views.listar,
        name='s2241_iniinsalperic_infoamb'),

    url(r'^s2241-iniinsalperic-infoamb/salvar/(?P<pk>[0-9]+)/$',
        s2241_iniinsalperic_infoamb_salvar_views.salvar,
        name='s2241_iniinsalperic_infoamb_salvar'),

    url(r'^s2241-iniinsalperic-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_iniinsalperic_infoamb_salvar_views.salvar,
        name='s2241_iniinsalperic_infoamb_salvar_tab'),

    url(r'^s2241-iniinsalperic-infoamb/cadastrar/$',
        s2241_iniinsalperic_infoamb_salvar_views.salvar,
        name='s2241_iniinsalperic_infoamb_cadastrar'),

    url(r'^s2241-iniinsalperic-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_iniinsalperic_infoamb_salvar_views.salvar,
        name='s2241_iniinsalperic_infoamb_salvar_output'),

    url(r'^s2241-iniinsalperic-infoamb/(?P<output>[\w-]+)/$',
        s2241_iniinsalperic_infoamb_listar_views.listar,
        name='s2241_iniinsalperic_infoamb_output'),

    url(r'^s2241-iniinsalperic-fatrisco/apagar/(?P<pk>[0-9]+)/$',
        s2241_iniinsalperic_fatrisco_apagar_views.apagar,
        name='s2241_iniinsalperic_fatrisco_apagar'),

    url(r'^s2241-iniinsalperic-fatrisco/api/$',
        s2241_iniinsalperic_fatrisco_api_views.s2241iniInsalPericfatRiscoList.as_view() ),

    url(r'^s2241-iniinsalperic-fatrisco/api/(?P<pk>[0-9]+)/$',
        s2241_iniinsalperic_fatrisco_api_views.s2241iniInsalPericfatRiscoDetail.as_view() ),

    url(r'^s2241-iniinsalperic-fatrisco/$',
        s2241_iniinsalperic_fatrisco_listar_views.listar,
        name='s2241_iniinsalperic_fatrisco'),

    url(r'^s2241-iniinsalperic-fatrisco/salvar/(?P<pk>[0-9]+)/$',
        s2241_iniinsalperic_fatrisco_salvar_views.salvar,
        name='s2241_iniinsalperic_fatrisco_salvar'),

    url(r'^s2241-iniinsalperic-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_iniinsalperic_fatrisco_salvar_views.salvar,
        name='s2241_iniinsalperic_fatrisco_salvar_tab'),

    url(r'^s2241-iniinsalperic-fatrisco/cadastrar/$',
        s2241_iniinsalperic_fatrisco_salvar_views.salvar,
        name='s2241_iniinsalperic_fatrisco_cadastrar'),

    url(r'^s2241-iniinsalperic-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_iniinsalperic_fatrisco_salvar_views.salvar,
        name='s2241_iniinsalperic_fatrisco_salvar_output'),

    url(r'^s2241-iniinsalperic-fatrisco/(?P<output>[\w-]+)/$',
        s2241_iniinsalperic_fatrisco_listar_views.listar,
        name='s2241_iniinsalperic_fatrisco_output'),

    url(r'^s2241-altinsalperic/apagar/(?P<pk>[0-9]+)/$',
        s2241_altinsalperic_apagar_views.apagar,
        name='s2241_altinsalperic_apagar'),

    url(r'^s2241-altinsalperic/api/$',
        s2241_altinsalperic_api_views.s2241altInsalPericList.as_view() ),

    url(r'^s2241-altinsalperic/api/(?P<pk>[0-9]+)/$',
        s2241_altinsalperic_api_views.s2241altInsalPericDetail.as_view() ),

    url(r'^s2241-altinsalperic/$',
        s2241_altinsalperic_listar_views.listar,
        name='s2241_altinsalperic'),

    url(r'^s2241-altinsalperic/salvar/(?P<pk>[0-9]+)/$',
        s2241_altinsalperic_salvar_views.salvar,
        name='s2241_altinsalperic_salvar'),

    url(r'^s2241-altinsalperic/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_altinsalperic_salvar_views.salvar,
        name='s2241_altinsalperic_salvar_tab'),

    url(r'^s2241-altinsalperic/cadastrar/$',
        s2241_altinsalperic_salvar_views.salvar,
        name='s2241_altinsalperic_cadastrar'),

    url(r'^s2241-altinsalperic/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_altinsalperic_salvar_views.salvar,
        name='s2241_altinsalperic_salvar_output'),

    url(r'^s2241-altinsalperic/(?P<output>[\w-]+)/$',
        s2241_altinsalperic_listar_views.listar,
        name='s2241_altinsalperic_output'),

    url(r'^s2241-altinsalperic-infoamb/apagar/(?P<pk>[0-9]+)/$',
        s2241_altinsalperic_infoamb_apagar_views.apagar,
        name='s2241_altinsalperic_infoamb_apagar'),

    url(r'^s2241-altinsalperic-infoamb/api/$',
        s2241_altinsalperic_infoamb_api_views.s2241altInsalPericinfoambList.as_view() ),

    url(r'^s2241-altinsalperic-infoamb/api/(?P<pk>[0-9]+)/$',
        s2241_altinsalperic_infoamb_api_views.s2241altInsalPericinfoambDetail.as_view() ),

    url(r'^s2241-altinsalperic-infoamb/$',
        s2241_altinsalperic_infoamb_listar_views.listar,
        name='s2241_altinsalperic_infoamb'),

    url(r'^s2241-altinsalperic-infoamb/salvar/(?P<pk>[0-9]+)/$',
        s2241_altinsalperic_infoamb_salvar_views.salvar,
        name='s2241_altinsalperic_infoamb_salvar'),

    url(r'^s2241-altinsalperic-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_altinsalperic_infoamb_salvar_views.salvar,
        name='s2241_altinsalperic_infoamb_salvar_tab'),

    url(r'^s2241-altinsalperic-infoamb/cadastrar/$',
        s2241_altinsalperic_infoamb_salvar_views.salvar,
        name='s2241_altinsalperic_infoamb_cadastrar'),

    url(r'^s2241-altinsalperic-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_altinsalperic_infoamb_salvar_views.salvar,
        name='s2241_altinsalperic_infoamb_salvar_output'),

    url(r'^s2241-altinsalperic-infoamb/(?P<output>[\w-]+)/$',
        s2241_altinsalperic_infoamb_listar_views.listar,
        name='s2241_altinsalperic_infoamb_output'),

    url(r'^s2241-altinsalperic-fatrisco/apagar/(?P<pk>[0-9]+)/$',
        s2241_altinsalperic_fatrisco_apagar_views.apagar,
        name='s2241_altinsalperic_fatrisco_apagar'),

    url(r'^s2241-altinsalperic-fatrisco/api/$',
        s2241_altinsalperic_fatrisco_api_views.s2241altInsalPericfatRiscoList.as_view() ),

    url(r'^s2241-altinsalperic-fatrisco/api/(?P<pk>[0-9]+)/$',
        s2241_altinsalperic_fatrisco_api_views.s2241altInsalPericfatRiscoDetail.as_view() ),

    url(r'^s2241-altinsalperic-fatrisco/$',
        s2241_altinsalperic_fatrisco_listar_views.listar,
        name='s2241_altinsalperic_fatrisco'),

    url(r'^s2241-altinsalperic-fatrisco/salvar/(?P<pk>[0-9]+)/$',
        s2241_altinsalperic_fatrisco_salvar_views.salvar,
        name='s2241_altinsalperic_fatrisco_salvar'),

    url(r'^s2241-altinsalperic-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_altinsalperic_fatrisco_salvar_views.salvar,
        name='s2241_altinsalperic_fatrisco_salvar_tab'),

    url(r'^s2241-altinsalperic-fatrisco/cadastrar/$',
        s2241_altinsalperic_fatrisco_salvar_views.salvar,
        name='s2241_altinsalperic_fatrisco_cadastrar'),

    url(r'^s2241-altinsalperic-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_altinsalperic_fatrisco_salvar_views.salvar,
        name='s2241_altinsalperic_fatrisco_salvar_output'),

    url(r'^s2241-altinsalperic-fatrisco/(?P<output>[\w-]+)/$',
        s2241_altinsalperic_fatrisco_listar_views.listar,
        name='s2241_altinsalperic_fatrisco_output'),

    url(r'^s2241-fiminsalperic/apagar/(?P<pk>[0-9]+)/$',
        s2241_fiminsalperic_apagar_views.apagar,
        name='s2241_fiminsalperic_apagar'),

    url(r'^s2241-fiminsalperic/api/$',
        s2241_fiminsalperic_api_views.s2241fimInsalPericList.as_view() ),

    url(r'^s2241-fiminsalperic/api/(?P<pk>[0-9]+)/$',
        s2241_fiminsalperic_api_views.s2241fimInsalPericDetail.as_view() ),

    url(r'^s2241-fiminsalperic/$',
        s2241_fiminsalperic_listar_views.listar,
        name='s2241_fiminsalperic'),

    url(r'^s2241-fiminsalperic/salvar/(?P<pk>[0-9]+)/$',
        s2241_fiminsalperic_salvar_views.salvar,
        name='s2241_fiminsalperic_salvar'),

    url(r'^s2241-fiminsalperic/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_fiminsalperic_salvar_views.salvar,
        name='s2241_fiminsalperic_salvar_tab'),

    url(r'^s2241-fiminsalperic/cadastrar/$',
        s2241_fiminsalperic_salvar_views.salvar,
        name='s2241_fiminsalperic_cadastrar'),

    url(r'^s2241-fiminsalperic/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_fiminsalperic_salvar_views.salvar,
        name='s2241_fiminsalperic_salvar_output'),

    url(r'^s2241-fiminsalperic/(?P<output>[\w-]+)/$',
        s2241_fiminsalperic_listar_views.listar,
        name='s2241_fiminsalperic_output'),

    url(r'^s2241-fiminsalperic-infoamb/apagar/(?P<pk>[0-9]+)/$',
        s2241_fiminsalperic_infoamb_apagar_views.apagar,
        name='s2241_fiminsalperic_infoamb_apagar'),

    url(r'^s2241-fiminsalperic-infoamb/api/$',
        s2241_fiminsalperic_infoamb_api_views.s2241fimInsalPericinfoAmbList.as_view() ),

    url(r'^s2241-fiminsalperic-infoamb/api/(?P<pk>[0-9]+)/$',
        s2241_fiminsalperic_infoamb_api_views.s2241fimInsalPericinfoAmbDetail.as_view() ),

    url(r'^s2241-fiminsalperic-infoamb/$',
        s2241_fiminsalperic_infoamb_listar_views.listar,
        name='s2241_fiminsalperic_infoamb'),

    url(r'^s2241-fiminsalperic-infoamb/salvar/(?P<pk>[0-9]+)/$',
        s2241_fiminsalperic_infoamb_salvar_views.salvar,
        name='s2241_fiminsalperic_infoamb_salvar'),

    url(r'^s2241-fiminsalperic-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_fiminsalperic_infoamb_salvar_views.salvar,
        name='s2241_fiminsalperic_infoamb_salvar_tab'),

    url(r'^s2241-fiminsalperic-infoamb/cadastrar/$',
        s2241_fiminsalperic_infoamb_salvar_views.salvar,
        name='s2241_fiminsalperic_infoamb_cadastrar'),

    url(r'^s2241-fiminsalperic-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_fiminsalperic_infoamb_salvar_views.salvar,
        name='s2241_fiminsalperic_infoamb_salvar_output'),

    url(r'^s2241-fiminsalperic-infoamb/(?P<output>[\w-]+)/$',
        s2241_fiminsalperic_infoamb_listar_views.listar,
        name='s2241_fiminsalperic_infoamb_output'),

    url(r'^s2241-aposentesp/apagar/(?P<pk>[0-9]+)/$',
        s2241_aposentesp_apagar_views.apagar,
        name='s2241_aposentesp_apagar'),

    url(r'^s2241-aposentesp/api/$',
        s2241_aposentesp_api_views.s2241aposentEspList.as_view() ),

    url(r'^s2241-aposentesp/api/(?P<pk>[0-9]+)/$',
        s2241_aposentesp_api_views.s2241aposentEspDetail.as_view() ),

    url(r'^s2241-aposentesp/$',
        s2241_aposentesp_listar_views.listar,
        name='s2241_aposentesp'),

    url(r'^s2241-aposentesp/salvar/(?P<pk>[0-9]+)/$',
        s2241_aposentesp_salvar_views.salvar,
        name='s2241_aposentesp_salvar'),

    url(r'^s2241-aposentesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_aposentesp_salvar_views.salvar,
        name='s2241_aposentesp_salvar_tab'),

    url(r'^s2241-aposentesp/cadastrar/$',
        s2241_aposentesp_salvar_views.salvar,
        name='s2241_aposentesp_cadastrar'),

    url(r'^s2241-aposentesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_aposentesp_salvar_views.salvar,
        name='s2241_aposentesp_salvar_output'),

    url(r'^s2241-aposentesp/(?P<output>[\w-]+)/$',
        s2241_aposentesp_listar_views.listar,
        name='s2241_aposentesp_output'),

    url(r'^s2241-iniaposentesp/apagar/(?P<pk>[0-9]+)/$',
        s2241_iniaposentesp_apagar_views.apagar,
        name='s2241_iniaposentesp_apagar'),

    url(r'^s2241-iniaposentesp/api/$',
        s2241_iniaposentesp_api_views.s2241iniAposentEspList.as_view() ),

    url(r'^s2241-iniaposentesp/api/(?P<pk>[0-9]+)/$',
        s2241_iniaposentesp_api_views.s2241iniAposentEspDetail.as_view() ),

    url(r'^s2241-iniaposentesp/$',
        s2241_iniaposentesp_listar_views.listar,
        name='s2241_iniaposentesp'),

    url(r'^s2241-iniaposentesp/salvar/(?P<pk>[0-9]+)/$',
        s2241_iniaposentesp_salvar_views.salvar,
        name='s2241_iniaposentesp_salvar'),

    url(r'^s2241-iniaposentesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_iniaposentesp_salvar_views.salvar,
        name='s2241_iniaposentesp_salvar_tab'),

    url(r'^s2241-iniaposentesp/cadastrar/$',
        s2241_iniaposentesp_salvar_views.salvar,
        name='s2241_iniaposentesp_cadastrar'),

    url(r'^s2241-iniaposentesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_iniaposentesp_salvar_views.salvar,
        name='s2241_iniaposentesp_salvar_output'),

    url(r'^s2241-iniaposentesp/(?P<output>[\w-]+)/$',
        s2241_iniaposentesp_listar_views.listar,
        name='s2241_iniaposentesp_output'),

    url(r'^s2241-iniaposentesp-infoamb/apagar/(?P<pk>[0-9]+)/$',
        s2241_iniaposentesp_infoamb_apagar_views.apagar,
        name='s2241_iniaposentesp_infoamb_apagar'),

    url(r'^s2241-iniaposentesp-infoamb/api/$',
        s2241_iniaposentesp_infoamb_api_views.s2241iniAposentEspinfoAmbList.as_view() ),

    url(r'^s2241-iniaposentesp-infoamb/api/(?P<pk>[0-9]+)/$',
        s2241_iniaposentesp_infoamb_api_views.s2241iniAposentEspinfoAmbDetail.as_view() ),

    url(r'^s2241-iniaposentesp-infoamb/$',
        s2241_iniaposentesp_infoamb_listar_views.listar,
        name='s2241_iniaposentesp_infoamb'),

    url(r'^s2241-iniaposentesp-infoamb/salvar/(?P<pk>[0-9]+)/$',
        s2241_iniaposentesp_infoamb_salvar_views.salvar,
        name='s2241_iniaposentesp_infoamb_salvar'),

    url(r'^s2241-iniaposentesp-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_iniaposentesp_infoamb_salvar_views.salvar,
        name='s2241_iniaposentesp_infoamb_salvar_tab'),

    url(r'^s2241-iniaposentesp-infoamb/cadastrar/$',
        s2241_iniaposentesp_infoamb_salvar_views.salvar,
        name='s2241_iniaposentesp_infoamb_cadastrar'),

    url(r'^s2241-iniaposentesp-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_iniaposentesp_infoamb_salvar_views.salvar,
        name='s2241_iniaposentesp_infoamb_salvar_output'),

    url(r'^s2241-iniaposentesp-infoamb/(?P<output>[\w-]+)/$',
        s2241_iniaposentesp_infoamb_listar_views.listar,
        name='s2241_iniaposentesp_infoamb_output'),

    url(r'^s2241-iniaposentesp-fatrisco/apagar/(?P<pk>[0-9]+)/$',
        s2241_iniaposentesp_fatrisco_apagar_views.apagar,
        name='s2241_iniaposentesp_fatrisco_apagar'),

    url(r'^s2241-iniaposentesp-fatrisco/api/$',
        s2241_iniaposentesp_fatrisco_api_views.s2241iniAposentEspfatRiscoList.as_view() ),

    url(r'^s2241-iniaposentesp-fatrisco/api/(?P<pk>[0-9]+)/$',
        s2241_iniaposentesp_fatrisco_api_views.s2241iniAposentEspfatRiscoDetail.as_view() ),

    url(r'^s2241-iniaposentesp-fatrisco/$',
        s2241_iniaposentesp_fatrisco_listar_views.listar,
        name='s2241_iniaposentesp_fatrisco'),

    url(r'^s2241-iniaposentesp-fatrisco/salvar/(?P<pk>[0-9]+)/$',
        s2241_iniaposentesp_fatrisco_salvar_views.salvar,
        name='s2241_iniaposentesp_fatrisco_salvar'),

    url(r'^s2241-iniaposentesp-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_iniaposentesp_fatrisco_salvar_views.salvar,
        name='s2241_iniaposentesp_fatrisco_salvar_tab'),

    url(r'^s2241-iniaposentesp-fatrisco/cadastrar/$',
        s2241_iniaposentesp_fatrisco_salvar_views.salvar,
        name='s2241_iniaposentesp_fatrisco_cadastrar'),

    url(r'^s2241-iniaposentesp-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_iniaposentesp_fatrisco_salvar_views.salvar,
        name='s2241_iniaposentesp_fatrisco_salvar_output'),

    url(r'^s2241-iniaposentesp-fatrisco/(?P<output>[\w-]+)/$',
        s2241_iniaposentesp_fatrisco_listar_views.listar,
        name='s2241_iniaposentesp_fatrisco_output'),

    url(r'^s2241-altaposentesp/apagar/(?P<pk>[0-9]+)/$',
        s2241_altaposentesp_apagar_views.apagar,
        name='s2241_altaposentesp_apagar'),

    url(r'^s2241-altaposentesp/api/$',
        s2241_altaposentesp_api_views.s2241altAposentEspList.as_view() ),

    url(r'^s2241-altaposentesp/api/(?P<pk>[0-9]+)/$',
        s2241_altaposentesp_api_views.s2241altAposentEspDetail.as_view() ),

    url(r'^s2241-altaposentesp/$',
        s2241_altaposentesp_listar_views.listar,
        name='s2241_altaposentesp'),

    url(r'^s2241-altaposentesp/salvar/(?P<pk>[0-9]+)/$',
        s2241_altaposentesp_salvar_views.salvar,
        name='s2241_altaposentesp_salvar'),

    url(r'^s2241-altaposentesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_altaposentesp_salvar_views.salvar,
        name='s2241_altaposentesp_salvar_tab'),

    url(r'^s2241-altaposentesp/cadastrar/$',
        s2241_altaposentesp_salvar_views.salvar,
        name='s2241_altaposentesp_cadastrar'),

    url(r'^s2241-altaposentesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_altaposentesp_salvar_views.salvar,
        name='s2241_altaposentesp_salvar_output'),

    url(r'^s2241-altaposentesp/(?P<output>[\w-]+)/$',
        s2241_altaposentesp_listar_views.listar,
        name='s2241_altaposentesp_output'),

    url(r'^s2241-altaposentesp-infoamb/apagar/(?P<pk>[0-9]+)/$',
        s2241_altaposentesp_infoamb_apagar_views.apagar,
        name='s2241_altaposentesp_infoamb_apagar'),

    url(r'^s2241-altaposentesp-infoamb/api/$',
        s2241_altaposentesp_infoamb_api_views.s2241altAposentEspinfoambList.as_view() ),

    url(r'^s2241-altaposentesp-infoamb/api/(?P<pk>[0-9]+)/$',
        s2241_altaposentesp_infoamb_api_views.s2241altAposentEspinfoambDetail.as_view() ),

    url(r'^s2241-altaposentesp-infoamb/$',
        s2241_altaposentesp_infoamb_listar_views.listar,
        name='s2241_altaposentesp_infoamb'),

    url(r'^s2241-altaposentesp-infoamb/salvar/(?P<pk>[0-9]+)/$',
        s2241_altaposentesp_infoamb_salvar_views.salvar,
        name='s2241_altaposentesp_infoamb_salvar'),

    url(r'^s2241-altaposentesp-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_altaposentesp_infoamb_salvar_views.salvar,
        name='s2241_altaposentesp_infoamb_salvar_tab'),

    url(r'^s2241-altaposentesp-infoamb/cadastrar/$',
        s2241_altaposentesp_infoamb_salvar_views.salvar,
        name='s2241_altaposentesp_infoamb_cadastrar'),

    url(r'^s2241-altaposentesp-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_altaposentesp_infoamb_salvar_views.salvar,
        name='s2241_altaposentesp_infoamb_salvar_output'),

    url(r'^s2241-altaposentesp-infoamb/(?P<output>[\w-]+)/$',
        s2241_altaposentesp_infoamb_listar_views.listar,
        name='s2241_altaposentesp_infoamb_output'),

    url(r'^s2241-altaposentesp-fatrisco/apagar/(?P<pk>[0-9]+)/$',
        s2241_altaposentesp_fatrisco_apagar_views.apagar,
        name='s2241_altaposentesp_fatrisco_apagar'),

    url(r'^s2241-altaposentesp-fatrisco/api/$',
        s2241_altaposentesp_fatrisco_api_views.s2241altAposentEspfatRiscoList.as_view() ),

    url(r'^s2241-altaposentesp-fatrisco/api/(?P<pk>[0-9]+)/$',
        s2241_altaposentesp_fatrisco_api_views.s2241altAposentEspfatRiscoDetail.as_view() ),

    url(r'^s2241-altaposentesp-fatrisco/$',
        s2241_altaposentesp_fatrisco_listar_views.listar,
        name='s2241_altaposentesp_fatrisco'),

    url(r'^s2241-altaposentesp-fatrisco/salvar/(?P<pk>[0-9]+)/$',
        s2241_altaposentesp_fatrisco_salvar_views.salvar,
        name='s2241_altaposentesp_fatrisco_salvar'),

    url(r'^s2241-altaposentesp-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_altaposentesp_fatrisco_salvar_views.salvar,
        name='s2241_altaposentesp_fatrisco_salvar_tab'),

    url(r'^s2241-altaposentesp-fatrisco/cadastrar/$',
        s2241_altaposentesp_fatrisco_salvar_views.salvar,
        name='s2241_altaposentesp_fatrisco_cadastrar'),

    url(r'^s2241-altaposentesp-fatrisco/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_altaposentesp_fatrisco_salvar_views.salvar,
        name='s2241_altaposentesp_fatrisco_salvar_output'),

    url(r'^s2241-altaposentesp-fatrisco/(?P<output>[\w-]+)/$',
        s2241_altaposentesp_fatrisco_listar_views.listar,
        name='s2241_altaposentesp_fatrisco_output'),

    url(r'^s2241-fimaposentesp/apagar/(?P<pk>[0-9]+)/$',
        s2241_fimaposentesp_apagar_views.apagar,
        name='s2241_fimaposentesp_apagar'),

    url(r'^s2241-fimaposentesp/api/$',
        s2241_fimaposentesp_api_views.s2241fimAposentEspList.as_view() ),

    url(r'^s2241-fimaposentesp/api/(?P<pk>[0-9]+)/$',
        s2241_fimaposentesp_api_views.s2241fimAposentEspDetail.as_view() ),

    url(r'^s2241-fimaposentesp/$',
        s2241_fimaposentesp_listar_views.listar,
        name='s2241_fimaposentesp'),

    url(r'^s2241-fimaposentesp/salvar/(?P<pk>[0-9]+)/$',
        s2241_fimaposentesp_salvar_views.salvar,
        name='s2241_fimaposentesp_salvar'),

    url(r'^s2241-fimaposentesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_fimaposentesp_salvar_views.salvar,
        name='s2241_fimaposentesp_salvar_tab'),

    url(r'^s2241-fimaposentesp/cadastrar/$',
        s2241_fimaposentesp_salvar_views.salvar,
        name='s2241_fimaposentesp_cadastrar'),

    url(r'^s2241-fimaposentesp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_fimaposentesp_salvar_views.salvar,
        name='s2241_fimaposentesp_salvar_output'),

    url(r'^s2241-fimaposentesp/(?P<output>[\w-]+)/$',
        s2241_fimaposentesp_listar_views.listar,
        name='s2241_fimaposentesp_output'),

    url(r'^s2241-fimaposentesp-infoamb/apagar/(?P<pk>[0-9]+)/$',
        s2241_fimaposentesp_infoamb_apagar_views.apagar,
        name='s2241_fimaposentesp_infoamb_apagar'),

    url(r'^s2241-fimaposentesp-infoamb/api/$',
        s2241_fimaposentesp_infoamb_api_views.s2241fimAposentEspinfoAmbList.as_view() ),

    url(r'^s2241-fimaposentesp-infoamb/api/(?P<pk>[0-9]+)/$',
        s2241_fimaposentesp_infoamb_api_views.s2241fimAposentEspinfoAmbDetail.as_view() ),

    url(r'^s2241-fimaposentesp-infoamb/$',
        s2241_fimaposentesp_infoamb_listar_views.listar,
        name='s2241_fimaposentesp_infoamb'),

    url(r'^s2241-fimaposentesp-infoamb/salvar/(?P<pk>[0-9]+)/$',
        s2241_fimaposentesp_infoamb_salvar_views.salvar,
        name='s2241_fimaposentesp_infoamb_salvar'),

    url(r'^s2241-fimaposentesp-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2241_fimaposentesp_infoamb_salvar_views.salvar,
        name='s2241_fimaposentesp_infoamb_salvar_tab'),

    url(r'^s2241-fimaposentesp-infoamb/cadastrar/$',
        s2241_fimaposentesp_infoamb_salvar_views.salvar,
        name='s2241_fimaposentesp_infoamb_cadastrar'),

    url(r'^s2241-fimaposentesp-infoamb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2241_fimaposentesp_infoamb_salvar_views.salvar,
        name='s2241_fimaposentesp_infoamb_salvar_output'),

    url(r'^s2241-fimaposentesp-infoamb/(?P<output>[\w-]+)/$',
        s2241_fimaposentesp_infoamb_listar_views.listar,
        name='s2241_fimaposentesp_infoamb_output'),


]