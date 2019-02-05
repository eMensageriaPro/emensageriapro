#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.mensageiro.views import transmissor_lote_esocial_comunicacao as transmissor_lote_esocial_comunicacao_views
from emensageriapro.mensageiro.views import transmissor_esocial as transmissor_esocial_views
from emensageriapro.mensageiro.views import arquivos_recuperacao as arquivos_recuperacao_views
from emensageriapro.mensageiro.views import mapa_processamento as mapa_processamento_views
from emensageriapro.mensageiro.views import transmissor_efdreinf as transmissor_efdreinf_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_comunicacao as transmissor_lote_efdreinf_comunicacao_views
from emensageriapro.mensageiro.views import processar_arquivos as processar_arquivos_views
from emensageriapro.mensageiro.views import automatizacao as automatizacao_views
from emensageriapro.mensageiro.views import relatorios_imprimir as relatorios_imprimir_views
from emensageriapro.mensageiro.views import importacoes as importacoes_views
from emensageriapro.mensageiro.views import relatorios as relatorios_views
from emensageriapro.mensageiro.views import transmissores as transmissores_views
from emensageriapro.mensageiro.views import regras_validacao as regras_validacao_views
from emensageriapro.mensageiro.views import importacao_arquivos as importacao_arquivos_views
from emensageriapro.mensageiro.views import importacao_arquivos_eventos as importacao_arquivos_eventos_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial as transmissor_lote_esocial_views
from emensageriapro.mensageiro.views import transmissor_lote_esocial_ocorrencias as transmissor_lote_esocial_ocorrencias_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf as transmissor_lote_efdreinf_views
from emensageriapro.mensageiro.views import transmissor_lote_efdreinf_ocorrencias as transmissor_lote_efdreinf_ocorrencias_views
from emensageriapro.mensageiro.views import arquivos as arquivos_views
from emensageriapro.mensageiro.views import retornos_eventos as retornos_eventos_views
from emensageriapro.mensageiro.views import retornos_eventos_ocorrencias as retornos_eventos_ocorrencias_views
from emensageriapro.mensageiro.views import retornos_eventos_horarios as retornos_eventos_horarios_views
from emensageriapro.mensageiro.views import retornos_eventos_intervalos as retornos_eventos_intervalos_views



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

url(r'^scripts/enviar-lote-esocial/(?P<chave>.*)/(?P<transmissor_lote_esocial_id>\d+)/$',
        transmissor_lote_esocial_comunicacao_views.scripts_enviar_lote,
        name='scripts_enviar_esocial_lote'),

url(r'^scripts/consultar-lote-esocial/(?P<chave>.*)/(?P<transmissor_lote_esocial_id>\d+)/$',
        transmissor_lote_esocial_comunicacao_views.scripts_consultar_lote,
        name='scripts_consultar_esocial_lote'),

url(r'^transmissor-lote-esocial/enviar/(?P<hash>.*)/$',
        transmissor_lote_esocial_comunicacao_views.enviar,
        name='transmissor_lote_esocial_enviar'),

url(r'^transmissor-lote-esocial/consultar/(?P<hash>.*)/$',
        transmissor_lote_esocial_comunicacao_views.consultar,
        name='transmissor_lote_esocial_consultar'),
        
        
url(r'^transmissor-lote-esocial/recibo/(?P<hash>.*)/$',
        transmissor_lote_esocial_comunicacao_views.recibo,
        name='transmissor_lote_esocial_recibo'),

url(r'^transmissor-eventos-esocial/vincular/(?P<hash>.+)/$',
        transmissor_esocial_views.vincular_eventos_esocial,
        name='vincular_eventos_esocial'),
        
url(r'^transmissor-eventos-esocial/desvincular/(?P<hash>.+)/$',
        transmissor_esocial_views.desvincular_eventos_esocial,
        name='desvincular_eventos_esocial'),

url(r'^recuperacao-de-arquivos/(?P<hash>.*)/$', 
        arquivos_recuperacao_views.arquivos_recuperacao, 
        name='arquivos_recuperacao'),

url(r'^reprocessar-arquivos/(?P<hash>.*)/$',
        arquivos_recuperacao_views.arquivos_reprocessar,
        name='arquivos_reprocessar'),
        
url(r'^visualizacao-de-arquivos/(?P<hash>.*)/$', 
        arquivos_recuperacao_views.arquivos_visualizacao,
        name='arquivos_visualizacao'),

url(r'^mapa-processamento/(?P<hash>.*)/$',
        mapa_processamento_views.listar,
        name='mapa_processamento'),

url(r'^transmissor-eventos-efdreinf/vincular/(?P<hash>.+)/$',
        transmissor_efdreinf_views.vincular_eventos_efdreinf,
        name='vincular_eventos_efdreinf'),
        
url(r'^transmissor-eventos-efdreinf/desvincular/(?P<hash>.+)/$',
        transmissor_efdreinf_views.desvincular_eventos_efdreinf,
        name='desvincular_eventos_efdreinf'),

url(r'^scripts/enviar-lote-efdreinf/(?P<chave>.*)/(?P<transmissor_lote_efdreinf_id>\d+)/$',
        transmissor_lote_efdreinf_comunicacao_views.scripts_enviar_lote,
        name='scripts_enviar_efdreinf_lote'),

url(r'^scripts/consultar-lote-efdreinf/(?P<chave>.*)/(?P<transmissor_lote_efdreinf_id>\d+)/$',
        transmissor_lote_efdreinf_comunicacao_views.scripts_consultar_lote,
        name='scripts_consultar_efdreinf_lote'),

url(r'^transmissor-lote-efdreinf/enviar/(?P<hash>.*)/$',
        transmissor_lote_efdreinf_comunicacao_views.enviar,
        name='transmissor_lote_efdreinf_enviar'),

url(r'^transmissor-lote-efdreinf/consultar/(?P<hash>.*)/$',
        transmissor_lote_efdreinf_comunicacao_views.consultar,
        name='transmissor_lote_efdreinf_consultar'),
        
        
url(r'^transmissor-lote-efdreinf/recibo/(?P<hash>.*)/$',
        transmissor_lote_efdreinf_comunicacao_views.recibo,
        name='transmissor_lote_efdreinf_recibo'),

url(r'^processar-arquivos/$',
        processar_arquivos_views.scripts_processar_arquivos,
        name='scripts_processar_arquivos'),

url(r'^importacoes-imprimir/(?P<hash>.*)/$',
        processar_arquivos_views.imprimir,
        name='processar_arquivos_imprimir'),
        

url(r'^processar-arquivos-salvar/(?P<hash>.*)/$',
        processar_arquivos_views.scripts_salvar_arquivos,
        name='scripts_salvar_arquivos'),

url(r'^validacao-automatica/$',
        automatizacao_views.scripts_validacao_automatica,
        name='scripts_validacao_automatica'),

url(r'^transmissao-automatica/$',
        automatizacao_views.scripts_transmissao_automatica,
        name='scripts_transmissao_automatica'),

url(r'^relatorios/imprimir/(?P<hash>.*)/$',
        relatorios_imprimir_views.imprimir,
        name='relatorios_imprimir'),

url(r'^importacoes/listar/(?P<hash>.*)/$', 
        importacoes_views.listar, 
        name='importacoes'),









url(r'^relatorios/apagar/(?P<hash>.*)/$', 
        relatorios_views.apagar, 
        name='relatorios_apagar'),

url(r'^relatorios/api/$',
            relatorios_views.RelatoriosList.as_view() ),

        url(r'^relatorios/api/(?P<pk>[0-9]+)/$',
            relatorios_views.RelatoriosDetail.as_view() ),

url(r'^relatorios/listar/(?P<hash>.*)/$', 
        relatorios_views.listar, 
        name='relatorios'),

url(r'^relatorios/salvar/(?P<hash>.*)/$', 
        relatorios_views.salvar, 
        name='relatorios_salvar'),



url(r'^transmissores/apagar/(?P<hash>.*)/$', 
        transmissores_views.apagar, 
        name='transmissores_apagar'),

url(r'^transmissores/api/$',
            transmissores_views.TransmissorLoteList.as_view() ),

        url(r'^transmissores/api/(?P<pk>[0-9]+)/$',
            transmissores_views.TransmissorLoteDetail.as_view() ),

url(r'^transmissores/listar/(?P<hash>.*)/$', 
        transmissores_views.listar, 
        name='transmissores'),

url(r'^transmissores/salvar/(?P<hash>.*)/$', 
        transmissores_views.salvar, 
        name='transmissores_salvar'),



url(r'^regras-validacao/apagar/(?P<hash>.*)/$', 
        regras_validacao_views.apagar, 
        name='regras_validacao_apagar'),

url(r'^regras-validacao/api/$',
            regras_validacao_views.RegrasDeValidacaoList.as_view() ),

        url(r'^regras-validacao/api/(?P<pk>[0-9]+)/$',
            regras_validacao_views.RegrasDeValidacaoDetail.as_view() ),

url(r'^regras-validacao/listar/(?P<hash>.*)/$', 
        regras_validacao_views.listar, 
        name='regras_validacao'),

url(r'^regras-validacao/salvar/(?P<hash>.*)/$', 
        regras_validacao_views.salvar, 
        name='regras_validacao_salvar'),



url(r'^importacao-arquivos/apagar/(?P<hash>.*)/$', 
        importacao_arquivos_views.apagar, 
        name='importacao_arquivos_apagar'),

url(r'^importacao-arquivos/api/$',
            importacao_arquivos_views.ImportacaoArquivosList.as_view() ),

        url(r'^importacao-arquivos/api/(?P<pk>[0-9]+)/$',
            importacao_arquivos_views.ImportacaoArquivosDetail.as_view() ),

url(r'^importacao-arquivos/listar/(?P<hash>.*)/$', 
        importacao_arquivos_views.listar, 
        name='importacao_arquivos'),

url(r'^importacao-arquivos/salvar/(?P<hash>.*)/$', 
        importacao_arquivos_views.salvar, 
        name='importacao_arquivos_salvar'),



url(r'^importacao-arquivos-eventos/apagar/(?P<hash>.*)/$', 
        importacao_arquivos_eventos_views.apagar, 
        name='importacao_arquivos_eventos_apagar'),

url(r'^importacao-arquivos-eventos/api/$',
            importacao_arquivos_eventos_views.ImportacaoArquivosEventosList.as_view() ),

        url(r'^importacao-arquivos-eventos/api/(?P<pk>[0-9]+)/$',
            importacao_arquivos_eventos_views.ImportacaoArquivosEventosDetail.as_view() ),

url(r'^importacao-arquivos-eventos/listar/(?P<hash>.*)/$', 
        importacao_arquivos_eventos_views.listar, 
        name='importacao_arquivos_eventos'),

url(r'^importacao-arquivos-eventos/salvar/(?P<hash>.*)/$', 
        importacao_arquivos_eventos_views.salvar, 
        name='importacao_arquivos_eventos_salvar'),



url(r'^transmissor-lote-esocial/apagar/(?P<hash>.*)/$', 
        transmissor_lote_esocial_views.apagar, 
        name='transmissor_lote_esocial_apagar'),

url(r'^transmissor-lote-esocial/api/$',
            transmissor_lote_esocial_views.TransmissorLoteEsocialList.as_view() ),

        url(r'^transmissor-lote-esocial/api/(?P<pk>[0-9]+)/$',
            transmissor_lote_esocial_views.TransmissorLoteEsocialDetail.as_view() ),

url(r'^transmissor-lote-esocial/listar/(?P<hash>.*)/$', 
        transmissor_lote_esocial_views.listar, 
        name='transmissor_lote_esocial'),

url(r'^transmissor-lote-esocial/salvar/(?P<hash>.*)/$', 
        transmissor_lote_esocial_views.salvar, 
        name='transmissor_lote_esocial_salvar'),



url(r'^transmissor-lote-esocial-ocorrencias/apagar/(?P<hash>.*)/$', 
        transmissor_lote_esocial_ocorrencias_views.apagar, 
        name='transmissor_lote_esocial_ocorrencias_apagar'),

url(r'^transmissor-lote-esocial-ocorrencias/api/$',
            transmissor_lote_esocial_ocorrencias_views.TransmissorLoteEsocialOcorrenciasList.as_view() ),

        url(r'^transmissor-lote-esocial-ocorrencias/api/(?P<pk>[0-9]+)/$',
            transmissor_lote_esocial_ocorrencias_views.TransmissorLoteEsocialOcorrenciasDetail.as_view() ),

url(r'^transmissor-lote-esocial-ocorrencias/listar/(?P<hash>.*)/$', 
        transmissor_lote_esocial_ocorrencias_views.listar, 
        name='transmissor_lote_esocial_ocorrencias'),

url(r'^transmissor-lote-esocial-ocorrencias/salvar/(?P<hash>.*)/$', 
        transmissor_lote_esocial_ocorrencias_views.salvar, 
        name='transmissor_lote_esocial_ocorrencias_salvar'),



url(r'^transmissor-lote-efdreinf/apagar/(?P<hash>.*)/$', 
        transmissor_lote_efdreinf_views.apagar, 
        name='transmissor_lote_efdreinf_apagar'),

url(r'^transmissor-lote-efdreinf/api/$',
            transmissor_lote_efdreinf_views.TransmissorLoteEfdreinfList.as_view() ),

        url(r'^transmissor-lote-efdreinf/api/(?P<pk>[0-9]+)/$',
            transmissor_lote_efdreinf_views.TransmissorLoteEfdreinfDetail.as_view() ),

url(r'^transmissor-lote-efdreinf/listar/(?P<hash>.*)/$', 
        transmissor_lote_efdreinf_views.listar, 
        name='transmissor_lote_efdreinf'),

url(r'^transmissor-lote-efdreinf/salvar/(?P<hash>.*)/$', 
        transmissor_lote_efdreinf_views.salvar, 
        name='transmissor_lote_efdreinf_salvar'),



url(r'^transmissor-lote-efdreinf-ocorrencias/apagar/(?P<hash>.*)/$', 
        transmissor_lote_efdreinf_ocorrencias_views.apagar, 
        name='transmissor_lote_efdreinf_ocorrencias_apagar'),

url(r'^transmissor-lote-efdreinf-ocorrencias/api/$',
            transmissor_lote_efdreinf_ocorrencias_views.TransmissorLoteEfdreinfOcorrenciasList.as_view() ),

        url(r'^transmissor-lote-efdreinf-ocorrencias/api/(?P<pk>[0-9]+)/$',
            transmissor_lote_efdreinf_ocorrencias_views.TransmissorLoteEfdreinfOcorrenciasDetail.as_view() ),

url(r'^transmissor-lote-efdreinf-ocorrencias/listar/(?P<hash>.*)/$', 
        transmissor_lote_efdreinf_ocorrencias_views.listar, 
        name='transmissor_lote_efdreinf_ocorrencias'),

url(r'^transmissor-lote-efdreinf-ocorrencias/salvar/(?P<hash>.*)/$', 
        transmissor_lote_efdreinf_ocorrencias_views.salvar, 
        name='transmissor_lote_efdreinf_ocorrencias_salvar'),



url(r'^arquivos/apagar/(?P<hash>.*)/$', 
        arquivos_views.apagar, 
        name='arquivos_apagar'),

url(r'^arquivos/api/$',
            arquivos_views.ArquivosList.as_view() ),

        url(r'^arquivos/api/(?P<pk>[0-9]+)/$',
            arquivos_views.ArquivosDetail.as_view() ),

url(r'^arquivos/listar/(?P<hash>.*)/$', 
        arquivos_views.listar, 
        name='arquivos'),

url(r'^arquivos/salvar/(?P<hash>.*)/$', 
        arquivos_views.salvar, 
        name='arquivos_salvar'),



url(r'^retornos-eventos/apagar/(?P<hash>.*)/$', 
        retornos_eventos_views.apagar, 
        name='retornos_eventos_apagar'),

url(r'^retornos-eventos/api/$',
            retornos_eventos_views.RetornosEventosList.as_view() ),

        url(r'^retornos-eventos/api/(?P<pk>[0-9]+)/$',
            retornos_eventos_views.RetornosEventosDetail.as_view() ),

url(r'^retornos-eventos/listar/(?P<hash>.*)/$', 
        retornos_eventos_views.listar, 
        name='retornos_eventos'),

url(r'^retornos-eventos/salvar/(?P<hash>.*)/$', 
        retornos_eventos_views.salvar, 
        name='retornos_eventos_salvar'),



url(r'^retornos-eventos-ocorrencias/apagar/(?P<hash>.*)/$', 
        retornos_eventos_ocorrencias_views.apagar, 
        name='retornos_eventos_ocorrencias_apagar'),

url(r'^retornos-eventos-ocorrencias/api/$',
            retornos_eventos_ocorrencias_views.RetornosEventosOcorrenciasList.as_view() ),

        url(r'^retornos-eventos-ocorrencias/api/(?P<pk>[0-9]+)/$',
            retornos_eventos_ocorrencias_views.RetornosEventosOcorrenciasDetail.as_view() ),

url(r'^retornos-eventos-ocorrencias/listar/(?P<hash>.*)/$', 
        retornos_eventos_ocorrencias_views.listar, 
        name='retornos_eventos_ocorrencias'),

url(r'^retornos-eventos-ocorrencias/salvar/(?P<hash>.*)/$', 
        retornos_eventos_ocorrencias_views.salvar, 
        name='retornos_eventos_ocorrencias_salvar'),



url(r'^retornos-eventos-horarios/apagar/(?P<hash>.*)/$', 
        retornos_eventos_horarios_views.apagar, 
        name='retornos_eventos_horarios_apagar'),

url(r'^retornos-eventos-horarios/api/$',
            retornos_eventos_horarios_views.RetornosEventosHorariosList.as_view() ),

        url(r'^retornos-eventos-horarios/api/(?P<pk>[0-9]+)/$',
            retornos_eventos_horarios_views.RetornosEventosHorariosDetail.as_view() ),

url(r'^retornos-eventos-horarios/listar/(?P<hash>.*)/$', 
        retornos_eventos_horarios_views.listar, 
        name='retornos_eventos_horarios'),

url(r'^retornos-eventos-horarios/salvar/(?P<hash>.*)/$', 
        retornos_eventos_horarios_views.salvar, 
        name='retornos_eventos_horarios_salvar'),



url(r'^retornos-eventos-intervalos/apagar/(?P<hash>.*)/$', 
        retornos_eventos_intervalos_views.apagar, 
        name='retornos_eventos_intervalos_apagar'),

url(r'^retornos-eventos-intervalos/api/$',
            retornos_eventos_intervalos_views.RetornosEventosIntervalosList.as_view() ),

        url(r'^retornos-eventos-intervalos/api/(?P<pk>[0-9]+)/$',
            retornos_eventos_intervalos_views.RetornosEventosIntervalosDetail.as_view() ),

url(r'^retornos-eventos-intervalos/listar/(?P<hash>.*)/$', 
        retornos_eventos_intervalos_views.listar, 
        name='retornos_eventos_intervalos'),

url(r'^retornos-eventos-intervalos/salvar/(?P<hash>.*)/$', 
        retornos_eventos_intervalos_views.salvar, 
        name='retornos_eventos_intervalos_salvar'),





]