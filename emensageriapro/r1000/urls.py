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



url(r'^r1000-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao.apagar', 
        name='r1000_inclusao_apagar'),

url(r'^r1000-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao.listar', 
        name='r1000_inclusao'),

url(r'^r1000-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao.salvar', 
        name='r1000_inclusao_salvar'),



url(r'^r1000-inclusao-softhouse/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_softhouse.apagar', 
        name='r1000_inclusao_softhouse_apagar'),

url(r'^r1000-inclusao-softhouse/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_softhouse.listar', 
        name='r1000_inclusao_softhouse'),

url(r'^r1000-inclusao-softhouse/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_softhouse.salvar', 
        name='r1000_inclusao_softhouse_salvar'),



url(r'^r1000-inclusao-infoefr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_infoefr.apagar', 
        name='r1000_inclusao_infoefr_apagar'),

url(r'^r1000-inclusao-infoefr/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_infoefr.listar', 
        name='r1000_inclusao_infoefr'),

url(r'^r1000-inclusao-infoefr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_infoefr.salvar', 
        name='r1000_inclusao_infoefr_salvar'),



url(r'^r1000-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao.apagar', 
        name='r1000_alteracao_apagar'),

url(r'^r1000-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao.listar', 
        name='r1000_alteracao'),

url(r'^r1000-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao.salvar', 
        name='r1000_alteracao_salvar'),



url(r'^r1000-alteracao-softhouse/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_softhouse.apagar', 
        name='r1000_alteracao_softhouse_apagar'),

url(r'^r1000-alteracao-softhouse/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_softhouse.listar', 
        name='r1000_alteracao_softhouse'),

url(r'^r1000-alteracao-softhouse/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_softhouse.salvar', 
        name='r1000_alteracao_softhouse_salvar'),



url(r'^r1000-alteracao-infoefr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_infoefr.apagar', 
        name='r1000_alteracao_infoefr_apagar'),

url(r'^r1000-alteracao-infoefr/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_infoefr.listar', 
        name='r1000_alteracao_infoefr'),

url(r'^r1000-alteracao-infoefr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_infoefr.salvar', 
        name='r1000_alteracao_infoefr_salvar'),



url(r'^r1000-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_novavalidade.apagar', 
        name='r1000_alteracao_novavalidade_apagar'),

url(r'^r1000-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_novavalidade.listar', 
        name='r1000_alteracao_novavalidade'),

url(r'^r1000-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_novavalidade.salvar', 
        name='r1000_alteracao_novavalidade_salvar'),



url(r'^r1000-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_exclusao.apagar', 
        name='r1000_exclusao_apagar'),

url(r'^r1000-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_exclusao.listar', 
        name='r1000_exclusao'),

url(r'^r1000-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_exclusao.salvar', 
        name='r1000_exclusao_salvar'),





)