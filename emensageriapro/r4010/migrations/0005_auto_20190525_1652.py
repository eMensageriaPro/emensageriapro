# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r4010', '0004_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r4010benefpen',
            name='nome',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='r4010benefpen',
            name='reldep',
            field=models.IntegerField(choices=[(1, '1 - Neto, bisneto'), (2, '2 - Irm\xe3o'), (3, '3 - C\xf4njuge/companheiro'), (4, '4 - Filho'), (5, '5 - Pais, av\xf3s e bisav\xf3s'), (6, '6 - Enteado'), (7, '7 - Sogro'), (99, '99 - Agregado/Outros.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010detded',
            name='indtpdeducao',
            field=models.IntegerField(choices=[(1, '1 - Previd\xeancia Oficial'), (2, '2 - Previd\xeancia Privada'), (3, '3 - Fapi'), (4, '4 - Funpresp'), (5, '5 - Pens\xe3o Aliment\xedcia'), (6, '6 - Contribui\xe7\xe3o do ente p\xfablico patrocinador'), (7, '7 - Dependentes.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010detded',
            name='vlrdeducao',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010fci',
            name='nrinscfci',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r4010ideopsaude',
            name='nrinsc',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r4010ideopsaude',
            name='vlrsaude',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010idepgto',
            name='natrend',
            field=models.CharField(choices=[(b'000000001', '000000001 - Decorrente de Decis\xe3o da Justi\xe7a do Trabalho'), (b'000000002', '000000002 - Decorrente de Decis\xe3o da Justi\xe7a Federal'), (b'000000003', '000000003 - Decorrente de Decis\xe3o da Justi\xe7a dos Estados/Distrito Federal'), (b'000000004', '000000004 - Honor\xe1rios advocat\xedcios de sucumb\xeancia pelos advogados e procuradores p\xfablicos de que trata o art. 27 da Lei n\xba 13.327'), (b'000000005', '000000005 - Benef\xedcio do Regime Geral de Previd\xeancia Social'), (b'000000006', '000000006 - Lucro e Dividendo'), (b'000000007', '000000007 - Resgate de Previd\xeancia Complementar - Modalidade Contribui\xe7\xe3o Definida/Vari\xe1vel - N\xe3o Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000008', '000000008 - Resgate de Fundo de Aposentadoria Programada Individual (Fapi)- N\xe3o Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000009', '000000009 - Resgate de Previd\xeancia Complementar - Modalidade Benef\xedcio Definido - N\xe3o Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000010', '000000010 - Resgate de Previd\xeancia Complementar - Modalidade Contribui\xe7\xe3o Definida/Vari\xe1vel - Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000011', '000000011 - Resgate de Fundo de Aposentadoria Programada Individual (Fapi)- Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000012', '000000012 - Resgate de Planos de Seguro de Vida com Cl\xe1usula de Cobertura por Sobreviv\xeancia- Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000013', '000000013 - Resgate de Planos de Seguro de Vida com Cl\xe1usula de Cobertura por Sobreviv\xeancia- N\xe3o Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000014', '000000014 - Benef\xedcio de Previd\xeancia Complementar - Modalidade Contribui\xe7\xe3o Definida/Vari\xe1vel - N\xe3o Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000015', '000000015 - Benef\xedcio de Fundo de Aposentadoria Programada Individual (Fapi)- N\xe3o Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000016', '000000016 - Benef\xedcio de Previd\xeancia Complementar - Modalidade Benef\xedcio Definido - N\xe3o Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000017', '000000017 - Benef\xedcio de Previd\xeancia Complementar - Modalidade Contribui\xe7\xe3o Definida/Vari\xe1vel - Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000018', '000000018 - Benef\xedcio de Fundo de Aposentadoria Programada Individual (Fapi)- Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000019', '000000019 - Benef\xedcio de Planos de Seguro de Vida com Cl\xe1usula de Cobertura por Sobreviv\xeancia- Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000020', '000000020 - Benef\xedcio de Planos de Seguro de Vida com Cl\xe1usula de Cobertura por Sobreviv\xeancia- N\xe3o Optante pela Tributa\xe7\xe3o Exclusiva'), (b'000000021', '000000021 - Juros sobre o Capital Pr\xf3prio'), (b'000000022', '000000022 - Rendimento de Aplica\xe7\xf5es Financeiras de Renda Fixa, decorrentes de aliena\xe7\xe3o, liquida\xe7\xe3o (total ou parcial), resgate, cess\xe3o ou repactua\xe7\xe3o do t\xedtulo ou aplica\xe7\xe3o'), (b'000000023', '000000023 - Rendimentos auferidos pela entrega de recursos \xe0 pessoa jur\xeddica'), (b'000000024', '000000024 - Rendimentos predeterminados obtidos em opera\xe7\xf5es conjugadas realizadas: nos mercados de op\xe7\xf5es de compra e venda em bolsas de valores, de mercadorias e de futuros (box), no mercado a termo nas bolsas de valores, de mercadorias e de futuros, em opera\xe7\xf5es de venda coberta e sem ajustes di\xe1rios, e no mercado de balc\xe3o.'), (b'000000025', '000000025 - Rendimentos obtidos nas opera\xe7\xf5es de transfer\xeancia de d\xedvidas realizadas com institui\xe7\xe3o financeira e outras institui\xe7\xf5es autorizadas a funcionar pelo Banco Central do Brasil'), (b'000000026', '000000026 - Rendimentos peri\xf3dicos produzidos por t\xedtulo ou aplica\xe7\xe3o, bem como qualquer remunera\xe7\xe3o adicional aos rendimentos prefixados'), (b'000000027', '000000027 - Rendimentos auferidos nas opera\xe7\xf5es de m\xfatuo de recursos financeiros'), (b'000000028', '000000028 - Rendimentos auferidos em opera\xe7\xf5es de adiantamento sobre contratos de c\xe2mbio de exporta\xe7\xe3o, n\xe3o sacado (trava de c\xe2mbio), bem como opera\xe7\xf5es com export notes, com deb\xeantures, com dep\xf3sitos volunt\xe1rios para garantia de inst\xe2ncia e com dep\xf3sitos judiciais ou administrativos, quando seu levantamento se der em favor do depositante'), (b'000000029', '000000029 - Rendimentos obtidos nas opera\xe7\xf5es de m\xfatuo e de compra vinculada \xe0 revenda tendo por objeto ouro, ativo financeiro'), (b'000000030', '000000030 - Rendimentos auferidos em contas de dep\xf3sitos de poupan\xe7a'), (b'000000031', '000000031 - Rendimentos auferidos sobre juros produzidos por letras hipotec\xe1rias'), (b'000000032', '000000032 - Rendimentos ou ganhos decorrentes da negocia\xe7\xe3o de t\xedtulos ou valores mobili\xe1rios de renda fixa em bolsas de valores, de mercadorias, de futuros e assemelhadas'), (b'000000033', '000000033 - Rendimentos auferidos em outras aplica\xe7\xf5es financeiras de renda fixa ou de renda vari\xe1vel'), (b'000000034', '000000034 - Rendimentos auferidos em Fundo de Investimento'), (b'000000035', '000000035 - Rendimentos auferidos em Fundos de investimento em quotas de fundos de investimento'), (b'000000036', '000000036 - Rendimentos produzidos por aplica\xe7\xf5es em fundos de investimento em a\xe7\xf5es'), (b'000000037', '000000037 - Rendimentos produzidos por aplica\xe7\xf5es em fundos de investimento em quotas de fundos de investimento em a\xe7\xf5es'), (b'000000038', '000000038 - Rendimentos produzidos por aplica\xe7\xf5es em Fundos M\xfatuos de Privatiza\xe7\xe3o com recursos do Fundo de Garantia por Tempo de Servi\xe7o (FGTS)'), (b'000000039', '000000039 - Rendimentos auferidos pela carteira dos Fundos de Investimento Imobili\xe1rio'), (b'000000040', '000000040 - Rendimentos distribu\xeddos pelo Fundo de Investimento Imobili\xe1rio aos seus cotistas'), (b'000000041', '000000041 - Rendimento auferido pelo cotista no resgate de cotas na liquida\xe7\xe3o do Fundo de Investimento Imobili\xe1rio'), (b'000000042', '000000042 - Rendimentos e ganhos de capital distribu\xeddos pelo Fundo de Investimento Cultural e Art\xedstico (Ficart)'), (b'000000043', '000000043 - Rendimentos e ganhos de capital distribu\xeddos pelo Fundo de Financiamento da Ind\xfastria Cinematogr\xe1fica Nacional (Funcines)'), (b'000000044', '000000044 - Juros n\xe3o especificados'), (b'000000045', '000000045 - Rendimentos auferidos no resgate de quotas de fundos de investimento mantidos com recursos provenientes de convers\xe3o de d\xe9bitos externos brasileiros, e de que participem, exclusivamente, residentes ou domiciliados no exterior'), (b'000000046', '000000046 - Demais rendimentos de capital'), (b'000000047', '000000047 - Rendimentos de Loca\xe7\xe3o ou Subloca\xe7\xe3o'), (b'000000048', '000000048 - Rendimentos de Arrendamento ou Subarrendamento'), (b'000000049', '000000049 - Import\xe2ncias pagas por terceiros por conta do locador do bem (juros, comiss\xf5es etc.)'), (b'000000050', '000000050 - Import\xe2ncias pagas ao locador pelo contrato celebrado (luvas, pr\xeamios etc.)'), (b'000000051', '000000051 - Benfeitorias e quaisquer melhoramentos realizados no bem locado'), (b'000000052', '000000052 - Juros decorrente da aliena\xe7\xe3o a prazo de bens'), (b'000000053', '000000053 - Rendimentos de Direito de Uso ou Passagem de Terrenos e de aproveitamento de \xe1guas'), (b'000000054', '000000054 - Rendimentos de Direito de explora\xe7\xe3o de pel\xedculas cinematogr\xe1ficas, Obras Audiovisuais, e Videof\xf4nicas'), (b'000000055', '000000055 - Rendimentos de  Direito de Conjuntos Industriais e Inven\xe7\xf5es'), (b'000000056', '000000056 - Rendimentos de Direito Autoral'), (b'000000057', '000000057 - Rendimentos de Direito Autoral (quando n\xe3o percebidos pelo autor ou criador da obra)'), (b'000000058', '000000058 - Rendimentos de Direito de Imagem'), (b'000000059', '000000059 - Rendimentos de Direito de colher ou extrair recursos vegetais, pesquisar e extrair recursos minerais'), (b'000000060', '000000060 - Produto da aliena\xe7\xe3o de marcas de ind\xfastria e com\xe9rcio, patentes de inven\xe7\xe3o e processo ou f\xf3rmulas de fabrica\xe7\xe3o'), (b'000000061', '000000061 - Import\xe2ncias pagas por terceiros por conta do cedente dos direitos (juros, comiss\xf5es etc.)'), (b'000000062', '000000062 - Import\xe2ncias pagas ao cedente do direito, pelo contrato celebrado (luvas, pr\xeamios etc.)'), (b'000000063', '000000063 - Despesas para conserva\xe7\xe3o dos direitos cedidos (quando compensadas pelo uso do bem ou direito)'), (b'000000064', '000000064 - Demais Royalties'), (b'000000065', '000000065 - Juros de mora e quaisquer outras compensa\xe7\xf5es pelo atraso no pagamento de royalties'), (b'000000066', '000000066 - Juros decorrente da aliena\xe7\xe3o a prazo de direitos'), (b'000000067', '000000067 - Ganho de capital decorrente da integraliza\xe7\xe3o de cotas de fundos ou clubes de investimento por meio da entrega de ativos financeiros'), (b'000000068', '000000068 - Distribui\xe7\xe3o de Juros sobre o Capital Pr\xf3prio pela companhia emissora de a\xe7\xf5es objeto de empr\xe9stimo'), (b'000000069', '000000069 - Rendimentos de Partes Benefici\xe1rias ou de Fundador'), (b'000000070', '000000070 - Rendimentos auferidos em opera\xe7\xf5es de swap'), (b'000000071', '000000071 - Rendimentos auferidos em opera\xe7\xf5es day trade realizadas em bolsa de valores, de mercadorias, de futuros e assemelhadas'), (b'000000072', '000000072 - Rendimento decorrente de Opera\xe7\xe3o realizada em bolsas de valores, de mercadorias, de futuros, e assemelhadas, exceto day trade'), (b'000000073', '000000073 - Rendimento decorrente de Opera\xe7\xe3o realizada no mercado de balc\xe3o, com intermedia\xe7\xe3o, tendo por objeto a\xe7\xf5es, ouro ativo financeiro e outros valores mobili\xe1rios negociados no mercado \xe0 vista'), (b'000000074', '000000074 - Rendimento decorrente de Opera\xe7\xe3o realizada em mercados de liquida\xe7\xe3o futura fora de bolsa'), (b'000000075', '000000075 - Aliena\xe7\xe3o de bens e direitos do ativo n\xe3o circulante localizados no Brasil'), (b'000000076', '000000076 - Comiss\xf5es, corretagens, ou qualquer outra import\xe2ncia paga/creditada pela representa\xe7\xe3o comercial ou pela media\xe7\xe3o na realiza\xe7\xe3o de neg\xf3cios civis e comerciais'), (b'000000077', '000000077 - Rendimento de Servi\xe7os de propaganda e publicidade'), (b'000000078', '000000078 - Pr\xeamios distribu\xeddos, sob a forma de bens e servi\xe7os, mediante concursos e sorteios'), (b'000000079', '000000079 - Pr\xeamios distribu\xeddos, sob a forma de dinheiro, mediante concursos e sorteios'), (b'000000080', '000000080 - Pr\xeamios de Propriet\xe1rios e Criadores de Cavalos de Corrida'), (b'000000081', '000000081 - Benef\xedcios l\xedquidos resultantes da amortiza\xe7\xe3o antecipada, mediante sorteio, dos t\xedtulos de capitaliza\xe7\xe3o'), (b'000000082', '000000082 - Benef\xedcios atribu\xeddos aos portadores de t\xedtulos de capitaliza\xe7\xe3o nos lucros da empresa emitente'), (b'000000083', '000000083 - Pr\xeamios distribu\xeddos, sob a forma de bens e servi\xe7os, mediante sorteios de jogos de bingo permanente ou eventual'), (b'000000084', '000000084 - Pr\xeamios distribu\xeddos, em dinheiro, obtido mediante sorteios de jogos de bingo permanente ou eventual'), (b'000000085', '000000085 - Import\xe2ncias correspondentes a multas e qualquer outra vantagem, ainda que a t\xedtulo de indeniza\xe7\xe3o, em virtude de rescis\xe3o de contrato'), (b'000000086', '000000086 - Responsabilidade Civil - juros e indeniza\xe7\xf5es por lucros cessantes'), (b'000000087', '000000087 - Import\xe2ncias pagas ou creditadas a cooperativas de trabalho, associa\xe7\xf5es de profissionais ou assemelhadas, relativas a servi\xe7os pessoais que lhes forem prestados por associados destas ou colocados \xe0 disposi\xe7\xe3o'), (b'000000088', '000000088 - Remunera\xe7\xe3o de Servi\xe7os de administra\xe7\xe3o de bens ou neg\xf3cios em geral, exceto cons\xf3rcios ou fundos m\xfatuos para aquisi\xe7\xe3o de bens'), (b'000000089', '000000089 - Remunera\xe7\xe3o de Servi\xe7os de advocacia'), (b'000000090', '000000090 - Remunera\xe7\xe3o de Servi\xe7os de an\xe1lise cl\xednica laboratorial'), (b'000000091', '000000091 - Remunera\xe7\xe3o de Servi\xe7os de an\xe1lises t\xe9cnicas'), (b'000000092', '000000092 - Remunera\xe7\xe3o de Servi\xe7os de arquitetura'), (b'000000093', '000000093 - Remunera\xe7\xe3o de Servi\xe7os de assessoria e consultoria t\xe9cnica, exceto servi\xe7o de assist\xeancia t\xe9cnica prestado a terceiros e concernente a ramo de ind\xfastria ou com\xe9rcio explorado pelo prestador do servi\xe7o,'), (b'000000094', '000000094 - Remunera\xe7\xe3o de Servi\xe7os de assist\xeancia social,'), (b'000000095', '000000095 - Remunera\xe7\xe3o de Servi\xe7os de auditoria,'), (b'000000096', '000000096 - Remunera\xe7\xe3o de Servi\xe7os de avalia\xe7\xe3o e per\xedcia,'), (b'000000097', '000000097 - Remunera\xe7\xe3o de Servi\xe7os de  biologia e biomedicina,'), (b'000000098', '000000098 - Remunera\xe7\xe3o de Servi\xe7os de c\xe1lculo em geral,'), (b'000000099', '000000099 - Remunera\xe7\xe3o de Servi\xe7os de consultoria,'), (b'000000100', '000000100 - Remunera\xe7\xe3o de Servi\xe7os de contabilidade,'), (b'000000101', '000000101 - Remunera\xe7\xe3o de Servi\xe7os de desenho t\xe9cnico,'), (b'000000102', '000000102 - Remunera\xe7\xe3o de Servi\xe7os de economia,'), (b'000000103', '000000103 - Remunera\xe7\xe3o de Servi\xe7os de elabora\xe7\xe3o de projetos,'), (b'000000104', '000000104 - Remunera\xe7\xe3o de Servi\xe7os de engenharia, exceto constru\xe7\xe3o de estradas, pontes, pr\xe9dios e obras assemelhadas,'), (b'000000105', '000000105 - Remunera\xe7\xe3o de Servi\xe7os de  ensino e treinamento,'), (b'000000106', '000000106 - Remunera\xe7\xe3o de Servi\xe7os de estat\xedstica,'), (b'000000107', '000000107 - Remunera\xe7\xe3o de Servi\xe7os de fisioterapia,'), (b'000000108', '000000108 - Remunera\xe7\xe3o de Servi\xe7os de fonoaudiologia,'), (b'000000109', '000000109 - Remunera\xe7\xe3o de Servi\xe7os de geologia,'), (b'000000110', '000000110 - Remunera\xe7\xe3o de Servi\xe7os de leil\xe3o,'), (b'000000111', '000000111 - Remunera\xe7\xe3o de Servi\xe7os de medicina, exceto aquela prestada por ambulat\xf3rio, banco de sangue, casa de sa\xfade, casa de recupera\xe7\xe3o ou repouso sob orienta\xe7\xe3o m\xe9dica, hospital e pronto-socorro,'), (b'000000112', '000000112 - Remunera\xe7\xe3o de Servi\xe7os de nutricionismo e diet\xe9tica,'), (b'000000113', '000000113 - Remunera\xe7\xe3o de Servi\xe7os de odontologia,'), (b'000000114', '000000114 - Remunera\xe7\xe3o de Servi\xe7os de organiza\xe7\xe3o de feiras de amostras, congressos, semin\xe1rios, simp\xf3sios e cong\xeaneres,'), (b'000000115', '000000115 - Remunera\xe7\xe3o de Servi\xe7os de pesquisa em geral,'), (b'000000116', '000000116 - Remunera\xe7\xe3o de Servi\xe7os de planejamento,'), (b'000000117', '000000117 - Remunera\xe7\xe3o de Servi\xe7os de programa\xe7\xe3o,'), (b'000000118', '000000118 - Remunera\xe7\xe3o de Servi\xe7os de  pr\xf3tese,'), (b'000000119', '000000119 - Remunera\xe7\xe3o de Servi\xe7os de  psicologia e psican\xe1lise,'), (b'000000120', '000000120 - Remunera\xe7\xe3o de Servi\xe7os de qu\xedmica,'), (b'000000121', '000000121 - Remunera\xe7\xe3o de Servi\xe7os de radiologia e radioterapia,'), (b'000000122', '000000122 - Remunera\xe7\xe3o de Servi\xe7os de rela\xe7\xf5es p\xfablicas,'), (b'000000123', '000000123 - Remunera\xe7\xe3o de Servi\xe7os de  servi\xe7o de despachante,'), (b'000000124', '000000124 - Remunera\xe7\xe3o de Servi\xe7os de  terap\xeautica ocupacional,'), (b'000000125', '000000125 - Remunera\xe7\xe3o de Servi\xe7os de  tradu\xe7\xe3o ou interpreta\xe7\xe3o comercial,'), (b'000000126', '000000126 - Remunera\xe7\xe3o de Servi\xe7os de urbanismo,'), (b'000000127', '000000127 - Remunera\xe7\xe3o de Servi\xe7os de  veterin\xe1ria.'), (b'000000128', '000000128 - Remunera\xe7\xe3o de Servi\xe7os de Limpeza'), (b'000000129', '000000129 - Remunera\xe7\xe3o de Servi\xe7os de Conserva\xe7\xe3o/ Manuten\xe7\xe3o'), (b'000000130', '000000130 - Remunera\xe7\xe3o de Servi\xe7os de Seguran\xe7a/Vigil\xe2ncia/Transporte de valores'), (b'000000131', '000000131 - Remunera\xe7\xe3o de Servi\xe7os Loca\xe7\xe3o de M\xe3o de obra'), (b'000000132', '000000132 - Remunera\xe7\xe3o de Servi\xe7os de Assessoria Credit\xedcia, Mercadol\xf3gica, Gest\xe3o de Cr\xe9dito, Sele\xe7\xe3o e Riscos e Administra\xe7\xe3o de Contas a Pagar e a Receber'), (b'000000133', '000000133 - Pagamentos Referentes \xe0 Aquisi\xe7\xe3o de Autope\xe7as'), (b'000000134', '000000134 - Rendimentos pago a companhias de navega\xe7\xe3o a\xe9rea e mar\xedtima'), (b'000000135', '000000135 - Demais pagamentos a entidades imunes ou isentas'), (b'200000001', '200000001 - Alimenta\xe7\xe3o'), (b'200000002', '200000002 - Energia el\xe9trica'), (b'200000003', '200000003 - Servi\xe7os prestados com emprego de materiais'), (b'200000004', '200000004 - Constru\xe7\xe3o Civil por empreitada com emprego de materiais'), (b'200000005', '200000005 - Servi\xe7os hospitalares de que trata o art. 30 da Instru\xe7\xe3o Normativa RFB n\xba 1.234, de 11 de janeiro de 2012'), (b'200000006', '200000006 - Transporte nacional de cargas'), (b'200000007', '200000007 - Servi\xe7os de aux\xedlio diagn\xf3stico e terapia, patologia cl\xednica, imagenologia, anatomia patol\xf3gica e citopatol\xf3gica, medicina nuclear e an\xe1lises e patologias cl\xednicas, exames por m\xe9todos gr\xe1ficos, procedimentos endosc\xf3picos, radioterapia, quimioterapia, di\xe1lise e oxigenoterapia hiperb\xe1rica de que trata o art. 31 e par\xe1grafo \xfanico da Instru\xe7\xe3o Normativa RFB n\xba 1.234, de 2012'), (b'200000008', '200000008 - Produtos farmac\xeauticos, de perfumaria, de toucador ou de higiene pessoal adquiridos de produtor, importador, distribuidor ou varejista,'), (b'200000009', '200000009 - Mercadorias e bens em geral'), (b'200000010', '200000010 - Gasolina, inclusive de avia\xe7\xe3o, \xf3leo diesel, g\xe1s liquefeito de petr\xf3leo (GLP), combust\xedveis derivados de petr\xf3leo ou de g\xe1s natural, querosene de avia\xe7\xe3o (QAV), e demais produtos derivados de petr\xf3leo, adquiridos de refinarias de petr\xf3leo, de demais produtores, de importadores, de distribuidor ou varejista'), (b'200000011', '200000011 - \xc1lcool et\xedlico hidratado, inclusive para fins carburantes, adquirido diretamente de produtor, importador ou do distribuidor'), (b'200000012', '200000012 - Biodiesel adquirido de produtor ou importador'), (b'200000013', '200000013 - Gasolina, exceto gasolina de avia\xe7\xe3o, \xf3leo diesel e g\xe1s liquefeito de petr\xf3leo (GLP), derivados de petr\xf3leo ou de g\xe1s natural e querosene de avia\xe7\xe3o adquiridos de distribuidores e comerciantes varejistas'), (b'200000014', '200000014 - \xc1lcool et\xedlico hidratado nacional, inclusive para fins carburantes adquirido de comerciante varejista'), (b'200000015', '200000015 - Biodiesel adquirido de distribuidores e comerciantes varejistas'), (b'200000016', '200000016 - Biodiesel adquirido de produtor detentor regular do selo \u201cCombust\xedvel Social\u201d, fabricado a partir de mamona ou fruto, caro\xe7o ou am\xeandoa de palma produzidos nas regi\xf5es norte e nordeste e no semi\xe1rido, por agricultor familiar enquadrado no Programa Nacional de Fortalecimento da Agricultura Familiar (Pronaf)'), (b'200000017', '200000017 - Transporte internacional de cargas efetuado por empresas nacionais'), (b'200000018', '200000018 - Estaleiros navais brasileiros nas atividades de Constru\xe7\xe3o, conserva\xe7\xe3o, moderniza\xe7\xe3o, convers\xe3o e reparo de embarca\xe7\xf5es pr\xe9- registradas ou registradas no REB'), (b'200000019', '200000019 - Produtos de perfumaria, de toucador e de higiene pessoal a que se refere o \xa7 1\xba do art. 22 da Instru\xe7\xe3o Normativa RFB n\xba 1.234, de 2012, adquiridos de distribuidores e de comerciantes varejistas'), (b'200000020', '200000020 - Produtos a que se refere o \xa7 2\xba do art. 22 da Instru\xe7\xe3o Normativa RFB n\xba 1.234, de 2012'), (b'200000021', '200000021 - Produtos de que tratam as al\xedneas \u201cc\u201d a \u201ck\u201d do inciso I do art. 5\xba da Instru\xe7\xe3o Normativa RFB n\xba 1.234, de 2012'), (b'200000022', '200000022 - Outros produtos ou servi\xe7os beneficiados com isen\xe7\xe3o, n\xe3o incid\xeancia ou al\xedquotas zero da Cofins e da Contribui\xe7\xe3o para o PIS/Pasep, observado o disposto no \xa7 5\xba do art. 2\xba da Instru\xe7\xe3o Normativa RFB n\xba 1.234, de 2012'), (b'200000023', '200000023 - Passagens a\xe9reas, rodovi\xe1rias e demais servi\xe7os de transporte de passageiros, inclusive, tarifa de embarque, exceto transporte internacional de passageiros'), (b'200000024', '200000024 - Transporte internacional de passageiros efetuado por empresas nacionais'), (b'200000025', '200000025 - Servi\xe7os prestados por associa\xe7\xf5es profissionais ou assemelhadas e cooperativas'), (b'200000026', '200000026 - Servi\xe7os prestados por bancos comerciais, bancos de investimento, bancos de desenvolvimento, caixas econ\xf4micas, sociedades de cr\xe9dito, financiamento e investimento, sociedades de cr\xe9dito imobili\xe1rio, e c\xe2mbio, distribuidoras de t\xedtulos e valores mobili\xe1rios, empresas de arrendamento mercantil, cooperativas de cr\xe9dito, empresas de seguros privados e de capitaliza\xe7\xe3o e entidades abertas de previd\xeancia complementar'), (b'200000027', '200000027 - Seguro Sa\xfade'), (b'200000028', '200000028 - Servi\xe7os de abastecimento de \xe1gua'), (b'200000029', '200000029 - Telefone'), (b'200000030', '200000030 - Correio e tel\xe9grafos'), (b'200000031', '200000031 - Vigil\xe2ncia'), (b'200000032', '200000032 - Limpeza'), (b'200000033', '200000033 - Loca\xe7\xe3o de m\xe3o de obra'), (b'200000034', '200000034 - Intermedia\xe7\xe3o de neg\xf3cios,'), (b'200000035', '200000035 - Administra\xe7\xe3o, loca\xe7\xe3o ou cess\xe3o de bens im\xf3veis, m\xf3veis e direitos de qualquer natureza'), (b'200000036', '200000036 - Factoring'), (b'200000037', '200000037 - Plano de sa\xfade humano, veterin\xe1rio ou odontol\xf3gico com valores fixos por servidor, por empregado ou por animal'), (b'200000038', '200000038 - Demais servi\xe7os')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='r4010idepgto',
            name='paisresid',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='r4010infodependpl',
            name='nome',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infodependpl',
            name='reldep',
            field=models.IntegerField(choices=[(1, '1 - Neto, bisneto'), (2, '2 - Irm\xe3o'), (3, '3 - C\xf4njuge/companheiro'), (4, '4 - Filho'), (5, '5 - Pais, av\xf3s e bisav\xf3s'), (6, '6 - Enteado'), (7, '7 - Sogro'), (99, '99 - Agregado/Outros.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010infodependpl',
            name='vlrsaude',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infopgto',
            name='dtfg',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='r4010infopgto',
            name='inddecterc',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infopgto',
            name='vlrrendbruto',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infopgtoext',
            name='dsclograd',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infopgtoext',
            name='frmtribut',
            field=models.CharField(choices=[(b'10', '10 - Reten\xe7\xe3o do IRRF - al\xedquota padr\xe3o.'), (b'11', '11 - Reten\xe7\xe3o do IRRF - al\xedquota da tabela progressiva.'), (b'12', '12 - Reten\xe7\xe3o do IRRF - al\xedquota diferenciada (pa\xedses com tributa\xe7\xe3o favorecida).'), (b'13', '13 - Reten\xe7\xe3o do IRRF - al\xedquota limitada conforme cl\xe1usula em conv\xeanio.'), (b'30', '30 - Reten\xe7\xe3o do IRRF - outras hip\xf3teses.'), (b'40', '40 - N\xe3o reten\xe7\xe3o do IRRF - isen\xe7\xe3o estabelecida em conv\xeanio.'), (b'41', '41 - N\xe3o reten\xe7\xe3o do IRRF - isen\xe7\xe3o prevista em lei interna'), (b'42', '42 - N\xe3o reten\xe7\xe3o do IRRF - al\xedquota Zero prevista em lei interna'), (b'43', '43 - N\xe3o reten\xe7\xe3o do IRRF - pagamento antecipado do imposto'), (b'44', '44 - N\xe3o reten\xe7\xe3o do IRRF - medida Judicial'), (b'50', '50 - N\xe3o reten\xe7\xe3o do IRRF - outras hip\xf3teses')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infopgtoext',
            name='indnif',
            field=models.IntegerField(choices=[(1, '1 - Benefici\xe1rio com NIF'), (2, '2 - Benefici\xe1rio dispensado do NIF'), (3, '3 - Pa\xeds n\xe3o exige NIF.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocjud',
            name='indorigrec',
            field=models.IntegerField(choices=[(1, '1 - Recursos do pr\xf3prio declarante'), (2, '2 - Recursos de terceiros - Declarante \xe9 a Institui\xe7\xe3o Financeira respons\xe1vel apenas pelo repasse dos valores.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocjud',
            name='nrproc',
            field=models.CharField(max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocjuddespprocjud',
            name='vlrdespadvogados',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocjuddespprocjud',
            name='vlrdespcustas',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocjudideadv',
            name='nrinscadv',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocjudideadv',
            name='tpinscadv',
            field=models.IntegerField(choices=[(1, '1 - Pessoa F\xedsica'), (2, '2 - Pessoa Jur\xeddica.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocjudideadv',
            name='vlradv',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocjudorigemrec',
            name='cnpjorigrecurso',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocret',
            name='nrprocret',
            field=models.CharField(max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='r4010infoprocret',
            name='tpprocret',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforeemb',
            name='nrinsc',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforeemb',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforeemb',
            name='vlrreemb',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforeembdep',
            name='nrinsc',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforeembdep',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforeembdep',
            name='vlrreemb',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforra',
            name='descrra',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforra',
            name='indorigrec',
            field=models.IntegerField(choices=[(1, '1 - Recursos do pr\xf3prio declarante'), (2, '2 - Recursos de terceiros - Declarante \xe9 a Institui\xe7\xe3o Financeira respons\xe1vel apenas pelo repasse dos valores.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforra',
            name='qtdmesesrra',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforra',
            name='tpprocrra',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforradespprocjud',
            name='vlrdespadvogados',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforradespprocjud',
            name='vlrdespcustas',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforraideadv',
            name='nrinscadv',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforraideadv',
            name='tpinscadv',
            field=models.IntegerField(choices=[(1, '1 - Pessoa F\xedsica'), (2, '2 - Pessoa Jur\xeddica.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforraideadv',
            name='vlradv',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforraorigemrec',
            name='cnpjorigrecurso',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r4010rendisento',
            name='tpisencao',
            field=models.IntegerField(choices=[(1, '1 - Parcela Isenta 65 anos'), (2, '2 - Di\xe1ria de viagem'), (3, '3 - Indeniza\xe7\xe3o e rescis\xe3o de contrato, inclusive a t\xedtulo de PDV'), (4, '4 - Abono pecuni\xe1rio'), (5, '5 - Valores pagos a titular ou s\xf3cio de microempresa ou empresa de pequeno porte, exceto pr\xf3-labore e alugueis'), (6, '6 - Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o'), (7, '7 - Complementa\xe7\xe3o de aposentadoria, correspondente \xe0s contribui\xe7\xf5es efetuadas no per\xedodo de 01/01/1989 a 31/12/1995'), (8, '8 - Ajuda de custo'), (99, '99 - Outros (especificar).')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010rendisento',
            name='vlrisento',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r4010scp',
            name='nrinscscp',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r4010scp',
            name='percscp',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]