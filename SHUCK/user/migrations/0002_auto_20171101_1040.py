# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Read',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Read', to='Book.Book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Reading',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reading', to='Book.Book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='toRead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toRead', to='Book.Book'),
        ),
    ]
