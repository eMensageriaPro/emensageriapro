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



CHOICES_S1010_ALTERACAO_CODINCCP = (
    ('00', u'00 - Não é base de cálculo'),
    ('01', u'01 - Não é base de cálculo em função de acordos internacionais de previdência social'),
    ('11', u'11 - Base de cálculo das contribuições sociais - Salário de Contribuição: Mensal'),
    ('12', u'12 - Base de cálculo das contribuições sociais - Salário de Contribuição: 13o Salário'),
    ('13', u'13 - Base de cálculo das contribuições sociais - Salário de Contribuição: Exclusiva do Empregador - mensal'),
    ('14', u'14 - Base de cálculo das contribuições sociais - Salário de Contribuição: Exclusiva do Empregador - 13° salário'),
    ('15', u'15 - Base de cálculo das contribuições sociais - Salário de Contribuição: Exclusiva do segurado - mensal'),
    ('16', u'16 - Base de cálculo das contribuições sociais - Salário de Contribuição: Exclusiva do segurado - 13° salário'),
    ('21', u'21 - Base de cálculo das contribuições sociais - Salário de Contribuição: Salário maternidade mensal pago pelo Empregador'),
    ('22', u'22 - Base de cálculo das contribuições sociais - Salário de Contribuição: Salário maternidade - 13o Salário, pago pelo Empregador'),
    ('23', u'23 - Base de cálculo das contribuições sociais - Salário de Contribuição: Auxilio doença mensal - Regime Próprio de Previdência Social'),
    ('24', u'24 - Base de cálculo das contribuições sociais - Salário de Contribuição: Auxilio doença 13o salário doença - Regime próprio de previdência social'),
    ('25', u'25 - Base de cálculo das contribuições sociais - Salário de Contribuição: Salário maternidade mensal pago pelo INSS'),
    ('26', u'26 - Base de cálculo das contribuições sociais - Salário de Contribuição: Salário maternidade - 13° salário, pago pelo INSS'),
    ('31', u'31 - Contribuição descontada do Segurado sobre salário de contribuição: Mensal'),
    ('32', u'32 - Contribuição descontada do Segurado sobre salário de contribuição: 13o Salário'),
    ('34', u'34 - Contribuição descontada do Segurado sobre salário de contribuição: SEST'),
    ('35', u'35 - Contribuição descontada do Segurado sobre salário de contribuição: SENAT'),
    ('51', u'51 - Outros: Salário-família'),
    ('61', u'61 - Outros: Complemento de salário-mínimo - Regime próprio de previdência social'),
    ('91', u'91 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Mensal'),
    ('92', u'92 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: 13o Salário'),
    ('93', u'93 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Salário maternidade'),
    ('94', u'94 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Salário maternidade 13o salário'),
    ('95', u'95 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Exclusiva do Empregador - mensal'),
    ('96', u'96 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Exclusiva do Empregador - 13º salário'),
    ('97', u'97 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Exclusiva do Empregador - Salário maternidade'),
    ('98', u'98 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Exclusiva do Empregador - Salário maternidade 13º salário'),
)

CHOICES_S1010_ALTERACAO_CODINCCPRP = (
    ('00', u'00 - Não compõe a apuração de contribuições devidas ao RPPS/regime militar: Sem incidência para RPPS/regime militar'),
    ('01', u'01 - Não compõe a apuração de contribuições devidas ao RPPS/regime militar: Sem incidência em função de acordos internacionais de previdência social'),
    ('10', u'10 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Do segurado de RPPS/militar e a cargo do ente público - mensal'),
    ('11', u'11 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Do segurado de RPPS/militar e a cargo do ente público - 13º salário'),
    ('12', u'12 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Somente para o ente público - mensal'),
    ('13', u'13 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Somente para o ente público - 13° salário'),
    ('14', u'14 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Somente do segurado - mensal'),
    ('15', u'15 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Somente do segurado - 13° salário'),
    ('16', u'16 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Verbas temporárias - contribuição do segurado e a cargo do ente - mensal'),
    ('17', u'17 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Verbas temporárias - contribuição do segurado e a cargo do ente - 13º salário'),
    ('18', u'18 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Verbas temporárias - contribuição somente do segurado - mensal'),
    ('19', u'19 - Verbas temporárias - contribuição somente do segurado - 13° salário'),
    ('20', u'20 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Provento/pensão considerado para apuração da parcela excedente a teto RGPS'),
    ('21', u'21 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Do segurado de RPPS/militar e a cargo do ente público - mensal'),
    ('22', u'22 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Do segurado de RPPS/militar e a cargo do ente público - 13º salário'),
    ('23', u'23 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Somente para o ente público - mensal'),
    ('24', u'24 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Somente para o ente público - 13° salário'),
    ('25', u'25 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Verbas temporárias - contribuição do segurado e a cargo do ente - mensal'),
    ('26', u'26 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Verbas temporárias - contribuição do segurado e a cargo do ente - 13º salário'),
    ('27', u'27 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Verbas temporárias - contribuição somente do segurado - mensal'),
    ('28', u'28 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Verbas temporárias - contribuição somente do segurado - 13° salário'),
    ('31', u'31 - Contribuição descontada do segurado e beneficiário: Do segurado ativo RPPS/militar - mensal'),
    ('32', u'32 - Contribuição descontada do segurado e beneficiário: Do segurado ativo RPPS/militar - 13º salário'),
    ('33', u'33 - Contribuição descontada do segurado e beneficiário: Do aposentado RPPS/reforma/reserva - mensal'),
    ('34', u'34 - Contribuição descontada do segurado e beneficiário: Do aposentado RPPS /reforma/reserva - 13º salário'),
    ('35', u'35 - Contribuição descontada do segurado e beneficiário: Do pensionista RPPS/militar - mensal'),
    ('36', u'36 - Contribuição descontada do segurado e beneficiário: Do pensionista RPPS/militar - 13º salário'),
    ('41', u'41 - Contribuição descontada para RPPS de outro ente público: Do segurado ativo RPPS/militar - mensal'),
    ('42', u'42 - Contribuição descontada para RPPS de outro ente público: Do segurado ativo RPPS/militar - 13º salário'),
    ('51', u'51 - Isenção de contribuição: Contribuição descontada para RPPS de outro ente público: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - mensal'),
    ('52', u'52 - Contribuição descontada para RPPS de outro ente público: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - 13º salário'),
    ('91', u'91 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do segurado ativo RPPS/militar - mensal'),
    ('92', u'92 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do segurado ativo RPPS/militar - 13º salário'),
    ('93', u'93 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do aposentado/reforma/reserva - mensal'),
    ('94', u'94 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do aposentado/reforma/reserva - 13º salário'),
    ('95', u'95 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do pensionista - mensal'),
    ('96', u'96 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do pensionista - 13º salário'),
)

CHOICES_S1010_ALTERACAO_CODINCFGTS = (
    ('00', u'00 - Não é Base de Cálculo do FGTS'),
    ('11', u'11 - Base de Cálculo do FGTS'),
    ('12', u'12 - Base de Cálculo do FGTS 13° salário'),
    ('21', u'21 - Base de Cálculo do FGTS Rescisório (aviso prévio)'),
    ('91', u'91 - Incidência suspensa em decorrência de decisão judicial'),
)

CHOICES_S1010_ALTERACAO_CODINCIRRF = (
    ('00', u'00 - Rendimento não tributável'),
    ('01', u'01 - Rendimento não tributável em função de acordos internacionais de bitributação'),
    ('09', u'09 - Outras verbas não consideradas como base de cálculo ou rendimento'),
    ('11', u'11 - Rendimentos tributáveis - base de cálculo do IRRF: Remuneração mensal'),
    ('12', u'12 - Rendimentos tributáveis - base de cálculo do IRRF: 13o Salário'),
    ('13', u'13 - Rendimentos tributáveis - base de cálculo do IRRF: Férias'),
    ('14', u'14 - Rendimentos tributáveis - base de cálculo do IRRF: PLR'),
    ('15', u'15 - Rendimentos tributáveis - base de cálculo do IRRF: Rendimentos Recebidos Acumuladamente - RRA'),
    ('31', u'31 - Retenções do IRRF efetuadas sobre: Remuneração mensal'),
    ('32', u'32 - Retenções do IRRF efetuadas sobre: 13o Salário'),
    ('33', u'33 - Retenções do IRRF efetuadas sobre: Férias'),
    ('34', u'34 - Retenções do IRRF efetuadas sobre: PLR'),
    ('35', u'35 - Retenções do IRRF efetuadas sobre: RRA'),
    ('41', u'41 - Deduções da base de cálculo do IRRF: Previdência Social Oficial - PSO - Remuner. mensal'),
    ('42', u'42 - Deduções da base de cálculo do IRRF: PSO - 13° salário'),
    ('43', u'43 - Deduções da base de cálculo do IRRF: PSO - Férias'),
    ('44', u'44 - Deduções da base de cálculo do IRRF: PSO - RRA'),
    ('46', u'46 - Deduções da base de cálculo do IRRF: Previdência Privada - salário mensal'),
    ('47', u'47 - Deduções da base de cálculo do IRRF: Previdência Privada - 13° salário'),
    ('51', u'51 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - Remuneração mensal'),
    ('52', u'52 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - 13° salário'),
    ('53', u'53 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - Férias'),
    ('54', u'54 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - PLR'),
    ('55', u'55 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - RRA'),
    ('61', u'61 - Deduções da base de cálculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - Remuneração mensal'),
    ('62', u'62 - Deduções da base de cálculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - 13° salário'),
    ('63', u'63 - Deduções da base de cálculo do IRRF: Fundação de Previdência Complementar do Servidor Público - Funpresp - Remuneração mensal'),
    ('64', u'64 - Deduções da base de cálculo do IRRF: Fundação de Previdência Complementar do Servidor Público - Funpresp - 13° salário'),
    ('70', u'70 - Isenções do IRRF: Parcela Isenta 65 anos - Remuneração mensal'),
    ('71', u'71 - Isenções do IRRF: Parcela Isenta 65 anos - 13° salário'),
    ('72', u'72 - Isenções do IRRF: Diárias'),
    ('73', u'73 - Isenções do IRRF: Ajuda de custo'),
    ('74', u'74 - Isenções do IRRF: Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho'),
    ('75', u'75 - Isenções do IRRF: Abono pecuniário'),
    ('76', u'76 - Isenções do IRRF: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - Remuneração Mensal'),
    ('77', u'77 - Isenções do IRRF: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - 13° salário'),
    ('78', u'78 - Isenções do IRRF: Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e alugueis'),
    ('79', u'79 - Isenções do IRRF: Outras isenções (o nome da rubrica deve ser claro para identificação da natureza dos valores)'),
    ('81', u'81 - Demandas Judiciais: Depósito judicial'),
    ('82', u'82 - Demandas Judiciais: Compensação judicial do ano calendário'),
    ('83', u'83 - Demandas Judiciais: Compensação judicial de anos anteriores'),
    ('91', u'91 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: Remuneração mensal'),
    ('92', u'92 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: 13o Salário'),
    ('93', u'93 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: Férias'),
    ('94', u'94 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: PLR'),
    ('95', u'95 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: RRA'),
)

CHOICES_S1010_ALTERACAO_CODINCSIND = (
    ('00', u'00 - Não é base de cálculo'),
    ('11', u'11 - Base de cálculo'),
    ('31', u'31 - Valor da contribuição sindical laboral descontada'),
    ('91', u'91 - Incidência suspensa em decorrência de decisão judicial'),
)

CHOICES_S1010_ALTERACAO_EXTDECISAO = (
    (1, u'1 - Contribuição Previdenciária Patronal'),
    (1, u'1 - Contribuição Previdenciária do Ente Público'),
    (2, u'2 - Contribuição Previdenciária Patronal + Descontada dos Segurados'),
    (2, u'2 - Contribuição Previdenciária do Ente Público + Descontada dos Segurados'),
    (3, u'3 - Contribuição Previdenciária Descontada dos Segurados'),
)

CHOICES_S1010_ALTERACAO_TETOREMUN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1010_ALTERACAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_S1010_ALTERACAO_TPRUBR = (
    (1, u'1 - Vencimento, provento ou pensão'),
    (2, u'2 - Desconto'),
    (3, u'3 - Informativa'),
    (4, u'4 - Informativa dedutora'),
)

CHOICES_S1010_INCLUSAO_CODINCCP = (
    ('00', u'00 - Não é base de cálculo'),
    ('01', u'01 - Não é base de cálculo em função de acordos internacionais de previdência social'),
    ('11', u'11 - Base de cálculo das contribuições sociais - Salário de Contribuição: Mensal'),
    ('12', u'12 - Base de cálculo das contribuições sociais - Salário de Contribuição: 13o Salário'),
    ('13', u'13 - Base de cálculo das contribuições sociais - Salário de Contribuição: Exclusiva do Empregador - mensal'),
    ('14', u'14 - Base de cálculo das contribuições sociais - Salário de Contribuição: Exclusiva do Empregador - 13° salário'),
    ('15', u'15 - Base de cálculo das contribuições sociais - Salário de Contribuição: Exclusiva do segurado - mensal'),
    ('16', u'16 - Base de cálculo das contribuições sociais - Salário de Contribuição: Exclusiva do segurado - 13° salário'),
    ('21', u'21 - Base de cálculo das contribuições sociais - Salário de Contribuição: Salário maternidade mensal pago pelo Empregador'),
    ('22', u'22 - Base de cálculo das contribuições sociais - Salário de Contribuição: Salário maternidade - 13o Salário, pago pelo Empregador'),
    ('23', u'23 - Base de cálculo das contribuições sociais - Salário de Contribuição: Auxilio doença mensal - Regime Próprio de Previdência Social'),
    ('24', u'24 - Base de cálculo das contribuições sociais - Salário de Contribuição: Auxilio doença 13o salário doença - Regime próprio de previdência social'),
    ('25', u'25 - Base de cálculo das contribuições sociais - Salário de Contribuição: Salário maternidade mensal pago pelo INSS'),
    ('26', u'26 - Base de cálculo das contribuições sociais - Salário de Contribuição: Salário maternidade - 13° salário, pago pelo INSS'),
    ('31', u'31 - Contribuição descontada do Segurado sobre salário de contribuição: Mensal'),
    ('32', u'32 - Contribuição descontada do Segurado sobre salário de contribuição: 13o Salário'),
    ('34', u'34 - Contribuição descontada do Segurado sobre salário de contribuição: SEST'),
    ('35', u'35 - Contribuição descontada do Segurado sobre salário de contribuição: SENAT'),
    ('51', u'51 - Outros: Salário-família'),
    ('61', u'61 - Outros: Complemento de salário-mínimo - Regime próprio de previdência social'),
    ('91', u'91 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Mensal'),
    ('92', u'92 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: 13o Salário'),
    ('93', u'93 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Salário maternidade'),
    ('94', u'94 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Salário maternidade 13o salário'),
    ('95', u'95 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Exclusiva do Empregador - mensal'),
    ('96', u'96 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Exclusiva do Empregador - 13º salário'),
    ('97', u'97 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Exclusiva do Empregador - Salário maternidade'),
    ('98', u'98 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Exclusiva do Empregador - Salário maternidade 13º salário'),
)

CHOICES_S1010_INCLUSAO_CODINCCPRP = (
    ('00', u'00 - Não compõe a apuração de contribuições devidas ao RPPS/regime militar: Sem incidência para RPPS/regime militar'),
    ('01', u'01 - Não compõe a apuração de contribuições devidas ao RPPS/regime militar: Sem incidência em função de acordos internacionais de previdência social'),
    ('10', u'10 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Do segurado de RPPS/militar e a cargo do ente público - mensal'),
    ('11', u'11 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Do segurado de RPPS/militar e a cargo do ente público - 13º salário'),
    ('12', u'12 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Somente para o ente público - mensal'),
    ('13', u'13 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Somente para o ente público - 13° salário'),
    ('14', u'14 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Somente do segurado - mensal'),
    ('15', u'15 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Somente do segurado - 13° salário'),
    ('16', u'16 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Verbas temporárias - contribuição do segurado e a cargo do ente - mensal'),
    ('17', u'17 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Verbas temporárias - contribuição do segurado e a cargo do ente - 13º salário'),
    ('18', u'18 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Verbas temporárias - contribuição somente do segurado - mensal'),
    ('19', u'19 - Verbas temporárias - contribuição somente do segurado - 13° salário'),
    ('20', u'20 - Base de cálculo das contribuições (remuneração de contribuição para o RPPS/regime militar): Provento/pensão considerado para apuração da parcela excedente a teto RGPS'),
    ('21', u'21 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Do segurado de RPPS/militar e a cargo do ente público - mensal'),
    ('22', u'22 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Do segurado de RPPS/militar e a cargo do ente público - 13º salário'),
    ('23', u'23 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Somente para o ente público - mensal'),
    ('24', u'24 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Somente para o ente público - 13° salário'),
    ('25', u'25 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Verbas temporárias - contribuição do segurado e a cargo do ente - mensal'),
    ('26', u'26 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Verbas temporárias - contribuição do segurado e a cargo do ente - 13º salário'),
    ('27', u'27 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Verbas temporárias - contribuição somente do segurado - mensal'),
    ('28', u'28 - Base de cálculo das contribuições (remuneração de contribuição) para o RPPS de outro ente público: Verbas temporárias - contribuição somente do segurado - 13° salário'),
    ('31', u'31 - Contribuição descontada do segurado e beneficiário: Do segurado ativo RPPS/militar - mensal'),
    ('32', u'32 - Contribuição descontada do segurado e beneficiário: Do segurado ativo RPPS/militar - 13º salário'),
    ('33', u'33 - Contribuição descontada do segurado e beneficiário: Do aposentado RPPS/reforma/reserva - mensal'),
    ('34', u'34 - Contribuição descontada do segurado e beneficiário: Do aposentado RPPS /reforma/reserva - 13º salário'),
    ('35', u'35 - Contribuição descontada do segurado e beneficiário: Do pensionista RPPS/militar - mensal'),
    ('36', u'36 - Contribuição descontada do segurado e beneficiário: Do pensionista RPPS/militar - 13º salário'),
    ('41', u'41 - Contribuição descontada para RPPS de outro ente público: Do segurado ativo RPPS/militar - mensal'),
    ('42', u'42 - Contribuição descontada para RPPS de outro ente público: Do segurado ativo RPPS/militar - 13º salário'),
    ('51', u'51 - Isenção de contribuição: Contribuição descontada para RPPS de outro ente público: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - mensal'),
    ('52', u'52 - Contribuição descontada para RPPS de outro ente público: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - 13º salário'),
    ('91', u'91 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do segurado ativo RPPS/militar - mensal'),
    ('92', u'92 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do segurado ativo RPPS/militar - 13º salário'),
    ('93', u'93 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do aposentado/reforma/reserva - mensal'),
    ('94', u'94 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do aposentado/reforma/reserva - 13º salário'),
    ('95', u'95 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do pensionista - mensal'),
    ('96', u'96 - Suspensão de incidência sobre Salário de Contribuição em decorrência de decisão judicial: Contribuição do pensionista - 13º salário'),
)

CHOICES_S1010_INCLUSAO_CODINCFGTS = (
    ('00', u'00 - Não é Base de Cálculo do FGTS'),
    ('11', u'11 - Base de Cálculo do FGTS'),
    ('12', u'12 - Base de Cálculo do FGTS 13° salário'),
    ('21', u'21 - Base de Cálculo do FGTS Rescisório (aviso prévio)'),
    ('91', u'91 - Incidência suspensa em decorrência de decisão judicial'),
)

CHOICES_S1010_INCLUSAO_CODINCIRRF = (
    ('00', u'00 - Rendimento não tributável'),
    ('01', u'01 - Rendimento não tributável em função de acordos internacionais de bitributação'),
    ('09', u'09 - Outras verbas não consideradas como base de cálculo ou rendimento'),
    ('11', u'11 - Rendimentos tributáveis - base de cálculo do IRRF: Remuneração mensal'),
    ('12', u'12 - Rendimentos tributáveis - base de cálculo do IRRF: 13o Salário'),
    ('13', u'13 - Rendimentos tributáveis - base de cálculo do IRRF: Férias'),
    ('14', u'14 - Rendimentos tributáveis - base de cálculo do IRRF: PLR'),
    ('15', u'15 - Rendimentos tributáveis - base de cálculo do IRRF: Rendimentos Recebidos Acumuladamente - RRA'),
    ('31', u'31 - Retenções do IRRF efetuadas sobre: Remuneração mensal'),
    ('32', u'32 - Retenções do IRRF efetuadas sobre: 13o Salário'),
    ('33', u'33 - Retenções do IRRF efetuadas sobre: Férias'),
    ('34', u'34 - Retenções do IRRF efetuadas sobre: PLR'),
    ('35', u'35 - Retenções do IRRF efetuadas sobre: RRA'),
    ('41', u'41 - Deduções da base de cálculo do IRRF: Previdência Social Oficial - PSO - Remuner. mensal'),
    ('42', u'42 - Deduções da base de cálculo do IRRF: PSO - 13° salário'),
    ('43', u'43 - Deduções da base de cálculo do IRRF: PSO - Férias'),
    ('44', u'44 - Deduções da base de cálculo do IRRF: PSO - RRA'),
    ('46', u'46 - Deduções da base de cálculo do IRRF: Previdência Privada - salário mensal'),
    ('47', u'47 - Deduções da base de cálculo do IRRF: Previdência Privada - 13° salário'),
    ('51', u'51 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - Remuneração mensal'),
    ('52', u'52 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - 13° salário'),
    ('53', u'53 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - Férias'),
    ('54', u'54 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - PLR'),
    ('55', u'55 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - RRA'),
    ('61', u'61 - Deduções da base de cálculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - Remuneração mensal'),
    ('62', u'62 - Deduções da base de cálculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - 13° salário'),
    ('63', u'63 - Deduções da base de cálculo do IRRF: Fundação de Previdência Complementar do Servidor Público - Funpresp - Remuneração mensal'),
    ('64', u'64 - Deduções da base de cálculo do IRRF: Fundação de Previdência Complementar do Servidor Público - Funpresp - 13° salário'),
    ('70', u'70 - Isenções do IRRF: Parcela Isenta 65 anos - Remuneração mensal'),
    ('71', u'71 - Isenções do IRRF: Parcela Isenta 65 anos - 13° salário'),
    ('72', u'72 - Isenções do IRRF: Diárias'),
    ('73', u'73 - Isenções do IRRF: Ajuda de custo'),
    ('74', u'74 - Isenções do IRRF: Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho'),
    ('75', u'75 - Isenções do IRRF: Abono pecuniário'),
    ('76', u'76 - Isenções do IRRF: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - Remuneração Mensal'),
    ('77', u'77 - Isenções do IRRF: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - 13° salário'),
    ('78', u'78 - Isenções do IRRF: Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e alugueis'),
    ('79', u'79 - Isenções do IRRF: Outras isenções (o nome da rubrica deve ser claro para identificação da natureza dos valores)'),
    ('81', u'81 - Demandas Judiciais: Depósito judicial'),
    ('82', u'82 - Demandas Judiciais: Compensação judicial do ano calendário'),
    ('83', u'83 - Demandas Judiciais: Compensação judicial de anos anteriores'),
    ('91', u'91 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: Remuneração mensal'),
    ('92', u'92 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: 13o Salário'),
    ('93', u'93 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: Férias'),
    ('94', u'94 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: PLR'),
    ('95', u'95 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: RRA'),
)

CHOICES_S1010_INCLUSAO_CODINCSIND = (
    ('00', u'00 - Não é base de cálculo'),
    ('11', u'11 - Base de cálculo'),
    ('31', u'31 - Valor da contribuição sindical laboral descontada'),
    ('91', u'91 - Incidência suspensa em decorrência de decisão judicial'),
)

CHOICES_S1010_INCLUSAO_EXTDECISAO = (
    (1, u'1 - Contribuição Previdenciária Patronal'),
    (1, u'1 - Contribuição Previdenciária do Ente Público'),
    (2, u'2 - Contribuição Previdenciária Patronal + Descontada dos Segurados'),
    (2, u'2 - Contribuição Previdenciária do Ente Público + Descontada dos Segurados'),
    (3, u'3 - Contribuição Previdenciária Descontada dos Segurados'),
)

CHOICES_S1010_INCLUSAO_TETOREMUN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1010_INCLUSAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_S1010_INCLUSAO_TPRUBR = (
    (1, u'1 - Vencimento, provento ou pensão'),
    (2, u'2 - Desconto'),
    (3, u'3 - Informativa'),
    (4, u'4 - Informativa dedutora'),
)

PERIODOS = (
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
)

class s1010alteracao(SoftDeletionModel):
    s1010_evttabrubrica = models.OneToOneField('esocial.s1010evtTabRubrica',
        related_name='%(class)s_s1010_evttabrubrica')
    def evento(self): return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dscrubr = models.CharField(max_length=100)
    natrubr = models.TextField(max_length=4)
    tprubr = models.IntegerField(choices=CHOICES_S1010_ALTERACAO_TPRUBR)
    codinccp = models.CharField(choices=CHOICES_S1010_ALTERACAO_CODINCCP, max_length=2)
    codincirrf = models.CharField(choices=CHOICES_S1010_ALTERACAO_CODINCIRRF, max_length=2)
    codincfgts = models.CharField(choices=CHOICES_S1010_ALTERACAO_CODINCFGTS, max_length=2)
    codincsind = models.CharField(choices=CHOICES_S1010_ALTERACAO_CODINCSIND, max_length=2)
    codinccprp = models.CharField(choices=CHOICES_S1010_ALTERACAO_CODINCCPRP, max_length=2, blank=True, null=True)
    tetoremun = models.CharField(choices=CHOICES_S1010_ALTERACAO_TETOREMUN, max_length=1, blank=True, null=True)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_evttabrubrica) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.dscrubr) + ' - ' + unicode(self.natrubr) + ' - ' + unicode(self.tprubr) + ' - ' + unicode(self.codinccp) + ' - ' + unicode(self.codincirrf) + ' - ' + unicode(self.codincfgts) + ' - ' + unicode(self.codincsind)
    #s1010_alteracao_custom#

    class Meta:
        db_table = r's1010_alteracao'       
        managed = True # s1010_alteracao #
        permissions = (
            ("can_view_s1010_alteracao", "Can view s1010_alteracao"),
            #custom_permissions_s1010_alteracao
        )
        ordering = ['s1010_evttabrubrica', 'codrubr', 'idetabrubr', 'inivalid', 'dscrubr', 'natrubr', 'tprubr', 'codinccp', 'codincirrf', 'codincfgts', 'codincsind']



class s1010alteracaoSerializer(ModelSerializer):
    class Meta:
        model = s1010alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010alteracaoideProcessoCP(SoftDeletionModel):
    s1010_alteracao = models.ForeignKey('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_ALTERACAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    extdecisao = models.IntegerField(choices=CHOICES_S1010_ALTERACAO_EXTDECISAO)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.extdecisao) + ' - ' + unicode(self.codsusp)
    #s1010_alteracao_ideprocessocp_custom#

    class Meta:
        db_table = r's1010_alteracao_ideprocessocp'       
        managed = True # s1010_alteracao_ideprocessocp #
        permissions = (
            ("can_view_s1010_alteracao_ideprocessocp", "Can view s1010_alteracao_ideprocessocp"),
            #custom_permissions_s1010_alteracao_ideprocessocp
        )
        ordering = ['s1010_alteracao', 'tpproc', 'nrproc', 'extdecisao', 'codsusp']



class s1010alteracaoideProcessoCPSerializer(ModelSerializer):
    class Meta:
        model = s1010alteracaoideProcessoCP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010alteracaoideProcessoCPRP(SoftDeletionModel):
    s1010_alteracao = models.ForeignKey('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_ALTERACAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    extdecisao = models.IntegerField(choices=CHOICES_S1010_ALTERACAO_EXTDECISAO)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.extdecisao)
    #s1010_alteracao_ideprocessocprp_custom#

    class Meta:
        db_table = r's1010_alteracao_ideprocessocprp'       
        managed = True # s1010_alteracao_ideprocessocprp #
        permissions = (
            ("can_view_s1010_alteracao_ideprocessocprp", "Can view s1010_alteracao_ideprocessocprp"),
            #custom_permissions_s1010_alteracao_ideprocessocprp
        )
        ordering = ['s1010_alteracao', 'tpproc', 'nrproc', 'extdecisao']



class s1010alteracaoideProcessoCPRPSerializer(ModelSerializer):
    class Meta:
        model = s1010alteracaoideProcessoCPRP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010alteracaoideProcessoFGTS(SoftDeletionModel):
    s1010_alteracao = models.ForeignKey('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.nrproc)
    #s1010_alteracao_ideprocessofgts_custom#

    class Meta:
        db_table = r's1010_alteracao_ideprocessofgts'       
        managed = True # s1010_alteracao_ideprocessofgts #
        permissions = (
            ("can_view_s1010_alteracao_ideprocessofgts", "Can view s1010_alteracao_ideprocessofgts"),
            #custom_permissions_s1010_alteracao_ideprocessofgts
        )
        ordering = ['s1010_alteracao', 'nrproc']



class s1010alteracaoideProcessoFGTSSerializer(ModelSerializer):
    class Meta:
        model = s1010alteracaoideProcessoFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010alteracaoideProcessoIRRF(SoftDeletionModel):
    s1010_alteracao = models.ForeignKey('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp)
    #s1010_alteracao_ideprocessoirrf_custom#

    class Meta:
        db_table = r's1010_alteracao_ideprocessoirrf'       
        managed = True # s1010_alteracao_ideprocessoirrf #
        permissions = (
            ("can_view_s1010_alteracao_ideprocessoirrf", "Can view s1010_alteracao_ideprocessoirrf"),
            #custom_permissions_s1010_alteracao_ideprocessoirrf
        )
        ordering = ['s1010_alteracao', 'nrproc', 'codsusp']



class s1010alteracaoideProcessoIRRFSerializer(ModelSerializer):
    class Meta:
        model = s1010alteracaoideProcessoIRRF
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010alteracaoideProcessoSIND(SoftDeletionModel):
    s1010_alteracao = models.ForeignKey('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.nrproc)
    #s1010_alteracao_ideprocessosind_custom#

    class Meta:
        db_table = r's1010_alteracao_ideprocessosind'       
        managed = True # s1010_alteracao_ideprocessosind #
        permissions = (
            ("can_view_s1010_alteracao_ideprocessosind", "Can view s1010_alteracao_ideprocessosind"),
            #custom_permissions_s1010_alteracao_ideprocessosind
        )
        ordering = ['s1010_alteracao', 'nrproc']



class s1010alteracaoideProcessoSINDSerializer(ModelSerializer):
    class Meta:
        model = s1010alteracaoideProcessoSIND
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010alteracaonovaValidade(SoftDeletionModel):
    s1010_alteracao = models.OneToOneField('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.inivalid)
    #s1010_alteracao_novavalidade_custom#

    class Meta:
        db_table = r's1010_alteracao_novavalidade'       
        managed = True # s1010_alteracao_novavalidade #
        permissions = (
            ("can_view_s1010_alteracao_novavalidade", "Can view s1010_alteracao_novavalidade"),
            #custom_permissions_s1010_alteracao_novavalidade
        )
        ordering = ['s1010_alteracao', 'inivalid']



class s1010alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = s1010alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010exclusao(SoftDeletionModel):
    s1010_evttabrubrica = models.OneToOneField('esocial.s1010evtTabRubrica',
        related_name='%(class)s_s1010_evttabrubrica')
    def evento(self): return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_evttabrubrica) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.inivalid)
    #s1010_exclusao_custom#

    class Meta:
        db_table = r's1010_exclusao'       
        managed = True # s1010_exclusao #
        permissions = (
            ("can_view_s1010_exclusao", "Can view s1010_exclusao"),
            #custom_permissions_s1010_exclusao
        )
        ordering = ['s1010_evttabrubrica', 'codrubr', 'idetabrubr', 'inivalid']



class s1010exclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1010exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010inclusao(SoftDeletionModel):
    s1010_evttabrubrica = models.OneToOneField('esocial.s1010evtTabRubrica',
        related_name='%(class)s_s1010_evttabrubrica')
    def evento(self): return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dscrubr = models.CharField(max_length=100)
    natrubr = models.TextField(max_length=4)
    tprubr = models.IntegerField(choices=CHOICES_S1010_INCLUSAO_TPRUBR)
    codinccp = models.CharField(choices=CHOICES_S1010_INCLUSAO_CODINCCP, max_length=2)
    codincirrf = models.CharField(choices=CHOICES_S1010_INCLUSAO_CODINCIRRF, max_length=2)
    codincfgts = models.CharField(choices=CHOICES_S1010_INCLUSAO_CODINCFGTS, max_length=2)
    codincsind = models.CharField(choices=CHOICES_S1010_INCLUSAO_CODINCSIND, max_length=2)
    codinccprp = models.CharField(choices=CHOICES_S1010_INCLUSAO_CODINCCPRP, max_length=2, blank=True, null=True)
    tetoremun = models.CharField(choices=CHOICES_S1010_INCLUSAO_TETOREMUN, max_length=1, blank=True, null=True)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_evttabrubrica) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.dscrubr) + ' - ' + unicode(self.natrubr) + ' - ' + unicode(self.tprubr) + ' - ' + unicode(self.codinccp) + ' - ' + unicode(self.codincirrf) + ' - ' + unicode(self.codincfgts) + ' - ' + unicode(self.codincsind)
    #s1010_inclusao_custom#

    class Meta:
        db_table = r's1010_inclusao'       
        managed = True # s1010_inclusao #
        permissions = (
            ("can_view_s1010_inclusao", "Can view s1010_inclusao"),
            #custom_permissions_s1010_inclusao
        )
        ordering = ['s1010_evttabrubrica', 'codrubr', 'idetabrubr', 'inivalid', 'dscrubr', 'natrubr', 'tprubr', 'codinccp', 'codincirrf', 'codincfgts', 'codincsind']



class s1010inclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1010inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010inclusaoideProcessoCP(SoftDeletionModel):
    s1010_inclusao = models.ForeignKey('s1010inclusao',
        related_name='%(class)s_s1010_inclusao')
    def evento(self): return self.s1010_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_INCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    extdecisao = models.IntegerField(choices=CHOICES_S1010_INCLUSAO_EXTDECISAO)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_inclusao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.extdecisao) + ' - ' + unicode(self.codsusp)
    #s1010_inclusao_ideprocessocp_custom#

    class Meta:
        db_table = r's1010_inclusao_ideprocessocp'       
        managed = True # s1010_inclusao_ideprocessocp #
        permissions = (
            ("can_view_s1010_inclusao_ideprocessocp", "Can view s1010_inclusao_ideprocessocp"),
            #custom_permissions_s1010_inclusao_ideprocessocp
        )
        ordering = ['s1010_inclusao', 'tpproc', 'nrproc', 'extdecisao', 'codsusp']



class s1010inclusaoideProcessoCPSerializer(ModelSerializer):
    class Meta:
        model = s1010inclusaoideProcessoCP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010inclusaoideProcessoCPRP(SoftDeletionModel):
    s1010_inclusao = models.ForeignKey('s1010inclusao',
        related_name='%(class)s_s1010_inclusao')
    def evento(self): return self.s1010_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_INCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    extdecisao = models.IntegerField(choices=CHOICES_S1010_INCLUSAO_EXTDECISAO)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_inclusao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.extdecisao)
    #s1010_inclusao_ideprocessocprp_custom#

    class Meta:
        db_table = r's1010_inclusao_ideprocessocprp'       
        managed = True # s1010_inclusao_ideprocessocprp #
        permissions = (
            ("can_view_s1010_inclusao_ideprocessocprp", "Can view s1010_inclusao_ideprocessocprp"),
            #custom_permissions_s1010_inclusao_ideprocessocprp
        )
        ordering = ['s1010_inclusao', 'tpproc', 'nrproc', 'extdecisao']



class s1010inclusaoideProcessoCPRPSerializer(ModelSerializer):
    class Meta:
        model = s1010inclusaoideProcessoCPRP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010inclusaoideProcessoFGTS(SoftDeletionModel):
    s1010_inclusao = models.ForeignKey('s1010inclusao',
        related_name='%(class)s_s1010_inclusao')
    def evento(self): return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_inclusao) + ' - ' + unicode(self.nrproc)
    #s1010_inclusao_ideprocessofgts_custom#

    class Meta:
        db_table = r's1010_inclusao_ideprocessofgts'       
        managed = True # s1010_inclusao_ideprocessofgts #
        permissions = (
            ("can_view_s1010_inclusao_ideprocessofgts", "Can view s1010_inclusao_ideprocessofgts"),
            #custom_permissions_s1010_inclusao_ideprocessofgts
        )
        ordering = ['s1010_inclusao', 'nrproc']



class s1010inclusaoideProcessoFGTSSerializer(ModelSerializer):
    class Meta:
        model = s1010inclusaoideProcessoFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010inclusaoideProcessoIRRF(SoftDeletionModel):
    s1010_inclusao = models.ForeignKey('s1010inclusao',
        related_name='%(class)s_s1010_inclusao')
    def evento(self): return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_inclusao) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp)
    #s1010_inclusao_ideprocessoirrf_custom#

    class Meta:
        db_table = r's1010_inclusao_ideprocessoirrf'       
        managed = True # s1010_inclusao_ideprocessoirrf #
        permissions = (
            ("can_view_s1010_inclusao_ideprocessoirrf", "Can view s1010_inclusao_ideprocessoirrf"),
            #custom_permissions_s1010_inclusao_ideprocessoirrf
        )
        ordering = ['s1010_inclusao', 'nrproc', 'codsusp']



class s1010inclusaoideProcessoIRRFSerializer(ModelSerializer):
    class Meta:
        model = s1010inclusaoideProcessoIRRF
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1010inclusaoideProcessoSIND(SoftDeletionModel):
    s1010_inclusao = models.ForeignKey('s1010inclusao',
        related_name='%(class)s_s1010_inclusao')
    def evento(self): return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1010_inclusao) + ' - ' + unicode(self.nrproc)
    #s1010_inclusao_ideprocessosind_custom#

    class Meta:
        db_table = r's1010_inclusao_ideprocessosind'       
        managed = True # s1010_inclusao_ideprocessosind #
        permissions = (
            ("can_view_s1010_inclusao_ideprocessosind", "Can view s1010_inclusao_ideprocessosind"),
            #custom_permissions_s1010_inclusao_ideprocessosind
        )
        ordering = ['s1010_inclusao', 'nrproc']



class s1010inclusaoideProcessoSINDSerializer(ModelSerializer):
    class Meta:
        model = s1010inclusaoideProcessoSIND
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
