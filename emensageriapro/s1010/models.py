#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



PERIODOS = (
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
)

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
    (2, u'2 - Contribuição Previdenciária Patronal + Descontada dos Segurados'),
)

CHOICES_S1010_ALTERACAO_NATRUBR = (
    (1000, u'1000 - Salário, vencimento, soldo ou subsídio'),
    (1002, u'1002 - Descanso semanal remunerado - DSR'),
    (1003, u'1003 - Horas extraordinárias'),
    (1004, u'1004 - Horas extraordinárias - Indenização de banco de horas'),
    (1005, u'1005 - Direito de arena'),
    (1006, u'1006 - Intervalos intra e inter jornadas não concedidos'),
    (1007, u'1007 - Luvas e premiações'),
    (1009, u'1009 - Salário-família - complemento'),
    (1010, u'1010 - Salário in natura - pagos em bens ou serviços'),
    (1011, u'1011 - Sobreaviso e prontidão'),
    (1020, u'1020 - Férias - gozadas'),
    (1021, u'1021 - Férias - abono ou gratificação de férias superior a 20 dias'),
    (1022, u'1022 - Férias - abono ou gratificação de férias não excedente a 20 dias'),
    (1023, u'1023 - Férias - abono pecuniário'),
    (1024, u'1024 - Férias - o dobro na vigência do contrato'),
    (1040, u'1040 - Licença-prêmio'),
    (1041, u'1041 - Licença-prêmio indenizada'),
    (1050, u'1050 - Remuneração de dias de afastamento'),
    (1080, u'1080 - Stock Option'),
    (1099, u'1099 - Outras verbas salariais'),
    (1201, u'1201 - Adicional de função / cargo confiança'),
    (1202, u'1202 - Adicional de insalubridade'),
    (1203, u'1203 - Adicional de periculosidade'),
    (1204, u'1204 - Adicional de transferência'),
    (1205, u'1205 - Adicional noturno'),
    (1206, u'1206 - Adicional por tempo de serviço'),
    (1207, u'1207 - Comissões, porcentagens, produção'),
    (1208, u'1208 - Gueltas ou gorjetas - repassadas por fornecedores ou clientes'),
    (1209, u'1209 - Gueltas ou gorjetas - repassadas pelo empregador'),
    (1210, u'1210 - Gratificação por acordo ou convenção coletiva'),
    (1211, u'1211 - Gratificações'),
    (1212, u'1212 - Gratificações ou outras verbas de natureza permanente'),
    (1213, u'1213 - Gratificações ou outras verbas de natureza transitória'),
    (1214, u'1214 - Adicional de penosidade'),
    (1215, u'1215 - Adicional de unidocência'),
    (1225, u'1225 - Quebra de caixa'),
    (1230, u'1230 - Remuneração do dirigente sindical'),
    (1299, u'1299 - Outros adicionais'),
    (1300, u'1300 - PLR - Participação em Lucros ou Resultados'),
    (1350, u'1350 - Bolsa de estudo - estagiário'),
    (1351, u'1351 - Bolsa de estudo - médico residente'),
    (1352, u'1352 - Bolsa de estudo ou pesquisa'),
    (1401, u'1401 - Abono'),
    (1402, u'1402 - Abono PIS / PASEP'),
    (1403, u'1403 - Abono legal'),
    (1404, u'1404 - Auxílio babá'),
    (1405, u'1405 - Assistência médica'),
    (1406, u'1406 - Auxílio-creche'),
    (1407, u'1407 - Auxílio-educação'),
    (1409, u'1409 - Salário-família'),
    (1410, u'1410 - Auxílio - Locais de difícil acesso'),
    (1601, u'1601 - Ajuda de custo - aeronauta'),
    (1602, u'1602 - Ajuda de custo de transferência'),
    (1620, u'1620 - Ressarcimento de despesas pelo uso de veículo próprio'),
    (1621, u'1621 - Ressarcimento de despesas de viagem, exceto despesas com veículos'),
    (1623, u'1623 - Ressarcimento de provisão'),
    (1629, u'1629 - Ressarcimento de outras despesas'),
    (1651, u'1651 - Diárias de viagem - até 50% do salário'),
    (1652, u'1652 - Diárias de viagem - acima de 50% do salário'),
    (1801, u'1801 - Alimentação'),
    (1802, u'1802 - Etapas (marítimos)'),
    (1805, u'1805 - Moradia'),
    (1810, u'1810 - Transporte'),
    (2501, u'2501 - Prêmios'),
    (2510, u'2510 - Direitos autorais e intelectuais'),
    (2801, u'2801 - Quarentena remunerada'),
    (2901, u'2901 - Empréstimos'),
    (2902, u'2902 - Vestuário e equipamentos'),
    (2920, u'2920 - Reembolsos diversos'),
    (2930, u'2930 - Insuficiência de saldo'),
    (2999, u'2999 - Arredondamentos'),
    (3501, u'3501 - Remuneração por prestação de serviços'),
    (3505, u'3505 - Retiradas (pró-labore) de diretores empregados'),
    (3506, u'3506 - Retiradas (pró-labore) de diretores não empregados'),
    (3508, u'3508 - Retiradas (pró-labore) de proprietários ou sócios'),
    (3509, u'3509 - Honorários a conselheiros'),
    (3520, u'3520 - Remuneração de cooperado'),
    (4010, u'4010 - Complementação salarial de auxílio-doença'),
    (4050, u'4050 - Salário maternidade'),
    (4051, u'4051 - Salário maternidade - 13° salário'),
    (5001, u'5001 - 13º salário'),
    (5005, u'5005 - 13° salário complementar'),
    (5501, u'5501 - Adiantamento de salário'),
    (5504, u'5504 - 13º salário - Adiantamento'),
    (5510, u'5510 - Adiantamento de benefícios previdenciários'),
    (6000, u'6000 - Saldo de salários na rescisão contratual'),
    (6001, u'6001 - 13º salário relativo ao aviso-prévio indenizado'),
    (6002, u'6002 - 13° salário proporcional na rescisão'),
    (6003, u'6003 - Indenização compensatória do aviso-prévio'),
    (6004, u'6004 - Férias - o dobro na rescisão'),
    (6006, u'6006 - Férias proporcionais'),
    (6007, u'6007 - Férias vencidas na rescisão'),
    (6101, u'6101 - Indenização compensatória - multa rescisória 20 ou 40% (CF/88)'),
    (6102, u'6102 - Indenização do art. 9º lei nº 7.238/84'),
    (6103, u'6103 - Indenização do art. 14 da lei nº 5.889, de 8 de junho de 1973'),
    (6104, u'6104 - Indenização do art. 479 da CLT'),
    (6105, u'6105 - Indenização recebida a título de incentivo a demissão'),
    (6106, u'6106 - Multa do art. 477 da CLT'),
    (6107, u'6107 - Indenização por quebra de estabilidade'),
    (6129, u'6129 - Outras Indenizações'),
    (6901, u'6901 - Desconto do aviso-prévio'),
    (6904, u'6904 - Multa prevista no art. 480 da CLT'),
    (7001, u'7001 - Proventos'),
    (7002, u'7002 - Proventos - Pensão por morte Civil'),
    (7003, u'7003 - Proventos - Reserva'),
    (7004, u'7004 - Proventos - Reforma'),
    (7005, u'7005 - Pensão Militar'),
    (9200, u'9200 - Desconto de Adiantamentos'),
    (9201, u'9201 - Contribuição Previdenciária'),
    (9203, u'9203 - Imposto de renda retido na fonte'),
    (9205, u'9205 - Provisão de contribuição previdenciária e IRRF'),
    (9209, u'9209 - Faltas ou atrasos'),
    (9210, u'9210 - DSR s/faltas e atrasos'),
    (9213, u'9213 - Pensão alimentícia'),
    (9214, u'9214 - 13° salário - desconto de adiantamento'),
    (9216, u'9216 - Desconto de vale- transporte'),
    (9217, u'9217 - Contribuição a Outras Entidades e Fundos'),
    (9218, u'9218 - Retenções judiciais'),
    (9219, u'9219 - Desconto de assistência médica ou odontológica'),
    (9220, u'9220 - Alimentação - desconto'),
    (9221, u'9221 - Desconto de férias'),
    (9222, u'9222 - Desconto de outros impostos e contribuições'),
    (9223, u'9223 - Previdência complementar - parte do empregado'),
    (9224, u'9224 - FAPI - parte do empregado'),
    (9225, u'9225 - Previdência complementar - parte do servidor'),
    (9226, u'9226 - Desconto de férias - abono'),
    (9230, u'9230 - Contribuição Sindical - Compulsória'),
    (9231, u'9231 - Contribuição Sindical - Associativa'),
    (9232, u'9232 - Contribuição Sindical - Assistencial'),
    (9233, u'9233 - Contribuição sindical - Confederativa'),
    (9250, u'9250 - Seguro de vida - desconto'),
    (9254, u'9254 - Empréstimos consignados - desconto'),
    (9255, u'9255 - Empréstimos do empregador - desconto'),
    (9258, u'9258 - Convênios'),
    (9270, u'9270 - Danos e prejuízos causados pelo trabalhador'),
    (9290, u'9290 - Desconto de pagamento indevido em meses anteriores'),
    (9299, u'9299 - Outros descontos'),
    (9901, u'9901 - Base de cálculo da contribuição previdenciária'),
    (9902, u'9902 - Total da base de cálculo do FGTS'),
    (9903, u'9903 - Total da base de cálculo do IRRF'),
    (9904, u'9904 - Total da base de cálculo do FGTS rescisório'),
    (9905, u'9905 - Serviço militar'),
    (9906, u'9906 - Remuneração no exterior'),
    (9908, u'9908 - FGTS - depósito'),
    (9910, u'9910 - Seguros'),
    (9911, u'9911 - Assistência Médica'),
    (9930, u'9930 - Salário maternidade pago pela Previdência Social'),
    (9931, u'9931 - 13° salário maternidade pago pela Previdência Social'),
    (9932, u'9932 - Auxílio-doença acidentário'),
    (9933, u'9933 - Auxílio-doença'),
    (9938, u'9938 - Isenção IRRF - 65 anos'),
    (9939, u'9939 - Outros valores tributáveis'),
    (9950, u'9950 - Horas extraordinárias - Banco de horas'),
    (9951, u'9951 - Horas compensadas - Banco de horas'),
    (9989, u'9989 - Outros valores informativos'),
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
    (2, u'2 - Contribuição Previdenciária Patronal + Descontada dos Segurados'),
)

CHOICES_S1010_INCLUSAO_NATRUBR = (
    (1000, u'1000 - Salário, vencimento, soldo ou subsídio'),
    (1002, u'1002 - Descanso semanal remunerado - DSR'),
    (1003, u'1003 - Horas extraordinárias'),
    (1004, u'1004 - Horas extraordinárias - Indenização de banco de horas'),
    (1005, u'1005 - Direito de arena'),
    (1006, u'1006 - Intervalos intra e inter jornadas não concedidos'),
    (1007, u'1007 - Luvas e premiações'),
    (1009, u'1009 - Salário-família - complemento'),
    (1010, u'1010 - Salário in natura - pagos em bens ou serviços'),
    (1011, u'1011 - Sobreaviso e prontidão'),
    (1020, u'1020 - Férias - gozadas'),
    (1021, u'1021 - Férias - abono ou gratificação de férias superior a 20 dias'),
    (1022, u'1022 - Férias - abono ou gratificação de férias não excedente a 20 dias'),
    (1023, u'1023 - Férias - abono pecuniário'),
    (1024, u'1024 - Férias - o dobro na vigência do contrato'),
    (1040, u'1040 - Licença-prêmio'),
    (1041, u'1041 - Licença-prêmio indenizada'),
    (1050, u'1050 - Remuneração de dias de afastamento'),
    (1080, u'1080 - Stock Option'),
    (1099, u'1099 - Outras verbas salariais'),
    (1201, u'1201 - Adicional de função / cargo confiança'),
    (1202, u'1202 - Adicional de insalubridade'),
    (1203, u'1203 - Adicional de periculosidade'),
    (1204, u'1204 - Adicional de transferência'),
    (1205, u'1205 - Adicional noturno'),
    (1206, u'1206 - Adicional por tempo de serviço'),
    (1207, u'1207 - Comissões, porcentagens, produção'),
    (1208, u'1208 - Gueltas ou gorjetas - repassadas por fornecedores ou clientes'),
    (1209, u'1209 - Gueltas ou gorjetas - repassadas pelo empregador'),
    (1210, u'1210 - Gratificação por acordo ou convenção coletiva'),
    (1211, u'1211 - Gratificações'),
    (1212, u'1212 - Gratificações ou outras verbas de natureza permanente'),
    (1213, u'1213 - Gratificações ou outras verbas de natureza transitória'),
    (1214, u'1214 - Adicional de penosidade'),
    (1215, u'1215 - Adicional de unidocência'),
    (1225, u'1225 - Quebra de caixa'),
    (1230, u'1230 - Remuneração do dirigente sindical'),
    (1299, u'1299 - Outros adicionais'),
    (1300, u'1300 - PLR - Participação em Lucros ou Resultados'),
    (1350, u'1350 - Bolsa de estudo - estagiário'),
    (1351, u'1351 - Bolsa de estudo - médico residente'),
    (1352, u'1352 - Bolsa de estudo ou pesquisa'),
    (1401, u'1401 - Abono'),
    (1402, u'1402 - Abono PIS / PASEP'),
    (1403, u'1403 - Abono legal'),
    (1404, u'1404 - Auxílio babá'),
    (1405, u'1405 - Assistência médica'),
    (1406, u'1406 - Auxílio-creche'),
    (1407, u'1407 - Auxílio-educação'),
    (1409, u'1409 - Salário-família'),
    (1410, u'1410 - Auxílio - Locais de difícil acesso'),
    (1601, u'1601 - Ajuda de custo - aeronauta'),
    (1602, u'1602 - Ajuda de custo de transferência'),
    (1620, u'1620 - Ressarcimento de despesas pelo uso de veículo próprio'),
    (1621, u'1621 - Ressarcimento de despesas de viagem, exceto despesas com veículos'),
    (1623, u'1623 - Ressarcimento de provisão'),
    (1629, u'1629 - Ressarcimento de outras despesas'),
    (1651, u'1651 - Diárias de viagem - até 50% do salário'),
    (1652, u'1652 - Diárias de viagem - acima de 50% do salário'),
    (1801, u'1801 - Alimentação'),
    (1802, u'1802 - Etapas (marítimos)'),
    (1805, u'1805 - Moradia'),
    (1810, u'1810 - Transporte'),
    (2501, u'2501 - Prêmios'),
    (2510, u'2510 - Direitos autorais e intelectuais'),
    (2801, u'2801 - Quarentena remunerada'),
    (2901, u'2901 - Empréstimos'),
    (2902, u'2902 - Vestuário e equipamentos'),
    (2920, u'2920 - Reembolsos diversos'),
    (2930, u'2930 - Insuficiência de saldo'),
    (2999, u'2999 - Arredondamentos'),
    (3501, u'3501 - Remuneração por prestação de serviços'),
    (3505, u'3505 - Retiradas (pró-labore) de diretores empregados'),
    (3506, u'3506 - Retiradas (pró-labore) de diretores não empregados'),
    (3508, u'3508 - Retiradas (pró-labore) de proprietários ou sócios'),
    (3509, u'3509 - Honorários a conselheiros'),
    (3520, u'3520 - Remuneração de cooperado'),
    (4010, u'4010 - Complementação salarial de auxílio-doença'),
    (4050, u'4050 - Salário maternidade'),
    (4051, u'4051 - Salário maternidade - 13° salário'),
    (5001, u'5001 - 13º salário'),
    (5005, u'5005 - 13° salário complementar'),
    (5501, u'5501 - Adiantamento de salário'),
    (5504, u'5504 - 13º salário - Adiantamento'),
    (5510, u'5510 - Adiantamento de benefícios previdenciários'),
    (6000, u'6000 - Saldo de salários na rescisão contratual'),
    (6001, u'6001 - 13º salário relativo ao aviso-prévio indenizado'),
    (6002, u'6002 - 13° salário proporcional na rescisão'),
    (6003, u'6003 - Indenização compensatória do aviso-prévio'),
    (6004, u'6004 - Férias - o dobro na rescisão'),
    (6006, u'6006 - Férias proporcionais'),
    (6007, u'6007 - Férias vencidas na rescisão'),
    (6101, u'6101 - Indenização compensatória - multa rescisória 20 ou 40% (CF/88)'),
    (6102, u'6102 - Indenização do art. 9º lei nº 7.238/84'),
    (6103, u'6103 - Indenização do art. 14 da lei nº 5.889, de 8 de junho de 1973'),
    (6104, u'6104 - Indenização do art. 479 da CLT'),
    (6105, u'6105 - Indenização recebida a título de incentivo a demissão'),
    (6106, u'6106 - Multa do art. 477 da CLT'),
    (6107, u'6107 - Indenização por quebra de estabilidade'),
    (6129, u'6129 - Outras Indenizações'),
    (6901, u'6901 - Desconto do aviso-prévio'),
    (6904, u'6904 - Multa prevista no art. 480 da CLT'),
    (7001, u'7001 - Proventos'),
    (7002, u'7002 - Proventos - Pensão por morte Civil'),
    (7003, u'7003 - Proventos - Reserva'),
    (7004, u'7004 - Proventos - Reforma'),
    (7005, u'7005 - Pensão Militar'),
    (9200, u'9200 - Desconto de Adiantamentos'),
    (9201, u'9201 - Contribuição Previdenciária'),
    (9203, u'9203 - Imposto de renda retido na fonte'),
    (9205, u'9205 - Provisão de contribuição previdenciária e IRRF'),
    (9209, u'9209 - Faltas ou atrasos'),
    (9210, u'9210 - DSR s/faltas e atrasos'),
    (9213, u'9213 - Pensão alimentícia'),
    (9214, u'9214 - 13° salário - desconto de adiantamento'),
    (9216, u'9216 - Desconto de vale- transporte'),
    (9217, u'9217 - Contribuição a Outras Entidades e Fundos'),
    (9218, u'9218 - Retenções judiciais'),
    (9219, u'9219 - Desconto de assistência médica ou odontológica'),
    (9220, u'9220 - Alimentação - desconto'),
    (9221, u'9221 - Desconto de férias'),
    (9222, u'9222 - Desconto de outros impostos e contribuições'),
    (9223, u'9223 - Previdência complementar - parte do empregado'),
    (9224, u'9224 - FAPI - parte do empregado'),
    (9225, u'9225 - Previdência complementar - parte do servidor'),
    (9226, u'9226 - Desconto de férias - abono'),
    (9230, u'9230 - Contribuição Sindical - Compulsória'),
    (9231, u'9231 - Contribuição Sindical - Associativa'),
    (9232, u'9232 - Contribuição Sindical - Assistencial'),
    (9233, u'9233 - Contribuição sindical - Confederativa'),
    (9250, u'9250 - Seguro de vida - desconto'),
    (9254, u'9254 - Empréstimos consignados - desconto'),
    (9255, u'9255 - Empréstimos do empregador - desconto'),
    (9258, u'9258 - Convênios'),
    (9270, u'9270 - Danos e prejuízos causados pelo trabalhador'),
    (9290, u'9290 - Desconto de pagamento indevido em meses anteriores'),
    (9299, u'9299 - Outros descontos'),
    (9901, u'9901 - Base de cálculo da contribuição previdenciária'),
    (9902, u'9902 - Total da base de cálculo do FGTS'),
    (9903, u'9903 - Total da base de cálculo do IRRF'),
    (9904, u'9904 - Total da base de cálculo do FGTS rescisório'),
    (9905, u'9905 - Serviço militar'),
    (9906, u'9906 - Remuneração no exterior'),
    (9908, u'9908 - FGTS - depósito'),
    (9910, u'9910 - Seguros'),
    (9911, u'9911 - Assistência Médica'),
    (9930, u'9930 - Salário maternidade pago pela Previdência Social'),
    (9931, u'9931 - 13° salário maternidade pago pela Previdência Social'),
    (9932, u'9932 - Auxílio-doença acidentário'),
    (9933, u'9933 - Auxílio-doença'),
    (9938, u'9938 - Isenção IRRF - 65 anos'),
    (9939, u'9939 - Outros valores tributáveis'),
    (9950, u'9950 - Horas extraordinárias - Banco de horas'),
    (9951, u'9951 - Horas compensadas - Banco de horas'),
    (9989, u'9989 - Outros valores informativos'),
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

class s1010alteracao(models.Model):
    s1010_evttabrubrica = models.OneToOneField('esocial.s1010evtTabRubrica',
        related_name='%(class)s_s1010_evttabrubrica')
    def evento(self): return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dscrubr = models.CharField(max_length=100)
    natrubr = models.IntegerField(choices=CHOICES_S1010_ALTERACAO_NATRUBR)
    tprubr = models.IntegerField(choices=CHOICES_S1010_ALTERACAO_TPRUBR)
    codinccp = models.CharField(choices=CHOICES_S1010_ALTERACAO_CODINCCP, max_length=2)
    codincirrf = models.CharField(choices=CHOICES_S1010_ALTERACAO_CODINCIRRF, max_length=2)
    codincfgts = models.CharField(choices=CHOICES_S1010_ALTERACAO_CODINCFGTS, max_length=2)
    codincsind = models.CharField(choices=CHOICES_S1010_ALTERACAO_CODINCSIND, max_length=2)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_evttabrubrica) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.dscrubr) + ' - ' + unicode(self.natrubr) + ' - ' + unicode(self.tprubr) + ' - ' + unicode(self.codinccp) + ' - ' + unicode(self.codincirrf) + ' - ' + unicode(self.codincfgts) + ' - ' + unicode(self.codincsind) + ' - ' + unicode(self.observacao)
    #s1010_alteracao_custom#
    #s1010_alteracao_custom#
    class Meta:
        db_table = r's1010_alteracao'
        managed = True
        ordering = ['s1010_evttabrubrica', 'codrubr', 'idetabrubr', 'inivalid', 'fimvalid', 'dscrubr', 'natrubr', 'tprubr', 'codinccp', 'codincirrf', 'codincfgts', 'codincsind', 'observacao']


class s1010alteracaoideProcessoCP(models.Model):
    s1010_alteracao = models.ForeignKey('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_ALTERACAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    extdecisao = models.IntegerField(choices=CHOICES_S1010_ALTERACAO_EXTDECISAO)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.extdecisao) + ' - ' + unicode(self.codsusp)
    #s1010_alteracao_ideprocessocp_custom#
    #s1010_alteracao_ideprocessocp_custom#
    class Meta:
        db_table = r's1010_alteracao_ideprocessocp'
        managed = True
        ordering = ['s1010_alteracao', 'tpproc', 'nrproc', 'extdecisao', 'codsusp']


class s1010alteracaoideProcessoFGTS(models.Model):
    s1010_alteracao = models.ForeignKey('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.nrproc)
    #s1010_alteracao_ideprocessofgts_custom#
    #s1010_alteracao_ideprocessofgts_custom#
    class Meta:
        db_table = r's1010_alteracao_ideprocessofgts'
        managed = True
        ordering = ['s1010_alteracao', 'nrproc']


class s1010alteracaoideProcessoIRRF(models.Model):
    s1010_alteracao = models.ForeignKey('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp)
    #s1010_alteracao_ideprocessoirrf_custom#
    #s1010_alteracao_ideprocessoirrf_custom#
    class Meta:
        db_table = r's1010_alteracao_ideprocessoirrf'
        managed = True
        ordering = ['s1010_alteracao', 'nrproc', 'codsusp']


class s1010alteracaoideProcessoSIND(models.Model):
    s1010_alteracao = models.ForeignKey('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.nrproc)
    #s1010_alteracao_ideprocessosind_custom#
    #s1010_alteracao_ideprocessosind_custom#
    class Meta:
        db_table = r's1010_alteracao_ideprocessosind'
        managed = True
        ordering = ['s1010_alteracao', 'nrproc']


class s1010alteracaonovaValidade(models.Model):
    s1010_alteracao = models.OneToOneField('s1010alteracao',
        related_name='%(class)s_s1010_alteracao')
    def evento(self): return self.s1010_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1010_alteracao_novavalidade_custom#
    #s1010_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1010_alteracao_novavalidade'
        managed = True
        ordering = ['s1010_alteracao', 'inivalid', 'fimvalid']


class s1010exclusao(models.Model):
    s1010_evttabrubrica = models.OneToOneField('esocial.s1010evtTabRubrica',
        related_name='%(class)s_s1010_evttabrubrica')
    def evento(self): return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_evttabrubrica) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1010_exclusao_custom#
    #s1010_exclusao_custom#
    class Meta:
        db_table = r's1010_exclusao'
        managed = True
        ordering = ['s1010_evttabrubrica', 'codrubr', 'idetabrubr', 'inivalid', 'fimvalid']


class s1010inclusao(models.Model):
    s1010_evttabrubrica = models.OneToOneField('esocial.s1010evtTabRubrica',
        related_name='%(class)s_s1010_evttabrubrica')
    def evento(self): return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dscrubr = models.CharField(max_length=100)
    natrubr = models.IntegerField(choices=CHOICES_S1010_INCLUSAO_NATRUBR)
    tprubr = models.IntegerField(choices=CHOICES_S1010_INCLUSAO_TPRUBR)
    codinccp = models.CharField(choices=CHOICES_S1010_INCLUSAO_CODINCCP, max_length=2)
    codincirrf = models.CharField(choices=CHOICES_S1010_INCLUSAO_CODINCIRRF, max_length=2)
    codincfgts = models.CharField(choices=CHOICES_S1010_INCLUSAO_CODINCFGTS, max_length=2)
    codincsind = models.CharField(choices=CHOICES_S1010_INCLUSAO_CODINCSIND, max_length=2)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_evttabrubrica) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.dscrubr) + ' - ' + unicode(self.natrubr) + ' - ' + unicode(self.tprubr) + ' - ' + unicode(self.codinccp) + ' - ' + unicode(self.codincirrf) + ' - ' + unicode(self.codincfgts) + ' - ' + unicode(self.codincsind) + ' - ' + unicode(self.observacao)
    #s1010_inclusao_custom#
    #s1010_inclusao_custom#
    class Meta:
        db_table = r's1010_inclusao'
        managed = True
        ordering = ['s1010_evttabrubrica', 'codrubr', 'idetabrubr', 'inivalid', 'fimvalid', 'dscrubr', 'natrubr', 'tprubr', 'codinccp', 'codincirrf', 'codincfgts', 'codincsind', 'observacao']


class s1010inclusaoideProcessoCP(models.Model):
    s1010_inclusao = models.ForeignKey('s1010inclusao',
        related_name='%(class)s_s1010_inclusao')
    def evento(self): return self.s1010_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_INCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    extdecisao = models.IntegerField(choices=CHOICES_S1010_INCLUSAO_EXTDECISAO)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_inclusao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.extdecisao) + ' - ' + unicode(self.codsusp)
    #s1010_inclusao_ideprocessocp_custom#
    #s1010_inclusao_ideprocessocp_custom#
    class Meta:
        db_table = r's1010_inclusao_ideprocessocp'
        managed = True
        ordering = ['s1010_inclusao', 'tpproc', 'nrproc', 'extdecisao', 'codsusp']


class s1010inclusaoideProcessoFGTS(models.Model):
    s1010_inclusao = models.ForeignKey('s1010inclusao',
        related_name='%(class)s_s1010_inclusao')
    def evento(self): return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_inclusao) + ' - ' + unicode(self.nrproc)
    #s1010_inclusao_ideprocessofgts_custom#
    #s1010_inclusao_ideprocessofgts_custom#
    class Meta:
        db_table = r's1010_inclusao_ideprocessofgts'
        managed = True
        ordering = ['s1010_inclusao', 'nrproc']


class s1010inclusaoideProcessoIRRF(models.Model):
    s1010_inclusao = models.ForeignKey('s1010inclusao',
        related_name='%(class)s_s1010_inclusao')
    def evento(self): return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_inclusao) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp)
    #s1010_inclusao_ideprocessoirrf_custom#
    #s1010_inclusao_ideprocessoirrf_custom#
    class Meta:
        db_table = r's1010_inclusao_ideprocessoirrf'
        managed = True
        ordering = ['s1010_inclusao', 'nrproc', 'codsusp']


class s1010inclusaoideProcessoSIND(models.Model):
    s1010_inclusao = models.ForeignKey('s1010inclusao',
        related_name='%(class)s_s1010_inclusao')
    def evento(self): return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1010_inclusao) + ' - ' + unicode(self.nrproc)
    #s1010_inclusao_ideprocessosind_custom#
    #s1010_inclusao_ideprocessosind_custom#
    class Meta:
        db_table = r's1010_inclusao_ideprocessosind'
        managed = True
        ordering = ['s1010_inclusao', 'nrproc']


#VIEWS_MODELS
