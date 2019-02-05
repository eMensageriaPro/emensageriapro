#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2245.views import s2245_ideprofresp as s2245_ideprofresp_views
from emensageriapro.s2245.views import s2245_infocomplem as s2245_infocomplem_views



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



url(r'^s2245-ideprofresp/apagar/(?P<hash>.*)/$', 
        s2245_ideprofresp_views.apagar, 
        name='s2245_ideprofresp_apagar'),

url(r'^s2245-ideprofresp/api/$',
            s2245_ideprofresp_views.s2245ideProfRespList.as_view() ),

        url(r'^s2245-ideprofresp/api/(?P<pk>[0-9]+)/$',
            s2245_ideprofresp_views.s2245ideProfRespDetail.as_view() ),

url(r'^s2245-ideprofresp/listar/(?P<hash>.*)/$', 
        s2245_ideprofresp_views.listar, 
        name='s2245_ideprofresp'),

url(r'^s2245-ideprofresp/salvar/(?P<hash>.*)/$', 
        s2245_ideprofresp_views.salvar, 
        name='s2245_ideprofresp_salvar'),



url(r'^s2245-infocomplem/apagar/(?P<hash>.*)/$', 
        s2245_infocomplem_views.apagar, 
        name='s2245_infocomplem_apagar'),

url(r'^s2245-infocomplem/api/$',
            s2245_infocomplem_views.s2245infoComplemList.as_view() ),

        url(r'^s2245-infocomplem/api/(?P<pk>[0-9]+)/$',
            s2245_infocomplem_views.s2245infoComplemDetail.as_view() ),

url(r'^s2245-infocomplem/listar/(?P<hash>.*)/$', 
        s2245_infocomplem_views.listar, 
        name='s2245_infocomplem'),

url(r'^s2245-infocomplem/salvar/(?P<hash>.*)/$', 
        s2245_infocomplem_views.salvar, 
        name='s2245_infocomplem_salvar'),





]