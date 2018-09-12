#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns = patterns('',
    # Examples:



url(r'^r2020-nfs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_nfs.apagar', 
        name='r2020_nfs_apagar'),

url(r'^r2020-nfs/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_nfs.listar', 
        name='r2020_nfs'),

url(r'^r2020-nfs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_nfs.salvar', 
        name='r2020_nfs_salvar'),



url(r'^r2020-infotpserv/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infotpserv.apagar', 
        name='r2020_infotpserv_apagar'),

url(r'^r2020-infotpserv/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infotpserv.listar', 
        name='r2020_infotpserv'),

url(r'^r2020-infotpserv/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infotpserv.salvar', 
        name='r2020_infotpserv_salvar'),



url(r'^r2020-infoprocretpr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretpr.apagar', 
        name='r2020_infoprocretpr_apagar'),

url(r'^r2020-infoprocretpr/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretpr.listar', 
        name='r2020_infoprocretpr'),

url(r'^r2020-infoprocretpr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretpr.salvar', 
        name='r2020_infoprocretpr_salvar'),



url(r'^r2020-infoprocretad/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretad.apagar', 
        name='r2020_infoprocretad_apagar'),

url(r'^r2020-infoprocretad/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretad.listar', 
        name='r2020_infoprocretad'),

url(r'^r2020-infoprocretad/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2020.views.r2020_infoprocretad.salvar', 
        name='r2020_infoprocretad_salvar'),





)