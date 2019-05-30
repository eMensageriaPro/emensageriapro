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



CHOICES_EFDREINFRENDIMENTOSBENEFICIARIOSEXTERIORTRIBUTACAO = [

    ('10', u'10 - Retenção do IRRF - alíquota padrão.'),
    ('11', u'11 - Retenção do IRRF - alíquota da tabela progressiva.'),
    ('12', u'12 - Retenção do IRRF - alíquota diferenciada (países com tributação favorecida).'),
    ('13', u'13 - Retenção do IRRF - alíquota limitada conforme cláusula em convênio.'),
    ('30', u'30 - Retenção do IRRF - outras hipóteses.'),
    ('40', u'40 - Não retenção do IRRF - isenção estabelecida em convênio.'),
    ('41', u'41 - Não retenção do IRRF - isenção prevista em lei interna'),
    ('42', u'42 - Não retenção do IRRF - alíquota Zero prevista em lei interna'),
    ('43', u'43 - Não retenção do IRRF - pagamento antecipado do imposto'),
    ('44', u'44 - Não retenção do IRRF - medida Judicial'),
    ('50', u'50 - Não retenção do IRRF - outras hipóteses'),
    
]




CHOICES_R4010_INDDECTERC = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_R4010_INDNIF = [

    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF.'),
    
]




CHOICES_R4010_INDORIGREC_INFOPROCJUD = [

    (1, u'1 - Recursos do próprio declarante'),
    (2, u'2 - Recursos de terceiros - Declarante é a Instituição Financeira responsável apenas pelo repasse dos valores.'),
    
]




CHOICES_R4010_INDORIGREC_INFORRA = [

    (1, u'1 - Recursos do próprio declarante'),
    (2, u'2 - Recursos de terceiros - Declarante é a Instituição Financeira responsável apenas pelo repasse dos valores.'),
    
]




CHOICES_R4010_INDTPDEDUCAO = [

    (1, u'1 - Previdência Oficial'),
    (2, u'2 - Previdência Privada'),
    (3, u'3 - Fapi'),
    (4, u'4 - Funpresp'),
    (5, u'5 - Pensão Alimentícia'),
    (6, u'6 - Contribuição do ente público patrocinador'),
    (7, u'7 - Dependentes.'),
    
]




CHOICES_R4010_RELDEP = [

    (1, u'1 - Neto, bisneto'),
    (2, u'2 - Irmão'),
    (3, u'3 - Cônjuge/companheiro'),
    (4, u'4 - Filho'),
    (5, u'5 - Pais, avós e bisavós'),
    (6, u'6 - Enteado'),
    (7, u'7 - Sogro'),
    (99, u'99 - Agregado/Outros.'),
    
]




CHOICES_R4010_TPINSC = [

    (1, u'1 - Pessoa Jurídica'),
    (2, u'2 - Pessoa Física.'),
    
]




CHOICES_R4010_TPINSCADV_INFOPROCJUD = [

    (1, u'1 - Pessoa Física'),
    (2, u'2 - Pessoa Jurídica.'),
    
]




CHOICES_R4010_TPINSCADV_INFORRA = [

    (1, u'1 - Pessoa Física'),
    (2, u'2 - Pessoa Jurídica.'),
    
]




CHOICES_R4010_TPISENCAO = [

    (1, u'1 - Parcela Isenta 65 anos'),
    (2, u'2 - Diária de viagem'),
    (3, u'3 - Indenização e rescisão de contrato, inclusive a título de PDV'),
    (4, u'4 - Abono pecuniário'),
    (5, u'5 - Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e alugueis'),
    (6, u'6 - Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço'),
    (7, u'7 - Complementação de aposentadoria, correspondente às contribuições efetuadas no período de 01/01/1989 a 31/12/1995'),
    (8, u'8 - Ajuda de custo'),
    (99, u'99 - Outros (especificar).'),
    
]




CHOICES_R4010_TPPROCRET = [

    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial.'),
    
]




CHOICES_R4010_TPPROCRRA_INFORRA = [

    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial.'),
    
]



