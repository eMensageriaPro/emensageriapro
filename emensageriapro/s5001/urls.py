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



url(r'^s5001-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_procjudtrab.apagar', 
        name='s5001_procjudtrab_apagar'),

url(r'^s5001-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_procjudtrab.listar', 
        name='s5001_procjudtrab'),

url(r'^s5001-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_procjudtrab.salvar', 
        name='s5001_procjudtrab_salvar'),



url(r'^s5001-infocpcalc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocpcalc.apagar', 
        name='s5001_infocpcalc_apagar'),

url(r'^s5001-infocpcalc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocpcalc.listar', 
        name='s5001_infocpcalc'),

url(r'^s5001-infocpcalc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocpcalc.salvar', 
        name='s5001_infocpcalc_salvar'),



url(r'^s5001-infocp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocp.apagar', 
        name='s5001_infocp_apagar'),

url(r'^s5001-infocp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocp.listar', 
        name='s5001_infocp'),

url(r'^s5001-infocp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocp.salvar', 
        name='s5001_infocp_salvar'),



url(r'^s5001-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_ideestablot.apagar', 
        name='s5001_ideestablot_apagar'),

url(r'^s5001-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_ideestablot.listar', 
        name='s5001_ideestablot'),

url(r'^s5001-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_ideestablot.salvar', 
        name='s5001_ideestablot_salvar'),



url(r'^s5001-infocategincid/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocategincid.apagar', 
        name='s5001_infocategincid_apagar'),

url(r'^s5001-infocategincid/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocategincid.listar', 
        name='s5001_infocategincid'),

url(r'^s5001-infocategincid/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infocategincid.salvar', 
        name='s5001_infocategincid_salvar'),



url(r'^s5001-infobasecs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infobasecs.apagar', 
        name='s5001_infobasecs_apagar'),

url(r'^s5001-infobasecs/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infobasecs.listar', 
        name='s5001_infobasecs'),

url(r'^s5001-infobasecs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_infobasecs.salvar', 
        name='s5001_infobasecs_salvar'),



url(r'^s5001-calcterc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_calcterc.apagar', 
        name='s5001_calcterc_apagar'),

url(r'^s5001-calcterc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_calcterc.listar', 
        name='s5001_calcterc'),

url(r'^s5001-calcterc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5001.views.s5001_calcterc.salvar', 
        name='s5001_calcterc_salvar'),





)