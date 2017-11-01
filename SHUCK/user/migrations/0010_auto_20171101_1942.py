# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0005_auto_20171101_1536'),
        ('user', '0009_auto_20171101_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Reading',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reading', to='Book.Book'),
        ),
        migrations.AddField(
            model_name='user',
            name='toRead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toRead', to='Book.Book'),
        ),
    ]