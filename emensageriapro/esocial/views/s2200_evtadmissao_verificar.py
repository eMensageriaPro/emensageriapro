#coding: utf-8
# © 2018 Marcelo Medeiros de Vasconcellos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
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


import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64
from emensageriapro.s2200.models import *
from emensageriapro.s2200.forms import *
import os


def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def txt_xml(texto):
    texto = str(texto)
    texto = texto.replace(">",'&gt;')
    texto = texto.replace("<",'&lt;')
    texto = texto.replace("&",'&amp;')
    texto = texto.replace('"','&quot;')
    texto = texto.replace("'",'&apos;')
    return texto



@login_required
def verificar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2200_evtadmissao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_evtadmissao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using( db_slug ), excluido = False, id = s2200_evtadmissao_id)
        s2200_evtadmissao_lista = s2200evtAdmissao.objects.using( db_slug ).filter(id=s2200_evtadmissao_id, excluido = False).all()
   

        s2200_documentos_lista = s2200documentos.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_ctps_lista = s2200CTPS.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_ric_lista = s2200RIC.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_rg_lista = s2200RG.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_rne_lista = s2200RNE.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_oc_lista = s2200OC.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_cnh_lista = s2200CNH.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_brasil_lista = s2200brasil.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_exterior_lista = s2200exterior.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_trabestrangeiro_lista = s2200trabEstrangeiro.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_infodeficiencia_lista = s2200infoDeficiencia.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_dependente_lista = s2200dependente.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_aposentadoria_lista = s2200aposentadoria.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_contato_lista = s2200contato.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_infoceletista_lista = s2200infoCeletista.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_trabtemporario_lista = s2200trabTemporario.objects.using(db_slug).filter(s2200_infoceletista_id__in = listar_ids(s2200_infoceletista_lista) ).filter(excluido=False).all()
        s2200_ideestabvinc_lista = s2200ideEstabVinc.objects.using(db_slug).filter(s2200_trabtemporario_id__in = listar_ids(s2200_trabtemporario_lista) ).filter(excluido=False).all()
        s2200_idetrabsubstituido_lista = s2200ideTrabSubstituido.objects.using(db_slug).filter(s2200_trabtemporario_id__in = listar_ids(s2200_trabtemporario_lista) ).filter(excluido=False).all()
        s2200_aprend_lista = s2200aprend.objects.using(db_slug).filter(s2200_infoceletista_id__in = listar_ids(s2200_infoceletista_lista) ).filter(excluido=False).all()
        s2200_infoestatutario_lista = s2200infoEstatutario.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_infodecjud_lista = s2200infoDecJud.objects.using(db_slug).filter(s2200_infoestatutario_id__in = listar_ids(s2200_infoestatutario_lista) ).filter(excluido=False).all()
        s2200_localtrabgeral_lista = s2200localTrabGeral.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_localtrabdom_lista = s2200localTrabDom.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_horcontratual_lista = s2200horContratual.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_horario_lista = s2200horario.objects.using(db_slug).filter(s2200_horcontratual_id__in = listar_ids(s2200_horcontratual_lista) ).filter(excluido=False).all()
        s2200_filiacaosindical_lista = s2200filiacaoSindical.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_alvarajudicial_lista = s2200alvaraJudicial.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_observacoes_lista = s2200observacoes.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_sucessaovinc_lista = s2200sucessaoVinc.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_transfdom_lista = s2200transfDom.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_afastamento_lista = s2200afastamento.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_desligamento_lista = s2200desligamento.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2200_evtadmissao'
        context = {
            's2200_evtadmissao_lista': s2200_evtadmissao_lista,
            's2200_evtadmissao_id': s2200_evtadmissao_id,
            's2200_evtadmissao': s2200_evtadmissao,
            
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            's2200_documentos_lista': s2200_documentos_lista,
            's2200_ctps_lista': s2200_ctps_lista,
            's2200_ric_lista': s2200_ric_lista,
            's2200_rg_lista': s2200_rg_lista,
            's2200_rne_lista': s2200_rne_lista,
            's2200_oc_lista': s2200_oc_lista,
            's2200_cnh_lista': s2200_cnh_lista,
            's2200_brasil_lista': s2200_brasil_lista,
            's2200_exterior_lista': s2200_exterior_lista,
            's2200_trabestrangeiro_lista': s2200_trabestrangeiro_lista,
            's2200_infodeficiencia_lista': s2200_infodeficiencia_lista,
            's2200_dependente_lista': s2200_dependente_lista,
            's2200_aposentadoria_lista': s2200_aposentadoria_lista,
            's2200_contato_lista': s2200_contato_lista,
            's2200_infoceletista_lista': s2200_infoceletista_lista,
            's2200_trabtemporario_lista': s2200_trabtemporario_lista,
            's2200_ideestabvinc_lista': s2200_ideestabvinc_lista,
            's2200_idetrabsubstituido_lista': s2200_idetrabsubstituido_lista,
            's2200_aprend_lista': s2200_aprend_lista,
            's2200_infoestatutario_lista': s2200_infoestatutario_lista,
            's2200_infodecjud_lista': s2200_infodecjud_lista,
            's2200_localtrabgeral_lista': s2200_localtrabgeral_lista,
            's2200_localtrabdom_lista': s2200_localtrabdom_lista,
            's2200_horcontratual_lista': s2200_horcontratual_lista,
            's2200_horario_lista': s2200_horario_lista,
            's2200_filiacaosindical_lista': s2200_filiacaosindical_lista,
            's2200_alvarajudicial_lista': s2200_alvarajudicial_lista,
            's2200_observacoes_lista': s2200_observacoes_lista,
            's2200_sucessaovinc_lista': s2200_sucessaovinc_lista,
            's2200_transfdom_lista': s2200_transfdom_lista,
            's2200_afastamento_lista': s2200_afastamento_lista,
            's2200_desligamento_lista': s2200_desligamento_lista,
        }
        if for_print == 2:
            #return render_to_pdf('%s/s2200_evtadmissao_verificar.html' % s2200_evtadmissao.versao, context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(request=request,
                                           template='%s/s2200_evtadmissao_verificar.html' % s2200_evtadmissao.versao,
                                           filename="s2200_evtadmissao.pdf",
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
            from django.shortcuts import render_to_response
            response =  render_to_response('%s/s2200_evtadmissao_verificar.html' % s2200_evtadmissao.versao, context)
            filename = "%s.xls" % s2200_evtadmissao.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response =  render_to_response('%s/s2200_evtadmissao_verificar.html' % s2200_evtadmissao.versao, context)
            filename = "%s.csv" % s2200_evtadmissao.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, '%s/s2200_evtadmissao_verificar.html' % s2200_evtadmissao.versao, context)
    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)



def gerar_xml_s2200(s2200_evtadmissao_id, db_slug):
    from django.template.loader import get_template
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using( db_slug ), excluido = False, id = s2200_evtadmissao_id)
        s2200_evtadmissao_lista = s2200evtAdmissao.objects.using( db_slug ).filter(id=s2200_evtadmissao_id, excluido = False).all()

        s2200_documentos_lista = s2200documentos.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_ctps_lista = s2200CTPS.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_ric_lista = s2200RIC.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_rg_lista = s2200RG.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_rne_lista = s2200RNE.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_oc_lista = s2200OC.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_cnh_lista = s2200CNH.objects.using(db_slug).filter(s2200_documentos_id__in = listar_ids(s2200_documentos_lista) ).filter(excluido=False).all()
        s2200_brasil_lista = s2200brasil.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_exterior_lista = s2200exterior.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_trabestrangeiro_lista = s2200trabEstrangeiro.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_infodeficiencia_lista = s2200infoDeficiencia.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_dependente_lista = s2200dependente.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_aposentadoria_lista = s2200aposentadoria.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_contato_lista = s2200contato.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_infoceletista_lista = s2200infoCeletista.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_trabtemporario_lista = s2200trabTemporario.objects.using(db_slug).filter(s2200_infoceletista_id__in = listar_ids(s2200_infoceletista_lista) ).filter(excluido=False).all()
        s2200_ideestabvinc_lista = s2200ideEstabVinc.objects.using(db_slug).filter(s2200_trabtemporario_id__in = listar_ids(s2200_trabtemporario_lista) ).filter(excluido=False).all()
        s2200_idetrabsubstituido_lista = s2200ideTrabSubstituido.objects.using(db_slug).filter(s2200_trabtemporario_id__in = listar_ids(s2200_trabtemporario_lista) ).filter(excluido=False).all()
        s2200_aprend_lista = s2200aprend.objects.using(db_slug).filter(s2200_infoceletista_id__in = listar_ids(s2200_infoceletista_lista) ).filter(excluido=False).all()
        s2200_infoestatutario_lista = s2200infoEstatutario.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_infodecjud_lista = s2200infoDecJud.objects.using(db_slug).filter(s2200_infoestatutario_id__in = listar_ids(s2200_infoestatutario_lista) ).filter(excluido=False).all()
        s2200_localtrabgeral_lista = s2200localTrabGeral.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_localtrabdom_lista = s2200localTrabDom.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_horcontratual_lista = s2200horContratual.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_horario_lista = s2200horario.objects.using(db_slug).filter(s2200_horcontratual_id__in = listar_ids(s2200_horcontratual_lista) ).filter(excluido=False).all()
        s2200_filiacaosindical_lista = s2200filiacaoSindical.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_alvarajudicial_lista = s2200alvaraJudicial.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_observacoes_lista = s2200observacoes.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_sucessaovinc_lista = s2200sucessaoVinc.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_transfdom_lista = s2200transfDom.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_afastamento_lista = s2200afastamento.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        s2200_desligamento_lista = s2200desligamento.objects.using(db_slug).filter(s2200_evtadmissao_id__in = listar_ids(s2200_evtadmissao_lista) ).filter(excluido=False).all()
        context = {
            'base': s2200_evtadmissao,
            's2200_evtadmissao_lista': s2200_evtadmissao_lista,
            's2200_evtadmissao_id': int(s2200_evtadmissao_id),
            's2200_evtadmissao': s2200_evtadmissao,

            's2200_documentos_lista': s2200_documentos_lista,
            's2200_ctps_lista': s2200_ctps_lista,
            's2200_ric_lista': s2200_ric_lista,
            's2200_rg_lista': s2200_rg_lista,
            's2200_rne_lista': s2200_rne_lista,
            's2200_oc_lista': s2200_oc_lista,
            's2200_cnh_lista': s2200_cnh_lista,
            's2200_brasil_lista': s2200_brasil_lista,
            's2200_exterior_lista': s2200_exterior_lista,
            's2200_trabestrangeiro_lista': s2200_trabestrangeiro_lista,
            's2200_infodeficiencia_lista': s2200_infodeficiencia_lista,
            's2200_dependente_lista': s2200_dependente_lista,
            's2200_aposentadoria_lista': s2200_aposentadoria_lista,
            's2200_contato_lista': s2200_contato_lista,
            's2200_infoceletista_lista': s2200_infoceletista_lista,
            's2200_trabtemporario_lista': s2200_trabtemporario_lista,
            's2200_ideestabvinc_lista': s2200_ideestabvinc_lista,
            's2200_idetrabsubstituido_lista': s2200_idetrabsubstituido_lista,
            's2200_aprend_lista': s2200_aprend_lista,
            's2200_infoestatutario_lista': s2200_infoestatutario_lista,
            's2200_infodecjud_lista': s2200_infodecjud_lista,
            's2200_localtrabgeral_lista': s2200_localtrabgeral_lista,
            's2200_localtrabdom_lista': s2200_localtrabdom_lista,
            's2200_horcontratual_lista': s2200_horcontratual_lista,
            's2200_horario_lista': s2200_horario_lista,
            's2200_filiacaosindical_lista': s2200_filiacaosindical_lista,
            's2200_alvarajudicial_lista': s2200_alvarajudicial_lista,
            's2200_observacoes_lista': s2200_observacoes_lista,
            's2200_sucessaovinc_lista': s2200_sucessaovinc_lista,
            's2200_transfdom_lista': s2200_transfdom_lista,
            's2200_afastamento_lista': s2200_afastamento_lista,
            's2200_desligamento_lista': s2200_desligamento_lista,
        }
        #return render(request, 'xml/%s/s2200_evtadmissao.html' % s2200_evtadmissao.versao, context, content_type='text/xml')
        t = get_template('%s/s2200_evtadmissao_xml.html' % s2200_evtadmissao.versao)
        xml = t.render(context)
        return xml
   


@login_required
def recibo(request, hash, tipo):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2200_evtadmissao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_evtadmissao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
   
        s2200_evtadmissao = get_object_or_404(
            s2200evtAdmissao.objects.using( db_slug ),
            excluido = False, id = s2200_evtadmissao_id)

        from emensageriapro.mensageiro.models import RetornosEventos, RetornosEventosHorarios, \
            RetornosEventosIntervalos, RetornosEventosOcorrencias

        retorno = get_object_or_404( RetornosEventos.objects.using(db_slug),
            id=s2200_evtadmissao.retornos_eventos_id, excluido=False)

        retorno_horarios = RetornosEventosHorarios.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()

        retorno_intervalos = RetornosEventosIntervalos.objects.using(db_slug).\
            filter(retornos_eventos_horarios_id__in=listar_ids(retorno_horarios),excluido=False).all()

        retorno_ocorrencias = RetornosEventosOcorrencias.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()
   
        context = {
            's2200_evtadmissao_id': s2200_evtadmissao_id,
            's2200_evtadmissao': s2200_evtadmissao,

            'retorno': retorno,
            'retorno_horarios': retorno_horarios,
            'retorno_intervalos': retorno_intervalos,
            'retorno_ocorrencias': retorno_ocorrencias,

            
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
        }

        if tipo == 'XLS':
            from django.shortcuts import render_to_response
            response =  render_to_response('s2200_evtadmissao_recibo_pdf.html', context)
            filename = "%s.xls" % s2200_evtadmissao.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif tipo == 'CSV':
            from django.shortcuts import render_to_response
            response =  render_to_response('s2200_evtadmissao_recibo_csv.html', context)
            filename = "%s.csv" % s2200_evtadmissao.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render_to_pdf('s2200_evtadmissao_recibo_pdf.html', context)
    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)



def gerar_xml_assinado(s2200_evtadmissao_id, db_slug):
    import os
    from datetime import datetime
    from django.http import HttpResponse
    from emensageriapro.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_esocial import assinar_esocial
    s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using(db_slug), excluido=False, id=s2200_evtadmissao_id)
    if s2200_evtadmissao.arquivo_original:
        xml = ler_arquivo(s2200_evtadmissao.arquivo)
    else:
        xml = gerar_xml_s2200(s2200_evtadmissao_id, db_slug)
    if 'Signature' in xml:
        xml_assinado = xml
    else:
        xml_assinado = assinar_esocial(xml)
    if s2200_evtadmissao.status in (0,1,2,11):
        s2200evtAdmissao.objects.using(db_slug).filter(id=s2200_evtadmissao_id,excluido=False).update(status=10)
    arquivo = 'arquivos/Eventos/s2200_evtadmissao/%s.xml' % (s2200_evtadmissao.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s2200_evtadmissao/' % BASE_DIR)
    if not os.path.exists(BASE_DIR+arquivo):
        salvar_arquivo_esocial(arquivo, xml_assinado, 1)
    xml_assinado = ler_arquivo(arquivo)
    return xml_assinado



@login_required
def gerar_xml(request, hash):
    import os
    from datetime import datetime
    from django.http import HttpResponse
    from emensageriapro.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_esocial import assinar_esocial
    hora_atual = str(datetime.now()).replace(' ', '_').replace('.', '_').replace(':', '_')
    for_print = 0
    db_slug = 'default'
    dict_hash = get_hash_url( hash )
    s2200_evtadmissao_id = int(dict_hash['id'])
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using(db_slug), excluido=False, id=s2200_evtadmissao_id)
        xml_assinado = gerar_xml_assinado(s2200_evtadmissao_id, db_slug)
        return HttpResponse(xml_assinado, content_type='text/xml')
    else:
        context = {
            
            
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)



@login_required
def duplicar(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2200_evtadmissao_id = int(dict_hash['id'])
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using(db_slug), excluido=False,
                                                    id=s2200_evtadmissao_id)

        arquivo = 'arquivos/Eventos/s2200_evtadmissao/%s.xml' % s2200_evtadmissao.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(s2200_evtadmissao_id, db_slug)
   
        texto = ler_arquivo('arquivos/Eventos/s2200_evtadmissao/%s.xml' % s2200_evtadmissao.identidade)
        salvar_arquivo('arquivos/Eventos/s2200_evtadmissao/%s_duplicado_temp.xml' % s2200_evtadmissao.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/s2200_evtadmissao/%s_duplicado_temp.xml' % s2200_evtadmissao.identidade, request)
        from emensageriapro.esocial.views.s2200_evtadmissao import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        s2200evtAdmissao.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        messages.success(request, 'Evento duplicado com sucesso! Foi criado uma nova identidade para este evento!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        usuario_id = request.session['usuario_id']
        gravar_auditoria(u'{}', u'{"funcao": "Evento de identidade %s criado a partir da duplicação do evento %s"}' % (dent, s2200_evtadmissao.identidade),
            's2200_evtadmissao', dados['identidade'], usuario_id, 1)
        return redirect('s2200_evtadmissao_salvar', hash=url_hash)
    messages.error(request, 'Erro ao duplicar evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



@login_required
def criar_alteracao(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2200_evtadmissao_id = int(dict_hash['id'])
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using(db_slug), excluido=False,
                                                    id=s2200_evtadmissao_id)
        arquivo = 'arquivos/Eventos/s2200_evtadmissao/%s.xml' % s2200_evtadmissao.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(s2200_evtadmissao_id, db_slug)
        texto = ler_arquivo('arquivos/Eventos/s2200_evtadmissao/%s.xml' % s2200_evtadmissao.identidade)
        texto = texto.replace('<inclusao>','<alteracao>').replace('</inclusao>','</alteracao>')
        salvar_arquivo('arquivos/Eventos/s2200_evtadmissao/%s_alteracao_temp.xml' % s2200_evtadmissao.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/s2200_evtadmissao/%s_alteracao_temp.xml' % s2200_evtadmissao.identidade, request)
        from emensageriapro.esocial.views.s2200_evtadmissao import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        s2200evtAdmissao.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        usuario_id = request.session['usuario_id']
        gravar_auditoria(u'{}', u'{"funcao": "Evento de de alteração de identidade %s criado a partir da duplicação do evento %s"}' % (dent, s2200_evtadmissao.identidade),
            's2200_evtadmissao', dados['identidade'], usuario_id, 1)
        messages.success(request, 'Evento de alteração criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        return redirect('s2200_evtadmissao_salvar', hash=url_hash)
    messages.error(request, 'Erro ao criar evento de alteração!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def criar_exclusao(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2200_evtadmissao_id = int(dict_hash['id'])
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using(db_slug), excluido=False,
                                                    id=s2200_evtadmissao_id)
        arquivo = 'arquivos/Eventos/s2200_evtadmissao/%s.xml' % s2200_evtadmissao.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(s2200_evtadmissao_id, db_slug)
        texto = ler_arquivo('arquivos/Eventos/s2200_evtadmissao/%s.xml' % s2200_evtadmissao.identidade)
        texto = texto.replace('<inclusao>','<exclusao>').replace('</inclusao>','</exclusao>')
        texto = texto.replace('<alteracao>','<exclusao>').replace('</alteracao>','</exclusao>')
        salvar_arquivo('arquivos/Eventos/s2200_evtadmissao/%s_exclusao_temp.xml' % s2200_evtadmissao.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/s2200_evtadmissao/%s_exclusao_temp.xml' % s2200_evtadmissao.identidade, request)
        from emensageriapro.esocial.views.s2200_evtadmissao import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        s2200evtAdmissao.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        usuario_id = request.session['usuario_id']
        gravar_auditoria(u'{}', u'{"funcao": "Evento de exclusão de identidade %s criado a partir da duplicação do evento %s"}' % (dent, s2200_evtadmissao.identidade),
            's2200_evtadmissao', dados['identidade'], usuario_id, 1)
        messages.success(request, 'Evento de exclusão criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        return redirect('s2200_evtadmissao_salvar', hash=url_hash)
    messages.error(request, 'Erro ao criar evento de exclusão!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




@login_required
def alterar_identidade(request, hash):
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2200_evtadmissao_id = int(dict_hash['id'])
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using(db_slug), excluido=False,
                                                    id=s2200_evtadmissao_id)
        if s2200_evtadmissao.status == 0:
            from emensageriapro.esocial.views.s2200_evtadmissao import identidade_evento
            dent = identidade_evento(s2200_evtadmissao_id, db_slug)
            messages.success(request, 'Identidade do evento alterada com sucesso!')
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s2200_evtadmissao_id )
            usuario_id = request.session['usuario_id']
            gravar_auditoria(u'{}', u'{"funcao": "Identidade do evento foi alterada"}',
            's2200_evtadmissao', s2200_evtadmissao_id, usuario_id, 1)
            return redirect('s2200_evtadmissao_salvar', hash=url_hash)
        else:
            messages.error(request, 'Não foi possível alterar a identidade do evento! Somente é possível alterar o status de eventos que estão abertos para edição (status: Cadastrado)!')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, 'Erro ao alterar identidade do evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



@login_required
def abrir_evento_para_edicao(request, hash):
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_esocial import gravar_nome_arquivo
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2200_evtadmissao_id = int(dict_hash['id'])
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using(db_slug), excluido=False, id=s2200_evtadmissao_id)
        if s2200_evtadmissao.status in (0, 1, 2, 3, 4, 10, 11) or s2200_evtadmissao.processamento_codigo_resposta in (401,402):
            s2200evtAdmissao.objects.using(db_slug).filter(id=s2200_evtadmissao_id).update(status=0, arquivo_original=0)
            arquivo = 'arquivos/Eventos/s2200_evtadmissao/%s.xml' % (s2200_evtadmissao.identidade)
            if os.path.exists(BASE_DIR + '/' + arquivo):
                from datetime import datetime
                data_hora_atual = str(datetime.now()).replace(':','_').replace(' ','_').replace('.','_')
                dad = (BASE_DIR, s2200_evtadmissao.identidade, BASE_DIR, s2200_evtadmissao.identidade, data_hora_atual)
                os.system('mv %s/arquivos/Eventos/s2200_evtadmissao/%s.xml %s/arquivos/Eventos/s2200_evtadmissao/%s_backup_%s.xml' % dad)
                gravar_nome_arquivo('/arquivos/Eventos/s2200_evtadmissao/%s_backup_%s.xml' % (s2200_evtadmissao.identidade, data_hora_atual),
                    1)
            messages.success(request, 'Evento aberto para edição!')
            usuario_id = request.session['usuario_id']
            gravar_auditoria(u'{}', u'{"funcao": "Evento aberto para edição"}',
            's2200_evtadmissao', s2200_evtadmissao_id, usuario_id, 1)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s2200_evtadmissao_id )
            return redirect('s2200_evtadmissao_salvar', hash=url_hash)
        else:
            messages.error(request, '''
            Não foi possível abrir o evento para edição! Somente é possível
            abrir eventos com os seguintes status: "Cadastrado", "Importado", "Validado",
            "Duplicado", "Erro na validação", "XML Assinado" ou "XML Gerado"
             ou com o status "Enviado com sucesso" e os seguintes códigos de resposta do servidor:
             "401 - Lote Incorreto - Erro preenchimento" ou "402 - Lote Incorreto - schema Inválido"!''')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, 'Erro ao abrir evento para edição!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



def validar_evento_funcao(s2200_evtadmissao_id, db_slug):
    from emensageriapro.padrao import executar_sql
    from emensageriapro.funcoes_importacao import get_versao_evento
    from emensageriapro.funcoes_validacoes_precedencia import validar_precedencia
    from emensageriapro.funcoes_validacoes import get_schema_name, validar_schema
    from emensageriapro.settings import BASE_DIR
    lista_validacoes = []
    s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using(db_slug), excluido=False, id=s2200_evtadmissao_id)
    quant = validar_precedencia('esocial', 's2200_evtadmissao', s2200_evtadmissao_id)
    if quant <= 0:
        #lista_validacoes.append('Precedência não foi enviada!')
        precedencia = 0
    else:
        precedencia = 1
    executar_sql("UPDATE public.s2200_evtadmissao SET validacao_precedencia=%s WHERE id=%s;" % (precedencia, s2200_evtadmissao_id), False)
    #
    # Validações internas
    #
    arquivo = 'arquivos/Eventos/s2200_evtadmissao/%s.xml' % (s2200_evtadmissao.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s2200_evtadmissao/' % BASE_DIR)
    lista = []
    tipo = 'esocial'
    if not os.path.exists(BASE_DIR + '/' + arquivo):
        gerar_xml_assinado(s2200_evtadmissao_id, db_slug)
    if os.path.exists(BASE_DIR + '/' + arquivo):
        texto_xml = ler_arquivo(arquivo).replace("s:", "")
        versao = get_versao_evento(texto_xml)
        if tipo == 'esocial':
            if versao == 'v02_04_02':
                from emensageriapro.esocial.validacoes.v02_04_02.s2200_evtadmissao import validacoes_s2200_evtadmissao
                lista = validacoes_s2200_evtadmissao(arquivo)
        elif tipo == 'efdreinf':
            if versao == 'v1_03_02':
                from emensageriapro.efdreinf.validacoes.v1_03_02.s2200_evtadmissao import validacoes_s2200_evtadmissao
                lista = validacoes_s2200_evtadmissao(arquivo)
    for a in lista:
        if a:
            lista_validacoes.append(a)
    #
    # validando schema
    #
    schema_filename = get_schema_name(arquivo)
    quant_erros, error_list = validar_schema(schema_filename, arquivo, lang='pt')
    for a in error_list:
        if a:
            lista_validacoes.append(a)
    #
    #
    #
    if lista_validacoes:
        executar_sql("UPDATE public.s2200_evtadmissao SET validacoes='%s', status=3 WHERE id=%s;" % ('<br>'.join(lista_validacoes).replace("'","''"), s2200_evtadmissao_id), False)
    else:
        executar_sql("UPDATE public.s2200_evtadmissao SET validacoes='', status=4 WHERE id=%s;" % (s2200_evtadmissao_id), False)
    return lista_validacoes



@login_required
def validar_evento(request, hash):
    from emensageriapro.funcoes_validacoes import VERSAO_ATUAL
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s2200_evtadmissao_id = int(dict_hash['id'])
    if s2200_evtadmissao_id:
        lista_validacoes = []
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using(db_slug), excluido=False, id=s2200_evtadmissao_id)
        if s2200_evtadmissao.versao in VERSAO_ATUAL:
            lista_validacoes = validar_evento_funcao(s2200_evtadmissao_id, db_slug)
            messages.success(request, 'Validações processadas com sucesso!')
        else:
            messages.error(request, 'Não foi possível validar o evento pois a versão do evento não é compatível com a versão do sistema!')
    else:
        messages.error(request, 'Não foi possível validar o evento pois o mesmo não foi identificado!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
