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



CHOICES_S2210_CODAGNTCAUSADOR = [

    (200004300, u'200004300 - Impacto de pessoa contra objeto parado. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior.'),
    (200004600, u'200004600 - Impacto de pessoa contra objeto em movimento. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior.'),
    (200008300, u'200008300 - Impacto sofrido por pessoa, de objeto que cai. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'),
    (200008600, u'200008600 - Impacto sofrido por pessoa, de objeto projetado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'),
    (200008900, u'200008900 - Impacto sofrido por pessoa, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'),
    (200012200, u'200012200 - Queda de pessoa com diferença de nível de andaime, passagem, plataforma, etc. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
    (200012300, u'200012300 - Queda de pessoa com diferença de nível de escada móvel ou fixada cujos degraus não permitem o apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
    (200012400, u'200012400 - Queda de pessoa com diferença de nível de material empilhado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
    (200012500, u'200012500 - Queda de pessoa com diferença de nível de veículo. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
    (200012600, u'200012600 - Queda de pessoa com diferença de nível em escada permanente cujos degraus permitem apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
    (200012700, u'200012700 - Queda de pessoa com diferença de nível em poço, escavação, abertura no piso, etc. (da borda da abertura). Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
    (200012900, u'200012900 - Queda de pessoa com diferença de nível, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
    (200016300, u'200016300 - Queda de pessoa em mesmo nível em passagem ou superfície de sustentação. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'),
    (200016600, u'200016600 - Queda de pessoa em mesmo nível sobre ou contra alguma coisa. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'),
    (200016900, u'200016900 - Queda de pessoa em mesmo nível, NIC. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'),
    (200020100, u'200020100 - Aprisionamento em, sob ou entre objetos em movimento convergente (calandra) ou de encaixe. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
    (200020300, u'200020300 - Aprisionamento em, sob ou entre um objeto parado e outro em movimento. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
    (200020500, u'200020500 - Aprisionamento em, sob ou entre dois ou mais objetos em movimento (sem encaixe). Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
    (200020700, u'200020700 - Aprisionamento em, sob ou entre desabamento ou desmoronamento de edificação, barreira, etc. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
    (200020900, u'200020900 - Aprisionamento em, sob ou entre, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
    (200024300, u'200024300 - Atrito ou abrasão por encostar, pisar, ajoelhar ou sentar em objeto (não em vibração). Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
    (200024400, u'200024400 - Atrito ou abrasão por manusear objeto (não em vibração). Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
    (200024500, u'200024500 - Atrito ou abrasão por objeto em vibração. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
    (200024600, u'200024600 - Atrito ou abrasão por corpo estranho no olho. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
    (200024700, u'200024700 - Atrito ou abrasão por compressão repetitiva Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
    (200024900, u'200024900 - Atrito ou abrasão, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
    (200028300, u'200028300 - Reação do corpo a seus movimentos - movimento involuntário (escorregão sem queda, etc.). Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto.'),
    (200028600, u'200028600 - Reação do corpo a seus movimentos - movimento voluntário. Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto.'),
    (200032200, u'200032200 - Esforço excessivo ao erguer objeto. Ver explicações da classificação anterior (200028000).'),
    (200032400, u'200032400 - Esforço excessivo ao empurrar ou puxar objeto. Ver explicações da classificação anterior (200028000).'),
    (200032600, u'200032600 - Esforço excessivo ao manejar, sacudir ou arremessar objeto. Ver explicações da classificação anterior (200028000).'),
    (200032900, u'200032900 - Esforço excessivo, NIC. Ver explicações da classificação anterior (200028000).'),
    (200036000, u'200036000 - Exposição a energia elétrica. Aplica-se somente a casos sem impacto, em que a lesão consiste em choque elétrico, queimadura ou eletroplessão (eletrocussão).'),
    (200040300, u'200040300 - Contato com objeto ou substância a temperatura muito alta. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica.'),
    (200040600, u'200040600 - Contato com objeto ou substância a temperatura muito baixa. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica.'),
    (200044300, u'200044300 - Exposição à temperatura ambiente elevada. Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica.'),
    (200044600, u'200044600 - Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica.'),
    (200048200, u'200048200 - Inalação de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
    (200048400, u'200048400 - Ingestão de substancia cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
    (200048600, u'200048600 - Absorção (por contato) de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
    (200048900, u'200048900 - Inalação, ingestão e absorção, NIC. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
    (200052000, u'200052000 - Imersão. Aplica-se aos acidentes que têm por consequência o afogamento.'),
    (200056000, u'200056000 - Exposição à radiação não ionizante. Aplica-se a casos em que as lesões são provocadas por exposição à radiação solar ou outras radiações não ionizantes (por exemplo: ultravioleta e infravermelho).'),
    (200060000, u'200060000 - Exposição à radiação ionizante.'),
    (200064000, u'200064000 - Exposição ao ruído.'),
    (200068000, u'200068000 - Exposição à vibração.'),
    (200072300, u'200072300 - Exposição à pressão ambiente elevada.'),
    (200072600, u'200072600 - Exposição à pressão ambiente baixa.'),
    (200076200, u'200076200 - Exposição à poluição da água.'),
    (200076400, u'200076400 - Exposição à poluição do ar.'),
    (200076600, u'200076600 - Exposição à poluição do solo.'),
    (200076900, u'200076900 - Exposição à poluição, NIC.'),
    (200080200, u'200080200 - Ataque de ser vivo por mordedura, picada, chifrada, coice, etc., não se aplicando no caso de haver peçonha ou transmissão de doença.'),
    (200080400, u'200080400 - Ataque de ser vivo com peçonha.'),
    (200080600, u'200080600 - Ataque de ser vivo com transmissão de doença.'),
    (200080900, u'200080900 - Ataque de ser vivo (inclusive do homem), NIC.'),
    (200080901, u'200080901 - Contato com pessoas doentes ou material infecto-contagiante - agentes biológicos.'),
    (209000000, u'209000000 - Tipo, NIC'),
    (209500000, u'209500000 - Tipo inexistente'),
    
]




CHOICES_S2210_CODPARTEATING = [

    (753030000, u'753030000 - Crânio (inclusive encéfalo)'),
    (753050000, u'753050000 - Ouvido (externo, médio, interno, audição e equilíbrio)'),
    (753070100, u'753070100 - Olho (inclusive nervo ótico e visão)'),
    (753070300, u'753070300 - Nariz (inclusive fossas nasais, seios da face e olfato)'),
    (753070500, u'753070500 - Boca (inclusive lábios, dentes, língua, garganta e paladar)'),
    (753070700, u'753070700 - Mandíbula (inclusive queixo)'),
    (753070800, u'753070800 - Face, partes múltiplas (qualquer combinação das partes acima)'),
    (753080000, u'753080000 - Cabeça, partes múltiplas (qualquer combinação das partes acima)'),
    (753090000, u'753090000 - Cabeça, NIC'),
    (753510000, u'753510000 - Braço (entre o punho a o ombro)'),
    (753510200, u'753510200 - Braço (acima do cotovelo)'),
    (754000000, u'754000000 - Pescoço'),
    (755010400, u'755010400 - Cotovelo'),
    (755010600, u'755010600 - Antebraço (entre o punho e o cotovelo)'),
    (755030000, u'755030000 - Punho'),
    (755050000, u'755050000 - Mão (exceto punho ou dedos)'),
    (755070000, u'755070000 - Dedo'),
    (755080000, u'755080000 - Membros superiores, partes múltiplas (qualquer combinação das partes acima)'),
    (755090000, u'755090000 - Membros superiores, NIC'),
    (756020000, u'756020000 - Ombro'),
    (756030000, u'756030000 - Tórax (inclusive órgãos internos)'),
    (756040000, u'756040000 - Dorso (inclusive músculos dorsais, coluna e medula espinhal)'),
    (756050000, u'756050000 - Abdome (inclusive órgãos internos)'),
    (756060000, u'756060000 - Quadris (inclusive pélvis, órgãos pélvicos e nádegas)'),
    (756070000, u'756070000 - Tronco, partes múltiplas (qualquer combinação das partes acima)'),
    (756090000, u'756090000 - Tronco, NIC'),
    (757010000, u'757010000 - Perna (entre o tornozelo e a pélvis)'),
    (757010200, u'757010200 - Coxa'),
    (757010400, u'757010400 - Joelho'),
    (757010600, u'757010600 - Perna (do tornozelo, exclusive, ao joelho, exclusive)'),
    (757030000, u'757030000 - Articulação do tornozelo'),
    (757050000, u'757050000 - Pé (exceto artelhos)'),
    (757070000, u'757070000 - Artelho'),
    (757080000, u'757080000 - Membros inferiores, partes múltiplas (qualquer combinação das partes acima)'),
    (757090000, u'757090000 - Membros inferiores, NIC'),
    (758000000, u'758000000 - Partes múltiplas. Aplica-se quando mais de uma parte importante do corpo for afetada, como por exemplo, um braço e uma perna'),
    (758500000, u'758500000 - Sistemas e aparelhos. Aplica-se quando o funcionamento de todo um sistema ou aparelho do corpo humano for afetado, sem lesão específica de qualquer outra parte, como no caso do envenenamento, ação corrosiva que afete órgãos internos, lesão dos centros nervosos, etc. não se aplica quando a lesão sistêmica for provocada por lesão externa, como lesão dorsal que afete nervos da medula espinhal.'),
    (758520000, u'758520000 - Aparelho circulatório'),
    (758530000, u'758530000 - Aparelho respiratório'),
    (758540000, u'758540000 - Sistema nervoso'),
    (758550000, u'758550000 - Aparelho digestivo'),
    (758560000, u'758560000 - Aparelho gênito-urinário'),
    (758570000, u'758570000 - Sistema musculoesquelético'),
    (758590000, u'758590000 - Sistemas e aparelhos, NIC'),
    (759000000, u'759000000 - Localização da lesão, NIC'),
    
]




CHOICES_S2210_DSCLESAO = [

    (702000000, u'702000000 - Lesão imediata'),
    (702005000, u'702005000 - Escoriação, abrasão (ferimento superficial)'),
    (702010000, u'702010000 - Corte, laceração, ferida contusa, punctura (ferida aberta)'),
    (702015000, u'702015000 - Contusão, esmagamento (superfície cutânea intacta)'),
    (702020000, u'702020000 - Distensão, torção'),
    (702025000, u'702025000 - Inflamação de articulação, tendão ou músculo - inclui sinovite, tenossionovite, etc. Não inclui distensão, torção ou suas consequências'),
    (702030000, u'702030000 - Luxação'),
    (702035000, u'702035000 - Fratura'),
    (702040000, u'702040000 - Queimadura ou escaldadura - efeito de temperatura elevada. Efeito do contato com substância quente. Inclui queimadura por eletricidade, mas não inclui choque elétrico. Não inclui queimadura por substância química, efeito de radiação, queimadura de sol, incapacidade sistêmica como intermação, queimadura por atrito, etc.'),
    (702042000, u'702042000 - Queimadura química (lesão de tecido provocada pela ação corrosiva de produto químico, suas emanações, etc.)'),
    (702045000, u'702045000 - Efeito de radiação (imediato) - queimadura de sol e toda forma de lesão de tecido, osso ou fluido orgânico, por exposição à radiação'),
    (702048000, u'702048000 - Congelamento, geladura e outros efeitos da exposição à baixa temperatura'),
    (702050000, u'702050000 - Asfixia, estrangulamento, afogamento'),
    (702055000, u'702055000 - Intermação, insolação, cãibra, exaustão e outros efeitos da temperatura ambiente elevada - não inclui queimadura de sol ou outros efeitos de radiação'),
    (702060000, u'702060000 - Choque elétrico e eletroplessão (eletrocussão)'),
    (702065000, u'702065000 - Hérnia de qualquer natureza, ruptura'),
    (702070000, u'702070000 - Amputação ou enucleação'),
    (702075000, u'702075000 - Perda ou diminuição de sentido (audição, visão, olfato, paladar e tato, desde que não seja sequela de outra lesão)'),
    (702080000, u'702080000 - Concussão cerebral'),
    (702090000, u'702090000 - Lesão imediata, NIC'),
    (704020000, u'704020000 - Doença contagiosa ou infecciosa (tuberculose, brucelose, etc.)'),
    (704030000, u'704030000 - Pneumoconiose (silicose, asbestose, etc.)'),
    (704040000, u'704040000 - Dermatose (erupção, inflamação da pele, inclusive furúnculo, etc.). Geralmente provocada pelo contato direto com substâncias ou agentes sensibilizantes ou irritantes, tais como medicamentos, óleos, agentes biológicos, plantas, madeiras ou metais. Não inclui lesão provocada pela ação corrosiva de produtos químicos, queimadura por contato com substâncias quentes, efeito de exposição à radiação, efeito de exposição a baixas temperaturas ou inflamação ou irritação causada por fricção ou impacto'),
    (704050000, u'704050000 - Envenenamento sistêmico - condição mórbida sistêmica provocada por inalação, ingestão ou absorção cutânea de substância tóxica, que afete o metabolismo, o funcionamento do sistema nervoso, do aparelho circulatório, do aparelho digestivo, do aparelho respiratório, dos órgãos de excreção, do sistema músculo-esquelético, etc., inclui ação de produto químico, medicamento, metal ou peçonha. Não inclui efeito de radiação, pneumoconiose, efeito corrosivo de produto químico, irritação cutânea, septicemia ou caso de ferida infectada'),
    (704060000, u'704060000 - Perda ou diminuição mediatas de sentido (audição, visão, olfato, paladar e tato, desde que não seja sequela de outra lesão)'),
    (704070000, u'704070000 - Efeito de radiação (mediato) - queimadura do sol e toda forma de lesão de tecido, osso, ou fluido orgânico por exposição à radiação.'),
    (704090000, u'704090000 - Doença, NIC'),
    (706050000, u'706050000 - Lesões múltiplas'),
    (706090000, u'706090000 - Outras lesões, NIC'),
    
]




CHOICES_S2210_IDEOC = [

    (1, u'1 - Conselho Regional de Medicina (CRM)'),
    (2, u'2 - Conselho Regional de Odontologia (CRO)'),
    (3, u'3 - Registro do Ministério da Saúde (RMS).'),
    
]




CHOICES_S2210_INDAFAST = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2210_INDINTERNACAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2210_LATERALIDADE = [

    (0, u'0 - Não aplicável'),
    (1, u'1 - Esquerda'),
    (2, u'2 - Direita'),
    (3, u'3 - Ambas. Nos casos de órgãos bilaterais, ou seja, que se situam dos lados do corpo, assinalar o lado (direito ou esquerdo). Exemplo: no caso de o órgão atingido ser uma perna, apontar qual foi a atingida (se a perna direita, se a perna esquerda, ou se ambas). Se o órgão atingido é único (como, por exemplo, a cabeça), assinalar este campo como não aplicável.'),
    
]




CHOICES_S2210_TPINSC = [

    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (5, u'5 - CGC'),
    
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



