#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2200.views import s2200_documentos_apagar as s2200_documentos_apagar_views
from emensageriapro.s2200.views import s2200_documentos_listar as s2200_documentos_listar_views
from emensageriapro.s2200.views import s2200_documentos_salvar as s2200_documentos_salvar_views
from emensageriapro.s2200.views import s2200_documentos_api as s2200_documentos_api_views
from emensageriapro.s2200.views import s2200_ctps_apagar as s2200_ctps_apagar_views
from emensageriapro.s2200.views import s2200_ctps_listar as s2200_ctps_listar_views
from emensageriapro.s2200.views import s2200_ctps_salvar as s2200_ctps_salvar_views
from emensageriapro.s2200.views import s2200_ctps_api as s2200_ctps_api_views
from emensageriapro.s2200.views import s2200_ric_apagar as s2200_ric_apagar_views
from emensageriapro.s2200.views import s2200_ric_listar as s2200_ric_listar_views
from emensageriapro.s2200.views import s2200_ric_salvar as s2200_ric_salvar_views
from emensageriapro.s2200.views import s2200_ric_api as s2200_ric_api_views
from emensageriapro.s2200.views import s2200_rg_apagar as s2200_rg_apagar_views
from emensageriapro.s2200.views import s2200_rg_listar as s2200_rg_listar_views
from emensageriapro.s2200.views import s2200_rg_salvar as s2200_rg_salvar_views
from emensageriapro.s2200.views import s2200_rg_api as s2200_rg_api_views
from emensageriapro.s2200.views import s2200_rne_apagar as s2200_rne_apagar_views
from emensageriapro.s2200.views import s2200_rne_listar as s2200_rne_listar_views
from emensageriapro.s2200.views import s2200_rne_salvar as s2200_rne_salvar_views
from emensageriapro.s2200.views import s2200_rne_api as s2200_rne_api_views
from emensageriapro.s2200.views import s2200_oc_apagar as s2200_oc_apagar_views
from emensageriapro.s2200.views import s2200_oc_listar as s2200_oc_listar_views
from emensageriapro.s2200.views import s2200_oc_salvar as s2200_oc_salvar_views
from emensageriapro.s2200.views import s2200_oc_api as s2200_oc_api_views
from emensageriapro.s2200.views import s2200_cnh_apagar as s2200_cnh_apagar_views
from emensageriapro.s2200.views import s2200_cnh_listar as s2200_cnh_listar_views
from emensageriapro.s2200.views import s2200_cnh_salvar as s2200_cnh_salvar_views
from emensageriapro.s2200.views import s2200_cnh_api as s2200_cnh_api_views
from emensageriapro.s2200.views import s2200_brasil_apagar as s2200_brasil_apagar_views
from emensageriapro.s2200.views import s2200_brasil_listar as s2200_brasil_listar_views
from emensageriapro.s2200.views import s2200_brasil_salvar as s2200_brasil_salvar_views
from emensageriapro.s2200.views import s2200_brasil_api as s2200_brasil_api_views
from emensageriapro.s2200.views import s2200_exterior_apagar as s2200_exterior_apagar_views
from emensageriapro.s2200.views import s2200_exterior_listar as s2200_exterior_listar_views
from emensageriapro.s2200.views import s2200_exterior_salvar as s2200_exterior_salvar_views
from emensageriapro.s2200.views import s2200_exterior_api as s2200_exterior_api_views
from emensageriapro.s2200.views import s2200_trabestrangeiro_apagar as s2200_trabestrangeiro_apagar_views
from emensageriapro.s2200.views import s2200_trabestrangeiro_listar as s2200_trabestrangeiro_listar_views
from emensageriapro.s2200.views import s2200_trabestrangeiro_salvar as s2200_trabestrangeiro_salvar_views
from emensageriapro.s2200.views import s2200_trabestrangeiro_api as s2200_trabestrangeiro_api_views
from emensageriapro.s2200.views import s2200_infodeficiencia_apagar as s2200_infodeficiencia_apagar_views
from emensageriapro.s2200.views import s2200_infodeficiencia_listar as s2200_infodeficiencia_listar_views
from emensageriapro.s2200.views import s2200_infodeficiencia_salvar as s2200_infodeficiencia_salvar_views
from emensageriapro.s2200.views import s2200_infodeficiencia_api as s2200_infodeficiencia_api_views
from emensageriapro.s2200.views import s2200_dependente_apagar as s2200_dependente_apagar_views
from emensageriapro.s2200.views import s2200_dependente_listar as s2200_dependente_listar_views
from emensageriapro.s2200.views import s2200_dependente_salvar as s2200_dependente_salvar_views
from emensageriapro.s2200.views import s2200_dependente_api as s2200_dependente_api_views
from emensageriapro.s2200.views import s2200_aposentadoria_apagar as s2200_aposentadoria_apagar_views
from emensageriapro.s2200.views import s2200_aposentadoria_listar as s2200_aposentadoria_listar_views
from emensageriapro.s2200.views import s2200_aposentadoria_salvar as s2200_aposentadoria_salvar_views
from emensageriapro.s2200.views import s2200_aposentadoria_api as s2200_aposentadoria_api_views
from emensageriapro.s2200.views import s2200_contato_apagar as s2200_contato_apagar_views
from emensageriapro.s2200.views import s2200_contato_listar as s2200_contato_listar_views
from emensageriapro.s2200.views import s2200_contato_salvar as s2200_contato_salvar_views
from emensageriapro.s2200.views import s2200_contato_api as s2200_contato_api_views
from emensageriapro.s2200.views import s2200_infoceletista_apagar as s2200_infoceletista_apagar_views
from emensageriapro.s2200.views import s2200_infoceletista_listar as s2200_infoceletista_listar_views
from emensageriapro.s2200.views import s2200_infoceletista_salvar as s2200_infoceletista_salvar_views
from emensageriapro.s2200.views import s2200_infoceletista_api as s2200_infoceletista_api_views
from emensageriapro.s2200.views import s2200_trabtemporario_apagar as s2200_trabtemporario_apagar_views
from emensageriapro.s2200.views import s2200_trabtemporario_listar as s2200_trabtemporario_listar_views
from emensageriapro.s2200.views import s2200_trabtemporario_salvar as s2200_trabtemporario_salvar_views
from emensageriapro.s2200.views import s2200_trabtemporario_api as s2200_trabtemporario_api_views
from emensageriapro.s2200.views import s2200_ideestabvinc_apagar as s2200_ideestabvinc_apagar_views
from emensageriapro.s2200.views import s2200_ideestabvinc_listar as s2200_ideestabvinc_listar_views
from emensageriapro.s2200.views import s2200_ideestabvinc_salvar as s2200_ideestabvinc_salvar_views
from emensageriapro.s2200.views import s2200_ideestabvinc_api as s2200_ideestabvinc_api_views
from emensageriapro.s2200.views import s2200_idetrabsubstituido_apagar as s2200_idetrabsubstituido_apagar_views
from emensageriapro.s2200.views import s2200_idetrabsubstituido_listar as s2200_idetrabsubstituido_listar_views
from emensageriapro.s2200.views import s2200_idetrabsubstituido_salvar as s2200_idetrabsubstituido_salvar_views
from emensageriapro.s2200.views import s2200_idetrabsubstituido_api as s2200_idetrabsubstituido_api_views
from emensageriapro.s2200.views import s2200_aprend_apagar as s2200_aprend_apagar_views
from emensageriapro.s2200.views import s2200_aprend_listar as s2200_aprend_listar_views
from emensageriapro.s2200.views import s2200_aprend_salvar as s2200_aprend_salvar_views
from emensageriapro.s2200.views import s2200_aprend_api as s2200_aprend_api_views
from emensageriapro.s2200.views import s2200_infoestatutario_apagar as s2200_infoestatutario_apagar_views
from emensageriapro.s2200.views import s2200_infoestatutario_listar as s2200_infoestatutario_listar_views
from emensageriapro.s2200.views import s2200_infoestatutario_salvar as s2200_infoestatutario_salvar_views
from emensageriapro.s2200.views import s2200_infoestatutario_api as s2200_infoestatutario_api_views
from emensageriapro.s2200.views import s2200_infodecjud_apagar as s2200_infodecjud_apagar_views
from emensageriapro.s2200.views import s2200_infodecjud_listar as s2200_infodecjud_listar_views
from emensageriapro.s2200.views import s2200_infodecjud_salvar as s2200_infodecjud_salvar_views
from emensageriapro.s2200.views import s2200_infodecjud_api as s2200_infodecjud_api_views
from emensageriapro.s2200.views import s2200_localtrabgeral_apagar as s2200_localtrabgeral_apagar_views
from emensageriapro.s2200.views import s2200_localtrabgeral_listar as s2200_localtrabgeral_listar_views
from emensageriapro.s2200.views import s2200_localtrabgeral_salvar as s2200_localtrabgeral_salvar_views
from emensageriapro.s2200.views import s2200_localtrabgeral_api as s2200_localtrabgeral_api_views
from emensageriapro.s2200.views import s2200_localtrabdom_apagar as s2200_localtrabdom_apagar_views
from emensageriapro.s2200.views import s2200_localtrabdom_listar as s2200_localtrabdom_listar_views
from emensageriapro.s2200.views import s2200_localtrabdom_salvar as s2200_localtrabdom_salvar_views
from emensageriapro.s2200.views import s2200_localtrabdom_api as s2200_localtrabdom_api_views
from emensageriapro.s2200.views import s2200_horcontratual_apagar as s2200_horcontratual_apagar_views
from emensageriapro.s2200.views import s2200_horcontratual_listar as s2200_horcontratual_listar_views
from emensageriapro.s2200.views import s2200_horcontratual_salvar as s2200_horcontratual_salvar_views
from emensageriapro.s2200.views import s2200_horcontratual_api as s2200_horcontratual_api_views
from emensageriapro.s2200.views import s2200_horario_apagar as s2200_horario_apagar_views
from emensageriapro.s2200.views import s2200_horario_listar as s2200_horario_listar_views
from emensageriapro.s2200.views import s2200_horario_salvar as s2200_horario_salvar_views
from emensageriapro.s2200.views import s2200_horario_api as s2200_horario_api_views
from emensageriapro.s2200.views import s2200_filiacaosindical_apagar as s2200_filiacaosindical_apagar_views
from emensageriapro.s2200.views import s2200_filiacaosindical_listar as s2200_filiacaosindical_listar_views
from emensageriapro.s2200.views import s2200_filiacaosindical_salvar as s2200_filiacaosindical_salvar_views
from emensageriapro.s2200.views import s2200_filiacaosindical_api as s2200_filiacaosindical_api_views
from emensageriapro.s2200.views import s2200_alvarajudicial_apagar as s2200_alvarajudicial_apagar_views
from emensageriapro.s2200.views import s2200_alvarajudicial_listar as s2200_alvarajudicial_listar_views
from emensageriapro.s2200.views import s2200_alvarajudicial_salvar as s2200_alvarajudicial_salvar_views
from emensageriapro.s2200.views import s2200_alvarajudicial_api as s2200_alvarajudicial_api_views
from emensageriapro.s2200.views import s2200_observacoes_apagar as s2200_observacoes_apagar_views
from emensageriapro.s2200.views import s2200_observacoes_listar as s2200_observacoes_listar_views
from emensageriapro.s2200.views import s2200_observacoes_salvar as s2200_observacoes_salvar_views
from emensageriapro.s2200.views import s2200_observacoes_api as s2200_observacoes_api_views
from emensageriapro.s2200.views import s2200_sucessaovinc_apagar as s2200_sucessaovinc_apagar_views
from emensageriapro.s2200.views import s2200_sucessaovinc_listar as s2200_sucessaovinc_listar_views
from emensageriapro.s2200.views import s2200_sucessaovinc_salvar as s2200_sucessaovinc_salvar_views
from emensageriapro.s2200.views import s2200_sucessaovinc_api as s2200_sucessaovinc_api_views
from emensageriapro.s2200.views import s2200_transfdom_apagar as s2200_transfdom_apagar_views
from emensageriapro.s2200.views import s2200_transfdom_listar as s2200_transfdom_listar_views
from emensageriapro.s2200.views import s2200_transfdom_salvar as s2200_transfdom_salvar_views
from emensageriapro.s2200.views import s2200_transfdom_api as s2200_transfdom_api_views
from emensageriapro.s2200.views import s2200_mudancacpf_apagar as s2200_mudancacpf_apagar_views
from emensageriapro.s2200.views import s2200_mudancacpf_listar as s2200_mudancacpf_listar_views
from emensageriapro.s2200.views import s2200_mudancacpf_salvar as s2200_mudancacpf_salvar_views
from emensageriapro.s2200.views import s2200_mudancacpf_api as s2200_mudancacpf_api_views
from emensageriapro.s2200.views import s2200_afastamento_apagar as s2200_afastamento_apagar_views
from emensageriapro.s2200.views import s2200_afastamento_listar as s2200_afastamento_listar_views
from emensageriapro.s2200.views import s2200_afastamento_salvar as s2200_afastamento_salvar_views
from emensageriapro.s2200.views import s2200_afastamento_api as s2200_afastamento_api_views
from emensageriapro.s2200.views import s2200_desligamento_apagar as s2200_desligamento_apagar_views
from emensageriapro.s2200.views import s2200_desligamento_listar as s2200_desligamento_listar_views
from emensageriapro.s2200.views import s2200_desligamento_salvar as s2200_desligamento_salvar_views
from emensageriapro.s2200.views import s2200_desligamento_api as s2200_desligamento_api_views
from emensageriapro.s2200.views import s2200_cessao_apagar as s2200_cessao_apagar_views
from emensageriapro.s2200.views import s2200_cessao_listar as s2200_cessao_listar_views
from emensageriapro.s2200.views import s2200_cessao_salvar as s2200_cessao_salvar_views
from emensageriapro.s2200.views import s2200_cessao_api as s2200_cessao_api_views


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


    url(r'^s2200-documentos/apagar/(?P<pk>[0-9]+)/$',
        s2200_documentos_apagar_views.apagar,
        name='s2200_documentos_apagar'),

    url(r'^s2200-documentos/api/$',
        s2200_documentos_api_views.s2200documentosList.as_view() ),

    url(r'^s2200-documentos/api/(?P<pk>[0-9]+)/$',
        s2200_documentos_api_views.s2200documentosDetail.as_view() ),

    url(r'^s2200-documentos/$',
        s2200_documentos_listar_views.listar,
        name='s2200_documentos'),

    url(r'^s2200-documentos/salvar/(?P<pk>[0-9]+)/$',
        s2200_documentos_salvar_views.salvar,
        name='s2200_documentos_salvar'),

    url(r'^s2200-documentos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_documentos_salvar_views.salvar,
        name='s2200_documentos_salvar_tab'),

    url(r'^s2200-documentos/cadastrar/$',
        s2200_documentos_salvar_views.salvar,
        name='s2200_documentos_cadastrar'),

    url(r'^s2200-documentos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_documentos_salvar_views.salvar,
        name='s2200_documentos_salvar_output'),

    url(r'^s2200-documentos/(?P<output>[\w-]+)/$',
        s2200_documentos_listar_views.listar,
        name='s2200_documentos_output'),

    url(r'^s2200-ctps/apagar/(?P<pk>[0-9]+)/$',
        s2200_ctps_apagar_views.apagar,
        name='s2200_ctps_apagar'),

    url(r'^s2200-ctps/api/$',
        s2200_ctps_api_views.s2200CTPSList.as_view() ),

    url(r'^s2200-ctps/api/(?P<pk>[0-9]+)/$',
        s2200_ctps_api_views.s2200CTPSDetail.as_view() ),

    url(r'^s2200-ctps/$',
        s2200_ctps_listar_views.listar,
        name='s2200_ctps'),

    url(r'^s2200-ctps/salvar/(?P<pk>[0-9]+)/$',
        s2200_ctps_salvar_views.salvar,
        name='s2200_ctps_salvar'),

    url(r'^s2200-ctps/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_ctps_salvar_views.salvar,
        name='s2200_ctps_salvar_tab'),

    url(r'^s2200-ctps/cadastrar/$',
        s2200_ctps_salvar_views.salvar,
        name='s2200_ctps_cadastrar'),

    url(r'^s2200-ctps/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_ctps_salvar_views.salvar,
        name='s2200_ctps_salvar_output'),

    url(r'^s2200-ctps/(?P<output>[\w-]+)/$',
        s2200_ctps_listar_views.listar,
        name='s2200_ctps_output'),

    url(r'^s2200-ric/apagar/(?P<pk>[0-9]+)/$',
        s2200_ric_apagar_views.apagar,
        name='s2200_ric_apagar'),

    url(r'^s2200-ric/api/$',
        s2200_ric_api_views.s2200RICList.as_view() ),

    url(r'^s2200-ric/api/(?P<pk>[0-9]+)/$',
        s2200_ric_api_views.s2200RICDetail.as_view() ),

    url(r'^s2200-ric/$',
        s2200_ric_listar_views.listar,
        name='s2200_ric'),

    url(r'^s2200-ric/salvar/(?P<pk>[0-9]+)/$',
        s2200_ric_salvar_views.salvar,
        name='s2200_ric_salvar'),

    url(r'^s2200-ric/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_ric_salvar_views.salvar,
        name='s2200_ric_salvar_tab'),

    url(r'^s2200-ric/cadastrar/$',
        s2200_ric_salvar_views.salvar,
        name='s2200_ric_cadastrar'),

    url(r'^s2200-ric/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_ric_salvar_views.salvar,
        name='s2200_ric_salvar_output'),

    url(r'^s2200-ric/(?P<output>[\w-]+)/$',
        s2200_ric_listar_views.listar,
        name='s2200_ric_output'),

    url(r'^s2200-rg/apagar/(?P<pk>[0-9]+)/$',
        s2200_rg_apagar_views.apagar,
        name='s2200_rg_apagar'),

    url(r'^s2200-rg/api/$',
        s2200_rg_api_views.s2200RGList.as_view() ),

    url(r'^s2200-rg/api/(?P<pk>[0-9]+)/$',
        s2200_rg_api_views.s2200RGDetail.as_view() ),

    url(r'^s2200-rg/$',
        s2200_rg_listar_views.listar,
        name='s2200_rg'),

    url(r'^s2200-rg/salvar/(?P<pk>[0-9]+)/$',
        s2200_rg_salvar_views.salvar,
        name='s2200_rg_salvar'),

    url(r'^s2200-rg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_rg_salvar_views.salvar,
        name='s2200_rg_salvar_tab'),

    url(r'^s2200-rg/cadastrar/$',
        s2200_rg_salvar_views.salvar,
        name='s2200_rg_cadastrar'),

    url(r'^s2200-rg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_rg_salvar_views.salvar,
        name='s2200_rg_salvar_output'),

    url(r'^s2200-rg/(?P<output>[\w-]+)/$',
        s2200_rg_listar_views.listar,
        name='s2200_rg_output'),

    url(r'^s2200-rne/apagar/(?P<pk>[0-9]+)/$',
        s2200_rne_apagar_views.apagar,
        name='s2200_rne_apagar'),

    url(r'^s2200-rne/api/$',
        s2200_rne_api_views.s2200RNEList.as_view() ),

    url(r'^s2200-rne/api/(?P<pk>[0-9]+)/$',
        s2200_rne_api_views.s2200RNEDetail.as_view() ),

    url(r'^s2200-rne/$',
        s2200_rne_listar_views.listar,
        name='s2200_rne'),

    url(r'^s2200-rne/salvar/(?P<pk>[0-9]+)/$',
        s2200_rne_salvar_views.salvar,
        name='s2200_rne_salvar'),

    url(r'^s2200-rne/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_rne_salvar_views.salvar,
        name='s2200_rne_salvar_tab'),

    url(r'^s2200-rne/cadastrar/$',
        s2200_rne_salvar_views.salvar,
        name='s2200_rne_cadastrar'),

    url(r'^s2200-rne/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_rne_salvar_views.salvar,
        name='s2200_rne_salvar_output'),

    url(r'^s2200-rne/(?P<output>[\w-]+)/$',
        s2200_rne_listar_views.listar,
        name='s2200_rne_output'),

    url(r'^s2200-oc/apagar/(?P<pk>[0-9]+)/$',
        s2200_oc_apagar_views.apagar,
        name='s2200_oc_apagar'),

    url(r'^s2200-oc/api/$',
        s2200_oc_api_views.s2200OCList.as_view() ),

    url(r'^s2200-oc/api/(?P<pk>[0-9]+)/$',
        s2200_oc_api_views.s2200OCDetail.as_view() ),

    url(r'^s2200-oc/$',
        s2200_oc_listar_views.listar,
        name='s2200_oc'),

    url(r'^s2200-oc/salvar/(?P<pk>[0-9]+)/$',
        s2200_oc_salvar_views.salvar,
        name='s2200_oc_salvar'),

    url(r'^s2200-oc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_oc_salvar_views.salvar,
        name='s2200_oc_salvar_tab'),

    url(r'^s2200-oc/cadastrar/$',
        s2200_oc_salvar_views.salvar,
        name='s2200_oc_cadastrar'),

    url(r'^s2200-oc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_oc_salvar_views.salvar,
        name='s2200_oc_salvar_output'),

    url(r'^s2200-oc/(?P<output>[\w-]+)/$',
        s2200_oc_listar_views.listar,
        name='s2200_oc_output'),

    url(r'^s2200-cnh/apagar/(?P<pk>[0-9]+)/$',
        s2200_cnh_apagar_views.apagar,
        name='s2200_cnh_apagar'),

    url(r'^s2200-cnh/api/$',
        s2200_cnh_api_views.s2200CNHList.as_view() ),

    url(r'^s2200-cnh/api/(?P<pk>[0-9]+)/$',
        s2200_cnh_api_views.s2200CNHDetail.as_view() ),

    url(r'^s2200-cnh/$',
        s2200_cnh_listar_views.listar,
        name='s2200_cnh'),

    url(r'^s2200-cnh/salvar/(?P<pk>[0-9]+)/$',
        s2200_cnh_salvar_views.salvar,
        name='s2200_cnh_salvar'),

    url(r'^s2200-cnh/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_cnh_salvar_views.salvar,
        name='s2200_cnh_salvar_tab'),

    url(r'^s2200-cnh/cadastrar/$',
        s2200_cnh_salvar_views.salvar,
        name='s2200_cnh_cadastrar'),

    url(r'^s2200-cnh/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_cnh_salvar_views.salvar,
        name='s2200_cnh_salvar_output'),

    url(r'^s2200-cnh/(?P<output>[\w-]+)/$',
        s2200_cnh_listar_views.listar,
        name='s2200_cnh_output'),

    url(r'^s2200-brasil/apagar/(?P<pk>[0-9]+)/$',
        s2200_brasil_apagar_views.apagar,
        name='s2200_brasil_apagar'),

    url(r'^s2200-brasil/api/$',
        s2200_brasil_api_views.s2200brasilList.as_view() ),

    url(r'^s2200-brasil/api/(?P<pk>[0-9]+)/$',
        s2200_brasil_api_views.s2200brasilDetail.as_view() ),

    url(r'^s2200-brasil/$',
        s2200_brasil_listar_views.listar,
        name='s2200_brasil'),

    url(r'^s2200-brasil/salvar/(?P<pk>[0-9]+)/$',
        s2200_brasil_salvar_views.salvar,
        name='s2200_brasil_salvar'),

    url(r'^s2200-brasil/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_brasil_salvar_views.salvar,
        name='s2200_brasil_salvar_tab'),

    url(r'^s2200-brasil/cadastrar/$',
        s2200_brasil_salvar_views.salvar,
        name='s2200_brasil_cadastrar'),

    url(r'^s2200-brasil/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_brasil_salvar_views.salvar,
        name='s2200_brasil_salvar_output'),

    url(r'^s2200-brasil/(?P<output>[\w-]+)/$',
        s2200_brasil_listar_views.listar,
        name='s2200_brasil_output'),

    url(r'^s2200-exterior/apagar/(?P<pk>[0-9]+)/$',
        s2200_exterior_apagar_views.apagar,
        name='s2200_exterior_apagar'),

    url(r'^s2200-exterior/api/$',
        s2200_exterior_api_views.s2200exteriorList.as_view() ),

    url(r'^s2200-exterior/api/(?P<pk>[0-9]+)/$',
        s2200_exterior_api_views.s2200exteriorDetail.as_view() ),

    url(r'^s2200-exterior/$',
        s2200_exterior_listar_views.listar,
        name='s2200_exterior'),

    url(r'^s2200-exterior/salvar/(?P<pk>[0-9]+)/$',
        s2200_exterior_salvar_views.salvar,
        name='s2200_exterior_salvar'),

    url(r'^s2200-exterior/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_exterior_salvar_views.salvar,
        name='s2200_exterior_salvar_tab'),

    url(r'^s2200-exterior/cadastrar/$',
        s2200_exterior_salvar_views.salvar,
        name='s2200_exterior_cadastrar'),

    url(r'^s2200-exterior/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_exterior_salvar_views.salvar,
        name='s2200_exterior_salvar_output'),

    url(r'^s2200-exterior/(?P<output>[\w-]+)/$',
        s2200_exterior_listar_views.listar,
        name='s2200_exterior_output'),

    url(r'^s2200-trabestrangeiro/apagar/(?P<pk>[0-9]+)/$',
        s2200_trabestrangeiro_apagar_views.apagar,
        name='s2200_trabestrangeiro_apagar'),

    url(r'^s2200-trabestrangeiro/api/$',
        s2200_trabestrangeiro_api_views.s2200trabEstrangeiroList.as_view() ),

    url(r'^s2200-trabestrangeiro/api/(?P<pk>[0-9]+)/$',
        s2200_trabestrangeiro_api_views.s2200trabEstrangeiroDetail.as_view() ),

    url(r'^s2200-trabestrangeiro/$',
        s2200_trabestrangeiro_listar_views.listar,
        name='s2200_trabestrangeiro'),

    url(r'^s2200-trabestrangeiro/salvar/(?P<pk>[0-9]+)/$',
        s2200_trabestrangeiro_salvar_views.salvar,
        name='s2200_trabestrangeiro_salvar'),

    url(r'^s2200-trabestrangeiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_trabestrangeiro_salvar_views.salvar,
        name='s2200_trabestrangeiro_salvar_tab'),

    url(r'^s2200-trabestrangeiro/cadastrar/$',
        s2200_trabestrangeiro_salvar_views.salvar,
        name='s2200_trabestrangeiro_cadastrar'),

    url(r'^s2200-trabestrangeiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_trabestrangeiro_salvar_views.salvar,
        name='s2200_trabestrangeiro_salvar_output'),

    url(r'^s2200-trabestrangeiro/(?P<output>[\w-]+)/$',
        s2200_trabestrangeiro_listar_views.listar,
        name='s2200_trabestrangeiro_output'),

    url(r'^s2200-infodeficiencia/apagar/(?P<pk>[0-9]+)/$',
        s2200_infodeficiencia_apagar_views.apagar,
        name='s2200_infodeficiencia_apagar'),

    url(r'^s2200-infodeficiencia/api/$',
        s2200_infodeficiencia_api_views.s2200infoDeficienciaList.as_view() ),

    url(r'^s2200-infodeficiencia/api/(?P<pk>[0-9]+)/$',
        s2200_infodeficiencia_api_views.s2200infoDeficienciaDetail.as_view() ),

    url(r'^s2200-infodeficiencia/$',
        s2200_infodeficiencia_listar_views.listar,
        name='s2200_infodeficiencia'),

    url(r'^s2200-infodeficiencia/salvar/(?P<pk>[0-9]+)/$',
        s2200_infodeficiencia_salvar_views.salvar,
        name='s2200_infodeficiencia_salvar'),

    url(r'^s2200-infodeficiencia/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_infodeficiencia_salvar_views.salvar,
        name='s2200_infodeficiencia_salvar_tab'),

    url(r'^s2200-infodeficiencia/cadastrar/$',
        s2200_infodeficiencia_salvar_views.salvar,
        name='s2200_infodeficiencia_cadastrar'),

    url(r'^s2200-infodeficiencia/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_infodeficiencia_salvar_views.salvar,
        name='s2200_infodeficiencia_salvar_output'),

    url(r'^s2200-infodeficiencia/(?P<output>[\w-]+)/$',
        s2200_infodeficiencia_listar_views.listar,
        name='s2200_infodeficiencia_output'),

    url(r'^s2200-dependente/apagar/(?P<pk>[0-9]+)/$',
        s2200_dependente_apagar_views.apagar,
        name='s2200_dependente_apagar'),

    url(r'^s2200-dependente/api/$',
        s2200_dependente_api_views.s2200dependenteList.as_view() ),

    url(r'^s2200-dependente/api/(?P<pk>[0-9]+)/$',
        s2200_dependente_api_views.s2200dependenteDetail.as_view() ),

    url(r'^s2200-dependente/$',
        s2200_dependente_listar_views.listar,
        name='s2200_dependente'),

    url(r'^s2200-dependente/salvar/(?P<pk>[0-9]+)/$',
        s2200_dependente_salvar_views.salvar,
        name='s2200_dependente_salvar'),

    url(r'^s2200-dependente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_dependente_salvar_views.salvar,
        name='s2200_dependente_salvar_tab'),

    url(r'^s2200-dependente/cadastrar/$',
        s2200_dependente_salvar_views.salvar,
        name='s2200_dependente_cadastrar'),

    url(r'^s2200-dependente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_dependente_salvar_views.salvar,
        name='s2200_dependente_salvar_output'),

    url(r'^s2200-dependente/(?P<output>[\w-]+)/$',
        s2200_dependente_listar_views.listar,
        name='s2200_dependente_output'),

    url(r'^s2200-aposentadoria/apagar/(?P<pk>[0-9]+)/$',
        s2200_aposentadoria_apagar_views.apagar,
        name='s2200_aposentadoria_apagar'),

    url(r'^s2200-aposentadoria/api/$',
        s2200_aposentadoria_api_views.s2200aposentadoriaList.as_view() ),

    url(r'^s2200-aposentadoria/api/(?P<pk>[0-9]+)/$',
        s2200_aposentadoria_api_views.s2200aposentadoriaDetail.as_view() ),

    url(r'^s2200-aposentadoria/$',
        s2200_aposentadoria_listar_views.listar,
        name='s2200_aposentadoria'),

    url(r'^s2200-aposentadoria/salvar/(?P<pk>[0-9]+)/$',
        s2200_aposentadoria_salvar_views.salvar,
        name='s2200_aposentadoria_salvar'),

    url(r'^s2200-aposentadoria/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_aposentadoria_salvar_views.salvar,
        name='s2200_aposentadoria_salvar_tab'),

    url(r'^s2200-aposentadoria/cadastrar/$',
        s2200_aposentadoria_salvar_views.salvar,
        name='s2200_aposentadoria_cadastrar'),

    url(r'^s2200-aposentadoria/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_aposentadoria_salvar_views.salvar,
        name='s2200_aposentadoria_salvar_output'),

    url(r'^s2200-aposentadoria/(?P<output>[\w-]+)/$',
        s2200_aposentadoria_listar_views.listar,
        name='s2200_aposentadoria_output'),

    url(r'^s2200-contato/apagar/(?P<pk>[0-9]+)/$',
        s2200_contato_apagar_views.apagar,
        name='s2200_contato_apagar'),

    url(r'^s2200-contato/api/$',
        s2200_contato_api_views.s2200contatoList.as_view() ),

    url(r'^s2200-contato/api/(?P<pk>[0-9]+)/$',
        s2200_contato_api_views.s2200contatoDetail.as_view() ),

    url(r'^s2200-contato/$',
        s2200_contato_listar_views.listar,
        name='s2200_contato'),

    url(r'^s2200-contato/salvar/(?P<pk>[0-9]+)/$',
        s2200_contato_salvar_views.salvar,
        name='s2200_contato_salvar'),

    url(r'^s2200-contato/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_contato_salvar_views.salvar,
        name='s2200_contato_salvar_tab'),

    url(r'^s2200-contato/cadastrar/$',
        s2200_contato_salvar_views.salvar,
        name='s2200_contato_cadastrar'),

    url(r'^s2200-contato/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_contato_salvar_views.salvar,
        name='s2200_contato_salvar_output'),

    url(r'^s2200-contato/(?P<output>[\w-]+)/$',
        s2200_contato_listar_views.listar,
        name='s2200_contato_output'),

    url(r'^s2200-infoceletista/apagar/(?P<pk>[0-9]+)/$',
        s2200_infoceletista_apagar_views.apagar,
        name='s2200_infoceletista_apagar'),

    url(r'^s2200-infoceletista/api/$',
        s2200_infoceletista_api_views.s2200infoCeletistaList.as_view() ),

    url(r'^s2200-infoceletista/api/(?P<pk>[0-9]+)/$',
        s2200_infoceletista_api_views.s2200infoCeletistaDetail.as_view() ),

    url(r'^s2200-infoceletista/$',
        s2200_infoceletista_listar_views.listar,
        name='s2200_infoceletista'),

    url(r'^s2200-infoceletista/salvar/(?P<pk>[0-9]+)/$',
        s2200_infoceletista_salvar_views.salvar,
        name='s2200_infoceletista_salvar'),

    url(r'^s2200-infoceletista/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_infoceletista_salvar_views.salvar,
        name='s2200_infoceletista_salvar_tab'),

    url(r'^s2200-infoceletista/cadastrar/$',
        s2200_infoceletista_salvar_views.salvar,
        name='s2200_infoceletista_cadastrar'),

    url(r'^s2200-infoceletista/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_infoceletista_salvar_views.salvar,
        name='s2200_infoceletista_salvar_output'),

    url(r'^s2200-infoceletista/(?P<output>[\w-]+)/$',
        s2200_infoceletista_listar_views.listar,
        name='s2200_infoceletista_output'),

    url(r'^s2200-trabtemporario/apagar/(?P<pk>[0-9]+)/$',
        s2200_trabtemporario_apagar_views.apagar,
        name='s2200_trabtemporario_apagar'),

    url(r'^s2200-trabtemporario/api/$',
        s2200_trabtemporario_api_views.s2200trabTemporarioList.as_view() ),

    url(r'^s2200-trabtemporario/api/(?P<pk>[0-9]+)/$',
        s2200_trabtemporario_api_views.s2200trabTemporarioDetail.as_view() ),

    url(r'^s2200-trabtemporario/$',
        s2200_trabtemporario_listar_views.listar,
        name='s2200_trabtemporario'),

    url(r'^s2200-trabtemporario/salvar/(?P<pk>[0-9]+)/$',
        s2200_trabtemporario_salvar_views.salvar,
        name='s2200_trabtemporario_salvar'),

    url(r'^s2200-trabtemporario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_trabtemporario_salvar_views.salvar,
        name='s2200_trabtemporario_salvar_tab'),

    url(r'^s2200-trabtemporario/cadastrar/$',
        s2200_trabtemporario_salvar_views.salvar,
        name='s2200_trabtemporario_cadastrar'),

    url(r'^s2200-trabtemporario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_trabtemporario_salvar_views.salvar,
        name='s2200_trabtemporario_salvar_output'),

    url(r'^s2200-trabtemporario/(?P<output>[\w-]+)/$',
        s2200_trabtemporario_listar_views.listar,
        name='s2200_trabtemporario_output'),

    url(r'^s2200-ideestabvinc/apagar/(?P<pk>[0-9]+)/$',
        s2200_ideestabvinc_apagar_views.apagar,
        name='s2200_ideestabvinc_apagar'),

    url(r'^s2200-ideestabvinc/api/$',
        s2200_ideestabvinc_api_views.s2200ideEstabVincList.as_view() ),

    url(r'^s2200-ideestabvinc/api/(?P<pk>[0-9]+)/$',
        s2200_ideestabvinc_api_views.s2200ideEstabVincDetail.as_view() ),

    url(r'^s2200-ideestabvinc/$',
        s2200_ideestabvinc_listar_views.listar,
        name='s2200_ideestabvinc'),

    url(r'^s2200-ideestabvinc/salvar/(?P<pk>[0-9]+)/$',
        s2200_ideestabvinc_salvar_views.salvar,
        name='s2200_ideestabvinc_salvar'),

    url(r'^s2200-ideestabvinc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_ideestabvinc_salvar_views.salvar,
        name='s2200_ideestabvinc_salvar_tab'),

    url(r'^s2200-ideestabvinc/cadastrar/$',
        s2200_ideestabvinc_salvar_views.salvar,
        name='s2200_ideestabvinc_cadastrar'),

    url(r'^s2200-ideestabvinc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_ideestabvinc_salvar_views.salvar,
        name='s2200_ideestabvinc_salvar_output'),

    url(r'^s2200-ideestabvinc/(?P<output>[\w-]+)/$',
        s2200_ideestabvinc_listar_views.listar,
        name='s2200_ideestabvinc_output'),

    url(r'^s2200-idetrabsubstituido/apagar/(?P<pk>[0-9]+)/$',
        s2200_idetrabsubstituido_apagar_views.apagar,
        name='s2200_idetrabsubstituido_apagar'),

    url(r'^s2200-idetrabsubstituido/api/$',
        s2200_idetrabsubstituido_api_views.s2200ideTrabSubstituidoList.as_view() ),

    url(r'^s2200-idetrabsubstituido/api/(?P<pk>[0-9]+)/$',
        s2200_idetrabsubstituido_api_views.s2200ideTrabSubstituidoDetail.as_view() ),

    url(r'^s2200-idetrabsubstituido/$',
        s2200_idetrabsubstituido_listar_views.listar,
        name='s2200_idetrabsubstituido'),

    url(r'^s2200-idetrabsubstituido/salvar/(?P<pk>[0-9]+)/$',
        s2200_idetrabsubstituido_salvar_views.salvar,
        name='s2200_idetrabsubstituido_salvar'),

    url(r'^s2200-idetrabsubstituido/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_idetrabsubstituido_salvar_views.salvar,
        name='s2200_idetrabsubstituido_salvar_tab'),

    url(r'^s2200-idetrabsubstituido/cadastrar/$',
        s2200_idetrabsubstituido_salvar_views.salvar,
        name='s2200_idetrabsubstituido_cadastrar'),

    url(r'^s2200-idetrabsubstituido/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_idetrabsubstituido_salvar_views.salvar,
        name='s2200_idetrabsubstituido_salvar_output'),

    url(r'^s2200-idetrabsubstituido/(?P<output>[\w-]+)/$',
        s2200_idetrabsubstituido_listar_views.listar,
        name='s2200_idetrabsubstituido_output'),

    url(r'^s2200-aprend/apagar/(?P<pk>[0-9]+)/$',
        s2200_aprend_apagar_views.apagar,
        name='s2200_aprend_apagar'),

    url(r'^s2200-aprend/api/$',
        s2200_aprend_api_views.s2200aprendList.as_view() ),

    url(r'^s2200-aprend/api/(?P<pk>[0-9]+)/$',
        s2200_aprend_api_views.s2200aprendDetail.as_view() ),

    url(r'^s2200-aprend/$',
        s2200_aprend_listar_views.listar,
        name='s2200_aprend'),

    url(r'^s2200-aprend/salvar/(?P<pk>[0-9]+)/$',
        s2200_aprend_salvar_views.salvar,
        name='s2200_aprend_salvar'),

    url(r'^s2200-aprend/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_aprend_salvar_views.salvar,
        name='s2200_aprend_salvar_tab'),

    url(r'^s2200-aprend/cadastrar/$',
        s2200_aprend_salvar_views.salvar,
        name='s2200_aprend_cadastrar'),

    url(r'^s2200-aprend/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_aprend_salvar_views.salvar,
        name='s2200_aprend_salvar_output'),

    url(r'^s2200-aprend/(?P<output>[\w-]+)/$',
        s2200_aprend_listar_views.listar,
        name='s2200_aprend_output'),

    url(r'^s2200-infoestatutario/apagar/(?P<pk>[0-9]+)/$',
        s2200_infoestatutario_apagar_views.apagar,
        name='s2200_infoestatutario_apagar'),

    url(r'^s2200-infoestatutario/api/$',
        s2200_infoestatutario_api_views.s2200infoEstatutarioList.as_view() ),

    url(r'^s2200-infoestatutario/api/(?P<pk>[0-9]+)/$',
        s2200_infoestatutario_api_views.s2200infoEstatutarioDetail.as_view() ),

    url(r'^s2200-infoestatutario/$',
        s2200_infoestatutario_listar_views.listar,
        name='s2200_infoestatutario'),

    url(r'^s2200-infoestatutario/salvar/(?P<pk>[0-9]+)/$',
        s2200_infoestatutario_salvar_views.salvar,
        name='s2200_infoestatutario_salvar'),

    url(r'^s2200-infoestatutario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_infoestatutario_salvar_views.salvar,
        name='s2200_infoestatutario_salvar_tab'),

    url(r'^s2200-infoestatutario/cadastrar/$',
        s2200_infoestatutario_salvar_views.salvar,
        name='s2200_infoestatutario_cadastrar'),

    url(r'^s2200-infoestatutario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_infoestatutario_salvar_views.salvar,
        name='s2200_infoestatutario_salvar_output'),

    url(r'^s2200-infoestatutario/(?P<output>[\w-]+)/$',
        s2200_infoestatutario_listar_views.listar,
        name='s2200_infoestatutario_output'),

    url(r'^s2200-infodecjud/apagar/(?P<pk>[0-9]+)/$',
        s2200_infodecjud_apagar_views.apagar,
        name='s2200_infodecjud_apagar'),

    url(r'^s2200-infodecjud/api/$',
        s2200_infodecjud_api_views.s2200infoDecJudList.as_view() ),

    url(r'^s2200-infodecjud/api/(?P<pk>[0-9]+)/$',
        s2200_infodecjud_api_views.s2200infoDecJudDetail.as_view() ),

    url(r'^s2200-infodecjud/$',
        s2200_infodecjud_listar_views.listar,
        name='s2200_infodecjud'),

    url(r'^s2200-infodecjud/salvar/(?P<pk>[0-9]+)/$',
        s2200_infodecjud_salvar_views.salvar,
        name='s2200_infodecjud_salvar'),

    url(r'^s2200-infodecjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_infodecjud_salvar_views.salvar,
        name='s2200_infodecjud_salvar_tab'),

    url(r'^s2200-infodecjud/cadastrar/$',
        s2200_infodecjud_salvar_views.salvar,
        name='s2200_infodecjud_cadastrar'),

    url(r'^s2200-infodecjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_infodecjud_salvar_views.salvar,
        name='s2200_infodecjud_salvar_output'),

    url(r'^s2200-infodecjud/(?P<output>[\w-]+)/$',
        s2200_infodecjud_listar_views.listar,
        name='s2200_infodecjud_output'),

    url(r'^s2200-localtrabgeral/apagar/(?P<pk>[0-9]+)/$',
        s2200_localtrabgeral_apagar_views.apagar,
        name='s2200_localtrabgeral_apagar'),

    url(r'^s2200-localtrabgeral/api/$',
        s2200_localtrabgeral_api_views.s2200localTrabGeralList.as_view() ),

    url(r'^s2200-localtrabgeral/api/(?P<pk>[0-9]+)/$',
        s2200_localtrabgeral_api_views.s2200localTrabGeralDetail.as_view() ),

    url(r'^s2200-localtrabgeral/$',
        s2200_localtrabgeral_listar_views.listar,
        name='s2200_localtrabgeral'),

    url(r'^s2200-localtrabgeral/salvar/(?P<pk>[0-9]+)/$',
        s2200_localtrabgeral_salvar_views.salvar,
        name='s2200_localtrabgeral_salvar'),

    url(r'^s2200-localtrabgeral/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_localtrabgeral_salvar_views.salvar,
        name='s2200_localtrabgeral_salvar_tab'),

    url(r'^s2200-localtrabgeral/cadastrar/$',
        s2200_localtrabgeral_salvar_views.salvar,
        name='s2200_localtrabgeral_cadastrar'),

    url(r'^s2200-localtrabgeral/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_localtrabgeral_salvar_views.salvar,
        name='s2200_localtrabgeral_salvar_output'),

    url(r'^s2200-localtrabgeral/(?P<output>[\w-]+)/$',
        s2200_localtrabgeral_listar_views.listar,
        name='s2200_localtrabgeral_output'),

    url(r'^s2200-localtrabdom/apagar/(?P<pk>[0-9]+)/$',
        s2200_localtrabdom_apagar_views.apagar,
        name='s2200_localtrabdom_apagar'),

    url(r'^s2200-localtrabdom/api/$',
        s2200_localtrabdom_api_views.s2200localTrabDomList.as_view() ),

    url(r'^s2200-localtrabdom/api/(?P<pk>[0-9]+)/$',
        s2200_localtrabdom_api_views.s2200localTrabDomDetail.as_view() ),

    url(r'^s2200-localtrabdom/$',
        s2200_localtrabdom_listar_views.listar,
        name='s2200_localtrabdom'),

    url(r'^s2200-localtrabdom/salvar/(?P<pk>[0-9]+)/$',
        s2200_localtrabdom_salvar_views.salvar,
        name='s2200_localtrabdom_salvar'),

    url(r'^s2200-localtrabdom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_localtrabdom_salvar_views.salvar,
        name='s2200_localtrabdom_salvar_tab'),

    url(r'^s2200-localtrabdom/cadastrar/$',
        s2200_localtrabdom_salvar_views.salvar,
        name='s2200_localtrabdom_cadastrar'),

    url(r'^s2200-localtrabdom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_localtrabdom_salvar_views.salvar,
        name='s2200_localtrabdom_salvar_output'),

    url(r'^s2200-localtrabdom/(?P<output>[\w-]+)/$',
        s2200_localtrabdom_listar_views.listar,
        name='s2200_localtrabdom_output'),

    url(r'^s2200-horcontratual/apagar/(?P<pk>[0-9]+)/$',
        s2200_horcontratual_apagar_views.apagar,
        name='s2200_horcontratual_apagar'),

    url(r'^s2200-horcontratual/api/$',
        s2200_horcontratual_api_views.s2200horContratualList.as_view() ),

    url(r'^s2200-horcontratual/api/(?P<pk>[0-9]+)/$',
        s2200_horcontratual_api_views.s2200horContratualDetail.as_view() ),

    url(r'^s2200-horcontratual/$',
        s2200_horcontratual_listar_views.listar,
        name='s2200_horcontratual'),

    url(r'^s2200-horcontratual/salvar/(?P<pk>[0-9]+)/$',
        s2200_horcontratual_salvar_views.salvar,
        name='s2200_horcontratual_salvar'),

    url(r'^s2200-horcontratual/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_horcontratual_salvar_views.salvar,
        name='s2200_horcontratual_salvar_tab'),

    url(r'^s2200-horcontratual/cadastrar/$',
        s2200_horcontratual_salvar_views.salvar,
        name='s2200_horcontratual_cadastrar'),

    url(r'^s2200-horcontratual/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_horcontratual_salvar_views.salvar,
        name='s2200_horcontratual_salvar_output'),

    url(r'^s2200-horcontratual/(?P<output>[\w-]+)/$',
        s2200_horcontratual_listar_views.listar,
        name='s2200_horcontratual_output'),

    url(r'^s2200-horario/apagar/(?P<pk>[0-9]+)/$',
        s2200_horario_apagar_views.apagar,
        name='s2200_horario_apagar'),

    url(r'^s2200-horario/api/$',
        s2200_horario_api_views.s2200horarioList.as_view() ),

    url(r'^s2200-horario/api/(?P<pk>[0-9]+)/$',
        s2200_horario_api_views.s2200horarioDetail.as_view() ),

    url(r'^s2200-horario/$',
        s2200_horario_listar_views.listar,
        name='s2200_horario'),

    url(r'^s2200-horario/salvar/(?P<pk>[0-9]+)/$',
        s2200_horario_salvar_views.salvar,
        name='s2200_horario_salvar'),

    url(r'^s2200-horario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_horario_salvar_views.salvar,
        name='s2200_horario_salvar_tab'),

    url(r'^s2200-horario/cadastrar/$',
        s2200_horario_salvar_views.salvar,
        name='s2200_horario_cadastrar'),

    url(r'^s2200-horario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_horario_salvar_views.salvar,
        name='s2200_horario_salvar_output'),

    url(r'^s2200-horario/(?P<output>[\w-]+)/$',
        s2200_horario_listar_views.listar,
        name='s2200_horario_output'),

    url(r'^s2200-filiacaosindical/apagar/(?P<pk>[0-9]+)/$',
        s2200_filiacaosindical_apagar_views.apagar,
        name='s2200_filiacaosindical_apagar'),

    url(r'^s2200-filiacaosindical/api/$',
        s2200_filiacaosindical_api_views.s2200filiacaoSindicalList.as_view() ),

    url(r'^s2200-filiacaosindical/api/(?P<pk>[0-9]+)/$',
        s2200_filiacaosindical_api_views.s2200filiacaoSindicalDetail.as_view() ),

    url(r'^s2200-filiacaosindical/$',
        s2200_filiacaosindical_listar_views.listar,
        name='s2200_filiacaosindical'),

    url(r'^s2200-filiacaosindical/salvar/(?P<pk>[0-9]+)/$',
        s2200_filiacaosindical_salvar_views.salvar,
        name='s2200_filiacaosindical_salvar'),

    url(r'^s2200-filiacaosindical/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_filiacaosindical_salvar_views.salvar,
        name='s2200_filiacaosindical_salvar_tab'),

    url(r'^s2200-filiacaosindical/cadastrar/$',
        s2200_filiacaosindical_salvar_views.salvar,
        name='s2200_filiacaosindical_cadastrar'),

    url(r'^s2200-filiacaosindical/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_filiacaosindical_salvar_views.salvar,
        name='s2200_filiacaosindical_salvar_output'),

    url(r'^s2200-filiacaosindical/(?P<output>[\w-]+)/$',
        s2200_filiacaosindical_listar_views.listar,
        name='s2200_filiacaosindical_output'),

    url(r'^s2200-alvarajudicial/apagar/(?P<pk>[0-9]+)/$',
        s2200_alvarajudicial_apagar_views.apagar,
        name='s2200_alvarajudicial_apagar'),

    url(r'^s2200-alvarajudicial/api/$',
        s2200_alvarajudicial_api_views.s2200alvaraJudicialList.as_view() ),

    url(r'^s2200-alvarajudicial/api/(?P<pk>[0-9]+)/$',
        s2200_alvarajudicial_api_views.s2200alvaraJudicialDetail.as_view() ),

    url(r'^s2200-alvarajudicial/$',
        s2200_alvarajudicial_listar_views.listar,
        name='s2200_alvarajudicial'),

    url(r'^s2200-alvarajudicial/salvar/(?P<pk>[0-9]+)/$',
        s2200_alvarajudicial_salvar_views.salvar,
        name='s2200_alvarajudicial_salvar'),

    url(r'^s2200-alvarajudicial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_alvarajudicial_salvar_views.salvar,
        name='s2200_alvarajudicial_salvar_tab'),

    url(r'^s2200-alvarajudicial/cadastrar/$',
        s2200_alvarajudicial_salvar_views.salvar,
        name='s2200_alvarajudicial_cadastrar'),

    url(r'^s2200-alvarajudicial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_alvarajudicial_salvar_views.salvar,
        name='s2200_alvarajudicial_salvar_output'),

    url(r'^s2200-alvarajudicial/(?P<output>[\w-]+)/$',
        s2200_alvarajudicial_listar_views.listar,
        name='s2200_alvarajudicial_output'),

    url(r'^s2200-observacoes/apagar/(?P<pk>[0-9]+)/$',
        s2200_observacoes_apagar_views.apagar,
        name='s2200_observacoes_apagar'),

    url(r'^s2200-observacoes/api/$',
        s2200_observacoes_api_views.s2200observacoesList.as_view() ),

    url(r'^s2200-observacoes/api/(?P<pk>[0-9]+)/$',
        s2200_observacoes_api_views.s2200observacoesDetail.as_view() ),

    url(r'^s2200-observacoes/$',
        s2200_observacoes_listar_views.listar,
        name='s2200_observacoes'),

    url(r'^s2200-observacoes/salvar/(?P<pk>[0-9]+)/$',
        s2200_observacoes_salvar_views.salvar,
        name='s2200_observacoes_salvar'),

    url(r'^s2200-observacoes/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_observacoes_salvar_views.salvar,
        name='s2200_observacoes_salvar_tab'),

    url(r'^s2200-observacoes/cadastrar/$',
        s2200_observacoes_salvar_views.salvar,
        name='s2200_observacoes_cadastrar'),

    url(r'^s2200-observacoes/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_observacoes_salvar_views.salvar,
        name='s2200_observacoes_salvar_output'),

    url(r'^s2200-observacoes/(?P<output>[\w-]+)/$',
        s2200_observacoes_listar_views.listar,
        name='s2200_observacoes_output'),

    url(r'^s2200-sucessaovinc/apagar/(?P<pk>[0-9]+)/$',
        s2200_sucessaovinc_apagar_views.apagar,
        name='s2200_sucessaovinc_apagar'),

    url(r'^s2200-sucessaovinc/api/$',
        s2200_sucessaovinc_api_views.s2200sucessaoVincList.as_view() ),

    url(r'^s2200-sucessaovinc/api/(?P<pk>[0-9]+)/$',
        s2200_sucessaovinc_api_views.s2200sucessaoVincDetail.as_view() ),

    url(r'^s2200-sucessaovinc/$',
        s2200_sucessaovinc_listar_views.listar,
        name='s2200_sucessaovinc'),

    url(r'^s2200-sucessaovinc/salvar/(?P<pk>[0-9]+)/$',
        s2200_sucessaovinc_salvar_views.salvar,
        name='s2200_sucessaovinc_salvar'),

    url(r'^s2200-sucessaovinc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_sucessaovinc_salvar_views.salvar,
        name='s2200_sucessaovinc_salvar_tab'),

    url(r'^s2200-sucessaovinc/cadastrar/$',
        s2200_sucessaovinc_salvar_views.salvar,
        name='s2200_sucessaovinc_cadastrar'),

    url(r'^s2200-sucessaovinc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_sucessaovinc_salvar_views.salvar,
        name='s2200_sucessaovinc_salvar_output'),

    url(r'^s2200-sucessaovinc/(?P<output>[\w-]+)/$',
        s2200_sucessaovinc_listar_views.listar,
        name='s2200_sucessaovinc_output'),

    url(r'^s2200-transfdom/apagar/(?P<pk>[0-9]+)/$',
        s2200_transfdom_apagar_views.apagar,
        name='s2200_transfdom_apagar'),

    url(r'^s2200-transfdom/api/$',
        s2200_transfdom_api_views.s2200transfDomList.as_view() ),

    url(r'^s2200-transfdom/api/(?P<pk>[0-9]+)/$',
        s2200_transfdom_api_views.s2200transfDomDetail.as_view() ),

    url(r'^s2200-transfdom/$',
        s2200_transfdom_listar_views.listar,
        name='s2200_transfdom'),

    url(r'^s2200-transfdom/salvar/(?P<pk>[0-9]+)/$',
        s2200_transfdom_salvar_views.salvar,
        name='s2200_transfdom_salvar'),

    url(r'^s2200-transfdom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_transfdom_salvar_views.salvar,
        name='s2200_transfdom_salvar_tab'),

    url(r'^s2200-transfdom/cadastrar/$',
        s2200_transfdom_salvar_views.salvar,
        name='s2200_transfdom_cadastrar'),

    url(r'^s2200-transfdom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_transfdom_salvar_views.salvar,
        name='s2200_transfdom_salvar_output'),

    url(r'^s2200-transfdom/(?P<output>[\w-]+)/$',
        s2200_transfdom_listar_views.listar,
        name='s2200_transfdom_output'),

    url(r'^s2200-mudancacpf/apagar/(?P<pk>[0-9]+)/$',
        s2200_mudancacpf_apagar_views.apagar,
        name='s2200_mudancacpf_apagar'),

    url(r'^s2200-mudancacpf/api/$',
        s2200_mudancacpf_api_views.s2200mudancaCPFList.as_view() ),

    url(r'^s2200-mudancacpf/api/(?P<pk>[0-9]+)/$',
        s2200_mudancacpf_api_views.s2200mudancaCPFDetail.as_view() ),

    url(r'^s2200-mudancacpf/$',
        s2200_mudancacpf_listar_views.listar,
        name='s2200_mudancacpf'),

    url(r'^s2200-mudancacpf/salvar/(?P<pk>[0-9]+)/$',
        s2200_mudancacpf_salvar_views.salvar,
        name='s2200_mudancacpf_salvar'),

    url(r'^s2200-mudancacpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_mudancacpf_salvar_views.salvar,
        name='s2200_mudancacpf_salvar_tab'),

    url(r'^s2200-mudancacpf/cadastrar/$',
        s2200_mudancacpf_salvar_views.salvar,
        name='s2200_mudancacpf_cadastrar'),

    url(r'^s2200-mudancacpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_mudancacpf_salvar_views.salvar,
        name='s2200_mudancacpf_salvar_output'),

    url(r'^s2200-mudancacpf/(?P<output>[\w-]+)/$',
        s2200_mudancacpf_listar_views.listar,
        name='s2200_mudancacpf_output'),

    url(r'^s2200-afastamento/apagar/(?P<pk>[0-9]+)/$',
        s2200_afastamento_apagar_views.apagar,
        name='s2200_afastamento_apagar'),

    url(r'^s2200-afastamento/api/$',
        s2200_afastamento_api_views.s2200afastamentoList.as_view() ),

    url(r'^s2200-afastamento/api/(?P<pk>[0-9]+)/$',
        s2200_afastamento_api_views.s2200afastamentoDetail.as_view() ),

    url(r'^s2200-afastamento/$',
        s2200_afastamento_listar_views.listar,
        name='s2200_afastamento'),

    url(r'^s2200-afastamento/salvar/(?P<pk>[0-9]+)/$',
        s2200_afastamento_salvar_views.salvar,
        name='s2200_afastamento_salvar'),

    url(r'^s2200-afastamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_afastamento_salvar_views.salvar,
        name='s2200_afastamento_salvar_tab'),

    url(r'^s2200-afastamento/cadastrar/$',
        s2200_afastamento_salvar_views.salvar,
        name='s2200_afastamento_cadastrar'),

    url(r'^s2200-afastamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_afastamento_salvar_views.salvar,
        name='s2200_afastamento_salvar_output'),

    url(r'^s2200-afastamento/(?P<output>[\w-]+)/$',
        s2200_afastamento_listar_views.listar,
        name='s2200_afastamento_output'),

    url(r'^s2200-desligamento/apagar/(?P<pk>[0-9]+)/$',
        s2200_desligamento_apagar_views.apagar,
        name='s2200_desligamento_apagar'),

    url(r'^s2200-desligamento/api/$',
        s2200_desligamento_api_views.s2200desligamentoList.as_view() ),

    url(r'^s2200-desligamento/api/(?P<pk>[0-9]+)/$',
        s2200_desligamento_api_views.s2200desligamentoDetail.as_view() ),

    url(r'^s2200-desligamento/$',
        s2200_desligamento_listar_views.listar,
        name='s2200_desligamento'),

    url(r'^s2200-desligamento/salvar/(?P<pk>[0-9]+)/$',
        s2200_desligamento_salvar_views.salvar,
        name='s2200_desligamento_salvar'),

    url(r'^s2200-desligamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_desligamento_salvar_views.salvar,
        name='s2200_desligamento_salvar_tab'),

    url(r'^s2200-desligamento/cadastrar/$',
        s2200_desligamento_salvar_views.salvar,
        name='s2200_desligamento_cadastrar'),

    url(r'^s2200-desligamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_desligamento_salvar_views.salvar,
        name='s2200_desligamento_salvar_output'),

    url(r'^s2200-desligamento/(?P<output>[\w-]+)/$',
        s2200_desligamento_listar_views.listar,
        name='s2200_desligamento_output'),

    url(r'^s2200-cessao/apagar/(?P<pk>[0-9]+)/$',
        s2200_cessao_apagar_views.apagar,
        name='s2200_cessao_apagar'),

    url(r'^s2200-cessao/api/$',
        s2200_cessao_api_views.s2200cessaoList.as_view() ),

    url(r'^s2200-cessao/api/(?P<pk>[0-9]+)/$',
        s2200_cessao_api_views.s2200cessaoDetail.as_view() ),

    url(r'^s2200-cessao/$',
        s2200_cessao_listar_views.listar,
        name='s2200_cessao'),

    url(r'^s2200-cessao/salvar/(?P<pk>[0-9]+)/$',
        s2200_cessao_salvar_views.salvar,
        name='s2200_cessao_salvar'),

    url(r'^s2200-cessao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        s2200_cessao_salvar_views.salvar,
        name='s2200_cessao_salvar_tab'),

    url(r'^s2200-cessao/cadastrar/$',
        s2200_cessao_salvar_views.salvar,
        name='s2200_cessao_cadastrar'),

    url(r'^s2200-cessao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        s2200_cessao_salvar_views.salvar,
        name='s2200_cessao_salvar_output'),

    url(r'^s2200-cessao/(?P<output>[\w-]+)/$',
        s2200_cessao_listar_views.listar,
        name='s2200_cessao_output'),


]