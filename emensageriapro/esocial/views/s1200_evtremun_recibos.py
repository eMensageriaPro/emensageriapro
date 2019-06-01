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
from emensageriapro.s1200.models import *
from emensageriapro.s1200.forms import *
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
def recibo(request, hash, tipo):

    from emensageriapro.mensageiro.models import RetornosEventos, RetornosEventosHorarios, \
        RetornosEventosIntervalos, RetornosEventosOcorrencias
            
    for_print = 0
    
    try:
    
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1200_evtremun_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])

    except:
    
        return redirect('login')

    usuario = get_object_or_404(Usuarios, id=usuario_id)

    if request.user.has_perm('esocial.can_view_s1200evtRemun'):

        s1200_evtremun = get_object_or_404(
            s1200evtRemun,
            id=s1200_evtremun_id)

        retorno = get_object_or_404(RetornosEventos,
            id=s1200_evtremun.retornos_eventos_id)

        retorno_horarios = RetornosEventosHorarios.objects.\
            filter(retornos_eventos_id=retorno.id).all()

        retorno_intervalos = RetornosEventosIntervalos.objects.\
            filter(retornos_eventos_horarios_id__in=listar_ids(retorno_horarios)).all()

        retorno_ocorrencias = RetornosEventosOcorrencias.objects.\
            filter(retornos_eventos_id=retorno.id).all()

        context = {
            's1200_evtremun_id': s1200_evtremun_id,
            's1200_evtremun': s1200_evtremun,
            'retorno': retorno,
            'retorno_horarios': retorno_horarios,
            'retorno_intervalos': retorno_intervalos,
            'retorno_ocorrencias': retorno_ocorrencias,
            'usuario': usuario,
            'data': datetime.now(),
            'for_print': for_print,
            'hash': hash,
        }

        if tipo == 'XLS':
        
            response =  render_to_response('s1200_evtremun_recibo_pdf.html', context)
            filename = "%s.xls" % s1200_evtremun.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif tipo == 'CSV':
        
            response =  render_to_response('s1200_evtremun_recibo_csv.html', context)
            filename = "%s.csv" % s1200_evtremun.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:
        
            return render_to_pdf('s1200_evtremun_recibo_pdf.html', context)

    else:

        context = {
            'usuario': usuario,
            'data': datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)