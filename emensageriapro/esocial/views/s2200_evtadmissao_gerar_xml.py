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
from emensageriapro.s2200.models import *
from emensageriapro.s2200.forms import *
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


def gerar_xml_s2200(request, pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    if pk:

        s2200_evtadmissao = get_object_or_404(
            s2200evtAdmissao,
            id=pk)

        if not versao or versao == '|':
            versao = s2200_evtadmissao.versao

        evento = 's2200evtAdmissao'[5:]
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

        s2200_evtadmissao_lista = s2200evtAdmissao.objects. \
            filter(id=pk).all()


        s2200_documentos_lista = s2200documentos.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_ctps_lista = s2200CTPS.objects. \
            filter(s2200_documentos_id__in=listar_ids(s2200_documentos_lista)).all()

        s2200_ric_lista = s2200RIC.objects. \
            filter(s2200_documentos_id__in=listar_ids(s2200_documentos_lista)).all()

        s2200_rg_lista = s2200RG.objects. \
            filter(s2200_documentos_id__in=listar_ids(s2200_documentos_lista)).all()

        s2200_rne_lista = s2200RNE.objects. \
            filter(s2200_documentos_id__in=listar_ids(s2200_documentos_lista)).all()

        s2200_oc_lista = s2200OC.objects. \
            filter(s2200_documentos_id__in=listar_ids(s2200_documentos_lista)).all()

        s2200_cnh_lista = s2200CNH.objects. \
            filter(s2200_documentos_id__in=listar_ids(s2200_documentos_lista)).all()

        s2200_brasil_lista = s2200brasil.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_exterior_lista = s2200exterior.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_trabestrangeiro_lista = s2200trabEstrangeiro.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_infodeficiencia_lista = s2200infoDeficiencia.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_dependente_lista = s2200dependente.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_aposentadoria_lista = s2200aposentadoria.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_contato_lista = s2200contato.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_infoceletista_lista = s2200infoCeletista.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_trabtemporario_lista = s2200trabTemporario.objects. \
            filter(s2200_infoceletista_id__in=listar_ids(s2200_infoceletista_lista)).all()

        s2200_ideestabvinc_lista = s2200ideEstabVinc.objects. \
            filter(s2200_trabtemporario_id__in=listar_ids(s2200_trabtemporario_lista)).all()

        s2200_idetrabsubstituido_lista = s2200ideTrabSubstituido.objects. \
            filter(s2200_trabtemporario_id__in=listar_ids(s2200_trabtemporario_lista)).all()

        s2200_aprend_lista = s2200aprend.objects. \
            filter(s2200_infoceletista_id__in=listar_ids(s2200_infoceletista_lista)).all()

        s2200_infoestatutario_lista = s2200infoEstatutario.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_infodecjud_lista = s2200infoDecJud.objects. \
            filter(s2200_infoestatutario_id__in=listar_ids(s2200_infoestatutario_lista)).all()

        s2200_localtrabgeral_lista = s2200localTrabGeral.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_localtrabdom_lista = s2200localTrabDom.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_horcontratual_lista = s2200horContratual.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_horario_lista = s2200horario.objects. \
            filter(s2200_horcontratual_id__in=listar_ids(s2200_horcontratual_lista)).all()

        s2200_filiacaosindical_lista = s2200filiacaoSindical.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_alvarajudicial_lista = s2200alvaraJudicial.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_observacoes_lista = s2200observacoes.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_sucessaovinc_lista = s2200sucessaoVinc.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_transfdom_lista = s2200transfDom.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_mudancacpf_lista = s2200mudancaCPF.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_afastamento_lista = s2200afastamento.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_desligamento_lista = s2200desligamento.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()

        s2200_cessao_lista = s2200cessao.objects. \
            filter(s2200_evtadmissao_id__in=listar_ids(s2200_evtadmissao_lista)).all()


        context = {
            'xmlns': xmlns,
            'versao': versao,
            'base': s2200_evtadmissao,
            's2200_evtadmissao_lista': s2200_evtadmissao_lista,
            'pk': int(pk),
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
            's2200_mudancacpf_lista': s2200_mudancacpf_lista,
            's2200_afastamento_lista': s2200_afastamento_lista,
            's2200_desligamento_lista': s2200_desligamento_lista,
            's2200_cessao_lista': s2200_cessao_lista,
        }

        t = get_template('s2200_evtadmissao.xml')
        xml = t.render(context)
        return xml


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s2200_evtadmissao = get_object_or_404(
        s2200evtAdmissao,
        id=pk)

    if s2200_evtadmissao.arquivo_original:

        xml = ler_arquivo(s2200_evtadmissao.arquivo)

    else:
        xml = gerar_xml_s2200(request, pk)

    if 'Signature' in xml:

        xml_assinado = xml

    else:

        if not s2200_evtadmissao.transmissor_lote_esocial:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_esocial \
                import vincular_transmissor_esocial, criar_transmissor_esocial, get_grupo

            grupo = get_grupo(s2200evtAdmissao)

            criar_transmissor_esocial(request,
                grupo,
                s2200_evtadmissao.nrinsc,
                s2200_evtadmissao.tpinsc)

            vincular_transmissor_esocial(request,
                grupo,
                s2200evtAdmissao,
                s2200_evtadmissao)

        s2200_evtadmissao = get_object_or_404(
            s2200evtAdmissao,
            id=pk)

        xml_assinado = assinar_esocial(
            request,
            xml,
            s2200_evtadmissao.transmissor_lote_esocial_id)

    if s2200_evtadmissao.status in (
        STATUS_EVENTO_CADASTRADO,
        STATUS_EVENTO_IMPORTADO,
        STATUS_EVENTO_DUPLICADO,
        STATUS_EVENTO_GERADO):

        s2200evtAdmissao.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    arquivo = 'arquivos/Eventos/s2200_evtadmissao/%s.xml' % (s2200_evtadmissao.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s2200_evtadmissao/' % BASE_DIR)

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