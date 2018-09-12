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



url(r'^r5011-regocorrs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_regocorrs.apagar', 
        name='r5011_regocorrs_apagar'),

url(r'^r5011-regocorrs/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_regocorrs.listar', 
        name='r5011_regocorrs'),

url(r'^r5011-regocorrs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_regocorrs.salvar', 
        name='r5011_regocorrs_salvar'),



url(r'^r5011-infototalcontrib/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infototalcontrib.apagar', 
        name='r5011_infototalcontrib_apagar'),

url(r'^r5011-infototalcontrib/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infototalcontrib.listar', 
        name='r5011_infototalcontrib'),

url(r'^r5011-infototalcontrib/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infototalcontrib.salvar', 
        name='r5011_infototalcontrib_salvar'),



url(r'^r5011-rtom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rtom.apagar', 
        name='r5011_rtom_apagar'),

url(r'^r5011-rtom/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rtom.listar', 
        name='r5011_rtom'),

url(r'^r5011-rtom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rtom.salvar', 
        name='r5011_rtom_salvar'),



url(r'^r5011-infocrtom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infocrtom.apagar', 
        name='r5011_infocrtom_apagar'),

url(r'^r5011-infocrtom/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infocrtom.listar', 
        name='r5011_infocrtom'),

url(r'^r5011-infocrtom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infocrtom.salvar', 
        name='r5011_infocrtom_salvar'),



url(r'^r5011-rprest/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rprest.apagar', 
        name='r5011_rprest_apagar'),

url(r'^r5011-rprest/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rprest.listar', 
        name='r5011_rprest'),

url(r'^r5011-rprest/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rprest.salvar', 
        name='r5011_rprest_salvar'),



url(r'^r5011-rrecrepad/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rrecrepad.apagar', 
        name='r5011_rrecrepad_apagar'),

url(r'^r5011-rrecrepad/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rrecrepad.listar', 
        name='r5011_rrecrepad'),

url(r'^r5011-rrecrepad/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rrecrepad.salvar', 
        name='r5011_rrecrepad_salvar'),



url(r'^r5011-rcoml/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcoml.apagar', 
        name='r5011_rcoml_apagar'),

url(r'^r5011-rcoml/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcoml.listar', 
        name='r5011_rcoml'),

url(r'^r5011-rcoml/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcoml.salvar', 
        name='r5011_rcoml_salvar'),



url(r'^r5011-rcprb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcprb.apagar', 
        name='r5011_rcprb_apagar'),

url(r'^r5011-rcprb/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcprb.listar', 
        name='r5011_rcprb'),

url(r'^r5011-rcprb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcprb.salvar', 
        name='r5011_rcprb_salvar'),





)