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



CHOICES_R1000_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R1000_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R1000_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]


CHOICES_R1070_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R1070_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R1070_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]


CHOICES_R2010_INDCPRB = [
    (0, u'0 - Não é contribuinte da Contribuição Previdenciária sobre a Receita Bruta (CPRB) - Retenção 11%'),
    (1, u'1 - Contribuinte da Contribuição Previdenciária sobre a Receita Bruta (CPRB) - Retenção 3,5%.'),
]


CHOICES_R2010_INDOBRA = [
    (0, u'0 - Não é obra de construção civil ou não está sujeita a matrícula de obra'),
    (1, u'1 - Obra de Construção Civil - Empreitada Total'),
    (2, u'2 - Obra de Construção Civil - Empreitada Parcial.'),
]


CHOICES_R2010_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_R2010_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R2010_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R2010_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]


CHOICES_R2010_TPINSCESTAB = [
    (1, u'1 - CNPJ'),
    (4, u'4 - CNO'),
]


CHOICES_R2020_INDOBRA = [
    (0, u'0 - Não é obra de construção civil ou não está sujeita a matrícula de obra'),
    (1, u'1 - Obra de Construção Civil - Empreitada Total'),
    (2, u'2 - Obra de Construção Civil - Empreitada Parcial.'),
]


CHOICES_R2020_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_R2020_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R2020_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R2020_TPINSC = [
    (1, u'1 - CNPJ'),
]


CHOICES_R2020_TPINSCTOMADOR = [
    (1, u'1 - CNPJ'),
    (4, u'4 - CNO'),
]


CHOICES_R2030_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_R2030_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R2030_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R2030_TPINSC = [
    (1, u'1 - CNPJ'),
]


CHOICES_R2040_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_R2040_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R2040_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R2040_TPINSC = [
    (1, u'1 - CNPJ'),
]


CHOICES_R2040_TPINSCESTAB = [
    (1, u'1 - CNPJ'),
]


CHOICES_R2050_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_R2050_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R2050_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R2050_TPINSC = [
    (1, u'1 - CNPJ'),
]


CHOICES_R2050_TPINSCESTAB = [
    (1, u'1 - CNPJ'),
]


CHOICES_R2060_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_R2060_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R2060_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R2060_TPINSC = [
    (1, u'1 - CNPJ'),
]


CHOICES_R2070_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_R2070_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R2070_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R2070_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]


CHOICES_R2070_TPINSCBENEF = [
    (1, u'1 - Pessoa Jurídica'),
    (2, u'2 - Pessoa Física.'),
]


CHOICES_R2098_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R2098_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R2098_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]


CHOICES_R2099_EVTASSDESPREC = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_R2099_EVTASSDESPREP = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_R2099_EVTCOMPROD = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_R2099_EVTCPRB = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_R2099_EVTPGTOS = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_R2099_EVTSERVPR = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_R2099_EVTSERVTM = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_R2099_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R2099_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R2099_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]


CHOICES_R3010_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_R3010_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R3010_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R3010_TPINSC = [
    (1, u'1 - CNPJ'),
]


CHOICES_R3010_TPINSCESTAB = [
    (1, u'1 - CNPJ.'),
]


CHOICES_R5001_CDRETORNO = [
    ('0', u'0 - Sucesso 1 - Erro 2 - Em processamento'),
]


CHOICES_R5001_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]


CHOICES_R5011_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]


CHOICES_R9000_PROCEMI = [
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental.'),
]


CHOICES_R9000_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_R9000_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
]


EFDREINF_VERSOES = [
    ('v1_03_02', u'Versão 1.03.02'),
    ('v1_04_00', u'Versão 1.04.00'),
    ('v2_00_00', u'Versão 2.00.00'),
]


EVENTO_STATUS = [
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
]


OPERACOES = [
    (1, u'Incluir'),
    (2, u'Alterar'),
    (3, u'Excluir'),
]


SIM_NAO = [
    (0, u'Não'),
    (1, u'Sim'),
]

