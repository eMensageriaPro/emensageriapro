#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2060.views import r2060_tipocod as r2060_tipocod_views
from emensageriapro.r2060.views import r2060_tipoajuste as r2060_tipoajuste_views
from emensageriapro.r2060.views import r2060_infoproc as r2060_infoproc_views





urlpatterns = [



url(r'^r2060-tipocod/apagar/(?P<hash>.*)/$', 
        r2060_tipocod_views.apagar, 
        name='r2060_tipocod_apagar'),

url(r'^r2060-tipocod/api/$',
            r2060_tipocod_views.r2060tipoCodList.as_view() ),

        url(r'^r2060-tipocod/api/(?P<pk>[0-9]+)/$',
            r2060_tipocod_views.r2060tipoCodDetail.as_view() ),

url(r'^r2060-tipocod/listar/(?P<hash>.*)/$', 
        r2060_tipocod_views.listar, 
        name='r2060_tipocod'),

url(r'^r2060-tipocod/salvar/(?P<hash>.*)/$', 
        r2060_tipocod_views.salvar, 
        name='r2060_tipocod_salvar'),



url(r'^r2060-tipoajuste/apagar/(?P<hash>.*)/$', 
        r2060_tipoajuste_views.apagar, 
        name='r2060_tipoajuste_apagar'),

url(r'^r2060-tipoajuste/api/$',
            r2060_tipoajuste_views.r2060tipoAjusteList.as_view() ),

        url(r'^r2060-tipoajuste/api/(?P<pk>[0-9]+)/$',
            r2060_tipoajuste_views.r2060tipoAjusteDetail.as_view() ),

url(r'^r2060-tipoajuste/listar/(?P<hash>.*)/$', 
        r2060_tipoajuste_views.listar, 
        name='r2060_tipoajuste'),

url(r'^r2060-tipoajuste/salvar/(?P<hash>.*)/$', 
        r2060_tipoajuste_views.salvar, 
        name='r2060_tipoajuste_salvar'),



url(r'^r2060-infoproc/apagar/(?P<hash>.*)/$', 
        r2060_infoproc_views.apagar, 
        name='r2060_infoproc_apagar'),

url(r'^r2060-infoproc/api/$',
            r2060_infoproc_views.r2060infoProcList.as_view() ),

        url(r'^r2060-infoproc/api/(?P<pk>[0-9]+)/$',
            r2060_infoproc_views.r2060infoProcDetail.as_view() ),

url(r'^r2060-infoproc/listar/(?P<hash>.*)/$', 
        r2060_infoproc_views.listar, 
        name='r2060_infoproc'),

url(r'^r2060-infoproc/salvar/(?P<hash>.*)/$', 
        r2060_infoproc_views.salvar, 
        name='r2060_infoproc_salvar'),





]