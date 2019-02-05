#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1200.views import s1200_dmdev as s1200_dmdev_views
from emensageriapro.s1200.views import s1200_infocomplem as s1200_infocomplem_views
from emensageriapro.s1200.views import s1200_infointerm as s1200_infointerm_views
from emensageriapro.s1200.views import s1200_infomv as s1200_infomv_views
from emensageriapro.s1200.views import s1200_infoperant_ideadc as s1200_infoperant_ideadc_views
from emensageriapro.s1200.views import s1200_infoperant_ideestablot as s1200_infoperant_ideestablot_views
from emensageriapro.s1200.views import s1200_infoperant_ideperiodo as s1200_infoperant_ideperiodo_views
from emensageriapro.s1200.views import s1200_infoperant_infoagnocivo as s1200_infoperant_infoagnocivo_views
from emensageriapro.s1200.views import s1200_infoperant_infocomplcont as s1200_infoperant_infocomplcont_views
from emensageriapro.s1200.views import s1200_infoperant_infotrabinterm as s1200_infoperant_infotrabinterm_views
from emensageriapro.s1200.views import s1200_infoperant_itensremun as s1200_infoperant_itensremun_views
from emensageriapro.s1200.views import s1200_infoperant_remunperant as s1200_infoperant_remunperant_views
from emensageriapro.s1200.views import s1200_infoperapur_detoper as s1200_infoperapur_detoper_views
from emensageriapro.s1200.views import s1200_infoperapur_detplano as s1200_infoperapur_detplano_views
from emensageriapro.s1200.views import s1200_infoperapur_ideestablot as s1200_infoperapur_ideestablot_views
from emensageriapro.s1200.views import s1200_infoperapur_infoagnocivo as s1200_infoperapur_infoagnocivo_views
from emensageriapro.s1200.views import s1200_infoperapur_infotrabinterm as s1200_infoperapur_infotrabinterm_views
from emensageriapro.s1200.views import s1200_infoperapur_itensremun as s1200_infoperapur_itensremun_views
from emensageriapro.s1200.views import s1200_infoperapur_remunperapur as s1200_infoperapur_remunperapur_views
from emensageriapro.s1200.views import s1200_procjudtrab as s1200_procjudtrab_views
from emensageriapro.s1200.views import s1200_remunoutrempr as s1200_remunoutrempr_views
from emensageriapro.s1200.views import s1200_sucessaovinc as s1200_sucessaovinc_views



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



url(r'^s1200-dmdev/apagar/(?P<hash>.*)/$', 
        s1200_dmdev_views.apagar, 
        name='s1200_dmdev_apagar'),

url(r'^s1200-dmdev/api/$',
            s1200_dmdev_views.s1200dmDevList.as_view() ),

        url(r'^s1200-dmdev/api/(?P<pk>[0-9]+)/$',
            s1200_dmdev_views.s1200dmDevDetail.as_view() ),

url(r'^s1200-dmdev/listar/(?P<hash>.*)/$', 
        s1200_dmdev_views.listar, 
        name='s1200_dmdev'),

url(r'^s1200-dmdev/salvar/(?P<hash>.*)/$', 
        s1200_dmdev_views.salvar, 
        name='s1200_dmdev_salvar'),



url(r'^s1200-infocomplem/apagar/(?P<hash>.*)/$', 
        s1200_infocomplem_views.apagar, 
        name='s1200_infocomplem_apagar'),

url(r'^s1200-infocomplem/api/$',
            s1200_infocomplem_views.s1200infoComplemList.as_view() ),

        url(r'^s1200-infocomplem/api/(?P<pk>[0-9]+)/$',
            s1200_infocomplem_views.s1200infoComplemDetail.as_view() ),

url(r'^s1200-infocomplem/listar/(?P<hash>.*)/$', 
        s1200_infocomplem_views.listar, 
        name='s1200_infocomplem'),

url(r'^s1200-infocomplem/salvar/(?P<hash>.*)/$', 
        s1200_infocomplem_views.salvar, 
        name='s1200_infocomplem_salvar'),



url(r'^s1200-infointerm/apagar/(?P<hash>.*)/$', 
        s1200_infointerm_views.apagar, 
        name='s1200_infointerm_apagar'),

url(r'^s1200-infointerm/api/$',
            s1200_infointerm_views.s1200infoIntermList.as_view() ),

        url(r'^s1200-infointerm/api/(?P<pk>[0-9]+)/$',
            s1200_infointerm_views.s1200infoIntermDetail.as_view() ),

url(r'^s1200-infointerm/listar/(?P<hash>.*)/$', 
        s1200_infointerm_views.listar, 
        name='s1200_infointerm'),

url(r'^s1200-infointerm/salvar/(?P<hash>.*)/$', 
        s1200_infointerm_views.salvar, 
        name='s1200_infointerm_salvar'),



url(r'^s1200-infomv/apagar/(?P<hash>.*)/$', 
        s1200_infomv_views.apagar, 
        name='s1200_infomv_apagar'),

url(r'^s1200-infomv/api/$',
            s1200_infomv_views.s1200infoMVList.as_view() ),

        url(r'^s1200-infomv/api/(?P<pk>[0-9]+)/$',
            s1200_infomv_views.s1200infoMVDetail.as_view() ),

url(r'^s1200-infomv/listar/(?P<hash>.*)/$', 
        s1200_infomv_views.listar, 
        name='s1200_infomv'),

url(r'^s1200-infomv/salvar/(?P<hash>.*)/$', 
        s1200_infomv_views.salvar, 
        name='s1200_infomv_salvar'),



url(r'^s1200-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_ideadc_views.apagar, 
        name='s1200_infoperant_ideadc_apagar'),

url(r'^s1200-infoperant-ideadc/api/$',
            s1200_infoperant_ideadc_views.s1200infoPerAntideADCList.as_view() ),

        url(r'^s1200-infoperant-ideadc/api/(?P<pk>[0-9]+)/$',
            s1200_infoperant_ideadc_views.s1200infoPerAntideADCDetail.as_view() ),

url(r'^s1200-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        s1200_infoperant_ideadc_views.listar, 
        name='s1200_infoperant_ideadc'),

url(r'^s1200-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_ideadc_views.salvar, 
        name='s1200_infoperant_ideadc_salvar'),



url(r'^s1200-infoperant-ideestablot/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_ideestablot_views.apagar, 
        name='s1200_infoperant_ideestablot_apagar'),

url(r'^s1200-infoperant-ideestablot/api/$',
            s1200_infoperant_ideestablot_views.s1200infoPerAntideEstabLotList.as_view() ),

        url(r'^s1200-infoperant-ideestablot/api/(?P<pk>[0-9]+)/$',
            s1200_infoperant_ideestablot_views.s1200infoPerAntideEstabLotDetail.as_view() ),

url(r'^s1200-infoperant-ideestablot/listar/(?P<hash>.*)/$', 
        s1200_infoperant_ideestablot_views.listar, 
        name='s1200_infoperant_ideestablot'),

url(r'^s1200-infoperant-ideestablot/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_ideestablot_views.salvar, 
        name='s1200_infoperant_ideestablot_salvar'),



url(r'^s1200-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_ideperiodo_views.apagar, 
        name='s1200_infoperant_ideperiodo_apagar'),

url(r'^s1200-infoperant-ideperiodo/api/$',
            s1200_infoperant_ideperiodo_views.s1200infoPerAntidePeriodoList.as_view() ),

        url(r'^s1200-infoperant-ideperiodo/api/(?P<pk>[0-9]+)/$',
            s1200_infoperant_ideperiodo_views.s1200infoPerAntidePeriodoDetail.as_view() ),

url(r'^s1200-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        s1200_infoperant_ideperiodo_views.listar, 
        name='s1200_infoperant_ideperiodo'),

url(r'^s1200-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_ideperiodo_views.salvar, 
        name='s1200_infoperant_ideperiodo_salvar'),



url(r'^s1200-infoperant-infoagnocivo/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_infoagnocivo_views.apagar, 
        name='s1200_infoperant_infoagnocivo_apagar'),

url(r'^s1200-infoperant-infoagnocivo/api/$',
            s1200_infoperant_infoagnocivo_views.s1200infoPerAntinfoAgNocivoList.as_view() ),

        url(r'^s1200-infoperant-infoagnocivo/api/(?P<pk>[0-9]+)/$',
            s1200_infoperant_infoagnocivo_views.s1200infoPerAntinfoAgNocivoDetail.as_view() ),

url(r'^s1200-infoperant-infoagnocivo/listar/(?P<hash>.*)/$', 
        s1200_infoperant_infoagnocivo_views.listar, 
        name='s1200_infoperant_infoagnocivo'),

url(r'^s1200-infoperant-infoagnocivo/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_infoagnocivo_views.salvar, 
        name='s1200_infoperant_infoagnocivo_salvar'),



url(r'^s1200-infoperant-infocomplcont/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_infocomplcont_views.apagar, 
        name='s1200_infoperant_infocomplcont_apagar'),

url(r'^s1200-infoperant-infocomplcont/api/$',
            s1200_infoperant_infocomplcont_views.s1200infoPerAntinfoComplContList.as_view() ),

        url(r'^s1200-infoperant-infocomplcont/api/(?P<pk>[0-9]+)/$',
            s1200_infoperant_infocomplcont_views.s1200infoPerAntinfoComplContDetail.as_view() ),

url(r'^s1200-infoperant-infocomplcont/listar/(?P<hash>.*)/$', 
        s1200_infoperant_infocomplcont_views.listar, 
        name='s1200_infoperant_infocomplcont'),

url(r'^s1200-infoperant-infocomplcont/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_infocomplcont_views.salvar, 
        name='s1200_infoperant_infocomplcont_salvar'),



url(r'^s1200-infoperant-infotrabinterm/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_infotrabinterm_views.apagar, 
        name='s1200_infoperant_infotrabinterm_apagar'),

url(r'^s1200-infoperant-infotrabinterm/api/$',
            s1200_infoperant_infotrabinterm_views.s1200infoPerAntinfoTrabIntermList.as_view() ),

        url(r'^s1200-infoperant-infotrabinterm/api/(?P<pk>[0-9]+)/$',
            s1200_infoperant_infotrabinterm_views.s1200infoPerAntinfoTrabIntermDetail.as_view() ),

url(r'^s1200-infoperant-infotrabinterm/listar/(?P<hash>.*)/$', 
        s1200_infoperant_infotrabinterm_views.listar, 
        name='s1200_infoperant_infotrabinterm'),

url(r'^s1200-infoperant-infotrabinterm/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_infotrabinterm_views.salvar, 
        name='s1200_infoperant_infotrabinterm_salvar'),



url(r'^s1200-infoperant-itensremun/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_itensremun_views.apagar, 
        name='s1200_infoperant_itensremun_apagar'),

url(r'^s1200-infoperant-itensremun/api/$',
            s1200_infoperant_itensremun_views.s1200infoPerAntitensRemunList.as_view() ),

        url(r'^s1200-infoperant-itensremun/api/(?P<pk>[0-9]+)/$',
            s1200_infoperant_itensremun_views.s1200infoPerAntitensRemunDetail.as_view() ),

url(r'^s1200-infoperant-itensremun/listar/(?P<hash>.*)/$', 
        s1200_infoperant_itensremun_views.listar, 
        name='s1200_infoperant_itensremun'),

url(r'^s1200-infoperant-itensremun/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_itensremun_views.salvar, 
        name='s1200_infoperant_itensremun_salvar'),



url(r'^s1200-infoperant-remunperant/apagar/(?P<hash>.*)/$', 
        s1200_infoperant_remunperant_views.apagar, 
        name='s1200_infoperant_remunperant_apagar'),

url(r'^s1200-infoperant-remunperant/api/$',
            s1200_infoperant_remunperant_views.s1200infoPerAntremunPerAntList.as_view() ),

        url(r'^s1200-infoperant-remunperant/api/(?P<pk>[0-9]+)/$',
            s1200_infoperant_remunperant_views.s1200infoPerAntremunPerAntDetail.as_view() ),

url(r'^s1200-infoperant-remunperant/listar/(?P<hash>.*)/$', 
        s1200_infoperant_remunperant_views.listar, 
        name='s1200_infoperant_remunperant'),

url(r'^s1200-infoperant-remunperant/salvar/(?P<hash>.*)/$', 
        s1200_infoperant_remunperant_views.salvar, 
        name='s1200_infoperant_remunperant_salvar'),



url(r'^s1200-infoperapur-detoper/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_detoper_views.apagar, 
        name='s1200_infoperapur_detoper_apagar'),

url(r'^s1200-infoperapur-detoper/api/$',
            s1200_infoperapur_detoper_views.s1200infoPerApurdetOperList.as_view() ),

        url(r'^s1200-infoperapur-detoper/api/(?P<pk>[0-9]+)/$',
            s1200_infoperapur_detoper_views.s1200infoPerApurdetOperDetail.as_view() ),

url(r'^s1200-infoperapur-detoper/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_detoper_views.listar, 
        name='s1200_infoperapur_detoper'),

url(r'^s1200-infoperapur-detoper/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_detoper_views.salvar, 
        name='s1200_infoperapur_detoper_salvar'),



url(r'^s1200-infoperapur-detplano/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_detplano_views.apagar, 
        name='s1200_infoperapur_detplano_apagar'),

url(r'^s1200-infoperapur-detplano/api/$',
            s1200_infoperapur_detplano_views.s1200infoPerApurdetPlanoList.as_view() ),

        url(r'^s1200-infoperapur-detplano/api/(?P<pk>[0-9]+)/$',
            s1200_infoperapur_detplano_views.s1200infoPerApurdetPlanoDetail.as_view() ),

url(r'^s1200-infoperapur-detplano/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_detplano_views.listar, 
        name='s1200_infoperapur_detplano'),

url(r'^s1200-infoperapur-detplano/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_detplano_views.salvar, 
        name='s1200_infoperapur_detplano_salvar'),



url(r'^s1200-infoperapur-ideestablot/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_ideestablot_views.apagar, 
        name='s1200_infoperapur_ideestablot_apagar'),

url(r'^s1200-infoperapur-ideestablot/api/$',
            s1200_infoperapur_ideestablot_views.s1200infoPerApurideEstabLotList.as_view() ),

        url(r'^s1200-infoperapur-ideestablot/api/(?P<pk>[0-9]+)/$',
            s1200_infoperapur_ideestablot_views.s1200infoPerApurideEstabLotDetail.as_view() ),

url(r'^s1200-infoperapur-ideestablot/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_ideestablot_views.listar, 
        name='s1200_infoperapur_ideestablot'),

url(r'^s1200-infoperapur-ideestablot/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_ideestablot_views.salvar, 
        name='s1200_infoperapur_ideestablot_salvar'),



url(r'^s1200-infoperapur-infoagnocivo/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_infoagnocivo_views.apagar, 
        name='s1200_infoperapur_infoagnocivo_apagar'),

url(r'^s1200-infoperapur-infoagnocivo/api/$',
            s1200_infoperapur_infoagnocivo_views.s1200infoPerApurinfoAgNocivoList.as_view() ),

        url(r'^s1200-infoperapur-infoagnocivo/api/(?P<pk>[0-9]+)/$',
            s1200_infoperapur_infoagnocivo_views.s1200infoPerApurinfoAgNocivoDetail.as_view() ),

url(r'^s1200-infoperapur-infoagnocivo/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_infoagnocivo_views.listar, 
        name='s1200_infoperapur_infoagnocivo'),

url(r'^s1200-infoperapur-infoagnocivo/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_infoagnocivo_views.salvar, 
        name='s1200_infoperapur_infoagnocivo_salvar'),



url(r'^s1200-infoperapur-infotrabinterm/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_infotrabinterm_views.apagar, 
        name='s1200_infoperapur_infotrabinterm_apagar'),

url(r'^s1200-infoperapur-infotrabinterm/api/$',
            s1200_infoperapur_infotrabinterm_views.s1200infoPerApurinfoTrabIntermList.as_view() ),

        url(r'^s1200-infoperapur-infotrabinterm/api/(?P<pk>[0-9]+)/$',
            s1200_infoperapur_infotrabinterm_views.s1200infoPerApurinfoTrabIntermDetail.as_view() ),

url(r'^s1200-infoperapur-infotrabinterm/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_infotrabinterm_views.listar, 
        name='s1200_infoperapur_infotrabinterm'),

url(r'^s1200-infoperapur-infotrabinterm/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_infotrabinterm_views.salvar, 
        name='s1200_infoperapur_infotrabinterm_salvar'),



url(r'^s1200-infoperapur-itensremun/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_itensremun_views.apagar, 
        name='s1200_infoperapur_itensremun_apagar'),

url(r'^s1200-infoperapur-itensremun/api/$',
            s1200_infoperapur_itensremun_views.s1200infoPerApuritensRemunList.as_view() ),

        url(r'^s1200-infoperapur-itensremun/api/(?P<pk>[0-9]+)/$',
            s1200_infoperapur_itensremun_views.s1200infoPerApuritensRemunDetail.as_view() ),

url(r'^s1200-infoperapur-itensremun/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_itensremun_views.listar, 
        name='s1200_infoperapur_itensremun'),

url(r'^s1200-infoperapur-itensremun/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_itensremun_views.salvar, 
        name='s1200_infoperapur_itensremun_salvar'),



url(r'^s1200-infoperapur-remunperapur/apagar/(?P<hash>.*)/$', 
        s1200_infoperapur_remunperapur_views.apagar, 
        name='s1200_infoperapur_remunperapur_apagar'),

url(r'^s1200-infoperapur-remunperapur/api/$',
            s1200_infoperapur_remunperapur_views.s1200infoPerApurremunPerApurList.as_view() ),

        url(r'^s1200-infoperapur-remunperapur/api/(?P<pk>[0-9]+)/$',
            s1200_infoperapur_remunperapur_views.s1200infoPerApurremunPerApurDetail.as_view() ),

url(r'^s1200-infoperapur-remunperapur/listar/(?P<hash>.*)/$', 
        s1200_infoperapur_remunperapur_views.listar, 
        name='s1200_infoperapur_remunperapur'),

url(r'^s1200-infoperapur-remunperapur/salvar/(?P<hash>.*)/$', 
        s1200_infoperapur_remunperapur_views.salvar, 
        name='s1200_infoperapur_remunperapur_salvar'),



url(r'^s1200-procjudtrab/apagar/(?P<hash>.*)/$', 
        s1200_procjudtrab_views.apagar, 
        name='s1200_procjudtrab_apagar'),

url(r'^s1200-procjudtrab/api/$',
            s1200_procjudtrab_views.s1200procJudTrabList.as_view() ),

        url(r'^s1200-procjudtrab/api/(?P<pk>[0-9]+)/$',
            s1200_procjudtrab_views.s1200procJudTrabDetail.as_view() ),

url(r'^s1200-procjudtrab/listar/(?P<hash>.*)/$', 
        s1200_procjudtrab_views.listar, 
        name='s1200_procjudtrab'),

url(r'^s1200-procjudtrab/salvar/(?P<hash>.*)/$', 
        s1200_procjudtrab_views.salvar, 
        name='s1200_procjudtrab_salvar'),



url(r'^s1200-remunoutrempr/apagar/(?P<hash>.*)/$', 
        s1200_remunoutrempr_views.apagar, 
        name='s1200_remunoutrempr_apagar'),

url(r'^s1200-remunoutrempr/api/$',
            s1200_remunoutrempr_views.s1200remunOutrEmprList.as_view() ),

        url(r'^s1200-remunoutrempr/api/(?P<pk>[0-9]+)/$',
            s1200_remunoutrempr_views.s1200remunOutrEmprDetail.as_view() ),

url(r'^s1200-remunoutrempr/listar/(?P<hash>.*)/$', 
        s1200_remunoutrempr_views.listar, 
        name='s1200_remunoutrempr'),

url(r'^s1200-remunoutrempr/salvar/(?P<hash>.*)/$', 
        s1200_remunoutrempr_views.salvar, 
        name='s1200_remunoutrempr_salvar'),



url(r'^s1200-sucessaovinc/apagar/(?P<hash>.*)/$', 
        s1200_sucessaovinc_views.apagar, 
        name='s1200_sucessaovinc_apagar'),

url(r'^s1200-sucessaovinc/api/$',
            s1200_sucessaovinc_views.s1200sucessaoVincList.as_view() ),

        url(r'^s1200-sucessaovinc/api/(?P<pk>[0-9]+)/$',
            s1200_sucessaovinc_views.s1200sucessaoVincDetail.as_view() ),

url(r'^s1200-sucessaovinc/listar/(?P<hash>.*)/$', 
        s1200_sucessaovinc_views.listar, 
        name='s1200_sucessaovinc'),

url(r'^s1200-sucessaovinc/salvar/(?P<hash>.*)/$', 
        s1200_sucessaovinc_views.salvar, 
        name='s1200_sucessaovinc_salvar'),





]