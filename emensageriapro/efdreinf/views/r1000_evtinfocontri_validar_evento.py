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


from constance import config
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.r1000.models import *
from emensageriapro.r1000.forms import *
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




def validar_evento_funcao(request, pk):

    from emensageriapro.padrao import executar_sql
    from emensageriapro.mensageiro.functions.funcoes_importacao import get_versao_evento
    from emensageriapro.mensageiro.functions.funcoes_validacoes_precedencia import validar_precedencia
    from emensageriapro.mensageiro.functions.funcoes_validacoes import get_schema_name, validar_schema
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.efdreinf.views.r1000_evtinfocontri_gerar_xml import gerar_xml_assinado
    VERIFICAR_PREDECESSAO_ANTES_ENVIO = config.EFDREINF_VERIFICAR_PREDECESSAO_ANTES_ENVIO
    
    lista_validacoes = []
    r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri, id=pk)

    #
    # Validações internas
    #

    arquivo = 'arquivos/Eventos/r1000_evtinfocontri/%s.xml' % (r1000_evtinfocontri.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r1000_evtinfocontri/' % BASE_DIR)
    lista = []
    tipo = 'efdreinf'
    
    if not os.path.exists(BASE_DIR + '/' + arquivo):
    
        gerar_xml_assinado(request, pk)
        
    if os.path.exists(BASE_DIR + '/' + arquivo):
    
        from emensageriapro.efdreinf.views.r1000_evtinfocontri_validar import validacoes_r1000_evtinfocontri
        
        texto_xml = ler_arquivo(arquivo).replace("s:", "")
        versao = get_versao_evento(texto_xml)
        lista = validacoes_r1000_evtinfocontri(arquivo)
        
    for a in lista:
    
        if a: 
            
            lista_validacoes.append(a)
        
    #
    # validando schema
    #
    
    schema_filename = get_schema_name(arquivo)
    quant_erros, error_list = validar_schema(request, schema_filename, arquivo, lang='pt')
    
    for a in error_list:
    
        if a: 
            
            lista_validacoes.append(a)
        
    #
    #
    #
    
    if lista_validacoes:

        validacoes = '<br>'.join(lista_validacoes).replace("'", "''")
        
        r1000evtInfoContri.objects.\
            filter(id=pk).\
            update(validacoes=validacoes,
                   status=STATUS_EVENTO_VALIDADO_ERRO)

        messages.error(request, 
            u'Validações foram processadas, porém foram encontrados erros!')

    else:

        if VERIFICAR_PREDECESSAO_ANTES_ENVIO:

            quant = validar_precedencia('efdreinf', 'r1000_evtinfocontri', pk)

            if quant <= 0:
            
                r1000evtInfoContri.objects.\
                    filter(id=pk).\
                    update(validacoes=None,
                           status=STATUS_EVENTO_AGUARD_PRECEDENCIA)

                messages.warning(request, 
                    u'Validações foram processadas com sucesso, porém o evento está aguardando envio de sua precedência!')

            else:
            
                r1000evtInfoContri.objects.\
                    filter(id=pk).\
                    update(validacoes=None,
                           status=STATUS_EVENTO_AGUARD_ENVIO)

                messages.success(request, 
                    u'Validações foram processadas com sucesso, evento está aguardandando envio!')

        else:

            r1000evtInfoContri.objects. \
                filter(id=pk).\
                update(validacoes=None,
                       status=STATUS_EVENTO_AGUARD_ENVIO)

            messages.success(request, 
                u'Validações foram processadas com sucesso, evento está aguardandando envio!')

    return lista_validacoes


@login_required
def validar_evento(request, pk, tab=None):

    from emensageriapro.settings import VERSOES_EFDREINF
    VERIFICAR_PREDECESSAO_ANTES_ENVIO = config.EFDREINF_VERIFICAR_PREDECESSAO_ANTES_ENVIO

    STATUS_VALIDACAO = (
        STATUS_EVENTO_CADASTRADO,
        STATUS_EVENTO_IMPORTADO,
        STATUS_EVENTO_DUPLICADO,
        STATUS_EVENTO_GERADO,
        STATUS_EVENTO_ASSINADO,
        STATUS_EVENTO_VALIDADO_ERRO,
    )

    r1000_evtinfocontri = get_object_or_404(
        r1000evtInfoContri,
        id=pk)

    if r1000_evtinfocontri.status in STATUS_VALIDACAO:

        if r1000_evtinfocontri.versao in VERSOES_EFDREINF:
        
            lista_validacoes = validar_evento_funcao(request, pk)

        else:
        
            messages.error(request, 
                u'''Não foi possível validar o evento pois a 
                    versão do evento não é compatível com a versão do sistema!''')
    else:
    
        messages.error(request, 
            u'''Não foi possível validar o 
                evento pois o mesmo não está em nenhum dos sequintes status: Cadastrado, 
                Importado, Duplicado, Gerado, Assinado ou com Erro de Validação!''')
                
    if tab == 'mapa':
    
        return redirect('mapa_efdreinf', tab='master')
        
    else:
    
        return redirect('r1000_evtinfocontri_salvar', pk=pk, tab='master')