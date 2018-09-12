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



url(r'^r3010-ideestab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_ideestab.apagar', 
        name='r3010_ideestab_apagar'),

url(r'^r3010-ideestab/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_ideestab.listar', 
        name='r3010_ideestab'),

url(r'^r3010-ideestab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_ideestab.salvar', 
        name='r3010_ideestab_salvar'),



url(r'^r3010-boletim/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_boletim.apagar', 
        name='r3010_boletim_apagar'),

url(r'^r3010-boletim/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_boletim.listar', 
        name='r3010_boletim'),

url(r'^r3010-boletim/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_boletim.salvar', 
        name='r3010_boletim_salvar'),



url(r'^r3010-receitaingressos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_receitaingressos.apagar', 
        name='r3010_receitaingressos_apagar'),

url(r'^r3010-receitaingressos/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_receitaingressos.listar', 
        name='r3010_receitaingressos'),

url(r'^r3010-receitaingressos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_receitaingressos.salvar', 
        name='r3010_receitaingressos_salvar'),



url(r'^r3010-outrasreceitas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_outrasreceitas.apagar', 
        name='r3010_outrasreceitas_apagar'),

url(r'^r3010-outrasreceitas/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_outrasreceitas.listar', 
        name='r3010_outrasreceitas'),

url(r'^r3010-outrasreceitas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_outrasreceitas.salvar', 
        name='r3010_outrasreceitas_salvar'),



url(r'^r3010-infoproc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_infoproc.apagar', 
        name='r3010_infoproc_apagar'),

url(r'^r3010-infoproc/listar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_infoproc.listar', 
        name='r3010_infoproc'),

url(r'^r3010-infoproc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r3010.views.r3010_infoproc.salvar', 
        name='r3010_infoproc_salvar'),





)