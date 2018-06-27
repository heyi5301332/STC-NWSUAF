# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-26 10:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('profile_photo', models.ImageField(blank=True, default='', upload_to='static/upload/profile_photo')),
                ('alipay', models.ImageField(blank=True, default='', upload_to='static/upload/alipay')),
                ('wechatpay', models.ImageField(blank=True, default='', upload_to='static/upload/wechatpay')),
                ('good_mark', models.IntegerField(default=0)),
                ('bad_mark', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
    ]