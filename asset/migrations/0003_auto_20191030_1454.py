# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-30 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_serverasset_networkarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverasset',
            name='networkarea',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u533a\u57df'),
        ),
    ]
