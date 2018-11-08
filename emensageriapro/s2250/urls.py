#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2250.views import s2250_detavprevio as s2250_detavprevio_views
from emensageriapro.s2250.views import s2250_cancavprevio as s2250_cancavprevio_views





urlpatterns = [



url(r'^s2250-detavprevio/apagar/(?P<hash>.*)/$', 
        s2250_detavprevio_views.apagar, 
        name='s2250_detavprevio_apagar'),

url(r'^s2250-detavprevio/api/$',
            s2250_detavprevio_views.s2250detAvPrevioList.as_view() ),

        url(r'^s2250-detavprevio/api/(?P<pk>[0-9]+)/$',
            s2250_detavprevio_views.s2250detAvPrevioDetail.as_view() ),

url(r'^s2250-detavprevio/listar/(?P<hash>.*)/$', 
        s2250_detavprevio_views.listar, 
        name='s2250_detavprevio'),

url(r'^s2250-detavprevio/salvar/(?P<hash>.*)/$', 
        s2250_detavprevio_views.salvar, 
        name='s2250_detavprevio_salvar'),



url(r'^s2250-cancavprevio/apagar/(?P<hash>.*)/$', 
        s2250_cancavprevio_views.apagar, 
        name='s2250_cancavprevio_apagar'),

url(r'^s2250-cancavprevio/api/$',
            s2250_cancavprevio_views.s2250cancAvPrevioList.as_view() ),

        url(r'^s2250-cancavprevio/api/(?P<pk>[0-9]+)/$',
            s2250_cancavprevio_views.s2250cancAvPrevioDetail.as_view() ),

url(r'^s2250-cancavprevio/listar/(?P<hash>.*)/$', 
        s2250_cancavprevio_views.listar, 
        name='s2250_cancavprevio'),

url(r'^s2250-cancavprevio/salvar/(?P<hash>.*)/$', 
        s2250_cancavprevio_views.salvar, 
        name='s2250_cancavprevio_salvar'),





]