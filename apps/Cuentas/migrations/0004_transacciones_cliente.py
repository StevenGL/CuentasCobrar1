# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 03:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0003_auto_20170713_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacciones',
            name='Cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cuentas.Clientes'),
            preserve_default=False,
        ),
    ]