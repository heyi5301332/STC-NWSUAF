# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-03 15:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
        ('market', '0003_auto_20180703_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('mark_type', models.IntegerField(choices=[(0, '好评'), (1, '差评')])),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Order')),
            ],
            options={
                'verbose_name_plural': '商品评论',
                'verbose_name': '商品评论',
                'ordering': ['create_time'],
            },
        ),
    ]