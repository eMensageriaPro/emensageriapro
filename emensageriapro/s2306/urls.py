#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.s2306.views import s2306_infocomplementares_apagar as s2306_infocomplementares_apagar_views
from emensageriapro.s2306.views import s2306_infocomplementares_listar as s2306_infocomplementares_listar_views
from emensageriapro.s2306.views import s2306_infocomplementares_salvar as s2306_infocomplementares_salvar_views
from emensageriapro.s2306.views import s2306_infocomplementares_api as s2306_infocomplementares_api_views
from emensageriapro.s2306.views import s2306_cargofuncao_apagar as s2306_cargofuncao_apagar_views
from emensageriapro.s2306.views import s2306_cargofuncao_listar as s2306_cargofuncao_listar_views
from emensageriapro.s2306.views import s2306_cargofuncao_salvar as s2306_cargofuncao_salvar_views
from emensageriapro.s2306.views import s2306_cargofuncao_api as s2306_cargofuncao_api_views
from emensageriapro.s2306.views import s2306_remuneracao_apagar as s2306_remuneracao_apagar_views
from emensageriapro.s2306.views import s2306_remuneracao_listar as s2306_remuneracao_listar_views
from emensageriapro.s2306.views import s2306_remuneracao_salvar as s2306_remuneracao_salvar_views
from emensageriapro.s2306.views import s2306_remuneracao_api as s2306_remuneracao_api_views
from emensageriapro.s2306.views import s2306_infotrabcedido_apagar as s2306_infotrabcedido_apagar_views
from emensageriapro.s2306.views import s2306_infotrabcedido_listar as s2306_infotrabcedido_listar_views
from emensageriapro.s2306.views import s2306_infotrabcedido_salvar as s2306_infotrabcedido_salvar_views
from emensageriapro.s2306.views import s2306_infotrabcedido_api as s2306_infotrabcedido_api_views
from emensageriapro.s2306.views import s2306_infoestagiario_apagar as s2306_infoestagiario_apagar_views
from emensageriapro.s2306.views import s2306_infoestagiario_listar as s2306_infoestagiario_listar_views
from emensageriapro.s2306.views import s2306_infoestagiario_salvar as s2306_infoestagiario_salvar_views
from emensageriapro.s2306.views import s2306_infoestagiario_api as s2306_infoestagiario_api_views
from emensageriapro.s2306.views import s2306_ageintegracao_apagar as s2306_ageintegracao_apagar_views
from emensageriapro.s2306.views import s2306_ageintegracao_listar as s2306_ageintegracao_listar_views
from emensageriapro.s2306.views import s2306_ageintegracao_salvar as s2306_ageintegracao_salvar_views
from emensageriapro.s2306.views import s2306_ageintegracao_api as s2306_ageintegracao_api_views
from emensageriapro.s2306.views import s2306_supervisorestagio_apagar as s2306_supervisorestagio_apagar_views
from emensageriapro.s2306.views import s2306_supervisorestagio_listar as s2306_supervisorestagio_listar_views
from emensageriapro.s2306.views import s2306_supervisorestagio_salvar as s2306_supervisorestagio_salvar_views
from emensageriapro.s2306.views import s2306_supervisorestagio_api as s2306_supervisorestagio_api_views



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


    url(r'^s2306-infocomplementares/apagar/(?P<pk>[0-9]+)/$', 
        s2306_infocomplementares_apagar_views.apagar, 
        name='s2306_infocomplementares_apagar'),

    url(r'^s2306-infocomplementares/api/$',
        s2306_infocomplementares_api_views.s2306infoComplementaresList.as_view() ),

    url(r'^s2306-infocomplementares/api/(?P<pk>[0-9]+)/$',
        s2306_infocomplementares_api_views.s2306infoComplementaresDetail.as_view() ),

    url(r'^s2306-infocomplementares/$', 
        s2306_infocomplementares_listar_views.listar, 
        name='s2306_infocomplementares'),

    url(r'^s2306-infocomplementares/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2306_infocomplementares_salvar_views.salvar, 
        name='s2306_infocomplementares_salvar'),
        
    url(r'^s2306-infocomplementares/cadastrar/$', 
        s2306_infocomplementares_salvar_views.salvar, 
        name='s2306_infocomplementares_cadastrar'),

    url(r'^s2306-infocomplementares/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2306_infocomplementares_salvar_views.salvar, 
        name='s2306_infocomplementares_salvar_output'),
        
    url(r'^s2306-infocomplementares/(?P<output>[\w-]+)/$', 
        s2306_infocomplementares_listar_views.listar, 
        name='s2306_infocomplementares_output'),

    url(r'^s2306-cargofuncao/apagar/(?P<pk>[0-9]+)/$', 
        s2306_cargofuncao_apagar_views.apagar, 
        name='s2306_cargofuncao_apagar'),

    url(r'^s2306-cargofuncao/api/$',
        s2306_cargofuncao_api_views.s2306cargoFuncaoList.as_view() ),

    url(r'^s2306-cargofuncao/api/(?P<pk>[0-9]+)/$',
        s2306_cargofuncao_api_views.s2306cargoFuncaoDetail.as_view() ),

    url(r'^s2306-cargofuncao/$', 
        s2306_cargofuncao_listar_views.listar, 
        name='s2306_cargofuncao'),

    url(r'^s2306-cargofuncao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2306_cargofuncao_salvar_views.salvar, 
        name='s2306_cargofuncao_salvar'),
        
    url(r'^s2306-cargofuncao/cadastrar/$', 
        s2306_cargofuncao_salvar_views.salvar, 
        name='s2306_cargofuncao_cadastrar'),

    url(r'^s2306-cargofuncao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2306_cargofuncao_salvar_views.salvar, 
        name='s2306_cargofuncao_salvar_output'),
        
    url(r'^s2306-cargofuncao/(?P<output>[\w-]+)/$', 
        s2306_cargofuncao_listar_views.listar, 
        name='s2306_cargofuncao_output'),

    url(r'^s2306-remuneracao/apagar/(?P<pk>[0-9]+)/$', 
        s2306_remuneracao_apagar_views.apagar, 
        name='s2306_remuneracao_apagar'),

    url(r'^s2306-remuneracao/api/$',
        s2306_remuneracao_api_views.s2306remuneracaoList.as_view() ),

    url(r'^s2306-remuneracao/api/(?P<pk>[0-9]+)/$',
        s2306_remuneracao_api_views.s2306remuneracaoDetail.as_view() ),

    url(r'^s2306-remuneracao/$', 
        s2306_remuneracao_listar_views.listar, 
        name='s2306_remuneracao'),

    url(r'^s2306-remuneracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2306_remuneracao_salvar_views.salvar, 
        name='s2306_remuneracao_salvar'),
        
    url(r'^s2306-remuneracao/cadastrar/$', 
        s2306_remuneracao_salvar_views.salvar, 
        name='s2306_remuneracao_cadastrar'),

    url(r'^s2306-remuneracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2306_remuneracao_salvar_views.salvar, 
        name='s2306_remuneracao_salvar_output'),
        
    url(r'^s2306-remuneracao/(?P<output>[\w-]+)/$', 
        s2306_remuneracao_listar_views.listar, 
        name='s2306_remuneracao_output'),

    url(r'^s2306-infotrabcedido/apagar/(?P<pk>[0-9]+)/$', 
        s2306_infotrabcedido_apagar_views.apagar, 
        name='s2306_infotrabcedido_apagar'),

    url(r'^s2306-infotrabcedido/api/$',
        s2306_infotrabcedido_api_views.s2306infoTrabCedidoList.as_view() ),

    url(r'^s2306-infotrabcedido/api/(?P<pk>[0-9]+)/$',
        s2306_infotrabcedido_api_views.s2306infoTrabCedidoDetail.as_view() ),

    url(r'^s2306-infotrabcedido/$', 
        s2306_infotrabcedido_listar_views.listar, 
        name='s2306_infotrabcedido'),

    url(r'^s2306-infotrabcedido/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2306_infotrabcedido_salvar_views.salvar, 
        name='s2306_infotrabcedido_salvar'),
        
    url(r'^s2306-infotrabcedido/cadastrar/$', 
        s2306_infotrabcedido_salvar_views.salvar, 
        name='s2306_infotrabcedido_cadastrar'),

    url(r'^s2306-infotrabcedido/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2306_infotrabcedido_salvar_views.salvar, 
        name='s2306_infotrabcedido_salvar_output'),
        
    url(r'^s2306-infotrabcedido/(?P<output>[\w-]+)/$', 
        s2306_infotrabcedido_listar_views.listar, 
        name='s2306_infotrabcedido_output'),

    url(r'^s2306-infoestagiario/apagar/(?P<pk>[0-9]+)/$', 
        s2306_infoestagiario_apagar_views.apagar, 
        name='s2306_infoestagiario_apagar'),

    url(r'^s2306-infoestagiario/api/$',
        s2306_infoestagiario_api_views.s2306infoEstagiarioList.as_view() ),

    url(r'^s2306-infoestagiario/api/(?P<pk>[0-9]+)/$',
        s2306_infoestagiario_api_views.s2306infoEstagiarioDetail.as_view() ),

    url(r'^s2306-infoestagiario/$', 
        s2306_infoestagiario_listar_views.listar, 
        name='s2306_infoestagiario'),

    url(r'^s2306-infoestagiario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2306_infoestagiario_salvar_views.salvar, 
        name='s2306_infoestagiario_salvar'),
        
    url(r'^s2306-infoestagiario/cadastrar/$', 
        s2306_infoestagiario_salvar_views.salvar, 
        name='s2306_infoestagiario_cadastrar'),

    url(r'^s2306-infoestagiario/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2306_infoestagiario_salvar_views.salvar, 
        name='s2306_infoestagiario_salvar_output'),
        
    url(r'^s2306-infoestagiario/(?P<output>[\w-]+)/$', 
        s2306_infoestagiario_listar_views.listar, 
        name='s2306_infoestagiario_output'),

    url(r'^s2306-ageintegracao/apagar/(?P<pk>[0-9]+)/$', 
        s2306_ageintegracao_apagar_views.apagar, 
        name='s2306_ageintegracao_apagar'),

    url(r'^s2306-ageintegracao/api/$',
        s2306_ageintegracao_api_views.s2306ageIntegracaoList.as_view() ),

    url(r'^s2306-ageintegracao/api/(?P<pk>[0-9]+)/$',
        s2306_ageintegracao_api_views.s2306ageIntegracaoDetail.as_view() ),

    url(r'^s2306-ageintegracao/$', 
        s2306_ageintegracao_listar_views.listar, 
        name='s2306_ageintegracao'),

    url(r'^s2306-ageintegracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2306_ageintegracao_salvar_views.salvar, 
        name='s2306_ageintegracao_salvar'),
        
    url(r'^s2306-ageintegracao/cadastrar/$', 
        s2306_ageintegracao_salvar_views.salvar, 
        name='s2306_ageintegracao_cadastrar'),

    url(r'^s2306-ageintegracao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2306_ageintegracao_salvar_views.salvar, 
        name='s2306_ageintegracao_salvar_output'),
        
    url(r'^s2306-ageintegracao/(?P<output>[\w-]+)/$', 
        s2306_ageintegracao_listar_views.listar, 
        name='s2306_ageintegracao_output'),

    url(r'^s2306-supervisorestagio/apagar/(?P<pk>[0-9]+)/$', 
        s2306_supervisorestagio_apagar_views.apagar, 
        name='s2306_supervisorestagio_apagar'),

    url(r'^s2306-supervisorestagio/api/$',
        s2306_supervisorestagio_api_views.s2306supervisorEstagioList.as_view() ),

    url(r'^s2306-supervisorestagio/api/(?P<pk>[0-9]+)/$',
        s2306_supervisorestagio_api_views.s2306supervisorEstagioDetail.as_view() ),

    url(r'^s2306-supervisorestagio/$', 
        s2306_supervisorestagio_listar_views.listar, 
        name='s2306_supervisorestagio'),

    url(r'^s2306-supervisorestagio/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        s2306_supervisorestagio_salvar_views.salvar, 
        name='s2306_supervisorestagio_salvar'),
        
    url(r'^s2306-supervisorestagio/cadastrar/$', 
        s2306_supervisorestagio_salvar_views.salvar, 
        name='s2306_supervisorestagio_cadastrar'),

    url(r'^s2306-supervisorestagio/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        s2306_supervisorestagio_salvar_views.salvar, 
        name='s2306_supervisorestagio_salvar_output'),
        
    url(r'^s2306-supervisorestagio/(?P<output>[\w-]+)/$', 
        s2306_supervisorestagio_listar_views.listar, 
        name='s2306_supervisorestagio_output'),


]