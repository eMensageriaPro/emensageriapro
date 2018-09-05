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
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64


def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def scripts_validacao_automatica(request):
    import os
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.padrao import executar_sql
    for_print = 0
    executar_sql("""
    UPDATE public.importacao_arquivos_eventos
       SET excluido=True
     WHERE importacao_arquivos_id IN (SELECT id FROM importacao_arquivos WHERE excluido=True) ;

    """, False)
    db_slug = 'default'
    arquivos = ImportacaoArquivosEventos.objects.using( db_slug ).filter(excluido = False, status=0).exclude(id=0).all()
    for arquivo in arquivos:
        filename = arquivo.arquivo

        arq_compl = filename
        from emensageriapro.funcoes_importacao import validar_arquivo, importar_arquivo
        dados_eventos = {}
        dados_eventos, request, quant_erros, error_list = validar_arquivo(filename, request, lang='pt')
        if not error_list:
            dados_eventos = importar_arquivo(filename, request, 1)
        if not dados_eventos:
            dados_eventos = {}
            dados_eventos['status'] = 5
            dados_eventos['validacoes'] = 'Evento já existe em nossa base!'
            dados_eventos['criado_em'] = datetime.datetime.now()
            dados_eventos['criado_por_id'] = 1
            dados_eventos['excluido'] = False
            ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(
                **dados_eventos)
            from emensageriapro.padrao import executar_sql
            ia_id = arquivo.importacao_arquivos_id
            executar_sql("""
                UPDATE public.importacao_arquivos SET
                quant_aquardando = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status=0),
                quant_error = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status in (2,5)),
                quant_processado = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status=1)
                WHERE id=%s
            """ % (ia_id, ia_id, ia_id, ia_id), False)



        else:
            if error_list:
                dados_eventos['status'] = 2
            else:
                dados_eventos['status'] = 4
            dados_eventos['validacoes'] = '<br>'.join(error_list)
            dados_eventos['criado_em'] = datetime.datetime.now()
            dados_eventos['criado_por_id'] = 1
            dados_eventos['excluido'] = False
            print dados_eventos
            ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(
                **dados_eventos)
            from emensageriapro.padrao import executar_sql
            ia_id = arquivo.importacao_arquivos_id
            executar_sql("""
                UPDATE public.importacao_arquivos SET
                quant_aquardando = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status=0),
                quant_error = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status in (2,5) ),
                quant_processado = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status=1)
                WHERE id=%s
            """ % (ia_id, ia_id, ia_id, ia_id), False)
    arquivos = ImportacaoArquivosEventos.objects.using(db_slug).filter(excluido=False).exclude(id=0).all()
    for arquivo in arquivos:
        if arquivo.status in [2,5]:
            for arquivo in arquivos:
                origem = BASE_DIR + '/' + arquivo.arquivo
                destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/erro/')
                print 'mv %s %s' % (origem, destino)
                os.system('mv %s %s' % (origem, destino))
                dados = {}
                dados['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/')
                ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(
                    **dados)
        elif arquivo.status == 1:
            for arquivo in arquivos:
                origem = BASE_DIR + '/' + arquivo.arquivo
                destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/processado/')
                print 'mv %s %s' % (origem, destino)
                os.system('mv %s %s' % (origem, destino))
                dados = {}
                dados['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/processado/')
                ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(
                    **dados)

    return HttpResponse('')




def scripts_transmissao_automatica(request):
    import os
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.padrao import executar_sql
    for_print = 0
    executar_sql("""
    UPDATE public.importacao_arquivos_eventos
       SET excluido=True
     WHERE importacao_arquivos_id IN (SELECT id FROM importacao_arquivos WHERE excluido=True) ;

    """, False)
    db_slug = 'default'
    arquivos = ImportacaoArquivosEventos.objects.using( db_slug ).filter(excluido = False, status=0).exclude(id=0).all()
    for arquivo in arquivos:
        filename = arquivo.arquivo

        arq_compl = filename
        from emensageriapro.funcoes_importacao import validar_arquivo, importar_arquivo
        dados_eventos = {}
        dados_eventos, request, quant_erros, error_list = validar_arquivo(filename, request, lang='pt')
        if not error_list:
            dados_eventos = importar_arquivo(filename, request, 1)
        if not dados_eventos:
            dados_eventos = {}
            dados_eventos['status'] = 5
            dados_eventos['validacoes'] = 'Evento já existe em nossa base!'
            dados_eventos['criado_em'] = datetime.datetime.now()
            dados_eventos['criado_por_id'] = 1
            dados_eventos['excluido'] = False
            ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(
                **dados_eventos)
            from emensageriapro.padrao import executar_sql
            ia_id = arquivo.importacao_arquivos_id
            executar_sql("""
                UPDATE public.importacao_arquivos SET
                quant_aquardando = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status=0),
                quant_error = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status in (2,5)),
                quant_processado = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status=1)
                WHERE id=%s
            """ % (ia_id, ia_id, ia_id, ia_id), False)



        else:
            if error_list:
                dados_eventos['status'] = 2
            else:
                dados_eventos['status'] = 4
            dados_eventos['validacoes'] = '<br>'.join(error_list)
            dados_eventos['criado_em'] = datetime.datetime.now()
            dados_eventos['criado_por_id'] = 1
            dados_eventos['excluido'] = False
            print dados_eventos
            ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(
                **dados_eventos)
            from emensageriapro.padrao import executar_sql
            ia_id = arquivo.importacao_arquivos_id
            executar_sql("""
                UPDATE public.importacao_arquivos SET
                quant_aquardando = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status=0),
                quant_error = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status in (2,5) ),
                quant_processado = (
                SELECT count(*) FROM public.importacao_arquivos_eventos e
                WHERE e.importacao_arquivos_id=%s AND e.status=1)
                WHERE id=%s
            """ % (ia_id, ia_id, ia_id, ia_id), False)
    arquivos = ImportacaoArquivosEventos.objects.using(db_slug).filter(excluido=False).exclude(id=0).all()
    for arquivo in arquivos:
        if arquivo.status in [2,5]:
            for arquivo in arquivos:
                origem = BASE_DIR + '/' + arquivo.arquivo
                destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/erro/')
                print 'mv %s %s' % (origem, destino)
                os.system('mv %s %s' % (origem, destino))
                dados = {}
                dados['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/')
                ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(
                    **dados)
        elif arquivo.status == 1:
            for arquivo in arquivos:
                origem = BASE_DIR + '/' + arquivo.arquivo
                destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/processado/')
                print 'mv %s %s' % (origem, destino)
                os.system('mv %s %s' % (origem, destino))
                dados = {}
                dados['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/processado/')
                ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(
                    **dados)

    return HttpResponse('')