#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1299.views import s1299_iderespinf as s1299_iderespinf_views





urlpatterns = [



url(r'^s1299-iderespinf/apagar/(?P<hash>.*)/$', 
        s1299_iderespinf_views.apagar, 
        name='s1299_iderespinf_apagar'),

url(r'^s1299-iderespinf/api/$',
            s1299_iderespinf_views.s1299ideRespInfList.as_view() ),

        url(r'^s1299-iderespinf/api/(?P<pk>[0-9]+)/$',
            s1299_iderespinf_views.s1299ideRespInfDetail.as_view() ),

url(r'^s1299-iderespinf/listar/(?P<hash>.*)/$', 
        s1299_iderespinf_views.listar, 
        name='s1299_iderespinf'),

url(r'^s1299-iderespinf/salvar/(?P<hash>.*)/$', 
        s1299_iderespinf_views.salvar, 
        name='s1299_iderespinf_salvar'),





]