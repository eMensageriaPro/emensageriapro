#coding: utf-8
# © 2018 Marcelo Medeiros de Vasconcellos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__credits__ = ["Marcelo Medeiros de Vasconcellos"]
__version__ = "1.0.0"
__maintainer__ = "Marcelo Medeiros de Vasconcellos"
__email__ = "marcelomdevasconcellos@gmail.com"


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.r9001.models import *
from emensageriapro.r9001.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from datetime import datetime
import base64
import os


from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



@login_required
def criar_alteracao(request, hash):

    from emensageriapro.efdreinf.views.r9001_evttotal_importar import read_r9001_evttotal_string
    from emensageriapro.efdreinf.views.r9001_evttotal_gerar_xml import gerar_xml_r9001
    from emensageriapro.functions import identidade_evento

    dict_hash = get_hash_url(hash)
    r9001_evttotal_id = int(dict_hash['id'])
    
    if request.user.has_perm('efdreinf.can_create_change_event_r9001evtTotal'):

        if r9001_evttotal_id:
    
            r9001_evttotal = get_object_or_404(
                r9001evtTotal,
                id=r9001_evttotal_id)
    
            texto = gerar_xml_r9001(r9001_evttotal_id, versao="|")
            texto = texto.replace('<inclusao>','<alteracao>').replace('</inclusao>','</alteracao>')
            dados = read_r9001_evttotal_string({}, texto.encode('utf-8'), 0)
            nova_identidade = identidade_evento(r9001_evttotal)
    
            r9001evtTotal.objects.filter(id=dados['id']).\
                update(status=STATUS_EVENTO_CADASTRADO,
                       arquivo_original=0,
                       arquivo='')
    
            gravar_auditoria(u'{}',
                u'{"funcao": "Evento de de alteração de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, r9001_evttotal.identidade),
                'r9001_evttotal', dados['id'], request.user.id, 1)
    
            messages.success(request, u'Evento de alteração criado com sucesso!')
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['id'] )
            return redirect('r9001_evttotal_salvar', hash=url_hash)
    
        messages.error(request, 'Erro ao criar evento de alteração!')
        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
        
    else:
    
        messages.error(request, u'''Você não possui permissão para criar evento de alteração a partir de evento existente. 
                                    Entre em contato com o administrador do sistema!''')
        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
