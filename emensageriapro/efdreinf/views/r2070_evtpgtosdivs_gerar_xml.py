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
from emensageriapro.r2070.forms import *
from emensageriapro.functions import get_xmlns


from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def gerar_xml_r2070_func(pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    r2070_evtpgtosdivs = get_object_or_404(
        r2070evtPgtosDivs,
        id=pk)

    if not versao or versao == '|':
        versao = r2070_evtpgtosdivs.versao

    evento = 'r2070evtPgtosDivs'[5:]
    arquivo = '/xsd/efdreinf/%s/%s.xsd' % (versao, evento)

    import os.path

    if os.path.isfile(BASE_DIR + arquivo):

        xmlns = get_xmlns(arquivo)

    else:

        xmlns = ''

    r2070_evtpgtosdivs_lista = r2070evtPgtosDivs.objects. \
        filter(id=pk).all()


    r2070_inforesidext_lista = r2070infoResidExt.objects. \
        filter(r2070_evtpgtosdivs_id__in=listar_ids(r2070_evtpgtosdivs_lista)).all()

    r2070_infomolestia_lista = r2070infoMolestia.objects. \
        filter(r2070_evtpgtosdivs_id__in=listar_ids(r2070_evtpgtosdivs_lista)).all()

    r2070_ideestab_lista = r2070ideEstab.objects. \
        filter(r2070_evtpgtosdivs_id__in=listar_ids(r2070_evtpgtosdivs_lista)).all()

    r2070_pgtoresidbr_lista = r2070pgtoResidBR.objects. \
        filter(r2070_ideestab_id__in=listar_ids(r2070_ideestab_lista)).all()

    r2070_pgtopf_lista = r2070pgtoPF.objects. \
        filter(r2070_pgtoresidbr_id__in=listar_ids(r2070_pgtoresidbr_lista)).all()

    r2070_detdeducao_lista = r2070detDeducao.objects. \
        filter(r2070_pgtopf_id__in=listar_ids(r2070_pgtopf_lista)).all()

    r2070_rendisento_lista = r2070rendIsento.objects. \
        filter(r2070_pgtopf_id__in=listar_ids(r2070_pgtopf_lista)).all()

    r2070_detcompet_lista = r2070detCompet.objects. \
        filter(r2070_pgtopf_id__in=listar_ids(r2070_pgtopf_lista)).all()

    r2070_compjud_lista = r2070compJud.objects. \
        filter(r2070_pgtopf_id__in=listar_ids(r2070_pgtopf_lista)).all()

    r2070_inforra_lista = r2070infoRRA.objects. \
        filter(r2070_pgtopf_id__in=listar_ids(r2070_pgtopf_lista)).all()

    r2070_inforra_despprocjud_lista = r2070infoRRAdespProcJud.objects. \
        filter(r2070_inforra_id__in=listar_ids(r2070_inforra_lista)).all()

    r2070_inforra_ideadvogado_lista = r2070infoRRAideAdvogado.objects. \
        filter(r2070_inforra_despprocjud_id__in=listar_ids(r2070_inforra_despprocjud_lista)).all()

    r2070_infoprocjud_lista = r2070infoProcJud.objects. \
        filter(r2070_pgtopf_id__in=listar_ids(r2070_pgtopf_lista)).all()

    r2070_infoprocjud_despprocjud_lista = r2070infoProcJuddespProcJud.objects. \
        filter(r2070_infoprocjud_id__in=listar_ids(r2070_infoprocjud_lista)).all()

    r2070_infoprocjud_ideadvogado_lista = r2070infoProcJudideAdvogado.objects. \
        filter(r2070_infoprocjud_despprocjud_id__in=listar_ids(r2070_infoprocjud_despprocjud_lista)).all()

    r2070_infoprocjud_origemrecursos_lista = r2070infoProcJudorigemRecursos.objects. \
        filter(r2070_infoprocjud_id__in=listar_ids(r2070_infoprocjud_lista)).all()

    r2070_depjudicial_lista = r2070depJudicial.objects. \
        filter(r2070_pgtopf_id__in=listar_ids(r2070_pgtopf_lista)).all()

    r2070_pgtopj_lista = r2070pgtoPJ.objects. \
        filter(r2070_pgtoresidbr_id__in=listar_ids(r2070_pgtoresidbr_lista)).all()

    r2070_pgtopj_infoprocjud_lista = r2070pgtoPJinfoProcJud.objects. \
        filter(r2070_pgtopj_id__in=listar_ids(r2070_pgtopj_lista)).all()

    r2070_pgtopj_despprocjud_lista = r2070pgtoPJdespProcJud.objects. \
        filter(r2070_pgtopj_infoprocjud_id__in=listar_ids(r2070_pgtopj_infoprocjud_lista)).all()

    r2070_pgtopj_ideadvogado_lista = r2070pgtoPJideAdvogado.objects. \
        filter(r2070_pgtopj_despprocjud_id__in=listar_ids(r2070_pgtopj_despprocjud_lista)).all()

    r2070_pgtopj_origemrecursos_lista = r2070pgtoPJorigemRecursos.objects. \
        filter(r2070_pgtopj_infoprocjud_id__in=listar_ids(r2070_pgtopj_infoprocjud_lista)).all()

    r2070_pgtoresidext_lista = r2070pgtoResidExt.objects. \
        filter(r2070_ideestab_id__in=listar_ids(r2070_ideestab_lista)).all()


    context = {
        'xmlns': xmlns,
        'versao': versao,
        'base': r2070_evtpgtosdivs,
        'r2070_evtpgtosdivs_lista': r2070_evtpgtosdivs_lista,
        'pk': int(pk),
        'r2070_evtpgtosdivs': r2070_evtpgtosdivs,
        'r2070_inforesidext_lista': r2070_inforesidext_lista,
        'r2070_infomolestia_lista': r2070_infomolestia_lista,
        'r2070_ideestab_lista': r2070_ideestab_lista,
        'r2070_pgtoresidbr_lista': r2070_pgtoresidbr_lista,
        'r2070_pgtopf_lista': r2070_pgtopf_lista,
        'r2070_detdeducao_lista': r2070_detdeducao_lista,
        'r2070_rendisento_lista': r2070_rendisento_lista,
        'r2070_detcompet_lista': r2070_detcompet_lista,
        'r2070_compjud_lista': r2070_compjud_lista,
        'r2070_inforra_lista': r2070_inforra_lista,
        'r2070_inforra_despprocjud_lista': r2070_inforra_despprocjud_lista,
        'r2070_inforra_ideadvogado_lista': r2070_inforra_ideadvogado_lista,
        'r2070_infoprocjud_lista': r2070_infoprocjud_lista,
        'r2070_infoprocjud_despprocjud_lista': r2070_infoprocjud_despprocjud_lista,
        'r2070_infoprocjud_ideadvogado_lista': r2070_infoprocjud_ideadvogado_lista,
        'r2070_infoprocjud_origemrecursos_lista': r2070_infoprocjud_origemrecursos_lista,
        'r2070_depjudicial_lista': r2070_depjudicial_lista,
        'r2070_pgtopj_lista': r2070_pgtopj_lista,
        'r2070_pgtopj_infoprocjud_lista': r2070_pgtopj_infoprocjud_lista,
        'r2070_pgtopj_despprocjud_lista': r2070_pgtopj_despprocjud_lista,
        'r2070_pgtopj_ideadvogado_lista': r2070_pgtopj_ideadvogado_lista,
        'r2070_pgtopj_origemrecursos_lista': r2070_pgtopj_origemrecursos_lista,
        'r2070_pgtoresidext_lista': r2070_pgtoresidext_lista,
    }

    t = get_template('r2070_evtpgtosdivs.xml')
    xml = t.render(context)
    return xml



def gerar_xml_r2070(request, pk, versao=None):

    r2070_evtpgtosdivs = get_object_or_404(
        r2070evtPgtosDivs,
        id=pk)

    return gerar_xml_r2070_func(pk, versao)


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes import salvar_arquivo_efdreinf
    from emensageriapro.mensageiro.functions.funcoes_efdreinf import assinar_efdreinf

    r2070_evtpgtosdivs = get_object_or_404(
        r2070evtPgtosDivs, id=pk)

    if not r2070_evtpgtosdivs.identidade:
        from emensageriapro.functions import identidade_evento
        ident = identidade_evento(r2070_evtpgtosdivs, 'efdreinf')
        r2070_evtpgtosdivs = get_object_or_404(r2070evtPgtosDivs, id=pk)

    if r2070_evtpgtosdivs.arquivo_original:
        xml = ler_arquivo(r2070_evtpgtosdivs.arquivo)

    else:
        xml = gerar_xml_r2070(request, pk)

    STATUS_ANT = [
            STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO,
            STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO
    ]

    if 'Signature' in xml and r2070_evtpgtosdivs.status in STATUS_ANT:

        xml_assinado = xml
        r2070evtPgtosDivs.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    else:

        if not r2070_evtpgtosdivs.transmissor_lote_efdreinf:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_efdreinf \
                import vincular_transmissor_efdreinf, criar_transmissor_efdreinf, get_grupo

            grupo = get_grupo(r2070evtPgtosDivs)

            criar_transmissor_efdreinf(request,
                grupo,
                r2070_evtpgtosdivs.nrinsc,
                r2070_evtpgtosdivs.tpinsc)

            vincular_transmissor_efdreinf(request,
                grupo,
                r2070evtPgtosDivs,
                r2070_evtpgtosdivs)

        r2070_evtpgtosdivs = get_object_or_404(
            r2070evtPgtosDivs,
            id=pk)

        xml_assinado = assinar_efdreinf(
            request,
            xml,
            r2070_evtpgtosdivs.transmissor_lote_efdreinf_id)


        if 'Signature' in xml_assinado and r2070_evtpgtosdivs.status in STATUS_ANT:

            r2070evtPgtosDivs.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

        elif s1000evtInfoEmpregador.status in STATUS_ANT:

            r2070evtPgtosDivs.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_GERADO)

    arquivo = '/arquivos/Eventos/r2070_evtpgtosdivs/%s.xml' % (r2070_evtpgtosdivs.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r2070_evtpgtosdivs/' % BASE_DIR)

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