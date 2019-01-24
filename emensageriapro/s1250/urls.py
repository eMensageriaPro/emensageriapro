#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1250.views import s1250_ideprodutor as s1250_ideprodutor_views
from emensageriapro.s1250.views import s1250_infoprocj as s1250_infoprocj_views
from emensageriapro.s1250.views import s1250_infoprocjud as s1250_infoprocjud_views
from emensageriapro.s1250.views import s1250_nfs as s1250_nfs_views
from emensageriapro.s1250.views import s1250_tpaquis as s1250_tpaquis_views



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



url(r'^s1250-ideprodutor/apagar/(?P<hash>.*)/$', 
        s1250_ideprodutor_views.apagar, 
        name='s1250_ideprodutor_apagar'),

url(r'^s1250-ideprodutor/api/$',
            s1250_ideprodutor_views.s1250ideProdutorList.as_view() ),

        url(r'^s1250-ideprodutor/api/(?P<pk>[0-9]+)/$',
            s1250_ideprodutor_views.s1250ideProdutorDetail.as_view() ),

url(r'^s1250-ideprodutor/listar/(?P<hash>.*)/$', 
        s1250_ideprodutor_views.listar, 
        name='s1250_ideprodutor'),

url(r'^s1250-ideprodutor/salvar/(?P<hash>.*)/$', 
        s1250_ideprodutor_views.salvar, 
        name='s1250_ideprodutor_salvar'),



url(r'^s1250-infoprocj/apagar/(?P<hash>.*)/$', 
        s1250_infoprocj_views.apagar, 
        name='s1250_infoprocj_apagar'),

url(r'^s1250-infoprocj/api/$',
            s1250_infoprocj_views.s1250infoProcJList.as_view() ),

        url(r'^s1250-infoprocj/api/(?P<pk>[0-9]+)/$',
            s1250_infoprocj_views.s1250infoProcJDetail.as_view() ),

url(r'^s1250-infoprocj/listar/(?P<hash>.*)/$', 
        s1250_infoprocj_views.listar, 
        name='s1250_infoprocj'),

url(r'^s1250-infoprocj/salvar/(?P<hash>.*)/$', 
        s1250_infoprocj_views.salvar, 
        name='s1250_infoprocj_salvar'),



url(r'^s1250-infoprocjud/apagar/(?P<hash>.*)/$', 
        s1250_infoprocjud_views.apagar, 
        name='s1250_infoprocjud_apagar'),

url(r'^s1250-infoprocjud/api/$',
            s1250_infoprocjud_views.s1250infoProcJudList.as_view() ),

        url(r'^s1250-infoprocjud/api/(?P<pk>[0-9]+)/$',
            s1250_infoprocjud_views.s1250infoProcJudDetail.as_view() ),

url(r'^s1250-infoprocjud/listar/(?P<hash>.*)/$', 
        s1250_infoprocjud_views.listar, 
        name='s1250_infoprocjud'),

url(r'^s1250-infoprocjud/salvar/(?P<hash>.*)/$', 
        s1250_infoprocjud_views.salvar, 
        name='s1250_infoprocjud_salvar'),



url(r'^s1250-nfs/apagar/(?P<hash>.*)/$', 
        s1250_nfs_views.apagar, 
        name='s1250_nfs_apagar'),

url(r'^s1250-nfs/api/$',
            s1250_nfs_views.s1250nfsList.as_view() ),

        url(r'^s1250-nfs/api/(?P<pk>[0-9]+)/$',
            s1250_nfs_views.s1250nfsDetail.as_view() ),

url(r'^s1250-nfs/listar/(?P<hash>.*)/$', 
        s1250_nfs_views.listar, 
        name='s1250_nfs'),

url(r'^s1250-nfs/salvar/(?P<hash>.*)/$', 
        s1250_nfs_views.salvar, 
        name='s1250_nfs_salvar'),



url(r'^s1250-tpaquis/apagar/(?P<hash>.*)/$', 
        s1250_tpaquis_views.apagar, 
        name='s1250_tpaquis_apagar'),

url(r'^s1250-tpaquis/api/$',
            s1250_tpaquis_views.s1250tpAquisList.as_view() ),

        url(r'^s1250-tpaquis/api/(?P<pk>[0-9]+)/$',
            s1250_tpaquis_views.s1250tpAquisDetail.as_view() ),

url(r'^s1250-tpaquis/listar/(?P<hash>.*)/$', 
        s1250_tpaquis_views.listar, 
        name='s1250_tpaquis'),

url(r'^s1250-tpaquis/salvar/(?P<hash>.*)/$', 
        s1250_tpaquis_views.salvar, 
        name='s1250_tpaquis_salvar'),





]