#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64
from emensageriapro.esocial.models import s1000evtInfoEmpregador
from emensageriapro.esocial.models import s1005evtTabEstab
from emensageriapro.esocial.models import s1010evtTabRubrica
from emensageriapro.esocial.models import s1020evtTabLotacao
from emensageriapro.esocial.models import s1030evtTabCargo
from emensageriapro.esocial.models import s1035evtTabCarreira
from emensageriapro.esocial.models import s1040evtTabFuncao
from emensageriapro.esocial.models import s1050evtTabHorTur
from emensageriapro.esocial.models import s1060evtTabAmbiente
from emensageriapro.esocial.models import s1070evtTabProcesso
from emensageriapro.esocial.models import s1080evtTabOperPort
from emensageriapro.esocial.models import s1200evtRemun
from emensageriapro.esocial.models import s1202evtRmnRPPS
from emensageriapro.esocial.models import s1207evtBenPrRP
from emensageriapro.esocial.models import s1210evtPgtos
from emensageriapro.esocial.models import s1250evtAqProd
from emensageriapro.esocial.models import s1260evtComProd
from emensageriapro.esocial.models import s1270evtContratAvNP
from emensageriapro.esocial.models import s1280evtInfoComplPer
from emensageriapro.esocial.models import s1295evtTotConting
from emensageriapro.esocial.models import s1298evtReabreEvPer
from emensageriapro.esocial.models import s1299evtFechaEvPer
from emensageriapro.esocial.models import s1300evtContrSindPatr
from emensageriapro.esocial.models import s2190evtAdmPrelim
from emensageriapro.esocial.models import s2200evtAdmissao
from emensageriapro.esocial.models import s2205evtAltCadastral
from emensageriapro.esocial.models import s2206evtAltContratual
from emensageriapro.esocial.models import s2210evtCAT
from emensageriapro.esocial.models import s2220evtMonit
from emensageriapro.esocial.models import s2221evtToxic
from emensageriapro.esocial.models import s2230evtAfastTemp
from emensageriapro.esocial.models import s2240evtExpRisco
from emensageriapro.esocial.models import s2241evtInsApo
from emensageriapro.esocial.models import s2245evtTreiCap
from emensageriapro.esocial.models import s2250evtAvPrevio
from emensageriapro.esocial.models import s2260evtConvInterm
from emensageriapro.esocial.models import s2298evtReintegr
from emensageriapro.esocial.models import s2299evtDeslig
from emensageriapro.esocial.models import s2300evtTSVInicio
from emensageriapro.esocial.models import s2306evtTSVAltContr
from emensageriapro.esocial.models import s2399evtTSVTermino
from emensageriapro.esocial.models import s2400evtCdBenefIn
from emensageriapro.esocial.models import s2405evtCdBenefAlt
from emensageriapro.esocial.models import s2410evtCdBenIn
from emensageriapro.esocial.models import s2416evtCdBenAlt
from emensageriapro.esocial.models import s2420evtCdBenTerm
from emensageriapro.esocial.models import s3000evtExclusao
from emensageriapro.esocial.models import s5001evtBasesTrab
from emensageriapro.esocial.models import s5002evtIrrfBenef
from emensageriapro.esocial.models import s5003evtBasesFGTS
from emensageriapro.esocial.models import s5011evtCS
from emensageriapro.esocial.models import s5012evtIrrf
from emensageriapro.esocial.models import s5013evtFGTS
from emensageriapro.esocial.forms import form_s1000_evtinfoempregador
from emensageriapro.esocial.forms import form_s1005_evttabestab
from emensageriapro.esocial.forms import form_s1010_evttabrubrica
from emensageriapro.esocial.forms import form_s1020_evttablotacao
from emensageriapro.esocial.forms import form_s1030_evttabcargo
from emensageriapro.esocial.forms import form_s1035_evttabcarreira
from emensageriapro.esocial.forms import form_s1040_evttabfuncao
from emensageriapro.esocial.forms import form_s1050_evttabhortur
from emensageriapro.esocial.forms import form_s1060_evttabambiente
from emensageriapro.esocial.forms import form_s1070_evttabprocesso
from emensageriapro.esocial.forms import form_s1080_evttaboperport
from emensageriapro.esocial.forms import form_s1200_evtremun
from emensageriapro.esocial.forms import form_s1202_evtrmnrpps
from emensageriapro.esocial.forms import form_s1207_evtbenprrp
from emensageriapro.esocial.forms import form_s1210_evtpgtos
from emensageriapro.esocial.forms import form_s1250_evtaqprod
from emensageriapro.esocial.forms import form_s1260_evtcomprod
from emensageriapro.esocial.forms import form_s1270_evtcontratavnp
from emensageriapro.esocial.forms import form_s1280_evtinfocomplper
from emensageriapro.esocial.forms import form_s1295_evttotconting
from emensageriapro.esocial.forms import form_s1298_evtreabreevper
from emensageriapro.esocial.forms import form_s1299_evtfechaevper
from emensageriapro.esocial.forms import form_s1300_evtcontrsindpatr
from emensageriapro.esocial.forms import form_s2190_evtadmprelim
from emensageriapro.esocial.forms import form_s2200_evtadmissao
from emensageriapro.esocial.forms import form_s2205_evtaltcadastral
from emensageriapro.esocial.forms import form_s2206_evtaltcontratual
from emensageriapro.esocial.forms import form_s2210_evtcat
from emensageriapro.esocial.forms import form_s2220_evtmonit
from emensageriapro.esocial.forms import form_s2221_evttoxic
from emensageriapro.esocial.forms import form_s2230_evtafasttemp
from emensageriapro.esocial.forms import form_s2240_evtexprisco
from emensageriapro.esocial.forms import form_s2241_evtinsapo
from emensageriapro.esocial.forms import form_s2245_evttreicap
from emensageriapro.esocial.forms import form_s2250_evtavprevio
from emensageriapro.esocial.forms import form_s2260_evtconvinterm
from emensageriapro.esocial.forms import form_s2298_evtreintegr
from emensageriapro.esocial.forms import form_s2299_evtdeslig
from emensageriapro.esocial.forms import form_s2300_evttsvinicio
from emensageriapro.esocial.forms import form_s2306_evttsvaltcontr
from emensageriapro.esocial.forms import form_s2399_evttsvtermino
from emensageriapro.esocial.forms import form_s2400_evtcdbenefin
from emensageriapro.esocial.forms import form_s2405_evtcdbenefalt
from emensageriapro.esocial.forms import form_s2410_evtcdbenin
from emensageriapro.esocial.forms import form_s2416_evtcdbenalt
from emensageriapro.esocial.forms import form_s2420_evtcdbenterm
from emensageriapro.esocial.forms import form_s3000_evtexclusao
from emensageriapro.esocial.forms import form_s5001_evtbasestrab
from emensageriapro.esocial.forms import form_s5002_evtirrfbenef
from emensageriapro.esocial.forms import form_s5003_evtbasesfgts
from emensageriapro.esocial.forms import form_s5011_evtcs
from emensageriapro.esocial.forms import form_s5012_evtirrf
from emensageriapro.esocial.forms import form_s5013_evtfgts

#IMPORTACOES


@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        transmissor_lote_esocial_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_esocial')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial.objects.using( db_slug ), excluido = False, id = transmissor_lote_esocial_id)
    if request.method == 'POST':
        TransmissorLoteEsocial.objects.using( db_slug ).filter(id = transmissor_lote_esocial_id).update(excluido = True)
        #transmissor_lote_esocial_apagar_custom
        #transmissor_lote_esocial_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'transmissor_lote_esocial_salvar':
            return redirect('transmissor_lote_esocial', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,
        
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,
        
        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'transmissor_lote_esocial_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class TransmissorLoteEsocialList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = TransmissorLoteEsocial.objects.using(db_slug).all()
    serializer_class = TransmissorLoteEsocialSerializer
    permission_classes = (IsAdminUser,)


class TransmissorLoteEsocialDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = TransmissorLoteEsocial.objects.using(db_slug).all()
    serializer_class = TransmissorLoteEsocialSerializer
    permission_classes = (IsAdminUser,)


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #transmissor_lote_esocial_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_esocial')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_empregador_nrinsc': 1,
            'show_empregador_tpinsc': 1,
            'show_grupo': 1,
            'show_processamento_versao_aplicativo': 0,
            'show_protocolo': 0,
            'show_recepcao_data_hora': 0,
            'show_recepcao_versao_aplicativo': 0,
            'show_resposta_codigo': 1,
            'show_resposta_descricao': 0,
            'show_status': 1,
            'show_tempo_estimado_conclusao': 0,
            'show_transmissor': 0, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'empregador_nrinsc__icontains': 'empregador_nrinsc__icontains',
                'empregador_tpinsc': 'empregador_tpinsc',
                'grupo': 'grupo',
                'processamento_versao_aplicativo__icontains': 'processamento_versao_aplicativo__icontains',
                'protocolo__icontains': 'protocolo__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'recepcao_versao_aplicativo__icontains': 'recepcao_versao_aplicativo__icontains',
                'resposta_codigo': 'resposta_codigo',
                'status': 'status',
                'tempo_estimado_conclusao': 'tempo_estimado_conclusao',
                'transmissor': 'transmissor',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'empregador_nrinsc__icontains': 'empregador_nrinsc__icontains',
                'empregador_tpinsc': 'empregador_tpinsc',
                'grupo': 'grupo',
                'processamento_versao_aplicativo__icontains': 'processamento_versao_aplicativo__icontains',
                'protocolo__icontains': 'protocolo__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'recepcao_versao_aplicativo__icontains': 'recepcao_versao_aplicativo__icontains',
                'resposta_codigo': 'resposta_codigo',
                'status': 'status',
                'tempo_estimado_conclusao': 'tempo_estimado_conclusao',
                'transmissor': 'transmissor',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(transmissor_lote_esocial_lista) > 100:
            filtrar = True
            transmissor_lote_esocial_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        transmissor_lista = TransmissorLote.objects.using( db_slug ).filter(excluido = False).all()
        #transmissor_lote_esocial_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'transmissor_lote_esocial'
        context = {
            'transmissor_lote_esocial_lista': transmissor_lote_esocial_lista,
            
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
       
            'transmissor_lista': transmissor_lista,
        }
        if for_print in (0,1):
            return render(request, 'transmissor_lote_esocial_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='transmissor_lote_esocial_listar.html',
                filename="transmissor_lote_esocial.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('transmissor_lote_esocial_listar.html', context)
            filename = "transmissor_lote_esocial.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/transmissor_lote_esocial_csv.html', context)
            filename = "transmissor_lote_esocial.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        transmissor_lote_esocial_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_esocial')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if transmissor_lote_esocial_id:
        transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial.objects.using( db_slug ), excluido = False, id = transmissor_lote_esocial_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if transmissor_lote_esocial_id:
            transmissor_lote_esocial_form = form_transmissor_lote_esocial(request.POST or None, instance = transmissor_lote_esocial, slug = db_slug)
        else:
            transmissor_lote_esocial_form = form_transmissor_lote_esocial(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if transmissor_lote_esocial_form.is_valid():
                dados = transmissor_lote_esocial_form.cleaned_data
                if transmissor_lote_esocial_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #transmissor_lote_esocial_campos_multiple_passo1
                    TransmissorLoteEsocial.objects.using(db_slug).filter(id=transmissor_lote_esocial_id).update(**dados)
                    obj = TransmissorLoteEsocial.objects.using(db_slug).get(id=transmissor_lote_esocial_id)
                    #transmissor_lote_esocial_editar_custom
                    #transmissor_lote_esocial_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #transmissor_lote_esocial_cadastrar_campos_multiple_passo1
                    obj = TransmissorLoteEsocial(**dados)
                    obj.save(using = db_slug)
                    #transmissor_lote_esocial_cadastrar_custom
                    #transmissor_lote_esocial_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('transmissor_lote_esocial_apagar', 'transmissor_lote_esocial_salvar', 'transmissor_lote_esocial'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if transmissor_lote_esocial_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('transmissor_lote_esocial_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        transmissor_lote_esocial_form = disabled_form_fields(transmissor_lote_esocial_form, permissao.permite_editar)
        #transmissor_lote_esocial_campos_multiple_passo3

        for field in transmissor_lote_esocial_form.fields.keys():
            transmissor_lote_esocial_form.fields[field].widget.attrs['ng-model'] = 'transmissor_lote_esocial_'+field
        if int(dict_hash['print']):
            transmissor_lote_esocial_form = disabled_form_for_print(transmissor_lote_esocial_form)
   
        transmissor_lote_esocial_ocorrencias_form = None
        transmissor_lote_esocial_ocorrencias_lista = None
        retornos_eventos_form = None
        retornos_eventos_lista = None
        if transmissor_lote_esocial_id:
            transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial.objects.using( db_slug ), excluido = False, id = transmissor_lote_esocial_id)
       
            transmissor_lote_esocial_ocorrencias_form = form_transmissor_lote_esocial_ocorrencias(initial={ 'transmissor_lote_esocial': transmissor_lote_esocial }, slug=db_slug)
            transmissor_lote_esocial_ocorrencias_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            transmissor_lote_esocial_ocorrencias_lista = TransmissorLoteEsocialOcorrencias.objects.using( db_slug ).filter(excluido = False, transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()
            retornos_eventos_form = form_retornos_eventos(initial={ 'transmissor_lote_esocial': transmissor_lote_esocial }, slug=db_slug)
            retornos_eventos_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            retornos_eventos_lista = RetornosEventos.objects.using( db_slug ).filter(excluido = False, transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()
        else:
            transmissor_lote_esocial = None
        if transmissor_lote_esocial:
            transmissor_eventos_esocial_lista = TransmissorEventosEsocial.objects.using(db_slug).filter(excluido=False, transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()
            transmissor_eventos_esocial_totalizacoes_lista = TransmissorEventosEsocialTotalizacoes.objects.using(db_slug).filter(excluido=False, transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()
        else:
            transmissor_eventos_esocial_lista = None
            transmissor_eventos_esocial_totalizacoes_lista = None
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'transmissor_lote_esocial' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'transmissor_lote_esocial_salvar'
        context = {
            'transmissor_lote_esocial': transmissor_lote_esocial,
            'transmissor_lote_esocial_form': transmissor_lote_esocial_form,
            'mensagem': mensagem,
            'transmissor_lote_esocial_id': int(transmissor_lote_esocial_id),
            'usuario': usuario,
            
            'hash': hash,
       
            'transmissor_lote_esocial_ocorrencias_form': transmissor_lote_esocial_ocorrencias_form,
            'transmissor_lote_esocial_ocorrencias_lista': transmissor_lote_esocial_ocorrencias_lista,
            'retornos_eventos_form': retornos_eventos_form,
            'retornos_eventos_lista': retornos_eventos_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            'transmissor_eventos_esocial_lista': transmissor_eventos_esocial_lista,
'transmissor_eventos_esocial_totalizacoes_lista': transmissor_eventos_esocial_totalizacoes_lista,
        }
        if for_print in (0,1 ):
            return render(request, 'transmissor_lote_esocial_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='transmissor_lote_esocial_salvar.html',
                filename="transmissor_lote_esocial.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('transmissor_lote_esocial_salvar.html', context)
            filename = "transmissor_lote_esocial.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

