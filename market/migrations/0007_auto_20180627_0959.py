# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-27 09:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20180627_0957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='creater',
            new_name='creator',
        ),
    ]