#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1270.views import s1270_remunavnp as s1270_remunavnp_views





urlpatterns = [



url(r'^s1270-remunavnp/apagar/(?P<hash>.*)/$', 
        s1270_remunavnp_views.apagar, 
        name='s1270_remunavnp_apagar'),

url(r'^s1270-remunavnp/api/$',
            s1270_remunavnp_views.s1270remunAvNPList.as_view() ),

        url(r'^s1270-remunavnp/api/(?P<pk>[0-9]+)/$',
            s1270_remunavnp_views.s1270remunAvNPDetail.as_view() ),

url(r'^s1270-remunavnp/listar/(?P<hash>.*)/$', 
        s1270_remunavnp_views.listar, 
        name='s1270_remunavnp'),

url(r'^s1270-remunavnp/salvar/(?P<hash>.*)/$', 
        s1270_remunavnp_views.salvar, 
        name='s1270_remunavnp_salvar'),





]