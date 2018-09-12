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



url(r'^s2400-brasil/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_brasil.apagar', 
        name='s2400_brasil_apagar'),

url(r'^s2400-brasil/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_brasil.listar', 
        name='s2400_brasil'),

url(r'^s2400-brasil/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_brasil.salvar', 
        name='s2400_brasil_salvar'),



url(r'^s2400-exterior/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_exterior.apagar', 
        name='s2400_exterior_apagar'),

url(r'^s2400-exterior/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_exterior.listar', 
        name='s2400_exterior'),

url(r'^s2400-exterior/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_exterior.salvar', 
        name='s2400_exterior_salvar'),



url(r'^s2400-inibeneficio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_inibeneficio.apagar', 
        name='s2400_inibeneficio_apagar'),

url(r'^s2400-inibeneficio/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_inibeneficio.listar', 
        name='s2400_inibeneficio'),

url(r'^s2400-inibeneficio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_inibeneficio.salvar', 
        name='s2400_inibeneficio_salvar'),



url(r'^s2400-inibeneficio-infopenmorte/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_inibeneficio_infopenmorte.apagar', 
        name='s2400_inibeneficio_infopenmorte_apagar'),

url(r'^s2400-inibeneficio-infopenmorte/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_inibeneficio_infopenmorte.listar', 
        name='s2400_inibeneficio_infopenmorte'),

url(r'^s2400-inibeneficio-infopenmorte/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_inibeneficio_infopenmorte.salvar', 
        name='s2400_inibeneficio_infopenmorte_salvar'),



url(r'^s2400-altbeneficio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_altbeneficio.apagar', 
        name='s2400_altbeneficio_apagar'),

url(r'^s2400-altbeneficio/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_altbeneficio.listar', 
        name='s2400_altbeneficio'),

url(r'^s2400-altbeneficio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_altbeneficio.salvar', 
        name='s2400_altbeneficio_salvar'),



url(r'^s2400-altbeneficio-infopenmorte/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_altbeneficio_infopenmorte.apagar', 
        name='s2400_altbeneficio_infopenmorte_apagar'),

url(r'^s2400-altbeneficio-infopenmorte/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_altbeneficio_infopenmorte.listar', 
        name='s2400_altbeneficio_infopenmorte'),

url(r'^s2400-altbeneficio-infopenmorte/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_altbeneficio_infopenmorte.salvar', 
        name='s2400_altbeneficio_infopenmorte_salvar'),



url(r'^s2400-fimbeneficio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_fimbeneficio.apagar', 
        name='s2400_fimbeneficio_apagar'),

url(r'^s2400-fimbeneficio/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_fimbeneficio.listar', 
        name='s2400_fimbeneficio'),

url(r'^s2400-fimbeneficio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_fimbeneficio.salvar', 
        name='s2400_fimbeneficio_salvar'),





)