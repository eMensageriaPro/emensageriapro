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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
from emensageriapro.r1070.models import *
from emensageriapro.r1070.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from datetime import datetime
import base64
import os


from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


@login_required
def verificar(request, hash):
    for_print = 0
    
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r1070_evttabprocesso_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get(endereco='r1070_evttabprocesso')
    permissao = ConfigPermissoes.objects.get(config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        r1070_evttabprocesso = get_object_or_404(r1070evtTabProcesso, id = r1070_evttabprocesso_id)
        r1070_evttabprocesso_lista = r1070evtTabProcesso.objects.filter(id=r1070_evttabprocesso_id).all()

        
        r1070_inclusao_lista = r1070inclusao.objects.filter(r1070_evttabprocesso_id__in = listar_ids(r1070_evttabprocesso_lista) ).all()
        r1070_inclusao_infosusp_lista = r1070inclusaoinfoSusp.objects.filter(r1070_inclusao_id__in = listar_ids(r1070_inclusao_lista) ).all()
        r1070_inclusao_dadosprocjud_lista = r1070inclusaodadosProcJud.objects.filter(r1070_inclusao_id__in = listar_ids(r1070_inclusao_lista) ).all()
        r1070_alteracao_lista = r1070alteracao.objects.filter(r1070_evttabprocesso_id__in = listar_ids(r1070_evttabprocesso_lista) ).all()
        r1070_alteracao_infosusp_lista = r1070alteracaoinfoSusp.objects.filter(r1070_alteracao_id__in = listar_ids(r1070_alteracao_lista) ).all()
        r1070_alteracao_dadosprocjud_lista = r1070alteracaodadosProcJud.objects.filter(r1070_alteracao_id__in = listar_ids(r1070_alteracao_lista) ).all()
        r1070_alteracao_novavalidade_lista = r1070alteracaonovaValidade.objects.filter(r1070_alteracao_id__in = listar_ids(r1070_alteracao_lista) ).all()
        r1070_exclusao_lista = r1070exclusao.objects.filter(r1070_evttabprocesso_id__in = listar_ids(r1070_evttabprocesso_lista) ).all()

        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r1070_evttabprocesso'

        context = {
            'r1070_evttabprocesso_lista': r1070_evttabprocesso_lista,
            'r1070_evttabprocesso_id': r1070_evttabprocesso_id,
            'r1070_evttabprocesso': r1070_evttabprocesso,
            
            
            'r1070_inclusao_lista': r1070_inclusao_lista,
            'r1070_inclusao_infosusp_lista': r1070_inclusao_infosusp_lista,
            'r1070_inclusao_dadosprocjud_lista': r1070_inclusao_dadosprocjud_lista,
            'r1070_alteracao_lista': r1070_alteracao_lista,
            'r1070_alteracao_infosusp_lista': r1070_alteracao_infosusp_lista,
            'r1070_alteracao_dadosprocjud_lista': r1070_alteracao_dadosprocjud_lista,
            'r1070_alteracao_novavalidade_lista': r1070_alteracao_novavalidade_lista,
            'r1070_exclusao_lista': r1070_exclusao_lista,
            
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            

        }
        if for_print == 2:
            response = PDFTemplateResponse(request=request,
                                           template='r1070_evttabprocesso_verificar.html',
                                           filename="r1070_evttabprocesso.pdf",
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
                                                        "no-stop-slow-scripts": True},
                                           )
            return response

        elif for_print == 3:
            response =  render_to_response('r1070_evttabprocesso_verificar.html', context)
            filename = "%s.xls" % r1070_evttabprocesso.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response =  render_to_response('r1070_evttabprocesso_verificar.html', context)
            filename = "%s.csv" % r1070_evttabprocesso.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:
            return render(request, 'r1070_evttabprocesso_verificar.html', context)

    else:

        context = {
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'permissao': permissao,
            'data': datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }

        return render(request, 'permissao_negada.html', context)