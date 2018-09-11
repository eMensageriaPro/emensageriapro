#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r5011-regocorrs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_regocorrs.apagar', 
        name='r5011_regocorrs_apagar'),

url(r'^r5011-regocorrs/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_regocorrs.listar', 
        name='r5011_regocorrs'),

url(r'^r5011-regocorrs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_regocorrs.salvar', 
        name='r5011_regocorrs_salvar'),



url(r'^r5011-infototalcontrib/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infototalcontrib.apagar', 
        name='r5011_infototalcontrib_apagar'),

url(r'^r5011-infototalcontrib/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infototalcontrib.listar', 
        name='r5011_infototalcontrib'),

url(r'^r5011-infototalcontrib/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infototalcontrib.salvar', 
        name='r5011_infototalcontrib_salvar'),



url(r'^r5011-rtom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rtom.apagar', 
        name='r5011_rtom_apagar'),

url(r'^r5011-rtom/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rtom.listar', 
        name='r5011_rtom'),

url(r'^r5011-rtom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rtom.salvar', 
        name='r5011_rtom_salvar'),



url(r'^r5011-infocrtom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infocrtom.apagar', 
        name='r5011_infocrtom_apagar'),

url(r'^r5011-infocrtom/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infocrtom.listar', 
        name='r5011_infocrtom'),

url(r'^r5011-infocrtom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_infocrtom.salvar', 
        name='r5011_infocrtom_salvar'),



url(r'^r5011-rprest/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rprest.apagar', 
        name='r5011_rprest_apagar'),

url(r'^r5011-rprest/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rprest.listar', 
        name='r5011_rprest'),

url(r'^r5011-rprest/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rprest.salvar', 
        name='r5011_rprest_salvar'),



url(r'^r5011-rrecrepad/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rrecrepad.apagar', 
        name='r5011_rrecrepad_apagar'),

url(r'^r5011-rrecrepad/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rrecrepad.listar', 
        name='r5011_rrecrepad'),

url(r'^r5011-rrecrepad/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rrecrepad.salvar', 
        name='r5011_rrecrepad_salvar'),



url(r'^r5011-rcoml/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcoml.apagar', 
        name='r5011_rcoml_apagar'),

url(r'^r5011-rcoml/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcoml.listar', 
        name='r5011_rcoml'),

url(r'^r5011-rcoml/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcoml.salvar', 
        name='r5011_rcoml_salvar'),



url(r'^r5011-rcprb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcprb.apagar', 
        name='r5011_rcprb_apagar'),

url(r'^r5011-rcprb/listar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcprb.listar', 
        name='r5011_rcprb'),

url(r'^r5011-rcprb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r5011.views.r5011_rcprb.salvar', 
        name='r5011_rcprb_salvar'),





)