#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^r1000-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao.apagar', 
        name='r1000_inclusao_apagar'),

url(r'^r1000-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao.listar', 
        name='r1000_inclusao'),

url(r'^r1000-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao.salvar', 
        name='r1000_inclusao_salvar'),



url(r'^r1000-inclusao-softhouse/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_softhouse.apagar', 
        name='r1000_inclusao_softhouse_apagar'),

url(r'^r1000-inclusao-softhouse/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_softhouse.listar', 
        name='r1000_inclusao_softhouse'),

url(r'^r1000-inclusao-softhouse/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_softhouse.salvar', 
        name='r1000_inclusao_softhouse_salvar'),



url(r'^r1000-inclusao-infoefr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_infoefr.apagar', 
        name='r1000_inclusao_infoefr_apagar'),

url(r'^r1000-inclusao-infoefr/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_infoefr.listar', 
        name='r1000_inclusao_infoefr'),

url(r'^r1000-inclusao-infoefr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_inclusao_infoefr.salvar', 
        name='r1000_inclusao_infoefr_salvar'),



url(r'^r1000-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao.apagar', 
        name='r1000_alteracao_apagar'),

url(r'^r1000-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao.listar', 
        name='r1000_alteracao'),

url(r'^r1000-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao.salvar', 
        name='r1000_alteracao_salvar'),



url(r'^r1000-alteracao-softhouse/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_softhouse.apagar', 
        name='r1000_alteracao_softhouse_apagar'),

url(r'^r1000-alteracao-softhouse/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_softhouse.listar', 
        name='r1000_alteracao_softhouse'),

url(r'^r1000-alteracao-softhouse/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_softhouse.salvar', 
        name='r1000_alteracao_softhouse_salvar'),



url(r'^r1000-alteracao-infoefr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_infoefr.apagar', 
        name='r1000_alteracao_infoefr_apagar'),

url(r'^r1000-alteracao-infoefr/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_infoefr.listar', 
        name='r1000_alteracao_infoefr'),

url(r'^r1000-alteracao-infoefr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_infoefr.salvar', 
        name='r1000_alteracao_infoefr_salvar'),



url(r'^r1000-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_novavalidade.apagar', 
        name='r1000_alteracao_novavalidade_apagar'),

url(r'^r1000-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_novavalidade.listar', 
        name='r1000_alteracao_novavalidade'),

url(r'^r1000-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_alteracao_novavalidade.salvar', 
        name='r1000_alteracao_novavalidade_salvar'),



url(r'^r1000-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_exclusao.apagar', 
        name='r1000_exclusao_apagar'),

url(r'^r1000-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_exclusao.listar', 
        name='r1000_exclusao'),

url(r'^r1000-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1000.views.r1000_exclusao.salvar', 
        name='r1000_exclusao_salvar'),





)