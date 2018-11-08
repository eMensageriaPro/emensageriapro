#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2416.views import s2416_infopenmorte as s2416_infopenmorte_views
from emensageriapro.s2416.views import s2416_homologtc as s2416_homologtc_views
from emensageriapro.s2416.views import s2416_suspensao as s2416_suspensao_views





urlpatterns = [



url(r'^s2416-infopenmorte/apagar/(?P<hash>.*)/$', 
        s2416_infopenmorte_views.apagar, 
        name='s2416_infopenmorte_apagar'),

url(r'^s2416-infopenmorte/api/$',
            s2416_infopenmorte_views.s2416infoPenMorteList.as_view() ),

        url(r'^s2416-infopenmorte/api/(?P<pk>[0-9]+)/$',
            s2416_infopenmorte_views.s2416infoPenMorteDetail.as_view() ),

url(r'^s2416-infopenmorte/listar/(?P<hash>.*)/$', 
        s2416_infopenmorte_views.listar, 
        name='s2416_infopenmorte'),

url(r'^s2416-infopenmorte/salvar/(?P<hash>.*)/$', 
        s2416_infopenmorte_views.salvar, 
        name='s2416_infopenmorte_salvar'),



url(r'^s2416-homologtc/apagar/(?P<hash>.*)/$', 
        s2416_homologtc_views.apagar, 
        name='s2416_homologtc_apagar'),

url(r'^s2416-homologtc/api/$',
            s2416_homologtc_views.s2416homologTCList.as_view() ),

        url(r'^s2416-homologtc/api/(?P<pk>[0-9]+)/$',
            s2416_homologtc_views.s2416homologTCDetail.as_view() ),

url(r'^s2416-homologtc/listar/(?P<hash>.*)/$', 
        s2416_homologtc_views.listar, 
        name='s2416_homologtc'),

url(r'^s2416-homologtc/salvar/(?P<hash>.*)/$', 
        s2416_homologtc_views.salvar, 
        name='s2416_homologtc_salvar'),



url(r'^s2416-suspensao/apagar/(?P<hash>.*)/$', 
        s2416_suspensao_views.apagar, 
        name='s2416_suspensao_apagar'),

url(r'^s2416-suspensao/api/$',
            s2416_suspensao_views.s2416suspensaoList.as_view() ),

        url(r'^s2416-suspensao/api/(?P<pk>[0-9]+)/$',
            s2416_suspensao_views.s2416suspensaoDetail.as_view() ),

url(r'^s2416-suspensao/listar/(?P<hash>.*)/$', 
        s2416_suspensao_views.listar, 
        name='s2416_suspensao'),

url(r'^s2416-suspensao/salvar/(?P<hash>.*)/$', 
        s2416_suspensao_views.salvar, 
        name='s2416_suspensao_salvar'),





]