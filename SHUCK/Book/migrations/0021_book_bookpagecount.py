# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0020_auto_20171026_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='BookPageCount',
            field=models.IntegerField(null=True),
        ),
    ]
