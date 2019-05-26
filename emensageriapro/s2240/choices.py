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



CHOICES_S2240_APOSENTESP_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_CODATIV_INIEXPRISCO = [

    ('01.001', u'01.001 - Trabalho ou operações, em contato permanente com pacientes em isolamento por doenças infecto-contagiosas, bem como objetos de seu uso, não previamente esterilizados.'),
    ('01.002', u'01.002 - Trabalho ou operações, em contato permanente com carnes, glândulas, vísceras, sangue, ossos, couros, pelos e dejeções de animais portadores de doenças infecto-contagiosas (carbunculose, brucelose, tuberculose).'),
    ('01.003', u'01.003 - Trabalho ou operações, em contato permanente com esgotos (galerias, fossas e tanques).'),
    ('01.004', u'01.004 - Trabalho ou operações, em contato permanente com lixo urbano (coleta e industrialização).'),
    ('01.005', u'01.005 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em hospitais, serviços de emergência, enfermarias, ambulatórios, postos de vacinação e outros estabelecimentos destinados aos cuidados da saúde humana.'),
    ('01.006', u'01.006 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em hospitais, ambulatórios, postos de vacinação e outros estabelecimentos destinados ao atendimento e tratamento de animais (aplica se apenas ao pessoal que tenha contato com tais animais).'),
    ('01.007', u'01.007 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em contato em laboratórios, com animais destinados ao preparo de soro, vacinas e outros produtos. Inclui os trabalhos com animais infectados para tratamento ou para o preparo de soro, vacinas e outros produtos.'),
    ('01.008', u'01.008 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em laboratórios de análise clínica e histopatologia. Inclui os trabalhos em laboratórios de autópsia, de anatomia e anátomo-histologia.'),
    ('01.009', u'01.009 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em gabinetes de autópsias, de anatomia e histoanatomopatologia (aplica-se somente ao pessoal técnico).'),
    ('01.010', u'01.010 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em cemitérios (exumação de corpos).'),
    ('01.011', u'01.011 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em estábulos e cavalariças.'),
    ('01.012', u'01.012 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em resíduos de animais deteriorados.'),
    ('01.013', u'01.013 - Trabalho de exumação de corpos e manipulação de resíduos de animais deteriorados.'),
    ('01.014', u'01.014 - Esvaziamento de biodigestores.'),
    ('02.001', u'02.001 - Extração e manipulação de arsênico e preparação de seus compostos.'),
    ('02.002', u'02.002 - Fabricação e preparação de tintas à base de arsênico.'),
    ('02.003', u'02.003 - Fabricação de produtos parasiticidas, inseticidas e raticidas contendo compostos de arsênico.'),
    ('02.004', u'02.004 - Pintura a pistola com pigmentos de compostos de arsênico, em recintos limitados ou fechados.'),
    ('02.005', u'02.005 - Preparação do Secret.'),
    ('02.006', u'02.006 - Produção de trióxido de arsênico.'),
    ('02.007', u'02.007 - Bronzeamento em negro e verde com compostos de arsênico.'),
    ('02.008', u'02.008 - Conservação e peles e plumas, depilação de peles à base de compostos de arsênico.'),
    ('02.009', u'02.009 - Descoloração de vidros e cristais à base de compostos de arsênico.'),
    ('02.010', u'02.010 - Emprego de produtos parasiticidas, inseticidas e raticidas à base de compostos de arsênico.'),
    ('02.011', u'02.011 - Fabricação de cartas de jogar, papéis pintados e flores artificiais à base de compostos de arsênico.'),
    ('02.012', u'02.012 - Metalurgia de minérios arsenicais (ouro, prata, chumbo, zinco, níquel, antimônio, cobalto e ferro).'),
    ('02.013', u'02.013 - Operações de galvanotécnica à base de compostos de arsênico.'),
    ('02.014', u'02.014 - Pintura manual (pincel, rolo e escova) com pigmentos de compostos de arsênico em recintos limitados ou fechados, exceto com pincel capilar.'),
    ('02.015', u'02.015 - Empalhamento de animais à base de compostos de arsênico.'),
    ('02.016', u'02.016 - Fabricação de tafetá “sire”.'),
    ('02.017', u'02.017 - Pintura a pistola ou manual com pigmentos de compostos de arsênico ao ar livre.'),
    ('02.018', u'02.018 - Trabalho permanente com carvão no subsolo em operações de corte, furação e desmonte, de carregamento no local de desmonte, em atividades de manobra, nos pontos de transferência de carga e de viradores.'),
    ('02.019', u'02.019 - Atividades permanentes com carvão do subsolo compreendendo serviços, tais como: operações de locomotiva, condutores, engatadores, bombeiros, madeireiros, trilheiros e eletricistas.'),
    ('02.020', u'02.020 - Atividades permanentes de superfície com carvão nas operações a seco, com britadores, peneiras, classificadores, carga e descarga de silos, de transportadores de correia e de teleférreos.'),
    ('02.021', u'02.021 - Fabricação de compostos de chumbo, carbonato, arseniato, cromato mínio, litargírio e outros.'),
    ('02.022', u'02.022 - Fabricação de esmaltes, vernizes, cores, pigmentos, tintas, unguentos, óleos, pastas, líquidos e pós à base de compostos de chumbo.'),
    ('02.023', u'02.023 - Fabricação e restauração de acumuladores, pilhas e baterias elétricas contendo compostos de chumbo.'),
    ('02.024', u'02.024 - Fabricação e emprego de chumbo tetraetila e chumbo tetrametila.'),
    ('02.025', u'02.025 - Fundição e laminação de chumbo, de zinco velho cobre e latão.'),
    ('02.026', u'02.026 - Limpeza, raspagem e reparação de tanques de mistura, armazenamento e demais trabalhos com gasolina contendo chumbo tetraetila.'),
    ('02.027', u'02.027 - Pintura a pistola com pigmentos de compostos de chumbo em recintos limitados ou fechados.'),
    ('02.028', u'02.028 - Vulcanização de borracha pelo litargírio ou outros compostos de chumbo.'),
    ('02.029', u'02.029 - Aplicação e emprego de esmaltes, vernizes, cores, pigmentos, tintas, unguentos, óleos, pastas, líquidos e pós à base de compostos de chumbo.'),
    ('02.030', u'02.030 - Fabricação de porcelana com esmaltes de compostos de chumbo.'),
    ('02.031', u'02.031 - Pintura e decoração manual (pincel, rolo e escova) com pigmentos de compostos de chumbo (exceto pincel capilar), em recintos limitados ou fechados.'),
    ('02.032', u'02.032 - Tinturaria e estamparia com pigmentos à base de compostos de chumbo.'),
    ('02.033', u'02.033 - Pintura a pistola ou manual com pigmentos de compostos de chumbo ao ar livre.'),
    ('02.034', u'02.034 - Fabricação de cromatos e bicromatos.'),
    ('02.035', u'02.035 - Pintura a pistola com pigmentos de compostos de cromo, em recintos limitados ou fechados.'),
    ('02.036', u'02.036 - Cromagem eletrolítica dos metais.'),
    ('02.037', u'02.037 - Fabricação de palitos fosfóricos à base de compostos de cromo (preparação da pasta e trabalho nos secadores).'),
    ('02.038', u'02.038 - Manipulação de cromatos e bicromatos.'),
    ('02.039', u'02.039 - Pintura manual com pigmentos de compostos de cromo em recintos limitados ou fechados (exceto pincel capilar).'),
    ('02.040', u'02.040 - Preparação por processos fotomecânicos de clichês para impressão à base de compostos de cromo.'),
    ('02.041', u'02.041 - Tanagem a cromo.'),
    ('02.042', u'02.042 - Extração e preparação de fósforo branco e seus compostos.'),
    ('02.043', u'02.043 - Fabricação de defensivos fosforados e organofosforados.'),
    ('02.044', u'02.044 - Fabricação de projéteis incendiários, explosivos e gases asfixiantes à base de fósforo branco.'),
    ('02.045', u'02.045 - Emprego de defensivos organofosforados.'),
    ('02.046', u'02.046 - Fabricação de bronze fosforado.'),
    ('02.047', u'02.047 - Fabricação de mechas fosforadas para lâmpadas de mineiros.'),
    ('02.048', u'02.048 - Destilação do alcatrão da hulha.'),
    ('02.049', u'02.049 - Destilação do petróleo.'),
    ('02.050', u'02.050 - Manipulação de alcatrão, breu, betume, antraceno, óleos minerais, óleo queimado, parafina ou outras substâncias cancerígenas afins.'),
    ('02.051', u'02.051 - Fabricação de fenóis, cresóis, naftóis, nitroderivados, aminoderivados, derivados halogenados e outras substâncias tóxicas derivadas de hidrocarbonetos cíclicos.'),
    ('02.052', u'02.052 - Pintura a pistola com esmaltes, tintas, vernizes e solventes contendo hidrocarbonetos aromáticos.'),
    ('02.053', u'02.053 - Emprego de defensivos organoclorados: DDT (diclorodifeniltricloretano), DDD (diclorodifenildicloretano), metoxicloro (dimetoxidifeniltricloretano), BHC (hexacloreto de benzeno) e seus compostos e isômeros.'),
    ('02.054', u'02.054 - Emprego de defensivos derivados do ácido carbônico.'),
    ('02.055', u'02.055 - Emprego de aminoderivados de hidrocarbonetos aromáticos (homólogos da anilina).'),
    ('02.056', u'02.056 - Emprego de cresol, naftaleno e derivados tóxicos.'),
    ('02.057', u'02.057 - Emprego de isocianatos na formação de poliuretanas (lacas de desmoldagem, lacas de dupla composição, lacas protetoras de madeira e metais, adesivos especiais e outros produtos à base de poliisocianetos e poliuretanas).'),
    ('02.058', u'02.058 - Emprego de produtos contendo hidrocarbonetos aromáticos como solventes ou em limpeza de peças.'),
    ('02.059', u'02.059 - Fabricação de artigos de borracha, de produtos para impermeabilização e de tecidos impermeáveis à base de hidrocarbonetos.'),
    ('02.060', u'02.060 - Fabricação de linóleos, celuloides, lacas, tintas, esmaltes, vernizes, solventes, colas, artefatos de ebonite, guta-percha, chapéus de palha e outros à base de hidrocarbonetos.'),
    ('02.061', u'02.061 - Limpeza de peças ou motores com óleo diesel aplicado sob pressão (nebulização).'),
    ('02.062', u'02.062 - Pintura a pincel com esmaltes, tintas e vernizes em solvente contendo hidrocarbonetos aromáticos.'),
    ('02.063', u'02.063 - Fabricação e manipulação de compostos orgânicos de mercúrio.'),
    ('02.064', u'02.064 - Operações que desprendam poeira de silicatos em trabalhos permanentes no subsolo, em minas e túneis (operações de corte, furação, desmonte, carregamentos e outras atividades exercidas no local do desmonte e britagem no subsolo).'),
    ('02.065', u'02.065 - Operações de extração, trituração e moagem de talco.'),
    ('02.066', u'02.066 - Fabricação de material refratário, como refratários para fôrmas, chaminés e cadinhos, recuperação de resíduos.'),
    ('02.067', u'02.067 - Exposição ou contato, por qualquer via com 4-amino difenil (p-xenilamina).'),
    ('02.068', u'02.068 - Produção de Benzidina.'),
    ('02.069', u'02.069 - Exposição ou contato, por qualquer via com Betanaftilamina.'),
    ('02.070', u'02.070 - Exposição ou contato, por qualquer via com 4-nitrodifenil.'),
    ('02.071', u'02.071 - Operações com Éter bis (cloro-metílico).'),
    ('02.072', u'02.072 - Operações com Benzopireno.'),
    ('02.073', u'02.073 - Operações com Berílio.'),
    ('02.074', u'02.074 - Operações com Cloreto de dimetil-carbamila.'),
    ('02.075', u'02.075 - Operações com 3,3"-dicloro-benzidina.'),
    ('02.076', u'02.076 - Operações com Dióxido de vinil ciclohexano.'),
    ('02.077', u'02.077 - Operações com Epicloridrina.'),
    ('02.078', u'02.078 - Operações com Hexametilfosforamida.'),
    ('02.079', u'02.079 - Operações com 4,4"-metileno bis (2-cloro anilina).'),
    ('02.080', u'02.080 - Operações com 4,4"-metileno dianilina.'),
    ('02.081', u'02.081 - Operações com Nitrosaminas.'),
    ('02.082', u'02.082 - Operações com Propano sultone.'),
    ('02.083', u'02.083 - Operações com Betapropiolactona.'),
    ('02.084', u'02.084 - Operações com Tálio.'),
    ('02.085', u'02.085 - Produção de trióxido de amônio.'),
    ('02.086', u'02.086 - Ustulação de sulfeto de níquel.'),
    ('02.087', u'02.087 - Aplicação a pistola de tintas de alumínio.'),
    ('02.088', u'02.088 - Fabricação de pós de alumínio (trituração e moagem).'),
    ('02.089', u'02.089 - Fabricação de emetina e pulverização de ipeca.'),
    ('02.090', u'02.090 - Fabricação e manipulação de ácido oxálico, nítrico sulfúrico, bromídrico, fosfórico, pícrico.'),
    ('02.091', u'02.091 - Metalização a pistola.'),
    ('02.092', u'02.092 - Operações com o timbó.'),
    ('02.093', u'02.093 - Operações com bagaço de cana nas fases de grande exposição à poeira.'),
    ('02.094', u'02.094 - Operações de galvanoplastia: douração, prateação, niquelagem, cromagem, zincagem, cobreagem, anodização de alumínio.'),
    ('02.095', u'02.095 - Telegrafia e radiotelegrafia, manipulação em aparelhos do tipo Morse e recepção de sinais em fones.'),
    ('02.096', u'02.096 - Trabalhos com escórias de Thomás: remoção, trituração, moagem e acondicionamento.'),
    ('02.097', u'02.097 - Trabalho de retirada, raspagem a seco e queima de pinturas.'),
    ('02.098', u'02.098 - Trabalhos na extração de sal (salinas).'),
    ('02.099', u'02.099 - Fabricação e manuseio de álcalis cáusticos.'),
    ('02.100', u'02.100 - Fabricação e transporte de cal e cimento nas fases de grande exposição a poeiras.'),
    ('02.101', u'02.101 - Trabalhos de carregamento, descarregamento ou remoção de enxofre ou sulfitos em geral, em sacos ou a granel.'),
    ('02.102', u'02.102 - Trabalhos com exposição a manganês no subsolo.'),
    ('03.001', u'03.001 - Armazenamento de explosivos.'),
    ('03.002', u'03.002 - Transporte de explosivos.'),
    ('03.003', u'03.003 - Operação de escorva dos cartuchos de explosivos.'),
    ('03.004', u'03.004 - Operação de carregamento de explosivos.'),
    ('03.005', u'03.005 - Detonação de explosivos.'),
    ('03.006', u'03.006 - Verificação de detonações de explosivos falhadas.'),
    ('03.007', u'03.007 - Queima e destruição de explosivos deteriorados.'),
    ('03.008', u'03.008 - Operações de manuseio de explosivos.'),
    ('04.001', u'04.001 - Produção, transporte, processamento e armazenamento de gás liquefeito.'),
    ('04.002', u'04.002 - Transporte e armazenagem de inflamáveis líquidos e gasosos liquefeitos e de vasilhames vazios não-desgaseificados ou decantados (todos os trabalhadores da área de operação).'),
    ('04.003', u'04.003 - Reabastecimento de aeronaves (todos os trabalhadores nessas atividades ou que operam na área de risco).'),
    ('04.004', u'04.004 - Operações nos locais de carregamento de navios-tanques, vagões-tanques e caminhões-tanques e enchimento de vasilhames, com inflamáveis líquidos ou gasosos liquefeitos (todos os trabalhadores nessas atividades ou que operam na área de risco).'),
    ('04.005', u'04.005 - Operações nos locais de descarga de navios-tanques, vagões-tanques e caminhões-tanques com inflamáveis líquidos ou gasosos liquefeitos ou de vasilhames vazios não-desgaseificados ou decantados (todos os trabalhadores nessas atividades ou que operam na área de risco).'),
    ('04.006', u'04.006 - Serviços de operações e manutenção de navios-tanque, vagões-tanques, caminhões-tanques, bombas e vasilhames, com inflamáveis líquidos ou gasosos liquefeitos, ou vazios não-desgaseificados ou decantados (todos os trabalhadores nessas atividades ou que operam na área de risco).'),
    ('04.007', u'04.007 - Operações de desgaseificação, decantação e reparos de vasilhames de inflamáveis não-desgaseificados ou decantados (todos os trabalhadores nessas atividades ou que operam na área de risco).'),
    ('04.008', u'04.008 - operações de testes de aparelhos de consumo do gás e seus equipamentos (todos os trabalhadores nessas atividades ou que operam na área de risco).'),
    ('04.009', u'04.009 - transporte de inflamáveis líquidos e gasosos liquefeitos em caminhão-tanque (motorista e ajudantes).'),
    ('04.010', u'04.010 - transporte de vasilhames (em caminhões de carga), contendo inflamável líquido, em quantidade total igual ou superior a 200 litros (motorista e ajudantes).'),
    ('04.011', u'04.011 - transporte de vasilhames (em carreta ou caminhão de carga), contendo inflamável gasosos e líquido, em quantidade total igual ou superior a 135 quilos (motorista e ajudantes).'),
    ('04.012', u'04.012 - operação em postos de serviço e bombas de abastecimento de inflamáveis líquidos (operador de bomba e trabalhadores que operam na área de risco).'),
    ('04.013', u'04.013 - Trabalho em poços de petróleo em produção de gás (círculo com raio de 30 metros, no mínimo, com centro na boca do poço).'),
    ('04.014', u'04.014 - Trabalho em unidade de processamento das refinarias (Faixa de 30 metros de largura, no mínimo, contornando a área de operação).'),
    ('04.015', u'04.015 - Operações com inflamáveis em refinaria, em estado de volatilização ou possibilidade de volatilização decorrente de falha ou defeito dos sistemas de segurança e fechamento das válvulas (Faixa de 15 metros de largura, no mínimo, contornando a área de operação).'),
    ('04.016', u'04.016 - Operações em tanques de inflamáveis líquidos (Toda a bacia de segurança).'),
    ('04.017', u'04.017 - Operações em tanques elevados de inflamáveis gasosos (Círculo com raio de 3 metros com centro nos pontos de vazamento eventual (válvula registros, dispositivos de medição por escapamento, gaxetas)).'),
    ('04.018', u'04.018 - Carga e descarga de inflamáveis líquidos contidos em navios, chatas e batelões (Afastamento de 15 metros da beira do cais, durante a operação, com extensão correspondente ao comprimento da embarcação).'),
    ('04.019', u'04.019 - Abastecimento de aeronaves (Toda a área de operação).'),
    ('04.020', u'04.020 - Enchimento de vagões - tanques e caminhões - tanques com inflamáveis líquidos (Círculo com raio de 15 metros com centro nas bocas de enchimento dos tanques).'),
    ('04.021', u'04.021 - Enchimento de vagões-tanques e caminhões-tanques inflamáveis gasosos liquefeitos (Círculo com 7,5 metros centro nos pontos de vazamento eventual (válvula e registros)).'),
    ('04.022', u'04.022 - Enchimento de vasilhames com inflamáveis gasosos liquefeitos (Círculos com raio de 15 metros com centro nos bicos de enchimentos).'),
    ('04.023', u'04.023 - Enchimento de vasilhames com inflamáveis líquidos, em locais abertos (Círculo com raio de 7,5 metros com centro nos bicos de enchimento).'),
    ('04.024', u'04.024 - Enchimento de vasilhames com inflamáveis líquidos, em recinto fechado (Toda a área interna do recinto).'),
    ('04.025', u'04.025 - Manutenção de viaturas-tanques, bombas e vasilhames que continham inflamável líquido (Local de operação, acrescido de faixa de 7,5 metros de largura em torno dos seus pontos externos).'),
    ('04.026', u'04.026 - Desgaseificação, decantação e reparos de vasilhames não desgaseificados ou decantados, utilizados no transporte de inflamáveis (Local da operação, acrescido de faixa de 7,5 metros de largura em torno dos seus pontos externos).'),
    ('04.027', u'04.027 - Testes em aparelhos de consumo de gás e seus equipamentos (Local da operação, acrescido de faixa de 7,5 metros de largura em torno dos seus pontos extremos).'),
    ('04.028', u'04.028 - Abastecimento de inflamáveis (Toda a área de operação, abrangendo, no mínimo, círculo com raio de 7,5 metros com centro no ponto de abastecimento e o círculo com raio de 7,5 metros com centro na bomba de abastecimento da viatura e faixa de 7,5 metros de largura para ambos os lados da máquina).'),
    ('04.029', u'04.029 - Armazenamento de vasilhames que contenham inflamáveis líquidos ou vazios não desgaseificados ou decantados, em locais abertos (Faixa de 3 metros de largura em torno dos seus pontos externos).'),
    ('04.030', u'04.030 - Armazenamento de vasilhames que contenham inflamáveis líquidos ou vazios não desgaseificados, ou decantados, em recinto fechado (Toda a área interna do recinto).'),
    ('04.031', u'04.031 - Carga e descarga de vasilhames contendo inflamáveis líquidos ou vasilhames vazios não desgaseificados ou decantados, transportados pôr navios, chatas ou batelões (Afastamento de 3 metros da beira do cais, durante a operação, com extensão correspondente ao comprimento da embarcação).'),
    ('05.001', u'05.001 - Produção, utilização, processamento, transporte, guarda, estocagem, e manuseio de materiais radioativos, selados e não selados, de estado físico e forma química quaisquer, naturais ou artificiais (Minas e depósitos de materiais radioativos. Plantas-piloto e usinas de beneficiamento de minerais radioativos. Outras áreas sujeitas a risco potencial devido às radiações ionizantes), incluindo: a) Prospecção, mineração, operação, beneficiamento e processamento de minerais radioativos (Lixiviação de minerais radioativos para a produção de concentrados de urânio e tório. Purificação de concentrados e conversão em outras formas para uso como combustível nuclear), b) Produção, transformação e tratamento de materiais nucleares para o ciclo do combustível nuclear (Produção de fluoretos de urânio para a produção de hexafluoreto e urânio metálico. Instalações para enriquecimento isotópico e reconversão. Fabricação do elemento combustível nuclear. Instalações para armazenamento dos elementos combustíveis usados. Instalações para o retratamento do combustível irradiado Instalações para o tratamento e deposições, provisórias e finais, dos rejeitos radioativos naturais e artificiais), c) Produção de radioisótopos para uso em medicina, agricultura agropecuária, pesquisa científica e tecnológica (Laboratórios para a produção de radioisótopos e moléculas marcadas), d) Produção de Fontes Radioativas (Instalações para tratamento do material radioativo e confecção de fontes. Laboratórios de testes, ensaios e calibração de fontes, detectores e monitores de radiação, com fontes radioativas) e) Testes, ensaios e calibração de detectores e monitores de radiação com fontes de radiação (Laboratórios de ensaios para materiais radioativos. Laboratórios de radioquímica), f) Descontaminação de superfícies, instrumentos, máquinas, ferramentas, utensílios de laboratório, vestimentas e de quaisquer outras áreas ou bens duráveis contaminados com material radioativo (Laboratórios para descontaminação de peças e materiais radioativos Coleta de rejeitos radioativos em instalações, prédios e em áreas abertas. Lavanderia para roupas contaminadas. Transporte de materiais e rejeitos radioativos, condicionamento, estocagens e sua deposição), g) Separação isotópica e processamento radioquímico (Instalações para tratamento, condicionamento, contenção, estabilização, estocagem e deposição de rejeitos radioativos. Instalações para retenção de rejeitos radioativos), h) Manuseio, condicionamento, liberação, monitoração, estabilização, inspeção, retenção e deposição de rejeitos radioativos (Sítio de rejeitos. Instalações para estocagem de produtos radioativos para posterior aproveitamento).'),
    ('05.002', u'05.002 - Atividades de operação e manutenção de reatores nucleares (Edifícios de reatores, Edifícios de estocagem de combustível), incluindo: a) montagem, instalação, substituição e inspeção de elementos combustíveis (Instalações de tratamento e estocagem de rejeitos radioativos), b) Manutenção de componentes integrantes do reator nuclear e dos sistemas hidráulicos mecânicos e elétricos, irradiados, contaminados ou situados em áreas de radiação (Instalações para tratamento de água de reatores e separação e contenção de produtos radioativos, Salas de operação de reatores, Salas de amostragem de efluentes radioativos), c) Manuseio de amostras irradiadas na operação e manutenção de reatores nucleares (Laboratórios de medidas de radiação), d) Experimentos utilizando canais de irradiação na operação e manutenção de reatores nucleares (Outras áreas sujeitas a risco potencial às radiações ionizantes passíveis de serem atingidas por dispersão de produtos voláteis), e) Medição de radiação, levantamento de dados radiológicos e nucleares, ensaios, testes, inspeções, fiscalização e supervisão de trabalhos técnicos na operação e manutenção de reatores nucleares (Laboratórios semiquentes e quentes, Minas de urânio e tório, Depósitos de minerais radioativos e produtos do tratamento de minerais radioativos), f) Segregação, manuseio, tratamento, acondicionamento e armazenamento de rejeitos radioativos na operação e manutenção de reatores nucleares (Segregação, manuseio, tratamento, acondicionamento e armazenamento de rejeitos radioativos).'),
    ('05.003', u'05.003 - Atividades de operação e manutenção de aceleradores de partículas (áreas de irradiação de alvos), incluindo: a) Montagem, instalação, substituição e manutenção de componentes irradiados ou contaminados (Oficinas de manutenção de componentes irradiados ou contaminados, Salas de operação de aceleradores), b) Processamento de alvos irradiados (laboratórios para tratamento de alvos irradiados e separação de radioisótopos), c) Experimentos com feixes de partículas (laboratórios de testes com radiação e medidas nucleares), d) Medição de radiação, levantamento de dados radiológicos e nucleares, testes, inspeções e supervisão de trabalhos técnicos (Áreas de tratamento e estocagem de rejeitos radioativos), e) Segregação, manuseio, tratamento, acondicionamento e armazenamento de rejeitos radioativos (Laboratórios de processamento de alvos irradiados).'),
    ('05.004', u'05.004 - Atividades de operação com aparelhos de raios-X, com irradiadores de radiação gama, radiação beta ou radiação de nêutrons (Salas de irradiação e de operação de aparelhos de raios-X e de irradiadores gama, beta ou nêutrons), incluindo: a) diagnóstico médico e odontológico (Laboratórios de testes, ensaios e calibração com as fontes de radiação descritas), b) Laboratórios de processamento de alvos irradiados, c) Radiografia industrial, gamagrafia e neutronradiografia (Manuseio de fontes), d) Análise de materiais por difratometria (Manuseio do equipamento), e) Testes, ensaios e calibração de detectores e monitores de radiação (Manuseio de fontes e amostras radioativas), f) Irradiação de alimentos (Manuseio de fontes e instalações para a irradiação de alimentos), g) Esterilização de instrumentos médico-hospitalares (Manuseio de fontes e instalações para a operação),h) Irradiação de espécimes minerais e biológicos (Manuseio de amostras irradiadas), i) Medição de radiação, levantamento de dados radiológicos ensaios, testes, inspeções, fiscalização de trabalhos técnicos (Laboratórios de ensaios e calibração de fontes emateriais radioativos).'),
    ('05.005', u'05.005 - Atividades de medicina nuclear (Salas de diagnóstico e terapia com medicina nuclear).'),
    ('05.006', u'05.006 - Manuseio e aplicação de radioisótopos para diagnóstico médico e terapia (Enfermaria de pacientes, sob treinamento com radioisótopos. Enfermaria de pacientes contaminados com radioisótopos em observação e sob tratamento de descontaminação).'),
    ('05.007', u'05.007 - Atividades de medicina nuclear: Manuseio de fontes seladas para aplicação em braquiterapia (Área de tratamento e estocagem de rejeitos radioativos).'),
    ('05.008', u'05.008 - Atividades de medicina nuclear: Obtenção de dados biológicos de pacientes com radioisótopos incorporados (Manuseio de materiais biológicos contendo radioisótopos ou moléculas marcadas).'),
    ('05.009', u'05.009 - Atividades de medicina nuclear: Segregação, manuseio, tratamento, acondicionamento e estocagem de rejeitos radioativos em medicina nuclear (Laboratórios para descontaminação e coleta de rejeitos radioativos).'),
    ('05.010', u'05.010 - Descomissionamento de instalações nucleares e radioativas (Áreas de instalações nucleares e radioativas contaminadas e com rejeitos) que inclui:a) Todas descontaminações radioativas inerentes (Depósitos provisórios e definitivos de rejeitos radioativos),b) Gerenciamento dos rejeitos radioativos existentes, ou sejam: tratamento e acondicionamento dos rejeitos líquidos, sólidos, gasosos e aerossóis, transporte e deposição dos mesmos (Instalações para contenção de rejeitos radioativos. Instalações para asfaltamento de rejeitos radioativos. Instalações para cimentação de rejeitos radioativos).'),
    ('05.011', u'05.011 - Descomissionamento de minas, moinhos e usinas de tratamento de minerais radioativos (Tratamento de rejeitos minerais. Repositório de rejeitos naturais (bacia de contenção de rádio e outros radioisótopos). Deposição de gangas e rejeitos de mineração).'),
    ('06.001', u'06.001 - Vigilância patrimonial: Segurança patrimonial e/ou pessoal na preservação do patrimônio em estabelecimentos públicos ou privados e da incolumidade física de pessoas.'),
    ('06.002', u'06.002 - Segurança de eventos: Segurança patrimonial e/ou pessoal em espaços públicos ou privados, de uso comum do povo.'),
    ('06.003', u'06.003 - Segurança nos transportes coletivos: Segurança patrimonial e/ou pessoal nos transportes coletivos e em suas respectivas instalações.'),
    ('06.004', u'06.004 - Segurança ambiental e florestal: Segurança patrimonial e/ou pessoal em áreas de conservação de fauna, flora natural e de reflorestamento.'),
    ('06.005', u'06.005 - Transporte de valores: Segurança na execução do serviço de transporte de valores.'),
    ('06.006', u'06.006 - Escolta armada: Segurança no acompanhamento de qualquer tipo de carga ou de valores.'),
    ('06.007', u'06.007 - Segurança pessoal: Acompanhamento e proteção da integridade física de pessoa ou de grupos.'),
    ('06.008', u'06.008 - Supervisão/fiscalização Operacional: Supervisão e/ou fiscalização direta dos locais de trabalho para acompanhamento e orientação dos vigilantes.'),
    ('06.009', u'06.009 - Telemonitoramento/telecontrole: Execução de controle e/ou monitoramento de locais, através de sistemas eletrônicos de segurança.'),
    ('07.001', u'07.001 - Atividades ou operações em instalações ou equipamentos elétricos energizados em alta tensão.'),
    ('07.002', u'07.002 - Atividades ou operações com trabalho em proximidade de instalações ou equipamentos elétricos energizados em alta tensão.'),
    ('07.003', u'07.003 - Atividades ou operações em instalações ou equipamentos elétricos energizados em baixa tensão no sistema elétrico de consumo - SEC.'),
    ('07.004', u'07.004 - Atividades, constantes no item 4.1 da NR 16, de construção, operação e manutenção de redes de linhas aéreas ou subterrâneas de alta e baixa tensão integrantes do SEP, energizados ou desenergizados, mas com possibilidade de energização acidental ou por falha operacional.'),
    ('07.005', u'07.005 - Atividades, constantes no item 4.2 da NR 16, de construção, operação e manutenção nas usinas, unidades geradoras, subestações e cabinas de distribuição em operações, integrantes do SEP, energizados ou desenergizados, mas com possibilidade de energização acidental ou por falha operacional.'),
    ('07.006', u'07.006 - Atividades de inspeção, testes, ensaios, calibração, medição e reparos em equipamentos e materiais elétricos, eletrônicos, eletromecânicos e de segurança individual e coletiva em sistemas elétricos de potência de alta e baixa tensão.'),
    ('07.007', u'07.007 - Atividades de treinamento em equipamentos ou instalações integrantes do SEP, energizadas ou desenergizadas, mas com possibilidade de energização acidental ou por falha operacional.'),
    ('08.001', u'08.001 - Atividades laborais com utilização de motocicleta ou motoneta no deslocamento de trabalhador em vias públicas.'),
    ('09.001', u'09.001 - Trabalhos com perfuratrizes e marteletes pneumáticos.'),
    ('09.002', u'09.002 - Extração e beneficiamento de minerais radioativos.'),
    ('09.003', u'09.003 - Atividades em minerações com exposição ao radônio.'),
    ('09.004', u'09.004 - Realização de manutenção e supervisão em unidades de extração, tratamento e beneficiamento de minerais radioativos com exposição às radiações ionizantes.'),
    ('09.005', u'09.005 - Operações com reatores nucleares ou com fontes radioativas.'),
    ('09.006', u'09.006 - Trabalhos realizados com exposição aos raios Alfa, Beta, Gama e X, aos nêutrons e às substâncias radioativas para fins industriais, terapêuticos e diagnósticos.'),
    ('09.007', u'09.007 - Fabricação e manipulação de produtos radioativos.'),
    ('09.008', u'09.008 - Pesquisas e estudos com radiações ionizantes em laboratórios.'),
    ('09.009', u'09.009 - Trabalhos em caixões ou câmaras hiperbáricas.'),
    ('09.010', u'09.010 - Trabalhos em tubulões ou túneis sob ar comprimido.'),
    ('09.011', u'09.011 - Operações de mergulho com o uso de escafandros ou outros equipamentos.'),
    ('10.001', u'10.001 - Operações em atmosfera IPVS.'),
    ('10.002', u'10.002 - Operações em espaço confinado.'),
    ('10.003', u'10.003 - Operações em áreas classificadas.'),
    ('10.005', u'10.005 - Atividade sob ar comprimido.'),
    ('10.006', u'10.006 - Atividade submersa.'),
    ('10.007', u'10.007 - Bombeiro Civil.'),
    ('10.008', u'10.008 - Atividade portuária conforme Lei nº 4.860/1965.'),
    ('10.009', u'10.009 - Atividades executadas em locais alagados ou encharcados, com umidade excessiva.'),
    ('11.001', u'11.001 - Mineração subterrânea cujas atividades sejam exercidas afastadas das frentes de produção.'),
    ('11.002', u'11.002 - Trabalhos em atividades permanentes no subsolo de minerações subterrâneas em frente de produção.'),
    ('99.999', u'99.999 - Ausência de correspondência.'),
    
]




CHOICES_S2240_CONDFUNCTO_ALTEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_CONDFUNCTO_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_EFICEPC_ALTEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_EFICEPC_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_EFICEPI_ALTEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_EFICEPI_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_HIGIENIZACAO_ALTEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_HIGIENIZACAO_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_IDEOC_INIEXPRISCO = [

    (1, u'1 - Conselho Regional de Medicina (CRM)'),
    (4, u'4 - Conselho Regional de Engenharia e Agronomia (CREA)'),
    (9, u'9 - Outros.'),
    
]




CHOICES_S2240_INSALUBRIDADE_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_MEDPROTECAO_ALTEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_MEDPROTECAO_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_PERICULOSIDADE_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_PERIODICTROCA_ALTEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_PERIODICTROCA_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_PRZVALID_ALTEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_PRZVALID_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_TPAVAL_INIEXPRISCO = [

    (1, u'1 - Critério quantitativo'),
    (2, u'2 - Critério qualitativo.'),
    
]




CHOICES_S2240_UNMED_INIEXPRISCO = [

    (1, u'1 - dose diária de ruído'),
    (10, u'10 - metro por segundo elevado a 1,75 (m/s1,75)'),
    (11, u'11 - parte de vapor ou gás por milhão de partes de ar contaminado (ppm)'),
    (12, u'12 - miligrama por metro cúbico de ar (mg/m3)'),
    (13, u'13 - fibra por centímetro cúbico (f/cm3)'),
    (14, u'14 - grau Celsius (ºC)'),
    (15, u'15 - metro por segundo (m/s)'),
    (16, u'16 - porcentual (%)'),
    (17, u'17 - lux (lx)'),
    (18, u'18 - unidade formadora de colônias por metro cúbico (ufc/m3)'),
    (19, u'19 - dose diária'),
    (2, u'2 - decibel linear (dB (linear))'),
    (20, u'20 - dose mensal'),
    (21, u'21 - dose trimestral'),
    (22, u'22 - dose anual'),
    (26, u'26 - watt por metro quadrado (W/m2)'),
    (27, u'27 - ampère por metro (A/m)'),
    (28, u'28 - militesla(mT)'),
    (29, u'29 - microtesla (µT)'),
    (3, u'3 - decibel (C) (dB(C))'),
    (30, u'30 - miliampère (mA)'),
    (31, u'31 - quilovolt por metro (kV/m)'),
    (32, u'32 - volt por metro (V/m)'),
    (35, u'35 - joule por metro quadrado (J/m2)'),
    (36, u'36 - milijoule por centímetro quadrado (mJ/cm2)'),
    (37, u'37 - milisievert (mSv)'),
    (39, u'39 - milhão de partículas por decímetro cúbico (mppdc)'),
    (4, u'4 - decibel (A) (dB(A))'),
    (43, u'43 - umidade relativa do ar (UR (%)).'),
    (9, u'9 - metro por segundo ao quadrado (m/s2)'),
    
]




CHOICES_S2240_USOININT_INIEXPRISCO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2240_UTILIZEPC_ALTEXPRISCO = [

    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado.'),
    
]




CHOICES_S2240_UTILIZEPC_INIEXPRISCO = [

    (0, u'0 - Não se aplica'),
    (1, u'1 - Não implementa'),
    (2, u'2 - Implementa.'),
    
]




CHOICES_S2240_UTILIZEPI_ALTEXPRISCO = [

    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado.'),
    
]




CHOICES_S2240_UTILIZEPI_INIEXPRISCO = [

    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado.'),
    
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



