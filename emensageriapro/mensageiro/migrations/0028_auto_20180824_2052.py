# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0027_auto_20180824_2010'),
    ]

    operations = [
        migrations.RunSQL("""
        
DROP VIEW IF EXISTS transmissor_eventos_esocial;


DROP VIEW IF EXISTS  transmissor_eventos_efdreinf;
        
        """)
    ]
