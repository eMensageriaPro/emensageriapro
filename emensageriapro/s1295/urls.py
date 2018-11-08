#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1295.views import s1295_iderespinf as s1295_iderespinf_views





urlpatterns = [



url(r'^s1295-iderespinf/apagar/(?P<hash>.*)/$', 
        s1295_iderespinf_views.apagar, 
        name='s1295_iderespinf_apagar'),

url(r'^s1295-iderespinf/api/$',
            s1295_iderespinf_views.s1295ideRespInfList.as_view() ),

        url(r'^s1295-iderespinf/api/(?P<pk>[0-9]+)/$',
            s1295_iderespinf_views.s1295ideRespInfDetail.as_view() ),

url(r'^s1295-iderespinf/listar/(?P<hash>.*)/$', 
        s1295_iderespinf_views.listar, 
        name='s1295_iderespinf'),

url(r'^s1295-iderespinf/salvar/(?P<hash>.*)/$', 
        s1295_iderespinf_views.salvar, 
        name='s1295_iderespinf_salvar'),





]