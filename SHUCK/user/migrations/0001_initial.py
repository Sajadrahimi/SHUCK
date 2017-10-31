# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 21:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_name', models.CharField(max_length=30)),
                ('shelf_books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.Book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('django_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('user_type', models.CharField(choices=[('SU', 'Super User'), ('U', 'User')], default='U', max_length=2)),
                ('shelves', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Shelf')),
            ],
        ),
    ]
