#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



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

CHOICES_S2400_ALTBENEFICIO_TPBENEF = (
    (1, u'1 - Aposentadoria Voluntária por Idade e Tempo de Contribuição - Proventos Integrais: Art. 40, § 1º, III “a” da CF, Redação EC 20/98'),
    (10, u'10 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c LC 152/2015'),
    (11, u'11 - Aposentadoria - Magistrado, Membro do MP e TC - Proventos Integrais correspondentes à última remuneração: Regra de Transição do Art. 8º, da EC 20/98'),
    (12, u'12 - Aposentadoria - Proventos Integrais correspondentes à última remuneração - Regra de Transição do Art. 8º, da EC 20/98: Geral'),
    (13, u'13 - Aposentadoria Especial do Professor - Regra de Transição do Art. 8º, da EC 20/98: Proventos Integrais correspondentes à última remuneração.'),
    (14, u'14 - Aposentadoria com proventos proporcionais calculados sobre a última remuneraçãoRegra de Transição do Art. 8º, da EC20/98 - Geral'),
    (15, u'15 - Aposentadoria - Regra de Transição do Art. 3º, da EC 47/05: Proventos Integrais correspondentes à última remuneração'),
    (16, u'16 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (17, u'17 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (18, u'18 - Aposentadoria Magistrado, Membro do MP e TC (homem) - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (19, u'19 - Aposentadoria Magistrado, Membro do MP e TC - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (2, u'2 - Aposentadoria por Idade - Proventos proporcionais: Art. 40, III, c da CF redação original - Anterior à EC 20/1998'),
    (20, u'20 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média com redutor - Geral (Implementação a partir de 01/01/2006)'),
    (21, u'21 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média reduzida - Geral (Implementação até 31/12/2005)'),
    (22, u'22 - Aposentadoria Voluntária - Regra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes á ultima remuneração do cargo - Geral'),
    (23, u'23 - Aposentadoria Voluntária Professor Educação infantil, ensino fundamental e médioRegra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes à última remuneração do cargo'),
    (24, u'24 - Aposentadoria Voluntária por Idade - Proventos Proporcionais calculados sobre a última remuneração do cargo: Art. 40, § 1º, Inciso III, alínea "b'),
    (25, u'25 - Aposentadoria Voluntária por Idade - Proventos pela Média proporcionais - Art. 40, § 1º, Inciso III, alínea "b'),
    (26, u'26 - Aposentadoria Voluntária por Idade e por Tempo de Contribuição - Proventos pela Média: Art. 40, § 1º, Inciso III, aliena "a", CF, Redação EC 41/03'),
    (27, u'27 - Aposentadoria Voluntária por Tempo de Contribuição - Especial do professor de q/q nível de ensino - Art. 40, III, alínea b, da CF- Red. Original até EC 20/1998'),
    (28, u'28 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial do professor ed. infantil, ensino fundamental e médio - Art. 40, § 1º, Inciso III, alínea a, c/c § 5º da CF red. da EC 20/1998 )'),
    (29, u'29 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial de Professor - Proventos pela Média: Art. 40, § 1º, Inciso III, alínea "a", C/C § 5º da CF, Redação EC 41/2003'),
    (3, u'3 - Aposentadoria por Invalidez - Proventos integrais ou proporcionais: Art. 40, I da CF redação original - anterior à EC 20/1998'),
    (30, u'30 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas com base na última remuneração do cargo) - Art. 40, Inciso I, Redação Original, CF'),
    (31, u'31 - Aposentadoria por Invalidez (proporcionais ou integrais , calculadas com base na última remuneração do cargo) - Art. 40, § 1º, Inciso I da CF com Redação da EC 20/1998'),
    (32, u'32 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas pela média) - Art. 40, § 1º, Inciso I da CF com Redação da EC 41/2003'),
    (33, u'33 - Aposentadoria por Invalidez (proporcionais ou integrais calculadas com base na última remuneração do cargo) - Art. 40 º 1º, Inciso I da CF C/C combinado com Art. 6ª- A da EC 70/2012'),
    (34, u'34 - Reforma por invalidez'),
    (35, u'35 - Reserva Remunerada Compulsória'),
    (36, u'36 - Reserva Remunerada Integral'),
    (37, u'37 - Reserva Remunerada Proporcional'),
    (38, u'38 - Auxílio Doença - Conforme lei do Ente'),
    (39, u'39 - Auxílio Reclusão - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (4, u'4 - Aposentadoria Compulsória - Proventos proporcionais: Art. 40, II da CF redação original, anterior à EC 20/1998 *'),
    (40, u'40 - Pensão por Morte'),
    (41, u'41 - Salário Família - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (42, u'42 - Salário Maternidade - Art. 7º, XVIII c/c art. 39, § 3º da Constituição Federal'),
    (43, u'43 - Complementação de Aposentadoria do Regime Geral de Previdência Social (RGPS)'),
    (44, u'44 - Complementação de Pensão por Morte do Regime Geral de Previdência Social (RGPS)'),
    (5, u'5 - Aposentadoria por Tempo de Serviço Integral - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (6, u'6 - Aposentadoria por Tempo de Serviço Proporcional - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (7, u'7 - Aposentadoria Compulsória Proporcional calculada sobre a última remuneração- Art. 40, § 1º, Inciso II da CF, Redação EC 20/1998'),
    (8, u'8 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03'),
    (9, u'9 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c EC 88/2015'),
    (91, u'91 - Aposentadoria sem paridade concedida antes do início de vigência do eSocial'),
    (92, u'92 - Aposentadoria com paridade concedida antes do início de vigência do eSocial'),
    (93, u'93 - Aposentadoria por invalidez com paridade concedida antes do início de vigência do eSocial'),
    (94, u'94 - Aposentadoria por invalidez sem paridade concedida antes do início de vigência do eSocial'),
    (95, u'95 - Transferência para reserva concedida antes do início de vigência do eSocial'),
    (96, u'96 - Reforma concedida antes do início de vigência do eSocial'),
    (97, u'97 - Pensão por morte com paridade concedida antes do início de vigência do eSocial'),
    (98, u'98 - Pensão por morte sem paridade concedida antes do início de vigência do eSocial'),
    (99, u'99 - Outros Benefícios previdenciários concedidos antes do início de vigência do eSocial'),
)

CHOICES_S2400_FIMBENEFICIO_MTVFIM = (
    (1, u'1 - Aposentadoria Voluntária por Idade e Tempo de Contribuição - Proventos Integrais: Art. 40, § 1º, III “a” da CF, Redação EC 20/98'),
    (10, u'10 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c LC 152/2015'),
    (11, u'11 - Aposentadoria - Magistrado, Membro do MP e TC - Proventos Integrais correspondentes à última remuneração: Regra de Transição do Art. 8º, da EC 20/98'),
    (12, u'12 - Aposentadoria - Proventos Integrais correspondentes à última remuneração - Regra de Transição do Art. 8º, da EC 20/98: Geral'),
    (13, u'13 - Aposentadoria Especial do Professor - Regra de Transição do Art. 8º, da EC 20/98: Proventos Integrais correspondentes à última remuneração.'),
    (14, u'14 - Aposentadoria com proventos proporcionais calculados sobre a última remuneraçãoRegra de Transição do Art. 8º, da EC20/98 - Geral'),
    (15, u'15 - Aposentadoria - Regra de Transição do Art. 3º, da EC 47/05: Proventos Integrais correspondentes à última remuneração'),
    (16, u'16 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (17, u'17 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (18, u'18 - Aposentadoria Magistrado, Membro do MP e TC (homem) - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (19, u'19 - Aposentadoria Magistrado, Membro do MP e TC - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (2, u'2 - Aposentadoria por Idade - Proventos proporcionais: Art. 40, III, c da CF redação original - Anterior à EC 20/1998'),
    (20, u'20 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média com redutor - Geral (Implementação a partir de 01/01/2006)'),
    (21, u'21 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média reduzida - Geral (Implementação até 31/12/2005)'),
    (22, u'22 - Aposentadoria Voluntária - Regra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes á ultima remuneração do cargo - Geral'),
    (23, u'23 - Aposentadoria Voluntária Professor Educação infantil, ensino fundamental e médioRegra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes à última remuneração do cargo'),
    (24, u'24 - Aposentadoria Voluntária por Idade - Proventos Proporcionais calculados sobre a última remuneração do cargo: Art. 40, § 1º, Inciso III, alínea "b'),
    (25, u'25 - Aposentadoria Voluntária por Idade - Proventos pela Média proporcionais - Art. 40, § 1º, Inciso III, alínea "b'),
    (26, u'26 - Aposentadoria Voluntária por Idade e por Tempo de Contribuição - Proventos pela Média: Art. 40, § 1º, Inciso III, aliena "a", CF, Redação EC 41/03'),
    (27, u'27 - Aposentadoria Voluntária por Tempo de Contribuição - Especial do professor de q/q nível de ensino - Art. 40, III, alínea b, da CF- Red. Original até EC 20/1998'),
    (28, u'28 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial do professor ed. infantil, ensino fundamental e médio - Art. 40, § 1º, Inciso III, alínea a, c/c § 5º da CF red. da EC 20/1998 )'),
    (29, u'29 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial de Professor - Proventos pela Média: Art. 40, § 1º, Inciso III, alínea "a", C/C § 5º da CF, Redação EC 41/2003'),
    (3, u'3 - Aposentadoria por Invalidez - Proventos integrais ou proporcionais: Art. 40, I da CF redação original - anterior à EC 20/1998'),
    (30, u'30 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas com base na última remuneração do cargo) - Art. 40, Inciso I, Redação Original, CF'),
    (31, u'31 - Aposentadoria por Invalidez (proporcionais ou integrais , calculadas com base na última remuneração do cargo) - Art. 40, § 1º, Inciso I da CF com Redação da EC 20/1998'),
    (32, u'32 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas pela média) - Art. 40, § 1º, Inciso I da CF com Redação da EC 41/2003'),
    (33, u'33 - Aposentadoria por Invalidez (proporcionais ou integrais calculadas com base na última remuneração do cargo) - Art. 40 º 1º, Inciso I da CF C/C combinado com Art. 6ª- A da EC 70/2012'),
    (34, u'34 - Reforma por invalidez'),
    (35, u'35 - Reserva Remunerada Compulsória'),
    (36, u'36 - Reserva Remunerada Integral'),
    (37, u'37 - Reserva Remunerada Proporcional'),
    (38, u'38 - Auxílio Doença - Conforme lei do Ente'),
    (39, u'39 - Auxílio Reclusão - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (4, u'4 - Aposentadoria Compulsória - Proventos proporcionais: Art. 40, II da CF redação original, anterior à EC 20/1998 *'),
    (40, u'40 - Pensão por Morte'),
    (41, u'41 - Salário Família - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (42, u'42 - Salário Maternidade - Art. 7º, XVIII c/c art. 39, § 3º da Constituição Federal'),
    (43, u'43 - Complementação de Aposentadoria do Regime Geral de Previdência Social (RGPS)'),
    (44, u'44 - Complementação de Pensão por Morte do Regime Geral de Previdência Social (RGPS)'),
    (5, u'5 - Aposentadoria por Tempo de Serviço Integral - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (6, u'6 - Aposentadoria por Tempo de Serviço Proporcional - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (7, u'7 - Aposentadoria Compulsória Proporcional calculada sobre a última remuneração- Art. 40, § 1º, Inciso II da CF, Redação EC 20/1998'),
    (8, u'8 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03'),
    (9, u'9 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c EC 88/2015'),
    (91, u'91 - Aposentadoria sem paridade concedida antes do início de vigência do eSocial'),
    (92, u'92 - Aposentadoria com paridade concedida antes do início de vigência do eSocial'),
    (93, u'93 - Aposentadoria por invalidez com paridade concedida antes do início de vigência do eSocial'),
    (94, u'94 - Aposentadoria por invalidez sem paridade concedida antes do início de vigência do eSocial'),
    (95, u'95 - Transferência para reserva concedida antes do início de vigência do eSocial'),
    (96, u'96 - Reforma concedida antes do início de vigência do eSocial'),
    (97, u'97 - Pensão por morte com paridade concedida antes do início de vigência do eSocial'),
    (98, u'98 - Pensão por morte sem paridade concedida antes do início de vigência do eSocial'),
    (99, u'99 - Outros Benefícios previdenciários concedidos antes do início de vigência do eSocial'),
)

CHOICES_S2400_FIMBENEFICIO_TPBENEF = (
    (1, u'1 - Aposentadoria Voluntária por Idade e Tempo de Contribuição - Proventos Integrais: Art. 40, § 1º, III “a” da CF, Redação EC 20/98'),
    (10, u'10 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c LC 152/2015'),
    (11, u'11 - Aposentadoria - Magistrado, Membro do MP e TC - Proventos Integrais correspondentes à última remuneração: Regra de Transição do Art. 8º, da EC 20/98'),
    (12, u'12 - Aposentadoria - Proventos Integrais correspondentes à última remuneração - Regra de Transição do Art. 8º, da EC 20/98: Geral'),
    (13, u'13 - Aposentadoria Especial do Professor - Regra de Transição do Art. 8º, da EC 20/98: Proventos Integrais correspondentes à última remuneração.'),
    (14, u'14 - Aposentadoria com proventos proporcionais calculados sobre a última remuneraçãoRegra de Transição do Art. 8º, da EC20/98 - Geral'),
    (15, u'15 - Aposentadoria - Regra de Transição do Art. 3º, da EC 47/05: Proventos Integrais correspondentes à última remuneração'),
    (16, u'16 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (17, u'17 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (18, u'18 - Aposentadoria Magistrado, Membro do MP e TC (homem) - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (19, u'19 - Aposentadoria Magistrado, Membro do MP e TC - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (2, u'2 - Aposentadoria por Idade - Proventos proporcionais: Art. 40, III, c da CF redação original - Anterior à EC 20/1998'),
    (20, u'20 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média com redutor - Geral (Implementação a partir de 01/01/2006)'),
    (21, u'21 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média reduzida - Geral (Implementação até 31/12/2005)'),
    (22, u'22 - Aposentadoria Voluntária - Regra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes á ultima remuneração do cargo - Geral'),
    (23, u'23 - Aposentadoria Voluntária Professor Educação infantil, ensino fundamental e médioRegra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes à última remuneração do cargo'),
    (24, u'24 - Aposentadoria Voluntária por Idade - Proventos Proporcionais calculados sobre a última remuneração do cargo: Art. 40, § 1º, Inciso III, alínea "b'),
    (25, u'25 - Aposentadoria Voluntária por Idade - Proventos pela Média proporcionais - Art. 40, § 1º, Inciso III, alínea "b'),
    (26, u'26 - Aposentadoria Voluntária por Idade e por Tempo de Contribuição - Proventos pela Média: Art. 40, § 1º, Inciso III, aliena "a", CF, Redação EC 41/03'),
    (27, u'27 - Aposentadoria Voluntária por Tempo de Contribuição - Especial do professor de q/q nível de ensino - Art. 40, III, alínea b, da CF- Red. Original até EC 20/1998'),
    (28, u'28 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial do professor ed. infantil, ensino fundamental e médio - Art. 40, § 1º, Inciso III, alínea a, c/c § 5º da CF red. da EC 20/1998 )'),
    (29, u'29 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial de Professor - Proventos pela Média: Art. 40, § 1º, Inciso III, alínea "a", C/C § 5º da CF, Redação EC 41/2003'),
    (3, u'3 - Aposentadoria por Invalidez - Proventos integrais ou proporcionais: Art. 40, I da CF redação original - anterior à EC 20/1998'),
    (30, u'30 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas com base na última remuneração do cargo) - Art. 40, Inciso I, Redação Original, CF'),
    (31, u'31 - Aposentadoria por Invalidez (proporcionais ou integrais , calculadas com base na última remuneração do cargo) - Art. 40, § 1º, Inciso I da CF com Redação da EC 20/1998'),
    (32, u'32 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas pela média) - Art. 40, § 1º, Inciso I da CF com Redação da EC 41/2003'),
    (33, u'33 - Aposentadoria por Invalidez (proporcionais ou integrais calculadas com base na última remuneração do cargo) - Art. 40 º 1º, Inciso I da CF C/C combinado com Art. 6ª- A da EC 70/2012'),
    (34, u'34 - Reforma por invalidez'),
    (35, u'35 - Reserva Remunerada Compulsória'),
    (36, u'36 - Reserva Remunerada Integral'),
    (37, u'37 - Reserva Remunerada Proporcional'),
    (38, u'38 - Auxílio Doença - Conforme lei do Ente'),
    (39, u'39 - Auxílio Reclusão - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (4, u'4 - Aposentadoria Compulsória - Proventos proporcionais: Art. 40, II da CF redação original, anterior à EC 20/1998 *'),
    (40, u'40 - Pensão por Morte'),
    (41, u'41 - Salário Família - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (42, u'42 - Salário Maternidade - Art. 7º, XVIII c/c art. 39, § 3º da Constituição Federal'),
    (43, u'43 - Complementação de Aposentadoria do Regime Geral de Previdência Social (RGPS)'),
    (44, u'44 - Complementação de Pensão por Morte do Regime Geral de Previdência Social (RGPS)'),
    (5, u'5 - Aposentadoria por Tempo de Serviço Integral - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (6, u'6 - Aposentadoria por Tempo de Serviço Proporcional - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (7, u'7 - Aposentadoria Compulsória Proporcional calculada sobre a última remuneração- Art. 40, § 1º, Inciso II da CF, Redação EC 20/1998'),
    (8, u'8 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03'),
    (9, u'9 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c EC 88/2015'),
    (91, u'91 - Aposentadoria sem paridade concedida antes do início de vigência do eSocial'),
    (92, u'92 - Aposentadoria com paridade concedida antes do início de vigência do eSocial'),
    (93, u'93 - Aposentadoria por invalidez com paridade concedida antes do início de vigência do eSocial'),
    (94, u'94 - Aposentadoria por invalidez sem paridade concedida antes do início de vigência do eSocial'),
    (95, u'95 - Transferência para reserva concedida antes do início de vigência do eSocial'),
    (96, u'96 - Reforma concedida antes do início de vigência do eSocial'),
    (97, u'97 - Pensão por morte com paridade concedida antes do início de vigência do eSocial'),
    (98, u'98 - Pensão por morte sem paridade concedida antes do início de vigência do eSocial'),
    (99, u'99 - Outros Benefícios previdenciários concedidos antes do início de vigência do eSocial'),
)

CHOICES_S2400_INIBENEFICIO_TPBENEF = (
    (1, u'1 - Aposentadoria Voluntária por Idade e Tempo de Contribuição - Proventos Integrais: Art. 40, § 1º, III “a” da CF, Redação EC 20/98'),
    (10, u'10 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c LC 152/2015'),
    (11, u'11 - Aposentadoria - Magistrado, Membro do MP e TC - Proventos Integrais correspondentes à última remuneração: Regra de Transição do Art. 8º, da EC 20/98'),
    (12, u'12 - Aposentadoria - Proventos Integrais correspondentes à última remuneração - Regra de Transição do Art. 8º, da EC 20/98: Geral'),
    (13, u'13 - Aposentadoria Especial do Professor - Regra de Transição do Art. 8º, da EC 20/98: Proventos Integrais correspondentes à última remuneração.'),
    (14, u'14 - Aposentadoria com proventos proporcionais calculados sobre a última remuneraçãoRegra de Transição do Art. 8º, da EC20/98 - Geral'),
    (15, u'15 - Aposentadoria - Regra de Transição do Art. 3º, da EC 47/05: Proventos Integrais correspondentes à última remuneração'),
    (16, u'16 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (17, u'17 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (18, u'18 - Aposentadoria Magistrado, Membro do MP e TC (homem) - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (19, u'19 - Aposentadoria Magistrado, Membro do MP e TC - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (2, u'2 - Aposentadoria por Idade - Proventos proporcionais: Art. 40, III, c da CF redação original - Anterior à EC 20/1998'),
    (20, u'20 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média com redutor - Geral (Implementação a partir de 01/01/2006)'),
    (21, u'21 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média reduzida - Geral (Implementação até 31/12/2005)'),
    (22, u'22 - Aposentadoria Voluntária - Regra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes á ultima remuneração do cargo - Geral'),
    (23, u'23 - Aposentadoria Voluntária Professor Educação infantil, ensino fundamental e médioRegra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes à última remuneração do cargo'),
    (24, u'24 - Aposentadoria Voluntária por Idade - Proventos Proporcionais calculados sobre a última remuneração do cargo: Art. 40, § 1º, Inciso III, alínea "b'),
    (25, u'25 - Aposentadoria Voluntária por Idade - Proventos pela Média proporcionais - Art. 40, § 1º, Inciso III, alínea "b'),
    (26, u'26 - Aposentadoria Voluntária por Idade e por Tempo de Contribuição - Proventos pela Média: Art. 40, § 1º, Inciso III, aliena "a", CF, Redação EC 41/03'),
    (27, u'27 - Aposentadoria Voluntária por Tempo de Contribuição - Especial do professor de q/q nível de ensino - Art. 40, III, alínea b, da CF- Red. Original até EC 20/1998'),
    (28, u'28 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial do professor ed. infantil, ensino fundamental e médio - Art. 40, § 1º, Inciso III, alínea a, c/c § 5º da CF red. da EC 20/1998 )'),
    (29, u'29 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial de Professor - Proventos pela Média: Art. 40, § 1º, Inciso III, alínea "a", C/C § 5º da CF, Redação EC 41/2003'),
    (3, u'3 - Aposentadoria por Invalidez - Proventos integrais ou proporcionais: Art. 40, I da CF redação original - anterior à EC 20/1998'),
    (30, u'30 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas com base na última remuneração do cargo) - Art. 40, Inciso I, Redação Original, CF'),
    (31, u'31 - Aposentadoria por Invalidez (proporcionais ou integrais , calculadas com base na última remuneração do cargo) - Art. 40, § 1º, Inciso I da CF com Redação da EC 20/1998'),
    (32, u'32 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas pela média) - Art. 40, § 1º, Inciso I da CF com Redação da EC 41/2003'),
    (33, u'33 - Aposentadoria por Invalidez (proporcionais ou integrais calculadas com base na última remuneração do cargo) - Art. 40 º 1º, Inciso I da CF C/C combinado com Art. 6ª- A da EC 70/2012'),
    (34, u'34 - Reforma por invalidez'),
    (35, u'35 - Reserva Remunerada Compulsória'),
    (36, u'36 - Reserva Remunerada Integral'),
    (37, u'37 - Reserva Remunerada Proporcional'),
    (38, u'38 - Auxílio Doença - Conforme lei do Ente'),
    (39, u'39 - Auxílio Reclusão - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (4, u'4 - Aposentadoria Compulsória - Proventos proporcionais: Art. 40, II da CF redação original, anterior à EC 20/1998 *'),
    (40, u'40 - Pensão por Morte'),
    (41, u'41 - Salário Família - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (42, u'42 - Salário Maternidade - Art. 7º, XVIII c/c art. 39, § 3º da Constituição Federal'),
    (43, u'43 - Complementação de Aposentadoria do Regime Geral de Previdência Social (RGPS)'),
    (44, u'44 - Complementação de Pensão por Morte do Regime Geral de Previdência Social (RGPS)'),
    (5, u'5 - Aposentadoria por Tempo de Serviço Integral - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (6, u'6 - Aposentadoria por Tempo de Serviço Proporcional - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (7, u'7 - Aposentadoria Compulsória Proporcional calculada sobre a última remuneração- Art. 40, § 1º, Inciso II da CF, Redação EC 20/1998'),
    (8, u'8 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03'),
    (9, u'9 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c EC 88/2015'),
    (91, u'91 - Aposentadoria sem paridade concedida antes do início de vigência do eSocial'),
    (92, u'92 - Aposentadoria com paridade concedida antes do início de vigência do eSocial'),
    (93, u'93 - Aposentadoria por invalidez com paridade concedida antes do início de vigência do eSocial'),
    (94, u'94 - Aposentadoria por invalidez sem paridade concedida antes do início de vigência do eSocial'),
    (95, u'95 - Transferência para reserva concedida antes do início de vigência do eSocial'),
    (96, u'96 - Reforma concedida antes do início de vigência do eSocial'),
    (97, u'97 - Pensão por morte com paridade concedida antes do início de vigência do eSocial'),
    (98, u'98 - Pensão por morte sem paridade concedida antes do início de vigência do eSocial'),
    (99, u'99 - Outros Benefícios previdenciários concedidos antes do início de vigência do eSocial'),
)

CHOICES_S2400_PAISRESID = (
    ('008', u'008 - Abu Dhabi'),
    ('009', u'009 - Dirce'),
    ('013', u'013 - Afeganistao'),
    ('017', u'017 - Albania, Republica Da'),
    ('020', u'020 - Alboran-Perejil,Ilhas'),
    ('023', u'023 - Alemanha'),
    ('025', u'025 - Alemanha, Republica Democratica'),
    ('031', u'031 - Burkina Faso'),
    ('037', u'037 - Andorra'),
    ('040', u'040 - Angola'),
    ('041', u'041 - Anguilla'),
    ('043', u'043 - Antigua E Barbuda'),
    ('047', u'047 - Antilhas Holandesas'),
    ('053', u'053 - Arabia Saudita'),
    ('059', u'059 - Argelia'),
    ('063', u'063 - Argentina'),
    ('064', u'064 - Armenia, Republica Da'),
    ('065', u'065 - Aruba'),
    ('069', u'069 - Australia'),
    ('072', u'072 - Austria'),
    ('073', u'073 - Azerbaijao, Republica Do'),
    ('077', u'077 - Bahamas, Ilhas'),
    ('080', u'080 - Bahrein, Ilhas'),
    ('081', u'081 - Bangladesh'),
    ('083', u'083 - Barbados'),
    ('085', u'085 - Belarus, Republica Da'),
    ('087', u'087 - Belgica'),
    ('088', u'088 - Belize'),
    ('090', u'090 - Bermudas'),
    ('093', u'093 - Mianmar (BIRMANIA)'),
    ('097', u'097 - Bolivia, Estado Plurinacional Da'),
    ('098', u'098 - Bosnia-Herzegovina (REPUBLICA Da)'),
    ('100', u'100 - Int.Z.F.Manaus'),
    ('101', u'101 - Botsuana'),
    ('105', u'105 - Brasil'),
    ('106', u'106 - Fretado P/Brasil'),
    ('108', u'108 - Brunei'),
    ('111', u'111 - Bulgaria, Republica Da'),
    ('115', u'115 - Burundi'),
    ('119', u'119 - Butao'),
    ('127', u'127 - Cabo Verde, Republica De'),
    ('131', u'131 - Cachemira'),
    ('137', u'137 - Cayman, Ilhas'),
    ('141', u'141 - Camboja'),
    ('145', u'145 - Camaroes'),
    ('149', u'149 - Canada'),
    ('150', u'150 - Jersey, Ilha Do Canal'),
    ('151', u'151 - Canarias, Ilhas'),
    ('152', u'152 - Canal,Ilhas'),
    ('153', u'153 - Cazaquistao, Republica Do'),
    ('154', u'154 - Catar'),
    ('158', u'158 - Chile'),
    ('160', u'160 - China, Republica Popular'),
    ('161', u'161 - Formosa (TAIWAN)'),
    ('163', u'163 - Chipre'),
    ('165', u'165 - Cocos(Keeling),Ilhas'),
    ('169', u'169 - Colombia'),
    ('173', u'173 - Comores, Ilhas'),
    ('177', u'177 - Congo'),
    ('183', u'183 - Cook, Ilhas'),
    ('187', u'187 - Coreia (DO Norte), Rep.Pop.Democratica'),
    ('190', u'190 - Coreia (DO Sul), Republica Da'),
    ('193', u'193 - Costa Do Marfim'),
    ('195', u'195 - Croacia (REPUBLICA Da)'),
    ('196', u'196 - Costa Rica'),
    ('198', u'198 - Coveite'),
    ('199', u'199 - Cuba'),
    ('229', u'229 - Benin'),
    ('232', u'232 - Dinamarca'),
    ('235', u'235 - Dominica,Ilha'),
    ('237', u'237 - Dubai'),
    ('239', u'239 - Equador'),
    ('240', u'240 - Egito'),
    ('243', u'243 - Eritreia'),
    ('244', u'244 - Emirados Arabes Unidos'),
    ('245', u'245 - Espanha'),
    ('246', u'246 - Eslovenia, Republica Da'),
    ('247', u'247 - Eslovaca, Republica'),
    ('249', u'249 - Estados Unidos'),
    ('251', u'251 - Estonia, Republica Da'),
    ('253', u'253 - Etiopia'),
    ('255', u'255 - Falkland (ILHAS Malvinas)'),
    ('259', u'259 - Feroe, Ilhas'),
    ('263', u'263 - Fezzan'),
    ('267', u'267 - Filipinas'),
    ('271', u'271 - Finlandia'),
    ('275', u'275 - Franca'),
    ('281', u'281 - Gabao'),
    ('285', u'285 - Gambia'),
    ('289', u'289 - Gana'),
    ('291', u'291 - Georgia, Republica Da'),
    ('293', u'293 - Gibraltar'),
    ('297', u'297 - Granada'),
    ('301', u'301 - Grecia'),
    ('305', u'305 - Groenlandia'),
    ('309', u'309 - Guadalupe'),
    ('313', u'313 - Guam'),
    ('317', u'317 - Guatemala'),
    ('325', u'325 - Guiana Francesa'),
    ('329', u'329 - Guine'),
    ('331', u'331 - Guine-Equatorial'),
    ('334', u'334 - Guine-Bissau'),
    ('337', u'337 - Guiana'),
    ('341', u'341 - Haiti'),
    ('345', u'345 - Honduras'),
    ('351', u'351 - Hong Kong'),
    ('355', u'355 - Hungria, Republica Da'),
    ('357', u'357 - Iemen'),
    ('358', u'358 - Iemem Do Sul'),
    ('359', u'359 - Man, Ilha De'),
    ('361', u'361 - India'),
    ('365', u'365 - Indonesia'),
    ('367', u'367 - Inglaterra'),
    ('369', u'369 - Iraque'),
    ('372', u'372 - Ira, Republica Islamica Do'),
    ('375', u'375 - Irlanda'),
    ('379', u'379 - Islandia'),
    ('383', u'383 - Israel'),
    ('386', u'386 - Italia'),
    ('388', u'388 - Servia E Montenegro'),
    ('391', u'391 - Jamaica'),
    ('395', u'395 - Jammu'),
    ('396', u'396 - Johnston, Ilhas'),
    ('399', u'399 - Japao'),
    ('403', u'403 - Jordania'),
    ('411', u'411 - Kiribati'),
    ('420', u'420 - Laos, Rep.Pop.Democr.Do'),
    ('423', u'423 - Lebuan,Ilhas'),
    ('426', u'426 - Lesoto'),
    ('427', u'427 - Letonia, Republica Da'),
    ('431', u'431 - Libano'),
    ('434', u'434 - Liberia'),
    ('438', u'438 - Libia'),
    ('440', u'440 - Liechtenstein'),
    ('442', u'442 - Lituania, Republica Da'),
    ('445', u'445 - Luxemburgo'),
    ('447', u'447 - Macau'),
    ('449', u'449 - Macedonia, Ant.Rep.Iugoslava'),
    ('450', u'450 - Madagascar'),
    ('452', u'452 - Ilha Da Madeira'),
    ('455', u'455 - Malasia'),
    ('458', u'458 - Malavi'),
    ('461', u'461 - Maldivas'),
    ('464', u'464 - Mali'),
    ('467', u'467 - Malta'),
    ('472', u'472 - Marianas Do Norte'),
    ('474', u'474 - Marrocos'),
    ('476', u'476 - Marshall,Ilhas'),
    ('477', u'477 - Martinica'),
    ('485', u'485 - Mauricio'),
    ('488', u'488 - Mauritania'),
    ('490', u'490 - Midway, Ilhas'),
    ('493', u'493 - Mexico'),
    ('494', u'494 - Moldavia, Republica Da'),
    ('495', u'495 - Monaco'),
    ('497', u'497 - Mongolia'),
    ('499', u'499 - Micronesia'),
    ('501', u'501 - Montserrat,Ilhas'),
    ('505', u'505 - Mocambique'),
    ('507', u'507 - Namibia'),
    ('508', u'508 - Nauru'),
    ('511', u'511 - Christmas,Ilha (NAVIDAD)'),
    ('517', u'517 - Nepal'),
    ('521', u'521 - Nicaragua'),
    ('525', u'525 - Niger'),
    ('528', u'528 - Nigeria'),
    ('531', u'531 - Niue,Ilha'),
    ('535', u'535 - Norfolk,Ilha'),
    ('538', u'538 - Noruega'),
    ('542', u'542 - Nova Caledonia'),
    ('545', u'545 - Papua Nova Guine'),
    ('548', u'548 - Nova Zelandia'),
    ('551', u'551 - Vanuatu'),
    ('556', u'556 - Oma'),
    ('563', u'563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'),
    ('566', u'566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'),
    ('569', u'569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'),
    ('573', u'573 - Paises Baixos (HOLANDA)'),
    ('575', u'575 - Palau'),
    ('576', u'576 - Paquistao'),
    ('578', u'578 - Palestina'),
    ('580', u'580 - Panama'),
    ('583', u'583 - Papua Nova Guiné'),
    ('586', u'586 - Paraguai'),
    ('589', u'589 - Peru'),
    ('593', u'593 - Pitcairn,Ilha'),
    ('599', u'599 - Polinesia Francesa'),
    ('603', u'603 - Polonia, Republica Da'),
    ('607', u'607 - Portugal'),
    ('611', u'611 - Porto Rico'),
    ('623', u'623 - Quenia'),
    ('625', u'625 - Quirguiz, Republica'),
    ('628', u'628 - Reino Unido'),
    ('640', u'640 - Republica Centro-Africana'),
    ('647', u'647 - Republica Dominicana'),
    ('660', u'660 - Reuniao, Ilha'),
    ('665', u'665 - Zimbabue'),
    ('670', u'670 - Romenia'),
    ('675', u'675 - Ruanda'),
    ('676', u'676 - Russia, Federacao Da'),
    ('677', u'677 - Salomao, Ilhas'),
    ('678', u'678 - Saint Kitts E Nevis'),
    ('685', u'685 - Saara Ocidental'),
    ('687', u'687 - El Salvador'),
    ('690', u'690 - Samoa'),
    ('691', u'691 - Samoa Americana'),
    ('695', u'695 - Sao Cristovao E Neves,Ilhas'),
    ('697', u'697 - San Marino'),
    ('700', u'700 - Sao Pedro E Miquelon'),
    ('705', u'705 - Sao Vicente E Granadinas'),
    ('710', u'710 - Santa Helena'),
    ('715', u'715 - Santa Lucia'),
    ('720', u'720 - Sao Tome E Principe, Ilhas'),
    ('728', u'728 - Senegal'),
    ('731', u'731 - Seychelles'),
    ('735', u'735 - Serra Leoa'),
    ('738', u'738 - Sikkim'),
    ('741', u'741 - Cingapura'),
    ('744', u'744 - Siria, Republica Arabe Da'),
    ('748', u'748 - Somalia'),
    ('750', u'750 - Sri Lanka'),
    ('754', u'754 - Suazilandia'),
    ('756', u'756 - Africa Do Sul'),
    ('759', u'759 - Sudao'),
    ('764', u'764 - Suecia'),
    ('767', u'767 - Suica'),
    ('770', u'770 - Suriname'),
    ('772', u'772 - Tadjiquistao, Republica Do'),
    ('776', u'776 - Tailandia'),
    ('780', u'780 - Tanzania, Rep.Unida Da'),
    ('782', u'782 - Territorio Brit.Oc.Indico'),
    ('783', u'783 - Djibuti'),
    ('785', u'785 - Territorio da Alta Comissao do Pacifico Ocidental'),
    ('788', u'788 - Chade'),
    ('790', u'790 - Tchecoslovaquia'),
    ('791', u'791 - Tcheca, Republica'),
    ('795', u'795 - Timor Leste'),
    ('800', u'800 - Togo'),
    ('805', u'805 - Toquelau,Ilhas'),
    ('810', u'810 - Tonga'),
    ('815', u'815 - Trinidad E Tobago'),
    ('820', u'820 - Tunisia'),
    ('823', u'823 - Turcas E Caicos,Ilhas'),
    ('824', u'824 - Turcomenistao, Republica Do'),
    ('827', u'827 - Turquia'),
    ('828', u'828 - Tuvalu'),
    ('831', u'831 - Ucrania'),
    ('833', u'833 - Uganda'),
    ('840', u'840 - Uniao Das Republicas Socialistas Sovieticas'),
    ('845', u'845 - Uruguai'),
    ('847', u'847 - Uzbequistao, Republica Do'),
    ('848', u'848 - Vaticano, Est.Da Cidade Do'),
    ('850', u'850 - Venezuela'),
    ('855', u'855 - Vietname Norte'),
    ('858', u'858 - Vietna'),
    ('863', u'863 - Virgens,Ilhas (BRITANICAS)'),
    ('866', u'866 - Virgens,Ilhas (E.U.A.)'),
    ('870', u'870 - Fiji'),
    ('873', u'873 - Wake, Ilha'),
    ('875', u'875 - Wallis E Futuna, Ilhas'),
    ('888', u'888 - Congo, Republica Democratica Do'),
    ('890', u'890 - Zambia'),
)

CHOICES_S2400_TPLOGRAD = (
    ('A', u'A - Área'),
    ('A V', u'A V - Área Verde'),
    ('AC', u'AC - Acesso'),
    ('ACA', u'ACA - Acampamento'),
    ('ACL', u'ACL - Acesso Local'),
    ('AD', u'AD - Adro'),
    ('AE', u'AE - Área Especial'),
    ('AER', u'AER - Aeroporto'),
    ('AL', u'AL - Alameda'),
    ('AMD', u'AMD - Avenida Marginal Direita'),
    ('AME', u'AME - Avenida Marginal Esquerda'),
    ('AN', u'AN - Anel Viário'),
    ('ANT', u'ANT - Antiga Estrada'),
    ('ART', u'ART - Artéria'),
    ('AT', u'AT - Alto'),
    ('ATL', u'ATL - Atalho'),
    ('AV', u'AV - Avenida'),
    ('AVC', u'AVC - Avenida Contorno'),
    ('AVM', u'AVM - Avenida Marginal'),
    ('AVV', u'AVV - Avenida Velha'),
    ('BAL', u'BAL - Balneário'),
    ('BC', u'BC - Beco'),
    ('BCO', u'BCO - Buraco'),
    ('BEL', u'BEL - Belvedere'),
    ('BL', u'BL - Bloco'),
    ('BLO', u'BLO - Balão'),
    ('BLS', u'BLS - Blocos'),
    ('BLV', u'BLV - Bulevar'),
    ('BSQ', u'BSQ - Bosque'),
    ('BVD', u'BVD - Boulevard'),
    ('BX', u'BX - Baixa'),
    ('C', u'C - Cais'),
    ('CAL', u'CAL - Calçada'),
    ('CAM', u'CAM - Caminho'),
    ('CAN', u'CAN - Canal'),
    ('CH', u'CH - Chácara'),
    ('CHA', u'CHA - Chapadão'),
    ('CIC', u'CIC - Ciclovia'),
    ('CIR', u'CIR - Circular'),
    ('CJ', u'CJ - Conjunto'),
    ('CJM', u'CJM - Conjunto Mutirão'),
    ('CMP', u'CMP - Complexo Viário'),
    ('COL', u'COL - Colônia'),
    ('COM', u'COM - Comunidade'),
    ('CON', u'CON - Condomínio'),
    ('COR', u'COR - Corredor'),
    ('CPO', u'CPO - Campo'),
    ('CRG', u'CRG - Córrego'),
    ('CTN', u'CTN - Contorno'),
    ('DSC', u'DSC - Descida'),
    ('DSV', u'DSV - Desvio'),
    ('DT', u'DT - Distrito'),
    ('EB', u'EB - Entre Bloco'),
    ('EIM', u'EIM - Estrada Intermunicipal'),
    ('ENS', u'ENS - Enseada'),
    ('ENT', u'ENT - Entrada Particular'),
    ('EQ', u'EQ - Entre Quadra'),
    ('ESC', u'ESC - Escada'),
    ('ESD', u'ESD - Escadaria'),
    ('ESE', u'ESE - Estrada Estadual'),
    ('ESI', u'ESI - Estrada Vicinal'),
    ('ESL', u'ESL - Estrada de Ligação'),
    ('ESM', u'ESM - Estrada Municipal'),
    ('ESP', u'ESP - Esplanada'),
    ('ESS', u'ESS - Estrada de Servidão'),
    ('EST', u'EST - Estrada'),
    ('ESV', u'ESV - Estrada Velha'),
    ('ETA', u'ETA - Estrada Antiga'),
    ('ETC', u'ETC - Estação'),
    ('ETD', u'ETD - Estádio'),
    ('ETN', u'ETN - Estância'),
    ('ETP', u'ETP - Estrada Particular'),
    ('ETT', u'ETT - Estacionamento'),
    ('EVA', u'EVA - Evangélica'),
    ('EVD', u'EVD - Elevada'),
    ('EX', u'EX - Eixo Industrial'),
    ('FAV', u'FAV - Favela'),
    ('FAZ', u'FAZ - Fazenda'),
    ('FER', u'FER - Ferrovia'),
    ('FNT', u'FNT - Fonte'),
    ('FRA', u'FRA - Feira'),
    ('FTE', u'FTE - Forte'),
    ('GAL', u'GAL - Galeria'),
    ('GJA', u'GJA - Granja'),
    ('HAB', u'HAB - Núcleo Habitacional'),
    ('IA', u'IA - Ilha'),
    ('IND', u'IND - Indeterminado'),
    ('IOA', u'IOA - Ilhota'),
    ('JD', u'JD - Jardim'),
    ('JDE', u'JDE - Jardinete'),
    ('LD', u'LD - Ladeira'),
    ('LGA', u'LGA - Lagoa'),
    ('LGO', u'LGO - Lago'),
    ('LOT', u'LOT - Loteamento'),
    ('LRG', u'LRG - Largo'),
    ('LT', u'LT - Lote'),
    ('MER', u'MER - Mercado'),
    ('MNA', u'MNA - Marina'),
    ('MOD', u'MOD - Modulo'),
    ('MRG', u'MRG - Projeção'),
    ('MRO', u'MRO - Morro'),
    ('MTE', u'MTE - Monte'),
    ('NUC', u'NUC - Núcleo'),
    ('NUR', u'NUR - Núcleo Rural'),
    ('OUT', u'OUT - Outeiro'),
    ('PAR', u'PAR - Paralela'),
    ('PAS', u'PAS - Passeio'),
    ('PAT', u'PAT - Pátio'),
    ('PC', u'PC - Praça'),
    ('PCE', u'PCE - Praça de Esportes'),
    ('PDA', u'PDA - Parada'),
    ('PDO', u'PDO - Paradouro'),
    ('PNT', u'PNT - Ponta'),
    ('PR', u'PR - Praia'),
    ('PRL', u'PRL - Prolongamento'),
    ('PRM', u'PRM - Parque Municipal'),
    ('PRQ', u'PRQ - Parque'),
    ('PRR', u'PRR - Parque Residencial'),
    ('PSA', u'PSA - Passarela'),
    ('PSG', u'PSG - Passagem'),
    ('PSP', u'PSP - Passagem de Pedestre'),
    ('PSS', u'PSS - Passagem Subterrânea'),
    ('PTE', u'PTE - Ponte'),
    ('PTO', u'PTO - Porto'),
    ('Q', u'Q - Quadra'),
    ('QTA', u'QTA - Quinta'),
    ('QTS', u'QTS - Quintas'),
    ('R', u'R - Rua'),
    ('R I', u'R I - Rua Integração'),
    ('R L', u'R L - Rua de Ligação'),
    ('R P', u'R P - Rua Particular'),
    ('R V', u'R V - Rua Velha'),
    ('RAM', u'RAM - Ramal'),
    ('RCR', u'RCR - Recreio'),
    ('REC', u'REC - Recanto'),
    ('RER', u'RER - Retiro'),
    ('RES', u'RES - Residencial'),
    ('RET', u'RET - Reta'),
    ('RLA', u'RLA - Ruela'),
    ('RMP', u'RMP - Rampa'),
    ('ROA', u'ROA - Rodo Anel'),
    ('ROD', u'ROD - Rodovia'),
    ('ROT', u'ROT - Rotula'),
    ('RPE', u'RPE - Rua de Pedestre'),
    ('RPR', u'RPR - Margem'),
    ('RTN', u'RTN - Retorno'),
    ('RTT', u'RTT - Rotatória'),
    ('SEG', u'SEG - Segunda Avenida'),
    ('SIT', u'SIT - Sitio'),
    ('SRV', u'SRV - Servidão'),
    ('ST', u'ST - Setor'),
    ('SUB', u'SUB - Subida'),
    ('TCH', u'TCH - Trincheira'),
    ('TER', u'TER - Terminal'),
    ('TR', u'TR - Trecho'),
    ('TRV', u'TRV - Trevo'),
    ('TUN', u'TUN - Túnel'),
    ('TV', u'TV - Travessa'),
    ('TVP', u'TVP - Travessa Particular'),
    ('TVV', u'TVV - Travessa Velha'),
    ('UNI', u'UNI - Unidade'),
    ('V', u'V - Via'),
    ('V C', u'V C - Via Coletora'),
    ('V L', u'V L - Via Local'),
    ('V-E', u'V-E - Via Expressa'),
    ('VAC', u'VAC - Via de Acesso'),
    ('VAL', u'VAL - Vala'),
    ('VCO', u'VCO - Via Costeira'),
    ('VD', u'VD - Viaduto'),
    ('VER', u'VER - Vereda'),
    ('VEV', u'VEV - Via Elevado'),
    ('VL', u'VL - Vila'),
    ('VLA', u'VLA - Viela'),
    ('VLE', u'VLE - Vale'),
    ('VLT', u'VLT - Via Litorânea'),
    ('VPE', u'VPE - Via de Pedestre'),
    ('VRT', u'VRT - Variante'),
    ('ZIG', u'ZIG - Zigue-Zague'),
)

class s2400altBeneficio(models.Model):
    s2400_evtcdbenprrp = models.OneToOneField('esocial.s2400evtCdBenPrRP',
        related_name='%(class)s_s2400_evtcdbenprrp')
    def evento(self): return self.s2400_evtcdbenprrp.evento()
    tpbenef = models.IntegerField(choices=CHOICES_S2400_ALTBENEFICIO_TPBENEF)
    nrbenefic = models.CharField(max_length=20)
    dtinibenef = models.DateField()
    vrbenef = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2400_evtcdbenprrp) + ' - ' + unicode(self.tpbenef) + ' - ' + unicode(self.nrbenefic) + ' - ' + unicode(self.dtinibenef) + ' - ' + unicode(self.vrbenef)
    #s2400_altbeneficio_custom#
    #s2400_altbeneficio_custom#
    class Meta:
        db_table = r's2400_altbeneficio'
        managed = True
        ordering = ['s2400_evtcdbenprrp', 'tpbenef', 'nrbenefic', 'dtinibenef', 'vrbenef']


class s2400altBeneficioinfoPenMorte(models.Model):
    s2400_altbeneficio = models.OneToOneField('s2400altBeneficio',
        related_name='%(class)s_s2400_altbeneficio')
    def evento(self): return self.s2400_altbeneficio.evento()
    idquota = models.CharField(max_length=30)
    cpfinst = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2400_altbeneficio) + ' - ' + unicode(self.idquota) + ' - ' + unicode(self.cpfinst)
    #s2400_altbeneficio_infopenmorte_custom#
    #s2400_altbeneficio_infopenmorte_custom#
    class Meta:
        db_table = r's2400_altbeneficio_infopenmorte'
        managed = True
        ordering = ['s2400_altbeneficio', 'idquota', 'cpfinst']


class s2400brasil(models.Model):
    s2400_evtcdbenprrp = models.OneToOneField('esocial.s2400evtCdBenPrRP',
        related_name='%(class)s_s2400_evtcdbenprrp')
    def evento(self): return self.s2400_evtcdbenprrp.evento()
    tplograd = models.CharField(choices=CHOICES_S2400_TPLOGRAD, max_length=4)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2400_evtcdbenprrp) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2400_brasil_custom#
    #s2400_brasil_custom#
    class Meta:
        db_table = r's2400_brasil'
        managed = True
        ordering = ['s2400_evtcdbenprrp', 'tplograd', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'cep', 'codmunic', 'uf']


class s2400exterior(models.Model):
    s2400_evtcdbenprrp = models.OneToOneField('esocial.s2400evtCdBenPrRP',
        related_name='%(class)s_s2400_evtcdbenprrp')
    def evento(self): return self.s2400_evtcdbenprrp.evento()
    paisresid = models.CharField(choices=CHOICES_S2400_PAISRESID, max_length=3)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    nmcid = models.CharField(max_length=50)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2400_evtcdbenprrp) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.nmcid) + ' - ' + unicode(self.codpostal)
    #s2400_exterior_custom#
    #s2400_exterior_custom#
    class Meta:
        db_table = r's2400_exterior'
        managed = True
        ordering = ['s2400_evtcdbenprrp', 'paisresid', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'nmcid', 'codpostal']


class s2400fimBeneficio(models.Model):
    s2400_evtcdbenprrp = models.OneToOneField('esocial.s2400evtCdBenPrRP',
        related_name='%(class)s_s2400_evtcdbenprrp')
    def evento(self): return self.s2400_evtcdbenprrp.evento()
    tpbenef = models.IntegerField(choices=CHOICES_S2400_FIMBENEFICIO_TPBENEF)
    nrbenefic = models.CharField(max_length=20)
    dtfimbenef = models.DateField()
    mtvfim = models.IntegerField(choices=CHOICES_S2400_FIMBENEFICIO_MTVFIM)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2400_evtcdbenprrp) + ' - ' + unicode(self.tpbenef) + ' - ' + unicode(self.nrbenefic) + ' - ' + unicode(self.dtfimbenef) + ' - ' + unicode(self.mtvfim)
    #s2400_fimbeneficio_custom#
    #s2400_fimbeneficio_custom#
    class Meta:
        db_table = r's2400_fimbeneficio'
        managed = True
        ordering = ['s2400_evtcdbenprrp', 'tpbenef', 'nrbenefic', 'dtfimbenef', 'mtvfim']


class s2400iniBeneficio(models.Model):
    s2400_evtcdbenprrp = models.OneToOneField('esocial.s2400evtCdBenPrRP',
        related_name='%(class)s_s2400_evtcdbenprrp')
    def evento(self): return self.s2400_evtcdbenprrp.evento()
    tpbenef = models.IntegerField(choices=CHOICES_S2400_INIBENEFICIO_TPBENEF)
    nrbenefic = models.CharField(max_length=20)
    dtinibenef = models.DateField()
    vrbenef = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2400_evtcdbenprrp) + ' - ' + unicode(self.tpbenef) + ' - ' + unicode(self.nrbenefic) + ' - ' + unicode(self.dtinibenef) + ' - ' + unicode(self.vrbenef)
    #s2400_inibeneficio_custom#
    #s2400_inibeneficio_custom#
    class Meta:
        db_table = r's2400_inibeneficio'
        managed = True
        ordering = ['s2400_evtcdbenprrp', 'tpbenef', 'nrbenefic', 'dtinibenef', 'vrbenef']


class s2400iniBeneficioinfoPenMorte(models.Model):
    s2400_inibeneficio = models.OneToOneField('s2400iniBeneficio',
        related_name='%(class)s_s2400_inibeneficio')
    def evento(self): return self.s2400_inibeneficio.evento()
    idquota = models.CharField(max_length=30)
    cpfinst = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2400_inibeneficio) + ' - ' + unicode(self.idquota) + ' - ' + unicode(self.cpfinst)
    #s2400_inibeneficio_infopenmorte_custom#
    #s2400_inibeneficio_infopenmorte_custom#
    class Meta:
        db_table = r's2400_inibeneficio_infopenmorte'
        managed = True
        ordering = ['s2400_inibeneficio', 'idquota', 'cpfinst']


#VIEWS_MODELS
