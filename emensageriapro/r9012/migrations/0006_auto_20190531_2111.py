# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r9012', '0005_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r9012infototalcontrib',
            options={'managed': True, 'ordering': ['r9012_evtretcons', 'indexistinfo'], 'permissions': (('can_view_r9012infoTotalContrib', 'Can view R9012INFOTOTALCONTRIB'), ('can_view_menu_r9012infoTotalContrib', 'Can view menu R9012INFOTOTALCONTRIB'))},
        ),
        migrations.AlterModelOptions(
            name='r9012regocorrs',
            options={'managed': True, 'ordering': ['r9012_evtretcons', 'tpocorr', 'localerroaviso', 'codresp', 'dscresp'], 'permissions': (('can_view_r9012regOcorrs', 'Can view R9012REGOCORRS'), ('can_view_menu_r9012regOcorrs', 'Can view menu R9012REGOCORRS'))},
        ),
        migrations.AlterModelOptions(
            name='r9012totapurdec',
            options={'managed': True, 'ordering': ['r9012_infototalcontrib', 'perapurdec', 'crdec', 'vlrbasecrdec', 'vlrcrdec'], 'permissions': (('can_view_r9012totApurDec', 'Can view R9012TOTAPURDEC'), ('can_view_menu_r9012totApurDec', 'Can view menu R9012TOTAPURDEC'))},
        ),
        migrations.AlterModelOptions(
            name='r9012totapurdia',
            options={'managed': True, 'ordering': ['r9012_infototalcontrib', 'perapurdia', 'crdia', 'vlrbasecrdia', 'vlrcrdia'], 'permissions': (('can_view_r9012totApurDia', 'Can view R9012TOTAPURDIA'), ('can_view_menu_r9012totApurDia', 'Can view menu R9012TOTAPURDIA'))},
        ),
        migrations.AlterModelOptions(
            name='r9012totapurmen',
            options={'managed': True, 'ordering': ['r9012_infototalcontrib', 'crmen', 'vlrbasecrmen', 'vlrcrmen'], 'permissions': (('can_view_r9012totApurMen', 'Can view R9012TOTAPURMEN'), ('can_view_menu_r9012totApurMen', 'Can view menu R9012TOTAPURMEN'))},
        ),
        migrations.AlterModelOptions(
            name='r9012totapurqui',
            options={'managed': True, 'ordering': ['r9012_infototalcontrib', 'perapurqui', 'crqui', 'vlrbasecrqui', 'vlrcrqui'], 'permissions': (('can_view_r9012totApurQui', 'Can view R9012TOTAPURQUI'), ('can_view_menu_r9012totApurQui', 'Can view menu R9012TOTAPURQUI'))},
        ),
        migrations.AlterModelOptions(
            name='r9012totapursem',
            options={'managed': True, 'ordering': ['r9012_infototalcontrib', 'perapursem', 'crsem', 'vlrbasecrsem', 'vlrcrsem'], 'permissions': (('can_view_r9012totApurSem', 'Can view R9012TOTAPURSEM'), ('can_view_menu_r9012totApurSem', 'Can view menu R9012TOTAPURSEM'))},
        ),
    ]
