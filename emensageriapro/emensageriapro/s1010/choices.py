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



CHOICES_S1010_CODINCFGTS_ALTERACAO = [

    ('00', u'00 - Não é Base de Cálculo do FGTS'),
    ('11', u'11 - Base de Cálculo do FGTS'),
    ('12', u'12 - Base de Cálculo do FGTS 13° salário'),
    ('21', u'21 - Base de Cálculo do FGTS Rescisório (aviso prévio)'),
    ('91', u'91 - Incidência suspensa em decorrência de decisão judicial.'),

]




CHOICES_S1010_CODINCFGTS_INCLUSAO = [

    ('00', u'00 - Não é Base de Cálculo do FGTS'),
    ('11', u'11 - Base de Cálculo do FGTS'),
    ('12', u'12 - Base de Cálculo do FGTS 13° salário'),
    ('21', u'21 - Base de Cálculo do FGTS Rescisório (aviso prévio)'),
    ('91', u'91 - Incidência suspensa em decorrência de decisão judicial.'),

]




CHOICES_S1010_CODINCSIND_ALTERACAO = [

    ('00', u'00 - Não é base de cálculo'),
    ('11', u'11 - Base de cálculo'),
    ('31', u'31 - Valor da contribuição sindical laboral descontada'),
    ('91', u'91 - Incidência suspensa em decorrência de decisão judicial.'),

]




CHOICES_S1010_CODINCSIND_INCLUSAO = [

    ('00', u'00 - Não é base de cálculo'),
    ('11', u'11 - Base de cálculo'),
    ('31', u'31 - Valor da contribuição sindical laboral descontada'),
    ('91', u'91 - Incidência suspensa em decorrência de decisão judicial.'),

]




CHOICES_S1010_EXTDECISAO_ALTERACAO = [

    (1, u'1 - Contribuição Previdenciária Patronal'),
    (2, u'2 - Contribuição Previdenciária Patronal + Descontada dos Segurados.'),

]




CHOICES_S1010_EXTDECISAO_INCLUSAO = [

    (1, u'1 - Contribuição Previdenciária Patronal'),
    (2, u'2 - Contribuição Previdenciária Patronal + Descontada dos Segurados.'),

]




CHOICES_S1010_TETOREMUN_ALTERACAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S1010_TETOREMUN_INCLUSAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S1010_TPPROC_ALTERACAO = [

    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial.'),

]




CHOICES_S1010_TPPROC_INCLUSAO = [

    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial.'),

]




CHOICES_S1010_TPRUBR_ALTERACAO = [

    (1, u'1 - Vencimento, provento ou pensão'),
    (2, u'2 - Desconto'),
    (3, u'3 - Informativa'),
    (4, u'4 - Informativa dedutora.'),

]




CHOICES_S1010_TPRUBR_INCLUSAO = [

    (1, u'1 - Vencimento, provento ou pensão'),
    (2, u'2 - Desconto'),
    (3, u'3 - Informativa'),
    (4, u'4 - Informativa dedutora.'),

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



