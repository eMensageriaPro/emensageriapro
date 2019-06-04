#coding: utf-8
# © 2018 Marcelo Medeiros de Vasconcellos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__credits__ = ["Marcelo Medeiros de Vasconcellos"]
__version__ = "1.0.0"
__maintainer__ = "Marcelo Medeiros de Vasconcellos"
__email__ = "marcelomdevasconcellos@gmail.com"


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.s2299.models import *
from emensageriapro.s2299.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from datetime import datetime
import base64
import os


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


@login_required
def verificar(request, pk, output=None):

    if request.user.has_perm('esocial.can_see_s2299evtDeslig'):
    
        s2299_evtdeslig = get_object_or_404(s2299evtDeslig, id=pk)
        s2299_evtdeslig_lista = s2299evtDeslig.objects.filter(id=pk).all()

        
        s2299_observacoes_lista = s2299observacoes.objects.filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).all()
        s2299_sucessaovinc_lista = s2299sucessaoVinc.objects.filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).all()
        s2299_transftit_lista = s2299transfTit.objects.filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).all()
        s2299_mudancacpf_lista = s2299mudancaCPF.objects.filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).all()
        s2299_verbasresc_lista = s2299verbasResc.objects.filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).all()
        s2299_dmdev_lista = s2299dmDev.objects.filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).all()
        s2299_infoperapur_lista = s2299infoPerApur.objects.filter(s2299_dmdev_id__in = listar_ids(s2299_dmdev_lista) ).all()
        s2299_infoperapur_ideestablot_lista = s2299infoPerApurideEstabLot.objects.filter(s2299_infoperapur_id__in = listar_ids(s2299_infoperapur_lista) ).all()
        s2299_infoperapur_detverbas_lista = s2299infoPerApurdetVerbas.objects.filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).all()
        s2299_infoperapur_infosaudecolet_lista = s2299infoPerApurinfoSaudeColet.objects.filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).all()
        s2299_infoperapur_detoper_lista = s2299infoPerApurdetOper.objects.filter(s2299_infoperapur_infosaudecolet_id__in = listar_ids(s2299_infoperapur_infosaudecolet_lista) ).all()
        s2299_infoperapur_detplano_lista = s2299infoPerApurdetPlano.objects.filter(s2299_infoperapur_detoper_id__in = listar_ids(s2299_infoperapur_detoper_lista) ).all()
        s2299_infoperapur_infoagnocivo_lista = s2299infoPerApurinfoAgNocivo.objects.filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).all()
        s2299_infoperapur_infosimples_lista = s2299infoPerApurinfoSimples.objects.filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).all()
        s2299_infoperant_lista = s2299infoPerAnt.objects.filter(s2299_dmdev_id__in = listar_ids(s2299_dmdev_lista) ).all()
        s2299_infoperant_ideadc_lista = s2299infoPerAntideADC.objects.filter(s2299_infoperant_id__in = listar_ids(s2299_infoperant_lista) ).all()
        s2299_infoperant_ideperiodo_lista = s2299infoPerAntidePeriodo.objects.filter(s2299_infoperant_ideadc_id__in = listar_ids(s2299_infoperant_ideadc_lista) ).all()
        s2299_infoperant_ideestablot_lista = s2299infoPerAntideEstabLot.objects.filter(s2299_infoperant_ideperiodo_id__in = listar_ids(s2299_infoperant_ideperiodo_lista) ).all()
        s2299_infoperant_detverbas_lista = s2299infoPerAntdetVerbas.objects.filter(s2299_infoperant_ideestablot_id__in = listar_ids(s2299_infoperant_ideestablot_lista) ).all()
        s2299_infoperant_infoagnocivo_lista = s2299infoPerAntinfoAgNocivo.objects.filter(s2299_infoperant_ideestablot_id__in = listar_ids(s2299_infoperant_ideestablot_lista) ).all()
        s2299_infoperant_infosimples_lista = s2299infoPerAntinfoSimples.objects.filter(s2299_infoperant_ideestablot_id__in = listar_ids(s2299_infoperant_ideestablot_lista) ).all()
        s2299_infotrabinterm_lista = s2299infoTrabInterm.objects.filter(s2299_dmdev_id__in = listar_ids(s2299_dmdev_lista) ).all()
        s2299_infotrabinterm_procjudtrab_lista = s2299infoTrabIntermprocJudTrab.objects.filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).all()
        s2299_infotrabinterm_infomv_lista = s2299infoTrabInterminfoMV.objects.filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).all()
        s2299_infotrabinterm_remunoutrempr_lista = s2299infoTrabIntermremunOutrEmpr.objects.filter(s2299_infotrabinterm_infomv_id__in = listar_ids(s2299_infotrabinterm_infomv_lista) ).all()
        s2299_infotrabinterm_proccs_lista = s2299infoTrabIntermprocCS.objects.filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).all()
        s2299_infotrabinterm_quarentena_lista = s2299infoTrabIntermquarentena.objects.filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).all()
        s2299_infotrabinterm_consigfgts_lista = s2299infoTrabIntermconsigFGTS.objects.filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).all()

        request.session['return_pk'] = pk
        request.session['return_page'] = 's2299_evtdeslig'

        context = {
            's2299_evtdeslig_lista': s2299_evtdeslig_lista,
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            's2299_evtdeslig': s2299_evtdeslig,
            's2299_observacoes_lista': s2299_observacoes_lista,
            's2299_sucessaovinc_lista': s2299_sucessaovinc_lista,
            's2299_transftit_lista': s2299_transftit_lista,
            's2299_mudancacpf_lista': s2299_mudancacpf_lista,
            's2299_verbasresc_lista': s2299_verbasresc_lista,
            's2299_dmdev_lista': s2299_dmdev_lista,
            's2299_infoperapur_lista': s2299_infoperapur_lista,
            's2299_infoperapur_ideestablot_lista': s2299_infoperapur_ideestablot_lista,
            's2299_infoperapur_detverbas_lista': s2299_infoperapur_detverbas_lista,
            's2299_infoperapur_infosaudecolet_lista': s2299_infoperapur_infosaudecolet_lista,
            's2299_infoperapur_detoper_lista': s2299_infoperapur_detoper_lista,
            's2299_infoperapur_detplano_lista': s2299_infoperapur_detplano_lista,
            's2299_infoperapur_infoagnocivo_lista': s2299_infoperapur_infoagnocivo_lista,
            's2299_infoperapur_infosimples_lista': s2299_infoperapur_infosimples_lista,
            's2299_infoperant_lista': s2299_infoperant_lista,
            's2299_infoperant_ideadc_lista': s2299_infoperant_ideadc_lista,
            's2299_infoperant_ideperiodo_lista': s2299_infoperant_ideperiodo_lista,
            's2299_infoperant_ideestablot_lista': s2299_infoperant_ideestablot_lista,
            's2299_infoperant_detverbas_lista': s2299_infoperant_detverbas_lista,
            's2299_infoperant_infoagnocivo_lista': s2299_infoperant_infoagnocivo_lista,
            's2299_infoperant_infosimples_lista': s2299_infoperant_infosimples_lista,
            's2299_infotrabinterm_lista': s2299_infotrabinterm_lista,
            's2299_infotrabinterm_procjudtrab_lista': s2299_infotrabinterm_procjudtrab_lista,
            's2299_infotrabinterm_infomv_lista': s2299_infotrabinterm_infomv_lista,
            's2299_infotrabinterm_remunoutrempr_lista': s2299_infotrabinterm_remunoutrempr_lista,
            's2299_infotrabinterm_proccs_lista': s2299_infotrabinterm_proccs_lista,
            's2299_infotrabinterm_quarentena_lista': s2299_infotrabinterm_quarentena_lista,
            's2299_infotrabinterm_consigfgts_lista': s2299_infotrabinterm_consigfgts_lista,
            'modulos': ['esocial', ],
            'paginas': ['s2299_evtdeslig', ],
            'data': datetime.now(),
            'output': output,
        }
        
        if output == 'pdf':
        
            response = PDFTemplateResponse(
                request=request,
                template='s2299_evtdeslig_verificar.html',
                filename="s2299_evtdeslig.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 5,
                            'margin-bottom': 5,
                            'margin-right': 5,
                            'margin-left': 5,
                            "zoom": 3,
                            "viewport-size": "1366 x 513",
                            'javascript-delay': 1000,
                            'footer-center': '[page]/[topage]',
                            "no-stop-slow-scripts": True} )
                            
            return response

        elif output == 'xls':
        
            response =  render_to_response('s2299_evtdeslig_verificar.html', context)
            filename = "%s.xls" % s2299_evtdeslig.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response

        elif output == 'csv':
        
            response =  render_to_response('s2299_evtdeslig_verificar.html', context)
            filename = "%s.csv" % s2299_evtdeslig.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:
        
            return render(request, 's2299_evtdeslig_verificar.html', context)

    else:

        context = {
            'modulos': ['esocial', ],
            'paginas': ['s2299_evtdeslig', ],
            'data': datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)