# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0004_transacciones_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipos_documentos',
            name='Cuenta_Contable',
            field=models.PositiveIntegerField(),
        ),
    ]
