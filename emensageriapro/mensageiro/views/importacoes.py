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
        #importacao_arquivos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    processar_arquivo = False
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='importacao_arquivos')
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
            'show_quant_erros': 0,
            'show_quant_processado': 0,
            'show_quant_aguardando': 0,
            'show_quant_total': 0,
            'show_importado_por': 1,
            'show_data_hora': 1,
            'show_status': 1,
            'show_arquivo': 1, }
        post = False
        if request.method == 'POST':
            # from emensageriapro.settings import BASE_DIR
            # import os
            # from django.core.files.storage import FileSystemStorage
            # myfile = request.FILES['arquivo']
            # fs = FileSystemStorage(location=BASE_DIR+'/arquivos/Importacao/enviado/')
            # nome_arquivo = myfile.name.replace(' ', '-')
            # filename = fs.save(nome_arquivo, myfile)
            # arquivo_destino = BASE_DIR + '/arquivos/Importacao/enviado/' + filename
            # dados_importacao = {}
            # dados_importacao['arquivo'] = arquivo_destino
            # dados_importacao['status'] = 0
            # dados_importacao['data_hora'] = datetime.datetime.now()
            # dados_importacao['quant_processado'] = 0
            # dados_importacao['quant_erros'] = 0
            # dados_importacao['quant_aguardando'] = 0
            # dados_importacao['importado_por_id'] = usuario_id
            # dados_importacao['criado_em'] = datetime.datetime.now()
            # dados_importacao['criado_por_id'] = usuario_id
            # dados_importacao['excluido'] = False
            # obj = ImportacaoArquivos(**dados_importacao)
            # obj.save(using=db_slug)
            # processar_arquivo = True
            #
            # ### EXTRAINDO ARQUIVOS
            #
            # arquivos = ImportacaoArquivos.objects.using(db_slug).filter(excluido=False, status=0).exclude(id=0).all()
            # for arquivo in arquivos:
            #     filename = arquivo.arquivo
            #     # print filename
            #     if '.xml' in filename.lower():
            #         destino = filename.replace('/enviado/', '/aguardando/')
            #         os.system('mv %s %s' % (filename, destino))
            #     elif ('.zip' in filename):
            #         os.system('unzip -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))
            #     #elif ('.tar.gz' in filename):
            #     #    os.system('gunzip -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))
            #     #    #os.system('tar -xzf -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))
            #     #    messages.error()
            #
            #     lista = os.listdir(BASE_DIR + '/arquivos/Importacao/aguardando')
            #     n = 0
            #     for arquivo_evento in lista:
            #         if '.xml' in arquivo_evento.lower():
            #             n += 1
            #             arq_compl = '/arquivos/Importacao/aguardando/' + arquivo_evento
            #             dados_eventos = {}
            #             dados_eventos['importacao_arquivos_id'] = arquivo.id
            #             dados_eventos['evento'] = '-'
            #             dados_eventos['versao'] = '-'
            #             dados_eventos['identidade_evento'] = '-'
            #             dados_eventos['identidade'] = 0
            #             dados_eventos['arquivo'] = arq_compl
            #             dados_eventos['status'] = 0
            #             dados_eventos['data_hora'] = datetime.datetime.now()
            #             dados_eventos['validacoes'] = ''
            #             dados_eventos['criado_em'] = datetime.datetime.now()
            #             dados_eventos['criado_por_id'] = 1
            #             dados_eventos['excluido'] = False
            #             obj = ImportacaoArquivosEventos(**dados_eventos)
            #             obj.save(using=db_slug)
            #     messages.success(request, 'Arquivo %s extraido com sucesso! Processando arquivos!' % arquivo)
            #     ImportacaoArquivos.objects.using(db_slug).filter(id=arquivo.id).update(
            #         quant_total=n, quant_aguardando=n, status=7)
            post = True
            dict_fields = {
                'quant_erros': 'quant_erros',
                'quant_processado': 'quant_processado',
                'quant_aguardando': 'quant_aguardando',
                'quant_total': 'quant_total',
                'importado_por': 'importado_por',
                'data_hora__range': 'data_hora__range',
                'status': 'status',
                'arquivo__icontains': 'arquivo__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'quant_erros': 'quant_erros',
                'quant_processado': 'quant_processado',
                'quant_aguardando': 'quant_aguardando',
                'quant_total': 'quant_total',
                'importado_por': 'importado_por',
                'data_hora__range': 'data_hora__range',
                'status': 'status',
                'arquivo__icontains': 'arquivo__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        importacao_arquivos_lista = ImportacaoArquivos.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(importacao_arquivos_lista) > 100:
            filtrar = True
            importacao_arquivos_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        importado_por_lista = Usuarios.objects.using( db_slug ).filter(excluido = False).all()
        #importacao_arquivos_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'importacao_arquivos'
        context = {
            'processar_arquivo': processar_arquivo,
            'importacao_arquivos_lista': importacao_arquivos_lista,

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

            'importado_por_lista': importado_por_lista,
        }
        return render(request, 'importacoes_listar.html', context)
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