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



CLASSIFICACAO_REGRAS_PAGAMENTOS_CODIGOS = [

    (1, u'Beneficiários'),
    (2, u'Beneficiários / Justiça – RRA'),
    
]




ESOCIAL_BENEFICIOS_PREVIDENCIARIOS_TIPOS_GRUPOS = [

    (1, u'Grupo 01 - Aposentadoria por Idade e Tempo de Contribuição'),
    (10, u'Grupo 10 - Benefícios Especiais com Vínculo Previdenciário'),
    (11, u'Grupo 11 - Benefícios Especiais sem Vínculo Previdenciário'),
    (12, u'Grupo 12 – Parlamentares'),
    (2, u'Grupo 02 - Aposentadoria Especial'),
    (3, u'Grupo 03 - Aposentadoria por Invalidez'),
    (4, u'Grupo 04 - Militares (Reforma)'),
    (5, u'Grupo 05 - Militares (Reserva)'),
    (6, u'Grupo 06 - Pensão por Morte'),
    (7, u'Grupo 07 - Auxílios Previdenciários'),
    (8, u'Grupo 08 - Complementação do Benefício do Regime Geral de Previdência Social (RGPS)'),
    (9, u'Grupo 09 - Benefícios Concedidos Antes da Obrigatoriedade de Envio dos Eventos Não Periódicos para Entes Públicos no eSocial (Carga Inicial)'),
    
]




GRUPOS_FATORES_RISCOS = [

    (1, u'FÍSICOS'),
    (10, u'PERICULOSO'),
    (11, u'ASSOCIAÇÃO DE FATORES DE RISCO'),
    (12, u'OUTROS FATORES DE RISCO'),
    (13, u'AUSÊNCIA DE FATORES DE RISCO'),
    (2, u'QUÍMICOS'),
    (3, u'BIOLÓGICOS'),
    (4, u'ERGONÔMICOS - BIOMECÂNICOS'),
    (5, u'ERGONÔMICOS - MOBILIÁRIO E EQUIPAMENTOS'),
    (6, u'ERGONÔMICOS - ORGANIZACIONAIS'),
    (7, u'ERGONÔMICOS - AMBIENTAIS'),
    (8, u'ERGONÔMICOS - PSICOSSOCIAIS/COGNITIVOS'),
    (9, u'MECÂNICOS/ACIDENTES'),
    
]




GRUPO_ATIVIDADES_PERICULOSAS = [

    (1, u'ATIVIDADES COM EXPOSIÇÃO A RISCOS BIOLÓGICOS'),
    (10, u'OUTRAS ATIVIDADES'),
    (11, u'AUSÊNCIA DE CORRESPONDÊNCIA'),
    (2, u'ATIVIDADES COM EXPOSIÇÃO A RISCOS QUÍMICOS'),
    (3, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM EXPLOSIVOS'),
    (4, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM INFLAMÁVEIS'),
    (5, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM RADIAÇÕES IONIZANTES OU SUBSTÂNCIAS RADIOATIVAS'),
    (6, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM EXPOSIÇÃO A ROUBOS OU OUTRAS ESPÉCIES DE VIOLÊNCIA FÍSICA NAS ATIVIDADES PROFISSIONAIS DE SEGURANÇA PESSOAL OU PATRIMONIAL'),
    (7, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM ENERGIA ELÉTRICA'),
    (8, u'ATIVIDADES PERIGOSAS EM MOTOCICLETA'),
    (9, u'ATIVIDADES ESPECIAIS POR EXPOSIÇÃO A AGENTES FÍSICOS'),
    
]




GRUPO_CODIGO_ATIV_PROD_SERV = [

    (1, u'I - Pessoas Jurídicas Prestadoras de Serviços -'),
    (2, u'II - Pessoas Jurídicas Comerciais - CR 2991-01'),
    (3, u'III - Pessoas Jurídicas Fabricantes - CR 2991-01'),
    (4, u'IV - Códigos Genéricos - Outras Receitas sujeitas à CPRB - CR 2991-01'),
    
]




GRUPO_NATUREZAS_JURIDICAS = [

    (1, u'Administração Pública'),
    (2, u'Entidades Empresariais'),
    (3, u'Entidades sem Fins Lucrativos'),
    (4, u'Pessoas Físicas'),
    (5, u'Organizações Internacionais e Outras Instituições Extraterritoriais'),
    
]




GRUPO_PAGAMENTOS_CODIGOS = [

    (1, u'Beneficiários no Brasil'),
    (2, u'Beneficiários no Brasil e Justiça – RRA'),
    (3, u'Remessa Exterior'),
    
]




SIM_NAO_TXT = [

    ('N', u'Não'),
    ('S', u'Sim'),
    
]




TRABALHADORES_CATEGORIAS_GRUPO = [

    (1, u'Empregado e Trabalhador Temporário'),
    (2, u'Avulso'),
    (3, u'Agente Público'),
    (4, u'Cessão'),
    (5, u'Contribuinte Individual'),
    (6, u'Bolsistas'),
    
]



