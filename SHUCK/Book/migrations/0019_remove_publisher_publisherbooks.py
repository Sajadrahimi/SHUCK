# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0018_auto_20171026_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='PublisherBooks',
        ),
    ]
