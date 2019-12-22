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



CHOICES_S1210_INDNIF_IDEPGTOEXT = [
    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF.'),
]


CHOICES_S1210_INDPGTOTT_DETPGTOBENPR = [
    ('N', u'N - O valor que está sendo pago é inferior ao previsto no eventoS - 1207 em {dmDev}. neste caso, significa que está sendo informando um pagamento de parte do que é devido ou então, está sendo informado um pagamento parcelado sendo o presente pagamento apenas uma das parcelas.'),
    ('S', u'S - O valor que está sendo pago é exatamente o previsto no eventoS - 1207 em {dmDev}'),
]


CHOICES_S1210_INDPGTOTT_DETPGTOFL = [
    ('N', u'N - O valor que está sendo pago é inferior ao previsto nos eventosS - 1200,S - 1202,S - 2299 ouS - 2399 em {dmDev}, neste caso, significa que está sendo informando um pagamento de parte do que é devido ou então, está sendo informado um pagamento parcelado sendo o presente pagamento apenas uma das parcelas.'),
    ('S', u'S - O valor que está sendo pago é exatamente o previsto nos eventosS - 1200,S - 1202,S - 2299 ouS - 2399 em {dmDev}'),
]


CHOICES_S1210_INDRESBR = [
    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
]


CHOICES_S1210_TPPGTO = [
    (1, u'1 - Pagamento de remuneração, conforme apurado em {dmDev} do S-1200'),
    (2, u'2 - Pagamento de verbas rescisórias conforme apurado em {dmDev} do S- 2299'),
    (3, u'3 - Pagamento de verbas rescisórias conforme apurado em {dmDev} do S- 2399'),
    (5, u'5 - Pagamento de remuneração conforme apurado em {dmDev} do S-1202'),
    (6, u'6 - Pagamento de Benefícios Previdenciários, conforme apurado em {dmDev} do S-1207'),
    (7, u'7 - Recibo de férias'),
    (9, u'9 - Pagamento relativo a competências anteriores ao início de obrigatoriedade dos eventos periódicos para o contribuinte.'),
]

