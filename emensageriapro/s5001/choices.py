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


CHOICES_S5001_IND13 = [
    (0, u'0 - Mensal'),
    (1, u'1 - 13° salário - {codIncCP} = [12, 14, 16, 22, 26, 32, 92, 94].'),
]


CHOICES_S5001_INDSIMPLES = [
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída. Evento de origem (S-1200/ S-2299/S-2399).'),
]


CHOICES_S5001_TPCR = [
    ('1082-01', u'1082-01 - Contribuição Previdenciária (CP) descontada do segurado empregado/avulso'),
    ('1082-02', u'1082-02 - CP descontada do segurado empregado rural curto prazo - Lei 11.718/2008'),
    ('1082-03', u'1082-03 - CP descontada do segurado empregado doméstico ou segurado especial'),
    ('1082-04', u'1082-04 - CP descontada do segurado especial curto prazo - Lei 11.718/2008'),
    ('1082-21', u'1082-21 - CP descontada do segurado empregado/avulso 13° salário'),
    ('1082-22', u'1082-22 - CP descontada do segurado empregado rural curto prazo 13° salário - Lei 11.718/2008'),
    ('1082-23', u'1082-23 - CP descontada do segurado empregado doméstico ou segurado especial 13° salário'),
    ('1082-24', u'1082-24 - CP descontada do segurado especial curto prazo 13° salário - Lei 11.718/2008'),
    ('1099-01', u'1099-01 - CP descontada do contribuinte individual, alíquota de 11%'),
    ('1099-02', u'1099-02 - CP descontada do contribuinte individual, alíquota de 20%. Validação: Se indApuracao = [2], tpCR = 1082-21, 1082,22, 1082-23, 1082- 24.'),
]

