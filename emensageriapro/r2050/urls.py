#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2050.views import r2050_tipocom as r2050_tipocom_views
from emensageriapro.r2050.views import r2050_infoproc as r2050_infoproc_views





urlpatterns = [



url(r'^r2050-tipocom/apagar/(?P<hash>.*)/$', 
        r2050_tipocom_views.apagar, 
        name='r2050_tipocom_apagar'),

url(r'^r2050-tipocom/api/$',
            r2050_tipocom_views.r2050tipoComList.as_view() ),

        url(r'^r2050-tipocom/api/(?P<pk>[0-9]+)/$',
            r2050_tipocom_views.r2050tipoComDetail.as_view() ),

url(r'^r2050-tipocom/listar/(?P<hash>.*)/$', 
        r2050_tipocom_views.listar, 
        name='r2050_tipocom'),

url(r'^r2050-tipocom/salvar/(?P<hash>.*)/$', 
        r2050_tipocom_views.salvar, 
        name='r2050_tipocom_salvar'),



url(r'^r2050-infoproc/apagar/(?P<hash>.*)/$', 
        r2050_infoproc_views.apagar, 
        name='r2050_infoproc_apagar'),

url(r'^r2050-infoproc/api/$',
            r2050_infoproc_views.r2050infoProcList.as_view() ),

        url(r'^r2050-infoproc/api/(?P<pk>[0-9]+)/$',
            r2050_infoproc_views.r2050infoProcDetail.as_view() ),

url(r'^r2050-infoproc/listar/(?P<hash>.*)/$', 
        r2050_infoproc_views.listar, 
        name='r2050_infoproc'),

url(r'^r2050-infoproc/salvar/(?P<hash>.*)/$', 
        r2050_infoproc_views.salvar, 
        name='r2050_infoproc_salvar'),





]