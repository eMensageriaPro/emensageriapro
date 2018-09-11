#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:

url(r'^alterar-senha/$',
        'emensageriapro.controle_de_acesso.views.login_alterar_senha.alterar_senha',
        name='alterar_senha'),

url(r'^$',
        'emensageriapro.controle_de_acesso.views.login.login', 
        name='login'),

url(r'^recuperar-senha/$',
        'emensageriapro.controle_de_acesso.views.login_recuperar_senha.recuperar_senha',
        name='recuperar_senha'),









url(r'^config-modulos/listar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_modulos.listar', 
        name='config_modulos'),

url(r'^config-modulos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_modulos.salvar', 
        name='config_modulos_salvar'),

url(r'^config-modulos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_modulos.apagar', 
        name='config_modulos_apagar'),



url(r'^config-paginas/listar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_paginas.listar', 
        name='config_paginas'),

url(r'^config-paginas/salvar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_paginas.salvar', 
        name='config_paginas_salvar'),

url(r'^config-paginas/apagar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_paginas.apagar', 
        name='config_paginas_apagar'),



url(r'^config-perfis/listar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_perfis.listar', 
        name='config_perfis'),

url(r'^config-perfis/salvar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_perfis.salvar', 
        name='config_perfis_salvar'),

url(r'^config-perfis/apagar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_perfis.apagar', 
        name='config_perfis_apagar'),



url(r'^config-permissoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_permissoes.listar', 
        name='config_permissoes'),

url(r'^config-permissoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_permissoes.salvar', 
        name='config_permissoes_salvar'),

url(r'^config-permissoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.config_permissoes.apagar', 
        name='config_permissoes_apagar'),



url(r'^usuarios/listar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.usuarios.listar', 
        name='usuarios'),

url(r'^usuarios/salvar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.usuarios.salvar', 
        name='usuarios_salvar'),

url(r'^usuarios/apagar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.usuarios.apagar', 
        name='usuarios_apagar'),



url(r'^auditoria/listar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.auditoria.listar', 
        name='auditoria'),

url(r'^auditoria/salvar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.auditoria.salvar', 
        name='auditoria_salvar'),

url(r'^auditoria/apagar/(?P<hash>.*)/$', 
        'emensageriapro.controle_de_acesso.views.auditoria.apagar', 
        name='auditoria_apagar'),





)