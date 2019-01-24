#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s3000.views import s3000_idefolhapagto as s3000_idefolhapagto_views
from emensageriapro.s3000.views import s3000_idetrabalhador as s3000_idetrabalhador_views



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



url(r'^s3000-idefolhapagto/apagar/(?P<hash>.*)/$', 
        s3000_idefolhapagto_views.apagar, 
        name='s3000_idefolhapagto_apagar'),

url(r'^s3000-idefolhapagto/api/$',
            s3000_idefolhapagto_views.s3000ideFolhaPagtoList.as_view() ),

        url(r'^s3000-idefolhapagto/api/(?P<pk>[0-9]+)/$',
            s3000_idefolhapagto_views.s3000ideFolhaPagtoDetail.as_view() ),

url(r'^s3000-idefolhapagto/listar/(?P<hash>.*)/$', 
        s3000_idefolhapagto_views.listar, 
        name='s3000_idefolhapagto'),

url(r'^s3000-idefolhapagto/salvar/(?P<hash>.*)/$', 
        s3000_idefolhapagto_views.salvar, 
        name='s3000_idefolhapagto_salvar'),



url(r'^s3000-idetrabalhador/apagar/(?P<hash>.*)/$', 
        s3000_idetrabalhador_views.apagar, 
        name='s3000_idetrabalhador_apagar'),

url(r'^s3000-idetrabalhador/api/$',
            s3000_idetrabalhador_views.s3000ideTrabalhadorList.as_view() ),

        url(r'^s3000-idetrabalhador/api/(?P<pk>[0-9]+)/$',
            s3000_idetrabalhador_views.s3000ideTrabalhadorDetail.as_view() ),

url(r'^s3000-idetrabalhador/listar/(?P<hash>.*)/$', 
        s3000_idetrabalhador_views.listar, 
        name='s3000_idetrabalhador'),

url(r'^s3000-idetrabalhador/salvar/(?P<hash>.*)/$', 
        s3000_idetrabalhador_views.salvar, 
        name='s3000_idetrabalhador_salvar'),





]