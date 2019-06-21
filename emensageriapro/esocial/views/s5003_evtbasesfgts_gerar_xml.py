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
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.s5003.models import *
from emensageriapro.s5003.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from django.template.loader import get_template
from emensageriapro.functions import get_xmlns


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def gerar_xml_s5003(request, pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    if pk:

        s5003_evtbasesfgts = get_object_or_404(
            s5003evtBasesFGTS,
            id=pk)

        if not versao or versao == '|':
            versao = s5003_evtbasesfgts.versao

        evento = 's5003evtBasesFGTS'[5:]
        arquivo = 'xsd/esocial/%s/%s.xsd' % (versao, evento)

        import os.path

        if os.path.isfile(BASE_DIR + '/' + arquivo):

            xmlns = get_xmlns(arquivo)

        else:
        
            from django.contrib import messages

            messages.warning(request, '''
                Não foi capturar o XMLNS pois o XSD do 
                evento não está contido na pasta!''')

            xmlns = ''

        s5003_evtbasesfgts_lista = s5003evtBasesFGTS.objects. \
            filter(id=pk).all()
            
        
        s5003_ideestablot_lista = s5003ideEstabLot.objects. \
            filter(s5003_evtbasesfgts_id__in=listar_ids(s5003_evtbasesfgts_lista)).all()
        
        s5003_infotrabfgts_lista = s5003infoTrabFGTS.objects. \
            filter(s5003_ideestablot_id__in=listar_ids(s5003_ideestablot_lista)).all()
        
        s5003_infobasefgts_lista = s5003infoBaseFGTS.objects. \
            filter(s5003_infotrabfgts_id__in=listar_ids(s5003_infotrabfgts_lista)).all()
        
        s5003_baseperapur_lista = s5003basePerApur.objects. \
            filter(s5003_infobasefgts_id__in=listar_ids(s5003_infobasefgts_lista)).all()
        
        s5003_infobaseperante_lista = s5003infoBasePerAntE.objects. \
            filter(s5003_infobasefgts_id__in=listar_ids(s5003_infobasefgts_lista)).all()
        
        s5003_baseperante_lista = s5003basePerAntE.objects. \
            filter(s5003_infobaseperante_id__in=listar_ids(s5003_infobaseperante_lista)).all()
        
        s5003_infodpsfgts_lista = s5003infoDpsFGTS.objects. \
            filter(s5003_evtbasesfgts_id__in=listar_ids(s5003_evtbasesfgts_lista)).all()
        
        s5003_infotrabdps_lista = s5003infoTrabDps.objects. \
            filter(s5003_infodpsfgts_id__in=listar_ids(s5003_infodpsfgts_lista)).all()
        
        s5003_dpsperapur_lista = s5003dpsPerApur.objects. \
            filter(s5003_infotrabdps_id__in=listar_ids(s5003_infotrabdps_lista)).all()
        
        s5003_infodpsperante_lista = s5003infoDpsPerAntE.objects. \
            filter(s5003_infotrabdps_id__in=listar_ids(s5003_infotrabdps_lista)).all()
        
        s5003_dpsperante_lista = s5003dpsPerAntE.objects. \
            filter(s5003_infodpsperante_id__in=listar_ids(s5003_infodpsperante_lista)).all()
        

        context = {
            'xmlns': xmlns,
            'versao': versao,
            'base': s5003_evtbasesfgts,
            's5003_evtbasesfgts_lista': s5003_evtbasesfgts_lista,
            'pk': int(pk),
            's5003_evtbasesfgts': s5003_evtbasesfgts,
            's5003_ideestablot_lista': s5003_ideestablot_lista,
            's5003_infotrabfgts_lista': s5003_infotrabfgts_lista,
            's5003_infobasefgts_lista': s5003_infobasefgts_lista,
            's5003_baseperapur_lista': s5003_baseperapur_lista,
            's5003_infobaseperante_lista': s5003_infobaseperante_lista,
            's5003_baseperante_lista': s5003_baseperante_lista,
            's5003_infodpsfgts_lista': s5003_infodpsfgts_lista,
            's5003_infotrabdps_lista': s5003_infotrabdps_lista,
            's5003_dpsperapur_lista': s5003_dpsperapur_lista,
            's5003_infodpsperante_lista': s5003_infodpsperante_lista,
            's5003_dpsperante_lista': s5003_dpsperante_lista,
        }

        t = get_template('s5003_evtbasesfgts.xml')
        xml = t.render(context)
        return xml


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s5003_evtbasesfgts = get_object_or_404(
        s5003evtBasesFGTS,
        id=pk)

    if s5003_evtbasesfgts.arquivo_original:
    
        xml = ler_arquivo(s5003_evtbasesfgts.arquivo)

    else:
        xml = gerar_xml_s5003(request, pk)

    if 'Signature' in xml:
    
        xml_assinado = xml

    else:

        if not s5003_evtbasesfgts.transmissor_lote_esocial:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_esocial \
                import vincular_transmissor_esocial, criar_transmissor_esocial, get_grupo

            grupo = get_grupo(s5003evtBasesFGTS)

            criar_transmissor_esocial(request,
                grupo,
                s5003_evtbasesfgts.nrinsc,
                s5003_evtbasesfgts.tpinsc)

            vincular_transmissor_esocial(request,
                grupo,
                s5003evtBasesFGTS,
                s5003_evtbasesfgts)
        
        s5003_evtbasesfgts = get_object_or_404(
            s5003evtBasesFGTS,
            id=pk)
        
        xml_assinado = assinar_esocial(
            request, 
            xml, 
            s5003_evtbasesfgts.transmissor_lote_esocial_id)
        
    if s5003_evtbasesfgts.status in (
        STATUS_EVENTO_CADASTRADO,
        STATUS_EVENTO_IMPORTADO,
        STATUS_EVENTO_DUPLICADO,
        STATUS_EVENTO_GERADO):

        s5003evtBasesFGTS.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    arquivo = 'arquivos/Eventos/s5003_evtbasesfgts/%s.xml' % (s5003_evtbasesfgts.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s5003_evtbasesfgts/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):
    
        salvar_arquivo_esocial(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)
    
    return xml_assinado


@login_required
def gerar_xml(request, pk):

    if pk:

        xml_assinado = gerar_xml_assinado(request, pk)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.now(),}
    
    return render(request, 'permissao_negada.html', context)