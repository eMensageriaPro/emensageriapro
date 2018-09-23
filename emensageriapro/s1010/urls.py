#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s1010.views import s1010_inclusao as s1010_inclusao_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocp as s1010_inclusao_ideprocessocp_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessoirrf as s1010_inclusao_ideprocessoirrf_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessofgts as s1010_inclusao_ideprocessofgts_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessosind as s1010_inclusao_ideprocessosind_views
from emensageriapro.s1010.views import s1010_inclusao_ideprocessocprp as s1010_inclusao_ideprocessocprp_views
from emensageriapro.s1010.views import s1010_alteracao as s1010_alteracao_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocp as s1010_alteracao_ideprocessocp_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessoirrf as s1010_alteracao_ideprocessoirrf_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessofgts as s1010_alteracao_ideprocessofgts_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessosind as s1010_alteracao_ideprocessosind_views
from emensageriapro.s1010.views import s1010_alteracao_ideprocessocprp as s1010_alteracao_ideprocessocprp_views
from emensageriapro.s1010.views import s1010_alteracao_novavalidade as s1010_alteracao_novavalidade_views
from emensageriapro.s1010.views import s1010_exclusao as s1010_exclusao_views



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



url(r'^s1010-inclusao/apagar/(?P<hash>.*)/$', 
        s1010_inclusao_views.apagar, 
        name='s1010_inclusao_apagar'),

url(r'^s1010-inclusao/listar/(?P<hash>.*)/$', 
        s1010_inclusao_views.listar, 
        name='s1010_inclusao'),

url(r'^s1010-inclusao/salvar/(?P<hash>.*)/$', 
        s1010_inclusao_views.salvar, 
        name='s1010_inclusao_salvar'),



url(r'^s1010-inclusao-ideprocessocp/apagar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessocp_views.apagar, 
        name='s1010_inclusao_ideprocessocp_apagar'),

url(r'^s1010-inclusao-ideprocessocp/listar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessocp_views.listar, 
        name='s1010_inclusao_ideprocessocp'),

url(r'^s1010-inclusao-ideprocessocp/salvar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessocp_views.salvar, 
        name='s1010_inclusao_ideprocessocp_salvar'),



url(r'^s1010-inclusao-ideprocessoirrf/apagar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessoirrf_views.apagar, 
        name='s1010_inclusao_ideprocessoirrf_apagar'),

url(r'^s1010-inclusao-ideprocessoirrf/listar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessoirrf_views.listar, 
        name='s1010_inclusao_ideprocessoirrf'),

url(r'^s1010-inclusao-ideprocessoirrf/salvar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessoirrf_views.salvar, 
        name='s1010_inclusao_ideprocessoirrf_salvar'),



url(r'^s1010-inclusao-ideprocessofgts/apagar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessofgts_views.apagar, 
        name='s1010_inclusao_ideprocessofgts_apagar'),

url(r'^s1010-inclusao-ideprocessofgts/listar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessofgts_views.listar, 
        name='s1010_inclusao_ideprocessofgts'),

url(r'^s1010-inclusao-ideprocessofgts/salvar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessofgts_views.salvar, 
        name='s1010_inclusao_ideprocessofgts_salvar'),



url(r'^s1010-inclusao-ideprocessosind/apagar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessosind_views.apagar, 
        name='s1010_inclusao_ideprocessosind_apagar'),

url(r'^s1010-inclusao-ideprocessosind/listar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessosind_views.listar, 
        name='s1010_inclusao_ideprocessosind'),

url(r'^s1010-inclusao-ideprocessosind/salvar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessosind_views.salvar, 
        name='s1010_inclusao_ideprocessosind_salvar'),



url(r'^s1010-inclusao-ideprocessocprp/apagar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessocprp_views.apagar, 
        name='s1010_inclusao_ideprocessocprp_apagar'),

url(r'^s1010-inclusao-ideprocessocprp/listar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessocprp_views.listar, 
        name='s1010_inclusao_ideprocessocprp'),

url(r'^s1010-inclusao-ideprocessocprp/salvar/(?P<hash>.*)/$', 
        s1010_inclusao_ideprocessocprp_views.salvar, 
        name='s1010_inclusao_ideprocessocprp_salvar'),



url(r'^s1010-alteracao/apagar/(?P<hash>.*)/$', 
        s1010_alteracao_views.apagar, 
        name='s1010_alteracao_apagar'),

url(r'^s1010-alteracao/listar/(?P<hash>.*)/$', 
        s1010_alteracao_views.listar, 
        name='s1010_alteracao'),

url(r'^s1010-alteracao/salvar/(?P<hash>.*)/$', 
        s1010_alteracao_views.salvar, 
        name='s1010_alteracao_salvar'),



url(r'^s1010-alteracao-ideprocessocp/apagar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessocp_views.apagar, 
        name='s1010_alteracao_ideprocessocp_apagar'),

url(r'^s1010-alteracao-ideprocessocp/listar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessocp_views.listar, 
        name='s1010_alteracao_ideprocessocp'),

url(r'^s1010-alteracao-ideprocessocp/salvar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessocp_views.salvar, 
        name='s1010_alteracao_ideprocessocp_salvar'),



url(r'^s1010-alteracao-ideprocessoirrf/apagar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessoirrf_views.apagar, 
        name='s1010_alteracao_ideprocessoirrf_apagar'),

url(r'^s1010-alteracao-ideprocessoirrf/listar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessoirrf_views.listar, 
        name='s1010_alteracao_ideprocessoirrf'),

url(r'^s1010-alteracao-ideprocessoirrf/salvar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessoirrf_views.salvar, 
        name='s1010_alteracao_ideprocessoirrf_salvar'),



url(r'^s1010-alteracao-ideprocessofgts/apagar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessofgts_views.apagar, 
        name='s1010_alteracao_ideprocessofgts_apagar'),

url(r'^s1010-alteracao-ideprocessofgts/listar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessofgts_views.listar, 
        name='s1010_alteracao_ideprocessofgts'),

url(r'^s1010-alteracao-ideprocessofgts/salvar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessofgts_views.salvar, 
        name='s1010_alteracao_ideprocessofgts_salvar'),



url(r'^s1010-alteracao-ideprocessosind/apagar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessosind_views.apagar, 
        name='s1010_alteracao_ideprocessosind_apagar'),

url(r'^s1010-alteracao-ideprocessosind/listar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessosind_views.listar, 
        name='s1010_alteracao_ideprocessosind'),

url(r'^s1010-alteracao-ideprocessosind/salvar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessosind_views.salvar, 
        name='s1010_alteracao_ideprocessosind_salvar'),



url(r'^s1010-alteracao-ideprocessocprp/apagar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessocprp_views.apagar, 
        name='s1010_alteracao_ideprocessocprp_apagar'),

url(r'^s1010-alteracao-ideprocessocprp/listar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessocprp_views.listar, 
        name='s1010_alteracao_ideprocessocprp'),

url(r'^s1010-alteracao-ideprocessocprp/salvar/(?P<hash>.*)/$', 
        s1010_alteracao_ideprocessocprp_views.salvar, 
        name='s1010_alteracao_ideprocessocprp_salvar'),



url(r'^s1010-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        s1010_alteracao_novavalidade_views.apagar, 
        name='s1010_alteracao_novavalidade_apagar'),

url(r'^s1010-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        s1010_alteracao_novavalidade_views.listar, 
        name='s1010_alteracao_novavalidade'),

url(r'^s1010-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        s1010_alteracao_novavalidade_views.salvar, 
        name='s1010_alteracao_novavalidade_salvar'),



url(r'^s1010-exclusao/apagar/(?P<hash>.*)/$', 
        s1010_exclusao_views.apagar, 
        name='s1010_exclusao_apagar'),

url(r'^s1010-exclusao/listar/(?P<hash>.*)/$', 
        s1010_exclusao_views.listar, 
        name='s1010_exclusao'),

url(r'^s1010-exclusao/salvar/(?P<hash>.*)/$', 
        s1010_exclusao_views.salvar, 
        name='s1010_exclusao_salvar'),





]