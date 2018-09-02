# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0004_auto_20180829_0951'),
    ]

    operations = [
        migrations.RunSQL("""

INSERT INTO config_paginas ( titulo, endereco, exibe_menu, tipo, ordem, criado_em, modificado_em, excluido, config_modulos_id, criado_por_id, modificado_por_id) VALUES ('MapaProcessamento', 'mapa_processamento', 1, 1, 1, '2017-01-01 00:00:00-03', '2017-01-01 00:00:00-03', false, 3, 1, 1);
INSERT INTO config_paginas (titulo, endereco, exibe_menu, tipo, ordem, criado_em, modificado_em, excluido, config_modulos_id, criado_por_id, modificado_por_id) VALUES ('Importacoes', 'importacoes', 1, 1, 1, '2017-01-01 00:00:00-03', '2017-01-01 00:00:00-03', false, 3, 1, 1);        
        
        """)
    ]
