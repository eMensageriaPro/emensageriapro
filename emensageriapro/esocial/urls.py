#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.esocial.views import s1000_evtinfoempregador as s1000_evtinfoempregador_views
from emensageriapro.esocial.views import s1000_evtinfoempregador_verificar as s1000_evtinfoempregador_verificar_views
from emensageriapro.esocial.views import s1005_evttabestab as s1005_evttabestab_views
from emensageriapro.esocial.views import s1005_evttabestab_verificar as s1005_evttabestab_verificar_views
from emensageriapro.esocial.views import s1010_evttabrubrica as s1010_evttabrubrica_views
from emensageriapro.esocial.views import s1010_evttabrubrica_verificar as s1010_evttabrubrica_verificar_views
from emensageriapro.esocial.views import s1020_evttablotacao as s1020_evttablotacao_views
from emensageriapro.esocial.views import s1020_evttablotacao_verificar as s1020_evttablotacao_verificar_views
from emensageriapro.esocial.views import s1030_evttabcargo as s1030_evttabcargo_views
from emensageriapro.esocial.views import s1030_evttabcargo_verificar as s1030_evttabcargo_verificar_views
from emensageriapro.esocial.views import s1035_evttabcarreira as s1035_evttabcarreira_views
from emensageriapro.esocial.views import s1035_evttabcarreira_verificar as s1035_evttabcarreira_verificar_views
from emensageriapro.esocial.views import s1040_evttabfuncao as s1040_evttabfuncao_views
from emensageriapro.esocial.views import s1040_evttabfuncao_verificar as s1040_evttabfuncao_verificar_views
from emensageriapro.esocial.views import s1050_evttabhortur as s1050_evttabhortur_views
from emensageriapro.esocial.views import s1050_evttabhortur_verificar as s1050_evttabhortur_verificar_views
from emensageriapro.esocial.views import s1060_evttabambiente as s1060_evttabambiente_views
from emensageriapro.esocial.views import s1060_evttabambiente_verificar as s1060_evttabambiente_verificar_views
from emensageriapro.esocial.views import s1070_evttabprocesso as s1070_evttabprocesso_views
from emensageriapro.esocial.views import s1070_evttabprocesso_verificar as s1070_evttabprocesso_verificar_views
from emensageriapro.esocial.views import s1080_evttaboperport as s1080_evttaboperport_views
from emensageriapro.esocial.views import s1080_evttaboperport_verificar as s1080_evttaboperport_verificar_views
from emensageriapro.esocial.views import s1200_evtremun as s1200_evtremun_views
from emensageriapro.esocial.views import s1200_evtremun_verificar as s1200_evtremun_verificar_views
from emensageriapro.esocial.views import s1202_evtrmnrpps as s1202_evtrmnrpps_views
from emensageriapro.esocial.views import s1202_evtrmnrpps_verificar as s1202_evtrmnrpps_verificar_views
from emensageriapro.esocial.views import s1207_evtbenprrp as s1207_evtbenprrp_views
from emensageriapro.esocial.views import s1207_evtbenprrp_verificar as s1207_evtbenprrp_verificar_views
from emensageriapro.esocial.views import s1210_evtpgtos as s1210_evtpgtos_views
from emensageriapro.esocial.views import s1210_evtpgtos_verificar as s1210_evtpgtos_verificar_views
from emensageriapro.esocial.views import s1250_evtaqprod as s1250_evtaqprod_views
from emensageriapro.esocial.views import s1250_evtaqprod_verificar as s1250_evtaqprod_verificar_views
from emensageriapro.esocial.views import s1260_evtcomprod as s1260_evtcomprod_views
from emensageriapro.esocial.views import s1260_evtcomprod_verificar as s1260_evtcomprod_verificar_views
from emensageriapro.esocial.views import s1270_evtcontratavnp as s1270_evtcontratavnp_views
from emensageriapro.esocial.views import s1270_evtcontratavnp_verificar as s1270_evtcontratavnp_verificar_views
from emensageriapro.esocial.views import s1280_evtinfocomplper as s1280_evtinfocomplper_views
from emensageriapro.esocial.views import s1280_evtinfocomplper_verificar as s1280_evtinfocomplper_verificar_views
from emensageriapro.esocial.views import s1295_evttotconting as s1295_evttotconting_views
from emensageriapro.esocial.views import s1295_evttotconting_verificar as s1295_evttotconting_verificar_views
from emensageriapro.esocial.views import s1298_evtreabreevper as s1298_evtreabreevper_views
from emensageriapro.esocial.views import s1298_evtreabreevper_verificar as s1298_evtreabreevper_verificar_views
from emensageriapro.esocial.views import s1299_evtfechaevper as s1299_evtfechaevper_views
from emensageriapro.esocial.views import s1299_evtfechaevper_verificar as s1299_evtfechaevper_verificar_views
from emensageriapro.esocial.views import s1300_evtcontrsindpatr as s1300_evtcontrsindpatr_views
from emensageriapro.esocial.views import s1300_evtcontrsindpatr_verificar as s1300_evtcontrsindpatr_verificar_views
from emensageriapro.esocial.views import s2190_evtadmprelim as s2190_evtadmprelim_views
from emensageriapro.esocial.views import s2190_evtadmprelim_verificar as s2190_evtadmprelim_verificar_views
from emensageriapro.esocial.views import s2200_evtadmissao as s2200_evtadmissao_views
from emensageriapro.esocial.views import s2200_evtadmissao_verificar as s2200_evtadmissao_verificar_views
from emensageriapro.esocial.views import s2205_evtaltcadastral as s2205_evtaltcadastral_views
from emensageriapro.esocial.views import s2205_evtaltcadastral_verificar as s2205_evtaltcadastral_verificar_views
from emensageriapro.esocial.views import s2206_evtaltcontratual as s2206_evtaltcontratual_views
from emensageriapro.esocial.views import s2206_evtaltcontratual_verificar as s2206_evtaltcontratual_verificar_views
from emensageriapro.esocial.views import s2210_evtcat as s2210_evtcat_views
from emensageriapro.esocial.views import s2210_evtcat_verificar as s2210_evtcat_verificar_views
from emensageriapro.esocial.views import s2220_evtmonit as s2220_evtmonit_views
from emensageriapro.esocial.views import s2220_evtmonit_verificar as s2220_evtmonit_verificar_views
from emensageriapro.esocial.views import s2221_evttoxic as s2221_evttoxic_views
from emensageriapro.esocial.views import s2221_evttoxic_verificar as s2221_evttoxic_verificar_views
from emensageriapro.esocial.views import s2230_evtafasttemp as s2230_evtafasttemp_views
from emensageriapro.esocial.views import s2230_evtafasttemp_verificar as s2230_evtafasttemp_verificar_views
from emensageriapro.esocial.views import s2231_evtcessao as s2231_evtcessao_views
from emensageriapro.esocial.views import s2231_evtcessao_verificar as s2231_evtcessao_verificar_views
from emensageriapro.esocial.views import s2240_evtexprisco as s2240_evtexprisco_views
from emensageriapro.esocial.views import s2240_evtexprisco_verificar as s2240_evtexprisco_verificar_views
from emensageriapro.esocial.views import s2241_evtinsapo as s2241_evtinsapo_views
from emensageriapro.esocial.views import s2241_evtinsapo_verificar as s2241_evtinsapo_verificar_views
from emensageriapro.esocial.views import s2245_evttreicap as s2245_evttreicap_views
from emensageriapro.esocial.views import s2245_evttreicap_verificar as s2245_evttreicap_verificar_views
from emensageriapro.esocial.views import s2250_evtavprevio as s2250_evtavprevio_views
from emensageriapro.esocial.views import s2250_evtavprevio_verificar as s2250_evtavprevio_verificar_views
from emensageriapro.esocial.views import s2260_evtconvinterm as s2260_evtconvinterm_views
from emensageriapro.esocial.views import s2260_evtconvinterm_verificar as s2260_evtconvinterm_verificar_views
from emensageriapro.esocial.views import s2298_evtreintegr as s2298_evtreintegr_views
from emensageriapro.esocial.views import s2298_evtreintegr_verificar as s2298_evtreintegr_verificar_views
from emensageriapro.esocial.views import s2299_evtdeslig as s2299_evtdeslig_views
from emensageriapro.esocial.views import s2299_evtdeslig_verificar as s2299_evtdeslig_verificar_views
from emensageriapro.esocial.views import s2300_evttsvinicio as s2300_evttsvinicio_views
from emensageriapro.esocial.views import s2300_evttsvinicio_verificar as s2300_evttsvinicio_verificar_views
from emensageriapro.esocial.views import s2306_evttsvaltcontr as s2306_evttsvaltcontr_views
from emensageriapro.esocial.views import s2306_evttsvaltcontr_verificar as s2306_evttsvaltcontr_verificar_views
from emensageriapro.esocial.views import s2399_evttsvtermino as s2399_evttsvtermino_views
from emensageriapro.esocial.views import s2399_evttsvtermino_verificar as s2399_evttsvtermino_verificar_views
from emensageriapro.esocial.views import s2400_evtcdbenefin as s2400_evtcdbenefin_views
from emensageriapro.esocial.views import s2400_evtcdbenefin_verificar as s2400_evtcdbenefin_verificar_views
from emensageriapro.esocial.views import s2405_evtcdbenefalt as s2405_evtcdbenefalt_views
from emensageriapro.esocial.views import s2405_evtcdbenefalt_verificar as s2405_evtcdbenefalt_verificar_views
from emensageriapro.esocial.views import s2410_evtcdbenin as s2410_evtcdbenin_views
from emensageriapro.esocial.views import s2410_evtcdbenin_verificar as s2410_evtcdbenin_verificar_views
from emensageriapro.esocial.views import s2416_evtcdbenalt as s2416_evtcdbenalt_views
from emensageriapro.esocial.views import s2416_evtcdbenalt_verificar as s2416_evtcdbenalt_verificar_views
from emensageriapro.esocial.views import s2420_evtcdbenterm as s2420_evtcdbenterm_views
from emensageriapro.esocial.views import s2420_evtcdbenterm_verificar as s2420_evtcdbenterm_verificar_views
from emensageriapro.esocial.views import s3000_evtexclusao as s3000_evtexclusao_views
from emensageriapro.esocial.views import s3000_evtexclusao_verificar as s3000_evtexclusao_verificar_views
from emensageriapro.esocial.views import s5001_evtbasestrab as s5001_evtbasestrab_views
from emensageriapro.esocial.views import s5001_evtbasestrab_verificar as s5001_evtbasestrab_verificar_views
from emensageriapro.esocial.views import s5002_evtirrfbenef as s5002_evtirrfbenef_views
from emensageriapro.esocial.views import s5002_evtirrfbenef_verificar as s5002_evtirrfbenef_verificar_views
from emensageriapro.esocial.views import s5011_evtcs as s5011_evtcs_views
from emensageriapro.esocial.views import s5011_evtcs_verificar as s5011_evtcs_verificar_views
from emensageriapro.esocial.views import s5012_evtirrf as s5012_evtirrf_views
from emensageriapro.esocial.views import s5012_evtirrf_verificar as s5012_evtirrf_verificar_views





urlpatterns = [



url(r'^s1000-evtinfoempregador/apagar/(?P<hash>.*)/$', 
        s1000_evtinfoempregador_views.apagar, 
        name='s1000_evtinfoempregador_apagar'),

url(r'^s1000-evtinfoempregador/api/$',
            s1000_evtinfoempregador_views.s1000evtInfoEmpregadorList.as_view() ),

        url(r'^s1000-evtinfoempregador/api/(?P<pk>[0-9]+)/$',
            s1000_evtinfoempregador_views.s1000evtInfoEmpregadorDetail.as_view() ),

url(r'^s1000-evtinfoempregador/listar/(?P<hash>.*)/$', 
        s1000_evtinfoempregador_views.listar, 
        name='s1000_evtinfoempregador'),
        
url(r'^s1000-evtinfoempregador/verificar/(?P<hash>.*)/$', 
        s1000_evtinfoempregador_verificar_views.verificar, 
        name='s1000_evtinfoempregador_verificar'),
        
url(r'^s1000-evtinfoempregador/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1000_evtinfoempregador_verificar_views.recibo, 
        name='s1000_evtinfoempregador_recibo'),
        
        
url(r'^s1000-evtinfoempregador/duplicar/(?P<hash>.*)/$',
        s1000_evtinfoempregador_verificar_views.duplicar,
        name='s1000_evtinfoempregador_duplicar'),

url(r'^s1000-evtinfoempregador/criar-alteracao/(?P<hash>.*)/$',
        s1000_evtinfoempregador_verificar_views.criar_alteracao,
        name='s1000_evtinfoempregador_criar_alteracao'),

url(r'^s1000-evtinfoempregador/criar-exclusao/(?P<hash>.*)/$',
        s1000_evtinfoempregador_verificar_views.criar_exclusao,
        name='s1000_evtinfoempregador_criar_exclusao'),
        
url(r'^s1000-evtinfoempregador/xml/(?P<hash>.*)/$', 
        s1000_evtinfoempregador_verificar_views.gerar_xml, 
                name='s1000_evtinfoempregador_xml'),
                

url(r'^s1000-evtinfoempregador/alterar-identidade/(?P<hash>.*)/$',
        s1000_evtinfoempregador_verificar_views.alterar_identidade,
        name='s1000_evtinfoempregador_alterar_identidade'),

url(r'^s1000-evtinfoempregador/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1000_evtinfoempregador_verificar_views.abrir_evento_para_edicao,
        name='s1000_evtinfoempregador_abrir_evento_para_edicao'),

url(r'^s1000-evtinfoempregador/validar-evento/(?P<hash>.*)/$',
        s1000_evtinfoempregador_verificar_views.validar_evento,
        name='s1000_evtinfoempregador_validar_evento'),

url(r'^s1000-evtinfoempregador/salvar/(?P<hash>.*)/$', 
        s1000_evtinfoempregador_views.salvar, 
        name='s1000_evtinfoempregador_salvar'),
        

url(r'^scripts/gerar-identidade/s1000-evtinfoempregador/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1000_evtinfoempregador_views.gerar_identidade, 
        name='s1000_evtinfoempregador_gerar_identidade'),



url(r'^s1005-evttabestab/apagar/(?P<hash>.*)/$', 
        s1005_evttabestab_views.apagar, 
        name='s1005_evttabestab_apagar'),

url(r'^s1005-evttabestab/api/$',
            s1005_evttabestab_views.s1005evtTabEstabList.as_view() ),

        url(r'^s1005-evttabestab/api/(?P<pk>[0-9]+)/$',
            s1005_evttabestab_views.s1005evtTabEstabDetail.as_view() ),

url(r'^s1005-evttabestab/listar/(?P<hash>.*)/$', 
        s1005_evttabestab_views.listar, 
        name='s1005_evttabestab'),
        
url(r'^s1005-evttabestab/verificar/(?P<hash>.*)/$', 
        s1005_evttabestab_verificar_views.verificar, 
        name='s1005_evttabestab_verificar'),
        
url(r'^s1005-evttabestab/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1005_evttabestab_verificar_views.recibo, 
        name='s1005_evttabestab_recibo'),
        
        
url(r'^s1005-evttabestab/duplicar/(?P<hash>.*)/$',
        s1005_evttabestab_verificar_views.duplicar,
        name='s1005_evttabestab_duplicar'),

url(r'^s1005-evttabestab/criar-alteracao/(?P<hash>.*)/$',
        s1005_evttabestab_verificar_views.criar_alteracao,
        name='s1005_evttabestab_criar_alteracao'),

url(r'^s1005-evttabestab/criar-exclusao/(?P<hash>.*)/$',
        s1005_evttabestab_verificar_views.criar_exclusao,
        name='s1005_evttabestab_criar_exclusao'),
        
url(r'^s1005-evttabestab/xml/(?P<hash>.*)/$', 
        s1005_evttabestab_verificar_views.gerar_xml, 
                name='s1005_evttabestab_xml'),
                

url(r'^s1005-evttabestab/alterar-identidade/(?P<hash>.*)/$',
        s1005_evttabestab_verificar_views.alterar_identidade,
        name='s1005_evttabestab_alterar_identidade'),

url(r'^s1005-evttabestab/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1005_evttabestab_verificar_views.abrir_evento_para_edicao,
        name='s1005_evttabestab_abrir_evento_para_edicao'),

url(r'^s1005-evttabestab/validar-evento/(?P<hash>.*)/$',
        s1005_evttabestab_verificar_views.validar_evento,
        name='s1005_evttabestab_validar_evento'),

url(r'^s1005-evttabestab/salvar/(?P<hash>.*)/$', 
        s1005_evttabestab_views.salvar, 
        name='s1005_evttabestab_salvar'),
        

url(r'^scripts/gerar-identidade/s1005-evttabestab/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1005_evttabestab_views.gerar_identidade, 
        name='s1005_evttabestab_gerar_identidade'),



url(r'^s1010-evttabrubrica/apagar/(?P<hash>.*)/$', 
        s1010_evttabrubrica_views.apagar, 
        name='s1010_evttabrubrica_apagar'),

url(r'^s1010-evttabrubrica/api/$',
            s1010_evttabrubrica_views.s1010evtTabRubricaList.as_view() ),

        url(r'^s1010-evttabrubrica/api/(?P<pk>[0-9]+)/$',
            s1010_evttabrubrica_views.s1010evtTabRubricaDetail.as_view() ),

url(r'^s1010-evttabrubrica/listar/(?P<hash>.*)/$', 
        s1010_evttabrubrica_views.listar, 
        name='s1010_evttabrubrica'),
        
url(r'^s1010-evttabrubrica/verificar/(?P<hash>.*)/$', 
        s1010_evttabrubrica_verificar_views.verificar, 
        name='s1010_evttabrubrica_verificar'),
        
url(r'^s1010-evttabrubrica/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1010_evttabrubrica_verificar_views.recibo, 
        name='s1010_evttabrubrica_recibo'),
        
        
url(r'^s1010-evttabrubrica/duplicar/(?P<hash>.*)/$',
        s1010_evttabrubrica_verificar_views.duplicar,
        name='s1010_evttabrubrica_duplicar'),

url(r'^s1010-evttabrubrica/criar-alteracao/(?P<hash>.*)/$',
        s1010_evttabrubrica_verificar_views.criar_alteracao,
        name='s1010_evttabrubrica_criar_alteracao'),

url(r'^s1010-evttabrubrica/criar-exclusao/(?P<hash>.*)/$',
        s1010_evttabrubrica_verificar_views.criar_exclusao,
        name='s1010_evttabrubrica_criar_exclusao'),
        
url(r'^s1010-evttabrubrica/xml/(?P<hash>.*)/$', 
        s1010_evttabrubrica_verificar_views.gerar_xml, 
                name='s1010_evttabrubrica_xml'),
                

url(r'^s1010-evttabrubrica/alterar-identidade/(?P<hash>.*)/$',
        s1010_evttabrubrica_verificar_views.alterar_identidade,
        name='s1010_evttabrubrica_alterar_identidade'),

url(r'^s1010-evttabrubrica/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1010_evttabrubrica_verificar_views.abrir_evento_para_edicao,
        name='s1010_evttabrubrica_abrir_evento_para_edicao'),

url(r'^s1010-evttabrubrica/validar-evento/(?P<hash>.*)/$',
        s1010_evttabrubrica_verificar_views.validar_evento,
        name='s1010_evttabrubrica_validar_evento'),

url(r'^s1010-evttabrubrica/salvar/(?P<hash>.*)/$', 
        s1010_evttabrubrica_views.salvar, 
        name='s1010_evttabrubrica_salvar'),
        

url(r'^scripts/gerar-identidade/s1010-evttabrubrica/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1010_evttabrubrica_views.gerar_identidade, 
        name='s1010_evttabrubrica_gerar_identidade'),



url(r'^s1020-evttablotacao/apagar/(?P<hash>.*)/$', 
        s1020_evttablotacao_views.apagar, 
        name='s1020_evttablotacao_apagar'),

url(r'^s1020-evttablotacao/api/$',
            s1020_evttablotacao_views.s1020evtTabLotacaoList.as_view() ),

        url(r'^s1020-evttablotacao/api/(?P<pk>[0-9]+)/$',
            s1020_evttablotacao_views.s1020evtTabLotacaoDetail.as_view() ),

url(r'^s1020-evttablotacao/listar/(?P<hash>.*)/$', 
        s1020_evttablotacao_views.listar, 
        name='s1020_evttablotacao'),
        
url(r'^s1020-evttablotacao/verificar/(?P<hash>.*)/$', 
        s1020_evttablotacao_verificar_views.verificar, 
        name='s1020_evttablotacao_verificar'),
        
url(r'^s1020-evttablotacao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1020_evttablotacao_verificar_views.recibo, 
        name='s1020_evttablotacao_recibo'),
        
        
url(r'^s1020-evttablotacao/duplicar/(?P<hash>.*)/$',
        s1020_evttablotacao_verificar_views.duplicar,
        name='s1020_evttablotacao_duplicar'),

url(r'^s1020-evttablotacao/criar-alteracao/(?P<hash>.*)/$',
        s1020_evttablotacao_verificar_views.criar_alteracao,
        name='s1020_evttablotacao_criar_alteracao'),

url(r'^s1020-evttablotacao/criar-exclusao/(?P<hash>.*)/$',
        s1020_evttablotacao_verificar_views.criar_exclusao,
        name='s1020_evttablotacao_criar_exclusao'),
        
url(r'^s1020-evttablotacao/xml/(?P<hash>.*)/$', 
        s1020_evttablotacao_verificar_views.gerar_xml, 
                name='s1020_evttablotacao_xml'),
                

url(r'^s1020-evttablotacao/alterar-identidade/(?P<hash>.*)/$',
        s1020_evttablotacao_verificar_views.alterar_identidade,
        name='s1020_evttablotacao_alterar_identidade'),

url(r'^s1020-evttablotacao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1020_evttablotacao_verificar_views.abrir_evento_para_edicao,
        name='s1020_evttablotacao_abrir_evento_para_edicao'),

url(r'^s1020-evttablotacao/validar-evento/(?P<hash>.*)/$',
        s1020_evttablotacao_verificar_views.validar_evento,
        name='s1020_evttablotacao_validar_evento'),

url(r'^s1020-evttablotacao/salvar/(?P<hash>.*)/$', 
        s1020_evttablotacao_views.salvar, 
        name='s1020_evttablotacao_salvar'),
        

url(r'^scripts/gerar-identidade/s1020-evttablotacao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1020_evttablotacao_views.gerar_identidade, 
        name='s1020_evttablotacao_gerar_identidade'),



url(r'^s1030-evttabcargo/apagar/(?P<hash>.*)/$', 
        s1030_evttabcargo_views.apagar, 
        name='s1030_evttabcargo_apagar'),

url(r'^s1030-evttabcargo/api/$',
            s1030_evttabcargo_views.s1030evtTabCargoList.as_view() ),

        url(r'^s1030-evttabcargo/api/(?P<pk>[0-9]+)/$',
            s1030_evttabcargo_views.s1030evtTabCargoDetail.as_view() ),

url(r'^s1030-evttabcargo/listar/(?P<hash>.*)/$', 
        s1030_evttabcargo_views.listar, 
        name='s1030_evttabcargo'),
        
url(r'^s1030-evttabcargo/verificar/(?P<hash>.*)/$', 
        s1030_evttabcargo_verificar_views.verificar, 
        name='s1030_evttabcargo_verificar'),
        
url(r'^s1030-evttabcargo/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1030_evttabcargo_verificar_views.recibo, 
        name='s1030_evttabcargo_recibo'),
        
        
url(r'^s1030-evttabcargo/duplicar/(?P<hash>.*)/$',
        s1030_evttabcargo_verificar_views.duplicar,
        name='s1030_evttabcargo_duplicar'),

url(r'^s1030-evttabcargo/criar-alteracao/(?P<hash>.*)/$',
        s1030_evttabcargo_verificar_views.criar_alteracao,
        name='s1030_evttabcargo_criar_alteracao'),

url(r'^s1030-evttabcargo/criar-exclusao/(?P<hash>.*)/$',
        s1030_evttabcargo_verificar_views.criar_exclusao,
        name='s1030_evttabcargo_criar_exclusao'),
        
url(r'^s1030-evttabcargo/xml/(?P<hash>.*)/$', 
        s1030_evttabcargo_verificar_views.gerar_xml, 
                name='s1030_evttabcargo_xml'),
                

url(r'^s1030-evttabcargo/alterar-identidade/(?P<hash>.*)/$',
        s1030_evttabcargo_verificar_views.alterar_identidade,
        name='s1030_evttabcargo_alterar_identidade'),

url(r'^s1030-evttabcargo/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1030_evttabcargo_verificar_views.abrir_evento_para_edicao,
        name='s1030_evttabcargo_abrir_evento_para_edicao'),

url(r'^s1030-evttabcargo/validar-evento/(?P<hash>.*)/$',
        s1030_evttabcargo_verificar_views.validar_evento,
        name='s1030_evttabcargo_validar_evento'),

url(r'^s1030-evttabcargo/salvar/(?P<hash>.*)/$', 
        s1030_evttabcargo_views.salvar, 
        name='s1030_evttabcargo_salvar'),
        

url(r'^scripts/gerar-identidade/s1030-evttabcargo/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1030_evttabcargo_views.gerar_identidade, 
        name='s1030_evttabcargo_gerar_identidade'),



url(r'^s1035-evttabcarreira/apagar/(?P<hash>.*)/$', 
        s1035_evttabcarreira_views.apagar, 
        name='s1035_evttabcarreira_apagar'),

url(r'^s1035-evttabcarreira/api/$',
            s1035_evttabcarreira_views.s1035evtTabCarreiraList.as_view() ),

        url(r'^s1035-evttabcarreira/api/(?P<pk>[0-9]+)/$',
            s1035_evttabcarreira_views.s1035evtTabCarreiraDetail.as_view() ),

url(r'^s1035-evttabcarreira/listar/(?P<hash>.*)/$', 
        s1035_evttabcarreira_views.listar, 
        name='s1035_evttabcarreira'),
        
url(r'^s1035-evttabcarreira/verificar/(?P<hash>.*)/$', 
        s1035_evttabcarreira_verificar_views.verificar, 
        name='s1035_evttabcarreira_verificar'),
        
url(r'^s1035-evttabcarreira/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1035_evttabcarreira_verificar_views.recibo, 
        name='s1035_evttabcarreira_recibo'),
        
        
url(r'^s1035-evttabcarreira/duplicar/(?P<hash>.*)/$',
        s1035_evttabcarreira_verificar_views.duplicar,
        name='s1035_evttabcarreira_duplicar'),

url(r'^s1035-evttabcarreira/criar-alteracao/(?P<hash>.*)/$',
        s1035_evttabcarreira_verificar_views.criar_alteracao,
        name='s1035_evttabcarreira_criar_alteracao'),

url(r'^s1035-evttabcarreira/criar-exclusao/(?P<hash>.*)/$',
        s1035_evttabcarreira_verificar_views.criar_exclusao,
        name='s1035_evttabcarreira_criar_exclusao'),
        
url(r'^s1035-evttabcarreira/xml/(?P<hash>.*)/$', 
        s1035_evttabcarreira_verificar_views.gerar_xml, 
                name='s1035_evttabcarreira_xml'),
                

url(r'^s1035-evttabcarreira/alterar-identidade/(?P<hash>.*)/$',
        s1035_evttabcarreira_verificar_views.alterar_identidade,
        name='s1035_evttabcarreira_alterar_identidade'),

url(r'^s1035-evttabcarreira/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1035_evttabcarreira_verificar_views.abrir_evento_para_edicao,
        name='s1035_evttabcarreira_abrir_evento_para_edicao'),

url(r'^s1035-evttabcarreira/validar-evento/(?P<hash>.*)/$',
        s1035_evttabcarreira_verificar_views.validar_evento,
        name='s1035_evttabcarreira_validar_evento'),

url(r'^s1035-evttabcarreira/salvar/(?P<hash>.*)/$', 
        s1035_evttabcarreira_views.salvar, 
        name='s1035_evttabcarreira_salvar'),
        

url(r'^scripts/gerar-identidade/s1035-evttabcarreira/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1035_evttabcarreira_views.gerar_identidade, 
        name='s1035_evttabcarreira_gerar_identidade'),



url(r'^s1040-evttabfuncao/apagar/(?P<hash>.*)/$', 
        s1040_evttabfuncao_views.apagar, 
        name='s1040_evttabfuncao_apagar'),

url(r'^s1040-evttabfuncao/api/$',
            s1040_evttabfuncao_views.s1040evtTabFuncaoList.as_view() ),

        url(r'^s1040-evttabfuncao/api/(?P<pk>[0-9]+)/$',
            s1040_evttabfuncao_views.s1040evtTabFuncaoDetail.as_view() ),

url(r'^s1040-evttabfuncao/listar/(?P<hash>.*)/$', 
        s1040_evttabfuncao_views.listar, 
        name='s1040_evttabfuncao'),
        
url(r'^s1040-evttabfuncao/verificar/(?P<hash>.*)/$', 
        s1040_evttabfuncao_verificar_views.verificar, 
        name='s1040_evttabfuncao_verificar'),
        
url(r'^s1040-evttabfuncao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1040_evttabfuncao_verificar_views.recibo, 
        name='s1040_evttabfuncao_recibo'),
        
        
url(r'^s1040-evttabfuncao/duplicar/(?P<hash>.*)/$',
        s1040_evttabfuncao_verificar_views.duplicar,
        name='s1040_evttabfuncao_duplicar'),

url(r'^s1040-evttabfuncao/criar-alteracao/(?P<hash>.*)/$',
        s1040_evttabfuncao_verificar_views.criar_alteracao,
        name='s1040_evttabfuncao_criar_alteracao'),

url(r'^s1040-evttabfuncao/criar-exclusao/(?P<hash>.*)/$',
        s1040_evttabfuncao_verificar_views.criar_exclusao,
        name='s1040_evttabfuncao_criar_exclusao'),
        
url(r'^s1040-evttabfuncao/xml/(?P<hash>.*)/$', 
        s1040_evttabfuncao_verificar_views.gerar_xml, 
                name='s1040_evttabfuncao_xml'),
                

url(r'^s1040-evttabfuncao/alterar-identidade/(?P<hash>.*)/$',
        s1040_evttabfuncao_verificar_views.alterar_identidade,
        name='s1040_evttabfuncao_alterar_identidade'),

url(r'^s1040-evttabfuncao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1040_evttabfuncao_verificar_views.abrir_evento_para_edicao,
        name='s1040_evttabfuncao_abrir_evento_para_edicao'),

url(r'^s1040-evttabfuncao/validar-evento/(?P<hash>.*)/$',
        s1040_evttabfuncao_verificar_views.validar_evento,
        name='s1040_evttabfuncao_validar_evento'),

url(r'^s1040-evttabfuncao/salvar/(?P<hash>.*)/$', 
        s1040_evttabfuncao_views.salvar, 
        name='s1040_evttabfuncao_salvar'),
        

url(r'^scripts/gerar-identidade/s1040-evttabfuncao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1040_evttabfuncao_views.gerar_identidade, 
        name='s1040_evttabfuncao_gerar_identidade'),



url(r'^s1050-evttabhortur/apagar/(?P<hash>.*)/$', 
        s1050_evttabhortur_views.apagar, 
        name='s1050_evttabhortur_apagar'),

url(r'^s1050-evttabhortur/api/$',
            s1050_evttabhortur_views.s1050evtTabHorTurList.as_view() ),

        url(r'^s1050-evttabhortur/api/(?P<pk>[0-9]+)/$',
            s1050_evttabhortur_views.s1050evtTabHorTurDetail.as_view() ),

url(r'^s1050-evttabhortur/listar/(?P<hash>.*)/$', 
        s1050_evttabhortur_views.listar, 
        name='s1050_evttabhortur'),
        
url(r'^s1050-evttabhortur/verificar/(?P<hash>.*)/$', 
        s1050_evttabhortur_verificar_views.verificar, 
        name='s1050_evttabhortur_verificar'),
        
url(r'^s1050-evttabhortur/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1050_evttabhortur_verificar_views.recibo, 
        name='s1050_evttabhortur_recibo'),
        
        
url(r'^s1050-evttabhortur/duplicar/(?P<hash>.*)/$',
        s1050_evttabhortur_verificar_views.duplicar,
        name='s1050_evttabhortur_duplicar'),

url(r'^s1050-evttabhortur/criar-alteracao/(?P<hash>.*)/$',
        s1050_evttabhortur_verificar_views.criar_alteracao,
        name='s1050_evttabhortur_criar_alteracao'),

url(r'^s1050-evttabhortur/criar-exclusao/(?P<hash>.*)/$',
        s1050_evttabhortur_verificar_views.criar_exclusao,
        name='s1050_evttabhortur_criar_exclusao'),
        
url(r'^s1050-evttabhortur/xml/(?P<hash>.*)/$', 
        s1050_evttabhortur_verificar_views.gerar_xml, 
                name='s1050_evttabhortur_xml'),
                

url(r'^s1050-evttabhortur/alterar-identidade/(?P<hash>.*)/$',
        s1050_evttabhortur_verificar_views.alterar_identidade,
        name='s1050_evttabhortur_alterar_identidade'),

url(r'^s1050-evttabhortur/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1050_evttabhortur_verificar_views.abrir_evento_para_edicao,
        name='s1050_evttabhortur_abrir_evento_para_edicao'),

url(r'^s1050-evttabhortur/validar-evento/(?P<hash>.*)/$',
        s1050_evttabhortur_verificar_views.validar_evento,
        name='s1050_evttabhortur_validar_evento'),

url(r'^s1050-evttabhortur/salvar/(?P<hash>.*)/$', 
        s1050_evttabhortur_views.salvar, 
        name='s1050_evttabhortur_salvar'),
        

url(r'^scripts/gerar-identidade/s1050-evttabhortur/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1050_evttabhortur_views.gerar_identidade, 
        name='s1050_evttabhortur_gerar_identidade'),



url(r'^s1060-evttabambiente/apagar/(?P<hash>.*)/$', 
        s1060_evttabambiente_views.apagar, 
        name='s1060_evttabambiente_apagar'),

url(r'^s1060-evttabambiente/api/$',
            s1060_evttabambiente_views.s1060evtTabAmbienteList.as_view() ),

        url(r'^s1060-evttabambiente/api/(?P<pk>[0-9]+)/$',
            s1060_evttabambiente_views.s1060evtTabAmbienteDetail.as_view() ),

url(r'^s1060-evttabambiente/listar/(?P<hash>.*)/$', 
        s1060_evttabambiente_views.listar, 
        name='s1060_evttabambiente'),
        
url(r'^s1060-evttabambiente/verificar/(?P<hash>.*)/$', 
        s1060_evttabambiente_verificar_views.verificar, 
        name='s1060_evttabambiente_verificar'),
        
url(r'^s1060-evttabambiente/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1060_evttabambiente_verificar_views.recibo, 
        name='s1060_evttabambiente_recibo'),
        
        
url(r'^s1060-evttabambiente/duplicar/(?P<hash>.*)/$',
        s1060_evttabambiente_verificar_views.duplicar,
        name='s1060_evttabambiente_duplicar'),

url(r'^s1060-evttabambiente/criar-alteracao/(?P<hash>.*)/$',
        s1060_evttabambiente_verificar_views.criar_alteracao,
        name='s1060_evttabambiente_criar_alteracao'),

url(r'^s1060-evttabambiente/criar-exclusao/(?P<hash>.*)/$',
        s1060_evttabambiente_verificar_views.criar_exclusao,
        name='s1060_evttabambiente_criar_exclusao'),
        
url(r'^s1060-evttabambiente/xml/(?P<hash>.*)/$', 
        s1060_evttabambiente_verificar_views.gerar_xml, 
                name='s1060_evttabambiente_xml'),
                

url(r'^s1060-evttabambiente/alterar-identidade/(?P<hash>.*)/$',
        s1060_evttabambiente_verificar_views.alterar_identidade,
        name='s1060_evttabambiente_alterar_identidade'),

url(r'^s1060-evttabambiente/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1060_evttabambiente_verificar_views.abrir_evento_para_edicao,
        name='s1060_evttabambiente_abrir_evento_para_edicao'),

url(r'^s1060-evttabambiente/validar-evento/(?P<hash>.*)/$',
        s1060_evttabambiente_verificar_views.validar_evento,
        name='s1060_evttabambiente_validar_evento'),

url(r'^s1060-evttabambiente/salvar/(?P<hash>.*)/$', 
        s1060_evttabambiente_views.salvar, 
        name='s1060_evttabambiente_salvar'),
        

url(r'^scripts/gerar-identidade/s1060-evttabambiente/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1060_evttabambiente_views.gerar_identidade, 
        name='s1060_evttabambiente_gerar_identidade'),



url(r'^s1070-evttabprocesso/apagar/(?P<hash>.*)/$', 
        s1070_evttabprocesso_views.apagar, 
        name='s1070_evttabprocesso_apagar'),

url(r'^s1070-evttabprocesso/api/$',
            s1070_evttabprocesso_views.s1070evtTabProcessoList.as_view() ),

        url(r'^s1070-evttabprocesso/api/(?P<pk>[0-9]+)/$',
            s1070_evttabprocesso_views.s1070evtTabProcessoDetail.as_view() ),

url(r'^s1070-evttabprocesso/listar/(?P<hash>.*)/$', 
        s1070_evttabprocesso_views.listar, 
        name='s1070_evttabprocesso'),
        
url(r'^s1070-evttabprocesso/verificar/(?P<hash>.*)/$', 
        s1070_evttabprocesso_verificar_views.verificar, 
        name='s1070_evttabprocesso_verificar'),
        
url(r'^s1070-evttabprocesso/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1070_evttabprocesso_verificar_views.recibo, 
        name='s1070_evttabprocesso_recibo'),
        
        
url(r'^s1070-evttabprocesso/duplicar/(?P<hash>.*)/$',
        s1070_evttabprocesso_verificar_views.duplicar,
        name='s1070_evttabprocesso_duplicar'),

url(r'^s1070-evttabprocesso/criar-alteracao/(?P<hash>.*)/$',
        s1070_evttabprocesso_verificar_views.criar_alteracao,
        name='s1070_evttabprocesso_criar_alteracao'),

url(r'^s1070-evttabprocesso/criar-exclusao/(?P<hash>.*)/$',
        s1070_evttabprocesso_verificar_views.criar_exclusao,
        name='s1070_evttabprocesso_criar_exclusao'),
        
url(r'^s1070-evttabprocesso/xml/(?P<hash>.*)/$', 
        s1070_evttabprocesso_verificar_views.gerar_xml, 
                name='s1070_evttabprocesso_xml'),
                

url(r'^s1070-evttabprocesso/alterar-identidade/(?P<hash>.*)/$',
        s1070_evttabprocesso_verificar_views.alterar_identidade,
        name='s1070_evttabprocesso_alterar_identidade'),

url(r'^s1070-evttabprocesso/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1070_evttabprocesso_verificar_views.abrir_evento_para_edicao,
        name='s1070_evttabprocesso_abrir_evento_para_edicao'),

url(r'^s1070-evttabprocesso/validar-evento/(?P<hash>.*)/$',
        s1070_evttabprocesso_verificar_views.validar_evento,
        name='s1070_evttabprocesso_validar_evento'),

url(r'^s1070-evttabprocesso/salvar/(?P<hash>.*)/$', 
        s1070_evttabprocesso_views.salvar, 
        name='s1070_evttabprocesso_salvar'),
        

url(r'^scripts/gerar-identidade/s1070-evttabprocesso/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1070_evttabprocesso_views.gerar_identidade, 
        name='s1070_evttabprocesso_gerar_identidade'),



url(r'^s1080-evttaboperport/apagar/(?P<hash>.*)/$', 
        s1080_evttaboperport_views.apagar, 
        name='s1080_evttaboperport_apagar'),

url(r'^s1080-evttaboperport/api/$',
            s1080_evttaboperport_views.s1080evtTabOperPortList.as_view() ),

        url(r'^s1080-evttaboperport/api/(?P<pk>[0-9]+)/$',
            s1080_evttaboperport_views.s1080evtTabOperPortDetail.as_view() ),

url(r'^s1080-evttaboperport/listar/(?P<hash>.*)/$', 
        s1080_evttaboperport_views.listar, 
        name='s1080_evttaboperport'),
        
url(r'^s1080-evttaboperport/verificar/(?P<hash>.*)/$', 
        s1080_evttaboperport_verificar_views.verificar, 
        name='s1080_evttaboperport_verificar'),
        
url(r'^s1080-evttaboperport/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1080_evttaboperport_verificar_views.recibo, 
        name='s1080_evttaboperport_recibo'),
        
        
url(r'^s1080-evttaboperport/duplicar/(?P<hash>.*)/$',
        s1080_evttaboperport_verificar_views.duplicar,
        name='s1080_evttaboperport_duplicar'),

url(r'^s1080-evttaboperport/criar-alteracao/(?P<hash>.*)/$',
        s1080_evttaboperport_verificar_views.criar_alteracao,
        name='s1080_evttaboperport_criar_alteracao'),

url(r'^s1080-evttaboperport/criar-exclusao/(?P<hash>.*)/$',
        s1080_evttaboperport_verificar_views.criar_exclusao,
        name='s1080_evttaboperport_criar_exclusao'),
        
url(r'^s1080-evttaboperport/xml/(?P<hash>.*)/$', 
        s1080_evttaboperport_verificar_views.gerar_xml, 
                name='s1080_evttaboperport_xml'),
                

url(r'^s1080-evttaboperport/alterar-identidade/(?P<hash>.*)/$',
        s1080_evttaboperport_verificar_views.alterar_identidade,
        name='s1080_evttaboperport_alterar_identidade'),

url(r'^s1080-evttaboperport/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1080_evttaboperport_verificar_views.abrir_evento_para_edicao,
        name='s1080_evttaboperport_abrir_evento_para_edicao'),

url(r'^s1080-evttaboperport/validar-evento/(?P<hash>.*)/$',
        s1080_evttaboperport_verificar_views.validar_evento,
        name='s1080_evttaboperport_validar_evento'),

url(r'^s1080-evttaboperport/salvar/(?P<hash>.*)/$', 
        s1080_evttaboperport_views.salvar, 
        name='s1080_evttaboperport_salvar'),
        

url(r'^scripts/gerar-identidade/s1080-evttaboperport/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1080_evttaboperport_views.gerar_identidade, 
        name='s1080_evttaboperport_gerar_identidade'),



url(r'^s1200-evtremun/apagar/(?P<hash>.*)/$', 
        s1200_evtremun_views.apagar, 
        name='s1200_evtremun_apagar'),

url(r'^s1200-evtremun/api/$',
            s1200_evtremun_views.s1200evtRemunList.as_view() ),

        url(r'^s1200-evtremun/api/(?P<pk>[0-9]+)/$',
            s1200_evtremun_views.s1200evtRemunDetail.as_view() ),

url(r'^s1200-evtremun/listar/(?P<hash>.*)/$', 
        s1200_evtremun_views.listar, 
        name='s1200_evtremun'),
        
url(r'^s1200-evtremun/verificar/(?P<hash>.*)/$', 
        s1200_evtremun_verificar_views.verificar, 
        name='s1200_evtremun_verificar'),
        
url(r'^s1200-evtremun/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1200_evtremun_verificar_views.recibo, 
        name='s1200_evtremun_recibo'),
        
        
url(r'^s1200-evtremun/duplicar/(?P<hash>.*)/$',
        s1200_evtremun_verificar_views.duplicar,
        name='s1200_evtremun_duplicar'),

url(r'^s1200-evtremun/criar-alteracao/(?P<hash>.*)/$',
        s1200_evtremun_verificar_views.criar_alteracao,
        name='s1200_evtremun_criar_alteracao'),

url(r'^s1200-evtremun/criar-exclusao/(?P<hash>.*)/$',
        s1200_evtremun_verificar_views.criar_exclusao,
        name='s1200_evtremun_criar_exclusao'),
        
url(r'^s1200-evtremun/xml/(?P<hash>.*)/$', 
        s1200_evtremun_verificar_views.gerar_xml, 
                name='s1200_evtremun_xml'),
                

url(r'^s1200-evtremun/alterar-identidade/(?P<hash>.*)/$',
        s1200_evtremun_verificar_views.alterar_identidade,
        name='s1200_evtremun_alterar_identidade'),

url(r'^s1200-evtremun/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1200_evtremun_verificar_views.abrir_evento_para_edicao,
        name='s1200_evtremun_abrir_evento_para_edicao'),

url(r'^s1200-evtremun/validar-evento/(?P<hash>.*)/$',
        s1200_evtremun_verificar_views.validar_evento,
        name='s1200_evtremun_validar_evento'),

url(r'^s1200-evtremun/salvar/(?P<hash>.*)/$', 
        s1200_evtremun_views.salvar, 
        name='s1200_evtremun_salvar'),
        

url(r'^scripts/gerar-identidade/s1200-evtremun/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1200_evtremun_views.gerar_identidade, 
        name='s1200_evtremun_gerar_identidade'),



url(r'^s1202-evtrmnrpps/apagar/(?P<hash>.*)/$', 
        s1202_evtrmnrpps_views.apagar, 
        name='s1202_evtrmnrpps_apagar'),

url(r'^s1202-evtrmnrpps/api/$',
            s1202_evtrmnrpps_views.s1202evtRmnRPPSList.as_view() ),

        url(r'^s1202-evtrmnrpps/api/(?P<pk>[0-9]+)/$',
            s1202_evtrmnrpps_views.s1202evtRmnRPPSDetail.as_view() ),

url(r'^s1202-evtrmnrpps/listar/(?P<hash>.*)/$', 
        s1202_evtrmnrpps_views.listar, 
        name='s1202_evtrmnrpps'),
        
url(r'^s1202-evtrmnrpps/verificar/(?P<hash>.*)/$', 
        s1202_evtrmnrpps_verificar_views.verificar, 
        name='s1202_evtrmnrpps_verificar'),
        
url(r'^s1202-evtrmnrpps/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1202_evtrmnrpps_verificar_views.recibo, 
        name='s1202_evtrmnrpps_recibo'),
        
        
url(r'^s1202-evtrmnrpps/duplicar/(?P<hash>.*)/$',
        s1202_evtrmnrpps_verificar_views.duplicar,
        name='s1202_evtrmnrpps_duplicar'),

url(r'^s1202-evtrmnrpps/criar-alteracao/(?P<hash>.*)/$',
        s1202_evtrmnrpps_verificar_views.criar_alteracao,
        name='s1202_evtrmnrpps_criar_alteracao'),

url(r'^s1202-evtrmnrpps/criar-exclusao/(?P<hash>.*)/$',
        s1202_evtrmnrpps_verificar_views.criar_exclusao,
        name='s1202_evtrmnrpps_criar_exclusao'),
        
url(r'^s1202-evtrmnrpps/xml/(?P<hash>.*)/$', 
        s1202_evtrmnrpps_verificar_views.gerar_xml, 
                name='s1202_evtrmnrpps_xml'),
                

url(r'^s1202-evtrmnrpps/alterar-identidade/(?P<hash>.*)/$',
        s1202_evtrmnrpps_verificar_views.alterar_identidade,
        name='s1202_evtrmnrpps_alterar_identidade'),

url(r'^s1202-evtrmnrpps/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1202_evtrmnrpps_verificar_views.abrir_evento_para_edicao,
        name='s1202_evtrmnrpps_abrir_evento_para_edicao'),

url(r'^s1202-evtrmnrpps/validar-evento/(?P<hash>.*)/$',
        s1202_evtrmnrpps_verificar_views.validar_evento,
        name='s1202_evtrmnrpps_validar_evento'),

url(r'^s1202-evtrmnrpps/salvar/(?P<hash>.*)/$', 
        s1202_evtrmnrpps_views.salvar, 
        name='s1202_evtrmnrpps_salvar'),
        

url(r'^scripts/gerar-identidade/s1202-evtrmnrpps/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1202_evtrmnrpps_views.gerar_identidade, 
        name='s1202_evtrmnrpps_gerar_identidade'),



url(r'^s1207-evtbenprrp/apagar/(?P<hash>.*)/$', 
        s1207_evtbenprrp_views.apagar, 
        name='s1207_evtbenprrp_apagar'),

url(r'^s1207-evtbenprrp/api/$',
            s1207_evtbenprrp_views.s1207evtBenPrRPList.as_view() ),

        url(r'^s1207-evtbenprrp/api/(?P<pk>[0-9]+)/$',
            s1207_evtbenprrp_views.s1207evtBenPrRPDetail.as_view() ),

url(r'^s1207-evtbenprrp/listar/(?P<hash>.*)/$', 
        s1207_evtbenprrp_views.listar, 
        name='s1207_evtbenprrp'),
        
url(r'^s1207-evtbenprrp/verificar/(?P<hash>.*)/$', 
        s1207_evtbenprrp_verificar_views.verificar, 
        name='s1207_evtbenprrp_verificar'),
        
url(r'^s1207-evtbenprrp/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1207_evtbenprrp_verificar_views.recibo, 
        name='s1207_evtbenprrp_recibo'),
        
        
url(r'^s1207-evtbenprrp/duplicar/(?P<hash>.*)/$',
        s1207_evtbenprrp_verificar_views.duplicar,
        name='s1207_evtbenprrp_duplicar'),

url(r'^s1207-evtbenprrp/criar-alteracao/(?P<hash>.*)/$',
        s1207_evtbenprrp_verificar_views.criar_alteracao,
        name='s1207_evtbenprrp_criar_alteracao'),

url(r'^s1207-evtbenprrp/criar-exclusao/(?P<hash>.*)/$',
        s1207_evtbenprrp_verificar_views.criar_exclusao,
        name='s1207_evtbenprrp_criar_exclusao'),
        
url(r'^s1207-evtbenprrp/xml/(?P<hash>.*)/$', 
        s1207_evtbenprrp_verificar_views.gerar_xml, 
                name='s1207_evtbenprrp_xml'),
                

url(r'^s1207-evtbenprrp/alterar-identidade/(?P<hash>.*)/$',
        s1207_evtbenprrp_verificar_views.alterar_identidade,
        name='s1207_evtbenprrp_alterar_identidade'),

url(r'^s1207-evtbenprrp/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1207_evtbenprrp_verificar_views.abrir_evento_para_edicao,
        name='s1207_evtbenprrp_abrir_evento_para_edicao'),

url(r'^s1207-evtbenprrp/validar-evento/(?P<hash>.*)/$',
        s1207_evtbenprrp_verificar_views.validar_evento,
        name='s1207_evtbenprrp_validar_evento'),

url(r'^s1207-evtbenprrp/salvar/(?P<hash>.*)/$', 
        s1207_evtbenprrp_views.salvar, 
        name='s1207_evtbenprrp_salvar'),
        

url(r'^scripts/gerar-identidade/s1207-evtbenprrp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1207_evtbenprrp_views.gerar_identidade, 
        name='s1207_evtbenprrp_gerar_identidade'),



url(r'^s1210-evtpgtos/apagar/(?P<hash>.*)/$', 
        s1210_evtpgtos_views.apagar, 
        name='s1210_evtpgtos_apagar'),

url(r'^s1210-evtpgtos/api/$',
            s1210_evtpgtos_views.s1210evtPgtosList.as_view() ),

        url(r'^s1210-evtpgtos/api/(?P<pk>[0-9]+)/$',
            s1210_evtpgtos_views.s1210evtPgtosDetail.as_view() ),

url(r'^s1210-evtpgtos/listar/(?P<hash>.*)/$', 
        s1210_evtpgtos_views.listar, 
        name='s1210_evtpgtos'),
        
url(r'^s1210-evtpgtos/verificar/(?P<hash>.*)/$', 
        s1210_evtpgtos_verificar_views.verificar, 
        name='s1210_evtpgtos_verificar'),
        
url(r'^s1210-evtpgtos/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1210_evtpgtos_verificar_views.recibo, 
        name='s1210_evtpgtos_recibo'),
        
        
url(r'^s1210-evtpgtos/duplicar/(?P<hash>.*)/$',
        s1210_evtpgtos_verificar_views.duplicar,
        name='s1210_evtpgtos_duplicar'),

url(r'^s1210-evtpgtos/criar-alteracao/(?P<hash>.*)/$',
        s1210_evtpgtos_verificar_views.criar_alteracao,
        name='s1210_evtpgtos_criar_alteracao'),

url(r'^s1210-evtpgtos/criar-exclusao/(?P<hash>.*)/$',
        s1210_evtpgtos_verificar_views.criar_exclusao,
        name='s1210_evtpgtos_criar_exclusao'),
        
url(r'^s1210-evtpgtos/xml/(?P<hash>.*)/$', 
        s1210_evtpgtos_verificar_views.gerar_xml, 
                name='s1210_evtpgtos_xml'),
                

url(r'^s1210-evtpgtos/alterar-identidade/(?P<hash>.*)/$',
        s1210_evtpgtos_verificar_views.alterar_identidade,
        name='s1210_evtpgtos_alterar_identidade'),

url(r'^s1210-evtpgtos/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1210_evtpgtos_verificar_views.abrir_evento_para_edicao,
        name='s1210_evtpgtos_abrir_evento_para_edicao'),

url(r'^s1210-evtpgtos/validar-evento/(?P<hash>.*)/$',
        s1210_evtpgtos_verificar_views.validar_evento,
        name='s1210_evtpgtos_validar_evento'),

url(r'^s1210-evtpgtos/salvar/(?P<hash>.*)/$', 
        s1210_evtpgtos_views.salvar, 
        name='s1210_evtpgtos_salvar'),
        

url(r'^scripts/gerar-identidade/s1210-evtpgtos/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1210_evtpgtos_views.gerar_identidade, 
        name='s1210_evtpgtos_gerar_identidade'),



url(r'^s1250-evtaqprod/apagar/(?P<hash>.*)/$', 
        s1250_evtaqprod_views.apagar, 
        name='s1250_evtaqprod_apagar'),

url(r'^s1250-evtaqprod/api/$',
            s1250_evtaqprod_views.s1250evtAqProdList.as_view() ),

        url(r'^s1250-evtaqprod/api/(?P<pk>[0-9]+)/$',
            s1250_evtaqprod_views.s1250evtAqProdDetail.as_view() ),

url(r'^s1250-evtaqprod/listar/(?P<hash>.*)/$', 
        s1250_evtaqprod_views.listar, 
        name='s1250_evtaqprod'),
        
url(r'^s1250-evtaqprod/verificar/(?P<hash>.*)/$', 
        s1250_evtaqprod_verificar_views.verificar, 
        name='s1250_evtaqprod_verificar'),
        
url(r'^s1250-evtaqprod/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1250_evtaqprod_verificar_views.recibo, 
        name='s1250_evtaqprod_recibo'),
        
        
url(r'^s1250-evtaqprod/duplicar/(?P<hash>.*)/$',
        s1250_evtaqprod_verificar_views.duplicar,
        name='s1250_evtaqprod_duplicar'),

url(r'^s1250-evtaqprod/criar-alteracao/(?P<hash>.*)/$',
        s1250_evtaqprod_verificar_views.criar_alteracao,
        name='s1250_evtaqprod_criar_alteracao'),

url(r'^s1250-evtaqprod/criar-exclusao/(?P<hash>.*)/$',
        s1250_evtaqprod_verificar_views.criar_exclusao,
        name='s1250_evtaqprod_criar_exclusao'),
        
url(r'^s1250-evtaqprod/xml/(?P<hash>.*)/$', 
        s1250_evtaqprod_verificar_views.gerar_xml, 
                name='s1250_evtaqprod_xml'),
                

url(r'^s1250-evtaqprod/alterar-identidade/(?P<hash>.*)/$',
        s1250_evtaqprod_verificar_views.alterar_identidade,
        name='s1250_evtaqprod_alterar_identidade'),

url(r'^s1250-evtaqprod/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1250_evtaqprod_verificar_views.abrir_evento_para_edicao,
        name='s1250_evtaqprod_abrir_evento_para_edicao'),

url(r'^s1250-evtaqprod/validar-evento/(?P<hash>.*)/$',
        s1250_evtaqprod_verificar_views.validar_evento,
        name='s1250_evtaqprod_validar_evento'),

url(r'^s1250-evtaqprod/salvar/(?P<hash>.*)/$', 
        s1250_evtaqprod_views.salvar, 
        name='s1250_evtaqprod_salvar'),
        

url(r'^scripts/gerar-identidade/s1250-evtaqprod/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1250_evtaqprod_views.gerar_identidade, 
        name='s1250_evtaqprod_gerar_identidade'),



url(r'^s1260-evtcomprod/apagar/(?P<hash>.*)/$', 
        s1260_evtcomprod_views.apagar, 
        name='s1260_evtcomprod_apagar'),

url(r'^s1260-evtcomprod/api/$',
            s1260_evtcomprod_views.s1260evtComProdList.as_view() ),

        url(r'^s1260-evtcomprod/api/(?P<pk>[0-9]+)/$',
            s1260_evtcomprod_views.s1260evtComProdDetail.as_view() ),

url(r'^s1260-evtcomprod/listar/(?P<hash>.*)/$', 
        s1260_evtcomprod_views.listar, 
        name='s1260_evtcomprod'),
        
url(r'^s1260-evtcomprod/verificar/(?P<hash>.*)/$', 
        s1260_evtcomprod_verificar_views.verificar, 
        name='s1260_evtcomprod_verificar'),
        
url(r'^s1260-evtcomprod/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1260_evtcomprod_verificar_views.recibo, 
        name='s1260_evtcomprod_recibo'),
        
        
url(r'^s1260-evtcomprod/duplicar/(?P<hash>.*)/$',
        s1260_evtcomprod_verificar_views.duplicar,
        name='s1260_evtcomprod_duplicar'),

url(r'^s1260-evtcomprod/criar-alteracao/(?P<hash>.*)/$',
        s1260_evtcomprod_verificar_views.criar_alteracao,
        name='s1260_evtcomprod_criar_alteracao'),

url(r'^s1260-evtcomprod/criar-exclusao/(?P<hash>.*)/$',
        s1260_evtcomprod_verificar_views.criar_exclusao,
        name='s1260_evtcomprod_criar_exclusao'),
        
url(r'^s1260-evtcomprod/xml/(?P<hash>.*)/$', 
        s1260_evtcomprod_verificar_views.gerar_xml, 
                name='s1260_evtcomprod_xml'),
                

url(r'^s1260-evtcomprod/alterar-identidade/(?P<hash>.*)/$',
        s1260_evtcomprod_verificar_views.alterar_identidade,
        name='s1260_evtcomprod_alterar_identidade'),

url(r'^s1260-evtcomprod/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1260_evtcomprod_verificar_views.abrir_evento_para_edicao,
        name='s1260_evtcomprod_abrir_evento_para_edicao'),

url(r'^s1260-evtcomprod/validar-evento/(?P<hash>.*)/$',
        s1260_evtcomprod_verificar_views.validar_evento,
        name='s1260_evtcomprod_validar_evento'),

url(r'^s1260-evtcomprod/salvar/(?P<hash>.*)/$', 
        s1260_evtcomprod_views.salvar, 
        name='s1260_evtcomprod_salvar'),
        

url(r'^scripts/gerar-identidade/s1260-evtcomprod/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1260_evtcomprod_views.gerar_identidade, 
        name='s1260_evtcomprod_gerar_identidade'),



url(r'^s1270-evtcontratavnp/apagar/(?P<hash>.*)/$', 
        s1270_evtcontratavnp_views.apagar, 
        name='s1270_evtcontratavnp_apagar'),

url(r'^s1270-evtcontratavnp/api/$',
            s1270_evtcontratavnp_views.s1270evtContratAvNPList.as_view() ),

        url(r'^s1270-evtcontratavnp/api/(?P<pk>[0-9]+)/$',
            s1270_evtcontratavnp_views.s1270evtContratAvNPDetail.as_view() ),

url(r'^s1270-evtcontratavnp/listar/(?P<hash>.*)/$', 
        s1270_evtcontratavnp_views.listar, 
        name='s1270_evtcontratavnp'),
        
url(r'^s1270-evtcontratavnp/verificar/(?P<hash>.*)/$', 
        s1270_evtcontratavnp_verificar_views.verificar, 
        name='s1270_evtcontratavnp_verificar'),
        
url(r'^s1270-evtcontratavnp/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1270_evtcontratavnp_verificar_views.recibo, 
        name='s1270_evtcontratavnp_recibo'),
        
        
url(r'^s1270-evtcontratavnp/duplicar/(?P<hash>.*)/$',
        s1270_evtcontratavnp_verificar_views.duplicar,
        name='s1270_evtcontratavnp_duplicar'),

url(r'^s1270-evtcontratavnp/criar-alteracao/(?P<hash>.*)/$',
        s1270_evtcontratavnp_verificar_views.criar_alteracao,
        name='s1270_evtcontratavnp_criar_alteracao'),

url(r'^s1270-evtcontratavnp/criar-exclusao/(?P<hash>.*)/$',
        s1270_evtcontratavnp_verificar_views.criar_exclusao,
        name='s1270_evtcontratavnp_criar_exclusao'),
        
url(r'^s1270-evtcontratavnp/xml/(?P<hash>.*)/$', 
        s1270_evtcontratavnp_verificar_views.gerar_xml, 
                name='s1270_evtcontratavnp_xml'),
                

url(r'^s1270-evtcontratavnp/alterar-identidade/(?P<hash>.*)/$',
        s1270_evtcontratavnp_verificar_views.alterar_identidade,
        name='s1270_evtcontratavnp_alterar_identidade'),

url(r'^s1270-evtcontratavnp/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1270_evtcontratavnp_verificar_views.abrir_evento_para_edicao,
        name='s1270_evtcontratavnp_abrir_evento_para_edicao'),

url(r'^s1270-evtcontratavnp/validar-evento/(?P<hash>.*)/$',
        s1270_evtcontratavnp_verificar_views.validar_evento,
        name='s1270_evtcontratavnp_validar_evento'),

url(r'^s1270-evtcontratavnp/salvar/(?P<hash>.*)/$', 
        s1270_evtcontratavnp_views.salvar, 
        name='s1270_evtcontratavnp_salvar'),
        

url(r'^scripts/gerar-identidade/s1270-evtcontratavnp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1270_evtcontratavnp_views.gerar_identidade, 
        name='s1270_evtcontratavnp_gerar_identidade'),



url(r'^s1280-evtinfocomplper/apagar/(?P<hash>.*)/$', 
        s1280_evtinfocomplper_views.apagar, 
        name='s1280_evtinfocomplper_apagar'),

url(r'^s1280-evtinfocomplper/api/$',
            s1280_evtinfocomplper_views.s1280evtInfoComplPerList.as_view() ),

        url(r'^s1280-evtinfocomplper/api/(?P<pk>[0-9]+)/$',
            s1280_evtinfocomplper_views.s1280evtInfoComplPerDetail.as_view() ),

url(r'^s1280-evtinfocomplper/listar/(?P<hash>.*)/$', 
        s1280_evtinfocomplper_views.listar, 
        name='s1280_evtinfocomplper'),
        
url(r'^s1280-evtinfocomplper/verificar/(?P<hash>.*)/$', 
        s1280_evtinfocomplper_verificar_views.verificar, 
        name='s1280_evtinfocomplper_verificar'),
        
url(r'^s1280-evtinfocomplper/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1280_evtinfocomplper_verificar_views.recibo, 
        name='s1280_evtinfocomplper_recibo'),
        
        
url(r'^s1280-evtinfocomplper/duplicar/(?P<hash>.*)/$',
        s1280_evtinfocomplper_verificar_views.duplicar,
        name='s1280_evtinfocomplper_duplicar'),

url(r'^s1280-evtinfocomplper/criar-alteracao/(?P<hash>.*)/$',
        s1280_evtinfocomplper_verificar_views.criar_alteracao,
        name='s1280_evtinfocomplper_criar_alteracao'),

url(r'^s1280-evtinfocomplper/criar-exclusao/(?P<hash>.*)/$',
        s1280_evtinfocomplper_verificar_views.criar_exclusao,
        name='s1280_evtinfocomplper_criar_exclusao'),
        
url(r'^s1280-evtinfocomplper/xml/(?P<hash>.*)/$', 
        s1280_evtinfocomplper_verificar_views.gerar_xml, 
                name='s1280_evtinfocomplper_xml'),
                

url(r'^s1280-evtinfocomplper/alterar-identidade/(?P<hash>.*)/$',
        s1280_evtinfocomplper_verificar_views.alterar_identidade,
        name='s1280_evtinfocomplper_alterar_identidade'),

url(r'^s1280-evtinfocomplper/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1280_evtinfocomplper_verificar_views.abrir_evento_para_edicao,
        name='s1280_evtinfocomplper_abrir_evento_para_edicao'),

url(r'^s1280-evtinfocomplper/validar-evento/(?P<hash>.*)/$',
        s1280_evtinfocomplper_verificar_views.validar_evento,
        name='s1280_evtinfocomplper_validar_evento'),

url(r'^s1280-evtinfocomplper/salvar/(?P<hash>.*)/$', 
        s1280_evtinfocomplper_views.salvar, 
        name='s1280_evtinfocomplper_salvar'),
        

url(r'^scripts/gerar-identidade/s1280-evtinfocomplper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1280_evtinfocomplper_views.gerar_identidade, 
        name='s1280_evtinfocomplper_gerar_identidade'),



url(r'^s1295-evttotconting/apagar/(?P<hash>.*)/$', 
        s1295_evttotconting_views.apagar, 
        name='s1295_evttotconting_apagar'),

url(r'^s1295-evttotconting/api/$',
            s1295_evttotconting_views.s1295evtTotContingList.as_view() ),

        url(r'^s1295-evttotconting/api/(?P<pk>[0-9]+)/$',
            s1295_evttotconting_views.s1295evtTotContingDetail.as_view() ),

url(r'^s1295-evttotconting/listar/(?P<hash>.*)/$', 
        s1295_evttotconting_views.listar, 
        name='s1295_evttotconting'),
        
url(r'^s1295-evttotconting/verificar/(?P<hash>.*)/$', 
        s1295_evttotconting_verificar_views.verificar, 
        name='s1295_evttotconting_verificar'),
        
url(r'^s1295-evttotconting/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1295_evttotconting_verificar_views.recibo, 
        name='s1295_evttotconting_recibo'),
        
        
url(r'^s1295-evttotconting/duplicar/(?P<hash>.*)/$',
        s1295_evttotconting_verificar_views.duplicar,
        name='s1295_evttotconting_duplicar'),

url(r'^s1295-evttotconting/criar-alteracao/(?P<hash>.*)/$',
        s1295_evttotconting_verificar_views.criar_alteracao,
        name='s1295_evttotconting_criar_alteracao'),

url(r'^s1295-evttotconting/criar-exclusao/(?P<hash>.*)/$',
        s1295_evttotconting_verificar_views.criar_exclusao,
        name='s1295_evttotconting_criar_exclusao'),
        
url(r'^s1295-evttotconting/xml/(?P<hash>.*)/$', 
        s1295_evttotconting_verificar_views.gerar_xml, 
                name='s1295_evttotconting_xml'),
                

url(r'^s1295-evttotconting/alterar-identidade/(?P<hash>.*)/$',
        s1295_evttotconting_verificar_views.alterar_identidade,
        name='s1295_evttotconting_alterar_identidade'),

url(r'^s1295-evttotconting/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1295_evttotconting_verificar_views.abrir_evento_para_edicao,
        name='s1295_evttotconting_abrir_evento_para_edicao'),

url(r'^s1295-evttotconting/validar-evento/(?P<hash>.*)/$',
        s1295_evttotconting_verificar_views.validar_evento,
        name='s1295_evttotconting_validar_evento'),

url(r'^s1295-evttotconting/salvar/(?P<hash>.*)/$', 
        s1295_evttotconting_views.salvar, 
        name='s1295_evttotconting_salvar'),
        

url(r'^scripts/gerar-identidade/s1295-evttotconting/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1295_evttotconting_views.gerar_identidade, 
        name='s1295_evttotconting_gerar_identidade'),



url(r'^s1298-evtreabreevper/apagar/(?P<hash>.*)/$', 
        s1298_evtreabreevper_views.apagar, 
        name='s1298_evtreabreevper_apagar'),

url(r'^s1298-evtreabreevper/api/$',
            s1298_evtreabreevper_views.s1298evtReabreEvPerList.as_view() ),

        url(r'^s1298-evtreabreevper/api/(?P<pk>[0-9]+)/$',
            s1298_evtreabreevper_views.s1298evtReabreEvPerDetail.as_view() ),

url(r'^s1298-evtreabreevper/listar/(?P<hash>.*)/$', 
        s1298_evtreabreevper_views.listar, 
        name='s1298_evtreabreevper'),
        
url(r'^s1298-evtreabreevper/verificar/(?P<hash>.*)/$', 
        s1298_evtreabreevper_verificar_views.verificar, 
        name='s1298_evtreabreevper_verificar'),
        
url(r'^s1298-evtreabreevper/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1298_evtreabreevper_verificar_views.recibo, 
        name='s1298_evtreabreevper_recibo'),
        
        
url(r'^s1298-evtreabreevper/duplicar/(?P<hash>.*)/$',
        s1298_evtreabreevper_verificar_views.duplicar,
        name='s1298_evtreabreevper_duplicar'),

url(r'^s1298-evtreabreevper/criar-alteracao/(?P<hash>.*)/$',
        s1298_evtreabreevper_verificar_views.criar_alteracao,
        name='s1298_evtreabreevper_criar_alteracao'),

url(r'^s1298-evtreabreevper/criar-exclusao/(?P<hash>.*)/$',
        s1298_evtreabreevper_verificar_views.criar_exclusao,
        name='s1298_evtreabreevper_criar_exclusao'),
        
url(r'^s1298-evtreabreevper/xml/(?P<hash>.*)/$', 
        s1298_evtreabreevper_verificar_views.gerar_xml, 
                name='s1298_evtreabreevper_xml'),
                

url(r'^s1298-evtreabreevper/alterar-identidade/(?P<hash>.*)/$',
        s1298_evtreabreevper_verificar_views.alterar_identidade,
        name='s1298_evtreabreevper_alterar_identidade'),

url(r'^s1298-evtreabreevper/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1298_evtreabreevper_verificar_views.abrir_evento_para_edicao,
        name='s1298_evtreabreevper_abrir_evento_para_edicao'),

url(r'^s1298-evtreabreevper/validar-evento/(?P<hash>.*)/$',
        s1298_evtreabreevper_verificar_views.validar_evento,
        name='s1298_evtreabreevper_validar_evento'),

url(r'^s1298-evtreabreevper/salvar/(?P<hash>.*)/$', 
        s1298_evtreabreevper_views.salvar, 
        name='s1298_evtreabreevper_salvar'),
        

url(r'^scripts/gerar-identidade/s1298-evtreabreevper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1298_evtreabreevper_views.gerar_identidade, 
        name='s1298_evtreabreevper_gerar_identidade'),



url(r'^s1299-evtfechaevper/apagar/(?P<hash>.*)/$', 
        s1299_evtfechaevper_views.apagar, 
        name='s1299_evtfechaevper_apagar'),

url(r'^s1299-evtfechaevper/api/$',
            s1299_evtfechaevper_views.s1299evtFechaEvPerList.as_view() ),

        url(r'^s1299-evtfechaevper/api/(?P<pk>[0-9]+)/$',
            s1299_evtfechaevper_views.s1299evtFechaEvPerDetail.as_view() ),

url(r'^s1299-evtfechaevper/listar/(?P<hash>.*)/$', 
        s1299_evtfechaevper_views.listar, 
        name='s1299_evtfechaevper'),
        
url(r'^s1299-evtfechaevper/verificar/(?P<hash>.*)/$', 
        s1299_evtfechaevper_verificar_views.verificar, 
        name='s1299_evtfechaevper_verificar'),
        
url(r'^s1299-evtfechaevper/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1299_evtfechaevper_verificar_views.recibo, 
        name='s1299_evtfechaevper_recibo'),
        
        
url(r'^s1299-evtfechaevper/duplicar/(?P<hash>.*)/$',
        s1299_evtfechaevper_verificar_views.duplicar,
        name='s1299_evtfechaevper_duplicar'),

url(r'^s1299-evtfechaevper/criar-alteracao/(?P<hash>.*)/$',
        s1299_evtfechaevper_verificar_views.criar_alteracao,
        name='s1299_evtfechaevper_criar_alteracao'),

url(r'^s1299-evtfechaevper/criar-exclusao/(?P<hash>.*)/$',
        s1299_evtfechaevper_verificar_views.criar_exclusao,
        name='s1299_evtfechaevper_criar_exclusao'),
        
url(r'^s1299-evtfechaevper/xml/(?P<hash>.*)/$', 
        s1299_evtfechaevper_verificar_views.gerar_xml, 
                name='s1299_evtfechaevper_xml'),
                

url(r'^s1299-evtfechaevper/alterar-identidade/(?P<hash>.*)/$',
        s1299_evtfechaevper_verificar_views.alterar_identidade,
        name='s1299_evtfechaevper_alterar_identidade'),

url(r'^s1299-evtfechaevper/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1299_evtfechaevper_verificar_views.abrir_evento_para_edicao,
        name='s1299_evtfechaevper_abrir_evento_para_edicao'),

url(r'^s1299-evtfechaevper/validar-evento/(?P<hash>.*)/$',
        s1299_evtfechaevper_verificar_views.validar_evento,
        name='s1299_evtfechaevper_validar_evento'),

url(r'^s1299-evtfechaevper/salvar/(?P<hash>.*)/$', 
        s1299_evtfechaevper_views.salvar, 
        name='s1299_evtfechaevper_salvar'),
        

url(r'^scripts/gerar-identidade/s1299-evtfechaevper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1299_evtfechaevper_views.gerar_identidade, 
        name='s1299_evtfechaevper_gerar_identidade'),



url(r'^s1300-evtcontrsindpatr/apagar/(?P<hash>.*)/$', 
        s1300_evtcontrsindpatr_views.apagar, 
        name='s1300_evtcontrsindpatr_apagar'),

url(r'^s1300-evtcontrsindpatr/api/$',
            s1300_evtcontrsindpatr_views.s1300evtContrSindPatrList.as_view() ),

        url(r'^s1300-evtcontrsindpatr/api/(?P<pk>[0-9]+)/$',
            s1300_evtcontrsindpatr_views.s1300evtContrSindPatrDetail.as_view() ),

url(r'^s1300-evtcontrsindpatr/listar/(?P<hash>.*)/$', 
        s1300_evtcontrsindpatr_views.listar, 
        name='s1300_evtcontrsindpatr'),
        
url(r'^s1300-evtcontrsindpatr/verificar/(?P<hash>.*)/$', 
        s1300_evtcontrsindpatr_verificar_views.verificar, 
        name='s1300_evtcontrsindpatr_verificar'),
        
url(r'^s1300-evtcontrsindpatr/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s1300_evtcontrsindpatr_verificar_views.recibo, 
        name='s1300_evtcontrsindpatr_recibo'),
        
        
url(r'^s1300-evtcontrsindpatr/duplicar/(?P<hash>.*)/$',
        s1300_evtcontrsindpatr_verificar_views.duplicar,
        name='s1300_evtcontrsindpatr_duplicar'),

url(r'^s1300-evtcontrsindpatr/criar-alteracao/(?P<hash>.*)/$',
        s1300_evtcontrsindpatr_verificar_views.criar_alteracao,
        name='s1300_evtcontrsindpatr_criar_alteracao'),

url(r'^s1300-evtcontrsindpatr/criar-exclusao/(?P<hash>.*)/$',
        s1300_evtcontrsindpatr_verificar_views.criar_exclusao,
        name='s1300_evtcontrsindpatr_criar_exclusao'),
        
url(r'^s1300-evtcontrsindpatr/xml/(?P<hash>.*)/$', 
        s1300_evtcontrsindpatr_verificar_views.gerar_xml, 
                name='s1300_evtcontrsindpatr_xml'),
                

url(r'^s1300-evtcontrsindpatr/alterar-identidade/(?P<hash>.*)/$',
        s1300_evtcontrsindpatr_verificar_views.alterar_identidade,
        name='s1300_evtcontrsindpatr_alterar_identidade'),

url(r'^s1300-evtcontrsindpatr/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s1300_evtcontrsindpatr_verificar_views.abrir_evento_para_edicao,
        name='s1300_evtcontrsindpatr_abrir_evento_para_edicao'),

url(r'^s1300-evtcontrsindpatr/validar-evento/(?P<hash>.*)/$',
        s1300_evtcontrsindpatr_verificar_views.validar_evento,
        name='s1300_evtcontrsindpatr_validar_evento'),

url(r'^s1300-evtcontrsindpatr/salvar/(?P<hash>.*)/$', 
        s1300_evtcontrsindpatr_views.salvar, 
        name='s1300_evtcontrsindpatr_salvar'),
        

url(r'^scripts/gerar-identidade/s1300-evtcontrsindpatr/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s1300_evtcontrsindpatr_views.gerar_identidade, 
        name='s1300_evtcontrsindpatr_gerar_identidade'),



url(r'^s2190-evtadmprelim/apagar/(?P<hash>.*)/$', 
        s2190_evtadmprelim_views.apagar, 
        name='s2190_evtadmprelim_apagar'),

url(r'^s2190-evtadmprelim/api/$',
            s2190_evtadmprelim_views.s2190evtAdmPrelimList.as_view() ),

        url(r'^s2190-evtadmprelim/api/(?P<pk>[0-9]+)/$',
            s2190_evtadmprelim_views.s2190evtAdmPrelimDetail.as_view() ),

url(r'^s2190-evtadmprelim/listar/(?P<hash>.*)/$', 
        s2190_evtadmprelim_views.listar, 
        name='s2190_evtadmprelim'),
        
url(r'^s2190-evtadmprelim/verificar/(?P<hash>.*)/$', 
        s2190_evtadmprelim_verificar_views.verificar, 
        name='s2190_evtadmprelim_verificar'),
        
url(r'^s2190-evtadmprelim/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2190_evtadmprelim_verificar_views.recibo, 
        name='s2190_evtadmprelim_recibo'),
        
        
url(r'^s2190-evtadmprelim/duplicar/(?P<hash>.*)/$',
        s2190_evtadmprelim_verificar_views.duplicar,
        name='s2190_evtadmprelim_duplicar'),

url(r'^s2190-evtadmprelim/criar-alteracao/(?P<hash>.*)/$',
        s2190_evtadmprelim_verificar_views.criar_alteracao,
        name='s2190_evtadmprelim_criar_alteracao'),

url(r'^s2190-evtadmprelim/criar-exclusao/(?P<hash>.*)/$',
        s2190_evtadmprelim_verificar_views.criar_exclusao,
        name='s2190_evtadmprelim_criar_exclusao'),
        
url(r'^s2190-evtadmprelim/xml/(?P<hash>.*)/$', 
        s2190_evtadmprelim_verificar_views.gerar_xml, 
                name='s2190_evtadmprelim_xml'),
                

url(r'^s2190-evtadmprelim/alterar-identidade/(?P<hash>.*)/$',
        s2190_evtadmprelim_verificar_views.alterar_identidade,
        name='s2190_evtadmprelim_alterar_identidade'),

url(r'^s2190-evtadmprelim/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2190_evtadmprelim_verificar_views.abrir_evento_para_edicao,
        name='s2190_evtadmprelim_abrir_evento_para_edicao'),

url(r'^s2190-evtadmprelim/validar-evento/(?P<hash>.*)/$',
        s2190_evtadmprelim_verificar_views.validar_evento,
        name='s2190_evtadmprelim_validar_evento'),

url(r'^s2190-evtadmprelim/salvar/(?P<hash>.*)/$', 
        s2190_evtadmprelim_views.salvar, 
        name='s2190_evtadmprelim_salvar'),
        

url(r'^scripts/gerar-identidade/s2190-evtadmprelim/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2190_evtadmprelim_views.gerar_identidade, 
        name='s2190_evtadmprelim_gerar_identidade'),



url(r'^s2200-evtadmissao/apagar/(?P<hash>.*)/$', 
        s2200_evtadmissao_views.apagar, 
        name='s2200_evtadmissao_apagar'),

url(r'^s2200-evtadmissao/api/$',
            s2200_evtadmissao_views.s2200evtAdmissaoList.as_view() ),

        url(r'^s2200-evtadmissao/api/(?P<pk>[0-9]+)/$',
            s2200_evtadmissao_views.s2200evtAdmissaoDetail.as_view() ),

url(r'^s2200-evtadmissao/listar/(?P<hash>.*)/$', 
        s2200_evtadmissao_views.listar, 
        name='s2200_evtadmissao'),
        
url(r'^s2200-evtadmissao/verificar/(?P<hash>.*)/$', 
        s2200_evtadmissao_verificar_views.verificar, 
        name='s2200_evtadmissao_verificar'),
        
url(r'^s2200-evtadmissao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2200_evtadmissao_verificar_views.recibo, 
        name='s2200_evtadmissao_recibo'),
        
        
url(r'^s2200-evtadmissao/duplicar/(?P<hash>.*)/$',
        s2200_evtadmissao_verificar_views.duplicar,
        name='s2200_evtadmissao_duplicar'),

url(r'^s2200-evtadmissao/criar-alteracao/(?P<hash>.*)/$',
        s2200_evtadmissao_verificar_views.criar_alteracao,
        name='s2200_evtadmissao_criar_alteracao'),

url(r'^s2200-evtadmissao/criar-exclusao/(?P<hash>.*)/$',
        s2200_evtadmissao_verificar_views.criar_exclusao,
        name='s2200_evtadmissao_criar_exclusao'),
        
url(r'^s2200-evtadmissao/xml/(?P<hash>.*)/$', 
        s2200_evtadmissao_verificar_views.gerar_xml, 
                name='s2200_evtadmissao_xml'),
                

url(r'^s2200-evtadmissao/alterar-identidade/(?P<hash>.*)/$',
        s2200_evtadmissao_verificar_views.alterar_identidade,
        name='s2200_evtadmissao_alterar_identidade'),

url(r'^s2200-evtadmissao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2200_evtadmissao_verificar_views.abrir_evento_para_edicao,
        name='s2200_evtadmissao_abrir_evento_para_edicao'),

url(r'^s2200-evtadmissao/validar-evento/(?P<hash>.*)/$',
        s2200_evtadmissao_verificar_views.validar_evento,
        name='s2200_evtadmissao_validar_evento'),

url(r'^s2200-evtadmissao/salvar/(?P<hash>.*)/$', 
        s2200_evtadmissao_views.salvar, 
        name='s2200_evtadmissao_salvar'),
        

url(r'^scripts/gerar-identidade/s2200-evtadmissao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2200_evtadmissao_views.gerar_identidade, 
        name='s2200_evtadmissao_gerar_identidade'),



url(r'^s2205-evtaltcadastral/apagar/(?P<hash>.*)/$', 
        s2205_evtaltcadastral_views.apagar, 
        name='s2205_evtaltcadastral_apagar'),

url(r'^s2205-evtaltcadastral/api/$',
            s2205_evtaltcadastral_views.s2205evtAltCadastralList.as_view() ),

        url(r'^s2205-evtaltcadastral/api/(?P<pk>[0-9]+)/$',
            s2205_evtaltcadastral_views.s2205evtAltCadastralDetail.as_view() ),

url(r'^s2205-evtaltcadastral/listar/(?P<hash>.*)/$', 
        s2205_evtaltcadastral_views.listar, 
        name='s2205_evtaltcadastral'),
        
url(r'^s2205-evtaltcadastral/verificar/(?P<hash>.*)/$', 
        s2205_evtaltcadastral_verificar_views.verificar, 
        name='s2205_evtaltcadastral_verificar'),
        
url(r'^s2205-evtaltcadastral/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2205_evtaltcadastral_verificar_views.recibo, 
        name='s2205_evtaltcadastral_recibo'),
        
        
url(r'^s2205-evtaltcadastral/duplicar/(?P<hash>.*)/$',
        s2205_evtaltcadastral_verificar_views.duplicar,
        name='s2205_evtaltcadastral_duplicar'),

url(r'^s2205-evtaltcadastral/criar-alteracao/(?P<hash>.*)/$',
        s2205_evtaltcadastral_verificar_views.criar_alteracao,
        name='s2205_evtaltcadastral_criar_alteracao'),

url(r'^s2205-evtaltcadastral/criar-exclusao/(?P<hash>.*)/$',
        s2205_evtaltcadastral_verificar_views.criar_exclusao,
        name='s2205_evtaltcadastral_criar_exclusao'),
        
url(r'^s2205-evtaltcadastral/xml/(?P<hash>.*)/$', 
        s2205_evtaltcadastral_verificar_views.gerar_xml, 
                name='s2205_evtaltcadastral_xml'),
                

url(r'^s2205-evtaltcadastral/alterar-identidade/(?P<hash>.*)/$',
        s2205_evtaltcadastral_verificar_views.alterar_identidade,
        name='s2205_evtaltcadastral_alterar_identidade'),

url(r'^s2205-evtaltcadastral/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2205_evtaltcadastral_verificar_views.abrir_evento_para_edicao,
        name='s2205_evtaltcadastral_abrir_evento_para_edicao'),

url(r'^s2205-evtaltcadastral/validar-evento/(?P<hash>.*)/$',
        s2205_evtaltcadastral_verificar_views.validar_evento,
        name='s2205_evtaltcadastral_validar_evento'),

url(r'^s2205-evtaltcadastral/salvar/(?P<hash>.*)/$', 
        s2205_evtaltcadastral_views.salvar, 
        name='s2205_evtaltcadastral_salvar'),
        

url(r'^scripts/gerar-identidade/s2205-evtaltcadastral/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2205_evtaltcadastral_views.gerar_identidade, 
        name='s2205_evtaltcadastral_gerar_identidade'),



url(r'^s2206-evtaltcontratual/apagar/(?P<hash>.*)/$', 
        s2206_evtaltcontratual_views.apagar, 
        name='s2206_evtaltcontratual_apagar'),

url(r'^s2206-evtaltcontratual/api/$',
            s2206_evtaltcontratual_views.s2206evtAltContratualList.as_view() ),

        url(r'^s2206-evtaltcontratual/api/(?P<pk>[0-9]+)/$',
            s2206_evtaltcontratual_views.s2206evtAltContratualDetail.as_view() ),

url(r'^s2206-evtaltcontratual/listar/(?P<hash>.*)/$', 
        s2206_evtaltcontratual_views.listar, 
        name='s2206_evtaltcontratual'),
        
url(r'^s2206-evtaltcontratual/verificar/(?P<hash>.*)/$', 
        s2206_evtaltcontratual_verificar_views.verificar, 
        name='s2206_evtaltcontratual_verificar'),
        
url(r'^s2206-evtaltcontratual/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2206_evtaltcontratual_verificar_views.recibo, 
        name='s2206_evtaltcontratual_recibo'),
        
        
url(r'^s2206-evtaltcontratual/duplicar/(?P<hash>.*)/$',
        s2206_evtaltcontratual_verificar_views.duplicar,
        name='s2206_evtaltcontratual_duplicar'),

url(r'^s2206-evtaltcontratual/criar-alteracao/(?P<hash>.*)/$',
        s2206_evtaltcontratual_verificar_views.criar_alteracao,
        name='s2206_evtaltcontratual_criar_alteracao'),

url(r'^s2206-evtaltcontratual/criar-exclusao/(?P<hash>.*)/$',
        s2206_evtaltcontratual_verificar_views.criar_exclusao,
        name='s2206_evtaltcontratual_criar_exclusao'),
        
url(r'^s2206-evtaltcontratual/xml/(?P<hash>.*)/$', 
        s2206_evtaltcontratual_verificar_views.gerar_xml, 
                name='s2206_evtaltcontratual_xml'),
                

url(r'^s2206-evtaltcontratual/alterar-identidade/(?P<hash>.*)/$',
        s2206_evtaltcontratual_verificar_views.alterar_identidade,
        name='s2206_evtaltcontratual_alterar_identidade'),

url(r'^s2206-evtaltcontratual/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2206_evtaltcontratual_verificar_views.abrir_evento_para_edicao,
        name='s2206_evtaltcontratual_abrir_evento_para_edicao'),

url(r'^s2206-evtaltcontratual/validar-evento/(?P<hash>.*)/$',
        s2206_evtaltcontratual_verificar_views.validar_evento,
        name='s2206_evtaltcontratual_validar_evento'),

url(r'^s2206-evtaltcontratual/salvar/(?P<hash>.*)/$', 
        s2206_evtaltcontratual_views.salvar, 
        name='s2206_evtaltcontratual_salvar'),
        

url(r'^scripts/gerar-identidade/s2206-evtaltcontratual/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2206_evtaltcontratual_views.gerar_identidade, 
        name='s2206_evtaltcontratual_gerar_identidade'),



url(r'^s2210-evtcat/apagar/(?P<hash>.*)/$', 
        s2210_evtcat_views.apagar, 
        name='s2210_evtcat_apagar'),

url(r'^s2210-evtcat/api/$',
            s2210_evtcat_views.s2210evtCATList.as_view() ),

        url(r'^s2210-evtcat/api/(?P<pk>[0-9]+)/$',
            s2210_evtcat_views.s2210evtCATDetail.as_view() ),

url(r'^s2210-evtcat/listar/(?P<hash>.*)/$', 
        s2210_evtcat_views.listar, 
        name='s2210_evtcat'),
        
url(r'^s2210-evtcat/verificar/(?P<hash>.*)/$', 
        s2210_evtcat_verificar_views.verificar, 
        name='s2210_evtcat_verificar'),
        
url(r'^s2210-evtcat/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2210_evtcat_verificar_views.recibo, 
        name='s2210_evtcat_recibo'),
        
        
url(r'^s2210-evtcat/duplicar/(?P<hash>.*)/$',
        s2210_evtcat_verificar_views.duplicar,
        name='s2210_evtcat_duplicar'),

url(r'^s2210-evtcat/criar-alteracao/(?P<hash>.*)/$',
        s2210_evtcat_verificar_views.criar_alteracao,
        name='s2210_evtcat_criar_alteracao'),

url(r'^s2210-evtcat/criar-exclusao/(?P<hash>.*)/$',
        s2210_evtcat_verificar_views.criar_exclusao,
        name='s2210_evtcat_criar_exclusao'),
        
url(r'^s2210-evtcat/xml/(?P<hash>.*)/$', 
        s2210_evtcat_verificar_views.gerar_xml, 
                name='s2210_evtcat_xml'),
                

url(r'^s2210-evtcat/alterar-identidade/(?P<hash>.*)/$',
        s2210_evtcat_verificar_views.alterar_identidade,
        name='s2210_evtcat_alterar_identidade'),

url(r'^s2210-evtcat/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2210_evtcat_verificar_views.abrir_evento_para_edicao,
        name='s2210_evtcat_abrir_evento_para_edicao'),

url(r'^s2210-evtcat/validar-evento/(?P<hash>.*)/$',
        s2210_evtcat_verificar_views.validar_evento,
        name='s2210_evtcat_validar_evento'),

url(r'^s2210-evtcat/salvar/(?P<hash>.*)/$', 
        s2210_evtcat_views.salvar, 
        name='s2210_evtcat_salvar'),
        

url(r'^scripts/gerar-identidade/s2210-evtcat/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2210_evtcat_views.gerar_identidade, 
        name='s2210_evtcat_gerar_identidade'),



url(r'^s2220-evtmonit/apagar/(?P<hash>.*)/$', 
        s2220_evtmonit_views.apagar, 
        name='s2220_evtmonit_apagar'),

url(r'^s2220-evtmonit/api/$',
            s2220_evtmonit_views.s2220evtMonitList.as_view() ),

        url(r'^s2220-evtmonit/api/(?P<pk>[0-9]+)/$',
            s2220_evtmonit_views.s2220evtMonitDetail.as_view() ),

url(r'^s2220-evtmonit/listar/(?P<hash>.*)/$', 
        s2220_evtmonit_views.listar, 
        name='s2220_evtmonit'),
        
url(r'^s2220-evtmonit/verificar/(?P<hash>.*)/$', 
        s2220_evtmonit_verificar_views.verificar, 
        name='s2220_evtmonit_verificar'),
        
url(r'^s2220-evtmonit/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2220_evtmonit_verificar_views.recibo, 
        name='s2220_evtmonit_recibo'),
        
        
url(r'^s2220-evtmonit/duplicar/(?P<hash>.*)/$',
        s2220_evtmonit_verificar_views.duplicar,
        name='s2220_evtmonit_duplicar'),

url(r'^s2220-evtmonit/criar-alteracao/(?P<hash>.*)/$',
        s2220_evtmonit_verificar_views.criar_alteracao,
        name='s2220_evtmonit_criar_alteracao'),

url(r'^s2220-evtmonit/criar-exclusao/(?P<hash>.*)/$',
        s2220_evtmonit_verificar_views.criar_exclusao,
        name='s2220_evtmonit_criar_exclusao'),
        
url(r'^s2220-evtmonit/xml/(?P<hash>.*)/$', 
        s2220_evtmonit_verificar_views.gerar_xml, 
                name='s2220_evtmonit_xml'),
                

url(r'^s2220-evtmonit/alterar-identidade/(?P<hash>.*)/$',
        s2220_evtmonit_verificar_views.alterar_identidade,
        name='s2220_evtmonit_alterar_identidade'),

url(r'^s2220-evtmonit/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2220_evtmonit_verificar_views.abrir_evento_para_edicao,
        name='s2220_evtmonit_abrir_evento_para_edicao'),

url(r'^s2220-evtmonit/validar-evento/(?P<hash>.*)/$',
        s2220_evtmonit_verificar_views.validar_evento,
        name='s2220_evtmonit_validar_evento'),

url(r'^s2220-evtmonit/salvar/(?P<hash>.*)/$', 
        s2220_evtmonit_views.salvar, 
        name='s2220_evtmonit_salvar'),
        

url(r'^scripts/gerar-identidade/s2220-evtmonit/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2220_evtmonit_views.gerar_identidade, 
        name='s2220_evtmonit_gerar_identidade'),



url(r'^s2221-evttoxic/apagar/(?P<hash>.*)/$', 
        s2221_evttoxic_views.apagar, 
        name='s2221_evttoxic_apagar'),

url(r'^s2221-evttoxic/api/$',
            s2221_evttoxic_views.s2221evtToxicList.as_view() ),

        url(r'^s2221-evttoxic/api/(?P<pk>[0-9]+)/$',
            s2221_evttoxic_views.s2221evtToxicDetail.as_view() ),

url(r'^s2221-evttoxic/listar/(?P<hash>.*)/$', 
        s2221_evttoxic_views.listar, 
        name='s2221_evttoxic'),
        
url(r'^s2221-evttoxic/verificar/(?P<hash>.*)/$', 
        s2221_evttoxic_verificar_views.verificar, 
        name='s2221_evttoxic_verificar'),
        
url(r'^s2221-evttoxic/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2221_evttoxic_verificar_views.recibo, 
        name='s2221_evttoxic_recibo'),
        
        
url(r'^s2221-evttoxic/duplicar/(?P<hash>.*)/$',
        s2221_evttoxic_verificar_views.duplicar,
        name='s2221_evttoxic_duplicar'),

url(r'^s2221-evttoxic/criar-alteracao/(?P<hash>.*)/$',
        s2221_evttoxic_verificar_views.criar_alteracao,
        name='s2221_evttoxic_criar_alteracao'),

url(r'^s2221-evttoxic/criar-exclusao/(?P<hash>.*)/$',
        s2221_evttoxic_verificar_views.criar_exclusao,
        name='s2221_evttoxic_criar_exclusao'),
        
url(r'^s2221-evttoxic/xml/(?P<hash>.*)/$', 
        s2221_evttoxic_verificar_views.gerar_xml, 
                name='s2221_evttoxic_xml'),
                

url(r'^s2221-evttoxic/alterar-identidade/(?P<hash>.*)/$',
        s2221_evttoxic_verificar_views.alterar_identidade,
        name='s2221_evttoxic_alterar_identidade'),

url(r'^s2221-evttoxic/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2221_evttoxic_verificar_views.abrir_evento_para_edicao,
        name='s2221_evttoxic_abrir_evento_para_edicao'),

url(r'^s2221-evttoxic/validar-evento/(?P<hash>.*)/$',
        s2221_evttoxic_verificar_views.validar_evento,
        name='s2221_evttoxic_validar_evento'),

url(r'^s2221-evttoxic/salvar/(?P<hash>.*)/$', 
        s2221_evttoxic_views.salvar, 
        name='s2221_evttoxic_salvar'),
        

url(r'^scripts/gerar-identidade/s2221-evttoxic/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2221_evttoxic_views.gerar_identidade, 
        name='s2221_evttoxic_gerar_identidade'),



url(r'^s2230-evtafasttemp/apagar/(?P<hash>.*)/$', 
        s2230_evtafasttemp_views.apagar, 
        name='s2230_evtafasttemp_apagar'),

url(r'^s2230-evtafasttemp/api/$',
            s2230_evtafasttemp_views.s2230evtAfastTempList.as_view() ),

        url(r'^s2230-evtafasttemp/api/(?P<pk>[0-9]+)/$',
            s2230_evtafasttemp_views.s2230evtAfastTempDetail.as_view() ),

url(r'^s2230-evtafasttemp/listar/(?P<hash>.*)/$', 
        s2230_evtafasttemp_views.listar, 
        name='s2230_evtafasttemp'),
        
url(r'^s2230-evtafasttemp/verificar/(?P<hash>.*)/$', 
        s2230_evtafasttemp_verificar_views.verificar, 
        name='s2230_evtafasttemp_verificar'),
        
url(r'^s2230-evtafasttemp/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2230_evtafasttemp_verificar_views.recibo, 
        name='s2230_evtafasttemp_recibo'),
        
        
url(r'^s2230-evtafasttemp/duplicar/(?P<hash>.*)/$',
        s2230_evtafasttemp_verificar_views.duplicar,
        name='s2230_evtafasttemp_duplicar'),

url(r'^s2230-evtafasttemp/criar-alteracao/(?P<hash>.*)/$',
        s2230_evtafasttemp_verificar_views.criar_alteracao,
        name='s2230_evtafasttemp_criar_alteracao'),

url(r'^s2230-evtafasttemp/criar-exclusao/(?P<hash>.*)/$',
        s2230_evtafasttemp_verificar_views.criar_exclusao,
        name='s2230_evtafasttemp_criar_exclusao'),
        
url(r'^s2230-evtafasttemp/xml/(?P<hash>.*)/$', 
        s2230_evtafasttemp_verificar_views.gerar_xml, 
                name='s2230_evtafasttemp_xml'),
                

url(r'^s2230-evtafasttemp/alterar-identidade/(?P<hash>.*)/$',
        s2230_evtafasttemp_verificar_views.alterar_identidade,
        name='s2230_evtafasttemp_alterar_identidade'),

url(r'^s2230-evtafasttemp/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2230_evtafasttemp_verificar_views.abrir_evento_para_edicao,
        name='s2230_evtafasttemp_abrir_evento_para_edicao'),

url(r'^s2230-evtafasttemp/validar-evento/(?P<hash>.*)/$',
        s2230_evtafasttemp_verificar_views.validar_evento,
        name='s2230_evtafasttemp_validar_evento'),

url(r'^s2230-evtafasttemp/salvar/(?P<hash>.*)/$', 
        s2230_evtafasttemp_views.salvar, 
        name='s2230_evtafasttemp_salvar'),
        

url(r'^scripts/gerar-identidade/s2230-evtafasttemp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2230_evtafasttemp_views.gerar_identidade, 
        name='s2230_evtafasttemp_gerar_identidade'),



url(r'^s2231-evtcessao/apagar/(?P<hash>.*)/$', 
        s2231_evtcessao_views.apagar, 
        name='s2231_evtcessao_apagar'),

url(r'^s2231-evtcessao/api/$',
            s2231_evtcessao_views.s2231evtCessaoList.as_view() ),

        url(r'^s2231-evtcessao/api/(?P<pk>[0-9]+)/$',
            s2231_evtcessao_views.s2231evtCessaoDetail.as_view() ),

url(r'^s2231-evtcessao/listar/(?P<hash>.*)/$', 
        s2231_evtcessao_views.listar, 
        name='s2231_evtcessao'),
        
url(r'^s2231-evtcessao/verificar/(?P<hash>.*)/$', 
        s2231_evtcessao_verificar_views.verificar, 
        name='s2231_evtcessao_verificar'),
        
url(r'^s2231-evtcessao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2231_evtcessao_verificar_views.recibo, 
        name='s2231_evtcessao_recibo'),
        
        
url(r'^s2231-evtcessao/duplicar/(?P<hash>.*)/$',
        s2231_evtcessao_verificar_views.duplicar,
        name='s2231_evtcessao_duplicar'),

url(r'^s2231-evtcessao/criar-alteracao/(?P<hash>.*)/$',
        s2231_evtcessao_verificar_views.criar_alteracao,
        name='s2231_evtcessao_criar_alteracao'),

url(r'^s2231-evtcessao/criar-exclusao/(?P<hash>.*)/$',
        s2231_evtcessao_verificar_views.criar_exclusao,
        name='s2231_evtcessao_criar_exclusao'),
        
url(r'^s2231-evtcessao/xml/(?P<hash>.*)/$', 
        s2231_evtcessao_verificar_views.gerar_xml, 
                name='s2231_evtcessao_xml'),
                

url(r'^s2231-evtcessao/alterar-identidade/(?P<hash>.*)/$',
        s2231_evtcessao_verificar_views.alterar_identidade,
        name='s2231_evtcessao_alterar_identidade'),

url(r'^s2231-evtcessao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2231_evtcessao_verificar_views.abrir_evento_para_edicao,
        name='s2231_evtcessao_abrir_evento_para_edicao'),

url(r'^s2231-evtcessao/validar-evento/(?P<hash>.*)/$',
        s2231_evtcessao_verificar_views.validar_evento,
        name='s2231_evtcessao_validar_evento'),

url(r'^s2231-evtcessao/salvar/(?P<hash>.*)/$', 
        s2231_evtcessao_views.salvar, 
        name='s2231_evtcessao_salvar'),
        

url(r'^scripts/gerar-identidade/s2231-evtcessao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2231_evtcessao_views.gerar_identidade, 
        name='s2231_evtcessao_gerar_identidade'),



url(r'^s2240-evtexprisco/apagar/(?P<hash>.*)/$', 
        s2240_evtexprisco_views.apagar, 
        name='s2240_evtexprisco_apagar'),

url(r'^s2240-evtexprisco/api/$',
            s2240_evtexprisco_views.s2240evtExpRiscoList.as_view() ),

        url(r'^s2240-evtexprisco/api/(?P<pk>[0-9]+)/$',
            s2240_evtexprisco_views.s2240evtExpRiscoDetail.as_view() ),

url(r'^s2240-evtexprisco/listar/(?P<hash>.*)/$', 
        s2240_evtexprisco_views.listar, 
        name='s2240_evtexprisco'),
        
url(r'^s2240-evtexprisco/verificar/(?P<hash>.*)/$', 
        s2240_evtexprisco_verificar_views.verificar, 
        name='s2240_evtexprisco_verificar'),
        
url(r'^s2240-evtexprisco/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2240_evtexprisco_verificar_views.recibo, 
        name='s2240_evtexprisco_recibo'),
        
        
url(r'^s2240-evtexprisco/duplicar/(?P<hash>.*)/$',
        s2240_evtexprisco_verificar_views.duplicar,
        name='s2240_evtexprisco_duplicar'),

url(r'^s2240-evtexprisco/criar-alteracao/(?P<hash>.*)/$',
        s2240_evtexprisco_verificar_views.criar_alteracao,
        name='s2240_evtexprisco_criar_alteracao'),

url(r'^s2240-evtexprisco/criar-exclusao/(?P<hash>.*)/$',
        s2240_evtexprisco_verificar_views.criar_exclusao,
        name='s2240_evtexprisco_criar_exclusao'),
        
url(r'^s2240-evtexprisco/xml/(?P<hash>.*)/$', 
        s2240_evtexprisco_verificar_views.gerar_xml, 
                name='s2240_evtexprisco_xml'),
                

url(r'^s2240-evtexprisco/alterar-identidade/(?P<hash>.*)/$',
        s2240_evtexprisco_verificar_views.alterar_identidade,
        name='s2240_evtexprisco_alterar_identidade'),

url(r'^s2240-evtexprisco/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2240_evtexprisco_verificar_views.abrir_evento_para_edicao,
        name='s2240_evtexprisco_abrir_evento_para_edicao'),

url(r'^s2240-evtexprisco/validar-evento/(?P<hash>.*)/$',
        s2240_evtexprisco_verificar_views.validar_evento,
        name='s2240_evtexprisco_validar_evento'),

url(r'^s2240-evtexprisco/salvar/(?P<hash>.*)/$', 
        s2240_evtexprisco_views.salvar, 
        name='s2240_evtexprisco_salvar'),
        

url(r'^scripts/gerar-identidade/s2240-evtexprisco/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2240_evtexprisco_views.gerar_identidade, 
        name='s2240_evtexprisco_gerar_identidade'),



url(r'^s2241-evtinsapo/apagar/(?P<hash>.*)/$', 
        s2241_evtinsapo_views.apagar, 
        name='s2241_evtinsapo_apagar'),

url(r'^s2241-evtinsapo/api/$',
            s2241_evtinsapo_views.s2241evtInsApoList.as_view() ),

        url(r'^s2241-evtinsapo/api/(?P<pk>[0-9]+)/$',
            s2241_evtinsapo_views.s2241evtInsApoDetail.as_view() ),

url(r'^s2241-evtinsapo/listar/(?P<hash>.*)/$', 
        s2241_evtinsapo_views.listar, 
        name='s2241_evtinsapo'),
        
url(r'^s2241-evtinsapo/verificar/(?P<hash>.*)/$', 
        s2241_evtinsapo_verificar_views.verificar, 
        name='s2241_evtinsapo_verificar'),
        
url(r'^s2241-evtinsapo/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2241_evtinsapo_verificar_views.recibo, 
        name='s2241_evtinsapo_recibo'),
        
        
url(r'^s2241-evtinsapo/duplicar/(?P<hash>.*)/$',
        s2241_evtinsapo_verificar_views.duplicar,
        name='s2241_evtinsapo_duplicar'),

url(r'^s2241-evtinsapo/criar-alteracao/(?P<hash>.*)/$',
        s2241_evtinsapo_verificar_views.criar_alteracao,
        name='s2241_evtinsapo_criar_alteracao'),

url(r'^s2241-evtinsapo/criar-exclusao/(?P<hash>.*)/$',
        s2241_evtinsapo_verificar_views.criar_exclusao,
        name='s2241_evtinsapo_criar_exclusao'),
        
url(r'^s2241-evtinsapo/xml/(?P<hash>.*)/$', 
        s2241_evtinsapo_verificar_views.gerar_xml, 
                name='s2241_evtinsapo_xml'),
                

url(r'^s2241-evtinsapo/alterar-identidade/(?P<hash>.*)/$',
        s2241_evtinsapo_verificar_views.alterar_identidade,
        name='s2241_evtinsapo_alterar_identidade'),

url(r'^s2241-evtinsapo/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2241_evtinsapo_verificar_views.abrir_evento_para_edicao,
        name='s2241_evtinsapo_abrir_evento_para_edicao'),

url(r'^s2241-evtinsapo/validar-evento/(?P<hash>.*)/$',
        s2241_evtinsapo_verificar_views.validar_evento,
        name='s2241_evtinsapo_validar_evento'),

url(r'^s2241-evtinsapo/salvar/(?P<hash>.*)/$', 
        s2241_evtinsapo_views.salvar, 
        name='s2241_evtinsapo_salvar'),
        

url(r'^scripts/gerar-identidade/s2241-evtinsapo/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2241_evtinsapo_views.gerar_identidade, 
        name='s2241_evtinsapo_gerar_identidade'),



url(r'^s2245-evttreicap/apagar/(?P<hash>.*)/$', 
        s2245_evttreicap_views.apagar, 
        name='s2245_evttreicap_apagar'),

url(r'^s2245-evttreicap/api/$',
            s2245_evttreicap_views.s2245evtTreiCapList.as_view() ),

        url(r'^s2245-evttreicap/api/(?P<pk>[0-9]+)/$',
            s2245_evttreicap_views.s2245evtTreiCapDetail.as_view() ),

url(r'^s2245-evttreicap/listar/(?P<hash>.*)/$', 
        s2245_evttreicap_views.listar, 
        name='s2245_evttreicap'),
        
url(r'^s2245-evttreicap/verificar/(?P<hash>.*)/$', 
        s2245_evttreicap_verificar_views.verificar, 
        name='s2245_evttreicap_verificar'),
        
url(r'^s2245-evttreicap/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2245_evttreicap_verificar_views.recibo, 
        name='s2245_evttreicap_recibo'),
        
        
url(r'^s2245-evttreicap/duplicar/(?P<hash>.*)/$',
        s2245_evttreicap_verificar_views.duplicar,
        name='s2245_evttreicap_duplicar'),

url(r'^s2245-evttreicap/criar-alteracao/(?P<hash>.*)/$',
        s2245_evttreicap_verificar_views.criar_alteracao,
        name='s2245_evttreicap_criar_alteracao'),

url(r'^s2245-evttreicap/criar-exclusao/(?P<hash>.*)/$',
        s2245_evttreicap_verificar_views.criar_exclusao,
        name='s2245_evttreicap_criar_exclusao'),
        
url(r'^s2245-evttreicap/xml/(?P<hash>.*)/$', 
        s2245_evttreicap_verificar_views.gerar_xml, 
                name='s2245_evttreicap_xml'),
                

url(r'^s2245-evttreicap/alterar-identidade/(?P<hash>.*)/$',
        s2245_evttreicap_verificar_views.alterar_identidade,
        name='s2245_evttreicap_alterar_identidade'),

url(r'^s2245-evttreicap/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2245_evttreicap_verificar_views.abrir_evento_para_edicao,
        name='s2245_evttreicap_abrir_evento_para_edicao'),

url(r'^s2245-evttreicap/validar-evento/(?P<hash>.*)/$',
        s2245_evttreicap_verificar_views.validar_evento,
        name='s2245_evttreicap_validar_evento'),

url(r'^s2245-evttreicap/salvar/(?P<hash>.*)/$', 
        s2245_evttreicap_views.salvar, 
        name='s2245_evttreicap_salvar'),
        

url(r'^scripts/gerar-identidade/s2245-evttreicap/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2245_evttreicap_views.gerar_identidade, 
        name='s2245_evttreicap_gerar_identidade'),



url(r'^s2250-evtavprevio/apagar/(?P<hash>.*)/$', 
        s2250_evtavprevio_views.apagar, 
        name='s2250_evtavprevio_apagar'),

url(r'^s2250-evtavprevio/api/$',
            s2250_evtavprevio_views.s2250evtAvPrevioList.as_view() ),

        url(r'^s2250-evtavprevio/api/(?P<pk>[0-9]+)/$',
            s2250_evtavprevio_views.s2250evtAvPrevioDetail.as_view() ),

url(r'^s2250-evtavprevio/listar/(?P<hash>.*)/$', 
        s2250_evtavprevio_views.listar, 
        name='s2250_evtavprevio'),
        
url(r'^s2250-evtavprevio/verificar/(?P<hash>.*)/$', 
        s2250_evtavprevio_verificar_views.verificar, 
        name='s2250_evtavprevio_verificar'),
        
url(r'^s2250-evtavprevio/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2250_evtavprevio_verificar_views.recibo, 
        name='s2250_evtavprevio_recibo'),
        
        
url(r'^s2250-evtavprevio/duplicar/(?P<hash>.*)/$',
        s2250_evtavprevio_verificar_views.duplicar,
        name='s2250_evtavprevio_duplicar'),

url(r'^s2250-evtavprevio/criar-alteracao/(?P<hash>.*)/$',
        s2250_evtavprevio_verificar_views.criar_alteracao,
        name='s2250_evtavprevio_criar_alteracao'),

url(r'^s2250-evtavprevio/criar-exclusao/(?P<hash>.*)/$',
        s2250_evtavprevio_verificar_views.criar_exclusao,
        name='s2250_evtavprevio_criar_exclusao'),
        
url(r'^s2250-evtavprevio/xml/(?P<hash>.*)/$', 
        s2250_evtavprevio_verificar_views.gerar_xml, 
                name='s2250_evtavprevio_xml'),
                

url(r'^s2250-evtavprevio/alterar-identidade/(?P<hash>.*)/$',
        s2250_evtavprevio_verificar_views.alterar_identidade,
        name='s2250_evtavprevio_alterar_identidade'),

url(r'^s2250-evtavprevio/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2250_evtavprevio_verificar_views.abrir_evento_para_edicao,
        name='s2250_evtavprevio_abrir_evento_para_edicao'),

url(r'^s2250-evtavprevio/validar-evento/(?P<hash>.*)/$',
        s2250_evtavprevio_verificar_views.validar_evento,
        name='s2250_evtavprevio_validar_evento'),

url(r'^s2250-evtavprevio/salvar/(?P<hash>.*)/$', 
        s2250_evtavprevio_views.salvar, 
        name='s2250_evtavprevio_salvar'),
        

url(r'^scripts/gerar-identidade/s2250-evtavprevio/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2250_evtavprevio_views.gerar_identidade, 
        name='s2250_evtavprevio_gerar_identidade'),



url(r'^s2260-evtconvinterm/apagar/(?P<hash>.*)/$', 
        s2260_evtconvinterm_views.apagar, 
        name='s2260_evtconvinterm_apagar'),

url(r'^s2260-evtconvinterm/api/$',
            s2260_evtconvinterm_views.s2260evtConvIntermList.as_view() ),

        url(r'^s2260-evtconvinterm/api/(?P<pk>[0-9]+)/$',
            s2260_evtconvinterm_views.s2260evtConvIntermDetail.as_view() ),

url(r'^s2260-evtconvinterm/listar/(?P<hash>.*)/$', 
        s2260_evtconvinterm_views.listar, 
        name='s2260_evtconvinterm'),
        
url(r'^s2260-evtconvinterm/verificar/(?P<hash>.*)/$', 
        s2260_evtconvinterm_verificar_views.verificar, 
        name='s2260_evtconvinterm_verificar'),
        
url(r'^s2260-evtconvinterm/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2260_evtconvinterm_verificar_views.recibo, 
        name='s2260_evtconvinterm_recibo'),
        
        
url(r'^s2260-evtconvinterm/duplicar/(?P<hash>.*)/$',
        s2260_evtconvinterm_verificar_views.duplicar,
        name='s2260_evtconvinterm_duplicar'),

url(r'^s2260-evtconvinterm/criar-alteracao/(?P<hash>.*)/$',
        s2260_evtconvinterm_verificar_views.criar_alteracao,
        name='s2260_evtconvinterm_criar_alteracao'),

url(r'^s2260-evtconvinterm/criar-exclusao/(?P<hash>.*)/$',
        s2260_evtconvinterm_verificar_views.criar_exclusao,
        name='s2260_evtconvinterm_criar_exclusao'),
        
url(r'^s2260-evtconvinterm/xml/(?P<hash>.*)/$', 
        s2260_evtconvinterm_verificar_views.gerar_xml, 
                name='s2260_evtconvinterm_xml'),
                

url(r'^s2260-evtconvinterm/alterar-identidade/(?P<hash>.*)/$',
        s2260_evtconvinterm_verificar_views.alterar_identidade,
        name='s2260_evtconvinterm_alterar_identidade'),

url(r'^s2260-evtconvinterm/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2260_evtconvinterm_verificar_views.abrir_evento_para_edicao,
        name='s2260_evtconvinterm_abrir_evento_para_edicao'),

url(r'^s2260-evtconvinterm/validar-evento/(?P<hash>.*)/$',
        s2260_evtconvinterm_verificar_views.validar_evento,
        name='s2260_evtconvinterm_validar_evento'),

url(r'^s2260-evtconvinterm/salvar/(?P<hash>.*)/$', 
        s2260_evtconvinterm_views.salvar, 
        name='s2260_evtconvinterm_salvar'),
        

url(r'^scripts/gerar-identidade/s2260-evtconvinterm/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2260_evtconvinterm_views.gerar_identidade, 
        name='s2260_evtconvinterm_gerar_identidade'),



url(r'^s2298-evtreintegr/apagar/(?P<hash>.*)/$', 
        s2298_evtreintegr_views.apagar, 
        name='s2298_evtreintegr_apagar'),

url(r'^s2298-evtreintegr/api/$',
            s2298_evtreintegr_views.s2298evtReintegrList.as_view() ),

        url(r'^s2298-evtreintegr/api/(?P<pk>[0-9]+)/$',
            s2298_evtreintegr_views.s2298evtReintegrDetail.as_view() ),

url(r'^s2298-evtreintegr/listar/(?P<hash>.*)/$', 
        s2298_evtreintegr_views.listar, 
        name='s2298_evtreintegr'),
        
url(r'^s2298-evtreintegr/verificar/(?P<hash>.*)/$', 
        s2298_evtreintegr_verificar_views.verificar, 
        name='s2298_evtreintegr_verificar'),
        
url(r'^s2298-evtreintegr/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2298_evtreintegr_verificar_views.recibo, 
        name='s2298_evtreintegr_recibo'),
        
        
url(r'^s2298-evtreintegr/duplicar/(?P<hash>.*)/$',
        s2298_evtreintegr_verificar_views.duplicar,
        name='s2298_evtreintegr_duplicar'),

url(r'^s2298-evtreintegr/criar-alteracao/(?P<hash>.*)/$',
        s2298_evtreintegr_verificar_views.criar_alteracao,
        name='s2298_evtreintegr_criar_alteracao'),

url(r'^s2298-evtreintegr/criar-exclusao/(?P<hash>.*)/$',
        s2298_evtreintegr_verificar_views.criar_exclusao,
        name='s2298_evtreintegr_criar_exclusao'),
        
url(r'^s2298-evtreintegr/xml/(?P<hash>.*)/$', 
        s2298_evtreintegr_verificar_views.gerar_xml, 
                name='s2298_evtreintegr_xml'),
                

url(r'^s2298-evtreintegr/alterar-identidade/(?P<hash>.*)/$',
        s2298_evtreintegr_verificar_views.alterar_identidade,
        name='s2298_evtreintegr_alterar_identidade'),

url(r'^s2298-evtreintegr/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2298_evtreintegr_verificar_views.abrir_evento_para_edicao,
        name='s2298_evtreintegr_abrir_evento_para_edicao'),

url(r'^s2298-evtreintegr/validar-evento/(?P<hash>.*)/$',
        s2298_evtreintegr_verificar_views.validar_evento,
        name='s2298_evtreintegr_validar_evento'),

url(r'^s2298-evtreintegr/salvar/(?P<hash>.*)/$', 
        s2298_evtreintegr_views.salvar, 
        name='s2298_evtreintegr_salvar'),
        

url(r'^scripts/gerar-identidade/s2298-evtreintegr/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2298_evtreintegr_views.gerar_identidade, 
        name='s2298_evtreintegr_gerar_identidade'),



url(r'^s2299-evtdeslig/apagar/(?P<hash>.*)/$', 
        s2299_evtdeslig_views.apagar, 
        name='s2299_evtdeslig_apagar'),

url(r'^s2299-evtdeslig/api/$',
            s2299_evtdeslig_views.s2299evtDesligList.as_view() ),

        url(r'^s2299-evtdeslig/api/(?P<pk>[0-9]+)/$',
            s2299_evtdeslig_views.s2299evtDesligDetail.as_view() ),

url(r'^s2299-evtdeslig/listar/(?P<hash>.*)/$', 
        s2299_evtdeslig_views.listar, 
        name='s2299_evtdeslig'),
        
url(r'^s2299-evtdeslig/verificar/(?P<hash>.*)/$', 
        s2299_evtdeslig_verificar_views.verificar, 
        name='s2299_evtdeslig_verificar'),
        
url(r'^s2299-evtdeslig/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2299_evtdeslig_verificar_views.recibo, 
        name='s2299_evtdeslig_recibo'),
        
        
url(r'^s2299-evtdeslig/duplicar/(?P<hash>.*)/$',
        s2299_evtdeslig_verificar_views.duplicar,
        name='s2299_evtdeslig_duplicar'),

url(r'^s2299-evtdeslig/criar-alteracao/(?P<hash>.*)/$',
        s2299_evtdeslig_verificar_views.criar_alteracao,
        name='s2299_evtdeslig_criar_alteracao'),

url(r'^s2299-evtdeslig/criar-exclusao/(?P<hash>.*)/$',
        s2299_evtdeslig_verificar_views.criar_exclusao,
        name='s2299_evtdeslig_criar_exclusao'),
        
url(r'^s2299-evtdeslig/xml/(?P<hash>.*)/$', 
        s2299_evtdeslig_verificar_views.gerar_xml, 
                name='s2299_evtdeslig_xml'),
                

url(r'^s2299-evtdeslig/alterar-identidade/(?P<hash>.*)/$',
        s2299_evtdeslig_verificar_views.alterar_identidade,
        name='s2299_evtdeslig_alterar_identidade'),

url(r'^s2299-evtdeslig/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2299_evtdeslig_verificar_views.abrir_evento_para_edicao,
        name='s2299_evtdeslig_abrir_evento_para_edicao'),

url(r'^s2299-evtdeslig/validar-evento/(?P<hash>.*)/$',
        s2299_evtdeslig_verificar_views.validar_evento,
        name='s2299_evtdeslig_validar_evento'),

url(r'^s2299-evtdeslig/salvar/(?P<hash>.*)/$', 
        s2299_evtdeslig_views.salvar, 
        name='s2299_evtdeslig_salvar'),
        

url(r'^scripts/gerar-identidade/s2299-evtdeslig/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2299_evtdeslig_views.gerar_identidade, 
        name='s2299_evtdeslig_gerar_identidade'),



url(r'^s2300-evttsvinicio/apagar/(?P<hash>.*)/$', 
        s2300_evttsvinicio_views.apagar, 
        name='s2300_evttsvinicio_apagar'),

url(r'^s2300-evttsvinicio/api/$',
            s2300_evttsvinicio_views.s2300evtTSVInicioList.as_view() ),

        url(r'^s2300-evttsvinicio/api/(?P<pk>[0-9]+)/$',
            s2300_evttsvinicio_views.s2300evtTSVInicioDetail.as_view() ),

url(r'^s2300-evttsvinicio/listar/(?P<hash>.*)/$', 
        s2300_evttsvinicio_views.listar, 
        name='s2300_evttsvinicio'),
        
url(r'^s2300-evttsvinicio/verificar/(?P<hash>.*)/$', 
        s2300_evttsvinicio_verificar_views.verificar, 
        name='s2300_evttsvinicio_verificar'),
        
url(r'^s2300-evttsvinicio/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2300_evttsvinicio_verificar_views.recibo, 
        name='s2300_evttsvinicio_recibo'),
        
        
url(r'^s2300-evttsvinicio/duplicar/(?P<hash>.*)/$',
        s2300_evttsvinicio_verificar_views.duplicar,
        name='s2300_evttsvinicio_duplicar'),

url(r'^s2300-evttsvinicio/criar-alteracao/(?P<hash>.*)/$',
        s2300_evttsvinicio_verificar_views.criar_alteracao,
        name='s2300_evttsvinicio_criar_alteracao'),

url(r'^s2300-evttsvinicio/criar-exclusao/(?P<hash>.*)/$',
        s2300_evttsvinicio_verificar_views.criar_exclusao,
        name='s2300_evttsvinicio_criar_exclusao'),
        
url(r'^s2300-evttsvinicio/xml/(?P<hash>.*)/$', 
        s2300_evttsvinicio_verificar_views.gerar_xml, 
                name='s2300_evttsvinicio_xml'),
                

url(r'^s2300-evttsvinicio/alterar-identidade/(?P<hash>.*)/$',
        s2300_evttsvinicio_verificar_views.alterar_identidade,
        name='s2300_evttsvinicio_alterar_identidade'),

url(r'^s2300-evttsvinicio/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2300_evttsvinicio_verificar_views.abrir_evento_para_edicao,
        name='s2300_evttsvinicio_abrir_evento_para_edicao'),

url(r'^s2300-evttsvinicio/validar-evento/(?P<hash>.*)/$',
        s2300_evttsvinicio_verificar_views.validar_evento,
        name='s2300_evttsvinicio_validar_evento'),

url(r'^s2300-evttsvinicio/salvar/(?P<hash>.*)/$', 
        s2300_evttsvinicio_views.salvar, 
        name='s2300_evttsvinicio_salvar'),
        

url(r'^scripts/gerar-identidade/s2300-evttsvinicio/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2300_evttsvinicio_views.gerar_identidade, 
        name='s2300_evttsvinicio_gerar_identidade'),



url(r'^s2306-evttsvaltcontr/apagar/(?P<hash>.*)/$', 
        s2306_evttsvaltcontr_views.apagar, 
        name='s2306_evttsvaltcontr_apagar'),

url(r'^s2306-evttsvaltcontr/api/$',
            s2306_evttsvaltcontr_views.s2306evtTSVAltContrList.as_view() ),

        url(r'^s2306-evttsvaltcontr/api/(?P<pk>[0-9]+)/$',
            s2306_evttsvaltcontr_views.s2306evtTSVAltContrDetail.as_view() ),

url(r'^s2306-evttsvaltcontr/listar/(?P<hash>.*)/$', 
        s2306_evttsvaltcontr_views.listar, 
        name='s2306_evttsvaltcontr'),
        
url(r'^s2306-evttsvaltcontr/verificar/(?P<hash>.*)/$', 
        s2306_evttsvaltcontr_verificar_views.verificar, 
        name='s2306_evttsvaltcontr_verificar'),
        
url(r'^s2306-evttsvaltcontr/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2306_evttsvaltcontr_verificar_views.recibo, 
        name='s2306_evttsvaltcontr_recibo'),
        
        
url(r'^s2306-evttsvaltcontr/duplicar/(?P<hash>.*)/$',
        s2306_evttsvaltcontr_verificar_views.duplicar,
        name='s2306_evttsvaltcontr_duplicar'),

url(r'^s2306-evttsvaltcontr/criar-alteracao/(?P<hash>.*)/$',
        s2306_evttsvaltcontr_verificar_views.criar_alteracao,
        name='s2306_evttsvaltcontr_criar_alteracao'),

url(r'^s2306-evttsvaltcontr/criar-exclusao/(?P<hash>.*)/$',
        s2306_evttsvaltcontr_verificar_views.criar_exclusao,
        name='s2306_evttsvaltcontr_criar_exclusao'),
        
url(r'^s2306-evttsvaltcontr/xml/(?P<hash>.*)/$', 
        s2306_evttsvaltcontr_verificar_views.gerar_xml, 
                name='s2306_evttsvaltcontr_xml'),
                

url(r'^s2306-evttsvaltcontr/alterar-identidade/(?P<hash>.*)/$',
        s2306_evttsvaltcontr_verificar_views.alterar_identidade,
        name='s2306_evttsvaltcontr_alterar_identidade'),

url(r'^s2306-evttsvaltcontr/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2306_evttsvaltcontr_verificar_views.abrir_evento_para_edicao,
        name='s2306_evttsvaltcontr_abrir_evento_para_edicao'),

url(r'^s2306-evttsvaltcontr/validar-evento/(?P<hash>.*)/$',
        s2306_evttsvaltcontr_verificar_views.validar_evento,
        name='s2306_evttsvaltcontr_validar_evento'),

url(r'^s2306-evttsvaltcontr/salvar/(?P<hash>.*)/$', 
        s2306_evttsvaltcontr_views.salvar, 
        name='s2306_evttsvaltcontr_salvar'),
        

url(r'^scripts/gerar-identidade/s2306-evttsvaltcontr/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2306_evttsvaltcontr_views.gerar_identidade, 
        name='s2306_evttsvaltcontr_gerar_identidade'),



url(r'^s2399-evttsvtermino/apagar/(?P<hash>.*)/$', 
        s2399_evttsvtermino_views.apagar, 
        name='s2399_evttsvtermino_apagar'),

url(r'^s2399-evttsvtermino/api/$',
            s2399_evttsvtermino_views.s2399evtTSVTerminoList.as_view() ),

        url(r'^s2399-evttsvtermino/api/(?P<pk>[0-9]+)/$',
            s2399_evttsvtermino_views.s2399evtTSVTerminoDetail.as_view() ),

url(r'^s2399-evttsvtermino/listar/(?P<hash>.*)/$', 
        s2399_evttsvtermino_views.listar, 
        name='s2399_evttsvtermino'),
        
url(r'^s2399-evttsvtermino/verificar/(?P<hash>.*)/$', 
        s2399_evttsvtermino_verificar_views.verificar, 
        name='s2399_evttsvtermino_verificar'),
        
url(r'^s2399-evttsvtermino/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2399_evttsvtermino_verificar_views.recibo, 
        name='s2399_evttsvtermino_recibo'),
        
        
url(r'^s2399-evttsvtermino/duplicar/(?P<hash>.*)/$',
        s2399_evttsvtermino_verificar_views.duplicar,
        name='s2399_evttsvtermino_duplicar'),

url(r'^s2399-evttsvtermino/criar-alteracao/(?P<hash>.*)/$',
        s2399_evttsvtermino_verificar_views.criar_alteracao,
        name='s2399_evttsvtermino_criar_alteracao'),

url(r'^s2399-evttsvtermino/criar-exclusao/(?P<hash>.*)/$',
        s2399_evttsvtermino_verificar_views.criar_exclusao,
        name='s2399_evttsvtermino_criar_exclusao'),
        
url(r'^s2399-evttsvtermino/xml/(?P<hash>.*)/$', 
        s2399_evttsvtermino_verificar_views.gerar_xml, 
                name='s2399_evttsvtermino_xml'),
                

url(r'^s2399-evttsvtermino/alterar-identidade/(?P<hash>.*)/$',
        s2399_evttsvtermino_verificar_views.alterar_identidade,
        name='s2399_evttsvtermino_alterar_identidade'),

url(r'^s2399-evttsvtermino/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2399_evttsvtermino_verificar_views.abrir_evento_para_edicao,
        name='s2399_evttsvtermino_abrir_evento_para_edicao'),

url(r'^s2399-evttsvtermino/validar-evento/(?P<hash>.*)/$',
        s2399_evttsvtermino_verificar_views.validar_evento,
        name='s2399_evttsvtermino_validar_evento'),

url(r'^s2399-evttsvtermino/salvar/(?P<hash>.*)/$', 
        s2399_evttsvtermino_views.salvar, 
        name='s2399_evttsvtermino_salvar'),
        

url(r'^scripts/gerar-identidade/s2399-evttsvtermino/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2399_evttsvtermino_views.gerar_identidade, 
        name='s2399_evttsvtermino_gerar_identidade'),



url(r'^s2400-evtcdbenefin/apagar/(?P<hash>.*)/$', 
        s2400_evtcdbenefin_views.apagar, 
        name='s2400_evtcdbenefin_apagar'),

url(r'^s2400-evtcdbenefin/api/$',
            s2400_evtcdbenefin_views.s2400evtCdBenefInList.as_view() ),

        url(r'^s2400-evtcdbenefin/api/(?P<pk>[0-9]+)/$',
            s2400_evtcdbenefin_views.s2400evtCdBenefInDetail.as_view() ),

url(r'^s2400-evtcdbenefin/listar/(?P<hash>.*)/$', 
        s2400_evtcdbenefin_views.listar, 
        name='s2400_evtcdbenefin'),
        
url(r'^s2400-evtcdbenefin/verificar/(?P<hash>.*)/$', 
        s2400_evtcdbenefin_verificar_views.verificar, 
        name='s2400_evtcdbenefin_verificar'),
        
url(r'^s2400-evtcdbenefin/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2400_evtcdbenefin_verificar_views.recibo, 
        name='s2400_evtcdbenefin_recibo'),
        
        
url(r'^s2400-evtcdbenefin/duplicar/(?P<hash>.*)/$',
        s2400_evtcdbenefin_verificar_views.duplicar,
        name='s2400_evtcdbenefin_duplicar'),

url(r'^s2400-evtcdbenefin/criar-alteracao/(?P<hash>.*)/$',
        s2400_evtcdbenefin_verificar_views.criar_alteracao,
        name='s2400_evtcdbenefin_criar_alteracao'),

url(r'^s2400-evtcdbenefin/criar-exclusao/(?P<hash>.*)/$',
        s2400_evtcdbenefin_verificar_views.criar_exclusao,
        name='s2400_evtcdbenefin_criar_exclusao'),
        
url(r'^s2400-evtcdbenefin/xml/(?P<hash>.*)/$', 
        s2400_evtcdbenefin_verificar_views.gerar_xml, 
                name='s2400_evtcdbenefin_xml'),
                

url(r'^s2400-evtcdbenefin/alterar-identidade/(?P<hash>.*)/$',
        s2400_evtcdbenefin_verificar_views.alterar_identidade,
        name='s2400_evtcdbenefin_alterar_identidade'),

url(r'^s2400-evtcdbenefin/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2400_evtcdbenefin_verificar_views.abrir_evento_para_edicao,
        name='s2400_evtcdbenefin_abrir_evento_para_edicao'),

url(r'^s2400-evtcdbenefin/validar-evento/(?P<hash>.*)/$',
        s2400_evtcdbenefin_verificar_views.validar_evento,
        name='s2400_evtcdbenefin_validar_evento'),

url(r'^s2400-evtcdbenefin/salvar/(?P<hash>.*)/$', 
        s2400_evtcdbenefin_views.salvar, 
        name='s2400_evtcdbenefin_salvar'),
        

url(r'^scripts/gerar-identidade/s2400-evtcdbenefin/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2400_evtcdbenefin_views.gerar_identidade, 
        name='s2400_evtcdbenefin_gerar_identidade'),



url(r'^s2405-evtcdbenefalt/apagar/(?P<hash>.*)/$', 
        s2405_evtcdbenefalt_views.apagar, 
        name='s2405_evtcdbenefalt_apagar'),

url(r'^s2405-evtcdbenefalt/api/$',
            s2405_evtcdbenefalt_views.s2405evtCdBenefAltList.as_view() ),

        url(r'^s2405-evtcdbenefalt/api/(?P<pk>[0-9]+)/$',
            s2405_evtcdbenefalt_views.s2405evtCdBenefAltDetail.as_view() ),

url(r'^s2405-evtcdbenefalt/listar/(?P<hash>.*)/$', 
        s2405_evtcdbenefalt_views.listar, 
        name='s2405_evtcdbenefalt'),
        
url(r'^s2405-evtcdbenefalt/verificar/(?P<hash>.*)/$', 
        s2405_evtcdbenefalt_verificar_views.verificar, 
        name='s2405_evtcdbenefalt_verificar'),
        
url(r'^s2405-evtcdbenefalt/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2405_evtcdbenefalt_verificar_views.recibo, 
        name='s2405_evtcdbenefalt_recibo'),
        
        
url(r'^s2405-evtcdbenefalt/duplicar/(?P<hash>.*)/$',
        s2405_evtcdbenefalt_verificar_views.duplicar,
        name='s2405_evtcdbenefalt_duplicar'),

url(r'^s2405-evtcdbenefalt/criar-alteracao/(?P<hash>.*)/$',
        s2405_evtcdbenefalt_verificar_views.criar_alteracao,
        name='s2405_evtcdbenefalt_criar_alteracao'),

url(r'^s2405-evtcdbenefalt/criar-exclusao/(?P<hash>.*)/$',
        s2405_evtcdbenefalt_verificar_views.criar_exclusao,
        name='s2405_evtcdbenefalt_criar_exclusao'),
        
url(r'^s2405-evtcdbenefalt/xml/(?P<hash>.*)/$', 
        s2405_evtcdbenefalt_verificar_views.gerar_xml, 
                name='s2405_evtcdbenefalt_xml'),
                

url(r'^s2405-evtcdbenefalt/alterar-identidade/(?P<hash>.*)/$',
        s2405_evtcdbenefalt_verificar_views.alterar_identidade,
        name='s2405_evtcdbenefalt_alterar_identidade'),

url(r'^s2405-evtcdbenefalt/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2405_evtcdbenefalt_verificar_views.abrir_evento_para_edicao,
        name='s2405_evtcdbenefalt_abrir_evento_para_edicao'),

url(r'^s2405-evtcdbenefalt/validar-evento/(?P<hash>.*)/$',
        s2405_evtcdbenefalt_verificar_views.validar_evento,
        name='s2405_evtcdbenefalt_validar_evento'),

url(r'^s2405-evtcdbenefalt/salvar/(?P<hash>.*)/$', 
        s2405_evtcdbenefalt_views.salvar, 
        name='s2405_evtcdbenefalt_salvar'),
        

url(r'^scripts/gerar-identidade/s2405-evtcdbenefalt/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2405_evtcdbenefalt_views.gerar_identidade, 
        name='s2405_evtcdbenefalt_gerar_identidade'),



url(r'^s2410-evtcdbenin/apagar/(?P<hash>.*)/$', 
        s2410_evtcdbenin_views.apagar, 
        name='s2410_evtcdbenin_apagar'),

url(r'^s2410-evtcdbenin/api/$',
            s2410_evtcdbenin_views.s2410evtCdBenInList.as_view() ),

        url(r'^s2410-evtcdbenin/api/(?P<pk>[0-9]+)/$',
            s2410_evtcdbenin_views.s2410evtCdBenInDetail.as_view() ),

url(r'^s2410-evtcdbenin/listar/(?P<hash>.*)/$', 
        s2410_evtcdbenin_views.listar, 
        name='s2410_evtcdbenin'),
        
url(r'^s2410-evtcdbenin/verificar/(?P<hash>.*)/$', 
        s2410_evtcdbenin_verificar_views.verificar, 
        name='s2410_evtcdbenin_verificar'),
        
url(r'^s2410-evtcdbenin/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2410_evtcdbenin_verificar_views.recibo, 
        name='s2410_evtcdbenin_recibo'),
        
        
url(r'^s2410-evtcdbenin/duplicar/(?P<hash>.*)/$',
        s2410_evtcdbenin_verificar_views.duplicar,
        name='s2410_evtcdbenin_duplicar'),

url(r'^s2410-evtcdbenin/criar-alteracao/(?P<hash>.*)/$',
        s2410_evtcdbenin_verificar_views.criar_alteracao,
        name='s2410_evtcdbenin_criar_alteracao'),

url(r'^s2410-evtcdbenin/criar-exclusao/(?P<hash>.*)/$',
        s2410_evtcdbenin_verificar_views.criar_exclusao,
        name='s2410_evtcdbenin_criar_exclusao'),
        
url(r'^s2410-evtcdbenin/xml/(?P<hash>.*)/$', 
        s2410_evtcdbenin_verificar_views.gerar_xml, 
                name='s2410_evtcdbenin_xml'),
                

url(r'^s2410-evtcdbenin/alterar-identidade/(?P<hash>.*)/$',
        s2410_evtcdbenin_verificar_views.alterar_identidade,
        name='s2410_evtcdbenin_alterar_identidade'),

url(r'^s2410-evtcdbenin/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2410_evtcdbenin_verificar_views.abrir_evento_para_edicao,
        name='s2410_evtcdbenin_abrir_evento_para_edicao'),

url(r'^s2410-evtcdbenin/validar-evento/(?P<hash>.*)/$',
        s2410_evtcdbenin_verificar_views.validar_evento,
        name='s2410_evtcdbenin_validar_evento'),

url(r'^s2410-evtcdbenin/salvar/(?P<hash>.*)/$', 
        s2410_evtcdbenin_views.salvar, 
        name='s2410_evtcdbenin_salvar'),
        

url(r'^scripts/gerar-identidade/s2410-evtcdbenin/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2410_evtcdbenin_views.gerar_identidade, 
        name='s2410_evtcdbenin_gerar_identidade'),



url(r'^s2416-evtcdbenalt/apagar/(?P<hash>.*)/$', 
        s2416_evtcdbenalt_views.apagar, 
        name='s2416_evtcdbenalt_apagar'),

url(r'^s2416-evtcdbenalt/api/$',
            s2416_evtcdbenalt_views.s2416evtCdBenAltList.as_view() ),

        url(r'^s2416-evtcdbenalt/api/(?P<pk>[0-9]+)/$',
            s2416_evtcdbenalt_views.s2416evtCdBenAltDetail.as_view() ),

url(r'^s2416-evtcdbenalt/listar/(?P<hash>.*)/$', 
        s2416_evtcdbenalt_views.listar, 
        name='s2416_evtcdbenalt'),
        
url(r'^s2416-evtcdbenalt/verificar/(?P<hash>.*)/$', 
        s2416_evtcdbenalt_verificar_views.verificar, 
        name='s2416_evtcdbenalt_verificar'),
        
url(r'^s2416-evtcdbenalt/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2416_evtcdbenalt_verificar_views.recibo, 
        name='s2416_evtcdbenalt_recibo'),
        
        
url(r'^s2416-evtcdbenalt/duplicar/(?P<hash>.*)/$',
        s2416_evtcdbenalt_verificar_views.duplicar,
        name='s2416_evtcdbenalt_duplicar'),

url(r'^s2416-evtcdbenalt/criar-alteracao/(?P<hash>.*)/$',
        s2416_evtcdbenalt_verificar_views.criar_alteracao,
        name='s2416_evtcdbenalt_criar_alteracao'),

url(r'^s2416-evtcdbenalt/criar-exclusao/(?P<hash>.*)/$',
        s2416_evtcdbenalt_verificar_views.criar_exclusao,
        name='s2416_evtcdbenalt_criar_exclusao'),
        
url(r'^s2416-evtcdbenalt/xml/(?P<hash>.*)/$', 
        s2416_evtcdbenalt_verificar_views.gerar_xml, 
                name='s2416_evtcdbenalt_xml'),
                

url(r'^s2416-evtcdbenalt/alterar-identidade/(?P<hash>.*)/$',
        s2416_evtcdbenalt_verificar_views.alterar_identidade,
        name='s2416_evtcdbenalt_alterar_identidade'),

url(r'^s2416-evtcdbenalt/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2416_evtcdbenalt_verificar_views.abrir_evento_para_edicao,
        name='s2416_evtcdbenalt_abrir_evento_para_edicao'),

url(r'^s2416-evtcdbenalt/validar-evento/(?P<hash>.*)/$',
        s2416_evtcdbenalt_verificar_views.validar_evento,
        name='s2416_evtcdbenalt_validar_evento'),

url(r'^s2416-evtcdbenalt/salvar/(?P<hash>.*)/$', 
        s2416_evtcdbenalt_views.salvar, 
        name='s2416_evtcdbenalt_salvar'),
        

url(r'^scripts/gerar-identidade/s2416-evtcdbenalt/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2416_evtcdbenalt_views.gerar_identidade, 
        name='s2416_evtcdbenalt_gerar_identidade'),



url(r'^s2420-evtcdbenterm/apagar/(?P<hash>.*)/$', 
        s2420_evtcdbenterm_views.apagar, 
        name='s2420_evtcdbenterm_apagar'),

url(r'^s2420-evtcdbenterm/api/$',
            s2420_evtcdbenterm_views.s2420evtCdBenTermList.as_view() ),

        url(r'^s2420-evtcdbenterm/api/(?P<pk>[0-9]+)/$',
            s2420_evtcdbenterm_views.s2420evtCdBenTermDetail.as_view() ),

url(r'^s2420-evtcdbenterm/listar/(?P<hash>.*)/$', 
        s2420_evtcdbenterm_views.listar, 
        name='s2420_evtcdbenterm'),
        
url(r'^s2420-evtcdbenterm/verificar/(?P<hash>.*)/$', 
        s2420_evtcdbenterm_verificar_views.verificar, 
        name='s2420_evtcdbenterm_verificar'),
        
url(r'^s2420-evtcdbenterm/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s2420_evtcdbenterm_verificar_views.recibo, 
        name='s2420_evtcdbenterm_recibo'),
        
        
url(r'^s2420-evtcdbenterm/duplicar/(?P<hash>.*)/$',
        s2420_evtcdbenterm_verificar_views.duplicar,
        name='s2420_evtcdbenterm_duplicar'),

url(r'^s2420-evtcdbenterm/criar-alteracao/(?P<hash>.*)/$',
        s2420_evtcdbenterm_verificar_views.criar_alteracao,
        name='s2420_evtcdbenterm_criar_alteracao'),

url(r'^s2420-evtcdbenterm/criar-exclusao/(?P<hash>.*)/$',
        s2420_evtcdbenterm_verificar_views.criar_exclusao,
        name='s2420_evtcdbenterm_criar_exclusao'),
        
url(r'^s2420-evtcdbenterm/xml/(?P<hash>.*)/$', 
        s2420_evtcdbenterm_verificar_views.gerar_xml, 
                name='s2420_evtcdbenterm_xml'),
                

url(r'^s2420-evtcdbenterm/alterar-identidade/(?P<hash>.*)/$',
        s2420_evtcdbenterm_verificar_views.alterar_identidade,
        name='s2420_evtcdbenterm_alterar_identidade'),

url(r'^s2420-evtcdbenterm/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s2420_evtcdbenterm_verificar_views.abrir_evento_para_edicao,
        name='s2420_evtcdbenterm_abrir_evento_para_edicao'),

url(r'^s2420-evtcdbenterm/validar-evento/(?P<hash>.*)/$',
        s2420_evtcdbenterm_verificar_views.validar_evento,
        name='s2420_evtcdbenterm_validar_evento'),

url(r'^s2420-evtcdbenterm/salvar/(?P<hash>.*)/$', 
        s2420_evtcdbenterm_views.salvar, 
        name='s2420_evtcdbenterm_salvar'),
        

url(r'^scripts/gerar-identidade/s2420-evtcdbenterm/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s2420_evtcdbenterm_views.gerar_identidade, 
        name='s2420_evtcdbenterm_gerar_identidade'),



url(r'^s3000-evtexclusao/apagar/(?P<hash>.*)/$', 
        s3000_evtexclusao_views.apagar, 
        name='s3000_evtexclusao_apagar'),

url(r'^s3000-evtexclusao/api/$',
            s3000_evtexclusao_views.s3000evtExclusaoList.as_view() ),

        url(r'^s3000-evtexclusao/api/(?P<pk>[0-9]+)/$',
            s3000_evtexclusao_views.s3000evtExclusaoDetail.as_view() ),

url(r'^s3000-evtexclusao/listar/(?P<hash>.*)/$', 
        s3000_evtexclusao_views.listar, 
        name='s3000_evtexclusao'),
        
url(r'^s3000-evtexclusao/verificar/(?P<hash>.*)/$', 
        s3000_evtexclusao_verificar_views.verificar, 
        name='s3000_evtexclusao_verificar'),
        
url(r'^s3000-evtexclusao/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s3000_evtexclusao_verificar_views.recibo, 
        name='s3000_evtexclusao_recibo'),
        
        
url(r'^s3000-evtexclusao/duplicar/(?P<hash>.*)/$',
        s3000_evtexclusao_verificar_views.duplicar,
        name='s3000_evtexclusao_duplicar'),

url(r'^s3000-evtexclusao/criar-alteracao/(?P<hash>.*)/$',
        s3000_evtexclusao_verificar_views.criar_alteracao,
        name='s3000_evtexclusao_criar_alteracao'),

url(r'^s3000-evtexclusao/criar-exclusao/(?P<hash>.*)/$',
        s3000_evtexclusao_verificar_views.criar_exclusao,
        name='s3000_evtexclusao_criar_exclusao'),
        
url(r'^s3000-evtexclusao/xml/(?P<hash>.*)/$', 
        s3000_evtexclusao_verificar_views.gerar_xml, 
                name='s3000_evtexclusao_xml'),
                

url(r'^s3000-evtexclusao/alterar-identidade/(?P<hash>.*)/$',
        s3000_evtexclusao_verificar_views.alterar_identidade,
        name='s3000_evtexclusao_alterar_identidade'),

url(r'^s3000-evtexclusao/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s3000_evtexclusao_verificar_views.abrir_evento_para_edicao,
        name='s3000_evtexclusao_abrir_evento_para_edicao'),

url(r'^s3000-evtexclusao/validar-evento/(?P<hash>.*)/$',
        s3000_evtexclusao_verificar_views.validar_evento,
        name='s3000_evtexclusao_validar_evento'),

url(r'^s3000-evtexclusao/salvar/(?P<hash>.*)/$', 
        s3000_evtexclusao_views.salvar, 
        name='s3000_evtexclusao_salvar'),
        

url(r'^scripts/gerar-identidade/s3000-evtexclusao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s3000_evtexclusao_views.gerar_identidade, 
        name='s3000_evtexclusao_gerar_identidade'),



url(r'^s5001-evtbasestrab/apagar/(?P<hash>.*)/$', 
        s5001_evtbasestrab_views.apagar, 
        name='s5001_evtbasestrab_apagar'),

url(r'^s5001-evtbasestrab/api/$',
            s5001_evtbasestrab_views.s5001evtBasesTrabList.as_view() ),

        url(r'^s5001-evtbasestrab/api/(?P<pk>[0-9]+)/$',
            s5001_evtbasestrab_views.s5001evtBasesTrabDetail.as_view() ),

url(r'^s5001-evtbasestrab/listar/(?P<hash>.*)/$', 
        s5001_evtbasestrab_views.listar, 
        name='s5001_evtbasestrab'),
        
url(r'^s5001-evtbasestrab/verificar/(?P<hash>.*)/$', 
        s5001_evtbasestrab_verificar_views.verificar, 
        name='s5001_evtbasestrab_verificar'),
        
url(r'^s5001-evtbasestrab/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s5001_evtbasestrab_verificar_views.recibo, 
        name='s5001_evtbasestrab_recibo'),
        
        
url(r'^s5001-evtbasestrab/duplicar/(?P<hash>.*)/$',
        s5001_evtbasestrab_verificar_views.duplicar,
        name='s5001_evtbasestrab_duplicar'),

url(r'^s5001-evtbasestrab/criar-alteracao/(?P<hash>.*)/$',
        s5001_evtbasestrab_verificar_views.criar_alteracao,
        name='s5001_evtbasestrab_criar_alteracao'),

url(r'^s5001-evtbasestrab/criar-exclusao/(?P<hash>.*)/$',
        s5001_evtbasestrab_verificar_views.criar_exclusao,
        name='s5001_evtbasestrab_criar_exclusao'),
        
url(r'^s5001-evtbasestrab/xml/(?P<hash>.*)/$', 
        s5001_evtbasestrab_verificar_views.gerar_xml, 
                name='s5001_evtbasestrab_xml'),
                

url(r'^s5001-evtbasestrab/alterar-identidade/(?P<hash>.*)/$',
        s5001_evtbasestrab_verificar_views.alterar_identidade,
        name='s5001_evtbasestrab_alterar_identidade'),

url(r'^s5001-evtbasestrab/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s5001_evtbasestrab_verificar_views.abrir_evento_para_edicao,
        name='s5001_evtbasestrab_abrir_evento_para_edicao'),

url(r'^s5001-evtbasestrab/validar-evento/(?P<hash>.*)/$',
        s5001_evtbasestrab_verificar_views.validar_evento,
        name='s5001_evtbasestrab_validar_evento'),

url(r'^s5001-evtbasestrab/salvar/(?P<hash>.*)/$', 
        s5001_evtbasestrab_views.salvar, 
        name='s5001_evtbasestrab_salvar'),
        

url(r'^scripts/gerar-identidade/s5001-evtbasestrab/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s5001_evtbasestrab_views.gerar_identidade, 
        name='s5001_evtbasestrab_gerar_identidade'),



url(r'^s5002-evtirrfbenef/apagar/(?P<hash>.*)/$', 
        s5002_evtirrfbenef_views.apagar, 
        name='s5002_evtirrfbenef_apagar'),

url(r'^s5002-evtirrfbenef/api/$',
            s5002_evtirrfbenef_views.s5002evtIrrfBenefList.as_view() ),

        url(r'^s5002-evtirrfbenef/api/(?P<pk>[0-9]+)/$',
            s5002_evtirrfbenef_views.s5002evtIrrfBenefDetail.as_view() ),

url(r'^s5002-evtirrfbenef/listar/(?P<hash>.*)/$', 
        s5002_evtirrfbenef_views.listar, 
        name='s5002_evtirrfbenef'),
        
url(r'^s5002-evtirrfbenef/verificar/(?P<hash>.*)/$', 
        s5002_evtirrfbenef_verificar_views.verificar, 
        name='s5002_evtirrfbenef_verificar'),
        
url(r'^s5002-evtirrfbenef/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s5002_evtirrfbenef_verificar_views.recibo, 
        name='s5002_evtirrfbenef_recibo'),
        
        
url(r'^s5002-evtirrfbenef/duplicar/(?P<hash>.*)/$',
        s5002_evtirrfbenef_verificar_views.duplicar,
        name='s5002_evtirrfbenef_duplicar'),

url(r'^s5002-evtirrfbenef/criar-alteracao/(?P<hash>.*)/$',
        s5002_evtirrfbenef_verificar_views.criar_alteracao,
        name='s5002_evtirrfbenef_criar_alteracao'),

url(r'^s5002-evtirrfbenef/criar-exclusao/(?P<hash>.*)/$',
        s5002_evtirrfbenef_verificar_views.criar_exclusao,
        name='s5002_evtirrfbenef_criar_exclusao'),
        
url(r'^s5002-evtirrfbenef/xml/(?P<hash>.*)/$', 
        s5002_evtirrfbenef_verificar_views.gerar_xml, 
                name='s5002_evtirrfbenef_xml'),
                

url(r'^s5002-evtirrfbenef/alterar-identidade/(?P<hash>.*)/$',
        s5002_evtirrfbenef_verificar_views.alterar_identidade,
        name='s5002_evtirrfbenef_alterar_identidade'),

url(r'^s5002-evtirrfbenef/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s5002_evtirrfbenef_verificar_views.abrir_evento_para_edicao,
        name='s5002_evtirrfbenef_abrir_evento_para_edicao'),

url(r'^s5002-evtirrfbenef/validar-evento/(?P<hash>.*)/$',
        s5002_evtirrfbenef_verificar_views.validar_evento,
        name='s5002_evtirrfbenef_validar_evento'),

url(r'^s5002-evtirrfbenef/salvar/(?P<hash>.*)/$', 
        s5002_evtirrfbenef_views.salvar, 
        name='s5002_evtirrfbenef_salvar'),
        

url(r'^scripts/gerar-identidade/s5002-evtirrfbenef/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s5002_evtirrfbenef_views.gerar_identidade, 
        name='s5002_evtirrfbenef_gerar_identidade'),



url(r'^s5011-evtcs/apagar/(?P<hash>.*)/$', 
        s5011_evtcs_views.apagar, 
        name='s5011_evtcs_apagar'),

url(r'^s5011-evtcs/api/$',
            s5011_evtcs_views.s5011evtCSList.as_view() ),

        url(r'^s5011-evtcs/api/(?P<pk>[0-9]+)/$',
            s5011_evtcs_views.s5011evtCSDetail.as_view() ),

url(r'^s5011-evtcs/listar/(?P<hash>.*)/$', 
        s5011_evtcs_views.listar, 
        name='s5011_evtcs'),
        
url(r'^s5011-evtcs/verificar/(?P<hash>.*)/$', 
        s5011_evtcs_verificar_views.verificar, 
        name='s5011_evtcs_verificar'),
        
url(r'^s5011-evtcs/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s5011_evtcs_verificar_views.recibo, 
        name='s5011_evtcs_recibo'),
        
        
url(r'^s5011-evtcs/duplicar/(?P<hash>.*)/$',
        s5011_evtcs_verificar_views.duplicar,
        name='s5011_evtcs_duplicar'),

url(r'^s5011-evtcs/criar-alteracao/(?P<hash>.*)/$',
        s5011_evtcs_verificar_views.criar_alteracao,
        name='s5011_evtcs_criar_alteracao'),

url(r'^s5011-evtcs/criar-exclusao/(?P<hash>.*)/$',
        s5011_evtcs_verificar_views.criar_exclusao,
        name='s5011_evtcs_criar_exclusao'),
        
url(r'^s5011-evtcs/xml/(?P<hash>.*)/$', 
        s5011_evtcs_verificar_views.gerar_xml, 
                name='s5011_evtcs_xml'),
                

url(r'^s5011-evtcs/alterar-identidade/(?P<hash>.*)/$',
        s5011_evtcs_verificar_views.alterar_identidade,
        name='s5011_evtcs_alterar_identidade'),

url(r'^s5011-evtcs/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s5011_evtcs_verificar_views.abrir_evento_para_edicao,
        name='s5011_evtcs_abrir_evento_para_edicao'),

url(r'^s5011-evtcs/validar-evento/(?P<hash>.*)/$',
        s5011_evtcs_verificar_views.validar_evento,
        name='s5011_evtcs_validar_evento'),

url(r'^s5011-evtcs/salvar/(?P<hash>.*)/$', 
        s5011_evtcs_views.salvar, 
        name='s5011_evtcs_salvar'),
        

url(r'^scripts/gerar-identidade/s5011-evtcs/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s5011_evtcs_views.gerar_identidade, 
        name='s5011_evtcs_gerar_identidade'),



url(r'^s5012-evtirrf/apagar/(?P<hash>.*)/$', 
        s5012_evtirrf_views.apagar, 
        name='s5012_evtirrf_apagar'),

url(r'^s5012-evtirrf/api/$',
            s5012_evtirrf_views.s5012evtIrrfList.as_view() ),

        url(r'^s5012-evtirrf/api/(?P<pk>[0-9]+)/$',
            s5012_evtirrf_views.s5012evtIrrfDetail.as_view() ),

url(r'^s5012-evtirrf/listar/(?P<hash>.*)/$', 
        s5012_evtirrf_views.listar, 
        name='s5012_evtirrf'),
        
url(r'^s5012-evtirrf/verificar/(?P<hash>.*)/$', 
        s5012_evtirrf_verificar_views.verificar, 
        name='s5012_evtirrf_verificar'),
        
url(r'^s5012-evtirrf/recibo/(?P<hash>.*)/(?P<tipo>[\w\-]+)/$', 
        s5012_evtirrf_verificar_views.recibo, 
        name='s5012_evtirrf_recibo'),
        
        
url(r'^s5012-evtirrf/duplicar/(?P<hash>.*)/$',
        s5012_evtirrf_verificar_views.duplicar,
        name='s5012_evtirrf_duplicar'),

url(r'^s5012-evtirrf/criar-alteracao/(?P<hash>.*)/$',
        s5012_evtirrf_verificar_views.criar_alteracao,
        name='s5012_evtirrf_criar_alteracao'),

url(r'^s5012-evtirrf/criar-exclusao/(?P<hash>.*)/$',
        s5012_evtirrf_verificar_views.criar_exclusao,
        name='s5012_evtirrf_criar_exclusao'),
        
url(r'^s5012-evtirrf/xml/(?P<hash>.*)/$', 
        s5012_evtirrf_verificar_views.gerar_xml, 
                name='s5012_evtirrf_xml'),
                

url(r'^s5012-evtirrf/alterar-identidade/(?P<hash>.*)/$',
        s5012_evtirrf_verificar_views.alterar_identidade,
        name='s5012_evtirrf_alterar_identidade'),

url(r'^s5012-evtirrf/abrir-evento-para-edicao/(?P<hash>.*)/$',
        s5012_evtirrf_verificar_views.abrir_evento_para_edicao,
        name='s5012_evtirrf_abrir_evento_para_edicao'),

url(r'^s5012-evtirrf/validar-evento/(?P<hash>.*)/$',
        s5012_evtirrf_verificar_views.validar_evento,
        name='s5012_evtirrf_validar_evento'),

url(r'^s5012-evtirrf/salvar/(?P<hash>.*)/$', 
        s5012_evtirrf_views.salvar, 
        name='s5012_evtirrf_salvar'),
        

url(r'^scripts/gerar-identidade/s5012-evtirrf/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        s5012_evtirrf_views.gerar_identidade, 
        name='s5012_evtirrf_gerar_identidade'),





]