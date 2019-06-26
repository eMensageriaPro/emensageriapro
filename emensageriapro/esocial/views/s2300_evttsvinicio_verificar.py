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
from emensageriapro.s2300.models import *
from emensageriapro.s2300.forms import *
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

    if request.user.has_perm('esocial.can_see_s2300evtTSVInicio'):

        s2300_evttsvinicio = get_object_or_404(s2300evtTSVInicio, id=pk)
        s2300_evttsvinicio_lista = s2300evtTSVInicio.objects.filter(id=pk).all()


        s2300_documentos_lista = s2300documentos.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_ctps_lista = s2300CTPS.objects.filter(s2300_documentos_id__in = listar_ids(s2300_documentos_lista) ).all()
        s2300_ric_lista = s2300RIC.objects.filter(s2300_documentos_id__in = listar_ids(s2300_documentos_lista) ).all()
        s2300_rg_lista = s2300RG.objects.filter(s2300_documentos_id__in = listar_ids(s2300_documentos_lista) ).all()
        s2300_rne_lista = s2300RNE.objects.filter(s2300_documentos_id__in = listar_ids(s2300_documentos_lista) ).all()
        s2300_oc_lista = s2300OC.objects.filter(s2300_documentos_id__in = listar_ids(s2300_documentos_lista) ).all()
        s2300_cnh_lista = s2300CNH.objects.filter(s2300_documentos_id__in = listar_ids(s2300_documentos_lista) ).all()
        s2300_brasil_lista = s2300brasil.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_exterior_lista = s2300exterior.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_trabestrangeiro_lista = s2300trabEstrangeiro.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_infodeficiencia_lista = s2300infoDeficiencia.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_dependente_lista = s2300dependente.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_contato_lista = s2300contato.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_infocomplementares_lista = s2300infoComplementares.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_cargofuncao_lista = s2300cargoFuncao.objects.filter(s2300_infocomplementares_id__in = listar_ids(s2300_infocomplementares_lista) ).all()
        s2300_remuneracao_lista = s2300remuneracao.objects.filter(s2300_infocomplementares_id__in = listar_ids(s2300_infocomplementares_lista) ).all()
        s2300_fgts_lista = s2300fgts.objects.filter(s2300_infocomplementares_id__in = listar_ids(s2300_infocomplementares_lista) ).all()
        s2300_infodirigentesindical_lista = s2300infoDirigenteSindical.objects.filter(s2300_infocomplementares_id__in = listar_ids(s2300_infocomplementares_lista) ).all()
        s2300_infotrabcedido_lista = s2300infoTrabCedido.objects.filter(s2300_infocomplementares_id__in = listar_ids(s2300_infocomplementares_lista) ).all()
        s2300_infoestagiario_lista = s2300infoEstagiario.objects.filter(s2300_infocomplementares_id__in = listar_ids(s2300_infocomplementares_lista) ).all()
        s2300_ageintegracao_lista = s2300ageIntegracao.objects.filter(s2300_infoestagiario_id__in = listar_ids(s2300_infoestagiario_lista) ).all()
        s2300_supervisorestagio_lista = s2300supervisorEstagio.objects.filter(s2300_infoestagiario_id__in = listar_ids(s2300_infoestagiario_lista) ).all()
        s2300_mudancacpf_lista = s2300mudancaCPF.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_afastamento_lista = s2300afastamento.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()
        s2300_termino_lista = s2300termino.objects.filter(s2300_evttsvinicio_id__in = listar_ids(s2300_evttsvinicio_lista) ).all()

        request.session['return_pk'] = pk
        request.session['return_page'] = 's2300_evttsvinicio'

        context = {
            's2300_evttsvinicio_lista': s2300_evttsvinicio_lista,
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            's2300_evttsvinicio': s2300_evttsvinicio,
            's2300_documentos_lista': s2300_documentos_lista,
            's2300_ctps_lista': s2300_ctps_lista,
            's2300_ric_lista': s2300_ric_lista,
            's2300_rg_lista': s2300_rg_lista,
            's2300_rne_lista': s2300_rne_lista,
            's2300_oc_lista': s2300_oc_lista,
            's2300_cnh_lista': s2300_cnh_lista,
            's2300_brasil_lista': s2300_brasil_lista,
            's2300_exterior_lista': s2300_exterior_lista,
            's2300_trabestrangeiro_lista': s2300_trabestrangeiro_lista,
            's2300_infodeficiencia_lista': s2300_infodeficiencia_lista,
            's2300_dependente_lista': s2300_dependente_lista,
            's2300_contato_lista': s2300_contato_lista,
            's2300_infocomplementares_lista': s2300_infocomplementares_lista,
            's2300_cargofuncao_lista': s2300_cargofuncao_lista,
            's2300_remuneracao_lista': s2300_remuneracao_lista,
            's2300_fgts_lista': s2300_fgts_lista,
            's2300_infodirigentesindical_lista': s2300_infodirigentesindical_lista,
            's2300_infotrabcedido_lista': s2300_infotrabcedido_lista,
            's2300_infoestagiario_lista': s2300_infoestagiario_lista,
            's2300_ageintegracao_lista': s2300_ageintegracao_lista,
            's2300_supervisorestagio_lista': s2300_supervisorestagio_lista,
            's2300_mudancacpf_lista': s2300_mudancacpf_lista,
            's2300_afastamento_lista': s2300_afastamento_lista,
            's2300_termino_lista': s2300_termino_lista,
            'modulos': ['esocial', ],
            'paginas': ['s2300_evttsvinicio', ],
            'data': datetime.now(),
            'output': output,
        }

        if output == 'pdf':

            response = PDFTemplateResponse(
                request=request,
                template='s2300_evttsvinicio_verificar.html',
                filename="s2300_evttsvinicio.pdf",
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

            response = render_to_response('s2300_evttsvinicio_verificar.html', context)
            filename = "%s.xls" % s2300_evttsvinicio.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        elif output == 'csv':

            response = render_to_response('s2300_evttsvinicio_verificar.html', context)
            filename = "%s.csv" % s2300_evttsvinicio.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:

            return render(request, 's2300_evttsvinicio_verificar.html', context)

    else:

        context = {
            'modulos': ['esocial', ],
            'paginas': ['s2300_evttsvinicio', ],
            'data': datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)