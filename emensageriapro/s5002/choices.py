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



CHOICES_S5002_INDNIF = [
    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF.'),
]


CHOICES_S5002_INDRESBR = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S5002_TPCR = [
    ('0473-01', u'0473-01 - Renda e Proventos de Qualquer Natureza'),
    ('0561-07', u'0561-07 - IRRF - Rendimento do Trabalho Assalariado no País/Ausente no Exterior a Serviço do País'),
    ('0561-08', u'0561-08 - IRRF - Empregado Doméstico'),
    ('0561-09', u'0561-09 - IRRF - Empregado Doméstico - 13º Sal Rescisão'),
    ('0561-10', u'0561-10 - IRRF - Empregado doméstico - 13º salário'),
    ('0561-11', u'0561-11 - IRRF - Empregado/Trabalhador Rural - Segurado Especial'),
    ('0561-12', u'0561-12 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13° salário'),
    ('0561-13', u'0561-13 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13° salário rescisório'),
    ('0588-06', u'0588-06 - IRRF - Rendimento do trabalho sem vínculo empregatício'),
    ('0610- 01', u'0610- 01 - IRRF - Rendimentos relativos a prestação de serviços de transporte rodoviário internacional de carga, pagos a transportador autônomo PF residente no Paraguai'),
    ('3533', u'3533 - Proventos de Aposentadoria, Reserva, Reforma ou Pensão Pagos por Previdência Pública'),
    ('3562-01', u'3562-01 - IRRF - Participação dos trabalhadores em Lucros ou Resultados (PLR). Origem S-1210, para definição do mês de ocorrência dos fatos geradores e os respectivos demonstrativos de pagamento constantes dos eventos S-1200, S- 1202,S-1207, S-2299 e S-2399.'),
]

