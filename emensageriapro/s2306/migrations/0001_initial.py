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
            name='s2306ageIntegracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjagntinteg', models.CharField(max_length=14)),
                ('nmrazao', models.CharField(max_length=100)),
                ('dsclograd', models.CharField(max_length=100)),
                ('nrlograd', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=90, null=True, blank=True)),
                ('cep', models.CharField(max_length=8)),
                ('codmunic', models.TextField(max_length=7, null=True, blank=True)),
                ('uf', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2306ageintegracao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2306ageintegracao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2306_infoestagiario', 'cnpjagntinteg', 'nmrazao', 'dsclograd', 'nrlograd', 'bairro', 'cep', 'codmunic', 'uf'],
                'db_table': 's2306_ageintegracao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2306cargoFuncao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codcargo', models.CharField(max_length=30)),
                ('codfuncao', models.CharField(max_length=30, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2306cargofuncao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2306cargofuncao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2306_infocomplementares', 'codcargo', 'codfuncao'],
                'db_table': 's2306_cargofuncao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2306infoComplementares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2306infocomplementares_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2306infocomplementares_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2306_evttsvaltcontr', models.OneToOneField(related_name='s2306infocomplementares_s2306_evttsvaltcontr', to='esocial.s2306evtTSVAltContr')),
            ],
            options={
                'ordering': ['s2306_evttsvaltcontr'],
                'db_table': 's2306_infocomplementares',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2306infoEstagiario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('natestagio', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o Obrigat\xf3rio'), (b'O', 'O - Obrigat\xf3rio')])),
                ('nivestagio', models.IntegerField(choices=[(1, '1 - Fundamental'), (2, '2 - M\xe9dio'), (3, '3 - Forma\xe7\xe3o Profissional'), (4, '4 - Superior'), (8, '8 - Especial'), (9, '9 - M\xe3e social (Lei 7644, de 1987)')])),
                ('areaatuacao', models.CharField(max_length=50, null=True, blank=True)),
                ('nrapol', models.CharField(max_length=30, null=True, blank=True)),
                ('vlrbolsa', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('dtprevterm', models.DateField()),
                ('cnpjinstensino', models.CharField(max_length=14, null=True, blank=True)),
                ('nmrazao', models.CharField(max_length=100)),
                ('dsclograd', models.CharField(max_length=100, null=True, blank=True)),
                ('nrlograd', models.CharField(max_length=10, null=True, blank=True)),
                ('bairro', models.CharField(max_length=90, null=True, blank=True)),
                ('cep', models.CharField(max_length=8, null=True, blank=True)),
                ('codmunic', models.TextField(max_length=7, null=True, blank=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2306infoestagiario_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2306infoestagiario_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2306_infocomplementares', models.OneToOneField(related_name='s2306infoestagiario_s2306_infocomplementares', to='s2306.s2306infoComplementares')),
            ],
            options={
                'ordering': ['s2306_infocomplementares', 'natestagio', 'nivestagio', 'areaatuacao', 'nrapol', 'vlrbolsa', 'dtprevterm', 'cnpjinstensino', 'nmrazao', 'dsclograd', 'nrlograd', 'bairro', 'cep', 'codmunic', 'uf'],
                'db_table': 's2306_infoestagiario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2306remuneracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vrsalfx', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('undsalfixo', models.IntegerField(choices=[(1, '1 - Por Hora'), (2, '2 - Por Dia'), (3, '3 - Por Semana'), (4, '4 - Por Quinzena'), (5, '5 - Por M\xeas'), (6, '6 - Por Tarefa'), (7, '7 - N\xe3o aplic\xe1vel - sal\xe1rio exclusivamente vari\xe1vel')])),
                ('dscsalvar', models.CharField(max_length=255, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2306remuneracao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2306remuneracao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2306_infocomplementares', models.OneToOneField(related_name='s2306remuneracao_s2306_infocomplementares', to='s2306.s2306infoComplementares')),
            ],
            options={
                'ordering': ['s2306_infocomplementares', 'vrsalfx', 'undsalfixo', 'dscsalvar'],
                'db_table': 's2306_remuneracao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2306supervisorEstagio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpfsupervisor', models.CharField(max_length=11)),
                ('nmsuperv', models.CharField(max_length=70)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2306supervisorestagio_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2306supervisorestagio_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2306_infoestagiario', models.OneToOneField(related_name='s2306supervisorestagio_s2306_infoestagiario', to='s2306.s2306infoEstagiario')),
            ],
            options={
                'ordering': ['s2306_infoestagiario', 'cpfsupervisor', 'nmsuperv'],
                'db_table': 's2306_supervisorestagio',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s2306cargofuncao',
            name='s2306_infocomplementares',
            field=models.OneToOneField(related_name='s2306cargofuncao_s2306_infocomplementares', to='s2306.s2306infoComplementares'),
        ),
        migrations.AddField(
            model_name='s2306ageintegracao',
            name='s2306_infoestagiario',
            field=models.OneToOneField(related_name='s2306ageintegracao_s2306_infoestagiario', to='s2306.s2306infoEstagiario'),
        ),
    ]
