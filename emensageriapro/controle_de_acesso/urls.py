#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.controle_de_acesso.views import login_recuperar_senha as login_recuperar_senha_views
from emensageriapro.controle_de_acesso.views import login_alterar_senha as login_alterar_senha_views
from emensageriapro.controle_de_acesso.views import usuarios_create_token as usuarios_create_token_views
from emensageriapro.controle_de_acesso.views import config_modulos as config_modulos_views
from emensageriapro.controle_de_acesso.views import config_paginas as config_paginas_views
from emensageriapro.controle_de_acesso.views import config_perfis as config_perfis_views
from emensageriapro.controle_de_acesso.views import config_permissoes as config_permissoes_views
from emensageriapro.controle_de_acesso.views import usuarios as usuarios_views
from emensageriapro.controle_de_acesso.views import auditoria as auditoria_views
from rest_framework.authtoken import views


"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

urlpatterns = [

url(r'^recuperar-senha/$',
        login_recuperar_senha_views.recuperar_senha,
        name='recuperar_senha'),

url(r'^alterar-senha/$',
        login_alterar_senha_views.alterar_senha,
        name='alterar_senha'),

url(r'^api-token-auth/', views.obtain_auth_token),

url(r'^usuarios/criar-token/(?P<hash>.*)/$', 
        usuarios_create_token_views.create_token, 
        name='usuarios_create_token'),



url(r'^config-modulos/apagar/(?P<hash>.*)/$', 
        config_modulos_views.apagar, 
        name='config_modulos_apagar'),

url(r'^config-modulos/api/$',
            config_modulos_views.ConfigModulosList.as_view() ),

        url(r'^config-modulos/api/(?P<pk>[0-9]+)/$',
            config_modulos_views.ConfigModulosDetail.as_view() ),

url(r'^config-modulos/listar/(?P<hash>.*)/$', 
        config_modulos_views.listar, 
        name='config_modulos'),

url(r'^config-modulos/salvar/(?P<hash>.*)/$', 
        config_modulos_views.salvar, 
        name='config_modulos_salvar'),



url(r'^config-paginas/apagar/(?P<hash>.*)/$', 
        config_paginas_views.apagar, 
        name='config_paginas_apagar'),

url(r'^config-paginas/api/$',
            config_paginas_views.ConfigPaginasList.as_view() ),

        url(r'^config-paginas/api/(?P<pk>[0-9]+)/$',
            config_paginas_views.ConfigPaginasDetail.as_view() ),

url(r'^config-paginas/listar/(?P<hash>.*)/$', 
        config_paginas_views.listar, 
        name='config_paginas'),

url(r'^config-paginas/salvar/(?P<hash>.*)/$', 
        config_paginas_views.salvar, 
        name='config_paginas_salvar'),



url(r'^config-perfis/apagar/(?P<hash>.*)/$', 
        config_perfis_views.apagar, 
        name='config_perfis_apagar'),

url(r'^config-perfis/api/$',
            config_perfis_views.ConfigPerfisList.as_view() ),

        url(r'^config-perfis/api/(?P<pk>[0-9]+)/$',
            config_perfis_views.ConfigPerfisDetail.as_view() ),

url(r'^config-perfis/listar/(?P<hash>.*)/$', 
        config_perfis_views.listar, 
        name='config_perfis'),

url(r'^config-perfis/salvar/(?P<hash>.*)/$', 
        config_perfis_views.salvar, 
        name='config_perfis_salvar'),



url(r'^config-permissoes/apagar/(?P<hash>.*)/$', 
        config_permissoes_views.apagar, 
        name='config_permissoes_apagar'),

url(r'^config-permissoes/api/$',
            config_permissoes_views.ConfigPermissoesList.as_view() ),

        url(r'^config-permissoes/api/(?P<pk>[0-9]+)/$',
            config_permissoes_views.ConfigPermissoesDetail.as_view() ),

url(r'^config-permissoes/listar/(?P<hash>.*)/$', 
        config_permissoes_views.listar, 
        name='config_permissoes'),

url(r'^config-permissoes/salvar/(?P<hash>.*)/$', 
        config_permissoes_views.salvar, 
        name='config_permissoes_salvar'),



url(r'^usuarios/apagar/(?P<hash>.*)/$', 
        usuarios_views.apagar, 
        name='usuarios_apagar'),

url(r'^usuarios/api/$',
            usuarios_views.UsuariosList.as_view() ),

        url(r'^usuarios/api/(?P<pk>[0-9]+)/$',
            usuarios_views.UsuariosDetail.as_view() ),

url(r'^usuarios/listar/(?P<hash>.*)/$', 
        usuarios_views.listar, 
        name='usuarios'),

url(r'^usuarios/salvar/(?P<hash>.*)/$', 
        usuarios_views.salvar, 
        name='usuarios_salvar'),



url(r'^auditoria/apagar/(?P<hash>.*)/$', 
        auditoria_views.apagar, 
        name='auditoria_apagar'),

url(r'^auditoria/api/$',
            auditoria_views.AuditoriaList.as_view() ),

        url(r'^auditoria/api/(?P<pk>[0-9]+)/$',
            auditoria_views.AuditoriaDetail.as_view() ),

url(r'^auditoria/listar/(?P<hash>.*)/$', 
        auditoria_views.listar, 
        name='auditoria'),

url(r'^auditoria/salvar/(?P<hash>.*)/$', 
        auditoria_views.salvar, 
        name='auditoria_salvar'),





]