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


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        importacao_arquivos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='importacao_arquivos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    importacao_arquivos = get_object_or_404(ImportacaoArquivos.objects.using( db_slug ), excluido = False, id = importacao_arquivos_id)
    if request.method == 'POST':
        ImportacaoArquivos.objects.using( db_slug ).filter(id = importacao_arquivos_id).update(excluido = True)
        #importacao_arquivos_apagar_custom
        #importacao_arquivos_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'importacao_arquivos_salvar':
            return redirect('importacao_arquivos', hash=request.session['retorno_hash'])
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
    return render(request, 'importacao_arquivos_apagar.html', context)

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
            'show_quant_importado': 0,
            'show_quant_processado': 0,
            'show_quant_aguardando': 0,
            'show_quant_total': 0,
            'show_importado_por': 1,
            'show_data_hora': 1,
            'show_status': 1,
            'show_arquivo': 1, }
        post = False
        if request.method == 'POST' and request.FILES['arquivo']:
            from emensageriapro.settings import BASE_DIR
            import os
            from django.core.files.storage import FileSystemStorage
            from emensageriapro.funcoes_importacao import validar_arquivo, importar_arquivo
            myfile = request.FILES['arquivo']
            fs = FileSystemStorage(location=BASE_DIR+'/arquivos/Importacao/enviado/')
            nome_arquivo = myfile.name.replace(' ', '-')
            filename = fs.save(nome_arquivo, myfile)
            arquivo_destino = BASE_DIR + '/arquivos/Importacao/enviado/' + filename
            dados_importacao = {}
            dados_importacao['arquivo'] = arquivo_destino
            dados_importacao['status'] = 0
            dados_importacao['data_hora'] = datetime.datetime.now()
            dados_importacao['quant_processado'] = 0
            dados_importacao['quant_error'] = 0
            dados_importacao['quant_aquardando'] = 0
            dados_importacao['importado_por_id'] = usuario_id
            dados_importacao['criado_em'] = datetime.datetime.now()
            dados_importacao['criado_por_id'] = usuario_id
            dados_importacao['excluido'] = False
            obj = ImportacaoArquivos(**dados_importacao)
            obj.save(using=db_slug)

            ### EXTRAINDO ARQUIVOS

            arquivos = ImportacaoArquivos.objects.using(db_slug).filter(excluido=False, status=0).exclude(id=0).all()
            for arquivo in arquivos:
                filename = arquivo.arquivo
                # print filename
                if '.xml' in filename:
                    destino = filename.replace('/enviado/', '/aguardando/')
                    os.system('cp %s %s' % (filename, destino))
                elif ('.zip' in filename):
                    os.system('unzip -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))
                #elif ('.tar.gz' in filename):
                #    os.system('gunzip -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))
                #    #os.system('tar -xzf -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))
                #    messages.error()

                lista = os.listdir(BASE_DIR + '/arquivos/Importacao/aguardando')
                #print lista
                for arquivo_evento in lista:
                    if '.xml' in arquivo_evento:
                        arq_compl = '/arquivos/Importacao/aguardando/' + arquivo_evento
                        print arq_compl
                        dados_eventos = {}
                        dados_eventos['importacao_arquivos_id'] = arquivo.id
                        dados_eventos['evento'] = '-'
                        dados_eventos['versao'] = '-'
                        dados_eventos['identidade_evento'] = '-'
                        dados_eventos['identidade'] = 0
                        dados_eventos['arquivo'] = arq_compl
                        dados_eventos['status'] = 0
                        dados_eventos['data_hora'] = datetime.datetime.now()
                        dados_eventos['validacoes'] = ''
                        dados_eventos['criado_em'] = datetime.datetime.now()
                        dados_eventos['criado_por_id'] = 1
                        dados_eventos['excluido'] = False
                        obj = ImportacaoArquivosEventos(**dados_eventos)
                        obj.save(using=db_slug)
                messages.success(request, 'Arquivo %s extraido com sucesso!' % arquivo)
                ImportacaoArquivos.objects.using(db_slug).filter(id=arquivo.id).update(
                    status=4)
            post = True
            dict_fields = {
                'quant_erros': 'quant_erros',
                'quant_importado': 'quant_importado',
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
                'quant_importado': 'quant_importado',
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
        if for_print in (0,1):
            return render(request, 'importacao_arquivos_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='importacao_arquivos_listar.html',
                filename="importacao_arquivos.pdf",
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
            response = render_to_response('importacao_arquivos_listar.html', context)
            filename = "importacao_arquivos.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/importacao_arquivos_csv.html', context)
            filename = "importacao_arquivos.csv"
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

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        importacao_arquivos_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='importacao_arquivos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if importacao_arquivos_id:
        importacao_arquivos = get_object_or_404(ImportacaoArquivos.objects.using( db_slug ), excluido = False, id = importacao_arquivos_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if importacao_arquivos_id:
            importacao_arquivos_form = form_importacao_arquivos(request.POST or None, instance = importacao_arquivos, slug = db_slug)
        else:
            importacao_arquivos_form = form_importacao_arquivos(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if importacao_arquivos_form.is_valid():
                dados = importacao_arquivos_form.cleaned_data
                if importacao_arquivos_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #importacao_arquivos_campos_multiple_passo1
                    ImportacaoArquivos.objects.using(db_slug).filter(id=importacao_arquivos_id).update(**dados)
                    obj = ImportacaoArquivos.objects.using(db_slug).get(id=importacao_arquivos_id)
                    #importacao_arquivos_editar_custom
                    #importacao_arquivos_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #importacao_arquivos_cadastrar_campos_multiple_passo1
                    obj = ImportacaoArquivos(**dados)
                    obj.save(using = db_slug)
                    #importacao_arquivos_cadastrar_custom
                    #importacao_arquivos_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('importacao_arquivos_apagar', 'importacao_arquivos_salvar', 'importacao_arquivos'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if importacao_arquivos_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('importacao_arquivos_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        importacao_arquivos_form = disabled_form_fields(importacao_arquivos_form, permissao.permite_editar)
        #importacao_arquivos_campos_multiple_passo3

        for field in importacao_arquivos_form.fields.keys():
            importacao_arquivos_form.fields[field].widget.attrs['ng-model'] = 'importacao_arquivos_'+field
        if int(dict_hash['print']):
            importacao_arquivos_form = disabled_form_for_print(importacao_arquivos_form)

        importacao_arquivos_eventos_form = None
        importacao_arquivos_eventos_lista = None
        if importacao_arquivos_id:
            importacao_arquivos = get_object_or_404(ImportacaoArquivos.objects.using( db_slug ), excluido = False, id = importacao_arquivos_id)
  
            importacao_arquivos_eventos_form = form_importacao_arquivos_eventos(initial={ 'importacao_arquivos': importacao_arquivos }, slug=db_slug)
            importacao_arquivos_eventos_form.fields['importacao_arquivos'].widget.attrs['readonly'] = True
            importacao_arquivos_eventos_lista = ImportacaoArquivosEventos.objects.using( db_slug ).filter(excluido = False, importacao_arquivos_id=importacao_arquivos.id).all()
        else:
            importacao_arquivos = None
        #importacao_arquivos_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'importacao_arquivos' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'importacao_arquivos_salvar'
        context = {
            'importacao_arquivos': importacao_arquivos,
            'importacao_arquivos_form': importacao_arquivos_form,
            'mensagem': mensagem,
            'importacao_arquivos_id': int(importacao_arquivos_id),
            'usuario': usuario,
       
            'hash': hash,
  
            'importacao_arquivos_eventos_form': importacao_arquivos_eventos_form,
            'importacao_arquivos_eventos_lista': importacao_arquivos_eventos_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #importacao_arquivos_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'importacao_arquivos_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='importacao_arquivos_salvar.html',
                filename="importacao_arquivos.pdf",
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
            response = render_to_response('importacao_arquivos_salvar.html', context)
            filename = "importacao_arquivos.xls"
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

