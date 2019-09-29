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



CHOICES_S1070_INDAUTORIA_ALTERACAO = [

    (1, u'1 - Próprio contribuinte'),
    (2, u'2 - Outra entidade, empresa ou empregado.'),

]




CHOICES_S1070_INDAUTORIA_INCLUSAO = [

    (1, u'1 - Próprio contribuinte'),
    (2, u'2 - Outra entidade, empresa ou empregado.'),

]




CHOICES_S1070_INDDEPOSITO_ALTERACAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S1070_INDDEPOSITO_INCLUSAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S1070_INDMATPROC_ALTERACAO = [

    (1, u'1 - Exclusivamente tributária ou tributária e FGTS'),
    (2, u'2 - Autorização de trabalho de menor'),
    (3, u'3 - Dispensa, ainda que parcial, de contratação de pessoa com deficiência (PCD)'),
    (4, u'4 - Dispensa, ainda que parcial, de contratação de aprendiz'),
    (5, u'5 - Segurança e Saúde no Trabalho'),
    (6, u'6 - Conversão de Licença Saúde em Acidente de Trabalho'),
    (7, u'7 - Exclusivamente FGTS e/ou Contribuição Social Rescisória (Lei Complementar 110/2001)'),
    (8, u'8 - Contribuição sindical'),
    (99, u'99 - Outros assuntos.'),

]




CHOICES_S1070_INDMATPROC_INCLUSAO = [

    (1, u'1 - Exclusivamente tributária ou tributária e FGTS'),
    (2, u'2 - Autorização de trabalho de menor'),
    (3, u'3 - Dispensa, ainda que parcial, de contratação de pessoa com deficiência (PCD)'),
    (4, u'4 - Dispensa, ainda que parcial, de contratação de aprendiz'),
    (5, u'5 - Segurança e Saúde no Trabalho'),
    (6, u'6 - Conversão de Licença Saúde em Acidente de Trabalho'),
    (7, u'7 - Exclusivamente FGTS e/ou Contribuição Social Rescisória (Lei Complementar 110/2001)'),
    (8, u'8 - Contribuição sindical'),
    (99, u'99 - Outros assuntos.'),

]




CHOICES_S1070_INDSUSP_ALTERACAO = [

    ('01', u'01 - Liminar em Mandado de Segurança'),
    ('02', u'02 - Depósito Judicial do Montante Integral'),
    ('03', u'03 - Depósito Administrativo do Montante Integral'),
    ('04', u'04 - Antecipação de Tutela'),
    ('05', u'05 - Liminar em Medida Cautelar'),
    ('08', u'08 - Sentença em Mandado de Segurança Favorável ao Contribuinte'),
    ('09', u'09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF'),
    ('10', u'10 - Acórdão do TRF Favorável ao Contribuinte'),
    ('11', u'11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte'),
    ('12', u'12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte'),
    ('13', u'13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo'),
    ('14', u'14 - Contestação Administrativa FAP'),
    ('90', u'90 - Decisão Definitiva a favor do contribuinte'),
    ('92', u'92 - Sem suspensão da exigibilidade.'),

]




CHOICES_S1070_INDSUSP_INCLUSAO = [

    ('01', u'01 - Liminar em Mandado de Segurança'),
    ('02', u'02 - Depósito Judicial do Montante Integral'),
    ('03', u'03 - Depósito Administrativo do Montante Integral'),
    ('04', u'04 - Antecipação de Tutela'),
    ('05', u'05 - Liminar em Medida Cautelar'),
    ('08', u'08 - Sentença em Mandado de Segurança Favorável ao Contribuinte'),
    ('09', u'09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF'),
    ('10', u'10 - Acórdão do TRF Favorável ao Contribuinte'),
    ('11', u'11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte'),
    ('12', u'12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte'),
    ('13', u'13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo'),
    ('14', u'14 - Contestação Administrativa FAP'),
    ('90', u'90 - Decisão Definitiva a favor do contribuinte'),
    ('92', u'92 - Sem suspensão da exigibilidade.'),

]




CHOICES_S1070_TPPROC_ALTERACAO = [

    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
    (3, u'3 - Número de Benefício (NB) do INSS'),
    (4, u'4 - Processo FAP de exercício anterior a 2019.'),

]




CHOICES_S1070_TPPROC_EXCLUSAO = [

    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
    (3, u'3 - Número de Benefício (NB) do INSS'),
    (4, u'4 - Processo FAP.'),

]




CHOICES_S1070_TPPROC_INCLUSAO = [

    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
    (3, u'3 - Número de Benefício (NB) do INSS'),
    (4, u'4 - Processo FAP de exercício anterior a 2019.'),

]




ESTADOS = [

    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AM', u'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', u'Minas Gerais'),
    ('MS', u'Mato Grosso do Sul'),
    ('MT', u'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('RS', u'Rio Grande do Sul'),
    ('SC', u'Santa Catarina'),
    ('SE', u'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', u'Tocantins'),

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



