#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2241.views import s2241_insalperic as s2241_insalperic_views
from emensageriapro.s2241.views import s2241_iniinsalperic as s2241_iniinsalperic_views
from emensageriapro.s2241.views import s2241_iniinsalperic_infoamb as s2241_iniinsalperic_infoamb_views
from emensageriapro.s2241.views import s2241_iniinsalperic_fatrisco as s2241_iniinsalperic_fatrisco_views
from emensageriapro.s2241.views import s2241_altinsalperic as s2241_altinsalperic_views
from emensageriapro.s2241.views import s2241_altinsalperic_infoamb as s2241_altinsalperic_infoamb_views
from emensageriapro.s2241.views import s2241_altinsalperic_fatrisco as s2241_altinsalperic_fatrisco_views
from emensageriapro.s2241.views import s2241_fiminsalperic as s2241_fiminsalperic_views
from emensageriapro.s2241.views import s2241_fiminsalperic_infoamb as s2241_fiminsalperic_infoamb_views
from emensageriapro.s2241.views import s2241_aposentesp as s2241_aposentesp_views
from emensageriapro.s2241.views import s2241_iniaposentesp as s2241_iniaposentesp_views
from emensageriapro.s2241.views import s2241_iniaposentesp_infoamb as s2241_iniaposentesp_infoamb_views
from emensageriapro.s2241.views import s2241_iniaposentesp_fatrisco as s2241_iniaposentesp_fatrisco_views
from emensageriapro.s2241.views import s2241_altaposentesp as s2241_altaposentesp_views
from emensageriapro.s2241.views import s2241_altaposentesp_infoamb as s2241_altaposentesp_infoamb_views
from emensageriapro.s2241.views import s2241_altaposentesp_fatrisco as s2241_altaposentesp_fatrisco_views
from emensageriapro.s2241.views import s2241_fimaposentesp as s2241_fimaposentesp_views
from emensageriapro.s2241.views import s2241_fimaposentesp_infoamb as s2241_fimaposentesp_infoamb_views



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



url(r'^s2241-insalperic/apagar/(?P<hash>.*)/$', 
        s2241_insalperic_views.apagar, 
        name='s2241_insalperic_apagar'),

url(r'^s2241-insalperic/api/$',
            s2241_insalperic_views.s2241insalPericList.as_view() ),

        url(r'^s2241-insalperic/api/(?P<pk>[0-9]+)/$',
            s2241_insalperic_views.s2241insalPericDetail.as_view() ),

url(r'^s2241-insalperic/listar/(?P<hash>.*)/$', 
        s2241_insalperic_views.listar, 
        name='s2241_insalperic'),

url(r'^s2241-insalperic/salvar/(?P<hash>.*)/$', 
        s2241_insalperic_views.salvar, 
        name='s2241_insalperic_salvar'),



url(r'^s2241-iniinsalperic/apagar/(?P<hash>.*)/$', 
        s2241_iniinsalperic_views.apagar, 
        name='s2241_iniinsalperic_apagar'),

url(r'^s2241-iniinsalperic/api/$',
            s2241_iniinsalperic_views.s2241iniInsalPericList.as_view() ),

        url(r'^s2241-iniinsalperic/api/(?P<pk>[0-9]+)/$',
            s2241_iniinsalperic_views.s2241iniInsalPericDetail.as_view() ),

url(r'^s2241-iniinsalperic/listar/(?P<hash>.*)/$', 
        s2241_iniinsalperic_views.listar, 
        name='s2241_iniinsalperic'),

url(r'^s2241-iniinsalperic/salvar/(?P<hash>.*)/$', 
        s2241_iniinsalperic_views.salvar, 
        name='s2241_iniinsalperic_salvar'),



url(r'^s2241-iniinsalperic-infoamb/apagar/(?P<hash>.*)/$', 
        s2241_iniinsalperic_infoamb_views.apagar, 
        name='s2241_iniinsalperic_infoamb_apagar'),

url(r'^s2241-iniinsalperic-infoamb/api/$',
            s2241_iniinsalperic_infoamb_views.s2241iniInsalPericinfoAmbList.as_view() ),

        url(r'^s2241-iniinsalperic-infoamb/api/(?P<pk>[0-9]+)/$',
            s2241_iniinsalperic_infoamb_views.s2241iniInsalPericinfoAmbDetail.as_view() ),

url(r'^s2241-iniinsalperic-infoamb/listar/(?P<hash>.*)/$', 
        s2241_iniinsalperic_infoamb_views.listar, 
        name='s2241_iniinsalperic_infoamb'),

url(r'^s2241-iniinsalperic-infoamb/salvar/(?P<hash>.*)/$', 
        s2241_iniinsalperic_infoamb_views.salvar, 
        name='s2241_iniinsalperic_infoamb_salvar'),



url(r'^s2241-iniinsalperic-fatrisco/apagar/(?P<hash>.*)/$', 
        s2241_iniinsalperic_fatrisco_views.apagar, 
        name='s2241_iniinsalperic_fatrisco_apagar'),

url(r'^s2241-iniinsalperic-fatrisco/api/$',
            s2241_iniinsalperic_fatrisco_views.s2241iniInsalPericfatRiscoList.as_view() ),

        url(r'^s2241-iniinsalperic-fatrisco/api/(?P<pk>[0-9]+)/$',
            s2241_iniinsalperic_fatrisco_views.s2241iniInsalPericfatRiscoDetail.as_view() ),

url(r'^s2241-iniinsalperic-fatrisco/listar/(?P<hash>.*)/$', 
        s2241_iniinsalperic_fatrisco_views.listar, 
        name='s2241_iniinsalperic_fatrisco'),

url(r'^s2241-iniinsalperic-fatrisco/salvar/(?P<hash>.*)/$', 
        s2241_iniinsalperic_fatrisco_views.salvar, 
        name='s2241_iniinsalperic_fatrisco_salvar'),



url(r'^s2241-altinsalperic/apagar/(?P<hash>.*)/$', 
        s2241_altinsalperic_views.apagar, 
        name='s2241_altinsalperic_apagar'),

url(r'^s2241-altinsalperic/api/$',
            s2241_altinsalperic_views.s2241altInsalPericList.as_view() ),

        url(r'^s2241-altinsalperic/api/(?P<pk>[0-9]+)/$',
            s2241_altinsalperic_views.s2241altInsalPericDetail.as_view() ),

url(r'^s2241-altinsalperic/listar/(?P<hash>.*)/$', 
        s2241_altinsalperic_views.listar, 
        name='s2241_altinsalperic'),

url(r'^s2241-altinsalperic/salvar/(?P<hash>.*)/$', 
        s2241_altinsalperic_views.salvar, 
        name='s2241_altinsalperic_salvar'),



url(r'^s2241-altinsalperic-infoamb/apagar/(?P<hash>.*)/$', 
        s2241_altinsalperic_infoamb_views.apagar, 
        name='s2241_altinsalperic_infoamb_apagar'),

url(r'^s2241-altinsalperic-infoamb/api/$',
            s2241_altinsalperic_infoamb_views.s2241altInsalPericinfoambList.as_view() ),

        url(r'^s2241-altinsalperic-infoamb/api/(?P<pk>[0-9]+)/$',
            s2241_altinsalperic_infoamb_views.s2241altInsalPericinfoambDetail.as_view() ),

url(r'^s2241-altinsalperic-infoamb/listar/(?P<hash>.*)/$', 
        s2241_altinsalperic_infoamb_views.listar, 
        name='s2241_altinsalperic_infoamb'),

url(r'^s2241-altinsalperic-infoamb/salvar/(?P<hash>.*)/$', 
        s2241_altinsalperic_infoamb_views.salvar, 
        name='s2241_altinsalperic_infoamb_salvar'),



url(r'^s2241-altinsalperic-fatrisco/apagar/(?P<hash>.*)/$', 
        s2241_altinsalperic_fatrisco_views.apagar, 
        name='s2241_altinsalperic_fatrisco_apagar'),

url(r'^s2241-altinsalperic-fatrisco/api/$',
            s2241_altinsalperic_fatrisco_views.s2241altInsalPericfatRiscoList.as_view() ),

        url(r'^s2241-altinsalperic-fatrisco/api/(?P<pk>[0-9]+)/$',
            s2241_altinsalperic_fatrisco_views.s2241altInsalPericfatRiscoDetail.as_view() ),

url(r'^s2241-altinsalperic-fatrisco/listar/(?P<hash>.*)/$', 
        s2241_altinsalperic_fatrisco_views.listar, 
        name='s2241_altinsalperic_fatrisco'),

url(r'^s2241-altinsalperic-fatrisco/salvar/(?P<hash>.*)/$', 
        s2241_altinsalperic_fatrisco_views.salvar, 
        name='s2241_altinsalperic_fatrisco_salvar'),



url(r'^s2241-fiminsalperic/apagar/(?P<hash>.*)/$', 
        s2241_fiminsalperic_views.apagar, 
        name='s2241_fiminsalperic_apagar'),

url(r'^s2241-fiminsalperic/api/$',
            s2241_fiminsalperic_views.s2241fimInsalPericList.as_view() ),

        url(r'^s2241-fiminsalperic/api/(?P<pk>[0-9]+)/$',
            s2241_fiminsalperic_views.s2241fimInsalPericDetail.as_view() ),

url(r'^s2241-fiminsalperic/listar/(?P<hash>.*)/$', 
        s2241_fiminsalperic_views.listar, 
        name='s2241_fiminsalperic'),

url(r'^s2241-fiminsalperic/salvar/(?P<hash>.*)/$', 
        s2241_fiminsalperic_views.salvar, 
        name='s2241_fiminsalperic_salvar'),



url(r'^s2241-fiminsalperic-infoamb/apagar/(?P<hash>.*)/$', 
        s2241_fiminsalperic_infoamb_views.apagar, 
        name='s2241_fiminsalperic_infoamb_apagar'),

url(r'^s2241-fiminsalperic-infoamb/api/$',
            s2241_fiminsalperic_infoamb_views.s2241fimInsalPericinfoAmbList.as_view() ),

        url(r'^s2241-fiminsalperic-infoamb/api/(?P<pk>[0-9]+)/$',
            s2241_fiminsalperic_infoamb_views.s2241fimInsalPericinfoAmbDetail.as_view() ),

url(r'^s2241-fiminsalperic-infoamb/listar/(?P<hash>.*)/$', 
        s2241_fiminsalperic_infoamb_views.listar, 
        name='s2241_fiminsalperic_infoamb'),

url(r'^s2241-fiminsalperic-infoamb/salvar/(?P<hash>.*)/$', 
        s2241_fiminsalperic_infoamb_views.salvar, 
        name='s2241_fiminsalperic_infoamb_salvar'),



url(r'^s2241-aposentesp/apagar/(?P<hash>.*)/$', 
        s2241_aposentesp_views.apagar, 
        name='s2241_aposentesp_apagar'),

url(r'^s2241-aposentesp/api/$',
            s2241_aposentesp_views.s2241aposentEspList.as_view() ),

        url(r'^s2241-aposentesp/api/(?P<pk>[0-9]+)/$',
            s2241_aposentesp_views.s2241aposentEspDetail.as_view() ),

url(r'^s2241-aposentesp/listar/(?P<hash>.*)/$', 
        s2241_aposentesp_views.listar, 
        name='s2241_aposentesp'),

url(r'^s2241-aposentesp/salvar/(?P<hash>.*)/$', 
        s2241_aposentesp_views.salvar, 
        name='s2241_aposentesp_salvar'),



url(r'^s2241-iniaposentesp/apagar/(?P<hash>.*)/$', 
        s2241_iniaposentesp_views.apagar, 
        name='s2241_iniaposentesp_apagar'),

url(r'^s2241-iniaposentesp/api/$',
            s2241_iniaposentesp_views.s2241iniAposentEspList.as_view() ),

        url(r'^s2241-iniaposentesp/api/(?P<pk>[0-9]+)/$',
            s2241_iniaposentesp_views.s2241iniAposentEspDetail.as_view() ),

url(r'^s2241-iniaposentesp/listar/(?P<hash>.*)/$', 
        s2241_iniaposentesp_views.listar, 
        name='s2241_iniaposentesp'),

url(r'^s2241-iniaposentesp/salvar/(?P<hash>.*)/$', 
        s2241_iniaposentesp_views.salvar, 
        name='s2241_iniaposentesp_salvar'),



url(r'^s2241-iniaposentesp-infoamb/apagar/(?P<hash>.*)/$', 
        s2241_iniaposentesp_infoamb_views.apagar, 
        name='s2241_iniaposentesp_infoamb_apagar'),

url(r'^s2241-iniaposentesp-infoamb/api/$',
            s2241_iniaposentesp_infoamb_views.s2241iniAposentEspinfoAmbList.as_view() ),

        url(r'^s2241-iniaposentesp-infoamb/api/(?P<pk>[0-9]+)/$',
            s2241_iniaposentesp_infoamb_views.s2241iniAposentEspinfoAmbDetail.as_view() ),

url(r'^s2241-iniaposentesp-infoamb/listar/(?P<hash>.*)/$', 
        s2241_iniaposentesp_infoamb_views.listar, 
        name='s2241_iniaposentesp_infoamb'),

url(r'^s2241-iniaposentesp-infoamb/salvar/(?P<hash>.*)/$', 
        s2241_iniaposentesp_infoamb_views.salvar, 
        name='s2241_iniaposentesp_infoamb_salvar'),



url(r'^s2241-iniaposentesp-fatrisco/apagar/(?P<hash>.*)/$', 
        s2241_iniaposentesp_fatrisco_views.apagar, 
        name='s2241_iniaposentesp_fatrisco_apagar'),

url(r'^s2241-iniaposentesp-fatrisco/api/$',
            s2241_iniaposentesp_fatrisco_views.s2241iniAposentEspfatRiscoList.as_view() ),

        url(r'^s2241-iniaposentesp-fatrisco/api/(?P<pk>[0-9]+)/$',
            s2241_iniaposentesp_fatrisco_views.s2241iniAposentEspfatRiscoDetail.as_view() ),

url(r'^s2241-iniaposentesp-fatrisco/listar/(?P<hash>.*)/$', 
        s2241_iniaposentesp_fatrisco_views.listar, 
        name='s2241_iniaposentesp_fatrisco'),

url(r'^s2241-iniaposentesp-fatrisco/salvar/(?P<hash>.*)/$', 
        s2241_iniaposentesp_fatrisco_views.salvar, 
        name='s2241_iniaposentesp_fatrisco_salvar'),



url(r'^s2241-altaposentesp/apagar/(?P<hash>.*)/$', 
        s2241_altaposentesp_views.apagar, 
        name='s2241_altaposentesp_apagar'),

url(r'^s2241-altaposentesp/api/$',
            s2241_altaposentesp_views.s2241altAposentEspList.as_view() ),

        url(r'^s2241-altaposentesp/api/(?P<pk>[0-9]+)/$',
            s2241_altaposentesp_views.s2241altAposentEspDetail.as_view() ),

url(r'^s2241-altaposentesp/listar/(?P<hash>.*)/$', 
        s2241_altaposentesp_views.listar, 
        name='s2241_altaposentesp'),

url(r'^s2241-altaposentesp/salvar/(?P<hash>.*)/$', 
        s2241_altaposentesp_views.salvar, 
        name='s2241_altaposentesp_salvar'),



url(r'^s2241-altaposentesp-infoamb/apagar/(?P<hash>.*)/$', 
        s2241_altaposentesp_infoamb_views.apagar, 
        name='s2241_altaposentesp_infoamb_apagar'),

url(r'^s2241-altaposentesp-infoamb/api/$',
            s2241_altaposentesp_infoamb_views.s2241altAposentEspinfoambList.as_view() ),

        url(r'^s2241-altaposentesp-infoamb/api/(?P<pk>[0-9]+)/$',
            s2241_altaposentesp_infoamb_views.s2241altAposentEspinfoambDetail.as_view() ),

url(r'^s2241-altaposentesp-infoamb/listar/(?P<hash>.*)/$', 
        s2241_altaposentesp_infoamb_views.listar, 
        name='s2241_altaposentesp_infoamb'),

url(r'^s2241-altaposentesp-infoamb/salvar/(?P<hash>.*)/$', 
        s2241_altaposentesp_infoamb_views.salvar, 
        name='s2241_altaposentesp_infoamb_salvar'),



url(r'^s2241-altaposentesp-fatrisco/apagar/(?P<hash>.*)/$', 
        s2241_altaposentesp_fatrisco_views.apagar, 
        name='s2241_altaposentesp_fatrisco_apagar'),

url(r'^s2241-altaposentesp-fatrisco/api/$',
            s2241_altaposentesp_fatrisco_views.s2241altAposentEspfatRiscoList.as_view() ),

        url(r'^s2241-altaposentesp-fatrisco/api/(?P<pk>[0-9]+)/$',
            s2241_altaposentesp_fatrisco_views.s2241altAposentEspfatRiscoDetail.as_view() ),

url(r'^s2241-altaposentesp-fatrisco/listar/(?P<hash>.*)/$', 
        s2241_altaposentesp_fatrisco_views.listar, 
        name='s2241_altaposentesp_fatrisco'),

url(r'^s2241-altaposentesp-fatrisco/salvar/(?P<hash>.*)/$', 
        s2241_altaposentesp_fatrisco_views.salvar, 
        name='s2241_altaposentesp_fatrisco_salvar'),



url(r'^s2241-fimaposentesp/apagar/(?P<hash>.*)/$', 
        s2241_fimaposentesp_views.apagar, 
        name='s2241_fimaposentesp_apagar'),

url(r'^s2241-fimaposentesp/api/$',
            s2241_fimaposentesp_views.s2241fimAposentEspList.as_view() ),

        url(r'^s2241-fimaposentesp/api/(?P<pk>[0-9]+)/$',
            s2241_fimaposentesp_views.s2241fimAposentEspDetail.as_view() ),

url(r'^s2241-fimaposentesp/listar/(?P<hash>.*)/$', 
        s2241_fimaposentesp_views.listar, 
        name='s2241_fimaposentesp'),

url(r'^s2241-fimaposentesp/salvar/(?P<hash>.*)/$', 
        s2241_fimaposentesp_views.salvar, 
        name='s2241_fimaposentesp_salvar'),



url(r'^s2241-fimaposentesp-infoamb/apagar/(?P<hash>.*)/$', 
        s2241_fimaposentesp_infoamb_views.apagar, 
        name='s2241_fimaposentesp_infoamb_apagar'),

url(r'^s2241-fimaposentesp-infoamb/api/$',
            s2241_fimaposentesp_infoamb_views.s2241fimAposentEspinfoAmbList.as_view() ),

        url(r'^s2241-fimaposentesp-infoamb/api/(?P<pk>[0-9]+)/$',
            s2241_fimaposentesp_infoamb_views.s2241fimAposentEspinfoAmbDetail.as_view() ),

url(r'^s2241-fimaposentesp-infoamb/listar/(?P<hash>.*)/$', 
        s2241_fimaposentesp_infoamb_views.listar, 
        name='s2241_fimaposentesp_infoamb'),

url(r'^s2241-fimaposentesp-infoamb/salvar/(?P<hash>.*)/$', 
        s2241_fimaposentesp_infoamb_views.salvar, 
        name='s2241_fimaposentesp_infoamb_salvar'),





]