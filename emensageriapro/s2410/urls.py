#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2410.views import s2410_infopenmorte as s2410_infopenmorte_views
from emensageriapro.s2410.views import s2410_instpenmorte as s2410_instpenmorte_views
from emensageriapro.s2410.views import s2410_homologtc as s2410_homologtc_views





urlpatterns = [



url(r'^s2410-infopenmorte/apagar/(?P<hash>.*)/$', 
        s2410_infopenmorte_views.apagar, 
        name='s2410_infopenmorte_apagar'),

url(r'^s2410-infopenmorte/api/$',
            s2410_infopenmorte_views.s2410infoPenMorteList.as_view() ),

        url(r'^s2410-infopenmorte/api/(?P<pk>[0-9]+)/$',
            s2410_infopenmorte_views.s2410infoPenMorteDetail.as_view() ),

url(r'^s2410-infopenmorte/listar/(?P<hash>.*)/$', 
        s2410_infopenmorte_views.listar, 
        name='s2410_infopenmorte'),

url(r'^s2410-infopenmorte/salvar/(?P<hash>.*)/$', 
        s2410_infopenmorte_views.salvar, 
        name='s2410_infopenmorte_salvar'),



url(r'^s2410-instpenmorte/apagar/(?P<hash>.*)/$', 
        s2410_instpenmorte_views.apagar, 
        name='s2410_instpenmorte_apagar'),

url(r'^s2410-instpenmorte/api/$',
            s2410_instpenmorte_views.s2410instPenMorteList.as_view() ),

        url(r'^s2410-instpenmorte/api/(?P<pk>[0-9]+)/$',
            s2410_instpenmorte_views.s2410instPenMorteDetail.as_view() ),

url(r'^s2410-instpenmorte/listar/(?P<hash>.*)/$', 
        s2410_instpenmorte_views.listar, 
        name='s2410_instpenmorte'),

url(r'^s2410-instpenmorte/salvar/(?P<hash>.*)/$', 
        s2410_instpenmorte_views.salvar, 
        name='s2410_instpenmorte_salvar'),



url(r'^s2410-homologtc/apagar/(?P<hash>.*)/$', 
        s2410_homologtc_views.apagar, 
        name='s2410_homologtc_apagar'),

url(r'^s2410-homologtc/api/$',
            s2410_homologtc_views.s2410homologTCList.as_view() ),

        url(r'^s2410-homologtc/api/(?P<pk>[0-9]+)/$',
            s2410_homologtc_views.s2410homologTCDetail.as_view() ),

url(r'^s2410-homologtc/listar/(?P<hash>.*)/$', 
        s2410_homologtc_views.listar, 
        name='s2410_homologtc'),

url(r'^s2410-homologtc/salvar/(?P<hash>.*)/$', 
        s2410_homologtc_views.salvar, 
        name='s2410_homologtc_salvar'),





]