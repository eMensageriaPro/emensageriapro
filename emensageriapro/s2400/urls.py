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



url(r'^s2400-endereco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_endereco.apagar', 
        name='s2400_endereco_apagar'),

url(r'^s2400-endereco/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_endereco.listar', 
        name='s2400_endereco'),

url(r'^s2400-endereco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_endereco.salvar', 
        name='s2400_endereco_salvar'),



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



url(r'^s2400-dependente/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_dependente.apagar', 
        name='s2400_dependente_apagar'),

url(r'^s2400-dependente/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_dependente.listar', 
        name='s2400_dependente'),

url(r'^s2400-dependente/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2400.views.s2400_dependente.salvar', 
        name='s2400_dependente_salvar'),





)