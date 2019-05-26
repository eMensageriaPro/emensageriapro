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



CHOICES_R4020_FRMTRIBUT = [

    ('10', u'10 - Retenção do IRRF - alíquota padrão.'),
    ('11', u'11 - Retenção do IRRF - alíquota da tabela progressiva.'),
    ('12', u'12 - Retenção do IRRF - alíquota diferenciada (países com tributação favorecida).'),
    ('13', u'13 - Retenção do IRRF - alíquota limitada conforme cláusula em convênio.'),
    ('30', u'30 - Retenção do IRRF - outras hipóteses.'),
    ('40', u'40 - Não retenção do IRRF - isenção estabelecida em convênio.'),
    ('41', u'41 - Não retenção do IRRF - isenção prevista em lei interna'),
    ('42', u'42 - Não retenção do IRRF - alíquota Zero prevista em lei interna'),
    ('43', u'43 - Não retenção do IRRF - pagamento antecipado do imposto'),
    ('44', u'44 - Não retenção do IRRF - medida Judicial'),
    ('50', u'50 - Não retenção do IRRF - outras hipóteses'),
    
]




CHOICES_R4020_INDNIF = [

    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF.'),
    
]




CHOICES_R4020_INDORIGEMRECURSOS = [

    (1, u'1 - Recursos do próprio declarante'),
    (2, u'2 - Recursos de terceiros - Declarante é a Instituição Financeira responsável apenas pelo repasse dos valores.'),
    
]




CHOICES_R4020_NATREND = [

    ('000000001', u'000000001 - Decorrente de Decisão da Justiça do Trabalho'),
    ('000000002', u'000000002 - Decorrente de Decisão da Justiça Federal'),
    ('000000003', u'000000003 - Decorrente de Decisão da Justiça dos Estados/Distrito Federal'),
    ('000000004', u'000000004 - Honorários advocatícios de sucumbência pelos advogados e procuradores públicos de que trata o art. 27 da Lei nº 13.327'),
    ('000000005', u'000000005 - Benefício do Regime Geral de Previdência Social'),
    ('000000006', u'000000006 - Lucro e Dividendo'),
    ('000000007', u'000000007 - Resgate de Previdência Complementar - Modalidade Contribuição Definida/Variável - Não Optante pela Tributação Exclusiva'),
    ('000000008', u'000000008 - Resgate de Fundo de Aposentadoria Programada Individual (Fapi)- Não Optante pela Tributação Exclusiva'),
    ('000000009', u'000000009 - Resgate de Previdência Complementar - Modalidade Benefício Definido - Não Optante pela Tributação Exclusiva'),
    ('000000010', u'000000010 - Resgate de Previdência Complementar - Modalidade Contribuição Definida/Variável - Optante pela Tributação Exclusiva'),
    ('000000011', u'000000011 - Resgate de Fundo de Aposentadoria Programada Individual (Fapi)- Optante pela Tributação Exclusiva'),
    ('000000012', u'000000012 - Resgate de Planos de Seguro de Vida com Cláusula de Cobertura por Sobrevivência- Optante pela Tributação Exclusiva'),
    ('000000013', u'000000013 - Resgate de Planos de Seguro de Vida com Cláusula de Cobertura por Sobrevivência- Não Optante pela Tributação Exclusiva'),
    ('000000014', u'000000014 - Benefício de Previdência Complementar - Modalidade Contribuição Definida/Variável - Não Optante pela Tributação Exclusiva'),
    ('000000015', u'000000015 - Benefício de Fundo de Aposentadoria Programada Individual (Fapi)- Não Optante pela Tributação Exclusiva'),
    ('000000016', u'000000016 - Benefício de Previdência Complementar - Modalidade Benefício Definido - Não Optante pela Tributação Exclusiva'),
    ('000000017', u'000000017 - Benefício de Previdência Complementar - Modalidade Contribuição Definida/Variável - Optante pela Tributação Exclusiva'),
    ('000000018', u'000000018 - Benefício de Fundo de Aposentadoria Programada Individual (Fapi)- Optante pela Tributação Exclusiva'),
    ('000000019', u'000000019 - Benefício de Planos de Seguro de Vida com Cláusula de Cobertura por Sobrevivência- Optante pela Tributação Exclusiva'),
    ('000000020', u'000000020 - Benefício de Planos de Seguro de Vida com Cláusula de Cobertura por Sobrevivência- Não Optante pela Tributação Exclusiva'),
    ('000000021', u'000000021 - Juros sobre o Capital Próprio'),
    ('000000022', u'000000022 - Rendimento de Aplicações Financeiras de Renda Fixa, decorrentes de alienação, liquidação (total ou parcial), resgate, cessão ou repactuação do título ou aplicação'),
    ('000000023', u'000000023 - Rendimentos auferidos pela entrega de recursos à pessoa jurídica'),
    ('000000024', u'000000024 - Rendimentos predeterminados obtidos em operações conjugadas realizadas: nos mercados de opções de compra e venda em bolsas de valores, de mercadorias e de futuros (box), no mercado a termo nas bolsas de valores, de mercadorias e de futuros, em operações de venda coberta e sem ajustes diários, e no mercado de balcão.'),
    ('000000025', u'000000025 - Rendimentos obtidos nas operações de transferência de dívidas realizadas com instituição financeira e outras instituições autorizadas a funcionar pelo Banco Central do Brasil'),
    ('000000026', u'000000026 - Rendimentos periódicos produzidos por título ou aplicação, bem como qualquer remuneração adicional aos rendimentos prefixados'),
    ('000000027', u'000000027 - Rendimentos auferidos nas operações de mútuo de recursos financeiros'),
    ('000000028', u'000000028 - Rendimentos auferidos em operações de adiantamento sobre contratos de câmbio de exportação, não sacado (trava de câmbio), bem como operações com export notes, com debêntures, com depósitos voluntários para garantia de instância e com depósitos judiciais ou administrativos, quando seu levantamento se der em favor do depositante'),
    ('000000029', u'000000029 - Rendimentos obtidos nas operações de mútuo e de compra vinculada à revenda tendo por objeto ouro, ativo financeiro'),
    ('000000030', u'000000030 - Rendimentos auferidos em contas de depósitos de poupança'),
    ('000000031', u'000000031 - Rendimentos auferidos sobre juros produzidos por letras hipotecárias'),
    ('000000032', u'000000032 - Rendimentos ou ganhos decorrentes da negociação de títulos ou valores mobiliários de renda fixa em bolsas de valores, de mercadorias, de futuros e assemelhadas'),
    ('000000033', u'000000033 - Rendimentos auferidos em outras aplicações financeiras de renda fixa ou de renda variável'),
    ('000000034', u'000000034 - Rendimentos auferidos em Fundo de Investimento'),
    ('000000035', u'000000035 - Rendimentos auferidos em Fundos de investimento em quotas de fundos de investimento'),
    ('000000036', u'000000036 - Rendimentos produzidos por aplicações em fundos de investimento em ações'),
    ('000000037', u'000000037 - Rendimentos produzidos por aplicações em fundos de investimento em quotas de fundos de investimento em ações'),
    ('000000038', u'000000038 - Rendimentos produzidos por aplicações em Fundos Mútuos de Privatização com recursos do Fundo de Garantia por Tempo de Serviço (FGTS)'),
    ('000000039', u'000000039 - Rendimentos auferidos pela carteira dos Fundos de Investimento Imobiliário'),
    ('000000040', u'000000040 - Rendimentos distribuídos pelo Fundo de Investimento Imobiliário aos seus cotistas'),
    ('000000041', u'000000041 - Rendimento auferido pelo cotista no resgate de cotas na liquidação do Fundo de Investimento Imobiliário'),
    ('000000042', u'000000042 - Rendimentos e ganhos de capital distribuídos pelo Fundo de Investimento Cultural e Artístico (Ficart)'),
    ('000000043', u'000000043 - Rendimentos e ganhos de capital distribuídos pelo Fundo de Financiamento da Indústria Cinematográfica Nacional (Funcines)'),
    ('000000044', u'000000044 - Juros não especificados'),
    ('000000045', u'000000045 - Rendimentos auferidos no resgate de quotas de fundos de investimento mantidos com recursos provenientes de conversão de débitos externos brasileiros, e de que participem, exclusivamente, residentes ou domiciliados no exterior'),
    ('000000046', u'000000046 - Demais rendimentos de capital'),
    ('000000047', u'000000047 - Rendimentos de Locação ou Sublocação'),
    ('000000048', u'000000048 - Rendimentos de Arrendamento ou Subarrendamento'),
    ('000000049', u'000000049 - Importâncias pagas por terceiros por conta do locador do bem (juros, comissões etc.)'),
    ('000000050', u'000000050 - Importâncias pagas ao locador pelo contrato celebrado (luvas, prêmios etc.)'),
    ('000000051', u'000000051 - Benfeitorias e quaisquer melhoramentos realizados no bem locado'),
    ('000000052', u'000000052 - Juros decorrente da alienação a prazo de bens'),
    ('000000053', u'000000053 - Rendimentos de Direito de Uso ou Passagem de Terrenos e de aproveitamento de águas'),
    ('000000054', u'000000054 - Rendimentos de Direito de exploração de películas cinematográficas, Obras Audiovisuais, e Videofônicas'),
    ('000000055', u'000000055 - Rendimentos de  Direito de Conjuntos Industriais e Invenções'),
    ('000000056', u'000000056 - Rendimentos de Direito Autoral'),
    ('000000057', u'000000057 - Rendimentos de Direito Autoral (quando não percebidos pelo autor ou criador da obra)'),
    ('000000058', u'000000058 - Rendimentos de Direito de Imagem'),
    ('000000059', u'000000059 - Rendimentos de Direito de colher ou extrair recursos vegetais, pesquisar e extrair recursos minerais'),
    ('000000060', u'000000060 - Produto da alienação de marcas de indústria e comércio, patentes de invenção e processo ou fórmulas de fabricação'),
    ('000000061', u'000000061 - Importâncias pagas por terceiros por conta do cedente dos direitos (juros, comissões etc.)'),
    ('000000062', u'000000062 - Importâncias pagas ao cedente do direito, pelo contrato celebrado (luvas, prêmios etc.)'),
    ('000000063', u'000000063 - Despesas para conservação dos direitos cedidos (quando compensadas pelo uso do bem ou direito)'),
    ('000000064', u'000000064 - Demais Royalties'),
    ('000000065', u'000000065 - Juros de mora e quaisquer outras compensações pelo atraso no pagamento de royalties'),
    ('000000066', u'000000066 - Juros decorrente da alienação a prazo de direitos'),
    ('000000067', u'000000067 - Ganho de capital decorrente da integralização de cotas de fundos ou clubes de investimento por meio da entrega de ativos financeiros'),
    ('000000068', u'000000068 - Distribuição de Juros sobre o Capital Próprio pela companhia emissora de ações objeto de empréstimo'),
    ('000000069', u'000000069 - Rendimentos de Partes Beneficiárias ou de Fundador'),
    ('000000070', u'000000070 - Rendimentos auferidos em operações de swap'),
    ('000000071', u'000000071 - Rendimentos auferidos em operações day trade realizadas em bolsa de valores, de mercadorias, de futuros e assemelhadas'),
    ('000000072', u'000000072 - Rendimento decorrente de Operação realizada em bolsas de valores, de mercadorias, de futuros, e assemelhadas, exceto day trade'),
    ('000000073', u'000000073 - Rendimento decorrente de Operação realizada no mercado de balcão, com intermediação, tendo por objeto ações, ouro ativo financeiro e outros valores mobiliários negociados no mercado à vista'),
    ('000000074', u'000000074 - Rendimento decorrente de Operação realizada em mercados de liquidação futura fora de bolsa'),
    ('000000075', u'000000075 - Alienação de bens e direitos do ativo não circulante localizados no Brasil'),
    ('000000076', u'000000076 - Comissões, corretagens, ou qualquer outra importância paga/creditada pela representação comercial ou pela mediação na realização de negócios civis e comerciais'),
    ('000000077', u'000000077 - Rendimento de Serviços de propaganda e publicidade'),
    ('000000078', u'000000078 - Prêmios distribuídos, sob a forma de bens e serviços, mediante concursos e sorteios'),
    ('000000079', u'000000079 - Prêmios distribuídos, sob a forma de dinheiro, mediante concursos e sorteios'),
    ('000000080', u'000000080 - Prêmios de Proprietários e Criadores de Cavalos de Corrida'),
    ('000000081', u'000000081 - Benefícios líquidos resultantes da amortização antecipada, mediante sorteio, dos títulos de capitalização'),
    ('000000082', u'000000082 - Benefícios atribuídos aos portadores de títulos de capitalização nos lucros da empresa emitente'),
    ('000000083', u'000000083 - Prêmios distribuídos, sob a forma de bens e serviços, mediante sorteios de jogos de bingo permanente ou eventual'),
    ('000000084', u'000000084 - Prêmios distribuídos, em dinheiro, obtido mediante sorteios de jogos de bingo permanente ou eventual'),
    ('000000085', u'000000085 - Importâncias correspondentes a multas e qualquer outra vantagem, ainda que a título de indenização, em virtude de rescisão de contrato'),
    ('000000086', u'000000086 - Responsabilidade Civil - juros e indenizações por lucros cessantes'),
    ('000000087', u'000000087 - Importâncias pagas ou creditadas a cooperativas de trabalho, associações de profissionais ou assemelhadas, relativas a serviços pessoais que lhes forem prestados por associados destas ou colocados à disposição'),
    ('000000088', u'000000088 - Remuneração de Serviços de administração de bens ou negócios em geral, exceto consórcios ou fundos mútuos para aquisição de bens'),
    ('000000089', u'000000089 - Remuneração de Serviços de advocacia'),
    ('000000090', u'000000090 - Remuneração de Serviços de análise clínica laboratorial'),
    ('000000091', u'000000091 - Remuneração de Serviços de análises técnicas'),
    ('000000092', u'000000092 - Remuneração de Serviços de arquitetura'),
    ('000000093', u'000000093 - Remuneração de Serviços de assessoria e consultoria técnica, exceto serviço de assistência técnica prestado a terceiros e concernente a ramo de indústria ou comércio explorado pelo prestador do serviço,'),
    ('000000094', u'000000094 - Remuneração de Serviços de assistência social,'),
    ('000000095', u'000000095 - Remuneração de Serviços de auditoria,'),
    ('000000096', u'000000096 - Remuneração de Serviços de avaliação e perícia,'),
    ('000000097', u'000000097 - Remuneração de Serviços de  biologia e biomedicina,'),
    ('000000098', u'000000098 - Remuneração de Serviços de cálculo em geral,'),
    ('000000099', u'000000099 - Remuneração de Serviços de consultoria,'),
    ('000000100', u'000000100 - Remuneração de Serviços de contabilidade,'),
    ('000000101', u'000000101 - Remuneração de Serviços de desenho técnico,'),
    ('000000102', u'000000102 - Remuneração de Serviços de economia,'),
    ('000000103', u'000000103 - Remuneração de Serviços de elaboração de projetos,'),
    ('000000104', u'000000104 - Remuneração de Serviços de engenharia, exceto construção de estradas, pontes, prédios e obras assemelhadas,'),
    ('000000105', u'000000105 - Remuneração de Serviços de  ensino e treinamento,'),
    ('000000106', u'000000106 - Remuneração de Serviços de estatística,'),
    ('000000107', u'000000107 - Remuneração de Serviços de fisioterapia,'),
    ('000000108', u'000000108 - Remuneração de Serviços de fonoaudiologia,'),
    ('000000109', u'000000109 - Remuneração de Serviços de geologia,'),
    ('000000110', u'000000110 - Remuneração de Serviços de leilão,'),
    ('000000111', u'000000111 - Remuneração de Serviços de medicina, exceto aquela prestada por ambulatório, banco de sangue, casa de saúde, casa de recuperação ou repouso sob orientação médica, hospital e pronto-socorro,'),
    ('000000112', u'000000112 - Remuneração de Serviços de nutricionismo e dietética,'),
    ('000000113', u'000000113 - Remuneração de Serviços de odontologia,'),
    ('000000114', u'000000114 - Remuneração de Serviços de organização de feiras de amostras, congressos, seminários, simpósios e congêneres,'),
    ('000000115', u'000000115 - Remuneração de Serviços de pesquisa em geral,'),
    ('000000116', u'000000116 - Remuneração de Serviços de planejamento,'),
    ('000000117', u'000000117 - Remuneração de Serviços de programação,'),
    ('000000118', u'000000118 - Remuneração de Serviços de  prótese,'),
    ('000000119', u'000000119 - Remuneração de Serviços de  psicologia e psicanálise,'),
    ('000000120', u'000000120 - Remuneração de Serviços de química,'),
    ('000000121', u'000000121 - Remuneração de Serviços de radiologia e radioterapia,'),
    ('000000122', u'000000122 - Remuneração de Serviços de relações públicas,'),
    ('000000123', u'000000123 - Remuneração de Serviços de  serviço de despachante,'),
    ('000000124', u'000000124 - Remuneração de Serviços de  terapêutica ocupacional,'),
    ('000000125', u'000000125 - Remuneração de Serviços de  tradução ou interpretação comercial,'),
    ('000000126', u'000000126 - Remuneração de Serviços de urbanismo,'),
    ('000000127', u'000000127 - Remuneração de Serviços de  veterinária.'),
    ('000000128', u'000000128 - Remuneração de Serviços de Limpeza'),
    ('000000129', u'000000129 - Remuneração de Serviços de Conservação/ Manutenção'),
    ('000000130', u'000000130 - Remuneração de Serviços de Segurança/Vigilância/Transporte de valores'),
    ('000000131', u'000000131 - Remuneração de Serviços Locação de Mão de obra'),
    ('000000132', u'000000132 - Remuneração de Serviços de Assessoria Creditícia, Mercadológica, Gestão de Crédito, Seleção e Riscos e Administração de Contas a Pagar e a Receber'),
    ('000000133', u'000000133 - Pagamentos Referentes à Aquisição de Autopeças'),
    ('000000134', u'000000134 - Rendimentos pago a companhias de navegação aérea e marítima'),
    ('000000135', u'000000135 - Demais pagamentos a entidades imunes ou isentas'),
    ('200000001', u'200000001 - Alimentação'),
    ('200000002', u'200000002 - Energia elétrica'),
    ('200000003', u'200000003 - Serviços prestados com emprego de materiais'),
    ('200000004', u'200000004 - Construção Civil por empreitada com emprego de materiais'),
    ('200000005', u'200000005 - Serviços hospitalares de que trata o art. 30 da Instrução Normativa RFB nº 1.234, de 11 de janeiro de 2012'),
    ('200000006', u'200000006 - Transporte nacional de cargas'),
    ('200000007', u'200000007 - Serviços de auxílio diagnóstico e terapia, patologia clínica, imagenologia, anatomia patológica e citopatológica, medicina nuclear e análises e patologias clínicas, exames por métodos gráficos, procedimentos endoscópicos, radioterapia, quimioterapia, diálise e oxigenoterapia hiperbárica de que trata o art. 31 e parágrafo único da Instrução Normativa RFB nº 1.234, de 2012'),
    ('200000008', u'200000008 - Produtos farmacêuticos, de perfumaria, de toucador ou de higiene pessoal adquiridos de produtor, importador, distribuidor ou varejista,'),
    ('200000009', u'200000009 - Mercadorias e bens em geral'),
    ('200000010', u'200000010 - Gasolina, inclusive de aviação, óleo diesel, gás liquefeito de petróleo (GLP), combustíveis derivados de petróleo ou de gás natural, querosene de aviação (QAV), e demais produtos derivados de petróleo, adquiridos de refinarias de petróleo, de demais produtores, de importadores, de distribuidor ou varejista'),
    ('200000011', u'200000011 - Álcool etílico hidratado, inclusive para fins carburantes, adquirido diretamente de produtor, importador ou do distribuidor'),
    ('200000012', u'200000012 - Biodiesel adquirido de produtor ou importador'),
    ('200000013', u'200000013 - Gasolina, exceto gasolina de aviação, óleo diesel e gás liquefeito de petróleo (GLP), derivados de petróleo ou de gás natural e querosene de aviação adquiridos de distribuidores e comerciantes varejistas'),
    ('200000014', u'200000014 - Álcool etílico hidratado nacional, inclusive para fins carburantes adquirido de comerciante varejista'),
    ('200000015', u'200000015 - Biodiesel adquirido de distribuidores e comerciantes varejistas'),
    ('200000016', u'200000016 - Biodiesel adquirido de produtor detentor regular do selo “Combustível Social”, fabricado a partir de mamona ou fruto, caroço ou amêndoa de palma produzidos nas regiões norte e nordeste e no semiárido, por agricultor familiar enquadrado no Programa Nacional de Fortalecimento da Agricultura Familiar (Pronaf)'),
    ('200000017', u'200000017 - Transporte internacional de cargas efetuado por empresas nacionais'),
    ('200000018', u'200000018 - Estaleiros navais brasileiros nas atividades de Construção, conservação, modernização, conversão e reparo de embarcações pré- registradas ou registradas no REB'),
    ('200000019', u'200000019 - Produtos de perfumaria, de toucador e de higiene pessoal a que se refere o § 1º do art. 22 da Instrução Normativa RFB nº 1.234, de 2012, adquiridos de distribuidores e de comerciantes varejistas'),
    ('200000020', u'200000020 - Produtos a que se refere o § 2º do art. 22 da Instrução Normativa RFB nº 1.234, de 2012'),
    ('200000021', u'200000021 - Produtos de que tratam as alíneas “c” a “k” do inciso I do art. 5º da Instrução Normativa RFB nº 1.234, de 2012'),
    ('200000022', u'200000022 - Outros produtos ou serviços beneficiados com isenção, não incidência ou alíquotas zero da Cofins e da Contribuição para o PIS/Pasep, observado o disposto no § 5º do art. 2º da Instrução Normativa RFB nº 1.234, de 2012'),
    ('200000023', u'200000023 - Passagens aéreas, rodoviárias e demais serviços de transporte de passageiros, inclusive, tarifa de embarque, exceto transporte internacional de passageiros'),
    ('200000024', u'200000024 - Transporte internacional de passageiros efetuado por empresas nacionais'),
    ('200000025', u'200000025 - Serviços prestados por associações profissionais ou assemelhadas e cooperativas'),
    ('200000026', u'200000026 - Serviços prestados por bancos comerciais, bancos de investimento, bancos de desenvolvimento, caixas econômicas, sociedades de crédito, financiamento e investimento, sociedades de crédito imobiliário, e câmbio, distribuidoras de títulos e valores mobiliários, empresas de arrendamento mercantil, cooperativas de crédito, empresas de seguros privados e de capitalização e entidades abertas de previdência complementar'),
    ('200000027', u'200000027 - Seguro Saúde'),
    ('200000028', u'200000028 - Serviços de abastecimento de água'),
    ('200000029', u'200000029 - Telefone'),
    ('200000030', u'200000030 - Correio e telégrafos'),
    ('200000031', u'200000031 - Vigilância'),
    ('200000032', u'200000032 - Limpeza'),
    ('200000033', u'200000033 - Locação de mão de obra'),
    ('200000034', u'200000034 - Intermediação de negócios,'),
    ('200000035', u'200000035 - Administração, locação ou cessão de bens imóveis, móveis e direitos de qualquer natureza'),
    ('200000036', u'200000036 - Factoring'),
    ('200000037', u'200000037 - Plano de saúde humano, veterinário ou odontológico com valores fixos por servidor, por empregado ou por animal'),
    ('200000038', u'200000038 - Demais serviços'),
    
]




CHOICES_R4020_RELFONTPG = [

    (500, u'500 - A fonte pagadora é matriz da beneficiária no exterior.'),
    (510, u'510 - A fonte pagadora é filial, sucursal ou agência de beneficiária no exterior.'),
    (520, u'520 - A fonte pagadora é controlada ou coligada da beneficiária no exterior, na forma dos §§ 1º e 2º do art. 243 da Lei nº 6.404, de 15 de dezembro de 1976.'),
    (530, u'530 - A fonte pagadora é controladora ou coligada da beneficiária no exterior, na forma dos §§ 1º e 2º do art. 243 da Lei nº 6.404, de 1976.'),
    (540, u'540 - A fonte pagadora e a beneficiária no exterior estão sob controle societário ou administrativo comum ou quando pelo menos 10% do capital de cada uma, pertencer a uma mesma pessoa física ou jurídica.'),
    (550, u'550 - A fonte pagadora e a beneficiária no exterior têm participação societária no capital de uma terceira pessoa jurídica, cuja soma as caracterize como controladoras ou coligadas na forma dos §§ 1º e 2º do art. 243 da Lei nº 6.404, de 1976.'),
    (560, u'560 - A fonte pagadora ou a beneficiária no exterior mantenha contrato de exclusividade como agente, como distribuidor ou como concessionário nas operações com bens, serviços e direitos.'),
    (570, u'570 - A fonte pagadora e a beneficiária mantêm acordo de atuação conjunta.'),
    (900, u'900 - Não há relação entre a fonte pagadora e a beneficiária no exterior.'),
    
]




CHOICES_R4020_TPINSCADV = [

    (1, u'1 - Pessoa Física'),
    (2, u'2 - Pessoa Jurídica.'),
    
]




CHOICES_R4020_TPPROCRET = [

    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial.'),
    
]



