#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.mapa_processamento.views import mapa_importacoes as mapa_importacoes_views
from emensageriapro.mapa_processamento.views import mapa_esocial as mapa_esocial_views
from emensageriapro.mapa_processamento.views import mapa_efdreinf as mapa_efdreinf_views
from emensageriapro.mapa_processamento.views import funcoes_automaticas_esocial as funcoes_automaticas_esocial_views
from emensageriapro.mapa_processamento.views import funcoes_automaticas_efdreinf as funcoes_automaticas_efdreinf_views
from emensageriapro.mapa_processamento.views import visao_geral as visao_geral_views



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


    url(r'^importacoes/(?P<tab>[\w-]+)/$',
        mapa_importacoes_views.listar,
        name='mapa_importacoes'),

    url(r'^esocial/(?P<tab>[\w-]+)/$',
        mapa_esocial_views.listar,
        name='mapa_esocial'),

    url(r'^efdreinf/(?P<tab>[\w-]+)/$',
        mapa_efdreinf_views.listar,
        name='mapa_efdreinf'),

    url(r'^esocial-validar/$',
        funcoes_automaticas_esocial_views.validar,
        name='esocial_validar'),

    url(r'^esocial-validar/(?P<tab>[\w-]+)/$',
        funcoes_automaticas_esocial_views.validar,
        name='esocial_validar_api'),

    url(r'^esocial-enviar/$',
        funcoes_automaticas_esocial_views.enviar,
        name='esocial_enviar'),

    url(r'^esocial-enviar/(?P<tab>[\w-]+)/$',
        funcoes_automaticas_esocial_views.enviar,
        name='esocial_enviar_api'),

    url(r'^esocial-consultar/$',
        funcoes_automaticas_esocial_views.consultar,
        name='esocial_consultar'),

    url(r'^esocial-consultar/(?P<tab>[\w-]+)/$',
        funcoes_automaticas_esocial_views.consultar,
        name='esocial_consultar_api'),

    url(r'^efdreinf-validar/$',
        funcoes_automaticas_efdreinf_views.validar,
        name='efdreinf_validar'),

    url(r'^efdreinf-validar/(?P<tab>[\w-]+)/$',
        funcoes_automaticas_efdreinf_views.validar,
        name='efdreinf_validar_api'),

    url(r'^efdreinf-enviar/$',
        funcoes_automaticas_efdreinf_views.enviar,
        name='efdreinf_enviar'),

    url(r'^efdreinf-enviar/(?P<tab>[\w-]+)/$',
        funcoes_automaticas_efdreinf_views.enviar,
        name='efdreinf_enviar_api'),

    url(r'^efdreinf-consultar/$',
        funcoes_automaticas_efdreinf_views.consultar,
        name='efdreinf_consultar'),

    url(r'^efdreinf-consultar/(?P<tab>[\w-]+)/$',
        funcoes_automaticas_efdreinf_views.consultar,
        name='efdreinf_consultar_api'),

    url(r'^visao-geral/$',
        visao_geral_views.listar,
        name='visao_geral'),

    

    

    

    


]