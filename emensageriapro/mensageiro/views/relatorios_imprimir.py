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


@login_required
def imprimir(request, hash):
    for_print = 0
    slug = 'default'
    if slug:
        conta = get_json(slug)
        if not conta:
            raise Http404
        else:
            db_slug = 'brtiro' + str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url(hash)
        relatorios_id = int(dict_hash['id'])
        for_print = 1
    except:
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='relatorios')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        relatorio = get_object_or_404(Relatorios.objects.using(db_slug), excluido=False, id=relatorios_id)
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
        return render(request, 'relatorios_imprimir.html', context)
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