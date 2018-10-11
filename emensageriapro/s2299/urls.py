#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2299.views import s2299_observacoes as s2299_observacoes_views
from emensageriapro.s2299.views import s2299_sucessaovinc as s2299_sucessaovinc_views
from emensageriapro.s2299.views import s2299_transftit as s2299_transftit_views
from emensageriapro.s2299.views import s2299_verbasresc as s2299_verbasresc_views
from emensageriapro.s2299.views import s2299_dmdev as s2299_dmdev_views
from emensageriapro.s2299.views import s2299_infoperapur as s2299_infoperapur_views
from emensageriapro.s2299.views import s2299_infoperapur_ideestablot as s2299_infoperapur_ideestablot_views
from emensageriapro.s2299.views import s2299_infoperapur_detverbas as s2299_infoperapur_detverbas_views
from emensageriapro.s2299.views import s2299_infoperapur_infosaudecolet as s2299_infoperapur_infosaudecolet_views
from emensageriapro.s2299.views import s2299_infoperapur_detoper as s2299_infoperapur_detoper_views
from emensageriapro.s2299.views import s2299_infoperapur_detplano as s2299_infoperapur_detplano_views
from emensageriapro.s2299.views import s2299_infoperapur_infoagnocivo as s2299_infoperapur_infoagnocivo_views
from emensageriapro.s2299.views import s2299_infoperapur_infosimples as s2299_infoperapur_infosimples_views
from emensageriapro.s2299.views import s2299_infotrabinterm_proccs as s2299_infotrabinterm_proccs_views
from emensageriapro.s2299.views import s2299_infotrabinterm_quarentena as s2299_infotrabinterm_quarentena_views
from emensageriapro.s2299.views import s2299_infoperant as s2299_infoperant_views
from emensageriapro.s2299.views import s2299_infoperant_ideadc as s2299_infoperant_ideadc_views
from emensageriapro.s2299.views import s2299_infoperant_ideperiodo as s2299_infoperant_ideperiodo_views
from emensageriapro.s2299.views import s2299_infoperant_ideestablot as s2299_infoperant_ideestablot_views
from emensageriapro.s2299.views import s2299_infoperant_detverbas as s2299_infoperant_detverbas_views
from emensageriapro.s2299.views import s2299_infoperant_infoagnocivo as s2299_infoperant_infoagnocivo_views
from emensageriapro.s2299.views import s2299_infoperant_infosimples as s2299_infoperant_infosimples_views
from emensageriapro.s2299.views import s2299_infotrabinterm as s2299_infotrabinterm_views
from emensageriapro.s2299.views import s2299_infotrabinterm_procjudtrab as s2299_infotrabinterm_procjudtrab_views
from emensageriapro.s2299.views import s2299_infotrabinterm_infomv as s2299_infotrabinterm_infomv_views
from emensageriapro.s2299.views import s2299_infotrabinterm_remunoutrempr as s2299_infotrabinterm_remunoutrempr_views
from emensageriapro.s2299.views import s2299_infotrabinterm_consigfgts as s2299_infotrabinterm_consigfgts_views



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



url(r'^s2299-observacoes/apagar/(?P<hash>.*)/$', 
        s2299_observacoes_views.apagar, 
        name='s2299_observacoes_apagar'),

url(r'^s2299-observacoes/api/$',
            s2299_observacoes_views.s2299observacoesList.as_view() ),

        url(r'^s2299-observacoes/api/(?P<pk>[0-9]+)/$',
            s2299_observacoes_views.s2299observacoesDetail.as_view() ),

url(r'^s2299-observacoes/listar/(?P<hash>.*)/$', 
        s2299_observacoes_views.listar, 
        name='s2299_observacoes'),

url(r'^s2299-observacoes/salvar/(?P<hash>.*)/$', 
        s2299_observacoes_views.salvar, 
        name='s2299_observacoes_salvar'),



url(r'^s2299-sucessaovinc/apagar/(?P<hash>.*)/$', 
        s2299_sucessaovinc_views.apagar, 
        name='s2299_sucessaovinc_apagar'),

url(r'^s2299-sucessaovinc/api/$',
            s2299_sucessaovinc_views.s2299sucessaoVincList.as_view() ),

        url(r'^s2299-sucessaovinc/api/(?P<pk>[0-9]+)/$',
            s2299_sucessaovinc_views.s2299sucessaoVincDetail.as_view() ),

url(r'^s2299-sucessaovinc/listar/(?P<hash>.*)/$', 
        s2299_sucessaovinc_views.listar, 
        name='s2299_sucessaovinc'),

url(r'^s2299-sucessaovinc/salvar/(?P<hash>.*)/$', 
        s2299_sucessaovinc_views.salvar, 
        name='s2299_sucessaovinc_salvar'),



url(r'^s2299-transftit/apagar/(?P<hash>.*)/$', 
        s2299_transftit_views.apagar, 
        name='s2299_transftit_apagar'),

url(r'^s2299-transftit/api/$',
            s2299_transftit_views.s2299transfTitList.as_view() ),

        url(r'^s2299-transftit/api/(?P<pk>[0-9]+)/$',
            s2299_transftit_views.s2299transfTitDetail.as_view() ),

url(r'^s2299-transftit/listar/(?P<hash>.*)/$', 
        s2299_transftit_views.listar, 
        name='s2299_transftit'),

url(r'^s2299-transftit/salvar/(?P<hash>.*)/$', 
        s2299_transftit_views.salvar, 
        name='s2299_transftit_salvar'),



url(r'^s2299-verbasresc/apagar/(?P<hash>.*)/$', 
        s2299_verbasresc_views.apagar, 
        name='s2299_verbasresc_apagar'),

url(r'^s2299-verbasresc/api/$',
            s2299_verbasresc_views.s2299verbasRescList.as_view() ),

        url(r'^s2299-verbasresc/api/(?P<pk>[0-9]+)/$',
            s2299_verbasresc_views.s2299verbasRescDetail.as_view() ),

url(r'^s2299-verbasresc/listar/(?P<hash>.*)/$', 
        s2299_verbasresc_views.listar, 
        name='s2299_verbasresc'),

url(r'^s2299-verbasresc/salvar/(?P<hash>.*)/$', 
        s2299_verbasresc_views.salvar, 
        name='s2299_verbasresc_salvar'),



url(r'^s2299-dmdev/apagar/(?P<hash>.*)/$', 
        s2299_dmdev_views.apagar, 
        name='s2299_dmdev_apagar'),

url(r'^s2299-dmdev/api/$',
            s2299_dmdev_views.s2299dmDevList.as_view() ),

        url(r'^s2299-dmdev/api/(?P<pk>[0-9]+)/$',
            s2299_dmdev_views.s2299dmDevDetail.as_view() ),

url(r'^s2299-dmdev/listar/(?P<hash>.*)/$', 
        s2299_dmdev_views.listar, 
        name='s2299_dmdev'),

url(r'^s2299-dmdev/salvar/(?P<hash>.*)/$', 
        s2299_dmdev_views.salvar, 
        name='s2299_dmdev_salvar'),



url(r'^s2299-infoperapur/apagar/(?P<hash>.*)/$', 
        s2299_infoperapur_views.apagar, 
        name='s2299_infoperapur_apagar'),

url(r'^s2299-infoperapur/api/$',
            s2299_infoperapur_views.s2299infoPerApurList.as_view() ),

        url(r'^s2299-infoperapur/api/(?P<pk>[0-9]+)/$',
            s2299_infoperapur_views.s2299infoPerApurDetail.as_view() ),

url(r'^s2299-infoperapur/listar/(?P<hash>.*)/$', 
        s2299_infoperapur_views.listar, 
        name='s2299_infoperapur'),

url(r'^s2299-infoperapur/salvar/(?P<hash>.*)/$', 
        s2299_infoperapur_views.salvar, 
        name='s2299_infoperapur_salvar'),



url(r'^s2299-infoperapur-ideestablot/apagar/(?P<hash>.*)/$', 
        s2299_infoperapur_ideestablot_views.apagar, 
        name='s2299_infoperapur_ideestablot_apagar'),

url(r'^s2299-infoperapur-ideestablot/api/$',
            s2299_infoperapur_ideestablot_views.s2299infoPerApurideEstabLotList.as_view() ),

        url(r'^s2299-infoperapur-ideestablot/api/(?P<pk>[0-9]+)/$',
            s2299_infoperapur_ideestablot_views.s2299infoPerApurideEstabLotDetail.as_view() ),

url(r'^s2299-infoperapur-ideestablot/listar/(?P<hash>.*)/$', 
        s2299_infoperapur_ideestablot_views.listar, 
        name='s2299_infoperapur_ideestablot'),

url(r'^s2299-infoperapur-ideestablot/salvar/(?P<hash>.*)/$', 
        s2299_infoperapur_ideestablot_views.salvar, 
        name='s2299_infoperapur_ideestablot_salvar'),



url(r'^s2299-infoperapur-detverbas/apagar/(?P<hash>.*)/$', 
        s2299_infoperapur_detverbas_views.apagar, 
        name='s2299_infoperapur_detverbas_apagar'),

url(r'^s2299-infoperapur-detverbas/api/$',
            s2299_infoperapur_detverbas_views.s2299infoPerApurdetVerbasList.as_view() ),

        url(r'^s2299-infoperapur-detverbas/api/(?P<pk>[0-9]+)/$',
            s2299_infoperapur_detverbas_views.s2299infoPerApurdetVerbasDetail.as_view() ),

url(r'^s2299-infoperapur-detverbas/listar/(?P<hash>.*)/$', 
        s2299_infoperapur_detverbas_views.listar, 
        name='s2299_infoperapur_detverbas'),

url(r'^s2299-infoperapur-detverbas/salvar/(?P<hash>.*)/$', 
        s2299_infoperapur_detverbas_views.salvar, 
        name='s2299_infoperapur_detverbas_salvar'),



url(r'^s2299-infoperapur-infosaudecolet/apagar/(?P<hash>.*)/$', 
        s2299_infoperapur_infosaudecolet_views.apagar, 
        name='s2299_infoperapur_infosaudecolet_apagar'),

url(r'^s2299-infoperapur-infosaudecolet/api/$',
            s2299_infoperapur_infosaudecolet_views.s2299infoPerApurinfoSaudeColetList.as_view() ),

        url(r'^s2299-infoperapur-infosaudecolet/api/(?P<pk>[0-9]+)/$',
            s2299_infoperapur_infosaudecolet_views.s2299infoPerApurinfoSaudeColetDetail.as_view() ),

url(r'^s2299-infoperapur-infosaudecolet/listar/(?P<hash>.*)/$', 
        s2299_infoperapur_infosaudecolet_views.listar, 
        name='s2299_infoperapur_infosaudecolet'),

url(r'^s2299-infoperapur-infosaudecolet/salvar/(?P<hash>.*)/$', 
        s2299_infoperapur_infosaudecolet_views.salvar, 
        name='s2299_infoperapur_infosaudecolet_salvar'),



url(r'^s2299-infoperapur-detoper/apagar/(?P<hash>.*)/$', 
        s2299_infoperapur_detoper_views.apagar, 
        name='s2299_infoperapur_detoper_apagar'),

url(r'^s2299-infoperapur-detoper/api/$',
            s2299_infoperapur_detoper_views.s2299infoPerApurdetOperList.as_view() ),

        url(r'^s2299-infoperapur-detoper/api/(?P<pk>[0-9]+)/$',
            s2299_infoperapur_detoper_views.s2299infoPerApurdetOperDetail.as_view() ),

url(r'^s2299-infoperapur-detoper/listar/(?P<hash>.*)/$', 
        s2299_infoperapur_detoper_views.listar, 
        name='s2299_infoperapur_detoper'),

url(r'^s2299-infoperapur-detoper/salvar/(?P<hash>.*)/$', 
        s2299_infoperapur_detoper_views.salvar, 
        name='s2299_infoperapur_detoper_salvar'),



url(r'^s2299-infoperapur-detplano/apagar/(?P<hash>.*)/$', 
        s2299_infoperapur_detplano_views.apagar, 
        name='s2299_infoperapur_detplano_apagar'),

url(r'^s2299-infoperapur-detplano/api/$',
            s2299_infoperapur_detplano_views.s2299infoPerApurdetPlanoList.as_view() ),

        url(r'^s2299-infoperapur-detplano/api/(?P<pk>[0-9]+)/$',
            s2299_infoperapur_detplano_views.s2299infoPerApurdetPlanoDetail.as_view() ),

url(r'^s2299-infoperapur-detplano/listar/(?P<hash>.*)/$', 
        s2299_infoperapur_detplano_views.listar, 
        name='s2299_infoperapur_detplano'),

url(r'^s2299-infoperapur-detplano/salvar/(?P<hash>.*)/$', 
        s2299_infoperapur_detplano_views.salvar, 
        name='s2299_infoperapur_detplano_salvar'),



url(r'^s2299-infoperapur-infoagnocivo/apagar/(?P<hash>.*)/$', 
        s2299_infoperapur_infoagnocivo_views.apagar, 
        name='s2299_infoperapur_infoagnocivo_apagar'),

url(r'^s2299-infoperapur-infoagnocivo/api/$',
            s2299_infoperapur_infoagnocivo_views.s2299infoPerApurinfoAgNocivoList.as_view() ),

        url(r'^s2299-infoperapur-infoagnocivo/api/(?P<pk>[0-9]+)/$',
            s2299_infoperapur_infoagnocivo_views.s2299infoPerApurinfoAgNocivoDetail.as_view() ),

url(r'^s2299-infoperapur-infoagnocivo/listar/(?P<hash>.*)/$', 
        s2299_infoperapur_infoagnocivo_views.listar, 
        name='s2299_infoperapur_infoagnocivo'),

url(r'^s2299-infoperapur-infoagnocivo/salvar/(?P<hash>.*)/$', 
        s2299_infoperapur_infoagnocivo_views.salvar, 
        name='s2299_infoperapur_infoagnocivo_salvar'),



url(r'^s2299-infoperapur-infosimples/apagar/(?P<hash>.*)/$', 
        s2299_infoperapur_infosimples_views.apagar, 
        name='s2299_infoperapur_infosimples_apagar'),

url(r'^s2299-infoperapur-infosimples/api/$',
            s2299_infoperapur_infosimples_views.s2299infoPerApurinfoSimplesList.as_view() ),

        url(r'^s2299-infoperapur-infosimples/api/(?P<pk>[0-9]+)/$',
            s2299_infoperapur_infosimples_views.s2299infoPerApurinfoSimplesDetail.as_view() ),

url(r'^s2299-infoperapur-infosimples/listar/(?P<hash>.*)/$', 
        s2299_infoperapur_infosimples_views.listar, 
        name='s2299_infoperapur_infosimples'),

url(r'^s2299-infoperapur-infosimples/salvar/(?P<hash>.*)/$', 
        s2299_infoperapur_infosimples_views.salvar, 
        name='s2299_infoperapur_infosimples_salvar'),



url(r'^s2299-infotrabinterm-proccs/apagar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_proccs_views.apagar, 
        name='s2299_infotrabinterm_proccs_apagar'),

url(r'^s2299-infotrabinterm-proccs/api/$',
            s2299_infotrabinterm_proccs_views.s2299infoTrabIntermprocCSList.as_view() ),

        url(r'^s2299-infotrabinterm-proccs/api/(?P<pk>[0-9]+)/$',
            s2299_infotrabinterm_proccs_views.s2299infoTrabIntermprocCSDetail.as_view() ),

url(r'^s2299-infotrabinterm-proccs/listar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_proccs_views.listar, 
        name='s2299_infotrabinterm_proccs'),

url(r'^s2299-infotrabinterm-proccs/salvar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_proccs_views.salvar, 
        name='s2299_infotrabinterm_proccs_salvar'),



url(r'^s2299-infotrabinterm-quarentena/apagar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_quarentena_views.apagar, 
        name='s2299_infotrabinterm_quarentena_apagar'),

url(r'^s2299-infotrabinterm-quarentena/api/$',
            s2299_infotrabinterm_quarentena_views.s2299infoTrabIntermquarentenaList.as_view() ),

        url(r'^s2299-infotrabinterm-quarentena/api/(?P<pk>[0-9]+)/$',
            s2299_infotrabinterm_quarentena_views.s2299infoTrabIntermquarentenaDetail.as_view() ),

url(r'^s2299-infotrabinterm-quarentena/listar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_quarentena_views.listar, 
        name='s2299_infotrabinterm_quarentena'),

url(r'^s2299-infotrabinterm-quarentena/salvar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_quarentena_views.salvar, 
        name='s2299_infotrabinterm_quarentena_salvar'),



url(r'^s2299-infoperant/apagar/(?P<hash>.*)/$', 
        s2299_infoperant_views.apagar, 
        name='s2299_infoperant_apagar'),

url(r'^s2299-infoperant/api/$',
            s2299_infoperant_views.s2299infoPerAntList.as_view() ),

        url(r'^s2299-infoperant/api/(?P<pk>[0-9]+)/$',
            s2299_infoperant_views.s2299infoPerAntDetail.as_view() ),

url(r'^s2299-infoperant/listar/(?P<hash>.*)/$', 
        s2299_infoperant_views.listar, 
        name='s2299_infoperant'),

url(r'^s2299-infoperant/salvar/(?P<hash>.*)/$', 
        s2299_infoperant_views.salvar, 
        name='s2299_infoperant_salvar'),



url(r'^s2299-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        s2299_infoperant_ideadc_views.apagar, 
        name='s2299_infoperant_ideadc_apagar'),

url(r'^s2299-infoperant-ideadc/api/$',
            s2299_infoperant_ideadc_views.s2299infoPerAntideADCList.as_view() ),

        url(r'^s2299-infoperant-ideadc/api/(?P<pk>[0-9]+)/$',
            s2299_infoperant_ideadc_views.s2299infoPerAntideADCDetail.as_view() ),

url(r'^s2299-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        s2299_infoperant_ideadc_views.listar, 
        name='s2299_infoperant_ideadc'),

url(r'^s2299-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        s2299_infoperant_ideadc_views.salvar, 
        name='s2299_infoperant_ideadc_salvar'),



url(r'^s2299-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        s2299_infoperant_ideperiodo_views.apagar, 
        name='s2299_infoperant_ideperiodo_apagar'),

url(r'^s2299-infoperant-ideperiodo/api/$',
            s2299_infoperant_ideperiodo_views.s2299infoPerAntidePeriodoList.as_view() ),

        url(r'^s2299-infoperant-ideperiodo/api/(?P<pk>[0-9]+)/$',
            s2299_infoperant_ideperiodo_views.s2299infoPerAntidePeriodoDetail.as_view() ),

url(r'^s2299-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        s2299_infoperant_ideperiodo_views.listar, 
        name='s2299_infoperant_ideperiodo'),

url(r'^s2299-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        s2299_infoperant_ideperiodo_views.salvar, 
        name='s2299_infoperant_ideperiodo_salvar'),



url(r'^s2299-infoperant-ideestablot/apagar/(?P<hash>.*)/$', 
        s2299_infoperant_ideestablot_views.apagar, 
        name='s2299_infoperant_ideestablot_apagar'),

url(r'^s2299-infoperant-ideestablot/api/$',
            s2299_infoperant_ideestablot_views.s2299infoPerAntideEstabLotList.as_view() ),

        url(r'^s2299-infoperant-ideestablot/api/(?P<pk>[0-9]+)/$',
            s2299_infoperant_ideestablot_views.s2299infoPerAntideEstabLotDetail.as_view() ),

url(r'^s2299-infoperant-ideestablot/listar/(?P<hash>.*)/$', 
        s2299_infoperant_ideestablot_views.listar, 
        name='s2299_infoperant_ideestablot'),

url(r'^s2299-infoperant-ideestablot/salvar/(?P<hash>.*)/$', 
        s2299_infoperant_ideestablot_views.salvar, 
        name='s2299_infoperant_ideestablot_salvar'),



url(r'^s2299-infoperant-detverbas/apagar/(?P<hash>.*)/$', 
        s2299_infoperant_detverbas_views.apagar, 
        name='s2299_infoperant_detverbas_apagar'),

url(r'^s2299-infoperant-detverbas/api/$',
            s2299_infoperant_detverbas_views.s2299infoPerAntdetVerbasList.as_view() ),

        url(r'^s2299-infoperant-detverbas/api/(?P<pk>[0-9]+)/$',
            s2299_infoperant_detverbas_views.s2299infoPerAntdetVerbasDetail.as_view() ),

url(r'^s2299-infoperant-detverbas/listar/(?P<hash>.*)/$', 
        s2299_infoperant_detverbas_views.listar, 
        name='s2299_infoperant_detverbas'),

url(r'^s2299-infoperant-detverbas/salvar/(?P<hash>.*)/$', 
        s2299_infoperant_detverbas_views.salvar, 
        name='s2299_infoperant_detverbas_salvar'),



url(r'^s2299-infoperant-infoagnocivo/apagar/(?P<hash>.*)/$', 
        s2299_infoperant_infoagnocivo_views.apagar, 
        name='s2299_infoperant_infoagnocivo_apagar'),

url(r'^s2299-infoperant-infoagnocivo/api/$',
            s2299_infoperant_infoagnocivo_views.s2299infoPerAntinfoAgNocivoList.as_view() ),

        url(r'^s2299-infoperant-infoagnocivo/api/(?P<pk>[0-9]+)/$',
            s2299_infoperant_infoagnocivo_views.s2299infoPerAntinfoAgNocivoDetail.as_view() ),

url(r'^s2299-infoperant-infoagnocivo/listar/(?P<hash>.*)/$', 
        s2299_infoperant_infoagnocivo_views.listar, 
        name='s2299_infoperant_infoagnocivo'),

url(r'^s2299-infoperant-infoagnocivo/salvar/(?P<hash>.*)/$', 
        s2299_infoperant_infoagnocivo_views.salvar, 
        name='s2299_infoperant_infoagnocivo_salvar'),



url(r'^s2299-infoperant-infosimples/apagar/(?P<hash>.*)/$', 
        s2299_infoperant_infosimples_views.apagar, 
        name='s2299_infoperant_infosimples_apagar'),

url(r'^s2299-infoperant-infosimples/api/$',
            s2299_infoperant_infosimples_views.s2299infoPerAntinfoSimplesList.as_view() ),

        url(r'^s2299-infoperant-infosimples/api/(?P<pk>[0-9]+)/$',
            s2299_infoperant_infosimples_views.s2299infoPerAntinfoSimplesDetail.as_view() ),

url(r'^s2299-infoperant-infosimples/listar/(?P<hash>.*)/$', 
        s2299_infoperant_infosimples_views.listar, 
        name='s2299_infoperant_infosimples'),

url(r'^s2299-infoperant-infosimples/salvar/(?P<hash>.*)/$', 
        s2299_infoperant_infosimples_views.salvar, 
        name='s2299_infoperant_infosimples_salvar'),



url(r'^s2299-infotrabinterm/apagar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_views.apagar, 
        name='s2299_infotrabinterm_apagar'),

url(r'^s2299-infotrabinterm/api/$',
            s2299_infotrabinterm_views.s2299infoTrabIntermList.as_view() ),

        url(r'^s2299-infotrabinterm/api/(?P<pk>[0-9]+)/$',
            s2299_infotrabinterm_views.s2299infoTrabIntermDetail.as_view() ),

url(r'^s2299-infotrabinterm/listar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_views.listar, 
        name='s2299_infotrabinterm'),

url(r'^s2299-infotrabinterm/salvar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_views.salvar, 
        name='s2299_infotrabinterm_salvar'),



url(r'^s2299-infotrabinterm-procjudtrab/apagar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_procjudtrab_views.apagar, 
        name='s2299_infotrabinterm_procjudtrab_apagar'),

url(r'^s2299-infotrabinterm-procjudtrab/api/$',
            s2299_infotrabinterm_procjudtrab_views.s2299infoTrabIntermprocJudTrabList.as_view() ),

        url(r'^s2299-infotrabinterm-procjudtrab/api/(?P<pk>[0-9]+)/$',
            s2299_infotrabinterm_procjudtrab_views.s2299infoTrabIntermprocJudTrabDetail.as_view() ),

url(r'^s2299-infotrabinterm-procjudtrab/listar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_procjudtrab_views.listar, 
        name='s2299_infotrabinterm_procjudtrab'),

url(r'^s2299-infotrabinterm-procjudtrab/salvar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_procjudtrab_views.salvar, 
        name='s2299_infotrabinterm_procjudtrab_salvar'),



url(r'^s2299-infotrabinterm-infomv/apagar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_infomv_views.apagar, 
        name='s2299_infotrabinterm_infomv_apagar'),

url(r'^s2299-infotrabinterm-infomv/api/$',
            s2299_infotrabinterm_infomv_views.s2299infoTrabInterminfoMVList.as_view() ),

        url(r'^s2299-infotrabinterm-infomv/api/(?P<pk>[0-9]+)/$',
            s2299_infotrabinterm_infomv_views.s2299infoTrabInterminfoMVDetail.as_view() ),

url(r'^s2299-infotrabinterm-infomv/listar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_infomv_views.listar, 
        name='s2299_infotrabinterm_infomv'),

url(r'^s2299-infotrabinterm-infomv/salvar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_infomv_views.salvar, 
        name='s2299_infotrabinterm_infomv_salvar'),



url(r'^s2299-infotrabinterm-remunoutrempr/apagar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_remunoutrempr_views.apagar, 
        name='s2299_infotrabinterm_remunoutrempr_apagar'),

url(r'^s2299-infotrabinterm-remunoutrempr/api/$',
            s2299_infotrabinterm_remunoutrempr_views.s2299infoTrabIntermremunOutrEmprList.as_view() ),

        url(r'^s2299-infotrabinterm-remunoutrempr/api/(?P<pk>[0-9]+)/$',
            s2299_infotrabinterm_remunoutrempr_views.s2299infoTrabIntermremunOutrEmprDetail.as_view() ),

url(r'^s2299-infotrabinterm-remunoutrempr/listar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_remunoutrempr_views.listar, 
        name='s2299_infotrabinterm_remunoutrempr'),

url(r'^s2299-infotrabinterm-remunoutrempr/salvar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_remunoutrempr_views.salvar, 
        name='s2299_infotrabinterm_remunoutrempr_salvar'),



url(r'^s2299-infotrabinterm-consigfgts/apagar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_consigfgts_views.apagar, 
        name='s2299_infotrabinterm_consigfgts_apagar'),

url(r'^s2299-infotrabinterm-consigfgts/api/$',
            s2299_infotrabinterm_consigfgts_views.s2299infoTrabIntermconsigFGTSList.as_view() ),

        url(r'^s2299-infotrabinterm-consigfgts/api/(?P<pk>[0-9]+)/$',
            s2299_infotrabinterm_consigfgts_views.s2299infoTrabIntermconsigFGTSDetail.as_view() ),

url(r'^s2299-infotrabinterm-consigfgts/listar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_consigfgts_views.listar, 
        name='s2299_infotrabinterm_consigfgts'),

url(r'^s2299-infotrabinterm-consigfgts/salvar/(?P<hash>.*)/$', 
        s2299_infotrabinterm_consigfgts_views.salvar, 
        name='s2299_infotrabinterm_consigfgts_salvar'),





]