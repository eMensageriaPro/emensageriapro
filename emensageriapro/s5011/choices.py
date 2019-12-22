# eMensageriaAI #
#coding:utf-8


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



CHOICES_ESOCIALINSCRICOESTIPOS = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (5, u'5 - CGC'),
    (6, u'6 - CEI'),
]


CHOICES_S5011_ALIQRAT = [
    (1, u'1'),
    (2, u'2'),
    (3, u'3'),
]


CHOICES_S5011_INDAQUIS = [
    (1, u'1 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral'),
    (2, u'2 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA'),
    (3, u'3 - Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA'),
    (4, u'4 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral - Produção Isenta (Lei 13.606/2018)'),
    (5, u'5 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA - Produção Isenta (Lei 13.606/2018)'),
    (6, u'6 - Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA - Produção Isenta (Lei 13.606/2018). Evento de origem (S-1250).'),
]


CHOICES_S5011_INDCOMERC = [
    (2, u'2 - Comercialização da Produção efetuada diretamente no varejo a consumidor final ou a outro produtor rural pessoa física por Produtor Rural Pessoa Física, inclusive por Segurado Especial ou por Pessoa Física não produtor rural'),
    (3, u'3 - Comercialização da Produção por Prod. Rural PF/Seg. Especial - Vendas a PJ (exceto Entidade inscrita no Programa de Aquisição de Alimentos - PAA) ou a Intermediário PF'),
    (7, u'7 - Comercialização da Produção Isenta de acordo com a Lei n° 13.606/2018'),
    (8, u'8 - Comercialização da Produção da Pessoa Física/Segurado Especial para Entidade inscrita no Programa de Aquisição de Alimentos - PAA'),
    (9, u'9 - Comercialização da Produção no Mercado Externo. Origem: {indComerc} do S-1260.'),
]


CHOICES_S5011_INDCONSTR = [
    (0, u'0 - Não é Construtora'),
    (1, u'1 - Empresa Construtora. Evento de origem (S-1000).'),
]


CHOICES_S5011_INDCOOP = [
    (0, u'0 - Não é cooperativa'),
    (1, u'1 - Cooperativa de Trabalho'),
    (2, u'2 - Cooperativa de Produção'),
    (3, u'3 - Outras Cooperativas. Evento de origem (S-1000).'),
]


CHOICES_S5011_INDINCID = [
    (1, u'1 - Normal'),
    (2, u'2 - Ativ. Concomitante'),
    (9, u'9 - Substituída ou Isenta.'),
]


CHOICES_S5011_INDSUBSTPATR = [
    (1, u'1 - Integralmente substituída'),
    (2, u'2 - Parcialmente substituída. Origem: {indSubsPatr} de S-1280.'),
]


CHOICES_S5011_INDSUBSTPATROBRA = [
    (1, u'1 - Contribuição Patronal Substituída'),
    (2, u'2 - Contribuição Patronal Não Substituída.'),
]


CHOICES_S5011_TPINSCCONTRAT = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF.'),
]


CHOICES_S5011_TPINSCPROP = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]

