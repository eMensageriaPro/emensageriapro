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



url(r'^s1260-tpcomerc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_tpcomerc.apagar', 
        name='s1260_tpcomerc_apagar'),

url(r'^s1260-tpcomerc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_tpcomerc.listar', 
        name='s1260_tpcomerc'),

url(r'^s1260-tpcomerc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_tpcomerc.salvar', 
        name='s1260_tpcomerc_salvar'),



url(r'^s1260-ideadquir/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_ideadquir.apagar', 
        name='s1260_ideadquir_apagar'),

url(r'^s1260-ideadquir/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_ideadquir.listar', 
        name='s1260_ideadquir'),

url(r'^s1260-ideadquir/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_ideadquir.salvar', 
        name='s1260_ideadquir_salvar'),



url(r'^s1260-nfs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_nfs.apagar', 
        name='s1260_nfs_apagar'),

url(r'^s1260-nfs/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_nfs.listar', 
        name='s1260_nfs'),

url(r'^s1260-nfs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_nfs.salvar', 
        name='s1260_nfs_salvar'),



url(r'^s1260-infoprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_infoprocjud.apagar', 
        name='s1260_infoprocjud_apagar'),

url(r'^s1260-infoprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_infoprocjud.listar', 
        name='s1260_infoprocjud'),

url(r'^s1260-infoprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1260.views.s1260_infoprocjud.salvar', 
        name='s1260_infoprocjud_salvar'),





)