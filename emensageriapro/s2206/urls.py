#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s2206-infoceletista/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_infoceletista.apagar', 
        name='s2206_infoceletista_apagar'),

url(r'^s2206-infoceletista/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_infoceletista.listar', 
        name='s2206_infoceletista'),

url(r'^s2206-infoceletista/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_infoceletista.salvar', 
        name='s2206_infoceletista_salvar'),



url(r'^s2206-trabtemp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_trabtemp.apagar', 
        name='s2206_trabtemp_apagar'),

url(r'^s2206-trabtemp/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_trabtemp.listar', 
        name='s2206_trabtemp'),

url(r'^s2206-trabtemp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_trabtemp.salvar', 
        name='s2206_trabtemp_salvar'),



url(r'^s2206-aprend/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_aprend.apagar', 
        name='s2206_aprend_apagar'),

url(r'^s2206-aprend/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_aprend.listar', 
        name='s2206_aprend'),

url(r'^s2206-aprend/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_aprend.salvar', 
        name='s2206_aprend_salvar'),



url(r'^s2206-infoestatutario/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_infoestatutario.apagar', 
        name='s2206_infoestatutario_apagar'),

url(r'^s2206-infoestatutario/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_infoestatutario.listar', 
        name='s2206_infoestatutario'),

url(r'^s2206-infoestatutario/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_infoestatutario.salvar', 
        name='s2206_infoestatutario_salvar'),



url(r'^s2206-localtrabgeral/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_localtrabgeral.apagar', 
        name='s2206_localtrabgeral_apagar'),

url(r'^s2206-localtrabgeral/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_localtrabgeral.listar', 
        name='s2206_localtrabgeral'),

url(r'^s2206-localtrabgeral/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_localtrabgeral.salvar', 
        name='s2206_localtrabgeral_salvar'),



url(r'^s2206-localtrabdom/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_localtrabdom.apagar', 
        name='s2206_localtrabdom_apagar'),

url(r'^s2206-localtrabdom/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_localtrabdom.listar', 
        name='s2206_localtrabdom'),

url(r'^s2206-localtrabdom/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_localtrabdom.salvar', 
        name='s2206_localtrabdom_salvar'),



url(r'^s2206-horcontratual/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_horcontratual.apagar', 
        name='s2206_horcontratual_apagar'),

url(r'^s2206-horcontratual/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_horcontratual.listar', 
        name='s2206_horcontratual'),

url(r'^s2206-horcontratual/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_horcontratual.salvar', 
        name='s2206_horcontratual_salvar'),



url(r'^s2206-horario/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_horario.apagar', 
        name='s2206_horario_apagar'),

url(r'^s2206-horario/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_horario.listar', 
        name='s2206_horario'),

url(r'^s2206-horario/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_horario.salvar', 
        name='s2206_horario_salvar'),



url(r'^s2206-filiacaosindical/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_filiacaosindical.apagar', 
        name='s2206_filiacaosindical_apagar'),

url(r'^s2206-filiacaosindical/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_filiacaosindical.listar', 
        name='s2206_filiacaosindical'),

url(r'^s2206-filiacaosindical/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_filiacaosindical.salvar', 
        name='s2206_filiacaosindical_salvar'),



url(r'^s2206-alvarajudicial/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_alvarajudicial.apagar', 
        name='s2206_alvarajudicial_apagar'),

url(r'^s2206-alvarajudicial/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_alvarajudicial.listar', 
        name='s2206_alvarajudicial'),

url(r'^s2206-alvarajudicial/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_alvarajudicial.salvar', 
        name='s2206_alvarajudicial_salvar'),

)


urlpatterns += patterns('',


url(r'^s2206-observacoes/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_observacoes.apagar', 
        name='s2206_observacoes_apagar'),

url(r'^s2206-observacoes/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_observacoes.listar', 
        name='s2206_observacoes'),

url(r'^s2206-observacoes/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_observacoes.salvar', 
        name='s2206_observacoes_salvar'),



url(r'^s2206-servpubl/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_servpubl.apagar', 
        name='s2206_servpubl_apagar'),

url(r'^s2206-servpubl/listar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_servpubl.listar', 
        name='s2206_servpubl'),

url(r'^s2206-servpubl/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s2206.views.s2206_servpubl.salvar', 
        name='s2206_servpubl_salvar'),





)