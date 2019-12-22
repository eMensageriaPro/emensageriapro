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



CHOICES_ESOCIALBENEFICIOSPREVIDENCIARIOSCESSACAOMOTIVOS = [
    ('1', u'1 - Óbito'),
    ('2', u'2 - Reversão'),
    ('3', u'3 - Por decisão judicial'),
    ('4', u'4 - Cassação'),
    ('5', u'5 - Término do prazo do benefício'),
    ('6', u'6 - Extinção de Quota'),
    ('7', u'7 - Não homologado pelo Tribunal de Contas'),
    ('8', u'8 - Renúncia Expressa'),
]


CHOICES_ESOCIALCLASSIFICACOESTRIBUTARIAS = [
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
    ('22', u'22 - Segurado Especial, inclusive quando for empregador doméstico'),
    ('60', u'60 - Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('70', u'70 - Empresa de que trata o Decreto 5.436/2005'),
    ('80', u'80 - Entidade Beneficente de Assistência Social isenta de contribuições sociais'),
    ('85', u'85 - Administração Direta da União, Estados, Distrito Federal e Municípíos, Autarquias e Fundações Públicas'),
    ('99', u'99 - Pessoas Jurídicas em Geral'),
]


CHOICES_ESOCIALINSCRICOESTIPOS = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (5, u'5 - CGC'),
    (6, u'6 - CEI'),
]


CHOICES_S1000_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1000_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1005_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1005_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1010_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1010_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1020_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1020_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1030_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1030_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1035_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1035_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1040_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1040_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1050_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1050_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1060_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1060_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1070_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1070_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1080_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1080_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1200_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário).'),
]


CHOICES_S1200_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S1200_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1200_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1202_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário).'),
]


CHOICES_S1202_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S1202_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1202_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1207_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário).'),
]


CHOICES_S1207_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S1207_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1207_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1210_INDAPURACAO = [
    (1, u'1 - Mensal.'),
]


CHOICES_S1210_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S1210_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1210_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1250_INDAPURACAO = [
    (1, u'1 - Mensal.'),
]


CHOICES_S1250_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S1250_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1250_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1260_INDAPURACAO = [
    (1, u'1 - Mensal.'),
]


CHOICES_S1260_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S1260_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1260_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1270_INDAPURACAO = [
    (1, u'1 - Mensal.'),
]


CHOICES_S1270_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S1270_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1270_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1280_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário).'),
]


CHOICES_S1280_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S1280_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1280_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1295_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário).'),
]


CHOICES_S1295_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1295_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1298_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário).'),
]


CHOICES_S1298_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1298_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1299_EVTAQPROD = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S1299_EVTCOMPROD = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S1299_EVTCONTRATAVNP = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S1299_EVTINFOCOMPLPER = [
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
]


CHOICES_S1299_EVTPGTOS = [
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
]


CHOICES_S1299_EVTREMUN = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S1299_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário).'),
]


CHOICES_S1299_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1299_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S1300_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual.'),
]


CHOICES_S1300_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S1300_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S1300_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2190_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2190_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2200_CADINI = [
    ('N', u'N - Não (Admissão).'),
    ('S', u'S - Sim (Cadastramento Inicial)'),
]


CHOICES_S2200_CLAUASSEC = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2200_ESTCIV = [
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo.'),
]


CHOICES_S2200_GRAUINSTR = [
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
    ('12', u'12 - Doutorado completo.'),
]


CHOICES_S2200_INDPRIEMPR = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2200_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2200_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2200_RACACOR = [
    (1, u'1 - Branca'),
    (2, u'2 - Preta'),
    (3, u'3 - Parda'),
    (4, u'4 - Amarela'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado.'),
]


CHOICES_S2200_SEXO = [
    ('F', u'F - Feminino.'),
    ('M', u'M - Masculino'),
]


CHOICES_S2200_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2200_TPCONTR = [
    (1, u'1 - Prazo indeterminado'),
    (2, u'2 - Prazo determinado, definido em dias'),
    (3, u'3 - Prazo determinado, vinculado à ocorrência de um fato.'),
]


CHOICES_S2200_TPREGPREV = [
    (1, u'1 - Regime Geral da Previdência Social - RGPS'),
    (2, u'2 - Regime Próprio de Previdência Social - RPPS'),
    (3, u'3 - Regime de Previdência Social no Exterior.'),
]


CHOICES_S2200_TPREGTRAB = [
    (1, u'1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas'),
    (2, u'2 - Estatutário.'),
]


CHOICES_S2200_UNDSALFIXO = [
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável.'),
]


CHOICES_S2205_ESTCIV = [
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo.'),
]


CHOICES_S2205_GRAUINSTR = [
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
    ('12', u'12 - Doutorado completo.'),
]


CHOICES_S2205_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2205_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2205_RACACOR = [
    (1, u'1 - Branca'),
    (2, u'2 - Preta'),
    (3, u'3 - Parda'),
    (4, u'4 - Amarela'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado.'),
]


CHOICES_S2205_SEXO = [
    ('F', u'F - Feminino.'),
    ('M', u'M - Masculino'),
]


CHOICES_S2205_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2206_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2206_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2206_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2206_TPCONTR = [
    (1, u'1 - Prazo indeterminado'),
    (2, u'2 - Prazo determinado, definido em dias'),
    (3, u'3 - Prazo determinado, vinculado à ocorrência de um fato.'),
]


CHOICES_S2206_TPREGPREV = [
    (1, u'1 - Regime Geral da Previdência Social - RGPS'),
    (2, u'2 - Regime Próprio de Previdência Social - RPPS'),
    (3, u'3 - Regime de Previdência Social no Exterior.'),
]


CHOICES_S2206_UNDSALFIXO = [
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável.'),
]


CHOICES_S2210_INDCATOBITO = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2210_INDCOMUNPOLICIA = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2210_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2210_INICIATCAT = [
    (1, u'1 - Iniciativa do empregador'),
    (2, u'2 - Ordem judicial'),
    (3, u'3 - Determinação de órgão fiscalizador.'),
]


CHOICES_S2210_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2210_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2210_TPCAT = [
    (1, u'1 - Inicial'),
    (2, u'2 - Reabertura'),
    (3, u'3 - Comunicação de Óbito.'),
]


CHOICES_S2210_TPLOCAL = [
    (1, u'1 - Estabelecimento do empregador no Brasil'),
    (2, u'2 - Estabelecimento do empregador no Exterior'),
    (3, u'3 - Estabelecimento de terceiros onde o empregador presta serviços'),
    (4, u'4 - Via pública'),
    (5, u'5 - Área rural'),
    (6, u'6 - Embarcação'),
    (9, u'9 - Outros.'),
]


CHOICES_S2220_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2220_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2220_RESASO = [
    (1, u'1 - Apto'),
    (2, u'2 - Inapto.'),
]


CHOICES_S2220_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2220_TPASO = [
    (0, u'0 - Admissional'),
    (1, u'1 - Periódico, conforme planejamento do PCMSO'),
    (2, u'2 - De retorno ao trabalho'),
    (3, u'3 - De mudança de função'),
    (4, u'4 - De monitoração pontual, não enquadrado nos casos anteriores'),
    (8, u'8 - Demissional.'),
]


CHOICES_S2220_TPEXAMEOCUP = [
    (0, u'0 - Exame médico admissional'),
    (1, u'1 - Exame médico periódico, conforme NR7 do MTb e/ou planejamento do PCMSO'),
    (2, u'2 - Exame médico de retorno ao trabalho'),
    (3, u'3 - Exame médico de mudança de função'),
    (4, u'4 - Exame médico de monitoração pontual, não enquadrado nos demais casos'),
    (9, u'9 - Exame médico demissional.'),
]


CHOICES_S2221_INDRECUSA = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2221_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2221_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2221_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2230_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2230_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2230_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2231_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2231_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2231_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2240_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2240_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2240_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2241_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2241_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual(MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2241_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2245_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2245_INDTREINANT = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2245_MODTREICAP = [
    (1, u'1 - Presencial'),
    (2, u'2 - Educação a Distância (EaD)'),
    (3, u'3 - Semipresencial.'),
]


CHOICES_S2245_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2245_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2245_TPTREICAP = [
    (1, u'1 - Inicial'),
    (2, u'2 - Periódico'),
    (3, u'3 - Reciclagem'),
    (4, u'4 - Eventual'),
    (5, u'5 - Outros.'),
]


CHOICES_S2250_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2250_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2250_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2260_INDLOCAL = [
    (0, u'0 - Prestação de serviços no estabelecimento informado no grupo {localTrabGeral} do S-2200 ou S-2206, quando for o caso'),
    (1, u'1 - Prestação de serviços em apenas um local e fora do estabelecimento informado no grupo {localTrabGeral} do S-2200 ou S-2206, quando for o caso'),
    (2, u'2 - Prestação de serviços de natureza externa ou em mais de um local.'),
]


CHOICES_S2260_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2260_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2260_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2298_INDPAGTOJUIZO = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2298_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2298_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2298_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2298_TPREINT = [
    (1, u'1 - Reintegração por Decisão Judicial'),
    (2, u'2 - Reintegração por Anistia Legal'),
    (3, u'3 - Reversão de Servidor Público'),
    (4, u'4 - Recondução de Servidor Público'),
    (5, u'5 - Reinclusão de Militar'),
    (9, u'9 - Outros.'),
]


CHOICES_S2299_INDCUMPRPARC = [
    (0, u'0 - Cumprimento total'),
    (1, u'1 - Cumprimento parcial em razão de obtenção de novo emprego pelo empregado'),
    (2, u'2 - Cumprimento parcial por iniciativa do empregador'),
    (3, u'3 - Outras hipóteses de cumprimento parcial do aviso prévio'),
    (4, u'4 - Aviso prévio indenizado ou não exigível. O preenchimento deste campo é facultativo.'),
]


CHOICES_S2299_INDPAGTOAPI = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2299_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2299_PENSALIM = [
    (0, u'0 - Não existe pensão alimentícia'),
    (1, u'1 - Percentual de pensão alimentícia'),
    (2, u'2 - Valor de pensão alimentícia'),
    (3, u'3 - Percentual e valor de pensão alimentícia.'),
]


CHOICES_S2299_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2299_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2300_CADINI = [
    ('N', u'N - Não (Início de TSVE).'),
    ('S', u'S - Sim (Cadastramento Inicial)'),
]


CHOICES_S2300_ESTCIV = [
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo.'),
]


CHOICES_S2300_GRAUINSTR = [
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
    ('12', u'12 - Doutorado completo.'),
]


CHOICES_S2300_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2300_NATATIVIDADE = [
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural.'),
]


CHOICES_S2300_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2300_RACACOR = [
    (1, u'1 - Branca'),
    (2, u'2 - Preta'),
    (3, u'3 - Parda'),
    (4, u'4 - Amarela'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado.'),
]


CHOICES_S2300_SEXO = [
    ('F', u'F - Feminino.'),
    ('M', u'M - Masculino'),
]


CHOICES_S2300_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2306_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2306_NATATIVIDADE = [
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural.'),
]


CHOICES_S2306_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2306_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2399_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2399_MTVDESLIGTSV = [
    ('01', u'01 - Exoneração do Diretor Não Empregado sem justa causa, por deliberação da assembleia, dos sócios cotistas ou da autoridade competente'),
    ('02', u'02 - Término de Mandato do Diretor Não Empregado que não tenha sido reconduzido ao cargo'),
    ('03', u'03 - Exoneração a pedido de Diretor Não Empregado'),
    ('04', u'04 - Exoneração do Diretor Não Empregado por culpa recíproca ou força maior'),
    ('05', u'05 - Morte do Diretor Não Empregado'),
    ('06', u'06 - Exoneração do Diretor Não Empregado por falência, encerramento ou supressão de parte da empresa'),
    ('07', u'07 - Mudança de CPF'),
    ('99', u'99 - Outros.'),
]


CHOICES_S2399_PENSALIM = [
    (0, u'0 - Não existe pensão alimentícia'),
    (1, u'1 - Percentual de pensão alimentícia'),
    (2, u'2 - Valor de pensão alimentícia'),
    (3, u'3 - Percentual e valor de pensão alimentícia.'),
]


CHOICES_S2399_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2399_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2400_ESTCIV = [
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo.'),
]


CHOICES_S2400_INCFISMEN = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2400_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2400_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2400_RACACOR = [
    (1, u'1 - Branca'),
    (2, u'2 - Preta'),
    (3, u'3 - Parda'),
    (4, u'4 - Amarela'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado.'),
]


CHOICES_S2400_SEXO = [
    ('F', u'F - Feminino.'),
    ('M', u'M - Masculino'),
]


CHOICES_S2400_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2405_ESTCIV = [
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo.'),
]


CHOICES_S2405_INCFISMEN = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2405_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2405_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2405_RACACOR = [
    (1, u'1 - Branca'),
    (2, u'2 - Preta'),
    (3, u'3 - Parda'),
    (4, u'4 - Amarela'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado.'),
]


CHOICES_S2405_SEXO = [
    ('F', u'F - Feminino.'),
    ('M', u'M - Masculino'),
]


CHOICES_S2405_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2410_CADINI = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2410_INDDECJUD = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2410_INDHOMOLOGTC = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2410_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2410_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2410_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2410_TPPLANRP = [
    (0, u'0 - Sem segregação da massa'),
    (1, u'1 - Fundo em capitalização'),
    (2, u'2 - Fundo em repartição'),
    (3, u'3 - Mantido pelo Tesouro.'),
]


CHOICES_S2416_INDDECJUD = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2416_INDHOMOLOGTC = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2416_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2416_INDSUSPENSAO = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S2416_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2416_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S2416_TPPLANRP = [
    (0, u'0 - Sem segregação da massa'),
    (1, u'1 - Fundo em capitalização'),
    (2, u'2 - Fundo em repartição'),
    (3, u'3 - Mantido pelo Tesouro.'),
]


CHOICES_S2420_INDRETIF = [
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de Retificação.'),
]


CHOICES_S2420_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Microempreendedor Individual (MEI)'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S2420_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S3000_PROCEMI = [
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental - Empregador Doméstico'),
    (3, u'3 - Aplicativo governamental - Web Geral'),
    (4, u'4 - Aplicativo governamental - Simplificado Pessoa Jurídica'),
    (5, u'5 - Aplicativo governamental - Segurado Especial.'),
]


CHOICES_S3000_TPAMB = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita.'),
]


CHOICES_S5001_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário).'),
]


CHOICES_S5011_INDAPURACAO = [
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário). Evento de origem: S-1295 ou S-1299.'),
]


CHOICES_S5011_INDEXISTINFO = [
    (1, u'1 - Há informações com apuração de contribuições sociais: 2 - Há movimento porém sem apuração de contribuições sociais'),
    (3, u'3 - Não há movimento no período informado em {perApur}.'),
]


CHOICES_S5012_INDEXISTINFO = [
    (1, u'1 - Há informações de Imposto de Renda Retido na Fonte'),
    (2, u'2 - Há movimento, porém não há informações de Imposto de Renda Retido na Fonte'),
    (3, u'3 - Não há movimento no período informado em {perApur}.'),
]


CHOICES_S5013_INDEXISTINFO = [
    (1, u'1 - Há informações de FGTS'),
    (2, u'2 - Há movimento, porém não há informações de FGTS'),
    (3, u'3 - Não há movimento no período informado em {perApur}.'),
]


ESOCIAL_VERSOES = [
    ('v02_04_02', u'Versão 2.04.02'),
    ('v02_05_00', u'Versão 2.05.00'),
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

