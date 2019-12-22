# eMensageriaAI #
#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2230.views import s2230_iniafastamento_apagar as s2230_iniafastamento_apagar_views
from emensageriapro.s2230.views import s2230_iniafastamento_listar as s2230_iniafastamento_listar_views
from emensageriapro.s2230.views import s2230_iniafastamento_salvar as s2230_iniafastamento_salvar_views
from emensageriapro.s2230.views import s2230_iniafastamento_api as s2230_iniafastamento_api_views
from emensageriapro.s2230.views import s2230_infoatestado_apagar as s2230_infoatestado_apagar_views
from emensageriapro.s2230.views import s2230_infoatestado_listar as s2230_infoatestado_listar_views
from emensageriapro.s2230.views import s2230_infoatestado_salvar as s2230_infoatestado_salvar_views
from emensageriapro.s2230.views import s2230_infoatestado_api as s2230_infoatestado_api_views
from emensageriapro.s2230.views import s2230_emitente_apagar as s2230_emitente_apagar_views
from emensageriapro.s2230.views import s2230_emitente_listar as s2230_emitente_listar_views
from emensageriapro.s2230.views import s2230_emitente_salvar as s2230_emitente_salvar_views
from emensageriapro.s2230.views import s2230_emitente_api as s2230_emitente_api_views
from emensageriapro.s2230.views import s2230_infocessao_apagar as s2230_infocessao_apagar_views
from emensageriapro.s2230.views import s2230_infocessao_listar as s2230_infocessao_listar_views
from emensageriapro.s2230.views import s2230_infocessao_salvar as s2230_infocessao_salvar_views
from emensageriapro.s2230.views import s2230_infocessao_api as s2230_infocessao_api_views
from emensageriapro.s2230.views import s2230_infomandsind_apagar as s2230_infomandsind_apagar_views
from emensageriapro.s2230.views import s2230_infomandsind_listar as s2230_infomandsind_listar_views
from emensageriapro.s2230.views import s2230_infomandsind_salvar as s2230_infomandsind_salvar_views
from emensageriapro.s2230.views import s2230_infomandsind_api as s2230_infomandsind_api_views
from emensageriapro.s2230.views import s2230_inforetif_apagar as s2230_inforetif_apagar_views
from emensageriapro.s2230.views import s2230_inforetif_listar as s2230_inforetif_listar_views
from emensageriapro.s2230.views import s2230_inforetif_salvar as s2230_inforetif_salvar_views
from emensageriapro.s2230.views import s2230_inforetif_api as s2230_inforetif_api_views
from emensageriapro.s2230.views import s2230_fimafastamento_apagar as s2230_fimafastamento_apagar_views
from emensageriapro.s2230.views import s2230_fimafastamento_listar as s2230_fimafastamento_listar_views
from emensageriapro.s2230.views import s2230_fimafastamento_salvar as s2230_fimafastamento_salvar_views
from emensageriapro.s2230.views import s2230_fimafastamento_api as s2230_fimafastamento_api_views


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


    url(r'^s2230-iniafastamento/apagar/(?P<pk>[0-9]+)/$',
        s2230_iniafastamento_apagar_views.apagar,
        name='s2230_iniafastamento_apagar'),

    url(r'^s2230-iniafastamento/api/$',
        s2230_iniafastamento_api_views.s2230iniAfastamentoList.as_view() ),

    url(r'^s2230-iniafastamento/api/(?P<pk>[0-9]+)/$',
        s2230_iniafastamento_api_views.s2230iniAfastamentoDetail.as_view() ),

    url(r'^s2230-iniafastamento/$',
        s2230_iniafastamento_listar_views.listar,
        name='s2230_iniafastamento'),

    url(r'^s2230-iniafastamento/salvar/(?P<pk>[0-9]+)/$',
        s2230_iniafastamento_salvar_views.salvar,
        name='s2230_iniafastamento_salvar'),

    url(r'^s2230-iniafastamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2230_iniafastamento_salvar_views.salvar,
        name='s2230_iniafastamento_salvar_tab'),

    url(r'^s2230-iniafastamento/cadastrar/$',
        s2230_iniafastamento_salvar_views.salvar,
        name='s2230_iniafastamento_cadastrar'),

    url(r'^s2230-iniafastamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2230_iniafastamento_salvar_views.salvar,
        name='s2230_iniafastamento_salvar_output'),

    url(r'^s2230-iniafastamento/(?P<output>[\w-]+)/$',
        s2230_iniafastamento_listar_views.listar,
        name='s2230_iniafastamento_output'),

    url(r'^s2230-infoatestado/apagar/(?P<pk>[0-9]+)/$',
        s2230_infoatestado_apagar_views.apagar,
        name='s2230_infoatestado_apagar'),

    url(r'^s2230-infoatestado/api/$',
        s2230_infoatestado_api_views.s2230infoAtestadoList.as_view() ),

    url(r'^s2230-infoatestado/api/(?P<pk>[0-9]+)/$',
        s2230_infoatestado_api_views.s2230infoAtestadoDetail.as_view() ),

    url(r'^s2230-infoatestado/$',
        s2230_infoatestado_listar_views.listar,
        name='s2230_infoatestado'),

    url(r'^s2230-infoatestado/salvar/(?P<pk>[0-9]+)/$',
        s2230_infoatestado_salvar_views.salvar,
        name='s2230_infoatestado_salvar'),

    url(r'^s2230-infoatestado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2230_infoatestado_salvar_views.salvar,
        name='s2230_infoatestado_salvar_tab'),

    url(r'^s2230-infoatestado/cadastrar/$',
        s2230_infoatestado_salvar_views.salvar,
        name='s2230_infoatestado_cadastrar'),

    url(r'^s2230-infoatestado/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2230_infoatestado_salvar_views.salvar,
        name='s2230_infoatestado_salvar_output'),

    url(r'^s2230-infoatestado/(?P<output>[\w-]+)/$',
        s2230_infoatestado_listar_views.listar,
        name='s2230_infoatestado_output'),

    url(r'^s2230-emitente/apagar/(?P<pk>[0-9]+)/$',
        s2230_emitente_apagar_views.apagar,
        name='s2230_emitente_apagar'),

    url(r'^s2230-emitente/api/$',
        s2230_emitente_api_views.s2230emitenteList.as_view() ),

    url(r'^s2230-emitente/api/(?P<pk>[0-9]+)/$',
        s2230_emitente_api_views.s2230emitenteDetail.as_view() ),

    url(r'^s2230-emitente/$',
        s2230_emitente_listar_views.listar,
        name='s2230_emitente'),

    url(r'^s2230-emitente/salvar/(?P<pk>[0-9]+)/$',
        s2230_emitente_salvar_views.salvar,
        name='s2230_emitente_salvar'),

    url(r'^s2230-emitente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2230_emitente_salvar_views.salvar,
        name='s2230_emitente_salvar_tab'),

    url(r'^s2230-emitente/cadastrar/$',
        s2230_emitente_salvar_views.salvar,
        name='s2230_emitente_cadastrar'),

    url(r'^s2230-emitente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2230_emitente_salvar_views.salvar,
        name='s2230_emitente_salvar_output'),

    url(r'^s2230-emitente/(?P<output>[\w-]+)/$',
        s2230_emitente_listar_views.listar,
        name='s2230_emitente_output'),

    url(r'^s2230-infocessao/apagar/(?P<pk>[0-9]+)/$',
        s2230_infocessao_apagar_views.apagar,
        name='s2230_infocessao_apagar'),

    url(r'^s2230-infocessao/api/$',
        s2230_infocessao_api_views.s2230infoCessaoList.as_view() ),

    url(r'^s2230-infocessao/api/(?P<pk>[0-9]+)/$',
        s2230_infocessao_api_views.s2230infoCessaoDetail.as_view() ),

    url(r'^s2230-infocessao/$',
        s2230_infocessao_listar_views.listar,
        name='s2230_infocessao'),

    url(r'^s2230-infocessao/salvar/(?P<pk>[0-9]+)/$',
        s2230_infocessao_salvar_views.salvar,
        name='s2230_infocessao_salvar'),

    url(r'^s2230-infocessao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2230_infocessao_salvar_views.salvar,
        name='s2230_infocessao_salvar_tab'),

    url(r'^s2230-infocessao/cadastrar/$',
        s2230_infocessao_salvar_views.salvar,
        name='s2230_infocessao_cadastrar'),

    url(r'^s2230-infocessao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2230_infocessao_salvar_views.salvar,
        name='s2230_infocessao_salvar_output'),

    url(r'^s2230-infocessao/(?P<output>[\w-]+)/$',
        s2230_infocessao_listar_views.listar,
        name='s2230_infocessao_output'),

    url(r'^s2230-infomandsind/apagar/(?P<pk>[0-9]+)/$',
        s2230_infomandsind_apagar_views.apagar,
        name='s2230_infomandsind_apagar'),

    url(r'^s2230-infomandsind/api/$',
        s2230_infomandsind_api_views.s2230infoMandSindList.as_view() ),

    url(r'^s2230-infomandsind/api/(?P<pk>[0-9]+)/$',
        s2230_infomandsind_api_views.s2230infoMandSindDetail.as_view() ),

    url(r'^s2230-infomandsind/$',
        s2230_infomandsind_listar_views.listar,
        name='s2230_infomandsind'),

    url(r'^s2230-infomandsind/salvar/(?P<pk>[0-9]+)/$',
        s2230_infomandsind_salvar_views.salvar,
        name='s2230_infomandsind_salvar'),

    url(r'^s2230-infomandsind/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2230_infomandsind_salvar_views.salvar,
        name='s2230_infomandsind_salvar_tab'),

    url(r'^s2230-infomandsind/cadastrar/$',
        s2230_infomandsind_salvar_views.salvar,
        name='s2230_infomandsind_cadastrar'),

    url(r'^s2230-infomandsind/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2230_infomandsind_salvar_views.salvar,
        name='s2230_infomandsind_salvar_output'),

    url(r'^s2230-infomandsind/(?P<output>[\w-]+)/$',
        s2230_infomandsind_listar_views.listar,
        name='s2230_infomandsind_output'),

    url(r'^s2230-inforetif/apagar/(?P<pk>[0-9]+)/$',
        s2230_inforetif_apagar_views.apagar,
        name='s2230_inforetif_apagar'),

    url(r'^s2230-inforetif/api/$',
        s2230_inforetif_api_views.s2230infoRetifList.as_view() ),

    url(r'^s2230-inforetif/api/(?P<pk>[0-9]+)/$',
        s2230_inforetif_api_views.s2230infoRetifDetail.as_view() ),

    url(r'^s2230-inforetif/$',
        s2230_inforetif_listar_views.listar,
        name='s2230_inforetif'),

    url(r'^s2230-inforetif/salvar/(?P<pk>[0-9]+)/$',
        s2230_inforetif_salvar_views.salvar,
        name='s2230_inforetif_salvar'),

    url(r'^s2230-inforetif/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2230_inforetif_salvar_views.salvar,
        name='s2230_inforetif_salvar_tab'),

    url(r'^s2230-inforetif/cadastrar/$',
        s2230_inforetif_salvar_views.salvar,
        name='s2230_inforetif_cadastrar'),

    url(r'^s2230-inforetif/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2230_inforetif_salvar_views.salvar,
        name='s2230_inforetif_salvar_output'),

    url(r'^s2230-inforetif/(?P<output>[\w-]+)/$',
        s2230_inforetif_listar_views.listar,
        name='s2230_inforetif_output'),

    url(r'^s2230-fimafastamento/apagar/(?P<pk>[0-9]+)/$',
        s2230_fimafastamento_apagar_views.apagar,
        name='s2230_fimafastamento_apagar'),

    url(r'^s2230-fimafastamento/api/$',
        s2230_fimafastamento_api_views.s2230fimAfastamentoList.as_view() ),

    url(r'^s2230-fimafastamento/api/(?P<pk>[0-9]+)/$',
        s2230_fimafastamento_api_views.s2230fimAfastamentoDetail.as_view() ),

    url(r'^s2230-fimafastamento/$',
        s2230_fimafastamento_listar_views.listar,
        name='s2230_fimafastamento'),

    url(r'^s2230-fimafastamento/salvar/(?P<pk>[0-9]+)/$',
        s2230_fimafastamento_salvar_views.salvar,
        name='s2230_fimafastamento_salvar'),

    url(r'^s2230-fimafastamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2230_fimafastamento_salvar_views.salvar,
        name='s2230_fimafastamento_salvar_tab'),

    url(r'^s2230-fimafastamento/cadastrar/$',
        s2230_fimafastamento_salvar_views.salvar,
        name='s2230_fimafastamento_cadastrar'),

    url(r'^s2230-fimafastamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2230_fimafastamento_salvar_views.salvar,
        name='s2230_fimafastamento_salvar_output'),

    url(r'^s2230-fimafastamento/(?P<output>[\w-]+)/$',
        s2230_fimafastamento_listar_views.listar,
        name='s2230_fimafastamento_output'),


]