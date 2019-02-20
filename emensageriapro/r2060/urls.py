#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2060.views import r2060_infoproc as r2060_infoproc_views
from emensageriapro.r2060.views import r2060_tipoajuste as r2060_tipoajuste_views
from emensageriapro.r2060.views import r2060_tipocod as r2060_tipocod_views



"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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



url(r'^r2060-infoproc/apagar/(?P<hash>.*)/$', 
        r2060_infoproc_views.apagar, 
        name='r2060_infoproc_apagar'),

url(r'^r2060-infoproc/api/$',
            r2060_infoproc_views.r2060infoProcList.as_view() ),

        url(r'^r2060-infoproc/api/(?P<pk>[0-9]+)/$',
            r2060_infoproc_views.r2060infoProcDetail.as_view() ),

url(r'^r2060-infoproc/listar/(?P<hash>.*)/$', 
        r2060_infoproc_views.listar, 
        name='r2060_infoproc'),

url(r'^r2060-infoproc/salvar/(?P<hash>.*)/$', 
        r2060_infoproc_views.salvar, 
        name='r2060_infoproc_salvar'),



url(r'^r2060-tipoajuste/apagar/(?P<hash>.*)/$', 
        r2060_tipoajuste_views.apagar, 
        name='r2060_tipoajuste_apagar'),

url(r'^r2060-tipoajuste/api/$',
            r2060_tipoajuste_views.r2060tipoAjusteList.as_view() ),

        url(r'^r2060-tipoajuste/api/(?P<pk>[0-9]+)/$',
            r2060_tipoajuste_views.r2060tipoAjusteDetail.as_view() ),

url(r'^r2060-tipoajuste/listar/(?P<hash>.*)/$', 
        r2060_tipoajuste_views.listar, 
        name='r2060_tipoajuste'),

url(r'^r2060-tipoajuste/salvar/(?P<hash>.*)/$', 
        r2060_tipoajuste_views.salvar, 
        name='r2060_tipoajuste_salvar'),



url(r'^r2060-tipocod/apagar/(?P<hash>.*)/$', 
        r2060_tipocod_views.apagar, 
        name='r2060_tipocod_apagar'),

url(r'^r2060-tipocod/api/$',
            r2060_tipocod_views.r2060tipoCodList.as_view() ),

        url(r'^r2060-tipocod/api/(?P<pk>[0-9]+)/$',
            r2060_tipocod_views.r2060tipoCodDetail.as_view() ),

url(r'^r2060-tipocod/listar/(?P<hash>.*)/$', 
        r2060_tipocod_views.listar, 
        name='r2060_tipocod'),

url(r'^r2060-tipocod/salvar/(?P<hash>.*)/$', 
        r2060_tipocod_views.salvar, 
        name='r2060_tipocod_salvar'),





]