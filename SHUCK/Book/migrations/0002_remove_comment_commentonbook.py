# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='CommentOnBook',
        ),
    ]