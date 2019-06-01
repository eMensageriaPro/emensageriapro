#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.controle_de_acesso.views import login_recuperar_senha as login_recuperar_senha_views
from emensageriapro.controle_de_acesso.views import login_alterar_senha as login_alterar_senha_views
from emensageriapro.controle_de_acesso.views import usuarios_create_token as usuarios_create_token_views
from emensageriapro.controle_de_acesso.views import usuarios_apagar as usuarios_apagar_views
from emensageriapro.controle_de_acesso.views import usuarios_listar as usuarios_listar_views
from emensageriapro.controle_de_acesso.views import usuarios_salvar as usuarios_salvar_views
from emensageriapro.controle_de_acesso.views import usuarios_api as usuarios_api_views



"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

    url(r'^api-token-auth/', 
        views.obtain_auth_token),

    url(r'^usuarios/criar-token/(?P<hash>.*)/$', 
        usuarios_create_token_views.create_token, 
        name='usuarios_create_token'),

    

    

    

    

    url(r'^usuarios/apagar/(?P<hash>.*)/$', 
        usuarios_apagar_views.apagar, 
        name='usuarios_apagar'),

    url(r'^usuarios/api/$',
        usuarios_api_views.UsuariosList.as_view() ),

    url(r'^usuarios/api/(?P<pk>[0-9]+)/$',
        usuarios_api_views.UsuariosDetail.as_view() ),

    url(r'^usuarios/listar/(?P<hash>.*)/$', 
        usuarios_listar_views.listar, 
        name='usuarios'),

    url(r'^usuarios/salvar/(?P<hash>.*)/$', 
        usuarios_salvar_views.salvar, 
        name='usuarios_salvar'),

    


]