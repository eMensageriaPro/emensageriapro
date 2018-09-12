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



url(r'^s2306-infocomplementares/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infocomplementares.apagar', 
        name='s2306_infocomplementares_apagar'),

url(r'^s2306-infocomplementares/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infocomplementares.listar', 
        name='s2306_infocomplementares'),

url(r'^s2306-infocomplementares/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infocomplementares.salvar', 
        name='s2306_infocomplementares_salvar'),



url(r'^s2306-cargofuncao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_cargofuncao.apagar', 
        name='s2306_cargofuncao_apagar'),

url(r'^s2306-cargofuncao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_cargofuncao.listar', 
        name='s2306_cargofuncao'),

url(r'^s2306-cargofuncao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_cargofuncao.salvar', 
        name='s2306_cargofuncao_salvar'),



url(r'^s2306-remuneracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_remuneracao.apagar', 
        name='s2306_remuneracao_apagar'),

url(r'^s2306-remuneracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_remuneracao.listar', 
        name='s2306_remuneracao'),

url(r'^s2306-remuneracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_remuneracao.salvar', 
        name='s2306_remuneracao_salvar'),



url(r'^s2306-infoestagiario/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infoestagiario.apagar', 
        name='s2306_infoestagiario_apagar'),

url(r'^s2306-infoestagiario/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infoestagiario.listar', 
        name='s2306_infoestagiario'),

url(r'^s2306-infoestagiario/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_infoestagiario.salvar', 
        name='s2306_infoestagiario_salvar'),



url(r'^s2306-ageintegracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_ageintegracao.apagar', 
        name='s2306_ageintegracao_apagar'),

url(r'^s2306-ageintegracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_ageintegracao.listar', 
        name='s2306_ageintegracao'),

url(r'^s2306-ageintegracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_ageintegracao.salvar', 
        name='s2306_ageintegracao_salvar'),



url(r'^s2306-supervisorestagio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_supervisorestagio.apagar', 
        name='s2306_supervisorestagio_apagar'),

url(r'^s2306-supervisorestagio/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_supervisorestagio.listar', 
        name='s2306_supervisorestagio'),

url(r'^s2306-supervisorestagio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2306.views.s2306_supervisorestagio.salvar', 
        name='s2306_supervisorestagio_salvar'),





)