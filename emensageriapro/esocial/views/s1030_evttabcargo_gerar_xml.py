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
from emensageriapro.s1030.models import *
from emensageriapro.s1030.forms import *
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


def gerar_xml_s1030(request, s1030_evttabcargo_id, versao=None):

    from django.template.loader import get_template
    from emensageriapro.functions import get_xmlns

    if s1030_evttabcargo_id:

        s1030_evttabcargo = get_object_or_404(
            s1030evtTabCargo,
            excluido = False,
            id = s1030_evttabcargo_id)

        if not versao or versao == '|':
            versao = s1030_evttabcargo.versao

        evento = 's1030evtTabCargo'[5:]
        arquivo = 'xsd/esocial/%s/%s.xsd' % (versao, evento)

        import os.path

        if os.path.isfile(arquivo):

            xmlns = get_xmlns(arquivo)

        else:
        
            from django.contrib import messages

            messages.warning(request, '''
                Não foi capturar o XMLNS pois o XSD do 
                evento não está contido na pasta!''')

            xmlns = ''

        s1030_evttabcargo_lista = s1030evtTabCargo.objects. \
            filter(id=s1030_evttabcargo_id, excluido = False).all()
        
        s1030_inclusao_lista = s1030inclusao.objects. \
            filter(s1030_evttabcargo_id__in=listar_ids(s1030_evttabcargo_lista)).all()
        
        s1030_inclusao_cargopublico_lista = s1030inclusaocargoPublico.objects. \
            filter(s1030_inclusao_id__in=listar_ids(s1030_inclusao_lista)).all()
        
        s1030_alteracao_lista = s1030alteracao.objects. \
            filter(s1030_evttabcargo_id__in=listar_ids(s1030_evttabcargo_lista)).all()
        
        s1030_alteracao_cargopublico_lista = s1030alteracaocargoPublico.objects. \
            filter(s1030_alteracao_id__in=listar_ids(s1030_alteracao_lista)).all()
        
        s1030_alteracao_novavalidade_lista = s1030alteracaonovaValidade.objects. \
            filter(s1030_alteracao_id__in=listar_ids(s1030_alteracao_lista)).all()
        
        s1030_exclusao_lista = s1030exclusao.objects. \
            filter(s1030_evttabcargo_id__in=listar_ids(s1030_evttabcargo_lista)).all()
        

        context = {
            'xmlns': xmlns,
            'versao': versao,
            'base': s1030_evttabcargo,
            's1030_evttabcargo_lista': s1030_evttabcargo_lista,
            's1030_evttabcargo_id': int(s1030_evttabcargo_id),
            's1030_evttabcargo': s1030_evttabcargo,

            
            's1030_inclusao_lista': s1030_inclusao_lista,
            's1030_inclusao_cargopublico_lista': s1030_inclusao_cargopublico_lista,
            's1030_alteracao_lista': s1030_alteracao_lista,
            's1030_alteracao_cargopublico_lista': s1030_alteracao_cargopublico_lista,
            's1030_alteracao_novavalidade_lista': s1030_alteracao_novavalidade_lista,
            's1030_exclusao_lista': s1030_exclusao_lista,
        }

        t = get_template('s1030_evttabcargo.xml')
        xml = t.render(context)
        return xml




def gerar_xml_assinado(request, s1030_evttabcargo_id):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s1030_evttabcargo = get_object_or_404(
        s1030evtTabCargo,
        id=s1030_evttabcargo_id)

    if s1030_evttabcargo.arquivo_original:
    
        xml = ler_arquivo(s1030_evttabcargo.arquivo)

    else:
        xml = gerar_xml_s1030(request, s1030_evttabcargo_id)

    if 'Signature' in xml:
    
        xml_assinado = xml

    else:

        if not s1030_evttabcargo.transmissor_lote_esocial:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_esocial \
                import vincular_transmissor_esocial, criar_transmissor_esocial, get_grupo

            grupo = get_grupo(s1030evtTabCargo)

            criar_transmissor_esocial(request,
                                      grupo,
                                      s1030_evttabcargo.nrinsc,
                                      s1030_evttabcargo.tpinsc)

            vincular_transmissor_esocial(request,
                                         grupo,
                                         s1030evtTabCargo,
                                         s1030_evttabcargo)
        
        s1030_evttabcargo = get_object_or_404(
            s1030evtTabCargo,
            id=s1030_evttabcargo_id)
        
        xml_assinado = assinar_esocial(request, xml, s1030_evttabcargo.transmissor_lote_esocial_id)
        
    if s1030_evttabcargo.status in (
        STATUS_EVENTO_CADASTRADO,
        STATUS_EVENTO_IMPORTADO,
        STATUS_EVENTO_DUPLICADO,
        STATUS_EVENTO_GERADO):

        s1030evtTabCargo.objects.\
            filter(id=s1030_evttabcargo_id).update(status=STATUS_EVENTO_ASSINADO)

    arquivo = 'arquivos/Eventos/s1030_evttabcargo/%s.xml' % (s1030_evttabcargo.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s1030_evttabcargo/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):
        salvar_arquivo_esocial(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)
    return xml_assinado



@login_required
def gerar_xml(request, hash):

    dict_hash = get_hash_url( hash )
    s1030_evttabcargo_id = int(dict_hash['id'])

    if s1030_evttabcargo_id:

        xml_assinado = gerar_xml_assinado(request, s1030_evttabcargo_id)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.now(),}
    return render(request, 'permissao_negada.html', context)