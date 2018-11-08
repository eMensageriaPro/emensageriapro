#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2260.views import s2260_localtrabinterm as s2260_localtrabinterm_views





urlpatterns = [



url(r'^s2260-localtrabinterm/apagar/(?P<hash>.*)/$', 
        s2260_localtrabinterm_views.apagar, 
        name='s2260_localtrabinterm_apagar'),

url(r'^s2260-localtrabinterm/api/$',
            s2260_localtrabinterm_views.s2260localTrabIntermList.as_view() ),

        url(r'^s2260-localtrabinterm/api/(?P<pk>[0-9]+)/$',
            s2260_localtrabinterm_views.s2260localTrabIntermDetail.as_view() ),

url(r'^s2260-localtrabinterm/listar/(?P<hash>.*)/$', 
        s2260_localtrabinterm_views.listar, 
        name='s2260_localtrabinterm'),

url(r'^s2260-localtrabinterm/salvar/(?P<hash>.*)/$', 
        s2260_localtrabinterm_views.salvar, 
        name='s2260_localtrabinterm_salvar'),





]