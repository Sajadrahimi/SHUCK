# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20171101_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Read',
            new_name='Reads',
        ),
    ]