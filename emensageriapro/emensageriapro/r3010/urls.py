#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r3010.views import r3010_boletim_apagar as r3010_boletim_apagar_views
from emensageriapro.r3010.views import r3010_boletim_listar as r3010_boletim_listar_views
from emensageriapro.r3010.views import r3010_boletim_salvar as r3010_boletim_salvar_views
from emensageriapro.r3010.views import r3010_boletim_api as r3010_boletim_api_views
from emensageriapro.r3010.views import r3010_receitaingressos_apagar as r3010_receitaingressos_apagar_views
from emensageriapro.r3010.views import r3010_receitaingressos_listar as r3010_receitaingressos_listar_views
from emensageriapro.r3010.views import r3010_receitaingressos_salvar as r3010_receitaingressos_salvar_views
from emensageriapro.r3010.views import r3010_receitaingressos_api as r3010_receitaingressos_api_views
from emensageriapro.r3010.views import r3010_outrasreceitas_apagar as r3010_outrasreceitas_apagar_views
from emensageriapro.r3010.views import r3010_outrasreceitas_listar as r3010_outrasreceitas_listar_views
from emensageriapro.r3010.views import r3010_outrasreceitas_salvar as r3010_outrasreceitas_salvar_views
from emensageriapro.r3010.views import r3010_outrasreceitas_api as r3010_outrasreceitas_api_views
from emensageriapro.r3010.views import r3010_infoproc_apagar as r3010_infoproc_apagar_views
from emensageriapro.r3010.views import r3010_infoproc_listar as r3010_infoproc_listar_views
from emensageriapro.r3010.views import r3010_infoproc_salvar as r3010_infoproc_salvar_views
from emensageriapro.r3010.views import r3010_infoproc_api as r3010_infoproc_api_views


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


    url(r'^r3010-boletim/apagar/(?P<pk>[0-9]+)/$',
        r3010_boletim_apagar_views.apagar,
        name='r3010_boletim_apagar'),

    url(r'^r3010-boletim/api/$',
        r3010_boletim_api_views.r3010boletimList.as_view() ),

    url(r'^r3010-boletim/api/(?P<pk>[0-9]+)/$',
        r3010_boletim_api_views.r3010boletimDetail.as_view() ),

    url(r'^r3010-boletim/$',
        r3010_boletim_listar_views.listar,
        name='r3010_boletim'),

    url(r'^r3010-boletim/salvar/(?P<pk>[0-9]+)/$',
        r3010_boletim_salvar_views.salvar,
        name='r3010_boletim_salvar'),

    url(r'^r3010-boletim/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r3010_boletim_salvar_views.salvar,
        name='r3010_boletim_salvar_tab'),

    url(r'^r3010-boletim/cadastrar/$',
        r3010_boletim_salvar_views.salvar,
        name='r3010_boletim_cadastrar'),

    url(r'^r3010-boletim/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r3010_boletim_salvar_views.salvar,
        name='r3010_boletim_salvar_output'),

    url(r'^r3010-boletim/(?P<output>[\w-]+)/$',
        r3010_boletim_listar_views.listar,
        name='r3010_boletim_output'),

    url(r'^r3010-receitaingressos/apagar/(?P<pk>[0-9]+)/$',
        r3010_receitaingressos_apagar_views.apagar,
        name='r3010_receitaingressos_apagar'),

    url(r'^r3010-receitaingressos/api/$',
        r3010_receitaingressos_api_views.r3010receitaIngressosList.as_view() ),

    url(r'^r3010-receitaingressos/api/(?P<pk>[0-9]+)/$',
        r3010_receitaingressos_api_views.r3010receitaIngressosDetail.as_view() ),

    url(r'^r3010-receitaingressos/$',
        r3010_receitaingressos_listar_views.listar,
        name='r3010_receitaingressos'),

    url(r'^r3010-receitaingressos/salvar/(?P<pk>[0-9]+)/$',
        r3010_receitaingressos_salvar_views.salvar,
        name='r3010_receitaingressos_salvar'),

    url(r'^r3010-receitaingressos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r3010_receitaingressos_salvar_views.salvar,
        name='r3010_receitaingressos_salvar_tab'),

    url(r'^r3010-receitaingressos/cadastrar/$',
        r3010_receitaingressos_salvar_views.salvar,
        name='r3010_receitaingressos_cadastrar'),

    url(r'^r3010-receitaingressos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r3010_receitaingressos_salvar_views.salvar,
        name='r3010_receitaingressos_salvar_output'),

    url(r'^r3010-receitaingressos/(?P<output>[\w-]+)/$',
        r3010_receitaingressos_listar_views.listar,
        name='r3010_receitaingressos_output'),

    url(r'^r3010-outrasreceitas/apagar/(?P<pk>[0-9]+)/$',
        r3010_outrasreceitas_apagar_views.apagar,
        name='r3010_outrasreceitas_apagar'),

    url(r'^r3010-outrasreceitas/api/$',
        r3010_outrasreceitas_api_views.r3010outrasReceitasList.as_view() ),

    url(r'^r3010-outrasreceitas/api/(?P<pk>[0-9]+)/$',
        r3010_outrasreceitas_api_views.r3010outrasReceitasDetail.as_view() ),

    url(r'^r3010-outrasreceitas/$',
        r3010_outrasreceitas_listar_views.listar,
        name='r3010_outrasreceitas'),

    url(r'^r3010-outrasreceitas/salvar/(?P<pk>[0-9]+)/$',
        r3010_outrasreceitas_salvar_views.salvar,
        name='r3010_outrasreceitas_salvar'),

    url(r'^r3010-outrasreceitas/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r3010_outrasreceitas_salvar_views.salvar,
        name='r3010_outrasreceitas_salvar_tab'),

    url(r'^r3010-outrasreceitas/cadastrar/$',
        r3010_outrasreceitas_salvar_views.salvar,
        name='r3010_outrasreceitas_cadastrar'),

    url(r'^r3010-outrasreceitas/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r3010_outrasreceitas_salvar_views.salvar,
        name='r3010_outrasreceitas_salvar_output'),

    url(r'^r3010-outrasreceitas/(?P<output>[\w-]+)/$',
        r3010_outrasreceitas_listar_views.listar,
        name='r3010_outrasreceitas_output'),

    url(r'^r3010-infoproc/apagar/(?P<pk>[0-9]+)/$',
        r3010_infoproc_apagar_views.apagar,
        name='r3010_infoproc_apagar'),

    url(r'^r3010-infoproc/api/$',
        r3010_infoproc_api_views.r3010infoProcList.as_view() ),

    url(r'^r3010-infoproc/api/(?P<pk>[0-9]+)/$',
        r3010_infoproc_api_views.r3010infoProcDetail.as_view() ),

    url(r'^r3010-infoproc/$',
        r3010_infoproc_listar_views.listar,
        name='r3010_infoproc'),

    url(r'^r3010-infoproc/salvar/(?P<pk>[0-9]+)/$',
        r3010_infoproc_salvar_views.salvar,
        name='r3010_infoproc_salvar'),

    url(r'^r3010-infoproc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r3010_infoproc_salvar_views.salvar,
        name='r3010_infoproc_salvar_tab'),

    url(r'^r3010-infoproc/cadastrar/$',
        r3010_infoproc_salvar_views.salvar,
        name='r3010_infoproc_cadastrar'),

    url(r'^r3010-infoproc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r3010_infoproc_salvar_views.salvar,
        name='r3010_infoproc_salvar_output'),

    url(r'^r3010-infoproc/(?P<output>[\w-]+)/$',
        r3010_infoproc_listar_views.listar,
        name='r3010_infoproc_output'),


]