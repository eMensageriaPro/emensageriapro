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


import os
import base64
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.r2099.models import *
from emensageriapro.r2099.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse


from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



@login_required
def recibo(request, pk, output=None):

    from datetime import datetime
    from emensageriapro.efdreinf.models import r5001evtTotal
    from emensageriapro.efdreinf.models import r5011evtTotalContrib

    if request.user.has_perm('efdreinf.can_see_r2099evtFechaEvPer'):

        r2099_evtfechaevper = get_object_or_404(
            r2099evtFechaEvPer,
            id=pk)

        if r2099_evtfechaevper.retornos_r5001_id:
            r5001_evttotal = get_object_or_404(r5001evtTotal,
                id=r2099_evtfechaevper.retornos_r5001_id)
        else:
            r5001_evttotal = None

        if r2099_evtfechaevper.retornos_r5011_id:
            r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib,
                id=r2099_evtfechaevper.retornos_r5011_id)
        else:
            r5011_evttotalcontrib = None

        context = {
            'pk': pk,
            'r2099_evtfechaevper': r2099_evtfechaevper,
            'r5001_evttotal': r5001_evttotal,
            'r5011_evttotalcontrib': r5011_evttotalcontrib,
            'data': datetime.now(),
            'output': output,
            'user': request.user,
        }

        if output == 'xls':

            response =  render_to_response('r2099_evtfechaevper_recibo_pdf.html', context)
            filename = "%s.xls" % r2099_evtfechaevper.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        elif output == 'csv':

            response =  render_to_response('r2099_evtfechaevper_recibo_csv.html', context)
            filename = "%s.csv" % r2099_evtfechaevper.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'

            return response

        elif output == 'pdf':

            return render_to_pdf('r2099_evtfechaevper_recibo_pdf.html', context)

        else:

            return render(request, 'r2099_evtfechaevper_recibo_pdf.html', context)

    else:

        context = {
            'data': datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)