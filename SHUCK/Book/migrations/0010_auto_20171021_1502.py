# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0009_remove_book_bookpublisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='PublisherBooks',
        ),
        migrations.AddField(
            model_name='book',
            name='BookPublisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.Publisher'),
        ),
    ]