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
from emensageriapro.controle_de_acesso.models import Usuarios
import base64


@login_required
def imprimir(request, pk, output):

    from django.db import connections

    if True:
        
        relatorio = get_object_or_404(Relatorios, id=pk)

        if 'delete' in relatorio.sql.lower() or \
            'insert' in relatorio.sql.lower() or \
            'update' in relatorio.sql.lower() or \
            'drop' in relatorio.sql.lower():

            messages.error(request, u'''
                Não foi possível criar o relatório pois o comando SQL contém  
                algumas das seguintes palavras: "DELETE", "UPDATE", "INSERT", "DROP"''')

            return redirect('relatorios')

        if output == 'csv':

            cabecalho = '"%s"\n' % relatorio.campos
            cabecalho = cabecalho.replace(",", '";"')
            cursor = connections['default'].cursor()
            cursor.execute(relatorio.sql)
            row = cursor.fetchall()
            listagem = ''

            for a in row:

                listagem_temp = '";"'.join(a)
                listagem_temp = '"%s"\n' % listagem_temp
                listagem += listagem_temp

        else:

            cabecalho = '<th>%s</th>' % relatorio.campos
            cabecalho = cabecalho.replace(",", "</th><th>")
            cursor = connections['default'].cursor()
            cursor.execute(relatorio.sql)
            row = cursor.fetchall()
            listagem = ''

            for a in row:

                listagem_temp = '</td><td>'.join(a)
                listagem_temp = '<tr><td>%s</td></tr>' % listagem_temp
                listagem += listagem_temp

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'relatorio': relatorio,
            'data': datetime.datetime.now(),
            'cabecalho': cabecalho,
            'listagem': listagem,
            'output': output,
            'user': request.user,
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='relatorios_imprimir.html',
                filename="relatorios.pdf",
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
                             "no-stop-slow-scripts": True}, )

            return response

        elif output == 'xls':

            from django.shortcuts import render_to_response

            response = render_to_response('relatorios_imprimir.html', context)
            filename = "relatorios.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        elif output == 'csv':

            from django.shortcuts import render_to_response

            response = render_to_response('csv/relatorios.csv', context)
            filename = "relatorios.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'

            return response

        else:

            return render(request, 'relatorios_imprimir.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)