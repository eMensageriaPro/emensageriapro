#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2306.views import s2306_ageintegracao as s2306_ageintegracao_views
from emensageriapro.s2306.views import s2306_cargofuncao as s2306_cargofuncao_views
from emensageriapro.s2306.views import s2306_infoestagiario as s2306_infoestagiario_views
from emensageriapro.s2306.views import s2306_infotrabcedido as s2306_infotrabcedido_views
from emensageriapro.s2306.views import s2306_remuneracao as s2306_remuneracao_views
from emensageriapro.s2306.views import s2306_supervisorestagio as s2306_supervisorestagio_views



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



url(r'^s2306-ageintegracao/apagar/(?P<hash>.*)/$', 
        s2306_ageintegracao_views.apagar, 
        name='s2306_ageintegracao_apagar'),

url(r'^s2306-ageintegracao/api/$',
            s2306_ageintegracao_views.s2306ageIntegracaoList.as_view() ),

        url(r'^s2306-ageintegracao/api/(?P<pk>[0-9]+)/$',
            s2306_ageintegracao_views.s2306ageIntegracaoDetail.as_view() ),

url(r'^s2306-ageintegracao/listar/(?P<hash>.*)/$', 
        s2306_ageintegracao_views.listar, 
        name='s2306_ageintegracao'),

url(r'^s2306-ageintegracao/salvar/(?P<hash>.*)/$', 
        s2306_ageintegracao_views.salvar, 
        name='s2306_ageintegracao_salvar'),



url(r'^s2306-cargofuncao/apagar/(?P<hash>.*)/$', 
        s2306_cargofuncao_views.apagar, 
        name='s2306_cargofuncao_apagar'),

url(r'^s2306-cargofuncao/api/$',
            s2306_cargofuncao_views.s2306cargoFuncaoList.as_view() ),

        url(r'^s2306-cargofuncao/api/(?P<pk>[0-9]+)/$',
            s2306_cargofuncao_views.s2306cargoFuncaoDetail.as_view() ),

url(r'^s2306-cargofuncao/listar/(?P<hash>.*)/$', 
        s2306_cargofuncao_views.listar, 
        name='s2306_cargofuncao'),

url(r'^s2306-cargofuncao/salvar/(?P<hash>.*)/$', 
        s2306_cargofuncao_views.salvar, 
        name='s2306_cargofuncao_salvar'),



url(r'^s2306-infoestagiario/apagar/(?P<hash>.*)/$', 
        s2306_infoestagiario_views.apagar, 
        name='s2306_infoestagiario_apagar'),

url(r'^s2306-infoestagiario/api/$',
            s2306_infoestagiario_views.s2306infoEstagiarioList.as_view() ),

        url(r'^s2306-infoestagiario/api/(?P<pk>[0-9]+)/$',
            s2306_infoestagiario_views.s2306infoEstagiarioDetail.as_view() ),

url(r'^s2306-infoestagiario/listar/(?P<hash>.*)/$', 
        s2306_infoestagiario_views.listar, 
        name='s2306_infoestagiario'),

url(r'^s2306-infoestagiario/salvar/(?P<hash>.*)/$', 
        s2306_infoestagiario_views.salvar, 
        name='s2306_infoestagiario_salvar'),



url(r'^s2306-infotrabcedido/apagar/(?P<hash>.*)/$', 
        s2306_infotrabcedido_views.apagar, 
        name='s2306_infotrabcedido_apagar'),

url(r'^s2306-infotrabcedido/api/$',
            s2306_infotrabcedido_views.s2306infoTrabCedidoList.as_view() ),

        url(r'^s2306-infotrabcedido/api/(?P<pk>[0-9]+)/$',
            s2306_infotrabcedido_views.s2306infoTrabCedidoDetail.as_view() ),

url(r'^s2306-infotrabcedido/listar/(?P<hash>.*)/$', 
        s2306_infotrabcedido_views.listar, 
        name='s2306_infotrabcedido'),

url(r'^s2306-infotrabcedido/salvar/(?P<hash>.*)/$', 
        s2306_infotrabcedido_views.salvar, 
        name='s2306_infotrabcedido_salvar'),



url(r'^s2306-remuneracao/apagar/(?P<hash>.*)/$', 
        s2306_remuneracao_views.apagar, 
        name='s2306_remuneracao_apagar'),

url(r'^s2306-remuneracao/api/$',
            s2306_remuneracao_views.s2306remuneracaoList.as_view() ),

        url(r'^s2306-remuneracao/api/(?P<pk>[0-9]+)/$',
            s2306_remuneracao_views.s2306remuneracaoDetail.as_view() ),

url(r'^s2306-remuneracao/listar/(?P<hash>.*)/$', 
        s2306_remuneracao_views.listar, 
        name='s2306_remuneracao'),

url(r'^s2306-remuneracao/salvar/(?P<hash>.*)/$', 
        s2306_remuneracao_views.salvar, 
        name='s2306_remuneracao_salvar'),



url(r'^s2306-supervisorestagio/apagar/(?P<hash>.*)/$', 
        s2306_supervisorestagio_views.apagar, 
        name='s2306_supervisorestagio_apagar'),

url(r'^s2306-supervisorestagio/api/$',
            s2306_supervisorestagio_views.s2306supervisorEstagioList.as_view() ),

        url(r'^s2306-supervisorestagio/api/(?P<pk>[0-9]+)/$',
            s2306_supervisorestagio_views.s2306supervisorEstagioDetail.as_view() ),

url(r'^s2306-supervisorestagio/listar/(?P<hash>.*)/$', 
        s2306_supervisorestagio_views.listar, 
        name='s2306_supervisorestagio'),

url(r'^s2306-supervisorestagio/salvar/(?P<hash>.*)/$', 
        s2306_supervisorestagio_views.salvar, 
        name='s2306_supervisorestagio_salvar'),





]