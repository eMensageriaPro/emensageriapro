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



CHOICES_S5013_TPDPS = [

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




CHOICES_S5013_TPDPSE = [

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




CHOICES_S5013_TPVALOR = [

    (11, u'11 - Base de Cálculo do FGTS'),
    (12, u'12 - Base de Cálculo do FGTS 13° Salário'),
    (13, u'13 - Base de Cálculo do FGTS Dissídio'),
    (14, u'14 - Base de Cálculo do FGTS Dissídio 13º Salário'),
    (15, u'15 - Base de Cálculo do FGTS - Aprendiz'),
    (16, u'16 - Base de Cálculo do FGTS 13° Salário - Aprendiz'),
    (17, u'17 - Base de Cálculo do FGTS Dissídio - Aprendiz'),
    (18, u'18 - Base de Cálculo do FGTS Dissídio 13º Salário - Aprendiz'),
    (21, u'21 - Base de Cálculo do FGTS Rescisório'),
    (22, u'22 - Base de Cálculo do FGTS Rescisório - 13° Salário'),
    (23, u'23 - Base de Cálculo do FGTS Rescisório - Aviso Prévio'),
    (24, u'24 - Base de Cálculo do FGTS Rescisório - Dissídio'),
    (25, u'25 - Base de Cálculo do FGTS Rescisório - Dissídio 13º Salário'),
    (26, u'26 - Base de Cálculo do FGTS Rescisório - Dissídio Aviso Prévio'),
    (27, u'27 - Base de Cálculo do FGTS Rescisório - Aprendiz'),
    (28, u'28 - Base de Cálculo do FGTS Rescisório - 13° Salário Aprendiz'),
    (29, u'29 - Base de Cálculo do FGTS Rescisório - Aviso Prévio Aprendiz'),
    (30, u'30 - Base de Cálculo do FGTS Rescisório - Dissídio Aprendiz'),
    (31, u'31 - Base de Cálculo do FGTS Rescisório - Dissídio 13° Salário Aprendiz'),
    (32, u'32 - Base de Cálculo do FGTS Rescisório - Dissídio Aviso Prévio Aprendiz'),
    (91, u'91 - Incidência suspensa em decorrência de decisão judicial.'),
    
]




CHOICES_S5013_TPVALORE = [

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



