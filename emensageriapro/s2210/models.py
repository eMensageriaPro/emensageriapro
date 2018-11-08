#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
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

CHOICES_S2210_CODAGNTCAUSADOR = (
    (302010200, u'302010200 - Rua e estrada - superfície utilizada para sustentar pessoas'),
    (302010250, u'302010250 - Calçada ou caminho para pedestre - superfície utilizada para sustentar pessoas'),
    (302010300, u'302010300 - Piso de edifício - superfície utilizada para sustentar pessoas'),
    (302010350, u'302010350 - Escada permanente cujos degraus permitem apoio integral do pé, degrau - superfície utilizada para sustentar pessoas'),
    (302010400, u'302010400 - Rampa - superfície utilizada para sustentar pessoas'),
    (302010450, u'302010450 - Passarela ou plataforma permanentes - superfície utilizada para sustentar pessoas'),
    (302010500, u'302010500 - Piso de mina - superfície utilizada para sustentar pessoas'),
    (302010550, u'302010550 - Chão - superfície utilizada para sustentar pessoas'),
    (302010600, u'302010600 - Piso de andaime e plataforma desmontável - superfície utilizada para sustentar pessoas'),
    (302010650, u'302010650 - Piso de veiculo - superfície utilizada para sustentar pessoas'),
    (302010700, u'302010700 - Telhado'),
    (302010900, u'302010900 - Superfície de sustentação, NIC - superfície utilizada para sustentar pessoas'),
    (302030900, u'302030900 - Escada móvel ou fixada, NIC'),
    (302050100, u'302050100 - Edifício - edifício ou estrutura'),
    (302050200, u'302050200 - Depósito fixo (tanque, silo, paiol, etc.) - edifício ou estrutura'),
    (302050300, u'302050300 - Cais, doca - edifício ou estrutura'),
    (302050400, u'302050400 - Dique, barragem – edifício ou estrutura'),
    (302050500, u'302050500 - Ponte, viaduto - edifício ou estrutura'),
    (302050600, u'302050600 - Arquibancada, estádio - edifício ou estrutura'),
    (302050700, u'302050700 - Andaime, plataforma - edifício ou estrutura'),
    (302050800, u'302050800 - Torre, poste - edifício ou estrutura'),
    (302050900, u'302050900 - Edifício ou estrutura (exceto piso, superfície de sustentação ou área de circulação), NIC'),
    (302070100, u'302070100 - Escavação (para edifício, estrada, etc.)'),
    (302070300, u'302070300 - Canal, fosso'),
    (302070500, u'302070500 - Poço, entrada, galeria, etc., de mina'),
    (302070700, u'302070700 - Túnel'),
    (302070900, u'302070900 - Escavação, fosso, túnel, NIC'),
    (302090000, u'302090000 - Superfície e estrutura, NIC'),
    (303010040, u'303010040 - Martelo, malho, marreta - ferramenta manual sem força motriz'),
    (303010080, u'303010080 - Machadinha, enxó - ferramenta manual sem força motriz'),
    (303010120, u'303010120 - Faca, facão - ferramenta manual sem força motriz'),
    (303010160, u'303010160 - Tesoura, tesourão - ferramenta manual sem força motriz'),
    (303010200, u'303010200 - Formão, cinzel - ferramenta manual sem força motriz'),
    (303010240, u'303010240 - Serra, serrote - ferramenta manual sem força motriz'),
    (303010280, u'303010280 - Alicate, torques, tenaz - ferramenta manual sem força motriz'),
    (303010320, u'303010320 - Plaina - ferramenta manual sem força motriz'),
    (303010360, u'303010360 - Lima, grosa - ferramenta manual sem força motriz'),
    (303010400, u'303010400 - Punção, ponteiro, vazador, talhadeira - ferramenta manual sem força motriz'),
    (303010440, u'303010440 - Pua, trado, verruma, máquina de furar manual - ferramenta manual sem força motriz'),
    (303010480, u'303010480 - Chave de parafuso - ferramenta manual sem força motriz'),
    (303010520, u'303010520 - chave de porca ou de abertura regulável, chave de boca - ferramenta manual sem força motriz'),
    (303010560, u'303010560 - Alavanca, pé-de-cabra - ferramenta manual sem força motriz'),
    (303010600, u'303010600 - Corda, cabo, corrente - ferramenta manual sem força motriz'),
    (303010640, u'303010640 - Machado - ferramenta manual sem força motriz'),
    (303010680, u'303010680 - Enxada, enxadão, sacho - ferramenta manual sem força motriz'),
    (303010720, u'303010720 - Pá, cavadeira - ferramenta manual sem força motriz'),
    (303010760, u'303010760 - Picareta - ferramenta manual sem força motriz'),
    (303010800, u'303010800 - Garfo, ancinho, forcado - ferramenta manual sem força motriz'),
    (303010900, u'303010900 - Ferramenta manual sem força motriz, NIC'),
    (303015050, u'303015050 - Martelete, socador - ferramenta portátil com força motriz ou aquecimento'),
    (303015100, u'303015100 - Talhadeira - ferramenta portátil com força motriz ou aquecimento'),
    (303015150, u'303015150 - Cortadeira, guilhotina - ferramenta portátil com força motriz ou aquecimento'),
    (303015200, u'303015200 - Serra - ferramenta portátil com força motriz ou aquecimento'),
    (303015250, u'303015250 - Punção, ponteiro, vazador - ferramenta portátil com força motriz ou aquecimento'),
    (303015300, u'303015300 - Perfuratriz - ferramenta portátil com força motriz ou aquecimento'),
    (303015350, u'303015350 - Rebitadeira - ferramenta portátil com força motriz ou aquecimento'),
    (303015400, u'303015400 - Máquina de aparafusar - ferramenta portátil com força motriz ou aquecimento'),
    (303015450, u'303015450 - Esmeril - ferramenta portátil com força motriz ou aquecimento'),
    (303015500, u'303015500 - Politriz, enceradeira - ferramenta portátil com força motriz ou aquecimento'),
    (303015550, u'303015550 - Ferro de passar - ferramenta portátil com força motriz ou aquecimento'),
    (303015600, u'303015600 - Ferramenta de soldagem - ferramenta portátil com força motriz ou aquecimento'),
    (303015650, u'303015650 - Maçarico - ferramenta portátil com força motriz ou aquecimento'),
    (303015700, u'303015700 - Ferramenta acionada por explosivo - ferramenta portátil com força motriz ou aquecimento'),
    (303015750, u'303015750 - Jato de areia - ferramenta portátil com força motriz ou aquecimento'),
    (303015900, u'303015900 - Ferramenta portátil com forca motriz ou aquecimento, NIC'),
    (303020040, u'303020040 - Serra - máquina'),
    (303020080, u'303020080 - Tesoura, guilhotina, máquina de cortar - máquina'),
    (303020120, u'303020120 - Laminadora, calandra - máquina'),
    (303020160, u'303020160 - Furadeira, broqueadeira, torno, freza - máquina'),
    (303020200, u'303020200 - Prensa - máquina'),
    (303020240, u'303020240 - Plaina, tupia - máquina'),
    (303020280, u'303020280 - Máquina de fundir, de forjar, de soldar'),
    (303020320, u'303020320 - Britador, moinho - máquina'),
    (303020360, u'303020360 - Misturador, batedeira, agitador - máquina'),
    (303020400, u'303020400 - Peneira mecânica, máquina separadora - máquina'),
    (303020440, u'303020440 - Politriz, lixadora, esmeril - máquina'),
    (303020480, u'303020480 - Máquina de terraplenagem e construção de estrada'),
    (303020520, u'303020520 - Máquina de mineração e perfuração (de túnel, poço, etc.)'),
    (303020560, u'303020560 - Máquina agrícola'),
    (303020600, u'303020600 - Máquina têxtil'),
    (303020640, u'303020640 - Máquina de costurar e de pespontar'),
    (303020680, u'303020680 - Máquina de imprimir'),
    (303020720, u'303020720 - Máquina de escritório'),
    (303020760, u'303020760 - Máquina de embalar ou empacotar'),
    (303020900, u'303020900 - Máquina, NIC'),
    (303025300, u'303025300 - Transportador por gravidade'),
    (303025600, u'303025600 - Transportador com força motriz'),
    (303025900, u'303025900 - Transportador, NIC'),
    (303030050, u'303030050 - Guindaste - equipamento de guindar'),
    (303030100, u'303030100 - Ponte rolante - equipamento de guindar'),
    (303030150, u'303030150 - Elevador - equipamento de guindar'),
    (303030200, u'303030200 - Elevador de caçamba para mineração - equipamento de guindar'),
    (303030250, u'303030250 - Pá mecânica, draga - equipamento de guindar'),
    (303030300, u'303030300 - Talha - equipamento de guindar'),
    (303030350, u'303030350 - Pau de carga - equipamento de guindar'),
    (303030400, u'303030400 - Macaco (mecânico, hidráulico, pneumático) - equipamento de guindar'),
    (303030450, u'303030450 - Guincho pneumático - equipamento de guindar'),
    (303030500, u'303030500 - Guincho elétrico - equipamento de guindar'),
    (303030900, u'303030900 - Equipamento de guindar, NIC'),
    (303035300, u'303035300 - Correia - dispositivo de transmissão de energia mecânica'),
    (303035400, u'303035400 - Corrente, corda, cabo - dispositivo de transmissão de energia mecânica'),
    (303035500, u'303035500 - Tambor, polia, roldana - dispositivo de transmissão de energia mecânica'),
    (303035600, u'303035600 - Embreagem de fricção - dispositivo de transmissão de energia mecânica'),
    (303035700, u'303035700 - Engrenagem - dispositivo de transmissão de energia mecânica'),
    (303035900, u'303035900 - Dispositivo de transmissão de energia mecânica, NIC'),
    (303040100, u'303040100 - Gerador - equipamento elétrico'),
    (303040200, u'303040200 - Condutor - equipamento elétrico'),
    (303040300, u'303040300 - Transformador, conversor - equipamento elétrico'),
    (303040400, u'303040400 - Painel de controle, barramento, chave, interruptor, disjuntor, fusível - equipamento elétrico'),
    (303040500, u'303040500 - Reostato, dispositivo de partida e aparelho de controle, capacitor, retificador, bateria de acumuladores - equipamento elétrico'),
    (303040600, u'303040600 - Motor elétrico - equipamento elétrico'),
    (303040700, u'303040700 - Equipamento magnético - equipamento elétrico'),
    (303040750, u'303040750 - Equipamento eletrolítico - equipamento elétrico'),
    (303040800, u'303040800 - Equipamento de aquecimento elétrico - equipamento elétrico'),
    (303040900, u'303040900 - Equipamento elétrico, NIC'),
    (303045200, u'303045200 - Motor (combustão interna, vapor)'),
    (303045400, u'303045400 - Bomba'),
    (303045600, u'303045600 - Turbina'),
    (303045900, u'303045900 - Motor, bomba, turbina, NIC'),
    (303050200, u'303050200 - Caldeira'),
    (303050400, u'303050400 - Vaso sob pressão (para líquido, gás ou vapor)'),
    (303050600, u'303050600 - Tubo sob pressão (mangueira ou tubo para liquido, gás ou vapor)'),
    (303050900, u'303050900 - Caldeira, vaso sob pressão, NIC'),
    (303055200, u'303055200 - Caixão pneumático - equipamento para trabalho em ambiente de pressão anormal'),
    (303055400, u'303055400 - Escafandro - equipamento para trabalho em ambiente de pressão anormal'),
    (303055600, u'303055600 - Equipamento de mergulho - equipamento para trabalho em ambiente de pressão anormal'),
    (303055900, u'303055900 - Equipamento para trabalho em ambiente de pressão anormal, NIC'),
    (303060000, u'303060000 - Forno, estufa, retorta, aquecedor de ambiente, fogão, etc., exceto quando a lesão principal for choque elétrico ou eletroplessão - equipamento de aquecimento'),
    (303065000, u'303065000 - Equipamento emissor de radiação não ionizante'),
    (303065300, u'303065300 - Equipamento de iluminação - equipamento emissor de radiação não ionizante'),
    (303065600, u'303065600 - Arco elétrico - equipamento emissor de radiação não ionizante'),
    (303065900, u'303065900 - Equipamento emissor de radiação não ionizante, NIC'),
    (303066300, u'303066300 - Equipamento de iluminação'),
    (303066600, u'303066600 - Arco elétrico'),
    (303070200, u'303070200 - Equipamento de raios X - equipamento ou substância emissores de radiação ionizante'),
    (303070400, u'303070400 - Reator (inclui combustível e resíduo) - equipamento ou substância emissores de radiação ionizante'),
    (303070600, u'303070600 - Fonte de radioisótopo - equipamento ou substância emissores de radiação ionizante'),
    (303070900, u'303070900 - Equipamento ou substância emissores de radiação ionizante, NIC'),
    (303075100, u'303075100 - Bicicleta'),
    (303075150, u'303075150 - Triciclo'),
    (303075200, u'303075200 - Motocicleta, motoneta'),
    (303075250, u'303075250 - Veículo rodoviário motorizado'),
    (303075300, u'303075300 - Veículo sobre trilho'),
    (303075350, u'303075350 - Veículo aquático'),
    (303075400, u'303075400 - Aeronave'),
    (303075450, u'303075450 - Empilhadeira'),
    (303075500, u'303075500 - Rebocador mecânico, mula mecânica'),
    (303075550, u'303075550 - Carro-de-mão'),
    (303075600, u'303075600 - Trator'),
    (303075650, u'303075650 - Veículo de terraplenagem'),
    (303075700, u'303075700 - Veículo de tração animal'),
    (303075750, u'303075750 - Veículo deslizante'),
    (303075800, u'303075800 - Veículo funicular (tração por cabo)'),
    (303075900, u'303075900 - Veículo, NIC'),
    (303090000, u'303090000 - Ferramenta, máquina, equipamento, veículo, NIC'),
    (305004100, u'305004100 - Composto metálico (de chumbo, mercúrio, zinco, cadmio, cromo, etc.)'),
    (305004150, u'305004150 - Composto de arsênio'),
    (305004200, u'305004200 - Gás carbônico (dióxido de carbono, CO2)'),
    (305004250, u'305004250 - Monóxido de carbono (CO)'),
    (305004300, u'305004300 - Óxidos de Nitrogênio (vapores nitrosos)'),
    (305004350, u'305004350 - Ácido'),
    (305004400, u'305004400 - Álcali'),
    (305004450, u'305004450 - Composto de fósforo'),
    (305004500, u'305004500 - Dissulfeto de carbono'),
    (305004550, u'305004550 - Cianeto ou composto de cianogênio'),
    (305004600, u'305004600 - Álcool'),
    (305004650, u'305004650 - Tetracloreto de carbono'),
    (305004700, u'305004700 - Composto orgânico halogenado (tricloretileno, percloretileno, cloreto de metilo, substâncias refrigerantes)'),
    (305004750, u'305004750 - Composto aromático (benzol, toluol, xilol, anilina, etc.)'),
    (305004900, u'305004900 - Substância química, NIC'),
    (305008500, u'305008500 - Água - usar quando o estado líquido contribuir preponderantemente para a ocorrência'),
    (305008900, u'305008900 - Líquido, NIC'),
    (305020000, u'305020000 - Partículas - não identificadas'),
    (305024100, u'305024100 - Pele, crina, pelo, lã (em bruto) - produto animal'),
    (305024300, u'305024300 - Pena - produto animal'),
    (305024500, u'305024500 - Couro cru ou curtido - produto animal'),
    (305024700, u'305024700 - Osso - produto animal'),
    (305024900, u'305024900 - Produto animal, NIC'),
    (305028000, u'305028000 - Madeira (toro, madeira serrada, pranchão, poste, barrote, ripa e produto de madeira)'),
    (305032000, u'305032000 - Produto mineral metálico - produto de mineração em bruto ou beneficiado, como minério e concentrado de minério'),
    (305032500, u'305032500 - Metal - inclui liga ferrosa e não ferrosa, tubo, placa, perfil, trilho, vergalhão, arame, porca, rebite, prego, etc. inclui metal fundido, lingote e sucata de fundição, exceto minério'),
    (305036000, u'305036000 - Produto mineral não metálico - produto de mineração, escavação, desbarrancamento, etc., como detrito, argila, areia, cascalho, pedra, etc.'),
    (305040100, u'305040100 - Petróleo bruto, bruto reduzido'),
    (305040150, u'305040150 - Asfalto, alcatrão, piche'),
    (305040200, u'305040200 - Óleo combustível'),
    (305040250, u'305040250 - Parafina, óleo lubrificante e de corte, graxas'),
    (305040300, u'305040300 - Gasóleo, óleo diesel'),
    (305040350, u'305040350 - Querosene'),
    (305040400, u'305040400 - Nafta e solvente de nafta (éter de petróleo, álcool mineral, solvente aromático, etc.)'),
    (305040450, u'305040450 - Gasolina (exceto quando a ocorrência for causada preponderantemente por composto de chumbo)'),
    (305040500, u'305040500 - Hidrocarboneto gasoso (inclui gás liquefeito, gás encanado de nafta, gás natural)'),
    (305040600, u'305040600 - Carvão'),
    (305040650, u'305040650 - Coque'),
    (305040700, u'305040700 - Gás encanado de carvão'),
    (305040900, u'305040900 - Produto de petróleo e de carvão, NIC'),
    (305044000, u'305044000 - Vidraria, fibra de vidro, lâmina, etc., exceto frasco, garrafa'),
    (305048000, u'305048000 - Cerâmica'),
    (305048300, u'305048300 - Tijolo e telha - cerâmica'),
    (305048400, u'305048400 - Louça de mesa e outros utensílios (de porcelana, barro, etc.) - cerâmica'),
    (305048500, u'305048500 - Tubo, manilha - cerâmica'),
    (305048600, u'305048600 - Revestimento cerâmico (azulejo, mosaico, etc.) - cerâmica'),
    (305048700, u'305048700 - Louca sanitária (pia, vaso sanitário, etc.) - cerâmica'),
    (305048900, u'305048900 - Cerâmica, NIC'),
    (305052000, u'305052000 - Têxteis - inclui fibras animais após o primeiro desengorduramento e limpeza, fibras vegetais e sintéticas (exceto vidro), fio, linha, tecido, passamanaria, feltro e produtos têxteis em geral'),
    (305056000, u'305056000 - Plástico - inclui pó, folha, trefilado, barra, perfil, etc., não incluindo produto a ser usado no fabrico de plástico'),
    (305060000, u'305060000 - Papel e pasta para papel'),
    (305064000, u'305064000 - Produtos alimentícios inclui carne leite e derivados legumes frutas cerais e derivados'),
    (305064300, u'305064300 - Carne e derivados - inclusive de origem animal'),
    (305064400, u'305064400 - Leite e derivados - inclusive de origem animal'),
    (305064500, u'305064500 - Legume, verdura e derivados'),
    (305064600, u'305064600 - Fruta e derivados'),
    (305064700, u'305064700 - Cereal e derivados'),
    (305064900, u'305064900 - Produto alimentício - inclusive de origem animal, NIC'),
    (305068300, u'305068300 - Medicamento em geral (exceto produto biológico)'),
    (305068600, u'305068600 - Produto biológico (soro, toxina, antitoxina, vacina, plasma) - medicamento'),
    (305072000, u'305072000 - Produto de limpeza, sabão, detergente'),
    (305076000, u'305076000 - Sucata, entulho, resíduo'),
    (305090000, u'305090000 - Substância química, material, produto, NIC'),
    (306020000, u'306020000 - Animal vivo'),
    (306040000, u'306040000 - Vegetal - planta, árvore, em estado natural, não beneficiada (não inclui grão debulhado, fruto colhido, toro mesmo com galho)'),
    (306060000, u'306060000 - Agente infeccioso ou parasitário - inclui bactéria, fungo, organismo parasitário, vírus, etc., não incluindo produto químico, preparado farmacêutico ou alimento'),
    (306090000, u'306090000 - Ser vivo, NIC'),
    (307030100, u'307030100 - Cadeira banco - mobiliário e acessórios'),
    (307030200, u'307030200 - Mesa, carteira, exceto mesa elástica desmontável - mobiliário e acessórios'),
    (307030250, u'307030250 - Mesa elástica desmontável - mobiliário e acessórios'),
    (307030300, u'307030300 - Balcão, bancada - mobiliário e acessórios'),
    (307030400, u'307030400 - Arquivo, fichário, estante - mobiliário e acessórios'),
    (307030500, u'307030500 - Tapete, forração de piso, capacho - mobiliário e acessórios'),
    (307030600, u'307030600 - Luminária, globo, lâmpada - mobiliário e acessórios'),
    (307030900, u'307030900 - Mobiliário e acessórios, NIC'),
    (307040100, u'307040100 - Caixa, engradado, caixote - embalagem, recipiente, vazio ou cheio'),
    (307040300, u'307040300 - Frasco, garrafa - embalagem, recipiente, vazio ou cheio'),
    (307040500, u'307040500 - Barril, barrica, barrilete, tambor - embalagem, recipiente, vazio ou cheio'),
    (307040700, u'307040700 - Tanque, cilindro (transportáveis e não sob pressão) - embalagem, recipiente, vazio ou cheio'),
    (307040900, u'307040900 - Embalagem e recipiente, vazio ou cheio, NIC'),
    (307050900, u'307050900 - Vestuário, NIC'),
    (307070000, u'307070000 - Área ou ambiente de trabalho - o agente do acidente ocorrido em consequência de fenômeno atmosférico, meteoro, etc., assim como da ação da radiação solar, deverá ser incluído neste item'),
    (309000000, u'309000000 - Agente do acidente, NIC'),
    (309500000, u'309500000 - Agente do acidente inexistente'),
    (354000000, u'354000000 - Energia'),
    (354010300, u'354010300 - Pressão ambiente alta trabalho em caixão pneumático mergulho'),
    (354010600, u'354010600 - Pressão ambiente baixa ar rarefeito'),
    (354020000, u'354020000 - Ruído'),
    (354040000, u'354040000 - Fogo chama material incandescente ou quente fumaça'),
    (354050300, u'354050300 - Temperatura ambiente - não inclui a de objeto ou substância quente'),
    (355016000, u'355016000 - Aerodispersóides'),
    (355016600, u'355016600 - Neblina'),
    (355016800, u'355016800 - Gás e vapor'),
)

CHOICES_S2210_CODPARTEATING = (
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
    (758500000, u'758500000 - Sistemas e aparelhos. Aplica-se quando o funcionamento de todo um sistema ou aparelho do corpo humano for afetado, sem lesão específica de qualquer outra parte, como no caso do envenenamento, ação corrosiva que afete órgãos internos, lesão dos (...)'),
    (758520000, u'758520000 - Aparelho circulatório'),
    (758530000, u'758530000 - Aparelho respiratório'),
    (758540000, u'758540000 - Sistema nervoso'),
    (758550000, u'758550000 - Aparelho digestivo'),
    (758560000, u'758560000 - Aparelho gênito-urinário'),
    (758570000, u'758570000 - Sistema musculoesquelético'),
    (758590000, u'758590000 - Sistemas e aparelhos, NIC'),
    (759000000, u'759000000 - Localização da lesão, NIC'),
)

CHOICES_S2210_DSCLESAO = (
    (702000000, u'702000000 - Lesão imediata'),
    (702005000, u'702005000 - Escoriação, abrasão (ferimento superficial)'),
    (702010000, u'702010000 - Corte, laceração, ferida contusa, punctura (ferida aberta)'),
    (702015000, u'702015000 - Contusão, esmagamento (superfície cutânea intacta)'),
    (702020000, u'702020000 - Distensão, torção'),
    (702025000, u'702025000 - Inflamação de articulação, tendão ou músculo - inclui sinovite, tenossionovite, etc. Não inclui distensão, torção ou suas consequências'),
    (702030000, u'702030000 - Luxação'),
    (702035000, u'702035000 - Fratura'),
    (702040000, u'702040000 - Queimadura ou escaldadura - efeito de temperatura elevada. Efeito do contato com substância quente. Inclui queimadura por eletricidade, mas não inclui choque elétrico. Não inclui queimadura por substância química, efeito de radiação, queimadura (...)'),
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
    (704040000, u'704040000 - Dermatose (erupção, inflamação da pele, inclusive furúnculo, etc.). Geralmente provocada pelo contato direto com substâncias ou agentes sensibilizantes ou irritantes, tais como medicamentos, óleos, agentes biológicos, plantas, madeiras ou metai (...)'),
    (704050000, u'704050000 - Envenenamento sistêmico - condição mórbida sistêmica provocada por inalação, ingestão ou absorção cutânea de substância tóxica, que afete o metabolismo, o funcionamento do sistema nervoso, do aparelho circulatório, do aparelho digestivo, do apa (...)'),
    (704060000, u'704060000 - Perda ou diminuição mediatas de sentido (audição, visão, olfato, paladar e tato, desde que não seja sequela de outra lesão)'),
    (704070000, u'704070000 - Efeito de radiação (mediato) - queimadura do sol e toda forma de lesão de tecido, osso, ou fluido orgânico por exposição à radiação.'),
    (704090000, u'704090000 - Doença, NIC'),
    (706050000, u'706050000 - Lesões múltiplas'),
    (706090000, u'706090000 - Outras lesões, NIC'),
)

CHOICES_S2210_IDEOC = (
    (1, u'1 - Conselho Regional de Medicina (CRM)'),
    (2, u'2 - Conselho Regional de Odontologia (CRO)'),
    (3, u'3 - Registro do Ministério da Saúde (RMS)'),
)

CHOICES_S2210_INDAFAST = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2210_INDINTERNACAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2210_LATERALIDADE = (
    (0, u'0 - Não aplicável'),
    (1, u'1 - Esquerda'),
    (2, u'2 - Direita'),
    (3, u'3 - Ambas'),
)

CHOICES_S2210_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

class s2210agenteCausador(models.Model):
    s2210_evtcat = models.ForeignKey('esocial.s2210evtCAT',
        related_name='%(class)s_s2210_evtcat')
    def evento(self): return self.s2210_evtcat.evento()
    codagntcausador = models.IntegerField(choices=CHOICES_S2210_CODAGNTCAUSADOR)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2210_evtcat) + ' - ' + unicode(self.codagntcausador)
    #s2210_agentecausador_custom#
    #s2210_agentecausador_custom#
    class Meta:
        db_table = r's2210_agentecausador'
        managed = True
        ordering = ['s2210_evtcat', 'codagntcausador']



class s2210agenteCausadorSerializer(ModelSerializer):
    class Meta:
        model = s2210agenteCausador
        fields = '__all__'
            

class s2210atestado(models.Model):
    s2210_evtcat = models.OneToOneField('esocial.s2210evtCAT',
        related_name='%(class)s_s2210_evtcat')
    def evento(self): return self.s2210_evtcat.evento()
    codcnes = models.CharField(max_length=7, blank=True, null=True)
    dtatendimento = models.DateField()
    hratendimento = models.CharField(max_length=4)
    indinternacao = models.CharField(choices=CHOICES_S2210_INDINTERNACAO, max_length=1)
    durtrat = models.IntegerField()
    indafast = models.CharField(choices=CHOICES_S2210_INDAFAST, max_length=1)
    dsclesao = models.IntegerField(choices=CHOICES_S2210_DSCLESAO)
    dsccomplesao = models.CharField(max_length=200, blank=True, null=True)
    diagprovavel = models.CharField(max_length=100, blank=True, null=True)
    codcid = models.CharField(max_length=4)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    nmemit = models.CharField(max_length=70)
    ideoc = models.IntegerField(choices=CHOICES_S2210_IDEOC)
    nroc = models.CharField(max_length=14)
    ufoc = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2210_evtcat) + ' - ' + unicode(self.codcnes) + ' - ' + unicode(self.dtatendimento) + ' - ' + unicode(self.hratendimento) + ' - ' + unicode(self.indinternacao) + ' - ' + unicode(self.durtrat) + ' - ' + unicode(self.indafast) + ' - ' + unicode(self.dsclesao) + ' - ' + unicode(self.dsccomplesao) + ' - ' + unicode(self.diagprovavel) + ' - ' + unicode(self.codcid) + ' - ' + unicode(self.observacao) + ' - ' + unicode(self.nmemit) + ' - ' + unicode(self.ideoc) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.ufoc)
    #s2210_atestado_custom#
    #s2210_atestado_custom#
    class Meta:
        db_table = r's2210_atestado'
        managed = True
        ordering = ['s2210_evtcat', 'codcnes', 'dtatendimento', 'hratendimento', 'indinternacao', 'durtrat', 'indafast', 'dsclesao', 'dsccomplesao', 'diagprovavel', 'codcid', 'observacao', 'nmemit', 'ideoc', 'nroc', 'ufoc']



class s2210atestadoSerializer(ModelSerializer):
    class Meta:
        model = s2210atestado
        fields = '__all__'
            

class s2210catOrigem(models.Model):
    s2210_evtcat = models.OneToOneField('esocial.s2210evtCAT',
        related_name='%(class)s_s2210_evtcat')
    def evento(self): return self.s2210_evtcat.evento()
    dtcatorig = models.DateField()
    nrreccatorig = models.CharField(max_length=40, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2210_evtcat) + ' - ' + unicode(self.dtcatorig) + ' - ' + unicode(self.nrreccatorig)
    #s2210_catorigem_custom#
    #s2210_catorigem_custom#
    class Meta:
        db_table = r's2210_catorigem'
        managed = True
        ordering = ['s2210_evtcat', 'dtcatorig', 'nrreccatorig']



class s2210catOrigemSerializer(ModelSerializer):
    class Meta:
        model = s2210catOrigem
        fields = '__all__'
            

class s2210ideLocalAcid(models.Model):
    s2210_evtcat = models.OneToOneField('esocial.s2210evtCAT',
        related_name='%(class)s_s2210_evtcat')
    def evento(self): return self.s2210_evtcat.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2210_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2210_evtcat) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2210_idelocalacid_custom#
    #s2210_idelocalacid_custom#
    class Meta:
        db_table = r's2210_idelocalacid'
        managed = True
        ordering = ['s2210_evtcat', 'tpinsc', 'nrinsc']



class s2210ideLocalAcidSerializer(ModelSerializer):
    class Meta:
        model = s2210ideLocalAcid
        fields = '__all__'
            

class s2210parteAtingida(models.Model):
    s2210_evtcat = models.ForeignKey('esocial.s2210evtCAT',
        related_name='%(class)s_s2210_evtcat')
    def evento(self): return self.s2210_evtcat.evento()
    codparteating = models.IntegerField(choices=CHOICES_S2210_CODPARTEATING)
    lateralidade = models.IntegerField(choices=CHOICES_S2210_LATERALIDADE)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2210_evtcat) + ' - ' + unicode(self.codparteating) + ' - ' + unicode(self.lateralidade)
    #s2210_parteatingida_custom#
    #s2210_parteatingida_custom#
    class Meta:
        db_table = r's2210_parteatingida'
        managed = True
        ordering = ['s2210_evtcat', 'codparteating', 'lateralidade']



class s2210parteAtingidaSerializer(ModelSerializer):
    class Meta:
        model = s2210parteAtingida
        fields = '__all__'
            

#VIEWS_MODELS
