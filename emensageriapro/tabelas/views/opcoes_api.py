# eMensageriaAI #
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
from emensageriapro.tabelas.forms import *
from emensageriapro.tabelas.models import *
from emensageriapro.controle_de_acesso.models import *



class OpcoesList(generics.ListCreateAPIView):

    queryset = Opcoes.objects.all()
    serializer_class = OpcoesSerializer

    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modificado_por=self.request.user)




class OpcoesDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Opcoes.objects.all()
    serializer_class = OpcoesSerializer

    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modificado_por=self.request.user)




@login_required
def json_search(request, pk, search):

    from django.http import JsonResponse
    import operator
    from django.db.models import Count, Q
    import urllib

    search = urllib.unquote(search)
    lista = search.split(" ")
    dicionario = {}

    if search.strip():

        try:
            query = reduce(operator.and_, ((Q(titulo__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = Opcoes.objects.filter(opcoes_id=pk).filter(query).all()

        except:
            query = reduce(operator.and_, ((Q(descricao__icontains=item) | Q(codigo__icontains=item)) for item in lista))
            lista = Opcoes.objects.filter(opcoes_id=pk).filter(query).all()

    else:
        lista = Opcoes.objects.filter(opcoes_id=pk).all()

    lista_opcoes = []

    for a in lista:

        dic = {}
        dic['key'] = a.codigo
        dic['value'] = a.titulo
        lista_opcoes.append(dic)

    dicionario['opcoes'] = lista_opcoes

    return JsonResponse(dicionario)
