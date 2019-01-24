#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2010.views import r2010_infoprocretad as r2010_infoprocretad_views
from emensageriapro.r2010.views import r2010_infoprocretpr as r2010_infoprocretpr_views
from emensageriapro.r2010.views import r2010_infotpserv as r2010_infotpserv_views
from emensageriapro.r2010.views import r2010_nfs as r2010_nfs_views



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



url(r'^r2010-infoprocretad/apagar/(?P<hash>.*)/$', 
        r2010_infoprocretad_views.apagar, 
        name='r2010_infoprocretad_apagar'),

url(r'^r2010-infoprocretad/api/$',
            r2010_infoprocretad_views.r2010infoProcRetAdList.as_view() ),

        url(r'^r2010-infoprocretad/api/(?P<pk>[0-9]+)/$',
            r2010_infoprocretad_views.r2010infoProcRetAdDetail.as_view() ),

url(r'^r2010-infoprocretad/listar/(?P<hash>.*)/$', 
        r2010_infoprocretad_views.listar, 
        name='r2010_infoprocretad'),

url(r'^r2010-infoprocretad/salvar/(?P<hash>.*)/$', 
        r2010_infoprocretad_views.salvar, 
        name='r2010_infoprocretad_salvar'),



url(r'^r2010-infoprocretpr/apagar/(?P<hash>.*)/$', 
        r2010_infoprocretpr_views.apagar, 
        name='r2010_infoprocretpr_apagar'),

url(r'^r2010-infoprocretpr/api/$',
            r2010_infoprocretpr_views.r2010infoProcRetPrList.as_view() ),

        url(r'^r2010-infoprocretpr/api/(?P<pk>[0-9]+)/$',
            r2010_infoprocretpr_views.r2010infoProcRetPrDetail.as_view() ),

url(r'^r2010-infoprocretpr/listar/(?P<hash>.*)/$', 
        r2010_infoprocretpr_views.listar, 
        name='r2010_infoprocretpr'),

url(r'^r2010-infoprocretpr/salvar/(?P<hash>.*)/$', 
        r2010_infoprocretpr_views.salvar, 
        name='r2010_infoprocretpr_salvar'),



url(r'^r2010-infotpserv/apagar/(?P<hash>.*)/$', 
        r2010_infotpserv_views.apagar, 
        name='r2010_infotpserv_apagar'),

url(r'^r2010-infotpserv/api/$',
            r2010_infotpserv_views.r2010infoTpServList.as_view() ),

        url(r'^r2010-infotpserv/api/(?P<pk>[0-9]+)/$',
            r2010_infotpserv_views.r2010infoTpServDetail.as_view() ),

url(r'^r2010-infotpserv/listar/(?P<hash>.*)/$', 
        r2010_infotpserv_views.listar, 
        name='r2010_infotpserv'),

url(r'^r2010-infotpserv/salvar/(?P<hash>.*)/$', 
        r2010_infotpserv_views.salvar, 
        name='r2010_infotpserv_salvar'),



url(r'^r2010-nfs/apagar/(?P<hash>.*)/$', 
        r2010_nfs_views.apagar, 
        name='r2010_nfs_apagar'),

url(r'^r2010-nfs/api/$',
            r2010_nfs_views.r2010nfsList.as_view() ),

        url(r'^r2010-nfs/api/(?P<pk>[0-9]+)/$',
            r2010_nfs_views.r2010nfsDetail.as_view() ),

url(r'^r2010-nfs/listar/(?P<hash>.*)/$', 
        r2010_nfs_views.listar, 
        name='r2010_nfs'),

url(r'^r2010-nfs/salvar/(?P<hash>.*)/$', 
        r2010_nfs_views.salvar, 
        name='r2010_nfs_salvar'),





]