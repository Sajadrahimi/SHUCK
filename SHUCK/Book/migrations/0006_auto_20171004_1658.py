# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0005_auto_20171004_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='BookComments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.Comment'),
        ),
    ]
