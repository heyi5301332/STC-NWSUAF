# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-22 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=20)),
                ('fileType', models.CharField(max_length=20)),
                ('fileStatus', models.CharField(max_length=20)),
                ('fileSize', models.IntegerField()),
                ('fileBeDown', models.IntegerField()),
                ('fileCreateTime', models.DateField()),
                ('fileClassify', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
        ),
    ]
