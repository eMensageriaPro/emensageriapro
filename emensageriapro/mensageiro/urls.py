#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns = patterns('',
    # Examples:

url(r'^validacao-automatica/$',
        'emensageriapro.mensageiro.views.automatizacao.scripts_validacao_automatica',
        name='scripts_validacao_automatica'),

url(r'^transmissao-automatica/$',
        'emensageriapro.mensageiro.views.automatizacao.scripts_transmissao_automatica',
        name='scripts_transmissao_automatica'),

url(r'^scripts/enviar-lote-esocial/(?P<chave>.*)/(?P<transmissor_lote_esocial_id>\d+)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_esocial_comunicacao.scripts_enviar_lote',
        name='scripts_enviar_esocial_lote'),

url(r'^scripts/consultar-lote-esocial/(?P<chave>.*)/(?P<transmissor_lote_esocial_id>\d+)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_esocial_comunicacao.scripts_consultar_lote',
        name='scripts_consultar_esocial_lote'),

url(r'^transmissor-lote-esocial/enviar/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_esocial_comunicacao.enviar',
        name='transmissor_lote_esocial_enviar'),

url(r'^transmissor-lote-esocial/consultar/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_esocial_comunicacao.consultar',
        name='transmissor_lote_esocial_consultar'),
        
        
url(r'^transmissor-lote-esocial/recibo/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_esocial_comunicacao.recibo',
        name='transmissor_lote_esocial_recibo'),

url(r'^importacoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.importacoes.listar', 
        name='importacoes'),

url(r'^mapa-processamento/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.mapa_processamento.listar',
        name='mapa_processamento'),

url(r'^transmissor-eventos-esocial/vincular/(?P<hash>.+)/$',
        'emensageriapro.mensageiro.views.transmissor_esocial.vincular_eventos_esocial',
        name='vincular_eventos_esocial'),
        
url(r'^transmissor-eventos-esocial/desvincular/(?P<hash>.+)/$',
        'emensageriapro.mensageiro.views.transmissor_esocial.desvincular_eventos_esocial',
        name='desvincular_eventos_esocial'),

url(r'^recuperacao-de-arquivos/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.arquivos_recuperacao.arquivos_recuperacao', 
        name='arquivos_recuperacao'),

url(r'^reprocessar-arquivos/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.arquivos_recuperacao.arquivos_reprocessar',
        name='arquivos_reprocessar'),
        
url(r'^visualizacao-de-arquivos/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.arquivos_recuperacao.arquivos_visualizacao',
        name='arquivos_visualizacao'),

url(r'^scripts/enviar-lote-efdreinf/(?P<chave>.*)/(?P<transmissor_lote_efdreinf_id>\d+)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf_comunicacao.scripts_enviar_lote',
        name='scripts_enviar_efdreinf_lote'),

url(r'^scripts/consultar-lote-efdreinf/(?P<chave>.*)/(?P<transmissor_lote_efdreinf_id>\d+)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf_comunicacao.scripts_consultar_lote',
        name='scripts_consultar_efdreinf_lote'),

url(r'^transmissor-lote-efdreinf/enviar/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf_comunicacao.enviar',
        name='transmissor_lote_efdreinf_enviar'),

url(r'^transmissor-lote-efdreinf/consultar/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf_comunicacao.consultar',
        name='transmissor_lote_efdreinf_consultar'),
        
        
url(r'^transmissor-lote-efdreinf/recibo/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf_comunicacao.recibo',
        name='transmissor_lote_efdreinf_recibo'),

url(r'^relatorios/imprimir/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.relatorios_imprimir.imprimir',
        name='relatorios_imprimir'),

url(r'^processar-arquivos/$',
        'emensageriapro.mensageiro.views.processar_arquivos.scripts_processar_arquivos',
        name='scripts_processar_arquivos'),

url(r'^importacoes-imprimir/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.processar_arquivos.imprimir',
        name='processar_arquivos_imprimir'),
        

url(r'^processar-arquivos-salvar/(?P<hash>.*)/$',
        'emensageriapro.mensageiro.views.processar_arquivos.scripts_salvar_arquivos',
        name='scripts_salvar_arquivos'),

url(r'^transmissor-eventos-efdreinf/vincular/(?P<hash>.+)/$',
        'emensageriapro.mensageiro.views.transmissor_efdreinf.vincular_eventos_efdreinf',
        name='vincular_eventos_efdreinf'),
        
url(r'^transmissor-eventos-efdreinf/desvincular/(?P<hash>.+)/$',
        'emensageriapro.mensageiro.views.transmissor_efdreinf.desvincular_eventos_efdreinf',
        name='desvincular_eventos_efdreinf'),









url(r'^relatorios/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.relatorios.apagar', 
        name='relatorios_apagar'),

url(r'^relatorios/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.relatorios.listar', 
        name='relatorios'),

url(r'^relatorios/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.relatorios.salvar', 
        name='relatorios_salvar'),



url(r'^transmissores/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissores.apagar', 
        name='transmissores_apagar'),

url(r'^transmissores/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissores.listar', 
        name='transmissores'),

url(r'^transmissores/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissores.salvar', 
        name='transmissores_salvar'),



url(r'^regras-validacao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.regras_validacao.apagar', 
        name='regras_validacao_apagar'),

url(r'^regras-validacao/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.regras_validacao.listar', 
        name='regras_validacao'),

url(r'^regras-validacao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.regras_validacao.salvar', 
        name='regras_validacao_salvar'),



url(r'^importacao-arquivos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.importacao_arquivos.apagar', 
        name='importacao_arquivos_apagar'),

url(r'^importacao-arquivos/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.importacao_arquivos.listar', 
        name='importacao_arquivos'),

url(r'^importacao-arquivos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.importacao_arquivos.salvar', 
        name='importacao_arquivos_salvar'),



url(r'^importacao-arquivos-eventos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.importacao_arquivos_eventos.apagar', 
        name='importacao_arquivos_eventos_apagar'),

url(r'^importacao-arquivos-eventos/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.importacao_arquivos_eventos.listar', 
        name='importacao_arquivos_eventos'),

url(r'^importacao-arquivos-eventos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.importacao_arquivos_eventos.salvar', 
        name='importacao_arquivos_eventos_salvar'),



url(r'^transmissor-lote-esocial/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_esocial.apagar', 
        name='transmissor_lote_esocial_apagar'),

url(r'^transmissor-lote-esocial/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_esocial.listar', 
        name='transmissor_lote_esocial'),

url(r'^transmissor-lote-esocial/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_esocial.salvar', 
        name='transmissor_lote_esocial_salvar'),



url(r'^transmissor-lote-esocial-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_esocial_ocorrencias.apagar', 
        name='transmissor_lote_esocial_ocorrencias_apagar'),

url(r'^transmissor-lote-esocial-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_esocial_ocorrencias.listar', 
        name='transmissor_lote_esocial_ocorrencias'),

url(r'^transmissor-lote-esocial-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_esocial_ocorrencias.salvar', 
        name='transmissor_lote_esocial_ocorrencias_salvar'),

)


urlpatterns += patterns('',


url(r'^transmissor-lote-efdreinf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf.apagar', 
        name='transmissor_lote_efdreinf_apagar'),

url(r'^transmissor-lote-efdreinf/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf.listar', 
        name='transmissor_lote_efdreinf'),

url(r'^transmissor-lote-efdreinf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf.salvar', 
        name='transmissor_lote_efdreinf_salvar'),



url(r'^transmissor-lote-efdreinf-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf_ocorrencias.apagar', 
        name='transmissor_lote_efdreinf_ocorrencias_apagar'),

url(r'^transmissor-lote-efdreinf-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf_ocorrencias.listar', 
        name='transmissor_lote_efdreinf_ocorrencias'),

url(r'^transmissor-lote-efdreinf-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.transmissor_lote_efdreinf_ocorrencias.salvar', 
        name='transmissor_lote_efdreinf_ocorrencias_salvar'),



url(r'^arquivos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.arquivos.apagar', 
        name='arquivos_apagar'),

url(r'^arquivos/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.arquivos.listar', 
        name='arquivos'),

url(r'^arquivos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.arquivos.salvar', 
        name='arquivos_salvar'),



url(r'^retornos-eventos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos.apagar', 
        name='retornos_eventos_apagar'),

url(r'^retornos-eventos/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos.listar', 
        name='retornos_eventos'),

url(r'^retornos-eventos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos.salvar', 
        name='retornos_eventos_salvar'),



url(r'^retornos-eventos-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos_ocorrencias.apagar', 
        name='retornos_eventos_ocorrencias_apagar'),

url(r'^retornos-eventos-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos_ocorrencias.listar', 
        name='retornos_eventos_ocorrencias'),

url(r'^retornos-eventos-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos_ocorrencias.salvar', 
        name='retornos_eventos_ocorrencias_salvar'),



url(r'^retornos-eventos-horarios/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos_horarios.apagar', 
        name='retornos_eventos_horarios_apagar'),

url(r'^retornos-eventos-horarios/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos_horarios.listar', 
        name='retornos_eventos_horarios'),

url(r'^retornos-eventos-horarios/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos_horarios.salvar', 
        name='retornos_eventos_horarios_salvar'),



url(r'^retornos-eventos-intervalos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos_intervalos.apagar', 
        name='retornos_eventos_intervalos_apagar'),

url(r'^retornos-eventos-intervalos/listar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos_intervalos.listar', 
        name='retornos_eventos_intervalos'),

url(r'^retornos-eventos-intervalos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.mensageiro.views.retornos_eventos_intervalos.salvar', 
        name='retornos_eventos_intervalos_salvar'),





)