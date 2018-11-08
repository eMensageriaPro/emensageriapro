#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2220.views import s2220_exame as s2220_exame_views





urlpatterns = [



url(r'^s2220-exame/apagar/(?P<hash>.*)/$', 
        s2220_exame_views.apagar, 
        name='s2220_exame_apagar'),

url(r'^s2220-exame/api/$',
            s2220_exame_views.s2220exameList.as_view() ),

        url(r'^s2220-exame/api/(?P<pk>[0-9]+)/$',
            s2220_exame_views.s2220exameDetail.as_view() ),

url(r'^s2220-exame/listar/(?P<hash>.*)/$', 
        s2220_exame_views.listar, 
        name='s2220_exame'),

url(r'^s2220-exame/salvar/(?P<hash>.*)/$', 
        s2220_exame_views.salvar, 
        name='s2220_exame_salvar'),





]