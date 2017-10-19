# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_auto_20171019_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='BookAuthor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='BookPublisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.Publisher'),
        ),
    ]