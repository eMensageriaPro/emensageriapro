#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_apagar as r1000_evtinfocontri_apagar_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_listar as r1000_evtinfocontri_listar_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_salvar as r1000_evtinfocontri_salvar_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_api as r1000_evtinfocontri_api_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_gerar_identidade as r1000_evtinfocontri_gerar_identidade_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_verificar as r1000_evtinfocontri_verificar_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_importar as r1000_evtinfocontri_importar_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_validar as r1000_evtinfocontri_validar_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_recibos as r1000_evtinfocontri_recibos_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_gerar_xml as r1000_evtinfocontri_gerar_xml_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_criar_alteracao as r1000_evtinfocontri_criar_alteracao_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_validar_evento as r1000_evtinfocontri_validar_evento_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_abrir_evento_para_edicao as r1000_evtinfocontri_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_alterar_identidade as r1000_evtinfocontri_alterar_identidade_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_criar_exclusao as r1000_evtinfocontri_criar_exclusao_views
from emensageriapro.efdreinf.views import r1000_evtinfocontri_duplicar as r1000_evtinfocontri_duplicar_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_apagar as r1070_evttabprocesso_apagar_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_listar as r1070_evttabprocesso_listar_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_salvar as r1070_evttabprocesso_salvar_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_api as r1070_evttabprocesso_api_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_gerar_identidade as r1070_evttabprocesso_gerar_identidade_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_verificar as r1070_evttabprocesso_verificar_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_importar as r1070_evttabprocesso_importar_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_validar as r1070_evttabprocesso_validar_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_recibos as r1070_evttabprocesso_recibos_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_gerar_xml as r1070_evttabprocesso_gerar_xml_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_criar_alteracao as r1070_evttabprocesso_criar_alteracao_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_validar_evento as r1070_evttabprocesso_validar_evento_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_abrir_evento_para_edicao as r1070_evttabprocesso_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_alterar_identidade as r1070_evttabprocesso_alterar_identidade_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_criar_exclusao as r1070_evttabprocesso_criar_exclusao_views
from emensageriapro.efdreinf.views import r1070_evttabprocesso_duplicar as r1070_evttabprocesso_duplicar_views
from emensageriapro.efdreinf.views import r2010_evtservtom_apagar as r2010_evtservtom_apagar_views
from emensageriapro.efdreinf.views import r2010_evtservtom_listar as r2010_evtservtom_listar_views
from emensageriapro.efdreinf.views import r2010_evtservtom_salvar as r2010_evtservtom_salvar_views
from emensageriapro.efdreinf.views import r2010_evtservtom_api as r2010_evtservtom_api_views
from emensageriapro.efdreinf.views import r2010_evtservtom_gerar_identidade as r2010_evtservtom_gerar_identidade_views
from emensageriapro.efdreinf.views import r2010_evtservtom_verificar as r2010_evtservtom_verificar_views
from emensageriapro.efdreinf.views import r2010_evtservtom_importar as r2010_evtservtom_importar_views
from emensageriapro.efdreinf.views import r2010_evtservtom_validar as r2010_evtservtom_validar_views
from emensageriapro.efdreinf.views import r2010_evtservtom_recibos as r2010_evtservtom_recibos_views
from emensageriapro.efdreinf.views import r2010_evtservtom_gerar_xml as r2010_evtservtom_gerar_xml_views
from emensageriapro.efdreinf.views import r2010_evtservtom_criar_alteracao as r2010_evtservtom_criar_alteracao_views
from emensageriapro.efdreinf.views import r2010_evtservtom_validar_evento as r2010_evtservtom_validar_evento_views
from emensageriapro.efdreinf.views import r2010_evtservtom_abrir_evento_para_edicao as r2010_evtservtom_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r2010_evtservtom_alterar_identidade as r2010_evtservtom_alterar_identidade_views
from emensageriapro.efdreinf.views import r2010_evtservtom_criar_exclusao as r2010_evtservtom_criar_exclusao_views
from emensageriapro.efdreinf.views import r2010_evtservtom_duplicar as r2010_evtservtom_duplicar_views
from emensageriapro.efdreinf.views import r2020_evtservprest_apagar as r2020_evtservprest_apagar_views
from emensageriapro.efdreinf.views import r2020_evtservprest_listar as r2020_evtservprest_listar_views
from emensageriapro.efdreinf.views import r2020_evtservprest_salvar as r2020_evtservprest_salvar_views
from emensageriapro.efdreinf.views import r2020_evtservprest_api as r2020_evtservprest_api_views
from emensageriapro.efdreinf.views import r2020_evtservprest_gerar_identidade as r2020_evtservprest_gerar_identidade_views
from emensageriapro.efdreinf.views import r2020_evtservprest_verificar as r2020_evtservprest_verificar_views
from emensageriapro.efdreinf.views import r2020_evtservprest_importar as r2020_evtservprest_importar_views
from emensageriapro.efdreinf.views import r2020_evtservprest_validar as r2020_evtservprest_validar_views
from emensageriapro.efdreinf.views import r2020_evtservprest_recibos as r2020_evtservprest_recibos_views
from emensageriapro.efdreinf.views import r2020_evtservprest_gerar_xml as r2020_evtservprest_gerar_xml_views
from emensageriapro.efdreinf.views import r2020_evtservprest_criar_alteracao as r2020_evtservprest_criar_alteracao_views
from emensageriapro.efdreinf.views import r2020_evtservprest_validar_evento as r2020_evtservprest_validar_evento_views
from emensageriapro.efdreinf.views import r2020_evtservprest_abrir_evento_para_edicao as r2020_evtservprest_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r2020_evtservprest_alterar_identidade as r2020_evtservprest_alterar_identidade_views
from emensageriapro.efdreinf.views import r2020_evtservprest_criar_exclusao as r2020_evtservprest_criar_exclusao_views
from emensageriapro.efdreinf.views import r2020_evtservprest_duplicar as r2020_evtservprest_duplicar_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_apagar as r2030_evtassocdesprec_apagar_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_listar as r2030_evtassocdesprec_listar_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_salvar as r2030_evtassocdesprec_salvar_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_api as r2030_evtassocdesprec_api_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_gerar_identidade as r2030_evtassocdesprec_gerar_identidade_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_verificar as r2030_evtassocdesprec_verificar_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_importar as r2030_evtassocdesprec_importar_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_validar as r2030_evtassocdesprec_validar_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_recibos as r2030_evtassocdesprec_recibos_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_gerar_xml as r2030_evtassocdesprec_gerar_xml_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_criar_alteracao as r2030_evtassocdesprec_criar_alteracao_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_validar_evento as r2030_evtassocdesprec_validar_evento_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_abrir_evento_para_edicao as r2030_evtassocdesprec_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_alterar_identidade as r2030_evtassocdesprec_alterar_identidade_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_criar_exclusao as r2030_evtassocdesprec_criar_exclusao_views
from emensageriapro.efdreinf.views import r2030_evtassocdesprec_duplicar as r2030_evtassocdesprec_duplicar_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_apagar as r2040_evtassocdesprep_apagar_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_listar as r2040_evtassocdesprep_listar_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_salvar as r2040_evtassocdesprep_salvar_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_api as r2040_evtassocdesprep_api_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_gerar_identidade as r2040_evtassocdesprep_gerar_identidade_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_verificar as r2040_evtassocdesprep_verificar_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_importar as r2040_evtassocdesprep_importar_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_validar as r2040_evtassocdesprep_validar_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_recibos as r2040_evtassocdesprep_recibos_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_gerar_xml as r2040_evtassocdesprep_gerar_xml_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_criar_alteracao as r2040_evtassocdesprep_criar_alteracao_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_validar_evento as r2040_evtassocdesprep_validar_evento_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_abrir_evento_para_edicao as r2040_evtassocdesprep_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_alterar_identidade as r2040_evtassocdesprep_alterar_identidade_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_criar_exclusao as r2040_evtassocdesprep_criar_exclusao_views
from emensageriapro.efdreinf.views import r2040_evtassocdesprep_duplicar as r2040_evtassocdesprep_duplicar_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_apagar as r2050_evtcomprod_apagar_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_listar as r2050_evtcomprod_listar_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_salvar as r2050_evtcomprod_salvar_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_api as r2050_evtcomprod_api_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_gerar_identidade as r2050_evtcomprod_gerar_identidade_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_verificar as r2050_evtcomprod_verificar_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_importar as r2050_evtcomprod_importar_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_validar as r2050_evtcomprod_validar_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_recibos as r2050_evtcomprod_recibos_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_gerar_xml as r2050_evtcomprod_gerar_xml_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_criar_alteracao as r2050_evtcomprod_criar_alteracao_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_validar_evento as r2050_evtcomprod_validar_evento_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_abrir_evento_para_edicao as r2050_evtcomprod_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_alterar_identidade as r2050_evtcomprod_alterar_identidade_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_criar_exclusao as r2050_evtcomprod_criar_exclusao_views
from emensageriapro.efdreinf.views import r2050_evtcomprod_duplicar as r2050_evtcomprod_duplicar_views
from emensageriapro.efdreinf.views import r2060_evtcprb_apagar as r2060_evtcprb_apagar_views
from emensageriapro.efdreinf.views import r2060_evtcprb_listar as r2060_evtcprb_listar_views
from emensageriapro.efdreinf.views import r2060_evtcprb_salvar as r2060_evtcprb_salvar_views
from emensageriapro.efdreinf.views import r2060_evtcprb_api as r2060_evtcprb_api_views
from emensageriapro.efdreinf.views import r2060_evtcprb_gerar_identidade as r2060_evtcprb_gerar_identidade_views
from emensageriapro.efdreinf.views import r2060_evtcprb_verificar as r2060_evtcprb_verificar_views
from emensageriapro.efdreinf.views import r2060_evtcprb_importar as r2060_evtcprb_importar_views
from emensageriapro.efdreinf.views import r2060_evtcprb_validar as r2060_evtcprb_validar_views
from emensageriapro.efdreinf.views import r2060_evtcprb_recibos as r2060_evtcprb_recibos_views
from emensageriapro.efdreinf.views import r2060_evtcprb_gerar_xml as r2060_evtcprb_gerar_xml_views
from emensageriapro.efdreinf.views import r2060_evtcprb_criar_alteracao as r2060_evtcprb_criar_alteracao_views
from emensageriapro.efdreinf.views import r2060_evtcprb_validar_evento as r2060_evtcprb_validar_evento_views
from emensageriapro.efdreinf.views import r2060_evtcprb_abrir_evento_para_edicao as r2060_evtcprb_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r2060_evtcprb_alterar_identidade as r2060_evtcprb_alterar_identidade_views
from emensageriapro.efdreinf.views import r2060_evtcprb_criar_exclusao as r2060_evtcprb_criar_exclusao_views
from emensageriapro.efdreinf.views import r2060_evtcprb_duplicar as r2060_evtcprb_duplicar_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_apagar as r2070_evtpgtosdivs_apagar_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_listar as r2070_evtpgtosdivs_listar_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_salvar as r2070_evtpgtosdivs_salvar_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_api as r2070_evtpgtosdivs_api_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_gerar_identidade as r2070_evtpgtosdivs_gerar_identidade_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_verificar as r2070_evtpgtosdivs_verificar_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_importar as r2070_evtpgtosdivs_importar_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_validar as r2070_evtpgtosdivs_validar_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_recibos as r2070_evtpgtosdivs_recibos_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_gerar_xml as r2070_evtpgtosdivs_gerar_xml_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_criar_alteracao as r2070_evtpgtosdivs_criar_alteracao_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_validar_evento as r2070_evtpgtosdivs_validar_evento_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_abrir_evento_para_edicao as r2070_evtpgtosdivs_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_alterar_identidade as r2070_evtpgtosdivs_alterar_identidade_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_criar_exclusao as r2070_evtpgtosdivs_criar_exclusao_views
from emensageriapro.efdreinf.views import r2070_evtpgtosdivs_duplicar as r2070_evtpgtosdivs_duplicar_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_apagar as r2098_evtreabreevper_apagar_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_listar as r2098_evtreabreevper_listar_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_salvar as r2098_evtreabreevper_salvar_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_api as r2098_evtreabreevper_api_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_gerar_identidade as r2098_evtreabreevper_gerar_identidade_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_verificar as r2098_evtreabreevper_verificar_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_importar as r2098_evtreabreevper_importar_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_validar as r2098_evtreabreevper_validar_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_recibos as r2098_evtreabreevper_recibos_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_gerar_xml as r2098_evtreabreevper_gerar_xml_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_criar_alteracao as r2098_evtreabreevper_criar_alteracao_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_validar_evento as r2098_evtreabreevper_validar_evento_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_abrir_evento_para_edicao as r2098_evtreabreevper_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_alterar_identidade as r2098_evtreabreevper_alterar_identidade_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_criar_exclusao as r2098_evtreabreevper_criar_exclusao_views
from emensageriapro.efdreinf.views import r2098_evtreabreevper_duplicar as r2098_evtreabreevper_duplicar_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_apagar as r2099_evtfechaevper_apagar_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_listar as r2099_evtfechaevper_listar_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_salvar as r2099_evtfechaevper_salvar_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_api as r2099_evtfechaevper_api_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_gerar_identidade as r2099_evtfechaevper_gerar_identidade_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_verificar as r2099_evtfechaevper_verificar_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_importar as r2099_evtfechaevper_importar_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_validar as r2099_evtfechaevper_validar_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_recibos as r2099_evtfechaevper_recibos_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_gerar_xml as r2099_evtfechaevper_gerar_xml_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_criar_alteracao as r2099_evtfechaevper_criar_alteracao_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_validar_evento as r2099_evtfechaevper_validar_evento_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_abrir_evento_para_edicao as r2099_evtfechaevper_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_alterar_identidade as r2099_evtfechaevper_alterar_identidade_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_criar_exclusao as r2099_evtfechaevper_criar_exclusao_views
from emensageriapro.efdreinf.views import r2099_evtfechaevper_duplicar as r2099_evtfechaevper_duplicar_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_apagar as r3010_evtespdesportivo_apagar_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_listar as r3010_evtespdesportivo_listar_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_salvar as r3010_evtespdesportivo_salvar_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_api as r3010_evtespdesportivo_api_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_gerar_identidade as r3010_evtespdesportivo_gerar_identidade_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_verificar as r3010_evtespdesportivo_verificar_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_importar as r3010_evtespdesportivo_importar_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_validar as r3010_evtespdesportivo_validar_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_recibos as r3010_evtespdesportivo_recibos_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_gerar_xml as r3010_evtespdesportivo_gerar_xml_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_criar_alteracao as r3010_evtespdesportivo_criar_alteracao_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_validar_evento as r3010_evtespdesportivo_validar_evento_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_abrir_evento_para_edicao as r3010_evtespdesportivo_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_alterar_identidade as r3010_evtespdesportivo_alterar_identidade_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_criar_exclusao as r3010_evtespdesportivo_criar_exclusao_views
from emensageriapro.efdreinf.views import r3010_evtespdesportivo_duplicar as r3010_evtespdesportivo_duplicar_views
from emensageriapro.efdreinf.views import r4010_evtretpf_apagar as r4010_evtretpf_apagar_views
from emensageriapro.efdreinf.views import r4010_evtretpf_listar as r4010_evtretpf_listar_views
from emensageriapro.efdreinf.views import r4010_evtretpf_salvar as r4010_evtretpf_salvar_views
from emensageriapro.efdreinf.views import r4010_evtretpf_api as r4010_evtretpf_api_views
from emensageriapro.efdreinf.views import r4010_evtretpf_gerar_identidade as r4010_evtretpf_gerar_identidade_views
from emensageriapro.efdreinf.views import r4010_evtretpf_verificar as r4010_evtretpf_verificar_views
from emensageriapro.efdreinf.views import r4010_evtretpf_importar as r4010_evtretpf_importar_views
from emensageriapro.efdreinf.views import r4010_evtretpf_validar as r4010_evtretpf_validar_views
from emensageriapro.efdreinf.views import r4010_evtretpf_recibos as r4010_evtretpf_recibos_views
from emensageriapro.efdreinf.views import r4010_evtretpf_gerar_xml as r4010_evtretpf_gerar_xml_views
from emensageriapro.efdreinf.views import r4010_evtretpf_criar_alteracao as r4010_evtretpf_criar_alteracao_views
from emensageriapro.efdreinf.views import r4010_evtretpf_validar_evento as r4010_evtretpf_validar_evento_views
from emensageriapro.efdreinf.views import r4010_evtretpf_abrir_evento_para_edicao as r4010_evtretpf_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r4010_evtretpf_alterar_identidade as r4010_evtretpf_alterar_identidade_views
from emensageriapro.efdreinf.views import r4010_evtretpf_criar_exclusao as r4010_evtretpf_criar_exclusao_views
from emensageriapro.efdreinf.views import r4010_evtretpf_duplicar as r4010_evtretpf_duplicar_views
from emensageriapro.efdreinf.views import r4020_evtretpj_apagar as r4020_evtretpj_apagar_views
from emensageriapro.efdreinf.views import r4020_evtretpj_listar as r4020_evtretpj_listar_views
from emensageriapro.efdreinf.views import r4020_evtretpj_salvar as r4020_evtretpj_salvar_views
from emensageriapro.efdreinf.views import r4020_evtretpj_api as r4020_evtretpj_api_views
from emensageriapro.efdreinf.views import r4020_evtretpj_gerar_identidade as r4020_evtretpj_gerar_identidade_views
from emensageriapro.efdreinf.views import r4020_evtretpj_verificar as r4020_evtretpj_verificar_views
from emensageriapro.efdreinf.views import r4020_evtretpj_importar as r4020_evtretpj_importar_views
from emensageriapro.efdreinf.views import r4020_evtretpj_validar as r4020_evtretpj_validar_views
from emensageriapro.efdreinf.views import r4020_evtretpj_recibos as r4020_evtretpj_recibos_views
from emensageriapro.efdreinf.views import r4020_evtretpj_gerar_xml as r4020_evtretpj_gerar_xml_views
from emensageriapro.efdreinf.views import r4020_evtretpj_criar_alteracao as r4020_evtretpj_criar_alteracao_views
from emensageriapro.efdreinf.views import r4020_evtretpj_validar_evento as r4020_evtretpj_validar_evento_views
from emensageriapro.efdreinf.views import r4020_evtretpj_abrir_evento_para_edicao as r4020_evtretpj_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r4020_evtretpj_alterar_identidade as r4020_evtretpj_alterar_identidade_views
from emensageriapro.efdreinf.views import r4020_evtretpj_criar_exclusao as r4020_evtretpj_criar_exclusao_views
from emensageriapro.efdreinf.views import r4020_evtretpj_duplicar as r4020_evtretpj_duplicar_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_apagar as r4040_evtbenefnid_apagar_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_listar as r4040_evtbenefnid_listar_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_salvar as r4040_evtbenefnid_salvar_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_api as r4040_evtbenefnid_api_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_gerar_identidade as r4040_evtbenefnid_gerar_identidade_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_verificar as r4040_evtbenefnid_verificar_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_importar as r4040_evtbenefnid_importar_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_validar as r4040_evtbenefnid_validar_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_recibos as r4040_evtbenefnid_recibos_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_gerar_xml as r4040_evtbenefnid_gerar_xml_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_criar_alteracao as r4040_evtbenefnid_criar_alteracao_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_validar_evento as r4040_evtbenefnid_validar_evento_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_abrir_evento_para_edicao as r4040_evtbenefnid_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_alterar_identidade as r4040_evtbenefnid_alterar_identidade_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_criar_exclusao as r4040_evtbenefnid_criar_exclusao_views
from emensageriapro.efdreinf.views import r4040_evtbenefnid_duplicar as r4040_evtbenefnid_duplicar_views
from emensageriapro.efdreinf.views import r4098_evtreab_apagar as r4098_evtreab_apagar_views
from emensageriapro.efdreinf.views import r4098_evtreab_listar as r4098_evtreab_listar_views
from emensageriapro.efdreinf.views import r4098_evtreab_salvar as r4098_evtreab_salvar_views
from emensageriapro.efdreinf.views import r4098_evtreab_api as r4098_evtreab_api_views
from emensageriapro.efdreinf.views import r4098_evtreab_gerar_identidade as r4098_evtreab_gerar_identidade_views
from emensageriapro.efdreinf.views import r4098_evtreab_verificar as r4098_evtreab_verificar_views
from emensageriapro.efdreinf.views import r4098_evtreab_importar as r4098_evtreab_importar_views
from emensageriapro.efdreinf.views import r4098_evtreab_validar as r4098_evtreab_validar_views
from emensageriapro.efdreinf.views import r4098_evtreab_recibos as r4098_evtreab_recibos_views
from emensageriapro.efdreinf.views import r4098_evtreab_gerar_xml as r4098_evtreab_gerar_xml_views
from emensageriapro.efdreinf.views import r4098_evtreab_criar_alteracao as r4098_evtreab_criar_alteracao_views
from emensageriapro.efdreinf.views import r4098_evtreab_validar_evento as r4098_evtreab_validar_evento_views
from emensageriapro.efdreinf.views import r4098_evtreab_abrir_evento_para_edicao as r4098_evtreab_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r4098_evtreab_alterar_identidade as r4098_evtreab_alterar_identidade_views
from emensageriapro.efdreinf.views import r4098_evtreab_criar_exclusao as r4098_evtreab_criar_exclusao_views
from emensageriapro.efdreinf.views import r4098_evtreab_duplicar as r4098_evtreab_duplicar_views
from emensageriapro.efdreinf.views import r4099_evtfech_apagar as r4099_evtfech_apagar_views
from emensageriapro.efdreinf.views import r4099_evtfech_listar as r4099_evtfech_listar_views
from emensageriapro.efdreinf.views import r4099_evtfech_salvar as r4099_evtfech_salvar_views
from emensageriapro.efdreinf.views import r4099_evtfech_api as r4099_evtfech_api_views
from emensageriapro.efdreinf.views import r4099_evtfech_gerar_identidade as r4099_evtfech_gerar_identidade_views
from emensageriapro.efdreinf.views import r4099_evtfech_verificar as r4099_evtfech_verificar_views
from emensageriapro.efdreinf.views import r4099_evtfech_importar as r4099_evtfech_importar_views
from emensageriapro.efdreinf.views import r4099_evtfech_validar as r4099_evtfech_validar_views
from emensageriapro.efdreinf.views import r4099_evtfech_recibos as r4099_evtfech_recibos_views
from emensageriapro.efdreinf.views import r4099_evtfech_gerar_xml as r4099_evtfech_gerar_xml_views
from emensageriapro.efdreinf.views import r4099_evtfech_criar_alteracao as r4099_evtfech_criar_alteracao_views
from emensageriapro.efdreinf.views import r4099_evtfech_validar_evento as r4099_evtfech_validar_evento_views
from emensageriapro.efdreinf.views import r4099_evtfech_abrir_evento_para_edicao as r4099_evtfech_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r4099_evtfech_alterar_identidade as r4099_evtfech_alterar_identidade_views
from emensageriapro.efdreinf.views import r4099_evtfech_criar_exclusao as r4099_evtfech_criar_exclusao_views
from emensageriapro.efdreinf.views import r4099_evtfech_duplicar as r4099_evtfech_duplicar_views
from emensageriapro.efdreinf.views import r5001_evttotal_api as r5001_evttotal_api_views
from emensageriapro.efdreinf.views import r5001_evttotal_listar as r5001_evttotal_listar_views
from emensageriapro.efdreinf.views import r5001_evttotal_recibos as r5001_evttotal_recibos_views
from emensageriapro.efdreinf.views import r5001_evttotal_importar as r5001_evttotal_importar_views
from emensageriapro.efdreinf.views import r5011_evttotalcontrib_api as r5011_evttotalcontrib_api_views
from emensageriapro.efdreinf.views import r5011_evttotalcontrib_listar as r5011_evttotalcontrib_listar_views
from emensageriapro.efdreinf.views import r5011_evttotalcontrib_recibos as r5011_evttotalcontrib_recibos_views
from emensageriapro.efdreinf.views import r5011_evttotalcontrib_importar as r5011_evttotalcontrib_importar_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_apagar as r9000_evtexclusao_apagar_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_listar as r9000_evtexclusao_listar_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_salvar as r9000_evtexclusao_salvar_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_api as r9000_evtexclusao_api_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_gerar_identidade as r9000_evtexclusao_gerar_identidade_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_verificar as r9000_evtexclusao_verificar_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_importar as r9000_evtexclusao_importar_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_validar as r9000_evtexclusao_validar_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_recibos as r9000_evtexclusao_recibos_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_gerar_xml as r9000_evtexclusao_gerar_xml_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_criar_alteracao as r9000_evtexclusao_criar_alteracao_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_validar_evento as r9000_evtexclusao_validar_evento_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_abrir_evento_para_edicao as r9000_evtexclusao_abrir_evento_para_edicao_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_alterar_identidade as r9000_evtexclusao_alterar_identidade_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_criar_exclusao as r9000_evtexclusao_criar_exclusao_views
from emensageriapro.efdreinf.views import r9000_evtexclusao_duplicar as r9000_evtexclusao_duplicar_views
from emensageriapro.efdreinf.views import r9001_evttotal_api as r9001_evttotal_api_views
from emensageriapro.efdreinf.views import r9001_evttotal_listar as r9001_evttotal_listar_views
from emensageriapro.efdreinf.views import r9001_evttotal_recibos as r9001_evttotal_recibos_views
from emensageriapro.efdreinf.views import r9001_evttotal_importar as r9001_evttotal_importar_views
from emensageriapro.efdreinf.views import r9002_evtret_api as r9002_evtret_api_views
from emensageriapro.efdreinf.views import r9002_evtret_listar as r9002_evtret_listar_views
from emensageriapro.efdreinf.views import r9002_evtret_recibos as r9002_evtret_recibos_views
from emensageriapro.efdreinf.views import r9002_evtret_importar as r9002_evtret_importar_views
from emensageriapro.efdreinf.views import r9011_evttotalcontrib_api as r9011_evttotalcontrib_api_views
from emensageriapro.efdreinf.views import r9011_evttotalcontrib_listar as r9011_evttotalcontrib_listar_views
from emensageriapro.efdreinf.views import r9011_evttotalcontrib_recibos as r9011_evttotalcontrib_recibos_views
from emensageriapro.efdreinf.views import r9011_evttotalcontrib_importar as r9011_evttotalcontrib_importar_views
from emensageriapro.efdreinf.views import r9012_evtretcons_api as r9012_evtretcons_api_views
from emensageriapro.efdreinf.views import r9012_evtretcons_listar as r9012_evtretcons_listar_views
from emensageriapro.efdreinf.views import r9012_evtretcons_recibos as r9012_evtretcons_recibos_views
from emensageriapro.efdreinf.views import r9012_evtretcons_importar as r9012_evtretcons_importar_views



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


    url(r'^r1000-evtinfocontri/apagar/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_apagar_views.apagar,
        name='r1000_evtinfocontri_apagar'),

    url(r'^r1000-evtinfocontri/api/$',
        r1000_evtinfocontri_api_views.r1000evtInfoContriList.as_view() ),

    url(r'^r1000-evtinfocontri/api/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_api_views.r1000evtInfoContriDetail.as_view() ),

    url(r'^r1000-evtinfocontri/$',
        r1000_evtinfocontri_listar_views.listar,
        name='r1000_evtinfocontri'),

    url(r'^r1000-evtinfocontri/verificar/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_verificar_views.verificar,
        name='r1000_evtinfocontri_verificar'),

    url(r'^r1000-evtinfocontri/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r1000_evtinfocontri_verificar_views.verificar,
        name='r1000_evtinfocontri_verificar_output'),

    url(r'^r1000-evtinfocontri/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r1000_evtinfocontri_recibos_views.recibo,
        name='r1000_evtinfocontri_recibo'),

    url(r'^r1000-evtinfocontri/duplicar/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_duplicar_views.duplicar,
        name='r1000_evtinfocontri_duplicar'),

    url(r'^r1000-evtinfocontri/criar-alteracao/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_criar_alteracao_views.criar_alteracao,
        name='r1000_evtinfocontri_criar_alteracao'),

    url(r'^r1000-evtinfocontri/criar-exclusao/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_criar_exclusao_views.criar_exclusao,
        name='r1000_evtinfocontri_criar_exclusao'),

    url(r'^r1000-evtinfocontri/xml/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_gerar_xml_views.gerar_xml,
        name='r1000_evtinfocontri_xml'),

    url(r'^r1000-evtinfocontri/alterar-identidade/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_alterar_identidade_views.alterar_identidade,
        name='r1000_evtinfocontri_alterar_identidade'),

    url(r'^r1000-evtinfocontri/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r1000_evtinfocontri_abrir_evento_para_edicao'),

    url(r'^r1000-evtinfocontri/validar-evento/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_validar_evento_views.validar_evento,
        name='r1000_evtinfocontri_validar_evento'),

    url(r'^r1000-evtinfocontri/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r1000_evtinfocontri_validar_evento_views.validar_evento,
        name='r1000_evtinfocontri_validar_evento_api'),

    url(r'^r1000-evtinfocontri/salvar/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_salvar_views.salvar,
        name='r1000_evtinfocontri_salvar'),

    url(r'^r1000-evtinfocontri/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r1000_evtinfocontri_salvar_views.salvar,
        name='r1000_evtinfocontri_salvar_tab'),

    url(r'^r1000-evtinfocontri/gerar-identidade/(?P<pk>[0-9]+)/$',
        r1000_evtinfocontri_gerar_identidade_views.gerar_identidade,
        name='r1000_evtinfocontri_gerar_identidade'),

    url(r'^r1000-evtinfocontri/cadastrar/$',
        r1000_evtinfocontri_salvar_views.salvar,
        name='r1000_evtinfocontri_cadastrar'),

    url(r'^r1000-evtinfocontri/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r1000_evtinfocontri_salvar_views.salvar,
        name='r1000_evtinfocontri_salvar_output'),

    url(r'^r1000-evtinfocontri/(?P<output>[\w-]+)/$',
        r1000_evtinfocontri_listar_views.listar,
        name='r1000_evtinfocontri_output'),

    url(r'^r1070-evttabprocesso/apagar/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_apagar_views.apagar,
        name='r1070_evttabprocesso_apagar'),

    url(r'^r1070-evttabprocesso/api/$',
        r1070_evttabprocesso_api_views.r1070evtTabProcessoList.as_view() ),

    url(r'^r1070-evttabprocesso/api/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_api_views.r1070evtTabProcessoDetail.as_view() ),

    url(r'^r1070-evttabprocesso/$',
        r1070_evttabprocesso_listar_views.listar,
        name='r1070_evttabprocesso'),

    url(r'^r1070-evttabprocesso/verificar/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_verificar_views.verificar,
        name='r1070_evttabprocesso_verificar'),

    url(r'^r1070-evttabprocesso/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r1070_evttabprocesso_verificar_views.verificar,
        name='r1070_evttabprocesso_verificar_output'),

    url(r'^r1070-evttabprocesso/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r1070_evttabprocesso_recibos_views.recibo,
        name='r1070_evttabprocesso_recibo'),

    url(r'^r1070-evttabprocesso/duplicar/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_duplicar_views.duplicar,
        name='r1070_evttabprocesso_duplicar'),

    url(r'^r1070-evttabprocesso/criar-alteracao/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_criar_alteracao_views.criar_alteracao,
        name='r1070_evttabprocesso_criar_alteracao'),

    url(r'^r1070-evttabprocesso/criar-exclusao/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_criar_exclusao_views.criar_exclusao,
        name='r1070_evttabprocesso_criar_exclusao'),

    url(r'^r1070-evttabprocesso/xml/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_gerar_xml_views.gerar_xml,
        name='r1070_evttabprocesso_xml'),

    url(r'^r1070-evttabprocesso/alterar-identidade/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_alterar_identidade_views.alterar_identidade,
        name='r1070_evttabprocesso_alterar_identidade'),

    url(r'^r1070-evttabprocesso/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r1070_evttabprocesso_abrir_evento_para_edicao'),

    url(r'^r1070-evttabprocesso/validar-evento/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_validar_evento_views.validar_evento,
        name='r1070_evttabprocesso_validar_evento'),

    url(r'^r1070-evttabprocesso/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r1070_evttabprocesso_validar_evento_views.validar_evento,
        name='r1070_evttabprocesso_validar_evento_api'),

    url(r'^r1070-evttabprocesso/salvar/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_salvar_views.salvar,
        name='r1070_evttabprocesso_salvar'),

    url(r'^r1070-evttabprocesso/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r1070_evttabprocesso_salvar_views.salvar,
        name='r1070_evttabprocesso_salvar_tab'),

    url(r'^r1070-evttabprocesso/gerar-identidade/(?P<pk>[0-9]+)/$',
        r1070_evttabprocesso_gerar_identidade_views.gerar_identidade,
        name='r1070_evttabprocesso_gerar_identidade'),

    url(r'^r1070-evttabprocesso/cadastrar/$',
        r1070_evttabprocesso_salvar_views.salvar,
        name='r1070_evttabprocesso_cadastrar'),

    url(r'^r1070-evttabprocesso/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r1070_evttabprocesso_salvar_views.salvar,
        name='r1070_evttabprocesso_salvar_output'),

    url(r'^r1070-evttabprocesso/(?P<output>[\w-]+)/$',
        r1070_evttabprocesso_listar_views.listar,
        name='r1070_evttabprocesso_output'),

    url(r'^r2010-evtservtom/apagar/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_apagar_views.apagar,
        name='r2010_evtservtom_apagar'),

    url(r'^r2010-evtservtom/api/$',
        r2010_evtservtom_api_views.r2010evtServTomList.as_view() ),

    url(r'^r2010-evtservtom/api/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_api_views.r2010evtServTomDetail.as_view() ),

    url(r'^r2010-evtservtom/$',
        r2010_evtservtom_listar_views.listar,
        name='r2010_evtservtom'),

    url(r'^r2010-evtservtom/verificar/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_verificar_views.verificar,
        name='r2010_evtservtom_verificar'),

    url(r'^r2010-evtservtom/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2010_evtservtom_verificar_views.verificar,
        name='r2010_evtservtom_verificar_output'),

    url(r'^r2010-evtservtom/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2010_evtservtom_recibos_views.recibo,
        name='r2010_evtservtom_recibo'),

    url(r'^r2010-evtservtom/duplicar/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_duplicar_views.duplicar,
        name='r2010_evtservtom_duplicar'),

    url(r'^r2010-evtservtom/criar-alteracao/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_criar_alteracao_views.criar_alteracao,
        name='r2010_evtservtom_criar_alteracao'),

    url(r'^r2010-evtservtom/criar-exclusao/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_criar_exclusao_views.criar_exclusao,
        name='r2010_evtservtom_criar_exclusao'),

    url(r'^r2010-evtservtom/xml/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_gerar_xml_views.gerar_xml,
        name='r2010_evtservtom_xml'),

    url(r'^r2010-evtservtom/alterar-identidade/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_alterar_identidade_views.alterar_identidade,
        name='r2010_evtservtom_alterar_identidade'),

    url(r'^r2010-evtservtom/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r2010_evtservtom_abrir_evento_para_edicao'),

    url(r'^r2010-evtservtom/validar-evento/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_validar_evento_views.validar_evento,
        name='r2010_evtservtom_validar_evento'),

    url(r'^r2010-evtservtom/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2010_evtservtom_validar_evento_views.validar_evento,
        name='r2010_evtservtom_validar_evento_api'),

    url(r'^r2010-evtservtom/salvar/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_salvar_views.salvar,
        name='r2010_evtservtom_salvar'),

    url(r'^r2010-evtservtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2010_evtservtom_salvar_views.salvar,
        name='r2010_evtservtom_salvar_tab'),

    url(r'^r2010-evtservtom/gerar-identidade/(?P<pk>[0-9]+)/$',
        r2010_evtservtom_gerar_identidade_views.gerar_identidade,
        name='r2010_evtservtom_gerar_identidade'),

    url(r'^r2010-evtservtom/cadastrar/$',
        r2010_evtservtom_salvar_views.salvar,
        name='r2010_evtservtom_cadastrar'),

    url(r'^r2010-evtservtom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2010_evtservtom_salvar_views.salvar,
        name='r2010_evtservtom_salvar_output'),

    url(r'^r2010-evtservtom/(?P<output>[\w-]+)/$',
        r2010_evtservtom_listar_views.listar,
        name='r2010_evtservtom_output'),

    url(r'^r2020-evtservprest/apagar/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_apagar_views.apagar,
        name='r2020_evtservprest_apagar'),

    url(r'^r2020-evtservprest/api/$',
        r2020_evtservprest_api_views.r2020evtServPrestList.as_view() ),

    url(r'^r2020-evtservprest/api/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_api_views.r2020evtServPrestDetail.as_view() ),

    url(r'^r2020-evtservprest/$',
        r2020_evtservprest_listar_views.listar,
        name='r2020_evtservprest'),

    url(r'^r2020-evtservprest/verificar/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_verificar_views.verificar,
        name='r2020_evtservprest_verificar'),

    url(r'^r2020-evtservprest/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2020_evtservprest_verificar_views.verificar,
        name='r2020_evtservprest_verificar_output'),

    url(r'^r2020-evtservprest/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2020_evtservprest_recibos_views.recibo,
        name='r2020_evtservprest_recibo'),

    url(r'^r2020-evtservprest/duplicar/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_duplicar_views.duplicar,
        name='r2020_evtservprest_duplicar'),

    url(r'^r2020-evtservprest/criar-alteracao/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_criar_alteracao_views.criar_alteracao,
        name='r2020_evtservprest_criar_alteracao'),

    url(r'^r2020-evtservprest/criar-exclusao/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_criar_exclusao_views.criar_exclusao,
        name='r2020_evtservprest_criar_exclusao'),

    url(r'^r2020-evtservprest/xml/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_gerar_xml_views.gerar_xml,
        name='r2020_evtservprest_xml'),

    url(r'^r2020-evtservprest/alterar-identidade/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_alterar_identidade_views.alterar_identidade,
        name='r2020_evtservprest_alterar_identidade'),

    url(r'^r2020-evtservprest/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r2020_evtservprest_abrir_evento_para_edicao'),

    url(r'^r2020-evtservprest/validar-evento/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_validar_evento_views.validar_evento,
        name='r2020_evtservprest_validar_evento'),

    url(r'^r2020-evtservprest/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2020_evtservprest_validar_evento_views.validar_evento,
        name='r2020_evtservprest_validar_evento_api'),

    url(r'^r2020-evtservprest/salvar/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_salvar_views.salvar,
        name='r2020_evtservprest_salvar'),

    url(r'^r2020-evtservprest/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2020_evtservprest_salvar_views.salvar,
        name='r2020_evtservprest_salvar_tab'),

    url(r'^r2020-evtservprest/gerar-identidade/(?P<pk>[0-9]+)/$',
        r2020_evtservprest_gerar_identidade_views.gerar_identidade,
        name='r2020_evtservprest_gerar_identidade'),

    url(r'^r2020-evtservprest/cadastrar/$',
        r2020_evtservprest_salvar_views.salvar,
        name='r2020_evtservprest_cadastrar'),

    url(r'^r2020-evtservprest/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2020_evtservprest_salvar_views.salvar,
        name='r2020_evtservprest_salvar_output'),

    url(r'^r2020-evtservprest/(?P<output>[\w-]+)/$',
        r2020_evtservprest_listar_views.listar,
        name='r2020_evtservprest_output'),

    url(r'^r2030-evtassocdesprec/apagar/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_apagar_views.apagar,
        name='r2030_evtassocdesprec_apagar'),

    url(r'^r2030-evtassocdesprec/api/$',
        r2030_evtassocdesprec_api_views.r2030evtAssocDespRecList.as_view() ),

    url(r'^r2030-evtassocdesprec/api/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_api_views.r2030evtAssocDespRecDetail.as_view() ),

    url(r'^r2030-evtassocdesprec/$',
        r2030_evtassocdesprec_listar_views.listar,
        name='r2030_evtassocdesprec'),

    url(r'^r2030-evtassocdesprec/verificar/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_verificar_views.verificar,
        name='r2030_evtassocdesprec_verificar'),

    url(r'^r2030-evtassocdesprec/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2030_evtassocdesprec_verificar_views.verificar,
        name='r2030_evtassocdesprec_verificar_output'),

    url(r'^r2030-evtassocdesprec/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2030_evtassocdesprec_recibos_views.recibo,
        name='r2030_evtassocdesprec_recibo'),

    url(r'^r2030-evtassocdesprec/duplicar/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_duplicar_views.duplicar,
        name='r2030_evtassocdesprec_duplicar'),

    url(r'^r2030-evtassocdesprec/criar-alteracao/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_criar_alteracao_views.criar_alteracao,
        name='r2030_evtassocdesprec_criar_alteracao'),

    url(r'^r2030-evtassocdesprec/criar-exclusao/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_criar_exclusao_views.criar_exclusao,
        name='r2030_evtassocdesprec_criar_exclusao'),

    url(r'^r2030-evtassocdesprec/xml/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_gerar_xml_views.gerar_xml,
        name='r2030_evtassocdesprec_xml'),

    url(r'^r2030-evtassocdesprec/alterar-identidade/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_alterar_identidade_views.alterar_identidade,
        name='r2030_evtassocdesprec_alterar_identidade'),

    url(r'^r2030-evtassocdesprec/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r2030_evtassocdesprec_abrir_evento_para_edicao'),

    url(r'^r2030-evtassocdesprec/validar-evento/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_validar_evento_views.validar_evento,
        name='r2030_evtassocdesprec_validar_evento'),

    url(r'^r2030-evtassocdesprec/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2030_evtassocdesprec_validar_evento_views.validar_evento,
        name='r2030_evtassocdesprec_validar_evento_api'),

    url(r'^r2030-evtassocdesprec/salvar/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_salvar_views.salvar,
        name='r2030_evtassocdesprec_salvar'),

    url(r'^r2030-evtassocdesprec/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2030_evtassocdesprec_salvar_views.salvar,
        name='r2030_evtassocdesprec_salvar_tab'),

    url(r'^r2030-evtassocdesprec/gerar-identidade/(?P<pk>[0-9]+)/$',
        r2030_evtassocdesprec_gerar_identidade_views.gerar_identidade,
        name='r2030_evtassocdesprec_gerar_identidade'),

    url(r'^r2030-evtassocdesprec/cadastrar/$',
        r2030_evtassocdesprec_salvar_views.salvar,
        name='r2030_evtassocdesprec_cadastrar'),

    url(r'^r2030-evtassocdesprec/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2030_evtassocdesprec_salvar_views.salvar,
        name='r2030_evtassocdesprec_salvar_output'),

    url(r'^r2030-evtassocdesprec/(?P<output>[\w-]+)/$',
        r2030_evtassocdesprec_listar_views.listar,
        name='r2030_evtassocdesprec_output'),

    url(r'^r2040-evtassocdesprep/apagar/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_apagar_views.apagar,
        name='r2040_evtassocdesprep_apagar'),

    url(r'^r2040-evtassocdesprep/api/$',
        r2040_evtassocdesprep_api_views.r2040evtAssocDespRepList.as_view() ),

    url(r'^r2040-evtassocdesprep/api/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_api_views.r2040evtAssocDespRepDetail.as_view() ),

    url(r'^r2040-evtassocdesprep/$',
        r2040_evtassocdesprep_listar_views.listar,
        name='r2040_evtassocdesprep'),

    url(r'^r2040-evtassocdesprep/verificar/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_verificar_views.verificar,
        name='r2040_evtassocdesprep_verificar'),

    url(r'^r2040-evtassocdesprep/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2040_evtassocdesprep_verificar_views.verificar,
        name='r2040_evtassocdesprep_verificar_output'),

    url(r'^r2040-evtassocdesprep/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2040_evtassocdesprep_recibos_views.recibo,
        name='r2040_evtassocdesprep_recibo'),

    url(r'^r2040-evtassocdesprep/duplicar/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_duplicar_views.duplicar,
        name='r2040_evtassocdesprep_duplicar'),

    url(r'^r2040-evtassocdesprep/criar-alteracao/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_criar_alteracao_views.criar_alteracao,
        name='r2040_evtassocdesprep_criar_alteracao'),

    url(r'^r2040-evtassocdesprep/criar-exclusao/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_criar_exclusao_views.criar_exclusao,
        name='r2040_evtassocdesprep_criar_exclusao'),

    url(r'^r2040-evtassocdesprep/xml/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_gerar_xml_views.gerar_xml,
        name='r2040_evtassocdesprep_xml'),

    url(r'^r2040-evtassocdesprep/alterar-identidade/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_alterar_identidade_views.alterar_identidade,
        name='r2040_evtassocdesprep_alterar_identidade'),

    url(r'^r2040-evtassocdesprep/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r2040_evtassocdesprep_abrir_evento_para_edicao'),

    url(r'^r2040-evtassocdesprep/validar-evento/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_validar_evento_views.validar_evento,
        name='r2040_evtassocdesprep_validar_evento'),

    url(r'^r2040-evtassocdesprep/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2040_evtassocdesprep_validar_evento_views.validar_evento,
        name='r2040_evtassocdesprep_validar_evento_api'),

    url(r'^r2040-evtassocdesprep/salvar/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_salvar_views.salvar,
        name='r2040_evtassocdesprep_salvar'),

    url(r'^r2040-evtassocdesprep/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2040_evtassocdesprep_salvar_views.salvar,
        name='r2040_evtassocdesprep_salvar_tab'),

    url(r'^r2040-evtassocdesprep/gerar-identidade/(?P<pk>[0-9]+)/$',
        r2040_evtassocdesprep_gerar_identidade_views.gerar_identidade,
        name='r2040_evtassocdesprep_gerar_identidade'),

    url(r'^r2040-evtassocdesprep/cadastrar/$',
        r2040_evtassocdesprep_salvar_views.salvar,
        name='r2040_evtassocdesprep_cadastrar'),

    url(r'^r2040-evtassocdesprep/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2040_evtassocdesprep_salvar_views.salvar,
        name='r2040_evtassocdesprep_salvar_output'),

    url(r'^r2040-evtassocdesprep/(?P<output>[\w-]+)/$',
        r2040_evtassocdesprep_listar_views.listar,
        name='r2040_evtassocdesprep_output'),

    url(r'^r2050-evtcomprod/apagar/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_apagar_views.apagar,
        name='r2050_evtcomprod_apagar'),

    url(r'^r2050-evtcomprod/api/$',
        r2050_evtcomprod_api_views.r2050evtComProdList.as_view() ),

    url(r'^r2050-evtcomprod/api/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_api_views.r2050evtComProdDetail.as_view() ),

    url(r'^r2050-evtcomprod/$',
        r2050_evtcomprod_listar_views.listar,
        name='r2050_evtcomprod'),

    url(r'^r2050-evtcomprod/verificar/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_verificar_views.verificar,
        name='r2050_evtcomprod_verificar'),

    url(r'^r2050-evtcomprod/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2050_evtcomprod_verificar_views.verificar,
        name='r2050_evtcomprod_verificar_output'),

    url(r'^r2050-evtcomprod/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2050_evtcomprod_recibos_views.recibo,
        name='r2050_evtcomprod_recibo'),

    url(r'^r2050-evtcomprod/duplicar/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_duplicar_views.duplicar,
        name='r2050_evtcomprod_duplicar'),

    url(r'^r2050-evtcomprod/criar-alteracao/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_criar_alteracao_views.criar_alteracao,
        name='r2050_evtcomprod_criar_alteracao'),

    url(r'^r2050-evtcomprod/criar-exclusao/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_criar_exclusao_views.criar_exclusao,
        name='r2050_evtcomprod_criar_exclusao'),

    url(r'^r2050-evtcomprod/xml/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_gerar_xml_views.gerar_xml,
        name='r2050_evtcomprod_xml'),

    url(r'^r2050-evtcomprod/alterar-identidade/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_alterar_identidade_views.alterar_identidade,
        name='r2050_evtcomprod_alterar_identidade'),

    url(r'^r2050-evtcomprod/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r2050_evtcomprod_abrir_evento_para_edicao'),

    url(r'^r2050-evtcomprod/validar-evento/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_validar_evento_views.validar_evento,
        name='r2050_evtcomprod_validar_evento'),

    url(r'^r2050-evtcomprod/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2050_evtcomprod_validar_evento_views.validar_evento,
        name='r2050_evtcomprod_validar_evento_api'),

    url(r'^r2050-evtcomprod/salvar/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_salvar_views.salvar,
        name='r2050_evtcomprod_salvar'),

    url(r'^r2050-evtcomprod/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2050_evtcomprod_salvar_views.salvar,
        name='r2050_evtcomprod_salvar_tab'),

    url(r'^r2050-evtcomprod/gerar-identidade/(?P<pk>[0-9]+)/$',
        r2050_evtcomprod_gerar_identidade_views.gerar_identidade,
        name='r2050_evtcomprod_gerar_identidade'),

    url(r'^r2050-evtcomprod/cadastrar/$',
        r2050_evtcomprod_salvar_views.salvar,
        name='r2050_evtcomprod_cadastrar'),

    url(r'^r2050-evtcomprod/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2050_evtcomprod_salvar_views.salvar,
        name='r2050_evtcomprod_salvar_output'),

    url(r'^r2050-evtcomprod/(?P<output>[\w-]+)/$',
        r2050_evtcomprod_listar_views.listar,
        name='r2050_evtcomprod_output'),

    url(r'^r2060-evtcprb/apagar/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_apagar_views.apagar,
        name='r2060_evtcprb_apagar'),

    url(r'^r2060-evtcprb/api/$',
        r2060_evtcprb_api_views.r2060evtCPRBList.as_view() ),

    url(r'^r2060-evtcprb/api/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_api_views.r2060evtCPRBDetail.as_view() ),

    url(r'^r2060-evtcprb/$',
        r2060_evtcprb_listar_views.listar,
        name='r2060_evtcprb'),

    url(r'^r2060-evtcprb/verificar/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_verificar_views.verificar,
        name='r2060_evtcprb_verificar'),

    url(r'^r2060-evtcprb/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2060_evtcprb_verificar_views.verificar,
        name='r2060_evtcprb_verificar_output'),

    url(r'^r2060-evtcprb/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2060_evtcprb_recibos_views.recibo,
        name='r2060_evtcprb_recibo'),

    url(r'^r2060-evtcprb/duplicar/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_duplicar_views.duplicar,
        name='r2060_evtcprb_duplicar'),

    url(r'^r2060-evtcprb/criar-alteracao/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_criar_alteracao_views.criar_alteracao,
        name='r2060_evtcprb_criar_alteracao'),

    url(r'^r2060-evtcprb/criar-exclusao/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_criar_exclusao_views.criar_exclusao,
        name='r2060_evtcprb_criar_exclusao'),

    url(r'^r2060-evtcprb/xml/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_gerar_xml_views.gerar_xml,
        name='r2060_evtcprb_xml'),

    url(r'^r2060-evtcprb/alterar-identidade/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_alterar_identidade_views.alterar_identidade,
        name='r2060_evtcprb_alterar_identidade'),

    url(r'^r2060-evtcprb/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r2060_evtcprb_abrir_evento_para_edicao'),

    url(r'^r2060-evtcprb/validar-evento/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_validar_evento_views.validar_evento,
        name='r2060_evtcprb_validar_evento'),

    url(r'^r2060-evtcprb/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2060_evtcprb_validar_evento_views.validar_evento,
        name='r2060_evtcprb_validar_evento_api'),

    url(r'^r2060-evtcprb/salvar/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_salvar_views.salvar,
        name='r2060_evtcprb_salvar'),

    url(r'^r2060-evtcprb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2060_evtcprb_salvar_views.salvar,
        name='r2060_evtcprb_salvar_tab'),

    url(r'^r2060-evtcprb/gerar-identidade/(?P<pk>[0-9]+)/$',
        r2060_evtcprb_gerar_identidade_views.gerar_identidade,
        name='r2060_evtcprb_gerar_identidade'),

    url(r'^r2060-evtcprb/cadastrar/$',
        r2060_evtcprb_salvar_views.salvar,
        name='r2060_evtcprb_cadastrar'),

    url(r'^r2060-evtcprb/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2060_evtcprb_salvar_views.salvar,
        name='r2060_evtcprb_salvar_output'),

    url(r'^r2060-evtcprb/(?P<output>[\w-]+)/$',
        r2060_evtcprb_listar_views.listar,
        name='r2060_evtcprb_output'),

    url(r'^r2070-evtpgtosdivs/apagar/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_apagar_views.apagar,
        name='r2070_evtpgtosdivs_apagar'),

    url(r'^r2070-evtpgtosdivs/api/$',
        r2070_evtpgtosdivs_api_views.r2070evtPgtosDivsList.as_view() ),

    url(r'^r2070-evtpgtosdivs/api/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_api_views.r2070evtPgtosDivsDetail.as_view() ),

    url(r'^r2070-evtpgtosdivs/$',
        r2070_evtpgtosdivs_listar_views.listar,
        name='r2070_evtpgtosdivs'),

    url(r'^r2070-evtpgtosdivs/verificar/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_verificar_views.verificar,
        name='r2070_evtpgtosdivs_verificar'),

    url(r'^r2070-evtpgtosdivs/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2070_evtpgtosdivs_verificar_views.verificar,
        name='r2070_evtpgtosdivs_verificar_output'),

    url(r'^r2070-evtpgtosdivs/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2070_evtpgtosdivs_recibos_views.recibo,
        name='r2070_evtpgtosdivs_recibo'),

    url(r'^r2070-evtpgtosdivs/duplicar/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_duplicar_views.duplicar,
        name='r2070_evtpgtosdivs_duplicar'),

    url(r'^r2070-evtpgtosdivs/criar-alteracao/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_criar_alteracao_views.criar_alteracao,
        name='r2070_evtpgtosdivs_criar_alteracao'),

    url(r'^r2070-evtpgtosdivs/criar-exclusao/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_criar_exclusao_views.criar_exclusao,
        name='r2070_evtpgtosdivs_criar_exclusao'),

    url(r'^r2070-evtpgtosdivs/xml/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_gerar_xml_views.gerar_xml,
        name='r2070_evtpgtosdivs_xml'),

    url(r'^r2070-evtpgtosdivs/alterar-identidade/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_alterar_identidade_views.alterar_identidade,
        name='r2070_evtpgtosdivs_alterar_identidade'),

    url(r'^r2070-evtpgtosdivs/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r2070_evtpgtosdivs_abrir_evento_para_edicao'),

    url(r'^r2070-evtpgtosdivs/validar-evento/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_validar_evento_views.validar_evento,
        name='r2070_evtpgtosdivs_validar_evento'),

    url(r'^r2070-evtpgtosdivs/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2070_evtpgtosdivs_validar_evento_views.validar_evento,
        name='r2070_evtpgtosdivs_validar_evento_api'),

    url(r'^r2070-evtpgtosdivs/salvar/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_salvar_views.salvar,
        name='r2070_evtpgtosdivs_salvar'),

    url(r'^r2070-evtpgtosdivs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2070_evtpgtosdivs_salvar_views.salvar,
        name='r2070_evtpgtosdivs_salvar_tab'),

    url(r'^r2070-evtpgtosdivs/gerar-identidade/(?P<pk>[0-9]+)/$',
        r2070_evtpgtosdivs_gerar_identidade_views.gerar_identidade,
        name='r2070_evtpgtosdivs_gerar_identidade'),

    url(r'^r2070-evtpgtosdivs/cadastrar/$',
        r2070_evtpgtosdivs_salvar_views.salvar,
        name='r2070_evtpgtosdivs_cadastrar'),

    url(r'^r2070-evtpgtosdivs/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2070_evtpgtosdivs_salvar_views.salvar,
        name='r2070_evtpgtosdivs_salvar_output'),

    url(r'^r2070-evtpgtosdivs/(?P<output>[\w-]+)/$',
        r2070_evtpgtosdivs_listar_views.listar,
        name='r2070_evtpgtosdivs_output'),

    url(r'^r2098-evtreabreevper/apagar/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_apagar_views.apagar,
        name='r2098_evtreabreevper_apagar'),

    url(r'^r2098-evtreabreevper/api/$',
        r2098_evtreabreevper_api_views.r2098evtReabreEvPerList.as_view() ),

    url(r'^r2098-evtreabreevper/api/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_api_views.r2098evtReabreEvPerDetail.as_view() ),

    url(r'^r2098-evtreabreevper/$',
        r2098_evtreabreevper_listar_views.listar,
        name='r2098_evtreabreevper'),

    url(r'^r2098-evtreabreevper/verificar/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_verificar_views.verificar,
        name='r2098_evtreabreevper_verificar'),

    url(r'^r2098-evtreabreevper/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2098_evtreabreevper_verificar_views.verificar,
        name='r2098_evtreabreevper_verificar_output'),

    url(r'^r2098-evtreabreevper/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2098_evtreabreevper_recibos_views.recibo,
        name='r2098_evtreabreevper_recibo'),

    url(r'^r2098-evtreabreevper/duplicar/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_duplicar_views.duplicar,
        name='r2098_evtreabreevper_duplicar'),

    url(r'^r2098-evtreabreevper/criar-alteracao/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_criar_alteracao_views.criar_alteracao,
        name='r2098_evtreabreevper_criar_alteracao'),

    url(r'^r2098-evtreabreevper/criar-exclusao/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_criar_exclusao_views.criar_exclusao,
        name='r2098_evtreabreevper_criar_exclusao'),

    url(r'^r2098-evtreabreevper/xml/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_gerar_xml_views.gerar_xml,
        name='r2098_evtreabreevper_xml'),

    url(r'^r2098-evtreabreevper/alterar-identidade/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_alterar_identidade_views.alterar_identidade,
        name='r2098_evtreabreevper_alterar_identidade'),

    url(r'^r2098-evtreabreevper/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r2098_evtreabreevper_abrir_evento_para_edicao'),

    url(r'^r2098-evtreabreevper/validar-evento/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_validar_evento_views.validar_evento,
        name='r2098_evtreabreevper_validar_evento'),

    url(r'^r2098-evtreabreevper/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2098_evtreabreevper_validar_evento_views.validar_evento,
        name='r2098_evtreabreevper_validar_evento_api'),

    url(r'^r2098-evtreabreevper/salvar/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_salvar_views.salvar,
        name='r2098_evtreabreevper_salvar'),

    url(r'^r2098-evtreabreevper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2098_evtreabreevper_salvar_views.salvar,
        name='r2098_evtreabreevper_salvar_tab'),

    url(r'^r2098-evtreabreevper/gerar-identidade/(?P<pk>[0-9]+)/$',
        r2098_evtreabreevper_gerar_identidade_views.gerar_identidade,
        name='r2098_evtreabreevper_gerar_identidade'),

    url(r'^r2098-evtreabreevper/cadastrar/$',
        r2098_evtreabreevper_salvar_views.salvar,
        name='r2098_evtreabreevper_cadastrar'),

    url(r'^r2098-evtreabreevper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2098_evtreabreevper_salvar_views.salvar,
        name='r2098_evtreabreevper_salvar_output'),

    url(r'^r2098-evtreabreevper/(?P<output>[\w-]+)/$',
        r2098_evtreabreevper_listar_views.listar,
        name='r2098_evtreabreevper_output'),

    url(r'^r2099-evtfechaevper/apagar/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_apagar_views.apagar,
        name='r2099_evtfechaevper_apagar'),

    url(r'^r2099-evtfechaevper/api/$',
        r2099_evtfechaevper_api_views.r2099evtFechaEvPerList.as_view() ),

    url(r'^r2099-evtfechaevper/api/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_api_views.r2099evtFechaEvPerDetail.as_view() ),

    url(r'^r2099-evtfechaevper/$',
        r2099_evtfechaevper_listar_views.listar,
        name='r2099_evtfechaevper'),

    url(r'^r2099-evtfechaevper/verificar/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_verificar_views.verificar,
        name='r2099_evtfechaevper_verificar'),

    url(r'^r2099-evtfechaevper/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2099_evtfechaevper_verificar_views.verificar,
        name='r2099_evtfechaevper_verificar_output'),

    url(r'^r2099-evtfechaevper/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r2099_evtfechaevper_recibos_views.recibo,
        name='r2099_evtfechaevper_recibo'),

    url(r'^r2099-evtfechaevper/duplicar/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_duplicar_views.duplicar,
        name='r2099_evtfechaevper_duplicar'),

    url(r'^r2099-evtfechaevper/criar-alteracao/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_criar_alteracao_views.criar_alteracao,
        name='r2099_evtfechaevper_criar_alteracao'),

    url(r'^r2099-evtfechaevper/criar-exclusao/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_criar_exclusao_views.criar_exclusao,
        name='r2099_evtfechaevper_criar_exclusao'),

    url(r'^r2099-evtfechaevper/xml/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_gerar_xml_views.gerar_xml,
        name='r2099_evtfechaevper_xml'),

    url(r'^r2099-evtfechaevper/alterar-identidade/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_alterar_identidade_views.alterar_identidade,
        name='r2099_evtfechaevper_alterar_identidade'),

    url(r'^r2099-evtfechaevper/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r2099_evtfechaevper_abrir_evento_para_edicao'),

    url(r'^r2099-evtfechaevper/validar-evento/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_validar_evento_views.validar_evento,
        name='r2099_evtfechaevper_validar_evento'),

    url(r'^r2099-evtfechaevper/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2099_evtfechaevper_validar_evento_views.validar_evento,
        name='r2099_evtfechaevper_validar_evento_api'),

    url(r'^r2099-evtfechaevper/salvar/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_salvar_views.salvar,
        name='r2099_evtfechaevper_salvar'),

    url(r'^r2099-evtfechaevper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2099_evtfechaevper_salvar_views.salvar,
        name='r2099_evtfechaevper_salvar_tab'),

    url(r'^r2099-evtfechaevper/gerar-identidade/(?P<pk>[0-9]+)/$',
        r2099_evtfechaevper_gerar_identidade_views.gerar_identidade,
        name='r2099_evtfechaevper_gerar_identidade'),

    url(r'^r2099-evtfechaevper/cadastrar/$',
        r2099_evtfechaevper_salvar_views.salvar,
        name='r2099_evtfechaevper_cadastrar'),

    url(r'^r2099-evtfechaevper/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2099_evtfechaevper_salvar_views.salvar,
        name='r2099_evtfechaevper_salvar_output'),

    url(r'^r2099-evtfechaevper/(?P<output>[\w-]+)/$',
        r2099_evtfechaevper_listar_views.listar,
        name='r2099_evtfechaevper_output'),

    url(r'^r3010-evtespdesportivo/apagar/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_apagar_views.apagar,
        name='r3010_evtespdesportivo_apagar'),

    url(r'^r3010-evtespdesportivo/api/$',
        r3010_evtespdesportivo_api_views.r3010evtEspDesportivoList.as_view() ),

    url(r'^r3010-evtespdesportivo/api/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_api_views.r3010evtEspDesportivoDetail.as_view() ),

    url(r'^r3010-evtespdesportivo/$',
        r3010_evtespdesportivo_listar_views.listar,
        name='r3010_evtespdesportivo'),

    url(r'^r3010-evtespdesportivo/verificar/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_verificar_views.verificar,
        name='r3010_evtespdesportivo_verificar'),

    url(r'^r3010-evtespdesportivo/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r3010_evtespdesportivo_verificar_views.verificar,
        name='r3010_evtespdesportivo_verificar_output'),

    url(r'^r3010-evtespdesportivo/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r3010_evtespdesportivo_recibos_views.recibo,
        name='r3010_evtespdesportivo_recibo'),

    url(r'^r3010-evtespdesportivo/duplicar/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_duplicar_views.duplicar,
        name='r3010_evtespdesportivo_duplicar'),

    url(r'^r3010-evtespdesportivo/criar-alteracao/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_criar_alteracao_views.criar_alteracao,
        name='r3010_evtespdesportivo_criar_alteracao'),

    url(r'^r3010-evtespdesportivo/criar-exclusao/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_criar_exclusao_views.criar_exclusao,
        name='r3010_evtespdesportivo_criar_exclusao'),

    url(r'^r3010-evtespdesportivo/xml/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_gerar_xml_views.gerar_xml,
        name='r3010_evtespdesportivo_xml'),

    url(r'^r3010-evtespdesportivo/alterar-identidade/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_alterar_identidade_views.alterar_identidade,
        name='r3010_evtespdesportivo_alterar_identidade'),

    url(r'^r3010-evtespdesportivo/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r3010_evtespdesportivo_abrir_evento_para_edicao'),

    url(r'^r3010-evtespdesportivo/validar-evento/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_validar_evento_views.validar_evento,
        name='r3010_evtespdesportivo_validar_evento'),

    url(r'^r3010-evtespdesportivo/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r3010_evtespdesportivo_validar_evento_views.validar_evento,
        name='r3010_evtespdesportivo_validar_evento_api'),

    url(r'^r3010-evtespdesportivo/salvar/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_salvar_views.salvar,
        name='r3010_evtespdesportivo_salvar'),

    url(r'^r3010-evtespdesportivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r3010_evtespdesportivo_salvar_views.salvar,
        name='r3010_evtespdesportivo_salvar_tab'),

    url(r'^r3010-evtespdesportivo/gerar-identidade/(?P<pk>[0-9]+)/$',
        r3010_evtespdesportivo_gerar_identidade_views.gerar_identidade,
        name='r3010_evtespdesportivo_gerar_identidade'),

    url(r'^r3010-evtespdesportivo/cadastrar/$',
        r3010_evtespdesportivo_salvar_views.salvar,
        name='r3010_evtespdesportivo_cadastrar'),

    url(r'^r3010-evtespdesportivo/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r3010_evtespdesportivo_salvar_views.salvar,
        name='r3010_evtespdesportivo_salvar_output'),

    url(r'^r3010-evtespdesportivo/(?P<output>[\w-]+)/$',
        r3010_evtespdesportivo_listar_views.listar,
        name='r3010_evtespdesportivo_output'),

    url(r'^r4010-evtretpf/apagar/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_apagar_views.apagar,
        name='r4010_evtretpf_apagar'),

    url(r'^r4010-evtretpf/api/$',
        r4010_evtretpf_api_views.r4010evtRetPFList.as_view() ),

    url(r'^r4010-evtretpf/api/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_api_views.r4010evtRetPFDetail.as_view() ),

    url(r'^r4010-evtretpf/$',
        r4010_evtretpf_listar_views.listar,
        name='r4010_evtretpf'),

    url(r'^r4010-evtretpf/verificar/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_verificar_views.verificar,
        name='r4010_evtretpf_verificar'),

    url(r'^r4010-evtretpf/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4010_evtretpf_verificar_views.verificar,
        name='r4010_evtretpf_verificar_output'),

    url(r'^r4010-evtretpf/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4010_evtretpf_recibos_views.recibo,
        name='r4010_evtretpf_recibo'),

    url(r'^r4010-evtretpf/duplicar/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_duplicar_views.duplicar,
        name='r4010_evtretpf_duplicar'),

    url(r'^r4010-evtretpf/criar-alteracao/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_criar_alteracao_views.criar_alteracao,
        name='r4010_evtretpf_criar_alteracao'),

    url(r'^r4010-evtretpf/criar-exclusao/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_criar_exclusao_views.criar_exclusao,
        name='r4010_evtretpf_criar_exclusao'),

    url(r'^r4010-evtretpf/xml/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_gerar_xml_views.gerar_xml,
        name='r4010_evtretpf_xml'),

    url(r'^r4010-evtretpf/alterar-identidade/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_alterar_identidade_views.alterar_identidade,
        name='r4010_evtretpf_alterar_identidade'),

    url(r'^r4010-evtretpf/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r4010_evtretpf_abrir_evento_para_edicao'),

    url(r'^r4010-evtretpf/validar-evento/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_validar_evento_views.validar_evento,
        name='r4010_evtretpf_validar_evento'),

    url(r'^r4010-evtretpf/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_evtretpf_validar_evento_views.validar_evento,
        name='r4010_evtretpf_validar_evento_api'),

    url(r'^r4010-evtretpf/salvar/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_salvar_views.salvar,
        name='r4010_evtretpf_salvar'),

    url(r'^r4010-evtretpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4010_evtretpf_salvar_views.salvar,
        name='r4010_evtretpf_salvar_tab'),

    url(r'^r4010-evtretpf/gerar-identidade/(?P<pk>[0-9]+)/$',
        r4010_evtretpf_gerar_identidade_views.gerar_identidade,
        name='r4010_evtretpf_gerar_identidade'),

    url(r'^r4010-evtretpf/cadastrar/$',
        r4010_evtretpf_salvar_views.salvar,
        name='r4010_evtretpf_cadastrar'),

    url(r'^r4010-evtretpf/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4010_evtretpf_salvar_views.salvar,
        name='r4010_evtretpf_salvar_output'),

    url(r'^r4010-evtretpf/(?P<output>[\w-]+)/$',
        r4010_evtretpf_listar_views.listar,
        name='r4010_evtretpf_output'),

    url(r'^r4020-evtretpj/apagar/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_apagar_views.apagar,
        name='r4020_evtretpj_apagar'),

    url(r'^r4020-evtretpj/api/$',
        r4020_evtretpj_api_views.r4020evtRetPJList.as_view() ),

    url(r'^r4020-evtretpj/api/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_api_views.r4020evtRetPJDetail.as_view() ),

    url(r'^r4020-evtretpj/$',
        r4020_evtretpj_listar_views.listar,
        name='r4020_evtretpj'),

    url(r'^r4020-evtretpj/verificar/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_verificar_views.verificar,
        name='r4020_evtretpj_verificar'),

    url(r'^r4020-evtretpj/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4020_evtretpj_verificar_views.verificar,
        name='r4020_evtretpj_verificar_output'),

    url(r'^r4020-evtretpj/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4020_evtretpj_recibos_views.recibo,
        name='r4020_evtretpj_recibo'),

    url(r'^r4020-evtretpj/duplicar/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_duplicar_views.duplicar,
        name='r4020_evtretpj_duplicar'),

    url(r'^r4020-evtretpj/criar-alteracao/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_criar_alteracao_views.criar_alteracao,
        name='r4020_evtretpj_criar_alteracao'),

    url(r'^r4020-evtretpj/criar-exclusao/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_criar_exclusao_views.criar_exclusao,
        name='r4020_evtretpj_criar_exclusao'),

    url(r'^r4020-evtretpj/xml/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_gerar_xml_views.gerar_xml,
        name='r4020_evtretpj_xml'),

    url(r'^r4020-evtretpj/alterar-identidade/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_alterar_identidade_views.alterar_identidade,
        name='r4020_evtretpj_alterar_identidade'),

    url(r'^r4020-evtretpj/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r4020_evtretpj_abrir_evento_para_edicao'),

    url(r'^r4020-evtretpj/validar-evento/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_validar_evento_views.validar_evento,
        name='r4020_evtretpj_validar_evento'),

    url(r'^r4020-evtretpj/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_evtretpj_validar_evento_views.validar_evento,
        name='r4020_evtretpj_validar_evento_api'),

    url(r'^r4020-evtretpj/salvar/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_salvar_views.salvar,
        name='r4020_evtretpj_salvar'),

    url(r'^r4020-evtretpj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_evtretpj_salvar_views.salvar,
        name='r4020_evtretpj_salvar_tab'),

    url(r'^r4020-evtretpj/gerar-identidade/(?P<pk>[0-9]+)/$',
        r4020_evtretpj_gerar_identidade_views.gerar_identidade,
        name='r4020_evtretpj_gerar_identidade'),

    url(r'^r4020-evtretpj/cadastrar/$',
        r4020_evtretpj_salvar_views.salvar,
        name='r4020_evtretpj_cadastrar'),

    url(r'^r4020-evtretpj/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_evtretpj_salvar_views.salvar,
        name='r4020_evtretpj_salvar_output'),

    url(r'^r4020-evtretpj/(?P<output>[\w-]+)/$',
        r4020_evtretpj_listar_views.listar,
        name='r4020_evtretpj_output'),

    url(r'^r4040-evtbenefnid/apagar/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_apagar_views.apagar,
        name='r4040_evtbenefnid_apagar'),

    url(r'^r4040-evtbenefnid/api/$',
        r4040_evtbenefnid_api_views.r4040evtBenefNIdList.as_view() ),

    url(r'^r4040-evtbenefnid/api/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_api_views.r4040evtBenefNIdDetail.as_view() ),

    url(r'^r4040-evtbenefnid/$',
        r4040_evtbenefnid_listar_views.listar,
        name='r4040_evtbenefnid'),

    url(r'^r4040-evtbenefnid/verificar/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_verificar_views.verificar,
        name='r4040_evtbenefnid_verificar'),

    url(r'^r4040-evtbenefnid/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4040_evtbenefnid_verificar_views.verificar,
        name='r4040_evtbenefnid_verificar_output'),

    url(r'^r4040-evtbenefnid/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4040_evtbenefnid_recibos_views.recibo,
        name='r4040_evtbenefnid_recibo'),

    url(r'^r4040-evtbenefnid/duplicar/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_duplicar_views.duplicar,
        name='r4040_evtbenefnid_duplicar'),

    url(r'^r4040-evtbenefnid/criar-alteracao/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_criar_alteracao_views.criar_alteracao,
        name='r4040_evtbenefnid_criar_alteracao'),

    url(r'^r4040-evtbenefnid/criar-exclusao/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_criar_exclusao_views.criar_exclusao,
        name='r4040_evtbenefnid_criar_exclusao'),

    url(r'^r4040-evtbenefnid/xml/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_gerar_xml_views.gerar_xml,
        name='r4040_evtbenefnid_xml'),

    url(r'^r4040-evtbenefnid/alterar-identidade/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_alterar_identidade_views.alterar_identidade,
        name='r4040_evtbenefnid_alterar_identidade'),

    url(r'^r4040-evtbenefnid/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r4040_evtbenefnid_abrir_evento_para_edicao'),

    url(r'^r4040-evtbenefnid/validar-evento/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_validar_evento_views.validar_evento,
        name='r4040_evtbenefnid_validar_evento'),

    url(r'^r4040-evtbenefnid/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4040_evtbenefnid_validar_evento_views.validar_evento,
        name='r4040_evtbenefnid_validar_evento_api'),

    url(r'^r4040-evtbenefnid/salvar/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_salvar_views.salvar,
        name='r4040_evtbenefnid_salvar'),

    url(r'^r4040-evtbenefnid/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4040_evtbenefnid_salvar_views.salvar,
        name='r4040_evtbenefnid_salvar_tab'),

    url(r'^r4040-evtbenefnid/gerar-identidade/(?P<pk>[0-9]+)/$',
        r4040_evtbenefnid_gerar_identidade_views.gerar_identidade,
        name='r4040_evtbenefnid_gerar_identidade'),

    url(r'^r4040-evtbenefnid/cadastrar/$',
        r4040_evtbenefnid_salvar_views.salvar,
        name='r4040_evtbenefnid_cadastrar'),

    url(r'^r4040-evtbenefnid/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4040_evtbenefnid_salvar_views.salvar,
        name='r4040_evtbenefnid_salvar_output'),

    url(r'^r4040-evtbenefnid/(?P<output>[\w-]+)/$',
        r4040_evtbenefnid_listar_views.listar,
        name='r4040_evtbenefnid_output'),

    url(r'^r4098-evtreab/apagar/(?P<pk>[0-9]+)/$',
        r4098_evtreab_apagar_views.apagar,
        name='r4098_evtreab_apagar'),

    url(r'^r4098-evtreab/api/$',
        r4098_evtreab_api_views.r4098evtReabList.as_view() ),

    url(r'^r4098-evtreab/api/(?P<pk>[0-9]+)/$',
        r4098_evtreab_api_views.r4098evtReabDetail.as_view() ),

    url(r'^r4098-evtreab/$',
        r4098_evtreab_listar_views.listar,
        name='r4098_evtreab'),

    url(r'^r4098-evtreab/verificar/(?P<pk>[0-9]+)/$',
        r4098_evtreab_verificar_views.verificar,
        name='r4098_evtreab_verificar'),

    url(r'^r4098-evtreab/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4098_evtreab_verificar_views.verificar,
        name='r4098_evtreab_verificar_output'),

    url(r'^r4098-evtreab/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4098_evtreab_recibos_views.recibo,
        name='r4098_evtreab_recibo'),

    url(r'^r4098-evtreab/duplicar/(?P<pk>[0-9]+)/$',
        r4098_evtreab_duplicar_views.duplicar,
        name='r4098_evtreab_duplicar'),

    url(r'^r4098-evtreab/criar-alteracao/(?P<pk>[0-9]+)/$',
        r4098_evtreab_criar_alteracao_views.criar_alteracao,
        name='r4098_evtreab_criar_alteracao'),

    url(r'^r4098-evtreab/criar-exclusao/(?P<pk>[0-9]+)/$',
        r4098_evtreab_criar_exclusao_views.criar_exclusao,
        name='r4098_evtreab_criar_exclusao'),

    url(r'^r4098-evtreab/xml/(?P<pk>[0-9]+)/$',
        r4098_evtreab_gerar_xml_views.gerar_xml,
        name='r4098_evtreab_xml'),

    url(r'^r4098-evtreab/alterar-identidade/(?P<pk>[0-9]+)/$',
        r4098_evtreab_alterar_identidade_views.alterar_identidade,
        name='r4098_evtreab_alterar_identidade'),

    url(r'^r4098-evtreab/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r4098_evtreab_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r4098_evtreab_abrir_evento_para_edicao'),

    url(r'^r4098-evtreab/validar-evento/(?P<pk>[0-9]+)/$',
        r4098_evtreab_validar_evento_views.validar_evento,
        name='r4098_evtreab_validar_evento'),

    url(r'^r4098-evtreab/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4098_evtreab_validar_evento_views.validar_evento,
        name='r4098_evtreab_validar_evento_api'),

    url(r'^r4098-evtreab/salvar/(?P<pk>[0-9]+)/$',
        r4098_evtreab_salvar_views.salvar,
        name='r4098_evtreab_salvar'),

    url(r'^r4098-evtreab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4098_evtreab_salvar_views.salvar,
        name='r4098_evtreab_salvar_tab'),

    url(r'^r4098-evtreab/gerar-identidade/(?P<pk>[0-9]+)/$',
        r4098_evtreab_gerar_identidade_views.gerar_identidade,
        name='r4098_evtreab_gerar_identidade'),

    url(r'^r4098-evtreab/cadastrar/$',
        r4098_evtreab_salvar_views.salvar,
        name='r4098_evtreab_cadastrar'),

    url(r'^r4098-evtreab/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4098_evtreab_salvar_views.salvar,
        name='r4098_evtreab_salvar_output'),

    url(r'^r4098-evtreab/(?P<output>[\w-]+)/$',
        r4098_evtreab_listar_views.listar,
        name='r4098_evtreab_output'),

    url(r'^r4099-evtfech/apagar/(?P<pk>[0-9]+)/$',
        r4099_evtfech_apagar_views.apagar,
        name='r4099_evtfech_apagar'),

    url(r'^r4099-evtfech/api/$',
        r4099_evtfech_api_views.r4099evtFechList.as_view() ),

    url(r'^r4099-evtfech/api/(?P<pk>[0-9]+)/$',
        r4099_evtfech_api_views.r4099evtFechDetail.as_view() ),

    url(r'^r4099-evtfech/$',
        r4099_evtfech_listar_views.listar,
        name='r4099_evtfech'),

    url(r'^r4099-evtfech/verificar/(?P<pk>[0-9]+)/$',
        r4099_evtfech_verificar_views.verificar,
        name='r4099_evtfech_verificar'),

    url(r'^r4099-evtfech/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4099_evtfech_verificar_views.verificar,
        name='r4099_evtfech_verificar_output'),

    url(r'^r4099-evtfech/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r4099_evtfech_recibos_views.recibo,
        name='r4099_evtfech_recibo'),

    url(r'^r4099-evtfech/duplicar/(?P<pk>[0-9]+)/$',
        r4099_evtfech_duplicar_views.duplicar,
        name='r4099_evtfech_duplicar'),

    url(r'^r4099-evtfech/criar-alteracao/(?P<pk>[0-9]+)/$',
        r4099_evtfech_criar_alteracao_views.criar_alteracao,
        name='r4099_evtfech_criar_alteracao'),

    url(r'^r4099-evtfech/criar-exclusao/(?P<pk>[0-9]+)/$',
        r4099_evtfech_criar_exclusao_views.criar_exclusao,
        name='r4099_evtfech_criar_exclusao'),

    url(r'^r4099-evtfech/xml/(?P<pk>[0-9]+)/$',
        r4099_evtfech_gerar_xml_views.gerar_xml,
        name='r4099_evtfech_xml'),

    url(r'^r4099-evtfech/alterar-identidade/(?P<pk>[0-9]+)/$',
        r4099_evtfech_alterar_identidade_views.alterar_identidade,
        name='r4099_evtfech_alterar_identidade'),

    url(r'^r4099-evtfech/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r4099_evtfech_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r4099_evtfech_abrir_evento_para_edicao'),

    url(r'^r4099-evtfech/validar-evento/(?P<pk>[0-9]+)/$',
        r4099_evtfech_validar_evento_views.validar_evento,
        name='r4099_evtfech_validar_evento'),

    url(r'^r4099-evtfech/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4099_evtfech_validar_evento_views.validar_evento,
        name='r4099_evtfech_validar_evento_api'),

    url(r'^r4099-evtfech/salvar/(?P<pk>[0-9]+)/$',
        r4099_evtfech_salvar_views.salvar,
        name='r4099_evtfech_salvar'),

    url(r'^r4099-evtfech/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4099_evtfech_salvar_views.salvar,
        name='r4099_evtfech_salvar_tab'),

    url(r'^r4099-evtfech/gerar-identidade/(?P<pk>[0-9]+)/$',
        r4099_evtfech_gerar_identidade_views.gerar_identidade,
        name='r4099_evtfech_gerar_identidade'),

    url(r'^r4099-evtfech/cadastrar/$',
        r4099_evtfech_salvar_views.salvar,
        name='r4099_evtfech_cadastrar'),

    url(r'^r4099-evtfech/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4099_evtfech_salvar_views.salvar,
        name='r4099_evtfech_salvar_output'),

    url(r'^r4099-evtfech/(?P<output>[\w-]+)/$',
        r4099_evtfech_listar_views.listar,
        name='r4099_evtfech_output'),

    url(r'^r5001-evttotal/api/$',
        r5001_evttotal_api_views.r5001evtTotalList.as_view() ),

    url(r'^r5001-evttotal/api/(?P<pk>[0-9]+)/$',
        r5001_evttotal_api_views.r5001evtTotalDetail.as_view() ),

    url(r'^r5001-evttotal/$',
        r5001_evttotal_listar_views.listar,
        name='r5001_evttotal'),

    url(r'^r5001-evttotal/(?P<output>[\w-]+)/$',
        r5001_evttotal_listar_views.listar,
        name='r5001_evttotal_output'),

    url(r'^r5001-evttotal/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r5001_evttotal_recibos_views.recibo,
        name='r5001_evttotal_recibo'),

    url(r'^r5011-evttotalcontrib/api/$',
        r5011_evttotalcontrib_api_views.r5011evtTotalContribList.as_view() ),

    url(r'^r5011-evttotalcontrib/api/(?P<pk>[0-9]+)/$',
        r5011_evttotalcontrib_api_views.r5011evtTotalContribDetail.as_view() ),

    url(r'^r5011-evttotalcontrib/$',
        r5011_evttotalcontrib_listar_views.listar,
        name='r5011_evttotalcontrib'),

    url(r'^r5011-evttotalcontrib/(?P<output>[\w-]+)/$',
        r5011_evttotalcontrib_listar_views.listar,
        name='r5011_evttotalcontrib_output'),

    url(r'^r5011-evttotalcontrib/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r5011_evttotalcontrib_recibos_views.recibo,
        name='r5011_evttotalcontrib_recibo'),

    url(r'^r9000-evtexclusao/apagar/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_apagar_views.apagar,
        name='r9000_evtexclusao_apagar'),

    url(r'^r9000-evtexclusao/api/$',
        r9000_evtexclusao_api_views.r9000evtExclusaoList.as_view() ),

    url(r'^r9000-evtexclusao/api/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_api_views.r9000evtExclusaoDetail.as_view() ),

    url(r'^r9000-evtexclusao/$',
        r9000_evtexclusao_listar_views.listar,
        name='r9000_evtexclusao'),

    url(r'^r9000-evtexclusao/verificar/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_verificar_views.verificar,
        name='r9000_evtexclusao_verificar'),

    url(r'^r9000-evtexclusao/verificar/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r9000_evtexclusao_verificar_views.verificar,
        name='r9000_evtexclusao_verificar_output'),

    url(r'^r9000-evtexclusao/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r9000_evtexclusao_recibos_views.recibo,
        name='r9000_evtexclusao_recibo'),

    url(r'^r9000-evtexclusao/duplicar/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_duplicar_views.duplicar,
        name='r9000_evtexclusao_duplicar'),

    url(r'^r9000-evtexclusao/criar-alteracao/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_criar_alteracao_views.criar_alteracao,
        name='r9000_evtexclusao_criar_alteracao'),

    url(r'^r9000-evtexclusao/criar-exclusao/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_criar_exclusao_views.criar_exclusao,
        name='r9000_evtexclusao_criar_exclusao'),

    url(r'^r9000-evtexclusao/xml/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_gerar_xml_views.gerar_xml,
        name='r9000_evtexclusao_xml'),

    url(r'^r9000-evtexclusao/alterar-identidade/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_alterar_identidade_views.alterar_identidade,
        name='r9000_evtexclusao_alterar_identidade'),

    url(r'^r9000-evtexclusao/abrir-evento-para-edicao/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_abrir_evento_para_edicao_views.abrir_evento_para_edicao,
        name='r9000_evtexclusao_abrir_evento_para_edicao'),

    url(r'^r9000-evtexclusao/validar-evento/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_validar_evento_views.validar_evento,
        name='r9000_evtexclusao_validar_evento'),

    url(r'^r9000-evtexclusao/validar-evento/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r9000_evtexclusao_validar_evento_views.validar_evento,
        name='r9000_evtexclusao_validar_evento_api'),

    url(r'^r9000-evtexclusao/salvar/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_salvar_views.salvar,
        name='r9000_evtexclusao_salvar'),

    url(r'^r9000-evtexclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r9000_evtexclusao_salvar_views.salvar,
        name='r9000_evtexclusao_salvar_tab'),

    url(r'^r9000-evtexclusao/gerar-identidade/(?P<pk>[0-9]+)/$',
        r9000_evtexclusao_gerar_identidade_views.gerar_identidade,
        name='r9000_evtexclusao_gerar_identidade'),

    url(r'^r9000-evtexclusao/cadastrar/$',
        r9000_evtexclusao_salvar_views.salvar,
        name='r9000_evtexclusao_cadastrar'),

    url(r'^r9000-evtexclusao/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r9000_evtexclusao_salvar_views.salvar,
        name='r9000_evtexclusao_salvar_output'),

    url(r'^r9000-evtexclusao/(?P<output>[\w-]+)/$',
        r9000_evtexclusao_listar_views.listar,
        name='r9000_evtexclusao_output'),

    url(r'^r9001-evttotal/api/$',
        r9001_evttotal_api_views.r9001evtTotalList.as_view() ),

    url(r'^r9001-evttotal/api/(?P<pk>[0-9]+)/$',
        r9001_evttotal_api_views.r9001evtTotalDetail.as_view() ),

    url(r'^r9001-evttotal/$',
        r9001_evttotal_listar_views.listar,
        name='r9001_evttotal'),

    url(r'^r9001-evttotal/(?P<output>[\w-]+)/$',
        r9001_evttotal_listar_views.listar,
        name='r9001_evttotal_output'),

    url(r'^r9001-evttotal/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r9001_evttotal_recibos_views.recibo,
        name='r9001_evttotal_recibo'),

    url(r'^r9002-evtret/api/$',
        r9002_evtret_api_views.r9002evtRetList.as_view() ),

    url(r'^r9002-evtret/api/(?P<pk>[0-9]+)/$',
        r9002_evtret_api_views.r9002evtRetDetail.as_view() ),

    url(r'^r9002-evtret/$',
        r9002_evtret_listar_views.listar,
        name='r9002_evtret'),

    url(r'^r9002-evtret/(?P<output>[\w-]+)/$',
        r9002_evtret_listar_views.listar,
        name='r9002_evtret_output'),

    url(r'^r9002-evtret/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r9002_evtret_recibos_views.recibo,
        name='r9002_evtret_recibo'),

    url(r'^r9011-evttotalcontrib/api/$',
        r9011_evttotalcontrib_api_views.r9011evtTotalContribList.as_view() ),

    url(r'^r9011-evttotalcontrib/api/(?P<pk>[0-9]+)/$',
        r9011_evttotalcontrib_api_views.r9011evtTotalContribDetail.as_view() ),

    url(r'^r9011-evttotalcontrib/$',
        r9011_evttotalcontrib_listar_views.listar,
        name='r9011_evttotalcontrib'),

    url(r'^r9011-evttotalcontrib/(?P<output>[\w-]+)/$',
        r9011_evttotalcontrib_listar_views.listar,
        name='r9011_evttotalcontrib_output'),

    url(r'^r9011-evttotalcontrib/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r9011_evttotalcontrib_recibos_views.recibo,
        name='r9011_evttotalcontrib_recibo'),

    url(r'^r9012-evtretcons/api/$',
        r9012_evtretcons_api_views.r9012evtRetConsList.as_view() ),

    url(r'^r9012-evtretcons/api/(?P<pk>[0-9]+)/$',
        r9012_evtretcons_api_views.r9012evtRetConsDetail.as_view() ),

    url(r'^r9012-evtretcons/$',
        r9012_evtretcons_listar_views.listar,
        name='r9012_evtretcons'),

    url(r'^r9012-evtretcons/(?P<output>[\w-]+)/$',
        r9012_evtretcons_listar_views.listar,
        name='r9012_evtretcons_output'),

    url(r'^r9012-evtretcons/recibo/(?P<pk>[0-9]+)/(?P<output>[\w-]+)/$',
        r9012_evtretcons_recibos_views.recibo,
        name='r9012_evtretcons_recibo'),


]