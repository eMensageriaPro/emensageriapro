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
from emensageriapro.r9001.models import *
from emensageriapro.r9001.forms import *
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


def gerar_xml_r9001(request, r9001_evttotal_id, versao=None):

    from django.template.loader import get_template
    from emensageriapro.functions import get_xmlns

    if r9001_evttotal_id:

        r9001_evttotal = get_object_or_404(
            r9001evtTotal,
            excluido = False,
            id = r9001_evttotal_id)

        if not versao or versao == '|':
            versao = r9001_evttotal.versao

        evento = 'r9001evtTotal'[5:]
        arquivo = 'xsd/efdreinf/%s/%s.xsd' % (versao, evento)

        import os.path

        if os.path.isfile(arquivo):

            xmlns = get_xmlns(arquivo)

        else:
        
            from django.contrib import messages

            messages.warning(request, '''
                Não foi capturar o XMLNS pois o XSD do 
                evento não está contido na pasta!''')

            xmlns = ''

        r9001_evttotal_lista = r9001evtTotal.objects. \
            filter(id=r9001_evttotal_id, excluido = False).all()
        
        r9001_regocorrs_lista = r9001regOcorrs.objects. \
            filter(r9001_evttotal_id__in=listar_ids(r9001_evttotal_lista)).all()
        
        r9001_infototal_lista = r9001infoTotal.objects. \
            filter(r9001_evttotal_id__in=listar_ids(r9001_evttotal_lista)).all()
        
        r9001_rtom_lista = r9001RTom.objects. \
            filter(r9001_infototal_id__in=listar_ids(r9001_infototal_lista)).all()
        
        r9001_infocrtom_lista = r9001infoCRTom.objects. \
            filter(r9001_rtom_id__in=listar_ids(r9001_rtom_lista)).all()
        
        r9001_rprest_lista = r9001RPrest.objects. \
            filter(r9001_infototal_id__in=listar_ids(r9001_infototal_lista)).all()
        
        r9001_rrecrepad_lista = r9001RRecRepAD.objects. \
            filter(r9001_infototal_id__in=listar_ids(r9001_infototal_lista)).all()
        
        r9001_rcoml_lista = r9001RComl.objects. \
            filter(r9001_infototal_id__in=listar_ids(r9001_infototal_lista)).all()
        
        r9001_rcprb_lista = r9001RCPRB.objects. \
            filter(r9001_infototal_id__in=listar_ids(r9001_infototal_lista)).all()
        
        r9001_rrecespetdesp_lista = r9001RRecEspetDesp.objects. \
            filter(r9001_infototal_id__in=listar_ids(r9001_infototal_lista)).all()
        
        r9001_evttotal_lista = r9001evtTotal.objects. \
            filter(retornos_r9001_id__in=listar_ids(r9001_evttotal_lista)).all()
        

        context = {
            'xmlns': xmlns,
            'versao': versao,
            'base': r9001_evttotal,
            'r9001_evttotal_lista': r9001_evttotal_lista,
            'r9001_evttotal_id': int(r9001_evttotal_id),
            'r9001_evttotal': r9001_evttotal,

            
            'r9001_regocorrs_lista': r9001_regocorrs_lista,
            'r9001_infototal_lista': r9001_infototal_lista,
            'r9001_rtom_lista': r9001_rtom_lista,
            'r9001_infocrtom_lista': r9001_infocrtom_lista,
            'r9001_rprest_lista': r9001_rprest_lista,
            'r9001_rrecrepad_lista': r9001_rrecrepad_lista,
            'r9001_rcoml_lista': r9001_rcoml_lista,
            'r9001_rcprb_lista': r9001_rcprb_lista,
            'r9001_rrecespetdesp_lista': r9001_rrecespetdesp_lista,
            'r9001_evttotal_lista': r9001_evttotal_lista,
        }

        t = get_template('r9001_evttotal.xml')
        xml = t.render(context)
        return xml




def gerar_xml_assinado(request, r9001_evttotal_id):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_efdreinf import salvar_arquivo_efdreinf
    from emensageriapro.mensageiro.functions.funcoes_efdreinf import assinar_efdreinf

    r9001_evttotal = get_object_or_404(
        r9001evtTotal,
        id=r9001_evttotal_id)

    if r9001_evttotal.arquivo_original:
    
        xml = ler_arquivo(r9001_evttotal.arquivo)

    else:
        xml = gerar_xml_r9001(request, r9001_evttotal_id)

    if 'Signature' in xml:
    
        xml_assinado = xml

    else:

        if not r9001_evttotal.transmissor_lote_efdreinf:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_efdreinf \
                import vincular_transmissor_efdreinf, criar_transmissor_efdreinf, get_grupo

            grupo = get_grupo(r9001evtTotal)

            criar_transmissor_efdreinf(request,
                                      grupo,
                                      r9001_evttotal.nrinsc,
                                      r9001_evttotal.tpinsc)

            vincular_transmissor_efdreinf(request,
                                         grupo,
                                         r9001evtTotal,
                                         r9001_evttotal)
        
        r9001_evttotal = get_object_or_404(
            r9001evtTotal,
            id=r9001_evttotal_id)
        
        xml_assinado = assinar_efdreinf(request, xml, r9001_evttotal.transmissor_lote_efdreinf_id)
        
    if r9001_evttotal.status in (
        STATUS_EVENTO_CADASTRADO,
        STATUS_EVENTO_IMPORTADO,
        STATUS_EVENTO_DUPLICADO,
        STATUS_EVENTO_GERADO):

        r9001evtTotal.objects.\
            filter(id=r9001_evttotal_id).update(status=STATUS_EVENTO_ASSINADO)

    arquivo = 'arquivos/Eventos/r9001_evttotal/%s.xml' % (r9001_evttotal.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r9001_evttotal/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):
        salvar_arquivo_efdreinf(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)
    return xml_assinado



@login_required
def gerar_xml(request, hash):

    dict_hash = get_hash_url( hash )
    r9001_evttotal_id = int(dict_hash['id'])

    if r9001_evttotal_id:

        xml_assinado = gerar_xml_assinado(request, r9001_evttotal_id)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.now(),}
    return render(request, 'permissao_negada.html', context)