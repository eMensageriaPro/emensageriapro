#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2210.views import s2210_idelocalacid as s2210_idelocalacid_views
from emensageriapro.s2210.views import s2210_parteatingida as s2210_parteatingida_views
from emensageriapro.s2210.views import s2210_agentecausador as s2210_agentecausador_views
from emensageriapro.s2210.views import s2210_atestado as s2210_atestado_views
from emensageriapro.s2210.views import s2210_catorigem as s2210_catorigem_views



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



url(r'^s2210-idelocalacid/apagar/(?P<hash>.*)/$', 
        s2210_idelocalacid_views.apagar, 
        name='s2210_idelocalacid_apagar'),

url(r'^s2210-idelocalacid/listar/(?P<hash>.*)/$', 
        s2210_idelocalacid_views.listar, 
        name='s2210_idelocalacid'),

url(r'^s2210-idelocalacid/salvar/(?P<hash>.*)/$', 
        s2210_idelocalacid_views.salvar, 
        name='s2210_idelocalacid_salvar'),



url(r'^s2210-parteatingida/apagar/(?P<hash>.*)/$', 
        s2210_parteatingida_views.apagar, 
        name='s2210_parteatingida_apagar'),

url(r'^s2210-parteatingida/listar/(?P<hash>.*)/$', 
        s2210_parteatingida_views.listar, 
        name='s2210_parteatingida'),

url(r'^s2210-parteatingida/salvar/(?P<hash>.*)/$', 
        s2210_parteatingida_views.salvar, 
        name='s2210_parteatingida_salvar'),



url(r'^s2210-agentecausador/apagar/(?P<hash>.*)/$', 
        s2210_agentecausador_views.apagar, 
        name='s2210_agentecausador_apagar'),

url(r'^s2210-agentecausador/listar/(?P<hash>.*)/$', 
        s2210_agentecausador_views.listar, 
        name='s2210_agentecausador'),

url(r'^s2210-agentecausador/salvar/(?P<hash>.*)/$', 
        s2210_agentecausador_views.salvar, 
        name='s2210_agentecausador_salvar'),



url(r'^s2210-atestado/apagar/(?P<hash>.*)/$', 
        s2210_atestado_views.apagar, 
        name='s2210_atestado_apagar'),

url(r'^s2210-atestado/listar/(?P<hash>.*)/$', 
        s2210_atestado_views.listar, 
        name='s2210_atestado'),

url(r'^s2210-atestado/salvar/(?P<hash>.*)/$', 
        s2210_atestado_views.salvar, 
        name='s2210_atestado_salvar'),



url(r'^s2210-catorigem/apagar/(?P<hash>.*)/$', 
        s2210_catorigem_views.apagar, 
        name='s2210_catorigem_apagar'),

url(r'^s2210-catorigem/listar/(?P<hash>.*)/$', 
        s2210_catorigem_views.listar, 
        name='s2210_catorigem'),

url(r'^s2210-catorigem/salvar/(?P<hash>.*)/$', 
        s2210_catorigem_views.salvar, 
        name='s2210_catorigem_salvar'),





]