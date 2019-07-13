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
from emensageriapro.s1260.models import *
from emensageriapro.s1260.forms import *
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


def gerar_xml_s1260_func(pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    s1260_evtcomprod = get_object_or_404(
        s1260evtComProd,
        id=pk)

    if not versao or versao == '|':
        versao = s1260_evtcomprod.versao

    evento = 's1260evtComProd'[5:]
    arquivo = '/xsd/esocial/%s/%s.xsd' % (versao, evento)

    import os.path

    if os.path.isfile(BASE_DIR + arquivo):

        xmlns = get_xmlns(arquivo)

    else:

        xmlns = ''

    s1260_evtcomprod_lista = s1260evtComProd.objects. \
        filter(id=pk).all()


    s1260_tpcomerc_lista = s1260tpComerc.objects. \
        filter(s1260_evtcomprod_id__in=listar_ids(s1260_evtcomprod_lista)).all()

    s1260_ideadquir_lista = s1260ideAdquir.objects. \
        filter(s1260_tpcomerc_id__in=listar_ids(s1260_tpcomerc_lista)).all()

    s1260_nfs_lista = s1260nfs.objects. \
        filter(s1260_ideadquir_id__in=listar_ids(s1260_ideadquir_lista)).all()

    s1260_infoprocjud_lista = s1260infoProcJud.objects. \
        filter(s1260_tpcomerc_id__in=listar_ids(s1260_tpcomerc_lista)).all()


    context = {
        'xmlns': xmlns,
        'versao': versao,
        'base': s1260_evtcomprod,
        's1260_evtcomprod_lista': s1260_evtcomprod_lista,
        'pk': int(pk),
        's1260_evtcomprod': s1260_evtcomprod,
        's1260_tpcomerc_lista': s1260_tpcomerc_lista,
        's1260_ideadquir_lista': s1260_ideadquir_lista,
        's1260_nfs_lista': s1260_nfs_lista,
        's1260_infoprocjud_lista': s1260_infoprocjud_lista,
    }

    t = get_template('s1260_evtcomprod.xml')
    xml = t.render(context)
    return xml



def gerar_xml_s1260(request, pk, versao=None):

    from emensageriapro.settings import BASE_DIR
    s1260_evtcomprod = get_object_or_404(
        s1260evtComProd,
        id=pk)
    return gerar_xml_s1260_func(pk, versao)


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes import salvar_arquivo_esocial
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s1260_evtcomprod = get_object_or_404(
        s1260evtComProd, id=pk)

    if not s1260_evtcomprod.identidade:
        from emensageriapro.functions import identidade_evento
        ident = identidade_evento(s1260_evtcomprod)
        s1260_evtcomprod = get_object_or_404(s1260evtComProd, id=pk)

    if s1260_evtcomprod.arquivo_original:
        xml = ler_arquivo(s1260_evtcomprod.arquivo)

    else:
        xml = gerar_xml_s1260(request, pk)

    if 'Signature' in xml:
        xml_assinado = xml
        s1260evtComProd.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    else:

        if not s1260_evtcomprod.transmissor_lote_esocial:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_esocial \
                import vincular_transmissor_esocial, criar_transmissor_esocial, get_grupo

            grupo = get_grupo(s1260evtComProd)

            criar_transmissor_esocial(request,
                grupo,
                s1260_evtcomprod.nrinsc,
                s1260_evtcomprod.tpinsc)

            vincular_transmissor_esocial(request,
                grupo,
                s1260evtComProd,
                s1260_evtcomprod)

        s1260_evtcomprod = get_object_or_404(
            s1260evtComProd,
            id=pk)

        xml_assinado = assinar_esocial(
            request,
            xml,
            s1260_evtcomprod.transmissor_lote_esocial_id)

        if 'Signature' in xml_assinado:

            s1260evtComProd.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)
        else:

            s1260evtComProd.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_GERADO)

    arquivo = '/arquivos/Eventos/s1260_evtcomprod/%s.xml' % (s1260_evtcomprod.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s1260_evtcomprod/' % BASE_DIR)

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