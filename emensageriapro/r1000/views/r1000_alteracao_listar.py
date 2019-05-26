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
from emensageriapro.r1000.forms import *
from emensageriapro.r1000.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def listar(request, hash):
    for_print = 0
    
    try: 
        usuario_id = request.user.id   
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #r1000_alteracao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='r1000_alteracao')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = { 
            'show_r1000_evtinfocontri': 1,
            'show_ideperiodo': 0,
            'show_inivalid': 1,
            'show_fimvalid': 0,
            'show_infocadastro': 0,
            'show_classtrib': 1,
            'show_indescrituracao': 1,
            'show_inddesoneracao': 1,
            'show_indacordoisenmulta': 1,
            'show_indsitpj': 0,
            'show_contato': 0,
            'show_nmctt': 1,
            'show_cpfctt': 1,
            'show_fonefixo': 0,
            'show_fonecel': 0,
            'show_email': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = { 
                'r1000_evtinfocontri__icontains': 'r1000_evtinfocontri__icontains',
                'ideperiodo': 'ideperiodo',
                'inivalid__icontains': 'inivalid__icontains',
                'fimvalid__icontains': 'fimvalid__icontains',
                'infocadastro': 'infocadastro',
                'classtrib__icontains': 'classtrib__icontains',
                'indescrituracao__icontains': 'indescrituracao__icontains',
                'inddesoneracao__icontains': 'inddesoneracao__icontains',
                'indacordoisenmulta__icontains': 'indacordoisenmulta__icontains',
                'indsitpj__icontains': 'indsitpj__icontains',
                'contato': 'contato',
                'nmctt__icontains': 'nmctt__icontains',
                'cpfctt__icontains': 'cpfctt__icontains',
                'fonefixo__icontains': 'fonefixo__icontains',
                'fonecel__icontains': 'fonecel__icontains',
                'email__icontains': 'email__icontains', }
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = { 
                    'r1000_evtinfocontri__icontains': 'r1000_evtinfocontri__icontains',
                    'ideperiodo': 'ideperiodo',
                    'inivalid__icontains': 'inivalid__icontains',
                    'fimvalid__icontains': 'fimvalid__icontains',
                    'infocadastro': 'infocadastro',
                    'classtrib__icontains': 'classtrib__icontains',
                    'indescrituracao__icontains': 'indescrituracao__icontains',
                    'inddesoneracao__icontains': 'inddesoneracao__icontains',
                    'indacordoisenmulta__icontains': 'indacordoisenmulta__icontains',
                    'indsitpj__icontains': 'indsitpj__icontains',
                    'contato': 'contato',
                    'nmctt__icontains': 'nmctt__icontains',
                    'cpfctt__icontains': 'cpfctt__icontains',
                    'fonefixo__icontains': 'fonefixo__icontains',
                    'fonecel__icontains': 'fonecel__icontains',
                    'email__icontains': 'email__icontains', }
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r1000_alteracao_lista = r1000alteracao.objects.filter(**dict_qs).filter().exclude(id=0).all()
        if not post and len(r1000_alteracao_lista) > 100:
            filtrar = True
            r1000_alteracao_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #r1000_alteracao_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r1000_alteracao'
        context = {
            'r1000_alteracao_lista': r1000_alteracao_lista, 
            
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
            #[VARIAVEIS_FILTRO_RELATORIO]
        }
        if for_print in (0,1):
            return render(request, 'r1000_alteracao_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/r1000_alteracao_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r1000_alteracao_listar.html',
                filename="r1000_alteracao.pdf",
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
            response = render_to_response('r1000_alteracao_listar.html', context)
            filename = "r1000_alteracao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('csv/r1000_alteracao.csv', context)
            filename = "r1000_alteracao.csv"
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