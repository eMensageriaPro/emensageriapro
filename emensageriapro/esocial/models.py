#coding: utf-8

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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model

STATUS_EVENTO_CADASTRADO = 0
STATUS_EVENTO_IMPORTADO = 1
STATUS_EVENTO_DUPLICADO = 2
STATUS_EVENTO_GERADO = 3
STATUS_EVENTO_GERADO_ERRO = 4
STATUS_EVENTO_ASSINADO = 5
STATUS_EVENTO_ASSINADO_ERRO = 6
STATUS_EVENTO_VALIDADO = 7
STATUS_EVENTO_VALIDADO_ERRO = 8
STATUS_EVENTO_AGUARD_PRECEDENCIA = 9
STATUS_EVENTO_AGUARD_ENVIO = 10
STATUS_EVENTO_ENVIADO = 11
STATUS_EVENTO_ENVIADO_ERRO = 12
STATUS_EVENTO_PROCESSADO = 13



CHOICES_S1000_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1000_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1000_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1005_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1005_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1005_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1010_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1010_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1010_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1020_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1020_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1020_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1030_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1030_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1030_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1035_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1035_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1035_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1040_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1040_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1040_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1050_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1050_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1050_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1060_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1060_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1060_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_S1070_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1070_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1070_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1080_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1080_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1080_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1200_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1200_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1200_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1200_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1200_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1202_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1202_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1202_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1202_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1202_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1207_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1207_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1207_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1207_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1207_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1210_INDAPURACAO = (
    (1, u'1 - Mensal'),
)

CHOICES_S1210_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1210_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1210_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1210_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1250_INDAPURACAO = (
    (1, u'1 - Mensal'),
)

CHOICES_S1250_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1250_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1250_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1250_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1250_TPINSCADQ = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1260_INDAPURACAO = (
    (1, u'1 - Mensal'),
)

CHOICES_S1260_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1260_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1260_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1260_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1270_INDAPURACAO = (
    (1, u'1 - Mensal'),
)

CHOICES_S1270_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1270_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1270_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1270_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1280_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1280_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1280_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1280_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1280_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1295_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1295_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1295_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1295_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1298_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1298_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1298_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1298_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1299_EVTAQPROD = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1299_EVTCOMPROD = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1299_EVTCONTRATAVNP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1299_EVTINFOCOMPLPER = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1299_EVTPGTOS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1299_EVTREMUN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1299_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1299_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1299_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1299_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1300_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual'),
)

CHOICES_S1300_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1300_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S1300_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1300_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2190_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2190_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2190_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2200_CADINI = (
    ('N', u'N - Não (Admissão)'),
    ('S', u'S - Sim (Cadastramento Inicial)'),
)

CHOICES_S2200_CLAUASSEC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_ESTCIV = (
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo'),
)

CHOICES_S2200_GRAUINSTR = (
    ('01', u'01 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou'),
    ('02', u'02 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular'),
    ('03', u'03 - 5º ano completo do Ensino Fundamental'),
    ('04', u'04 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)'),
    ('05', u'05 - Ensino Fundamental Completo'),
    ('06', u'06 - Ensino Médio incompleto'),
    ('07', u'07 - Ensino Médio completo'),
    ('08', u'08 - Educação Superior incompleta'),
    ('09', u'09 - Educação Superior completa'),
    ('10', u'10 - Pós-Graduação completa'),
    ('11', u'11 - Mestrado completo'),
    ('12', u'12 - Doutorado completo'),
)

CHOICES_S2200_INDPRIEMPR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2200_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2200_RACACOR = (
    (1, u'1 - Branca'),
    (2, u'2 - Negra'),
    (3, u'3 - Parda (parda ou declarada como mulata, cabocla, cafuza, mameluca ou mestiça de negro com pessoa de outra cor ou raça)'),
    (4, u'4 - Amarela (de origem japonesa, chinesa, coreana etc)'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado'),
)

CHOICES_S2200_SEXO = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2200_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2200_TPCONTR = (
    (1, u'1 - Prazo indeterminado'),
    (2, u'2 - Prazo determinado'),
)

CHOICES_S2200_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2200_TPREGPREV = (
    (1, u'1 - Regime Geral da Previdência Social - RGPS'),
    (2, u'2 - Regime Próprio de Previdência Social - RPPS'),
    (3, u'3 - Regime de Previdência Social no Exterior'),
)

CHOICES_S2200_TPREGTRAB = (
    (1, u'1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas'),
    (2, u'2 - Estatutário'),
)

CHOICES_S2200_UNDSALFIXO = (
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável'),
)

CHOICES_S2205_ESTCIV = (
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo'),
)

CHOICES_S2205_GRAUINSTR = (
    ('01', u'01 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou'),
    ('02', u'02 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular'),
    ('03', u'03 - 5º ano completo do Ensino Fundamental'),
    ('04', u'04 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)'),
    ('05', u'05 - Ensino Fundamental Completo'),
    ('06', u'06 - Ensino Médio incompleto'),
    ('07', u'07 - Ensino Médio completo'),
    ('08', u'08 - Educação Superior incompleta'),
    ('09', u'09 - Educação Superior completa'),
    ('10', u'10 - Pós-Graduação completa'),
    ('11', u'11 - Mestrado completo'),
    ('12', u'12 - Doutorado completo'),
)

CHOICES_S2205_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2205_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2205_RACACOR = (
    (1, u'1 - Branca'),
    (2, u'2 - Negra'),
    (3, u'3 - Parda (parda ou declarada como mulata, cabocla, cafuza, mameluca ou mestiça de negro com pessoa de outra cor ou raça)'),
    (4, u'4 - Amarela (de origem japonesa, chinesa, coreana etc)'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado'),
)

CHOICES_S2205_SEXO = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2205_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2205_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2206_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2206_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2206_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2206_TPCONTR = (
    (1, u'1 - Prazo indeterminado'),
    (2, u'2 - Prazo determinado'),
)

CHOICES_S2206_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2206_TPREGPREV = (
    (1, u'1 - Regime Geral da Previdência Social - RGPS'),
    (2, u'2 - Regime Próprio de Previdência Social - RPPS'),
    (3, u'3 - Regime de Previdência Social no Exterior'),
)

CHOICES_S2206_UNDSALFIXO = (
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável'),
)

CHOICES_S2210_CODSITGERADORA = (
    (200004300, u'200004300 - Impacto de pessoa contra objeto parado'),
    (200004600, u'200004600 - Impacto de pessoa contra objeto em movimento'),
    (200008300, u'200008300 - Impacto sofrido por pessoa de objeto que cai'),
    (200008600, u'200008600 - Impacto sofrido por pessoa de objeto projetado'),
    (200008900, u'200008900 - Impacto sofrido por pessoa, NIC'),
    (200012200, u'200012200 - Queda de pessoa com diferença de nível de andaime, passagem, plataforma, etc.'),
    (200012300, u'200012300 - Queda de pessoa com diferença de nível de escada móvel ou fixada cujos degraus'),
    (200012400, u'200012400 - Queda de pessoa com diferença de nível de material empilhado'),
    (200012500, u'200012500 - Queda de pessoa com diferença de nível de veículo'),
    (200012600, u'200012600 - Queda de pessoa com diferença de nível em escada permanente'),
    (200012700, u'200012700 - Queda de pessoa com diferença de nível em poço, escavação, abertura no piso, etc.'),
    (200012900, u'200012900 - Queda de pessoa com diferença de nível, NIC'),
    (200016300, u'200016300 - Queda de pessoa em mesmo nível em passagem ou superfície de sustentação'),
    (200016600, u'200016600 - Queda de pessoa em mesmo nível sobre ou contra alguma coisa'),
    (200016900, u'200016900 - Queda de pessoa em mesmo nível, NIC'),
    (200020100, u'200020100 - Aprisionamento em, sobre ou entre objetos em movimento convergente'),
    (200020300, u'200020300 - Aprisionamento em, sobre ou entre objeto parado e outro em movimento'),
    (200020500, u'200020500 - Aprisionamento em, sobre ou entre dois ou mais objetos em movimento'),
    (200020700, u'200020700 - Aprisionamento em, sobre ou entre desabamento ou desmoronamento'),
    (200020900, u'200020900 - Aprisionamento em, sob ou entre, NIC'),
    (200024300, u'200024300 - Atrito ou abrasão por encostar, pisar, ajoelhar ou sentar em objeto'),
    (200024400, u'200024400 - Atrito ou abrasão por manusear objeto'),
    (200024500, u'200024500 - Atrito ou abrasão por objeto em vibração'),
    (200024600, u'200024600 - Atrito ou abrasão por corpo estranho no olho'),
    (200024700, u'200024700 - Atrito ou abrasão por compressão repetitiva'),
    (200024900, u'200024900 - Atrito ou abrasão, NIC'),
    (200028300, u'200028300 - Reação do corpo a movimento involuntário'),
    (200028600, u'200028600 - Reação do corpo a movimento voluntário'),
    (200032200, u'200032200 - Esforço excessivo ao erguer objeto'),
    (200032400, u'200032400 - Esforço excessivo ao empurrar ou puxar objeto'),
    (200032600, u'200032600 - Esforço excessivo ao manejar, sacudir ou arremessar objeto'),
    (200032900, u'200032900 - Esforço excessivo, NIC'),
    (200036000, u'200036000 - Elétrica, exposição a energia'),
    (200040300, u'200040300 - Temperatura muito alta, contato com objeto ou substância a'),
    (200040600, u'200040600 - Temperatura muito baixa, contato com objeto ou substância a'),
    (200044300, u'200044300 - Temperatura ambiente elevada, exposição a'),
    (200044600, u'200044600 - Temperatura ambiente baixa, exposição a'),
    (200048200, u'200048200 - Inalação de substância cáustica, tóxica ou nociva'),
    (200048400, u'200048400 - Ingestão de substância cáustica'),
    (200048600, u'200048600 - Absorção de substância cáustica'),
    (200048900, u'200048900 - Inalação, ingestão ou absorção, NIC'),
    (200052000, u'200052000 - Imersão'),
    (200056000, u'200056000 - Radiação não ionizante, exposição a'),
    (200060000, u'200060000 - Radiação ionizante, exposição a'),
    (200064000, u'200064000 - Ruído, exposição a'),
    (200068000, u'200068000 - Vibração, exposição a'),
    (200072000, u'200072000 - Pressão ambiente, exposição a'),
    (200072300, u'200072300 - Exposição à pressão ambiente elevada'),
    (200072600, u'200072600 - Exposição à pressão ambiente baixa'),
    (200076200, u'200076200 - Poluição da água, ação da (exposição à poluição da água)'),
    (200076400, u'200076400 - Poluição do ar, ação da (exposição à poluição do ar)'),
    (200076600, u'200076600 - Poluição do solo, ação da (exposição à poluição do solo)'),
    (200076900, u'200076900 - Poluição, NIC, exposição a (exposição à poluição, NIC)'),
    (200080200, u'200080200 - Ataque de ser vivo por mordedura, picada, chifrada, coice, etc.'),
    (200080400, u'200080400 - Ataque de ser vivo com peçonha'),
    (200080600, u'200080600 - Ataque de ser vivo com transmissão de doença'),
    (200080900, u'200080900 - Ataque de ser vivo, NIC'),
    (209000000, u'209000000 - Tipo, NIC'),
    (209500000, u'209500000 - Tipo inexistente'),
)

CHOICES_S2210_INDCATOBITO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2210_INDCOMUNPOLICIA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2210_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2210_INICIATCAT = (
    (1, u'1 - Iniciativa do Registrador (identificado em {ideRegistrador})'),
    (2, u'2 - Ordem judicial'),
    (3, u'3 - Determinação de órgão fiscalizador'),
)

CHOICES_S2210_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2210_TPACID = (
    ('1.0.01', u'1.0.01 - Lesão corporal que cause a morte ou a perda ou redução, permanente ou temporária, da capacidade para o trabalho, desde que não enquadrada em nenhum dos demais códigos.'),
    ('1.0.02', u'1.0.02 - Perturbação funcional que cause a morte ou a perda ou redução, permanente ou temporária, da capacidade para o trabalho, desde que não enquadrada em nenhum dos demais códigos.'),
    ('2.0.01', u'2.0.01 - Doença profissional, assim entendida a produzida ou desencadeada pelo exercício do trabalho peculiar a determinada atividade e constante da respectiva relação elaborada pelo Ministério do Trabalho e Previdência Social, desde que não enquadrada em (...)'),
    ('2.0.02', u'2.0.02 - Doença do trabalho, assim entendida a adquirida ou desencadeada em função de condições especiais em que o trabalho é realizado e com ele se relacione diretamente, constante da respectiva relação elaborada pelo Ministério do Trabalho e Previdência (...)'),
    ('2.0.03', u'2.0.03 - Doença proveniente de contaminação acidental do empregado no exercício de sua atividade.'),
    ('2.0.04', u'2.0.04 - Doença endêmica adquirida por segurado habitante de região em que ela se desenvolva quando resultante de exposição ou contato direto determinado pela natureza do trabalho.'),
    ('2.0.05', u'2.0.05 - Doença profissional ou do trabalho não incluída na relação elaborada pelo Ministério do Trabalho e Previdência Social quando resultante das condições especiais em que o trabalho é executado e com ele se relaciona diretamente.'),
    ('2.0.06', u'2.0.06 - Doença profissional ou do trabalho enquadrada na relação elaborada pelo Ministério do Trabalho e Previdência Social relativa nexo técnico epidemiológico previdenciário - NTEP.'),
    ('3.0.01', u'3.0.01 - Acidente ligado ao trabalho que, embora não tenha sido a causa única, haja contribuído diretamente para a morte do segurado, para redução ou perda da sua capacidade para o trabalho, ou produzido lesão que exija atenção médica para a sua recuperaçã (...)'),
    ('3.0.02', u'3.0.02 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de ato de agressão, sabotagem ou terrorismo praticado por terceiro ou companheiro de trabalho.'),
    ('3.0.03', u'3.0.03 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de ofensa física intencional, inclusive de terceiro, por motivo de disputa relacionada ao trabalho.'),
    ('3.0.04', u'3.0.04 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de ato de imprudência, de negligência ou de imperícia de terceiro ou de companheiro de trabalho.'),
    ('3.0.05', u'3.0.05 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de ato de pessoa privada do uso da razão.'),
    ('3.0.06', u'3.0.06 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de desabamento, inundação, incêndio e outros casos fortuitos ou decorrentes de força maior.'),
    ('3.0.07', u'3.0.07 - Acidente sofrido pelo segurado ainda que fora do local e horário de trabalho na execução de ordem ou na realização de serviço sob a autoridade da empresa.'),
    ('3.0.08', u'3.0.08 - Acidente sofrido pelo segurado ainda que fora do local e horário de trabalho na prestação espontânea de qualquer serviço à empresa para lhe evitar prejuízo ou proporcionar proveito.'),
    ('3.0.09', u'3.0.09 - Acidente sofrido pelo segurado ainda que fora do local e horário de trabalho em viagem a serviço da empresa, inclusive para estudo quando financiada por esta dentro de seus planos para melhor capacitação da mão-de- obra, independentemente do meio (...)'),
    ('3.0.10', u'3.0.10 - Acidente sofrido pelo segurado ainda que fora do local e horário de trabalho no percurso da residência para o local de trabalho ou deste para aquela, qualquer que seja o meio de locomoção, inclusive veículo de propriedade do segurado.'),
    ('3.0.11', u'3.0.11 - Acidente sofrido pelo segurado nos períodos destinados a refeição ou descanso, ou por ocasião da satisfação de outras necessidades fisiológicas, no local do trabalho ou durante este.'),
    ('4.0.01', u'4.0.01 - Suspeita de doenças profissionais ou do trabalho produzidas pelas condições especiais de trabalho, nos termos do art 169 da CLT.'),
    ('4.0.02', u'4.0.02 - Constatação de ocorrência ou agravamento de doenças profissionais, através de exames médicos que incluam os definidos na NR 07; ou sendo verificadas alterações que revelem qualquer tipo de disfunção de órgão ou sistema biológico, através dos exame (...)'),
    ('5.0.01', u'5.0.01 - Outros'),
)

CHOICES_S2210_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2210_TPCAT = (
    (1, u'1 - Inicial'),
    (2, u'2 - Reabertura'),
    (3, u'3 - Comunicação de Óbito'),
)

CHOICES_S2210_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2210_TPLOCAL = (
    (1, u'1 - Estabelecimento do empregador no Brasil'),
    (2, u'2 - Estabelecimento do empregador no Exterior'),
    (3, u'3 - Estabelecimento de terceiros onde o empregador presta serviços'),
    (4, u'4 - Via pública'),
    (5, u'5 - Área rural'),
    (6, u'6 - Embarcação'),
    (9, u'9 - Outros'),
)

CHOICES_S2220_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2220_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2220_RESASO = (
    (1, u'1 - Apto'),
    (2, u'2 - Inapto'),
)

CHOICES_S2220_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2220_TPASO = (
    (0, u'0 - Admissional'),
    (1, u'1 - Periódico, conforme planejamento do PCMSO'),
    (2, u'2 - De retorno ao trabalho'),
    (3, u'3 - De mudança de função'),
    (4, u'4 - De monitoração pontual, não enquadrado nos casos anteriores'),
    (8, u'8 - Demissional'),
)

CHOICES_S2220_TPEXAMEOCUP = (
    (0, u'0 - Exame médico admissional'),
    (1, u'1 - Exame médico periódico, conforme NR7 do MTb e/ou planejamento do PCMSO'),
    (2, u'2 - Exame médico de retorno ao trabalho'),
    (3, u'3 - Exame médico de mudança de função'),
    (4, u'4 - Exame médico de monitoração pontual, não enquadrado nos demais casos'),
    (9, u'9 - Exame médico demissional'),
)

CHOICES_S2220_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_S2221_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2221_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2221_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2221_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_S2230_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2230_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2230_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2230_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2231_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_S2231_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2231_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2240_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2240_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2240_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2240_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2241_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2241_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2241_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2241_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2245_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_S2245_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2245_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2245_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_S2250_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2250_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2250_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2250_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2260_INDLOCAL = (
    (0, u'0 - Prestação de serviços no estabelecimento informado no grupo {localTrabGeral} do S-2200 ou S-2206, quando for o caso'),
    (1, u'1 - Prestação de serviços em apenas um local e fora do estabelecimento informado no grupo {localTrabGeral} do S-2200 ou S-2206, quando for o caso'),
    (2, u'2 - Prestação de serviços de natureza externa ou em mais de um local'),
)

CHOICES_S2260_INDRETIF = (
    (1, u'1 - arquivo original'),
    (2, u'2 - arquivo de retificação'),
)

CHOICES_S2260_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2260_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2260_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2298_INDPAGTOJUIZO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2298_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2298_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2298_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2298_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2298_TPREINT = (
    (1, u'1 - Reintegração por Decisão Judicial'),
    (2, u'2 - Reintegração por Anistia Legal'),
    (3, u'3 - Reversão de Servidor Público'),
    (4, u'4 - Recondução de Servidor Público'),
    (5, u'5 - Reinclusão de Militar'),
    (9, u'9 - Outros'),
)

CHOICES_S2299_INDCUMPRPARC = (
    (0, u'0 - Cumprimento total'),
    (1, u'1 - Cumprimento parcial em razão de obtenção de novo emprego pelo empregado'),
    (2, u'2 - Cumprimento parcial por iniciativa do empregador'),
    (3, u'3 - Outras hipóteses de cumprimento parcial do aviso prévio'),
    (4, u'4 - Aviso prévio indenizado ou não exigível'),
)

CHOICES_S2299_INDPAGTOAPI = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2299_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2299_MTVDESLIG = (
    ('01', u'01 - Rescisão com justa causa, por iniciativa do empregador'),
    ('02', u'02 - Rescisão sem justa causa, por iniciativa do empregador'),
    ('03', u'03 - Rescisão antecipada do contrato a termo por iniciativa do empregador'),
    ('04', u'04 - Rescisão antecipada do contrato a termo por iniciativa do empregado'),
    ('05', u'05 - Rescisão por culpa recíproca'),
    ('06', u'06 - Rescisão por término do contrato a termo'),
    ('07', u'07 - Rescisão do contrato de trabalho por iniciativa do empregado'),
    ('08', u'08 - Rescisão do contrato de trabalho por interesse do(a) empregado(a), nas hipóteses previstas nos arts. 394 e 483, § 1º da CLT'),
    ('09', u'09 - Rescisão por falecimento do empregador individual ou empregador doméstico por opção do empregado'),
    ('10', u'10 - Rescisão por falecimento do empregado'),
    ('11', u'11 - Transferência de empregado para empresa do mesmo grupo empresarial que tenha assumido os encargos trabalhistas, sem que tenha havido rescisão do contrato de trabalho'),
    ('12', u'12 - Transferência de empregado da empresa consorciada para o consórcio que tenha assumido os encargos trabalhistas, e vice-versa, sem que tenha havido rescisão do contrato de trabalho'),
    ('13', u'13 - Transferência de empregado de empresa ou consórcio, para outra empresa ou consórcio que tenha assumido os encargos trabalhistas por motivo de sucessão (fusão, cisão ou incorporação), sem que tenha havido rescisão do contrato de trabalho'),
    ('14', u'14 - Rescisão do contrato de trabalho por encerramento da empresa, de seus estabelecimentos ou supressão de parte de suas atividades ou falecimento do empregador individual ou empregador doméstico sem continuação da atividade'),
    ('15', u'15 - Demissão de Aprendizes por Desempenho Insuficiente ou Inadaptação'),
    ('16', u'16 - Declaração de nulidade do contrato de trabalho por infringência ao inciso II do art. 37 da Constituição Federal, quando mantido o direito ao salário'),
    ('17', u'17 - Rescisão Indireta do Contrato de Trabalho'),
    ('18', u'18 - Aposentadoria Compulsória (somente para categorias de trabalhadores 301 a 309)'),
    ('19', u'19 - Aposentadoria por idade (somente para categorias de trabalhadores 301 a 309)'),
    ('20', u'20 - Aposentadoria por idade e tempo de contribuição (somente categorias 301 a 309)'),
    ('21', u'21 - Reforma Militar (somente para categorias de trabalhadores 301 a 309)'),
    ('22', u'22 - Reserva Militar (somente para categorias de trabalhadores 301 a 309)'),
    ('23', u'23 - Exoneração (somente para categorias de trabalhadores 301 a 309)'),
    ('24', u'24 - Demissão (somente para categorias de trabalhadores 301 a 309)'),
    ('25', u'25 - Vacância para assumir outro cargo efetivo (somente para categorias de trabalhadores 301 a 309)'),
    ('26', u'26 - Rescisão do contrato de trabalho por paralisação temporária ou definitiva da empresa, estabelecimento ou parte das atividades motivada por atos de autoridade municipal, estadual ou federal'),
    ('27', u'27 - Rescisão por motivo de força maior'),
    ('28', u'28 - Término da Cessão/Requisição'),
    ('29', u'29 - Redistribuição'),
    ('30', u'30 - Mudança de Regime Trabalhista'),
    ('31', u'31 - Reversão de Reintegração'),
    ('32', u'32 - Extravio de Militar'),
    ('33', u'33 - Rescisão por acordo entre as partes (art. 484-A da CLT)'),
    ('34', u'34 - Transferência de titularidade do empregado doméstico para outro representante da mesma unidade familiar'),
)

CHOICES_S2299_PENSALIM = (
    (0, u'0 - Não existe pensão alimentícia'),
    (1, u'1 - Percentual de pensão alimentícia'),
    (2, u'2 - Valor de pensão alimentícia'),
    (3, u'3 - Percentual e valor de pensão alimentícia'),
)

CHOICES_S2299_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2299_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2299_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2300_CADINI = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_ESTCIV = (
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo'),
)

CHOICES_S2300_GRAUINSTR = (
    ('01', u'01 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou'),
    ('02', u'02 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular'),
    ('03', u'03 - 5º ano completo do Ensino Fundamental'),
    ('04', u'04 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)'),
    ('05', u'05 - Ensino Fundamental Completo'),
    ('06', u'06 - Ensino Médio incompleto'),
    ('07', u'07 - Ensino Médio completo'),
    ('08', u'08 - Educação Superior incompleta'),
    ('09', u'09 - Educação Superior completa'),
    ('10', u'10 - Pós-Graduação completa'),
    ('11', u'11 - Mestrado completo'),
    ('12', u'12 - Doutorado completo'),
)

CHOICES_S2300_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2300_NATATIVIDADE = (
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural'),
)

CHOICES_S2300_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2300_RACACOR = (
    (1, u'1 - Branca'),
    (2, u'2 - Negra'),
    (3, u'3 - Parda (parda ou declarada como mulata, cabocla, cafuza, mameluca ou mestiça de negro com pessoa de outra cor ou raça)'),
    (4, u'4 - Amarela (de origem japonesa, chinesa, coreana etc)'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado'),
)

CHOICES_S2300_SEXO = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2300_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2300_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2306_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2306_NATATIVIDADE = (
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural'),
)

CHOICES_S2306_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2306_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2306_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2399_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2399_MTVDESLIGTSV = (
    ('01', u'01 - Exoneração do Diretor Não Empregado sem justa causa, por deliberação da assembleia, dos sócios cotistas ou da autoridade competente'),
    ('02', u'02 - Término de Mandato do Diretor Não Empregado que não tenha sido reconduzido ao cargo'),
    ('03', u'03 - Exoneração a pedido de Diretor Não Empregado'),
    ('04', u'04 - Exoneração do Diretor Não Empregado por culpa recíproca ou força maior'),
    ('05', u'05 - Morte do Diretor Não Empregado'),
    ('06', u'06 - Exoneração do Diretor Não Empregado por falência, encerramento ou supressão de parte da empresa'),
    ('99', u'99 - Outros'),
)

CHOICES_S2399_PENSALIM = (
    (1, u'1 - Percentual de pensão alimentícia'),
    (2, u'2 - Valor de pensão alimentícia'),
    (3, u'3 - Percentual e valor de pensão alimentícia'),
)

CHOICES_S2399_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2399_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2399_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2400_ESTCIV = (
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo'),
)

CHOICES_S2400_INCFISMEN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2400_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_S2400_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2400_RACACOR = (
    (1, u'1 - Branca'),
    (2, u'2 - Preta'),
    (3, u'3 - Parda'),
    (4, u'4 - Amarela'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado'),
)

CHOICES_S2400_SEXO = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2400_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2400_TPINSC = (
    (1, u'1 - CNPJ'),
)

CHOICES_S2405_ESTCIV = (
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo'),
)

CHOICES_S2405_INCFISMEN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2405_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_S2405_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2405_RACACOR = (
    (1, u'1 - Branca'),
    (2, u'2 - Preta'),
    (3, u'3 - Parda'),
    (4, u'4 - Amarela'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado'),
)

CHOICES_S2405_SEXO = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2405_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2405_TPINSC = (
    (1, u'1 - CNPJ'),
)

CHOICES_S2410_CADINI = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2410_INDDECJUD = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2410_INDHOMOLOGTC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2410_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_S2410_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2410_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2410_TPINSC = (
    (1, u'1 - CNPJ'),
)

CHOICES_S2410_TPPLANRP = (
    (0, u'0 - Sem segregação da massa'),
    (1, u'1 - Fundo em capitalização'),
    (2, u'2 - Fundo em repartição'),
    (3, u'3 - Mantido pelo Tesouro'),
)

CHOICES_S2416_INDDECJUD = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2416_INDHOMOLOGTC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2416_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_S2416_INDSUSPENSAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2416_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2416_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2416_TPINSC = (
    (1, u'1 - CNPJ'),
)

CHOICES_S2416_TPPLANRP = (
    (0, u'0 - Sem segregação da massa'),
    (1, u'1 - Fundo em capitalização'),
    (2, u'2 - Fundo em repartição'),
    (3, u'3 - Mantido pelo Tesouro'),
)

CHOICES_S2420_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_S2420_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S2420_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2420_TPINSC = (
    (1, u'1 - CNPJ'),
)

CHOICES_S3000_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial'),
)

CHOICES_S3000_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S3000_TPEVENTO = (
    ('S-1000', u'S-1000 - Informações do Empregador/Contribuinte/Órgão Público'),
    ('S-1005', u'S-1005 - Tabela de Estabelecimentos, Obras de Construção Civil ou Unidades de Órgãos Públicos'),
    ('S-1010', u'S-1010 - Tabela de Rubricas'),
    ('S-1020', u'S-1020 - Tabela de Lotações Tributárias'),
    ('S-1030', u'S-1030 - Tabela de Cargos/Empregos Públicos'),
    ('S-1035', u'S-1035 - Tabela de Carreiras Públicas'),
    ('S-1040', u'S-1040 - Tabela de Funções/Cargos em Comissão'),
    ('S-1050', u'S-1050 - Tabela de Horários/Turnos de Trabalho'),
    ('S-1060', u'S-1060 - Tabela de Ambientes de Trabalho'),
    ('S-1070', u'S-1070 - Tabela de Processos Administrativos/Judiciais'),
    ('S-1080', u'S-1080 - Tabela de Operadores Portuários'),
    ('S-1200', u'S-1200 - Remuneração do Trabalhador vinculado ao Regime Geral de Previdência Social - RGPS'),
    ('S-1202', u'S-1202 - Remuneração do Trabalhador vinculado a Regime Próprio de Previdência Social - RPPS'),
    ('S-1207', u'S-1207 - Benefícios Previdenciários - RPPS'),
    ('S-1210', u'S-1210 - Pagamentos de Rendimentos do Trabalho'),
    ('S-1250', u'S-1250 - Aquisição de Produção Rural'),
    ('S-1260', u'S-1260 - Comercialização da Produção Rural Pessoa Física'),
    ('S-1270', u'S-1270 - Contratação de Trabalhadores Avulsos Não Portuários'),
    ('S-1280', u'S-1280 - Informações Complementares aos Eventos Periódicos'),
    ('S-1295', u'S-1295 - Solicitação de Totalização para Pagamento em Contingência'),
    ('S-1298', u'S-1298 - Reabertura dos Eventos Periódicos'),
    ('S-1299', u'S-1299 - Fechamento dos Eventos Periódicos'),
    ('S-1300', u'S-1300 - Contribuição Sindical Patronal'),
    ('S-2190', u'S-2190 - Admissão de Trabalhador - Registro Preliminar'),
    ('S-2200', u'S-2200 - Admissão / Ingresso de Trabalhador'),
    ('S-2205', u'S-2205 - Alteração de Dados Cadastrais do Trabalhador'),
    ('S-2206', u'S-2206 - Alteração de Contrato de Trabalho'),
    ('S-2210', u'S-2210 - Comunicação de Acidente de Trabalho'),
    ('S-2220', u'S-2220 - Monitoramento da saúde do trabalhador'),
    ('S-2230', u'S-2230 - Afastamento Temporário'),
    ('S-2240', u'S-2240 - Condições Ambientais do Trabalho - Fatores de Risco'),
    ('S-2241', u'S-2241 - Insalubridade/Periculosidade/Aposentadoria Especial'),
    ('S-2250', u'S-2250 - Aviso Prévio'),
    ('S-2260', u'S-2260 - Convocação para Trabalho Intermitente'),
    ('S-2298', u'S-2298 - Reintegração'),
    ('S-2299', u'S-2299 - Desligamento'),
    ('S-2300', u'S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início'),
    ('S-2306', u'S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual'),
    ('S-2399', u'S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término'),
    ('S-2400', u'S-2400 - Cadastro de Beneficios Previdenciários - RPPS'),
    ('S-3000', u'S-3000 - Exclusão de Eventos'),
    ('S-5001', u'S-5001 - Informações das contribuições sociais por Trabalhador'),
    ('S-5002', u'S-5002 - Imposto de Renda Retido na Fonte por Trabalhador'),
    ('S-5011', u'S-5011 - Informações das contribuições sociais consolidadas por contribuinte'),
    ('S-5012', u'S-5012 - Informações do IRRF consolidadas por Contribuinte'),
)

CHOICES_S3000_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5001_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S5001_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5002_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5003_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_S5011_CLASSTRIB = (
    ('01', u'01 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída'),
    ('02', u'02 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída'),
    ('03', u'03 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída'),
    ('04', u'04 - MEI - Micro Empreendedor Individual'),
    ('06', u'06 - Agroindústria'),
    ('07', u'07 - Produtor Rural Pessoa Jurídica'),
    ('08', u'08 - Consórcio Simplificado de Produtores Rurais'),
    ('09', u'09 - Órgão Gestor de Mão de Obra'),
    ('10', u'10 - Entidade Sindical a que se refere a Lei 12.023/2009'),
    ('11', u'11 - Associação Desportiva que mantém Clube de Futebol Profissional'),
    ('13', u'13 - Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas relacionadas no parágrafo 1º do art. 22 da Lei 8.212./91'),
    ('14', u'14 - Sindicatos em geral, exceto aquele classificado no código [10]'),
    ('21', u'21 - Pessoa Física, exceto Segurado Especial'),
    ('22', u'22 - Segurado Especial'),
    ('60', u'60 - Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('70', u'70 - Empresa de que trata o Decreto 5.436/2005'),
    ('80', u'80 - Entidade Beneficente de Assistência Social isenta de contribuições sociais'),
    ('85', u'85 - Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas'),
    ('99', u'99 - Pessoas Jurídicas em Geral'),
)

CHOICES_S5011_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S5011_INDEXISTINFO = (
    (1, u'1 - Há informações com apuração de contribuições sociais'),
    (2, u'2 - Há movimento porém sem apuração de contribuições sociais'),
    (3, u'3 - Não há movimento no período informado em {perApur}.'),
)

CHOICES_S5011_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5012_INDEXISTINFO = (
    (1, u'1 - Há informações de Imposto de Renda Retido na Fonte'),
    (2, u'2 - Há movimento, porém não há informações de Imposto de Renda Retido na Fonte'),
    (3, u'3 - Não há movimento no período informado em {perApur}.'),
)

CHOICES_S5012_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5013_INDEXISTINFO = (
    (1, u'1 - Há informações de FGTS'),
    (2, u'2 - Há movimento'),
)

CHOICES_S5013_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

ESOCIAL_VERSOES = (
    ('v02_04_02', u'Versão 2.04.02'),
    ('v02_05_00', u'Versão 2.05.00'),
)

ESTADOS = (
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
)

EVENTO_STATUS = (
    (0, u'Cadastrado'),
    (1, u'Importado'),
    (10, u'Aguardando envio'),
    (11, u'Enviado'),
    (12, u'Erro no Envio/Consulta'),
    (13, u'Processado'),
    (2, u'Duplicado'),
    (3, u'Gerado'),
    (4, u'Erro na Geração'),
    (5, u'Assinado'),
    (6, u'Erro na Assinatura'),
    (7, u'Validado'),
    (8, u'Erro na validação'),
    (9, u'Aguardando envio de precedência'),
)

OPERACOES = (
    (1, u'Incluir'),
    (2, u'Alterar'),
    (3, u'Excluir'),
)

OPERACOES_INSALPERIC_APOSENTESP = (
    (1, u'Insalubridade/Periculosidade - Incluir'),
    (2, u'Insalubridade/Periculosidade - Alterar'),
    (3, u'Insalubridade/Periculosidade - Excluir'),
    (4, u'Aposentadoria Especial - Incluir'),
    (5, u'Aposentadoria Especial - Alterar'),
    (6, u'Aposentadoria Especial - Excluir'),
)

SIM_NAO = (
    (0, u'Não'),
    (1, u'Sim'),
)

class s1000evtInfoEmpregador(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1000_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1000_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1000_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1000_evtinfoempregador_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1000_evtinfoempregador_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1000 - Informações do Empregador/Contribuinte/Órgão Público'
        db_table = r's1000_evtinfoempregador'       
        managed = True # s1000_evtinfoempregador #
        unique_together = (
            #custom_unique_together_s1000_evtinfoempregador#
            
        )
        index_together = (
            #custom_index_together_s1000_evtinfoempregador
            #index_together_s1000_evtinfoempregador
        )
        permissions = (
            ("can_view_s1000_evtinfoempregador", "Can view s1000_evtinfoempregador"),
            #custom_permissions_s1000_evtinfoempregador
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1000evtInfoEmpregadorSerializer(ModelSerializer):
    class Meta:
        model = s1000evtInfoEmpregador
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1005evtTabEstab(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1005_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1005_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1005_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1005_evttabestab_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1005_evttabestab_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos'
        db_table = r's1005_evttabestab'       
        managed = True # s1005_evttabestab #
        unique_together = (
            #custom_unique_together_s1005_evttabestab#
            
        )
        index_together = (
            #custom_index_together_s1005_evttabestab
            #index_together_s1005_evttabestab
        )
        permissions = (
            ("can_view_s1005_evttabestab", "Can view s1005_evttabestab"),
            #custom_permissions_s1005_evttabestab
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1005evtTabEstabSerializer(ModelSerializer):
    class Meta:
        model = s1005evtTabEstab
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010evtTabRubrica(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1010_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1010_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1010_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1010_evttabrubrica_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1010_evttabrubrica_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1010 - Tabela de Rubricas'
        db_table = r's1010_evttabrubrica'       
        managed = True # s1010_evttabrubrica #
        unique_together = (
            #custom_unique_together_s1010_evttabrubrica#
            
        )
        index_together = (
            #custom_index_together_s1010_evttabrubrica
            #index_together_s1010_evttabrubrica
        )
        permissions = (
            ("can_view_s1010_evttabrubrica", "Can view s1010_evttabrubrica"),
            #custom_permissions_s1010_evttabrubrica
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1010evtTabRubricaSerializer(ModelSerializer):
    class Meta:
        model = s1010evtTabRubrica
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1020evtTabLotacao(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1020_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1020_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1020_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1020_evttablotacao_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1020_evttablotacao_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1020 - Tabela de Lotações Tributárias'
        db_table = r's1020_evttablotacao'       
        managed = True # s1020_evttablotacao #
        unique_together = (
            #custom_unique_together_s1020_evttablotacao#
            
        )
        index_together = (
            #custom_index_together_s1020_evttablotacao
            #index_together_s1020_evttablotacao
        )
        permissions = (
            ("can_view_s1020_evttablotacao", "Can view s1020_evttablotacao"),
            #custom_permissions_s1020_evttablotacao
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1020evtTabLotacaoSerializer(ModelSerializer):
    class Meta:
        model = s1020evtTabLotacao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1030evtTabCargo(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1030_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1030_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1030_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1030_evttabcargo_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1030_evttabcargo_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1030 - Tabela de Cargos/Empregos Públicos'
        db_table = r's1030_evttabcargo'       
        managed = True # s1030_evttabcargo #
        unique_together = (
            #custom_unique_together_s1030_evttabcargo#
            
        )
        index_together = (
            #custom_index_together_s1030_evttabcargo
            #index_together_s1030_evttabcargo
        )
        permissions = (
            ("can_view_s1030_evttabcargo", "Can view s1030_evttabcargo"),
            #custom_permissions_s1030_evttabcargo
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1030evtTabCargoSerializer(ModelSerializer):
    class Meta:
        model = s1030evtTabCargo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1035evtTabCarreira(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1035_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1035_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1035_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1035_evttabcarreira_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1035_evttabcarreira_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1035 - Tabela de Carreiras Públicas'
        db_table = r's1035_evttabcarreira'       
        managed = True # s1035_evttabcarreira #
        unique_together = (
            #custom_unique_together_s1035_evttabcarreira#
            
        )
        index_together = (
            #custom_index_together_s1035_evttabcarreira
            #index_together_s1035_evttabcarreira
        )
        permissions = (
            ("can_view_s1035_evttabcarreira", "Can view s1035_evttabcarreira"),
            #custom_permissions_s1035_evttabcarreira
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1035evtTabCarreiraSerializer(ModelSerializer):
    class Meta:
        model = s1035evtTabCarreira
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1040evtTabFuncao(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1040_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1040_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1040_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1040_evttabfuncao_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1040_evttabfuncao_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1040 - Tabela de Funções/Cargos em Comissão'
        db_table = r's1040_evttabfuncao'       
        managed = True # s1040_evttabfuncao #
        unique_together = (
            #custom_unique_together_s1040_evttabfuncao#
            
        )
        index_together = (
            #custom_index_together_s1040_evttabfuncao
            #index_together_s1040_evttabfuncao
        )
        permissions = (
            ("can_view_s1040_evttabfuncao", "Can view s1040_evttabfuncao"),
            #custom_permissions_s1040_evttabfuncao
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1040evtTabFuncaoSerializer(ModelSerializer):
    class Meta:
        model = s1040evtTabFuncao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1050evtTabHorTur(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1050_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1050_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1050_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1050_evttabhortur_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1050_evttabhortur_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1050 - Tabela de Horários/Turnos de Trabalho'
        db_table = r's1050_evttabhortur'       
        managed = True # s1050_evttabhortur #
        unique_together = (
            #custom_unique_together_s1050_evttabhortur#
            
        )
        index_together = (
            #custom_index_together_s1050_evttabhortur
            #index_together_s1050_evttabhortur
        )
        permissions = (
            ("can_view_s1050_evttabhortur", "Can view s1050_evttabhortur"),
            #custom_permissions_s1050_evttabhortur
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1050evtTabHorTurSerializer(ModelSerializer):
    class Meta:
        model = s1050evtTabHorTur
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1060evtTabAmbiente(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1060_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1060_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1060_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1060_evttabambiente_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1060_evttabambiente_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1060 - Tabela de Ambientes de Trabalho'
        db_table = r's1060_evttabambiente'       
        managed = True # s1060_evttabambiente #
        unique_together = (
            #custom_unique_together_s1060_evttabambiente#
            
        )
        index_together = (
            #custom_index_together_s1060_evttabambiente
            #index_together_s1060_evttabambiente
        )
        permissions = (
            ("can_view_s1060_evttabambiente", "Can view s1060_evttabambiente"),
            #custom_permissions_s1060_evttabambiente
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1060evtTabAmbienteSerializer(ModelSerializer):
    class Meta:
        model = s1060evtTabAmbiente
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1070evtTabProcesso(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1070_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1070_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1070_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1070_evttabprocesso_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1070_evttabprocesso_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1070 - Tabela de Processos Administrativos/Judiciais'
        db_table = r's1070_evttabprocesso'       
        managed = True # s1070_evttabprocesso #
        unique_together = (
            #custom_unique_together_s1070_evttabprocesso#
            
        )
        index_together = (
            #custom_index_together_s1070_evttabprocesso
            #index_together_s1070_evttabprocesso
        )
        permissions = (
            ("can_view_s1070_evttabprocesso", "Can view s1070_evttabprocesso"),
            #custom_permissions_s1070_evttabprocesso
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1070evtTabProcessoSerializer(ModelSerializer):
    class Meta:
        model = s1070evtTabProcesso
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1080evtTabOperPort(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1080_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1080_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1080_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1080_evttaboperport_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1080_evttaboperport_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1080 - Tabela de Operadores Portuários'
        db_table = r's1080_evttaboperport'       
        managed = True # s1080_evttaboperport #
        unique_together = (
            #custom_unique_together_s1080_evttaboperport#
            
        )
        index_together = (
            #custom_index_together_s1080_evttaboperport
            #index_together_s1080_evttaboperport
        )
        permissions = (
            ("can_view_s1080_evttaboperport", "Can view s1080_evttaboperport"),
            #custom_permissions_s1080_evttaboperport
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1080evtTabOperPortSerializer(ModelSerializer):
    class Meta:
        model = s1080evtTabOperPort
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1200evtRemun(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1200_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1200_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1200_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1200_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab)
    #s1200_evtremun_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1200_evtremun_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social'
        db_table = r's1200_evtremun'       
        managed = True # s1200_evtremun #
        unique_together = (
            #custom_unique_together_s1200_evtremun#
            
        )
        index_together = (
            #custom_index_together_s1200_evtremun
            #index_together_s1200_evtremun
        )
        permissions = (
            ("can_view_s1200_evtremun", "Can view s1200_evtremun"),
            #custom_permissions_s1200_evtremun
        )
        ordering = ['identidade', 'indretif', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab']



class s1200evtRemunSerializer(ModelSerializer):
    class Meta:
        model = s1200evtRemun
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1202evtRmnRPPS(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1202_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1202_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1202_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1202_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1202_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    qtddepfp = models.IntegerField(blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab)
    #s1202_evtrmnrpps_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1202_evtrmnrpps_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1202 - Remuneração de servidor vinculado a Regime Próprio de Previd. Social'
        db_table = r's1202_evtrmnrpps'       
        managed = True # s1202_evtrmnrpps #
        unique_together = (
            #custom_unique_together_s1202_evtrmnrpps#
            
        )
        index_together = (
            #custom_index_together_s1202_evtrmnrpps
            #index_together_s1202_evtrmnrpps
        )
        permissions = (
            ("can_view_s1202_evtrmnrpps", "Can view s1202_evtrmnrpps"),
            #custom_permissions_s1202_evtrmnrpps
        )
        ordering = ['identidade', 'indretif', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab']



class s1202evtRmnRPPSSerializer(ModelSerializer):
    class Meta:
        model = s1202evtRmnRPPS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1207evtBenPrRP(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1207_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1207_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1207_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1207_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1207_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef)
    #s1207_evtbenprrp_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1207_evtbenprrp_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1207 - Benefícios previdenciários - RPPS'
        db_table = r's1207_evtbenprrp'       
        managed = True # s1207_evtbenprrp #
        unique_together = (
            #custom_unique_together_s1207_evtbenprrp#
            
        )
        index_together = (
            #custom_index_together_s1207_evtbenprrp
            #index_together_s1207_evtbenprrp
        )
        permissions = (
            ("can_view_s1207_evtbenprrp", "Can view s1207_evtbenprrp"),
            #custom_permissions_s1207_evtbenprrp
        )
        ordering = ['identidade', 'indretif', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef']



class s1207evtBenPrRPSerializer(ModelSerializer):
    class Meta:
        model = s1207evtBenPrRP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1210evtPgtos(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1210_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1210_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1210_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1210_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1210_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef)
    #s1210_evtpgtos_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1210_evtpgtos_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1210 - Pagamentos de Rendimentos do Trabalho'
        db_table = r's1210_evtpgtos'       
        managed = True # s1210_evtpgtos #
        unique_together = (
            #custom_unique_together_s1210_evtpgtos#
            
        )
        index_together = (
            #custom_index_together_s1210_evtpgtos
            #index_together_s1210_evtpgtos
        )
        permissions = (
            ("can_view_s1210_evtpgtos", "Can view s1210_evtpgtos"),
            #custom_permissions_s1210_evtpgtos
        )
        ordering = ['identidade', 'indretif', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef']



class s1210evtPgtosSerializer(ModelSerializer):
    class Meta:
        model = s1210evtPgtos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1250evtAqProd(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1250_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1250_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1250_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1250_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1250_TPINSC)
    nrinsc = models.CharField(max_length=15)
    tpinscadq = models.IntegerField(choices=CHOICES_S1250_TPINSCADQ)
    nrinscadq = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpinscadq) + ' - ' + unicode(self.nrinscadq)
    #s1250_evtaqprod_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1250_evtaqprod_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1250 - Aquisição de Produção Rural'
        db_table = r's1250_evtaqprod'       
        managed = True # s1250_evtaqprod #
        unique_together = (
            #custom_unique_together_s1250_evtaqprod#
            
        )
        index_together = (
            #custom_index_together_s1250_evtaqprod
            #index_together_s1250_evtaqprod
        )
        permissions = (
            ("can_view_s1250_evtaqprod", "Can view s1250_evtaqprod"),
            #custom_permissions_s1250_evtaqprod
        )
        ordering = ['identidade', 'indretif', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscadq', 'nrinscadq']



class s1250evtAqProdSerializer(ModelSerializer):
    class Meta:
        model = s1250evtAqProd
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1260evtComProd(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1260_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1260_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1260_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1260_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1260_TPINSC)
    nrinsc = models.CharField(max_length=15)
    nrinscestabrural = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.nrinscestabrural)
    #s1260_evtcomprod_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1260_evtcomprod_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1260 - Comercialização da Produção Rural Pessoa Física'
        db_table = r's1260_evtcomprod'       
        managed = True # s1260_evtcomprod #
        unique_together = (
            #custom_unique_together_s1260_evtcomprod#
            
        )
        index_together = (
            #custom_index_together_s1260_evtcomprod
            #index_together_s1260_evtcomprod
        )
        permissions = (
            ("can_view_s1260_evtcomprod", "Can view s1260_evtcomprod"),
            #custom_permissions_s1260_evtcomprod
        )
        ordering = ['identidade', 'indretif', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'nrinscestabrural']



class s1260evtComProdSerializer(ModelSerializer):
    class Meta:
        model = s1260evtComProd
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1270evtContratAvNP(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1270_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1270_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1270_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1270_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1270_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1270_evtcontratavnp_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1270_evtcontratavnp_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1270 - Contratação de Trabalhadores Avulsos Não Portuários'
        db_table = r's1270_evtcontratavnp'       
        managed = True # s1270_evtcontratavnp #
        unique_together = (
            #custom_unique_together_s1270_evtcontratavnp#
            
        )
        index_together = (
            #custom_index_together_s1270_evtcontratavnp
            #index_together_s1270_evtcontratavnp
        )
        permissions = (
            ("can_view_s1270_evtcontratavnp", "Can view s1270_evtcontratavnp"),
            #custom_permissions_s1270_evtcontratavnp
        )
        ordering = ['identidade', 'indretif', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1270evtContratAvNPSerializer(ModelSerializer):
    class Meta:
        model = s1270evtContratAvNP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1280evtInfoComplPer(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1280_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1280_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1280_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1280_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1280_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1280_evtinfocomplper_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1280_evtinfocomplper_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1280 - Informações Complementares aos Eventos Periódicos'
        db_table = r's1280_evtinfocomplper'       
        managed = True # s1280_evtinfocomplper #
        unique_together = (
            #custom_unique_together_s1280_evtinfocomplper#
            
        )
        index_together = (
            #custom_index_together_s1280_evtinfocomplper
            #index_together_s1280_evtinfocomplper
        )
        permissions = (
            ("can_view_s1280_evtinfocomplper", "Can view s1280_evtinfocomplper"),
            #custom_permissions_s1280_evtinfocomplper
        )
        ordering = ['identidade', 'indretif', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1280evtInfoComplPerSerializer(ModelSerializer):
    class Meta:
        model = s1280evtInfoComplPer
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1295evtTotConting(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1295_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1295_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1295_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1295_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1295_evttotconting_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1295_evttotconting_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1295 - Solicitação de Totalização para Pagamento em Contingência'
        db_table = r's1295_evttotconting'       
        managed = True # s1295_evttotconting #
        unique_together = (
            #custom_unique_together_s1295_evttotconting#
            
        )
        index_together = (
            #custom_index_together_s1295_evttotconting
            #index_together_s1295_evttotconting
        )
        permissions = (
            ("can_view_s1295_evttotconting", "Can view s1295_evttotconting"),
            #custom_permissions_s1295_evttotconting
        )
        ordering = ['identidade', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1295evtTotContingSerializer(ModelSerializer):
    class Meta:
        model = s1295evtTotConting
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1298evtReabreEvPer(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1298_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1298_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1298_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1298_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1298_evtreabreevper_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1298_evtreabreevper_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1298 - Reabertura dos Eventos Periódicos'
        db_table = r's1298_evtreabreevper'       
        managed = True # s1298_evtreabreevper #
        unique_together = (
            #custom_unique_together_s1298_evtreabreevper#
            
        )
        index_together = (
            #custom_index_together_s1298_evtreabreevper
            #index_together_s1298_evtreabreevper
        )
        permissions = (
            ("can_view_s1298_evtreabreevper", "Can view s1298_evtreabreevper"),
            #custom_permissions_s1298_evtreabreevper
        )
        ordering = ['identidade', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1298evtReabreEvPerSerializer(ModelSerializer):
    class Meta:
        model = s1298evtReabreEvPer
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1299evtFechaEvPer(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1299_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1299_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1299_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1299_TPINSC)
    nrinsc = models.CharField(max_length=15)
    evtremun = models.CharField(choices=CHOICES_S1299_EVTREMUN, max_length=1)
    evtpgtos = models.CharField(choices=CHOICES_S1299_EVTPGTOS, max_length=1)
    evtaqprod = models.CharField(choices=CHOICES_S1299_EVTAQPROD, max_length=1)
    evtcomprod = models.CharField(choices=CHOICES_S1299_EVTCOMPROD, max_length=1)
    evtcontratavnp = models.CharField(choices=CHOICES_S1299_EVTCONTRATAVNP, max_length=1)
    evtinfocomplper = models.CharField(choices=CHOICES_S1299_EVTINFOCOMPLPER, max_length=1)
    compsemmovto = models.CharField(max_length=7, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.evtremun) + ' - ' + unicode(self.evtpgtos) + ' - ' + unicode(self.evtaqprod) + ' - ' + unicode(self.evtcomprod) + ' - ' + unicode(self.evtcontratavnp) + ' - ' + unicode(self.evtinfocomplper)
    #s1299_evtfechaevper_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1299_evtfechaevper_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1299 - Fechamento dos Eventos Periódicos'
        db_table = r's1299_evtfechaevper'       
        managed = True # s1299_evtfechaevper #
        unique_together = (
            #custom_unique_together_s1299_evtfechaevper#
            
        )
        index_together = (
            #custom_index_together_s1299_evtfechaevper
            #index_together_s1299_evtfechaevper
        )
        permissions = (
            ("can_view_s1299_evtfechaevper", "Can view s1299_evtfechaevper"),
            #custom_permissions_s1299_evtfechaevper
        )
        ordering = ['identidade', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'evtremun', 'evtpgtos', 'evtaqprod', 'evtcomprod', 'evtcontratavnp', 'evtinfocomplper']



class s1299evtFechaEvPerSerializer(ModelSerializer):
    class Meta:
        model = s1299evtFechaEvPer
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1300evtContrSindPatr(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1300_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1300_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1300_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S1300_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S1300_TPINSC)
    nrinsc = models.CharField(max_length=15)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1300_evtcontrsindpatr_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s1300_evtcontrsindpatr_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-1300 - Contribuição Sindical Patronal'
        db_table = r's1300_evtcontrsindpatr'       
        managed = True # s1300_evtcontrsindpatr #
        unique_together = (
            #custom_unique_together_s1300_evtcontrsindpatr#
            
        )
        index_together = (
            #custom_index_together_s1300_evtcontrsindpatr
            #index_together_s1300_evtcontrsindpatr
        )
        permissions = (
            ("can_view_s1300_evtcontrsindpatr", "Can view s1300_evtcontrsindpatr"),
            #custom_permissions_s1300_evtcontrsindpatr
        )
        ordering = ['identidade', 'indretif', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']



class s1300evtContrSindPatrSerializer(ModelSerializer):
    class Meta:
        model = s1300evtContrSindPatr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2190evtAdmPrelim(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2190_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2190_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2190_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    dtnascto = models.DateField()
    dtadm = models.DateField()
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.dtadm)
    #s2190_evtadmprelim_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2190_evtadmprelim_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2190 - Admissão de Trabalhador - Registro Preliminar'
        db_table = r's2190_evtadmprelim'       
        managed = True # s2190_evtadmprelim #
        unique_together = (
            #custom_unique_together_s2190_evtadmprelim#
            
        )
        index_together = (
            #custom_index_together_s2190_evtadmprelim
            #index_together_s2190_evtadmprelim
        )
        permissions = (
            ("can_view_s2190_evtadmprelim", "Can view s2190_evtadmprelim"),
            #custom_permissions_s2190_evtadmprelim
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'dtnascto', 'dtadm']



class s2190evtAdmPrelimSerializer(ModelSerializer):
    class Meta:
        model = s2190evtAdmPrelim
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2200evtAdmissao(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2200_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2200_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2200_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    nmtrab = models.CharField(max_length=70)
    sexo = models.CharField(choices=CHOICES_S2200_SEXO, max_length=1)
    racacor = models.IntegerField(choices=CHOICES_S2200_RACACOR)
    estciv = models.IntegerField(choices=CHOICES_S2200_ESTCIV, blank=True, null=True)
    grauinstr = models.CharField(choices=CHOICES_S2200_GRAUINSTR, max_length=2)
    indpriempr = models.CharField(choices=CHOICES_S2200_INDPRIEMPR, max_length=1, blank=True, null=True)
    nmsoc = models.CharField(max_length=70, blank=True, null=True)
    dtnascto = models.DateField()
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    paisnascto = models.TextField(max_length=3)
    paisnac = models.TextField(max_length=3)
    nmmae = models.CharField(max_length=70, blank=True, null=True)
    nmpai = models.CharField(max_length=70, blank=True, null=True)
    matricula = models.CharField(max_length=30)
    tpregtrab = models.IntegerField(choices=CHOICES_S2200_TPREGTRAB)
    tpregprev = models.IntegerField(choices=CHOICES_S2200_TPREGPREV)
    nrrecinfprelim = models.CharField(max_length=40, blank=True, null=True)
    cadini = models.CharField(choices=CHOICES_S2200_CADINI, max_length=1)
    codcargo = models.CharField(max_length=30, blank=True, null=True)
    dtingrcargo = models.DateField(blank=True, null=True)
    codfuncao = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3)
    codcarreira = models.CharField(max_length=30, blank=True, null=True)
    dtingrcarr = models.DateField(blank=True, null=True)
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    undsalfixo = models.IntegerField(choices=CHOICES_S2200_UNDSALFIXO)
    dscsalvar = models.CharField(max_length=255, blank=True, null=True)
    tpcontr = models.IntegerField(choices=CHOICES_S2200_TPCONTR)
    dtterm = models.DateField(blank=True, null=True)
    clauassec = models.CharField(choices=CHOICES_S2200_CLAUASSEC, max_length=1, blank=True, null=True)
    objdet = models.CharField(max_length=255, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.nmtrab) + ' - ' + unicode(self.sexo) + ' - ' + unicode(self.racacor) + ' - ' + unicode(self.grauinstr) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.paisnascto) + ' - ' + unicode(self.paisnac) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.tpregtrab) + ' - ' + unicode(self.tpregprev) + ' - ' + unicode(self.cadini) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vrsalfx) + ' - ' + unicode(self.undsalfixo) + ' - ' + unicode(self.tpcontr)
    #s2200_evtadmissao_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2200_evtadmissao_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador'
        db_table = r's2200_evtadmissao'       
        managed = True # s2200_evtadmissao #
        unique_together = (
            #custom_unique_together_s2200_evtadmissao#
            
        )
        index_together = (
            #custom_index_together_s2200_evtadmissao
            #index_together_s2200_evtadmissao
        )
        permissions = (
            ("can_view_s2200_evtadmissao", "Can view s2200_evtadmissao"),
            #custom_permissions_s2200_evtadmissao
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'nmtrab', 'sexo', 'racacor', 'grauinstr', 'dtnascto', 'paisnascto', 'paisnac', 'matricula', 'tpregtrab', 'tpregprev', 'cadini', 'codcateg', 'vrsalfx', 'undsalfixo', 'tpcontr']



class s2200evtAdmissaoSerializer(ModelSerializer):
    class Meta:
        model = s2200evtAdmissao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205evtAltCadastral(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2205_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2205_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2205_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2205_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    dtalteracao = models.DateField()
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    nmtrab = models.CharField(max_length=70)
    sexo = models.CharField(choices=CHOICES_S2205_SEXO, max_length=1)
    racacor = models.IntegerField(choices=CHOICES_S2205_RACACOR)
    estciv = models.IntegerField(choices=CHOICES_S2205_ESTCIV, blank=True, null=True)
    grauinstr = models.CharField(choices=CHOICES_S2205_GRAUINSTR, max_length=2)
    nmsoc = models.CharField(max_length=70, blank=True, null=True)
    dtnascto = models.DateField()
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    paisnascto = models.TextField(max_length=3)
    paisnac = models.TextField(max_length=3)
    nmmae = models.CharField(max_length=70, blank=True, null=True)
    nmpai = models.CharField(max_length=70, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.dtalteracao) + ' - ' + unicode(self.nmtrab) + ' - ' + unicode(self.sexo) + ' - ' + unicode(self.racacor) + ' - ' + unicode(self.grauinstr) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.paisnascto) + ' - ' + unicode(self.paisnac)
    #s2205_evtaltcadastral_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2205_evtaltcadastral_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2205 - Alteração de Dados Cadastrais do Trabalhador'
        db_table = r's2205_evtaltcadastral'       
        managed = True # s2205_evtaltcadastral #
        unique_together = (
            #custom_unique_together_s2205_evtaltcadastral#
            
        )
        index_together = (
            #custom_index_together_s2205_evtaltcadastral
            #index_together_s2205_evtaltcadastral
        )
        permissions = (
            ("can_view_s2205_evtaltcadastral", "Can view s2205_evtaltcadastral"),
            #custom_permissions_s2205_evtaltcadastral
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'dtalteracao', 'nmtrab', 'sexo', 'racacor', 'grauinstr', 'dtnascto', 'paisnascto', 'paisnac']



class s2205evtAltCadastralSerializer(ModelSerializer):
    class Meta:
        model = s2205evtAltCadastral
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206evtAltContratual(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2206_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2206_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2206_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2206_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    dtalteracao = models.DateField()
    dtef = models.DateField(blank=True, null=True)
    dscalt = models.CharField(max_length=150, blank=True, null=True)
    tpregprev = models.IntegerField(choices=CHOICES_S2206_TPREGPREV)
    codcargo = models.CharField(max_length=30, blank=True, null=True)
    codfuncao = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3)
    codcarreira = models.CharField(max_length=30, blank=True, null=True)
    dtingrcarr = models.DateField(blank=True, null=True)
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    undsalfixo = models.IntegerField(choices=CHOICES_S2206_UNDSALFIXO)
    dscsalvar = models.CharField(max_length=255, blank=True, null=True)
    tpcontr = models.IntegerField(choices=CHOICES_S2206_TPCONTR)
    dtterm = models.DateField(blank=True, null=True)
    objdet = models.CharField(max_length=255, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.dtalteracao) + ' - ' + unicode(self.tpregprev) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vrsalfx) + ' - ' + unicode(self.undsalfixo) + ' - ' + unicode(self.tpcontr)
    #s2206_evtaltcontratual_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2206_evtaltcontratual_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2206 - Alteração de Contrato de Trabalho'
        db_table = r's2206_evtaltcontratual'       
        managed = True # s2206_evtaltcontratual #
        unique_together = (
            #custom_unique_together_s2206_evtaltcontratual#
            
        )
        index_together = (
            #custom_index_together_s2206_evtaltcontratual
            #index_together_s2206_evtaltcontratual
        )
        permissions = (
            ("can_view_s2206_evtaltcontratual", "Can view s2206_evtaltcontratual"),
            #custom_permissions_s2206_evtaltcontratual
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'dtalteracao', 'tpregprev', 'codcateg', 'vrsalfx', 'undsalfixo', 'tpcontr']



class s2206evtAltContratualSerializer(ModelSerializer):
    class Meta:
        model = s2206evtAltContratual
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2210evtCAT(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2210_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2210_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2210_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2210_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3, blank=True, null=True)
    dtacid = models.DateField()
    tpacid = models.CharField(choices=CHOICES_S2210_TPACID, max_length=6)
    hracid = models.CharField(max_length=4, blank=True, null=True)
    hrstrabantesacid = models.CharField(max_length=4)
    tpcat = models.IntegerField(choices=CHOICES_S2210_TPCAT)
    indcatobito = models.CharField(choices=CHOICES_S2210_INDCATOBITO, max_length=1)
    dtobito = models.DateField(blank=True, null=True)
    indcomunpolicia = models.CharField(choices=CHOICES_S2210_INDCOMUNPOLICIA, max_length=1)
    codsitgeradora = models.IntegerField(choices=CHOICES_S2210_CODSITGERADORA)
    iniciatcat = models.IntegerField(choices=CHOICES_S2210_INICIATCAT)
    obscat = models.CharField(max_length=999, blank=True, null=True)
    observacao = models.CharField(max_length=999, blank=True, null=True)
    tplocal = models.IntegerField(choices=CHOICES_S2210_TPLOCAL)
    dsclocal = models.CharField(max_length=255, blank=True, null=True)
    codamb = models.CharField(max_length=30, blank=True, null=True)
    tplograd = models.TextField(max_length=4)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    pais = models.TextField(max_length=3, blank=True, null=True)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.dtacid) + ' - ' + unicode(self.tpacid) + ' - ' + unicode(self.hrstrabantesacid) + ' - ' + unicode(self.tpcat) + ' - ' + unicode(self.indcatobito) + ' - ' + unicode(self.indcomunpolicia) + ' - ' + unicode(self.codsitgeradora) + ' - ' + unicode(self.iniciatcat) + ' - ' + unicode(self.tplocal) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd)
    #s2210_evtcat_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2210_evtcat_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2210 - Comunicação de Acidente de Trabalho'
        db_table = r's2210_evtcat'       
        managed = True # s2210_evtcat #
        unique_together = (
            #custom_unique_together_s2210_evtcat#
            
        )
        index_together = (
            #custom_index_together_s2210_evtcat
            #index_together_s2210_evtcat
        )
        permissions = (
            ("can_view_s2210_evtcat", "Can view s2210_evtcat"),
            #custom_permissions_s2210_evtcat
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'dtacid', 'tpacid', 'hrstrabantesacid', 'tpcat', 'indcatobito', 'indcomunpolicia', 'codsitgeradora', 'iniciatcat', 'tplocal', 'tplograd', 'dsclograd', 'nrlograd']



class s2210evtCATSerializer(ModelSerializer):
    class Meta:
        model = s2210evtCAT
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2220evtMonit(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2220_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2220_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2220_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2220_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3, blank=True, null=True)
    tpexameocup = models.IntegerField(choices=CHOICES_S2220_TPEXAMEOCUP)
    dtaso = models.DateField()
    tpaso = models.IntegerField(choices=CHOICES_S2220_TPASO)
    resaso = models.IntegerField(choices=CHOICES_S2220_RESASO)
    cpfmed = models.CharField(max_length=11, blank=True, null=True)
    nismed = models.CharField(max_length=11, blank=True, null=True)
    nmmed = models.CharField(max_length=70)
    nrcrm = models.CharField(max_length=8)
    ufcrm = models.CharField(choices=ESTADOS, max_length=2)
    nisresp = models.CharField(max_length=11)
    nrconsclasse = models.CharField(max_length=8)
    ufconsclasse = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    cpfresp = models.CharField(max_length=11, blank=True, null=True)
    nmresp = models.CharField(max_length=70)
    nrcrm = models.CharField(max_length=8)
    ufcrm = models.CharField(choices=ESTADOS, max_length=2)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.tpexameocup) + ' - ' + unicode(self.dtaso) + ' - ' + unicode(self.tpaso) + ' - ' + unicode(self.resaso) + ' - ' + unicode(self.nmmed) + ' - ' + unicode(self.nrcrm) + ' - ' + unicode(self.ufcrm) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nrconsclasse) + ' - ' + unicode(self.nmresp) + ' - ' + unicode(self.nrcrm) + ' - ' + unicode(self.ufcrm)
    #s2220_evtmonit_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2220_evtmonit_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2220 - Monitoramento da Saúde do Trabalhador'
        db_table = r's2220_evtmonit'       
        managed = True # s2220_evtmonit #
        unique_together = (
            #custom_unique_together_s2220_evtmonit#
            
        )
        index_together = (
            #custom_index_together_s2220_evtmonit
            #index_together_s2220_evtmonit
        )
        permissions = (
            ("can_view_s2220_evtmonit", "Can view s2220_evtmonit"),
            #custom_permissions_s2220_evtmonit
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'tpexameocup', 'dtaso', 'tpaso', 'resaso', 'nmmed', 'nrcrm', 'ufcrm', 'nisresp', 'nrconsclasse', 'nmresp', 'nrcrm', 'ufcrm']



class s2220evtMonitSerializer(ModelSerializer):
    class Meta:
        model = s2220evtMonit
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2221evtToxic(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2221_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2221_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2221_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2221_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3, blank=True, null=True)
    dtexame = models.DateField()
    cnpjlab = models.CharField(max_length=14, blank=True, null=True)
    codseqexame = models.CharField(max_length=11, blank=True, null=True)
    nmmed = models.CharField(max_length=70, blank=True, null=True)
    nrcrm = models.CharField(max_length=8, blank=True, null=True)
    ufcrm = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    indrecusa = models.CharField(max_length=1)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.dtexame) + ' - ' + unicode(self.indrecusa)
    #s2221_evttoxic_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2221_evttoxic_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2221 - Exame Toxicológico do Motorista Profissional'
        db_table = r's2221_evttoxic'       
        managed = True # s2221_evttoxic #
        unique_together = (
            #custom_unique_together_s2221_evttoxic#
            
        )
        index_together = (
            #custom_index_together_s2221_evttoxic
            #index_together_s2221_evttoxic
        )
        permissions = (
            ("can_view_s2221_evttoxic", "Can view s2221_evttoxic"),
            #custom_permissions_s2221_evttoxic
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'dtexame', 'indrecusa']



class s2221evtToxicSerializer(ModelSerializer):
    class Meta:
        model = s2221evtToxic
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2230evtAfastTemp(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2230_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2230_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2230_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2230_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab)
    #s2230_evtafasttemp_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2230_evtafasttemp_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2230 - Afastamento Temporário'
        db_table = r's2230_evtafasttemp'       
        managed = True # s2230_evtafasttemp #
        unique_together = (
            #custom_unique_together_s2230_evtafasttemp#
            
        )
        index_together = (
            #custom_index_together_s2230_evtafasttemp
            #index_together_s2230_evtafasttemp
        )
        permissions = (
            ("can_view_s2230_evtafasttemp", "Can view s2230_evtafasttemp"),
            #custom_permissions_s2230_evtafasttemp
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab']



class s2230evtAfastTempSerializer(ModelSerializer):
    class Meta:
        model = s2230evtAfastTemp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2231evtCessao(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2231_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2231_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2231_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField()
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula)
    #s2231_evtcessao_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2231_evtcessao_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2231 - Cessão/Exercício em Outro Órgão'
        db_table = r's2231_evtcessao'       
        managed = True # s2231_evtcessao #
        unique_together = (
            #custom_unique_together_s2231_evtcessao#
            
        )
        index_together = (
            #custom_index_together_s2231_evtcessao
            #index_together_s2231_evtcessao
        )
        permissions = (
            ("can_view_s2231_evtcessao", "Can view s2231_evtcessao"),
            #custom_permissions_s2231_evtcessao
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula']



class s2231evtCessaoSerializer(ModelSerializer):
    class Meta:
        model = s2231evtCessao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240evtExpRisco(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2240_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2240_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2240_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2240_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3, blank=True, null=True)
    dtinicondicao = models.DateField()
    dscativdes = models.CharField(max_length=999)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.dtinicondicao) + ' - ' + unicode(self.dscativdes)
    #s2240_evtexprisco_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2240_evtexprisco_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2240 - Condições Ambientais do Trabalho - Fatores de Risco'
        db_table = r's2240_evtexprisco'       
        managed = True # s2240_evtexprisco #
        unique_together = (
            #custom_unique_together_s2240_evtexprisco#
            
        )
        index_together = (
            #custom_index_together_s2240_evtexprisco
            #index_together_s2240_evtexprisco
        )
        permissions = (
            ("can_view_s2240_evtexprisco", "Can view s2240_evtexprisco"),
            #custom_permissions_s2240_evtexprisco
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'dtinicondicao', 'dscativdes']



class s2240evtExpRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2240evtExpRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241evtInsApo(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2241_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2241_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2241_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2241_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES_INSALPERIC_APOSENTESP)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab)
    #s2241_evtinsapo_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2241_evtinsapo_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2241 - Insalubridade, Periculosidade e Aposentadoria Especial'
        db_table = r's2241_evtinsapo'       
        managed = True # s2241_evtinsapo #
        unique_together = (
            #custom_unique_together_s2241_evtinsapo#
            
        )
        index_together = (
            #custom_index_together_s2241_evtinsapo
            #index_together_s2241_evtinsapo
        )
        permissions = (
            ("can_view_s2241_evtinsapo", "Can view s2241_evtinsapo"),
            #custom_permissions_s2241_evtinsapo
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab']



class s2241evtInsApoSerializer(ModelSerializer):
    class Meta:
        model = s2241evtInsApo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2245evtTreiCap(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2245_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2245_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2245_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2245_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3, blank=True, null=True)
    codtreicap = models.CharField(max_length=4)
    obstreicap = models.CharField(max_length=999, blank=True, null=True)
    observacao = models.CharField(max_length=999, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES_INSALPERIC_APOSENTESP)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.codtreicap)
    #s2245_evttreicap_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2245_evttreicap_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2245 - Treinamentos, Capacitações e Exercícios Simulados'
        db_table = r's2245_evttreicap'       
        managed = True # s2245_evttreicap #
        unique_together = (
            #custom_unique_together_s2245_evttreicap#
            
        )
        index_together = (
            #custom_index_together_s2245_evttreicap
            #index_together_s2245_evttreicap
        )
        permissions = (
            ("can_view_s2245_evttreicap", "Can view s2245_evttreicap"),
            #custom_permissions_s2245_evttreicap
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'codtreicap']



class s2245evtTreiCapSerializer(ModelSerializer):
    class Meta:
        model = s2245evtTreiCap
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2250evtAvPrevio(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2250_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2250_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2250_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2250_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula)
    #s2250_evtavprevio_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2250_evtavprevio_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2250 - Aviso Prévio'
        db_table = r's2250_evtavprevio'       
        managed = True # s2250_evtavprevio #
        unique_together = (
            #custom_unique_together_s2250_evtavprevio#
            
        )
        index_together = (
            #custom_index_together_s2250_evtavprevio
            #index_together_s2250_evtavprevio
        )
        permissions = (
            ("can_view_s2250_evtavprevio", "Can view s2250_evtavprevio"),
            #custom_permissions_s2250_evtavprevio
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula']



class s2250evtAvPrevioSerializer(ModelSerializer):
    class Meta:
        model = s2250evtAvPrevio
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2260evtConvInterm(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2260_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2260_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2260_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2260_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    codconv = models.CharField(max_length=30)
    dtinicio = models.DateField()
    dtfim = models.DateField()
    dtprevpgto = models.DateField()
    codhorcontrat = models.CharField(max_length=30, blank=True, null=True)
    dscjornada = models.CharField(max_length=999, blank=True, null=True)
    indlocal = models.IntegerField(choices=CHOICES_S2260_INDLOCAL)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.codconv) + ' - ' + unicode(self.dtinicio) + ' - ' + unicode(self.dtfim) + ' - ' + unicode(self.dtprevpgto) + ' - ' + unicode(self.indlocal)
    #s2260_evtconvinterm_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2260_evtconvinterm_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2260 - Convocação para Trabalho Intermitente'
        db_table = r's2260_evtconvinterm'       
        managed = True # s2260_evtconvinterm #
        unique_together = (
            #custom_unique_together_s2260_evtconvinterm#
            
        )
        index_together = (
            #custom_index_together_s2260_evtconvinterm
            #index_together_s2260_evtconvinterm
        )
        permissions = (
            ("can_view_s2260_evtconvinterm", "Can view s2260_evtconvinterm"),
            #custom_permissions_s2260_evtconvinterm
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'codconv', 'dtinicio', 'dtfim', 'dtprevpgto', 'indlocal']



class s2260evtConvIntermSerializer(ModelSerializer):
    class Meta:
        model = s2260evtConvInterm
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2298evtReintegr(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2298_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2298_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2298_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2298_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    tpreint = models.IntegerField(choices=CHOICES_S2298_TPREINT)
    nrprocjud = models.CharField(max_length=20, blank=True, null=True)
    nrleianistia = models.CharField(max_length=13, blank=True, null=True)
    dtefetretorno = models.DateField()
    dtefeito = models.DateField()
    indpagtojuizo = models.CharField(choices=CHOICES_S2298_INDPAGTOJUIZO, max_length=1)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.tpreint) + ' - ' + unicode(self.dtefetretorno) + ' - ' + unicode(self.dtefeito) + ' - ' + unicode(self.indpagtojuizo)
    #s2298_evtreintegr_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2298_evtreintegr_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2298 - Reintegração'
        db_table = r's2298_evtreintegr'       
        managed = True # s2298_evtreintegr #
        unique_together = (
            #custom_unique_together_s2298_evtreintegr#
            
        )
        index_together = (
            #custom_index_together_s2298_evtreintegr
            #index_together_s2298_evtreintegr
        )
        permissions = (
            ("can_view_s2298_evtreintegr", "Can view s2298_evtreintegr"),
            #custom_permissions_s2298_evtreintegr
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'tpreint', 'dtefetretorno', 'dtefeito', 'indpagtojuizo']



class s2298evtReintegrSerializer(ModelSerializer):
    class Meta:
        model = s2298evtReintegr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299evtDeslig(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2299_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2299_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2299_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2299_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    mtvdeslig = models.CharField(choices=CHOICES_S2299_MTVDESLIG, max_length=2)
    dtdeslig = models.DateField()
    indpagtoapi = models.CharField(choices=CHOICES_S2299_INDPAGTOAPI, max_length=1)
    dtprojfimapi = models.DateField(blank=True, null=True)
    pensalim = models.IntegerField(choices=CHOICES_S2299_PENSALIM)
    percaliment = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vralim = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    nrcertobito = models.CharField(max_length=32, blank=True, null=True)
    nrproctrab = models.CharField(max_length=20, blank=True, null=True)
    indcumprparc = models.IntegerField(choices=CHOICES_S2299_INDCUMPRPARC)
    qtddiasinterm = models.IntegerField(blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.mtvdeslig) + ' - ' + unicode(self.dtdeslig) + ' - ' + unicode(self.indpagtoapi) + ' - ' + unicode(self.pensalim) + ' - ' + unicode(self.indcumprparc)
    #s2299_evtdeslig_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2299_evtdeslig_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2299 - Desligamento'
        db_table = r's2299_evtdeslig'       
        managed = True # s2299_evtdeslig #
        unique_together = (
            #custom_unique_together_s2299_evtdeslig#
            
        )
        index_together = (
            #custom_index_together_s2299_evtdeslig
            #index_together_s2299_evtdeslig
        )
        permissions = (
            ("can_view_s2299_evtdeslig", "Can view s2299_evtdeslig"),
            #custom_permissions_s2299_evtdeslig
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'mtvdeslig', 'dtdeslig', 'indpagtoapi', 'pensalim', 'indcumprparc']



class s2299evtDesligSerializer(ModelSerializer):
    class Meta:
        model = s2299evtDeslig
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2300evtTSVInicio(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2300_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2300_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2300_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2300_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    nmtrab = models.CharField(max_length=70)
    sexo = models.CharField(choices=CHOICES_S2300_SEXO, max_length=1)
    racacor = models.IntegerField(choices=CHOICES_S2300_RACACOR)
    estciv = models.IntegerField(choices=CHOICES_S2300_ESTCIV, blank=True, null=True)
    grauinstr = models.CharField(choices=CHOICES_S2300_GRAUINSTR, max_length=2)
    nmsoc = models.CharField(max_length=70, blank=True, null=True)
    dtnascto = models.DateField()
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    paisnascto = models.TextField(max_length=3)
    paisnac = models.TextField(max_length=3)
    nmmae = models.CharField(max_length=70, blank=True, null=True)
    nmpai = models.CharField(max_length=70, blank=True, null=True)
    cadini = models.CharField(choices=CHOICES_S2300_CADINI, max_length=1)
    codcateg = models.TextField(max_length=3)
    dtinicio = models.DateField()
    natatividade = models.IntegerField(choices=CHOICES_S2300_NATATIVIDADE, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nmtrab) + ' - ' + unicode(self.sexo) + ' - ' + unicode(self.racacor) + ' - ' + unicode(self.grauinstr) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.paisnascto) + ' - ' + unicode(self.paisnac) + ' - ' + unicode(self.cadini) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.dtinicio)
    #s2300_evttsvinicio_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2300_evttsvinicio_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início'
        db_table = r's2300_evttsvinicio'       
        managed = True # s2300_evttsvinicio #
        unique_together = (
            #custom_unique_together_s2300_evttsvinicio#
            
        )
        index_together = (
            #custom_index_together_s2300_evttsvinicio
            #index_together_s2300_evttsvinicio
        )
        permissions = (
            ("can_view_s2300_evttsvinicio", "Can view s2300_evttsvinicio"),
            #custom_permissions_s2300_evttsvinicio
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nmtrab', 'sexo', 'racacor', 'grauinstr', 'dtnascto', 'paisnascto', 'paisnac', 'cadini', 'codcateg', 'dtinicio']



class s2300evtTSVInicioSerializer(ModelSerializer):
    class Meta:
        model = s2300evtTSVInicio
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2306evtTSVAltContr(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2306_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2306_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2306_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2306_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    codcateg = models.TextField(max_length=3)
    dtalteracao = models.DateField()
    natatividade = models.IntegerField(choices=CHOICES_S2306_NATATIVIDADE, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.dtalteracao)
    #s2306_evttsvaltcontr_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2306_evttsvaltcontr_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual'
        db_table = r's2306_evttsvaltcontr'       
        managed = True # s2306_evttsvaltcontr #
        unique_together = (
            #custom_unique_together_s2306_evttsvaltcontr#
            
        )
        index_together = (
            #custom_index_together_s2306_evttsvaltcontr
            #index_together_s2306_evttsvaltcontr
        )
        permissions = (
            ("can_view_s2306_evttsvaltcontr", "Can view s2306_evttsvaltcontr"),
            #custom_permissions_s2306_evttsvaltcontr
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'codcateg', 'dtalteracao']



class s2306evtTSVAltContrSerializer(ModelSerializer):
    class Meta:
        model = s2306evtTSVAltContr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399evtTSVTermino(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2399_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2399_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2399_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2399_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    codcateg = models.TextField(max_length=3)
    dtterm = models.DateField()
    mtvdesligtsv = models.CharField(choices=CHOICES_S2399_MTVDESLIGTSV, max_length=2, blank=True, null=True)
    pensalim = models.IntegerField(choices=CHOICES_S2399_PENSALIM, blank=True, null=True)
    percaliment = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vralim = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.dtterm)
    #s2399_evttsvtermino_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2399_evttsvtermino_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término'
        db_table = r's2399_evttsvtermino'       
        managed = True # s2399_evttsvtermino #
        unique_together = (
            #custom_unique_together_s2399_evttsvtermino#
            
        )
        index_together = (
            #custom_index_together_s2399_evttsvtermino
            #index_together_s2399_evttsvtermino
        )
        permissions = (
            ("can_view_s2399_evttsvtermino", "Can view s2399_evttsvtermino"),
            #custom_permissions_s2399_evttsvtermino
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'codcateg', 'dtterm']



class s2399evtTSVTerminoSerializer(ModelSerializer):
    class Meta:
        model = s2399evtTSVTermino
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2400evtCdBenefIn(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2400_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2400_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2400_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2400_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    nisbenef = models.CharField(max_length=11, blank=True, null=True)
    nmbenefic = models.CharField(max_length=70)
    dtinicio = models.DateField()
    sexo = models.CharField(choices=CHOICES_S2400_SEXO, max_length=1)
    racacor = models.IntegerField(choices=CHOICES_S2400_RACACOR)
    estciv = models.IntegerField(choices=CHOICES_S2400_ESTCIV, blank=True, null=True)
    incfismen = models.CharField(choices=CHOICES_S2400_INCFISMEN, max_length=1)
    dtincfismen = models.DateField(max_length=1, blank=True, null=True)
    dtnascto = models.DateField()
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    paisnascto = models.TextField(max_length=3, blank=True, null=True)
    paisnac = models.TextField(max_length=3)
    nmmae = models.CharField(max_length=70, blank=True, null=True)
    nmpai = models.CharField(max_length=70, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.nmbenefic) + ' - ' + unicode(self.dtinicio) + ' - ' + unicode(self.sexo) + ' - ' + unicode(self.racacor) + ' - ' + unicode(self.incfismen) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.paisnac)
    #s2400_evtcdbenefin_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2400_evtcdbenefin_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2400 - Cadastro de Beneficiários - Entes Públicos - Início'
        db_table = r's2400_evtcdbenefin'       
        managed = True # s2400_evtcdbenefin #
        unique_together = (
            #custom_unique_together_s2400_evtcdbenefin#
            
        )
        index_together = (
            #custom_index_together_s2400_evtcdbenefin
            #index_together_s2400_evtcdbenefin
        )
        permissions = (
            ("can_view_s2400_evtcdbenefin", "Can view s2400_evtcdbenefin"),
            #custom_permissions_s2400_evtcdbenefin
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef', 'nmbenefic', 'dtinicio', 'sexo', 'racacor', 'incfismen', 'dtnascto', 'paisnac']



class s2400evtCdBenefInSerializer(ModelSerializer):
    class Meta:
        model = s2400evtCdBenefIn
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2405evtCdBenefAlt(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2405_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2405_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2405_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2405_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    dtalteracao = models.DateField()
    nisbenef = models.CharField(max_length=11, blank=True, null=True)
    nmbenefic = models.CharField(max_length=70)
    sexo = models.CharField(choices=CHOICES_S2405_SEXO, max_length=1)
    racacor = models.IntegerField(choices=CHOICES_S2405_RACACOR)
    estciv = models.IntegerField(choices=CHOICES_S2405_ESTCIV, blank=True, null=True)
    incfismen = models.CharField(choices=CHOICES_S2405_INCFISMEN, max_length=1)
    dtincfismen = models.DateField(max_length=1, blank=True, null=True)
    paisnac = models.TextField(max_length=3)
    nmmae = models.CharField(max_length=70, blank=True, null=True)
    nmpai = models.CharField(max_length=70, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.dtalteracao) + ' - ' + unicode(self.nmbenefic) + ' - ' + unicode(self.sexo) + ' - ' + unicode(self.racacor) + ' - ' + unicode(self.incfismen) + ' - ' + unicode(self.paisnac)
    #s2405_evtcdbenefalt_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2405_evtcdbenefalt_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2405 - Cadastro de Beneficiários - Entes Públicos - Alteração'
        db_table = r's2405_evtcdbenefalt'       
        managed = True # s2405_evtcdbenefalt #
        unique_together = (
            #custom_unique_together_s2405_evtcdbenefalt#
            
        )
        index_together = (
            #custom_index_together_s2405_evtcdbenefalt
            #index_together_s2405_evtcdbenefalt
        )
        permissions = (
            ("can_view_s2405_evtcdbenefalt", "Can view s2405_evtcdbenefalt"),
            #custom_permissions_s2405_evtcdbenefalt
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef', 'dtalteracao', 'nmbenefic', 'sexo', 'racacor', 'incfismen', 'paisnac']



class s2405evtCdBenefAltSerializer(ModelSerializer):
    class Meta:
        model = s2405evtCdBenefAlt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2410evtCdBenIn(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2410_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2410_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2410_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2410_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    cnpjorigem = models.CharField(max_length=14, blank=True, null=True)
    cadini = models.CharField(choices=CHOICES_S2410_CADINI, max_length=1)
    nrbeneficio = models.CharField(max_length=20)
    dtinibeneficio = models.DateField()
    tpbeneficio = models.CharField(max_length=4)
    vrbeneficio = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    tpplanrp = models.IntegerField(choices=CHOICES_S2410_TPPLANRP)
    dsc = models.CharField(max_length=255, blank=True, null=True)
    inddecjud = models.CharField(choices=CHOICES_S2410_INDDECJUD, max_length=1)
    indhomologtc = models.CharField(choices=CHOICES_S2410_INDHOMOLOGTC, max_length=1)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.cadini) + ' - ' + unicode(self.nrbeneficio) + ' - ' + unicode(self.dtinibeneficio) + ' - ' + unicode(self.tpbeneficio) + ' - ' + unicode(self.vrbeneficio) + ' - ' + unicode(self.tpplanrp) + ' - ' + unicode(self.inddecjud) + ' - ' + unicode(self.indhomologtc)
    #s2410_evtcdbenin_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2410_evtcdbenin_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2410 - Cadastro de Benefícios - Entes Públicos - Início'
        db_table = r's2410_evtcdbenin'       
        managed = True # s2410_evtcdbenin #
        unique_together = (
            #custom_unique_together_s2410_evtcdbenin#
            
        )
        index_together = (
            #custom_index_together_s2410_evtcdbenin
            #index_together_s2410_evtcdbenin
        )
        permissions = (
            ("can_view_s2410_evtcdbenin", "Can view s2410_evtcdbenin"),
            #custom_permissions_s2410_evtcdbenin
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef', 'cadini', 'nrbeneficio', 'dtinibeneficio', 'tpbeneficio', 'vrbeneficio', 'tpplanrp', 'inddecjud', 'indhomologtc']



class s2410evtCdBenInSerializer(ModelSerializer):
    class Meta:
        model = s2410evtCdBenIn
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2416evtCdBenAlt(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2416_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2416_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2416_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2416_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    nrbeneficio = models.CharField(max_length=20)
    dtaltbeneficio = models.DateField()
    tpbeneficio = models.CharField(max_length=4)
    tpplanrp = models.IntegerField(choices=CHOICES_S2416_TPPLANRP)
    dsc = models.CharField(max_length=255, blank=True, null=True)
    inddecjud = models.CharField(choices=CHOICES_S2416_INDDECJUD, max_length=1)
    indhomologtc = models.CharField(choices=CHOICES_S2416_INDHOMOLOGTC, max_length=1)
    indsuspensao = models.CharField(choices=CHOICES_S2416_INDSUSPENSAO, max_length=1)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.nrbeneficio) + ' - ' + unicode(self.dtaltbeneficio) + ' - ' + unicode(self.tpbeneficio) + ' - ' + unicode(self.tpplanrp) + ' - ' + unicode(self.inddecjud) + ' - ' + unicode(self.indhomologtc) + ' - ' + unicode(self.indsuspensao)
    #s2416_evtcdbenalt_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2416_evtcdbenalt_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2416 - Cadastro de Benefícios - Entes Públicos - Alteração'
        db_table = r's2416_evtcdbenalt'       
        managed = True # s2416_evtcdbenalt #
        unique_together = (
            #custom_unique_together_s2416_evtcdbenalt#
            
        )
        index_together = (
            #custom_index_together_s2416_evtcdbenalt
            #index_together_s2416_evtcdbenalt
        )
        permissions = (
            ("can_view_s2416_evtcdbenalt", "Can view s2416_evtcdbenalt"),
            #custom_permissions_s2416_evtcdbenalt
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef', 'nrbeneficio', 'dtaltbeneficio', 'tpbeneficio', 'tpplanrp', 'inddecjud', 'indhomologtc', 'indsuspensao']



class s2416evtCdBenAltSerializer(ModelSerializer):
    class Meta:
        model = s2416evtCdBenAlt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2420evtCdBenTerm(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2420_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2420_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S2420_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S2420_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    nrbeneficio = models.CharField(max_length=20)
    dttermbeneficio = models.DateField()
    mtvtermino = models.CharField(max_length=2)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    operacao = models.IntegerField(choices=OPERACOES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.nrbeneficio) + ' - ' + unicode(self.dttermbeneficio) + ' - ' + unicode(self.mtvtermino)
    #s2420_evtcdbenterm_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s2420_evtcdbenterm_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-2420 - Cadastro de Benefícios - Entes Públicos - Término'
        db_table = r's2420_evtcdbenterm'       
        managed = True # s2420_evtcdbenterm #
        unique_together = (
            #custom_unique_together_s2420_evtcdbenterm#
            
        )
        index_together = (
            #custom_index_together_s2420_evtcdbenterm
            #index_together_s2420_evtcdbenterm
        )
        permissions = (
            ("can_view_s2420_evtcdbenterm", "Can view s2420_evtcdbenterm"),
            #custom_permissions_s2420_evtcdbenterm
        )
        ordering = ['identidade', 'indretif', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef', 'nrbeneficio', 'dttermbeneficio', 'mtvtermino']



class s2420evtCdBenTermSerializer(ModelSerializer):
    class Meta:
        model = s2420evtCdBenTerm
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s3000evtExclusao(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S3000_TPAMB, blank=True)
    procemi = models.IntegerField(choices=CHOICES_S3000_PROCEMI, blank=True)
    verproc = models.CharField(max_length=20, blank=True, default='1.2')
    tpinsc = models.IntegerField(choices=CHOICES_S3000_TPINSC)
    nrinsc = models.CharField(max_length=15)
    tpevento = models.CharField(choices=CHOICES_S3000_TPEVENTO, max_length=6)
    nrrecevt = models.CharField(max_length=40)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpevento) + ' - ' + unicode(self.nrrecevt)
    #s3000_evtexclusao_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s3000_evtexclusao_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-3000 - Exclusão de eventos'
        db_table = r's3000_evtexclusao'       
        managed = True # s3000_evtexclusao #
        unique_together = (
            #custom_unique_together_s3000_evtexclusao#
            
        )
        index_together = (
            #custom_index_together_s3000_evtexclusao
            #index_together_s3000_evtexclusao
        )
        permissions = (
            ("can_view_s3000_evtexclusao", "Can view s3000_evtexclusao"),
            #custom_permissions_s3000_evtexclusao
        )
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpevento', 'nrrecevt']



class s3000evtExclusaoSerializer(ModelSerializer):
    class Meta:
        model = s3000evtExclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s5001evtBasesTrab(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    nrrecarqbase = models.CharField(max_length=40)
    indapuracao = models.IntegerField(choices=CHOICES_S5001_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5001_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab)
    #s5001_evtbasestrab_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s5001_evtbasestrab_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-5001 - Informações das contribuições sociais por trabalhador'
        db_table = r's5001_evtbasestrab'       
        managed = True # s5001_evtbasestrab #
        unique_together = (
            #custom_unique_together_s5001_evtbasestrab#
            
        )
        index_together = (
            #custom_index_together_s5001_evtbasestrab
            #index_together_s5001_evtbasestrab
        )
        permissions = (
            ("can_view_s5001_evtbasestrab", "Can view s5001_evtbasestrab"),
            #custom_permissions_s5001_evtbasestrab
        )
        ordering = ['identidade', 'nrrecarqbase', 'indapuracao', 'perapur', 'tpinsc', 'nrinsc', 'cpftrab']



class s5001evtBasesTrabSerializer(ModelSerializer):
    class Meta:
        model = s5001evtBasesTrab
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s5002evtIrrfBenef(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    nrrecarqbase = models.CharField(max_length=40)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5002_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab)
    #s5002_evtirrfbenef_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s5002_evtirrfbenef_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-5002 - Imposto de Renda Retido na Fonte'
        db_table = r's5002_evtirrfbenef'       
        managed = True # s5002_evtirrfbenef #
        unique_together = (
            #custom_unique_together_s5002_evtirrfbenef#
            
        )
        index_together = (
            #custom_index_together_s5002_evtirrfbenef
            #index_together_s5002_evtirrfbenef
        )
        permissions = (
            ("can_view_s5002_evtirrfbenef", "Can view s5002_evtirrfbenef"),
            #custom_permissions_s5002_evtirrfbenef
        )
        ordering = ['identidade', 'nrrecarqbase', 'perapur', 'tpinsc', 'nrinsc', 'cpftrab']



class s5002evtIrrfBenefSerializer(ModelSerializer):
    class Meta:
        model = s5002evtIrrfBenef
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s5003evtBasesFGTS(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    nrrecarqbase = models.CharField(max_length=40)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5003_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab)
    #s5003_evtbasesfgts_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s5003_evtbasesfgts_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-5003 - Informações do FGTS por Trabalhador'
        db_table = r's5003_evtbasesfgts'       
        managed = True # s5003_evtbasesfgts #
        unique_together = (
            #custom_unique_together_s5003_evtbasesfgts#
            
        )
        index_together = (
            #custom_index_together_s5003_evtbasesfgts
            #index_together_s5003_evtbasesfgts
        )
        permissions = (
            ("can_view_s5003_evtbasesfgts", "Can view s5003_evtbasesfgts"),
            #custom_permissions_s5003_evtbasesfgts
        )
        ordering = ['identidade', 'nrrecarqbase', 'perapur', 'tpinsc', 'nrinsc', 'cpftrab']



class s5003evtBasesFGTSSerializer(ModelSerializer):
    class Meta:
        model = s5003evtBasesFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s5011evtCS(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S5011_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5011_TPINSC)
    nrinsc = models.CharField(max_length=15)
    nrrecarqbase = models.CharField(max_length=40)
    indexistinfo = models.IntegerField(choices=CHOICES_S5011_INDEXISTINFO)
    classtrib = models.CharField(choices=CHOICES_S5011_CLASSTRIB, max_length=2)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.indexistinfo) + ' - ' + unicode(self.classtrib)
    #s5011_evtcs_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s5011_evtcs_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-5011 - Informações das contribuições sociais consolidadas por contribuinte'
        db_table = r's5011_evtcs'       
        managed = True # s5011_evtcs #
        unique_together = (
            #custom_unique_together_s5011_evtcs#
            
        )
        index_together = (
            #custom_index_together_s5011_evtcs
            #index_together_s5011_evtcs
        )
        permissions = (
            ("can_view_s5011_evtcs", "Can view s5011_evtcs"),
            #custom_permissions_s5011_evtcs
        )
        ordering = ['identidade', 'indapuracao', 'perapur', 'tpinsc', 'nrinsc', 'nrrecarqbase', 'indexistinfo', 'classtrib']



class s5011evtCSSerializer(ModelSerializer):
    class Meta:
        model = s5011evtCS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s5012evtIrrf(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5012_TPINSC)
    nrinsc = models.CharField(max_length=15)
    nrrecarqbase = models.CharField(max_length=40)
    indexistinfo = models.IntegerField(choices=CHOICES_S5012_INDEXISTINFO)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.indexistinfo)
    #s5012_evtirrf_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s5012_evtirrf_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-5012 - Informações do IRRF consolidadas por contribuinte'
        db_table = r's5012_evtirrf'       
        managed = True # s5012_evtirrf #
        unique_together = (
            #custom_unique_together_s5012_evtirrf#
            
        )
        index_together = (
            #custom_index_together_s5012_evtirrf
            #index_together_s5012_evtirrf
        )
        permissions = (
            ("can_view_s5012_evtirrf", "Can view s5012_evtirrf"),
            #custom_permissions_s5012_evtirrf
        )
        ordering = ['identidade', 'perapur', 'tpinsc', 'nrinsc', 'nrrecarqbase', 'indexistinfo']



class s5012evtIrrfSerializer(ModelSerializer):
    class Meta:
        model = s5012evtIrrf
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s5013evtFGTS(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5013_TPINSC)
    nrinsc = models.CharField(max_length=15)
    nrrecarqbase = models.CharField(max_length=40)
    indexistinfo = models.IntegerField(choices=CHOICES_S5013_INDEXISTINFO)
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00')
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.indexistinfo)
    #s5013_evtfgts_custom#
    
    def evento(self): 
        return self.__dict__

    def validar(self):
        from emensageriapro.esocial.views.s5013_evtfgts_verificar import validar_evento_funcao
        validar_evento_funcao(self.id, 'default')

    
    class Meta:
        # verbose_name = u'S-5013 - Informações do FGTS consolidadas por contribuinte'
        db_table = r's5013_evtfgts'       
        managed = True # s5013_evtfgts #
        unique_together = (
            #custom_unique_together_s5013_evtfgts#
            
        )
        index_together = (
            #custom_index_together_s5013_evtfgts
            #index_together_s5013_evtfgts
        )
        permissions = (
            ("can_view_s5013_evtfgts", "Can view s5013_evtfgts"),
            #custom_permissions_s5013_evtfgts
        )
        ordering = ['identidade', 'perapur', 'tpinsc', 'nrinsc', 'nrrecarqbase', 'indexistinfo']



class s5013evtFGTSSerializer(ModelSerializer):
    class Meta:
        model = s5013evtFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
