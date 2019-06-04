#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2300.views import s2300_documentos_apagar as s2300_documentos_apagar_views
from emensageriapro.s2300.views import s2300_documentos_listar as s2300_documentos_listar_views
from emensageriapro.s2300.views import s2300_documentos_salvar as s2300_documentos_salvar_views
from emensageriapro.s2300.views import s2300_documentos_api as s2300_documentos_api_views
from emensageriapro.s2300.views import s2300_ctps_apagar as s2300_ctps_apagar_views
from emensageriapro.s2300.views import s2300_ctps_listar as s2300_ctps_listar_views
from emensageriapro.s2300.views import s2300_ctps_salvar as s2300_ctps_salvar_views
from emensageriapro.s2300.views import s2300_ctps_api as s2300_ctps_api_views
from emensageriapro.s2300.views import s2300_ric_apagar as s2300_ric_apagar_views
from emensageriapro.s2300.views import s2300_ric_listar as s2300_ric_listar_views
from emensageriapro.s2300.views import s2300_ric_salvar as s2300_ric_salvar_views
from emensageriapro.s2300.views import s2300_ric_api as s2300_ric_api_views
from emensageriapro.s2300.views import s2300_rg_apagar as s2300_rg_apagar_views
from emensageriapro.s2300.views import s2300_rg_listar as s2300_rg_listar_views
from emensageriapro.s2300.views import s2300_rg_salvar as s2300_rg_salvar_views
from emensageriapro.s2300.views import s2300_rg_api as s2300_rg_api_views
from emensageriapro.s2300.views import s2300_rne_apagar as s2300_rne_apagar_views
from emensageriapro.s2300.views import s2300_rne_listar as s2300_rne_listar_views
from emensageriapro.s2300.views import s2300_rne_salvar as s2300_rne_salvar_views
from emensageriapro.s2300.views import s2300_rne_api as s2300_rne_api_views
from emensageriapro.s2300.views import s2300_oc_apagar as s2300_oc_apagar_views
from emensageriapro.s2300.views import s2300_oc_listar as s2300_oc_listar_views
from emensageriapro.s2300.views import s2300_oc_salvar as s2300_oc_salvar_views
from emensageriapro.s2300.views import s2300_oc_api as s2300_oc_api_views
from emensageriapro.s2300.views import s2300_cnh_apagar as s2300_cnh_apagar_views
from emensageriapro.s2300.views import s2300_cnh_listar as s2300_cnh_listar_views
from emensageriapro.s2300.views import s2300_cnh_salvar as s2300_cnh_salvar_views
from emensageriapro.s2300.views import s2300_cnh_api as s2300_cnh_api_views
from emensageriapro.s2300.views import s2300_brasil_apagar as s2300_brasil_apagar_views
from emensageriapro.s2300.views import s2300_brasil_listar as s2300_brasil_listar_views
from emensageriapro.s2300.views import s2300_brasil_salvar as s2300_brasil_salvar_views
from emensageriapro.s2300.views import s2300_brasil_api as s2300_brasil_api_views
from emensageriapro.s2300.views import s2300_exterior_apagar as s2300_exterior_apagar_views
from emensageriapro.s2300.views import s2300_exterior_listar as s2300_exterior_listar_views
from emensageriapro.s2300.views import s2300_exterior_salvar as s2300_exterior_salvar_views
from emensageriapro.s2300.views import s2300_exterior_api as s2300_exterior_api_views
from emensageriapro.s2300.views import s2300_trabestrangeiro_apagar as s2300_trabestrangeiro_apagar_views
from emensageriapro.s2300.views import s2300_trabestrangeiro_listar as s2300_trabestrangeiro_listar_views
from emensageriapro.s2300.views import s2300_trabestrangeiro_salvar as s2300_trabestrangeiro_salvar_views
from emensageriapro.s2300.views import s2300_trabestrangeiro_api as s2300_trabestrangeiro_api_views
from emensageriapro.s2300.views import s2300_infodeficiencia_apagar as s2300_infodeficiencia_apagar_views
from emensageriapro.s2300.views import s2300_infodeficiencia_listar as s2300_infodeficiencia_listar_views
from emensageriapro.s2300.views import s2300_infodeficiencia_salvar as s2300_infodeficiencia_salvar_views
from emensageriapro.s2300.views import s2300_infodeficiencia_api as s2300_infodeficiencia_api_views
from emensageriapro.s2300.views import s2300_dependente_apagar as s2300_dependente_apagar_views
from emensageriapro.s2300.views import s2300_dependente_listar as s2300_dependente_listar_views
from emensageriapro.s2300.views import s2300_dependente_salvar as s2300_dependente_salvar_views
from emensageriapro.s2300.views import s2300_dependente_api as s2300_dependente_api_views
from emensageriapro.s2300.views import s2300_contato_apagar as s2300_contato_apagar_views
from emensageriapro.s2300.views import s2300_contato_listar as s2300_contato_listar_views
from emensageriapro.s2300.views import s2300_contato_salvar as s2300_contato_salvar_views
from emensageriapro.s2300.views import s2300_contato_api as s2300_contato_api_views
from emensageriapro.s2300.views import s2300_infocomplementares_apagar as s2300_infocomplementares_apagar_views
from emensageriapro.s2300.views import s2300_infocomplementares_listar as s2300_infocomplementares_listar_views
from emensageriapro.s2300.views import s2300_infocomplementares_salvar as s2300_infocomplementares_salvar_views
from emensageriapro.s2300.views import s2300_infocomplementares_api as s2300_infocomplementares_api_views
from emensageriapro.s2300.views import s2300_cargofuncao_apagar as s2300_cargofuncao_apagar_views
from emensageriapro.s2300.views import s2300_cargofuncao_listar as s2300_cargofuncao_listar_views
from emensageriapro.s2300.views import s2300_cargofuncao_salvar as s2300_cargofuncao_salvar_views
from emensageriapro.s2300.views import s2300_cargofuncao_api as s2300_cargofuncao_api_views
from emensageriapro.s2300.views import s2300_remuneracao_apagar as s2300_remuneracao_apagar_views
from emensageriapro.s2300.views import s2300_remuneracao_listar as s2300_remuneracao_listar_views
from emensageriapro.s2300.views import s2300_remuneracao_salvar as s2300_remuneracao_salvar_views
from emensageriapro.s2300.views import s2300_remuneracao_api as s2300_remuneracao_api_views
from emensageriapro.s2300.views import s2300_fgts_apagar as s2300_fgts_apagar_views
from emensageriapro.s2300.views import s2300_fgts_listar as s2300_fgts_listar_views
from emensageriapro.s2300.views import s2300_fgts_salvar as s2300_fgts_salvar_views
from emensageriapro.s2300.views import s2300_fgts_api as s2300_fgts_api_views
from emensageriapro.s2300.views import s2300_infodirigentesindical_apagar as s2300_infodirigentesindical_apagar_views
from emensageriapro.s2300.views import s2300_infodirigentesindical_listar as s2300_infodirigentesindical_listar_views
from emensageriapro.s2300.views import s2300_infodirigentesindical_salvar as s2300_infodirigentesindical_salvar_views
from emensageriapro.s2300.views import s2300_infodirigentesindical_api as s2300_infodirigentesindical_api_views
from emensageriapro.s2300.views import s2300_infotrabcedido_apagar as s2300_infotrabcedido_apagar_views
from emensageriapro.s2300.views import s2300_infotrabcedido_listar as s2300_infotrabcedido_listar_views
from emensageriapro.s2300.views import s2300_infotrabcedido_salvar as s2300_infotrabcedido_salvar_views
from emensageriapro.s2300.views import s2300_infotrabcedido_api as s2300_infotrabcedido_api_views
from emensageriapro.s2300.views import s2300_infoestagiario_apagar as s2300_infoestagiario_apagar_views
from emensageriapro.s2300.views import s2300_infoestagiario_listar as s2300_infoestagiario_listar_views
from emensageriapro.s2300.views import s2300_infoestagiario_salvar as s2300_infoestagiario_salvar_views
from emensageriapro.s2300.views import s2300_infoestagiario_api as s2300_infoestagiario_api_views
from emensageriapro.s2300.views import s2300_ageintegracao_apagar as s2300_ageintegracao_apagar_views
from emensageriapro.s2300.views import s2300_ageintegracao_listar as s2300_ageintegracao_listar_views
from emensageriapro.s2300.views import s2300_ageintegracao_salvar as s2300_ageintegracao_salvar_views
from emensageriapro.s2300.views import s2300_ageintegracao_api as s2300_ageintegracao_api_views
from emensageriapro.s2300.views import s2300_supervisorestagio_apagar as s2300_supervisorestagio_apagar_views
from emensageriapro.s2300.views import s2300_supervisorestagio_listar as s2300_supervisorestagio_listar_views
from emensageriapro.s2300.views import s2300_supervisorestagio_salvar as s2300_supervisorestagio_salvar_views
from emensageriapro.s2300.views import s2300_supervisorestagio_api as s2300_supervisorestagio_api_views
from emensageriapro.s2300.views import s2300_mudancacpf_apagar as s2300_mudancacpf_apagar_views
from emensageriapro.s2300.views import s2300_mudancacpf_listar as s2300_mudancacpf_listar_views
from emensageriapro.s2300.views import s2300_mudancacpf_salvar as s2300_mudancacpf_salvar_views
from emensageriapro.s2300.views import s2300_mudancacpf_api as s2300_mudancacpf_api_views
from emensageriapro.s2300.views import s2300_afastamento_apagar as s2300_afastamento_apagar_views
from emensageriapro.s2300.views import s2300_afastamento_listar as s2300_afastamento_listar_views
from emensageriapro.s2300.views import s2300_afastamento_salvar as s2300_afastamento_salvar_views
from emensageriapro.s2300.views import s2300_afastamento_api as s2300_afastamento_api_views
from emensageriapro.s2300.views import s2300_termino_apagar as s2300_termino_apagar_views
from emensageriapro.s2300.views import s2300_termino_listar as s2300_termino_listar_views
from emensageriapro.s2300.views import s2300_termino_salvar as s2300_termino_salvar_views
from emensageriapro.s2300.views import s2300_termino_api as s2300_termino_api_views



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


    url(r'^s2300-documentos/apagar/(?P<pk>[0-9]+)/$', 
        s2300_documentos_apagar_views.apagar, 
        name='s2300_documentos_apagar'),

    url(r'^s2300-documentos/api/$',
        s2300_documentos_api_views.s2300documentosList.as_view() ),

    url(r'^s2300-documentos/api/(?P<pk>[0-9]+)/$',
        s2300_documentos_api_views.s2300documentosDetail.as_view() ),

    url(r'^s2300-documentos/$', 
        s2300_documentos_listar_views.listar, 
        name='s2300_documentos'),

    url(r'^s2300-documentos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_documentos_salvar_views.salvar, 
        name='s2300_documentos_salvar'),
        
    url(r'^s2300-documentos/cadastrar/$', 
        s2300_documentos_salvar_views.salvar, 
        name='s2300_documentos_cadastrar'),

    url(r'^s2300-documentos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_documentos_salvar_views.salvar, 
        name='s2300_documentos_salvar_output'),
        
    url(r'^s2300-documentos/(?P<output>[\w-]+)/$', 
        s2300_documentos_listar_views.listar, 
        name='s2300_documentos_output'),

    url(r'^s2300-ctps/apagar/(?P<pk>[0-9]+)/$', 
        s2300_ctps_apagar_views.apagar, 
        name='s2300_ctps_apagar'),

    url(r'^s2300-ctps/api/$',
        s2300_ctps_api_views.s2300CTPSList.as_view() ),

    url(r'^s2300-ctps/api/(?P<pk>[0-9]+)/$',
        s2300_ctps_api_views.s2300CTPSDetail.as_view() ),

    url(r'^s2300-ctps/$', 
        s2300_ctps_listar_views.listar, 
        name='s2300_ctps'),

    url(r'^s2300-ctps/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_ctps_salvar_views.salvar, 
        name='s2300_ctps_salvar'),
        
    url(r'^s2300-ctps/cadastrar/$', 
        s2300_ctps_salvar_views.salvar, 
        name='s2300_ctps_cadastrar'),

    url(r'^s2300-ctps/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_ctps_salvar_views.salvar, 
        name='s2300_ctps_salvar_output'),
        
    url(r'^s2300-ctps/(?P<output>[\w-]+)/$', 
        s2300_ctps_listar_views.listar, 
        name='s2300_ctps_output'),

    url(r'^s2300-ric/apagar/(?P<pk>[0-9]+)/$', 
        s2300_ric_apagar_views.apagar, 
        name='s2300_ric_apagar'),

    url(r'^s2300-ric/api/$',
        s2300_ric_api_views.s2300RICList.as_view() ),

    url(r'^s2300-ric/api/(?P<pk>[0-9]+)/$',
        s2300_ric_api_views.s2300RICDetail.as_view() ),

    url(r'^s2300-ric/$', 
        s2300_ric_listar_views.listar, 
        name='s2300_ric'),

    url(r'^s2300-ric/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_ric_salvar_views.salvar, 
        name='s2300_ric_salvar'),
        
    url(r'^s2300-ric/cadastrar/$', 
        s2300_ric_salvar_views.salvar, 
        name='s2300_ric_cadastrar'),

    url(r'^s2300-ric/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_ric_salvar_views.salvar, 
        name='s2300_ric_salvar_output'),
        
    url(r'^s2300-ric/(?P<output>[\w-]+)/$', 
        s2300_ric_listar_views.listar, 
        name='s2300_ric_output'),

    url(r'^s2300-rg/apagar/(?P<pk>[0-9]+)/$', 
        s2300_rg_apagar_views.apagar, 
        name='s2300_rg_apagar'),

    url(r'^s2300-rg/api/$',
        s2300_rg_api_views.s2300RGList.as_view() ),

    url(r'^s2300-rg/api/(?P<pk>[0-9]+)/$',
        s2300_rg_api_views.s2300RGDetail.as_view() ),

    url(r'^s2300-rg/$', 
        s2300_rg_listar_views.listar, 
        name='s2300_rg'),

    url(r'^s2300-rg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_rg_salvar_views.salvar, 
        name='s2300_rg_salvar'),
        
    url(r'^s2300-rg/cadastrar/$', 
        s2300_rg_salvar_views.salvar, 
        name='s2300_rg_cadastrar'),

    url(r'^s2300-rg/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_rg_salvar_views.salvar, 
        name='s2300_rg_salvar_output'),
        
    url(r'^s2300-rg/(?P<output>[\w-]+)/$', 
        s2300_rg_listar_views.listar, 
        name='s2300_rg_output'),

    url(r'^s2300-rne/apagar/(?P<pk>[0-9]+)/$', 
        s2300_rne_apagar_views.apagar, 
        name='s2300_rne_apagar'),

    url(r'^s2300-rne/api/$',
        s2300_rne_api_views.s2300RNEList.as_view() ),

    url(r'^s2300-rne/api/(?P<pk>[0-9]+)/$',
        s2300_rne_api_views.s2300RNEDetail.as_view() ),

    url(r'^s2300-rne/$', 
        s2300_rne_listar_views.listar, 
        name='s2300_rne'),

    url(r'^s2300-rne/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_rne_salvar_views.salvar, 
        name='s2300_rne_salvar'),
        
    url(r'^s2300-rne/cadastrar/$', 
        s2300_rne_salvar_views.salvar, 
        name='s2300_rne_cadastrar'),

    url(r'^s2300-rne/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_rne_salvar_views.salvar, 
        name='s2300_rne_salvar_output'),
        
    url(r'^s2300-rne/(?P<output>[\w-]+)/$', 
        s2300_rne_listar_views.listar, 
        name='s2300_rne_output'),

    url(r'^s2300-oc/apagar/(?P<pk>[0-9]+)/$', 
        s2300_oc_apagar_views.apagar, 
        name='s2300_oc_apagar'),

    url(r'^s2300-oc/api/$',
        s2300_oc_api_views.s2300OCList.as_view() ),

    url(r'^s2300-oc/api/(?P<pk>[0-9]+)/$',
        s2300_oc_api_views.s2300OCDetail.as_view() ),

    url(r'^s2300-oc/$', 
        s2300_oc_listar_views.listar, 
        name='s2300_oc'),

    url(r'^s2300-oc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_oc_salvar_views.salvar, 
        name='s2300_oc_salvar'),
        
    url(r'^s2300-oc/cadastrar/$', 
        s2300_oc_salvar_views.salvar, 
        name='s2300_oc_cadastrar'),

    url(r'^s2300-oc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_oc_salvar_views.salvar, 
        name='s2300_oc_salvar_output'),
        
    url(r'^s2300-oc/(?P<output>[\w-]+)/$', 
        s2300_oc_listar_views.listar, 
        name='s2300_oc_output'),

    url(r'^s2300-cnh/apagar/(?P<pk>[0-9]+)/$', 
        s2300_cnh_apagar_views.apagar, 
        name='s2300_cnh_apagar'),

    url(r'^s2300-cnh/api/$',
        s2300_cnh_api_views.s2300CNHList.as_view() ),

    url(r'^s2300-cnh/api/(?P<pk>[0-9]+)/$',
        s2300_cnh_api_views.s2300CNHDetail.as_view() ),

    url(r'^s2300-cnh/$', 
        s2300_cnh_listar_views.listar, 
        name='s2300_cnh'),

    url(r'^s2300-cnh/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_cnh_salvar_views.salvar, 
        name='s2300_cnh_salvar'),
        
    url(r'^s2300-cnh/cadastrar/$', 
        s2300_cnh_salvar_views.salvar, 
        name='s2300_cnh_cadastrar'),

    url(r'^s2300-cnh/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_cnh_salvar_views.salvar, 
        name='s2300_cnh_salvar_output'),
        
    url(r'^s2300-cnh/(?P<output>[\w-]+)/$', 
        s2300_cnh_listar_views.listar, 
        name='s2300_cnh_output'),

    url(r'^s2300-brasil/apagar/(?P<pk>[0-9]+)/$', 
        s2300_brasil_apagar_views.apagar, 
        name='s2300_brasil_apagar'),

    url(r'^s2300-brasil/api/$',
        s2300_brasil_api_views.s2300brasilList.as_view() ),

    url(r'^s2300-brasil/api/(?P<pk>[0-9]+)/$',
        s2300_brasil_api_views.s2300brasilDetail.as_view() ),

    url(r'^s2300-brasil/$', 
        s2300_brasil_listar_views.listar, 
        name='s2300_brasil'),

    url(r'^s2300-brasil/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_brasil_salvar_views.salvar, 
        name='s2300_brasil_salvar'),
        
    url(r'^s2300-brasil/cadastrar/$', 
        s2300_brasil_salvar_views.salvar, 
        name='s2300_brasil_cadastrar'),

    url(r'^s2300-brasil/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_brasil_salvar_views.salvar, 
        name='s2300_brasil_salvar_output'),
        
    url(r'^s2300-brasil/(?P<output>[\w-]+)/$', 
        s2300_brasil_listar_views.listar, 
        name='s2300_brasil_output'),

    url(r'^s2300-exterior/apagar/(?P<pk>[0-9]+)/$', 
        s2300_exterior_apagar_views.apagar, 
        name='s2300_exterior_apagar'),

    url(r'^s2300-exterior/api/$',
        s2300_exterior_api_views.s2300exteriorList.as_view() ),

    url(r'^s2300-exterior/api/(?P<pk>[0-9]+)/$',
        s2300_exterior_api_views.s2300exteriorDetail.as_view() ),

    url(r'^s2300-exterior/$', 
        s2300_exterior_listar_views.listar, 
        name='s2300_exterior'),

    url(r'^s2300-exterior/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_exterior_salvar_views.salvar, 
        name='s2300_exterior_salvar'),
        
    url(r'^s2300-exterior/cadastrar/$', 
        s2300_exterior_salvar_views.salvar, 
        name='s2300_exterior_cadastrar'),

    url(r'^s2300-exterior/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_exterior_salvar_views.salvar, 
        name='s2300_exterior_salvar_output'),
        
    url(r'^s2300-exterior/(?P<output>[\w-]+)/$', 
        s2300_exterior_listar_views.listar, 
        name='s2300_exterior_output'),

    url(r'^s2300-trabestrangeiro/apagar/(?P<pk>[0-9]+)/$', 
        s2300_trabestrangeiro_apagar_views.apagar, 
        name='s2300_trabestrangeiro_apagar'),

    url(r'^s2300-trabestrangeiro/api/$',
        s2300_trabestrangeiro_api_views.s2300trabEstrangeiroList.as_view() ),

    url(r'^s2300-trabestrangeiro/api/(?P<pk>[0-9]+)/$',
        s2300_trabestrangeiro_api_views.s2300trabEstrangeiroDetail.as_view() ),

    url(r'^s2300-trabestrangeiro/$', 
        s2300_trabestrangeiro_listar_views.listar, 
        name='s2300_trabestrangeiro'),

    url(r'^s2300-trabestrangeiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_trabestrangeiro_salvar_views.salvar, 
        name='s2300_trabestrangeiro_salvar'),
        
    url(r'^s2300-trabestrangeiro/cadastrar/$', 
        s2300_trabestrangeiro_salvar_views.salvar, 
        name='s2300_trabestrangeiro_cadastrar'),

    url(r'^s2300-trabestrangeiro/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_trabestrangeiro_salvar_views.salvar, 
        name='s2300_trabestrangeiro_salvar_output'),
        
    url(r'^s2300-trabestrangeiro/(?P<output>[\w-]+)/$', 
        s2300_trabestrangeiro_listar_views.listar, 
        name='s2300_trabestrangeiro_output'),

    url(r'^s2300-infodeficiencia/apagar/(?P<pk>[0-9]+)/$', 
        s2300_infodeficiencia_apagar_views.apagar, 
        name='s2300_infodeficiencia_apagar'),

    url(r'^s2300-infodeficiencia/api/$',
        s2300_infodeficiencia_api_views.s2300infoDeficienciaList.as_view() ),

    url(r'^s2300-infodeficiencia/api/(?P<pk>[0-9]+)/$',
        s2300_infodeficiencia_api_views.s2300infoDeficienciaDetail.as_view() ),

    url(r'^s2300-infodeficiencia/$', 
        s2300_infodeficiencia_listar_views.listar, 
        name='s2300_infodeficiencia'),

    url(r'^s2300-infodeficiencia/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_infodeficiencia_salvar_views.salvar, 
        name='s2300_infodeficiencia_salvar'),
        
    url(r'^s2300-infodeficiencia/cadastrar/$', 
        s2300_infodeficiencia_salvar_views.salvar, 
        name='s2300_infodeficiencia_cadastrar'),

    url(r'^s2300-infodeficiencia/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_infodeficiencia_salvar_views.salvar, 
        name='s2300_infodeficiencia_salvar_output'),
        
    url(r'^s2300-infodeficiencia/(?P<output>[\w-]+)/$', 
        s2300_infodeficiencia_listar_views.listar, 
        name='s2300_infodeficiencia_output'),

    url(r'^s2300-dependente/apagar/(?P<pk>[0-9]+)/$', 
        s2300_dependente_apagar_views.apagar, 
        name='s2300_dependente_apagar'),

    url(r'^s2300-dependente/api/$',
        s2300_dependente_api_views.s2300dependenteList.as_view() ),

    url(r'^s2300-dependente/api/(?P<pk>[0-9]+)/$',
        s2300_dependente_api_views.s2300dependenteDetail.as_view() ),

    url(r'^s2300-dependente/$', 
        s2300_dependente_listar_views.listar, 
        name='s2300_dependente'),

    url(r'^s2300-dependente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_dependente_salvar_views.salvar, 
        name='s2300_dependente_salvar'),
        
    url(r'^s2300-dependente/cadastrar/$', 
        s2300_dependente_salvar_views.salvar, 
        name='s2300_dependente_cadastrar'),

    url(r'^s2300-dependente/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_dependente_salvar_views.salvar, 
        name='s2300_dependente_salvar_output'),
        
    url(r'^s2300-dependente/(?P<output>[\w-]+)/$', 
        s2300_dependente_listar_views.listar, 
        name='s2300_dependente_output'),

    url(r'^s2300-contato/apagar/(?P<pk>[0-9]+)/$', 
        s2300_contato_apagar_views.apagar, 
        name='s2300_contato_apagar'),

    url(r'^s2300-contato/api/$',
        s2300_contato_api_views.s2300contatoList.as_view() ),

    url(r'^s2300-contato/api/(?P<pk>[0-9]+)/$',
        s2300_contato_api_views.s2300contatoDetail.as_view() ),

    url(r'^s2300-contato/$', 
        s2300_contato_listar_views.listar, 
        name='s2300_contato'),

    url(r'^s2300-contato/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_contato_salvar_views.salvar, 
        name='s2300_contato_salvar'),
        
    url(r'^s2300-contato/cadastrar/$', 
        s2300_contato_salvar_views.salvar, 
        name='s2300_contato_cadastrar'),

    url(r'^s2300-contato/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_contato_salvar_views.salvar, 
        name='s2300_contato_salvar_output'),
        
    url(r'^s2300-contato/(?P<output>[\w-]+)/$', 
        s2300_contato_listar_views.listar, 
        name='s2300_contato_output'),

    url(r'^s2300-infocomplementares/apagar/(?P<pk>[0-9]+)/$', 
        s2300_infocomplementares_apagar_views.apagar, 
        name='s2300_infocomplementares_apagar'),

    url(r'^s2300-infocomplementares/api/$',
        s2300_infocomplementares_api_views.s2300infoComplementaresList.as_view() ),

    url(r'^s2300-infocomplementares/api/(?P<pk>[0-9]+)/$',
        s2300_infocomplementares_api_views.s2300infoComplementaresDetail.as_view() ),

    url(r'^s2300-infocomplementares/$', 
        s2300_infocomplementares_listar_views.listar, 
        name='s2300_infocomplementares'),

    url(r'^s2300-infocomplementares/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_infocomplementares_salvar_views.salvar, 
        name='s2300_infocomplementares_salvar'),
        
    url(r'^s2300-infocomplementares/cadastrar/$', 
        s2300_infocomplementares_salvar_views.salvar, 
        name='s2300_infocomplementares_cadastrar'),

    url(r'^s2300-infocomplementares/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_infocomplementares_salvar_views.salvar, 
        name='s2300_infocomplementares_salvar_output'),
        
    url(r'^s2300-infocomplementares/(?P<output>[\w-]+)/$', 
        s2300_infocomplementares_listar_views.listar, 
        name='s2300_infocomplementares_output'),

    url(r'^s2300-cargofuncao/apagar/(?P<pk>[0-9]+)/$', 
        s2300_cargofuncao_apagar_views.apagar, 
        name='s2300_cargofuncao_apagar'),

    url(r'^s2300-cargofuncao/api/$',
        s2300_cargofuncao_api_views.s2300cargoFuncaoList.as_view() ),

    url(r'^s2300-cargofuncao/api/(?P<pk>[0-9]+)/$',
        s2300_cargofuncao_api_views.s2300cargoFuncaoDetail.as_view() ),

    url(r'^s2300-cargofuncao/$', 
        s2300_cargofuncao_listar_views.listar, 
        name='s2300_cargofuncao'),

    url(r'^s2300-cargofuncao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_cargofuncao_salvar_views.salvar, 
        name='s2300_cargofuncao_salvar'),
        
    url(r'^s2300-cargofuncao/cadastrar/$', 
        s2300_cargofuncao_salvar_views.salvar, 
        name='s2300_cargofuncao_cadastrar'),

    url(r'^s2300-cargofuncao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_cargofuncao_salvar_views.salvar, 
        name='s2300_cargofuncao_salvar_output'),
        
    url(r'^s2300-cargofuncao/(?P<output>[\w-]+)/$', 
        s2300_cargofuncao_listar_views.listar, 
        name='s2300_cargofuncao_output'),

    url(r'^s2300-remuneracao/apagar/(?P<pk>[0-9]+)/$', 
        s2300_remuneracao_apagar_views.apagar, 
        name='s2300_remuneracao_apagar'),

    url(r'^s2300-remuneracao/api/$',
        s2300_remuneracao_api_views.s2300remuneracaoList.as_view() ),

    url(r'^s2300-remuneracao/api/(?P<pk>[0-9]+)/$',
        s2300_remuneracao_api_views.s2300remuneracaoDetail.as_view() ),

    url(r'^s2300-remuneracao/$', 
        s2300_remuneracao_listar_views.listar, 
        name='s2300_remuneracao'),

    url(r'^s2300-remuneracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_remuneracao_salvar_views.salvar, 
        name='s2300_remuneracao_salvar'),
        
    url(r'^s2300-remuneracao/cadastrar/$', 
        s2300_remuneracao_salvar_views.salvar, 
        name='s2300_remuneracao_cadastrar'),

    url(r'^s2300-remuneracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_remuneracao_salvar_views.salvar, 
        name='s2300_remuneracao_salvar_output'),
        
    url(r'^s2300-remuneracao/(?P<output>[\w-]+)/$', 
        s2300_remuneracao_listar_views.listar, 
        name='s2300_remuneracao_output'),

    url(r'^s2300-fgts/apagar/(?P<pk>[0-9]+)/$', 
        s2300_fgts_apagar_views.apagar, 
        name='s2300_fgts_apagar'),

    url(r'^s2300-fgts/api/$',
        s2300_fgts_api_views.s2300fgtsList.as_view() ),

    url(r'^s2300-fgts/api/(?P<pk>[0-9]+)/$',
        s2300_fgts_api_views.s2300fgtsDetail.as_view() ),

    url(r'^s2300-fgts/$', 
        s2300_fgts_listar_views.listar, 
        name='s2300_fgts'),

    url(r'^s2300-fgts/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_fgts_salvar_views.salvar, 
        name='s2300_fgts_salvar'),
        
    url(r'^s2300-fgts/cadastrar/$', 
        s2300_fgts_salvar_views.salvar, 
        name='s2300_fgts_cadastrar'),

    url(r'^s2300-fgts/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_fgts_salvar_views.salvar, 
        name='s2300_fgts_salvar_output'),
        
    url(r'^s2300-fgts/(?P<output>[\w-]+)/$', 
        s2300_fgts_listar_views.listar, 
        name='s2300_fgts_output'),

    url(r'^s2300-infodirigentesindical/apagar/(?P<pk>[0-9]+)/$', 
        s2300_infodirigentesindical_apagar_views.apagar, 
        name='s2300_infodirigentesindical_apagar'),

    url(r'^s2300-infodirigentesindical/api/$',
        s2300_infodirigentesindical_api_views.s2300infoDirigenteSindicalList.as_view() ),

    url(r'^s2300-infodirigentesindical/api/(?P<pk>[0-9]+)/$',
        s2300_infodirigentesindical_api_views.s2300infoDirigenteSindicalDetail.as_view() ),

    url(r'^s2300-infodirigentesindical/$', 
        s2300_infodirigentesindical_listar_views.listar, 
        name='s2300_infodirigentesindical'),

    url(r'^s2300-infodirigentesindical/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_infodirigentesindical_salvar_views.salvar, 
        name='s2300_infodirigentesindical_salvar'),
        
    url(r'^s2300-infodirigentesindical/cadastrar/$', 
        s2300_infodirigentesindical_salvar_views.salvar, 
        name='s2300_infodirigentesindical_cadastrar'),

    url(r'^s2300-infodirigentesindical/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_infodirigentesindical_salvar_views.salvar, 
        name='s2300_infodirigentesindical_salvar_output'),
        
    url(r'^s2300-infodirigentesindical/(?P<output>[\w-]+)/$', 
        s2300_infodirigentesindical_listar_views.listar, 
        name='s2300_infodirigentesindical_output'),

    url(r'^s2300-infotrabcedido/apagar/(?P<pk>[0-9]+)/$', 
        s2300_infotrabcedido_apagar_views.apagar, 
        name='s2300_infotrabcedido_apagar'),

    url(r'^s2300-infotrabcedido/api/$',
        s2300_infotrabcedido_api_views.s2300infoTrabCedidoList.as_view() ),

    url(r'^s2300-infotrabcedido/api/(?P<pk>[0-9]+)/$',
        s2300_infotrabcedido_api_views.s2300infoTrabCedidoDetail.as_view() ),

    url(r'^s2300-infotrabcedido/$', 
        s2300_infotrabcedido_listar_views.listar, 
        name='s2300_infotrabcedido'),

    url(r'^s2300-infotrabcedido/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_infotrabcedido_salvar_views.salvar, 
        name='s2300_infotrabcedido_salvar'),
        
    url(r'^s2300-infotrabcedido/cadastrar/$', 
        s2300_infotrabcedido_salvar_views.salvar, 
        name='s2300_infotrabcedido_cadastrar'),

    url(r'^s2300-infotrabcedido/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_infotrabcedido_salvar_views.salvar, 
        name='s2300_infotrabcedido_salvar_output'),
        
    url(r'^s2300-infotrabcedido/(?P<output>[\w-]+)/$', 
        s2300_infotrabcedido_listar_views.listar, 
        name='s2300_infotrabcedido_output'),

    url(r'^s2300-infoestagiario/apagar/(?P<pk>[0-9]+)/$', 
        s2300_infoestagiario_apagar_views.apagar, 
        name='s2300_infoestagiario_apagar'),

    url(r'^s2300-infoestagiario/api/$',
        s2300_infoestagiario_api_views.s2300infoEstagiarioList.as_view() ),

    url(r'^s2300-infoestagiario/api/(?P<pk>[0-9]+)/$',
        s2300_infoestagiario_api_views.s2300infoEstagiarioDetail.as_view() ),

    url(r'^s2300-infoestagiario/$', 
        s2300_infoestagiario_listar_views.listar, 
        name='s2300_infoestagiario'),

    url(r'^s2300-infoestagiario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_infoestagiario_salvar_views.salvar, 
        name='s2300_infoestagiario_salvar'),
        
    url(r'^s2300-infoestagiario/cadastrar/$', 
        s2300_infoestagiario_salvar_views.salvar, 
        name='s2300_infoestagiario_cadastrar'),

    url(r'^s2300-infoestagiario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_infoestagiario_salvar_views.salvar, 
        name='s2300_infoestagiario_salvar_output'),
        
    url(r'^s2300-infoestagiario/(?P<output>[\w-]+)/$', 
        s2300_infoestagiario_listar_views.listar, 
        name='s2300_infoestagiario_output'),

    url(r'^s2300-ageintegracao/apagar/(?P<pk>[0-9]+)/$', 
        s2300_ageintegracao_apagar_views.apagar, 
        name='s2300_ageintegracao_apagar'),

    url(r'^s2300-ageintegracao/api/$',
        s2300_ageintegracao_api_views.s2300ageIntegracaoList.as_view() ),

    url(r'^s2300-ageintegracao/api/(?P<pk>[0-9]+)/$',
        s2300_ageintegracao_api_views.s2300ageIntegracaoDetail.as_view() ),

    url(r'^s2300-ageintegracao/$', 
        s2300_ageintegracao_listar_views.listar, 
        name='s2300_ageintegracao'),

    url(r'^s2300-ageintegracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_ageintegracao_salvar_views.salvar, 
        name='s2300_ageintegracao_salvar'),
        
    url(r'^s2300-ageintegracao/cadastrar/$', 
        s2300_ageintegracao_salvar_views.salvar, 
        name='s2300_ageintegracao_cadastrar'),

    url(r'^s2300-ageintegracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_ageintegracao_salvar_views.salvar, 
        name='s2300_ageintegracao_salvar_output'),
        
    url(r'^s2300-ageintegracao/(?P<output>[\w-]+)/$', 
        s2300_ageintegracao_listar_views.listar, 
        name='s2300_ageintegracao_output'),

    url(r'^s2300-supervisorestagio/apagar/(?P<pk>[0-9]+)/$', 
        s2300_supervisorestagio_apagar_views.apagar, 
        name='s2300_supervisorestagio_apagar'),

    url(r'^s2300-supervisorestagio/api/$',
        s2300_supervisorestagio_api_views.s2300supervisorEstagioList.as_view() ),

    url(r'^s2300-supervisorestagio/api/(?P<pk>[0-9]+)/$',
        s2300_supervisorestagio_api_views.s2300supervisorEstagioDetail.as_view() ),

    url(r'^s2300-supervisorestagio/$', 
        s2300_supervisorestagio_listar_views.listar, 
        name='s2300_supervisorestagio'),

    url(r'^s2300-supervisorestagio/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_supervisorestagio_salvar_views.salvar, 
        name='s2300_supervisorestagio_salvar'),
        
    url(r'^s2300-supervisorestagio/cadastrar/$', 
        s2300_supervisorestagio_salvar_views.salvar, 
        name='s2300_supervisorestagio_cadastrar'),

    url(r'^s2300-supervisorestagio/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_supervisorestagio_salvar_views.salvar, 
        name='s2300_supervisorestagio_salvar_output'),
        
    url(r'^s2300-supervisorestagio/(?P<output>[\w-]+)/$', 
        s2300_supervisorestagio_listar_views.listar, 
        name='s2300_supervisorestagio_output'),

    url(r'^s2300-mudancacpf/apagar/(?P<pk>[0-9]+)/$', 
        s2300_mudancacpf_apagar_views.apagar, 
        name='s2300_mudancacpf_apagar'),

    url(r'^s2300-mudancacpf/api/$',
        s2300_mudancacpf_api_views.s2300mudancaCPFList.as_view() ),

    url(r'^s2300-mudancacpf/api/(?P<pk>[0-9]+)/$',
        s2300_mudancacpf_api_views.s2300mudancaCPFDetail.as_view() ),

    url(r'^s2300-mudancacpf/$', 
        s2300_mudancacpf_listar_views.listar, 
        name='s2300_mudancacpf'),

    url(r'^s2300-mudancacpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_mudancacpf_salvar_views.salvar, 
        name='s2300_mudancacpf_salvar'),
        
    url(r'^s2300-mudancacpf/cadastrar/$', 
        s2300_mudancacpf_salvar_views.salvar, 
        name='s2300_mudancacpf_cadastrar'),

    url(r'^s2300-mudancacpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_mudancacpf_salvar_views.salvar, 
        name='s2300_mudancacpf_salvar_output'),
        
    url(r'^s2300-mudancacpf/(?P<output>[\w-]+)/$', 
        s2300_mudancacpf_listar_views.listar, 
        name='s2300_mudancacpf_output'),

    url(r'^s2300-afastamento/apagar/(?P<pk>[0-9]+)/$', 
        s2300_afastamento_apagar_views.apagar, 
        name='s2300_afastamento_apagar'),

    url(r'^s2300-afastamento/api/$',
        s2300_afastamento_api_views.s2300afastamentoList.as_view() ),

    url(r'^s2300-afastamento/api/(?P<pk>[0-9]+)/$',
        s2300_afastamento_api_views.s2300afastamentoDetail.as_view() ),

    url(r'^s2300-afastamento/$', 
        s2300_afastamento_listar_views.listar, 
        name='s2300_afastamento'),

    url(r'^s2300-afastamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_afastamento_salvar_views.salvar, 
        name='s2300_afastamento_salvar'),
        
    url(r'^s2300-afastamento/cadastrar/$', 
        s2300_afastamento_salvar_views.salvar, 
        name='s2300_afastamento_cadastrar'),

    url(r'^s2300-afastamento/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_afastamento_salvar_views.salvar, 
        name='s2300_afastamento_salvar_output'),
        
    url(r'^s2300-afastamento/(?P<output>[\w-]+)/$', 
        s2300_afastamento_listar_views.listar, 
        name='s2300_afastamento_output'),

    url(r'^s2300-termino/apagar/(?P<pk>[0-9]+)/$', 
        s2300_termino_apagar_views.apagar, 
        name='s2300_termino_apagar'),

    url(r'^s2300-termino/api/$',
        s2300_termino_api_views.s2300terminoList.as_view() ),

    url(r'^s2300-termino/api/(?P<pk>[0-9]+)/$',
        s2300_termino_api_views.s2300terminoDetail.as_view() ),

    url(r'^s2300-termino/$', 
        s2300_termino_listar_views.listar, 
        name='s2300_termino'),

    url(r'^s2300-termino/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2300_termino_salvar_views.salvar, 
        name='s2300_termino_salvar'),
        
    url(r'^s2300-termino/cadastrar/$', 
        s2300_termino_salvar_views.salvar, 
        name='s2300_termino_cadastrar'),

    url(r'^s2300-termino/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2300_termino_salvar_views.salvar, 
        name='s2300_termino_salvar_output'),
        
    url(r'^s2300-termino/(?P<output>[\w-]+)/$', 
        s2300_termino_listar_views.listar, 
        name='s2300_termino_output'),


]