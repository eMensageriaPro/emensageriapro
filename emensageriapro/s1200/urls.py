#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1200.views import s1200_infomv as s1200_infomv_views
from emensageriapro.s1200.views import s1200_remunoutrempr as s1200_remunoutrempr_views
from emensageriapro.s1200.views import s1200_infocomplem as s1200_infocomplem_views
from emensageriapro.s1200.views import s1200_sucessaovinc as s1200_sucessaovinc_views
from emensageriapro.s1200.views import s1200_procjudtrab as s1200_procjudtrab_views
from emensageriapro.s1200.views import s1200_infointerm as s1200_infointerm_views
from emensageriapro.s1200.views import s1200_dmdev as s1200_dmdev_views
from emensageriapro.s1200.views import s1200_infoperapur as s1200_infoperapur_views
from emensageriapro.s1200.views import s1200_infoperapur_ideestablot as s1200_infoperapur_ideestablot_views
from emensageriapro.s1200.views import s1200_infoperapur_remunperapur as s1200_infoperapur_remunperapur_views
from emensageriapro.s1200.views import s1200_infoperapur_itensremun as s1200_infoperapur_itensremun_views
from emensageriapro.s1200.views import s1200_infoperapur_infosaudecolet as s1200_infoperapur_infosaudecolet_views
from emensageriapro.s1200.views import s1200_infoperapur_detoper as s1200_infoperapur_detoper_views
from emensageriapro.s1200.views import s1200_infoperapur_detplano as s1200_infoperapur_detplano_views
from emensageriapro.s1200.views import s1200_infoperapur_infoagnocivo as s1200_infoperapur_infoagnocivo_views
from emensageriapro.s1200.views import s1200_infoperapur_infotrabinterm as s1200_infoperapur_infotrabinterm_views
from emensageriapro.s1200.views import s1200_infoperant as s1200_infoperant_views
from emensageriapro.s1200.views import s1200_infoperant_ideadc as s1200_infoperant_ideadc_views
from emensageriapro.s1200.views import s1200_infoperant_ideperiodo as s1200_infoperant_ideperiodo_views
from emensageriapro.s1200.views import s1200_infoperant_ideestablot as s1200_infoperant_ideestablot_views
from emensageriapro.s1200.views import s1200_infoperant_remunperant as s1200_infoperant_remunperant_views
from emensageriapro.s1200.views import s1200_infoperant_itensremun as s1200_infoperant_itensremun_views
from emensageriapro.s1200.views import s1200_infoperant_infoagnocivo as s1200_infoperant_infoagnocivo_views
from emensageriapro.s1200.views import s1200_infoperant_infotrabinterm as s1200_infoperant_infotrabinterm_views
from emensageriapro.s1200.views import s1200_infoperant_infocomplcont as s1200_infoperant_infocomplcont_views



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



url(r'^s1200-infomv/apagar/(?P<hash>.*)/$', 
        s1200_infomv_views.apagar, 
        name='s1200_infomv_apagar'),

url(r'^s1200-infomv/listar/(?P<hash>.*)/$', 
        s1200_infomv_views.listar, 
        name='s1200_infomv'),

url(r'^s1200-infomv/salvar/(?P<hash>.*)/$', 
        s1200_infomv_views.salvar, 
        name='s1200_infomv_salvar'),



url(r'^s1200-remunoutrempr/apagar/(?P<hash>.*)/$', 
        s1200_remunoutrempr_views.apagar, 
        name='s1200_remunoutrempr_apagar'),

url(r'^s1200-remunoutrempr/listar/(?P<hash>.*)/$', 
        s1200_remunoutrempr_views.listar, 
        name='s1200_remunoutrempr'),

url(r'^s1200-remunoutrempr/salvar/(?P<hash>.*)/$', 
        s1200_remunoutrempr_views.salvar, 
        name='s1200_remunoutrempr_salvar'),



url(r'^s1200-infocomplem/apagar/(?P<hash>.*)/$', 
        s1200_infocomplem_views.apagar, 
        name='s1200_infocomplem_apagar'),

url(r'^s1200-infocomplem/listar/(?P<hash>.*)/$', 
        s1200_infocomplem_views.listar, 
        name='s1200_infocomplem'),

url(r'^s1200-infocomplem/salvar/(?P<hash>.*)/$', 
        s1200_infocomplem_views.salvar, 
        name='s1200_infocomplem_salvar'),



url(r'^s1200-sucessaovinc/apagar/(?P<hash>.*)/$', 
        s1200_sucessaovinc_views.apagar, 
        name='s1200_sucessaovinc_apagar'),

url(r'^s1200-sucessaovinc/listar/(?P<hash>.*)/$', 
        s1200_sucessaovinc_views.listar, 
        name='s1200_sucessaovinc'),

url(r'^s1200-sucessaovinc/salvar/(?P<hash>.*)/$', 
        s1200_sucessaovinc_views.salvar, 
        name='s1200_sucessaovinc_salvar'),



url(r'^s1200-procjudtrab/apagar/(?P<hash>.*)/$', 
        s1200_procjudtrab_views.apagar, 
        name='s1200_procjudtrab_apagar'),

url(r'^s1200-procjudtrab/listar/(?P<hash>.*)/$', 
        s1200_procjudtrab_views.listar, 
        name='s1200_procjudtrab'),

url(r'^s1200-procjudtrab/salvar/(?P<hash>.*)/$', 
        s1200_procjudtrab_views.salvar, 
        name='s1200_procjudtrab_salvar'),



url(r'^s1200-infointerm/apagar/(?P<hash>.*)/$', 
        s1200_infointerm_views.apagar, 
        name='s1200_infointerm_apagar'),

url(r'^s1200-infointerm/listar/(?P<hash>.*)/$', 
        s1200_infointerm_views.listar, 
        name='s1200_infointerm'),

url(r'^s1200-infointerm/salvar/(?P<hash>.*)/$', 
        s1200_infointerm_views.salvar, 
        name='s1200_infointerm_salvar'),



url(r'^s1200-dmdev/apagar/(?P<hash>.*)/$', 
        s1200_dmdev_views.apagar, 
        name='s1200_dmdev_apagar'),

url(r'^s1200-dmdev/listar/(?P<hash>.*)/$', 
        s1200_dmdev_views.listar, 
        name='s1200_dmdev'),

url(r'^s1200-dmdev/salvar/(?P<hash>.*)/$', 
        s1200_dmdev_views.salvar, 
        name='s1200_dmdev_salvar'),



url(r'^s1200-infoperapur/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_views.apagar, 
        name='s1200_infoperapur_apagar'),

url(r'^s1200-infoperapur/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_views.listar, 
        name='s1200_infoperapur'),

url(r'^s1200-infoperapur/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_views.salvar, 
        name='s1200_infoperapur_salvar'),



url(r'^s1200-infoperapur-ideestablot/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_ideestablot_views.apagar, 
        name='s1200_infoperapur_ideestablot_apagar'),

url(r'^s1200-infoperapur-ideestablot/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_ideestablot_views.listar, 
        name='s1200_infoperapur_ideestablot'),

url(r'^s1200-infoperapur-ideestablot/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_ideestablot_views.salvar, 
        name='s1200_infoperapur_ideestablot_salvar'),



url(r'^s1200-infoperapur-remunperapur/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_remunperapur_views.apagar, 
        name='s1200_infoperapur_remunperapur_apagar'),

url(r'^s1200-infoperapur-remunperapur/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_remunperapur_views.listar, 
        name='s1200_infoperapur_remunperapur'),

url(r'^s1200-infoperapur-remunperapur/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_remunperapur_views.salvar, 
        name='s1200_infoperapur_remunperapur_salvar'),



url(r'^s1200-infoperapur-itensremun/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_itensremun_views.apagar, 
        name='s1200_infoperapur_itensremun_apagar'),

url(r'^s1200-infoperapur-itensremun/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_itensremun_views.listar, 
        name='s1200_infoperapur_itensremun'),

url(r'^s1200-infoperapur-itensremun/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_itensremun_views.salvar, 
        name='s1200_infoperapur_itensremun_salvar'),



url(r'^s1200-infoperapur-infosaudecolet/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_infosaudecolet_views.apagar, 
        name='s1200_infoperapur_infosaudecolet_apagar'),

url(r'^s1200-infoperapur-infosaudecolet/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_infosaudecolet_views.listar, 
        name='s1200_infoperapur_infosaudecolet'),

url(r'^s1200-infoperapur-infosaudecolet/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_infosaudecolet_views.salvar, 
        name='s1200_infoperapur_infosaudecolet_salvar'),



url(r'^s1200-infoperapur-detoper/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_detoper_views.apagar, 
        name='s1200_infoperapur_detoper_apagar'),

url(r'^s1200-infoperapur-detoper/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_detoper_views.listar, 
        name='s1200_infoperapur_detoper'),

url(r'^s1200-infoperapur-detoper/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_detoper_views.salvar, 
        name='s1200_infoperapur_detoper_salvar'),



url(r'^s1200-infoperapur-detplano/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_detplano_views.apagar, 
        name='s1200_infoperapur_detplano_apagar'),

url(r'^s1200-infoperapur-detplano/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_detplano_views.listar, 
        name='s1200_infoperapur_detplano'),

url(r'^s1200-infoperapur-detplano/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_detplano_views.salvar, 
        name='s1200_infoperapur_detplano_salvar'),



url(r'^s1200-infoperapur-infoagnocivo/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_infoagnocivo_views.apagar, 
        name='s1200_infoperapur_infoagnocivo_apagar'),

url(r'^s1200-infoperapur-infoagnocivo/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_infoagnocivo_views.listar, 
        name='s1200_infoperapur_infoagnocivo'),

url(r'^s1200-infoperapur-infoagnocivo/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_infoagnocivo_views.salvar, 
        name='s1200_infoperapur_infoagnocivo_salvar'),



url(r'^s1200-infoperapur-infotrabinterm/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_infotrabinterm_views.apagar, 
        name='s1200_infoperapur_infotrabinterm_apagar'),

url(r'^s1200-infoperapur-infotrabinterm/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_infotrabinterm_views.listar, 
        name='s1200_infoperapur_infotrabinterm'),

url(r'^s1200-infoperapur-infotrabinterm/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_infotrabinterm_views.salvar, 
        name='s1200_infoperapur_infotrabinterm_salvar'),



url(r'^s1200-infoperant/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_views.apagar, 
        name='s1200_infoperant_apagar'),

url(r'^s1200-infoperant/listar/(?P<hash>.*)/$', 
        s1200_infoperant_views.listar, 
        name='s1200_infoperant'),

url(r'^s1200-infoperant/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_views.salvar, 
        name='s1200_infoperant_salvar'),



url(r'^s1200-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_ideadc_views.apagar, 
        name='s1200_infoperant_ideadc_apagar'),

url(r'^s1200-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        s1200_infoperant_ideadc_views.listar, 
        name='s1200_infoperant_ideadc'),

url(r'^s1200-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_ideadc_views.salvar, 
        name='s1200_infoperant_ideadc_salvar'),



url(r'^s1200-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_ideperiodo_views.apagar, 
        name='s1200_infoperant_ideperiodo_apagar'),

url(r'^s1200-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        s1200_infoperant_ideperiodo_views.listar, 
        name='s1200_infoperant_ideperiodo'),

url(r'^s1200-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_ideperiodo_views.salvar, 
        name='s1200_infoperant_ideperiodo_salvar'),



url(r'^s1200-infoperant-ideestablot/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_ideestablot_views.apagar, 
        name='s1200_infoperant_ideestablot_apagar'),

url(r'^s1200-infoperant-ideestablot/listar/(?P<hash>.*)/$', 
        s1200_infoperant_ideestablot_views.listar, 
        name='s1200_infoperant_ideestablot'),

url(r'^s1200-infoperant-ideestablot/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_ideestablot_views.salvar, 
        name='s1200_infoperant_ideestablot_salvar'),



url(r'^s1200-infoperant-remunperant/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_remunperant_views.apagar, 
        name='s1200_infoperant_remunperant_apagar'),

url(r'^s1200-infoperant-remunperant/listar/(?P<hash>.*)/$', 
        s1200_infoperant_remunperant_views.listar, 
        name='s1200_infoperant_remunperant'),

url(r'^s1200-infoperant-remunperant/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_remunperant_views.salvar, 
        name='s1200_infoperant_remunperant_salvar'),



url(r'^s1200-infoperant-itensremun/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_itensremun_views.apagar, 
        name='s1200_infoperant_itensremun_apagar'),

url(r'^s1200-infoperant-itensremun/listar/(?P<hash>.*)/$', 
        s1200_infoperant_itensremun_views.listar, 
        name='s1200_infoperant_itensremun'),

url(r'^s1200-infoperant-itensremun/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_itensremun_views.salvar, 
        name='s1200_infoperant_itensremun_salvar'),



url(r'^s1200-infoperant-infoagnocivo/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_infoagnocivo_views.apagar, 
        name='s1200_infoperant_infoagnocivo_apagar'),

url(r'^s1200-infoperant-infoagnocivo/listar/(?P<hash>.*)/$', 
        s1200_infoperant_infoagnocivo_views.listar, 
        name='s1200_infoperant_infoagnocivo'),

url(r'^s1200-infoperant-infoagnocivo/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_infoagnocivo_views.salvar, 
        name='s1200_infoperant_infoagnocivo_salvar'),



url(r'^s1200-infoperant-infotrabinterm/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_infotrabinterm_views.apagar, 
        name='s1200_infoperant_infotrabinterm_apagar'),

url(r'^s1200-infoperant-infotrabinterm/listar/(?P<hash>.*)/$', 
        s1200_infoperant_infotrabinterm_views.listar, 
        name='s1200_infoperant_infotrabinterm'),

url(r'^s1200-infoperant-infotrabinterm/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_infotrabinterm_views.salvar, 
        name='s1200_infoperant_infotrabinterm_salvar'),



url(r'^s1200-infoperant-infocomplcont/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_infocomplcont_views.apagar, 
        name='s1200_infoperant_infocomplcont_apagar'),

url(r'^s1200-infoperant-infocomplcont/listar/(?P<hash>.*)/$', 
        s1200_infoperant_infocomplcont_views.listar, 
        name='s1200_infoperant_infocomplcont'),

url(r'^s1200-infoperant-infocomplcont/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_infocomplcont_views.salvar, 
        name='s1200_infoperant_infocomplcont_salvar'),





]