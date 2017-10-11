# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(max_length=50)),
                ('BookDateOfPublish', models.DateField(blank=True, null=True)),
                ('BookImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('BookSummary', models.TextField(blank=True, max_length=1000)),
                ('BookRatesCount', models.IntegerField(blank=True, default=0)),
                ('BookRatesSum', models.IntegerField(blank=True, default=0)),
                ('BookCommentsCount', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PublisherName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(5, 'Excellent'), (4, 'Good'), (3, 'Not Bad'), (2, 'Bad'), (1, 'Awful')])),
            ],
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TranslatorName', models.CharField(max_length=50)),
                ('books', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Book.Book')),
            ],
        ),
    ]