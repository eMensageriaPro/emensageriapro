#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1280.views import s1280_infosubstpatr as s1280_infosubstpatr_views
from emensageriapro.s1280.views import s1280_infosubstpatropport as s1280_infosubstpatropport_views
from emensageriapro.s1280.views import s1280_infoativconcom as s1280_infoativconcom_views





urlpatterns = [



url(r'^s1280-infosubstpatr/apagar/(?P<hash>.*)/$', 
        s1280_infosubstpatr_views.apagar, 
        name='s1280_infosubstpatr_apagar'),

url(r'^s1280-infosubstpatr/api/$',
            s1280_infosubstpatr_views.s1280infoSubstPatrList.as_view() ),

        url(r'^s1280-infosubstpatr/api/(?P<pk>[0-9]+)/$',
            s1280_infosubstpatr_views.s1280infoSubstPatrDetail.as_view() ),

url(r'^s1280-infosubstpatr/listar/(?P<hash>.*)/$', 
        s1280_infosubstpatr_views.listar, 
        name='s1280_infosubstpatr'),

url(r'^s1280-infosubstpatr/salvar/(?P<hash>.*)/$', 
        s1280_infosubstpatr_views.salvar, 
        name='s1280_infosubstpatr_salvar'),



url(r'^s1280-infosubstpatropport/apagar/(?P<hash>.*)/$', 
        s1280_infosubstpatropport_views.apagar, 
        name='s1280_infosubstpatropport_apagar'),

url(r'^s1280-infosubstpatropport/api/$',
            s1280_infosubstpatropport_views.s1280infoSubstPatrOpPortList.as_view() ),

        url(r'^s1280-infosubstpatropport/api/(?P<pk>[0-9]+)/$',
            s1280_infosubstpatropport_views.s1280infoSubstPatrOpPortDetail.as_view() ),

url(r'^s1280-infosubstpatropport/listar/(?P<hash>.*)/$', 
        s1280_infosubstpatropport_views.listar, 
        name='s1280_infosubstpatropport'),

url(r'^s1280-infosubstpatropport/salvar/(?P<hash>.*)/$', 
        s1280_infosubstpatropport_views.salvar, 
        name='s1280_infosubstpatropport_salvar'),



url(r'^s1280-infoativconcom/apagar/(?P<hash>.*)/$', 
        s1280_infoativconcom_views.apagar, 
        name='s1280_infoativconcom_apagar'),

url(r'^s1280-infoativconcom/api/$',
            s1280_infoativconcom_views.s1280infoAtivConcomList.as_view() ),

        url(r'^s1280-infoativconcom/api/(?P<pk>[0-9]+)/$',
            s1280_infoativconcom_views.s1280infoAtivConcomDetail.as_view() ),

url(r'^s1280-infoativconcom/listar/(?P<hash>.*)/$', 
        s1280_infoativconcom_views.listar, 
        name='s1280_infoativconcom'),

url(r'^s1280-infoativconcom/salvar/(?P<hash>.*)/$', 
        s1280_infoativconcom_views.salvar, 
        name='s1280_infoativconcom_salvar'),





]