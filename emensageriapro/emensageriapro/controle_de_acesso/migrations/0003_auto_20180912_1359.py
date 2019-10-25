# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0002_auto_20180904_2050'),
    ]

    operations = [
        migrations.RunSQL("""
        

INSERT INTO auth_user (id, password, last_login, is_superuser, 
username, first_name, last_name, email, is_staff, is_active, date_joined) 
VALUES (1, 'pbkdf2_sha256$20000$KzjN6s7JgWzT$N212Wj4ATRC0TzfS0dtq0C6Z3ZrW4gzOeA9xqi3+dCM=', 
now(), true, 'admin', 'admin', 'admin', 'contato@emensageria.com.br', 
true, true, now());

	     
        """),
        migrations.AlterModelOptions(
            name='usuarios',
            options={'ordering': ['first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'date_joined'], 'managed': True},
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='senha',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='usuario',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='date_joined',
            field=models.DateField(default='2018-09-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='first_name',
            field=models.CharField(default='admin', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='is_staff',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='is_superuser',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='last_login',
            field=models.DateTimeField(default='2018-09-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='last_name',
            field=models.CharField(default='aaa', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='password',
            field=models.CharField(default=b'asdkl1231', max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='username',
            field=models.CharField(default='admin', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(max_length=60),
        ),
    ]
