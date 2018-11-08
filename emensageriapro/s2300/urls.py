#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s2300.views import s2300_documentos as s2300_documentos_views
from emensageriapro.s2300.views import s2300_ctps as s2300_ctps_views
from emensageriapro.s2300.views import s2300_ric as s2300_ric_views
from emensageriapro.s2300.views import s2300_rg as s2300_rg_views
from emensageriapro.s2300.views import s2300_rne as s2300_rne_views
from emensageriapro.s2300.views import s2300_oc as s2300_oc_views
from emensageriapro.s2300.views import s2300_cnh as s2300_cnh_views
from emensageriapro.s2300.views import s2300_brasil as s2300_brasil_views
from emensageriapro.s2300.views import s2300_exterior as s2300_exterior_views
from emensageriapro.s2300.views import s2300_trabestrangeiro as s2300_trabestrangeiro_views
from emensageriapro.s2300.views import s2300_infodeficiencia as s2300_infodeficiencia_views
from emensageriapro.s2300.views import s2300_dependente as s2300_dependente_views
from emensageriapro.s2300.views import s2300_contato as s2300_contato_views
from emensageriapro.s2300.views import s2300_infocomplementares as s2300_infocomplementares_views
from emensageriapro.s2300.views import s2300_cargofuncao as s2300_cargofuncao_views
from emensageriapro.s2300.views import s2300_remuneracao as s2300_remuneracao_views
from emensageriapro.s2300.views import s2300_fgts as s2300_fgts_views
from emensageriapro.s2300.views import s2300_infodirigentesindical as s2300_infodirigentesindical_views
from emensageriapro.s2300.views import s2300_infotrabcedido as s2300_infotrabcedido_views
from emensageriapro.s2300.views import s2300_infoestagiario as s2300_infoestagiario_views
from emensageriapro.s2300.views import s2300_ageintegracao as s2300_ageintegracao_views
from emensageriapro.s2300.views import s2300_supervisorestagio as s2300_supervisorestagio_views
from emensageriapro.s2300.views import s2300_afastamento as s2300_afastamento_views
from emensageriapro.s2300.views import s2300_termino as s2300_termino_views





urlpatterns = [



url(r'^s2300-documentos/apagar/(?P<hash>.*)/$', 
        s2300_documentos_views.apagar, 
        name='s2300_documentos_apagar'),

url(r'^s2300-documentos/api/$',
            s2300_documentos_views.s2300documentosList.as_view() ),

        url(r'^s2300-documentos/api/(?P<pk>[0-9]+)/$',
            s2300_documentos_views.s2300documentosDetail.as_view() ),

url(r'^s2300-documentos/listar/(?P<hash>.*)/$', 
        s2300_documentos_views.listar, 
        name='s2300_documentos'),

url(r'^s2300-documentos/salvar/(?P<hash>.*)/$', 
        s2300_documentos_views.salvar, 
        name='s2300_documentos_salvar'),



url(r'^s2300-ctps/apagar/(?P<hash>.*)/$', 
        s2300_ctps_views.apagar, 
        name='s2300_ctps_apagar'),

url(r'^s2300-ctps/api/$',
            s2300_ctps_views.s2300CTPSList.as_view() ),

        url(r'^s2300-ctps/api/(?P<pk>[0-9]+)/$',
            s2300_ctps_views.s2300CTPSDetail.as_view() ),

url(r'^s2300-ctps/listar/(?P<hash>.*)/$', 
        s2300_ctps_views.listar, 
        name='s2300_ctps'),

url(r'^s2300-ctps/salvar/(?P<hash>.*)/$', 
        s2300_ctps_views.salvar, 
        name='s2300_ctps_salvar'),



url(r'^s2300-ric/apagar/(?P<hash>.*)/$', 
        s2300_ric_views.apagar, 
        name='s2300_ric_apagar'),

url(r'^s2300-ric/api/$',
            s2300_ric_views.s2300RICList.as_view() ),

        url(r'^s2300-ric/api/(?P<pk>[0-9]+)/$',
            s2300_ric_views.s2300RICDetail.as_view() ),

url(r'^s2300-ric/listar/(?P<hash>.*)/$', 
        s2300_ric_views.listar, 
        name='s2300_ric'),

url(r'^s2300-ric/salvar/(?P<hash>.*)/$', 
        s2300_ric_views.salvar, 
        name='s2300_ric_salvar'),



url(r'^s2300-rg/apagar/(?P<hash>.*)/$', 
        s2300_rg_views.apagar, 
        name='s2300_rg_apagar'),

url(r'^s2300-rg/api/$',
            s2300_rg_views.s2300RGList.as_view() ),

        url(r'^s2300-rg/api/(?P<pk>[0-9]+)/$',
            s2300_rg_views.s2300RGDetail.as_view() ),

url(r'^s2300-rg/listar/(?P<hash>.*)/$', 
        s2300_rg_views.listar, 
        name='s2300_rg'),

url(r'^s2300-rg/salvar/(?P<hash>.*)/$', 
        s2300_rg_views.salvar, 
        name='s2300_rg_salvar'),



url(r'^s2300-rne/apagar/(?P<hash>.*)/$', 
        s2300_rne_views.apagar, 
        name='s2300_rne_apagar'),

url(r'^s2300-rne/api/$',
            s2300_rne_views.s2300RNEList.as_view() ),

        url(r'^s2300-rne/api/(?P<pk>[0-9]+)/$',
            s2300_rne_views.s2300RNEDetail.as_view() ),

url(r'^s2300-rne/listar/(?P<hash>.*)/$', 
        s2300_rne_views.listar, 
        name='s2300_rne'),

url(r'^s2300-rne/salvar/(?P<hash>.*)/$', 
        s2300_rne_views.salvar, 
        name='s2300_rne_salvar'),



url(r'^s2300-oc/apagar/(?P<hash>.*)/$', 
        s2300_oc_views.apagar, 
        name='s2300_oc_apagar'),

url(r'^s2300-oc/api/$',
            s2300_oc_views.s2300OCList.as_view() ),

        url(r'^s2300-oc/api/(?P<pk>[0-9]+)/$',
            s2300_oc_views.s2300OCDetail.as_view() ),

url(r'^s2300-oc/listar/(?P<hash>.*)/$', 
        s2300_oc_views.listar, 
        name='s2300_oc'),

url(r'^s2300-oc/salvar/(?P<hash>.*)/$', 
        s2300_oc_views.salvar, 
        name='s2300_oc_salvar'),



url(r'^s2300-cnh/apagar/(?P<hash>.*)/$', 
        s2300_cnh_views.apagar, 
        name='s2300_cnh_apagar'),

url(r'^s2300-cnh/api/$',
            s2300_cnh_views.s2300CNHList.as_view() ),

        url(r'^s2300-cnh/api/(?P<pk>[0-9]+)/$',
            s2300_cnh_views.s2300CNHDetail.as_view() ),

url(r'^s2300-cnh/listar/(?P<hash>.*)/$', 
        s2300_cnh_views.listar, 
        name='s2300_cnh'),

url(r'^s2300-cnh/salvar/(?P<hash>.*)/$', 
        s2300_cnh_views.salvar, 
        name='s2300_cnh_salvar'),



url(r'^s2300-brasil/apagar/(?P<hash>.*)/$', 
        s2300_brasil_views.apagar, 
        name='s2300_brasil_apagar'),

url(r'^s2300-brasil/api/$',
            s2300_brasil_views.s2300brasilList.as_view() ),

        url(r'^s2300-brasil/api/(?P<pk>[0-9]+)/$',
            s2300_brasil_views.s2300brasilDetail.as_view() ),

url(r'^s2300-brasil/listar/(?P<hash>.*)/$', 
        s2300_brasil_views.listar, 
        name='s2300_brasil'),

url(r'^s2300-brasil/salvar/(?P<hash>.*)/$', 
        s2300_brasil_views.salvar, 
        name='s2300_brasil_salvar'),



url(r'^s2300-exterior/apagar/(?P<hash>.*)/$', 
        s2300_exterior_views.apagar, 
        name='s2300_exterior_apagar'),

url(r'^s2300-exterior/api/$',
            s2300_exterior_views.s2300exteriorList.as_view() ),

        url(r'^s2300-exterior/api/(?P<pk>[0-9]+)/$',
            s2300_exterior_views.s2300exteriorDetail.as_view() ),

url(r'^s2300-exterior/listar/(?P<hash>.*)/$', 
        s2300_exterior_views.listar, 
        name='s2300_exterior'),

url(r'^s2300-exterior/salvar/(?P<hash>.*)/$', 
        s2300_exterior_views.salvar, 
        name='s2300_exterior_salvar'),



url(r'^s2300-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        s2300_trabestrangeiro_views.apagar, 
        name='s2300_trabestrangeiro_apagar'),

url(r'^s2300-trabestrangeiro/api/$',
            s2300_trabestrangeiro_views.s2300trabEstrangeiroList.as_view() ),

        url(r'^s2300-trabestrangeiro/api/(?P<pk>[0-9]+)/$',
            s2300_trabestrangeiro_views.s2300trabEstrangeiroDetail.as_view() ),

url(r'^s2300-trabestrangeiro/listar/(?P<hash>.*)/$', 
        s2300_trabestrangeiro_views.listar, 
        name='s2300_trabestrangeiro'),

url(r'^s2300-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        s2300_trabestrangeiro_views.salvar, 
        name='s2300_trabestrangeiro_salvar'),



url(r'^s2300-infodeficiencia/apagar/(?P<hash>.*)/$', 
        s2300_infodeficiencia_views.apagar, 
        name='s2300_infodeficiencia_apagar'),

url(r'^s2300-infodeficiencia/api/$',
            s2300_infodeficiencia_views.s2300infoDeficienciaList.as_view() ),

        url(r'^s2300-infodeficiencia/api/(?P<pk>[0-9]+)/$',
            s2300_infodeficiencia_views.s2300infoDeficienciaDetail.as_view() ),

url(r'^s2300-infodeficiencia/listar/(?P<hash>.*)/$', 
        s2300_infodeficiencia_views.listar, 
        name='s2300_infodeficiencia'),

url(r'^s2300-infodeficiencia/salvar/(?P<hash>.*)/$', 
        s2300_infodeficiencia_views.salvar, 
        name='s2300_infodeficiencia_salvar'),



url(r'^s2300-dependente/apagar/(?P<hash>.*)/$', 
        s2300_dependente_views.apagar, 
        name='s2300_dependente_apagar'),

url(r'^s2300-dependente/api/$',
            s2300_dependente_views.s2300dependenteList.as_view() ),

        url(r'^s2300-dependente/api/(?P<pk>[0-9]+)/$',
            s2300_dependente_views.s2300dependenteDetail.as_view() ),

url(r'^s2300-dependente/listar/(?P<hash>.*)/$', 
        s2300_dependente_views.listar, 
        name='s2300_dependente'),

url(r'^s2300-dependente/salvar/(?P<hash>.*)/$', 
        s2300_dependente_views.salvar, 
        name='s2300_dependente_salvar'),



url(r'^s2300-contato/apagar/(?P<hash>.*)/$', 
        s2300_contato_views.apagar, 
        name='s2300_contato_apagar'),

url(r'^s2300-contato/api/$',
            s2300_contato_views.s2300contatoList.as_view() ),

        url(r'^s2300-contato/api/(?P<pk>[0-9]+)/$',
            s2300_contato_views.s2300contatoDetail.as_view() ),

url(r'^s2300-contato/listar/(?P<hash>.*)/$', 
        s2300_contato_views.listar, 
        name='s2300_contato'),

url(r'^s2300-contato/salvar/(?P<hash>.*)/$', 
        s2300_contato_views.salvar, 
        name='s2300_contato_salvar'),



url(r'^s2300-infocomplementares/apagar/(?P<hash>.*)/$', 
        s2300_infocomplementares_views.apagar, 
        name='s2300_infocomplementares_apagar'),

url(r'^s2300-infocomplementares/api/$',
            s2300_infocomplementares_views.s2300infoComplementaresList.as_view() ),

        url(r'^s2300-infocomplementares/api/(?P<pk>[0-9]+)/$',
            s2300_infocomplementares_views.s2300infoComplementaresDetail.as_view() ),

url(r'^s2300-infocomplementares/listar/(?P<hash>.*)/$', 
        s2300_infocomplementares_views.listar, 
        name='s2300_infocomplementares'),

url(r'^s2300-infocomplementares/salvar/(?P<hash>.*)/$', 
        s2300_infocomplementares_views.salvar, 
        name='s2300_infocomplementares_salvar'),



url(r'^s2300-cargofuncao/apagar/(?P<hash>.*)/$', 
        s2300_cargofuncao_views.apagar, 
        name='s2300_cargofuncao_apagar'),

url(r'^s2300-cargofuncao/api/$',
            s2300_cargofuncao_views.s2300cargoFuncaoList.as_view() ),

        url(r'^s2300-cargofuncao/api/(?P<pk>[0-9]+)/$',
            s2300_cargofuncao_views.s2300cargoFuncaoDetail.as_view() ),

url(r'^s2300-cargofuncao/listar/(?P<hash>.*)/$', 
        s2300_cargofuncao_views.listar, 
        name='s2300_cargofuncao'),

url(r'^s2300-cargofuncao/salvar/(?P<hash>.*)/$', 
        s2300_cargofuncao_views.salvar, 
        name='s2300_cargofuncao_salvar'),



url(r'^s2300-remuneracao/apagar/(?P<hash>.*)/$', 
        s2300_remuneracao_views.apagar, 
        name='s2300_remuneracao_apagar'),

url(r'^s2300-remuneracao/api/$',
            s2300_remuneracao_views.s2300remuneracaoList.as_view() ),

        url(r'^s2300-remuneracao/api/(?P<pk>[0-9]+)/$',
            s2300_remuneracao_views.s2300remuneracaoDetail.as_view() ),

url(r'^s2300-remuneracao/listar/(?P<hash>.*)/$', 
        s2300_remuneracao_views.listar, 
        name='s2300_remuneracao'),

url(r'^s2300-remuneracao/salvar/(?P<hash>.*)/$', 
        s2300_remuneracao_views.salvar, 
        name='s2300_remuneracao_salvar'),



url(r'^s2300-fgts/apagar/(?P<hash>.*)/$', 
        s2300_fgts_views.apagar, 
        name='s2300_fgts_apagar'),

url(r'^s2300-fgts/api/$',
            s2300_fgts_views.s2300fgtsList.as_view() ),

        url(r'^s2300-fgts/api/(?P<pk>[0-9]+)/$',
            s2300_fgts_views.s2300fgtsDetail.as_view() ),

url(r'^s2300-fgts/listar/(?P<hash>.*)/$', 
        s2300_fgts_views.listar, 
        name='s2300_fgts'),

url(r'^s2300-fgts/salvar/(?P<hash>.*)/$', 
        s2300_fgts_views.salvar, 
        name='s2300_fgts_salvar'),



url(r'^s2300-infodirigentesindical/apagar/(?P<hash>.*)/$', 
        s2300_infodirigentesindical_views.apagar, 
        name='s2300_infodirigentesindical_apagar'),

url(r'^s2300-infodirigentesindical/api/$',
            s2300_infodirigentesindical_views.s2300infoDirigenteSindicalList.as_view() ),

        url(r'^s2300-infodirigentesindical/api/(?P<pk>[0-9]+)/$',
            s2300_infodirigentesindical_views.s2300infoDirigenteSindicalDetail.as_view() ),

url(r'^s2300-infodirigentesindical/listar/(?P<hash>.*)/$', 
        s2300_infodirigentesindical_views.listar, 
        name='s2300_infodirigentesindical'),

url(r'^s2300-infodirigentesindical/salvar/(?P<hash>.*)/$', 
        s2300_infodirigentesindical_views.salvar, 
        name='s2300_infodirigentesindical_salvar'),



url(r'^s2300-infotrabcedido/apagar/(?P<hash>.*)/$', 
        s2300_infotrabcedido_views.apagar, 
        name='s2300_infotrabcedido_apagar'),

url(r'^s2300-infotrabcedido/api/$',
            s2300_infotrabcedido_views.s2300infoTrabCedidoList.as_view() ),

        url(r'^s2300-infotrabcedido/api/(?P<pk>[0-9]+)/$',
            s2300_infotrabcedido_views.s2300infoTrabCedidoDetail.as_view() ),

url(r'^s2300-infotrabcedido/listar/(?P<hash>.*)/$', 
        s2300_infotrabcedido_views.listar, 
        name='s2300_infotrabcedido'),

url(r'^s2300-infotrabcedido/salvar/(?P<hash>.*)/$', 
        s2300_infotrabcedido_views.salvar, 
        name='s2300_infotrabcedido_salvar'),



url(r'^s2300-infoestagiario/apagar/(?P<hash>.*)/$', 
        s2300_infoestagiario_views.apagar, 
        name='s2300_infoestagiario_apagar'),

url(r'^s2300-infoestagiario/api/$',
            s2300_infoestagiario_views.s2300infoEstagiarioList.as_view() ),

        url(r'^s2300-infoestagiario/api/(?P<pk>[0-9]+)/$',
            s2300_infoestagiario_views.s2300infoEstagiarioDetail.as_view() ),

url(r'^s2300-infoestagiario/listar/(?P<hash>.*)/$', 
        s2300_infoestagiario_views.listar, 
        name='s2300_infoestagiario'),

url(r'^s2300-infoestagiario/salvar/(?P<hash>.*)/$', 
        s2300_infoestagiario_views.salvar, 
        name='s2300_infoestagiario_salvar'),



url(r'^s2300-ageintegracao/apagar/(?P<hash>.*)/$', 
        s2300_ageintegracao_views.apagar, 
        name='s2300_ageintegracao_apagar'),

url(r'^s2300-ageintegracao/api/$',
            s2300_ageintegracao_views.s2300ageIntegracaoList.as_view() ),

        url(r'^s2300-ageintegracao/api/(?P<pk>[0-9]+)/$',
            s2300_ageintegracao_views.s2300ageIntegracaoDetail.as_view() ),

url(r'^s2300-ageintegracao/listar/(?P<hash>.*)/$', 
        s2300_ageintegracao_views.listar, 
        name='s2300_ageintegracao'),

url(r'^s2300-ageintegracao/salvar/(?P<hash>.*)/$', 
        s2300_ageintegracao_views.salvar, 
        name='s2300_ageintegracao_salvar'),



url(r'^s2300-supervisorestagio/apagar/(?P<hash>.*)/$', 
        s2300_supervisorestagio_views.apagar, 
        name='s2300_supervisorestagio_apagar'),

url(r'^s2300-supervisorestagio/api/$',
            s2300_supervisorestagio_views.s2300supervisorEstagioList.as_view() ),

        url(r'^s2300-supervisorestagio/api/(?P<pk>[0-9]+)/$',
            s2300_supervisorestagio_views.s2300supervisorEstagioDetail.as_view() ),

url(r'^s2300-supervisorestagio/listar/(?P<hash>.*)/$', 
        s2300_supervisorestagio_views.listar, 
        name='s2300_supervisorestagio'),

url(r'^s2300-supervisorestagio/salvar/(?P<hash>.*)/$', 
        s2300_supervisorestagio_views.salvar, 
        name='s2300_supervisorestagio_salvar'),



url(r'^s2300-afastamento/apagar/(?P<hash>.*)/$', 
        s2300_afastamento_views.apagar, 
        name='s2300_afastamento_apagar'),

url(r'^s2300-afastamento/api/$',
            s2300_afastamento_views.s2300afastamentoList.as_view() ),

        url(r'^s2300-afastamento/api/(?P<pk>[0-9]+)/$',
            s2300_afastamento_views.s2300afastamentoDetail.as_view() ),

url(r'^s2300-afastamento/listar/(?P<hash>.*)/$', 
        s2300_afastamento_views.listar, 
        name='s2300_afastamento'),

url(r'^s2300-afastamento/salvar/(?P<hash>.*)/$', 
        s2300_afastamento_views.salvar, 
        name='s2300_afastamento_salvar'),



url(r'^s2300-termino/apagar/(?P<hash>.*)/$', 
        s2300_termino_views.apagar, 
        name='s2300_termino_apagar'),

url(r'^s2300-termino/api/$',
            s2300_termino_views.s2300terminoList.as_view() ),

        url(r'^s2300-termino/api/(?P<pk>[0-9]+)/$',
            s2300_termino_views.s2300terminoDetail.as_view() ),

url(r'^s2300-termino/listar/(?P<hash>.*)/$', 
        s2300_termino_views.listar, 
        name='s2300_termino'),

url(r'^s2300-termino/salvar/(?P<hash>.*)/$', 
        s2300_termino_views.salvar, 
        name='s2300_termino_salvar'),





]