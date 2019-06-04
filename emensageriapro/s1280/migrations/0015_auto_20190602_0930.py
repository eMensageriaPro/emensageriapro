# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1280', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1280infoativconcom',
            options={'managed': True, 'ordering': ['s1280_evtinfocomplper', 'fatormes', 'fator13'], 'permissions': (('can_see_list_s1280infoAtivConcom', 'Pode ver listagem do modelo S1280INFOATIVCONCOM'), ('can_see_data_s1280infoAtivConcom', 'Pode visualizar o conte\xfado do modelo S1280INFOATIVCONCOM'), ('can_see_menu_s1280infoAtivConcom', 'Pode visualizar no menu o modelo S1280INFOATIVCONCOM'), ('can_print_list_s1280infoAtivConcom', 'Pode imprimir listagem do modelo S1280INFOATIVCONCOM'), ('can_print_data_s1280infoAtivConcom', 'Pode imprimir o conte\xfado do modelo S1280INFOATIVCONCOM'))},
        ),
        migrations.AlterModelOptions(
            name='s1280infosubstpatr',
            options={'managed': True, 'ordering': ['s1280_evtinfocomplper', 'indsubstpatr', 'percredcontrib'], 'permissions': (('can_see_list_s1280infoSubstPatr', 'Pode ver listagem do modelo S1280INFOSUBSTPATR'), ('can_see_data_s1280infoSubstPatr', 'Pode visualizar o conte\xfado do modelo S1280INFOSUBSTPATR'), ('can_see_menu_s1280infoSubstPatr', 'Pode visualizar no menu o modelo S1280INFOSUBSTPATR'), ('can_print_list_s1280infoSubstPatr', 'Pode imprimir listagem do modelo S1280INFOSUBSTPATR'), ('can_print_data_s1280infoSubstPatr', 'Pode imprimir o conte\xfado do modelo S1280INFOSUBSTPATR'))},
        ),
        migrations.AlterModelOptions(
            name='s1280infosubstpatropport',
            options={'managed': True, 'ordering': ['s1280_evtinfocomplper', 'cnpjopportuario'], 'permissions': (('can_see_list_s1280infoSubstPatrOpPort', 'Pode ver listagem do modelo S1280INFOSUBSTPATROPPORT'), ('can_see_data_s1280infoSubstPatrOpPort', 'Pode visualizar o conte\xfado do modelo S1280INFOSUBSTPATROPPORT'), ('can_see_menu_s1280infoSubstPatrOpPort', 'Pode visualizar no menu o modelo S1280INFOSUBSTPATROPPORT'), ('can_print_list_s1280infoSubstPatrOpPort', 'Pode imprimir listagem do modelo S1280INFOSUBSTPATROPPORT'), ('can_print_data_s1280infoSubstPatrOpPort', 'Pode imprimir o conte\xfado do modelo S1280INFOSUBSTPATROPPORT'))},
        ),
    ]