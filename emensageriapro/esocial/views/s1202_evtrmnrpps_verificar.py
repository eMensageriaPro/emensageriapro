# eMensageriaAI #
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
from emensageriapro.s1202.models import *
from emensageriapro.s1202.forms import *
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

    if request.user.has_perm('esocial.can_see_s1202evtRmnRPPS'):

        s1202_evtrmnrpps = get_object_or_404(s1202evtRmnRPPS, id=pk)
        s1202_evtrmnrpps_lista = s1202evtRmnRPPS.objects.filter(id=pk).all()


        s1202_procjudtrab_lista = s1202procJudTrab.objects.filter(s1202_evtrmnrpps_id__in = listar_ids(s1202_evtrmnrpps_lista) ).all()
        s1202_dmdev_lista = s1202dmDev.objects.filter(s1202_evtrmnrpps_id__in = listar_ids(s1202_evtrmnrpps_lista) ).all()
        s1202_infoperapur_lista = s1202infoPerApur.objects.filter(s1202_dmdev_id__in = listar_ids(s1202_dmdev_lista) ).all()
        s1202_infoperapur_ideestab_lista = s1202infoPerApurideEstab.objects.filter(s1202_infoperapur_id__in = listar_ids(s1202_infoperapur_lista) ).all()
        s1202_infoperapur_remunperapur_lista = s1202infoPerApurremunPerApur.objects.filter(s1202_infoperapur_ideestab_id__in = listar_ids(s1202_infoperapur_ideestab_lista) ).all()
        s1202_infoperapur_itensremun_lista = s1202infoPerApuritensRemun.objects.filter(s1202_infoperapur_remunperapur_id__in = listar_ids(s1202_infoperapur_remunperapur_lista) ).all()
        s1202_infoperapur_infosaudecolet_lista = s1202infoPerApurinfoSaudeColet.objects.filter(s1202_infoperapur_remunperapur_id__in = listar_ids(s1202_infoperapur_remunperapur_lista) ).all()
        s1202_infoperapur_detoper_lista = s1202infoPerApurdetOper.objects.filter(s1202_infoperapur_infosaudecolet_id__in = listar_ids(s1202_infoperapur_infosaudecolet_lista) ).all()
        s1202_infoperapur_detplano_lista = s1202infoPerApurdetPlano.objects.filter(s1202_infoperapur_detoper_id__in = listar_ids(s1202_infoperapur_detoper_lista) ).all()
        s1202_infoperant_lista = s1202infoPerAnt.objects.filter(s1202_dmdev_id__in = listar_ids(s1202_dmdev_lista) ).all()
        s1202_infoperant_ideadc_lista = s1202infoPerAntideADC.objects.filter(s1202_infoperant_id__in = listar_ids(s1202_infoperant_lista) ).all()
        s1202_infoperant_ideperiodo_lista = s1202infoPerAntidePeriodo.objects.filter(s1202_infoperant_ideadc_id__in = listar_ids(s1202_infoperant_ideadc_lista) ).all()
        s1202_infoperant_ideestab_lista = s1202infoPerAntideEstab.objects.filter(s1202_infoperant_ideperiodo_id__in = listar_ids(s1202_infoperant_ideperiodo_lista) ).all()
        s1202_infoperant_remunperant_lista = s1202infoPerAntremunPerAnt.objects.filter(s1202_infoperant_ideestab_id__in = listar_ids(s1202_infoperant_ideestab_lista) ).all()
        s1202_infoperant_itensremun_lista = s1202infoPerAntitensRemun.objects.filter(s1202_infoperant_remunperant_id__in = listar_ids(s1202_infoperant_remunperant_lista) ).all()

        request.session['return_pk'] = pk
        request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            's1202_evtrmnrpps_lista': s1202_evtrmnrpps_lista,
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            's1202_evtrmnrpps': s1202_evtrmnrpps,
            's1202_procjudtrab_lista': s1202_procjudtrab_lista,
            's1202_dmdev_lista': s1202_dmdev_lista,
            's1202_infoperapur_lista': s1202_infoperapur_lista,
            's1202_infoperapur_ideestab_lista': s1202_infoperapur_ideestab_lista,
            's1202_infoperapur_remunperapur_lista': s1202_infoperapur_remunperapur_lista,
            's1202_infoperapur_itensremun_lista': s1202_infoperapur_itensremun_lista,
            's1202_infoperapur_infosaudecolet_lista': s1202_infoperapur_infosaudecolet_lista,
            's1202_infoperapur_detoper_lista': s1202_infoperapur_detoper_lista,
            's1202_infoperapur_detplano_lista': s1202_infoperapur_detplano_lista,
            's1202_infoperant_lista': s1202_infoperant_lista,
            's1202_infoperant_ideadc_lista': s1202_infoperant_ideadc_lista,
            's1202_infoperant_ideperiodo_lista': s1202_infoperant_ideperiodo_lista,
            's1202_infoperant_ideestab_lista': s1202_infoperant_ideestab_lista,
            's1202_infoperant_remunperant_lista': s1202_infoperant_remunperant_lista,
            's1202_infoperant_itensremun_lista': s1202_infoperant_itensremun_lista,
            'modulos': ['esocial', ],
            'paginas': ['s1202_evtrmnrpps', ],
            'data': datetime.now(),
            'output': output,
        }

        if output == 'pdf':

            response = PDFTemplateResponse(
                request=request,
                template='s1202_evtrmnrpps_verificar.html',
                filename="s1202_evtrmnrpps.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 20,
                             'zoom': 1,
                             'viewport-size': '1366 x 513',
                             'javascript-delay': 1000,
                             'footer-center': u'Página [page]/[topage]',
                             'footer-font-size': 10,
                             'no-stop-slow-scripts': True})
        
            return response

        elif output == 'xls':

            response = render_to_response('s1202_evtrmnrpps_verificar.html', context)
            filename = "%s.xls" % s1202_evtrmnrpps.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        elif output == 'csv':

            response = render_to_response('s1202_evtrmnrpps_verificar.html', context)
            filename = "%s.csv" % s1202_evtrmnrpps.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:

            return render(request, 's1202_evtrmnrpps_verificar.html', context)

    else:

        context = {
            'modulos': ['esocial', ],
            'paginas': ['s1202_evtrmnrpps', ],
            'data': datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)