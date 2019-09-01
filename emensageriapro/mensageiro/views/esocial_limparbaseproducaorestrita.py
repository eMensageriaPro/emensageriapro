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
from django.shortcuts import redirect, get_object_or_404

from emensageriapro.esocial.models import *
from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
from emensageriapro.padrao import *
from emensageriapro.s1000.forms import *

"""
As empresas poderão remover todos os eventos enviados ao ambiente de Produção Restrita, 
inclusive o evento S-1000. Esta funcionalidade é exclusiva para os testes neste 
ambiente e não está disponível na produção. Para tanto, a empresa deverá transmitir 
um evento S-1000 preenchido conforme abaixo:

Tag nmRazao = RemoverEmpregadorDaBaseDeDadosDaProducaoRestrita
Tag classTrib = 00
tag tpAmb = 2 – Produção Restrita.

Será retornada a mensagem “1012 – Empregador {0} removido com sucesso da base de 
dados da Producao Restrita do eSocial”, onde {0} é o identificador do empregador. 
esocial_limparbaseproducaorestrita
"""


@login_required
def limpar_base(request, pk):

    from emensageriapro.esocial.views.s1000_evtinfoempregador_importar import read_s1000_evtinfoempregador_string
    from emensageriapro.esocial.views.s1000_evtinfoempregador_gerar_xml import gerar_xml_s1000
    from emensageriapro.s1000.models import s1000inclusao
    from emensageriapro.functions import identidade_evento

    if request.user.has_perm('esocial.can_duplicate_s1000evtInfoEmpregador'):

        if pk:

            s1000_evtinfoempregador = get_object_or_404(
                s1000evtInfoEmpregador,
                id=pk)

            texto = gerar_xml_s1000(request, pk, versao="|")
            dados = read_s1000_evtinfoempregador_string(request, {}, texto.encode('utf-8'), 0)
            nova_identidade = identidade_evento(s1000_evtinfoempregador, 'esocial')

            s1000evtInfoEmpregador.objects.\
                filter(id=dados['id']).\
                update(status=STATUS_EVENTO_CADASTRADO,
                       arquivo_original=0,
                       tpamb=2,
                       arquivo='')

            s1000inclusao.objects.\
                filter(s1000_evtinfoempregador_id=dados['id']).\
                update(nmrazao='RemoverEmpregadorDaBaseDeDadosDaProducaoRestrita',
                       natjurid=None,
                       inivalid='2019-01',
                       classtrib='00')

            gravar_auditoria(u'{}', u'{"funcao": "Evento de limpeza de base de produção restrita de identidade %s criado a partir da duplicação do evento %s"}' % (nova_identidade, s1000_evtinfoempregador.identidade),
                's1000_evtinfoempregador', dados['id'], request.user.id, 1)

            messages.success(request, u'''Evento de limpeza de base de produção 
                                          restrita criado com sucesso! 
                                          Valide, envie o evento e verifique o retorno!''')
            return_pk = dados['id']

            return redirect('s1000_evtinfoempregador_salvar', pk=return_pk)

        messages.error(request, 'Erro ao duplicar evento!')

        return redirect('s1000_evtinfoempregador_salvar', pk=pk)

    else:

        messages.error(request, u'''Você não possui permissão para duplicar o evento.
                                    Entre em contato com o administrador do sistema!''')
                
        return redirect('s1000_evtinfoempregador_salvar', pk=pk)
    