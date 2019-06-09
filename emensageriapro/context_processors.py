#coding: utf-8
import datetime


"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

from emensageriapro import settings
from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def admin_media(request):

    return {
        'LINK_WEBSITE': settings.LINK_WEBSITE,
        'VERSAO_EMENSAGERIA': settings.VERSAO_EMENSAGERIA,
        'VERIFICAR_PREDECESSAO_ANTES_ENVIO': settings.VERIFICAR_PREDECESSAO_ANTES_ENVIO,
        'STATUS_EVENTO_CADASTRADO': STATUS_EVENTO_CADASTRADO,
        'STATUS_EVENTO_IMPORTADO': STATUS_EVENTO_IMPORTADO,
        'STATUS_EVENTO_DUPLICADO': STATUS_EVENTO_DUPLICADO,
        'STATUS_EVENTO_GERADO': STATUS_EVENTO_GERADO,
        'STATUS_EVENTO_GERADO_ERRO': STATUS_EVENTO_GERADO_ERRO,
        'STATUS_EVENTO_ASSINADO': STATUS_EVENTO_ASSINADO,
        'STATUS_EVENTO_ASSINADO_ERRO': STATUS_EVENTO_ASSINADO_ERRO,
        'STATUS_EVENTO_VALIDADO': STATUS_EVENTO_VALIDADO,
        'STATUS_EVENTO_VALIDADO_ERRO': STATUS_EVENTO_VALIDADO_ERRO,
        'STATUS_EVENTO_AGUARD_PRECEDENCIA': STATUS_EVENTO_AGUARD_PRECEDENCIA,
        'STATUS_EVENTO_AGUARD_ENVIO': STATUS_EVENTO_AGUARD_ENVIO,
        'STATUS_EVENTO_ENVIADO': STATUS_EVENTO_ENVIADO,
        'STATUS_EVENTO_ENVIADO_ERRO': STATUS_EVENTO_ENVIADO_ERRO,
        'STATUS_EVENTO_PROCESSADO': STATUS_EVENTO_PROCESSADO,
    }