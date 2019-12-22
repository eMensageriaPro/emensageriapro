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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *



class r1070evtTabProcessoList(generics.ListCreateAPIView):

    queryset = r1070evtTabProcesso.objects.all()
    serializer_class = r1070evtTabProcessoSerializer

    def perform_create(self, serializer):
        from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
        from constance import config
        serializer.save(
            criado_por=self.request.user,
            tpamb=config.EFDREINF_TP_AMB,
            verproc=VERSAO_EMENSAGERIA,
            procemi=1,
            versao=VERSAO_LAYOUT_EFDREINF,
            arquivo_original=0,
            status=0)

    def perform_update(self, serializer):
        from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
        from constance import config
        serializer.save(
            modificado_por=self.request.user,
            tpamb=config.EFDREINF_TP_AMB,
            verproc=VERSAO_EMENSAGERIA,
            procemi=1,
            versao=VERSAO_LAYOUT_EFDREINF,
            arquivo_original=0,
            status=0)



class r1070evtTabProcessoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = r1070evtTabProcesso.objects.all()
    serializer_class = r1070evtTabProcessoSerializer

    def perform_create(self, serializer):
        from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
        from constance import config
        serializer.save(
            criado_por=self.request.user,
            tpamb=config.EFDREINF_TP_AMB,
            verproc=VERSAO_EMENSAGERIA,
            procemi=1,
            versao=VERSAO_LAYOUT_EFDREINF,
            arquivo_original=0,
            status=0)

    def perform_update(self, serializer):
        from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
        from constance import config
        serializer.save(
            modificado_por=self.request.user,
            tpamb=config.EFDREINF_TP_AMB,
            verproc=VERSAO_EMENSAGERIA,
            procemi=1,
            versao=VERSAO_LAYOUT_EFDREINF,
            arquivo_original=0,
            status=0)
