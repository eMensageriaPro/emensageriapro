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
from emensageriapro.r2060.models import *
from emensageriapro.r2060.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from django.template.loader import get_template
from emensageriapro.functions import get_xmlns


from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def gerar_xml_r2060(request, pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    if pk:

        r2060_evtcprb = get_object_or_404(
            r2060evtCPRB,
            id=pk)

        if not versao or versao == '|':
            versao = r2060_evtcprb.versao

        evento = 'r2060evtCPRB'[5:]
        arquivo = 'xsd/efdreinf/%s/%s.xsd' % (versao, evento)

        import os.path

        if os.path.isfile(BASE_DIR + '/' + arquivo):

            xmlns = get_xmlns(arquivo)

        else:
        
            from django.contrib import messages

            messages.warning(request, '''
                Não foi capturar o XMLNS pois o XSD do 
                evento não está contido na pasta!''')

            xmlns = ''

        r2060_evtcprb_lista = r2060evtCPRB.objects. \
            filter(id=pk).all()
            
        
        r2060_tipocod_lista = r2060tipoCod.objects. \
            filter(r2060_evtcprb_id__in=listar_ids(r2060_evtcprb_lista)).all()
        
        r2060_tipoajuste_lista = r2060tipoAjuste.objects. \
            filter(r2060_tipocod_id__in=listar_ids(r2060_tipocod_lista)).all()
        
        r2060_infoproc_lista = r2060infoProc.objects. \
            filter(r2060_tipocod_id__in=listar_ids(r2060_tipocod_lista)).all()
        

        context = {
            'xmlns': xmlns,
            'versao': versao,
            'base': r2060_evtcprb,
            'r2060_evtcprb_lista': r2060_evtcprb_lista,
            'pk': int(pk),
            'r2060_evtcprb': r2060_evtcprb,
            'r2060_tipocod_lista': r2060_tipocod_lista,
            'r2060_tipoajuste_lista': r2060_tipoajuste_lista,
            'r2060_infoproc_lista': r2060_infoproc_lista,
        }

        t = get_template('r2060_evtcprb.xml')
        xml = t.render(context)
        return xml


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_efdreinf import salvar_arquivo_efdreinf
    from emensageriapro.mensageiro.functions.funcoes_efdreinf import assinar_efdreinf

    r2060_evtcprb = get_object_or_404(
        r2060evtCPRB,
        id=pk)

    if r2060_evtcprb.arquivo_original:
    
        xml = ler_arquivo(r2060_evtcprb.arquivo)

    else:
        xml = gerar_xml_r2060(request, pk)

    if 'Signature' in xml:
    
        xml_assinado = xml

    else:

        if not r2060_evtcprb.transmissor_lote_efdreinf:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_efdreinf \
                import vincular_transmissor_efdreinf, criar_transmissor_efdreinf, get_grupo

            grupo = get_grupo(r2060evtCPRB)

            criar_transmissor_efdreinf(request,
                grupo,
                r2060_evtcprb.nrinsc,
                r2060_evtcprb.tpinsc)

            vincular_transmissor_efdreinf(request,
                grupo,
                r2060evtCPRB,
                r2060_evtcprb)
        
        r2060_evtcprb = get_object_or_404(
            r2060evtCPRB,
            id=pk)
        
        xml_assinado = assinar_efdreinf(
            request, 
            xml, 
            r2060_evtcprb.transmissor_lote_efdreinf_id)
        
    if r2060_evtcprb.status in (
        STATUS_EVENTO_CADASTRADO,
        STATUS_EVENTO_IMPORTADO,
        STATUS_EVENTO_DUPLICADO,
        STATUS_EVENTO_GERADO):

        r2060evtCPRB.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    arquivo = 'arquivos/Eventos/r2060_evtcprb/%s.xml' % (r2060_evtcprb.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r2060_evtcprb/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):
    
        salvar_arquivo_efdreinf(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)
    
    return xml_assinado


@login_required
def gerar_xml(request, pk):

    if pk:

        xml_assinado = gerar_xml_assinado(request, pk)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.now(),}
    
    return render(request, 'permissao_negada.html', context)