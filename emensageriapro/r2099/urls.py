#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2099.views import r2099_iderespinf as r2099_iderespinf_views





urlpatterns = [



url(r'^r2099-iderespinf/apagar/(?P<hash>.*)/$', 
        r2099_iderespinf_views.apagar, 
        name='r2099_iderespinf_apagar'),

url(r'^r2099-iderespinf/api/$',
            r2099_iderespinf_views.r2099ideRespInfList.as_view() ),

        url(r'^r2099-iderespinf/api/(?P<pk>[0-9]+)/$',
            r2099_iderespinf_views.r2099ideRespInfDetail.as_view() ),

url(r'^r2099-iderespinf/listar/(?P<hash>.*)/$', 
        r2099_iderespinf_views.listar, 
        name='r2099_iderespinf'),

url(r'^r2099-iderespinf/salvar/(?P<hash>.*)/$', 
        r2099_iderespinf_views.salvar, 
        name='r2099_iderespinf_salvar'),





]