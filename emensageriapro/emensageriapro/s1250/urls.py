#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s1250.views import s1250_tpaquis_apagar as s1250_tpaquis_apagar_views
from emensageriapro.s1250.views import s1250_tpaquis_listar as s1250_tpaquis_listar_views
from emensageriapro.s1250.views import s1250_tpaquis_salvar as s1250_tpaquis_salvar_views
from emensageriapro.s1250.views import s1250_tpaquis_api as s1250_tpaquis_api_views
from emensageriapro.s1250.views import s1250_ideprodutor_apagar as s1250_ideprodutor_apagar_views
from emensageriapro.s1250.views import s1250_ideprodutor_listar as s1250_ideprodutor_listar_views
from emensageriapro.s1250.views import s1250_ideprodutor_salvar as s1250_ideprodutor_salvar_views
from emensageriapro.s1250.views import s1250_ideprodutor_api as s1250_ideprodutor_api_views
from emensageriapro.s1250.views import s1250_nfs_apagar as s1250_nfs_apagar_views
from emensageriapro.s1250.views import s1250_nfs_listar as s1250_nfs_listar_views
from emensageriapro.s1250.views import s1250_nfs_salvar as s1250_nfs_salvar_views
from emensageriapro.s1250.views import s1250_nfs_api as s1250_nfs_api_views
from emensageriapro.s1250.views import s1250_infoprocjud_apagar as s1250_infoprocjud_apagar_views
from emensageriapro.s1250.views import s1250_infoprocjud_listar as s1250_infoprocjud_listar_views
from emensageriapro.s1250.views import s1250_infoprocjud_salvar as s1250_infoprocjud_salvar_views
from emensageriapro.s1250.views import s1250_infoprocjud_api as s1250_infoprocjud_api_views
from emensageriapro.s1250.views import s1250_infoprocj_apagar as s1250_infoprocj_apagar_views
from emensageriapro.s1250.views import s1250_infoprocj_listar as s1250_infoprocj_listar_views
from emensageriapro.s1250.views import s1250_infoprocj_salvar as s1250_infoprocj_salvar_views
from emensageriapro.s1250.views import s1250_infoprocj_api as s1250_infoprocj_api_views


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


    url(r'^s1250-tpaquis/apagar/(?P<pk>[0-9]+)/$',
        s1250_tpaquis_apagar_views.apagar,
        name='s1250_tpaquis_apagar'),

    url(r'^s1250-tpaquis/api/$',
        s1250_tpaquis_api_views.s1250tpAquisList.as_view() ),

    url(r'^s1250-tpaquis/api/(?P<pk>[0-9]+)/$',
        s1250_tpaquis_api_views.s1250tpAquisDetail.as_view() ),

    url(r'^s1250-tpaquis/$',
        s1250_tpaquis_listar_views.listar,
        name='s1250_tpaquis'),

    url(r'^s1250-tpaquis/salvar/(?P<pk>[0-9]+)/$',
        s1250_tpaquis_salvar_views.salvar,
        name='s1250_tpaquis_salvar'),

    url(r'^s1250-tpaquis/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1250_tpaquis_salvar_views.salvar,
        name='s1250_tpaquis_salvar_tab'),

    url(r'^s1250-tpaquis/cadastrar/$',
        s1250_tpaquis_salvar_views.salvar,
        name='s1250_tpaquis_cadastrar'),

    url(r'^s1250-tpaquis/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1250_tpaquis_salvar_views.salvar,
        name='s1250_tpaquis_salvar_output'),

    url(r'^s1250-tpaquis/(?P<output>[\w-]+)/$',
        s1250_tpaquis_listar_views.listar,
        name='s1250_tpaquis_output'),

    url(r'^s1250-ideprodutor/apagar/(?P<pk>[0-9]+)/$',
        s1250_ideprodutor_apagar_views.apagar,
        name='s1250_ideprodutor_apagar'),

    url(r'^s1250-ideprodutor/api/$',
        s1250_ideprodutor_api_views.s1250ideProdutorList.as_view() ),

    url(r'^s1250-ideprodutor/api/(?P<pk>[0-9]+)/$',
        s1250_ideprodutor_api_views.s1250ideProdutorDetail.as_view() ),

    url(r'^s1250-ideprodutor/$',
        s1250_ideprodutor_listar_views.listar,
        name='s1250_ideprodutor'),

    url(r'^s1250-ideprodutor/salvar/(?P<pk>[0-9]+)/$',
        s1250_ideprodutor_salvar_views.salvar,
        name='s1250_ideprodutor_salvar'),

    url(r'^s1250-ideprodutor/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1250_ideprodutor_salvar_views.salvar,
        name='s1250_ideprodutor_salvar_tab'),

    url(r'^s1250-ideprodutor/cadastrar/$',
        s1250_ideprodutor_salvar_views.salvar,
        name='s1250_ideprodutor_cadastrar'),

    url(r'^s1250-ideprodutor/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1250_ideprodutor_salvar_views.salvar,
        name='s1250_ideprodutor_salvar_output'),

    url(r'^s1250-ideprodutor/(?P<output>[\w-]+)/$',
        s1250_ideprodutor_listar_views.listar,
        name='s1250_ideprodutor_output'),

    url(r'^s1250-nfs/apagar/(?P<pk>[0-9]+)/$',
        s1250_nfs_apagar_views.apagar,
        name='s1250_nfs_apagar'),

    url(r'^s1250-nfs/api/$',
        s1250_nfs_api_views.s1250nfsList.as_view() ),

    url(r'^s1250-nfs/api/(?P<pk>[0-9]+)/$',
        s1250_nfs_api_views.s1250nfsDetail.as_view() ),

    url(r'^s1250-nfs/$',
        s1250_nfs_listar_views.listar,
        name='s1250_nfs'),

    url(r'^s1250-nfs/salvar/(?P<pk>[0-9]+)/$',
        s1250_nfs_salvar_views.salvar,
        name='s1250_nfs_salvar'),

    url(r'^s1250-nfs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1250_nfs_salvar_views.salvar,
        name='s1250_nfs_salvar_tab'),

    url(r'^s1250-nfs/cadastrar/$',
        s1250_nfs_salvar_views.salvar,
        name='s1250_nfs_cadastrar'),

    url(r'^s1250-nfs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1250_nfs_salvar_views.salvar,
        name='s1250_nfs_salvar_output'),

    url(r'^s1250-nfs/(?P<output>[\w-]+)/$',
        s1250_nfs_listar_views.listar,
        name='s1250_nfs_output'),

    url(r'^s1250-infoprocjud/apagar/(?P<pk>[0-9]+)/$',
        s1250_infoprocjud_apagar_views.apagar,
        name='s1250_infoprocjud_apagar'),

    url(r'^s1250-infoprocjud/api/$',
        s1250_infoprocjud_api_views.s1250infoProcJudList.as_view() ),

    url(r'^s1250-infoprocjud/api/(?P<pk>[0-9]+)/$',
        s1250_infoprocjud_api_views.s1250infoProcJudDetail.as_view() ),

    url(r'^s1250-infoprocjud/$',
        s1250_infoprocjud_listar_views.listar,
        name='s1250_infoprocjud'),

    url(r'^s1250-infoprocjud/salvar/(?P<pk>[0-9]+)/$',
        s1250_infoprocjud_salvar_views.salvar,
        name='s1250_infoprocjud_salvar'),

    url(r'^s1250-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1250_infoprocjud_salvar_views.salvar,
        name='s1250_infoprocjud_salvar_tab'),

    url(r'^s1250-infoprocjud/cadastrar/$',
        s1250_infoprocjud_salvar_views.salvar,
        name='s1250_infoprocjud_cadastrar'),

    url(r'^s1250-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1250_infoprocjud_salvar_views.salvar,
        name='s1250_infoprocjud_salvar_output'),

    url(r'^s1250-infoprocjud/(?P<output>[\w-]+)/$',
        s1250_infoprocjud_listar_views.listar,
        name='s1250_infoprocjud_output'),

    url(r'^s1250-infoprocj/apagar/(?P<pk>[0-9]+)/$',
        s1250_infoprocj_apagar_views.apagar,
        name='s1250_infoprocj_apagar'),

    url(r'^s1250-infoprocj/api/$',
        s1250_infoprocj_api_views.s1250infoProcJList.as_view() ),

    url(r'^s1250-infoprocj/api/(?P<pk>[0-9]+)/$',
        s1250_infoprocj_api_views.s1250infoProcJDetail.as_view() ),

    url(r'^s1250-infoprocj/$',
        s1250_infoprocj_listar_views.listar,
        name='s1250_infoprocj'),

    url(r'^s1250-infoprocj/salvar/(?P<pk>[0-9]+)/$',
        s1250_infoprocj_salvar_views.salvar,
        name='s1250_infoprocj_salvar'),

    url(r'^s1250-infoprocj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s1250_infoprocj_salvar_views.salvar,
        name='s1250_infoprocj_salvar_tab'),

    url(r'^s1250-infoprocj/cadastrar/$',
        s1250_infoprocj_salvar_views.salvar,
        name='s1250_infoprocj_cadastrar'),

    url(r'^s1250-infoprocj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s1250_infoprocj_salvar_views.salvar,
        name='s1250_infoprocj_salvar_output'),

    url(r'^s1250-infoprocj/(?P<output>[\w-]+)/$',
        s1250_infoprocj_listar_views.listar,
        name='s1250_infoprocj_output'),


]