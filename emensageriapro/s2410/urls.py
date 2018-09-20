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



url(r'^s2410-infopenmorte/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2410.views.s2410_infopenmorte.apagar', 
        name='s2410_infopenmorte_apagar'),

url(r'^s2410-infopenmorte/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2410.views.s2410_infopenmorte.listar', 
        name='s2410_infopenmorte'),

url(r'^s2410-infopenmorte/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2410.views.s2410_infopenmorte.salvar', 
        name='s2410_infopenmorte_salvar'),



url(r'^s2410-instpenmorte/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2410.views.s2410_instpenmorte.apagar', 
        name='s2410_instpenmorte_apagar'),

url(r'^s2410-instpenmorte/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2410.views.s2410_instpenmorte.listar', 
        name='s2410_instpenmorte'),

url(r'^s2410-instpenmorte/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2410.views.s2410_instpenmorte.salvar', 
        name='s2410_instpenmorte_salvar'),



url(r'^s2410-homologtc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2410.views.s2410_homologtc.apagar', 
        name='s2410_homologtc_apagar'),

url(r'^s2410-homologtc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2410.views.s2410_homologtc.listar', 
        name='s2410_homologtc'),

url(r'^s2410-homologtc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2410.views.s2410_homologtc.salvar', 
        name='s2410_homologtc_salvar'),





)