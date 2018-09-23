#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1207.views import s1207_procjudtrab as s1207_procjudtrab_views
from emensageriapro.s1207.views import s1207_dmdev as s1207_dmdev_views
from emensageriapro.s1207.views import s1207_itens as s1207_itens_views
from emensageriapro.s1207.views import s1207_infoperapur as s1207_infoperapur_views
from emensageriapro.s1207.views import s1207_infoperapur_ideestab as s1207_infoperapur_ideestab_views
from emensageriapro.s1207.views import s1207_infoperapur_remunperapur as s1207_infoperapur_remunperapur_views
from emensageriapro.s1207.views import s1207_infoperapur_itensremun as s1207_infoperapur_itensremun_views
from emensageriapro.s1207.views import s1207_infoperant as s1207_infoperant_views
from emensageriapro.s1207.views import s1207_infoperant_ideadc as s1207_infoperant_ideadc_views
from emensageriapro.s1207.views import s1207_infoperant_ideperiodo as s1207_infoperant_ideperiodo_views
from emensageriapro.s1207.views import s1207_infoperant_ideestab as s1207_infoperant_ideestab_views
from emensageriapro.s1207.views import s1207_infoperant_remunperant as s1207_infoperant_remunperant_views
from emensageriapro.s1207.views import s1207_infoperant_itensremun as s1207_infoperant_itensremun_views



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



url(r'^s1207-procjudtrab/apagar/(?P<hash>.*)/$', 
        s1207_procjudtrab_views.apagar, 
        name='s1207_procjudtrab_apagar'),

url(r'^s1207-procjudtrab/listar/(?P<hash>.*)/$', 
        s1207_procjudtrab_views.listar, 
        name='s1207_procjudtrab'),

url(r'^s1207-procjudtrab/salvar/(?P<hash>.*)/$', 
        s1207_procjudtrab_views.salvar, 
        name='s1207_procjudtrab_salvar'),



url(r'^s1207-dmdev/apagar/(?P<hash>.*)/$', 
        s1207_dmdev_views.apagar, 
        name='s1207_dmdev_apagar'),

url(r'^s1207-dmdev/listar/(?P<hash>.*)/$', 
        s1207_dmdev_views.listar, 
        name='s1207_dmdev'),

url(r'^s1207-dmdev/salvar/(?P<hash>.*)/$', 
        s1207_dmdev_views.salvar, 
        name='s1207_dmdev_salvar'),



url(r'^s1207-itens/apagar/(?P<hash>.*)/$', 
        s1207_itens_views.apagar, 
        name='s1207_itens_apagar'),

url(r'^s1207-itens/listar/(?P<hash>.*)/$', 
        s1207_itens_views.listar, 
        name='s1207_itens'),

url(r'^s1207-itens/salvar/(?P<hash>.*)/$', 
        s1207_itens_views.salvar, 
        name='s1207_itens_salvar'),



url(r'^s1207-infoperapur/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_views.apagar, 
        name='s1207_infoperapur_apagar'),

url(r'^s1207-infoperapur/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_views.listar, 
        name='s1207_infoperapur'),

url(r'^s1207-infoperapur/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_views.salvar, 
        name='s1207_infoperapur_salvar'),



url(r'^s1207-infoperapur-ideestab/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_ideestab_views.apagar, 
        name='s1207_infoperapur_ideestab_apagar'),

url(r'^s1207-infoperapur-ideestab/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_ideestab_views.listar, 
        name='s1207_infoperapur_ideestab'),

url(r'^s1207-infoperapur-ideestab/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_ideestab_views.salvar, 
        name='s1207_infoperapur_ideestab_salvar'),



url(r'^s1207-infoperapur-remunperapur/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_remunperapur_views.apagar, 
        name='s1207_infoperapur_remunperapur_apagar'),

url(r'^s1207-infoperapur-remunperapur/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_remunperapur_views.listar, 
        name='s1207_infoperapur_remunperapur'),

url(r'^s1207-infoperapur-remunperapur/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_remunperapur_views.salvar, 
        name='s1207_infoperapur_remunperapur_salvar'),



url(r'^s1207-infoperapur-itensremun/apagar/(?P<hash>.*)/$', 
        s1207_infoperapur_itensremun_views.apagar, 
        name='s1207_infoperapur_itensremun_apagar'),

url(r'^s1207-infoperapur-itensremun/listar/(?P<hash>.*)/$', 
        s1207_infoperapur_itensremun_views.listar, 
        name='s1207_infoperapur_itensremun'),

url(r'^s1207-infoperapur-itensremun/salvar/(?P<hash>.*)/$', 
        s1207_infoperapur_itensremun_views.salvar, 
        name='s1207_infoperapur_itensremun_salvar'),



url(r'^s1207-infoperant/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_views.apagar, 
        name='s1207_infoperant_apagar'),

url(r'^s1207-infoperant/listar/(?P<hash>.*)/$', 
        s1207_infoperant_views.listar, 
        name='s1207_infoperant'),

url(r'^s1207-infoperant/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_views.salvar, 
        name='s1207_infoperant_salvar'),



url(r'^s1207-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_ideadc_views.apagar, 
        name='s1207_infoperant_ideadc_apagar'),

url(r'^s1207-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        s1207_infoperant_ideadc_views.listar, 
        name='s1207_infoperant_ideadc'),

url(r'^s1207-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_ideadc_views.salvar, 
        name='s1207_infoperant_ideadc_salvar'),



url(r'^s1207-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_ideperiodo_views.apagar, 
        name='s1207_infoperant_ideperiodo_apagar'),

url(r'^s1207-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        s1207_infoperant_ideperiodo_views.listar, 
        name='s1207_infoperant_ideperiodo'),

url(r'^s1207-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_ideperiodo_views.salvar, 
        name='s1207_infoperant_ideperiodo_salvar'),



url(r'^s1207-infoperant-ideestab/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_ideestab_views.apagar, 
        name='s1207_infoperant_ideestab_apagar'),

url(r'^s1207-infoperant-ideestab/listar/(?P<hash>.*)/$', 
        s1207_infoperant_ideestab_views.listar, 
        name='s1207_infoperant_ideestab'),

url(r'^s1207-infoperant-ideestab/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_ideestab_views.salvar, 
        name='s1207_infoperant_ideestab_salvar'),



url(r'^s1207-infoperant-remunperant/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_remunperant_views.apagar, 
        name='s1207_infoperant_remunperant_apagar'),

url(r'^s1207-infoperant-remunperant/listar/(?P<hash>.*)/$', 
        s1207_infoperant_remunperant_views.listar, 
        name='s1207_infoperant_remunperant'),

url(r'^s1207-infoperant-remunperant/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_remunperant_views.salvar, 
        name='s1207_infoperant_remunperant_salvar'),



url(r'^s1207-infoperant-itensremun/apagar/(?P<hash>.*)/$', 
        s1207_infoperant_itensremun_views.apagar, 
        name='s1207_infoperant_itensremun_apagar'),

url(r'^s1207-infoperant-itensremun/listar/(?P<hash>.*)/$', 
        s1207_infoperant_itensremun_views.listar, 
        name='s1207_infoperant_itensremun'),

url(r'^s1207-infoperant-itensremun/salvar/(?P<hash>.*)/$', 
        s1207_infoperant_itensremun_views.salvar, 
        name='s1207_infoperant_itensremun_salvar'),





]