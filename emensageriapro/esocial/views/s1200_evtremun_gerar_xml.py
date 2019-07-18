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
from emensageriapro.esocial.models import *
from emensageriapro.s1200.forms import *
from emensageriapro.functions import get_xmlns


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def gerar_xml_s1200_func(pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    s1200_evtremun = get_object_or_404(
        s1200evtRemun,
        id=pk)

    if not versao or versao == '|':
        versao = s1200_evtremun.versao

    evento = 's1200evtRemun'[5:]
    arquivo = '/xsd/esocial/%s/%s.xsd' % (versao, evento)

    import os.path

    if os.path.isfile(BASE_DIR + arquivo):

        xmlns = get_xmlns(arquivo)

    else:

        xmlns = ''

    s1200_evtremun_lista = s1200evtRemun.objects. \
        filter(id=pk).all()


    s1200_infomv_lista = s1200infoMV.objects. \
        filter(s1200_evtremun_id__in=listar_ids(s1200_evtremun_lista)).all()

    s1200_remunoutrempr_lista = s1200remunOutrEmpr.objects. \
        filter(s1200_infomv_id__in=listar_ids(s1200_infomv_lista)).all()

    s1200_infocomplem_lista = s1200infoComplem.objects. \
        filter(s1200_evtremun_id__in=listar_ids(s1200_evtremun_lista)).all()

    s1200_sucessaovinc_lista = s1200sucessaoVinc.objects. \
        filter(s1200_infocomplem_id__in=listar_ids(s1200_infocomplem_lista)).all()

    s1200_procjudtrab_lista = s1200procJudTrab.objects. \
        filter(s1200_evtremun_id__in=listar_ids(s1200_evtremun_lista)).all()

    s1200_infointerm_lista = s1200infoInterm.objects. \
        filter(s1200_evtremun_id__in=listar_ids(s1200_evtremun_lista)).all()

    s1200_dmdev_lista = s1200dmDev.objects. \
        filter(s1200_evtremun_id__in=listar_ids(s1200_evtremun_lista)).all()

    s1200_infoperapur_lista = s1200infoPerApur.objects. \
        filter(s1200_dmdev_id__in=listar_ids(s1200_dmdev_lista)).all()

    s1200_infoperapur_ideestablot_lista = s1200infoPerApurideEstabLot.objects. \
        filter(s1200_infoperapur_id__in=listar_ids(s1200_infoperapur_lista)).all()

    s1200_infoperapur_remunperapur_lista = s1200infoPerApurremunPerApur.objects. \
        filter(s1200_infoperapur_ideestablot_id__in=listar_ids(s1200_infoperapur_ideestablot_lista)).all()

    s1200_infoperapur_itensremun_lista = s1200infoPerApuritensRemun.objects. \
        filter(s1200_infoperapur_remunperapur_id__in=listar_ids(s1200_infoperapur_remunperapur_lista)).all()

    s1200_infoperapur_infosaudecolet_lista = s1200infoPerApurinfoSaudeColet.objects. \
        filter(s1200_infoperapur_remunperapur_id__in=listar_ids(s1200_infoperapur_remunperapur_lista)).all()

    s1200_infoperapur_detoper_lista = s1200infoPerApurdetOper.objects. \
        filter(s1200_infoperapur_infosaudecolet_id__in=listar_ids(s1200_infoperapur_infosaudecolet_lista)).all()

    s1200_infoperapur_detplano_lista = s1200infoPerApurdetPlano.objects. \
        filter(s1200_infoperapur_detoper_id__in=listar_ids(s1200_infoperapur_detoper_lista)).all()

    s1200_infoperapur_infoagnocivo_lista = s1200infoPerApurinfoAgNocivo.objects. \
        filter(s1200_infoperapur_remunperapur_id__in=listar_ids(s1200_infoperapur_remunperapur_lista)).all()

    s1200_infoperapur_infotrabinterm_lista = s1200infoPerApurinfoTrabInterm.objects. \
        filter(s1200_infoperapur_remunperapur_id__in=listar_ids(s1200_infoperapur_remunperapur_lista)).all()

    s1200_infoperant_lista = s1200infoPerAnt.objects. \
        filter(s1200_dmdev_id__in=listar_ids(s1200_dmdev_lista)).all()

    s1200_infoperant_ideadc_lista = s1200infoPerAntideADC.objects. \
        filter(s1200_infoperant_id__in=listar_ids(s1200_infoperant_lista)).all()

    s1200_infoperant_ideperiodo_lista = s1200infoPerAntidePeriodo.objects. \
        filter(s1200_infoperant_ideadc_id__in=listar_ids(s1200_infoperant_ideadc_lista)).all()

    s1200_infoperant_ideestablot_lista = s1200infoPerAntideEstabLot.objects. \
        filter(s1200_infoperant_ideperiodo_id__in=listar_ids(s1200_infoperant_ideperiodo_lista)).all()

    s1200_infoperant_remunperant_lista = s1200infoPerAntremunPerAnt.objects. \
        filter(s1200_infoperant_ideestablot_id__in=listar_ids(s1200_infoperant_ideestablot_lista)).all()

    s1200_infoperant_itensremun_lista = s1200infoPerAntitensRemun.objects. \
        filter(s1200_infoperant_remunperant_id__in=listar_ids(s1200_infoperant_remunperant_lista)).all()

    s1200_infoperant_infoagnocivo_lista = s1200infoPerAntinfoAgNocivo.objects. \
        filter(s1200_infoperant_remunperant_id__in=listar_ids(s1200_infoperant_remunperant_lista)).all()

    s1200_infoperant_infotrabinterm_lista = s1200infoPerAntinfoTrabInterm.objects. \
        filter(s1200_infoperant_remunperant_id__in=listar_ids(s1200_infoperant_remunperant_lista)).all()

    s1200_infoperant_infocomplcont_lista = s1200infoPerAntinfoComplCont.objects. \
        filter(s1200_dmdev_id__in=listar_ids(s1200_dmdev_lista)).all()


    context = {
        'xmlns': xmlns,
        'versao': versao,
        'base': s1200_evtremun,
        's1200_evtremun_lista': s1200_evtremun_lista,
        'pk': int(pk),
        's1200_evtremun': s1200_evtremun,
        's1200_infomv_lista': s1200_infomv_lista,
        's1200_remunoutrempr_lista': s1200_remunoutrempr_lista,
        's1200_infocomplem_lista': s1200_infocomplem_lista,
        's1200_sucessaovinc_lista': s1200_sucessaovinc_lista,
        's1200_procjudtrab_lista': s1200_procjudtrab_lista,
        's1200_infointerm_lista': s1200_infointerm_lista,
        's1200_dmdev_lista': s1200_dmdev_lista,
        's1200_infoperapur_lista': s1200_infoperapur_lista,
        's1200_infoperapur_ideestablot_lista': s1200_infoperapur_ideestablot_lista,
        's1200_infoperapur_remunperapur_lista': s1200_infoperapur_remunperapur_lista,
        's1200_infoperapur_itensremun_lista': s1200_infoperapur_itensremun_lista,
        's1200_infoperapur_infosaudecolet_lista': s1200_infoperapur_infosaudecolet_lista,
        's1200_infoperapur_detoper_lista': s1200_infoperapur_detoper_lista,
        's1200_infoperapur_detplano_lista': s1200_infoperapur_detplano_lista,
        's1200_infoperapur_infoagnocivo_lista': s1200_infoperapur_infoagnocivo_lista,
        's1200_infoperapur_infotrabinterm_lista': s1200_infoperapur_infotrabinterm_lista,
        's1200_infoperant_lista': s1200_infoperant_lista,
        's1200_infoperant_ideadc_lista': s1200_infoperant_ideadc_lista,
        's1200_infoperant_ideperiodo_lista': s1200_infoperant_ideperiodo_lista,
        's1200_infoperant_ideestablot_lista': s1200_infoperant_ideestablot_lista,
        's1200_infoperant_remunperant_lista': s1200_infoperant_remunperant_lista,
        's1200_infoperant_itensremun_lista': s1200_infoperant_itensremun_lista,
        's1200_infoperant_infoagnocivo_lista': s1200_infoperant_infoagnocivo_lista,
        's1200_infoperant_infotrabinterm_lista': s1200_infoperant_infotrabinterm_lista,
        's1200_infoperant_infocomplcont_lista': s1200_infoperant_infocomplcont_lista,
    }

    t = get_template('s1200_evtremun.xml')
    xml = t.render(context)
    return xml



def gerar_xml_s1200(request, pk, versao=None):

    s1200_evtremun = get_object_or_404(
        s1200evtRemun,
        id=pk)

    return gerar_xml_s1200_func(pk, versao)


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes import salvar_arquivo_esocial
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s1200_evtremun = get_object_or_404(
        s1200evtRemun, id=pk)

    if not s1200_evtremun.identidade:
        from emensageriapro.functions import identidade_evento
        ident = identidade_evento(s1200_evtremun, 'esocial')
        s1200_evtremun = get_object_or_404(s1200evtRemun, id=pk)

    if s1200_evtremun.arquivo_original:
        xml = ler_arquivo(s1200_evtremun.arquivo)

    else:
        xml = gerar_xml_s1200(request, pk)

    STATUS_ANT = [
            STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO,
            STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO
    ]

    if 'Signature' in xml and s1200_evtremun.status in STATUS_ANT:

        xml_assinado = xml
        s1200evtRemun.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    else:

        if not s1200_evtremun.transmissor_lote_esocial:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_esocial \
                import vincular_transmissor_esocial, criar_transmissor_esocial, get_grupo

            grupo = get_grupo(s1200evtRemun)

            criar_transmissor_esocial(request,
                grupo,
                s1200_evtremun.nrinsc,
                s1200_evtremun.tpinsc)

            vincular_transmissor_esocial(request,
                grupo,
                s1200evtRemun,
                s1200_evtremun)

        s1200_evtremun = get_object_or_404(
            s1200evtRemun,
            id=pk)

        xml_assinado = assinar_esocial(
            request,
            xml,
            s1200_evtremun.transmissor_lote_esocial_id)


        if 'Signature' in xml_assinado and s1200_evtremun.status in STATUS_ANT:

            s1200evtRemun.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

        elif s1000evtInfoEmpregador.status in STATUS_ANT:

            s1200evtRemun.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_GERADO)

    arquivo = '/arquivos/Eventos/s1200_evtremun/%s.xml' % (s1200_evtremun.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s1200_evtremun/' % BASE_DIR)

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