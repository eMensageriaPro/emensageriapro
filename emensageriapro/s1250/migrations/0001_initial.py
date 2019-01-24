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
            name='s1250ideProdutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinscprod', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinscprod', models.CharField(max_length=14)),
                ('vlrbruto', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcpdescpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrratdescpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsenardesc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1250ideprodutor_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1250ideprodutor_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1250_tpaquis', 'tpinscprod', 'nrinscprod', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc'],
                'db_table': 's1250_ideprodutor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1250infoProcJud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nrprocjud', models.CharField(max_length=20)),
                ('codsusp', models.IntegerField()),
                ('vrcpnret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrratnret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsenarnret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1250infoprocjud_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1250infoprocjud_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1250_ideprodutor', models.ForeignKey(related_name='s1250infoprocjud_s1250_ideprodutor', to='s1250.s1250ideProdutor')),
            ],
            options={
                'ordering': ['s1250_ideprodutor', 'nrprocjud', 'codsusp', 'vrcpnret', 'vrratnret', 'vrsenarnret'],
                'db_table': 's1250_infoprocjud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1250nfs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.CharField(max_length=5, null=True, blank=True)),
                ('nrdocto', models.CharField(max_length=20)),
                ('dtemisnf', models.DateField()),
                ('vlrbruto', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcpdescpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrratdescpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsenardesc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1250nfs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1250nfs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1250_ideprodutor', models.ForeignKey(related_name='s1250nfs_s1250_ideprodutor', to='s1250.s1250ideProdutor')),
            ],
            options={
                'ordering': ['s1250_ideprodutor', 'serie', 'nrdocto', 'dtemisnf', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc'],
                'db_table': 's1250_nfs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1250tpAquis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indaquis', models.IntegerField(choices=[(1, '1 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral'), (2, '2 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA'), (3, '3 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA. Evento de origem (S- 1250)'), (4, '4 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (5, '5 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (6, '6 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018)')])),
                ('vlrtotaquis', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1250tpaquis_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1250tpaquis_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1250_evtaqprod', models.ForeignKey(related_name='s1250tpaquis_s1250_evtaqprod', to='esocial.s1250evtAqProd')),
            ],
            options={
                'ordering': ['s1250_evtaqprod', 'indaquis', 'vlrtotaquis'],
                'db_table': 's1250_tpaquis',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s1250ideprodutor',
            name='s1250_tpaquis',
            field=models.ForeignKey(related_name='s1250ideprodutor_s1250_tpaquis', to='s1250.s1250tpAquis'),
        ),
    ]
