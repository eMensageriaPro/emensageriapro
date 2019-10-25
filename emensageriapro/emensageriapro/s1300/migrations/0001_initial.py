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
            name='s1300contribSind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjsindic', models.CharField(max_length=14)),
                ('tpcontribsind', models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Sindical Compuls\xf3ria'), (2, '2 - Contribui\xe7\xe3o Associativa'), (3, '3 - Contribui\xe7\xe3o Assistencial'), (4, '4 - Contribui\xe7\xe3o Confederativa')])),
                ('vlrcontribsind', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1300contribsind_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1300contribsind_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1300_evtcontrsindpatr', models.ForeignKey(related_name='s1300contribsind_s1300_evtcontrsindpatr', to='esocial.s1300evtContrSindPatr')),
            ],
            options={
                'ordering': ['s1300_evtcontrsindpatr', 'cnpjsindic', 'tpcontribsind', 'vlrcontribsind'],
                'db_table': 's1300_contribsind',
                'managed': True,
            },
        ),
    ]
