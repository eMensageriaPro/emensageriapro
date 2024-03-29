# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2030', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2030infoproc',
            options={'managed': True, 'ordering': ['r2030_recursosrec', 'tpproc', 'nrproc', 'vlrnret'], 'permissions': (('can_see_list_r2030infoProc', 'Pode ver listagem do modelo R2030INFOPROC'), ('can_see_data_r2030infoProc', 'Pode visualizar o conte\xfado do modelo R2030INFOPROC'), ('can_see_menu_r2030infoProc', 'Pode visualizar no menu o modelo R2030INFOPROC'), ('can_print_list_r2030infoProc', 'Pode imprimir listagem do modelo R2030INFOPROC'), ('can_print_data_r2030infoProc', 'Pode imprimir o conte\xfado do modelo R2030INFOPROC'))},
        ),
        migrations.AlterModelOptions(
            name='r2030inforecurso',
            options={'managed': True, 'ordering': ['r2030_recursosrec', 'tprepasse', 'descrecurso', 'vlrbruto', 'vlrretapur'], 'permissions': (('can_see_list_r2030infoRecurso', 'Pode ver listagem do modelo R2030INFORECURSO'), ('can_see_data_r2030infoRecurso', 'Pode visualizar o conte\xfado do modelo R2030INFORECURSO'), ('can_see_menu_r2030infoRecurso', 'Pode visualizar no menu o modelo R2030INFORECURSO'), ('can_print_list_r2030infoRecurso', 'Pode imprimir listagem do modelo R2030INFORECURSO'), ('can_print_data_r2030infoRecurso', 'Pode imprimir o conte\xfado do modelo R2030INFORECURSO'))},
        ),
        migrations.AlterModelOptions(
            name='r2030recursosrec',
            options={'managed': True, 'ordering': ['r2030_evtassocdesprec', 'cnpjorigrecurso', 'vlrtotalrec', 'vlrtotalret'], 'permissions': (('can_see_list_r2030recursosRec', 'Pode ver listagem do modelo R2030RECURSOSREC'), ('can_see_data_r2030recursosRec', 'Pode visualizar o conte\xfado do modelo R2030RECURSOSREC'), ('can_see_menu_r2030recursosRec', 'Pode visualizar no menu o modelo R2030RECURSOSREC'), ('can_print_list_r2030recursosRec', 'Pode imprimir listagem do modelo R2030RECURSOSREC'), ('can_print_data_r2030recursosRec', 'Pode imprimir o conte\xfado do modelo R2030RECURSOSREC'))},
        ),
    ]
