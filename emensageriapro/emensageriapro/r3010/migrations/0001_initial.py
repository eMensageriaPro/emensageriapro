# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0001_initial'),
        ('efdreinf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='r3010boletim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nrboletim', models.CharField(max_length=4)),
                ('tpcompeticao', models.IntegerField(choices=[(1, '1 - Oficial'), (2, '2 - N\xe3o Oficial')])),
                ('categevento', models.IntegerField(choices=[(1, '1 - Internacional'), (2, '2 - Interestadual'), (3, '3 - Estadual'), (4, '4 - Local')])),
                ('moddesportiva', models.CharField(max_length=100)),
                ('nomecompeticao', models.CharField(max_length=100)),
                ('cnpjmandante', models.CharField(max_length=14)),
                ('cnpjvisitante', models.CharField(max_length=14, null=True, blank=True)),
                ('nomevisitante', models.CharField(max_length=80, null=True, blank=True)),
                ('pracadesportiva', models.CharField(max_length=100)),
                ('codmunic', models.TextField(max_length=7, null=True, blank=True)),
                ('uf', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('qtdepagantes', models.IntegerField()),
                ('qtdenaopagantes', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r3010boletim_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r3010boletim_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r3010_ideestab', 'nrboletim', 'tpcompeticao', 'categevento', 'moddesportiva', 'nomecompeticao', 'cnpjmandante', 'cnpjvisitante', 'nomevisitante', 'pracadesportiva', 'codmunic', 'uf', 'qtdepagantes', 'qtdenaopagantes'],
                'db_table': 'r3010_boletim',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r3010ideEstab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinscestab', models.IntegerField(choices=[(1, '1 - CNPJ')])),
                ('nrinscestab', models.CharField(max_length=14)),
                ('vlrreceitatotal', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcp', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcpsusptotal', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrreceitaclubes', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrretparc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r3010ideestab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r3010ideestab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r3010_evtespdesportivo', models.ForeignKey(related_name='r3010ideestab_r3010_evtespdesportivo', to='efdreinf.r3010evtEspDesportivo')),
            ],
            options={
                'ordering': ['r3010_evtespdesportivo', 'tpinscestab', 'nrinscestab', 'vlrreceitatotal', 'vlrcp', 'vlrcpsusptotal', 'vlrreceitaclubes', 'vlrretparc'],
                'db_table': 'r3010_ideestab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r3010infoProc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrproc', models.CharField(max_length=21)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('vlrcpsusp', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r3010infoproc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r3010infoproc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r3010_ideestab', models.ForeignKey(related_name='r3010infoproc_r3010_ideestab', to='r3010.r3010ideEstab')),
            ],
            options={
                'ordering': ['r3010_ideestab', 'tpproc', 'nrproc', 'codsusp', 'vlrcpsusp'],
                'db_table': 'r3010_infoproc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r3010outrasReceitas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpreceita', models.IntegerField(choices=[(1, '1 - Transmiss\xe3o'), (2, '2 - Propaganda'), (3, '3 - Publicidade'), (4, '4 - Sorteio'), (5, '5 - Outros')])),
                ('vlrreceita', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('descreceita', models.CharField(max_length=20)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r3010outrasreceitas_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r3010outrasreceitas_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r3010_boletim', models.ForeignKey(related_name='r3010outrasreceitas_r3010_boletim', to='r3010.r3010boletim')),
            ],
            options={
                'ordering': ['r3010_boletim', 'tpreceita', 'vlrreceita', 'descreceita'],
                'db_table': 'r3010_outrasreceitas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r3010receitaIngressos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpingresso', models.IntegerField(choices=[(1, '1 - Arquibancada'), (2, '2 - Geral'), (3, '3 - Cadeiras'), (4, '4 - Camarote')])),
                ('descingr', models.CharField(max_length=30)),
                ('qtdeingrvenda', models.IntegerField()),
                ('qtdeingrvendidos', models.IntegerField()),
                ('qtdeingrdev', models.IntegerField()),
                ('precoindiv', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrtotal', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r3010receitaingressos_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r3010receitaingressos_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r3010_boletim', models.ForeignKey(related_name='r3010receitaingressos_r3010_boletim', to='r3010.r3010boletim')),
            ],
            options={
                'ordering': ['r3010_boletim', 'tpingresso', 'descingr', 'qtdeingrvenda', 'qtdeingrvendidos', 'qtdeingrdev', 'precoindiv', 'vlrtotal'],
                'db_table': 'r3010_receitaingressos',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='r3010boletim',
            name='r3010_ideestab',
            field=models.ForeignKey(related_name='r3010boletim_r3010_ideestab', to='r3010.r3010ideEstab'),
        ),
    ]
