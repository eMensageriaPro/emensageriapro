#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2040.views import r2040_recursosrep as r2040_recursosrep_views
from emensageriapro.r2040.views import r2040_inforecurso as r2040_inforecurso_views
from emensageriapro.r2040.views import r2040_infoproc as r2040_infoproc_views





urlpatterns = [



url(r'^r2040-recursosrep/apagar/(?P<hash>.*)/$', 
        r2040_recursosrep_views.apagar, 
        name='r2040_recursosrep_apagar'),

url(r'^r2040-recursosrep/api/$',
            r2040_recursosrep_views.r2040recursosRepList.as_view() ),

        url(r'^r2040-recursosrep/api/(?P<pk>[0-9]+)/$',
            r2040_recursosrep_views.r2040recursosRepDetail.as_view() ),

url(r'^r2040-recursosrep/listar/(?P<hash>.*)/$', 
        r2040_recursosrep_views.listar, 
        name='r2040_recursosrep'),

url(r'^r2040-recursosrep/salvar/(?P<hash>.*)/$', 
        r2040_recursosrep_views.salvar, 
        name='r2040_recursosrep_salvar'),



url(r'^r2040-inforecurso/apagar/(?P<hash>.*)/$', 
        r2040_inforecurso_views.apagar, 
        name='r2040_inforecurso_apagar'),

url(r'^r2040-inforecurso/api/$',
            r2040_inforecurso_views.r2040infoRecursoList.as_view() ),

        url(r'^r2040-inforecurso/api/(?P<pk>[0-9]+)/$',
            r2040_inforecurso_views.r2040infoRecursoDetail.as_view() ),

url(r'^r2040-inforecurso/listar/(?P<hash>.*)/$', 
        r2040_inforecurso_views.listar, 
        name='r2040_inforecurso'),

url(r'^r2040-inforecurso/salvar/(?P<hash>.*)/$', 
        r2040_inforecurso_views.salvar, 
        name='r2040_inforecurso_salvar'),



url(r'^r2040-infoproc/apagar/(?P<hash>.*)/$', 
        r2040_infoproc_views.apagar, 
        name='r2040_infoproc_apagar'),

url(r'^r2040-infoproc/api/$',
            r2040_infoproc_views.r2040infoProcList.as_view() ),

        url(r'^r2040-infoproc/api/(?P<pk>[0-9]+)/$',
            r2040_infoproc_views.r2040infoProcDetail.as_view() ),

url(r'^r2040-infoproc/listar/(?P<hash>.*)/$', 
        r2040_infoproc_views.listar, 
        name='r2040_infoproc'),

url(r'^r2040-infoproc/salvar/(?P<hash>.*)/$', 
        r2040_infoproc_views.salvar, 
        name='r2040_infoproc_salvar'),





]