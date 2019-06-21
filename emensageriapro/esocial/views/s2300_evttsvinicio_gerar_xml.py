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
from emensageriapro.s2300.models import *
from emensageriapro.s2300.forms import *
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


def gerar_xml_s2300(request, pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    if pk:

        s2300_evttsvinicio = get_object_or_404(
            s2300evtTSVInicio,
            id=pk)

        if not versao or versao == '|':
            versao = s2300_evttsvinicio.versao

        evento = 's2300evtTSVInicio'[5:]
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

        s2300_evttsvinicio_lista = s2300evtTSVInicio.objects. \
            filter(id=pk).all()
            
        
        s2300_documentos_lista = s2300documentos.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_ctps_lista = s2300CTPS.objects. \
            filter(s2300_documentos_id__in=listar_ids(s2300_documentos_lista)).all()
        
        s2300_ric_lista = s2300RIC.objects. \
            filter(s2300_documentos_id__in=listar_ids(s2300_documentos_lista)).all()
        
        s2300_rg_lista = s2300RG.objects. \
            filter(s2300_documentos_id__in=listar_ids(s2300_documentos_lista)).all()
        
        s2300_rne_lista = s2300RNE.objects. \
            filter(s2300_documentos_id__in=listar_ids(s2300_documentos_lista)).all()
        
        s2300_oc_lista = s2300OC.objects. \
            filter(s2300_documentos_id__in=listar_ids(s2300_documentos_lista)).all()
        
        s2300_cnh_lista = s2300CNH.objects. \
            filter(s2300_documentos_id__in=listar_ids(s2300_documentos_lista)).all()
        
        s2300_brasil_lista = s2300brasil.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_exterior_lista = s2300exterior.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_trabestrangeiro_lista = s2300trabEstrangeiro.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_infodeficiencia_lista = s2300infoDeficiencia.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_dependente_lista = s2300dependente.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_contato_lista = s2300contato.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_infocomplementares_lista = s2300infoComplementares.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_cargofuncao_lista = s2300cargoFuncao.objects. \
            filter(s2300_infocomplementares_id__in=listar_ids(s2300_infocomplementares_lista)).all()
        
        s2300_remuneracao_lista = s2300remuneracao.objects. \
            filter(s2300_infocomplementares_id__in=listar_ids(s2300_infocomplementares_lista)).all()
        
        s2300_fgts_lista = s2300fgts.objects. \
            filter(s2300_infocomplementares_id__in=listar_ids(s2300_infocomplementares_lista)).all()
        
        s2300_infodirigentesindical_lista = s2300infoDirigenteSindical.objects. \
            filter(s2300_infocomplementares_id__in=listar_ids(s2300_infocomplementares_lista)).all()
        
        s2300_infotrabcedido_lista = s2300infoTrabCedido.objects. \
            filter(s2300_infocomplementares_id__in=listar_ids(s2300_infocomplementares_lista)).all()
        
        s2300_infoestagiario_lista = s2300infoEstagiario.objects. \
            filter(s2300_infocomplementares_id__in=listar_ids(s2300_infocomplementares_lista)).all()
        
        s2300_ageintegracao_lista = s2300ageIntegracao.objects. \
            filter(s2300_infoestagiario_id__in=listar_ids(s2300_infoestagiario_lista)).all()
        
        s2300_supervisorestagio_lista = s2300supervisorEstagio.objects. \
            filter(s2300_infoestagiario_id__in=listar_ids(s2300_infoestagiario_lista)).all()
        
        s2300_mudancacpf_lista = s2300mudancaCPF.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_afastamento_lista = s2300afastamento.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        
        s2300_termino_lista = s2300termino.objects. \
            filter(s2300_evttsvinicio_id__in=listar_ids(s2300_evttsvinicio_lista)).all()
        

        context = {
            'xmlns': xmlns,
            'versao': versao,
            'base': s2300_evttsvinicio,
            's2300_evttsvinicio_lista': s2300_evttsvinicio_lista,
            'pk': int(pk),
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
        }

        t = get_template('s2300_evttsvinicio.xml')
        xml = t.render(context)
        return xml


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s2300_evttsvinicio = get_object_or_404(
        s2300evtTSVInicio,
        id=pk)

    if s2300_evttsvinicio.arquivo_original:
    
        xml = ler_arquivo(s2300_evttsvinicio.arquivo)

    else:
        xml = gerar_xml_s2300(request, pk)

    if 'Signature' in xml:
    
        xml_assinado = xml

    else:

        if not s2300_evttsvinicio.transmissor_lote_esocial:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_esocial \
                import vincular_transmissor_esocial, criar_transmissor_esocial, get_grupo

            grupo = get_grupo(s2300evtTSVInicio)

            criar_transmissor_esocial(request,
                grupo,
                s2300_evttsvinicio.nrinsc,
                s2300_evttsvinicio.tpinsc)

            vincular_transmissor_esocial(request,
                grupo,
                s2300evtTSVInicio,
                s2300_evttsvinicio)
        
        s2300_evttsvinicio = get_object_or_404(
            s2300evtTSVInicio,
            id=pk)
        
        xml_assinado = assinar_esocial(
            request, 
            xml, 
            s2300_evttsvinicio.transmissor_lote_esocial_id)
        
    if s2300_evttsvinicio.status in (
        STATUS_EVENTO_CADASTRADO,
        STATUS_EVENTO_IMPORTADO,
        STATUS_EVENTO_DUPLICADO,
        STATUS_EVENTO_GERADO):

        s2300evtTSVInicio.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    arquivo = 'arquivos/Eventos/s2300_evttsvinicio/%s.xml' % (s2300_evttsvinicio.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s2300_evttsvinicio/' % BASE_DIR)

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