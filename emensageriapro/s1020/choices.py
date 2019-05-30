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
    
]




CHOICES_ESOCIALLOTACOESTRIBUTARIASTIPOS = [

    ('01', u'01 - Classificação da atividade econômica exercida pela Pessoa Jurídica para fins de atribuição de código FPAS, inclusive obras de construção civil própria, exceto: a) empreitada parcial ou sub-empreitada de obra de construção civil (utilizar opção 02), b) prestação de serviços em instalações de terceiros (utilizar opções 03 a 09), c) Embarcação inscrita no Registro Especial Brasileiro - REB (utilizar opção 10).'),
    ('02', u'02 - Obra de Construção Civil - Empreitada Parcial ou Sub- empreitada'),
    ('03', u'03 - Pessoa Física Tomadora de Serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa'),
    ('04', u'04 - Pessoa Jurídica Tomadora de Serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991'),
    ('05', u'05 - Pessoa Jurídica Tomadora de Serviços prestados por cooperados por intermédio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta'),
    ('06', u'06 - Entidade beneficente/isenta Tomadora de Serviços prestados por cooperados por intermédio de cooperativa de trabalho'),
    ('07', u'07 - Pessoa Física tomadora de Serviços prestados por Cooperados por intermédio de Cooperativa de Trabalho'),
    ('08', u'08 - Operador Portuário tomador de serviços de trabalhadores avulsos'),
    ('09', u'09 - Contratante de trabalhadores avulsos não portuários por intermédio de Sindicato'),
    ('10', u'10 - Embarcação inscrita no Registro Especial Brasileiro - REB'),
    ('21', u'21 - Classificação da atividade econômica ou obra própria de construção civil da Pessoa Física'),
    ('24', u'24 - Empregador Doméstico'),
    ('90', u'90 - Atividades desenvolvidas no exterior por trabalhador vinculado ao Regime Geral de Previdência Social (expatriados)'),
    ('91', u'91 - Atividades desenvolvidas por trabalhador estrangeiro vinculado a Regime de Previdência Social Estrangeiro'),
    
]




CHOICES_S1020_TPINSCCONTRAT_ALTERACAO = [

    (1, u'1 - CNPJ'),
    (2, u'2 - CPF.'),
    
]




CHOICES_S1020_TPINSCCONTRAT_INCLUSAO = [

    (1, u'1 - CNPJ'),
    (2, u'2 - CPF.'),
    
]




PERIODOS = [

    ('2017-01', u'Janeiro/2017'),
    ('2017-02', u'Fevereiro/2017'),
    ('2017-03', u'Março/2017'),
    ('2017-04', u'Abril/2017'),
    ('2017-05', u'Maio/2017'),
    ('2017-06', u'Junho/2017'),
    ('2017-07', u'Julho/2017'),
    ('2017-08', u'Agosto/2017'),
    ('2017-09', u'Setembro/2017'),
    ('2017-10', u'Outubro/2017'),
    ('2017-11', u'Novembro/2017'),
    ('2017-12', u'Dezembro/2017'),
    ('2018-01', u'Janeiro/2018'),
    ('2018-02', u'Fevereiro/2018'),
    ('2018-03', u'Março/2018'),
    ('2018-04', u'Abril/2018'),
    ('2018-05', u'Maio/2018'),
    ('2018-06', u'Junho/2018'),
    ('2018-07', u'Julho/2018'),
    ('2018-08', u'Agosto/2018'),
    ('2018-09', u'Setembro/2018'),
    ('2018-10', u'Outubro/2018'),
    ('2018-11', u'Novembro/2018'),
    ('2018-12', u'Dezembro/2018'),
    ('2019-01', u'Janeiro/2019'),
    ('2019-02', u'Fevereiro/2019'),
    ('2019-03', u'Março/2019'),
    ('2019-04', u'Abril/2019'),
    ('2019-05', u'Maio/2019'),
    ('2019-06', u'Junho/2019'),
    ('2019-07', u'Julho/2019'),
    ('2019-08', u'Agosto/2019'),
    ('2019-09', u'Setembro/2019'),
    ('2019-10', u'Outubro/2019'),
    ('2019-11', u'Novembro/2019'),
    ('2019-12', u'Dezembro/2019'),
    
]



