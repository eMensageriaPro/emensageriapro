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



url(r'^s1000-evtinfoempregador/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1000_evtinfoempregador.apagar', 
        name='s1000_evtinfoempregador_apagar'),

url(r'^s1000-evtinfoempregador/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1000_evtinfoempregador.listar', 
        name='s1000_evtinfoempregador'),
        
url(r'^s1000-evtinfoempregador/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1000_evtinfoempregador_verificar.verificar', 
        name='s1000_evtinfoempregador_verificar'),
        
url(r'^s1000-evtinfoempregador/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1000_evtinfoempregador_verificar.recibo', 
        name='s1000_evtinfoempregador_recibo'),
        
        
url(r'^s1000-evtinfoempregador/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1000_evtinfoempregador_verificar.duplicar',
        name='s1000_evtinfoempregador_duplicar'),

url(r'^s1000-evtinfoempregador/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1000_evtinfoempregador_verificar.criar_alteracao',
        name='s1000_evtinfoempregador_criar_alteracao'),

url(r'^s1000-evtinfoempregador/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1000_evtinfoempregador_verificar.criar_exclusao',
        name='s1000_evtinfoempregador_criar_exclusao'),
        
url(r'^s1000-evtinfoempregador/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1000_evtinfoempregador_verificar.gerar_xml', 
                name='s1000_evtinfoempregador_xml'),
                

url(r'^s1000-evtinfoempregador/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1000_evtinfoempregador_verificar.alterar_identidade',
        name='s1000_evtinfoempregador_alterar_identidade'),

url(r'^s1000-evtinfoempregador/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1000_evtinfoempregador_verificar.abrir_evento_para_edicao',
        name='s1000_evtinfoempregador_abrir_evento_para_edicao'),

url(r'^s1000-evtinfoempregador/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1000_evtinfoempregador_verificar.validar_evento',
        name='s1000_evtinfoempregador_validar_evento'),

url(r'^s1000-evtinfoempregador/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1000_evtinfoempregador.salvar', 
        name='s1000_evtinfoempregador_salvar'),
        

url(r'^scripts/gerar-identidade/s1000-evtinfoempregador/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1000_evtinfoempregador.gerar_identidade', 
        name='s1000_evtinfoempregador_gerar_identidade'),



url(r'^s1005-evttabestab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1005_evttabestab.apagar', 
        name='s1005_evttabestab_apagar'),

url(r'^s1005-evttabestab/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1005_evttabestab.listar', 
        name='s1005_evttabestab'),
        
url(r'^s1005-evttabestab/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1005_evttabestab_verificar.verificar', 
        name='s1005_evttabestab_verificar'),
        
url(r'^s1005-evttabestab/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1005_evttabestab_verificar.recibo', 
        name='s1005_evttabestab_recibo'),
        
        
url(r'^s1005-evttabestab/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1005_evttabestab_verificar.duplicar',
        name='s1005_evttabestab_duplicar'),

url(r'^s1005-evttabestab/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1005_evttabestab_verificar.criar_alteracao',
        name='s1005_evttabestab_criar_alteracao'),

url(r'^s1005-evttabestab/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1005_evttabestab_verificar.criar_exclusao',
        name='s1005_evttabestab_criar_exclusao'),
        
url(r'^s1005-evttabestab/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1005_evttabestab_verificar.gerar_xml', 
                name='s1005_evttabestab_xml'),
                

url(r'^s1005-evttabestab/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1005_evttabestab_verificar.alterar_identidade',
        name='s1005_evttabestab_alterar_identidade'),

url(r'^s1005-evttabestab/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1005_evttabestab_verificar.abrir_evento_para_edicao',
        name='s1005_evttabestab_abrir_evento_para_edicao'),

url(r'^s1005-evttabestab/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1005_evttabestab_verificar.validar_evento',
        name='s1005_evttabestab_validar_evento'),

url(r'^s1005-evttabestab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1005_evttabestab.salvar', 
        name='s1005_evttabestab_salvar'),
        

url(r'^scripts/gerar-identidade/s1005-evttabestab/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1005_evttabestab.gerar_identidade', 
        name='s1005_evttabestab_gerar_identidade'),



url(r'^s1010-evttabrubrica/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1010_evttabrubrica.apagar', 
        name='s1010_evttabrubrica_apagar'),

url(r'^s1010-evttabrubrica/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1010_evttabrubrica.listar', 
        name='s1010_evttabrubrica'),
        
url(r'^s1010-evttabrubrica/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1010_evttabrubrica_verificar.verificar', 
        name='s1010_evttabrubrica_verificar'),
        
url(r'^s1010-evttabrubrica/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1010_evttabrubrica_verificar.recibo', 
        name='s1010_evttabrubrica_recibo'),
        
        
url(r'^s1010-evttabrubrica/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1010_evttabrubrica_verificar.duplicar',
        name='s1010_evttabrubrica_duplicar'),

url(r'^s1010-evttabrubrica/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1010_evttabrubrica_verificar.criar_alteracao',
        name='s1010_evttabrubrica_criar_alteracao'),

url(r'^s1010-evttabrubrica/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1010_evttabrubrica_verificar.criar_exclusao',
        name='s1010_evttabrubrica_criar_exclusao'),
        
url(r'^s1010-evttabrubrica/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1010_evttabrubrica_verificar.gerar_xml', 
                name='s1010_evttabrubrica_xml'),
                

url(r'^s1010-evttabrubrica/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1010_evttabrubrica_verificar.alterar_identidade',
        name='s1010_evttabrubrica_alterar_identidade'),

url(r'^s1010-evttabrubrica/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1010_evttabrubrica_verificar.abrir_evento_para_edicao',
        name='s1010_evttabrubrica_abrir_evento_para_edicao'),

url(r'^s1010-evttabrubrica/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1010_evttabrubrica_verificar.validar_evento',
        name='s1010_evttabrubrica_validar_evento'),

url(r'^s1010-evttabrubrica/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1010_evttabrubrica.salvar', 
        name='s1010_evttabrubrica_salvar'),
        

url(r'^scripts/gerar-identidade/s1010-evttabrubrica/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1010_evttabrubrica.gerar_identidade', 
        name='s1010_evttabrubrica_gerar_identidade'),



url(r'^s1020-evttablotacao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1020_evttablotacao.apagar', 
        name='s1020_evttablotacao_apagar'),

url(r'^s1020-evttablotacao/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1020_evttablotacao.listar', 
        name='s1020_evttablotacao'),
        
url(r'^s1020-evttablotacao/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1020_evttablotacao_verificar.verificar', 
        name='s1020_evttablotacao_verificar'),
        
url(r'^s1020-evttablotacao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1020_evttablotacao_verificar.recibo', 
        name='s1020_evttablotacao_recibo'),
        
        
url(r'^s1020-evttablotacao/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1020_evttablotacao_verificar.duplicar',
        name='s1020_evttablotacao_duplicar'),

url(r'^s1020-evttablotacao/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1020_evttablotacao_verificar.criar_alteracao',
        name='s1020_evttablotacao_criar_alteracao'),

url(r'^s1020-evttablotacao/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1020_evttablotacao_verificar.criar_exclusao',
        name='s1020_evttablotacao_criar_exclusao'),
        
url(r'^s1020-evttablotacao/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1020_evttablotacao_verificar.gerar_xml', 
                name='s1020_evttablotacao_xml'),
                

url(r'^s1020-evttablotacao/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1020_evttablotacao_verificar.alterar_identidade',
        name='s1020_evttablotacao_alterar_identidade'),

url(r'^s1020-evttablotacao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1020_evttablotacao_verificar.abrir_evento_para_edicao',
        name='s1020_evttablotacao_abrir_evento_para_edicao'),

url(r'^s1020-evttablotacao/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1020_evttablotacao_verificar.validar_evento',
        name='s1020_evttablotacao_validar_evento'),

url(r'^s1020-evttablotacao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1020_evttablotacao.salvar', 
        name='s1020_evttablotacao_salvar'),
        

url(r'^scripts/gerar-identidade/s1020-evttablotacao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1020_evttablotacao.gerar_identidade', 
        name='s1020_evttablotacao_gerar_identidade'),



url(r'^s1030-evttabcargo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1030_evttabcargo.apagar', 
        name='s1030_evttabcargo_apagar'),

url(r'^s1030-evttabcargo/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1030_evttabcargo.listar', 
        name='s1030_evttabcargo'),
        
url(r'^s1030-evttabcargo/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1030_evttabcargo_verificar.verificar', 
        name='s1030_evttabcargo_verificar'),
        
url(r'^s1030-evttabcargo/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1030_evttabcargo_verificar.recibo', 
        name='s1030_evttabcargo_recibo'),
        
        
url(r'^s1030-evttabcargo/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1030_evttabcargo_verificar.duplicar',
        name='s1030_evttabcargo_duplicar'),

url(r'^s1030-evttabcargo/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1030_evttabcargo_verificar.criar_alteracao',
        name='s1030_evttabcargo_criar_alteracao'),

url(r'^s1030-evttabcargo/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1030_evttabcargo_verificar.criar_exclusao',
        name='s1030_evttabcargo_criar_exclusao'),
        
url(r'^s1030-evttabcargo/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1030_evttabcargo_verificar.gerar_xml', 
                name='s1030_evttabcargo_xml'),
                

url(r'^s1030-evttabcargo/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1030_evttabcargo_verificar.alterar_identidade',
        name='s1030_evttabcargo_alterar_identidade'),

url(r'^s1030-evttabcargo/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1030_evttabcargo_verificar.abrir_evento_para_edicao',
        name='s1030_evttabcargo_abrir_evento_para_edicao'),

url(r'^s1030-evttabcargo/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1030_evttabcargo_verificar.validar_evento',
        name='s1030_evttabcargo_validar_evento'),

url(r'^s1030-evttabcargo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1030_evttabcargo.salvar', 
        name='s1030_evttabcargo_salvar'),
        

url(r'^scripts/gerar-identidade/s1030-evttabcargo/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1030_evttabcargo.gerar_identidade', 
        name='s1030_evttabcargo_gerar_identidade'),



url(r'^s1035-evttabcarreira/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1035_evttabcarreira.apagar', 
        name='s1035_evttabcarreira_apagar'),

url(r'^s1035-evttabcarreira/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1035_evttabcarreira.listar', 
        name='s1035_evttabcarreira'),
        
url(r'^s1035-evttabcarreira/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1035_evttabcarreira_verificar.verificar', 
        name='s1035_evttabcarreira_verificar'),
        
url(r'^s1035-evttabcarreira/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1035_evttabcarreira_verificar.recibo', 
        name='s1035_evttabcarreira_recibo'),
        
        
url(r'^s1035-evttabcarreira/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1035_evttabcarreira_verificar.duplicar',
        name='s1035_evttabcarreira_duplicar'),

url(r'^s1035-evttabcarreira/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1035_evttabcarreira_verificar.criar_alteracao',
        name='s1035_evttabcarreira_criar_alteracao'),

url(r'^s1035-evttabcarreira/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1035_evttabcarreira_verificar.criar_exclusao',
        name='s1035_evttabcarreira_criar_exclusao'),
        
url(r'^s1035-evttabcarreira/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1035_evttabcarreira_verificar.gerar_xml', 
                name='s1035_evttabcarreira_xml'),
                

url(r'^s1035-evttabcarreira/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1035_evttabcarreira_verificar.alterar_identidade',
        name='s1035_evttabcarreira_alterar_identidade'),

url(r'^s1035-evttabcarreira/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1035_evttabcarreira_verificar.abrir_evento_para_edicao',
        name='s1035_evttabcarreira_abrir_evento_para_edicao'),

url(r'^s1035-evttabcarreira/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1035_evttabcarreira_verificar.validar_evento',
        name='s1035_evttabcarreira_validar_evento'),

url(r'^s1035-evttabcarreira/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1035_evttabcarreira.salvar', 
        name='s1035_evttabcarreira_salvar'),
        

url(r'^scripts/gerar-identidade/s1035-evttabcarreira/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1035_evttabcarreira.gerar_identidade', 
        name='s1035_evttabcarreira_gerar_identidade'),



url(r'^s1040-evttabfuncao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1040_evttabfuncao.apagar', 
        name='s1040_evttabfuncao_apagar'),

url(r'^s1040-evttabfuncao/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1040_evttabfuncao.listar', 
        name='s1040_evttabfuncao'),
        
url(r'^s1040-evttabfuncao/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1040_evttabfuncao_verificar.verificar', 
        name='s1040_evttabfuncao_verificar'),
        
url(r'^s1040-evttabfuncao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1040_evttabfuncao_verificar.recibo', 
        name='s1040_evttabfuncao_recibo'),
        
        
url(r'^s1040-evttabfuncao/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1040_evttabfuncao_verificar.duplicar',
        name='s1040_evttabfuncao_duplicar'),

url(r'^s1040-evttabfuncao/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1040_evttabfuncao_verificar.criar_alteracao',
        name='s1040_evttabfuncao_criar_alteracao'),

url(r'^s1040-evttabfuncao/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1040_evttabfuncao_verificar.criar_exclusao',
        name='s1040_evttabfuncao_criar_exclusao'),
        
url(r'^s1040-evttabfuncao/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1040_evttabfuncao_verificar.gerar_xml', 
                name='s1040_evttabfuncao_xml'),
                

url(r'^s1040-evttabfuncao/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1040_evttabfuncao_verificar.alterar_identidade',
        name='s1040_evttabfuncao_alterar_identidade'),

url(r'^s1040-evttabfuncao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1040_evttabfuncao_verificar.abrir_evento_para_edicao',
        name='s1040_evttabfuncao_abrir_evento_para_edicao'),

url(r'^s1040-evttabfuncao/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1040_evttabfuncao_verificar.validar_evento',
        name='s1040_evttabfuncao_validar_evento'),

url(r'^s1040-evttabfuncao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1040_evttabfuncao.salvar', 
        name='s1040_evttabfuncao_salvar'),
        

url(r'^scripts/gerar-identidade/s1040-evttabfuncao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1040_evttabfuncao.gerar_identidade', 
        name='s1040_evttabfuncao_gerar_identidade'),



url(r'^s1050-evttabhortur/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1050_evttabhortur.apagar', 
        name='s1050_evttabhortur_apagar'),

url(r'^s1050-evttabhortur/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1050_evttabhortur.listar', 
        name='s1050_evttabhortur'),
        
url(r'^s1050-evttabhortur/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1050_evttabhortur_verificar.verificar', 
        name='s1050_evttabhortur_verificar'),
        
url(r'^s1050-evttabhortur/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1050_evttabhortur_verificar.recibo', 
        name='s1050_evttabhortur_recibo'),
        
        
url(r'^s1050-evttabhortur/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1050_evttabhortur_verificar.duplicar',
        name='s1050_evttabhortur_duplicar'),

url(r'^s1050-evttabhortur/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1050_evttabhortur_verificar.criar_alteracao',
        name='s1050_evttabhortur_criar_alteracao'),

url(r'^s1050-evttabhortur/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1050_evttabhortur_verificar.criar_exclusao',
        name='s1050_evttabhortur_criar_exclusao'),
        
url(r'^s1050-evttabhortur/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1050_evttabhortur_verificar.gerar_xml', 
                name='s1050_evttabhortur_xml'),
                

url(r'^s1050-evttabhortur/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1050_evttabhortur_verificar.alterar_identidade',
        name='s1050_evttabhortur_alterar_identidade'),

url(r'^s1050-evttabhortur/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1050_evttabhortur_verificar.abrir_evento_para_edicao',
        name='s1050_evttabhortur_abrir_evento_para_edicao'),

url(r'^s1050-evttabhortur/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1050_evttabhortur_verificar.validar_evento',
        name='s1050_evttabhortur_validar_evento'),

url(r'^s1050-evttabhortur/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1050_evttabhortur.salvar', 
        name='s1050_evttabhortur_salvar'),
        

url(r'^scripts/gerar-identidade/s1050-evttabhortur/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1050_evttabhortur.gerar_identidade', 
        name='s1050_evttabhortur_gerar_identidade'),



url(r'^s1060-evttabambiente/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1060_evttabambiente.apagar', 
        name='s1060_evttabambiente_apagar'),

url(r'^s1060-evttabambiente/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1060_evttabambiente.listar', 
        name='s1060_evttabambiente'),
        
url(r'^s1060-evttabambiente/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1060_evttabambiente_verificar.verificar', 
        name='s1060_evttabambiente_verificar'),
        
url(r'^s1060-evttabambiente/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1060_evttabambiente_verificar.recibo', 
        name='s1060_evttabambiente_recibo'),
        
        
url(r'^s1060-evttabambiente/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1060_evttabambiente_verificar.duplicar',
        name='s1060_evttabambiente_duplicar'),

url(r'^s1060-evttabambiente/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1060_evttabambiente_verificar.criar_alteracao',
        name='s1060_evttabambiente_criar_alteracao'),

url(r'^s1060-evttabambiente/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1060_evttabambiente_verificar.criar_exclusao',
        name='s1060_evttabambiente_criar_exclusao'),
        
url(r'^s1060-evttabambiente/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1060_evttabambiente_verificar.gerar_xml', 
                name='s1060_evttabambiente_xml'),
                

url(r'^s1060-evttabambiente/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1060_evttabambiente_verificar.alterar_identidade',
        name='s1060_evttabambiente_alterar_identidade'),

url(r'^s1060-evttabambiente/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1060_evttabambiente_verificar.abrir_evento_para_edicao',
        name='s1060_evttabambiente_abrir_evento_para_edicao'),

url(r'^s1060-evttabambiente/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1060_evttabambiente_verificar.validar_evento',
        name='s1060_evttabambiente_validar_evento'),

url(r'^s1060-evttabambiente/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1060_evttabambiente.salvar', 
        name='s1060_evttabambiente_salvar'),
        

url(r'^scripts/gerar-identidade/s1060-evttabambiente/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1060_evttabambiente.gerar_identidade', 
        name='s1060_evttabambiente_gerar_identidade'),



url(r'^s1065-evttabequipamento/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1065_evttabequipamento.apagar', 
        name='s1065_evttabequipamento_apagar'),

url(r'^s1065-evttabequipamento/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1065_evttabequipamento.listar', 
        name='s1065_evttabequipamento'),
        
url(r'^s1065-evttabequipamento/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1065_evttabequipamento_verificar.verificar', 
        name='s1065_evttabequipamento_verificar'),
        
url(r'^s1065-evttabequipamento/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1065_evttabequipamento_verificar.recibo', 
        name='s1065_evttabequipamento_recibo'),
        
        
url(r'^s1065-evttabequipamento/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1065_evttabequipamento_verificar.duplicar',
        name='s1065_evttabequipamento_duplicar'),

url(r'^s1065-evttabequipamento/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1065_evttabequipamento_verificar.criar_alteracao',
        name='s1065_evttabequipamento_criar_alteracao'),

url(r'^s1065-evttabequipamento/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1065_evttabequipamento_verificar.criar_exclusao',
        name='s1065_evttabequipamento_criar_exclusao'),
        
url(r'^s1065-evttabequipamento/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1065_evttabequipamento_verificar.gerar_xml', 
                name='s1065_evttabequipamento_xml'),
                

url(r'^s1065-evttabequipamento/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1065_evttabequipamento_verificar.alterar_identidade',
        name='s1065_evttabequipamento_alterar_identidade'),

url(r'^s1065-evttabequipamento/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1065_evttabequipamento_verificar.abrir_evento_para_edicao',
        name='s1065_evttabequipamento_abrir_evento_para_edicao'),

url(r'^s1065-evttabequipamento/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1065_evttabequipamento_verificar.validar_evento',
        name='s1065_evttabequipamento_validar_evento'),

url(r'^s1065-evttabequipamento/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1065_evttabequipamento.salvar', 
        name='s1065_evttabequipamento_salvar'),
        

url(r'^scripts/gerar-identidade/s1065-evttabequipamento/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1065_evttabequipamento.gerar_identidade', 
        name='s1065_evttabequipamento_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^s1070-evttabprocesso/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1070_evttabprocesso.apagar', 
        name='s1070_evttabprocesso_apagar'),

url(r'^s1070-evttabprocesso/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1070_evttabprocesso.listar', 
        name='s1070_evttabprocesso'),
        
url(r'^s1070-evttabprocesso/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1070_evttabprocesso_verificar.verificar', 
        name='s1070_evttabprocesso_verificar'),
        
url(r'^s1070-evttabprocesso/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1070_evttabprocesso_verificar.recibo', 
        name='s1070_evttabprocesso_recibo'),
        
        
url(r'^s1070-evttabprocesso/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1070_evttabprocesso_verificar.duplicar',
        name='s1070_evttabprocesso_duplicar'),

url(r'^s1070-evttabprocesso/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1070_evttabprocesso_verificar.criar_alteracao',
        name='s1070_evttabprocesso_criar_alteracao'),

url(r'^s1070-evttabprocesso/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1070_evttabprocesso_verificar.criar_exclusao',
        name='s1070_evttabprocesso_criar_exclusao'),
        
url(r'^s1070-evttabprocesso/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1070_evttabprocesso_verificar.gerar_xml', 
                name='s1070_evttabprocesso_xml'),
                

url(r'^s1070-evttabprocesso/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1070_evttabprocesso_verificar.alterar_identidade',
        name='s1070_evttabprocesso_alterar_identidade'),

url(r'^s1070-evttabprocesso/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1070_evttabprocesso_verificar.abrir_evento_para_edicao',
        name='s1070_evttabprocesso_abrir_evento_para_edicao'),

url(r'^s1070-evttabprocesso/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1070_evttabprocesso_verificar.validar_evento',
        name='s1070_evttabprocesso_validar_evento'),

url(r'^s1070-evttabprocesso/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1070_evttabprocesso.salvar', 
        name='s1070_evttabprocesso_salvar'),
        

url(r'^scripts/gerar-identidade/s1070-evttabprocesso/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1070_evttabprocesso.gerar_identidade', 
        name='s1070_evttabprocesso_gerar_identidade'),



url(r'^s1080-evttaboperport/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1080_evttaboperport.apagar', 
        name='s1080_evttaboperport_apagar'),

url(r'^s1080-evttaboperport/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1080_evttaboperport.listar', 
        name='s1080_evttaboperport'),
        
url(r'^s1080-evttaboperport/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1080_evttaboperport_verificar.verificar', 
        name='s1080_evttaboperport_verificar'),
        
url(r'^s1080-evttaboperport/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1080_evttaboperport_verificar.recibo', 
        name='s1080_evttaboperport_recibo'),
        
        
url(r'^s1080-evttaboperport/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1080_evttaboperport_verificar.duplicar',
        name='s1080_evttaboperport_duplicar'),

url(r'^s1080-evttaboperport/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1080_evttaboperport_verificar.criar_alteracao',
        name='s1080_evttaboperport_criar_alteracao'),

url(r'^s1080-evttaboperport/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1080_evttaboperport_verificar.criar_exclusao',
        name='s1080_evttaboperport_criar_exclusao'),
        
url(r'^s1080-evttaboperport/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1080_evttaboperport_verificar.gerar_xml', 
                name='s1080_evttaboperport_xml'),
                

url(r'^s1080-evttaboperport/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1080_evttaboperport_verificar.alterar_identidade',
        name='s1080_evttaboperport_alterar_identidade'),

url(r'^s1080-evttaboperport/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1080_evttaboperport_verificar.abrir_evento_para_edicao',
        name='s1080_evttaboperport_abrir_evento_para_edicao'),

url(r'^s1080-evttaboperport/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1080_evttaboperport_verificar.validar_evento',
        name='s1080_evttaboperport_validar_evento'),

url(r'^s1080-evttaboperport/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1080_evttaboperport.salvar', 
        name='s1080_evttaboperport_salvar'),
        

url(r'^scripts/gerar-identidade/s1080-evttaboperport/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1080_evttaboperport.gerar_identidade', 
        name='s1080_evttaboperport_gerar_identidade'),



url(r'^s1200-evtremun/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1200_evtremun.apagar', 
        name='s1200_evtremun_apagar'),

url(r'^s1200-evtremun/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1200_evtremun.listar', 
        name='s1200_evtremun'),
        
url(r'^s1200-evtremun/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1200_evtremun_verificar.verificar', 
        name='s1200_evtremun_verificar'),
        
url(r'^s1200-evtremun/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1200_evtremun_verificar.recibo', 
        name='s1200_evtremun_recibo'),
        
        
url(r'^s1200-evtremun/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1200_evtremun_verificar.duplicar',
        name='s1200_evtremun_duplicar'),

url(r'^s1200-evtremun/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1200_evtremun_verificar.criar_alteracao',
        name='s1200_evtremun_criar_alteracao'),

url(r'^s1200-evtremun/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1200_evtremun_verificar.criar_exclusao',
        name='s1200_evtremun_criar_exclusao'),
        
url(r'^s1200-evtremun/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1200_evtremun_verificar.gerar_xml', 
                name='s1200_evtremun_xml'),
                

url(r'^s1200-evtremun/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1200_evtremun_verificar.alterar_identidade',
        name='s1200_evtremun_alterar_identidade'),

url(r'^s1200-evtremun/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1200_evtremun_verificar.abrir_evento_para_edicao',
        name='s1200_evtremun_abrir_evento_para_edicao'),

url(r'^s1200-evtremun/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1200_evtremun_verificar.validar_evento',
        name='s1200_evtremun_validar_evento'),

url(r'^s1200-evtremun/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1200_evtremun.salvar', 
        name='s1200_evtremun_salvar'),
        

url(r'^scripts/gerar-identidade/s1200-evtremun/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1200_evtremun.gerar_identidade', 
        name='s1200_evtremun_gerar_identidade'),



url(r'^s1202-evtrmnrpps/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1202_evtrmnrpps.apagar', 
        name='s1202_evtrmnrpps_apagar'),

url(r'^s1202-evtrmnrpps/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1202_evtrmnrpps.listar', 
        name='s1202_evtrmnrpps'),
        
url(r'^s1202-evtrmnrpps/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1202_evtrmnrpps_verificar.verificar', 
        name='s1202_evtrmnrpps_verificar'),
        
url(r'^s1202-evtrmnrpps/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1202_evtrmnrpps_verificar.recibo', 
        name='s1202_evtrmnrpps_recibo'),
        
        
url(r'^s1202-evtrmnrpps/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1202_evtrmnrpps_verificar.duplicar',
        name='s1202_evtrmnrpps_duplicar'),

url(r'^s1202-evtrmnrpps/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1202_evtrmnrpps_verificar.criar_alteracao',
        name='s1202_evtrmnrpps_criar_alteracao'),

url(r'^s1202-evtrmnrpps/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1202_evtrmnrpps_verificar.criar_exclusao',
        name='s1202_evtrmnrpps_criar_exclusao'),
        
url(r'^s1202-evtrmnrpps/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1202_evtrmnrpps_verificar.gerar_xml', 
                name='s1202_evtrmnrpps_xml'),
                

url(r'^s1202-evtrmnrpps/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1202_evtrmnrpps_verificar.alterar_identidade',
        name='s1202_evtrmnrpps_alterar_identidade'),

url(r'^s1202-evtrmnrpps/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1202_evtrmnrpps_verificar.abrir_evento_para_edicao',
        name='s1202_evtrmnrpps_abrir_evento_para_edicao'),

url(r'^s1202-evtrmnrpps/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1202_evtrmnrpps_verificar.validar_evento',
        name='s1202_evtrmnrpps_validar_evento'),

url(r'^s1202-evtrmnrpps/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1202_evtrmnrpps.salvar', 
        name='s1202_evtrmnrpps_salvar'),
        

url(r'^scripts/gerar-identidade/s1202-evtrmnrpps/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1202_evtrmnrpps.gerar_identidade', 
        name='s1202_evtrmnrpps_gerar_identidade'),



url(r'^s1207-evtbenprrp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1207_evtbenprrp.apagar', 
        name='s1207_evtbenprrp_apagar'),

url(r'^s1207-evtbenprrp/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1207_evtbenprrp.listar', 
        name='s1207_evtbenprrp'),
        
url(r'^s1207-evtbenprrp/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1207_evtbenprrp_verificar.verificar', 
        name='s1207_evtbenprrp_verificar'),
        
url(r'^s1207-evtbenprrp/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1207_evtbenprrp_verificar.recibo', 
        name='s1207_evtbenprrp_recibo'),
        
        
url(r'^s1207-evtbenprrp/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1207_evtbenprrp_verificar.duplicar',
        name='s1207_evtbenprrp_duplicar'),

url(r'^s1207-evtbenprrp/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1207_evtbenprrp_verificar.criar_alteracao',
        name='s1207_evtbenprrp_criar_alteracao'),

url(r'^s1207-evtbenprrp/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1207_evtbenprrp_verificar.criar_exclusao',
        name='s1207_evtbenprrp_criar_exclusao'),
        
url(r'^s1207-evtbenprrp/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1207_evtbenprrp_verificar.gerar_xml', 
                name='s1207_evtbenprrp_xml'),
                

url(r'^s1207-evtbenprrp/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1207_evtbenprrp_verificar.alterar_identidade',
        name='s1207_evtbenprrp_alterar_identidade'),

url(r'^s1207-evtbenprrp/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1207_evtbenprrp_verificar.abrir_evento_para_edicao',
        name='s1207_evtbenprrp_abrir_evento_para_edicao'),

url(r'^s1207-evtbenprrp/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1207_evtbenprrp_verificar.validar_evento',
        name='s1207_evtbenprrp_validar_evento'),

url(r'^s1207-evtbenprrp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1207_evtbenprrp.salvar', 
        name='s1207_evtbenprrp_salvar'),
        

url(r'^scripts/gerar-identidade/s1207-evtbenprrp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1207_evtbenprrp.gerar_identidade', 
        name='s1207_evtbenprrp_gerar_identidade'),



url(r'^s1210-evtpgtos/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1210_evtpgtos.apagar', 
        name='s1210_evtpgtos_apagar'),

url(r'^s1210-evtpgtos/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1210_evtpgtos.listar', 
        name='s1210_evtpgtos'),
        
url(r'^s1210-evtpgtos/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1210_evtpgtos_verificar.verificar', 
        name='s1210_evtpgtos_verificar'),
        
url(r'^s1210-evtpgtos/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1210_evtpgtos_verificar.recibo', 
        name='s1210_evtpgtos_recibo'),
        
        
url(r'^s1210-evtpgtos/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1210_evtpgtos_verificar.duplicar',
        name='s1210_evtpgtos_duplicar'),

url(r'^s1210-evtpgtos/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1210_evtpgtos_verificar.criar_alteracao',
        name='s1210_evtpgtos_criar_alteracao'),

url(r'^s1210-evtpgtos/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1210_evtpgtos_verificar.criar_exclusao',
        name='s1210_evtpgtos_criar_exclusao'),
        
url(r'^s1210-evtpgtos/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1210_evtpgtos_verificar.gerar_xml', 
                name='s1210_evtpgtos_xml'),
                

url(r'^s1210-evtpgtos/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1210_evtpgtos_verificar.alterar_identidade',
        name='s1210_evtpgtos_alterar_identidade'),

url(r'^s1210-evtpgtos/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1210_evtpgtos_verificar.abrir_evento_para_edicao',
        name='s1210_evtpgtos_abrir_evento_para_edicao'),

url(r'^s1210-evtpgtos/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1210_evtpgtos_verificar.validar_evento',
        name='s1210_evtpgtos_validar_evento'),

url(r'^s1210-evtpgtos/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1210_evtpgtos.salvar', 
        name='s1210_evtpgtos_salvar'),
        

url(r'^scripts/gerar-identidade/s1210-evtpgtos/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1210_evtpgtos.gerar_identidade', 
        name='s1210_evtpgtos_gerar_identidade'),



url(r'^s1250-evtaqprod/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1250_evtaqprod.apagar', 
        name='s1250_evtaqprod_apagar'),

url(r'^s1250-evtaqprod/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1250_evtaqprod.listar', 
        name='s1250_evtaqprod'),
        
url(r'^s1250-evtaqprod/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1250_evtaqprod_verificar.verificar', 
        name='s1250_evtaqprod_verificar'),
        
url(r'^s1250-evtaqprod/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1250_evtaqprod_verificar.recibo', 
        name='s1250_evtaqprod_recibo'),
        
        
url(r'^s1250-evtaqprod/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1250_evtaqprod_verificar.duplicar',
        name='s1250_evtaqprod_duplicar'),

url(r'^s1250-evtaqprod/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1250_evtaqprod_verificar.criar_alteracao',
        name='s1250_evtaqprod_criar_alteracao'),

url(r'^s1250-evtaqprod/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1250_evtaqprod_verificar.criar_exclusao',
        name='s1250_evtaqprod_criar_exclusao'),
        
url(r'^s1250-evtaqprod/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1250_evtaqprod_verificar.gerar_xml', 
                name='s1250_evtaqprod_xml'),
                

url(r'^s1250-evtaqprod/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1250_evtaqprod_verificar.alterar_identidade',
        name='s1250_evtaqprod_alterar_identidade'),

url(r'^s1250-evtaqprod/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1250_evtaqprod_verificar.abrir_evento_para_edicao',
        name='s1250_evtaqprod_abrir_evento_para_edicao'),

url(r'^s1250-evtaqprod/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1250_evtaqprod_verificar.validar_evento',
        name='s1250_evtaqprod_validar_evento'),

url(r'^s1250-evtaqprod/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1250_evtaqprod.salvar', 
        name='s1250_evtaqprod_salvar'),
        

url(r'^scripts/gerar-identidade/s1250-evtaqprod/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1250_evtaqprod.gerar_identidade', 
        name='s1250_evtaqprod_gerar_identidade'),



url(r'^s1260-evtcomprod/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1260_evtcomprod.apagar', 
        name='s1260_evtcomprod_apagar'),

url(r'^s1260-evtcomprod/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1260_evtcomprod.listar', 
        name='s1260_evtcomprod'),
        
url(r'^s1260-evtcomprod/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1260_evtcomprod_verificar.verificar', 
        name='s1260_evtcomprod_verificar'),
        
url(r'^s1260-evtcomprod/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1260_evtcomprod_verificar.recibo', 
        name='s1260_evtcomprod_recibo'),
        
        
url(r'^s1260-evtcomprod/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1260_evtcomprod_verificar.duplicar',
        name='s1260_evtcomprod_duplicar'),

url(r'^s1260-evtcomprod/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1260_evtcomprod_verificar.criar_alteracao',
        name='s1260_evtcomprod_criar_alteracao'),

url(r'^s1260-evtcomprod/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1260_evtcomprod_verificar.criar_exclusao',
        name='s1260_evtcomprod_criar_exclusao'),
        
url(r'^s1260-evtcomprod/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1260_evtcomprod_verificar.gerar_xml', 
                name='s1260_evtcomprod_xml'),
                

url(r'^s1260-evtcomprod/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1260_evtcomprod_verificar.alterar_identidade',
        name='s1260_evtcomprod_alterar_identidade'),

url(r'^s1260-evtcomprod/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1260_evtcomprod_verificar.abrir_evento_para_edicao',
        name='s1260_evtcomprod_abrir_evento_para_edicao'),

url(r'^s1260-evtcomprod/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1260_evtcomprod_verificar.validar_evento',
        name='s1260_evtcomprod_validar_evento'),

url(r'^s1260-evtcomprod/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1260_evtcomprod.salvar', 
        name='s1260_evtcomprod_salvar'),
        

url(r'^scripts/gerar-identidade/s1260-evtcomprod/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1260_evtcomprod.gerar_identidade', 
        name='s1260_evtcomprod_gerar_identidade'),



url(r'^s1270-evtcontratavnp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1270_evtcontratavnp.apagar', 
        name='s1270_evtcontratavnp_apagar'),

url(r'^s1270-evtcontratavnp/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1270_evtcontratavnp.listar', 
        name='s1270_evtcontratavnp'),
        
url(r'^s1270-evtcontratavnp/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1270_evtcontratavnp_verificar.verificar', 
        name='s1270_evtcontratavnp_verificar'),
        
url(r'^s1270-evtcontratavnp/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1270_evtcontratavnp_verificar.recibo', 
        name='s1270_evtcontratavnp_recibo'),
        
        
url(r'^s1270-evtcontratavnp/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1270_evtcontratavnp_verificar.duplicar',
        name='s1270_evtcontratavnp_duplicar'),

url(r'^s1270-evtcontratavnp/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1270_evtcontratavnp_verificar.criar_alteracao',
        name='s1270_evtcontratavnp_criar_alteracao'),

url(r'^s1270-evtcontratavnp/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1270_evtcontratavnp_verificar.criar_exclusao',
        name='s1270_evtcontratavnp_criar_exclusao'),
        
url(r'^s1270-evtcontratavnp/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1270_evtcontratavnp_verificar.gerar_xml', 
                name='s1270_evtcontratavnp_xml'),
                

url(r'^s1270-evtcontratavnp/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1270_evtcontratavnp_verificar.alterar_identidade',
        name='s1270_evtcontratavnp_alterar_identidade'),

url(r'^s1270-evtcontratavnp/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1270_evtcontratavnp_verificar.abrir_evento_para_edicao',
        name='s1270_evtcontratavnp_abrir_evento_para_edicao'),

url(r'^s1270-evtcontratavnp/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1270_evtcontratavnp_verificar.validar_evento',
        name='s1270_evtcontratavnp_validar_evento'),

url(r'^s1270-evtcontratavnp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1270_evtcontratavnp.salvar', 
        name='s1270_evtcontratavnp_salvar'),
        

url(r'^scripts/gerar-identidade/s1270-evtcontratavnp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1270_evtcontratavnp.gerar_identidade', 
        name='s1270_evtcontratavnp_gerar_identidade'),



url(r'^s1280-evtinfocomplper/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1280_evtinfocomplper.apagar', 
        name='s1280_evtinfocomplper_apagar'),

url(r'^s1280-evtinfocomplper/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1280_evtinfocomplper.listar', 
        name='s1280_evtinfocomplper'),
        
url(r'^s1280-evtinfocomplper/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1280_evtinfocomplper_verificar.verificar', 
        name='s1280_evtinfocomplper_verificar'),
        
url(r'^s1280-evtinfocomplper/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1280_evtinfocomplper_verificar.recibo', 
        name='s1280_evtinfocomplper_recibo'),
        
        
url(r'^s1280-evtinfocomplper/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1280_evtinfocomplper_verificar.duplicar',
        name='s1280_evtinfocomplper_duplicar'),

url(r'^s1280-evtinfocomplper/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1280_evtinfocomplper_verificar.criar_alteracao',
        name='s1280_evtinfocomplper_criar_alteracao'),

url(r'^s1280-evtinfocomplper/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1280_evtinfocomplper_verificar.criar_exclusao',
        name='s1280_evtinfocomplper_criar_exclusao'),
        
url(r'^s1280-evtinfocomplper/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1280_evtinfocomplper_verificar.gerar_xml', 
                name='s1280_evtinfocomplper_xml'),
                

url(r'^s1280-evtinfocomplper/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1280_evtinfocomplper_verificar.alterar_identidade',
        name='s1280_evtinfocomplper_alterar_identidade'),

url(r'^s1280-evtinfocomplper/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1280_evtinfocomplper_verificar.abrir_evento_para_edicao',
        name='s1280_evtinfocomplper_abrir_evento_para_edicao'),

url(r'^s1280-evtinfocomplper/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1280_evtinfocomplper_verificar.validar_evento',
        name='s1280_evtinfocomplper_validar_evento'),

url(r'^s1280-evtinfocomplper/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1280_evtinfocomplper.salvar', 
        name='s1280_evtinfocomplper_salvar'),
        

url(r'^scripts/gerar-identidade/s1280-evtinfocomplper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1280_evtinfocomplper.gerar_identidade', 
        name='s1280_evtinfocomplper_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^s1295-evttotconting/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1295_evttotconting.apagar', 
        name='s1295_evttotconting_apagar'),

url(r'^s1295-evttotconting/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1295_evttotconting.listar', 
        name='s1295_evttotconting'),
        
url(r'^s1295-evttotconting/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1295_evttotconting_verificar.verificar', 
        name='s1295_evttotconting_verificar'),
        
url(r'^s1295-evttotconting/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1295_evttotconting_verificar.recibo', 
        name='s1295_evttotconting_recibo'),
        
        
url(r'^s1295-evttotconting/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1295_evttotconting_verificar.duplicar',
        name='s1295_evttotconting_duplicar'),

url(r'^s1295-evttotconting/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1295_evttotconting_verificar.criar_alteracao',
        name='s1295_evttotconting_criar_alteracao'),

url(r'^s1295-evttotconting/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1295_evttotconting_verificar.criar_exclusao',
        name='s1295_evttotconting_criar_exclusao'),
        
url(r'^s1295-evttotconting/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1295_evttotconting_verificar.gerar_xml', 
                name='s1295_evttotconting_xml'),
                

url(r'^s1295-evttotconting/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1295_evttotconting_verificar.alterar_identidade',
        name='s1295_evttotconting_alterar_identidade'),

url(r'^s1295-evttotconting/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1295_evttotconting_verificar.abrir_evento_para_edicao',
        name='s1295_evttotconting_abrir_evento_para_edicao'),

url(r'^s1295-evttotconting/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1295_evttotconting_verificar.validar_evento',
        name='s1295_evttotconting_validar_evento'),

url(r'^s1295-evttotconting/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1295_evttotconting.salvar', 
        name='s1295_evttotconting_salvar'),
        

url(r'^scripts/gerar-identidade/s1295-evttotconting/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1295_evttotconting.gerar_identidade', 
        name='s1295_evttotconting_gerar_identidade'),



url(r'^s1298-evtreabreevper/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1298_evtreabreevper.apagar', 
        name='s1298_evtreabreevper_apagar'),

url(r'^s1298-evtreabreevper/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1298_evtreabreevper.listar', 
        name='s1298_evtreabreevper'),
        
url(r'^s1298-evtreabreevper/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1298_evtreabreevper_verificar.verificar', 
        name='s1298_evtreabreevper_verificar'),
        
url(r'^s1298-evtreabreevper/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1298_evtreabreevper_verificar.recibo', 
        name='s1298_evtreabreevper_recibo'),
        
        
url(r'^s1298-evtreabreevper/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1298_evtreabreevper_verificar.duplicar',
        name='s1298_evtreabreevper_duplicar'),

url(r'^s1298-evtreabreevper/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1298_evtreabreevper_verificar.criar_alteracao',
        name='s1298_evtreabreevper_criar_alteracao'),

url(r'^s1298-evtreabreevper/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1298_evtreabreevper_verificar.criar_exclusao',
        name='s1298_evtreabreevper_criar_exclusao'),
        
url(r'^s1298-evtreabreevper/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1298_evtreabreevper_verificar.gerar_xml', 
                name='s1298_evtreabreevper_xml'),
                

url(r'^s1298-evtreabreevper/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1298_evtreabreevper_verificar.alterar_identidade',
        name='s1298_evtreabreevper_alterar_identidade'),

url(r'^s1298-evtreabreevper/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1298_evtreabreevper_verificar.abrir_evento_para_edicao',
        name='s1298_evtreabreevper_abrir_evento_para_edicao'),

url(r'^s1298-evtreabreevper/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1298_evtreabreevper_verificar.validar_evento',
        name='s1298_evtreabreevper_validar_evento'),

url(r'^s1298-evtreabreevper/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1298_evtreabreevper.salvar', 
        name='s1298_evtreabreevper_salvar'),
        

url(r'^scripts/gerar-identidade/s1298-evtreabreevper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1298_evtreabreevper.gerar_identidade', 
        name='s1298_evtreabreevper_gerar_identidade'),



url(r'^s1299-evtfechaevper/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1299_evtfechaevper.apagar', 
        name='s1299_evtfechaevper_apagar'),

url(r'^s1299-evtfechaevper/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1299_evtfechaevper.listar', 
        name='s1299_evtfechaevper'),
        
url(r'^s1299-evtfechaevper/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1299_evtfechaevper_verificar.verificar', 
        name='s1299_evtfechaevper_verificar'),
        
url(r'^s1299-evtfechaevper/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1299_evtfechaevper_verificar.recibo', 
        name='s1299_evtfechaevper_recibo'),
        
        
url(r'^s1299-evtfechaevper/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1299_evtfechaevper_verificar.duplicar',
        name='s1299_evtfechaevper_duplicar'),

url(r'^s1299-evtfechaevper/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1299_evtfechaevper_verificar.criar_alteracao',
        name='s1299_evtfechaevper_criar_alteracao'),

url(r'^s1299-evtfechaevper/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1299_evtfechaevper_verificar.criar_exclusao',
        name='s1299_evtfechaevper_criar_exclusao'),
        
url(r'^s1299-evtfechaevper/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1299_evtfechaevper_verificar.gerar_xml', 
                name='s1299_evtfechaevper_xml'),
                

url(r'^s1299-evtfechaevper/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1299_evtfechaevper_verificar.alterar_identidade',
        name='s1299_evtfechaevper_alterar_identidade'),

url(r'^s1299-evtfechaevper/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1299_evtfechaevper_verificar.abrir_evento_para_edicao',
        name='s1299_evtfechaevper_abrir_evento_para_edicao'),

url(r'^s1299-evtfechaevper/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1299_evtfechaevper_verificar.validar_evento',
        name='s1299_evtfechaevper_validar_evento'),

url(r'^s1299-evtfechaevper/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1299_evtfechaevper.salvar', 
        name='s1299_evtfechaevper_salvar'),
        

url(r'^scripts/gerar-identidade/s1299-evtfechaevper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1299_evtfechaevper.gerar_identidade', 
        name='s1299_evtfechaevper_gerar_identidade'),



url(r'^s1300-evtcontrsindpatr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr.apagar', 
        name='s1300_evtcontrsindpatr_apagar'),

url(r'^s1300-evtcontrsindpatr/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr.listar', 
        name='s1300_evtcontrsindpatr'),
        
url(r'^s1300-evtcontrsindpatr/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar.verificar', 
        name='s1300_evtcontrsindpatr_verificar'),
        
url(r'^s1300-evtcontrsindpatr/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar.recibo', 
        name='s1300_evtcontrsindpatr_recibo'),
        
        
url(r'^s1300-evtcontrsindpatr/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar.duplicar',
        name='s1300_evtcontrsindpatr_duplicar'),

url(r'^s1300-evtcontrsindpatr/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar.criar_alteracao',
        name='s1300_evtcontrsindpatr_criar_alteracao'),

url(r'^s1300-evtcontrsindpatr/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar.criar_exclusao',
        name='s1300_evtcontrsindpatr_criar_exclusao'),
        
url(r'^s1300-evtcontrsindpatr/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar.gerar_xml', 
                name='s1300_evtcontrsindpatr_xml'),
                

url(r'^s1300-evtcontrsindpatr/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar.alterar_identidade',
        name='s1300_evtcontrsindpatr_alterar_identidade'),

url(r'^s1300-evtcontrsindpatr/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar.abrir_evento_para_edicao',
        name='s1300_evtcontrsindpatr_abrir_evento_para_edicao'),

url(r'^s1300-evtcontrsindpatr/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar.validar_evento',
        name='s1300_evtcontrsindpatr_validar_evento'),

url(r'^s1300-evtcontrsindpatr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr.salvar', 
        name='s1300_evtcontrsindpatr_salvar'),
        

url(r'^scripts/gerar-identidade/s1300-evtcontrsindpatr/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s1300_evtcontrsindpatr.gerar_identidade', 
        name='s1300_evtcontrsindpatr_gerar_identidade'),



url(r'^s2190-evtadmprelim/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2190_evtadmprelim.apagar', 
        name='s2190_evtadmprelim_apagar'),

url(r'^s2190-evtadmprelim/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2190_evtadmprelim.listar', 
        name='s2190_evtadmprelim'),
        
url(r'^s2190-evtadmprelim/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2190_evtadmprelim_verificar.verificar', 
        name='s2190_evtadmprelim_verificar'),
        
url(r'^s2190-evtadmprelim/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2190_evtadmprelim_verificar.recibo', 
        name='s2190_evtadmprelim_recibo'),
        
        
url(r'^s2190-evtadmprelim/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2190_evtadmprelim_verificar.duplicar',
        name='s2190_evtadmprelim_duplicar'),

url(r'^s2190-evtadmprelim/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2190_evtadmprelim_verificar.criar_alteracao',
        name='s2190_evtadmprelim_criar_alteracao'),

url(r'^s2190-evtadmprelim/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2190_evtadmprelim_verificar.criar_exclusao',
        name='s2190_evtadmprelim_criar_exclusao'),
        
url(r'^s2190-evtadmprelim/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2190_evtadmprelim_verificar.gerar_xml', 
                name='s2190_evtadmprelim_xml'),
                

url(r'^s2190-evtadmprelim/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2190_evtadmprelim_verificar.alterar_identidade',
        name='s2190_evtadmprelim_alterar_identidade'),

url(r'^s2190-evtadmprelim/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2190_evtadmprelim_verificar.abrir_evento_para_edicao',
        name='s2190_evtadmprelim_abrir_evento_para_edicao'),

url(r'^s2190-evtadmprelim/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2190_evtadmprelim_verificar.validar_evento',
        name='s2190_evtadmprelim_validar_evento'),

url(r'^s2190-evtadmprelim/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2190_evtadmprelim.salvar', 
        name='s2190_evtadmprelim_salvar'),
        

url(r'^scripts/gerar-identidade/s2190-evtadmprelim/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2190_evtadmprelim.gerar_identidade', 
        name='s2190_evtadmprelim_gerar_identidade'),



url(r'^s2200-evtadmissao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2200_evtadmissao.apagar', 
        name='s2200_evtadmissao_apagar'),

url(r'^s2200-evtadmissao/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2200_evtadmissao.listar', 
        name='s2200_evtadmissao'),
        
url(r'^s2200-evtadmissao/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2200_evtadmissao_verificar.verificar', 
        name='s2200_evtadmissao_verificar'),
        
url(r'^s2200-evtadmissao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2200_evtadmissao_verificar.recibo', 
        name='s2200_evtadmissao_recibo'),
        
        
url(r'^s2200-evtadmissao/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2200_evtadmissao_verificar.duplicar',
        name='s2200_evtadmissao_duplicar'),

url(r'^s2200-evtadmissao/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2200_evtadmissao_verificar.criar_alteracao',
        name='s2200_evtadmissao_criar_alteracao'),

url(r'^s2200-evtadmissao/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2200_evtadmissao_verificar.criar_exclusao',
        name='s2200_evtadmissao_criar_exclusao'),
        
url(r'^s2200-evtadmissao/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2200_evtadmissao_verificar.gerar_xml', 
                name='s2200_evtadmissao_xml'),
                

url(r'^s2200-evtadmissao/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2200_evtadmissao_verificar.alterar_identidade',
        name='s2200_evtadmissao_alterar_identidade'),

url(r'^s2200-evtadmissao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2200_evtadmissao_verificar.abrir_evento_para_edicao',
        name='s2200_evtadmissao_abrir_evento_para_edicao'),

url(r'^s2200-evtadmissao/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2200_evtadmissao_verificar.validar_evento',
        name='s2200_evtadmissao_validar_evento'),

url(r'^s2200-evtadmissao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2200_evtadmissao.salvar', 
        name='s2200_evtadmissao_salvar'),
        

url(r'^scripts/gerar-identidade/s2200-evtadmissao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2200_evtadmissao.gerar_identidade', 
        name='s2200_evtadmissao_gerar_identidade'),



url(r'^s2205-evtaltcadastral/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2205_evtaltcadastral.apagar', 
        name='s2205_evtaltcadastral_apagar'),

url(r'^s2205-evtaltcadastral/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2205_evtaltcadastral.listar', 
        name='s2205_evtaltcadastral'),
        
url(r'^s2205-evtaltcadastral/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2205_evtaltcadastral_verificar.verificar', 
        name='s2205_evtaltcadastral_verificar'),
        
url(r'^s2205-evtaltcadastral/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2205_evtaltcadastral_verificar.recibo', 
        name='s2205_evtaltcadastral_recibo'),
        
        
url(r'^s2205-evtaltcadastral/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2205_evtaltcadastral_verificar.duplicar',
        name='s2205_evtaltcadastral_duplicar'),

url(r'^s2205-evtaltcadastral/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2205_evtaltcadastral_verificar.criar_alteracao',
        name='s2205_evtaltcadastral_criar_alteracao'),

url(r'^s2205-evtaltcadastral/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2205_evtaltcadastral_verificar.criar_exclusao',
        name='s2205_evtaltcadastral_criar_exclusao'),
        
url(r'^s2205-evtaltcadastral/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2205_evtaltcadastral_verificar.gerar_xml', 
                name='s2205_evtaltcadastral_xml'),
                

url(r'^s2205-evtaltcadastral/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2205_evtaltcadastral_verificar.alterar_identidade',
        name='s2205_evtaltcadastral_alterar_identidade'),

url(r'^s2205-evtaltcadastral/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2205_evtaltcadastral_verificar.abrir_evento_para_edicao',
        name='s2205_evtaltcadastral_abrir_evento_para_edicao'),

url(r'^s2205-evtaltcadastral/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2205_evtaltcadastral_verificar.validar_evento',
        name='s2205_evtaltcadastral_validar_evento'),

url(r'^s2205-evtaltcadastral/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2205_evtaltcadastral.salvar', 
        name='s2205_evtaltcadastral_salvar'),
        

url(r'^scripts/gerar-identidade/s2205-evtaltcadastral/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2205_evtaltcadastral.gerar_identidade', 
        name='s2205_evtaltcadastral_gerar_identidade'),



url(r'^s2206-evtaltcontratual/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2206_evtaltcontratual.apagar', 
        name='s2206_evtaltcontratual_apagar'),

url(r'^s2206-evtaltcontratual/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2206_evtaltcontratual.listar', 
        name='s2206_evtaltcontratual'),
        
url(r'^s2206-evtaltcontratual/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2206_evtaltcontratual_verificar.verificar', 
        name='s2206_evtaltcontratual_verificar'),
        
url(r'^s2206-evtaltcontratual/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2206_evtaltcontratual_verificar.recibo', 
        name='s2206_evtaltcontratual_recibo'),
        
        
url(r'^s2206-evtaltcontratual/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2206_evtaltcontratual_verificar.duplicar',
        name='s2206_evtaltcontratual_duplicar'),

url(r'^s2206-evtaltcontratual/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2206_evtaltcontratual_verificar.criar_alteracao',
        name='s2206_evtaltcontratual_criar_alteracao'),

url(r'^s2206-evtaltcontratual/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2206_evtaltcontratual_verificar.criar_exclusao',
        name='s2206_evtaltcontratual_criar_exclusao'),
        
url(r'^s2206-evtaltcontratual/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2206_evtaltcontratual_verificar.gerar_xml', 
                name='s2206_evtaltcontratual_xml'),
                

url(r'^s2206-evtaltcontratual/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2206_evtaltcontratual_verificar.alterar_identidade',
        name='s2206_evtaltcontratual_alterar_identidade'),

url(r'^s2206-evtaltcontratual/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2206_evtaltcontratual_verificar.abrir_evento_para_edicao',
        name='s2206_evtaltcontratual_abrir_evento_para_edicao'),

url(r'^s2206-evtaltcontratual/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2206_evtaltcontratual_verificar.validar_evento',
        name='s2206_evtaltcontratual_validar_evento'),

url(r'^s2206-evtaltcontratual/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2206_evtaltcontratual.salvar', 
        name='s2206_evtaltcontratual_salvar'),
        

url(r'^scripts/gerar-identidade/s2206-evtaltcontratual/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2206_evtaltcontratual.gerar_identidade', 
        name='s2206_evtaltcontratual_gerar_identidade'),



url(r'^s2210-evtcat/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2210_evtcat.apagar', 
        name='s2210_evtcat_apagar'),

url(r'^s2210-evtcat/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2210_evtcat.listar', 
        name='s2210_evtcat'),
        
url(r'^s2210-evtcat/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2210_evtcat_verificar.verificar', 
        name='s2210_evtcat_verificar'),
        
url(r'^s2210-evtcat/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2210_evtcat_verificar.recibo', 
        name='s2210_evtcat_recibo'),
        
        
url(r'^s2210-evtcat/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2210_evtcat_verificar.duplicar',
        name='s2210_evtcat_duplicar'),

url(r'^s2210-evtcat/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2210_evtcat_verificar.criar_alteracao',
        name='s2210_evtcat_criar_alteracao'),

url(r'^s2210-evtcat/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2210_evtcat_verificar.criar_exclusao',
        name='s2210_evtcat_criar_exclusao'),
        
url(r'^s2210-evtcat/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2210_evtcat_verificar.gerar_xml', 
                name='s2210_evtcat_xml'),
                

url(r'^s2210-evtcat/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2210_evtcat_verificar.alterar_identidade',
        name='s2210_evtcat_alterar_identidade'),

url(r'^s2210-evtcat/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2210_evtcat_verificar.abrir_evento_para_edicao',
        name='s2210_evtcat_abrir_evento_para_edicao'),

url(r'^s2210-evtcat/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2210_evtcat_verificar.validar_evento',
        name='s2210_evtcat_validar_evento'),

url(r'^s2210-evtcat/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2210_evtcat.salvar', 
        name='s2210_evtcat_salvar'),
        

url(r'^scripts/gerar-identidade/s2210-evtcat/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2210_evtcat.gerar_identidade', 
        name='s2210_evtcat_gerar_identidade'),



url(r'^s2220-evtmonit/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2220_evtmonit.apagar', 
        name='s2220_evtmonit_apagar'),

url(r'^s2220-evtmonit/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2220_evtmonit.listar', 
        name='s2220_evtmonit'),
        
url(r'^s2220-evtmonit/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2220_evtmonit_verificar.verificar', 
        name='s2220_evtmonit_verificar'),
        
url(r'^s2220-evtmonit/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2220_evtmonit_verificar.recibo', 
        name='s2220_evtmonit_recibo'),
        
        
url(r'^s2220-evtmonit/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2220_evtmonit_verificar.duplicar',
        name='s2220_evtmonit_duplicar'),

url(r'^s2220-evtmonit/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2220_evtmonit_verificar.criar_alteracao',
        name='s2220_evtmonit_criar_alteracao'),

url(r'^s2220-evtmonit/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2220_evtmonit_verificar.criar_exclusao',
        name='s2220_evtmonit_criar_exclusao'),
        
url(r'^s2220-evtmonit/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2220_evtmonit_verificar.gerar_xml', 
                name='s2220_evtmonit_xml'),
                

url(r'^s2220-evtmonit/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2220_evtmonit_verificar.alterar_identidade',
        name='s2220_evtmonit_alterar_identidade'),

url(r'^s2220-evtmonit/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2220_evtmonit_verificar.abrir_evento_para_edicao',
        name='s2220_evtmonit_abrir_evento_para_edicao'),

url(r'^s2220-evtmonit/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2220_evtmonit_verificar.validar_evento',
        name='s2220_evtmonit_validar_evento'),

url(r'^s2220-evtmonit/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2220_evtmonit.salvar', 
        name='s2220_evtmonit_salvar'),
        

url(r'^scripts/gerar-identidade/s2220-evtmonit/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2220_evtmonit.gerar_identidade', 
        name='s2220_evtmonit_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^s2230-evtafasttemp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2230_evtafasttemp.apagar', 
        name='s2230_evtafasttemp_apagar'),

url(r'^s2230-evtafasttemp/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2230_evtafasttemp.listar', 
        name='s2230_evtafasttemp'),
        
url(r'^s2230-evtafasttemp/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2230_evtafasttemp_verificar.verificar', 
        name='s2230_evtafasttemp_verificar'),
        
url(r'^s2230-evtafasttemp/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2230_evtafasttemp_verificar.recibo', 
        name='s2230_evtafasttemp_recibo'),
        
        
url(r'^s2230-evtafasttemp/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2230_evtafasttemp_verificar.duplicar',
        name='s2230_evtafasttemp_duplicar'),

url(r'^s2230-evtafasttemp/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2230_evtafasttemp_verificar.criar_alteracao',
        name='s2230_evtafasttemp_criar_alteracao'),

url(r'^s2230-evtafasttemp/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2230_evtafasttemp_verificar.criar_exclusao',
        name='s2230_evtafasttemp_criar_exclusao'),
        
url(r'^s2230-evtafasttemp/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2230_evtafasttemp_verificar.gerar_xml', 
                name='s2230_evtafasttemp_xml'),
                

url(r'^s2230-evtafasttemp/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2230_evtafasttemp_verificar.alterar_identidade',
        name='s2230_evtafasttemp_alterar_identidade'),

url(r'^s2230-evtafasttemp/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2230_evtafasttemp_verificar.abrir_evento_para_edicao',
        name='s2230_evtafasttemp_abrir_evento_para_edicao'),

url(r'^s2230-evtafasttemp/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2230_evtafasttemp_verificar.validar_evento',
        name='s2230_evtafasttemp_validar_evento'),

url(r'^s2230-evtafasttemp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2230_evtafasttemp.salvar', 
        name='s2230_evtafasttemp_salvar'),
        

url(r'^scripts/gerar-identidade/s2230-evtafasttemp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2230_evtafasttemp.gerar_identidade', 
        name='s2230_evtafasttemp_gerar_identidade'),



url(r'^s2231-evtcessao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2231_evtcessao.apagar', 
        name='s2231_evtcessao_apagar'),

url(r'^s2231-evtcessao/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2231_evtcessao.listar', 
        name='s2231_evtcessao'),
        
url(r'^s2231-evtcessao/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2231_evtcessao_verificar.verificar', 
        name='s2231_evtcessao_verificar'),
        
url(r'^s2231-evtcessao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2231_evtcessao_verificar.recibo', 
        name='s2231_evtcessao_recibo'),
        
        
url(r'^s2231-evtcessao/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2231_evtcessao_verificar.duplicar',
        name='s2231_evtcessao_duplicar'),

url(r'^s2231-evtcessao/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2231_evtcessao_verificar.criar_alteracao',
        name='s2231_evtcessao_criar_alteracao'),

url(r'^s2231-evtcessao/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2231_evtcessao_verificar.criar_exclusao',
        name='s2231_evtcessao_criar_exclusao'),
        
url(r'^s2231-evtcessao/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2231_evtcessao_verificar.gerar_xml', 
                name='s2231_evtcessao_xml'),
                

url(r'^s2231-evtcessao/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2231_evtcessao_verificar.alterar_identidade',
        name='s2231_evtcessao_alterar_identidade'),

url(r'^s2231-evtcessao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2231_evtcessao_verificar.abrir_evento_para_edicao',
        name='s2231_evtcessao_abrir_evento_para_edicao'),

url(r'^s2231-evtcessao/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2231_evtcessao_verificar.validar_evento',
        name='s2231_evtcessao_validar_evento'),

url(r'^s2231-evtcessao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2231_evtcessao.salvar', 
        name='s2231_evtcessao_salvar'),
        

url(r'^scripts/gerar-identidade/s2231-evtcessao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2231_evtcessao.gerar_identidade', 
        name='s2231_evtcessao_gerar_identidade'),



url(r'^s2240-evtexprisco/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2240_evtexprisco.apagar', 
        name='s2240_evtexprisco_apagar'),

url(r'^s2240-evtexprisco/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2240_evtexprisco.listar', 
        name='s2240_evtexprisco'),
        
url(r'^s2240-evtexprisco/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2240_evtexprisco_verificar.verificar', 
        name='s2240_evtexprisco_verificar'),
        
url(r'^s2240-evtexprisco/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2240_evtexprisco_verificar.recibo', 
        name='s2240_evtexprisco_recibo'),
        
        
url(r'^s2240-evtexprisco/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2240_evtexprisco_verificar.duplicar',
        name='s2240_evtexprisco_duplicar'),

url(r'^s2240-evtexprisco/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2240_evtexprisco_verificar.criar_alteracao',
        name='s2240_evtexprisco_criar_alteracao'),

url(r'^s2240-evtexprisco/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2240_evtexprisco_verificar.criar_exclusao',
        name='s2240_evtexprisco_criar_exclusao'),
        
url(r'^s2240-evtexprisco/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2240_evtexprisco_verificar.gerar_xml', 
                name='s2240_evtexprisco_xml'),
                

url(r'^s2240-evtexprisco/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2240_evtexprisco_verificar.alterar_identidade',
        name='s2240_evtexprisco_alterar_identidade'),

url(r'^s2240-evtexprisco/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2240_evtexprisco_verificar.abrir_evento_para_edicao',
        name='s2240_evtexprisco_abrir_evento_para_edicao'),

url(r'^s2240-evtexprisco/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2240_evtexprisco_verificar.validar_evento',
        name='s2240_evtexprisco_validar_evento'),

url(r'^s2240-evtexprisco/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2240_evtexprisco.salvar', 
        name='s2240_evtexprisco_salvar'),
        

url(r'^scripts/gerar-identidade/s2240-evtexprisco/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2240_evtexprisco.gerar_identidade', 
        name='s2240_evtexprisco_gerar_identidade'),



url(r'^s2241-evtinsapo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2241_evtinsapo.apagar', 
        name='s2241_evtinsapo_apagar'),

url(r'^s2241-evtinsapo/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2241_evtinsapo.listar', 
        name='s2241_evtinsapo'),
        
url(r'^s2241-evtinsapo/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2241_evtinsapo_verificar.verificar', 
        name='s2241_evtinsapo_verificar'),
        
url(r'^s2241-evtinsapo/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2241_evtinsapo_verificar.recibo', 
        name='s2241_evtinsapo_recibo'),
        
        
url(r'^s2241-evtinsapo/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2241_evtinsapo_verificar.duplicar',
        name='s2241_evtinsapo_duplicar'),

url(r'^s2241-evtinsapo/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2241_evtinsapo_verificar.criar_alteracao',
        name='s2241_evtinsapo_criar_alteracao'),

url(r'^s2241-evtinsapo/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2241_evtinsapo_verificar.criar_exclusao',
        name='s2241_evtinsapo_criar_exclusao'),
        
url(r'^s2241-evtinsapo/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2241_evtinsapo_verificar.gerar_xml', 
                name='s2241_evtinsapo_xml'),
                

url(r'^s2241-evtinsapo/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2241_evtinsapo_verificar.alterar_identidade',
        name='s2241_evtinsapo_alterar_identidade'),

url(r'^s2241-evtinsapo/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2241_evtinsapo_verificar.abrir_evento_para_edicao',
        name='s2241_evtinsapo_abrir_evento_para_edicao'),

url(r'^s2241-evtinsapo/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2241_evtinsapo_verificar.validar_evento',
        name='s2241_evtinsapo_validar_evento'),

url(r'^s2241-evtinsapo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2241_evtinsapo.salvar', 
        name='s2241_evtinsapo_salvar'),
        

url(r'^scripts/gerar-identidade/s2241-evtinsapo/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2241_evtinsapo.gerar_identidade', 
        name='s2241_evtinsapo_gerar_identidade'),



url(r'^s2245-evttreicap/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2245_evttreicap.apagar', 
        name='s2245_evttreicap_apagar'),

url(r'^s2245-evttreicap/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2245_evttreicap.listar', 
        name='s2245_evttreicap'),
        
url(r'^s2245-evttreicap/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2245_evttreicap_verificar.verificar', 
        name='s2245_evttreicap_verificar'),
        
url(r'^s2245-evttreicap/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2245_evttreicap_verificar.recibo', 
        name='s2245_evttreicap_recibo'),
        
        
url(r'^s2245-evttreicap/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2245_evttreicap_verificar.duplicar',
        name='s2245_evttreicap_duplicar'),

url(r'^s2245-evttreicap/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2245_evttreicap_verificar.criar_alteracao',
        name='s2245_evttreicap_criar_alteracao'),

url(r'^s2245-evttreicap/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2245_evttreicap_verificar.criar_exclusao',
        name='s2245_evttreicap_criar_exclusao'),
        
url(r'^s2245-evttreicap/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2245_evttreicap_verificar.gerar_xml', 
                name='s2245_evttreicap_xml'),
                

url(r'^s2245-evttreicap/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2245_evttreicap_verificar.alterar_identidade',
        name='s2245_evttreicap_alterar_identidade'),

url(r'^s2245-evttreicap/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2245_evttreicap_verificar.abrir_evento_para_edicao',
        name='s2245_evttreicap_abrir_evento_para_edicao'),

url(r'^s2245-evttreicap/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2245_evttreicap_verificar.validar_evento',
        name='s2245_evttreicap_validar_evento'),

url(r'^s2245-evttreicap/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2245_evttreicap.salvar', 
        name='s2245_evttreicap_salvar'),
        

url(r'^scripts/gerar-identidade/s2245-evttreicap/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2245_evttreicap.gerar_identidade', 
        name='s2245_evttreicap_gerar_identidade'),



url(r'^s2250-evtavprevio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2250_evtavprevio.apagar', 
        name='s2250_evtavprevio_apagar'),

url(r'^s2250-evtavprevio/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2250_evtavprevio.listar', 
        name='s2250_evtavprevio'),
        
url(r'^s2250-evtavprevio/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2250_evtavprevio_verificar.verificar', 
        name='s2250_evtavprevio_verificar'),
        
url(r'^s2250-evtavprevio/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2250_evtavprevio_verificar.recibo', 
        name='s2250_evtavprevio_recibo'),
        
        
url(r'^s2250-evtavprevio/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2250_evtavprevio_verificar.duplicar',
        name='s2250_evtavprevio_duplicar'),

url(r'^s2250-evtavprevio/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2250_evtavprevio_verificar.criar_alteracao',
        name='s2250_evtavprevio_criar_alteracao'),

url(r'^s2250-evtavprevio/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2250_evtavprevio_verificar.criar_exclusao',
        name='s2250_evtavprevio_criar_exclusao'),
        
url(r'^s2250-evtavprevio/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2250_evtavprevio_verificar.gerar_xml', 
                name='s2250_evtavprevio_xml'),
                

url(r'^s2250-evtavprevio/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2250_evtavprevio_verificar.alterar_identidade',
        name='s2250_evtavprevio_alterar_identidade'),

url(r'^s2250-evtavprevio/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2250_evtavprevio_verificar.abrir_evento_para_edicao',
        name='s2250_evtavprevio_abrir_evento_para_edicao'),

url(r'^s2250-evtavprevio/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2250_evtavprevio_verificar.validar_evento',
        name='s2250_evtavprevio_validar_evento'),

url(r'^s2250-evtavprevio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2250_evtavprevio.salvar', 
        name='s2250_evtavprevio_salvar'),
        

url(r'^scripts/gerar-identidade/s2250-evtavprevio/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2250_evtavprevio.gerar_identidade', 
        name='s2250_evtavprevio_gerar_identidade'),



url(r'^s2260-evtconvinterm/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2260_evtconvinterm.apagar', 
        name='s2260_evtconvinterm_apagar'),

url(r'^s2260-evtconvinterm/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2260_evtconvinterm.listar', 
        name='s2260_evtconvinterm'),
        
url(r'^s2260-evtconvinterm/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2260_evtconvinterm_verificar.verificar', 
        name='s2260_evtconvinterm_verificar'),
        
url(r'^s2260-evtconvinterm/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2260_evtconvinterm_verificar.recibo', 
        name='s2260_evtconvinterm_recibo'),
        
        
url(r'^s2260-evtconvinterm/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2260_evtconvinterm_verificar.duplicar',
        name='s2260_evtconvinterm_duplicar'),

url(r'^s2260-evtconvinterm/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2260_evtconvinterm_verificar.criar_alteracao',
        name='s2260_evtconvinterm_criar_alteracao'),

url(r'^s2260-evtconvinterm/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2260_evtconvinterm_verificar.criar_exclusao',
        name='s2260_evtconvinterm_criar_exclusao'),
        
url(r'^s2260-evtconvinterm/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2260_evtconvinterm_verificar.gerar_xml', 
                name='s2260_evtconvinterm_xml'),
                

url(r'^s2260-evtconvinterm/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2260_evtconvinterm_verificar.alterar_identidade',
        name='s2260_evtconvinterm_alterar_identidade'),

url(r'^s2260-evtconvinterm/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2260_evtconvinterm_verificar.abrir_evento_para_edicao',
        name='s2260_evtconvinterm_abrir_evento_para_edicao'),

url(r'^s2260-evtconvinterm/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2260_evtconvinterm_verificar.validar_evento',
        name='s2260_evtconvinterm_validar_evento'),

url(r'^s2260-evtconvinterm/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2260_evtconvinterm.salvar', 
        name='s2260_evtconvinterm_salvar'),
        

url(r'^scripts/gerar-identidade/s2260-evtconvinterm/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2260_evtconvinterm.gerar_identidade', 
        name='s2260_evtconvinterm_gerar_identidade'),



url(r'^s2298-evtreintegr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2298_evtreintegr.apagar', 
        name='s2298_evtreintegr_apagar'),

url(r'^s2298-evtreintegr/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2298_evtreintegr.listar', 
        name='s2298_evtreintegr'),
        
url(r'^s2298-evtreintegr/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2298_evtreintegr_verificar.verificar', 
        name='s2298_evtreintegr_verificar'),
        
url(r'^s2298-evtreintegr/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2298_evtreintegr_verificar.recibo', 
        name='s2298_evtreintegr_recibo'),
        
        
url(r'^s2298-evtreintegr/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2298_evtreintegr_verificar.duplicar',
        name='s2298_evtreintegr_duplicar'),

url(r'^s2298-evtreintegr/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2298_evtreintegr_verificar.criar_alteracao',
        name='s2298_evtreintegr_criar_alteracao'),

url(r'^s2298-evtreintegr/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2298_evtreintegr_verificar.criar_exclusao',
        name='s2298_evtreintegr_criar_exclusao'),
        
url(r'^s2298-evtreintegr/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2298_evtreintegr_verificar.gerar_xml', 
                name='s2298_evtreintegr_xml'),
                

url(r'^s2298-evtreintegr/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2298_evtreintegr_verificar.alterar_identidade',
        name='s2298_evtreintegr_alterar_identidade'),

url(r'^s2298-evtreintegr/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2298_evtreintegr_verificar.abrir_evento_para_edicao',
        name='s2298_evtreintegr_abrir_evento_para_edicao'),

url(r'^s2298-evtreintegr/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2298_evtreintegr_verificar.validar_evento',
        name='s2298_evtreintegr_validar_evento'),

url(r'^s2298-evtreintegr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2298_evtreintegr.salvar', 
        name='s2298_evtreintegr_salvar'),
        

url(r'^scripts/gerar-identidade/s2298-evtreintegr/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2298_evtreintegr.gerar_identidade', 
        name='s2298_evtreintegr_gerar_identidade'),



url(r'^s2299-evtdeslig/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2299_evtdeslig.apagar', 
        name='s2299_evtdeslig_apagar'),

url(r'^s2299-evtdeslig/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2299_evtdeslig.listar', 
        name='s2299_evtdeslig'),
        
url(r'^s2299-evtdeslig/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2299_evtdeslig_verificar.verificar', 
        name='s2299_evtdeslig_verificar'),
        
url(r'^s2299-evtdeslig/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2299_evtdeslig_verificar.recibo', 
        name='s2299_evtdeslig_recibo'),
        
        
url(r'^s2299-evtdeslig/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2299_evtdeslig_verificar.duplicar',
        name='s2299_evtdeslig_duplicar'),

url(r'^s2299-evtdeslig/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2299_evtdeslig_verificar.criar_alteracao',
        name='s2299_evtdeslig_criar_alteracao'),

url(r'^s2299-evtdeslig/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2299_evtdeslig_verificar.criar_exclusao',
        name='s2299_evtdeslig_criar_exclusao'),
        
url(r'^s2299-evtdeslig/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2299_evtdeslig_verificar.gerar_xml', 
                name='s2299_evtdeslig_xml'),
                

url(r'^s2299-evtdeslig/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2299_evtdeslig_verificar.alterar_identidade',
        name='s2299_evtdeslig_alterar_identidade'),

url(r'^s2299-evtdeslig/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2299_evtdeslig_verificar.abrir_evento_para_edicao',
        name='s2299_evtdeslig_abrir_evento_para_edicao'),

url(r'^s2299-evtdeslig/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2299_evtdeslig_verificar.validar_evento',
        name='s2299_evtdeslig_validar_evento'),

url(r'^s2299-evtdeslig/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2299_evtdeslig.salvar', 
        name='s2299_evtdeslig_salvar'),
        

url(r'^scripts/gerar-identidade/s2299-evtdeslig/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2299_evtdeslig.gerar_identidade', 
        name='s2299_evtdeslig_gerar_identidade'),



url(r'^s2300-evttsvinicio/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2300_evttsvinicio.apagar', 
        name='s2300_evttsvinicio_apagar'),

url(r'^s2300-evttsvinicio/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2300_evttsvinicio.listar', 
        name='s2300_evttsvinicio'),
        
url(r'^s2300-evttsvinicio/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2300_evttsvinicio_verificar.verificar', 
        name='s2300_evttsvinicio_verificar'),
        
url(r'^s2300-evttsvinicio/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2300_evttsvinicio_verificar.recibo', 
        name='s2300_evttsvinicio_recibo'),
        
        
url(r'^s2300-evttsvinicio/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2300_evttsvinicio_verificar.duplicar',
        name='s2300_evttsvinicio_duplicar'),

url(r'^s2300-evttsvinicio/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2300_evttsvinicio_verificar.criar_alteracao',
        name='s2300_evttsvinicio_criar_alteracao'),

url(r'^s2300-evttsvinicio/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2300_evttsvinicio_verificar.criar_exclusao',
        name='s2300_evttsvinicio_criar_exclusao'),
        
url(r'^s2300-evttsvinicio/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2300_evttsvinicio_verificar.gerar_xml', 
                name='s2300_evttsvinicio_xml'),
                

url(r'^s2300-evttsvinicio/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2300_evttsvinicio_verificar.alterar_identidade',
        name='s2300_evttsvinicio_alterar_identidade'),

url(r'^s2300-evttsvinicio/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2300_evttsvinicio_verificar.abrir_evento_para_edicao',
        name='s2300_evttsvinicio_abrir_evento_para_edicao'),

url(r'^s2300-evttsvinicio/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2300_evttsvinicio_verificar.validar_evento',
        name='s2300_evttsvinicio_validar_evento'),

url(r'^s2300-evttsvinicio/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2300_evttsvinicio.salvar', 
        name='s2300_evttsvinicio_salvar'),
        

url(r'^scripts/gerar-identidade/s2300-evttsvinicio/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2300_evttsvinicio.gerar_identidade', 
        name='s2300_evttsvinicio_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^s2306-evttsvaltcontr/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2306_evttsvaltcontr.apagar', 
        name='s2306_evttsvaltcontr_apagar'),

url(r'^s2306-evttsvaltcontr/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2306_evttsvaltcontr.listar', 
        name='s2306_evttsvaltcontr'),
        
url(r'^s2306-evttsvaltcontr/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar.verificar', 
        name='s2306_evttsvaltcontr_verificar'),
        
url(r'^s2306-evttsvaltcontr/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar.recibo', 
        name='s2306_evttsvaltcontr_recibo'),
        
        
url(r'^s2306-evttsvaltcontr/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar.duplicar',
        name='s2306_evttsvaltcontr_duplicar'),

url(r'^s2306-evttsvaltcontr/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar.criar_alteracao',
        name='s2306_evttsvaltcontr_criar_alteracao'),

url(r'^s2306-evttsvaltcontr/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar.criar_exclusao',
        name='s2306_evttsvaltcontr_criar_exclusao'),
        
url(r'^s2306-evttsvaltcontr/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar.gerar_xml', 
                name='s2306_evttsvaltcontr_xml'),
                

url(r'^s2306-evttsvaltcontr/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar.alterar_identidade',
        name='s2306_evttsvaltcontr_alterar_identidade'),

url(r'^s2306-evttsvaltcontr/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar.abrir_evento_para_edicao',
        name='s2306_evttsvaltcontr_abrir_evento_para_edicao'),

url(r'^s2306-evttsvaltcontr/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar.validar_evento',
        name='s2306_evttsvaltcontr_validar_evento'),

url(r'^s2306-evttsvaltcontr/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2306_evttsvaltcontr.salvar', 
        name='s2306_evttsvaltcontr_salvar'),
        

url(r'^scripts/gerar-identidade/s2306-evttsvaltcontr/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2306_evttsvaltcontr.gerar_identidade', 
        name='s2306_evttsvaltcontr_gerar_identidade'),



url(r'^s2399-evttsvtermino/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2399_evttsvtermino.apagar', 
        name='s2399_evttsvtermino_apagar'),

url(r'^s2399-evttsvtermino/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2399_evttsvtermino.listar', 
        name='s2399_evttsvtermino'),
        
url(r'^s2399-evttsvtermino/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2399_evttsvtermino_verificar.verificar', 
        name='s2399_evttsvtermino_verificar'),
        
url(r'^s2399-evttsvtermino/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2399_evttsvtermino_verificar.recibo', 
        name='s2399_evttsvtermino_recibo'),
        
        
url(r'^s2399-evttsvtermino/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2399_evttsvtermino_verificar.duplicar',
        name='s2399_evttsvtermino_duplicar'),

url(r'^s2399-evttsvtermino/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2399_evttsvtermino_verificar.criar_alteracao',
        name='s2399_evttsvtermino_criar_alteracao'),

url(r'^s2399-evttsvtermino/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2399_evttsvtermino_verificar.criar_exclusao',
        name='s2399_evttsvtermino_criar_exclusao'),
        
url(r'^s2399-evttsvtermino/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2399_evttsvtermino_verificar.gerar_xml', 
                name='s2399_evttsvtermino_xml'),
                

url(r'^s2399-evttsvtermino/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2399_evttsvtermino_verificar.alterar_identidade',
        name='s2399_evttsvtermino_alterar_identidade'),

url(r'^s2399-evttsvtermino/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2399_evttsvtermino_verificar.abrir_evento_para_edicao',
        name='s2399_evttsvtermino_abrir_evento_para_edicao'),

url(r'^s2399-evttsvtermino/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2399_evttsvtermino_verificar.validar_evento',
        name='s2399_evttsvtermino_validar_evento'),

url(r'^s2399-evttsvtermino/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2399_evttsvtermino.salvar', 
        name='s2399_evttsvtermino_salvar'),
        

url(r'^scripts/gerar-identidade/s2399-evttsvtermino/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2399_evttsvtermino.gerar_identidade', 
        name='s2399_evttsvtermino_gerar_identidade'),



url(r'^s2400-evtcdbenefin/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2400_evtcdbenefin.apagar', 
        name='s2400_evtcdbenefin_apagar'),

url(r'^s2400-evtcdbenefin/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2400_evtcdbenefin.listar', 
        name='s2400_evtcdbenefin'),
        
url(r'^s2400-evtcdbenefin/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2400_evtcdbenefin_verificar.verificar', 
        name='s2400_evtcdbenefin_verificar'),
        
url(r'^s2400-evtcdbenefin/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2400_evtcdbenefin_verificar.recibo', 
        name='s2400_evtcdbenefin_recibo'),
        
        
url(r'^s2400-evtcdbenefin/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2400_evtcdbenefin_verificar.duplicar',
        name='s2400_evtcdbenefin_duplicar'),

url(r'^s2400-evtcdbenefin/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2400_evtcdbenefin_verificar.criar_alteracao',
        name='s2400_evtcdbenefin_criar_alteracao'),

url(r'^s2400-evtcdbenefin/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2400_evtcdbenefin_verificar.criar_exclusao',
        name='s2400_evtcdbenefin_criar_exclusao'),
        
url(r'^s2400-evtcdbenefin/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2400_evtcdbenefin_verificar.gerar_xml', 
                name='s2400_evtcdbenefin_xml'),
                

url(r'^s2400-evtcdbenefin/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2400_evtcdbenefin_verificar.alterar_identidade',
        name='s2400_evtcdbenefin_alterar_identidade'),

url(r'^s2400-evtcdbenefin/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2400_evtcdbenefin_verificar.abrir_evento_para_edicao',
        name='s2400_evtcdbenefin_abrir_evento_para_edicao'),

url(r'^s2400-evtcdbenefin/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2400_evtcdbenefin_verificar.validar_evento',
        name='s2400_evtcdbenefin_validar_evento'),

url(r'^s2400-evtcdbenefin/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2400_evtcdbenefin.salvar', 
        name='s2400_evtcdbenefin_salvar'),
        

url(r'^scripts/gerar-identidade/s2400-evtcdbenefin/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2400_evtcdbenefin.gerar_identidade', 
        name='s2400_evtcdbenefin_gerar_identidade'),



url(r'^s2405-evtcdbenefalt/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2405_evtcdbenefalt.apagar', 
        name='s2405_evtcdbenefalt_apagar'),

url(r'^s2405-evtcdbenefalt/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2405_evtcdbenefalt.listar', 
        name='s2405_evtcdbenefalt'),
        
url(r'^s2405-evtcdbenefalt/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar.verificar', 
        name='s2405_evtcdbenefalt_verificar'),
        
url(r'^s2405-evtcdbenefalt/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar.recibo', 
        name='s2405_evtcdbenefalt_recibo'),
        
        
url(r'^s2405-evtcdbenefalt/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar.duplicar',
        name='s2405_evtcdbenefalt_duplicar'),

url(r'^s2405-evtcdbenefalt/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar.criar_alteracao',
        name='s2405_evtcdbenefalt_criar_alteracao'),

url(r'^s2405-evtcdbenefalt/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar.criar_exclusao',
        name='s2405_evtcdbenefalt_criar_exclusao'),
        
url(r'^s2405-evtcdbenefalt/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar.gerar_xml', 
                name='s2405_evtcdbenefalt_xml'),
                

url(r'^s2405-evtcdbenefalt/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar.alterar_identidade',
        name='s2405_evtcdbenefalt_alterar_identidade'),

url(r'^s2405-evtcdbenefalt/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar.abrir_evento_para_edicao',
        name='s2405_evtcdbenefalt_abrir_evento_para_edicao'),

url(r'^s2405-evtcdbenefalt/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar.validar_evento',
        name='s2405_evtcdbenefalt_validar_evento'),

url(r'^s2405-evtcdbenefalt/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2405_evtcdbenefalt.salvar', 
        name='s2405_evtcdbenefalt_salvar'),
        

url(r'^scripts/gerar-identidade/s2405-evtcdbenefalt/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2405_evtcdbenefalt.gerar_identidade', 
        name='s2405_evtcdbenefalt_gerar_identidade'),



url(r'^s2410-evtcdbenin/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2410_evtcdbenin.apagar', 
        name='s2410_evtcdbenin_apagar'),

url(r'^s2410-evtcdbenin/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2410_evtcdbenin.listar', 
        name='s2410_evtcdbenin'),
        
url(r'^s2410-evtcdbenin/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2410_evtcdbenin_verificar.verificar', 
        name='s2410_evtcdbenin_verificar'),
        
url(r'^s2410-evtcdbenin/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2410_evtcdbenin_verificar.recibo', 
        name='s2410_evtcdbenin_recibo'),
        
        
url(r'^s2410-evtcdbenin/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2410_evtcdbenin_verificar.duplicar',
        name='s2410_evtcdbenin_duplicar'),

url(r'^s2410-evtcdbenin/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2410_evtcdbenin_verificar.criar_alteracao',
        name='s2410_evtcdbenin_criar_alteracao'),

url(r'^s2410-evtcdbenin/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2410_evtcdbenin_verificar.criar_exclusao',
        name='s2410_evtcdbenin_criar_exclusao'),
        
url(r'^s2410-evtcdbenin/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2410_evtcdbenin_verificar.gerar_xml', 
                name='s2410_evtcdbenin_xml'),
                

url(r'^s2410-evtcdbenin/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2410_evtcdbenin_verificar.alterar_identidade',
        name='s2410_evtcdbenin_alterar_identidade'),

url(r'^s2410-evtcdbenin/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2410_evtcdbenin_verificar.abrir_evento_para_edicao',
        name='s2410_evtcdbenin_abrir_evento_para_edicao'),

url(r'^s2410-evtcdbenin/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2410_evtcdbenin_verificar.validar_evento',
        name='s2410_evtcdbenin_validar_evento'),

url(r'^s2410-evtcdbenin/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2410_evtcdbenin.salvar', 
        name='s2410_evtcdbenin_salvar'),
        

url(r'^scripts/gerar-identidade/s2410-evtcdbenin/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2410_evtcdbenin.gerar_identidade', 
        name='s2410_evtcdbenin_gerar_identidade'),



url(r'^s2416-evtcdbenalt/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2416_evtcdbenalt.apagar', 
        name='s2416_evtcdbenalt_apagar'),

url(r'^s2416-evtcdbenalt/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2416_evtcdbenalt.listar', 
        name='s2416_evtcdbenalt'),
        
url(r'^s2416-evtcdbenalt/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2416_evtcdbenalt_verificar.verificar', 
        name='s2416_evtcdbenalt_verificar'),
        
url(r'^s2416-evtcdbenalt/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2416_evtcdbenalt_verificar.recibo', 
        name='s2416_evtcdbenalt_recibo'),
        
        
url(r'^s2416-evtcdbenalt/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2416_evtcdbenalt_verificar.duplicar',
        name='s2416_evtcdbenalt_duplicar'),

url(r'^s2416-evtcdbenalt/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2416_evtcdbenalt_verificar.criar_alteracao',
        name='s2416_evtcdbenalt_criar_alteracao'),

url(r'^s2416-evtcdbenalt/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2416_evtcdbenalt_verificar.criar_exclusao',
        name='s2416_evtcdbenalt_criar_exclusao'),
        
url(r'^s2416-evtcdbenalt/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2416_evtcdbenalt_verificar.gerar_xml', 
                name='s2416_evtcdbenalt_xml'),
                

url(r'^s2416-evtcdbenalt/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2416_evtcdbenalt_verificar.alterar_identidade',
        name='s2416_evtcdbenalt_alterar_identidade'),

url(r'^s2416-evtcdbenalt/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2416_evtcdbenalt_verificar.abrir_evento_para_edicao',
        name='s2416_evtcdbenalt_abrir_evento_para_edicao'),

url(r'^s2416-evtcdbenalt/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2416_evtcdbenalt_verificar.validar_evento',
        name='s2416_evtcdbenalt_validar_evento'),

url(r'^s2416-evtcdbenalt/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2416_evtcdbenalt.salvar', 
        name='s2416_evtcdbenalt_salvar'),
        

url(r'^scripts/gerar-identidade/s2416-evtcdbenalt/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2416_evtcdbenalt.gerar_identidade', 
        name='s2416_evtcdbenalt_gerar_identidade'),



url(r'^s2420-evtcdbenterm/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2420_evtcdbenterm.apagar', 
        name='s2420_evtcdbenterm_apagar'),

url(r'^s2420-evtcdbenterm/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2420_evtcdbenterm.listar', 
        name='s2420_evtcdbenterm'),
        
url(r'^s2420-evtcdbenterm/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2420_evtcdbenterm_verificar.verificar', 
        name='s2420_evtcdbenterm_verificar'),
        
url(r'^s2420-evtcdbenterm/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s2420_evtcdbenterm_verificar.recibo', 
        name='s2420_evtcdbenterm_recibo'),
        
        
url(r'^s2420-evtcdbenterm/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2420_evtcdbenterm_verificar.duplicar',
        name='s2420_evtcdbenterm_duplicar'),

url(r'^s2420-evtcdbenterm/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2420_evtcdbenterm_verificar.criar_alteracao',
        name='s2420_evtcdbenterm_criar_alteracao'),

url(r'^s2420-evtcdbenterm/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2420_evtcdbenterm_verificar.criar_exclusao',
        name='s2420_evtcdbenterm_criar_exclusao'),
        
url(r'^s2420-evtcdbenterm/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2420_evtcdbenterm_verificar.gerar_xml', 
                name='s2420_evtcdbenterm_xml'),
                

url(r'^s2420-evtcdbenterm/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2420_evtcdbenterm_verificar.alterar_identidade',
        name='s2420_evtcdbenterm_alterar_identidade'),

url(r'^s2420-evtcdbenterm/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2420_evtcdbenterm_verificar.abrir_evento_para_edicao',
        name='s2420_evtcdbenterm_abrir_evento_para_edicao'),

url(r'^s2420-evtcdbenterm/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s2420_evtcdbenterm_verificar.validar_evento',
        name='s2420_evtcdbenterm_validar_evento'),

url(r'^s2420-evtcdbenterm/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s2420_evtcdbenterm.salvar', 
        name='s2420_evtcdbenterm_salvar'),
        

url(r'^scripts/gerar-identidade/s2420-evtcdbenterm/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s2420_evtcdbenterm.gerar_identidade', 
        name='s2420_evtcdbenterm_gerar_identidade'),



url(r'^s3000-evtexclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s3000_evtexclusao.apagar', 
        name='s3000_evtexclusao_apagar'),

url(r'^s3000-evtexclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s3000_evtexclusao.listar', 
        name='s3000_evtexclusao'),
        
url(r'^s3000-evtexclusao/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s3000_evtexclusao_verificar.verificar', 
        name='s3000_evtexclusao_verificar'),
        
url(r'^s3000-evtexclusao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s3000_evtexclusao_verificar.recibo', 
        name='s3000_evtexclusao_recibo'),
        
        
url(r'^s3000-evtexclusao/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s3000_evtexclusao_verificar.duplicar',
        name='s3000_evtexclusao_duplicar'),

url(r'^s3000-evtexclusao/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s3000_evtexclusao_verificar.criar_alteracao',
        name='s3000_evtexclusao_criar_alteracao'),

url(r'^s3000-evtexclusao/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s3000_evtexclusao_verificar.criar_exclusao',
        name='s3000_evtexclusao_criar_exclusao'),
        
url(r'^s3000-evtexclusao/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s3000_evtexclusao_verificar.gerar_xml', 
                name='s3000_evtexclusao_xml'),
                

url(r'^s3000-evtexclusao/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s3000_evtexclusao_verificar.alterar_identidade',
        name='s3000_evtexclusao_alterar_identidade'),

url(r'^s3000-evtexclusao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s3000_evtexclusao_verificar.abrir_evento_para_edicao',
        name='s3000_evtexclusao_abrir_evento_para_edicao'),

url(r'^s3000-evtexclusao/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s3000_evtexclusao_verificar.validar_evento',
        name='s3000_evtexclusao_validar_evento'),

url(r'^s3000-evtexclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s3000_evtexclusao.salvar', 
        name='s3000_evtexclusao_salvar'),
        

url(r'^scripts/gerar-identidade/s3000-evtexclusao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s3000_evtexclusao.gerar_identidade', 
        name='s3000_evtexclusao_gerar_identidade'),



url(r'^s5001-evtbasestrab/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5001_evtbasestrab.apagar', 
        name='s5001_evtbasestrab_apagar'),

url(r'^s5001-evtbasestrab/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5001_evtbasestrab.listar', 
        name='s5001_evtbasestrab'),
        
url(r'^s5001-evtbasestrab/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5001_evtbasestrab_verificar.verificar', 
        name='s5001_evtbasestrab_verificar'),
        
url(r'^s5001-evtbasestrab/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s5001_evtbasestrab_verificar.recibo', 
        name='s5001_evtbasestrab_recibo'),
        
        
url(r'^s5001-evtbasestrab/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5001_evtbasestrab_verificar.duplicar',
        name='s5001_evtbasestrab_duplicar'),

url(r'^s5001-evtbasestrab/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5001_evtbasestrab_verificar.criar_alteracao',
        name='s5001_evtbasestrab_criar_alteracao'),

url(r'^s5001-evtbasestrab/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5001_evtbasestrab_verificar.criar_exclusao',
        name='s5001_evtbasestrab_criar_exclusao'),
        
url(r'^s5001-evtbasestrab/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5001_evtbasestrab_verificar.gerar_xml', 
                name='s5001_evtbasestrab_xml'),
                

url(r'^s5001-evtbasestrab/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5001_evtbasestrab_verificar.alterar_identidade',
        name='s5001_evtbasestrab_alterar_identidade'),

url(r'^s5001-evtbasestrab/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5001_evtbasestrab_verificar.abrir_evento_para_edicao',
        name='s5001_evtbasestrab_abrir_evento_para_edicao'),

url(r'^s5001-evtbasestrab/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5001_evtbasestrab_verificar.validar_evento',
        name='s5001_evtbasestrab_validar_evento'),

url(r'^s5001-evtbasestrab/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5001_evtbasestrab.salvar', 
        name='s5001_evtbasestrab_salvar'),
        

url(r'^scripts/gerar-identidade/s5001-evtbasestrab/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s5001_evtbasestrab.gerar_identidade', 
        name='s5001_evtbasestrab_gerar_identidade'),



url(r'^s5002-evtirrfbenef/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5002_evtirrfbenef.apagar', 
        name='s5002_evtirrfbenef_apagar'),

url(r'^s5002-evtirrfbenef/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5002_evtirrfbenef.listar', 
        name='s5002_evtirrfbenef'),
        
url(r'^s5002-evtirrfbenef/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5002_evtirrfbenef_verificar.verificar', 
        name='s5002_evtirrfbenef_verificar'),
        
url(r'^s5002-evtirrfbenef/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s5002_evtirrfbenef_verificar.recibo', 
        name='s5002_evtirrfbenef_recibo'),
        
        
url(r'^s5002-evtirrfbenef/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5002_evtirrfbenef_verificar.duplicar',
        name='s5002_evtirrfbenef_duplicar'),

url(r'^s5002-evtirrfbenef/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5002_evtirrfbenef_verificar.criar_alteracao',
        name='s5002_evtirrfbenef_criar_alteracao'),

url(r'^s5002-evtirrfbenef/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5002_evtirrfbenef_verificar.criar_exclusao',
        name='s5002_evtirrfbenef_criar_exclusao'),
        
url(r'^s5002-evtirrfbenef/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5002_evtirrfbenef_verificar.gerar_xml', 
                name='s5002_evtirrfbenef_xml'),
                

url(r'^s5002-evtirrfbenef/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5002_evtirrfbenef_verificar.alterar_identidade',
        name='s5002_evtirrfbenef_alterar_identidade'),

url(r'^s5002-evtirrfbenef/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5002_evtirrfbenef_verificar.abrir_evento_para_edicao',
        name='s5002_evtirrfbenef_abrir_evento_para_edicao'),

url(r'^s5002-evtirrfbenef/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5002_evtirrfbenef_verificar.validar_evento',
        name='s5002_evtirrfbenef_validar_evento'),

url(r'^s5002-evtirrfbenef/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5002_evtirrfbenef.salvar', 
        name='s5002_evtirrfbenef_salvar'),
        

url(r'^scripts/gerar-identidade/s5002-evtirrfbenef/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s5002_evtirrfbenef.gerar_identidade', 
        name='s5002_evtirrfbenef_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^s5011-evtcs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5011_evtcs.apagar', 
        name='s5011_evtcs_apagar'),

url(r'^s5011-evtcs/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5011_evtcs.listar', 
        name='s5011_evtcs'),
        
url(r'^s5011-evtcs/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5011_evtcs_verificar.verificar', 
        name='s5011_evtcs_verificar'),
        
url(r'^s5011-evtcs/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s5011_evtcs_verificar.recibo', 
        name='s5011_evtcs_recibo'),
        
        
url(r'^s5011-evtcs/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5011_evtcs_verificar.duplicar',
        name='s5011_evtcs_duplicar'),

url(r'^s5011-evtcs/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5011_evtcs_verificar.criar_alteracao',
        name='s5011_evtcs_criar_alteracao'),

url(r'^s5011-evtcs/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5011_evtcs_verificar.criar_exclusao',
        name='s5011_evtcs_criar_exclusao'),
        
url(r'^s5011-evtcs/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5011_evtcs_verificar.gerar_xml', 
                name='s5011_evtcs_xml'),
                

url(r'^s5011-evtcs/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5011_evtcs_verificar.alterar_identidade',
        name='s5011_evtcs_alterar_identidade'),

url(r'^s5011-evtcs/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5011_evtcs_verificar.abrir_evento_para_edicao',
        name='s5011_evtcs_abrir_evento_para_edicao'),

url(r'^s5011-evtcs/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5011_evtcs_verificar.validar_evento',
        name='s5011_evtcs_validar_evento'),

url(r'^s5011-evtcs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5011_evtcs.salvar', 
        name='s5011_evtcs_salvar'),
        

url(r'^scripts/gerar-identidade/s5011-evtcs/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s5011_evtcs.gerar_identidade', 
        name='s5011_evtcs_gerar_identidade'),



url(r'^s5012-evtirrf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5012_evtirrf.apagar', 
        name='s5012_evtirrf_apagar'),

url(r'^s5012-evtirrf/listar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5012_evtirrf.listar', 
        name='s5012_evtirrf'),
        
url(r'^s5012-evtirrf/verificar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5012_evtirrf_verificar.verificar', 
        name='s5012_evtirrf_verificar'),
        
url(r'^s5012-evtirrf/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.esocial.views.s5012_evtirrf_verificar.recibo', 
        name='s5012_evtirrf_recibo'),
        
        
url(r'^s5012-evtirrf/duplicar/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5012_evtirrf_verificar.duplicar',
        name='s5012_evtirrf_duplicar'),

url(r'^s5012-evtirrf/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5012_evtirrf_verificar.criar_alteracao',
        name='s5012_evtirrf_criar_alteracao'),

url(r'^s5012-evtirrf/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5012_evtirrf_verificar.criar_exclusao',
        name='s5012_evtirrf_criar_exclusao'),
        
url(r'^s5012-evtirrf/xml/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5012_evtirrf_verificar.gerar_xml', 
                name='s5012_evtirrf_xml'),
                

url(r'^s5012-evtirrf/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5012_evtirrf_verificar.alterar_identidade',
        name='s5012_evtirrf_alterar_identidade'),

url(r'^s5012-evtirrf/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5012_evtirrf_verificar.abrir_evento_para_edicao',
        name='s5012_evtirrf_abrir_evento_para_edicao'),

url(r'^s5012-evtirrf/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.esocial.views.s5012_evtirrf_verificar.validar_evento',
        name='s5012_evtirrf_validar_evento'),

url(r'^s5012-evtirrf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.esocial.views.s5012_evtirrf.salvar', 
        name='s5012_evtirrf_salvar'),
        

url(r'^scripts/gerar-identidade/s5012-evtirrf/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.esocial.views.s5012_evtirrf.gerar_identidade', 
        name='s5012_evtirrf_gerar_identidade'),





)