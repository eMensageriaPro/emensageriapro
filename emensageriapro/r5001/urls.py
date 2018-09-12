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



url(r'^r5001-regocorrs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_regocorrs.apagar', 
        name='r5001_regocorrs_apagar'),

url(r'^r5001-regocorrs/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_regocorrs.listar', 
        name='r5001_regocorrs'),

url(r'^r5001-regocorrs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_regocorrs.salvar', 
        name='r5001_regocorrs_salvar'),



url(r'^r5001-infototal/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_infototal.apagar', 
        name='r5001_infototal_apagar'),

url(r'^r5001-infototal/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_infototal.listar', 
        name='r5001_infototal'),

url(r'^r5001-infototal/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_infototal.salvar', 
        name='r5001_infototal_salvar'),



url(r'^r5001-rtom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rtom.apagar', 
        name='r5001_rtom_apagar'),

url(r'^r5001-rtom/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rtom.listar', 
        name='r5001_rtom'),

url(r'^r5001-rtom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rtom.salvar', 
        name='r5001_rtom_salvar'),



url(r'^r5001-infocrtom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_infocrtom.apagar', 
        name='r5001_infocrtom_apagar'),

url(r'^r5001-infocrtom/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_infocrtom.listar', 
        name='r5001_infocrtom'),

url(r'^r5001-infocrtom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_infocrtom.salvar', 
        name='r5001_infocrtom_salvar'),



url(r'^r5001-rprest/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rprest.apagar', 
        name='r5001_rprest_apagar'),

url(r'^r5001-rprest/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rprest.listar', 
        name='r5001_rprest'),

url(r'^r5001-rprest/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rprest.salvar', 
        name='r5001_rprest_salvar'),



url(r'^r5001-rrecrepad/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rrecrepad.apagar', 
        name='r5001_rrecrepad_apagar'),

url(r'^r5001-rrecrepad/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rrecrepad.listar', 
        name='r5001_rrecrepad'),

url(r'^r5001-rrecrepad/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rrecrepad.salvar', 
        name='r5001_rrecrepad_salvar'),



url(r'^r5001-rcoml/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rcoml.apagar', 
        name='r5001_rcoml_apagar'),

url(r'^r5001-rcoml/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rcoml.listar', 
        name='r5001_rcoml'),

url(r'^r5001-rcoml/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rcoml.salvar', 
        name='r5001_rcoml_salvar'),



url(r'^r5001-rcprb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rcprb.apagar', 
        name='r5001_rcprb_apagar'),

url(r'^r5001-rcprb/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rcprb.listar', 
        name='r5001_rcprb'),

url(r'^r5001-rcprb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rcprb.salvar', 
        name='r5001_rcprb_salvar'),



url(r'^r5001-rrecespetdesp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rrecespetdesp.apagar', 
        name='r5001_rrecespetdesp_apagar'),

url(r'^r5001-rrecespetdesp/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rrecespetdesp.listar', 
        name='r5001_rrecespetdesp'),

url(r'^r5001-rrecespetdesp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5001.views.r5001_rrecespetdesp.salvar', 
        name='r5001_rrecespetdesp_salvar'),





)