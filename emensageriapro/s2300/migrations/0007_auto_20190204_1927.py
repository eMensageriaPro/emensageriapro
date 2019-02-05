# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2300', '0006_auto_20190202_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2300afastamento',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'dtiniafast', 'codmotafast'], 'permissions': (('can_view_s2300_afastamento', 'Can view s2300_afastamento'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300ageintegracao',
            options={'managed': True, 'ordering': ['s2300_infoestagiario', 'cnpjagntinteg', 'nmrazao', 'dsclograd', 'nrlograd', 'cep', 'uf'], 'permissions': (('can_view_s2300_ageintegracao', 'Can view s2300_ageintegracao'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300brasil',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf'], 'permissions': (('can_view_s2300_brasil', 'Can view s2300_brasil'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300cargofuncao',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'codcargo'], 'permissions': (('can_view_s2300_cargofuncao', 'Can view s2300_cargofuncao'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300cnh',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrregcnh', 'ufcnh', 'dtvalid', 'categoriacnh'], 'permissions': (('can_view_s2300_cnh', 'Can view s2300_cnh'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300contato',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio'], 'permissions': (('can_view_s2300_contato', 'Can view s2300_contato'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300ctps',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrctps', 'seriectps', 'ufctps'], 'permissions': (('can_view_s2300_ctps', 'Can view s2300_ctps'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300dependente',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'tpdep', 'nmdep', 'dtnascto', 'depirrf', 'depsf', 'inctrab'], 'permissions': (('can_view_s2300_dependente', 'Can view s2300_dependente'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300exterior',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'paisresid', 'dsclograd', 'nrlograd', 'nmcid'], 'permissions': (('can_view_s2300_exterior', 'Can view s2300_exterior'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300fgts',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'opcfgts'], 'permissions': (('can_view_s2300_fgts', 'Can view s2300_fgts'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300infodeficiencia',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'deffisica', 'defvisual', 'defauditiva', 'defmental', 'defintelectual', 'reabreadap'], 'permissions': (('can_view_s2300_infodeficiencia', 'Can view s2300_infodeficiencia'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300infodirigentesindical',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'categorig'], 'permissions': (('can_view_s2300_infodirigentesindical', 'Can view s2300_infodirigentesindical'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300infoestagiario',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'natestagio', 'nivestagio', 'dtprevterm', 'nmrazao'], 'permissions': (('can_view_s2300_infoestagiario', 'Can view s2300_infoestagiario'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300infotrabcedido',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'categorig', 'cnpjcednt', 'matricced', 'dtadmced', 'tpregtrab', 'tpregprev', 'infonus'], 'permissions': (('can_view_s2300_infotrabcedido', 'Can view s2300_infotrabcedido'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300mudancacpf',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'cpfant', 'dtaltcpf'], 'permissions': (('can_view_s2300_mudancacpf', 'Can view s2300_mudancacpf'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300oc',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nroc', 'orgaoemissor'], 'permissions': (('can_view_s2300_oc', 'Can view s2300_oc'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300remuneracao',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'vrsalfx', 'undsalfixo'], 'permissions': (('can_view_s2300_remuneracao', 'Can view s2300_remuneracao'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300rg',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrrg', 'orgaoemissor'], 'permissions': (('can_view_s2300_rg', 'Can view s2300_rg'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300ric',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrric', 'orgaoemissor'], 'permissions': (('can_view_s2300_ric', 'Can view s2300_ric'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300rne',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrrne', 'orgaoemissor'], 'permissions': (('can_view_s2300_rne', 'Can view s2300_rne'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300supervisorestagio',
            options={'managed': True, 'ordering': ['s2300_infoestagiario', 'cpfsupervisor', 'nmsuperv'], 'permissions': (('can_view_s2300_supervisorestagio', 'Can view s2300_supervisorestagio'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300termino',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'dtterm'], 'permissions': (('can_view_s2300_termino', 'Can view s2300_termino'),)},
        ),
        migrations.AlterModelOptions(
            name='s2300trabestrangeiro',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'classtrabestrang', 'casadobr', 'filhosbr'], 'permissions': (('can_view_s2300_trabestrangeiro', 'Can view s2300_trabestrangeiro'),)},
        ),
    ]
