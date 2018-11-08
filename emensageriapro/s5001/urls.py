#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s5001.views import s5001_procjudtrab as s5001_procjudtrab_views
from emensageriapro.s5001.views import s5001_infocpcalc as s5001_infocpcalc_views
from emensageriapro.s5001.views import s5001_infocp as s5001_infocp_views
from emensageriapro.s5001.views import s5001_ideestablot as s5001_ideestablot_views
from emensageriapro.s5001.views import s5001_infocategincid as s5001_infocategincid_views
from emensageriapro.s5001.views import s5001_infobasecs as s5001_infobasecs_views
from emensageriapro.s5001.views import s5001_calcterc as s5001_calcterc_views





urlpatterns = [



url(r'^s5001-procjudtrab/apagar/(?P<hash>.*)/$', 
        s5001_procjudtrab_views.apagar, 
        name='s5001_procjudtrab_apagar'),

url(r'^s5001-procjudtrab/api/$',
            s5001_procjudtrab_views.s5001procJudTrabList.as_view() ),

        url(r'^s5001-procjudtrab/api/(?P<pk>[0-9]+)/$',
            s5001_procjudtrab_views.s5001procJudTrabDetail.as_view() ),

url(r'^s5001-procjudtrab/listar/(?P<hash>.*)/$', 
        s5001_procjudtrab_views.listar, 
        name='s5001_procjudtrab'),

url(r'^s5001-procjudtrab/salvar/(?P<hash>.*)/$', 
        s5001_procjudtrab_views.salvar, 
        name='s5001_procjudtrab_salvar'),



url(r'^s5001-infocpcalc/apagar/(?P<hash>.*)/$', 
        s5001_infocpcalc_views.apagar, 
        name='s5001_infocpcalc_apagar'),

url(r'^s5001-infocpcalc/api/$',
            s5001_infocpcalc_views.s5001infoCpCalcList.as_view() ),

        url(r'^s5001-infocpcalc/api/(?P<pk>[0-9]+)/$',
            s5001_infocpcalc_views.s5001infoCpCalcDetail.as_view() ),

url(r'^s5001-infocpcalc/listar/(?P<hash>.*)/$', 
        s5001_infocpcalc_views.listar, 
        name='s5001_infocpcalc'),

url(r'^s5001-infocpcalc/salvar/(?P<hash>.*)/$', 
        s5001_infocpcalc_views.salvar, 
        name='s5001_infocpcalc_salvar'),



url(r'^s5001-infocp/apagar/(?P<hash>.*)/$', 
        s5001_infocp_views.apagar, 
        name='s5001_infocp_apagar'),

url(r'^s5001-infocp/api/$',
            s5001_infocp_views.s5001infoCpList.as_view() ),

        url(r'^s5001-infocp/api/(?P<pk>[0-9]+)/$',
            s5001_infocp_views.s5001infoCpDetail.as_view() ),

url(r'^s5001-infocp/listar/(?P<hash>.*)/$', 
        s5001_infocp_views.listar, 
        name='s5001_infocp'),

url(r'^s5001-infocp/salvar/(?P<hash>.*)/$', 
        s5001_infocp_views.salvar, 
        name='s5001_infocp_salvar'),



url(r'^s5001-ideestablot/apagar/(?P<hash>.*)/$', 
        s5001_ideestablot_views.apagar, 
        name='s5001_ideestablot_apagar'),

url(r'^s5001-ideestablot/api/$',
            s5001_ideestablot_views.s5001ideEstabLotList.as_view() ),

        url(r'^s5001-ideestablot/api/(?P<pk>[0-9]+)/$',
            s5001_ideestablot_views.s5001ideEstabLotDetail.as_view() ),

url(r'^s5001-ideestablot/listar/(?P<hash>.*)/$', 
        s5001_ideestablot_views.listar, 
        name='s5001_ideestablot'),

url(r'^s5001-ideestablot/salvar/(?P<hash>.*)/$', 
        s5001_ideestablot_views.salvar, 
        name='s5001_ideestablot_salvar'),



url(r'^s5001-infocategincid/apagar/(?P<hash>.*)/$', 
        s5001_infocategincid_views.apagar, 
        name='s5001_infocategincid_apagar'),

url(r'^s5001-infocategincid/api/$',
            s5001_infocategincid_views.s5001infoCategIncidList.as_view() ),

        url(r'^s5001-infocategincid/api/(?P<pk>[0-9]+)/$',
            s5001_infocategincid_views.s5001infoCategIncidDetail.as_view() ),

url(r'^s5001-infocategincid/listar/(?P<hash>.*)/$', 
        s5001_infocategincid_views.listar, 
        name='s5001_infocategincid'),

url(r'^s5001-infocategincid/salvar/(?P<hash>.*)/$', 
        s5001_infocategincid_views.salvar, 
        name='s5001_infocategincid_salvar'),



url(r'^s5001-infobasecs/apagar/(?P<hash>.*)/$', 
        s5001_infobasecs_views.apagar, 
        name='s5001_infobasecs_apagar'),

url(r'^s5001-infobasecs/api/$',
            s5001_infobasecs_views.s5001infoBaseCSList.as_view() ),

        url(r'^s5001-infobasecs/api/(?P<pk>[0-9]+)/$',
            s5001_infobasecs_views.s5001infoBaseCSDetail.as_view() ),

url(r'^s5001-infobasecs/listar/(?P<hash>.*)/$', 
        s5001_infobasecs_views.listar, 
        name='s5001_infobasecs'),

url(r'^s5001-infobasecs/salvar/(?P<hash>.*)/$', 
        s5001_infobasecs_views.salvar, 
        name='s5001_infobasecs_salvar'),



url(r'^s5001-calcterc/apagar/(?P<hash>.*)/$', 
        s5001_calcterc_views.apagar, 
        name='s5001_calcterc_apagar'),

url(r'^s5001-calcterc/api/$',
            s5001_calcterc_views.s5001calcTercList.as_view() ),

        url(r'^s5001-calcterc/api/(?P<pk>[0-9]+)/$',
            s5001_calcterc_views.s5001calcTercDetail.as_view() ),

url(r'^s5001-calcterc/listar/(?P<hash>.*)/$', 
        s5001_calcterc_views.listar, 
        name='s5001_calcterc'),

url(r'^s5001-calcterc/salvar/(?P<hash>.*)/$', 
        s5001_calcterc_views.salvar, 
        name='s5001_calcterc_salvar'),





]