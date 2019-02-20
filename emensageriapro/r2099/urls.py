#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2099.views import r2099_iderespinf as r2099_iderespinf_views



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



url(r'^r2099-iderespinf/apagar/(?P<hash>.*)/$', 
        r2099_iderespinf_views.apagar, 
        name='r2099_iderespinf_apagar'),

url(r'^r2099-iderespinf/api/$',
            r2099_iderespinf_views.r2099ideRespInfList.as_view() ),

        url(r'^r2099-iderespinf/api/(?P<pk>[0-9]+)/$',
            r2099_iderespinf_views.r2099ideRespInfDetail.as_view() ),

url(r'^r2099-iderespinf/listar/(?P<hash>.*)/$', 
        r2099_iderespinf_views.listar, 
        name='r2099_iderespinf'),

url(r'^r2099-iderespinf/salvar/(?P<hash>.*)/$', 
        r2099_iderespinf_views.salvar, 
        name='r2099_iderespinf_salvar'),





]