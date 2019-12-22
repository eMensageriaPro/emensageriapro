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



CHOICES_DIA = [
    (1, u'1 - Segunda-Feira'),
    (2, u'2 - Terça-Feira'),
    (3, u'3 - Quarta-Feira'),
    (4, u'4 - Quinta-Feira'),
    (5, u'5 - Sexta-Feira'),
    (6, u'6 - Sábado'),
    (7, u'7 - Domingo'),
    (8, u'8 - Dia variável.'),
]


CHOICES_INFOCOTA = [
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
]


CHOICES_PERHORFLEXIVEL = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_TMPPARC = [
    (0, u'0 - Não é contrato em tempo parcial'),
    (1, u'1 - Limitado a 25 horas semanais'),
    (2, u'2 - Limitado a 30 horas semanais'),
    (3, u'3 - Limitado a 26 horas semanais.'),
]


CHOICES_TPCONTR = [
    (1, u'1 - Contribuição Sindical Compulsória'),
    (2, u'2 - Contribuição Associativa'),
    (3, u'3 - Contribuição Assistencial'),
    (4, u'4 - Contribuição Confederativa.'),
]


CHOICES_TPINSC = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF.'),
]


CHOICES_TPINTERV = [
    (1, u'1 - Intervalo em Horário Fixo'),
    (2, u'2 - Intervalo em Horário Variável.'),
]


CHOICES_TPJORNADA = [
    (1, u'1 - Jornada com horário diário e folga fixos'),
    (2, u'2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)'),
    (3, u'3 - Jornada com horário diário fixo e folga variável'),
    (9, u'9 - Demais tipos de jornada.'),
]


CHOICES_TPREGJOR = [
    (1, u'1 - Submetidos a Horário de Trabalho (Cap. II da CLT)'),
    (2, u'2 - Atividade Externa especificada no Inciso I do Art. 62 da CLT'),
    (3, u'3 - Funções especificadas no Inciso II do Art. 62 da CLT'),
    (4, u'4 - Teletrabalho, previsto no Inciso III do Art. 62 da CLT.'),
]


CHOICES_UNDSALFIXO = [
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável.'),
]


CODIGO_RESPOSTA = [
    (0, u'Cadastrado'),
    (101, u'101 - Lote Aguardando Processamento'),
    (201, u'201 - Lote Processado com Sucesso'),
    (202, u'202 - Lote Processado com Advertências'),
    (301, u'301 - Erro Servidor eSocial'),
    (401, u'401 - Lote Incorreto - Erro preenchimento'),
    (402, u'402 - Lote Incorreto - schema Inválido'),
    (403, u'403 - Lote Incorreto - Versão do Schema não permitida'),
    (404, u'404 - Lote Incorreto - Erro Certificado'),
    (405, u'405 - Lote Incorreto - Lote nulo ou vazio'),
    (501, u'501 - Solicitação de Consulta Incorreta - Erro Preenchimento'),
    (502, u'502 - Solicitação de Consulta Incorreta - Schema Inválido.'),
    (503, u'503 - Solicitação de Consulta Incorreta - Versão do Schema Não Permitida.'),
    (504, u'504 - Solicitação de Consulta Incorreta - Erro Certificado.'),
    (505, u'505 - Solicitação de Consulta Incorreta - Consulta nula ou vazia.'),
]


CODIGO_STATUS_EFDREINF = [
    (0, u'0 - Sucesso'),
    (1, u'1 - Erro'),
    (2, u'2 - Em Processamento'),
]


EVENTOS_GRUPOS = [
    (1, u'1 - Eventos de Tabelas'),
    (2, u'2 - Eventos Não Periódicos'),
    (3, u'3 - Eventos Periódicos'),
]


EVENTOS_OCORRENCIAS_TIPO = [
    (1, u'1 - Erro'),
    (2, u'2 - Advertência'),
]


EVENTOS_OCORRENCIAS_TIPO_EFDREINF = [
    (1, u'1 - Aviso'),
    (2, u'2 - Erro'),
]


IMPORTACAO_STATUS = [
    (0, u'Aguardando'),
    (1, u'Processando'),
    (2, u'Processado com sucesso'),
    (3, u'Erro - Processamento'),
    (4, u'Erro - Outros'),
    (5, u'Erro - Arquivo Inválido'),
    (6, u'Erro - Identidade já existente'),
    (7, u'Erro - Versão de leiaute incompatível'),
    (8, u'Erro - Validação de Leiaute'),
]


SIM_NAO = [
    (0, u'Não'),
    (1, u'Sim'),
]


TIPO_AMBIENTE = [
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
]


TIPO_INSCRICAO = [
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
]


TIPO_OCORRENCIA = [
    (1, u'1 - Erro'),
    (2, u'2 - Advertência'),
]


TRANSMISSOR_STATUS = [
    (0, u'Cadastrado'),
    (1, u'Enviado'),
    (2, u'Erro no envio'),
    (3, u'Consultado'),
    (4, u'Erro na consulta'),
]

