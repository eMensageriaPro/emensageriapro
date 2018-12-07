#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64
from emensageriapro.padrao import executar_sql
from emensageriapro.mensageiro.functions.funcoes_esocial import gravar_nome_arquivo


@login_required
def atualizar_arquivo_tabela(tabela, tabela_id, arquivo, arquivo_id):
    executar_sql("""
        UPDATE public.%s
        SET arquivo='%s'
        WHERE id=%s""" % (tabela, arquivo, tabela_id), False)
    executar_sql("""
        UPDATE public.importacao_arquivos_eventos iae
        SET versao=(SELECT versao FROM public.%s WHERE id = %s)
        WHERE id=%s""" % (tabela, tabela_id, arquivo_id), False)


@login_required
def atualizar_importador():
    executar_sql("""UPDATE public.importacao_arquivos e SET
                    quant_total = (
                    SELECT count(*) FROM public.importacao_arquivos_eventos e1
                    WHERE e1.importacao_arquivos_id=e.id),
                    quant_aguardando = (
                    SELECT count(*) FROM public.importacao_arquivos_eventos e2
                    WHERE e2.importacao_arquivos_id=e.id AND e2.status=0),
                    quant_erros = (
                    SELECT count(*) FROM public.importacao_arquivos_eventos e3
                    WHERE e3.importacao_arquivos_id=e.id AND e3.status in (2,3,5)),
                    quant_processado = (
                    SELECT count(*) FROM public.importacao_arquivos_eventos e4
                    WHERE e4.importacao_arquivos_id=e.id AND e4.status in (1,4));
                """ , False)
    executar_sql("""
                        UPDATE public.importacao_arquivos SET
                        status = 7 -- processando
                        WHERE (quant_processado + quant_erros) < quant_total;
                    """, False)
    executar_sql("""
                        UPDATE public.importacao_arquivos SET
                        status = 6 -- processado com sucesso
                        WHERE (quant_processado + quant_erros) = quant_total;
                    """, False)


@login_required
def validar_arquivo(arquivo, request, lang=None):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_schema
    from django.contrib import messages
    import untangle
    quant_erros = 0
    error_list = 0
    xml = ler_arquivo(arquivo).replace("s:", "")
    dados = {}
    try:
        doc = untangle.parse(xml)
        dados['status'] = 1
    except:
        messages.error(request, 'Erro na importação. Arquivo XML inválido!')
        dados['status'] = 3
        return dados, request, 1, ['Erro na importação. Arquivo XML inválido!']

    if dados['status'] == 1:
        from emensageriapro.mensageiro.functions.funcoes_validacoes import get_schema_name
        schema_filename = get_schema_name(arquivo)
        quant_erros, error_list = validar_schema(schema_filename, arquivo, lang=lang)
    return quant_erros, error_list




def scripts_processar_arquivos(request):
    #atualizar_importador()
    import os
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_importacao import importar_arquivo, get_identidade_evento, get_versao_evento
    from emensageriapro.mensageiro.functions.funcoes_validacoes import VERSAO_ATUAL
    db_slug = 'default'

    for_print = 0
    executar_sql("""
    UPDATE public.importacao_arquivos_eventos
       SET excluido=True
     WHERE importacao_arquivos_id IN (SELECT id FROM importacao_arquivos WHERE excluido=True);""", False)

    arquivos = ImportacaoArquivosEventos.objects.using( db_slug ).filter(excluido = False, status=0).exclude(id=0).all()

    for arquivo in arquivos:
        error_list = []

        ident = str(arquivo.id)
        while len(ident) < 10: ident = '0' + ident
        filename = arquivo.arquivo
        dados_eventos = {}
        import os.path
        if os.path.isfile(BASE_DIR+'/'+filename):
            dados_eventos['identidade_evento'] = get_identidade_evento(ler_arquivo(filename))
            dados_eventos['versao'] = get_versao_evento(ler_arquivo(filename))
            existe_identidade = executar_sql(
                "SELECT count(*) FROM public.transmissor_eventos_esocial WHERE identidade='%s'" % dados_eventos['identidade_evento'], True)
            existe_identidade = existe_identidade[0][0]

            if existe_identidade:
                dados_eventos['status'] = 5
                error_list = ['Não é possível importar o evento pois o ID já existe em nossa base!']
                origem = BASE_DIR + '/' + arquivo.arquivo
                destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/erro/' + ident + '__')
                os.system('mv %s %s' % (origem, destino))
                dados_eventos['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/'+ ident + '__')
                ia_id = arquivo.importacao_arquivos_id
                gravar_nome_arquivo(dados_eventos['arquivo'], 1)

            elif dados_eventos['versao'] in VERSAO_ATUAL:
                quant_erros, error_list = validar_arquivo(filename, request, lang='pt')
                if not quant_erros or (quant_erros == 1 and 'Signature' in str(error_list) ):
                    dados_importacao = importar_arquivo(filename, request, 1)
                    #dados_eventos['evento'] = dados_eventos['tabela']
                    #del dados_eventos['tabela']
                    dados_eventos['evento'] = dados_importacao['tabela']
                    dados_eventos['status'] = 1
                    origem = BASE_DIR + '/' + arquivo.arquivo
                    destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/processado/' + ident + '__')
                    os.system('mv %s %s' % (origem, destino))
                    dados_eventos['arquivo'] = '/' + arquivo.arquivo.replace('/aguardando/', '/processado/' + ident + '__')
                    atualizar_arquivo_tabela(dados_eventos['evento'], dados_importacao['identidade'], dados_eventos['arquivo'], arquivo.id)
                    gravar_nome_arquivo(dados_eventos['arquivo'], 1)
                else:
                    #dados_eventos['evento'] = dados_eventos['tabela']
                    #del dados_eventos['tabela']
                    dados_eventos['status'] = 2
                    origem = BASE_DIR + '/' + arquivo.arquivo
                    destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/erro/' + ident + '__')
                    os.system('mv %s %s' % (origem, destino))
                    dados_eventos['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/' + ident + '__')
                    gravar_nome_arquivo(dados_eventos['arquivo'], 1)

            else:
                dados_eventos['status'] = 2
                error_list = ['Versão do evento incompatível!']
                origem = BASE_DIR + '/' + arquivo.arquivo
                destino = BASE_DIR + '/' + arquivo.arquivo.replace('/aguardando/', '/erro/' + ident + '__')
                os.system('mv %s %s' % (origem, destino))
                dados_eventos['arquivo'] = arquivo.arquivo.replace('/aguardando/', '/erro/'+ ident + '__')
                ia_id = arquivo.importacao_arquivos_id
                gravar_nome_arquivo(dados_eventos['arquivo'], 1)
        else:
            dados_eventos['status'] = 2
            error_list = ['Arquivo não encontrado!']

        dados_eventos['validacoes'] = '<br>'.join(error_list)
        dados_eventos['criado_em'] = datetime.datetime.now()
        dados_eventos['criado_por_id'] = 1
        dados_eventos['excluido'] = False
        ImportacaoArquivosEventos.objects.using(db_slug).filter(id=arquivo.id).update(**dados_eventos)
        ia_id = arquivo.importacao_arquivos_id
        atualizar_importador()
    return HttpResponse('')




@login_required
def scripts_salvar_arquivos(request, hash):
    # tipos: 1-pdf; 2-xls, 3-csv
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url(hash)
        # retorno_pagina = dict_hash['retorno_pagina']
        # retorno_hash = dict_hash['retorno_hash']
        importacao_arquivos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')

    if request.method == 'POST' and request.FILES['arquivo']:
        from emensageriapro.settings import BASE_DIR
        import os
        from django.core.files.storage import FileSystemStorage
        myfile = request.FILES['arquivo']
        fs = FileSystemStorage(location=BASE_DIR + '/arquivos/Importacao/enviado/')
        nome_arquivo = myfile.name.replace(' ', '-')
        filename = fs.save(nome_arquivo, myfile)
        dados_importacao = {}
        dados_importacao['arquivo'] = '/arquivos/Importacao/enviado/' + filename
        dados_importacao['status'] = 0
        dados_importacao['data_hora'] = datetime.datetime.now()
        dados_importacao['quant_processado'] = 0
        dados_importacao['quant_erros'] = 0
        dados_importacao['quant_aguardando'] = 0
        dados_importacao['importado_por_id'] = usuario_id
        dados_importacao['criado_em'] = datetime.datetime.now()
        dados_importacao['criado_por_id'] = usuario_id
        dados_importacao['excluido'] = False
        obj = ImportacaoArquivos(**dados_importacao)
        obj.save(using=db_slug)
        db_slug = 'default'
        arquivos = ImportacaoArquivos.objects.using(db_slug).filter(excluido=False, status=0).exclude(id=0).all()
        for arquivo in arquivos:
            filename = BASE_DIR + '/' + arquivo.arquivo

            if '.xml' in filename.lower():
                destino = filename.replace('/enviado/', '/aguardando/')
                os.system('mv %s %s' % (filename, destino))
            elif ('.zip' in filename):
                os.system('unzip -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))
            # elif ('.tar.gz' in filename):
            #    os.system('gunzip -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))
            #    #os.system('tar -xzf -o -a %s -d %s' % (filename, BASE_DIR + '/arquivos/Importacao/aguardando'))
            #    messages.error()

            lista = os.listdir(BASE_DIR + '/arquivos/Importacao/aguardando')
            n = 0
            for arquivo_evento in lista:
                if '.xml' in arquivo_evento.lower():
                    n += 1
                    arq_compl = '/arquivos/Importacao/aguardando/' + arquivo_evento
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
            messages.success(request, 'Arquivo %s extraido com sucesso! Processando arquivos...' % arquivo)
    else:
        messages.error(request, 'Não foram encontrados arquivos para processamento!')
    return redirect('importacao_arquivos', hash=hash)




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


@login_required
def imprimir(request, hash):
    # tipos: 1-pdf; 2-xls, 3-csv
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url(hash)
        # retorno_pagina = dict_hash['retorno_pagina']
        # retorno_hash = dict_hash['retorno_hash']
        importacao_arquivos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='importacao_arquivos')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)
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
            'show_importado_por': 1,
            'show_data_hora': 1,
            'show_status': 1,
            'show_arquivo': 1, }
        post = False

        dict_qs = clear_dict_fields(dict_fields)
        importacao_arquivos_lista = ImportacaoArquivos.objects.using(db_slug).filter(**dict_qs).filter(
            excluido=False, id=importacao_arquivos_id).exclude(id=0).all()
        ia_lista = []
        for a in importacao_arquivos_lista:
            ia_lista.append(a.id)
        importacao_arquivos_eventos_lista = ImportacaoArquivosEventos.objects.using(db_slug).\
            filter(**dict_qs).filter(
            excluido=False, importacao_arquivos_id__in=ia_lista).exclude(id=0).all()

        importado_por_lista = Usuarios.objects.using(db_slug).filter(excluido=False).all()

        context = {
            'importacao_arquivos_lista': importacao_arquivos_lista,
            'importacao_arquivos_eventos_lista': importacao_arquivos_eventos_lista,
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
        # from wkhtmltopdf.views import PDFTemplateResponse
        # response = PDFTemplateResponse(
        #     request=request,
        #     template='processar_arquivos_imprimir.html',
        #     filename="processamento_arquivos.pdf",
        #     context=context,
        #     show_content_in_browser=True,
        #     cmd_options={'margin-top': 10,
        #                  'margin-bottom': 10,
        #                  'margin-right': 10,
        #                  'margin-left': 10,
        #                  'zoom': 1,
        #                  'dpi': 72,
        #                  'orientation': 'Landscape',
        #                  'viewport-size': "1366 x 513",
        #                  'javascript-delay': 1000,
        #                  'footer-center': '[page]/[topage]',
        #                  "no-stop-slow-scripts": True},
        # )
        # return response
        #return render(request, 'processar_arquivos_imprimir.html', context)
        return render_to_pdf('importacoes_imprimir.html', context)
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