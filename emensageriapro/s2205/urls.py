#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2205.views import s2205_documentos_apagar as s2205_documentos_apagar_views
from emensageriapro.s2205.views import s2205_documentos_listar as s2205_documentos_listar_views
from emensageriapro.s2205.views import s2205_documentos_salvar as s2205_documentos_salvar_views
from emensageriapro.s2205.views import s2205_documentos_api as s2205_documentos_api_views
from emensageriapro.s2205.views import s2205_ctps_apagar as s2205_ctps_apagar_views
from emensageriapro.s2205.views import s2205_ctps_listar as s2205_ctps_listar_views
from emensageriapro.s2205.views import s2205_ctps_salvar as s2205_ctps_salvar_views
from emensageriapro.s2205.views import s2205_ctps_api as s2205_ctps_api_views
from emensageriapro.s2205.views import s2205_ric_apagar as s2205_ric_apagar_views
from emensageriapro.s2205.views import s2205_ric_listar as s2205_ric_listar_views
from emensageriapro.s2205.views import s2205_ric_salvar as s2205_ric_salvar_views
from emensageriapro.s2205.views import s2205_ric_api as s2205_ric_api_views
from emensageriapro.s2205.views import s2205_rg_apagar as s2205_rg_apagar_views
from emensageriapro.s2205.views import s2205_rg_listar as s2205_rg_listar_views
from emensageriapro.s2205.views import s2205_rg_salvar as s2205_rg_salvar_views
from emensageriapro.s2205.views import s2205_rg_api as s2205_rg_api_views
from emensageriapro.s2205.views import s2205_rne_apagar as s2205_rne_apagar_views
from emensageriapro.s2205.views import s2205_rne_listar as s2205_rne_listar_views
from emensageriapro.s2205.views import s2205_rne_salvar as s2205_rne_salvar_views
from emensageriapro.s2205.views import s2205_rne_api as s2205_rne_api_views
from emensageriapro.s2205.views import s2205_oc_apagar as s2205_oc_apagar_views
from emensageriapro.s2205.views import s2205_oc_listar as s2205_oc_listar_views
from emensageriapro.s2205.views import s2205_oc_salvar as s2205_oc_salvar_views
from emensageriapro.s2205.views import s2205_oc_api as s2205_oc_api_views
from emensageriapro.s2205.views import s2205_cnh_apagar as s2205_cnh_apagar_views
from emensageriapro.s2205.views import s2205_cnh_listar as s2205_cnh_listar_views
from emensageriapro.s2205.views import s2205_cnh_salvar as s2205_cnh_salvar_views
from emensageriapro.s2205.views import s2205_cnh_api as s2205_cnh_api_views
from emensageriapro.s2205.views import s2205_brasil_apagar as s2205_brasil_apagar_views
from emensageriapro.s2205.views import s2205_brasil_listar as s2205_brasil_listar_views
from emensageriapro.s2205.views import s2205_brasil_salvar as s2205_brasil_salvar_views
from emensageriapro.s2205.views import s2205_brasil_api as s2205_brasil_api_views
from emensageriapro.s2205.views import s2205_exterior_apagar as s2205_exterior_apagar_views
from emensageriapro.s2205.views import s2205_exterior_listar as s2205_exterior_listar_views
from emensageriapro.s2205.views import s2205_exterior_salvar as s2205_exterior_salvar_views
from emensageriapro.s2205.views import s2205_exterior_api as s2205_exterior_api_views
from emensageriapro.s2205.views import s2205_trabestrangeiro_apagar as s2205_trabestrangeiro_apagar_views
from emensageriapro.s2205.views import s2205_trabestrangeiro_listar as s2205_trabestrangeiro_listar_views
from emensageriapro.s2205.views import s2205_trabestrangeiro_salvar as s2205_trabestrangeiro_salvar_views
from emensageriapro.s2205.views import s2205_trabestrangeiro_api as s2205_trabestrangeiro_api_views
from emensageriapro.s2205.views import s2205_infodeficiencia_apagar as s2205_infodeficiencia_apagar_views
from emensageriapro.s2205.views import s2205_infodeficiencia_listar as s2205_infodeficiencia_listar_views
from emensageriapro.s2205.views import s2205_infodeficiencia_salvar as s2205_infodeficiencia_salvar_views
from emensageriapro.s2205.views import s2205_infodeficiencia_api as s2205_infodeficiencia_api_views
from emensageriapro.s2205.views import s2205_dependente_apagar as s2205_dependente_apagar_views
from emensageriapro.s2205.views import s2205_dependente_listar as s2205_dependente_listar_views
from emensageriapro.s2205.views import s2205_dependente_salvar as s2205_dependente_salvar_views
from emensageriapro.s2205.views import s2205_dependente_api as s2205_dependente_api_views
from emensageriapro.s2205.views import s2205_aposentadoria_apagar as s2205_aposentadoria_apagar_views
from emensageriapro.s2205.views import s2205_aposentadoria_listar as s2205_aposentadoria_listar_views
from emensageriapro.s2205.views import s2205_aposentadoria_salvar as s2205_aposentadoria_salvar_views
from emensageriapro.s2205.views import s2205_aposentadoria_api as s2205_aposentadoria_api_views
from emensageriapro.s2205.views import s2205_contato_apagar as s2205_contato_apagar_views
from emensageriapro.s2205.views import s2205_contato_listar as s2205_contato_listar_views
from emensageriapro.s2205.views import s2205_contato_salvar as s2205_contato_salvar_views
from emensageriapro.s2205.views import s2205_contato_api as s2205_contato_api_views



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


    url(r'^s2205-documentos/apagar/(?P<pk>[0-9]+)/$',
        s2205_documentos_apagar_views.apagar,
        name='s2205_documentos_apagar'),

    url(r'^s2205-documentos/api/$',
        s2205_documentos_api_views.s2205documentosList.as_view() ),

    url(r'^s2205-documentos/api/(?P<pk>[0-9]+)/$',
        s2205_documentos_api_views.s2205documentosDetail.as_view() ),

    url(r'^s2205-documentos/$',
        s2205_documentos_listar_views.listar,
        name='s2205_documentos'),

    url(r'^s2205-documentos/salvar/(?P<pk>[0-9]+)/$',
        s2205_documentos_salvar_views.salvar,
        name='s2205_documentos_salvar'),

    url(r'^s2205-documentos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_documentos_salvar_views.salvar,
        name='s2205_documentos_salvar_tab'),

    url(r'^s2205-documentos/cadastrar/$',
        s2205_documentos_salvar_views.salvar,
        name='s2205_documentos_cadastrar'),

    url(r'^s2205-documentos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_documentos_salvar_views.salvar,
        name='s2205_documentos_salvar_output'),

    url(r'^s2205-documentos/(?P<output>[\w-]+)/$',
        s2205_documentos_listar_views.listar,
        name='s2205_documentos_output'),

    url(r'^s2205-ctps/apagar/(?P<pk>[0-9]+)/$',
        s2205_ctps_apagar_views.apagar,
        name='s2205_ctps_apagar'),

    url(r'^s2205-ctps/api/$',
        s2205_ctps_api_views.s2205CTPSList.as_view() ),

    url(r'^s2205-ctps/api/(?P<pk>[0-9]+)/$',
        s2205_ctps_api_views.s2205CTPSDetail.as_view() ),

    url(r'^s2205-ctps/$',
        s2205_ctps_listar_views.listar,
        name='s2205_ctps'),

    url(r'^s2205-ctps/salvar/(?P<pk>[0-9]+)/$',
        s2205_ctps_salvar_views.salvar,
        name='s2205_ctps_salvar'),

    url(r'^s2205-ctps/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_ctps_salvar_views.salvar,
        name='s2205_ctps_salvar_tab'),

    url(r'^s2205-ctps/cadastrar/$',
        s2205_ctps_salvar_views.salvar,
        name='s2205_ctps_cadastrar'),

    url(r'^s2205-ctps/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_ctps_salvar_views.salvar,
        name='s2205_ctps_salvar_output'),

    url(r'^s2205-ctps/(?P<output>[\w-]+)/$',
        s2205_ctps_listar_views.listar,
        name='s2205_ctps_output'),

    url(r'^s2205-ric/apagar/(?P<pk>[0-9]+)/$',
        s2205_ric_apagar_views.apagar,
        name='s2205_ric_apagar'),

    url(r'^s2205-ric/api/$',
        s2205_ric_api_views.s2205RICList.as_view() ),

    url(r'^s2205-ric/api/(?P<pk>[0-9]+)/$',
        s2205_ric_api_views.s2205RICDetail.as_view() ),

    url(r'^s2205-ric/$',
        s2205_ric_listar_views.listar,
        name='s2205_ric'),

    url(r'^s2205-ric/salvar/(?P<pk>[0-9]+)/$',
        s2205_ric_salvar_views.salvar,
        name='s2205_ric_salvar'),

    url(r'^s2205-ric/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_ric_salvar_views.salvar,
        name='s2205_ric_salvar_tab'),

    url(r'^s2205-ric/cadastrar/$',
        s2205_ric_salvar_views.salvar,
        name='s2205_ric_cadastrar'),

    url(r'^s2205-ric/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_ric_salvar_views.salvar,
        name='s2205_ric_salvar_output'),

    url(r'^s2205-ric/(?P<output>[\w-]+)/$',
        s2205_ric_listar_views.listar,
        name='s2205_ric_output'),

    url(r'^s2205-rg/apagar/(?P<pk>[0-9]+)/$',
        s2205_rg_apagar_views.apagar,
        name='s2205_rg_apagar'),

    url(r'^s2205-rg/api/$',
        s2205_rg_api_views.s2205RGList.as_view() ),

    url(r'^s2205-rg/api/(?P<pk>[0-9]+)/$',
        s2205_rg_api_views.s2205RGDetail.as_view() ),

    url(r'^s2205-rg/$',
        s2205_rg_listar_views.listar,
        name='s2205_rg'),

    url(r'^s2205-rg/salvar/(?P<pk>[0-9]+)/$',
        s2205_rg_salvar_views.salvar,
        name='s2205_rg_salvar'),

    url(r'^s2205-rg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_rg_salvar_views.salvar,
        name='s2205_rg_salvar_tab'),

    url(r'^s2205-rg/cadastrar/$',
        s2205_rg_salvar_views.salvar,
        name='s2205_rg_cadastrar'),

    url(r'^s2205-rg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_rg_salvar_views.salvar,
        name='s2205_rg_salvar_output'),

    url(r'^s2205-rg/(?P<output>[\w-]+)/$',
        s2205_rg_listar_views.listar,
        name='s2205_rg_output'),

    url(r'^s2205-rne/apagar/(?P<pk>[0-9]+)/$',
        s2205_rne_apagar_views.apagar,
        name='s2205_rne_apagar'),

    url(r'^s2205-rne/api/$',
        s2205_rne_api_views.s2205RNEList.as_view() ),

    url(r'^s2205-rne/api/(?P<pk>[0-9]+)/$',
        s2205_rne_api_views.s2205RNEDetail.as_view() ),

    url(r'^s2205-rne/$',
        s2205_rne_listar_views.listar,
        name='s2205_rne'),

    url(r'^s2205-rne/salvar/(?P<pk>[0-9]+)/$',
        s2205_rne_salvar_views.salvar,
        name='s2205_rne_salvar'),

    url(r'^s2205-rne/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_rne_salvar_views.salvar,
        name='s2205_rne_salvar_tab'),

    url(r'^s2205-rne/cadastrar/$',
        s2205_rne_salvar_views.salvar,
        name='s2205_rne_cadastrar'),

    url(r'^s2205-rne/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_rne_salvar_views.salvar,
        name='s2205_rne_salvar_output'),

    url(r'^s2205-rne/(?P<output>[\w-]+)/$',
        s2205_rne_listar_views.listar,
        name='s2205_rne_output'),

    url(r'^s2205-oc/apagar/(?P<pk>[0-9]+)/$',
        s2205_oc_apagar_views.apagar,
        name='s2205_oc_apagar'),

    url(r'^s2205-oc/api/$',
        s2205_oc_api_views.s2205OCList.as_view() ),

    url(r'^s2205-oc/api/(?P<pk>[0-9]+)/$',
        s2205_oc_api_views.s2205OCDetail.as_view() ),

    url(r'^s2205-oc/$',
        s2205_oc_listar_views.listar,
        name='s2205_oc'),

    url(r'^s2205-oc/salvar/(?P<pk>[0-9]+)/$',
        s2205_oc_salvar_views.salvar,
        name='s2205_oc_salvar'),

    url(r'^s2205-oc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_oc_salvar_views.salvar,
        name='s2205_oc_salvar_tab'),

    url(r'^s2205-oc/cadastrar/$',
        s2205_oc_salvar_views.salvar,
        name='s2205_oc_cadastrar'),

    url(r'^s2205-oc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_oc_salvar_views.salvar,
        name='s2205_oc_salvar_output'),

    url(r'^s2205-oc/(?P<output>[\w-]+)/$',
        s2205_oc_listar_views.listar,
        name='s2205_oc_output'),

    url(r'^s2205-cnh/apagar/(?P<pk>[0-9]+)/$',
        s2205_cnh_apagar_views.apagar,
        name='s2205_cnh_apagar'),

    url(r'^s2205-cnh/api/$',
        s2205_cnh_api_views.s2205CNHList.as_view() ),

    url(r'^s2205-cnh/api/(?P<pk>[0-9]+)/$',
        s2205_cnh_api_views.s2205CNHDetail.as_view() ),

    url(r'^s2205-cnh/$',
        s2205_cnh_listar_views.listar,
        name='s2205_cnh'),

    url(r'^s2205-cnh/salvar/(?P<pk>[0-9]+)/$',
        s2205_cnh_salvar_views.salvar,
        name='s2205_cnh_salvar'),

    url(r'^s2205-cnh/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_cnh_salvar_views.salvar,
        name='s2205_cnh_salvar_tab'),

    url(r'^s2205-cnh/cadastrar/$',
        s2205_cnh_salvar_views.salvar,
        name='s2205_cnh_cadastrar'),

    url(r'^s2205-cnh/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_cnh_salvar_views.salvar,
        name='s2205_cnh_salvar_output'),

    url(r'^s2205-cnh/(?P<output>[\w-]+)/$',
        s2205_cnh_listar_views.listar,
        name='s2205_cnh_output'),

    url(r'^s2205-brasil/apagar/(?P<pk>[0-9]+)/$',
        s2205_brasil_apagar_views.apagar,
        name='s2205_brasil_apagar'),

    url(r'^s2205-brasil/api/$',
        s2205_brasil_api_views.s2205brasilList.as_view() ),

    url(r'^s2205-brasil/api/(?P<pk>[0-9]+)/$',
        s2205_brasil_api_views.s2205brasilDetail.as_view() ),

    url(r'^s2205-brasil/$',
        s2205_brasil_listar_views.listar,
        name='s2205_brasil'),

    url(r'^s2205-brasil/salvar/(?P<pk>[0-9]+)/$',
        s2205_brasil_salvar_views.salvar,
        name='s2205_brasil_salvar'),

    url(r'^s2205-brasil/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_brasil_salvar_views.salvar,
        name='s2205_brasil_salvar_tab'),

    url(r'^s2205-brasil/cadastrar/$',
        s2205_brasil_salvar_views.salvar,
        name='s2205_brasil_cadastrar'),

    url(r'^s2205-brasil/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_brasil_salvar_views.salvar,
        name='s2205_brasil_salvar_output'),

    url(r'^s2205-brasil/(?P<output>[\w-]+)/$',
        s2205_brasil_listar_views.listar,
        name='s2205_brasil_output'),

    url(r'^s2205-exterior/apagar/(?P<pk>[0-9]+)/$',
        s2205_exterior_apagar_views.apagar,
        name='s2205_exterior_apagar'),

    url(r'^s2205-exterior/api/$',
        s2205_exterior_api_views.s2205exteriorList.as_view() ),

    url(r'^s2205-exterior/api/(?P<pk>[0-9]+)/$',
        s2205_exterior_api_views.s2205exteriorDetail.as_view() ),

    url(r'^s2205-exterior/$',
        s2205_exterior_listar_views.listar,
        name='s2205_exterior'),

    url(r'^s2205-exterior/salvar/(?P<pk>[0-9]+)/$',
        s2205_exterior_salvar_views.salvar,
        name='s2205_exterior_salvar'),

    url(r'^s2205-exterior/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_exterior_salvar_views.salvar,
        name='s2205_exterior_salvar_tab'),

    url(r'^s2205-exterior/cadastrar/$',
        s2205_exterior_salvar_views.salvar,
        name='s2205_exterior_cadastrar'),

    url(r'^s2205-exterior/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_exterior_salvar_views.salvar,
        name='s2205_exterior_salvar_output'),

    url(r'^s2205-exterior/(?P<output>[\w-]+)/$',
        s2205_exterior_listar_views.listar,
        name='s2205_exterior_output'),

    url(r'^s2205-trabestrangeiro/apagar/(?P<pk>[0-9]+)/$',
        s2205_trabestrangeiro_apagar_views.apagar,
        name='s2205_trabestrangeiro_apagar'),

    url(r'^s2205-trabestrangeiro/api/$',
        s2205_trabestrangeiro_api_views.s2205trabEstrangeiroList.as_view() ),

    url(r'^s2205-trabestrangeiro/api/(?P<pk>[0-9]+)/$',
        s2205_trabestrangeiro_api_views.s2205trabEstrangeiroDetail.as_view() ),

    url(r'^s2205-trabestrangeiro/$',
        s2205_trabestrangeiro_listar_views.listar,
        name='s2205_trabestrangeiro'),

    url(r'^s2205-trabestrangeiro/salvar/(?P<pk>[0-9]+)/$',
        s2205_trabestrangeiro_salvar_views.salvar,
        name='s2205_trabestrangeiro_salvar'),

    url(r'^s2205-trabestrangeiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_trabestrangeiro_salvar_views.salvar,
        name='s2205_trabestrangeiro_salvar_tab'),

    url(r'^s2205-trabestrangeiro/cadastrar/$',
        s2205_trabestrangeiro_salvar_views.salvar,
        name='s2205_trabestrangeiro_cadastrar'),

    url(r'^s2205-trabestrangeiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_trabestrangeiro_salvar_views.salvar,
        name='s2205_trabestrangeiro_salvar_output'),

    url(r'^s2205-trabestrangeiro/(?P<output>[\w-]+)/$',
        s2205_trabestrangeiro_listar_views.listar,
        name='s2205_trabestrangeiro_output'),

    url(r'^s2205-infodeficiencia/apagar/(?P<pk>[0-9]+)/$',
        s2205_infodeficiencia_apagar_views.apagar,
        name='s2205_infodeficiencia_apagar'),

    url(r'^s2205-infodeficiencia/api/$',
        s2205_infodeficiencia_api_views.s2205infoDeficienciaList.as_view() ),

    url(r'^s2205-infodeficiencia/api/(?P<pk>[0-9]+)/$',
        s2205_infodeficiencia_api_views.s2205infoDeficienciaDetail.as_view() ),

    url(r'^s2205-infodeficiencia/$',
        s2205_infodeficiencia_listar_views.listar,
        name='s2205_infodeficiencia'),

    url(r'^s2205-infodeficiencia/salvar/(?P<pk>[0-9]+)/$',
        s2205_infodeficiencia_salvar_views.salvar,
        name='s2205_infodeficiencia_salvar'),

    url(r'^s2205-infodeficiencia/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_infodeficiencia_salvar_views.salvar,
        name='s2205_infodeficiencia_salvar_tab'),

    url(r'^s2205-infodeficiencia/cadastrar/$',
        s2205_infodeficiencia_salvar_views.salvar,
        name='s2205_infodeficiencia_cadastrar'),

    url(r'^s2205-infodeficiencia/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_infodeficiencia_salvar_views.salvar,
        name='s2205_infodeficiencia_salvar_output'),

    url(r'^s2205-infodeficiencia/(?P<output>[\w-]+)/$',
        s2205_infodeficiencia_listar_views.listar,
        name='s2205_infodeficiencia_output'),

    url(r'^s2205-dependente/apagar/(?P<pk>[0-9]+)/$',
        s2205_dependente_apagar_views.apagar,
        name='s2205_dependente_apagar'),

    url(r'^s2205-dependente/api/$',
        s2205_dependente_api_views.s2205dependenteList.as_view() ),

    url(r'^s2205-dependente/api/(?P<pk>[0-9]+)/$',
        s2205_dependente_api_views.s2205dependenteDetail.as_view() ),

    url(r'^s2205-dependente/$',
        s2205_dependente_listar_views.listar,
        name='s2205_dependente'),

    url(r'^s2205-dependente/salvar/(?P<pk>[0-9]+)/$',
        s2205_dependente_salvar_views.salvar,
        name='s2205_dependente_salvar'),

    url(r'^s2205-dependente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_dependente_salvar_views.salvar,
        name='s2205_dependente_salvar_tab'),

    url(r'^s2205-dependente/cadastrar/$',
        s2205_dependente_salvar_views.salvar,
        name='s2205_dependente_cadastrar'),

    url(r'^s2205-dependente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_dependente_salvar_views.salvar,
        name='s2205_dependente_salvar_output'),

    url(r'^s2205-dependente/(?P<output>[\w-]+)/$',
        s2205_dependente_listar_views.listar,
        name='s2205_dependente_output'),

    url(r'^s2205-aposentadoria/apagar/(?P<pk>[0-9]+)/$',
        s2205_aposentadoria_apagar_views.apagar,
        name='s2205_aposentadoria_apagar'),

    url(r'^s2205-aposentadoria/api/$',
        s2205_aposentadoria_api_views.s2205aposentadoriaList.as_view() ),

    url(r'^s2205-aposentadoria/api/(?P<pk>[0-9]+)/$',
        s2205_aposentadoria_api_views.s2205aposentadoriaDetail.as_view() ),

    url(r'^s2205-aposentadoria/$',
        s2205_aposentadoria_listar_views.listar,
        name='s2205_aposentadoria'),

    url(r'^s2205-aposentadoria/salvar/(?P<pk>[0-9]+)/$',
        s2205_aposentadoria_salvar_views.salvar,
        name='s2205_aposentadoria_salvar'),

    url(r'^s2205-aposentadoria/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_aposentadoria_salvar_views.salvar,
        name='s2205_aposentadoria_salvar_tab'),

    url(r'^s2205-aposentadoria/cadastrar/$',
        s2205_aposentadoria_salvar_views.salvar,
        name='s2205_aposentadoria_cadastrar'),

    url(r'^s2205-aposentadoria/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_aposentadoria_salvar_views.salvar,
        name='s2205_aposentadoria_salvar_output'),

    url(r'^s2205-aposentadoria/(?P<output>[\w-]+)/$',
        s2205_aposentadoria_listar_views.listar,
        name='s2205_aposentadoria_output'),

    url(r'^s2205-contato/apagar/(?P<pk>[0-9]+)/$',
        s2205_contato_apagar_views.apagar,
        name='s2205_contato_apagar'),

    url(r'^s2205-contato/api/$',
        s2205_contato_api_views.s2205contatoList.as_view() ),

    url(r'^s2205-contato/api/(?P<pk>[0-9]+)/$',
        s2205_contato_api_views.s2205contatoDetail.as_view() ),

    url(r'^s2205-contato/$',
        s2205_contato_listar_views.listar,
        name='s2205_contato'),

    url(r'^s2205-contato/salvar/(?P<pk>[0-9]+)/$',
        s2205_contato_salvar_views.salvar,
        name='s2205_contato_salvar'),

    url(r'^s2205-contato/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2205_contato_salvar_views.salvar,
        name='s2205_contato_salvar_tab'),

    url(r'^s2205-contato/cadastrar/$',
        s2205_contato_salvar_views.salvar,
        name='s2205_contato_cadastrar'),

    url(r'^s2205-contato/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2205_contato_salvar_views.salvar,
        name='s2205_contato_salvar_output'),

    url(r'^s2205-contato/(?P<output>[\w-]+)/$',
        s2205_contato_listar_views.listar,
        name='s2205_contato_output'),


]