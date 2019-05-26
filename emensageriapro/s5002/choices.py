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




CHOICES_S5002_TPVALOR = [

    (11, u'11 - Remuneração Mensal'),
    (12, u'12 - 13o Salário'),
    (13, u'13 - Férias'),
    (14, u'14 - PLR'),
    (15, u'15 - Rendimentos Recebidos Acumuladamente - RRA'),
    (31, u'31 - (Retenções do IRRF efetuadas sobre) Remuneração Mensal'),
    (32, u'32 - (Retenções do IRRF efetuadas sobre) 13o Salário'),
    (33, u'33 - (Retenções do IRRF efetuadas sobre) Férias'),
    (34, u'34 - (Retenções do IRRF efetuadas sobre) PLR'),
    (35, u'35 - (Retenções do IRRF efetuadas sobre) RRA'),
    (41, u'41 - (Deduções da base de cálculo do IRRF) Previdência Social Oficial - PSO - Remuner. Mensal'),
    (42, u'42 - (Deduções da base de cálculo do IRRF) PSO - 13° salário'),
    (43, u'43 - (Deduções da base de cálculo do IRRF) PSO - Férias'),
    (44, u'44 - (Deduções da base de cálculo do IRRF) PSO - RRA'),
    (46, u'46 - (Deduções da base de cálculo do IRRF) Previdência Privada - salário mensal'),
    (47, u'47 - (Deduções da base de cálculo do IRRF) Previdência Privada - 13° salário'),
    (51, u'51 - (Deduções da base de cálculo do IRRF) Pensão Alimentícia - Remuneração Mensal'),
    (52, u'52 - (Deduções da base de cálculo do IRRF) Pensão Alimentícia - 13° salário'),
    (53, u'53 - (Deduções da base de cálculo do IRRF) Pensão Alimentícia - Férias'),
    (54, u'54 - (Deduções da base de cálculo do IRRF) Pensão Alimentícia - PLR'),
    (55, u'55 - (Deduções da base de cálculo do IRRF) Pensão Alimentícia - RRA'),
    (61, u'61 - (Deduções da base de cálculo do IRRF) Fundo de Aposentadoria Programada Individual - FAPI - Remuneração Mensal'),
    (62, u'62 - (Deduções da base de cálculo do IRRF) Fundo de Aposentadoria Programada Individual - FAPI - 13° salário'),
    (63, u'63 - (Deduções da base de cálculo do IRRF) Fundação de Previdência Complementar do Servidor Público - Funpresp - Remuneração Mensal'),
    (64, u'64 - (Deduções da base de cálculo do IRRF) Fundação de Previdência Complementar do Servidor Público - Funpresp - 13° salário'),
    (70, u'70 - (Isenções do IRRF) Parcela Isenta 65 anos - Remuneração Mensal'),
    (71, u'71 - (Isenções do IRRF) Parcela Isenta 65 anos - 13° salário'),
    (72, u'72 - (Isenções do IRRF) Diárias'),
    (73, u'73 - (Isenções do IRRF) Ajuda de Custo'),
    (74, u'74 - (Isenções do IRRF) Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho'),
    (75, u'75 - (Isenções do IRRF) Abono pecuniário'),
    (76, u'76 - (Isenções do IRRF) Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - Remuneração Mensal'),
    (77, u'77 - (Isenções do IRRF) Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - 13° salário'),
    (78, u'78 - (Isenções do IRRF) Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e alugueis'),
    (79, u'79 - (Isenções do IRRF) Outras isenções (identificar o nome da rubrica em S-1010)'),
    (81, u'81 - (Demandas Judiciais) Depósito Judicial'),
    (82, u'82 - (Demandas Judiciais) Compensação Judicial do ano calendário'),
    (83, u'83 - (Demandas Judiciais) Compensação Judicial de anos anteriores'),
    (91, u'91 - (Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre) Remuneração Mensal'),
    (92, u'92 - (Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre) 13o Salário'),
    (93, u'93 - (Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre)Férias'),
    (94, u'94 - (Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre) PLR'),
    (95, u'95 - (Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre) RRA.'),
    
]



