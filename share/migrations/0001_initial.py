# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-27 03:01
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
                ('file_name', models.CharField(max_length=20)),
                ('file_type', models.CharField(max_length=20)),
                ('file_size', models.IntegerField()),
                ('file_bedown', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='share/upload')),
                ('file_status', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': '文件',
                'verbose_name_plural': '文件',
            },
        ),
        migrations.CreateModel(
            name='FileClassify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
            options={
                'verbose_name': '文件类型',
                'verbose_name_plural': '文件类型',
            },
        ),
        migrations.AddField(
            model_name='file',
            name='file_classify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.FileClassify'),
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User'),
        ),
    ]
