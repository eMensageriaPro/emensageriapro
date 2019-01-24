# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-20 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2206', '0004_auto_20181119_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2206alvarajudicial',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206alvarajudicial',
            name='nrprocjud',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='s2206alvarajudicial',
            name='s2206_evtaltcontratual',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2206alvarajudicial_s2206_evtaltcontratual', to='esocial.s2206evtAltContratual'),
        ),
        migrations.AlterField(
            model_name='s2206aprend',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206aprend',
            name='nrinsc',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='s2206aprend',
            name='s2206_infoceletista',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2206aprend_s2206_infoceletista', to='s2206.s2206infoCeletista'),
        ),
        migrations.AlterField(
            model_name='s2206aprend',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
        ),
        migrations.AlterField(
            model_name='s2206filiacaosindical',
            name='cnpjsindtrab',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s2206filiacaosindical',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206filiacaosindical',
            name='s2206_evtaltcontratual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2206filiacaosindical_s2206_evtaltcontratual', to='esocial.s2206evtAltContratual'),
        ),
        migrations.AlterField(
            model_name='s2206horario',
            name='codhorcontrat',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s2206horario',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206horario',
            name='dia',
            field=models.IntegerField(choices=[(1, '1 - Segunda-Feira'), (2, '2 - Ter\xe7a-Feira'), (3, '3 - Quarta-Feira'), (4, '4 - Quinta-Feira'), (5, '5 - Sexta-Feira'), (6, '6 - S\xe1bado'), (7, '7 - Domingo'), (8, '8 - Dia vari\xe1vel')]),
        ),
        migrations.AlterField(
            model_name='s2206horario',
            name='s2206_horcontratual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2206horario_s2206_horcontratual', to='s2206.s2206horContratual'),
        ),
        migrations.AlterField(
            model_name='s2206horcontratual',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206horcontratual',
            name='s2206_evtaltcontratual',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2206horcontratual_s2206_evtaltcontratual', to='esocial.s2206evtAltContratual'),
        ),
        migrations.AlterField(
            model_name='s2206horcontratual',
            name='tmpparc',
            field=models.IntegerField(choices=[(0, '0 - N\xe3o \xe9 contrato em tempo parcial'), (1, '1 - Limitado a 25 horas semanais'), (2, '2 - Limitado a 30 horas semanais'), (3, '3 - Limitado a 26 horas semanais')]),
        ),
        migrations.AlterField(
            model_name='s2206horcontratual',
            name='tpjornada',
            field=models.IntegerField(choices=[(1, '1 - Jornada com hor\xe1rio di\xe1rio e folga fixos'), (2, '2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)'), (3, '3 - Jornada com hor\xe1rio di\xe1rio fixo e folga vari\xe1vel'), (9, '9 - Demais tipos de jornada')]),
        ),
        migrations.AlterField(
            model_name='s2206infoceletista',
            name='cnpjsindcategprof',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s2206infoceletista',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206infoceletista',
            name='natatividade',
            field=models.IntegerField(choices=[(1, '1 - Trabalho Urbano'), (2, '2 - Trabalho Rural')]),
        ),
        migrations.AlterField(
            model_name='s2206infoceletista',
            name='s2206_evtaltcontratual',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2206infoceletista_s2206_evtaltcontratual', to='esocial.s2206evtAltContratual'),
        ),
        migrations.AlterField(
            model_name='s2206infoceletista',
            name='tpregjor',
            field=models.IntegerField(choices=[(1, '1 - Submetidos a Hor\xe1rio de Trabalho (Cap. II da CLT)'), (2, '2 - Atividade Externa especificada no Inciso I do Art. 62 da CLT'), (3, '3 - Fun\xe7\xf5es especificadas no Inciso II do Art. 62 da CLT'), (4, '4 - Teletrabalho, previsto no Inciso III do Art. 62 da CLT')]),
        ),
        migrations.AlterField(
            model_name='s2206infoestatutario',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206infoestatutario',
            name='s2206_evtaltcontratual',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2206infoestatutario_s2206_evtaltcontratual', to='esocial.s2206evtAltContratual'),
        ),
        migrations.AlterField(
            model_name='s2206infoestatutario',
            name='tpplanrp',
            field=models.IntegerField(choices=[(1, '1 - Plano previdenci\xe1rio ou \xfanico'), (2, '2 - Plano financeiro')]),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='cep',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='codmunic',
            field=models.TextField(max_length=7),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='dsclograd',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='nrlograd',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='s2206_evtaltcontratual',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2206localtrabdom_s2206_evtaltcontratual', to='esocial.s2206evtAltContratual'),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='tplograd',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s2206localtrabgeral',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206localtrabgeral',
            name='nrinsc',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='s2206localtrabgeral',
            name='s2206_evtaltcontratual',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2206localtrabgeral_s2206_evtaltcontratual', to='esocial.s2206evtAltContratual'),
        ),
        migrations.AlterField(
            model_name='s2206localtrabgeral',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
        ),
        migrations.AlterField(
            model_name='s2206observacoes',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206observacoes',
            name='observacao',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='s2206observacoes',
            name='s2206_evtaltcontratual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2206observacoes_s2206_evtaltcontratual', to='esocial.s2206evtAltContratual'),
        ),
        migrations.AlterField(
            model_name='s2206servpubl',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206servpubl',
            name='mtvalter',
            field=models.IntegerField(choices=[(1, '1 - Promo\xe7\xe3o'), (2, '2 - Readapta\xe7\xe3o'), (3, '3 - Aproveitamento'), (8, '8 - Outros'), (9, '9 - N\xe3o alterado')]),
        ),
        migrations.AlterField(
            model_name='s2206servpubl',
            name='s2206_evtaltcontratual',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2206servpubl_s2206_evtaltcontratual', to='esocial.s2206evtAltContratual'),
        ),
        migrations.AlterField(
            model_name='s2206trabtemp',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2206trabtemp',
            name='justprorr',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='s2206trabtemp',
            name='s2206_infoceletista',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2206trabtemp_s2206_infoceletista', to='s2206.s2206infoCeletista'),
        ),
    ]
