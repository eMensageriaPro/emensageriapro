#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2399.views import s2399_verbasresc as s2399_verbasresc_views
from emensageriapro.s2399.views import s2399_dmdev as s2399_dmdev_views
from emensageriapro.s2399.views import s2399_ideestablot as s2399_ideestablot_views
from emensageriapro.s2399.views import s2399_detverbas as s2399_detverbas_views
from emensageriapro.s2399.views import s2399_infosaudecolet as s2399_infosaudecolet_views
from emensageriapro.s2399.views import s2399_detoper as s2399_detoper_views
from emensageriapro.s2399.views import s2399_detplano as s2399_detplano_views
from emensageriapro.s2399.views import s2399_infoagnocivo as s2399_infoagnocivo_views
from emensageriapro.s2399.views import s2399_infosimples as s2399_infosimples_views
from emensageriapro.s2399.views import s2399_procjudtrab as s2399_procjudtrab_views
from emensageriapro.s2399.views import s2399_infomv as s2399_infomv_views
from emensageriapro.s2399.views import s2399_remunoutrempr as s2399_remunoutrempr_views
from emensageriapro.s2399.views import s2399_quarentena as s2399_quarentena_views



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



url(r'^s2399-verbasresc/apagar/(?P<hash>.*)/$', 
        s2399_verbasresc_views.apagar, 
        name='s2399_verbasresc_apagar'),

url(r'^s2399-verbasresc/listar/(?P<hash>.*)/$', 
        s2399_verbasresc_views.listar, 
        name='s2399_verbasresc'),

url(r'^s2399-verbasresc/salvar/(?P<hash>.*)/$', 
        s2399_verbasresc_views.salvar, 
        name='s2399_verbasresc_salvar'),



url(r'^s2399-dmdev/apagar/(?P<hash>.*)/$', 
        s2399_dmdev_views.apagar, 
        name='s2399_dmdev_apagar'),

url(r'^s2399-dmdev/listar/(?P<hash>.*)/$', 
        s2399_dmdev_views.listar, 
        name='s2399_dmdev'),

url(r'^s2399-dmdev/salvar/(?P<hash>.*)/$', 
        s2399_dmdev_views.salvar, 
        name='s2399_dmdev_salvar'),



url(r'^s2399-ideestablot/apagar/(?P<hash>.*)/$', 
        s2399_ideestablot_views.apagar, 
        name='s2399_ideestablot_apagar'),

url(r'^s2399-ideestablot/listar/(?P<hash>.*)/$', 
        s2399_ideestablot_views.listar, 
        name='s2399_ideestablot'),

url(r'^s2399-ideestablot/salvar/(?P<hash>.*)/$', 
        s2399_ideestablot_views.salvar, 
        name='s2399_ideestablot_salvar'),



url(r'^s2399-detverbas/apagar/(?P<hash>.*)/$', 
        s2399_detverbas_views.apagar, 
        name='s2399_detverbas_apagar'),

url(r'^s2399-detverbas/listar/(?P<hash>.*)/$', 
        s2399_detverbas_views.listar, 
        name='s2399_detverbas'),

url(r'^s2399-detverbas/salvar/(?P<hash>.*)/$', 
        s2399_detverbas_views.salvar, 
        name='s2399_detverbas_salvar'),



url(r'^s2399-infosaudecolet/apagar/(?P<hash>.*)/$', 
        s2399_infosaudecolet_views.apagar, 
        name='s2399_infosaudecolet_apagar'),

url(r'^s2399-infosaudecolet/listar/(?P<hash>.*)/$', 
        s2399_infosaudecolet_views.listar, 
        name='s2399_infosaudecolet'),

url(r'^s2399-infosaudecolet/salvar/(?P<hash>.*)/$', 
        s2399_infosaudecolet_views.salvar, 
        name='s2399_infosaudecolet_salvar'),



url(r'^s2399-detoper/apagar/(?P<hash>.*)/$', 
        s2399_detoper_views.apagar, 
        name='s2399_detoper_apagar'),

url(r'^s2399-detoper/listar/(?P<hash>.*)/$', 
        s2399_detoper_views.listar, 
        name='s2399_detoper'),

url(r'^s2399-detoper/salvar/(?P<hash>.*)/$', 
        s2399_detoper_views.salvar, 
        name='s2399_detoper_salvar'),



url(r'^s2399-detplano/apagar/(?P<hash>.*)/$', 
        s2399_detplano_views.apagar, 
        name='s2399_detplano_apagar'),

url(r'^s2399-detplano/listar/(?P<hash>.*)/$', 
        s2399_detplano_views.listar, 
        name='s2399_detplano'),

url(r'^s2399-detplano/salvar/(?P<hash>.*)/$', 
        s2399_detplano_views.salvar, 
        name='s2399_detplano_salvar'),



url(r'^s2399-infoagnocivo/apagar/(?P<hash>.*)/$', 
        s2399_infoagnocivo_views.apagar, 
        name='s2399_infoagnocivo_apagar'),

url(r'^s2399-infoagnocivo/listar/(?P<hash>.*)/$', 
        s2399_infoagnocivo_views.listar, 
        name='s2399_infoagnocivo'),

url(r'^s2399-infoagnocivo/salvar/(?P<hash>.*)/$', 
        s2399_infoagnocivo_views.salvar, 
        name='s2399_infoagnocivo_salvar'),



url(r'^s2399-infosimples/apagar/(?P<hash>.*)/$', 
        s2399_infosimples_views.apagar, 
        name='s2399_infosimples_apagar'),

url(r'^s2399-infosimples/listar/(?P<hash>.*)/$', 
        s2399_infosimples_views.listar, 
        name='s2399_infosimples'),

url(r'^s2399-infosimples/salvar/(?P<hash>.*)/$', 
        s2399_infosimples_views.salvar, 
        name='s2399_infosimples_salvar'),



url(r'^s2399-procjudtrab/apagar/(?P<hash>.*)/$', 
        s2399_procjudtrab_views.apagar, 
        name='s2399_procjudtrab_apagar'),

url(r'^s2399-procjudtrab/listar/(?P<hash>.*)/$', 
        s2399_procjudtrab_views.listar, 
        name='s2399_procjudtrab'),

url(r'^s2399-procjudtrab/salvar/(?P<hash>.*)/$', 
        s2399_procjudtrab_views.salvar, 
        name='s2399_procjudtrab_salvar'),



url(r'^s2399-infomv/apagar/(?P<hash>.*)/$', 
        s2399_infomv_views.apagar, 
        name='s2399_infomv_apagar'),

url(r'^s2399-infomv/listar/(?P<hash>.*)/$', 
        s2399_infomv_views.listar, 
        name='s2399_infomv'),

url(r'^s2399-infomv/salvar/(?P<hash>.*)/$', 
        s2399_infomv_views.salvar, 
        name='s2399_infomv_salvar'),



url(r'^s2399-remunoutrempr/apagar/(?P<hash>.*)/$', 
        s2399_remunoutrempr_views.apagar, 
        name='s2399_remunoutrempr_apagar'),

url(r'^s2399-remunoutrempr/listar/(?P<hash>.*)/$', 
        s2399_remunoutrempr_views.listar, 
        name='s2399_remunoutrempr'),

url(r'^s2399-remunoutrempr/salvar/(?P<hash>.*)/$', 
        s2399_remunoutrempr_views.salvar, 
        name='s2399_remunoutrempr_salvar'),



url(r'^s2399-quarentena/apagar/(?P<hash>.*)/$', 
        s2399_quarentena_views.apagar, 
        name='s2399_quarentena_apagar'),

url(r'^s2399-quarentena/listar/(?P<hash>.*)/$', 
        s2399_quarentena_views.listar, 
        name='s2399_quarentena'),

url(r'^s2399-quarentena/salvar/(?P<hash>.*)/$', 
        s2399_quarentena_views.salvar, 
        name='s2399_quarentena_salvar'),





]