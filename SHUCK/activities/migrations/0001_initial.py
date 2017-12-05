# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('F', 'Favorite'), ('L', 'Like'), ('U', 'Up Vote'), ('D', 'Down Vote')], max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('feed', models.IntegerField(blank=True, null=True)),
                ('answer', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(choices=[('L', 'Liked'), ('C', 'Commented'), ('F', 'Favorited'), ('A', 'Answered'), ('W', 'Accepted Answer'), ('S', 'Also Commented')], max_length=1)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ('-date',),
            },
        ),
    ]
