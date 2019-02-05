# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0010_auto_20190202_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r1000evtinfocontri',
            options={'managed': True, 'ordering': ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc'], 'permissions': (('can_view_r1000_evtinfocontri', 'Can view r1000_evtinfocontri'),)},
        ),
        migrations.AlterModelOptions(
            name='r1070evttabprocesso',
            options={'managed': True, 'ordering': ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc'], 'permissions': (('can_view_r1070_evttabprocesso', 'Can view r1070_evttabprocesso'),)},
        ),
        migrations.AlterModelOptions(
            name='r2010evtservtom',
            options={'managed': True, 'ordering': ['identidade', 'indretif', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab', 'indobra', 'cnpjprestador', 'vlrtotalbruto', 'vlrtotalbaseret', 'vlrtotalretprinc', 'indcprb'], 'permissions': (('can_view_r2010_evtservtom', 'Can view r2010_evtservtom'),)},
        ),
        migrations.AlterModelOptions(
            name='r2020evtservprest',
            options={'managed': True, 'ordering': ['identidade', 'indretif', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestabprest', 'nrinscestabprest', 'tpinsctomador', 'nrinsctomador', 'indobra', 'vlrtotalbruto', 'vlrtotalbaseret', 'vlrtotalretprinc'], 'permissions': (('can_view_r2020_evtservprest', 'Can view r2020_evtservprest'),)},
        ),
        migrations.AlterModelOptions(
            name='r2030evtassocdesprec',
            options={'managed': True, 'ordering': ['identidade', 'indretif', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab'], 'permissions': (('can_view_r2030_evtassocdesprec', 'Can view r2030_evtassocdesprec'),)},
        ),
        migrations.AlterModelOptions(
            name='r2040evtassocdesprep',
            options={'managed': True, 'ordering': ['identidade', 'indretif', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab'], 'permissions': (('can_view_r2040_evtassocdesprep', 'Can view r2040_evtassocdesprep'),)},
        ),
        migrations.AlterModelOptions(
            name='r2050evtcomprod',
            options={'managed': True, 'ordering': ['identidade', 'indretif', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab', 'vlrrecbrutatotal', 'vlrcpapur', 'vlrratapur', 'vlrsenarapur'], 'permissions': (('can_view_r2050_evtcomprod', 'Can view r2050_evtcomprod'),)},
        ),
        migrations.AlterModelOptions(
            name='r2060evtcprb',
            options={'managed': True, 'ordering': ['identidade', 'indretif', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab', 'vlrrecbrutatotal', 'vlrcpapurtotal'], 'permissions': (('can_view_r2060_evtcprb', 'Can view r2060_evtcprb'),)},
        ),
        migrations.AlterModelOptions(
            name='r2070evtpgtosdivs',
            options={'managed': True, 'ordering': ['identidade', 'indretif', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'codpgto', 'nmrazaobenef'], 'permissions': (('can_view_r2070_evtpgtosdivs', 'Can view r2070_evtpgtosdivs'),)},
        ),
        migrations.AlterModelOptions(
            name='r2098evtreabreevper',
            options={'managed': True, 'ordering': ['identidade', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc'], 'permissions': (('can_view_r2098_evtreabreevper', 'Can view r2098_evtreabreevper'),)},
        ),
        migrations.AlterModelOptions(
            name='r2099evtfechaevper',
            options={'managed': True, 'ordering': ['identidade', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'evtservtm', 'evtservpr', 'evtassdesprec', 'evtassdesprep', 'evtcomprod', 'evtcprb'], 'permissions': (('can_view_r2099_evtfechaevper', 'Can view r2099_evtfechaevper'),)},
        ),
        migrations.AlterModelOptions(
            name='r3010evtespdesportivo',
            options={'managed': True, 'ordering': ['identidade', 'indretif', 'dtapuracao', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab', 'vlrreceitatotal', 'vlrcp', 'vlrreceitaclubes', 'vlrretparc'], 'permissions': (('can_view_r3010_evtespdesportivo', 'Can view r3010_evtespdesportivo'),)},
        ),
        migrations.AlterModelOptions(
            name='r5001evttotal',
            options={'managed': True, 'ordering': ['identidade', 'perapur', 'tpinsc', 'nrinsc', 'cdretorno', 'descretorno', 'dhprocess', 'tpev', 'idev', 'hash'], 'permissions': (('can_view_r5001_evttotal', 'Can view r5001_evttotal'),)},
        ),
        migrations.AlterModelOptions(
            name='r5011evttotalcontrib',
            options={'managed': True, 'ordering': ['identidade', 'perapur', 'tpinsc', 'nrinsc', 'cdretorno', 'descretorno', 'nrprotentr', 'dhprocess', 'tpev', 'idev', 'hash'], 'permissions': (('can_view_r5011_evttotalcontrib', 'Can view r5011_evttotalcontrib'),)},
        ),
        migrations.AlterModelOptions(
            name='r9000evtexclusao',
            options={'managed': True, 'ordering': ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpevento', 'nrrecevt', 'perapur'], 'permissions': (('can_view_r9000_evtexclusao', 'Can view r9000_evtexclusao'),)},
        ),
    ]
