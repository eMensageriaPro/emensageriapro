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



url(r'^r2060-tipocod/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipocod.apagar', 
        name='r2060_tipocod_apagar'),

url(r'^r2060-tipocod/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipocod.listar', 
        name='r2060_tipocod'),

url(r'^r2060-tipocod/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipocod.salvar', 
        name='r2060_tipocod_salvar'),



url(r'^r2060-tipoajuste/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipoajuste.apagar', 
        name='r2060_tipoajuste_apagar'),

url(r'^r2060-tipoajuste/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipoajuste.listar', 
        name='r2060_tipoajuste'),

url(r'^r2060-tipoajuste/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_tipoajuste.salvar', 
        name='r2060_tipoajuste_salvar'),



url(r'^r2060-infoproc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_infoproc.apagar', 
        name='r2060_infoproc_apagar'),

url(r'^r2060-infoproc/listar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_infoproc.listar', 
        name='r2060_infoproc'),

url(r'^r2060-infoproc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r2060.views.r2060_infoproc.salvar', 
        name='r2060_infoproc_salvar'),





)