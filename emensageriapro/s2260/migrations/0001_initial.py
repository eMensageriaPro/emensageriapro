# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0001_initial'),
        ('controle_de_acesso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2260localTrabInterm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tplograd', models.CharField(max_length=4, choices=[(b'A', 'A - \xc1rea'), (b'A V', 'A V - \xc1rea Verde'), (b'AC', 'AC - Acesso'), (b'ACA', 'ACA - Acampamento'), (b'ACL', 'ACL - Acesso Local'), (b'AD', 'AD - Adro'), (b'AE', 'AE - \xc1rea Especial'), (b'AER', 'AER - Aeroporto'), (b'AL', 'AL - Alameda'), (b'AMD', 'AMD - Avenida Marginal Direita'), (b'AME', 'AME - Avenida Marginal Esquerda'), (b'AN', 'AN - Anel Vi\xe1rio'), (b'ANT', 'ANT - Antiga Estrada'), (b'ART', 'ART - Art\xe9ria'), (b'AT', 'AT - Alto'), (b'ATL', 'ATL - Atalho'), (b'AV', 'AV - Avenida'), (b'AVC', 'AVC - Avenida Contorno'), (b'AVM', 'AVM - Avenida Marginal'), (b'AVV', 'AVV - Avenida Velha'), (b'BAL', 'BAL - Balne\xe1rio'), (b'BC', 'BC - Beco'), (b'BCO', 'BCO - Buraco'), (b'BEL', 'BEL - Belvedere'), (b'BL', 'BL - Bloco'), (b'BLO', 'BLO - Bal\xe3o'), (b'BLS', 'BLS - Blocos'), (b'BLV', 'BLV - Bulevar'), (b'BSQ', 'BSQ - Bosque'), (b'BVD', 'BVD - Boulevard'), (b'BX', 'BX - Baixa'), (b'C', 'C - Cais'), (b'CAL', 'CAL - Cal\xe7ada'), (b'CAM', 'CAM - Caminho'), (b'CAN', 'CAN - Canal'), (b'CH', 'CH - Ch\xe1cara'), (b'CHA', 'CHA - Chapad\xe3o'), (b'CIC', 'CIC - Ciclovia'), (b'CIR', 'CIR - Circular'), (b'CJ', 'CJ - Conjunto'), (b'CJM', 'CJM - Conjunto Mutir\xe3o'), (b'CMP', 'CMP - Complexo Vi\xe1rio'), (b'COL', 'COL - Col\xf4nia'), (b'COM', 'COM - Comunidade'), (b'CON', 'CON - Condom\xednio'), (b'COR', 'COR - Corredor'), (b'CPO', 'CPO - Campo'), (b'CRG', 'CRG - C\xf3rrego'), (b'CTN', 'CTN - Contorno'), (b'DSC', 'DSC - Descida'), (b'DSV', 'DSV - Desvio'), (b'DT', 'DT - Distrito'), (b'EB', 'EB - Entre Bloco'), (b'EIM', 'EIM - Estrada Intermunicipal'), (b'ENS', 'ENS - Enseada'), (b'ENT', 'ENT - Entrada Particular'), (b'EQ', 'EQ - Entre Quadra'), (b'ESC', 'ESC - Escada'), (b'ESD', 'ESD - Escadaria'), (b'ESE', 'ESE - Estrada Estadual'), (b'ESI', 'ESI - Estrada Vicinal'), (b'ESL', 'ESL - Estrada de Liga\xe7\xe3o'), (b'ESM', 'ESM - Estrada Municipal'), (b'ESP', 'ESP - Esplanada'), (b'ESS', 'ESS - Estrada de Servid\xe3o'), (b'EST', 'EST - Estrada'), (b'ESV', 'ESV - Estrada Velha'), (b'ETA', 'ETA - Estrada Antiga'), (b'ETC', 'ETC - Esta\xe7\xe3o'), (b'ETD', 'ETD - Est\xe1dio'), (b'ETN', 'ETN - Est\xe2ncia'), (b'ETP', 'ETP - Estrada Particular'), (b'ETT', 'ETT - Estacionamento'), (b'EVA', 'EVA - Evang\xe9lica'), (b'EVD', 'EVD - Elevada'), (b'EX', 'EX - Eixo Industrial'), (b'FAV', 'FAV - Favela'), (b'FAZ', 'FAZ - Fazenda'), (b'FER', 'FER - Ferrovia'), (b'FNT', 'FNT - Fonte'), (b'FRA', 'FRA - Feira'), (b'FTE', 'FTE - Forte'), (b'GAL', 'GAL - Galeria'), (b'GJA', 'GJA - Granja'), (b'HAB', 'HAB - N\xfacleo Habitacional'), (b'IA', 'IA - Ilha'), (b'IND', 'IND - Indeterminado'), (b'IOA', 'IOA - Ilhota'), (b'JD', 'JD - Jardim'), (b'JDE', 'JDE - Jardinete'), (b'LD', 'LD - Ladeira'), (b'LGA', 'LGA - Lagoa'), (b'LGO', 'LGO - Lago'), (b'LOT', 'LOT - Loteamento'), (b'LRG', 'LRG - Largo'), (b'LT', 'LT - Lote'), (b'MER', 'MER - Mercado'), (b'MNA', 'MNA - Marina'), (b'MOD', 'MOD - Modulo'), (b'MRG', 'MRG - Proje\xe7\xe3o'), (b'MRO', 'MRO - Morro'), (b'MTE', 'MTE - Monte'), (b'NUC', 'NUC - N\xfacleo'), (b'NUR', 'NUR - N\xfacleo Rural'), (b'OUT', 'OUT - Outeiro'), (b'PAR', 'PAR - Paralela'), (b'PAS', 'PAS - Passeio'), (b'PAT', 'PAT - P\xe1tio'), (b'PC', 'PC - Pra\xe7a'), (b'PCE', 'PCE - Pra\xe7a de Esportes'), (b'PDA', 'PDA - Parada'), (b'PDO', 'PDO - Paradouro'), (b'PNT', 'PNT - Ponta'), (b'PR', 'PR - Praia'), (b'PRL', 'PRL - Prolongamento'), (b'PRM', 'PRM - Parque Municipal'), (b'PRQ', 'PRQ - Parque'), (b'PRR', 'PRR - Parque Residencial'), (b'PSA', 'PSA - Passarela'), (b'PSG', 'PSG - Passagem'), (b'PSP', 'PSP - Passagem de Pedestre'), (b'PSS', 'PSS - Passagem Subterr\xe2nea'), (b'PTE', 'PTE - Ponte'), (b'PTO', 'PTO - Porto'), (b'Q', 'Q - Quadra'), (b'QTA', 'QTA - Quinta'), (b'QTS', 'QTS - Quintas'), (b'R', 'R - Rua'), (b'R I', 'R I - Rua Integra\xe7\xe3o'), (b'R L', 'R L - Rua de Liga\xe7\xe3o'), (b'R P', 'R P - Rua Particular'), (b'R V', 'R V - Rua Velha'), (b'RAM', 'RAM - Ramal'), (b'RCR', 'RCR - Recreio'), (b'REC', 'REC - Recanto'), (b'RER', 'RER - Retiro'), (b'RES', 'RES - Residencial'), (b'RET', 'RET - Reta'), (b'RLA', 'RLA - Ruela'), (b'RMP', 'RMP - Rampa'), (b'ROA', 'ROA - Rodo Anel'), (b'ROD', 'ROD - Rodovia'), (b'ROT', 'ROT - Rotula'), (b'RPE', 'RPE - Rua de Pedestre'), (b'RPR', 'RPR - Margem'), (b'RTN', 'RTN - Retorno'), (b'RTT', 'RTT - Rotat\xf3ria'), (b'SEG', 'SEG - Segunda Avenida'), (b'SIT', 'SIT - Sitio'), (b'SRV', 'SRV - Servid\xe3o'), (b'ST', 'ST - Setor'), (b'SUB', 'SUB - Subida'), (b'TCH', 'TCH - Trincheira'), (b'TER', 'TER - Terminal'), (b'TR', 'TR - Trecho'), (b'TRV', 'TRV - Trevo'), (b'TUN', 'TUN - T\xfanel'), (b'TV', 'TV - Travessa'), (b'TVP', 'TVP - Travessa Particular'), (b'TVV', 'TVV - Travessa Velha'), (b'UNI', 'UNI - Unidade'), (b'V', 'V-E - Via Expressa'), (b'V', 'V - Via'), (b'V C', 'V C - Via Coletora'), (b'V L', 'V L - Via Local'), (b'VAC', 'VAC - Via de Acesso'), (b'VAL', 'VAL - Vala'), (b'VCO', 'VCO - Via Costeira'), (b'VD', 'VD - Viaduto'), (b'VER', 'VER - Vereda'), (b'VEV', 'VEV - Via Elevado'), (b'VL', 'VL - Vila'), (b'VLA', 'VLA - Viela'), (b'VLE', 'VLE - Vale'), (b'VLT', 'VLT - Via Litor\xe2nea'), (b'VPE', 'VPE - Via de Pedestre'), (b'VRT', 'VRT - Variante'), (b'ZIG', 'ZIG - Zigue-Zague')])),
                ('dsclograd', models.CharField(max_length=100)),
                ('nrlograd', models.CharField(max_length=10)),
                ('complem', models.CharField(max_length=30, null=True, blank=True)),
                ('bairro', models.CharField(max_length=90, null=True, blank=True)),
                ('cep', models.CharField(max_length=8)),
                ('codmunic', models.TextField(max_length=7)),
                ('uf', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2260localtrabinterm_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2260localtrabinterm_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2260_evtconvinterm', models.OneToOneField(related_name='s2260localtrabinterm_s2260_evtconvinterm', to='esocial.s2260evtConvInterm')),
            ],
            options={
                'ordering': ['s2260_evtconvinterm', 'tplograd', 'dsclograd', 'nrlograd', 'complem', 'bairro', 'cep', 'codmunic', 'uf'],
                'db_table': 's2260_localtrabinterm',
                'managed': True,
            },
        ),
    ]
