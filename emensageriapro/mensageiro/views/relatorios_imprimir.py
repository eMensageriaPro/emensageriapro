#coding: utf-8
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

def imprimir(request, hash):
    for_print = 0
    db_slug = 'default'
    usuario_id = request.session['usuario_id']
    dict_hash = get_hash_url(hash)
    relatorios_id = int(dict_hash['id'])
    for_print = int(dict_hash['print'])
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='relatorios')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        relatorio = get_object_or_404(Relatorios.objects.using(db_slug), excluido=False, id=relatorios_id)
        if for_print != 4:
            cabecalho = '<th>%s</th>' % relatorio.campos
            cabecalho = cabecalho.replace(",","</th><th>")
            from django.db import connections
            cursor = connections[db_slug].cursor()
            cursor.execute(relatorio.sql)
            row = cursor.fetchall()
            listagem = ''
            for a in row:
                listagem_temp = '</td><td>'.join(a)
                listagem_temp = '<tr><td>%s</td></tr>' % listagem_temp
                listagem += listagem_temp
        else:
            import csv

            campos = relatorio.campos
            texto = '"'+relatorio.titulo+'"\n'
            texto += '"'+campos+'"\n'
            texto = texto.replace(',', '";"')

            from django.db import connections
            cursor = connections[db_slug].cursor()
            cursor.execute(relatorio.sql)
            row = cursor.fetchall()
            listagem = ''
            for a in row:
                b = '";"'.join(a)
                texto += '"'+b+'"\n'

            response = HttpResponse(texto, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="relatorios_imprimir.csv"'
            return response

        context = {
            'relatorio': relatorio,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
            'cabecalho': cabecalho,
            'listagem': listagem,
        }

        #return render(request, 'relatorios_imprimir.html', context)
        if for_print in (0, 1):
            return render(request, 'relatorios_imprimir.html', context)
        elif for_print == 2:
            # return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='relatorios_imprimir.html',
                filename="relatorios_imprimir.pdf",
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
            response = render_to_response('relatorios_imprimir.html', context)
            filename = "relatorios_imprimir.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            import csv
            # from django.shortcuts import render_to_response
            # response = render_to_response('relatorios_imprimir.html', context)
            # filename = "relatorios.csv"
            # response['Content-Disposition'] = 'attachment; filename=' + filename
            # response['Content-Type'] = 'text/csv; charset=UTF-8'
            # return response
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="relatorios_imprimir.csv"'

            writer = csv.writer(response)
            writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
            writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

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