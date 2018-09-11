#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s5012-infocrcontrib/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s5012.views.s5012_infocrcontrib.apagar', 
        name='s5012_infocrcontrib_apagar'),

url(r'^s5012-infocrcontrib/listar/(?P<hash>.*)/$', 
        'emensageriapro.s5012.views.s5012_infocrcontrib.listar', 
        name='s5012_infocrcontrib'),

url(r'^s5012-infocrcontrib/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s5012.views.s5012_infocrcontrib.salvar', 
        name='s5012_infocrcontrib_salvar'),





)