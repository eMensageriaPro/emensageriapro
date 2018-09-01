# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1200', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1200infoperantideadc',
            name='tpacconv',
            field=models.CharField(max_length=1, choices=[(b'A', 'A - Acordo Coletivo de Trabalho'), (b'B', 'B - Legisla\xe7\xe3o federal, estadual, municipal ou distrital'), (b'C', 'C - Conven\xe7\xe3o Coletiva de Trabalho'), (b'D', 'D - Senten\xe7a Normativa - Diss\xeddio'), (b'E', 'E - Convers\xe3o de Licen\xe7a Sa\xfade em Acidente de Trabalho')]),
        ),
        migrations.AlterField(
            model_name='s1200infoperapurdetplano',
            name='tpdep',
            field=models.CharField(max_length=2, choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')]),
        ),
    ]
