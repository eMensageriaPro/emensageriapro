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
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #importacao_arquivos_eventos_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='importacao_arquivos_eventos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_validacoes': 0,
            'show_data_hora': 1,
            'show_status': 1,
            'show_identidade': 0,
            'show_identidade_evento': 1,
            'show_versao': 0,
            'show_evento': 1,
            'show_arquivo': 1,
            'show_importacao_arquivos': 0, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'validacoes__icontains': 'validacoes__icontains',
                'data_hora__range': 'data_hora__range',
                'status': 'status',
                'identidade': 'identidade',
                'identidade_evento__icontains': 'identidade_evento__icontains',
                'versao__icontains': 'versao__icontains',
                'evento__icontains': 'evento__icontains',
                'arquivo__icontains': 'arquivo__icontains',
                'importacao_arquivos': 'importacao_arquivos',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'validacoes__icontains': 'validacoes__icontains',
                'data_hora__range': 'data_hora__range',
                'status': 'status',
                'identidade': 'identidade',
                'identidade_evento__icontains': 'identidade_evento__icontains',
                'versao__icontains': 'versao__icontains',
                'evento__icontains': 'evento__icontains',
                'arquivo__icontains': 'arquivo__icontains',
                'importacao_arquivos': 'importacao_arquivos',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)

        importacao_arquivos_eventos_lista = ImportacaoArquivosEventos.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False, status=0).exclude(id=0).all()
        importacao_arquivos_eventos_erros_lista = ImportacaoArquivosEventos.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False, status=2).exclude(id=0).all()

        esocial_enviados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False, status__in=[7,9,14]).exclude(id=0).all()
        esocial_validados_aguardando_envio = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False, status=4, validacao_precedencia=1).exclude(id=0).all()
        esocial_validados_aguardando_precedencia = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False, status=4, validacao_precedencia=0).exclude(id=0).all()
        esocial_erros_validacao = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False, status=3).exclude(id=0).all()
        esocial_assinados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False, status__in=[10]).exclude(id=0).all()
        esocial_cadastrados = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False, status__in=[0,1,10,11]).exclude(id=0).all()
        esocial_erros_envio = TransmissorEventosEsocial.objects.using( db_slug ).\
            filter(excluido = False, status__in=[5,8]).exclude(id=0).all()

        efdreinf_enviados = TransmissorEventosEfdreinf.objects.using( db_slug ).\
            filter(excluido = False, status__in=[7,9,14]).exclude(id=0).all()
        efdreinf_validados_aguardando_envio = TransmissorEventosEfdreinf.objects.using( db_slug ).\
            filter(excluido = False, status=4, validacao_precedencia=1).exclude(id=0).all()
        efdreinf_validados_aguardando_precedencia = TransmissorEventosEfdreinf.objects.using( db_slug ).\
            filter(excluido = False, status=4, validacao_precedencia=0).exclude(id=0).all()
        efdreinf_erros_validacao = TransmissorEventosEfdreinf.objects.using( db_slug ).\
            filter(excluido = False, status=3).exclude(id=0).all()
        efdreinf_assinados = TransmissorEventosEfdreinf.objects.using( db_slug ).\
            filter(excluido = False, status__in=[10]).exclude(id=0).all()
        efdreinf_cadastrados = TransmissorEventosEfdreinf.objects.using( db_slug ).\
            filter(excluido = False, status__in=[0,1,10,11]).exclude(id=0).all()
        efdreinf_erros_envio = TransmissorEventosEfdreinf.objects.using( db_slug ).\
            filter(excluido = False, status__in=[5,8]).exclude(id=0).all()


        # if not post and len(importacao_arquivos_eventos_lista) > 100:
        #     filtrar = True
        #     importacao_arquivos_eventos_lista = None
        #     messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        importacao_arquivos_lista = ImportacaoArquivos.objects.using( db_slug ).filter(excluido = False, status=0).all()
        #importacao_arquivos_eventos_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'importacao_arquivos_eventos'
        context = {

            'tab': dict_hash['tab'],
            'importacao_arquivos_eventos_lista': importacao_arquivos_eventos_lista,
            'importacao_arquivos_eventos_erros_lista': importacao_arquivos_eventos_erros_lista,

            'esocial_enviados': esocial_enviados,
            'esocial_validados_aguardando_envio': esocial_validados_aguardando_envio,
            'esocial_validados_aguardando_precedencia': esocial_validados_aguardando_precedencia,
            'esocial_erros_validacao': esocial_erros_validacao,
            'esocial_assinados': esocial_assinados,
            'esocial_cadastrados': esocial_cadastrados,
            'esocial_erros_envio': esocial_erros_envio,

            'efdreinf_enviados': efdreinf_enviados,
            'efdreinf_validados_aguardando_envio': efdreinf_validados_aguardando_envio,
            'efdreinf_validados_aguardando_precedencia': efdreinf_validados_aguardando_precedencia,
            'efdreinf_erros_validacao': efdreinf_erros_validacao,
            'efdreinf_assinados': efdreinf_assinados,
            'efdreinf_cadastrados': efdreinf_cadastrados,
            'efdreinf_erros_envio': efdreinf_erros_envio,

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

            'importacao_arquivos_lista': importacao_arquivos_lista,
        }
        return render(request, 'mapa_processamento.html', context)
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