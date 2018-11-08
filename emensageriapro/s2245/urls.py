#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2245.views import s2245_infocomplem as s2245_infocomplem_views
from emensageriapro.s2245.views import s2245_ideprofresp as s2245_ideprofresp_views





urlpatterns = [



url(r'^s2245-infocomplem/apagar/(?P<hash>.*)/$', 
        s2245_infocomplem_views.apagar, 
        name='s2245_infocomplem_apagar'),

url(r'^s2245-infocomplem/api/$',
            s2245_infocomplem_views.s2245infoComplemList.as_view() ),

        url(r'^s2245-infocomplem/api/(?P<pk>[0-9]+)/$',
            s2245_infocomplem_views.s2245infoComplemDetail.as_view() ),

url(r'^s2245-infocomplem/listar/(?P<hash>.*)/$', 
        s2245_infocomplem_views.listar, 
        name='s2245_infocomplem'),

url(r'^s2245-infocomplem/salvar/(?P<hash>.*)/$', 
        s2245_infocomplem_views.salvar, 
        name='s2245_infocomplem_salvar'),



url(r'^s2245-ideprofresp/apagar/(?P<hash>.*)/$', 
        s2245_ideprofresp_views.apagar, 
        name='s2245_ideprofresp_apagar'),

url(r'^s2245-ideprofresp/api/$',
            s2245_ideprofresp_views.s2245ideProfRespList.as_view() ),

        url(r'^s2245-ideprofresp/api/(?P<pk>[0-9]+)/$',
            s2245_ideprofresp_views.s2245ideProfRespDetail.as_view() ),

url(r'^s2245-ideprofresp/listar/(?P<hash>.*)/$', 
        s2245_ideprofresp_views.listar, 
        name='s2245_ideprofresp'),

url(r'^s2245-ideprofresp/salvar/(?P<hash>.*)/$', 
        s2245_ideprofresp_views.salvar, 
        name='s2245_ideprofresp_salvar'),





]