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
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
from emensageriapro.s1005.models import *
from emensageriapro.s1005.forms import *
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
def verificar(request, hash):
    for_print = 0
    
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1005_evttabestab_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get(endereco='s1005_evttabestab')
    permissao = ConfigPermissoes.objects.get(config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s1005_evttabestab = get_object_or_404(s1005evtTabEstab, id = s1005_evttabestab_id)
        s1005_evttabestab_lista = s1005evtTabEstab.objects.filter(id=s1005_evttabestab_id).all()

        
        s1005_inclusao_lista = s1005inclusao.objects.filter(s1005_evttabestab_id__in = listar_ids(s1005_evttabestab_lista) ).all()
        s1005_inclusao_procadmjudrat_lista = s1005inclusaoprocAdmJudRat.objects.filter(s1005_inclusao_id__in = listar_ids(s1005_inclusao_lista) ).all()
        s1005_inclusao_procadmjudfap_lista = s1005inclusaoprocAdmJudFap.objects.filter(s1005_inclusao_id__in = listar_ids(s1005_inclusao_lista) ).all()
        s1005_inclusao_infocaepf_lista = s1005inclusaoinfoCaepf.objects.filter(s1005_inclusao_id__in = listar_ids(s1005_inclusao_lista) ).all()
        s1005_inclusao_infoobra_lista = s1005inclusaoinfoObra.objects.filter(s1005_inclusao_id__in = listar_ids(s1005_inclusao_lista) ).all()
        s1005_inclusao_infoenteduc_lista = s1005inclusaoinfoEntEduc.objects.filter(s1005_inclusao_id__in = listar_ids(s1005_inclusao_lista) ).all()
        s1005_inclusao_infopcd_lista = s1005inclusaoinfoPCD.objects.filter(s1005_inclusao_id__in = listar_ids(s1005_inclusao_lista) ).all()
        s1005_alteracao_lista = s1005alteracao.objects.filter(s1005_evttabestab_id__in = listar_ids(s1005_evttabestab_lista) ).all()
        s1005_alteracao_procadmjudrat_lista = s1005alteracaoprocAdmJudRat.objects.filter(s1005_alteracao_id__in = listar_ids(s1005_alteracao_lista) ).all()
        s1005_alteracao_procadmjudfap_lista = s1005alteracaoprocAdmJudFap.objects.filter(s1005_alteracao_id__in = listar_ids(s1005_alteracao_lista) ).all()
        s1005_alteracao_infocaepf_lista = s1005alteracaoinfoCaepf.objects.filter(s1005_alteracao_id__in = listar_ids(s1005_alteracao_lista) ).all()
        s1005_alteracao_infoobra_lista = s1005alteracaoinfoObra.objects.filter(s1005_alteracao_id__in = listar_ids(s1005_alteracao_lista) ).all()
        s1005_alteracao_infoenteduc_lista = s1005alteracaoinfoEntEduc.objects.filter(s1005_alteracao_id__in = listar_ids(s1005_alteracao_lista) ).all()
        s1005_alteracao_infopcd_lista = s1005alteracaoinfoPCD.objects.filter(s1005_alteracao_id__in = listar_ids(s1005_alteracao_lista) ).all()
        s1005_alteracao_novavalidade_lista = s1005alteracaonovaValidade.objects.filter(s1005_alteracao_id__in = listar_ids(s1005_alteracao_lista) ).all()
        s1005_exclusao_lista = s1005exclusao.objects.filter(s1005_evttabestab_id__in = listar_ids(s1005_evttabestab_lista) ).all()

        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1005_evttabestab'

        context = {
            's1005_evttabestab_lista': s1005_evttabestab_lista,
            's1005_evttabestab_id': s1005_evttabestab_id,
            's1005_evttabestab': s1005_evttabestab,
            
            
            's1005_inclusao_lista': s1005_inclusao_lista,
            's1005_inclusao_procadmjudrat_lista': s1005_inclusao_procadmjudrat_lista,
            's1005_inclusao_procadmjudfap_lista': s1005_inclusao_procadmjudfap_lista,
            's1005_inclusao_infocaepf_lista': s1005_inclusao_infocaepf_lista,
            's1005_inclusao_infoobra_lista': s1005_inclusao_infoobra_lista,
            's1005_inclusao_infoenteduc_lista': s1005_inclusao_infoenteduc_lista,
            's1005_inclusao_infopcd_lista': s1005_inclusao_infopcd_lista,
            's1005_alteracao_lista': s1005_alteracao_lista,
            's1005_alteracao_procadmjudrat_lista': s1005_alteracao_procadmjudrat_lista,
            's1005_alteracao_procadmjudfap_lista': s1005_alteracao_procadmjudfap_lista,
            's1005_alteracao_infocaepf_lista': s1005_alteracao_infocaepf_lista,
            's1005_alteracao_infoobra_lista': s1005_alteracao_infoobra_lista,
            's1005_alteracao_infoenteduc_lista': s1005_alteracao_infoenteduc_lista,
            's1005_alteracao_infopcd_lista': s1005_alteracao_infopcd_lista,
            's1005_alteracao_novavalidade_lista': s1005_alteracao_novavalidade_lista,
            's1005_exclusao_lista': s1005_exclusao_lista,
            
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
                                           template='s1005_evttabestab_verificar.html',
                                           filename="s1005_evttabestab.pdf",
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
            response =  render_to_response('s1005_evttabestab_verificar.html', context)
            filename = "%s.xls" % s1005_evttabestab.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response =  render_to_response('s1005_evttabestab_verificar.html', context)
            filename = "%s.csv" % s1005_evttabestab.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:
            return render(request, 's1005_evttabestab_verificar.html', context)

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