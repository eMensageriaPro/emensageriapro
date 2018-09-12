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



url(r'^r1000-evtinfocontri/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1000_evtinfocontri.apagar', 
        name='r1000_evtinfocontri_apagar'),

url(r'^r1000-evtinfocontri/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1000_evtinfocontri.listar', 
        name='r1000_evtinfocontri'),
        
url(r'^r1000-evtinfocontri/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar.verificar', 
        name='r1000_evtinfocontri_verificar'),
        
url(r'^r1000-evtinfocontri/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar.recibo', 
        name='r1000_evtinfocontri_recibo'),
        
        
url(r'^r1000-evtinfocontri/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar.duplicar',
        name='r1000_evtinfocontri_duplicar'),

url(r'^r1000-evtinfocontri/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar.criar_alteracao',
        name='r1000_evtinfocontri_criar_alteracao'),

url(r'^r1000-evtinfocontri/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar.criar_exclusao',
        name='r1000_evtinfocontri_criar_exclusao'),
        
url(r'^r1000-evtinfocontri/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar.gerar_xml', 
                name='r1000_evtinfocontri_xml'),
                

url(r'^r1000-evtinfocontri/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar.alterar_identidade',
        name='r1000_evtinfocontri_alterar_identidade'),

url(r'^r1000-evtinfocontri/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar.abrir_evento_para_edicao',
        name='r1000_evtinfocontri_abrir_evento_para_edicao'),

url(r'^r1000-evtinfocontri/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1000_evtinfocontri_verificar.validar_evento',
        name='r1000_evtinfocontri_validar_evento'),

url(r'^r1000-evtinfocontri/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1000_evtinfocontri.salvar', 
        name='r1000_evtinfocontri_salvar'),
        

url(r'^scripts/gerar-identidade/r1000-evtinfocontri/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r1000_evtinfocontri.gerar_identidade', 
        name='r1000_evtinfocontri_gerar_identidade'),



url(r'^r1070-evttabprocesso/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1070_evttabprocesso.apagar', 
        name='r1070_evttabprocesso_apagar'),

url(r'^r1070-evttabprocesso/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1070_evttabprocesso.listar', 
        name='r1070_evttabprocesso'),
        
url(r'^r1070-evttabprocesso/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar.verificar', 
        name='r1070_evttabprocesso_verificar'),
        
url(r'^r1070-evttabprocesso/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar.recibo', 
        name='r1070_evttabprocesso_recibo'),
        
        
url(r'^r1070-evttabprocesso/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar.duplicar',
        name='r1070_evttabprocesso_duplicar'),

url(r'^r1070-evttabprocesso/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar.criar_alteracao',
        name='r1070_evttabprocesso_criar_alteracao'),

url(r'^r1070-evttabprocesso/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar.criar_exclusao',
        name='r1070_evttabprocesso_criar_exclusao'),
        
url(r'^r1070-evttabprocesso/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar.gerar_xml', 
                name='r1070_evttabprocesso_xml'),
                

url(r'^r1070-evttabprocesso/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar.alterar_identidade',
        name='r1070_evttabprocesso_alterar_identidade'),

url(r'^r1070-evttabprocesso/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar.abrir_evento_para_edicao',
        name='r1070_evttabprocesso_abrir_evento_para_edicao'),

url(r'^r1070-evttabprocesso/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r1070_evttabprocesso_verificar.validar_evento',
        name='r1070_evttabprocesso_validar_evento'),

url(r'^r1070-evttabprocesso/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r1070_evttabprocesso.salvar', 
        name='r1070_evttabprocesso_salvar'),
        

url(r'^scripts/gerar-identidade/r1070-evttabprocesso/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r1070_evttabprocesso.gerar_identidade', 
        name='r1070_evttabprocesso_gerar_identidade'),



url(r'^r2010-evtservtom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2010_evtservtom.apagar', 
        name='r2010_evtservtom_apagar'),

url(r'^r2010-evtservtom/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2010_evtservtom.listar', 
        name='r2010_evtservtom'),
        
url(r'^r2010-evtservtom/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2010_evtservtom_verificar.verificar', 
        name='r2010_evtservtom_verificar'),
        
url(r'^r2010-evtservtom/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r2010_evtservtom_verificar.recibo', 
        name='r2010_evtservtom_recibo'),
        
        
url(r'^r2010-evtservtom/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2010_evtservtom_verificar.duplicar',
        name='r2010_evtservtom_duplicar'),

url(r'^r2010-evtservtom/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2010_evtservtom_verificar.criar_alteracao',
        name='r2010_evtservtom_criar_alteracao'),

url(r'^r2010-evtservtom/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2010_evtservtom_verificar.criar_exclusao',
        name='r2010_evtservtom_criar_exclusao'),
        
url(r'^r2010-evtservtom/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2010_evtservtom_verificar.gerar_xml', 
                name='r2010_evtservtom_xml'),
                

url(r'^r2010-evtservtom/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2010_evtservtom_verificar.alterar_identidade',
        name='r2010_evtservtom_alterar_identidade'),

url(r'^r2010-evtservtom/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2010_evtservtom_verificar.abrir_evento_para_edicao',
        name='r2010_evtservtom_abrir_evento_para_edicao'),

url(r'^r2010-evtservtom/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2010_evtservtom_verificar.validar_evento',
        name='r2010_evtservtom_validar_evento'),

url(r'^r2010-evtservtom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2010_evtservtom.salvar', 
        name='r2010_evtservtom_salvar'),
        

url(r'^scripts/gerar-identidade/r2010-evtservtom/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r2010_evtservtom.gerar_identidade', 
        name='r2010_evtservtom_gerar_identidade'),



url(r'^r2020-evtservprest/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2020_evtservprest.apagar', 
        name='r2020_evtservprest_apagar'),

url(r'^r2020-evtservprest/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2020_evtservprest.listar', 
        name='r2020_evtservprest'),
        
url(r'^r2020-evtservprest/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2020_evtservprest_verificar.verificar', 
        name='r2020_evtservprest_verificar'),
        
url(r'^r2020-evtservprest/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r2020_evtservprest_verificar.recibo', 
        name='r2020_evtservprest_recibo'),
        
        
url(r'^r2020-evtservprest/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2020_evtservprest_verificar.duplicar',
        name='r2020_evtservprest_duplicar'),

url(r'^r2020-evtservprest/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2020_evtservprest_verificar.criar_alteracao',
        name='r2020_evtservprest_criar_alteracao'),

url(r'^r2020-evtservprest/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2020_evtservprest_verificar.criar_exclusao',
        name='r2020_evtservprest_criar_exclusao'),
        
url(r'^r2020-evtservprest/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2020_evtservprest_verificar.gerar_xml', 
                name='r2020_evtservprest_xml'),
                

url(r'^r2020-evtservprest/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2020_evtservprest_verificar.alterar_identidade',
        name='r2020_evtservprest_alterar_identidade'),

url(r'^r2020-evtservprest/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2020_evtservprest_verificar.abrir_evento_para_edicao',
        name='r2020_evtservprest_abrir_evento_para_edicao'),

url(r'^r2020-evtservprest/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2020_evtservprest_verificar.validar_evento',
        name='r2020_evtservprest_validar_evento'),

url(r'^r2020-evtservprest/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2020_evtservprest.salvar', 
        name='r2020_evtservprest_salvar'),
        

url(r'^scripts/gerar-identidade/r2020-evtservprest/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r2020_evtservprest.gerar_identidade', 
        name='r2020_evtservprest_gerar_identidade'),



url(r'^r2030-evtassocdesprec/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec.apagar', 
        name='r2030_evtassocdesprec_apagar'),

url(r'^r2030-evtassocdesprec/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec.listar', 
        name='r2030_evtassocdesprec'),
        
url(r'^r2030-evtassocdesprec/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar.verificar', 
        name='r2030_evtassocdesprec_verificar'),
        
url(r'^r2030-evtassocdesprec/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar.recibo', 
        name='r2030_evtassocdesprec_recibo'),
        
        
url(r'^r2030-evtassocdesprec/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar.duplicar',
        name='r2030_evtassocdesprec_duplicar'),

url(r'^r2030-evtassocdesprec/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar.criar_alteracao',
        name='r2030_evtassocdesprec_criar_alteracao'),

url(r'^r2030-evtassocdesprec/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar.criar_exclusao',
        name='r2030_evtassocdesprec_criar_exclusao'),
        
url(r'^r2030-evtassocdesprec/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar.gerar_xml', 
                name='r2030_evtassocdesprec_xml'),
                

url(r'^r2030-evtassocdesprec/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar.alterar_identidade',
        name='r2030_evtassocdesprec_alterar_identidade'),

url(r'^r2030-evtassocdesprec/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar.abrir_evento_para_edicao',
        name='r2030_evtassocdesprec_abrir_evento_para_edicao'),

url(r'^r2030-evtassocdesprec/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec_verificar.validar_evento',
        name='r2030_evtassocdesprec_validar_evento'),

url(r'^r2030-evtassocdesprec/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec.salvar', 
        name='r2030_evtassocdesprec_salvar'),
        

url(r'^scripts/gerar-identidade/r2030-evtassocdesprec/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r2030_evtassocdesprec.gerar_identidade', 
        name='r2030_evtassocdesprec_gerar_identidade'),



url(r'^r2040-evtassocdesprep/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep.apagar', 
        name='r2040_evtassocdesprep_apagar'),

url(r'^r2040-evtassocdesprep/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep.listar', 
        name='r2040_evtassocdesprep'),
        
url(r'^r2040-evtassocdesprep/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar.verificar', 
        name='r2040_evtassocdesprep_verificar'),
        
url(r'^r2040-evtassocdesprep/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar.recibo', 
        name='r2040_evtassocdesprep_recibo'),
        
        
url(r'^r2040-evtassocdesprep/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar.duplicar',
        name='r2040_evtassocdesprep_duplicar'),

url(r'^r2040-evtassocdesprep/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar.criar_alteracao',
        name='r2040_evtassocdesprep_criar_alteracao'),

url(r'^r2040-evtassocdesprep/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar.criar_exclusao',
        name='r2040_evtassocdesprep_criar_exclusao'),
        
url(r'^r2040-evtassocdesprep/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar.gerar_xml', 
                name='r2040_evtassocdesprep_xml'),
                

url(r'^r2040-evtassocdesprep/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar.alterar_identidade',
        name='r2040_evtassocdesprep_alterar_identidade'),

url(r'^r2040-evtassocdesprep/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar.abrir_evento_para_edicao',
        name='r2040_evtassocdesprep_abrir_evento_para_edicao'),

url(r'^r2040-evtassocdesprep/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep_verificar.validar_evento',
        name='r2040_evtassocdesprep_validar_evento'),

url(r'^r2040-evtassocdesprep/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep.salvar', 
        name='r2040_evtassocdesprep_salvar'),
        

url(r'^scripts/gerar-identidade/r2040-evtassocdesprep/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r2040_evtassocdesprep.gerar_identidade', 
        name='r2040_evtassocdesprep_gerar_identidade'),



url(r'^r2050-evtcomprod/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2050_evtcomprod.apagar', 
        name='r2050_evtcomprod_apagar'),

url(r'^r2050-evtcomprod/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2050_evtcomprod.listar', 
        name='r2050_evtcomprod'),
        
url(r'^r2050-evtcomprod/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2050_evtcomprod_verificar.verificar', 
        name='r2050_evtcomprod_verificar'),
        
url(r'^r2050-evtcomprod/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r2050_evtcomprod_verificar.recibo', 
        name='r2050_evtcomprod_recibo'),
        
        
url(r'^r2050-evtcomprod/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2050_evtcomprod_verificar.duplicar',
        name='r2050_evtcomprod_duplicar'),

url(r'^r2050-evtcomprod/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2050_evtcomprod_verificar.criar_alteracao',
        name='r2050_evtcomprod_criar_alteracao'),

url(r'^r2050-evtcomprod/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2050_evtcomprod_verificar.criar_exclusao',
        name='r2050_evtcomprod_criar_exclusao'),
        
url(r'^r2050-evtcomprod/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2050_evtcomprod_verificar.gerar_xml', 
                name='r2050_evtcomprod_xml'),
                

url(r'^r2050-evtcomprod/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2050_evtcomprod_verificar.alterar_identidade',
        name='r2050_evtcomprod_alterar_identidade'),

url(r'^r2050-evtcomprod/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2050_evtcomprod_verificar.abrir_evento_para_edicao',
        name='r2050_evtcomprod_abrir_evento_para_edicao'),

url(r'^r2050-evtcomprod/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2050_evtcomprod_verificar.validar_evento',
        name='r2050_evtcomprod_validar_evento'),

url(r'^r2050-evtcomprod/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2050_evtcomprod.salvar', 
        name='r2050_evtcomprod_salvar'),
        

url(r'^scripts/gerar-identidade/r2050-evtcomprod/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r2050_evtcomprod.gerar_identidade', 
        name='r2050_evtcomprod_gerar_identidade'),



url(r'^r2060-evtcprb/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2060_evtcprb.apagar', 
        name='r2060_evtcprb_apagar'),

url(r'^r2060-evtcprb/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2060_evtcprb.listar', 
        name='r2060_evtcprb'),
        
url(r'^r2060-evtcprb/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2060_evtcprb_verificar.verificar', 
        name='r2060_evtcprb_verificar'),
        
url(r'^r2060-evtcprb/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r2060_evtcprb_verificar.recibo', 
        name='r2060_evtcprb_recibo'),
        
        
url(r'^r2060-evtcprb/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2060_evtcprb_verificar.duplicar',
        name='r2060_evtcprb_duplicar'),

url(r'^r2060-evtcprb/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2060_evtcprb_verificar.criar_alteracao',
        name='r2060_evtcprb_criar_alteracao'),

url(r'^r2060-evtcprb/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2060_evtcprb_verificar.criar_exclusao',
        name='r2060_evtcprb_criar_exclusao'),
        
url(r'^r2060-evtcprb/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2060_evtcprb_verificar.gerar_xml', 
                name='r2060_evtcprb_xml'),
                

url(r'^r2060-evtcprb/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2060_evtcprb_verificar.alterar_identidade',
        name='r2060_evtcprb_alterar_identidade'),

url(r'^r2060-evtcprb/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2060_evtcprb_verificar.abrir_evento_para_edicao',
        name='r2060_evtcprb_abrir_evento_para_edicao'),

url(r'^r2060-evtcprb/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2060_evtcprb_verificar.validar_evento',
        name='r2060_evtcprb_validar_evento'),

url(r'^r2060-evtcprb/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2060_evtcprb.salvar', 
        name='r2060_evtcprb_salvar'),
        

url(r'^scripts/gerar-identidade/r2060-evtcprb/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r2060_evtcprb.gerar_identidade', 
        name='r2060_evtcprb_gerar_identidade'),



url(r'^r2070-evtpgtosdivs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs.apagar', 
        name='r2070_evtpgtosdivs_apagar'),

url(r'^r2070-evtpgtosdivs/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs.listar', 
        name='r2070_evtpgtosdivs'),
        
url(r'^r2070-evtpgtosdivs/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar.verificar', 
        name='r2070_evtpgtosdivs_verificar'),
        
url(r'^r2070-evtpgtosdivs/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar.recibo', 
        name='r2070_evtpgtosdivs_recibo'),
        
        
url(r'^r2070-evtpgtosdivs/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar.duplicar',
        name='r2070_evtpgtosdivs_duplicar'),

url(r'^r2070-evtpgtosdivs/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar.criar_alteracao',
        name='r2070_evtpgtosdivs_criar_alteracao'),

url(r'^r2070-evtpgtosdivs/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar.criar_exclusao',
        name='r2070_evtpgtosdivs_criar_exclusao'),
        
url(r'^r2070-evtpgtosdivs/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar.gerar_xml', 
                name='r2070_evtpgtosdivs_xml'),
                

url(r'^r2070-evtpgtosdivs/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar.alterar_identidade',
        name='r2070_evtpgtosdivs_alterar_identidade'),

url(r'^r2070-evtpgtosdivs/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar.abrir_evento_para_edicao',
        name='r2070_evtpgtosdivs_abrir_evento_para_edicao'),

url(r'^r2070-evtpgtosdivs/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs_verificar.validar_evento',
        name='r2070_evtpgtosdivs_validar_evento'),

url(r'^r2070-evtpgtosdivs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs.salvar', 
        name='r2070_evtpgtosdivs_salvar'),
        

url(r'^scripts/gerar-identidade/r2070-evtpgtosdivs/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r2070_evtpgtosdivs.gerar_identidade', 
        name='r2070_evtpgtosdivs_gerar_identidade'),



url(r'^r2098-evtreabreevper/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2098_evtreabreevper.apagar', 
        name='r2098_evtreabreevper_apagar'),

url(r'^r2098-evtreabreevper/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2098_evtreabreevper.listar', 
        name='r2098_evtreabreevper'),
        
url(r'^r2098-evtreabreevper/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar.verificar', 
        name='r2098_evtreabreevper_verificar'),
        
url(r'^r2098-evtreabreevper/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar.recibo', 
        name='r2098_evtreabreevper_recibo'),
        
        
url(r'^r2098-evtreabreevper/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar.duplicar',
        name='r2098_evtreabreevper_duplicar'),

url(r'^r2098-evtreabreevper/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar.criar_alteracao',
        name='r2098_evtreabreevper_criar_alteracao'),

url(r'^r2098-evtreabreevper/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar.criar_exclusao',
        name='r2098_evtreabreevper_criar_exclusao'),
        
url(r'^r2098-evtreabreevper/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar.gerar_xml', 
                name='r2098_evtreabreevper_xml'),
                

url(r'^r2098-evtreabreevper/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar.alterar_identidade',
        name='r2098_evtreabreevper_alterar_identidade'),

url(r'^r2098-evtreabreevper/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar.abrir_evento_para_edicao',
        name='r2098_evtreabreevper_abrir_evento_para_edicao'),

url(r'^r2098-evtreabreevper/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar.validar_evento',
        name='r2098_evtreabreevper_validar_evento'),

url(r'^r2098-evtreabreevper/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2098_evtreabreevper.salvar', 
        name='r2098_evtreabreevper_salvar'),
        

url(r'^scripts/gerar-identidade/r2098-evtreabreevper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r2098_evtreabreevper.gerar_identidade', 
        name='r2098_evtreabreevper_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^r2099-evtfechaevper/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2099_evtfechaevper.apagar', 
        name='r2099_evtfechaevper_apagar'),

url(r'^r2099-evtfechaevper/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2099_evtfechaevper.listar', 
        name='r2099_evtfechaevper'),
        
url(r'^r2099-evtfechaevper/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar.verificar', 
        name='r2099_evtfechaevper_verificar'),
        
url(r'^r2099-evtfechaevper/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar.recibo', 
        name='r2099_evtfechaevper_recibo'),
        
        
url(r'^r2099-evtfechaevper/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar.duplicar',
        name='r2099_evtfechaevper_duplicar'),

url(r'^r2099-evtfechaevper/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar.criar_alteracao',
        name='r2099_evtfechaevper_criar_alteracao'),

url(r'^r2099-evtfechaevper/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar.criar_exclusao',
        name='r2099_evtfechaevper_criar_exclusao'),
        
url(r'^r2099-evtfechaevper/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar.gerar_xml', 
                name='r2099_evtfechaevper_xml'),
                

url(r'^r2099-evtfechaevper/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar.alterar_identidade',
        name='r2099_evtfechaevper_alterar_identidade'),

url(r'^r2099-evtfechaevper/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar.abrir_evento_para_edicao',
        name='r2099_evtfechaevper_abrir_evento_para_edicao'),

url(r'^r2099-evtfechaevper/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r2099_evtfechaevper_verificar.validar_evento',
        name='r2099_evtfechaevper_validar_evento'),

url(r'^r2099-evtfechaevper/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r2099_evtfechaevper.salvar', 
        name='r2099_evtfechaevper_salvar'),
        

url(r'^scripts/gerar-identidade/r2099-evtfechaevper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r2099_evtfechaevper.gerar_identidade', 
        name='r2099_evtfechaevper_gerar_identidade'),



url(r'^r3010-evtespdesportivo/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo.apagar', 
        name='r3010_evtespdesportivo_apagar'),

url(r'^r3010-evtespdesportivo/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo.listar', 
        name='r3010_evtespdesportivo'),
        
url(r'^r3010-evtespdesportivo/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar.verificar', 
        name='r3010_evtespdesportivo_verificar'),
        
url(r'^r3010-evtespdesportivo/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar.recibo', 
        name='r3010_evtespdesportivo_recibo'),
        
        
url(r'^r3010-evtespdesportivo/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar.duplicar',
        name='r3010_evtespdesportivo_duplicar'),

url(r'^r3010-evtespdesportivo/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar.criar_alteracao',
        name='r3010_evtespdesportivo_criar_alteracao'),

url(r'^r3010-evtespdesportivo/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar.criar_exclusao',
        name='r3010_evtespdesportivo_criar_exclusao'),
        
url(r'^r3010-evtespdesportivo/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar.gerar_xml', 
                name='r3010_evtespdesportivo_xml'),
                

url(r'^r3010-evtespdesportivo/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar.alterar_identidade',
        name='r3010_evtespdesportivo_alterar_identidade'),

url(r'^r3010-evtespdesportivo/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar.abrir_evento_para_edicao',
        name='r3010_evtespdesportivo_abrir_evento_para_edicao'),

url(r'^r3010-evtespdesportivo/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo_verificar.validar_evento',
        name='r3010_evtespdesportivo_validar_evento'),

url(r'^r3010-evtespdesportivo/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo.salvar', 
        name='r3010_evtespdesportivo_salvar'),
        

url(r'^scripts/gerar-identidade/r3010-evtespdesportivo/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r3010_evtespdesportivo.gerar_identidade', 
        name='r3010_evtespdesportivo_gerar_identidade'),



url(r'^r5001-evttotal/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5001_evttotal.apagar', 
        name='r5001_evttotal_apagar'),

url(r'^r5001-evttotal/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5001_evttotal.listar', 
        name='r5001_evttotal'),
        
url(r'^r5001-evttotal/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5001_evttotal_verificar.verificar', 
        name='r5001_evttotal_verificar'),
        
url(r'^r5001-evttotal/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r5001_evttotal_verificar.recibo', 
        name='r5001_evttotal_recibo'),
        
        
url(r'^r5001-evttotal/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5001_evttotal_verificar.duplicar',
        name='r5001_evttotal_duplicar'),

url(r'^r5001-evttotal/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5001_evttotal_verificar.criar_alteracao',
        name='r5001_evttotal_criar_alteracao'),

url(r'^r5001-evttotal/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5001_evttotal_verificar.criar_exclusao',
        name='r5001_evttotal_criar_exclusao'),
        
url(r'^r5001-evttotal/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5001_evttotal_verificar.gerar_xml', 
                name='r5001_evttotal_xml'),
                

url(r'^r5001-evttotal/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5001_evttotal_verificar.alterar_identidade',
        name='r5001_evttotal_alterar_identidade'),

url(r'^r5001-evttotal/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5001_evttotal_verificar.abrir_evento_para_edicao',
        name='r5001_evttotal_abrir_evento_para_edicao'),

url(r'^r5001-evttotal/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5001_evttotal_verificar.validar_evento',
        name='r5001_evttotal_validar_evento'),

url(r'^r5001-evttotal/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5001_evttotal.salvar', 
        name='r5001_evttotal_salvar'),
        

url(r'^scripts/gerar-identidade/r5001-evttotal/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r5001_evttotal.gerar_identidade', 
        name='r5001_evttotal_gerar_identidade'),



url(r'^r5011-evttotalcontrib/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib.apagar', 
        name='r5011_evttotalcontrib_apagar'),

url(r'^r5011-evttotalcontrib/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib.listar', 
        name='r5011_evttotalcontrib'),
        
url(r'^r5011-evttotalcontrib/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar.verificar', 
        name='r5011_evttotalcontrib_verificar'),
        
url(r'^r5011-evttotalcontrib/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar.recibo', 
        name='r5011_evttotalcontrib_recibo'),
        
        
url(r'^r5011-evttotalcontrib/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar.duplicar',
        name='r5011_evttotalcontrib_duplicar'),

url(r'^r5011-evttotalcontrib/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar.criar_alteracao',
        name='r5011_evttotalcontrib_criar_alteracao'),

url(r'^r5011-evttotalcontrib/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar.criar_exclusao',
        name='r5011_evttotalcontrib_criar_exclusao'),
        
url(r'^r5011-evttotalcontrib/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar.gerar_xml', 
                name='r5011_evttotalcontrib_xml'),
                

url(r'^r5011-evttotalcontrib/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar.alterar_identidade',
        name='r5011_evttotalcontrib_alterar_identidade'),

url(r'^r5011-evttotalcontrib/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar.abrir_evento_para_edicao',
        name='r5011_evttotalcontrib_abrir_evento_para_edicao'),

url(r'^r5011-evttotalcontrib/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib_verificar.validar_evento',
        name='r5011_evttotalcontrib_validar_evento'),

url(r'^r5011-evttotalcontrib/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib.salvar', 
        name='r5011_evttotalcontrib_salvar'),
        

url(r'^scripts/gerar-identidade/r5011-evttotalcontrib/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r5011_evttotalcontrib.gerar_identidade', 
        name='r5011_evttotalcontrib_gerar_identidade'),



url(r'^r9000-evtexclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r9000_evtexclusao.apagar', 
        name='r9000_evtexclusao_apagar'),

url(r'^r9000-evtexclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r9000_evtexclusao.listar', 
        name='r9000_evtexclusao'),
        
url(r'^r9000-evtexclusao/verificar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r9000_evtexclusao_verificar.verificar', 
        name='r9000_evtexclusao_verificar'),
        
url(r'^r9000-evtexclusao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        'emensageriapro.efdreinf.views.r9000_evtexclusao_verificar.recibo', 
        name='r9000_evtexclusao_recibo'),
        
        
url(r'^r9000-evtexclusao/duplicar/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r9000_evtexclusao_verificar.duplicar',
        name='r9000_evtexclusao_duplicar'),

url(r'^r9000-evtexclusao/criar-alteracao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r9000_evtexclusao_verificar.criar_alteracao',
        name='r9000_evtexclusao_criar_alteracao'),

url(r'^r9000-evtexclusao/criar-exclusao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r9000_evtexclusao_verificar.criar_exclusao',
        name='r9000_evtexclusao_criar_exclusao'),
        
url(r'^r9000-evtexclusao/xml/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r9000_evtexclusao_verificar.gerar_xml', 
                name='r9000_evtexclusao_xml'),
                

url(r'^r9000-evtexclusao/alterar-identidade/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r9000_evtexclusao_verificar.alterar_identidade',
        name='r9000_evtexclusao_alterar_identidade'),

url(r'^r9000-evtexclusao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r9000_evtexclusao_verificar.abrir_evento_para_edicao',
        name='r9000_evtexclusao_abrir_evento_para_edicao'),

url(r'^r9000-evtexclusao/validar-evento/(?P<hash>.*)/$',
        'emensageriapro.efdreinf.views.r9000_evtexclusao_verificar.validar_evento',
        name='r9000_evtexclusao_validar_evento'),

url(r'^r9000-evtexclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.efdreinf.views.r9000_evtexclusao.salvar', 
        name='r9000_evtexclusao_salvar'),
        

url(r'^scripts/gerar-identidade/r9000-evtexclusao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageriapro.efdreinf.views.r9000_evtexclusao.gerar_identidade', 
        name='r9000_evtexclusao_gerar_identidade'),





)