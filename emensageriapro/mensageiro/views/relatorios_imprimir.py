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
def imprimir(request, hash):

    from django.db import connections

    for_print = 0

    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url(hash)
        relatorios_id = int(dict_hash['id'])
        for_print = 1
    except:
        usuario_id = False
        return redirect('login', slug=slug)

    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    if True:
        
        relatorio = get_object_or_404(Relatorios, id=relatorios_id)

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
            'relatorio': relatorio,
            'usuario': usuario,
            'data': datetime.datetime.now(),
            'for_print': for_print,
            'hash': hash,
            'cabecalho': cabecalho,
            'listagem': listagem,
        }

        return render(request, 'relatorios_imprimir.html', context)

    else:

        context = {
            'usuario': usuario,
            'data': datetime.datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)