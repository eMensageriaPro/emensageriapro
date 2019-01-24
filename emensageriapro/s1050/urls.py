#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1050.views import s1050_alteracao as s1050_alteracao_views
from emensageriapro.s1050.views import s1050_alteracao_horariointervalo as s1050_alteracao_horariointervalo_views
from emensageriapro.s1050.views import s1050_alteracao_novavalidade as s1050_alteracao_novavalidade_views
from emensageriapro.s1050.views import s1050_exclusao as s1050_exclusao_views
from emensageriapro.s1050.views import s1050_inclusao as s1050_inclusao_views
from emensageriapro.s1050.views import s1050_inclusao_horariointervalo as s1050_inclusao_horariointervalo_views



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



url(r'^s1050-alteracao/apagar/(?P<hash>.*)/$', 
        s1050_alteracao_views.apagar, 
        name='s1050_alteracao_apagar'),

url(r'^s1050-alteracao/api/$',
            s1050_alteracao_views.s1050alteracaoList.as_view() ),

        url(r'^s1050-alteracao/api/(?P<pk>[0-9]+)/$',
            s1050_alteracao_views.s1050alteracaoDetail.as_view() ),

url(r'^s1050-alteracao/listar/(?P<hash>.*)/$', 
        s1050_alteracao_views.listar, 
        name='s1050_alteracao'),

url(r'^s1050-alteracao/salvar/(?P<hash>.*)/$', 
        s1050_alteracao_views.salvar, 
        name='s1050_alteracao_salvar'),



url(r'^s1050-alteracao-horariointervalo/apagar/(?P<hash>.*)/$', 
        s1050_alteracao_horariointervalo_views.apagar, 
        name='s1050_alteracao_horariointervalo_apagar'),

url(r'^s1050-alteracao-horariointervalo/api/$',
            s1050_alteracao_horariointervalo_views.s1050alteracaohorarioIntervaloList.as_view() ),

        url(r'^s1050-alteracao-horariointervalo/api/(?P<pk>[0-9]+)/$',
            s1050_alteracao_horariointervalo_views.s1050alteracaohorarioIntervaloDetail.as_view() ),

url(r'^s1050-alteracao-horariointervalo/listar/(?P<hash>.*)/$', 
        s1050_alteracao_horariointervalo_views.listar, 
        name='s1050_alteracao_horariointervalo'),

url(r'^s1050-alteracao-horariointervalo/salvar/(?P<hash>.*)/$', 
        s1050_alteracao_horariointervalo_views.salvar, 
        name='s1050_alteracao_horariointervalo_salvar'),



url(r'^s1050-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1050_alteracao_novavalidade_views.apagar, 
        name='s1050_alteracao_novavalidade_apagar'),

url(r'^s1050-alteracao-novavalidade/api/$',
            s1050_alteracao_novavalidade_views.s1050alteracaonovaValidadeList.as_view() ),

        url(r'^s1050-alteracao-novavalidade/api/(?P<pk>[0-9]+)/$',
            s1050_alteracao_novavalidade_views.s1050alteracaonovaValidadeDetail.as_view() ),

url(r'^s1050-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1050_alteracao_novavalidade_views.listar, 
        name='s1050_alteracao_novavalidade'),

url(r'^s1050-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1050_alteracao_novavalidade_views.salvar, 
        name='s1050_alteracao_novavalidade_salvar'),



url(r'^s1050-exclusao/apagar/(?P<hash>.*)/$', 
        s1050_exclusao_views.apagar, 
        name='s1050_exclusao_apagar'),

url(r'^s1050-exclusao/api/$',
            s1050_exclusao_views.s1050exclusaoList.as_view() ),

        url(r'^s1050-exclusao/api/(?P<pk>[0-9]+)/$',
            s1050_exclusao_views.s1050exclusaoDetail.as_view() ),

url(r'^s1050-exclusao/listar/(?P<hash>.*)/$', 
        s1050_exclusao_views.listar, 
        name='s1050_exclusao'),

url(r'^s1050-exclusao/salvar/(?P<hash>.*)/$', 
        s1050_exclusao_views.salvar, 
        name='s1050_exclusao_salvar'),



url(r'^s1050-inclusao/apagar/(?P<hash>.*)/$', 
        s1050_inclusao_views.apagar, 
        name='s1050_inclusao_apagar'),

url(r'^s1050-inclusao/api/$',
            s1050_inclusao_views.s1050inclusaoList.as_view() ),

        url(r'^s1050-inclusao/api/(?P<pk>[0-9]+)/$',
            s1050_inclusao_views.s1050inclusaoDetail.as_view() ),

url(r'^s1050-inclusao/listar/(?P<hash>.*)/$', 
        s1050_inclusao_views.listar, 
        name='s1050_inclusao'),

url(r'^s1050-inclusao/salvar/(?P<hash>.*)/$', 
        s1050_inclusao_views.salvar, 
        name='s1050_inclusao_salvar'),



url(r'^s1050-inclusao-horariointervalo/apagar/(?P<hash>.*)/$', 
        s1050_inclusao_horariointervalo_views.apagar, 
        name='s1050_inclusao_horariointervalo_apagar'),

url(r'^s1050-inclusao-horariointervalo/api/$',
            s1050_inclusao_horariointervalo_views.s1050inclusaohorarioIntervaloList.as_view() ),

        url(r'^s1050-inclusao-horariointervalo/api/(?P<pk>[0-9]+)/$',
            s1050_inclusao_horariointervalo_views.s1050inclusaohorarioIntervaloDetail.as_view() ),

url(r'^s1050-inclusao-horariointervalo/listar/(?P<hash>.*)/$', 
        s1050_inclusao_horariointervalo_views.listar, 
        name='s1050_inclusao_horariointervalo'),

url(r'^s1050-inclusao-horariointervalo/salvar/(?P<hash>.*)/$', 
        s1050_inclusao_horariointervalo_views.salvar, 
        name='s1050_inclusao_horariointervalo_salvar'),





]