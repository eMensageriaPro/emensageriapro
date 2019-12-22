# eMensageriaAI #
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
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from emensageriapro.padrao import *
from emensageriapro.efdreinf.models import *
from emensageriapro.r2020.forms import *
from emensageriapro.functions import get_xmlns


from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def gerar_xml_r2020_func(pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    r2020_evtservprest = get_object_or_404(
        r2020evtServPrest,
        id=pk)

    if not versao or versao == '|':
        versao = r2020_evtservprest.versao

    evento = 'r2020evtServPrest'[5:]
    arquivo = '/xsd/efdreinf/%s/%s.xsd' % (versao, evento)

    import os.path

    if os.path.isfile(BASE_DIR + arquivo):

        xmlns = get_xmlns(arquivo)

    else:

        xmlns = ''

    r2020_evtservprest_lista = r2020evtServPrest.objects. \
        filter(id=pk).all()


    r2020_nfs_lista = r2020nfs.objects. \
        filter(r2020_evtservprest_id__in=listar_ids(r2020_evtservprest_lista)).all()

    r2020_infotpserv_lista = r2020infoTpServ.objects. \
        filter(r2020_nfs_id__in=listar_ids(r2020_nfs_lista)).all()

    r2020_infoprocretpr_lista = r2020infoProcRetPr.objects. \
        filter(r2020_evtservprest_id__in=listar_ids(r2020_evtservprest_lista)).all()

    r2020_infoprocretad_lista = r2020infoProcRetAd.objects. \
        filter(r2020_evtservprest_id__in=listar_ids(r2020_evtservprest_lista)).all()


    context = {
        'xmlns': xmlns,
        'versao': versao,
        'base': r2020_evtservprest,
        'r2020_evtservprest_lista': r2020_evtservprest_lista,
        'pk': int(pk),
        'r2020_evtservprest': r2020_evtservprest,
        'r2020_nfs_lista': r2020_nfs_lista,
        'r2020_infotpserv_lista': r2020_infotpserv_lista,
        'r2020_infoprocretpr_lista': r2020_infoprocretpr_lista,
        'r2020_infoprocretad_lista': r2020_infoprocretad_lista,
    }

    t = get_template('r2020_evtservprest.xml')
    xml = t.render(context)
    return xml



def gerar_xml_r2020(request, pk, versao=None):

    r2020_evtservprest = get_object_or_404(
        r2020evtServPrest,
        id=pk)

    return gerar_xml_r2020_func(pk, versao)


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes import salvar_arquivo_efdreinf
    from emensageriapro.mensageiro.functions.funcoes_efdreinf import assinar_efdreinf

    r2020_evtservprest = get_object_or_404(
        r2020evtServPrest, id=pk)

    if not r2020_evtservprest.identidade:
        from emensageriapro.functions import identidade_evento
        ident = identidade_evento(r2020_evtservprest, 'efdreinf')
        r2020_evtservprest = get_object_or_404(r2020evtServPrest, id=pk)

    if r2020_evtservprest.arquivo_original:
        xml = ler_arquivo(r2020_evtservprest.arquivo)

    else:
        xml = gerar_xml_r2020(request, pk)

    STATUS_ANT = [
            STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO,
            STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO
    ]

    if 'Signature' in xml and r2020_evtservprest.status in STATUS_ANT:

        xml_assinado = xml
        r2020evtServPrest.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    else:

        if not r2020_evtservprest.transmissor_lote_efdreinf:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_efdreinf \
                import vincular_transmissor_efdreinf, criar_transmissor_efdreinf, get_grupo

            grupo = get_grupo(r2020evtServPrest)

            criar_transmissor_efdreinf(request,
                grupo,
                r2020_evtservprest.nrinsc,
                r2020_evtservprest.tpinsc)

            vincular_transmissor_efdreinf(request,
                grupo,
                r2020evtServPrest,
                r2020_evtservprest)

        r2020_evtservprest = get_object_or_404(
            r2020evtServPrest,
            id=pk)

        xml_assinado = assinar_efdreinf(
            request,
            xml,
            r2020_evtservprest.transmissor_lote_efdreinf_id)


        if 'Signature' in xml_assinado and r2020_evtservprest.status in STATUS_ANT:

            r2020evtServPrest.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

        elif s1000evtInfoEmpregador.status in STATUS_ANT:

            r2020evtServPrest.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_GERADO)

    arquivo = '/arquivos/Eventos/r2020_evtservprest/%s.xml' % (r2020_evtservprest.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r2020_evtservprest/' % BASE_DIR)

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