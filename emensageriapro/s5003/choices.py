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




CHOICES_S5003_MTVDESLIGTSV = [

    ('01', u'01'),
    ('02', u'02'),
    ('03', u'03'),
    ('04', u'04'),
    ('05', u'05'),
    ('06', u'06'),
    ('07', u'07'),
    ('99', u'99'),
    
]




CHOICES_S5003_TPDPS = [

    (51, u'51 - Depósito do FGTS'),
    (52, u'52 - Depósito do FGTS 13° Salário'),
    (53, u'53 - Depósito do FGTS Dissídio'),
    (54, u'54 - Depósito do FGTS Dissídio 13º Salário'),
    (55, u'55 - Depósito do FGTS - Aprendiz'),
    (56, u'56 - Depósito do FGTS 13° Salário - Aprendiz'),
    (57, u'57 - Depósito do FGTS Dissídio - Aprendiz'),
    (58, u'58 - Depósito do FGTS Dissídio 13º Salário - Aprendiz'),
    (61, u'61 - Depósito do FGTS Rescisório'),
    (62, u'62 - Depósito do FGTS Rescisório - 13° Salário'),
    (63, u'63 - Depósito do FGTS Rescisório - Aviso Prévio'),
    (64, u'64 - Depósito do FGTS Rescisório - Dissídio'),
    (65, u'65 - Depósito do FGTS Rescisório - Dissídio 13º Salário'),
    (66, u'66 - Depósito do FGTS Rescisório - Dissídio Aviso Prévio'),
    (67, u'67 - Depósito do FGTS Rescisório - Aprendiz'),
    (68, u'68 - Depósito do FGTS Rescisório - 13° Salário Aprendiz'),
    (69, u'69 - Depósito do FGTS Rescisório - Aviso Prévio Aprendiz'),
    (70, u'70 - Depósito do FGTS Rescisório - Dissídio Aprendiz'),
    (71, u'71 - Depósito do FGTS Rescisório - Dissídio 13° Salário Aprendiz'),
    (72, u'72 - Depósito do FGTS Rescisório - Dissídio Aviso Prévio Aprendiz.'),
    
]




CHOICES_S5003_TPDPSE = [

    (53, u'53 - Depósito do FGTS Dissídio'),
    (54, u'54 - Depósito do FGTS Dissídio 13º Salário'),
    (57, u'57 - Depósito do FGTS Dissídio - Aprendiz'),
    (58, u'58 - Depósito do FGTS Dissídio 13º Salário - Aprendiz'),
    (64, u'64 - Depósito do FGTS Rescisório - Dissídio'),
    (65, u'65 - Depósito do FGTS Rescisório - Dissídio 13º Salário'),
    (66, u'66 - Depósito do FGTS Rescisório - Dissídio Aviso Prévio'),
    (70, u'70 - Depósito do FGTS Rescisório - Dissídio Aprendiz'),
    (71, u'71 - Depósito do FGTS Rescisório - Dissídio 13° Salário Aprendiz'),
    (72, u'72 - Depósito do FGTS Rescisório - Dissídio Aviso Prévio Aprendiz.'),
    
]




CHOICES_S5003_TPVALORE = [

    (13, u'13 - Base de Cálculo do FGTS Dissídio'),
    (14, u'14 - Base de Cálculo do FGTS Dissídio 13º Salário'),
    (17, u'17 - Base de Cálculo do FGTS Dissídio - Aprendiz'),
    (18, u'18 - Base de Cálculo do FGTS Dissídio 13º Salário - Aprendiz'),
    (24, u'24 - Base de Cálculo do FGTS Rescisório - Dissídio'),
    (25, u'25 - Base de Cálculo do FGTS Rescisório - Dissídio 13º Salário'),
    (26, u'26 - Base de Cálculo do FGTS Rescisório - Dissídio Aviso Prévio'),
    (30, u'30 - Base de Cálculo do FGTS Rescisório - Dissídio Aprendiz'),
    (31, u'31 - Base de Cálculo do FGTS Rescisório - Dissídio 13° Salário Aprendiz'),
    (32, u'32 - Base de Cálculo do FGTS Rescisório - Dissídio Aviso Prévio Aprendiz'),
    (91, u'91 - Incidência suspensa em decorrência de decisão judicial.'),
    
]



