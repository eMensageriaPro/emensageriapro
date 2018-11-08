#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1300.views import s1300_contribsind as s1300_contribsind_views





urlpatterns = [



url(r'^s1300-contribsind/apagar/(?P<hash>.*)/$', 
        s1300_contribsind_views.apagar, 
        name='s1300_contribsind_apagar'),

url(r'^s1300-contribsind/api/$',
            s1300_contribsind_views.s1300contribSindList.as_view() ),

        url(r'^s1300-contribsind/api/(?P<pk>[0-9]+)/$',
            s1300_contribsind_views.s1300contribSindDetail.as_view() ),

url(r'^s1300-contribsind/listar/(?P<hash>.*)/$', 
        s1300_contribsind_views.listar, 
        name='s1300_contribsind'),

url(r'^s1300-contribsind/salvar/(?P<hash>.*)/$', 
        s1300_contribsind_views.salvar, 
        name='s1300_contribsind_salvar'),





]