#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_comunicacao as transmissor_lote_esocial_comunicacao_views
from emensageriapro.mensageiro.views import transmissor_esocial as transmissor_esocial_views
from emensageriapro.mensageiro.views import arquivos_recuperacao as arquivos_recuperacao_views
from emensageriapro.mensageiro.views import transmissor_efdreinf as transmissor_efdreinf_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_comunicacao as transmissor_lote_efdreinf_comunicacao_views
from emensageriapro.mensageiro.views import processar_arquivos as processar_arquivos_views
from emensageriapro.mensageiro.views import automatizacao as automatizacao_views
from emensageriapro.mensageiro.views import relatorios_imprimir as relatorios_imprimir_views
from emensageriapro.mensageiro.views import importacoes as importacoes_views
from emensageriapro.mensageiro.views import relatorios_apagar as relatorios_apagar_views
from emensageriapro.mensageiro.views import relatorios_listar as relatorios_listar_views
from emensageriapro.mensageiro.views import relatorios_salvar as relatorios_salvar_views
from emensageriapro.mensageiro.views import relatorios_api as relatorios_api_views
from emensageriapro.mensageiro.views import transmissores_apagar as transmissores_apagar_views
from emensageriapro.mensageiro.views import transmissores_listar as transmissores_listar_views
from emensageriapro.mensageiro.views import transmissores_salvar as transmissores_salvar_views
from emensageriapro.mensageiro.views import transmissores_api as transmissores_api_views
from emensageriapro.mensageiro.views import regras_validacao_apagar as regras_validacao_apagar_views
from emensageriapro.mensageiro.views import regras_validacao_listar as regras_validacao_listar_views
from emensageriapro.mensageiro.views import regras_validacao_salvar as regras_validacao_salvar_views
from emensageriapro.mensageiro.views import regras_validacao_api as regras_validacao_api_views
from emensageriapro.mensageiro.views import importacao_arquivos_apagar as importacao_arquivos_apagar_views
from emensageriapro.mensageiro.views import importacao_arquivos_listar as importacao_arquivos_listar_views
from emensageriapro.mensageiro.views import importacao_arquivos_salvar as importacao_arquivos_salvar_views
from emensageriapro.mensageiro.views import importacao_arquivos_api as importacao_arquivos_api_views
from emensageriapro.mensageiro.views import importacao_arquivos_eventos_apagar as importacao_arquivos_eventos_apagar_views
from emensageriapro.mensageiro.views import importacao_arquivos_eventos_listar as importacao_arquivos_eventos_listar_views
from emensageriapro.mensageiro.views import importacao_arquivos_eventos_salvar as importacao_arquivos_eventos_salvar_views
from emensageriapro.mensageiro.views import importacao_arquivos_eventos_api as importacao_arquivos_eventos_api_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_apagar as transmissor_lote_esocial_apagar_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_listar as transmissor_lote_esocial_listar_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_salvar as transmissor_lote_esocial_salvar_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_api as transmissor_lote_esocial_api_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_ocorrencias_apagar as transmissor_lote_esocial_ocorrencias_apagar_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_ocorrencias_listar as transmissor_lote_esocial_ocorrencias_listar_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_ocorrencias_salvar as transmissor_lote_esocial_ocorrencias_salvar_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_ocorrencias_api as transmissor_lote_esocial_ocorrencias_api_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_apagar as transmissor_lote_efdreinf_apagar_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_listar as transmissor_lote_efdreinf_listar_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_salvar as transmissor_lote_efdreinf_salvar_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_api as transmissor_lote_efdreinf_api_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_ocorrencias_apagar as transmissor_lote_efdreinf_ocorrencias_apagar_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_ocorrencias_listar as transmissor_lote_efdreinf_ocorrencias_listar_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_ocorrencias_salvar as transmissor_lote_efdreinf_ocorrencias_salvar_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_ocorrencias_api as transmissor_lote_efdreinf_ocorrencias_api_views
from emensageriapro.mensageiro.views import arquivos_apagar as arquivos_apagar_views
from emensageriapro.mensageiro.views import arquivos_listar as arquivos_listar_views
from emensageriapro.mensageiro.views import arquivos_salvar as arquivos_salvar_views
from emensageriapro.mensageiro.views import arquivos_api as arquivos_api_views
from emensageriapro.mensageiro.views import retornos_eventos_apagar as retornos_eventos_apagar_views
from emensageriapro.mensageiro.views import retornos_eventos_listar as retornos_eventos_listar_views
from emensageriapro.mensageiro.views import retornos_eventos_salvar as retornos_eventos_salvar_views
from emensageriapro.mensageiro.views import retornos_eventos_api as retornos_eventos_api_views
from emensageriapro.mensageiro.views import retornos_eventos_ocorrencias_apagar as retornos_eventos_ocorrencias_apagar_views
from emensageriapro.mensageiro.views import retornos_eventos_ocorrencias_listar as retornos_eventos_ocorrencias_listar_views
from emensageriapro.mensageiro.views import retornos_eventos_ocorrencias_salvar as retornos_eventos_ocorrencias_salvar_views
from emensageriapro.mensageiro.views import retornos_eventos_ocorrencias_api as retornos_eventos_ocorrencias_api_views
from emensageriapro.mensageiro.views import retornos_eventos_horarios_apagar as retornos_eventos_horarios_apagar_views
from emensageriapro.mensageiro.views import retornos_eventos_horarios_listar as retornos_eventos_horarios_listar_views
from emensageriapro.mensageiro.views import retornos_eventos_horarios_salvar as retornos_eventos_horarios_salvar_views
from emensageriapro.mensageiro.views import retornos_eventos_horarios_api as retornos_eventos_horarios_api_views
from emensageriapro.mensageiro.views import retornos_eventos_intervalos_apagar as retornos_eventos_intervalos_apagar_views
from emensageriapro.mensageiro.views import retornos_eventos_intervalos_listar as retornos_eventos_intervalos_listar_views
from emensageriapro.mensageiro.views import retornos_eventos_intervalos_salvar as retornos_eventos_intervalos_salvar_views
from emensageriapro.mensageiro.views import retornos_eventos_intervalos_api as retornos_eventos_intervalos_api_views



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


    url(r'^transmissor-lote-esocial/enviar/(?P<pk>[0-9]+)/$',
        transmissor_lote_esocial_comunicacao_views.enviar,
        name='transmissor_lote_esocial_enviar'),

    url(r'^transmissor-lote-esocial/consultar/(?P<pk>[0-9]+)/$',
        transmissor_lote_esocial_comunicacao_views.consultar,
        name='transmissor_lote_esocial_consultar'),
               
    url(r'^transmissor-lote-esocial/recibo/(?P<pk>[0-9]+)/$',
        transmissor_lote_esocial_comunicacao_views.recibo,
        name='transmissor_lote_esocial_recibo'),

    url(r'^transmissor-eventos-esocial/vincular/(?P<pk>[0-9]+)/$',
        transmissor_esocial_views.vincular_eventos_esocial,
        name='vincular_eventos_esocial'),
        
    url(r'^transmissor-eventos-esocial/desvincular/(?P<pk>[\w-]+)/$',
        transmissor_esocial_views.desvincular_eventos_esocial,
        name='desvincular_eventos_esocial'),

    url(r'^recuperacao-de-arquivos/(?P<pk>[0-9]+)/$', 
        arquivos_recuperacao_views.arquivos_recuperacao, 
        name='arquivos_recuperacao'),

    url(r'^reprocessar-arquivos/(?P<pk>[0-9]+)/$',
        arquivos_recuperacao_views.arquivos_reprocessar,
        name='arquivos_reprocessar'),
        
    url(r'^visualizacao-de-arquivos/(?P<pk>[0-9]+)/$', 
        arquivos_recuperacao_views.arquivos_visualizacao,
        name='arquivos_visualizacao'),

    url(r'^transmissor-eventos-efdreinf/vincular/(?P<pk>[0-9]+)/$',
        transmissor_efdreinf_views.vincular_eventos_efdreinf,
        name='vincular_eventos_efdreinf'),
        
    url(r'^transmissor-eventos-efdreinf/desvincular/(?P<pk>[\w-]+)/$',
        transmissor_efdreinf_views.desvincular_eventos_efdreinf,
        name='desvincular_eventos_efdreinf'),

    url(r'^transmissor-lote-efdreinf/enviar/(?P<pk>[0-9]+)/$',
        transmissor_lote_efdreinf_comunicacao_views.enviar,
        name='transmissor_lote_efdreinf_enviar'),

    url(r'^transmissor-lote-efdreinf/consultar/(?P<pk>[0-9]+)/$',
        transmissor_lote_efdreinf_comunicacao_views.consultar,
        name='transmissor_lote_efdreinf_consultar'),
        
    url(r'^transmissor-lote-efdreinf/recibo/(?P<pk>[0-9]+)/$',
        transmissor_lote_efdreinf_comunicacao_views.recibo,
        name='transmissor_lote_efdreinf_recibo'),

    url(r'^processar-arquivos/(?P<tab>[\w-]+)/$',
        processar_arquivos_views.scripts_processar_arquivos,
        name='scripts_processar_arquivos'),

    url(r'^importacoes-imprimir/(?P<pk>[0-9]+)/$',
        processar_arquivos_views.imprimir,
        name='processar_arquivos_imprimir'),

    url(r'^processar-arquivos-salvar/(?P<tab>[\w-]+)/$',
        processar_arquivos_views.scripts_salvar_arquivos,
        name='scripts_salvar_arquivos'),

    url(r'^validacao-automatica/$',
        automatizacao_views.scripts_validacao_automatica,
        name='scripts_validacao_automatica'),

    url(r'^transmissao-automatica/$',
        automatizacao_views.scripts_transmissao_automatica,
        name='scripts_transmissao_automatica'),

    url(r'^relatorios/imprimir/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        relatorios_imprimir_views.imprimir,
        name='relatorios_imprimir'),

    url(r'^importacoes/listar/$', 
        importacoes_views.listar, 
        name='importacoes'),

    

    

    url(r'^relatorios/apagar/(?P<pk>[0-9]+)/$', 
        relatorios_apagar_views.apagar, 
        name='relatorios_apagar'),

    url(r'^relatorios/api/$',
        relatorios_api_views.RelatoriosList.as_view() ),

    url(r'^relatorios/api/(?P<pk>[0-9]+)/$',
        relatorios_api_views.RelatoriosDetail.as_view() ),

    url(r'^relatorios/$', 
        relatorios_listar_views.listar, 
        name='relatorios'),

    url(r'^relatorios/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        relatorios_salvar_views.salvar, 
        name='relatorios_salvar'),
        
    url(r'^relatorios/cadastrar/$', 
        relatorios_salvar_views.salvar, 
        name='relatorios_cadastrar'),

    url(r'^relatorios/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        relatorios_salvar_views.salvar, 
        name='relatorios_salvar_output'),
        
    url(r'^relatorios/(?P<output>[\w-]+)/$', 
        relatorios_listar_views.listar, 
        name='relatorios_output'),

    url(r'^transmissores/apagar/(?P<pk>[0-9]+)/$', 
        transmissores_apagar_views.apagar, 
        name='transmissores_apagar'),

    url(r'^transmissores/api/$',
        transmissores_api_views.TransmissorLoteList.as_view() ),

    url(r'^transmissores/api/(?P<pk>[0-9]+)/$',
        transmissores_api_views.TransmissorLoteDetail.as_view() ),

    url(r'^transmissores/$', 
        transmissores_listar_views.listar, 
        name='transmissores'),

    url(r'^transmissores/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        transmissores_salvar_views.salvar, 
        name='transmissores_salvar'),
        
    url(r'^transmissores/cadastrar/$', 
        transmissores_salvar_views.salvar, 
        name='transmissores_cadastrar'),

    url(r'^transmissores/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        transmissores_salvar_views.salvar, 
        name='transmissores_salvar_output'),
        
    url(r'^transmissores/(?P<output>[\w-]+)/$', 
        transmissores_listar_views.listar, 
        name='transmissores_output'),

    url(r'^regras-validacao/apagar/(?P<pk>[0-9]+)/$', 
        regras_validacao_apagar_views.apagar, 
        name='regras_validacao_apagar'),

    url(r'^regras-validacao/api/$',
        regras_validacao_api_views.RegrasDeValidacaoList.as_view() ),

    url(r'^regras-validacao/api/(?P<pk>[0-9]+)/$',
        regras_validacao_api_views.RegrasDeValidacaoDetail.as_view() ),

    url(r'^regras-validacao/$', 
        regras_validacao_listar_views.listar, 
        name='regras_validacao'),

    url(r'^regras-validacao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        regras_validacao_salvar_views.salvar, 
        name='regras_validacao_salvar'),
        
    url(r'^regras-validacao/cadastrar/$', 
        regras_validacao_salvar_views.salvar, 
        name='regras_validacao_cadastrar'),

    url(r'^regras-validacao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        regras_validacao_salvar_views.salvar, 
        name='regras_validacao_salvar_output'),
        
    url(r'^regras-validacao/(?P<output>[\w-]+)/$', 
        regras_validacao_listar_views.listar, 
        name='regras_validacao_output'),

    url(r'^importacao-arquivos/apagar/(?P<pk>[0-9]+)/$', 
        importacao_arquivos_apagar_views.apagar, 
        name='importacao_arquivos_apagar'),

    url(r'^importacao-arquivos/api/$',
        importacao_arquivos_api_views.ImportacaoArquivosList.as_view() ),

    url(r'^importacao-arquivos/api/(?P<pk>[0-9]+)/$',
        importacao_arquivos_api_views.ImportacaoArquivosDetail.as_view() ),

    url(r'^importacao-arquivos/$', 
        importacao_arquivos_listar_views.listar, 
        name='importacao_arquivos'),

    url(r'^importacao-arquivos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        importacao_arquivos_salvar_views.salvar, 
        name='importacao_arquivos_salvar'),
        
    url(r'^importacao-arquivos/cadastrar/$', 
        importacao_arquivos_salvar_views.salvar, 
        name='importacao_arquivos_cadastrar'),

    url(r'^importacao-arquivos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        importacao_arquivos_salvar_views.salvar, 
        name='importacao_arquivos_salvar_output'),
        
    url(r'^importacao-arquivos/(?P<output>[\w-]+)/$', 
        importacao_arquivos_listar_views.listar, 
        name='importacao_arquivos_output'),

    url(r'^importacao-arquivos-eventos/apagar/(?P<pk>[0-9]+)/$', 
        importacao_arquivos_eventos_apagar_views.apagar, 
        name='importacao_arquivos_eventos_apagar'),

    url(r'^importacao-arquivos-eventos/api/$',
        importacao_arquivos_eventos_api_views.ImportacaoArquivosEventosList.as_view() ),

    url(r'^importacao-arquivos-eventos/api/(?P<pk>[0-9]+)/$',
        importacao_arquivos_eventos_api_views.ImportacaoArquivosEventosDetail.as_view() ),

    url(r'^importacao-arquivos-eventos/$', 
        importacao_arquivos_eventos_listar_views.listar, 
        name='importacao_arquivos_eventos'),

    url(r'^importacao-arquivos-eventos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        importacao_arquivos_eventos_salvar_views.salvar, 
        name='importacao_arquivos_eventos_salvar'),
        
    url(r'^importacao-arquivos-eventos/cadastrar/$', 
        importacao_arquivos_eventos_salvar_views.salvar, 
        name='importacao_arquivos_eventos_cadastrar'),

    url(r'^importacao-arquivos-eventos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        importacao_arquivos_eventos_salvar_views.salvar, 
        name='importacao_arquivos_eventos_salvar_output'),
        
    url(r'^importacao-arquivos-eventos/(?P<output>[\w-]+)/$', 
        importacao_arquivos_eventos_listar_views.listar, 
        name='importacao_arquivos_eventos_output'),

    url(r'^transmissor-lote-esocial/apagar/(?P<pk>[0-9]+)/$', 
        transmissor_lote_esocial_apagar_views.apagar, 
        name='transmissor_lote_esocial_apagar'),

    url(r'^transmissor-lote-esocial/api/$',
        transmissor_lote_esocial_api_views.TransmissorLoteEsocialList.as_view() ),

    url(r'^transmissor-lote-esocial/api/(?P<pk>[0-9]+)/$',
        transmissor_lote_esocial_api_views.TransmissorLoteEsocialDetail.as_view() ),

    url(r'^transmissor-lote-esocial/$', 
        transmissor_lote_esocial_listar_views.listar, 
        name='transmissor_lote_esocial'),

    url(r'^transmissor-lote-esocial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        transmissor_lote_esocial_salvar_views.salvar, 
        name='transmissor_lote_esocial_salvar'),
        
    url(r'^transmissor-lote-esocial/cadastrar/$', 
        transmissor_lote_esocial_salvar_views.salvar, 
        name='transmissor_lote_esocial_cadastrar'),

    url(r'^transmissor-lote-esocial/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        transmissor_lote_esocial_salvar_views.salvar, 
        name='transmissor_lote_esocial_salvar_output'),
        
    url(r'^transmissor-lote-esocial/(?P<output>[\w-]+)/$', 
        transmissor_lote_esocial_listar_views.listar, 
        name='transmissor_lote_esocial_output'),

    url(r'^transmissor-lote-esocial-ocorrencias/apagar/(?P<pk>[0-9]+)/$', 
        transmissor_lote_esocial_ocorrencias_apagar_views.apagar, 
        name='transmissor_lote_esocial_ocorrencias_apagar'),

    url(r'^transmissor-lote-esocial-ocorrencias/api/$',
        transmissor_lote_esocial_ocorrencias_api_views.TransmissorLoteEsocialOcorrenciasList.as_view() ),

    url(r'^transmissor-lote-esocial-ocorrencias/api/(?P<pk>[0-9]+)/$',
        transmissor_lote_esocial_ocorrencias_api_views.TransmissorLoteEsocialOcorrenciasDetail.as_view() ),

    url(r'^transmissor-lote-esocial-ocorrencias/$', 
        transmissor_lote_esocial_ocorrencias_listar_views.listar, 
        name='transmissor_lote_esocial_ocorrencias'),

    url(r'^transmissor-lote-esocial-ocorrencias/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        transmissor_lote_esocial_ocorrencias_salvar_views.salvar, 
        name='transmissor_lote_esocial_ocorrencias_salvar'),
        
    url(r'^transmissor-lote-esocial-ocorrencias/cadastrar/$', 
        transmissor_lote_esocial_ocorrencias_salvar_views.salvar, 
        name='transmissor_lote_esocial_ocorrencias_cadastrar'),

    url(r'^transmissor-lote-esocial-ocorrencias/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        transmissor_lote_esocial_ocorrencias_salvar_views.salvar, 
        name='transmissor_lote_esocial_ocorrencias_salvar_output'),
        
    url(r'^transmissor-lote-esocial-ocorrencias/(?P<output>[\w-]+)/$', 
        transmissor_lote_esocial_ocorrencias_listar_views.listar, 
        name='transmissor_lote_esocial_ocorrencias_output'),

    url(r'^transmissor-lote-efdreinf/apagar/(?P<pk>[0-9]+)/$', 
        transmissor_lote_efdreinf_apagar_views.apagar, 
        name='transmissor_lote_efdreinf_apagar'),

    url(r'^transmissor-lote-efdreinf/api/$',
        transmissor_lote_efdreinf_api_views.TransmissorLoteEfdreinfList.as_view() ),

    url(r'^transmissor-lote-efdreinf/api/(?P<pk>[0-9]+)/$',
        transmissor_lote_efdreinf_api_views.TransmissorLoteEfdreinfDetail.as_view() ),

    url(r'^transmissor-lote-efdreinf/$', 
        transmissor_lote_efdreinf_listar_views.listar, 
        name='transmissor_lote_efdreinf'),

    url(r'^transmissor-lote-efdreinf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        transmissor_lote_efdreinf_salvar_views.salvar, 
        name='transmissor_lote_efdreinf_salvar'),
        
    url(r'^transmissor-lote-efdreinf/cadastrar/$', 
        transmissor_lote_efdreinf_salvar_views.salvar, 
        name='transmissor_lote_efdreinf_cadastrar'),

    url(r'^transmissor-lote-efdreinf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        transmissor_lote_efdreinf_salvar_views.salvar, 
        name='transmissor_lote_efdreinf_salvar_output'),
        
    url(r'^transmissor-lote-efdreinf/(?P<output>[\w-]+)/$', 
        transmissor_lote_efdreinf_listar_views.listar, 
        name='transmissor_lote_efdreinf_output'),

    url(r'^transmissor-lote-efdreinf-ocorrencias/apagar/(?P<pk>[0-9]+)/$', 
        transmissor_lote_efdreinf_ocorrencias_apagar_views.apagar, 
        name='transmissor_lote_efdreinf_ocorrencias_apagar'),

    url(r'^transmissor-lote-efdreinf-ocorrencias/api/$',
        transmissor_lote_efdreinf_ocorrencias_api_views.TransmissorLoteEfdreinfOcorrenciasList.as_view() ),

    url(r'^transmissor-lote-efdreinf-ocorrencias/api/(?P<pk>[0-9]+)/$',
        transmissor_lote_efdreinf_ocorrencias_api_views.TransmissorLoteEfdreinfOcorrenciasDetail.as_view() ),

    url(r'^transmissor-lote-efdreinf-ocorrencias/$', 
        transmissor_lote_efdreinf_ocorrencias_listar_views.listar, 
        name='transmissor_lote_efdreinf_ocorrencias'),

    url(r'^transmissor-lote-efdreinf-ocorrencias/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        transmissor_lote_efdreinf_ocorrencias_salvar_views.salvar, 
        name='transmissor_lote_efdreinf_ocorrencias_salvar'),
        
    url(r'^transmissor-lote-efdreinf-ocorrencias/cadastrar/$', 
        transmissor_lote_efdreinf_ocorrencias_salvar_views.salvar, 
        name='transmissor_lote_efdreinf_ocorrencias_cadastrar'),

    url(r'^transmissor-lote-efdreinf-ocorrencias/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        transmissor_lote_efdreinf_ocorrencias_salvar_views.salvar, 
        name='transmissor_lote_efdreinf_ocorrencias_salvar_output'),
        
    url(r'^transmissor-lote-efdreinf-ocorrencias/(?P<output>[\w-]+)/$', 
        transmissor_lote_efdreinf_ocorrencias_listar_views.listar, 
        name='transmissor_lote_efdreinf_ocorrencias_output'),

    url(r'^arquivos/apagar/(?P<pk>[0-9]+)/$', 
        arquivos_apagar_views.apagar, 
        name='arquivos_apagar'),

    url(r'^arquivos/api/$',
        arquivos_api_views.ArquivosList.as_view() ),

    url(r'^arquivos/api/(?P<pk>[0-9]+)/$',
        arquivos_api_views.ArquivosDetail.as_view() ),

    url(r'^arquivos/$', 
        arquivos_listar_views.listar, 
        name='arquivos'),

    url(r'^arquivos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        arquivos_salvar_views.salvar, 
        name='arquivos_salvar'),
        
    url(r'^arquivos/cadastrar/$', 
        arquivos_salvar_views.salvar, 
        name='arquivos_cadastrar'),

    url(r'^arquivos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        arquivos_salvar_views.salvar, 
        name='arquivos_salvar_output'),
        
    url(r'^arquivos/(?P<output>[\w-]+)/$', 
        arquivos_listar_views.listar, 
        name='arquivos_output'),

    url(r'^retornos-eventos/apagar/(?P<pk>[0-9]+)/$', 
        retornos_eventos_apagar_views.apagar, 
        name='retornos_eventos_apagar'),

    url(r'^retornos-eventos/api/$',
        retornos_eventos_api_views.RetornosEventosList.as_view() ),

    url(r'^retornos-eventos/api/(?P<pk>[0-9]+)/$',
        retornos_eventos_api_views.RetornosEventosDetail.as_view() ),

    url(r'^retornos-eventos/$', 
        retornos_eventos_listar_views.listar, 
        name='retornos_eventos'),

    url(r'^retornos-eventos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        retornos_eventos_salvar_views.salvar, 
        name='retornos_eventos_salvar'),
        
    url(r'^retornos-eventos/cadastrar/$', 
        retornos_eventos_salvar_views.salvar, 
        name='retornos_eventos_cadastrar'),

    url(r'^retornos-eventos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        retornos_eventos_salvar_views.salvar, 
        name='retornos_eventos_salvar_output'),
        
    url(r'^retornos-eventos/(?P<output>[\w-]+)/$', 
        retornos_eventos_listar_views.listar, 
        name='retornos_eventos_output'),

    url(r'^retornos-eventos-ocorrencias/apagar/(?P<pk>[0-9]+)/$', 
        retornos_eventos_ocorrencias_apagar_views.apagar, 
        name='retornos_eventos_ocorrencias_apagar'),

    url(r'^retornos-eventos-ocorrencias/api/$',
        retornos_eventos_ocorrencias_api_views.RetornosEventosOcorrenciasList.as_view() ),

    url(r'^retornos-eventos-ocorrencias/api/(?P<pk>[0-9]+)/$',
        retornos_eventos_ocorrencias_api_views.RetornosEventosOcorrenciasDetail.as_view() ),

    url(r'^retornos-eventos-ocorrencias/$', 
        retornos_eventos_ocorrencias_listar_views.listar, 
        name='retornos_eventos_ocorrencias'),

    url(r'^retornos-eventos-ocorrencias/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        retornos_eventos_ocorrencias_salvar_views.salvar, 
        name='retornos_eventos_ocorrencias_salvar'),
        
    url(r'^retornos-eventos-ocorrencias/cadastrar/$', 
        retornos_eventos_ocorrencias_salvar_views.salvar, 
        name='retornos_eventos_ocorrencias_cadastrar'),

    url(r'^retornos-eventos-ocorrencias/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        retornos_eventos_ocorrencias_salvar_views.salvar, 
        name='retornos_eventos_ocorrencias_salvar_output'),
        
    url(r'^retornos-eventos-ocorrencias/(?P<output>[\w-]+)/$', 
        retornos_eventos_ocorrencias_listar_views.listar, 
        name='retornos_eventos_ocorrencias_output'),

    url(r'^retornos-eventos-horarios/apagar/(?P<pk>[0-9]+)/$', 
        retornos_eventos_horarios_apagar_views.apagar, 
        name='retornos_eventos_horarios_apagar'),

    url(r'^retornos-eventos-horarios/api/$',
        retornos_eventos_horarios_api_views.RetornosEventosHorariosList.as_view() ),

    url(r'^retornos-eventos-horarios/api/(?P<pk>[0-9]+)/$',
        retornos_eventos_horarios_api_views.RetornosEventosHorariosDetail.as_view() ),

    url(r'^retornos-eventos-horarios/$', 
        retornos_eventos_horarios_listar_views.listar, 
        name='retornos_eventos_horarios'),

    url(r'^retornos-eventos-horarios/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        retornos_eventos_horarios_salvar_views.salvar, 
        name='retornos_eventos_horarios_salvar'),
        
    url(r'^retornos-eventos-horarios/cadastrar/$', 
        retornos_eventos_horarios_salvar_views.salvar, 
        name='retornos_eventos_horarios_cadastrar'),

    url(r'^retornos-eventos-horarios/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        retornos_eventos_horarios_salvar_views.salvar, 
        name='retornos_eventos_horarios_salvar_output'),
        
    url(r'^retornos-eventos-horarios/(?P<output>[\w-]+)/$', 
        retornos_eventos_horarios_listar_views.listar, 
        name='retornos_eventos_horarios_output'),

    url(r'^retornos-eventos-intervalos/apagar/(?P<pk>[0-9]+)/$', 
        retornos_eventos_intervalos_apagar_views.apagar, 
        name='retornos_eventos_intervalos_apagar'),

    url(r'^retornos-eventos-intervalos/api/$',
        retornos_eventos_intervalos_api_views.RetornosEventosIntervalosList.as_view() ),

    url(r'^retornos-eventos-intervalos/api/(?P<pk>[0-9]+)/$',
        retornos_eventos_intervalos_api_views.RetornosEventosIntervalosDetail.as_view() ),

    url(r'^retornos-eventos-intervalos/$', 
        retornos_eventos_intervalos_listar_views.listar, 
        name='retornos_eventos_intervalos'),

    url(r'^retornos-eventos-intervalos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$', 
        retornos_eventos_intervalos_salvar_views.salvar, 
        name='retornos_eventos_intervalos_salvar'),
        
    url(r'^retornos-eventos-intervalos/cadastrar/$', 
        retornos_eventos_intervalos_salvar_views.salvar, 
        name='retornos_eventos_intervalos_cadastrar'),

    url(r'^retornos-eventos-intervalos/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$', 
        retornos_eventos_intervalos_salvar_views.salvar, 
        name='retornos_eventos_intervalos_salvar_output'),
        
    url(r'^retornos-eventos-intervalos/(?P<output>[\w-]+)/$', 
        retornos_eventos_intervalos_listar_views.listar, 
        name='retornos_eventos_intervalos_output'),

    


]