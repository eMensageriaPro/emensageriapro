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
from emensageriapro.s1000.models import *
from emensageriapro.s1000.forms import *
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

    if request.user.has_perm('esocial.can_see_s1000evtInfoEmpregador'):
    
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador, id=pk)
        s1000_evtinfoempregador_lista = s1000evtInfoEmpregador.objects.filter(id=pk).all()

        
        s1000_inclusao_lista = s1000inclusao.objects.filter(s1000_evtinfoempregador_id__in = listar_ids(s1000_evtinfoempregador_lista) ).all()
        s1000_inclusao_dadosisencao_lista = s1000inclusaodadosIsencao.objects.filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).all()
        s1000_inclusao_infoop_lista = s1000inclusaoinfoOP.objects.filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).all()
        s1000_inclusao_infoefr_lista = s1000inclusaoinfoEFR.objects.filter(s1000_inclusao_infoop_id__in = listar_ids(s1000_inclusao_infoop_lista) ).all()
        s1000_inclusao_infoente_lista = s1000inclusaoinfoEnte.objects.filter(s1000_inclusao_infoop_id__in = listar_ids(s1000_inclusao_infoop_lista) ).all()
        s1000_inclusao_infoorginternacional_lista = s1000inclusaoinfoOrgInternacional.objects.filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).all()
        s1000_inclusao_softwarehouse_lista = s1000inclusaosoftwareHouse.objects.filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).all()
        s1000_inclusao_situacaopj_lista = s1000inclusaosituacaoPJ.objects.filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).all()
        s1000_inclusao_situacaopf_lista = s1000inclusaosituacaoPF.objects.filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).all()
        s1000_alteracao_lista = s1000alteracao.objects.filter(s1000_evtinfoempregador_id__in = listar_ids(s1000_evtinfoempregador_lista) ).all()
        s1000_alteracao_dadosisencao_lista = s1000alteracaodadosIsencao.objects.filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).all()
        s1000_alteracao_infoop_lista = s1000alteracaoinfoOP.objects.filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).all()
        s1000_alteracao_infoefr_lista = s1000alteracaoinfoEFR.objects.filter(s1000_alteracao_infoop_id__in = listar_ids(s1000_alteracao_infoop_lista) ).all()
        s1000_alteracao_infoente_lista = s1000alteracaoinfoEnte.objects.filter(s1000_alteracao_infoop_id__in = listar_ids(s1000_alteracao_infoop_lista) ).all()
        s1000_alteracao_infoorginternacional_lista = s1000alteracaoinfoOrgInternacional.objects.filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).all()
        s1000_alteracao_softwarehouse_lista = s1000alteracaosoftwareHouse.objects.filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).all()
        s1000_alteracao_situacaopj_lista = s1000alteracaosituacaoPJ.objects.filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).all()
        s1000_alteracao_situacaopf_lista = s1000alteracaosituacaoPF.objects.filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).all()
        s1000_alteracao_novavalidade_lista = s1000alteracaonovaValidade.objects.filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).all()
        s1000_exclusao_lista = s1000exclusao.objects.filter(s1000_evtinfoempregador_id__in = listar_ids(s1000_evtinfoempregador_lista) ).all()

        request.session['return_pk'] = pk
        request.session['return_page'] = 's1000_evtinfoempregador'

        context = {
            's1000_evtinfoempregador_lista': s1000_evtinfoempregador_lista,
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            's1000_evtinfoempregador': s1000_evtinfoempregador,
            's1000_inclusao_lista': s1000_inclusao_lista,
            's1000_inclusao_dadosisencao_lista': s1000_inclusao_dadosisencao_lista,
            's1000_inclusao_infoop_lista': s1000_inclusao_infoop_lista,
            's1000_inclusao_infoefr_lista': s1000_inclusao_infoefr_lista,
            's1000_inclusao_infoente_lista': s1000_inclusao_infoente_lista,
            's1000_inclusao_infoorginternacional_lista': s1000_inclusao_infoorginternacional_lista,
            's1000_inclusao_softwarehouse_lista': s1000_inclusao_softwarehouse_lista,
            's1000_inclusao_situacaopj_lista': s1000_inclusao_situacaopj_lista,
            's1000_inclusao_situacaopf_lista': s1000_inclusao_situacaopf_lista,
            's1000_alteracao_lista': s1000_alteracao_lista,
            's1000_alteracao_dadosisencao_lista': s1000_alteracao_dadosisencao_lista,
            's1000_alteracao_infoop_lista': s1000_alteracao_infoop_lista,
            's1000_alteracao_infoefr_lista': s1000_alteracao_infoefr_lista,
            's1000_alteracao_infoente_lista': s1000_alteracao_infoente_lista,
            's1000_alteracao_infoorginternacional_lista': s1000_alteracao_infoorginternacional_lista,
            's1000_alteracao_softwarehouse_lista': s1000_alteracao_softwarehouse_lista,
            's1000_alteracao_situacaopj_lista': s1000_alteracao_situacaopj_lista,
            's1000_alteracao_situacaopf_lista': s1000_alteracao_situacaopf_lista,
            's1000_alteracao_novavalidade_lista': s1000_alteracao_novavalidade_lista,
            's1000_exclusao_lista': s1000_exclusao_lista,
            'modulos': ['esocial', ],
            'paginas': ['s1000_evtinfoempregador', ],
            'data': datetime.now(),
            'output': output,
        }
        
        if output == 'pdf':
        
            response = PDFTemplateResponse(
                request=request,
                template='s1000_evtinfoempregador_verificar.html',
                filename="s1000_evtinfoempregador.pdf",
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
        
            response = render_to_response('s1000_evtinfoempregador_verificar.html', context)
            filename = "%s.xls" % s1000_evtinfoempregador.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response

        elif output == 'csv':
        
            response = render_to_response('s1000_evtinfoempregador_verificar.html', context)
            filename = "%s.csv" % s1000_evtinfoempregador.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:
        
            return render(request, 's1000_evtinfoempregador_verificar.html', context)

    else:

        context = {
            'modulos': ['esocial', ],
            'paginas': ['s1000_evtinfoempregador', ],
            'data': datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)