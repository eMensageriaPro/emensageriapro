#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"


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


import datetime
import json
import base64
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2200.models import s2200documentos
from emensageriapro.s2200.forms import form_s2200_documentos
from emensageriapro.s2200.models import s2200brasil
from emensageriapro.s2200.forms import form_s2200_brasil
from emensageriapro.s2200.models import s2200exterior
from emensageriapro.s2200.forms import form_s2200_exterior
from emensageriapro.s2200.models import s2200trabEstrangeiro
from emensageriapro.s2200.forms import form_s2200_trabestrangeiro
from emensageriapro.s2200.models import s2200infoDeficiencia
from emensageriapro.s2200.forms import form_s2200_infodeficiencia
from emensageriapro.s2200.models import s2200dependente
from emensageriapro.s2200.forms import form_s2200_dependente
from emensageriapro.s2200.models import s2200aposentadoria
from emensageriapro.s2200.forms import form_s2200_aposentadoria
from emensageriapro.s2200.models import s2200contato
from emensageriapro.s2200.forms import form_s2200_contato
from emensageriapro.s2200.models import s2200infoCeletista
from emensageriapro.s2200.forms import form_s2200_infoceletista
from emensageriapro.s2200.models import s2200infoEstatutario
from emensageriapro.s2200.forms import form_s2200_infoestatutario
from emensageriapro.s2200.models import s2200localTrabGeral
from emensageriapro.s2200.forms import form_s2200_localtrabgeral
from emensageriapro.s2200.models import s2200localTrabDom
from emensageriapro.s2200.forms import form_s2200_localtrabdom
from emensageriapro.s2200.models import s2200horContratual
from emensageriapro.s2200.forms import form_s2200_horcontratual
from emensageriapro.s2200.models import s2200filiacaoSindical
from emensageriapro.s2200.forms import form_s2200_filiacaosindical
from emensageriapro.s2200.models import s2200alvaraJudicial
from emensageriapro.s2200.forms import form_s2200_alvarajudicial
from emensageriapro.s2200.models import s2200observacoes
from emensageriapro.s2200.forms import form_s2200_observacoes
from emensageriapro.s2200.models import s2200sucessaoVinc
from emensageriapro.s2200.forms import form_s2200_sucessaovinc
from emensageriapro.s2200.models import s2200transfDom
from emensageriapro.s2200.forms import form_s2200_transfdom
from emensageriapro.s2200.models import s2200mudancaCPF
from emensageriapro.s2200.forms import form_s2200_mudancacpf
from emensageriapro.s2200.models import s2200afastamento
from emensageriapro.s2200.forms import form_s2200_afastamento
from emensageriapro.s2200.models import s2200desligamento
from emensageriapro.s2200.forms import form_s2200_desligamento
from emensageriapro.s2200.models import s2200cessao
from emensageriapro.s2200.forms import form_s2200_cessao


@login_required
def salvar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL, TP_AMB
    
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2200_evtadmissao_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='s2200_evtadmissao')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao, id = s2200_evtadmissao_id)
        
        if s2200_evtadmissao.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2200_evtadmissao_apagar'] = 0
            dict_permissoes['s2200_evtadmissao_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2200_evtadmissao_id:
            s2200_evtadmissao_form = form_s2200_evtadmissao(request.POST or None, instance = s2200_evtadmissao, 
                                         initial={'excluido': False})
        else:
            s2200_evtadmissao_form = form_s2200_evtadmissao(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_ESOCIAL, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
        if request.method == 'POST':
            if s2200_evtadmissao_form.is_valid():
            
                dados = s2200_evtadmissao_form.cleaned_data
                obj = s2200_evtadmissao_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s2200_evtadmissao_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2200_evtadmissao', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2200_evtadmissao), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2200_evtadmissao', s2200_evtadmissao_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('s2200_evtadmissao_apagar', 's2200_evtadmissao_salvar', 's2200_evtadmissao'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2200_evtadmissao_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2200_evtadmissao_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
        s2200_evtadmissao_form = disabled_form_fields(s2200_evtadmissao_form, permissao.permite_editar)
        
        if s2200_evtadmissao_id:
            if s2200_evtadmissao.status != 0:
                s2200_evtadmissao_form = disabled_form_fields(s2200_evtadmissao_form, False)
        #s2200_evtadmissao_campos_multiple_passo3

        for field in s2200_evtadmissao_form.fields.keys():
            s2200_evtadmissao_form.fields[field].widget.attrs['ng-model'] = 's2200_evtadmissao_'+field
        if int(dict_hash['print']):
            s2200_evtadmissao_form = disabled_form_for_print(s2200_evtadmissao_form)

        
        s2200_documentos_lista = None 
        s2200_documentos_form = None 
        s2200_brasil_lista = None 
        s2200_brasil_form = None 
        s2200_exterior_lista = None 
        s2200_exterior_form = None 
        s2200_trabestrangeiro_lista = None 
        s2200_trabestrangeiro_form = None 
        s2200_infodeficiencia_lista = None 
        s2200_infodeficiencia_form = None 
        s2200_dependente_lista = None 
        s2200_dependente_form = None 
        s2200_aposentadoria_lista = None 
        s2200_aposentadoria_form = None 
        s2200_contato_lista = None 
        s2200_contato_form = None 
        s2200_infoceletista_lista = None 
        s2200_infoceletista_form = None 
        s2200_infoestatutario_lista = None 
        s2200_infoestatutario_form = None 
        s2200_localtrabgeral_lista = None 
        s2200_localtrabgeral_form = None 
        s2200_localtrabdom_lista = None 
        s2200_localtrabdom_form = None 
        s2200_horcontratual_lista = None 
        s2200_horcontratual_form = None 
        s2200_filiacaosindical_lista = None 
        s2200_filiacaosindical_form = None 
        s2200_alvarajudicial_lista = None 
        s2200_alvarajudicial_form = None 
        s2200_observacoes_lista = None 
        s2200_observacoes_form = None 
        s2200_sucessaovinc_lista = None 
        s2200_sucessaovinc_form = None 
        s2200_transfdom_lista = None 
        s2200_transfdom_form = None 
        s2200_mudancacpf_lista = None 
        s2200_mudancacpf_form = None 
        s2200_afastamento_lista = None 
        s2200_afastamento_form = None 
        s2200_desligamento_lista = None 
        s2200_desligamento_form = None 
        s2200_cessao_lista = None 
        s2200_cessao_form = None 
        
        if s2200_evtadmissao_id:
            s2200_evtadmissao = get_object_or_404(s2200evtAdmissao, id = s2200_evtadmissao_id)
            
            s2200_documentos_form = form_s2200_documentos(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_documentos_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_documentos_lista = s2200documentos.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_brasil_form = form_s2200_brasil(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_brasil_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_brasil_lista = s2200brasil.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_exterior_form = form_s2200_exterior(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_exterior_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_exterior_lista = s2200exterior.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_trabestrangeiro_form = form_s2200_trabestrangeiro(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_trabestrangeiro_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_trabestrangeiro_lista = s2200trabEstrangeiro.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_infodeficiencia_form = form_s2200_infodeficiencia(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_infodeficiencia_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_infodeficiencia_lista = s2200infoDeficiencia.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_dependente_form = form_s2200_dependente(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_dependente_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_dependente_lista = s2200dependente.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_aposentadoria_form = form_s2200_aposentadoria(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_aposentadoria_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_aposentadoria_lista = s2200aposentadoria.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_contato_form = form_s2200_contato(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_contato_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_contato_lista = s2200contato.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_infoceletista_form = form_s2200_infoceletista(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_infoceletista_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_infoceletista_lista = s2200infoCeletista.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_infoestatutario_form = form_s2200_infoestatutario(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_infoestatutario_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_infoestatutario_lista = s2200infoEstatutario.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_localtrabgeral_form = form_s2200_localtrabgeral(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_localtrabgeral_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_localtrabgeral_lista = s2200localTrabGeral.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_localtrabdom_form = form_s2200_localtrabdom(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_localtrabdom_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_localtrabdom_lista = s2200localTrabDom.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_horcontratual_form = form_s2200_horcontratual(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_horcontratual_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_horcontratual_lista = s2200horContratual.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_filiacaosindical_form = form_s2200_filiacaosindical(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_filiacaosindical_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_filiacaosindical_lista = s2200filiacaoSindical.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_alvarajudicial_form = form_s2200_alvarajudicial(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_alvarajudicial_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_alvarajudicial_lista = s2200alvaraJudicial.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_observacoes_form = form_s2200_observacoes(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_observacoes_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_observacoes_lista = s2200observacoes.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_sucessaovinc_form = form_s2200_sucessaovinc(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_sucessaovinc_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_sucessaovinc_lista = s2200sucessaoVinc.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_transfdom_form = form_s2200_transfdom(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_transfdom_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_transfdom_lista = s2200transfDom.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_mudancacpf_form = form_s2200_mudancacpf(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_mudancacpf_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_mudancacpf_lista = s2200mudancaCPF.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_afastamento_form = form_s2200_afastamento(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_afastamento_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_afastamento_lista = s2200afastamento.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_desligamento_form = form_s2200_desligamento(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_desligamento_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_desligamento_lista = s2200desligamento.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_cessao_form = form_s2200_cessao(
                initial={ 's2200_evtadmissao': s2200_evtadmissao })
            s2200_cessao_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_cessao_lista = s2200cessao.objects.\
                filter(s2200_evtadmissao_id=s2200_evtadmissao.id).all()
                
        else:
            s2200_evtadmissao = None
        #s2200_evtadmissao_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 's2200_evtadmissao'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 's2200_evtadmissao' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2200_evtadmissao_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=s2200_evtadmissao_id, tabela='s2200_evtadmissao').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            's2200_evtadmissao': s2200_evtadmissao, 
            's2200_evtadmissao_form': s2200_evtadmissao_form, 
            'mensagem': mensagem, 
            's2200_evtadmissao_id': int(s2200_evtadmissao_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            's2200_documentos_form': s2200_documentos_form,
            's2200_documentos_lista': s2200_documentos_lista,
            's2200_brasil_form': s2200_brasil_form,
            's2200_brasil_lista': s2200_brasil_lista,
            's2200_exterior_form': s2200_exterior_form,
            's2200_exterior_lista': s2200_exterior_lista,
            's2200_trabestrangeiro_form': s2200_trabestrangeiro_form,
            's2200_trabestrangeiro_lista': s2200_trabestrangeiro_lista,
            's2200_infodeficiencia_form': s2200_infodeficiencia_form,
            's2200_infodeficiencia_lista': s2200_infodeficiencia_lista,
            's2200_dependente_form': s2200_dependente_form,
            's2200_dependente_lista': s2200_dependente_lista,
            's2200_aposentadoria_form': s2200_aposentadoria_form,
            's2200_aposentadoria_lista': s2200_aposentadoria_lista,
            's2200_contato_form': s2200_contato_form,
            's2200_contato_lista': s2200_contato_lista,
            's2200_infoceletista_form': s2200_infoceletista_form,
            's2200_infoceletista_lista': s2200_infoceletista_lista,
            's2200_infoestatutario_form': s2200_infoestatutario_form,
            's2200_infoestatutario_lista': s2200_infoestatutario_lista,
            's2200_localtrabgeral_form': s2200_localtrabgeral_form,
            's2200_localtrabgeral_lista': s2200_localtrabgeral_lista,
            's2200_localtrabdom_form': s2200_localtrabdom_form,
            's2200_localtrabdom_lista': s2200_localtrabdom_lista,
            's2200_horcontratual_form': s2200_horcontratual_form,
            's2200_horcontratual_lista': s2200_horcontratual_lista,
            's2200_filiacaosindical_form': s2200_filiacaosindical_form,
            's2200_filiacaosindical_lista': s2200_filiacaosindical_lista,
            's2200_alvarajudicial_form': s2200_alvarajudicial_form,
            's2200_alvarajudicial_lista': s2200_alvarajudicial_lista,
            's2200_observacoes_form': s2200_observacoes_form,
            's2200_observacoes_lista': s2200_observacoes_lista,
            's2200_sucessaovinc_form': s2200_sucessaovinc_form,
            's2200_sucessaovinc_lista': s2200_sucessaovinc_lista,
            's2200_transfdom_form': s2200_transfdom_form,
            's2200_transfdom_lista': s2200_transfdom_lista,
            's2200_mudancacpf_form': s2200_mudancacpf_form,
            's2200_mudancacpf_lista': s2200_mudancacpf_lista,
            's2200_afastamento_form': s2200_afastamento_form,
            's2200_afastamento_lista': s2200_afastamento_lista,
            's2200_desligamento_form': s2200_desligamento_form,
            's2200_desligamento_lista': s2200_desligamento_lista,
            's2200_cessao_form': s2200_cessao_form,
            's2200_cessao_lista': s2200_cessao_lista,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2200_evtadmissao_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
            return render(request, 's2200_evtadmissao_salvar.html', context)
            
        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='s2200_evtadmissao_salvar.html',
                filename="s2200_evtadmissao.pdf",
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
            response = render_to_response('s2200_evtadmissao_salvar.html', context)
            filename = "s2200_evtadmissao.xls"
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
