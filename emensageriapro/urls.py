#coding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
admin.autodiscover()

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

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', 
        auth_views.login,
        name='home'),

    url(r'^', include('emensageriapro.controle_de_acesso.urls')),
    url(r'^efdreinf/', include('emensageriapro.efdreinf.urls')),
    url(r'^esocial/', include('emensageriapro.esocial.urls')),
    url(r'^mapa-processamento/', include('emensageriapro.mapa_processamento.urls')),
    url(r'^mensageiro/', include('emensageriapro.mensageiro.urls')),
    url(r'^r1000/', include('emensageriapro.r1000.urls')),
    url(r'^r1070/', include('emensageriapro.r1070.urls')),
    url(r'^r2010/', include('emensageriapro.r2010.urls')),
    url(r'^r2020/', include('emensageriapro.r2020.urls')),
    url(r'^r2030/', include('emensageriapro.r2030.urls')),
    url(r'^r2040/', include('emensageriapro.r2040.urls')),
    url(r'^r2050/', include('emensageriapro.r2050.urls')),
    url(r'^r2060/', include('emensageriapro.r2060.urls')),
    url(r'^r2070/', include('emensageriapro.r2070.urls')),
    url(r'^r2098/', include('emensageriapro.r2098.urls')),
    url(r'^r2099/', include('emensageriapro.r2099.urls')),
    url(r'^r3010/', include('emensageriapro.r3010.urls')),
    url(r'^r4010/', include('emensageriapro.r4010.urls')),
    url(r'^r4020/', include('emensageriapro.r4020.urls')),
    url(r'^r4040/', include('emensageriapro.r4040.urls')),
    url(r'^r4098/', include('emensageriapro.r4098.urls')),
    url(r'^r4099/', include('emensageriapro.r4099.urls')),
    url(r'^r5001/', include('emensageriapro.r5001.urls')),
    url(r'^r5011/', include('emensageriapro.r5011.urls')),
    url(r'^r9000/', include('emensageriapro.r9000.urls')),
    url(r'^r9001/', include('emensageriapro.r9001.urls')),
    url(r'^r9002/', include('emensageriapro.r9002.urls')),
    url(r'^r9011/', include('emensageriapro.r9011.urls')),
    url(r'^r9012/', include('emensageriapro.r9012.urls')),
    url(r'^s1000/', include('emensageriapro.s1000.urls')),
    url(r'^s1005/', include('emensageriapro.s1005.urls')),
    url(r'^s1010/', include('emensageriapro.s1010.urls')),
    url(r'^s1020/', include('emensageriapro.s1020.urls')),
    url(r'^s1030/', include('emensageriapro.s1030.urls')),
    url(r'^s1035/', include('emensageriapro.s1035.urls')),
    url(r'^s1040/', include('emensageriapro.s1040.urls')),
    url(r'^s1050/', include('emensageriapro.s1050.urls')),
    url(r'^s1060/', include('emensageriapro.s1060.urls')),
    url(r'^s1070/', include('emensageriapro.s1070.urls')),
    url(r'^s1080/', include('emensageriapro.s1080.urls')),
    url(r'^s1200/', include('emensageriapro.s1200.urls')),
    url(r'^s1202/', include('emensageriapro.s1202.urls')),
    url(r'^s1207/', include('emensageriapro.s1207.urls')),
    url(r'^s1210/', include('emensageriapro.s1210.urls')),
    url(r'^s1250/', include('emensageriapro.s1250.urls')),
    url(r'^s1260/', include('emensageriapro.s1260.urls')),
    url(r'^s1270/', include('emensageriapro.s1270.urls')),
    url(r'^s1280/', include('emensageriapro.s1280.urls')),
    url(r'^s1295/', include('emensageriapro.s1295.urls')),
    url(r'^s1298/', include('emensageriapro.s1298.urls')),
    url(r'^s1299/', include('emensageriapro.s1299.urls')),
    url(r'^s1300/', include('emensageriapro.s1300.urls')),
    url(r'^s2190/', include('emensageriapro.s2190.urls')),
    url(r'^s2200/', include('emensageriapro.s2200.urls')),
    url(r'^s2205/', include('emensageriapro.s2205.urls')),
    url(r'^s2206/', include('emensageriapro.s2206.urls')),
    url(r'^s2210/', include('emensageriapro.s2210.urls')),
    url(r'^s2220/', include('emensageriapro.s2220.urls')),
    url(r'^s2221/', include('emensageriapro.s2221.urls')),
    url(r'^s2230/', include('emensageriapro.s2230.urls')),
    url(r'^s2231/', include('emensageriapro.s2231.urls')),
    url(r'^s2240/', include('emensageriapro.s2240.urls')),
    url(r'^s2241/', include('emensageriapro.s2241.urls')),
    url(r'^s2245/', include('emensageriapro.s2245.urls')),
    url(r'^s2250/', include('emensageriapro.s2250.urls')),
    url(r'^s2260/', include('emensageriapro.s2260.urls')),
    url(r'^s2298/', include('emensageriapro.s2298.urls')),
    url(r'^s2299/', include('emensageriapro.s2299.urls')),
    url(r'^s2300/', include('emensageriapro.s2300.urls')),
    url(r'^s2306/', include('emensageriapro.s2306.urls')),
    url(r'^s2399/', include('emensageriapro.s2399.urls')),
    url(r'^s2400/', include('emensageriapro.s2400.urls')),
    url(r'^s2405/', include('emensageriapro.s2405.urls')),
    url(r'^s2410/', include('emensageriapro.s2410.urls')),
    url(r'^s2416/', include('emensageriapro.s2416.urls')),
    url(r'^s2420/', include('emensageriapro.s2420.urls')),
    url(r'^s3000/', include('emensageriapro.s3000.urls')),
    url(r'^s5001/', include('emensageriapro.s5001.urls')),
    url(r'^s5002/', include('emensageriapro.s5002.urls')),
    url(r'^s5003/', include('emensageriapro.s5003.urls')),
    url(r'^s5011/', include('emensageriapro.s5011.urls')),
    url(r'^s5012/', include('emensageriapro.s5012.urls')),
    url(r'^s5013/', include('emensageriapro.s5013.urls')),
    url(r'^tabelas/', include('emensageriapro.tabelas.urls')),

    url(r'^admin/', include(admin.site.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = _(u"Administração eMensageria")
admin.site.site_title = _(u"Administração eMensageria")
admin.site.index_title = _(u"Administração eMensageria")