# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 14:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='UsersReadThisBook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UsersReadThisBook', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='UsersReadingThisBook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UsersReadingThinBook', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='UsersWantsToReadThisBook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UsersWantToReadThisBook', to=settings.AUTH_USER_MODEL),
        ),
    ]